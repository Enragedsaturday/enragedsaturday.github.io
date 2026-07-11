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

## GROUP: _overhaul2/lake/cases/Ohio v. Robinette.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Ohio v. Robinette"
type: case
citation: "519 U.S. 33 (1996)"
parallel_cite: "117 S. Ct. 417; 136 L. Ed. 2d 347"
neutral_cite: 1996 U.S. LEXIS 6971
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1996
date_decided: 1996-11-18
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1996-11-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Ohio v. Robinette
  varies_by_point: false
  scope_note: "No 'free to go' advisory required for voluntary consent; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118066/ohio-v-robinette/"
  cluster_id: 118066
  opinion_id: 118066
  identity_checked: true
homes:
  - page: "[[Consent Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Schneckloth v. Bustamonte]]", "[[Florida v. Bostick]]"]
aliases: []
tags: ["case", "fourth-amendment", "consent-search", "voluntariness", "traffic-stop"]
holding: "No-warning rule: officers need not tell a lawfully stopped motorist he is 'free to go' for his subsequent consent to search to be voluntary."
lake:
  record_id: Ohio v. Robinette
  status: verified
  projected_at: 2026-07-06
---

# Ohio v. Robinette

*519 U.S. 33 (1996)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A deputy stopped Robinette for speeding, ran his license, returned it, and told him he was getting a warning. The deputy then asked whether Robinette was carrying any contraband and for consent to search his car. Robinette consented, and the deputy found drugs. The Ohio Supreme Court held the consent invalid because the deputy had not first told Robinette he was free to go.

## Issue
Whether the Fourth Amendment requires officers to tell a lawfully detained motorist that he is "free to go" before a consent to search obtained during the encounter can be voluntary.

## Rule
No. Just as the Court has not required a detailed warning before an ordinary consent search, "so too would it be unrealistic to require police officers to always inform detainees that they are free to go before a consent to search may be deemed voluntary." — 519 U.S. at 39–40. ^pin-39

"The Fourth Amendment test for a valid consent to search is that the consent be voluntary, and '[v]oluntariness is a question of fact to be determined from all the circumstances.'" — *Id.* at 40. ^pin-40

## Application
The absence of a "free to go" advisory did not by itself render Robinette's consent involuntary; whether his consent was voluntary had to be determined from all the circumstances of the encounter. The Court rejected the Ohio Supreme Court's [[Common Legal Terms#per-se|per se]] rule and [[Reading and Citing Cases#on-remand|remanded]] for application of the totality-of-the-circumstances standard.

## Conclusion
No "free to go" warning is constitutionally required; the [[Common Legal Terms#per-se|per se]] rule was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Robinette* applies the totality-of-the-circumstances voluntariness standard of [[Schneckloth v. Bustamonte]] and parallels [[Florida v. Bostick]]'s rejection of bright-line advisory requirements.

## Appears on
- [[Consent Searches]] — *Key — Progeny / Refinement*

## Sources
- *Ohio v. Robinette*, 519 U.S. 33 (1996) — https://www.courtlistener.com/opinion/118066/ohio-v-robinette/ — pinpoints: 39–40, 40.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f5502b35a49379b0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Ohio v. Robinette"}, "payload": {"all": [{"cite": "519 U.S. 33", "page": "33", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "519"}, {"cite": "117 S. Ct. 417", "page": "417", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "117"}, {"cite": "136 L. Ed. 2d 347", "page": "347", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "136"}, {"cite": "1996 U.S. LEXIS 6971", "page": "6971", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1996"}], "display": "519 U.S. 33", "official": {"cite": "519 U.S. 33", "page": "33", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "519"}, "official_selection_present": true, "record_id": "Ohio v. Robinette"}}
{"assertion_id": "02e6cb4ab7dbb6ef", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-39", "record_id": "Ohio v. Robinette"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-39", "pinpoint_status": "slip-only", "quote": "before a consent to search obtained during the encounter can be voluntary. ## Rule No. Just as the Court has not required a detailed warning before an ordinary consent search,", "quote_fidelity": "mismatch", "record_id": "Ohio v. Robinette", "star_marker": null}}
{"assertion_id": "e91cb8fa7e3d80de", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-40", "record_id": "Ohio v. Robinette"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-40", "pinpoint_status": "slip-only", "quote": "The Fourth Amendment test for a valid consent to search is that the consent be voluntary, and '[v]oluntariness is a question of fact to be determined from all the circumstances.'", "quote_fidelity": "mismatch", "record_id": "Ohio v. Robinette", "star_marker": null}}
{"assertion_id": "0218e380dae0ed5b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Ohio v. Robinette"}, "payload": {"as_of_content": "1996-11-18", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Ohio v. Robinette", "scope_note": "No 'free to go' advisory required for voluntary consent; good law.", "varies_by_point": false}}
```

### lake record — Ohio v. Robinette

```json
{
  "schema_version": "s2.v1",
  "record_id": "Ohio v. Robinette",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Ohio v. Robinette",
    "case_name_short": "Robinette",
    "case_name_full": "Ohio v. Robinette",
    "input_case_name": "Ohio v. Robinette",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1996-11-18",
    "year": 1996,
    "docket": null,
    "cluster_id": 118066,
    "lead_opinion_id": 118066,
    "sibling_ids": [
      118066,
      9433390,
      9433391,
      9433392
    ],
    "absolute_url": "/opinion/118066/ohio-v-robinette/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9161388,
        "score": 20,
        "case_name": "Ohio v. Robinette"
      },
      {
        "cluster_id": 9161387,
        "score": 20,
        "case_name": "Ohio v. Robinette"
      },
      {
        "cluster_id": 9159470,
        "score": 20,
        "case_name": "Ohio v. Robinette"
      },
      {
        "cluster_id": 9159469,
        "score": 20,
        "case_name": "Ohio v. Robinette"
      },
      {
        "cluster_id": 9274301,
        "score": 20,
        "case_name": "Ohio v. Robinette"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "519 U.S. 33",
      "volume": "519",
      "reporter": "U.S.",
      "page": "33",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "117 S. Ct. 417",
        "volume": "117",
        "reporter": "S. Ct.",
        "page": "417",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "136 L. Ed. 2d 347",
        "volume": "136",
        "reporter": "L. Ed. 2d",
        "page": "347",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1996 U.S. LEXIS 6971",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "6971",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "519 U.S. 33",
        "volume": "519",
        "reporter": "U.S.",
        "page": "33",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "117 S. Ct. 417",
        "volume": "117",
        "reporter": "S. Ct.",
        "page": "417",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "136 L. Ed. 2d 347",
        "volume": "136",
        "reporter": "L. Ed. 2d",
        "page": "347",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1996 U.S. LEXIS 6971",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "6971",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "519 U.S. 33",
    "official_selection": {
      "court_class": "scotus",
      "selected": "519 U.S. 33",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-39",
      "page": null,
      "quote": "before a consent to search obtained during the encounter can be voluntary. ## Rule No. Just as the Court has not required a detailed warning before an ordinary consent search,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-40",
      "page": null,
      "quote": "The Fourth Amendment test for a valid consent to search is that the consent be voluntary, and '[v]oluntariness is a question of fact to be determined from all the circumstances.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1996-11-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Ohio v. Robinette",
    "varies_by_point": false,
    "scope_note": "No 'free to go' advisory required for voluntary consent; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Marlon Juan Lall v. the State of Texas",
          "cluster_id": 10046849,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Privette",
          "cluster_id": 9387170,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Villagran",
          "cluster_id": 4422358,
          "cite": [
            "477 Mass. 711",
            "81 N.E.3d 310"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Connor William Clar Steffens",
          "cluster_id": 4332280,
          "cite": [
            "889 N.W.2d 691",
            "2016 Iowa App. LEXIS 1316",
            "2016 WL 7393893"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dickson",
          "cluster_id": 4244499,
          "cite": [
            "141 A.3d 810",
            "322 Conn. 410",
            "2016 Conn. LEXIS 236"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane1_negative"
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
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Layne",
          "cluster_id": 118289,
          "cite": [
            "143 L. Ed. 2d 818",
            "119 S. Ct. 1692",
            "526 U.S. 603",
            "1999 U.S. LEXIS 3633"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baldwin v. Reese",
          "cluster_id": 134723,
          "cite": [
            "158 L. Ed. 2d 64",
            "124 S. Ct. 1347",
            "541 U.S. 27",
            "2004 U.S. LEXIS 1835"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
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
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
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
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
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
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Knights",
          "cluster_id": 118468,
          "cite": [
            "151 L. Ed. 2d 497",
            "122 S. Ct. 587",
            "534 U.S. 112",
            "2001 U.S. LEXIS 10950"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
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
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Genesis HealthCare Corp. v. Symczyk",
          "cluster_id": 858086,
          "cite": [
            "185 L. Ed. 2d 636",
            "133 S. Ct. 1523",
            "569 U.S. 66",
            "2013 U.S. LEXIS 3157",
            "24 Fla. L. Weekly Fed. S 133",
            "81 U.S.L.W. 4229",
            "20 Wage & Hour Cas.2d (BNA) 801",
            "2013 WL 1567370"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. State",
          "cluster_id": 2419717,
          "cite": [
            "947 S.W.2d 240",
            "1997 Tex. Crim. App. LEXIS 43",
            "1997 WL 292676"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
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
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Drayton",
          "cluster_id": 121153,
          "cite": [
            "153 L. Ed. 2d 242",
            "122 S. Ct. 2105",
            "536 U.S. 194",
            "2002 U.S. LEXIS 4420"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. United States",
          "cluster_id": 118309,
          "cite": [
            "144 L. Ed. 2d 370",
            "119 S. Ct. 2090",
            "527 U.S. 373",
            "1999 U.S. LEXIS 4201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kothe v. State",
          "cluster_id": 1504839,
          "cite": [
            "152 S.W.3d 54",
            "2004 Tex. Crim. App. LEXIS 1749",
            "2004 WL 2347781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Yeargan",
          "cluster_id": 1060948,
          "cite": [
            "958 S.W.2d 626",
            "1997 Tenn. LEXIS 574",
            "1997 WL 724993"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
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
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maxwell v. State",
          "cluster_id": 2105782,
          "cite": [
            "73 S.W.3d 278",
            "2002 Tex. Crim. App. LEXIS 84",
            "2002 WL 562264"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thornton v. United States",
          "cluster_id": 134746,
          "cite": [
            "158 L. Ed. 2d 905",
            "124 S. Ct. 2127",
            "541 U.S. 615",
            "2004 U.S. LEXIS 3681"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
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
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gutierrez v. State",
          "cluster_id": 1508583,
          "cite": [
            "221 S.W.3d 680",
            "2007 Tex. Crim. App. LEXIS 500",
            "2007 WL 1217343"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Granite Rock Co. v. International Brotherhood of Teamsters",
          "cluster_id": 149288,
          "cite": [
            "177 L. Ed. 2d 567",
            "130 S. Ct. 2847",
            "561 U.S. 287",
            "2010 U.S. LEXIS 5255",
            "22 Fla. L. Weekly Fed. S 593",
            "78 U.S.L.W. 4712",
            "188 L.R.R.M. (BNA) 2897"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
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
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Grubbs",
          "cluster_id": 145670,
          "cite": [
            "164 L. Ed. 2d 195",
            "126 S. Ct. 1494",
            "547 U.S. 90",
            "2006 U.S. LEXIS 2496"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Strickler",
          "cluster_id": 2156861,
          "cite": [
            "757 A.2d 884",
            "563 Pa. 47",
            "2000 Pa. LEXIS 2114"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark A. Lee v. City of Chicago",
          "cluster_id": 782110,
          "cite": [
            "330 F.3d 456",
            "2003 U.S. App. LEXIS 10254",
            "2003 WL 21196550"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ohio v. Robinette:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118066 OR 9433390 OR 9433391 OR 9433392) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDY0NjUyODAwMDAwJnM9MzIwODE1MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118066+OR+9433390+OR+9433391+OR+9433392%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 5,
        "triage_snippet_classified": 195
      },
      "lane2_top_cited": {
        "query": "cites:(118066 OR 9433390 OR 9433391 OR 9433392)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNTImcz00NDcyMzkyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28118066+OR+9433390+OR+9433391+OR+9433392%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118066 OR 9433390 OR 9433391 OR 9433392)",
        "reviewed": 45,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 45,
        "triage_read": 1,
        "triage_snippet_classified": 44
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118066 OR 9433390 OR 9433391 OR 9433392)",
    "indexed_citing_opinions": 1352,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118066,
        "count": 1211,
        "count_source": "search"
      },
      {
        "opinion_id": 9433390,
        "count": 175,
        "count_source": "search"
      },
      {
        "opinion_id": 9433391,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433392,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2025,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/ohio-v-robinette.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4NTE5OTkmcz05NTY3NjgzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118066+OR+9433390+OR+9433391+OR+9433392%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118066,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 109424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 109611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 109730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 110168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 110380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 110636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 111093,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 111221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 111378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 112595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 112631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 117905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118066,
        "cited_id": 3755951,
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
    "date_created": "2026-07-05T16:05:25Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:05:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:05:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:08:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:05:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Ohio v. Robinette

```
<div>
<center><b><span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/" aria-description="Citation for case: Ohio v. Robinette">519 U.S. 33</a></span> (1996)</b></center>
<center><h1>OHIO<br>
v.<br>
ROBINETTE</h1></center>
<center>No. 95-891.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued October 8, 1996.</center>
<center>Decided November 18, 1996.</center>
CERTIORARI TO THE SUPREME COURT OF OHIO
<p><span class="star-pagination">*35</span> Rehnquist, C. J., delivered the opinion of the Court, in which O'Connor, Scalia, Kennedy, Souter, Thomas, and Breyer, JJ., joined. Ginsburg, J.,filed an opinion concurring in the judgment, <i>post,</i> p. 40. Stevens, J., filed a dissenting opinion, <i>post,</i> p. 45.</p>
<p><i>Carley J. Ingram</i> argued the cause for petitioner. With her on the briefs was <i>Mathias H. Heck, Jr.</i> </p>
<p><i>Irving L. Gornstein</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. On the brief were <i>Solicitor General Days, Acting Assistant Attorney General Keeney, Deputy Solicitor General Dreeben, Paul A. Engelmayer,</i> and <i>Joseph C. Wyderko.</i> </p>
<p><i>James D. Ruppert</i> argued the cause and filed a brief for respondent.<sup>[*]</sup></p>
<p><span class="star-pagination">*35</span> Chief Justice Rehnquist delivered the opinion of the Court.</p>
<p>We are here presented with the question whether the Fourth Amendment requires that a lawfully seized defendant must be advised that he is "free to go" before his consent to search will be recognized as voluntary. We hold that it does not.</p>
<p>This case arose on a stretch of Interstate 70 north of Dayton, Ohio, where the posted speed limit was 45 miles per hour because of construction. Respondent Robert D. Robinette was clocked at 69 miles per hour as he drove his car along this stretch of road, and was stopped by Deputy Roger Newsome of the Montgomery County Sheriff's Office. Newsome asked for and was handed Robinette's driver's license, and he ran a computer check which indicated that Robinette had no previous violations. Newsome then asked Robinette to step out of his car, turned on his mounted video camera, issued a verbal warning to Robinette, and returned his license.</p>
<p>At this point, Newsome asked, "One question before you get gone: [A]re you carrying any illegal contraband in your <span class="star-pagination">*36</span> car? Any weapons of any kind, drugs, anything like that?" App. to Brief for Respondent 2 (internal quotation marks omitted). Robinette answered "no" to these questions, after which Deputy Newsome asked if he could search the car. Robinette consented. In the car, Deputy Newsome discovered a small amount of marijuana and, in a film container, a pill which was later determined to be methylenedioxymethamphetamine (MDMA). Robinette was then arrested and charged with knowing possession of a controlled substance, MDMA, in violation of <span class="citation no-link">Ohio Rev. Code Ann. § 2925.11</span>(A) (1993).</p>
<p>Before trial, Robinette unsuccessfully sought to suppress this evidence. He then pleaded "no contest," and was found guilty. On appeal, the Ohio Court of Appeals reversed, ruling that the search resulted from an unlawful detention. The Supreme Court of Ohio, by a divided vote, affirmed. <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/" aria-description="Citation for case: State v. Robinette">73 Ohio St. 3d 650</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/" aria-description="Citation for case: State v. Robinette">653 N. E. 2d 695</a></span> (1995). In its opinion, that court established a bright-line prerequisite for consensual interrogation under these circumstances:</p>
<blockquote>"The right, guaranteed by the federal and Ohio Constitutions, to be secure in one's person and property requires that citizens stopped for traffic offenses be clearly informed by the detaining officer when they are free to go after a valid detention, before an officer attempts to engage in a consensual interrogation. Any attempt at consensual interrogation must be preceded by the phrase `At this time you legally are free to go' or by words of similar import." <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#650" aria-description="Citation for case: State v. Robinette"><i>Id.,</i> at 650-651</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#696" aria-description="Citation for case: State v. Robinette">653 N. E. 2d, at 696</a></span>.</blockquote>
<p>We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./516/1157/">516 U. S. 1157</a></span> (1996), to review this <i>per se</i> rule, and we now reverse.</p>
<p>We must first consider whether we have jurisdiction to review the Ohio Supreme Court's decision. Respondent contends that we lack such jurisdiction because the Ohio decision rested upon the Ohio Constitution, in addition to the <span class="star-pagination">*37</span> Federal Constitution. Under <i>Michigan</i> v.<i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983),when "a state court decision fairly appears to rest primarily on federal law, or to be interwoven with the federal law, and when the adequacy and independence of any possible state law ground is not clear from the face of the opinion, we will accept as the most reasonable explanation that the state court decided the case the way it did because it believed that federal law required it to do so."<sup>[*]</sup><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long"><i>Id.,</i> at 1040-1041</a></span>. Although the opinion below mentions Art. I, § 14, of the Ohio Constitution in passing (a section which reads identically to the Fourth Amendment), the opinion clearly relies on federal law nevertheless. Indeed, the only cases it discusses or even cites are federal cases, except for one state case which itself applies the Federal Constitution.</p>
<p>Our jurisdiction is not defeated by the fact that these citations appear in the body of the opinion, while, under Ohio law, "[the] Supreme Court speaks as a court only through the syllabi of its cases." See <i>Ohio</i> v. <i>Gallagher,</i> <span class="citation" data-id="9426357"><a href="/opinion/109424/ohio-v-gallagher/#259" aria-description="Citation for case: Ohio v. Gallagher">425 U. S. 257, 259</a></span> (1976). When the syllabus, as here, speaks only in general terms of "the federal and Ohio Constitutions," it is permissible for us to turn to the body of the opinion to discern the grounds for decision. <i>Zacchini</i> v. <i>Scripps-Howard Broadcasting Co.</i> , <span class="citation" data-id="9426968"><a href="/opinion/109730/zacchini-v-scripps-howard-broadcasting-co/#566" aria-description="Citation for case: Zacchini v. Scripps-Howard Broadcasting Co.">433 U. S. 562, 566</a></span> (1977).</p>
<p>Respondent Robinette also contends that we may not reach the question presented in the petition because the Supreme Court of Ohio also held, as set out in the syllabus paragraph (1):</p>
<blockquote>"When the motivation behind a police officer's continued detention of a person stopped for a traffic violation is not related to the purpose of the original, constitutional stop, and when that continued detention is not based on any articulable facts giving rise to a suspicion of some <span class="star-pagination">*38</span> separate illegal activity justifying an extension of the detention, the continued detention constitutes an illegal seizure." <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#650" aria-description="Citation for case: State v. Robinette">73 Ohio St. 3d, at 650</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#696" aria-description="Citation for case: State v. Robinette">653 N. E. 2d, at 696</a></span>.</blockquote>
<p>In reliance on this ground, the Supreme Court of Ohio held that when Newsome returned to Robinette's car and asked him to get out of the car, after he had determined in his own mind not to give Robinette a ticket, the detention then became unlawful.</p>
<p>Respondent failed to make any such argument in his brief in opposition to certiorari. See this Court's Rule 15.2. We believe the issue as to the continuing legality of the detention is a "predicate to an intelligent resolution" of the question presented, and therefore "fairly included therein." This Court's Rule 14.1(a); <i>Vance</i> v. <i>Terrazas,</i> <span class="citation" data-id="9427734"><a href="/opinion/110168/vance-v-terrazas/" aria-description="Citation for case: Vance v. Terrazas">444 U. S. 252</a></span>, 258 259, n. 5 (1980). The parties have briefed this issue, and we proceed to decide it.</p>
<p>We think that under our recent decision in <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U. S. 806</a></span> (1996) (decided after the Supreme Court of Ohio decided the present case), the subjective intentions of the officer did not make the continued detention of respondent illegal under the Fourth Amendment. As we made clear in <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span>,</i> "`the fact that [an] officer does not have the state of mind which is hypothecated by the reasons which provide the legal justification for the officer's action does not invalidate the action taken as long as the circumstances, viewed objectively, justify that action.'. . . Subjective intentions play no role in ordinary, probablecause Fourth Amendment analysis." <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Id.,</a></span></i> at 813 (quoting <i>Scott</i> v. <i>United States,</i> <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#138" aria-description="Citation for case: Scott v. United States">436 U. S. 128, 138</a></span> (1978)). And there is no question that, in light of the admitted probable cause to stop Robinette for speeding, Deputy Newsome was objectively justified in asking Robinette to get out of the car, subjective thoughts notwithstanding. See <i>Pennsylvania</i> v. <i>Mimms,</i> <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#111" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 111, n. 6</a></span> (1977) ("We hold .. . that once a motor vehicle has been lawfully detained for a traffic violation, the police officers may order the driver to get out <span class="star-pagination">*39</span> of the vehicle without violating the Fourth Amendment's proscription of unreasonable searches and seizures").</p>
<p>We now turn to the merits of the question presented. We have long held that the "touchstone of the Fourth Amendment is reasonableness." <i>Florida</i> v. <i>Jimeno,</i> <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#250" aria-description="Citation for case: Florida v. Jimeno">500 U. S. 248, 250</a></span> (1991). Reasonableness, in turn, is measured in objective terms by examining the totality of the circumstances.</p>
<p>In applying this test we have consistently eschewed bright-line rules, instead emphasizing the fact-specific nature of the reasonableness inquiry. Thus, in <i>Florida</i> v. <i>Royer,</i>  <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U. S. 491</a></span> (1983), we expressly disavowed any "litmuspaper test" or single "sentence or . . . paragraph . . . rule," in recognition of the "endless variations in the facts and circumstances" implicating the Fourth Amendment. <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#506" aria-description="Citation for case: Florida v. Royer"><i>Id.,</i> at 506</a></span>. Then, in <i>Michigan</i> v. <i>Chesternut,</i> <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/" aria-description="Citation for case: Michigan v. Chesternut">486 U. S. 567</a></span> (1988), when both parties urged "bright-line rule[s] applicable to all investigatory pursuits," we rejected both proposed rules as contrary to our "traditional contextual approach." <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#572" aria-description="Citation for case: Michigan v. Chesternut"><i>Id.,</i> at 572-573</a></span>. And again, in <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429</a></span> (1991), when the Florida Supreme Court adopted a <i>per se</i>  rule that questioning aboard a bus always constitutes a seizure, we reversed, reiterating that the proper inquiry necessitates a consideration of "all the circumstances surrounding the encounter." <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#439" aria-description="Citation for case: Florida v. Bostick"><i>Id.,</i> at 439</a></span>.</p>
<p>We have previously rejected a <i>per se</i> rule very similar to that adopted by the Supreme Court of Ohio in determining the validity of a consent to search. In <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973), it was argued that such a consent could not be valid unless the defendant knew that he had a right to refuse the request. We rejected this argument: "While knowledge of the right to refuse consent is one factor to be taken into account, the government need not establish such knowledge as the <i>sine qua non</i> of an effective consent." <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#227" aria-description="Citation for case: Schneckloth v. Bustamonte"><i>Id.,</i> at 227</a></span>. And just as it "would be thoroughly impractical to impose on the normal consent search the detailed requirements of an effective warning," <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#231" aria-description="Citation for case: Schneckloth v. Bustamonte"><i>id.,</i> at 231</a></span>, so too would it be <span class="star-pagination">*40</span> unrealistic to require police officers to always inform detainees that they are free to go before a consent to search may be deemed voluntary.</p>
<p>The Fourth Amendment test for a valid consent to search is that the consent be voluntary, and "[v]oluntariness is a question of fact to be determined from all the circumstances," <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#248" aria-description="Citation for case: Schneckloth v. Bustamonte"><i>id.,</i> at 248-249</a></span>. The Supreme Court of Ohio having held otherwise, its judgment is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i> </p>
<p>Justice Ginsburg, concurring in the judgment.</p>
<p>Robert Robinette's traffic stop for a speeding violation on an interstate highway in Ohio served as prelude to a search of his automobile for illegal drugs. Robinette's experience was not uncommon in Ohio. As the Ohio Supreme Court related, the sheriff's deputy who detained Robinette for speeding and then asked Robinette for permission to search his vehicle "was on drug interdiction patrol at the time." <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#651" aria-description="Citation for case: State v. Robinette">73 Ohio St. 3d 650, 651</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#696" aria-description="Citation for case: State v. Robinette">653 N. E. 2d 695, 696</a></span> (1995). The deputy testified in Robinette's case that he routinely requested permission to search automobiles he stopped for traffic violations. <i><span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/" aria-description="Citation for case: State v. Robinette">Ibid.</a></span></i> According to the deputy's testimony in another prosecution, he requested consent to search in 786 traffic stops in 1992, the year of Robinette's arrest. <i>State</i>  v. <i>Retherford,</i> <span class="citation" data-id="3755951"><a href="/opinion/4001886/state-v-retherford/#594" aria-description="Citation for case: State v. Retherford">93 Ohio App. 3d 586, 594, n. 3</a></span>, <span class="citation" data-id="3755951"><a href="/opinion/4001886/state-v-retherford/#503" aria-description="Citation for case: State v. Retherford">639 N. E. 2d 498, 503, n. 3</a></span>, dism'd, <span class="citation" data-id="6770179"><a href="/opinion/6877572/cleveland-bar-assn-v-young/" aria-description="Citation for case: Cleveland Bar Ass&#x27;n v. Young">69 Ohio St. 3d 1488</a></span>, <span class="citation no-link">635 N. E. 2d 43</span> (1994).</p>
<p>From their unique vantage point, Ohio's courts observed that traffic stops in the State were regularly giving way to contraband searches, characterized as consensual, even when officers had no reason to suspect illegal activity. One Ohio appellate court noted: "[H]undreds, and perhaps thousands of Ohio citizens are being routinely delayed in their travels and asked to relinquish to uniformed police officers their <span class="star-pagination">*41</span> right to privacy in their automobiles and luggage, sometimes for no better reason than to provide an officer the opportunity to `practice' his drug interdiction technique." <span class="citation" data-id="3755951"><a href="/opinion/4001886/state-v-retherford/#594" aria-description="Citation for case: State v. Retherford">93 Ohio App. 3d, at 594</a></span>, <span class="citation" data-id="3755951"><a href="/opinion/4001886/state-v-retherford/#503" aria-description="Citation for case: State v. Retherford">639 N. E. 2d, at 503</a></span> (footnote omitted).</p>
<p>Against this background, the Ohio Supreme Court determined, and announced in Robinette's case, that the federal and state constitutional rights of Ohio citizens to be secure in their persons and property called for the protection of a clear-cut instruction to the State's police officers: An officer wishing to engage in consensual interrogation of a motorist at the conclusion of a traffic stop must first tell the motorist that he or she is free to go. The Ohio Supreme Court described the need for its first-tell-then-ask rule this way:</p>
<blockquote>"The transition between detention and a consensual exchange can be so seamless that the untrained eye may not notice that it has occurred. . . .</blockquote>
<p>. . . . .</p>
<blockquote>"Most people believe that they are validly in a police officer's custody as long as the officer continues to interrogate them. The police officer retains the upper hand and the accouterments of authority. That the officer lacks legal license to continue to detain them is unknown to most citizens, and a reasonable person would not feel free to walk away as the officer continues to address him.</blockquote>
<p>. . . . .</p>
<blockquote>"While the legality of consensual encounters between police and citizens should be preserved, we do not believe that this legality should be used by police officers to turn a routine traffic stop into a fishing expedition for unrelated criminal activity. The Fourth Amendment to the federal Constitution and Section 14, Article I of the Ohio Constitution exist to protect citizens against such an unreasonable interference with their liberty." <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#654" aria-description="Citation for case: State v. Robinette">73 Ohio St. 3d, at 654-655</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#698" aria-description="Citation for case: State v. Robinette">653 N. E. 2d, at 698-699</a></span>.</blockquote>
<p><span class="star-pagination">*42</span> Today's opinion reversing the decision of the Ohio Supreme Court does not pass judgment on the wisdom of the first-tell-then-ask rule. This Court's opinion simply clarifies that the Ohio Supreme Court's instruction to police officers in Ohio is not, under this Court's controlling jurisprudence, the command of the Federal Constitution. See <i>ante,</i> at 39 40. The Ohio Supreme Court invoked both the Federal Constitution and the Ohio Constitution without clearly indicating whether state law, standing alone, independently justified the court's rule. The ambiguity in the Ohio Supreme Court's decision renders this Court's exercise of jurisdiction proper under <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1040-1042</a></span> (1983), and this Court's decision on the merits is consistent with the Court's "totality of the circumstances" Fourth Amendment precedents, see <i>ante,</i> at 39. I therefore concur in the Court's judgment.</p>
<p>I write separately, however, because it seems to me improbable that the Ohio Supreme Court understood its firsttell-then-ask rule to be the Federal Constitution's mandate for the Nation as a whole. "[A] State is free <i>as a matter of its own law</i> to impose greater restrictions on police activity than those this Court holds to be necessary upon federal constitutional standards." <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#719" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714, 719</a></span> (1975).<sup>[*]</sup> But ordinarily, when a state high court grounds a rule of criminal procedure in the Federal Constitution, the <span class="star-pagination">*43</span> court thereby signals its view that the Nation's Constitution would require the rule in all 50 States. Given this Court's decisions in consent-to-search cases such as <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973), and <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429</a></span> (1991), however, I suspect that the Ohio Supreme Court may not have homed in on the implication ordinarily to be drawn from a state court's reliance on the Federal Constitution. In other words, I question whether the Ohio court thought of the strict rule it announced as a rule for the governance of police conduct not only in Miami County, Ohio, but also in Miami, Florida.</p>
<p>The first-tell-then-ask rule seems to be a prophylactic measure not so much extracted from the text of any constitutional provision as crafted by the Ohio Supreme Court to reduce the number of violations of textually guaranteed rights. In <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), this Court announced a similarly motivated rule as a minimal national requirement without suggesting that the text of the Federal Constitution required the precise measures the Court's opinion set forth. See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 467</a></span> ("[T]he Constitution [does not] necessarily requir[e] adherence to any particular solution" to the problems associated with custodial interrogations.); see also <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#306" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 306</a></span> (1985) ("The <i>Miranda</i> exclusionary rule . . . sweeps more broadly than the Fifth Amendment itself."). Although all parts of the United States fall within this Court's domain, the Ohio Supreme Court is not similarly situated. That court can declare prophylactic rules governing the conduct of officials in Ohio, but it cannot command the police forces of sister States. The very ease with which the Court today disposes of the federal leg of the Ohio Supreme Court's decision strengthens my impression that the Ohio Supreme Court saw its rule as a measure made for Ohio, designed to reinforce in that State the right of the people to be secure against unreasonable searches and seizures.</p>
<p><span class="star-pagination">*44</span> The Ohio Supreme Court's syllabus and opinion, however, were ambiguous. Under <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span>,</i> the existence of ambiguity regarding the federal- or state-law basis of a state-court decision will trigger this Court's jurisdiction. <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span></i> governs even when, all things considered, the more plausible reading of the state court's decision may be that the state court did not regard the Federal Constitution alone as a sufficient basis for its ruling. Compare <i>Arizona</i> v. <i>Evans,</i> <span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#7" aria-description="Citation for case: Arizona v. Evans">514 U. S. 1, 7-9</a></span> (1995), with <span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#31" aria-description="Citation for case: Arizona v. Evans"><i>id.,</i> at 31-33</a></span> (Ginsburg, J., dissenting).</p>
<p>It is incumbent on a state court, therefore, when it determines that its State's laws call for protection more complete than the Federal Constitution demands, to be clear about its ultimate reliance on state law. Similarly, a state court announcing a new legal rule arguably derived from both federal and state law can definitively render state law an adequate and independent ground for its decision by a simple declaration to that effect. A recent Montana Supreme Court opinion on the scope of an individual's privilege against self-incrimination includes such a declaration:</p>
<blockquote>"While we have devoted considerable time to a lengthy discussion of the application of the Fifth Amendment to the United States Constitution, it is to be noted that this holding is also based separately and independently on [the defendant's] right to remain silent pursuant to Article II, Section 25 of the Montana Constitution." <i>State</i>  v. <i>Fuller,</i> <span class="citation" data-id="9509960"><a href="/opinion/884042/state-v-fuller/#167" aria-description="Citation for case: State v. Fuller">276 Mont. 155, 167</a></span>, <span class="citation" data-id="9509960"><a href="/opinion/884042/state-v-fuller/#816" aria-description="Citation for case: State v. Fuller">915 P. 2d 809, 816</a></span>, cert. denied, <i>post,</i> p. 930.</blockquote>
<p>An explanation of this order meets the Court's instruction in <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span></i> that "[i]f the state court decision indicates clearly and expressly that it is alternatively based on bona fide separate, adequate, and independent grounds, [this Court] will not undertake to review the decision." <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1041" aria-description="Citation for case: Michigan v. Long">463 U. S., at 1041</a></span>.</p>
<p>On remand, the Ohio Supreme Court may choose to clarify that its instructions to law enforcement officers in Ohio find <span class="star-pagination">*45</span> adequate and independent support in state law, and that in issuing these instructions, the court endeavored to state dispositively only the law applicable in Ohio. See <i>Evans,</i> <span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#30" aria-description="Citation for case: Arizona v. Evans">514 U. S., at 30-34</a></span> (Ginsburg, J., dissenting). To avoid misunderstanding, the Ohio Supreme Court must itself speak with the clarity it sought to require of its State's police officers. The efficacy of its endeavor to safeguard the liberties of Ohioans without disarming the State's police can then be tested in the precise way Our Federalism was designed to work. See, <i>e. g.,</i> Kaye, State Courts at the Dawn of a New Century: Common Law Courts Reading Statutes and Constitutions, 70 N. Y. U. L. Rev. 1, 11-18 (1995); Linde, First Things First: Rediscovering the States' Bills of Rights, <span class="citation no-link">9 U. Balt. L. Rev. 379</span>, 392-396 (1980).</p>
<p>Justice Stevens, dissenting.</p>
<p>The Court's holding today is narrow: The Federal Constitution does not require that a lawfully seized person be advised that he is "free to go" before his consent to search will be recognized as voluntary. I agree with that holding. Given the Court's reading of the opinion of the Supreme Court of Ohio, I also agree that it is appropriate for the Court to limit its review to answering the sole question presented in the State's certiorari petition.<sup>[1]</sup> As I read the state-court opinion, however, the prophylactic rule announced in the second syllabus was intended as a guide to the decision of future cases rather than an explanation of the decision in this case. I would therefore affirm the judgment of the Supreme Court of Ohio because it correctly held that respondent's consent to the search of his vehicle was the product of an unlawful detention. Moreover, it is important <span class="star-pagination">*46</span> to emphasize that nothing in the Federal Constitutionor in this Court's opinionprevents a State from requiring its law enforcement officers to give detained motorists the advice mandated by the Ohio court.</p>
<p></p>
<h2>I</h2>
<p>The relevant facts are undisputed.<sup>[2]</sup> Officer Newsome stopped respondent because he was speeding. Neither at the time of the stop nor at any later time prior to the search of respondent's vehicle did the officer have any basis for believing that there were drugs in the car. After ordering respondent to get out of his car, issuing a warning, and returning his driver's license, Newsome took no further action related to the speeding violation. He did, however, state: "One question before you get gone: are you carrying any illegal contraband in your car? Any weapons of any kind, drugs, anything like that?" Thereafter, he obtained respondent's consent to search the car.</p>
<p>These facts give rise to two questions of law: whether respondent was still being detained when the "one question" was asked, and, if so, whether that detention was unlawful. In my opinion the Ohio Appellate Court and the Ohio Supreme Court correctly answered both of those questions.</p>
<p>The Ohio Supreme Court correctly relied upon <i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544</a></span> (1980),<sup>[3]</sup> which stated that "a person has been `seized' within the meaning of the Fourth Amendment . . . if, in view of all of the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave." <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall"><i>Id.,</i> at 554</a></span> (opinion of Stewart, J.); see <i>Michigan</i> v. <i>Chesternut,</i> <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#573" aria-description="Citation for case: Michigan v. Chesternut">486 U. S. 567, 573</a></span> (1988) (noting that "[t]he Court has since embraced this test"). See also <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#435" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429, 435-436</a></span> (1991) (applying variant of this approach). The Ohio Court <span class="star-pagination">*47</span> of Appeals applied a similar analysis. See App. to Pet. for Cert. 17-18.</p>
<p>Several circumstances support the Ohio courts' conclusion that a reasonable motorist in respondent's shoes would have believed that he had an obligation to answer the "one question" and that he could not simply walk away from the officer, get back in his car, and drive away. The question itself sought an answer "<i>before</i> you get gone." In addition, the facts that respondent had been detained, had received no advice that he was free to leave, and was then standing in front of a television camera in response to an official command are all inconsistent with an assumption that he could reasonably believe that he had no duty to respond. The Ohio Supreme Court was surely correct in stating: "Most people believe that they are validly in a police officer's custody as long as the officer continues to interrogate them. The police officer retains the upper hand and the accouterments of authority. That the officer lacks legal license to continue to detain them is unknown to most citizens, and a reasonable person would not feel free to walk away as the officer continues to address him." <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#655" aria-description="Citation for case: State v. Robinette">73 Ohio St. 3d, at 655</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#698" aria-description="Citation for case: State v. Robinette">653 N. E. 2d, at 698</a></span>.<sup>[4]</sup></p>
<p>Moreover, as an objective matter it is fair to presume that most drivers who have been stopped for speeding are in a hurry to get to their destinations; such drivers have no interest in prolonging the delay occasioned by the stop just to engage in idle conversation with an officer, much less to allow <span class="star-pagination">*48</span> a potentially lengthy search.<sup>[5]</sup> I also assume that motoristseven those who are not carrying contrabandhave an interest in preserving the privacy of their vehicles and possessions from the prying eyes of a curious stranger. The fact that this particular officer successfully used a similar method of obtaining consent to search roughly 786 times in one year, <i>State</i> v. <i>Retherford,</i> <span class="citation" data-id="3755951"><a href="/opinion/4001886/state-v-retherford/" aria-description="Citation for case: State v. Retherford">93 Ohio App. 3d 586</a></span>, 591 592, <span class="citation" data-id="3755951"><a href="/opinion/4001886/state-v-retherford/#502" aria-description="Citation for case: State v. Retherford">639 N. E. 2d 498, 502</a></span>, dism'd, <span class="citation" data-id="6770179"><a href="/opinion/6877572/cleveland-bar-assn-v-young/" aria-description="Citation for case: Cleveland Bar Ass&#x27;n v. Young">69 Ohio St. 3d 1488</a></span>, <span class="citation no-link">635 N. E. 2d 43</span> (1994), indicates that motorists generally respond in a manner that is contrary to their self-interest. Repeated decisions by ordinary citizens to surrender that interest cannot satisfactorily be explained on any hypothesis other than an assumption that they believed they had a legal duty to do so.</p>
<p>The Ohio Supreme Court was therefore entirely correct to presume in the first syllabus preceding its opinion that a "continued detention" was at issue here. <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#650" aria-description="Citation for case: State v. Robinette">73 Ohio St. 3d, at 650</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#696" aria-description="Citation for case: State v. Robinette">653 N. E. 2d, at 696</a></span>.<sup>[6]</sup> The Ohio Court of Appeals reached a similar conclusion. In response to the State's contention <span class="star-pagination">*49</span> that Robinette "was free to go" at the time consent was sought, that court heldafter reviewing the record that "a reasonable person in Robinette's position would not believe that the investigative stop had been concluded, and that he or she was free to go,so long as the police officer was continuing to ask investigative questions." App. to Pet. for Cert. 17-18. As I read the Ohio opinions, these determinations were independent of the bright-line rule criticized by the majority.<sup>[7]</sup> I see no reason to disturb them.</p>
<p>In the first syllabus, the Ohio Supreme Court also answered the question whether the officer's continued detention of respondent was lawful or unlawful. See <i>ante,</i> at 37 38. Although there is a possible ambiguity in the use of the word "motivation" in the Ohio Supreme Court's explanation of why the traffic officer's continued detention of respondent was an illegal seizure, the first syllabus otherwise was a correct statement of the relevant federal rule as well as the relevant Ohio rule. As this Court points out in its opinion, as a matter of federal law the subjective motivation of the officer does not determine the legality of a detention. Because I assume that the learned judges sitting on the Ohio Supreme Court were well aware of this proposition, we should construe the syllabus generously by replacing the ambiguous term "motivation behind" with the term "justification for" in order to make the syllabus unambiguously state the correct rule of federal law. So amended, the controlling proposition of federal law reads:</p>
<blockquote>"When the [justification for] a police officer's continued detention of a person stopped for a traffic violation is <span class="star-pagination">*50</span> not related to the purpose of the original, constitutional stop, and when that continued detention is not based on any articulable facts giving rise to a suspicion of some separate illegal activity justifying an extension of the detention, the continued detention constitutes an illegal seizure." <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#650" aria-description="Citation for case: State v. Robinette">73 Ohio St. 3d, at 650</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#696" aria-description="Citation for case: State v. Robinette">653 N. E. 2d, at 696</a></span>.</blockquote>
<p>Notwithstanding that the subjective motivation for the officer's decision to stop respondent related to drug interdiction, the legality of the stop depended entirely on the fact that respondent was speeding. Of course, "[a]s a general matter, the decision to stop an automobile is reasonable where the police have probable cause to believe that a traffic violation has occurred." <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#810" aria-description="Citation for case: Whren v. United States">517 U. S. 806, 810</a></span> (1996). As noted above, however, by the time Robinette was asked for consent to search his automobile, the lawful traffic stop had come to an end; Robinette had been given his warning, and the speeding violation provided no further justification for detention. The continued detention was therefore only justifiable, if at all, on some other grounds.<sup>[8]</sup></p>
<p>At no time prior to the search of respondent's vehicle did any articulable facts give rise to a reasonable suspicion of some separate illegal activity that would justify further detention. See <i>United States</i> v. <i>Sharpe,</i> <span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#682" aria-description="Citation for case: United States v. Sharpe">470 U. S. 675, 682</a></span> (1985); <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span>, 881 882 (1975); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 21</a></span> (1968). As an objective matter, it inexorably follows that when the officer had completed his task of either arresting or reprimanding the driver of the speeding car, his continued detention of that <span class="star-pagination">*51</span> person constituted an illegal seizure. This holding by the Ohio Supreme Court is entirely consistent with federal law.<sup>[9]</sup></p>
<p>The proper disposition follows as an application of wellsettled law. We held in <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U. S. 491</a></span> (1983), that a consent obtained during an illegal detention is ordinarily ineffective to justify an otherwise invalid search.<sup>[10]</sup> See also <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#433" aria-description="Citation for case: Florida v. Bostick">501 U. S., at 433-434</a></span> (noting that if consent was given during the course of an unlawful seizure, the results of the search "must be suppressed as tainted fruit"); <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#218" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 218-219</a></span> (1979); <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#601" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590, 601-602</a></span> (1975). Cf. <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963). Because Robinette's consent to the search was the product of an unlawful detention, "the consent was tainted by the illegality and was ineffective to justify the search." <i><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span>,</i> 460 U. S., at 507 508 (plurality opinion). I would therefore affirm the judgment below.</p>
<p></p>
<h2>II</h2>
<p>A point correctly raised by Justice Ginsburg merits emphasis. The Court's opinion today does not address either the wisdom of the rule announced in the second syllabus preceding <span class="star-pagination">*52</span> the Ohio Supreme Court's opinion or the validity of that rule as a matter of Ohio law. Nevertheless the risk that the narrowness of the Court's holding may not be fully understood prompts these additional words.</p>
<p>There is no rule of federal law that precludes Ohio from requiring its police officers to give its citizens warnings that will help them to understand whether a valid traffic stop has come to an end, and will help judges to decide whether a reasonable person would have felt free to leave under the circumstances at issue in any given case.<sup>[11]</sup> Nor, as I have previously observed, is there anything "in the Federal Constitution that prohibits a State from giving lawmaking power to its courts." <i>Minnesota</i> v. <i>Clover Leaf Creamery Co.,</i> <span class="citation" data-id="9428137"><a href="/opinion/110380/minnesota-v-clover-leaf-creamery-co/#479" aria-description="Citation for case: Minnesota v. Clover Leaf Creamery Co.">449 U. S. 456, 479</a></span>, and n. 3 (1981) (dissenting opinion). Thus, as far as we are concerned, whether Ohio acts through one branch of its government or another, it has the same power to enforce a warning rule as other States that may adopt such rules by executive action.<sup>[12]</sup></p>
<p><span class="star-pagination">*53</span> Moreover, while I recognize that warning rules provide benefits to the law enforcement profession and the courts, as well as to the public, I agree that it is not our function to pass judgment on the wisdom of such rules. Accordingly, while I have concluded that the judgment of the Supreme Court of Ohio should be affirmed, and thus dissent from this Court's disposition of the case, I am in full accord with its conclusion that the Federal Constitution neither mandates nor prohibits the warnings prescribed by the Ohio Court. Whether such a practice should be followed in Ohio is a matter for Ohio lawmakers to decide.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for the State of Alabama et al. by <i>Betty D. Montgomery,</i> Attorney General of Ohio<i>, Jeffrey S. Sutton,</i> State Solicitor, and <i>Simon B. Karas,</i> and by the Attorneys General for their respective States as follows: <i>Jeff Sessions</i> of Alabama, <i>Daniel E. Lungren</i> of California, <i>Gale A. Norton</i> of Colorado, <i>M. Jane Brady</i> of Delaware, <i>Robert Butterworth</i> of Florida, <i>Margery S. Bronster</i>  of Hawaii, <i>Alan G. Lance</i> of Idaho, <i>Jim Ryan</i> of Illinois, <i>Carla J. Stovall</i>  of Kansas, <i>A. B. Chandler III</i> of Kentucky, <i>Richard P. Ieyoub</i> of Louisiana, <i>Andrew Ketterer</i> of Maine, <i>J. Joseph Curran, Jr.,</i> of Maryland, <i>Scott Harshbarger</i> of Massachusetts, <i>Frank J. Kelley</i> of Michigan, <i>Hubert H. Humphrey III</i> of Minnesota, <i>Mike Moore</i> of Mississippi, <i>Joseph P. Mazurek</i> of Montana, <i>Don Stenberg</i> of Nebraska, <i>Frankie Sue Del Papa</i>  of Nevada, <i>Jeffrey R. Howard</i> of New Hampshire, <i>Deborah T. Poritz</i> of New Jersey, <i>Dennis C. Vacco</i> of New York, <i>Michael F. Easley</i> of North Carolina, <i>W. A. Drew Edmondson</i> of Oklahoma, <i>Theodore Kulongoski</i> of Oregon, <i>Thomas W. Corbett, Jr.,</i> of Pennsylvania, <i>Jeffrey B. Pine</i> of Rhode Island, <i>Mark Bennett</i> of South Dakota, <i>Charles W. Bursen</i> of Tennessee, <i>Dan Morales</i> of Texas, <i>Jeffrey L. Amestoy</i> of Vermont, <i>James S. Gilmore III</i> of Virginia, <i>Darrell V. McGraw, Jr.,</i> of West Virginia, <i>James E. Doyle</i>  of Wisconsin, and <i>William U. Hill</i> of Wyoming; and for Americans for Effective Law Enforcement, Inc., by <i>Fred E. Inbau, Wayne W. Schmidt, James P. Manak,</i> and <i>Bernard J. Farber.</i>
</p>
<p><i>Tracey Maclin, Steven R. Shapiro,</i> and <i>Jeffrey M. Gamso</i> filed a brief for the American Civil Liberties Union et al. as <i>amici curiae</i> urging affirmance.</p>
<p>Briefs of <i>amicus curiae</i> were filed for the National Association of Criminal Defense Lawyers by <i>Sheryl Gordon McCloud;</i> and for the Ohio Association of Criminal Defense Lawyers by <i>W. Andrew Hasselbach.</i> </p>
<p>[*]   Respondent and his <i>amici</i> ask us to take this opportunity to depart from <i>Michigan</i> v. <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span></i><i>.</i> We are no more persuaded by this argument now than we were two Terms ago, see <i>Arizona</i> v.<span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/" aria-description="Citation for case: Arizona v. Evans"><i>Evans,</i></a></span> 514 U. S.1 (1995), and we again reaffirm the <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span></i> presumption.</p>
<p>[*]   Formerly, the Ohio Supreme Court was "reluctant to use the Ohio Constitution to extend greater protection to the rights and civil libertiesof Ohio citizens" and had usually not taken advantage of opportunities to "us[e] the Ohio Constitution as an independent source of constitutional rights." <i>Arnold</i> v.<i>Cleveland,</i> <span class="citation" data-id="6768465"><a href="/opinion/6876050/arnold-v-city-of-cleveland/#42" aria-description="Citation for case: Arnold v. City of Cleveland">67 Ohio St. 3d 35, 42,n. 8</a></span>,<span class="citation" data-id="6768465"><a href="/opinion/6876050/arnold-v-city-of-cleveland/#168" aria-description="Citation for case: Arnold v. City of Cleveland">616 N. E. 2d 163, 168, n. 8</a></span> (1993). Recently, however, the state high court declared: "The Ohio Constitution is a document of independent force. .. .As long as state courts provide at least as much protection as the United States Supreme Court has provided in its interpretation of the federal Bill of Rights, state courts are unrestricted in according greater civil liberties and protections to individuals and groups." <span class="citation" data-id="6768465"><a href="/opinion/6876050/arnold-v-city-of-cleveland/#35" aria-description="Citation for case: Arnold v. City of Cleveland"><i>Id.,</i> at 35</a></span>, <span class="citation" data-id="6768465"><a href="/opinion/6876050/arnold-v-city-of-cleveland/#164" aria-description="Citation for case: Arnold v. City of Cleveland">616 N. E. 2d, at 164</a></span> (syllabus).</p>
<p>[1]  "Whether the Fourth Amendment to the United States Constitution requires police officers to inform motorists, lawfully stopped for traffic violations, that the legal detention has concluded before any subsequent interrogation or search will be found to be consensual?" Pet. for Cert. i.</p>
<p>[2]  This is in part because crucial portions of the exchange were videotaped; this recording is a part of the record.</p>
<p>[3]  See <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#654" aria-description="Citation for case: State v. Robinette">73 Ohio St. 3d 650, 654</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#698" aria-description="Citation for case: State v. Robinette">653 N. E. 2d 695, 698</a></span> (1995).</p>
<p>[4]  A learned commentator has expressed agreement on this point.See 4 W. LaFave, Search and Seizure § 9.3(a),p.112 (3ded. 1996 and Supp. 1997) ("Given the fact that [defendant] quite clearly had been seized when his car was pulled over, the return of the credentials hardly manifests a change in status when it was immediately followed by interrogation concerning other criminal activity");see also <i>ibid.</i> (approving of Ohio Supreme Court's analysisin this case). We have indicated as much ourselves in the past. See <i>Berkemer</i> v.<i>McCarty,</i> 468U. S.420, 436(1984) ("Certainly few motorists would feel free either to disobey a directive to pullover or to leave the scene of a traffic stop without being told they might do so").</p>
<p>[5]  Though this search does not appear to have been particularly intrusive, that may not always be so. See Brief for American Civil Liberties Union et al. as <i>Amici Curiae</i> 28-29. Indeed, our holding in <i>Florida</i> v. <i>Jimeno,</i>  <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/" aria-description="Citation for case: Florida v. Jimeno">500 U. S. 248</a></span> (1991), allowing police to open closed containers in the context of an automobile consent search where the "consent would reasonably be understood to extend to a particular container," <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#252" aria-description="Citation for case: Florida v. Jimeno"><i>id.,</i> at 252</a></span>, ensures that many motorists will wind up "consenting" to a far broader search than they might have imagined. See <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#254" aria-description="Citation for case: Florida v. Jimeno"><i>id.,</i> at 254-255</a></span> ("only objection that the police could have to" a rule requiring police to seek consent to search containers as well as the automobile itself "is that it would prevent them from exploiting the ignorance of a citizen who simply did not anticipate that his consent to search the car would be understood to authorize the police to rummage through his packages") (Marshall, J., dissenting).</p>
<p>[6]  It is ordinarily the syllabus that precedes an Ohio Supreme Court opinion, rather than the opinion itself, that states the law of the case. <i>Cassidy</i>  v. <i>Glossip,</i> <span class="citation" data-id="6753896"><a href="/opinion/6864181/cassidy-v-glossip/#24" aria-description="Citation for case: Cassidy v. Glossip">12 Ohio St. 2d 17, 24</a></span>, <span class="citation" data-id="6753896"><a href="/opinion/6864181/cassidy-v-glossip/#68" aria-description="Citation for case: Cassidy v. Glossip">231 N. E. 2d 64, 68</a></span> (1967); see <i>Migra</i> v. <i>Warren City School Dist. Bd. of Ed.,</i> <span class="citation" data-id="9429481"><a href="/opinion/111093/migra-v-warren-city-school-district-board-of-education/#86" aria-description="Citation for case: Migra v. Warren City School District Board of Education">465 U. S. 75, 86, n. 8</a></span> (1984); <i>Ohio</i> v. <i>Gallagher,</i> <span class="citation" data-id="9426357"><a href="/opinion/109424/ohio-v-gallagher/#259" aria-description="Citation for case: Ohio v. Gallagher">425 U. S. 257, 259</a></span> (1976).</p>
<p>[7]  Indeed, the first paragraph of the Ohio Supreme Court's opinion clearly indicates that the bright-line rule was meant to apply only in <i>future</i> cases. The Ohio Supreme Court first explained:"We find that the search was invalid since it was the product of an unlawful seizure."<span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#652" aria-description="Citation for case: State v. Robinette">73 Ohio St.3d, at 652</a></span>, <span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/#697" aria-description="Citation for case: State v. Robinette">653 N. E. 2d, at 697</a></span>.Only then did the court proceed to point out that it would "also use this case to establish a bright-line test . . . ."<i><span class="citation" data-id="6772304"><a href="/opinion/6879491/state-v-robinette/" aria-description="Citation for case: State v. Robinette">Ibid.</a></span></i> </p>
<p>[8]  Cf. <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#500" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 500</a></span> (1983) (plurality opinion) ("[A]n investigative detention must be temporary and last no longer than is necessary to effectuate the purpose of the stop"); <i>United States</i> v. <i>BrignoniPonce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 881</a></span> (1975) ("stop and inquiry must be `reasonably related in scope to the justification for their initiation' " (quoting <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 29</a></span> (1968)).</p>
<p>[9]  Since "this Court reviews judgments, not opinions," <i>Chevron U. S. A. Inc.</i> v. <i>Natural Resources Defense Council, Inc.,</i> <span class="citation" data-id="111221"><a href="/opinion/111221/chevron-u-s-a-inc-v-natural-resources-defense-council-inc/#842" aria-description="Citation for case: Chevron U. S. A. Inc. v. Natural Resources Defense...">467 U. S. 837, 842</a></span> (1984), the Ohio Supreme Court's holding that Robinette's continued seizure was illegal on these grounds provides a sufficient basis for affirming its judgment.</p>
<p>[10]  Writing for a plurality of the Court, Justice White explained that "statements given during a period of illegal detention are inadmissible even though voluntarily given if they are the product of the illegal detention and not the result of an independent act of free will." <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#501" aria-description="Citation for case: Florida v. Royer">460 U. S., at 501</a></span>. The defendant in <i><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span></i> had been "illegally detained when he consented to the search." <i><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Id.</a></span></i> , at 507. As a result, the plurality agreed that "the consent was tainted by the illegality and was ineffective to justify the search." <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#507" aria-description="Citation for case: Florida v. Royer"><i>Id.,</i> at 507-508</a></span>. Concurring in the result, Justice Brennan agreed with this much of the plurality's decision, diverging on other grounds. See <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#509" aria-description="Citation for case: Florida v. Royer"><i>id.,</i> at 509</a></span>. Justice Brennan's agreement on that narrow principle represents the holding of the Court. See <i>Marks</i> v. <i>United States,</i> <span class="citation" data-id="9004890"><a href="/opinion/9011945/marks-v-united-states/#193" aria-description="Citation for case: Marks v. United States">430 U. S. 188, 193</a></span> (1977).</p>
<p>[11]  Indeed, we indicated in <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#437" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429, 437</a></span> (1991), that the fact a defendant had been explicitly advised that he could refuse to give consent was relevant to the question whether he was seized at the time consent was sought. And, in other cases, we have stressed the importance of similar advice as a circumstance supporting the conclusion that a consent to search was voluntary. See <i>Schneckloth</i> v. <i>Bustamonte,</i>  <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#227" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 227</a></span> (1973); <i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544</a></span>, 558 559 (1980). Cf. <i>Washington</i> v. <i>Chrisman,</i> <span class="citation" data-id="9428641"><a href="/opinion/110636/washington-v-chrisman/#9" aria-description="Citation for case: Washington v. Chrisman">455 U. S. 1, 9</a></span> (1982) (consent to search was voluntary where defendant "consented, in writing, . . . after being advised that his consent must be voluntary and that he had an absolute right to refuse consent").</p>
<p>[12]  As we are informed by a brief <i>amicus curiae</i> filed by Americans For Effective Law Enforcement, Inc.: "Such a warning may be good police practice, and indeed <i>amicus</i> knows that many law enforcement agencies among our constituents have routinely incorporated a warning into their Fourth Amendment consent forms that they use in the field, but it is precisely thata <i>practice</i> and <i>not a constitutional imperative.</i> An officer who includes such a warning in his request for consent undoubtedly presents a stronger case for a finding of voluntariness in a suppression hearing, and we would not suggest that such agencies and officers do otherwise. We know, too, that instructors in many police training programs of leading universities and management institutes routinely recommend such warnings as a sound practice, likely to bolster the voluntariness of a consent to search. [We ourselves] conduc[t] law enforcement training programs at the national level and many of our own speakers have made this very point." Brief for Americans For Effective Law Enforcement, Inc., as <i>Amicus Curiae</i> 7.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Oliver v. United States.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Oliver v. United States"
type: case
citation: "466 U.S. 170 (1984)"
parallel_cite: "104 S. Ct. 1735; 80 L. Ed. 2d 214; 52 U.S.L.W. 4425"
neutral_cite: 1984 U.S. LEXIS 55
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-04-17
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-04-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Oliver v. United States
  varies_by_point: false
  scope_note: "Reaffirms the open-fields doctrine and the curtilage distinction; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111146/oliver-v-united-states/"
  cluster_id: 111146
  opinion_id: 9429563
  identity_checked: true
homes:
  - page: "[[Open Fields]]"
    role: "Key — Anchor"
  - page: "[[Curtilage]]"
    role: "Key"
related: ["[[Hester v. United States]]", "[[United States v. Dunn]]", "[[Florida v. Jardines]]", "[[California v. Ciraolo]]"]
aliases: []
tags: ["case", "fourth-amendment", "open-fields", "curtilage", "search"]
holding: "Reaffirms that open fields get no Fourth Amendment protection — even fenced, posted 'No Trespassing' land; only curtilage carries the home's protection."
lake:
  record_id: Oliver v. United States
  status: verified
  projected_at: 2026-07-06
---

# Oliver v. United States

*466 U.S. 170 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Acting on a tip, officers went onto Oliver's farm, drove past his house, went around a locked gate marked with a "No Trespassing" sign, and walked along a footpath into a secluded field, where they found a marijuana crop more than a mile from his house. (Decided together with *Maine v. Thornton*.)

## Issue
Whether the open-fields doctrine applies even to fields that are fenced, posted with "No Trespassing" signs, and secluded.

## Rule
Yes. "[O]pen fields do not provide the setting for those intimate activities that the Amendment is intended to shelter from government interference or surveillance." — 466 U.S. at 179. ^pin-179

Fencing and posting do not change that: "It is not generally true that fences or 'No Trespassing' signs effectively bar the public from viewing open fields." — *Id.* ^pin-179b

The common law "distinguished 'open fields' from the 'curtilage,' the land immediately surrounding and associated with the home," and "[t]he distinction implies that only the curtilage, not the neighboring open fields, warrants the Fourth Amendment protections that attach to the home." — *Id.* at 180. ^pin-180

## Application
The marijuana field, located more than a mile from Oliver's house and outside the [[Curtilage|curtilage]], was an open field. The locked gate and "No Trespassing" sign did not give it Fourth Amendment protection, so the officers' entry onto the land and observation of the crop were not a "search." The evidence was not subject to suppression on Fourth Amendment grounds.

## Conclusion
Because the field was an open field outside the [[Curtilage|curtilage]], no Fourth Amendment search occurred; the open-fields doctrine controlled.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Oliver* reaffirms the open-fields rule of [[Hester v. United States]] and frames the open-fields/[[Curtilage|curtilage]] line later refined by the four-factor test of [[United States v. Dunn]]; [[Curtilage|curtilage]]'s protection at the home's entrance was reinforced in [[Florida v. Jardines]].

## Appears on
- [[Curtilage]] — *Key — Progeny / Refinement*

## Sources
- *Oliver v. United States*, 466 U.S. 170 (1984) — https://www.courtlistener.com/opinion/111146/oliver-v-united-states/ — pinpoints: 179, 180.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ef22fd2a2b8de626", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Oliver v. United States"}, "payload": {"all": [{"cite": "466 U.S. 170", "page": "170", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "466"}, {"cite": "104 S. Ct. 1735", "page": "1735", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "104"}, {"cite": "80 L. Ed. 2d 214", "page": "214", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "80"}, {"cite": "1984 U.S. LEXIS 55", "page": "55", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1984"}, {"cite": "52 U.S.L.W. 4425", "page": "4425", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "52"}], "display": "466 U.S. 170", "official": {"cite": "466 U.S. 170", "page": "170", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "466"}, "official_selection_present": true, "record_id": "Oliver v. United States"}}
{"assertion_id": "9aced01f5fcee6e3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-179b", "record_id": "Oliver v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-179b", "pinpoint_status": "slip-only", "quote": "It is not generally true that fences or 'No Trespassing' signs effectively bar the public from viewing open fields.", "quote_fidelity": "mismatch", "record_id": "Oliver v. United States", "star_marker": null}}
{"assertion_id": "a92326cf2e260130", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-179", "record_id": "Oliver v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-179", "pinpoint_status": "slip-only", "quote": "signs, and secluded. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Oliver v. United States", "star_marker": null}}
{"assertion_id": "e2937de357bc76c4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-180", "record_id": "Oliver v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-180", "pinpoint_status": "slip-only", "quote": "distinguished 'open fields' from the 'curtilage,' the land immediately surrounding and associated with the home,", "quote_fidelity": "mismatch", "record_id": "Oliver v. United States", "star_marker": null}}
{"assertion_id": "2df7707c68537eec", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Oliver v. United States"}, "payload": {"as_of_content": "1984-04-17", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Oliver v. United States", "scope_note": "Reaffirms the open-fields doctrine and the curtilage distinction; good law.", "varies_by_point": false}}
```

### lake record — Oliver v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Oliver v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Oliver v. United States",
    "case_name_short": "Oliver",
    "case_name_full": "Oliver v. United States",
    "input_case_name": "Oliver v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-04-17",
    "year": 1984,
    "docket": null,
    "cluster_id": 111146,
    "lead_opinion_id": 9429563,
    "sibling_ids": [
      111146,
      9429563,
      9429564,
      9429565
    ],
    "absolute_url": "/opinion/111146/oliver-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9050194,
        "score": 20,
        "case_name": "Oliver v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "466 U.S. 170",
      "volume": "466",
      "reporter": "U.S.",
      "page": "170",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 1735",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "1735",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 L. Ed. 2d 214",
        "volume": "80",
        "reporter": "L. Ed. 2d",
        "page": "214",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4425",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4425",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 55",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "55",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "466 U.S. 170",
        "volume": "466",
        "reporter": "U.S.",
        "page": "170",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 1735",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "1735",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 L. Ed. 2d 214",
        "volume": "80",
        "reporter": "L. Ed. 2d",
        "page": "214",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 55",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "55",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4425",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4425",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "466 U.S. 170",
    "official_selection": {
      "court_class": "scotus",
      "selected": "466 U.S. 170",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-179",
      "page": null,
      "quote": "signs, and secluded. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-179b",
      "page": null,
      "quote": "It is not generally true that fences or 'No Trespassing' signs effectively bar the public from viewing open fields.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-180",
      "page": null,
      "quote": "distinguished 'open fields' from the 'curtilage,' the land immediately surrounding and associated with the home,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-04-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Oliver v. United States",
    "varies_by_point": false,
    "scope_note": "Reaffirms the open-fields doctrine and the curtilage distinction; good law.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Oliver v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Sorenson",
          "cluster_id": 4806437,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "The People v. Sean Garvin",
          "cluster_id": 4436829,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Missouri, Plaintiff/Respondent v. Timothy A. Pierce",
          "cluster_id": 4254135,
          "cite": [
            "504 S.W.3d 766",
            "2016 Mo. App. LEXIS 864"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane1_negative"
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
        "journal_ref": "Oliver v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4288590,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4287047,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4286131,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane1_negative"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jardines",
          "cluster_id": 856347,
          "cite": [
            "185 L. Ed. 2d 495",
            "133 S. Ct. 1409",
            "569 U.S. 1",
            "2013 U.S. LEXIS 2542",
            "24 Fla. L. Weekly Fed. S 117",
            "81 U.S.L.W. 4209",
            "2013 WL 1196577"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Ciraolo",
          "cluster_id": 111666,
          "cite": [
            "90 L. Ed. 2d 210",
            "106 S. Ct. 1809",
            "476 U.S. 207",
            "1986 U.S. LEXIS 154"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Villarreal v. State",
          "cluster_id": 2365320,
          "cite": [
            "935 S.W.2d 134",
            "1996 Tex. Crim. App. LEXIS 237",
            "1996 WL 668593"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Maury",
          "cluster_id": 2598797,
          "cite": [
            "68 P.3d 1",
            "133 Cal. Rptr. 2d 561",
            "30 Cal. 4th 342"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 622304,
          "cite": [
            "181 L. Ed. 2d 911",
            "132 S. Ct. 945",
            "565 U.S. 400",
            "2012 U.S. LEXIS 1063"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'CONNOR v. Ortega",
          "cluster_id": 111851,
          "cite": [
            "94 L. Ed. 2d 714",
            "107 S. Ct. 1492",
            "480 U.S. 709",
            "1987 U.S. LEXIS 1507",
            "1 I.E.R. Cas. (BNA) 1617",
            "55 U.S.L.W. 4405",
            "42 Empl. Prac. Dec. (CCH) 36,891"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Greenwood",
          "cluster_id": 112067,
          "cite": [
            "100 L. Ed. 2d 30",
            "108 S. Ct. 1625",
            "486 U.S. 35",
            "1988 U.S. LEXIS 2279",
            "56 U.S.L.W. 4409"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shirley Presley v. City of Charlottesville Rivanna Trails Foundation",
          "cluster_id": 795822,
          "cite": [
            "464 F.3d 480",
            "2006 U.S. App. LEXIS 24048",
            "2006 WL 2709208"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karo",
          "cluster_id": 111257,
          "cite": [
            "82 L. Ed. 2d 530",
            "104 S. Ct. 3296",
            "468 U.S. 705",
            "1984 U.S. LEXIS 148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Class",
          "cluster_id": 111600,
          "cite": [
            "89 L. Ed. 2d 81",
            "106 S. Ct. 960",
            "475 U.S. 106",
            "1986 U.S. LEXIS 5",
            "54 U.S.L.W. 4178"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ross",
          "cluster_id": 1060457,
          "cite": [
            "49 S.W.3d 833",
            "2001 Tenn. LEXIS 563",
            "2001 WL 760100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ramirez-Portoreal",
          "cluster_id": 2033638,
          "cite": [
            "666 N.E.2d 207",
            "88 N.Y.2d 99",
            "643 N.Y.S.2d 502"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. Virginia",
          "cluster_id": 4501697,
          "cite": [
            "584 U.S. 586",
            "138 S. Ct. 1663",
            "201 L. Ed. 2d 9",
            "2018 U.S. LEXIS 3210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
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
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Riley",
          "cluster_id": 112175,
          "cite": [
            "102 L. Ed. 2d 835",
            "109 S. Ct. 693",
            "488 U.S. 445",
            "1989 U.S. LEXIS 580"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oliver v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111146 OR 9429563 OR 9429564 OR 9429565) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDMwMjY1NjAwMDAwJnM9Mjc5NzI3NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111146+OR+9429563+OR+9429564+OR+9429565%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111146 OR 9429563 OR 9429564 OR 9429565)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMTYmcz0xNDM1NDY5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111146+OR+9429563+OR+9429564+OR+9429565%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111146 OR 9429563 OR 9429564 OR 9429565)",
        "reviewed": 40,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 40,
        "triage_read": 1,
        "triage_snippet_classified": 39
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111146 OR 9429563 OR 9429564 OR 9429565)",
    "indexed_citing_opinions": 1195,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111146,
        "count": 1026,
        "count_source": "search"
      },
      {
        "opinion_id": 9429563,
        "count": 201,
        "count_source": "search"
      },
      {
        "opinion_id": 9429564,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429565,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1924,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/oliver-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5OTk3NzImcz0xMDEyNDc3OCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111146+OR+9429563+OR+9429564+OR+9429565%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111146,
        "cited_id": 85272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 85827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 103355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 106538,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 108988,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 109032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 111013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 111112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 238889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 285923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 304813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 308561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 340832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 358699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 388191,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 393323,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 398901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 421926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 1092690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 1503690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 1557741,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 1852754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111146,
        "cited_id": 1948051,
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
    "date_created": "2026-07-05T16:08:49Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:09:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:09:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:11:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:09:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Oliver v. United States

```
<opinion type="majority">
<author id="b233-7"><page-number citation-index="1" label="173">*173</page-number>Justice Powell</author>
<p id="Az-">delivered the opinion of the Court.</p>
<p id="b233-8">The “open fields” doctrine, first enunciated by this Court in <em>Hester </em>v. <em>United States, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924), permits police officers to enter and search a field without a warrant. We granted certiorari in these cases to clarify confusion that has arisen as to the continued vitality of the doctrine.</p>
<p id="b233-3">
<em>I</em>
</p>
<p id="AC-">No. 82-15.Acting on reports that marihuana was being raised on the farm of petitioner Oliver, two narcotics agents of the Kentucky State Police went to the farm to investigate.<footnotemark>1</footnotemark> Arriving at the farm, they drove past petitioner's house to a locked gate with a “No Trespassing” sign. A footpath led around one side of the gate. The agents walked around the gate and along the road for several hundred yards, passing a bam and a parked camper. At that point, someone standing in front of the camper shouted: “No hunting is allowed, come back up here.” The officers shouted back that they were Kentucky State Police officers, but found no one when they returned to the camper. The officers resumed their investigation of the farm and found a field of marihuana over a mile from petitioner’s home.</p>
<p id="b233-4">Petitioner was arrested and indicted for “manufacturing]” a “controlled substance.” <span class="citation no-link">21 U. S. C. § 841</span>(a)(1). After a pretrial hearing, the District Court suppressed evidence of the discovery of the marihuana field. Applying <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> (1967), the court found that petitioner had a reasonable expectation that the field would remain private because petitioner “had done all that could be expected of him to assert his privacy in the area of farm that was searched.” He had posted “No Trespassing” signs at regular intervals and had locked the gate at the entrance to the center of the farm. App. to Pet. for Cert. in No. 82-15, <page-number citation-index="1" label="174">*174</page-number>pp. 23-24. Further, the court noted that the field itself is highly secluded: it is bounded on all sides by woods, fences, and embankments and cannot be seen from any point of public access. The court concluded that this was not an “open” field that invited casual intrusion.</p>
<p id="b234-5">The Court of Appeals for the Sixth Circuit, sitting en banc, reversed the District Court. <span class="citation multiple-matches"><a href="/c/F.%202d/686/356/">686 F. 2d 356</a></span> (1982).<footnotemark>2</footnotemark> The court concluded that <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>upon which the District Court relied, had not impaired the vitality of the open fields doctrine of <em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">Hester</a></span>. </em>Rather, the open fields doctrine was entirely compatible with <em>Katz’ </em>emphasis on privacy. The court reasoned that the “human relations that create the need for privacy do not ordinarily take place” in open fields, and that the property owner’s common-law right to exclude trespassers is insufficiently linked to privacy to warrant the Fourth Amendment’s protection. 686 F. 2d, at 360.<footnotemark>3</footnotemark> We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./459/1168/">459 U. S. 1168</a></span> (1983).</p>
<p id="b234-6"><em>No. 82-1273. </em>After receiving an anonymous tip that marihuana was being grown in the woods behind respondent Thornton’s residence, two police officers entered the woods by a path between this residence and a neighboring house. They followed a footpath through the woods until they reached two marihuana patches fenced with chicken wire. Later, the officers determined that the patches were on the property of respondent, obtained a warrant to search the property, and seized the marihuana. On the basis of this evidence, respondent was arrested and indicted.</p>
<p id="b235-4"><page-number citation-index="1" label="175">*175</page-number>The trial court granted respondent’s motion to suppress the fruits of the second search. The warrant for this search was premised on information that the police had obtained during their previous warrantless search, that the court found to be unreasonable.<footnotemark>4</footnotemark> “No Trespassing” signs and the secluded location of the marihuana patches evinced a reasonable expectation of privacy. Therefore, the court held, the open fields doctrine did not apply.</p>
<p id="b235-5">The Maine Supreme Judicial Court affirmed. <span class="citation" data-id="1948051"><a href="/opinion/1948051/state-v-thornton/" aria-description="Citation for case: State v. Thornton">453 A. 2d 489</a></span> (1982). It agreed with the trial court that the correct question was whether the search “is a violation of privacy on which the individual justifiably relied,” <span class="citation" data-id="1948051"><a href="/opinion/1948051/state-v-thornton/#493" aria-description="Citation for case: State v. Thornton"><em>id., </em>at 493</a></span>, and that the search violated respondent’s privacy. The court also agreed that the open fields doctrine did not justify the search. That doctrine applies, according to the court, only when officers are lawfully present on property and observe “open and patent” activity. <span class="citation" data-id="1948051"><a href="/opinion/1948051/state-v-thornton/#495" aria-description="Citation for case: State v. Thornton"><em>Id., </em>at 495</a></span>. In this case, the officers had trespassed upon defendant’s property, and the respondent had made every effort to conceal his activity. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./460/1068/">460 U. S. 1068</a></span> (1983).<footnotemark>5</footnotemark></p>
<p id="pAaq"><page-number citation-index="1" label="176">*176</page-number>h — I</p>
<p id="b236-3">The rule announced in <em>Hester </em>v. <em>United States </em>was founded upon the explicit language of the Fourth Amendment. That Amendment indicates with some precision the places and things encompassed by its protections. As Justice Holmes explained for the Court in his characteristically laconic style: “[T]he special protection accorded by the Fourth Amendment to the people in their ‘persons, houses, papers, and effects,’ is not extended to the open fields. The distinction between the latter and the house is as old as the common law.” <em>Hester </em>v. <em>United States, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#59" aria-description="Citation for case: Hester v. United States">265 U. S., at 59</a></span>.<footnotemark>6</footnotemark></p>
<p id="b236-4">Nor are the open fields “effects” within the meaning of the Fourth Amendment. In this respect, it is suggestive that James Madison’s proposed draft of what became the Fourth <page-number citation-index="1" label="177">*177</page-number>Amendment preserves “[t]he rights of the people to be secured in their persons, their houses, their papers, and their other property, from all unreasonable searches and seizures . . . .” See N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 100, n. 77 (1937). Although Congress’ revisions of Madison’s proposal broadened the scope of the Amendment in some respects, <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#100" aria-description="Citation for case: Hester v. United States"><em>id., </em>at 100-103</a></span>, the term “effects” is less inclusive than “property” and cannot be said to encompass open fields.<footnotemark>7</footnotemark> We conclude, as did the Court in deciding <em>Hester </em>v. <em>United States, </em>that the government’s intrusion upon the open fields is not one of those “unreasonable searches” proscribed by the text of the Fourth Amendment.</p>
<p id="pAku">hH HH</p>
<p id="b237-3">This interpretation of the Fourth Amendment’s language is consistent with the understanding of the right to privacy expressed in our Fourth Amendment jurisprudence. Since <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), the touchstone of Amendment analysis has been the question whether a person has a “constitutionally protected reasonable expectation of privacy.” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States"><em>Id., </em>at 360</a></span> (Harlan, J., concurring). The Amendment does not protect the merely subjective expectation of privacy, but only those “expectation[s] that society is prepared to recognize as ‘reasonable.’” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States"><em>Id., </em>at 361</a></span>. See also <em>Smith </em>v. <em>Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#740" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735, 740-741</a></span> (1979).</p>
<p id="b237-4">A</p>
<p id="b237-5">No single factor determines whether an individual legitimately may claim under the Fourth Amendment that a place should be free of government intrusion not authorized by warrant. See <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#152" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 152-153</a></span> <page-number citation-index="1" label="178">*178</page-number>(1978) (Powell, J., concurring). In assessing the degree to which a search infringes upon individual privacy, the Court has given weight to such factors as the intention of the Framers of the Fourth Amendment, <em>e. g., United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#7" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 7-8</a></span> (1977), the uses to which the individual has put a location, <em>e. g., Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#265" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 265</a></span> (1960), and our societal understanding that certain areas deserve the most scrupulous protection from government invasion, <em>e. g., Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980). These factors are equally relevant to determining whether the government’s intrusion upon open fields without a warrant or probable cause violates reasonable expectations of privacy and is therefore a search proscribed by the Amendment.</p>
<p id="b238-5">In this light, the rule of <em>Hester </em>v. <em>United States, supra, </em>that we reaffirm today, may be understood as providing that an individual may not legitimately demand privacy for activities conducted out of doors in fields, except in the area immediately surrounding the home. See also <em>Air Pollution Variance Bd. </em>v. <em>Western Alfalfa Corp., </em><span class="citation" data-id="109032"><a href="/opinion/109032/air-pollution-variance-bd-of-colo-v-western-alfalfa-corp/#865" aria-description="Citation for case: Air Pollution Variance Bd. of Colo. v. Western Alfalfa Corp.">416 U. S. 861, 865</a></span> (1974). This rule is true to the conception of the right to privacy embodied in the Fourth Amendment. The Amendment reflects the recognition of the Framers that certain enclaves should be free from arbitrary government interference. For example, the Court since the enactment of the Fourth Amendment has stressed “the overriding respect for the sanctity of the home that has been embedded in our traditions since the origins of the Republic.” <em>Payton </em>v. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#601" aria-description="Citation for case: Payton v. New York"><em>New York, supra, </em>at 601</a></span>.<footnotemark>8</footnotemark> See also <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 511</a></span> (1961); <em>United States </em>v. <em>United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 313</a></span> (1972).</p>
<p id="b239-4"><page-number citation-index="1" label="179">*179</page-number>In contrast, open fields do not provide the setting for those intimate activities that the Amendment is intended to shelter from government interference or surveillance. There is no societal interest in protecting the privacy of those activities, such as the cultivation of crops, that occur in open fields. Moreover, as a practical matter these lands usually are accessible to the public and the police in ways that a home, an office, or commercial structure would not be. It is not generally true that fences or “No Trespassing” signs effectively bar the public from viewing open fields in rural areas. And both petitioner Oliver and respondent Thornton concede that the public and police lawfully may survey lands from the air.<footnotemark>9</footnotemark> For these reasons, the asserted expectation of privacy in open fields is not an expectation that “society recognizes as reasonable.”<footnotemark>10</footnotemark></p>
<p id="b240-4"><page-number citation-index="1" label="180">*180</page-number>The historical underpinnings of the open fields doctrine also demonstrate that the doctrine is consistent with respect for “reasonable expectations of privacy. ” As Justice Holmes, writing for the Court, observed in <em>Hester, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#59" aria-description="Citation for case: Hester v. United States">265 U. S., at 59</a></span>, the common law distinguished “open fields” from the “curti-lage,” the land immediately surrounding and associated with the home. See 4 W. Blackstone, Commentaries *225. The distinction implies that only the curtilage, not the neighboring open fields, warrants the Fourth Amendment protections that attach to the home. At common law, the curtilage is the area to which extends the intimate activity associated with the “sanctity of a man’s home and the privacies of life,” <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span> (1886), and therefore has been considered part of the home itself for Fourth Amendment purposes. Thus, courts have extended Fourth Amendment protection to the curtilage; and they have defined the curtilage, as did the common law, by reference to the factors that determine whether an individual reasonably may expect that an area immediately adjacent to the home will remain private. See, <em>e. g., United States </em>v. <em>Van Dyke, </em><span class="citation" data-id="388191"><a href="/opinion/388191/united-states-v-larry-g-van-dyke/#993" aria-description="Citation for case: United States v. Larry G. Van Dyke">643 F. 2d 992, 993-994</a></span> (CA4 1981); <em>United States </em>v. <em>Williams, </em><span class="citation" data-id="358699"><a href="/opinion/358699/united-states-v-otis-williams/#453" aria-description="Citation for case: United States v. Otis Williams">581 F. 2d 451, 453</a></span> (CA5 1978); <em>Care </em>v. <em>United States, </em><span class="citation" data-id="238889"><a href="/opinion/238889/orval-care-v-united-states/#25" aria-description="Citation for case: Orval Care v. United States">231 F. 2d 22, 25</a></span> (CA10), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./351/932/">351 U. S. 932</a></span> (1956). Conversely, the common law implies, as we reaffirm today, that no expectation of privacy legitimately attaches to open fields.<footnotemark>11</footnotemark></p>
<p id="b241-4"><page-number citation-index="1" label="181">*181</page-number>We conclude, from the text of the Fourth Amendment and from the historical and contemporary understanding of its purposes, that an individual has no legitimate expectation that open fields will remain free from warrantless intrusion by government officers.</p>
<p id="b241-5">B</p>
<p id="b241-6">Petitioner Oliver and respondent Thornton contend, to the contrary, that the circumstances of a search sometimes may indicate that reasonable expectations of privacy were violated; and that courts therefore should analyze these circumstances on a case-by-case basis. The language of the Fourth Amendment itself answers their contention.</p>
<p id="b241-7">Nor would a case-by-case approach provide a workable accommodation between the needs of law enforcement and the interests protected by the Fourth Amendment. Under this approach, police officers would have to guess before every search whether landowners had erected fences sufficiently high, posted a sufficient number of warning signs, or located contraband in an area sufficiently secluded to establish a right of privacy. The lawfulness of a search would turn on “ ‘[a] highly sophisticated set of rules, qualified by all sorts of ifs, ands, and buts and requiring the drawing of subtle nuances and hairline distinctions . . . <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#458" aria-description="Citation for case: New York v. Belton">453 U. S. 454, 458</a></span> (1981) (quoting LaFave, “Case-By-Case Adjudication” versus “Standardized Procedures”: The Robinson Dilemma, 1974 S. Ct. Rev. 127, 142). This Court repeatedly has acknowledged the difficulties created for courts, police, and citizens by an ad hoc, case-by-case definition of Fourth Amendment standards to be applied in differing factual circumstances. See <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#458" aria-description="Citation for case: New York v. Belton"><em>Belton, supra, </em>at 458-460</a></span>; <em>Robbins </em>v. <em>California, </em><span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#430" aria-description="Citation for case: Robbins v. California">453 U. S. 420, 430</a></span> (1981) (Powell, J., concurring in judgment); <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#213" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 213-214</a></span> (1979); <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#235" aria-description="Citation for case: United States v. Robinson">414 U. S. 218, 235</a></span> (1973). The ad hoc approach not only makes it difficult for the policeman to discern the scope of his authority, <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton"><em>Belton, supra, </em>at 460</a></span>; it also creates a danger that consti<page-number citation-index="1" label="182">*182</page-number>tutional rights will be arbitrarily and inequitably enforced. Cf. <em>Smith </em>v. <em>Goguen, </em><span class="citation" data-id="9425639"><a href="/opinion/108988/smith-v-goguen/#572" aria-description="Citation for case: Smith v. Goguen">415 U. S. 566, 572-573</a></span> (1974).<footnotemark>12</footnotemark></p>
<p id="b242-5">IV</p>
<p id="b242-6">In any event, while the factors that petitioner Oliver and respondent Thornton urge the courts to consider may be relevant to Fourth Amendment analysis in some contexts, these factors cannot be decisive on the question whether the search of an open field is subject to the Amendment. Initially, we reject the suggestion that steps taken to protect privacy establish that expectations of privacy in an open field are legitimate. It is true, of course, that petitioner Oliver and respondent Thornton, in order to conceal their criminal activities, planted the marihuana upon secluded land and erected fences and “No Trespassing” signs around the property. And it may be that because of such precautions, few members of the public stumbled upon the marihuana crops seized by the police. Neither of these suppositions demonstrates, however, that the expectation of privacy was <em>legitimate </em>in the sense required by the Fourth Amendment. The test of legitimacy is not whether the individual chooses to conceal assertedly “private” activity.<footnotemark>13</footnotemark> Rather, the correct inquiry is whether the government’s intrusion infringes upon the per<page-number citation-index="1" label="183">*183</page-number>sonal and societal values protected by the Fourth Amendment. As we have explained, we find no basis for concluding that a police inspection of open fields accomplishes such an infringement.</p>
<p id="b243-5">Nor is the government’s intrusion upon an open field a “search” in the constitutional sense because that intrusion is a trespass at common law. The existence of a property right is but one element in determining whether expectations of privacy are legitimate. “ ‘The premise that property interests control the right of the Government to search and seize has been discredited.’” <em>Katz, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S., at 353</a></span> (quoting <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#304" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 304</a></span> (1967)). “[E]ven a property interest in premises may not be sufficient to establish a legitimate expectation of privacy with respect to particular items located on the premises or activity conducted thereon.” <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#144" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 144, n. 12</a></span>.</p>
<p id="b243-6">The common law may guide consideration of what areas are protected by the Fourth Amendment by defining areas whose invasion by others is wrongful. <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#153" aria-description="Citation for case: Rakas v. Illinois">Id., at 153</a></span> (Powell, J., concurring).<footnotemark>14</footnotemark> The law of trespass, however, forbids intrusions upon land that the Fourth Amendment would not proscribe. For trespass law extends to instances where the exercise of the right to exclude vindicates no legitimate privacy interest.<footnotemark>15</footnotemark> Thus, in the case of open fields, the general <page-number citation-index="1" label="184">*184</page-number>rights of property protected by the common law of trespass have little or no relevance to the applicability of the Fourth Amendment.</p>
<p id="b244-5">V</p>
<p id="b244-6">We conclude that the open fields doctrine, as enunciated in <em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">Hester</a></span>, </em>is consistent with the plain language of the Fourth Amendment and its historical purposes. Moreover, Justice Holmes’ interpretation of the Amendment in <em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">Hester</a></span> </em>accords with the “reasonable expectation of privacy” analysis developed in subsequent decisions of this Court. We therefore affirm <em>Oliver </em>v. <em>United States; Maine </em>v. <em>Thornton </em>is reversed and remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b244-7">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b233-5"> It is conceded that the police did not have a warrant authorizing the search, that there was no probable cause for the search, and that no exception to the warrant requirement is applicable.</p>
</footnote>
<footnote label="2">
<p id="b234-7"> A panel of the Sixth Circuit had affirmed the suppression order. <span class="citation" data-id="393323"><a href="/opinion/393323/united-states-v-ray-e-oliver-aka-edward-ray-oliver/" aria-description="Citation for case: United States v. Ray E. Oliver, A/K/A Edward Ray Oliver">657 F. 2d 85</a></span> (1981).</p>
</footnote>
<footnote label="3">
<p id="b234-8"> The four dissenting judges contended that the open fields doctrine did not apply where, as in this case, “reasonable effortfs] [have] been made to exclude the public.” 686 F. 2d, at 372. To that extent, the dissent considered that <em>Katz </em>v. <em>United States </em>implicitly had overruled previous holdings of this Court. The dissent then concluded that petitioner had established a “reasonable expectation of privacy” under the <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>standard. Judge Lively also wrote separately to argue that the open fields doctrine applied only to lands that could be viewed by the public.</p>
</footnote>
<footnote label="4">
<p id="b235-6"> The court also discredited other information, supplied by a confidential informant, upon which the police had based their warrant application.</p>
</footnote>
<footnote label="5">
<p id="b235-8"> Respondent contends that the decision below rests upon adequate and independent state-law grounds. We do not read that decision, however, as excluding the evidence because the search violated the State Constitution. The Maine Supreme Judicial Court referred only to the Fourth Amendment of the Federal Constitution and purported to apply the <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>test; the prior state cases that the court cited also construed the Federal Constitution. In any case, the Maine Supreme Judicial Court did not articulate an independent state ground with the clarity required by <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983).</p>
<p id="b235-9">Contrary to respondent’s assertion, we do not review here the state courts’ finding as a matter of “fact” that the area searched was not an “open field. ” Rather, the question before us is the appropriate legal standard for determining whether search of that area without a warrant was lawful under the Federal Constitution.</p>
<p id="b235-10">The conflict between the two cases that we review here is illustrative of the confusion the open fields doctrine has generated among the state and <page-number citation-index="1" label="176">*176</page-number>federal courts. Compare, <em>e. g., State </em>v. <em>Byers, </em><span class="citation" data-id="1852754"><a href="/opinion/1852754/state-v-byers/" aria-description="Citation for case: State v. Byers">359 So. 2d 84</a></span> (La. 1978) (refusing to apply open fields doctrine); <em>State </em>v. <em>Brady, </em><span class="citation" data-id="1092690"><a href="/opinion/1092690/state-v-brady/" aria-description="Citation for case: State v. Brady">406 So. 2d 1098</a></span> (Fla. 1981) (same), with <em>United States </em>v. <em>Lace, </em><span class="citation" data-id="9468813"><a href="/opinion/398901/united-states-v-david-t-lace-roger-r-ducharme-gary-d-butts-patricia/#50" aria-description="Citation for case: United States v. David T. Lace, Roger R. Ducharme, Gary...">669 F. 2d 46, 50-51</a></span> (CA2 1982); <em>United States </em>v. <em>Freie, </em><span class="citation" data-id="8900337"><a href="/opinion/8912486/united-states-v-freie/" aria-description="Citation for case: United States v. Freie">545 F. 2d 1217</a></span> (CA9 1976); <em>United States </em>v. <em>Brown, </em><span class="citation" data-id="308561"><a href="/opinion/308561/united-states-v-larry-joseph-brown/#954" aria-description="Citation for case: United States v. Larry Joseph Brown">473 F. 2d 952, 954</a></span> (CA5 1973); <em>Atwell </em>v. <em>United States, </em><span class="citation" data-id="285923"><a href="/opinion/285923/james-d-atwell-and-melvin-edmon-surrett-v-united-states/#138" aria-description="Citation for case: James D. Atwell and Melvin Edmon Surrett v. United States">414 F. 2d 136, 138</a></span> (CA5 1969).</p>
</footnote>
<footnote label="6">
<p id="b236-10"> The dissent offers no basis for its suggestion that <em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">Hester</a></span> </em>rests upon some narrow, unarticulated principle rather than upon the reasoning enunciated by the Court’s opinion in that case. Nor have subsequent cases discredited Hester*s reasoning. This Court frequently has relied on the explicit language of the Fourth Amendment as delineating the scope of its affirmative protections. See, <em>e. g., Robbins </em>v. <em>California, </em><span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#426" aria-description="Citation for case: Robbins v. California">453 U. S. 420, 426</a></span> (1981) (opinion of Stewart, J.); <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#589" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 589-590</a></span> (1980); <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#178" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 178-180</a></span> (1969). As these cases, decided after <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>indicate, <em>Katz’ </em>“reasonable expectation of privacy” standard did not sever Fourth Amendment doctrine from the Amendment’s language. <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>itself construed the Amendment’s protection of the person against unreasonable searches to encompass electronic eavesdropping of telephone conversations sought to be kept private; and <em>Katz’ </em>fundamental recognition that “the Fourth Amendment protects people — and not simply ‘areas’ — against unreasonable searches and seizures,” see <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States">389 U. S., at 353</a></span>, is faithful to the Amendment’s language. As <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>demonstrates, the Court fairly may respect the constraints of the Constitution’s language without wedding itself to an unreasoning literalism. In contrast, the dissent’s approach would ignore the language of the Constitution itself as well as overturn this Court’s governing precedent.</p>
</footnote>
<footnote label="7">
<p id="b237-6"> The Framers would have understood the term “effects” to be limited to personal, rather than real, property. See generally <em>Doe </em>v. <em>Dring, 2 M. &amp; </em>S. 448, 454, 105 Eng. Rep. 447, 449 (K. B. 1814) (discussing prior cases); 2 W. Blackstone, Commentaries *16, *384-*385.</p>
</footnote>
<footnote label="8">
<p id="b238-6"> The Fourth Amendment’s protection of offices and commercial buildings, in which there may be legitimate expectations of privacy, is also based upon societal expectations that have deep roots in the history of the Amendment. See <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#311" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 311</a></span> (1978); <em>G. M. Leasing Corp. </em>v. <em>United States, </em><span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#366" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 366</a></span> (1977).</p>
</footnote>
<footnote label="9">
<p id="b239-5"> Tr. of Oral Arg. 14-15, 58. See, <em>e. g., United States </em>v. <em>Allen, </em><span class="citation" data-id="8915013"><a href="/opinion/8925485/united-states-v-allen/#1380" aria-description="Citation for case: United States v. Allen">675 F. 2d 1373, 1380-1381</a></span> (CA9 1980); <em>United States </em>v. <em>DeBacker, </em><span class="citation" data-id="1557741"><a href="/opinion/1557741/united-states-v-debacker/#1081" aria-description="Citation for case: United States v. DeBacker">493 F. Supp. 1078, 1081</a></span> (WD Mich. 1980). In practical terms, petitioner Oliver’s and respondent Thornton’s analysis merely would require law enforcement officers, in most situations, to use aerial surveillance to gather the information necessary to obtain a warrant or to justify warrantless entry onto the property. It is not easy to see how such a requirement would advance legitimate privacy interests.</p>
</footnote>
<footnote label="10">
<p id="b239-6"> The dissent conceives of open fields as bustling with private activity as diverse as lovers’ trysts and worship services. <em>Post, </em>at 191-193. But in most instances police will disturb no one when they enter upon open fields. These fields, by their very character as open and unoccupied, are unlikely to provide the setting for activities whose privacy is sought to be protected by the Fourth Amendment. One need think only of the vast expanse of some western ranches or of the undeveloped woods of the Northwest to see the unreality of the dissent’s conception. Further, the Fourth Amendment provides ample protection to activities in the open fields that might implicate an individual’s privacy. An individual who enters a place defined to be “public” for Fourth Amendment analysis does not lose all claims to privacy or personal security. Cf. <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#766" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 766-767</a></span> (1979) (Burger, C. J., concurring in judgment). For example, the Fourth Amendment’s protections against unreasonable arrest or unreasonable seizure of effects upon the person remain fully applicable. See, <em>e. g., United States </em>v. <em>Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976).</p>
</footnote>
<footnote label="11">
<p id="b240-5"> Neither petitioner Oliver nor respondent Thornton has contended that the property searched was within the curtilage. Nor is it necessary in these cases to consider the scope of the curtilage exception to the open fields doctrine or the degree of Fourth Amendment protection afforded the curtilage, as opposed to the home itself. It is clear, however, that the term “open fields” may include any unoccupied or undeveloped area outside of the curtilage. An open field need be neither “open” nor a “field” as those terms are used in common speech. For example, contrary to respondent Thornton's suggestion, Tr. of Oral Arg. 21-22, a thickly wooded area nonetheless may be an open field as that term is used in construing the Fourth Amendment. See, <em>e. g., United States </em>v. <em>Pruitt, </em><span class="citation" data-id="304813"><a href="/opinion/304813/united-states-v-harry-william-pruitt/" aria-description="Citation for case: United States v. Harry William Pruitt">464 F. 2d 494</a></span> (CA9 1972); <em>Bedell </em>v. <em>State, </em><span class="citation" data-id="9642483"><a href="/opinion/1503690/bedell-v-state/" aria-description="Citation for case: Bedell v. State">257 Ark. 895</a></span>, <span class="citation" data-id="9642483"><a href="/opinion/1503690/bedell-v-state/" aria-description="Citation for case: Bedell v. State">521 S. W. 2d 200</a></span> (1975).</p>
</footnote>
<footnote label="12">
<p id="b242-7"> The clarity of the open fields doctrine that we reaffirm today is not sacrificed, as the dissent suggests, by our recognition that the curtilage remains within the protections of the Fourth Amendment. Most of the many millions of acres that are “open fields” are not close to any structure and so not arguably within the curtilage. And, for most homes, the boundaries of the curtilage will be clearly marked; and the conception defining the curtilage — as the area around the home to which the activity of home life extends — is a familiar one easily understood from our daily experience. The occasional difficulties that courts might have in applying this, like other, legal concepts, do not argue for the unprecedented expansion of the Fourth Amendment advocated by the dissent.</p>
</footnote>
<footnote label="13">
<p id="b242-8"> Certainly the Framers did not intend that the Fourth Amendment should shelter criminal activity wherever persons with criminal intent choose to erect barriers and post “No Trespassing” signs.</p>
</footnote>
<footnote label="14">
<p id="b243-7"> As noted above, the common-law conception of the “curtilage” has served this function.</p>
</footnote>
<footnote label="15">
<p id="b243-8"> The law of trespass recognizes the interest in possession and control of one’s property and for that reason permits exclusion of unwanted intruders. But it does not follow that the right to exclude conferred by trespass law embodies a privacy interest also protected by the Fourth Amendment. To the contrary, the common law of trespass furthers a range of interests that have nothing to do with privacy and that would not be served by applying the strictures of trespass law to public officers. Criminal laws against trespass are prophylactic: they protect against intruders who poach, steal livestock and crops, or vandalize property. And the civil action of trespass serves the important function of authorizing an owner to defeat claims of prescription by asserting his own title. See, <em>e. g., </em><page-number citation-index="1" label="184">*184</page-number>0. Holmes, The Common Law 98-100, 244-246 (1881). In any event, unlicensed use of property by others is presumptively unjustified, as anyone who wishes to use the property is free to bargain for the right to do so with the property owner, cf. R. Posner, Economic Analysis of Law 10-13, 21 (1973). For these reasons, the law of trespass confers protections from intrusion by others far broader than those required by Fourth Amendment interests.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Olivier v. City of Brandon.json  (`lake-record`, 1 assertions)

### content_page

```
---
title: Olivier v. City of Brandon
type: case
citation: "No. 24-993, slip op. (U.S. 2026)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2026
date_decided: ""
docket: 24-993
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
  opinion_url: "https://www.courtlistener.com/opinion/10811625/olivier-v-city-of-brandon/"
  cluster_id: 10811625
  opinion_id: null
  identity_checked: false
lake:
  record_id: Olivier v. City of Brandon
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Heck v. Humphrey]]"
tags:
  - case
  - section-1983
  - heck-v-humphrey
  - prospective-relief
  - first-amendment
  - favorable-termination
  - supreme-court
holding: "Heck v. Humphrey does not bar a § 1983 suit seeking purely prospective relief — here an injunction against future enforcement of a protest-permit ordinance — even where the plaintiff was previously convicted of violating that same ordinance, because such a suit is not designed to annul the prior conviction and falls within § 1983's heartland."
aliases:
  - Olivier v. City of Brandon
  - "Olivier v. City of Brandon, Mississippi"
  - "Olivier v. City of Brandon (2026)"
---

# Olivier v. City of Brandon

*No. 24-993, slip op. (U.S. 2026)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10811625 → majority opinion 11278377 (No. 24-993, decided Mar. 20, 2026). Rule quote string-matched to the CL slip-opinion syllabus 2026-07-07; slip-style pin (current-Term slip opinion, no reporter cite assigned — S2 A3). S9 promotes. -->

## Background
Gabriel Olivier, a street preacher, was convicted in municipal court of violating a City of Brandon ordinance requiring protesters and demonstrators near an amphitheater to stay within a "designated protest area." He paid a fine, served no prison time, and did not appeal. Still wishing to preach near the amphitheater, he sued the City under 42 U.S.C. § 1983, seeking only prospective relief: a declaration that the ordinance violates the First Amendment and an injunction against its future enforcement. The lower courts held the suit barred by *[[Heck v. Humphrey]]*, reasoning that success would cast doubt on the validity of his prior conviction.

## Issue
Whether *[[Heck v. Humphrey]]* bars a § 1983 suit for wholly prospective relief brought by a plaintiff previously convicted under the challenged law.

## Rule
*[[Heck v. Humphrey|Heck]]* prohibits using § 1983 to obtain relief that would necessarily imply the invalidity of a conviction or sentence when the plaintiff seeks release or damages, but a suit that is "in no way designed to annul the results of a state trial" and seeks only "to be free from prosecutions for future violations" falls within § 1983's heartland (*Wooley v. Maynard*). The Court held: "Olivier's suit seeking purely prospective relief — an injunction stopping officials from enforcing an ordinance in the future — can proceed, notwithstanding Olivier's prior conviction for violating that ordinance; *Heck* does not hold otherwise." — slip op. at 1. ^pin-slip1

## Application
Olivier sought neither the reversal of his conviction nor damages for it — only forward-looking relief so he could preach without fear of future arrest. That request does not question the validity of his completed conviction; it seeks to prevent future enforcement, exactly the kind of claim *Wooley* permitted a previously convicted plaintiff to bring. Reading *[[Heck v. Humphrey|Heck]]* to bar it would trap Olivier between intentionally flouting state law and forgoing what he believes to be constitutionally protected activity.

## Conclusion
**Reversed and [[Reading and Citing Cases#on-remand|remanded]].** Justice Kagan wrote for a unanimous Court (9–0).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Olivier* cabins *[[Heck v. Humphrey|Heck]]*'s favorable-termination rule to claims that would undermine a conviction or seek release/damages, confirming that prospective injunctive relief against future enforcement remains available under § 1983 even to a previously convicted plaintiff.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Olivier v. City of Brandon*, No. 24-993, slip op. (U.S. 2026)](https://www.courtlistener.com/opinion/10811625/olivier-v-city-of-brandon/) — pinpoint: slip op. at 1 (Heck does not bar prospective-relief § 1983 suits). Rule quote string-matched to the CL slip-opinion syllabus 2026-07-07. Current-Term slip opinion; no U.S. Reports cite assigned yet (S2 A3 slip precedent).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "22a752c0b1cdc7db", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Olivier v. City of Brandon"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Olivier v. City of Brandon", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Olivier v. City of Brandon

```json
{
  "schema_version": "s2.v1",
  "record_id": "Olivier v. City of Brandon",
  "status": "under_review",
  "identity": {
    "case_name": "Olivier v. City of Brandon",
    "case_name_short": "Olivier",
    "case_name_full": "",
    "input_case_name": "Olivier v. City of Brandon",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2026,
    "docket": "24-993",
    "cluster_id": 10811625,
    "lead_opinion_id": 11278377,
    "sibling_ids": [],
    "absolute_url": "/opinion/10811625/olivier-v-city-of-brandon/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [],
    "all": [],
    "display": null,
    "official_selection": {
      "court_class": "scotus",
      "selected": null,
      "reason": "no_official_class_citation"
    },
    "slip_only": true,
    "slip_only_provenance": {
      "source": "R8-R3-web-cites.jsonl",
      "as_of": "2026-07-07",
      "by": "s6-slip-stamp",
      "note": "SCOTUS No. 24-993, decided 2026-03-20 (607 U.S. ___; Kagan, 9-0). No S. Ct. page yet. (Search-floated '146 S. Ct. 916' rejected as fabricated.)",
      "legs": [
        {
          "source": "Cornell LII",
          "url": "https://www.law.cornell.edu/supremecourt/text/24-993",
          "cite": "No. 24-993, decided 2026-03-20"
        },
        {
          "source": "SCOTUSblog",
          "url": "https://www.scotusblog.com/cases/case-files/olivier-v-city-of-brandon-mississippi/",
          "cite": "No. 24-993; no reporter cite listed"
        }
      ]
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
    "date_created": "2026-07-06T12:13:43Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:13:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:13:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:13:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:13:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "olivier-v-city-of-brandon--10811625",
      "to_record_id": "Olivier v. City of Brandon",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Olivier v. City of Brandon

```
(Slip Opinion)              OCTOBER TERM, 2025                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

        OLIVIER v. CITY OF BRANDON, MISSISSIPPI

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE FIFTH CIRCUIT

   No. 24–993.      Argued December 3, 2025—Decided March 20, 2026


Petitioner Gabriel Olivier is a street preacher in Mississippi who believes
  that sharing his religious views with fellow citizens is an important
  part of exercising his faith. His vocation sometimes took him to the
  sidewalks near an amphitheater in the City of Brandon, where he
  could find sizable audiences attending events. In 2019, the City
  adopted an ordinance requiring all individuals or groups engaging in
  “protests” or “demonstrations,” at around the time events were sched-
  uled, to stay within a “designated protest area.” In 2021, Olivier was
  arrested for violating that ordinance. He pleaded no contest in munic-
  ipal court. The court imposed a $304 fine, one year of probation, and
  10 days of imprisonment to be served only if he violated the ordinance
  during his probation. Olivier did not appeal, paid the fine, and served
  no prison time. Because he still wanted to preach near the amphithe-
  ater, Olivier filed suit against the City in federal court under 42
  U. S. C. §1983, alleging that the city ordinance violates the Free
  Speech Clause of the First Amendment by consigning him and other
  speakers to the amphitheater’s protest area. The complaint seeks, as
  a remedy, a declaration that the ordinance infringes the First Amend-
  ment and an injunction preventing city officials from enforcing the or-
  dinance in the future. In other words, the relief requested is only pro-
  spective; Olivier seeks neither the reversal of, nor compensation for,
  his prior conviction.
    The parties contested in the lower courts whether this Court’s deci-
  sion in Heck v. Humphrey, 512 U. S. 477—which prohibits the use of
  §1983 to challenge the validity of a prior conviction or sentence so as
  to obtain release from custody or monetary damages—bars the suit
  from going forward. On the City’s view of Heck, a person previously
2                    OLIVIER v. CITY OF BRANDON

                                  Syllabus

    convicted of violating a statute cannot challenge its constitutionality
    under §1983 because success in the suit would cast doubt on the prior
    conviction’s correctness. On Olivier’s contrary view, Heck does not ap-
    ply when a plaintiff seeks wholly prospective relief, rather than relief
    relating to the prior conviction. The District Court agreed with the
    City’s understanding of Heck and found Olivier’s suit barred. The
    Court of Appeals for the Fifth Circuit affirmed on the same reasoning.
Held: Olivier’s suit seeking purely prospective relief—an injunction stop-
 ping officials from enforcing an ordinance in the future—can proceed,
 notwithstanding Olivier’s prior conviction for violating that ordinance;
 Heck does not hold otherwise. Pp. 5–13.
    (a) Before the Court’s decision in Heck, the City would have had no
 plausible basis for claiming Olivier’s suit is barred. That type of suit
 falls within §1983’s heartland: Assuming a credible threat of prosecu-
 tion, a plaintiff may bring a §1983 action to challenge a local law as
 violating the Constitution and to prevent that law’s future enforce-
 ment. See, e.g., Steffel v. Thompson, 415 U. S. 452. In Wooley v.
 Maynard, 430 U. S. 705, the Court held that rule to apply even when
 the plaintiff was previously convicted under the challenged law. The
 Court explained that because the suit at issue sought “wholly prospec-
 tive” relief—“only to be free from prosecutions for future violations”—
 and was “in no way designed to annul the results of a state trial,” §1983
 provided an avenue for the plaintiff ’s claim. Id., at 711. Were it oth-
 erwise, the plaintiff would have been trapped “between the Scylla of
 intentionally flouting state law and the Charybdis of forgoing what he
 believes to be constitutionally protected activity.” Id., at 710.
    The Court’s decision in Wooley, taken alone, would defeat the City’s
 attempt to prevent Olivier’s suit from going forward, but the City ar-
 gues the Court’s later decision in Heck requires the opposite result. In
 Heck, the Court held that a state prisoner could not use §1983 to seek
 damages attributable to his allegedly unconstitutional conviction. The
 Court reasoned that such a suit in truth mounts a “collateral attack”
 on the validity of the conviction, and thus intrudes on the habeas stat-
 ute’s domain. 512 U. S., at 485. And such a suit could lead to “parallel
 litigation” and “conflicting” judgments about the same conduct, with
 the §1983 suit suggesting that the plaintiff should be released even as
 criminal or habeas proceedings found the opposite. Id., at 484. Hence
 the so-called Heck bar on “§1983 damages actions that necessarily re-
 quire the plaintiff to prove the unlawfulness of his conviction or con-
 finement.” Id., at 486. “[W]hen a state prisoner seeks damages in a
 §1983 suit,” the Court went on, “the district court must consider
 whether a judgment in favor of the plaintiff would necessarily imply
 the invalidity of his conviction or sentence.” Id., at 487.
    The Court subsequently drew a line between Heck-type claims and
                     Cite as: 607 U. S. ___ (2026)                         3

                                Syllabus

those seeking forward-looking relief. In Edwards v. Balisok, 520 U. S.
641, the Court held that while a state prisoner could not obtain dam-
ages for an alleged past violation, a claim for “prospective injunctive
relief ”—the use of fairer procedures in the future—may “properly be
brought under §1983,” because it does not depend on showing the “in-
validity of a previous” sentencing decision. Id., at 648. In Wilkinson
v. Dotson, 544 U. S. 74, the Court allowed state prisoners to bring a
§1983 suit requesting an injunction requiring the State to “comply
with constitutional” parole requirements “in the future,” determining
that such a claim for “future relief ” was “distant” from “the core of ha-
beas” and so not barred by Heck. 544 U. S., at 77, 82. Pp. 5–9.
  (b) As in Balisok and Dotson, Olivier’s suit falls outside habeas’s
core—and likewise outside Heck’s concerns. Olivier is not challenging
the “validity of [his] conviction or sentence,” for the purpose of securing
release or obtaining monetary damages. Nance v. Ward, 597 U. S. 159,
167–168. Instead, he seeks “wholly prospective” relief—“only to be free
from prosecutions for future violations” of the ordinance. Wooley, 430
U. S., at 711. Because Olivier’s suit does not, as habeas suits do, “col-
lateral[ly] attack” the old conviction, it cannot give rise to “parallel lit-
igation” respecting his prior conduct, and does not risk “conflicting”
judgments over how that conduct was prosecuted or punished. Heck,
512 U. S., at 484, 485. Unlike in Heck, Olivier’s suit merely attempts
to prevent a future prosecution, so the Heck bar does not come into
play. Pp. 9–10.
  (c) The City’s main argument to the contrary rests on one sentence
in Heck that states: “[W]hen a state prisoner seeks damages in a §1983
suit, the district court must consider whether a judgment in favor of
the plaintiff would necessarily imply the invalidity of his conviction or
sentence; if it would, the complaint must be dismissed.” 512 U. S., at
487. Strictly speaking, the “necessarily imply” language fits: If Olivier
succeeds in this suit, it would mean his prior conviction was unconsti-
tutional. But “general language in judicial opinions should be read as
referring in context to circumstances similar to [those] then before the
Court,” Turkiye Halk Bankasi A.S. v. United States, 598 U. S. 264, 278,
and the circumstances here differ from those in Heck. The Heck lan-
guage at issue was used to identify claims that were really assaults on
a prior conviction, even though involving some indirection. By con-
trast, there is no looking back in Olivier’s suit; both in the allegations
made, and in the relief sought, the suit is entirely future oriented—
even if success in it shows that something past should not have oc-
curred. The Heck Court did not consider such a suit, and the Heck
language was not meant to address it. Heck, properly understood, does
not preclude suits that only attempt to prevent future prosecutions.
4                    OLIVIER v. CITY OF BRANDON

                                  Syllabus

    Olivier’s suit to enjoin future prosecutions under the city ordinance, so
    he can return to the amphitheater, may proceed. Pp. 10–13.

    KAGAN, J., delivered the opinion for a unanimous Court.
                        Cite as: 607 U. S. ____ (2026)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     United States Reports. Readers are requested to notify the Reporter of
     Decisions, Supreme Court of the United States, Washington, D. C. 20543,
     pio@supremecourt.gov, of any typographical or other formal errors.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 24–993
                                   _________________


     GABRIEL OLIVIER, PETITIONER v. CITY OF
             BRANDON, MISSISSIPPI
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE FIFTH CIRCUIT
                                [March 20, 2026]

  JUSTICE KAGAN delivered the opinion of the Court.
  Petitioner Gabriel Olivier was once convicted of violating
a city ordinance restricting expressive activity near a public
amphitheater. He now wishes to return to that venue to
voice his beliefs—but this time, without the threat of crim-
inal punishment. He therefore filed this suit, alleging that
the city ordinance infringes the First Amendment. The
suit, brought under 42 U. S. C. §1983, seeks an order de-
claring the ordinance unconstitutional and preventing its
enforcement in the future. The suit, in other words, re-
quests only forward-looking relief—nothing to do with Oliv-
ier’s prior conviction.
  The question presented here is whether this Court’s deci-
sion in Heck v. Humphrey, 512 U. S. 477 (1994), bars Oliv-
ier’s suit. The answer is no. Heck prohibits the use of §1983
to challenge the validity of a prior conviction or sentence so
as to obtain release from custody or monetary damages.
That decision has no bearing on Olivier’s suit seeking a
purely prospective remedy.
2               OLIVIER v. CITY OF BRANDON

                      Opinion of the Court

                               I
   Olivier was convicted some five years ago for violating the
local ordinance he now challenges. Olivier is a street
preacher in Mississippi—a Christian who believes that
sharing his religious views with fellow citizens is an im-
portant part of exercising his faith. His vocation sometimes
took him to the sidewalks near an amphitheater in the City
of Brandon, where he could find sizable audiences attend-
ing events. Olivier was apparently not the only speaker at-
tracted to that area, and the activities there caused some
disruption. In 2019, the City adopted an ordinance requir-
ing all individuals or groups engaging in “protests” or
“demonstrations,” at around the time events were sched-
uled, to stay within a “designated protest area.” Supp. to
App. 70 (capitalization deleted). On his next trip to the am-
phitheater, in 2021, Olivier checked out that area, but
found it too remote for communicating his message. So he
returned, along with his signs and loudspeaker, to the side-
walk fronting the amphitheater. And there he was arrested
by the Brandon police chief for violating the city ordinance.
The next month, Olivier pleaded no contest in municipal
court. The court imposed a $304 fine; one year of probation;
and ten days of imprisonment, to be served only if, during
his probation, he again violated the ordinance. Olivier did
not appeal, paid the fine, and served no prison time.
   Because he still wanted to preach near the amphitheater,
Olivier’s next step was to file this lawsuit in federal court,
naming the City and its police chief as defendants. The suit
is brought under §1983, which authorizes claims against
state and local officials for the “deprivation of any rights”
secured by the Constitution. Olivier’s complaint alleges
that the city ordinance violates the Free Speech Clause of
the First Amendment by consigning him (and other speak-
ers) to the amphitheater’s out-of-the-way protest area. The
complaint seeks, as a remedy, a declaration that the ordi-
nance infringes his (and other speakers’) First Amendment
                     Cite as: 607 U. S. ____ (2026)                     3

                          Opinion of the Court

rights and an injunction preventing city officials from en-
forcing the ordinance in the future.1 In other words, the
relief requested is only prospective; Olivier seeks neither
the reversal of, nor compensation for, his prior conviction.
And Olivier has since made clear that he has no interest in
using a favorable judgment in this suit to later get his rec-
ord expunged or avoid his conviction’s collateral effects. See
Tr. of Oral Arg. 7. The suit is just meant to ensure that
Olivier may return to the amphitheater to speak without
fear of further punishment.
  The parties contested in the lower courts whether this
Court’s decision in Heck v. Humphrey bars the suit from go-
ing forward. On the City’s view of Heck, a person previously
convicted of violating a statute cannot challenge its consti-
tutionality under §1983 because success in the suit would
cast doubt on the prior conviction’s correctness. On Oliv-
ier’s contrary view, that rule is subject to two limitations,
either of which enables his suit to proceed. First, Olivier
contended, Heck does not preclude a suit seeking wholly
prospective relief, rather than relief relating to the prior
conviction. And second, Olivier argued, Heck does not apply
(regardless of the relief sought) when the person suing was
never in custody for his conviction, so never had a chance to
challenge it in federal habeas proceedings.2
——————
  1 Originally, Olivier also sought damages for the City’s prior enforce-

ment of the ordinance against him. But he abandoned that request as
the suit progressed, leaving only the above-described pleas for declara-
tory and injunctive relief.
  2 The premise of Olivier’s second argument is, of course, that he had

not been in custody following his conviction. That premise appears to be
wrong. Under his sentence, Olivier served a year of probation—indeed,
was still serving that time when he filed this suit. And a person on pro-
bation is generally “ ‘in custody’ for purposes of federal habeas corpus.”
Minnesota v. Murphy, 465 U. S. 420, 430 (1984); see Jones v. Cunning-
ham, 371 U. S. 236, 241–243 (1963). For whatever reason, though, the
City failed to raise that objection below, and both lower courts accepted
that Olivier was not put in custody for his conviction. See 2022 WL
4                 OLIVIER v. CITY OF BRANDON

                         Opinion of the Court

   The District Court agreed with the City’s understanding
of Heck, and the Court of Appeals for the Fifth Circuit af-
firmed on the same reasoning. If Olivier’s §1983 suit suc-
ceeded, the District Court reasoned, the judgment would
“undermine his Municipal Court conviction.” 2022 WL
15047414, *11 (SD Miss., Sept. 23, 2022). And so the suit
was categorically barred under Heck. Similarly, the Fifth
Circuit viewed Heck as precluding any §1983 claim that, if
successful, would “necessarily imply the invalidity of the
plaintiff ’s criminal conviction.” 2023 WL 5500223, *1 (Aug.
25, 2023); see Heck, 512 U. S., at 487 (using near-identical
language). Olivier’s claim, the court maintained, was of
that sort: If he showed that the city ordinance violated the
First Amendment, he also would show that his prior convic-
tion should not have happened. And that fact, the court
concluded, was dispositive. It did not matter whether Oliv-
ier’s conviction had landed him in custody. See 2023 WL
5500223, *4. Nor did it matter whether Olivier’s suit
sought only prospective relief. See ibid.
   The Fifth Circuit denied rehearing en banc, but eight (of
seventeen) judges dissented. Those judges understood Heck
to bar only the “retrospective use of [§1983] to collaterally
attack criminal convictions.” 121 F. 4th 511, 514 (2024)
(Oldham, J., dissenting) (emphasis in original). A suit like
Olivier’s for “prospective injunctive relief,” the dissenters
argued, is not precluded because granting a “forward-
looking injunction” neither “invalidate[s]” nor “impose[s]
tort liability” for a prior conviction. Id., at 514–515; see id.,
at 513 (Ho, J., dissenting) (similar). The dissenters noted
that the Court of Appeals for the Ninth Circuit had adopted
their view, which meant there was now a Circuit split about

——————
15047414, *10 (SD Miss., Sept. 23, 2022); 2023 WL 5500223, *4 (CA5,
Aug. 25, 2023). Given that the case has proceeded so far on that basis,
we treat any contrary argument as forfeited and proceed in the same
way.
                     Cite as: 607 U. S. ____ (2026)                    5

                          Opinion of the Court

Heck’s proper reach. 121 F. 4th, at 515 (Oldham, J., dis-
senting) (citing Martin v. Boise, 920 F. 3d 584, 614 (2019)).
   We granted certiorari, 606 U. S. 959 (2025), to consider
the two independent reasons Olivier offered below for why
his suit escapes the so-called Heck bar: that he was never
in custody for his prior conviction, and that he now seeks
purely prospective relief. See Pet. for Cert. i. We need not
address the former reason today because we agree with
Olivier (and the Fifth Circuit’s dissenting judges) on the lat-
ter. Given that Olivier asked for only a forward-looking
remedy—an injunction stopping officials from enforcing the
city ordinance in the future—his suit can proceed, notwith-
standing his prior conviction.3 Heck, properly understood,
does not say otherwise.
                             II
  Before our decision in Heck, the City would have had no
plausible basis for claiming Olivier’s suit is barred. That
type of suit, as no one here disputes, falls within §1983’s
heartland: Assuming a credible threat of prosecution, a
plaintiff may bring a §1983 action to challenge a local law
as violating the Constitution and to prevent that law’s fu-
ture enforcement. See, e.g., Steffel v. Thompson, 415 U. S.
452 (1974). And a half-century ago, in Wooley v. Maynard,
430 U. S. 705 (1977), this Court held that rule to apply even
when the plaintiff (like Olivier) was previously convicted
under the challenged law.

——————
   3 In reaching that holding, we do not say that every person can chal-

lenge his statute of conviction through a §1983 suit for wholly prospec-
tive relief. The Government, appearing here as amicus curiae, urges us
to reserve the issue whether a person may bring such a suit while he is
in custody for violating the statute challenged. See Tr. of Oral Arg. 41–
42, 46–47; see also Brief for United States 27 (positing why that circum-
stance might matter). We think it appropriate to do so because, as we
have explained, our assumption here is that Olivier was never in custody.
See supra, at 3–4, n. 2.
6               OLIVIER v. CITY OF BRANDON

                      Opinion of the Court

   For anyone who has followed along this far, a description
of Wooley should strike a chord. George Maynard viewed
the “Live Free or Die” motto on his New Hampshire license
plate as “repugnant to [his] moral and religious beliefs.”
Id., at 707. So he covered those words with reflective tape,
in violation of a state statute. Maynard was convicted for
that conduct three times over in state court, receiving
(mostly suspended) sentences involving small fines and
short jail terms. After the last proceeding had concluded—
and presumably anxious that there not be a fourth—
Maynard brought a §1983 suit in federal court, seeking a
declaration that the state statute violated the First Amend-
ment and an injunction to prevent its future enforcement.
New Hampshire argued, as its front line of defense, that the
suit was precluded “because [Maynard] has already been
subjected to prosecution” under the challenged law. Id., at
712, n. 9. Our decision in Heck had not yet issued. Instead,
New Hampshire relied on “Younger principles,” which cau-
tion against federal interference with state-court proceed-
ings. Ibid.; see Younger v. Harris, 401 U. S. 37 (1971).
Those principles would be offended, New Hampshire
claimed, if a federal court were to enjoin the enforcement of
a state law at the behest of someone earlier convicted under
it in state court.
   This Court rejected New Hampshire’s argument on the
ground that Maynard’s suit sought only to prevent “further
prosecution” under the New Hampshire statute. Wooley,
430 U. S., at 711. The suit, the Court explained, was “in no
way designed to annul the results of a state trial” (as indeed
would have been troubling under Younger doctrine). 430
U. S., at 711. Maynard had “already sustained [his] convic-
tions” and “served [his] sentence[s].” Ibid. And he did “not
seek to have his record expunged, or to annul any collateral
effects” his convictions might have—for example, “upon his
driving privileges.” Ibid. Rather, Maynard sought “wholly
prospective” relief: He wanted “only to be free from
                  Cite as: 607 U. S. ____ (2026)            7

                      Opinion of the Court

prosecutions for future violations of the same” (allegedly
unconstitutional) statute. Ibid. Because that was so, the
Court held, §1983 provided an avenue to bring his claim.
See id., at 710. Were it otherwise, the Court reasoned,
Maynard would have no good way to vindicate his First
Amendment rights: He would be trapped “between the
Scylla of intentionally flouting state law and the Charybdis
of forgoing what he believes to be constitutionally protected
activity” so as to avoid yet another criminal prosecution.
Ibid.
   All of that could as easily be said of Olivier’s suit. Like
Maynard, Olivier was convicted under the statute he now
alleges to violate the First Amendment. But also like
Maynard, Olivier did not seek in his §1983 suit to upset that
conviction, or even to avert its collateral effects. Rather,
Olivier sought “wholly prospective” relief—an injunction to
preclude “further prosecution” under the law he had earlier
broken. Id., at 711. If not able to bring such a suit, Olivier
would face the same untenable choice as Maynard: violate
the law and suffer the consequences (the Scylla), or else give
up what he takes to be his First Amendment rights (the
Charybdis). See id., at 710. Our decision in Wooley, taken
alone, would thus defeat the City’s attempt to prevent Oliv-
ier’s suit from going forward.
   Some two decades later, though, the Court encountered
Heck v. Humphrey, which the City now argues requires the
opposite result. Roy Heck had been convicted in state court
of manslaughter, and was serving a fifteen-year prison sen-
tence. While his appeal was pending, he filed a §1983 suit
in federal court naming two prosecutors and a police inves-
tigator as defendants. Heck alleged that they had commit-
ted misconduct, such as destroying exculpatory evidence, to
gain his conviction. He sought as a remedy monetary “dam-
ages attributable to [his] unconstitutional conviction.” 512
U. S., at 489–490. The question raised was whether §1983
allowed the suit.
8               OLIVIER v. CITY OF BRANDON

                      Opinion of the Court

   The Court held it did not. The Court took as settled that
Heck could not have used §1983 to “challenge[ ] the fact or
duration of his confinement and seek[ ] immediate or speed-
ier release” from custody. Id., at 481 (citing Preiser v. Ro-
driguez, 411 U. S. 475, 488–490 (1973)). A claim of that
sort, the Court noted, “must be brought in habeas corpus
proceedings.” Heck, 512 U. S., at 481. And so too, the Court
held, Heck could not use §1983 to seek damages deriving
from a conviction, unless it had already been overturned.
See id., at 486–487. To be sure, Heck could not get damages
by way of a habeas action. See id., at 481. But in suing for
them under §1983, Heck was in truth mounting a “collat-
eral attack” on the validity of his conviction, and thus in-
truding on the habeas statute’s domain. Id., at 485. Such
a suit could lead to “parallel litigation” respecting “the is-
sues of probable cause and guilt.” Id., at 484. And it could
give rise to “conflicting” judgments about the same conduct,
with the §1983 suit suggesting that Heck should be re-
leased even as criminal or habeas proceedings found the op-
posite. Ibid. Hence the Heck bar on “§1983 damages ac-
tions that necessarily require the plaintiff to prove the
unlawfulness of his conviction or confinement.” Id., at 486.
“[W]hen a state prisoner seeks damages in a §1983 suit,”
the Court went on, “the district court must consider
whether a judgment in favor of the plaintiff would neces-
sarily imply the invalidity of his conviction or sentence.”
Id., at 487. A judgment for Heck would have done so, for
his success rested on proof discrediting his conviction. His
§1983 suit therefore could not go forward.
   In two later decisions, though, the Court drew a line be-
tween Heck-type claims and those seeking forward-looking
relief. In Edwards v. Balisok, 520 U. S. 641 (1997), a state
prisoner alleged that procedures used in a disciplinary
hearing—which had deprived him of good-time credits and
thus lengthened his sentence—violated his Fourteenth
Amendment due process rights. He sought money damages
                  Cite as: 607 U. S. ____ (2026)              9

                      Opinion of the Court

for the alleged past violation; he also sought an injunction
requiring prison officials to adopt new procedures, so as to
“prevent future violations.” Id., at 643. The Court made
short work of the claim for damages. As in Heck, the Court
reasoned, the prisoner could not obtain damages without
demonstrating “the invalidity of the punishment imposed”
on him (i.e., the loss of his good-time credits), and thus im-
pinging on habeas. 520 U. S., at 648. But the claim for
“prospective injunctive relief ”—the use of fairer procedures
in the future—was a different thing. Said the Court: “Or-
dinarily, a prayer for such prospective relief ” may “properly
be brought under §1983,” because it does not depend on
showing the “invalidity of a previous” sentencing decision.
Ibid. Likewise, in Wilkinson v. Dotson, 544 U. S. 74, 77
(2005), the Court allowed state prisoners to bring a §1983
suit alleging that existing parole procedures violated the
Due Process Clause and requesting an injunction that the
State “comply with constitutional” requirements “in the fu-
ture.” That claim for “future relief,” the Court determined,
was “distant” from “the core of habeas” and so not barred by
Heck. 544 U. S., at 82 (emphasis in original).
   The same is true of Olivier’s suit. Olivier is not challeng-
ing the “validity of [his] conviction or sentence,” for the pur-
pose either of securing (or speeding) release or of obtaining
monetary damages. Nance v. Ward, 597 U. S. 159, 167–168
(2022). Instead, Olivier is seeking (in Wooley’s words)
“wholly prospective” relief—“only to be free from prosecu-
tions for future violations” of the city ordinance. 430 U. S.,
at 711. And that request, as Balisok and Dotson recognized,
falls outside habeas’s core—and likewise outside Heck’s
concerns. See 520 U. S., at 648; 544 U. S., at 82. Olivier’s
suit does not, as habeas suits do, “collateral[ly] attack” the
old conviction. Heck, 512 U. S., at 485. It thus cannot give
rise, as Heck feared, to “parallel litigation” respecting his
prior conduct. Id., at 484. Nor does it risk “conflicting”
judgments over how that conduct was prosecuted or
10              OLIVIER v. CITY OF BRANDON

                      Opinion of the Court

punished. Ibid. The suit, after all, is not about what Olivier
did in the past, and depends on no proof addressed to his
prior conviction. Unlike in Heck, the suit merely attempts
to prevent a future prosecution. So the Heck bar does not
come into play.
  The City’s main argument to the contrary (echoing the
decisions below) rests on one sentence of our Heck opinion.
That supposedly dispositive line states: “[W]hen a state
prisoner seeks damages in a §1983 suit, the district court
must consider whether a judgment in favor of the plaintiff
would necessarily imply the invalidity of his conviction or
sentence; if it would, the complaint must be dismissed” (un-
less the conviction has already been invalidated). Id., at
487; see supra, at 8. Of course, Olivier does not “seek[ ]
damages” in his §1983 suit, but the City points out that sev-
eral post-Heck decisions dropped the sentence’s prefatory
phrase while repeating the rest. See, e.g., Dotson, 544 U. S.,
at 81–82; Skinner v. Switzer, 562 U. S. 521, 533–534 (2011).
And in the City’s view, that modified inquiry suggests that
the Heck bar should apply to Olivier’s suit. That is because,
the City says, a judgment in Olivier’s favor would “neces-
sarily imply the invalidity of [his] prior conviction[ ].” Brief
for Respondent 33. To declare the city ordinance unconsti-
tutional, as Olivier seeks, would be to imply that no one—
including Olivier—should have been convicted under that
law.
  The argument is a fair one, but hardly dispositive. We
have to agree that if Olivier succeeds in this suit, it would
mean his prior conviction was unconstitutional. So, strictly
speaking, the Heck language fits. But that could just show
that the phrasing was not quite as tailored as it should have
been. This Court has often cautioned that “general lan-
guage in judicial opinions should be read as referring in
context to circumstances similar to the circumstances then
before the Court and not referring to quite different circum-
stances that the Court was not then considering.” Turkiye
                  Cite as: 607 U. S. ____ (2026)           11

                      Opinion of the Court

Halk Bankasi A.S. v. United States, 598 U. S. 264, 278
(2023) (quoting Illinois v. Lidster, 540 U. S. 419, 424
(2004)). The City’s argument raises the question whether
that is true here.
   We think, with the benefit of hindsight, that it is—that
the sentence relied on swept a bit too broad. That language
was used in Heck to identify claims that were really as-
saults on a prior conviction, even though involving some in-
direction. One example was found in Heck itself: a claim
seeking not straightforward reversal of a conviction (and
release from custody), but damages attributable to that con-
viction, requiring proof that police misconduct made it in-
valid. Another example Heck offered was yet further atten-
uated. See 512 U. S., at 486–487, n. 6. A person convicted
of resisting arrest—defined as preventing an officer from
effecting a lawful arrest—brings a §1983 action for dam-
ages against the arresting officer for violation of his Fourth
Amendment right not to be unreasonably seized. The dam-
ages sought, unlike in Heck, are not attributable to his con-
viction (for resisting arrest); they are damages deriving only
from the underlying arrest. Still, a “§1983 action will not
lie” because the plaintiff, to prevail, “would have to negate
an element of the offense of which he has been convicted”—
i.e., that the underlying arrest was “lawful.” Ibid. Once
again, the suit requires looking back to conduct involved in
a prior conviction, and offering contradictory proof. By con-
trast, there is no looking back in Olivier’s suit. Both in the
allegations made, and in the relief sought, the suit is all
future-oriented—even if, as a kind of byproduct, success in
it shows that something past should not have occurred. The
Heck Court did not consider such a suit, and the Heck lan-
guage was not meant to address it.
   Proof positive comes from the logical—but wholly unten-
able—consequences of the City’s position. Suppose that af-
ter Olivier’s conviction, another citizen brings a §1983 suit
to enjoin the city ordinance so that he can speak outside the
12              OLIVIER v. CITY OF BRANDON

                      Opinion of the Court

amphitheater. Let’s name this citizen Laurence and say
that he boasts a clean police record. Would Heck allow Lau-
rence’s suit to proceed? See 121 F. 4th, at 514 (Oldham, J.,
dissenting) (offering a similar hypothetical). The very ques-
tion seems ludicrous: No one would say Heck poses a bar.
But under the City’s logic, it should—because here, too,
Heck’s language fits. The hypothetical suit—no less than
Olivier’s own—would, if successful, “necessarily imply the
invalidity” of Olivier’s conviction (as well as all other con-
victions under the statute). 512 U. S., at 487. A judgment
in that suit too would demonstrate, and in just the same
way, that Olivier’s conviction was unconstitutional. The
hypothetical thus shows that the “necessarily imply” lan-
guage cannot extend as far as the City wants. Contra the
City’s logic, the Heck language does not preclude Laurence’s
§1983 suit because, rather than challenging a prior convic-
tion, that suit only attempts to prevent future ones. And
contra the City’s actual position, the language does not pre-
clude Olivier’s §1983 suit for the identical reason—because,
as explained above, it looks forward only. See supra, at 9–
10.
   With Heck thus out of the way, Wooley returns to center
stage. Recall the Court held in that case that Maynard
could sue under §1983 to prevent future enforcement of an
allegedly unconstitutional statute, despite a prior convic-
tion under that law. See supra, at 6–7. The same rule al-
lows Olivier to sue under §1983 to enjoin future prosecu-
tions under the city ordinance, despite his prior conviction.
Were that not so, Olivier would face the same dilemma as
Maynard: flout the law and risk another prosecution, or else
forgo speech he believes is constitutionally protected. See
Wooley, 430 U. S., at 710; supra, at 7. We declined to put
Maynard to that choice, and we will not put Olivier to it
either. His suit to enjoin the ordinance, so he can return to
the amphitheater, may proceed.
                Cite as: 607 U. S. ____ (2026)                 13

                    Opinion of the Court

  We accordingly reverse the judgment of the Court of Ap-
peals and remand the case for further proceedings con-
sistent with this opinion.
                                                 It is so ordered.

```

---

## GROUP: _overhaul2/lake/cases/Olmstead v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Olmstead v. United States"
type: case
citation: "277 U.S. 438 (1928)"
parallel_cite: "48 S. Ct. 564; 72 L. Ed. 944; 66 A.L.R. 376"
neutral_cite: 1928 U.S. LEXIS 694
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1928
date_decided: 1928-06-04
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: superseded
  as_of_content: 1928-06-04
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Olmstead v. United States
  varies_by_point: false
  scope_note: "Overruled on the privacy point by Katz v. United States (1967); survives only as history. The property-trespass approach was later revived as an alternative test in United States v. Jones (2012)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/101320/olmstead-v-united-states/"
  cluster_id: 101320
  opinion_id: 101320
  identity_checked: true
homes:
  - page: "[[Trespass]]"
    role: "Historical / origin"
  - page: "[[Electronic Surveillance and Title III]]"
    role: "Key — Historical (overruled by Katz)"
related: ["[[Katz v. United States]]", "[[United States v. Jones]]", "[[Berger v. New York]]"]
aliases: []
tags: ["case", "fourth-amendment", "wiretap", "trespass", "overruled", "historical"]
holding: "Wiretapping with no physical entry was not a search — pure property/trespass framing; overruled on the privacy point by *Katz* (property instinct later revived by *Jones*)."
lake:
  record_id: Olmstead v. United States
  status: verified
  projected_at: 2026-07-09
---

# Olmstead v. United States

*277 U.S. 438 (1928)* · U.S. Supreme Court · **Historical** · Treatment: **overruled** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal Prohibition agents gathered evidence against a large bootlegging operation by wiretapping the defendants' telephone lines. The taps were placed on wires in the streets and in the basement of the building — without any physical trespass into the defendants' homes or offices.

## Issue
Whether wiretapping a person's telephone conversations, accomplished without physical entry into a constitutionally protected area, is a "search and seizure" within the Fourth Amendment.

## Rule
*(Historical — this holding has been overruled; see Treatment.)* The Court tied Fourth Amendment protection to physical trespass and tangible things: "The Amendment itself shows that the search is to be of material things — the person, the house, his papers or his effects." — 277 U.S. at 464. ^pin-464

Because the wiretaps involved no physical entry, the Court held there was no search or seizure: "There was no searching. There was no seizure. The evidence was secured by the use of the sense of hearing and that only." — [*Id.*](https://www.courtlistener.com/opinion/101320/olmstead-v-united-states/#:~:text=There%20was%20no%20searching.%20There) ^pin-464b

## Application
Because the wiretaps involved no physical entry into the defendants' premises and seized no tangible "material things" — only overheard conversations — the Court held there had been no search or seizure, and the wiretap evidence was admissible against Olmstead.

## Conclusion
On these facts the warrantless wiretapping was held not to be a Fourth Amendment search, and the convictions were affirmed. *(This holding no longer states the law — see Treatment.)*

## Treatment & subsequent history
- **Status:** overruled *(as of 2026-06-30)* — **Historical**.
- **Overruled by [[Katz v. United States]] (1967)**, which rejected *Olmstead*'s trespass and "material things" framing and held that the Fourth Amendment protects people, not places, so that a warrantless wiretap of a telephone conversation is a search. The property-trespass approach *Olmstead* embodied was later partially revived as an alternative test in [[United States v. Jones]] (2012), but *Olmstead*'s holding that wiretapping is not a search remains overruled.

## Appears on
- [[Trespass]] — *Historical / origin*
- [[Electronic Surveillance and Title III]] — *Key — Historical (overruled by Katz)*

## Sources
- *Olmstead v. United States*, 277 U.S. 438 (1928) — https://www.courtlistener.com/opinion/101320/olmstead-v-united-states/ — pinpoint: 464.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8f0014cec35d894f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Olmstead v. United States"}, "payload": {"all": [{"cite": "277 U.S. 438", "page": "438", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "277"}, {"cite": "48 S. Ct. 564", "page": "564", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "48"}, {"cite": "72 L. Ed. 944", "page": "944", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "72"}, {"cite": "1928 U.S. LEXIS 694", "page": "694", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1928"}, {"cite": "66 A.L.R. 376", "page": "376", "reporter": "A.L.R.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "66"}], "display": "277 U.S. 438", "official": {"cite": "277 U.S. 438", "page": "438", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "277"}, "official_selection_present": true, "record_id": "Olmstead v. United States"}}
{"assertion_id": "7b49e527492026b3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-464", "record_id": "Olmstead v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-464", "pinpoint_status": "slip-only", "quote": "within the Fourth Amendment. ## Rule *(Historical — this holding has been overruled; see Treatment.)* The Court tied Fourth Amendment protection to physical trespass and tangible things:", "quote_fidelity": "mismatch", "record_id": "Olmstead v. United States", "star_marker": null}}
{"assertion_id": "a9f4933be830080d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-464b", "record_id": "Olmstead v. United States"}, "payload": {"fragment": "#:~:text=There%20was%20no%20searching.%20There", "page": null, "pin_id": "pin-464b", "pinpoint_status": "star-verified", "quote": "There was no searching. There was no seizure. The evidence was secured by the use of the sense of hearing and that only.", "quote_fidelity": "matched", "record_id": "Olmstead v. United States", "star_marker": "464"}}
{"assertion_id": "dae9a04461320ed6", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Olmstead v. United States"}, "payload": {"as_of_content": "1928-06-04", "as_of_treatment": "2026-06-30", "field_i_validity": "superseded", "record_id": "Olmstead v. United States", "scope_note": "Overruled on the privacy point by Katz v. United States (1967); survives only as history. The property-trespass approach was later revived as an alternative test in United States v. Jones (2012).", "varies_by_point": false}}
```

### lake record — Olmstead v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Olmstead v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Olmstead v. United States",
    "case_name_short": "Olmstead",
    "case_name_full": "OLMSTEAD Et Al. v. UNITED STATES; GREEN Et Al. v. SAME; McINNIS v. SAME",
    "input_case_name": "Olmstead v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1928-06-04",
    "year": 1928,
    "docket": null,
    "cluster_id": 101320,
    "lead_opinion_id": 101320,
    "sibling_ids": [
      101320,
      9418652,
      9418653,
      9418654,
      9418655,
      9418656
    ],
    "absolute_url": "/opinion/101320/olmstead-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "277 U.S. 438",
      "volume": "277",
      "reporter": "U.S.",
      "page": "438",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "48 S. Ct. 564",
        "volume": "48",
        "reporter": "S. Ct.",
        "page": "564",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 L. Ed. 944",
        "volume": "72",
        "reporter": "L. Ed.",
        "page": "944",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "66 A.L.R. 376",
        "volume": "66",
        "reporter": "A.L.R.",
        "page": "376",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1928 U.S. LEXIS 694",
        "volume": "1928",
        "reporter": "U.S. LEXIS",
        "page": "694",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "277 U.S. 438",
        "volume": "277",
        "reporter": "U.S.",
        "page": "438",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "48 S. Ct. 564",
        "volume": "48",
        "reporter": "S. Ct.",
        "page": "564",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 L. Ed. 944",
        "volume": "72",
        "reporter": "L. Ed.",
        "page": "944",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1928 U.S. LEXIS 694",
        "volume": "1928",
        "reporter": "U.S. LEXIS",
        "page": "694",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "66 A.L.R. 376",
        "volume": "66",
        "reporter": "A.L.R.",
        "page": "376",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "277 U.S. 438",
    "official_selection": {
      "court_class": "scotus",
      "selected": "277 U.S. 438",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-464",
      "page": null,
      "quote": "within the Fourth Amendment. ## Rule *(Historical \u2014 this holding has been overruled; see Treatment.)* The Court tied Fourth Amendment protection to physical trespass and tangible things:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-464b",
      "page": null,
      "quote": "There was no searching. There was no seizure. The evidence was secured by the use of the sense of hearing and that only.",
      "star_marker": "464",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 22716,
      "fragment": "#:~:text=There%20was%20no%20searching.%20There",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "superseded",
    "as_of_content": "1928-06-04",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Olmstead v. United States",
    "varies_by_point": false,
    "scope_note": "Overruled on the privacy point by Katz v. United States (1967); survives only as history. The property-trespass approach was later revived as an alternative test in United States v. Jones (2012).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Katz v. United States",
          "cluster_id": 107564,
          "cite": "389 U.S. 347",
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:overruled"
      },
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 10705828,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andrew Lennette, Individually and on behalf of C.L., O.L. and S.L., Minor Children v. State of Iowa, Melody Siver, Amy Howell, and Valerie Lovaglia",
          "cluster_id": 6476611,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Isaac Andrew Baldon III",
          "cluster_id": 4472245,
          "cite": [
            "829 N.W.2d 785",
            "2013 WL 1694553",
            "2013 Iowa Sup. LEXIS 42"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Henderson",
          "cluster_id": 8714803,
          "cite": [
            "857 F. Supp. 2d 191",
            "2012 WL 1432552",
            "2012 U.S. Dist. LEXIS 57729"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Rabb",
          "cluster_id": 5640827,
          "cite": [
            "16 N.Y.3d 145",
            "945 N.E.2d 447"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mason v. State",
          "cluster_id": 2167970,
          "cite": [
            "290 S.W.3d 498",
            "2009 WL 1563551"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Scattaretico v. Puglisi",
          "cluster_id": 6587685,
          "cite": [
            "60 Mass. App. Ct. 138",
            "799 N.E.2d 1258"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hernandez v. State",
          "cluster_id": 1882057,
          "cite": [
            "60 S.W.3d 106",
            "2001 Tex. Crim. App. LEXIS 104",
            "2001 WL 1415274"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Miranda v. Arizona",
          "cluster_id": 107252,
          "cite": [
            "16 L. Ed. 2d 694",
            "86 S. Ct. 1602",
            "384 U.S. 436",
            "1966 U.S. LEXIS 2817",
            "10 Ohio Misc. 9",
            "36 Ohio Op. 2d 237",
            "10 A.L.R. 3d 974"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
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
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mapp v. Ohio",
          "cluster_id": 106285,
          "cite": [
            "6 L. Ed. 2d 1081",
            "81 S. Ct. 1684",
            "367 U.S. 643",
            "1961 U.S. LEXIS 812"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
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
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Citizens United v. Federal Election Commission",
          "cluster_id": 1741,
          "cite": [
            "175 L. Ed. 2d 753",
            "130 S. Ct. 876",
            "558 U.S. 310",
            "2010 U.S. LEXIS 766",
            "22 Fla. L. Weekly Fed. S 73",
            "78 U.S.L.W. 4078",
            "187 L.R.R.M. (BNA) 2961",
            "159 Lab. Cas. (CCH) 10,166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herring v. United States",
          "cluster_id": 145922,
          "cite": [
            "172 L. Ed. 2d 496",
            "129 S. Ct. 695",
            "555 U.S. 135",
            "2009 U.S. LEXIS 581"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Devereaux v. Abbey",
          "cluster_id": 7099058,
          "cite": [
            "263 F.3d 1070",
            "2001 Daily Journal DAR 9669",
            "2001 Cal. Daily Op. Serv. 7797",
            "2001 U.S. App. LEXIS 19674",
            "2001 WL 1008128"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Edmunds",
          "cluster_id": 2316698,
          "cite": [
            "586 A.2d 887",
            "526 Pa. 374",
            "1991 Pa. LEXIS 28"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe v. Poritz",
          "cluster_id": 1473573,
          "cite": [
            "662 A.2d 367",
            "142 N.J. 1",
            "36 A.L.R. 5th 711",
            "1995 N.J. LEXIS 519"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Retherford",
          "cluster_id": 4001886,
          "cite": [
            "639 N.E.2d 498",
            "93 Ohio App. 3d 586",
            "1994 Ohio App. LEXIS 1066"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Howard",
          "cluster_id": 5684310,
          "cite": [
            "50 N.Y.2d 583",
            "408 N.E.2d 908",
            "430 N.Y.S.2d 578",
            "1980 N.Y. LEXIS 2454"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cahan",
          "cluster_id": 1237532,
          "cite": [
            "282 P.2d 905",
            "44 Cal. 2d 434",
            "50 A.L.R. 2d 513",
            "1955 Cal. LEXIS 243"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 104313,
          "cite": [
            "328 U.S. 582",
            "66 S. Ct. 1256",
            "90 L. Ed. 1453",
            "1946 U.S. LEXIS 2180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hill v. National Collegiate Athletic Assn.",
          "cluster_id": 1235436,
          "cite": [
            "865 P.2d 633",
            "7 Cal. 4th 1",
            "26 Cal. Rptr. 2d 834",
            "94 Cal. Daily Op. Serv. 681",
            "94 Daily Journal DAR 1141",
            "9 I.E.R. Cas. (BNA) 716",
            "1994 Cal. LEXIS 9"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 1676406,
          "cite": [
            "912 S.W.2d 227",
            "1995 Tex. Crim. App. LEXIS 115",
            "1995 WL 675559"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fare v. Tony C.",
          "cluster_id": 1386533,
          "cite": [
            "582 P.2d 957",
            "21 Cal. 3d 888",
            "148 Cal. Rptr. 366",
            "1978 Cal. LEXIS 269"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCambridge v. City of Little Rock",
          "cluster_id": 1495689,
          "cite": [
            "766 S.W.2d 909",
            "298 Ark. 219",
            "16 Media L. Rep. (BNA) 1593",
            "1989 Ark. LEXIS 112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Owens",
          "cluster_id": 1227976,
          "cite": [
            "729 P.2d 524",
            "302 Or. 196",
            "1986 Ore. LEXIS 1790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Riser",
          "cluster_id": 1148989,
          "cite": [
            "47 Cal. 2d 566",
            "305 P.2d 1",
            "1956 Cal. LEXIS 302"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. May",
          "cluster_id": 5691156,
          "cite": [
            "81 N.Y.2d 725",
            "609 N.E.2d 113",
            "593 N.Y.S.2d 760",
            "1992 N.Y. LEXIS 4219"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "UNITED STATES of America v. WESTINGHOUSE ELECTRIC CORPORATION, Appellant",
          "cluster_id": 386024,
          "cite": [
            "638 F.2d 570",
            "8 BNA OSHC 2131",
            "8 OSHC (BNA) 2131",
            "1980 U.S. App. LEXIS 12983"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dennis",
          "cluster_id": 225410,
          "cite": [
            "183 F.2d 201"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ashish Patel, Anverali Satani, Nazira Momin, Minaz Chamadia, and Vijay Lakshmi Yogi v. Texas Department of Licensing and Regulation",
          "cluster_id": 2831518,
          "cite": [
            "469 S.W.3d 69",
            "58 Tex. Sup. Ct. J. 1298",
            "2015 Tex. LEXIS 617",
            "2015 WL 3982687"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCORMICK v. CARRIER",
          "cluster_id": 830367,
          "cite": [
            "487 Mich. 180",
            "795 N.W.2d 517"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. White",
          "cluster_id": 1194272,
          "cite": [
            "640 P.2d 1061",
            "97 Wash. 2d 92",
            "1982 Wash. LEXIS 1262"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Olmstead v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(101320 OR 9418652 OR 9418653 OR 9418654 OR 9418655 OR 9418656) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05OTc5MjAwMDAwMDAmcz0yMzg2MzMxJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28101320+OR+9418652+OR+9418653+OR+9418654+OR+9418655+OR+9418656%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(101320 OR 9418652 OR 9418653 OR 9418654 OR 9418655 OR 9418656)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMzgmcz0zNzQ3MTYmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28101320+OR+9418652+OR+9418653+OR+9418654+OR+9418655+OR+9418656%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(101320 OR 9418652 OR 9418653 OR 9418654 OR 9418655 OR 9418656)",
        "reviewed": 19,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 19,
        "triage_read": 1,
        "triage_snippet_classified": 18
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(101320 OR 9418652 OR 9418653 OR 9418654 OR 9418655 OR 9418656)",
    "indexed_citing_opinions": 1206,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 101320,
        "count": 1092,
        "count_source": "search"
      },
      {
        "opinion_id": 9418652,
        "count": 157,
        "count_source": "search"
      },
      {
        "opinion_id": 9418653,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9418654,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9418655,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9418656,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2291,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/olmstead-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc5MDA1NDImcz03ODYwNjEyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28101320+OR+9418652+OR+9418653+OR+9418654+OR+9418655+OR+9418656%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 101320,
        "cited_id": 84759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 84810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 87533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 87601,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 87628,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 87951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 88038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 88341,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 88397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 88700,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 89027,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 89664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 90098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 90320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 91053,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 91577,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 92439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 92483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 92547,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 92567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 92798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 93318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 93322,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 93392,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 93951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 95090,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 95218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 95873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 96460,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 96812,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 97242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 98638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99248,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99406,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 99914,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100934,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 101076,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 101118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 101177,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 101180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 101214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 3543071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101320,
        "cited_id": 4732864,
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
    "date_created": "2026-07-05T16:11:49Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: overruled -> superseded",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:11:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:11:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:11:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Olmstead v. United States

```
<div>
<center><b><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U.S. 438</a></span> (1928)</b></center>
<center><h1>OLMSTEAD ET AL.<br>
v.<br>
UNITED STATES.<br>
GREEN ET AL.<br>
v.<br>
SAME.<br>
McINNIS<br>
v.<br>
SAME.</h1></center>
<center>Nos. 493, 532 and 533.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 20, 21, 1928.</center>
<center>Decided June 4, 1928.</center>
CERTIORARI TO THE CIRCUIT COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><span class="star-pagination">*439</span> <i>Mr. John F. Dore,</i> with whom <i>Messrs. F.C. Reagan</i> and <i>J.L. Finch</i> were on the brief, for petitioners in No. 493.</p>
<p><i>Mr. Frank R. Jeffery,</i> for petitioner in No. 533, and some of the petitioners in No. 532.</p>
<p><i>Messrs. Arthur E. Griffin, George F. Vanderveer,</i> and <i>Samuel B. Bassett,</i> on a brief for petitioners in No. 532.</p>
<p><i>Mr. Michael J. Doherty,</i> Special Assistant to the Attorney General, with whom <i>Solicitor General Mitchell</i> was on the brief, for the United States.</p>
<p><i>Messrs. Otto B. Rupp, Charles M. Bracelen, Robert H. Strahan,</i> and <i>Clarence B. Randall</i> on behalf of The Pacific Telephone and Telegraph Company, American Telephone and Telegraph Company, United States Independent Telephone Association, and the Tri-State Telephone and Telegraph Company, as <i>amici curiae,</i> filed a brief by special leave of Court.</p>
<p><span class="star-pagination">*455</span> MR. CHIEF JUSTICE TAFT delivered the opinion of the Court.</p>
<p>These cases are here by certiorari from the Circuit Court of Appeals for the Ninth Circuit. 19 F. (2d) 842 and 850. The petition in No. 493 was filed August 30, 1927; in Nos. 532 and 533, September 9, 1927. They were granted with the distinct limitation that the hearing should be confined to the single question whether the use of evidence of private telephone conversations between the defendants and others, intercepted by means of wire tapping, amounted to a violation of the Fourth and Fifth Amendments.</p>
<p>The petitioners were convicted in the District Court for the Western District of Washington of a conspiracy to violate the National Prohibition Act by unlawfully possessing, transporting and importing intoxicating liquors and maintaining nuisances, and by selling intoxicating liquors. Seventy-two others in addition to the petitioners were indicted. Some were not apprehended, some were acquitted and others pleaded guilty.</p>
<p>The evidence in the records discloses a conspiracy of amazing magnitude to import, possess and sell liquor unlawfully. <span class="star-pagination">*456</span> It involved the employment of not less than fifty persons, of two seagoing vessels for the transportation of liquor to British Columbia, of smaller vessels for coastwise transportation to the State of Washington, the purchase and use of a ranch beyond the suburban limits of Seattle, with a large underground cache for storage and a number of smaller caches in that city, the maintenance of a central office manned with operators, the employment of executives, salesmen, deliverymen, dispatchers, scouts, bookkeepers, collectors and an attorney. In a bad month sales amounted to $176,000; the aggregate for a year must have exceeded two millions of dollars.</p>
<p>Olmstead was the leading conspirator and the general manager of the business. He made a contribution of $10,000 to the capital; eleven others contributed $1,000 each. The profits were divided one-half to Olmstead and the remainder to the other eleven. Of the several offices in Seattle the chief one was in a large office building. In this there were three telephones on three different lines. There were telephones in an office of the manager in his own home, at the homes of his associates, and at other places in the city. Communication was had frequently with Vancouver, British Columbia. Times were fixed for the deliveries of the "stuff," to places along Puget Sound near Seattle and from there the liquor was removed and deposited in the caches already referred to. One of the chief men was always on duty at the main office to receive orders by telephones and to direct their filling by a corps of men stationed in another room  the "bull pen." The call numbers of the telephones were given to those known to be likely customers. At times the sales amounted to 200 cases of liquor per day.</p>
<p>The information which led to the discovery of the conspiracy and its nature and extent was largely obtained by intercepting messages on the telephones of the conspirators by four federal prohibition officers. Small <span class="star-pagination">*457</span> wires were inserted along the ordinary telephone wires from the residences of four of the petitioners and those leading from the chief office. The insertions were made without trespass upon any property of the defendants. They were made in the basement of the large office building. The taps from house lines were made in the streets near the houses.</p>
<p>The gathering of evidence continued for many months. Conversations of the conspirators of which refreshing stenographic notes were currently made, were testified to by the government witnesses. They revealed the large business transactions of the partners and their subordinates. Men at the wires heard the orders given for liquor by customers and the acceptances; they became auditors of the conversations between the partners. All this disclosed the conspiracy charged in the indictment. Many of the intercepted conversations were not merely reports but parts of the criminal acts. The evidence also disclosed the difficulties to which the conspirators were subjected, the reported news of the capture of vessels, the arrest of their men and the seizure of cases of liquor in garages and other places. It showed the dealing by Olmstead, the chief conspirator, with members of the Seattle police, the messages to them which secured the release of arrested members of the conspiracy, and also direct promises to officers of payments as soon as opportunity offered.</p>
<p>The Fourth Amendment provides  "The right of the people to be secure in their persons, houses, papers, and effects against unreasonable searches and seizures shall not be violated; and no warrants shall issue but upon probable cause, supported by oath or affirmation and particularly describing the place to be searched and the persons or things to be seized." And the Fifth: "No person . . . shall be compelled, in any criminal case, to be a witness against himself."</p>
<p><span class="star-pagination">*458</span> It will be helpful to consider the chief cases in this Court which bear upon the construction of these Amendments.</p>
<p><i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U.S. 616</a></span>, was an information filed by the District Attorney in the federal court in a cause of seizure and forfeiture against thirty-five cases of plate glass, which charged that the owner and importer, with intent to defraud the revenue, made an entry of the imported merchandise by means of a fraudulent or false invoice. It became important to show the quantity and value of glass contained in twenty-nine cases previously imported. The fifth section of the Act of June 22, 1874, provided that in cases not criminal under the revenue laws, the United States Attorney, whenever he thought an invoice, belonging to the defendant, would tend to prove any allegation made by the United States, might by a written motion describing the invoice and setting forth the allegation which he expected to prove, secure a notice from the court to the defendant to produce the invoice, and if the defendant refused to produce it, the allegations stated in the motion should be taken as confessed, but if produced, the United States Attorney should be permitted, under the direction of the court, to make an examination of the invoice, and might offer the same in evidence. This Act had succeeded the Act of 1867, which provided that in such cases the District Judge, on affidavit of any person interested, might issue a warrant to the marshal to enter the premises where the invoice was and take possession of it and hold it subject to the order of the judge. This had been preceded by the Act of 1863 of a similar tenor, except that it directed the warrant to the collector instead of the marshal. The United States Attorney followed the Act of 1874 and compelled the production of the invoice.</p>
<p>The court held the Act of 1874 repugnant to the Fourth and Fifth Amendments. As to the Fourth Amendment, Justice Bradley said (page 621):</p>
<p><span class="star-pagination">*459</span> "But, in regard to the Fourth Amendment, it is contended that, whatever might have been alleged against the constitutionality of the acts of 1863 and 1867, that of 1874, under which the order in the present case was made, is free from constitutional objection because it does not authorize the search and seizure of books and papers, but only requires the defendant or claimant to produce them. That is so; but it declares that if he does not produce them, the allegations which it is affirmed they will prove shall be taken as confessed. This is tantamount to compelling their production; for the prosecuting attorney will always be sure to state the evidence expected to be derived from them as strongly as the case will admit of. It is true that certain aggravating incidents of actual search and seizure, such as forcible entry into a man's house and searching amongst his papers, are wanting, and to this extent the proceeding under the Act of 1874 is a mitigation of that which was authorized by the former acts; but it accomplishes the substantial object of those acts in forcing from a party evidence against himself. It is our opinion, therefore, that a compulsory production of a man's private papers to establish a criminal charge against him, or to forfeit his property, is within the scope of the Fourth Amendment to the Constitution, in all cases in which a search and seizure would be; because it is a material ingredient, and effects the sole object and purpose of search and seizure."</p>
<p>Concurring, Mr. Justice Miller and Chief Justice Waite said that they did not think the machinery used to get this evidence amounted to a search and seizure, but they agreed that the Fifth Amendment had been violated.</p>
<p>The statute provided an official demand for the production of a paper or document by the defendant for official search and use as evidence on penalty that by refusal he should be conclusively held to admit the incriminating <span class="star-pagination">*460</span> character of the document as charged. It was certainly no straining of the language to construe the search and seizure under the Fourth Amendment to include such official procedure.</p>
<p>The next case, and perhaps the most important, is <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U.S. 383</a></span>,  a conviction for using the mails to transmit coupons or tickets in a lottery enterprise. The defendant was arrested by a police officer without a warrant. After his arrest other police officers and the United States marshal went to his house, got the key from a neighbor, entered the defendant's room and searched it, and took possession of various papers and articles. Neither the marshal nor the police officers had a search warrant. The defendant filed a petition in court asking the return of all his property. The court ordered the return of everything not pertinent to the charge, but denied return of relevant evidence. After the jury was sworn, the defendant again made objection, and on introduction of the papers contended that the search without warrant was a violation of the Fourth and Fifth Amendments and they were therefore inadmissible. This court held that such taking of papers by an official of the United States, acting under color of his office, was in violation of the constitutional rights of the defendant, and upon making seasonable application he was entitled to have them restored, and that by permitting their use upon the trial, the trial court erred.</p>
<p>The opinion cited with approval language of Mr. Justice Field in <i>Ex parte Jackson,</i> <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U.S. 727, 733</a></span>, saying that the Fourth Amendment as a principle of protection was applicable to sealed letters and packages in the mail and that, consistently with it, such matter could only be opened and examined upon warrants issued on oath or affirmation particularly describing the thing to be seized.</p>
<p>In <i>Silverthorne Lumber Company</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U.S. 385</a></span>, the defendants were arrested at their homes and <span class="star-pagination">*461</span> detained in custody. While so detained, representatives of the Government without authority went to the office of their company and seized all the books, papers and documents found there. An application for return of the things was opposed by the District Attorney, who produced a subpoena for certain documents relating to the charge in the indictment then on file. The court said:</p>
<p>"Thus the case is not that of knowledge acquired through the wrongful act of a stranger, but it must be assumed that the Government planned or at all events ratified the whole performance."</p>
<p>And it held that the illegal character of the original seizure characterized the entire proceeding and under the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case the seized papers must be restored.</p>
<p>In <i>Amos</i> v. <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U.S. 313</a></span>, the defendant was convicted of concealing whiskey on which the tax had not been paid. At the trial he presented a petition asking that private property seized in a search of his house and store "within his curtilage," without warrant should be returned. This was denied. A woman, who claimed to be his wife, was told by the revenue officers that they had come to search the premises for violation of the revenue law. She opened the door; they entered and found whiskey. Further searches in the house disclosed more. It was held that this action constituted a violation of the Fourth Amendment, and that the denial of the motion to restore the whiskey and to exclude the testimony was error.</p>
<p>In <i>Gouled</i> v. <i>The United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>, the facts were these: Gouled and two others were charged with conspiracy to defraud the United States. One pleaded guilty and another was acquitted. Gouled prosecuted error. The matter was presented here on questions propounded by the lower court. The first related to the admission in evidence of a paper surreptitiously taken from the office of the defendant by one acting under the direction <span class="star-pagination">*462</span> of an officer of the Intelligence Department of the Army of the United States. Gouled was suspected of the crime. A private in the U.S. Army, pretending to make a friendly call on him, gained admission to his office and in his absence, without warrant of any character, seized and carried away several documents. One of these belonging to Gouled, was delivered to the United States Attorney and by him introduced in evidence. When produced, it was a surprise to the defendant. He had had no opportunity to make a previous motion to secure a return of it. The paper had no pecuniary value, but was relevant to the issue made on the trial. Admission of the paper was considered a violation of the Fourth Amendment.</p>
<p><i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U.S. 20</a></span>, held that the Fourth and Fifth Amendments were violated by admission in evidence of contraband narcotics found in defendant's house, several blocks distant from the place of arrest, after his arrest, and seized there without a warrant. Under such circumstances the seizure could not be justified as incidental to the arrest.</p>
<p>There is no room in the present case for applying the Fifth Amendment unless the Fourth Amendment was first violated. There was no evidence of compulsion to induce the defendants to talk over their many telephones. They were continually and voluntarily transacting business without knowledge of the interception. Our consideration must be confined to the Fourth Amendment.</p>
<p>The striking outcome of the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case and those which followed it was the sweeping declaration that the Fourth Amendment, although not referring to or limiting the use of evidence in courts, really forbade its introduction if obtained by government officers through a violation of the Amendment. Theretofore many had supposed that under the ordinary common law rules, if the tendered evidence was pertinent, the method of obtaining it was <span class="star-pagination">*463</span> unimportant. This was held by the Supreme Judicial Court of Massachusetts in <i>Commonwealth</i> v. <i>Dana,</i> 2 Metcalf, 329, 337. There it was ruled that the only remedy open to a defendant whose rights under a state constitutional equivalent of the Fourth Amendment had been invaded was by suit and judgment for damages, as Lord Camden held in <i>Entick</i> v. <i>Carrington,</i> 19 Howell State Trials, 1029. Mr. Justice Bradley made effective use of this case in <i>Boyd</i> v. <i>United States</i><i>.</i> But in the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case, and those which followed, this Court decided with great emphasis, and established as the law for the federal courts, that the protection of the Fourth Amendment would be much impaired unless it was held that not only was the official violator of the rights under the Amendment subject to action at the suit of the injured defendant, but also that the evidence thereby obtained could not be received.</p>
<p>The well known historical purpose of the Fourth Amendment, directed against general warrants and writs of assistance, was to prevent the use of governmental force to search a man's house, his person, his papers and his effects; and to prevent their seizure against his will. This phase of the misuse of governmental power of compulsion is the emphasis of the opinion of the Court in the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case. This appears too in the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case, in the <i>Silverthorne</i> case and in the <i><span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">Amos</a></span></i> case.</p>
<p><i>Gouled</i> v. <i>United States</i> carried the inhibition against unreasonable searches and seizures to the extreme limit. Its authority is not to be enlarged by implication and must be confined to the precise state of facts disclosed by the record. A representative of the Intelligence Department of the Army, having by stealth obtained admission to the defendant's office, seized and carried away certain private papers valuable for evidential purposes. This was held an unreasonable search and seizure within the Fourth Amendment. A stealthy entrance in such circumstances <span class="star-pagination">*464</span> became the equivalent to an entry by force. There was actual entrance into the private quarters of defendant and the taking away of something tangible. Here we have testimony only of voluntary conversations secretly overheard.</p>
<p>The Amendment itself shows that the search is to be of material things  the person, the house, his papers or his effects. The description of the warrant necessary to make the proceeding lawful, is that it must specify the place to be searched and the person or <i>things</i> to be seized.</p>
<p>It is urged that the language of Mr. Justice Field in <i>Ex parte Jackson,</i> already quoted, offers an analogy to the interpretation of the Fourth Amendment in respect of wire tapping. But the analogy fails. The Fourth Amendment may have proper application to a sealed letter in the mail because of the constitutional provision for the Postoffice Department and the relations between the Government and those who pay to secure protection of their sealed letters. See Revised Statutes, §§ 3978 to 3988, whereby Congress monopolizes the carriage of letters and excludes from that business everyone else, and § 3929 which forbids any postmaster or other person to open any letter not addressed to himself. It is plainly within the words of the Amendment to say that the unlawful rifling by a government agent of a sealed letter is a search and seizure of the sender's papers or effects. The letter is a paper, an effect, and in the custody of a Government that forbids carriage except under its protection.</p>
<p>The United States takes no such care of telegraph or telephone messages as of mailed sealed letters. The Amendment does not forbid what was done here. There was no searching. There was no seizure. The evidence was secured by the use of the sense of hearing and that only. There was no entry of the houses or offices of the defendants.</p>
<p><span class="star-pagination">*465</span> By the invention of the telephone, fifty years ago, and its application for the purpose of extending communications, one can talk with another at a far distant place. The language of the Amendment can not be extended and expanded to include telephone wires reaching to the whole world from the defendant's house or office. The intervening wires are not part of his house or office any more than are the highways along which they are stretched.</p>
<p>This Court in <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#149" aria-description="Citation for case: Carroll v. United States">267 U.S. 132, 149</a></span>, declared:</p>
<p>"The Fourth Amendment is to be construed in the light of what was deemed an unreasonable search and seizure when it was adopted and in a manner which will conserve public interests as well as the interests and rights of individual citizens."</p>
<p>Justice Bradley in the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case, and Justice Clark in the <i><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span></i> case, said that the Fifth Amendment and the Fourth Amendment were to be liberally construed to effect the purpose of the framers of the Constitution in the interest of liberty. But that can not justify enlargement of the language employed beyond the possible practical meaning of houses, persons, papers, and effects, or so to apply the words search and seizure as to forbid hearing or sight.</p>
<p><i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U.S. 57</a></span>, held that the testimony of two officers of the law who trespassed on the defendant's land, concealed themselves one hundred yards away from his house and saw him come out and hand a bottle of whiskey to another, was not inadmissible. While there was a trespass, there was no search of person, house, papers or effects. <i>United States</i> v. <i>Lee,</i> <span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/#563" aria-description="Citation for case: United States v. Lee">274 U.S. 559, 563</a></span>; <i>Eversole</i> v. <i>State,</i> 106 Tex. Cr. 567.</p>
<p>Congress may of course protect the secrecy of telephone messages by making them, when intercepted, inadmissible in evidence in federal criminal trials, by direct legislation, <span class="star-pagination">*466</span> and thus depart from the common law of evidence. But the courts may not adopt such a policy by attributing an enlarged and unusual meaning to the Fourth Amendment. The reasonable view is that one who installs in his house a telephone instrument with connecting wires intends to project his voice to those quite outside, and that the wires beyond his house and messages while passing over them are not within the protection of the Fourth Amendment. Here those who intercepted the projected voices were not in the house of either party to the conversation.</p>
<p>Neither the cases we have cited nor any of the many federal decisions brought to our attention hold the Fourth Amendment to have been violated as against a defendant unless there has been an official search and seizure of his person, or such a seizure of his papers or his tangible material effects, or an actual physical invasion of his house "or curtilage" for the purpose of making a seizure.</p>
<p>We think, therefore, that the wire tapping here disclosed did not amount to a search or seizure within the meaning of the Fourth Amendment.</p>
<p>What has been said disposes of the only question that comes within the terms of our order granting certiorari in these cases. But some of our number, departing from that order, have concluded that there is merit in the two-fold objection overruled in both courts below that evidence obtained through intercepting of telephone messages by government agents was inadmissible because the mode of obtaining it was unethical and a misdemeanor under the law of Washington. To avoid any misapprehension of our views of that objection we shall deal with it in both of its phases.</p>
<p>While a Territory, the English common law prevailed in Washington and thus continued after her admission in 1889. The rules of evidence in criminal cases in courts of the United States sitting there, consequently are those of the common law. <i>United States</i> v. <i>Reid,</i> <span class="citation" data-id="86700"><a href="/opinion/86700/united-states-v-reid/" aria-description="Citation for case: United States v. Reid">12 How. 361</a></span>, <span class="star-pagination">*467</span> 363, 366; <i>Logan</i> v. <i>United States,</i> <span class="citation" data-id="93322"><a href="/opinion/93322/logan-v-united-states/#301" aria-description="Citation for case: Logan v. United States">144 U.S. 263, 301</a></span>; <i>Rosen</i> v. <i>United States,</i> <span class="citation" data-id="9418348"><a href="/opinion/99065/rosen-v-united-states/" aria-description="Citation for case: Rosen v. United States">245 U.S. 467</a></span>; <i>Withaup</i> v. <i>United States,</i> <span class="citation" data-id="8753153"><a href="/opinion/8769634/withaup-v-united-states/#534" aria-description="Citation for case: Withaup v. United States">127 Fed. 530, 534</a></span>; <i>Robinson</i> v. <i>United States,</i> <span class="citation" data-id="8832383"><a href="/opinion/8847089/robinson-v-united-states/#685" aria-description="Citation for case: Robinson v. United States">292 Fed. 683, 685</a></span>.</p>
<p>The common law rule is that the admissibility of evidence is not affected by the illegality of the means by which it was obtained. Professor Greenleaf in his work on evidence, vol. 1, 12th ed., by Redfield, § 254(a) says:</p>
<p>"It may be mentioned in this place, that though papers and other subjects of evidence may have been <i>illegally taken</i> from the possession of the party against whom they are offered, or otherwise unlawfully obtained, this is no valid objection to their admissibility, if they are pertinent to the issue. The court will not take notice how they were obtained, whether lawfully or unlawfully, nor will it form an issue, to determine that question."</p>
<p>Mr. Jones in his work on the same subject refers to Mr. Greenleaf's statement, and says:</p>
<p>"Where there is no violation of a constitutional guaranty, the verity of the above statement is absolute." Vol. 5, § 2075, note 3.</p>
<p>The rule is supported by many English and American cases cited by Jones in vol. 5, § 2075, note 3, and § 2076, note 6; and by Wigmore, vol. 4, § 2183. It is recognized by this Court in <i>Adams</i> v. <i>New York,</i> <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U.S. 585</a></span>. The <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case, announced an exception to the common law rule by excluding all evidence in the procuring of which government officials took part by methods forbidden by the Fourth and Fifth Amendments. Many state courts do not follow the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case. <i>People</i> v. <i>Defore,</i> <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">242 N.Y. 13</a></span>. But those who do, treat it as an exception to the general common law rule and required by constitutional limitations. <i>Hughes</i> v. <i>State,</i> <span class="citation" data-id="8302107"><a href="/opinion/8334068/hughes-v-state/#551" aria-description="Citation for case: Hughes v. State">145 Tenn. 544, 551, 566</a></span>; <i>State</i> v. <i>Wills,</i> <span class="citation" data-id="8179537"><a href="/opinion/8216688/state-v-wills/#677" aria-description="Citation for case: State v. Wills">91 W. Va. 659, 677</a></span>; <i>State</i> v. <i>Slamon,</i> <span class="citation" data-id="6585198"><a href="/opinion/6705054/state-v-slamon/#214" aria-description="Citation for case: State v. Slamon">73 Vt. 212, 214, 215</a></span>; <i>Gindrat</i> v. <i>People,</i> <span class="citation" data-id="6964776"><a href="/opinion/7060795/gindrat-v-people/#111" aria-description="Citation for case: Gindrat v. People">138 Ill. 103, 111</a></span>; <i>People</i> v. <i>Castree,</i> <span class="citation" data-id="6981353"><a href="/opinion/7076578/people-v-castree/#396" aria-description="Citation for case: People v. Castree">311 Ill. 392, 396, 397</a></span>; <i>State</i> v. <span class="star-pagination">*468</span> <i>Gardner,</i> <span class="citation" data-id="3543071"><a href="/opinion/3564065/state-v-gardner/#21" aria-description="Citation for case: State v. Gardner">77 Mont. 8, 21</a></span>; <i>State</i> v. <i>Fahn,</i> 53 N. Dak. 203, 210. The common law rule must apply in the case at bar.</p>
<p>Nor can we, without the sanction of congressional enactment, subscribe to the suggestion that the courts have a discretion to exclude evidence, the admission of which is not unconstitutional, because unethically secured. This would be at variance with the common law doctrine generally supported by authority. There is no case that sustains, nor any recognized text book that gives color to such a view. Our general experience shows that much evidence has always been receivable although not obtained by conformity to the highest ethics. The history of criminal trials shows numerous cases of prosecutions of oath-bound conspiracies for murder, robbery, and other crimes, where officers of the law have disguised themselves and joined the organizations, taken the oaths and given themselves every appearance of active members engaged in the promotion of crime, for the purpose of securing evidence. Evidence secured by such means has always been received.</p>
<p>A standard which would forbid the reception of evidence if obtained by other than nice ethical conduct by government officials would make society suffer and give criminals greater immunity than has been known heretofore. In the absence of controlling legislation by Congress, those who realize the difficulties in bringing offenders to justice may well deem it wise that the exclusion of evidence should be confined to cases where rights under the Constitution would be violated by admitting it.</p>
<p>The statute of Washington, adopted in 1909, provides (Remington Compiled Statutes, 1922, § 2656-18) that:</p>
<p>"Every person . . . who shall intercept, read or in any manner interrupt or delay the sending of a message over any telegraph or telephone line . . . shall be guilty of a misdemeanor."</p>
<p><span class="star-pagination">*469</span> This statute does not declare that evidence obtained by such interception shall be inadmissible, and by the common law, already referred to, it would not be. <i>People</i> v. <i>McDonald,</i> 177 App. Div. (N.Y.) 806. Whether the State of Washington may prosecute and punish federal officers violating this law and those whose messages were intercepted may sue them civilly is not before us. But clearly a statute, passed twenty years after the admission of the State into the Union can not affect the rules of evidence applicable in courts of the United States in criminal cases. Chief Justice Taney, in <i>United States</i> v. <i>Reid,</i> <span class="citation" data-id="86700"><a href="/opinion/86700/united-states-v-reid/#363" aria-description="Citation for case: United States v. Reid">12 How. 361, 363</a></span>, construing the 34th section of the Judiciary Act, said:</p>
<p>"But it could not be supposed, without very plain words to show it, that Congress intended to give the states the power of prescribing the rules of evidence in trials for offenses against the United States. For this construction would place the criminal jurisprudence of one sovereignty under the control of another." See also <i>Withaup</i> v. <i>United States,</i> <span class="citation" data-id="8753153"><a href="/opinion/8769634/withaup-v-united-states/#534" aria-description="Citation for case: Withaup v. United States">127 Fed. 530, 534</a></span>.</p>
<p>The judgments of the Circuit Court of Appeals are affirmed. The mandates will go down forthwith under Rule 31.</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE HOLMES:</p>
<p>My brother BRANDEIS has given this case so exhaustive an examination that I desire to add but a few words. While I do not deny it, I am not prepared to say that the penumbra of the Fourth and Fifth Amendments covers the defendant, although I fully agree that Courts are apt to err by sticking too closely to the words of a law where those words import a policy that goes beyond them. <i>Gooch</i> v. <i>Oregon Short Line R.R. Co.,</i> <span class="citation" data-id="99914"><a href="/opinion/99914/gooch-v-oregon-short-line-railroad/#24" aria-description="Citation for case: Gooch v. Oregon Short Line Railroad">258 U.S. 22, 24</a></span>. But I think, as MR. JUSTICE BRANDEIS says, that apart from the Constitution the Government ought not to use <span class="star-pagination">*470</span> evidence obtained and only obtainable by a criminal act. There is no body of precedents by which we are bound, and which confines us to logical deduction from established rules. Therefore we must consider the two objects of desire, both of which we cannot have, and make up our minds which to choose. It is desirable that criminals should be detected, and to that end that all available evidence should be used. It also is desirable that the Government should not itself foster and pay for other crimes, when they are the means by which the evidence is to be obtained. If it pays its officers for having got evidence by crime I do not see why it may not as well pay them for getting it in the same way, and I can attach no importance to protestations of disapproval if it knowingly accepts and pays and announces that in the future it will pay for the fruits. We have to chose, and for my part I think it a less evil that some criminals should escape than that the Government should play an ignoble part.</p>
<p>For those who agree with me, no distinction can be taken between the Government as prosecutor and the Government as judge. If the existing code does not permit district attorneys to have a hand in such dirty business it does not permit the judge to allow such iniquities to succeed. See <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U.S. 385</a></span>. And if all that I have said so far be accepted it makes no difference that in this case wire tapping is made a crime by the law of the State, not by the law of the United States. It is true that a State cannot make rules of evidence for Courts of the United States, but the State has authority over the conduct in question, and I hardly think that the United States would appear to greater advantage when paying for an odious crime against State law than when inciting to the disregard of its own. I am aware of the often repeated statement that in a criminal proceeding the Court will not take notice of the manner in which papers offered in evidence have been <span class="star-pagination">*471</span> obtained. But that somewhat rudimentary mode of disposing of the question has been overthrown by <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U.S. 383</a></span> and the cases that have followed it. I have said that we are free to choose between two principles of policy. But if we are to confine ourselves to precedent and logic the reason for excluding evidence obtained by violating the Constitution seems to me logically to lead to excluding evidence obtained by a crime of the officers of the law.</p>
<p>MR. JUSTICE BRANDEIS, dissenting.</p>
<p>The defendants were convicted of conspiring to violate the National Prohibition Act. Before any of the persons now charged had been arrested or indicted, the telephones by means of which they habitually communicated with one another and with others had been tapped by federal officers. To this end, a lineman of long experience in wire-tapping was employed, on behalf of the Government and at its expense. He tapped eight telephones, some in the homes of the persons charged, some in their offices. Acting on behalf of the Government and in their official capacity, at least six other prohibition agents listened over the tapped wires and reported the messages taken. Their operations extended over a period of nearly five months. The type-written record of the notes of conversations overheard occupies 775 typewritten pages. By objections seasonably made and persistently renewed, the defendants objected to the admission of the evidence obtained by wire-tapping, on the ground that the Government's wire-tapping constituted an unreasonable search and seizure, in violation of the Fourth Amendment; and that the use as evidence of the conversations overheard compelled the defendants to be witnesses against themselves, in violation of the Fifth Amendment.</p>
<p>The Government makes no attempt to defend the methods employed by its officers. Indeed, it concedes <span class="star-pagination">*472</span> that if wire-tapping can be deemed a search and seizure within the Fourth Amendment, such wire-tapping as was practiced in the case at bar was an unreasonable search and seizure, and that the evidence thus obtained was inadmissible. But it relies on the language of the Amendment; and it claims that the protection given thereby cannot properly be held to include a telephone conversation.</p>
<p>"We must never forget," said Mr. Chief Justice Marshall in <i>McCulloch</i> v. <i>Maryland,</i> <span class="citation" data-id="85272"><a href="/opinion/85272/mculloch-v-state-of-maryland/#407" aria-description="Citation for case: M&#x27;culloch v. State of Maryland">4 Wheat. 316, 407</a></span>, "that it is a constitution we are expounding." Since then, this Court has repeatedly sustained the exercise of power by Congress, under various clauses of that instrument, over objects of which the Fathers could not have dreamed. See <i>Pensacola Telegraph Co.</i> v. <i>Western Union Telegraph Co.,</i> <span class="citation" data-id="9417106"><a href="/opinion/89664/pensacola-telegraph-co-v-western-union-telegraph-co/#9" aria-description="Citation for case: Pensacola Telegraph Co. v. Western Union Telegraph Co.">96 U.S. 1, 9</a></span>; <i>Northern Pacific Ry. Co.</i> v. <i>North Dakota,</i> <span class="citation" data-id="99406"><a href="/opinion/99406/northern-pacific-railway-co-v-north-dakota-ex-rel-langer/" aria-description="Citation for case: Northern Pacific Railway Co. v. North Dakota Ex Rel. Langer">250 U.S. 135</a></span>; <i>Dakota Central Telephone Co.</i> v. <i>South Dakota,</i> <span class="citation" data-id="99408"><a href="/opinion/99408/dakota-central-telephone-co-v-south-dakota-ex-rel-payne/" aria-description="Citation for case: Dakota Central Telephone Co. v. South Dakota Ex Rel. Payne">250 U.S. 163</a></span>; <i>Brooks</i> v. <i>United States,</i> <span class="citation" data-id="100610"><a href="/opinion/100610/brooks-v-united-states/" aria-description="Citation for case: Brooks v. United States">267 U.S. 432</a></span>. We have likewise held that general limitations on the powers of Government, like those embodied in the due process clauses of the Fifth and Fourteenth Amendments, do not forbid the United States or the States from meeting modern conditions by regulations which "a century ago, or even half a century ago, probably would have been rejected as arbitrary and oppressive." <i>Village of Euclid</i> v. <i>Ambler Realty Co.,</i> <span class="citation" data-id="100934"><a href="/opinion/100934/village-of-euclid-v-ambler-realty-co/#387" aria-description="Citation for case: Village of Euclid v. Ambler Realty Co.">272 U.S. 365, 387</a></span>; <i>Buck</i> v. <i>Bell,</i> <span class="citation" data-id="101076"><a href="/opinion/101076/buck-v-bell/" aria-description="Citation for case: Buck v. Bell">274 U.S. 200</a></span>. Clauses guaranteeing to the individual protection against specific abuses of power, must have a similar capacity of adaptation to a changing world. It was with reference to such a clause that this Court said in <i>Weems</i> v. <i>United States,</i> <span class="citation" data-id="9418181"><a href="/opinion/97242/weems-v-united-states/" aria-description="Citation for case: Weems v. United States">217 U.S. 349</a></span>, 373: "Legislation, both statutory and constitutional, is enacted, it is true, from an experience of evils, but its general language should not, therefore, be necessarily confined to the form that evil had theretofore taken. Time works changes, brings into existence new conditions <span class="star-pagination">*473</span> and purposes. Therefore a principle to be vital must be capable of wider application than the mischief which gave it birth. This is peculiarly true of constitutions. They are not ephemeral enactments, designed to meet passing occasions. They are, to use the words of Chief Justice Marshall `designed to approach immortality as nearly as human institutions can approach it.' The future is their care and provision for events of good and bad tendencies of which no prophecy can be made. In the application of a constitution, therefore, our contemplation cannot be only of what has been but of what may be. Under any other rule a constitution would indeed be as easy of application as it would be deficient in efficacy and power. Its general principles would have little value and be converted by precedent into impotent and lifeless formulas. Rights declared in words might be lost in reality."</p>
<p>When the Fourth and Fifth Amendments were adopted, "the form that evil had theretofore taken," had been necessarily simple. Force and violence were then the only means known to man by which a Government could directly effect self-incrimination. It could compel the individual to testify  a compulsion effected, if need be, by torture. It could secure possession of his papers and other articles incident to his private life  a seizure effected, if need be, by breaking and entry. Protection against such invasion of "the sanctities of a man's home and the privacies of life" was provided in the Fourth and Fifth Amendments by specific language. <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U.S. 616, 630</a></span>. But "time works changes, brings into existence new conditions and purposes." Subtler and more far-reaching means of invading privacy have become available to the Government. Discovery and invention have made it possible for the Government, by means far more effective than stretching upon the rack, to obtain disclosure in court of what is whispered in the closet.</p>
<p><span class="star-pagination">*474</span> Moreover, "in the application of a constitution, our contemplation cannot be only of what has been but of what may be." The progress of science in furnishing the Government with means of espionage is not likely to stop with wire-tapping. Ways may some day be developed by which the Government, without removing papers from secret drawers, can reproduce them in court, and by which it will be enabled to expose to a jury the most intimate occurrences of the home. Advances in the psychic and related sciences may bring means of exploring unexpressed beliefs, thoughts and emotions. "That places the liberty of every man in the hands of every petty officer" was said by James Otis of much lesser intrusions than these.<sup>[1]</sup> To Lord Camden, a far slighter intrusions seemed "subversive of all the comforts of society."<sup>[2]</sup> Can it be that the Constitution affords no protection against such invasions of individual security?</p>
<p>A sufficient answer is found in <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#627" aria-description="Citation for case: Boyd v. United States">116 U.S. 616, 627-630</a></span>, a case that will be remembered as long as civil liberty lives in the United States. This Court there reviewed the history that lay behind the Fourth and Fifth Amendments. We said with reference to Lord Camden's judgment in <i>Entick</i> v. <i>Carrington,</i> 19 Howell's State Trials, 1030: "The principles laid down in this opinion affect the very essence of constitutional liberty and security. They reach farther than the concrete form of the case there before the court, with its adventitious circumstances; they apply to all invasions on the part of the Government and its employes of the sanctities of a man's home and the privacies of life. It is not the breaking of his doors, and the rummaging of his drawers, that constitutes the essence of the offence; but it is the invasion of his indefeasible right of personal security, <span class="star-pagination">*475</span> personal liberty and private property, where that right has never been forfeited by his conviction of some public offence,  it is the invasion of this sacred right which underlies and constitutes the essence of Lord Camden's judgment. Breaking into a house and opening boxes and drawers are circumstances of aggravation; but any forcible and compulsory extortion of a man's own testimony or of his private papers to be used as evidence of a crime or to forfeit his goods, is within the condemnation of that judgment. In this regard the Fourth and Fifth Amendments run almost into each other."<sup>[3]</sup></p>
<p>In <i>Ex parte Jackson,</i> <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/" aria-description="Citation for case: Ex Parte Jackson">96 U.S. 727</a></span>, it was held that a sealed letter entrusted to the mail is protected by the Amendments. The mail is a public service furnished by the Government. The telephone is a public service furnished by its authority. There is, in essence, no difference between the sealed letter and the private telephone message. As Judge Rudkin said below: "True the one is visible, the other invisible; the one is tangible, the other intangible; the one is sealed and the other unsealed, but these are distinctions without a difference." The evil incident to invasion of the privacy of the telephone is far greater than that involved in tampering with the mails. Whenever a telephone line is tapped, the privacy of the persons at both ends of the line is invaded and all conversations <span class="star-pagination">*476</span> between them upon any subject, and although proper, confidential and privileged, may be overheard. Moreover, the tapping of one man's telephone line involves the tapping of the telephone of every other person whom he may call or who may call him. As a means of espionage, writs of assistance and general warrants are but puny instruments of tyranny and oppression when compared with wire-tapping.</p>
<p>Time and again, this Court in giving effect to the principle underlying the Fourth Amendment, has refused to place an unduly literal construction upon it. This was notably illustrated in the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case itself. Taking language in its ordinary meaning, there is no "search" or "seizure" when a defendant is required to produce a document in the orderly process of a court's procedure. "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures," would not be violated, under any ordinary construction of language, by compelling obedience to a subpoena. But this Court holds the evidence inadmissible simply because the information leading to the issue of the subpoena has been unlawfully secured. <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U.S. 385</a></span>. Literally, there is no "search" or "seizure" when a friendly visitor abstracts papers from an office; yet we held in <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>, that evidence so obtained could not be used. No court which looked at the words of the Amendment rather than at its underlying purpose would hold, as this Court did in <i>Ex parte Jackson,</i> <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U.S. 727, 733</a></span>, that its protection extended to letters in the mails. The provision against self-incrimination in the Fifth Amendment has been given an equally broad construction. The language is: "No person. . . shall be compelled in any criminal case to be a witness against himself." Yet we have held, not only that the <span class="star-pagination">*477</span> protection of the Amendment extends to a witness before a grand jury, although he has not been charged with crime, <i>Counselman</i> v. <i>Hitchcock,</i> <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#562" aria-description="Citation for case: Counselman v. Hitchcock">142 U.S. 547, 562, 586</a></span>. but that: "It applies alike to civil and criminal proceedings, wherever the answer might tend to subject to criminal responsibility him who gives it. The privilege protects a mere witness as fully as it does one who is also a party defendant." <i>McCarthy</i> v. <i>Arndstein,</i> <span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/#40" aria-description="Citation for case: McCarthy v. Arndstein">266 U.S. 34, 40</a></span>. The narrow language of the Amendment has been consistently construed in the light of its object, "to insure that a person should not be compelled, when acting as a witness in any investigation, to give testimony which might tend to show that he himself had committed a crime. The privilege is limited to criminal matters, but it is as broad as the mischief against which it seeks to guard." <i>Counselman</i> v. <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#562" aria-description="Citation for case: Counselman v. Hitchcock"><i>Hitchcock, supra,</i> p. 562</a></span>.</p>
<p>Decisions of this Court applying the principle of the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case have settled these things. Unjustified search and seizure violates the Fourth Amendment, whatever the character of the paper;<sup>[4]</sup> whether the paper when taken by the federal officers was in the home,<sup>[5]</sup> in an office<sup>[6]</sup> or elsewhere;<sup>[7]</sup> whether the taking was effected by force,<sup>[8]</sup> by <span class="star-pagination">*478</span> fraud,<sup>[9]</sup> or in the orderly process of a court's procedure.<sup>[10]</sup> From these decisions, it follows necessarily that the Amendment is violated by the officer's reading the paper without a physical seizure, without his even touching it; and that use, in any criminal proceeding, of the contents of the paper so examined  as where they are testified to by a federal officer who thus saw the document or where, through knowledge so obtained, a copy has been procured elsewhere<sup>[11]</sup>  any such use constitutes a violation of the Fifth Amendment.</p>
<p>The protection guaranteed by the Amendments is much broader in scope. The makers of our Constitution undertook to secure conditions favorable to the pursuit of happiness. They recognized the significance of man's spiritual nature, of his feelings and of his intellect. They knew that only a part of the pain, pleasure and satisfactions of life are to be found in material things. They sought to protect Americans in their beliefs, their thoughts, their emotions and their sensations. They conferred, as against the Government, the right to be let alone  the most comprehensive of rights and the right most valued by civilized men. To protect that right, every unjustifiable intrusion by the Government upon the privacy of the individual, whatever the means employed, must be deemed a violation of the Fourth Amendment. And the use, as evidence <span class="star-pagination">*479</span> in a criminal proceeding, of facts ascertained by such intrusion must be deemed a violation of the Fifth.</p>
<p>Applying to the Fourth and Fifth Amendments the established rule of construction, the defendants' objections to the evidence obtained by wire-tapping must, in my opinion, be sustained. It is, of course, immaterial where the physical connection with the telephone wires leading into the defendants' premises was made. And it is also immaterial that the intrusion was in aid of law enforcement. Experience should teach us to be most on our guard to protect liberty when the Government's purposes are beneficent. Men born to freedom are naturally alert to repel invasion of their liberty by evil-minded rulers. The greatest dangers to liberty lurk in insidious encroachment by men of zeal, well-meaning but without understanding.<sup>[12]</sup></p>
<p>Independently of the constitutional question, I am of opinion that the judgment should be reversed. By the laws of Washington, wire-tapping is a crime.<sup>[13]</sup> Pierce's <span class="star-pagination">*480</span> Code, 1921, § 8976(18). To prove its case, the Government was obliged to lay bare the crimes committed by its officers on its behalf. A federal court should not permit such a prosecution to continue. Compare <i>Harkin</i> v. <i>Brundage,</i> <span class="citation" data-id="101214"><a href="/opinion/101214/harkin-v-brundage/" aria-description="Citation for case: Harkin v. Brundage">276 U.S. 36</a></span>, <i>id.</i> 604.</p>
<p><span class="star-pagination">*481</span> The situation in the case at bar differs widely from that presented in <i>Burdeau</i> v. <i>McDowell,</i> <span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/" aria-description="Citation for case: Burdeau v. McDowell">256 U.S. 465</a></span>. There, only a single lot of papers was involved. They had been obtained by a private detective while acting on behalf of a private party; without the knowledge of any federal official; long before anyone had thought of instituting a <span class="star-pagination">*482</span> federal prosecution. Here, the evidence obtained by crime was obtained at the Government's expense, by its officers, while acting on its behalf; the officers who committed these crimes are the same officers who were charged with the enforcement of the Prohibition Act; the crimes of these officers were committed for the purpose of securing evidence with which to obtain an indictment and to secure a conviction. The evidence so obtained constitutes the warp and woof of the Government's case. The aggregate of the Government evidence occupies 306 pages of the printed record. More than 210 of them are filled by recitals of the details of the wire-tapping and of facts ascertained thereby.<sup>[14]</sup> There is literally no other evidence of guilt on the part of some of the defendants except that illegally obtained by these officers. As to nearly all the defendants (except those who admitted guilt), the evidence relied upon to secure a conviction consisted mainly of that which these officers had so obtained by violating the state law.</p>
<p>As Judge Rudkin said below: "Here we are concerned with neither eavesdroppers nor thieves. Nor are we concerned with the acts of private individuals. . . . We are concerned only with the acts of federal agents whose powers are limited and controlled by the Constitution of the United States." The Eighteenth Amendment has not in terms empowered Congress to authorize anyone to violate the criminal laws of a State. And Congress has never purported to do so. Compare <i>Maryland</i> v. <i>Soper,</i> <span class="citation" data-id="100776"><a href="/opinion/100776/maryland-v-soper-judge/" aria-description="Citation for case: Maryland v. Soper, Judge">270 U.S. 9</a></span>. The terms of appointment of federal prohibition agents do not purport to confer upon them authority to violate any criminal law. Their superior officer, the Secretary of the Treasury, has not instructed them to commit <span class="star-pagination">*483</span> crime on behalf of the United States. It may be assumed that the Attorney General of the United States did not give any such instruction.<sup>[15]</sup></p>
<p>When these unlawful acts were committed, they were crimes only of the officers individually. The Government was innocent, in legal contemplation; for no federal official is authorized to commit a crime on its behalf. When the Government, having full knowledge, sought, through the Department of Justice, to avail itself of the fruits of these acts in order to accomplish its own ends, it assumed moral responsibility for the officers' crimes. Compare <i>The Paquete Habana,</i> <span class="citation" data-id="95873"><a href="/opinion/95873/the-paquete-habana/#465" aria-description="Citation for case: The Paquete Habana">189 U.S. 453, 465</a></span>; <i>O'Reilly deCamara</i> v. <i>Brooke,</i> <span class="citation" data-id="96812"><a href="/opinion/96812/oreilly-de-camara-v-brooke/#52" aria-description="Citation for case: O&#x27;Reilly De Camara v. Brooke">209 U.S. 45, 52</a></span>; <i>Dodge</i> v. <i>United States,</i> <span class="citation" data-id="100949"><a href="/opinion/100949/dodge-v-united-states/#532" aria-description="Citation for case: Dodge v. United States">272 U.S. 530, 532</a></span>; <i>Gambino</i> v. <i>United States,</i> <span class="citation" data-id="101180"><a href="/opinion/101180/gambino-v-united-states/" aria-description="Citation for case: Gambino v. United States">275 U.S. 310</a></span>. And if this Court should permit the Government, by means of its officers' crimes, to effect its purpose of punishing the defendants, there would seem to be present all the elements of a ratification. If so, the Government itself would become a lawbreaker.</p>
<p>Will this Court by sustaining the judgment below sanction such conduct on the part of the Executive? The governing principle has long been settled. It is that a court will not redress a wrong when he who invokes its aid has unclean hands.<sup>[16]</sup> The maxim of unclean hands comes <span class="star-pagination">*484</span> from courts of equity.<sup>[17]</sup> But the principle prevails also in courts of law. Its common application is in civil actions between private parties. Where the Government is the actor, the reasons for applying it are even more persuasive. Where the remedies invoked are those of the criminal law, the reasons are compelling.<sup>[18]</sup></p>
<p>The door of a court is not barred because the plaintiff has committed a crime. The confirmed criminal is as much entitled to redress as his most virtuous fellow citizen; no record of crime, however long, makes one an outlaw. The court's aid is denied only when he who seeks it has violated the law in connection with the very transaction as to which he seeks legal redress.<sup>[19]</sup> Then aid is denied despite the defendant's wrong. It is denied in order to maintain respect for law; in order is to promote confidence in the administration of justice; in order to preserve the judicial process from contamination. The rule is one, not of action, but of inaction. It is sometimes <span class="star-pagination">*485</span> spoken of as a rule of substantive law. But it extends to matters of procedure as well.<sup>[20]</sup> A defense may be waived. It is waived when not pleaded. But the objection that the plaintiff comes with unclean hands will be taken by the court itself.<sup>[21]</sup> It will be taken despite the wish to the contrary of all the parties to the litigation. The court protects itself.</p>
<p>Decency, security and liberty alike demand that government officials shall be subjected to the same rules of conduct that are commands to the citizen. In a government of laws, existence of the government will be imperilled if it fails to observe the law scrupulously. Our Government is the potent, the omnipresent teacher. For good or for ill, it teaches the whole people by its example. Crime is contagious. If the Government becomes a lawbreaker, it breeds contempt for law; it invites every man to become a law unto himself; it invites anarchy. To declare that in the administration of the criminal law the end justifies the means  to declare that the Government may commit crimes in order to secure the conviction of a private criminal  would bring terrible retribution. Against that pernicious doctrine this Court should resolutely set its face.</p>
<p>MR. JUSTICE BUTLER, dissenting.</p>
<p>I sincerely regret that I cannot support the opinion and judgments of the Court in these cases.</p>
<p><span class="star-pagination">*486</span> The order allowing the writs of certiorari operated to limit arguments of counsel to the constitutional question. I do not participate in the controversy that has arisen here as to whether the evidence was inadmissible because the mode of obtaining it was unethical and a misdemeanor under state law. I prefer to say nothing concerning those questions because they are not within the jurisdiction taken by the order.</p>
<p>The Court is required to construe the provision of the Fourth Amendment that declares: "The right of the people to be secure in their persons, houses, papers and effects, against unreasonable searches and seizures, shall not be violated." The Fifth Amendment prevents the use of evidence obtained through searches and seizures in violation of the rights of the accused protected by the Fourth Amendment.</p>
<p>The single question for consideration is this: May the Government, consistently with that clause, have its officers whenever they see fit, tap wires, listen to, take down and report, the private messages and conversations transmitted by telephones?</p>
<p>The United States maintains that "The `wire tapping' operations of the federal prohibition agents were not a `search and seizure' in violation of the security of the `persons, houses, papers and effects' of the petitioners in the constitutional sense or within the intendment of the Fourth Amendment." The Court, adhering to and reiterating the principles laid down and applied in prior decisions<sup>[*]</sup> construing the search and seizure clause, in substance adopts the contention of the Government.</p>
<p>The question at issue depends upon a just appreciation of the facts.</p>
<p><span class="star-pagination">*487</span> Telephones are used generally for transmission of messages concerning official, social, business and personal affairs including communications that are private and privileged  those between physician and patient, lawyer and client, parent and child, husband and wife. The contracts between telephone companies and users contemplate the private use of the facilities employed in the service. The communications belong to the parties between whom they pass. During their transmission the exclusive use of the wire belongs to the persons served by it. Wire tapping involves interference with the wire while being used. Tapping the wires and listening in by the officers literally constituted a search for evidence. As the communications passed, they were heard and taken down.</p>
<p>In <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U.S. 616</a></span>, there was no "search or seizure" within the literal or ordinary meaning of the words, nor was Boyd  if these constitutional provisions were read strictly according to the letter  compelled in a "criminal case" to be a "witness" against himself. The statute, there held unconstitutional because repugnant to the search and seizure clause, merely authorized judgment for sums claimed by the Government on account of revenue if the defendant failed to produce his books, invoices and papers. The principle of that case has been followed, developed and applied in this and many other courts. And it is in harmony with the rule of liberal construction that always has been applied to provisions of the Constitution safeguarding personal rights (<i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#32" aria-description="Citation for case: Byars v. United States">273 U.S. 28, 32</a></span>), as well as to those granting governmental powers. <i>McCulloch</i> v. <i>Maryland,</i> <span class="citation" data-id="85272"><a href="/opinion/85272/mculloch-v-state-of-maryland/#404" aria-description="Citation for case: M&#x27;culloch v. State of Maryland">4 Wheat. 316, 404, 406, 407, 421</a></span>. <i>Marbury</i> v. <i>Madison,</i> <span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/#153" aria-description="Citation for case: Marbury v. Madison">1 Cranch 137, 153, 176</a></span>. <i>Cohens</i> v. <i>Virginia,</i> <span class="citation" data-id="85330"><a href="/opinion/85330/cohens-v-virginia/" aria-description="Citation for case: Cohens v. Virginia">6 Wheat. 264</a></span>. <i>Myers</i> v. <i>United States,</i> <span class="citation" data-id="9418565"><a href="/opinion/100926/myers-v-united-states/" aria-description="Citation for case: Myers v. United States">272 U.S. 52</a></span>.</p>
<p>This Court has always construed the Constitution in the light of the principles upon which it was founded. <span class="star-pagination">*488</span> The direct operation or literal meaning of the words used do not measure the purpose or scope of its provisions. Under the principles established and applied by this Court, the Fourth Amendment safeguards against all evils that are like and equivalent to those embraced within the ordinary meaning of its words. That construction is consonant with sound reason and in full accord with the course of decisions since <i>McCulloch</i> v. <i>Maryland</i><i>.</i> That is the principle directly applied in the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case.</p>
<p>When the facts in these cases are truly estimated, a fair application of that principle decides the constitutional question in favor of the petitioners. With great deference, I think they should be given a new trial.</p>
<p>MR. JUSTICE STONE, dissenting.</p>
<p>I concur in the opinions of MR. JUSTICE HOLMES and MR. JUSTICE BRANDEIS. I agree also with that of MR. JUSTICE BUTLER so far as it deals with the merits. The effect of the order granting certiorari was to limit the argument to a single question, but I do not understand that it restrains the Court from a consideration of any question which we find to be presented by the record, for, under Jud. Code, § 240(a), this Court determines a case here on certiorari "with the same power and authority, and with like effect, as if the cause had been brought [here] by unrestricted writ of error or appeal."</p>
<h2>NOTES</h2>
<p>[1]  Otis' Argument against Writs of Assistance. See Tudor, James Otis, p. 66; John Adams, Works, Vol. II, p. 524; Minot, Continuation of the History of Massachusetts Bay, Vol. II, p. 95.</p>
<p>[2]  <i>Entick</i> v. <i>Carrington,</i> 19 Howell's State Trials, 1030, 1066.</p>
<p>[3]  In <i>Interstate Commerce Commission</i> v. <i>Brimson,</i> <span class="citation" data-id="93951"><a href="/opinion/93951/interstate-commerce-commission-v-brimson/#479" aria-description="Citation for case: Interstate Commerce Commission v. Brimson">154 U.S. 447, 479</a></span>, the statement made in the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case was repeated; and the Court quoted the statement of Mr. Justice Field in <i>In re Pacific Railway Commission,</i> <span class="citation" data-id="8310981"><a href="/opinion/8342559/in-re-pacific-railway-commission/" aria-description="Citation for case: In re Pacific Railway Commission">32 Fed. 241</a></span>, 250: "Of all the rights of the citizen, few are of greater importance or more essential to his peace and happiness than the right of personal security, and that involves, not merely protection of his person from assault, but exemption of his private affairs, books, and papers, from the inspection and scrutiny of others. Without the enjoyment of this right, all others would lose half their value." The <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case has been recently reaffirmed in <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U.S. 385</a></span>, in <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>, and in <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U.S. 28</a></span>.</p>
<p>[4]  <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>.</p>
<p>[5]  <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U.S. 383</a></span>; <i>Amos</i> v. <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U.S. 313</a></span>; <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U.S. 20</a></span>; <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U.S. 28</a></span>.</p>
<p>[6]  <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U.S. 616</a></span>; <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#70" aria-description="Citation for case: Hale v. Henkel">201 U.S. 43, 70</a></span>; <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U.S. 385</a></span>; <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>; <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U.S. 192</a></span>.</p>
<p>[7]  <i>Ex parte Jackson,</i> <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U.S. 727, 733</a></span>; <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States">267 U.S. 132, 156</a></span>; <i>Gambino</i> v. <i>United States,</i> <span class="citation" data-id="101180"><a href="/opinion/101180/gambino-v-united-states/" aria-description="Citation for case: Gambino v. United States">275 U.S. 310</a></span>.</p>
<p>[8]  <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U.S. 383</a></span>; <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U.S. 385</a></span>; <i>Amos</i> v. <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U.S. 313</a></span>; <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States">267 U.S. 132, 156</a></span>; <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U.S. 20</a></span>; <i>Gambino</i> v. <i>United States,</i> <span class="citation" data-id="101180"><a href="/opinion/101180/gambino-v-united-states/" aria-description="Citation for case: Gambino v. United States">275 U.S. 310</a></span>.</p>
<p>[9]  <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>.</p>
<p>[10]  <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U.S. 616</a></span>; <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#70" aria-description="Citation for case: Hale v. Henkel">201 U.S. 43, 70</a></span>. See <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>; <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U.S. 28</a></span>; <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U.S. 192</a></span>.</p>
<p>[11]  <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U.S. 385</a></span>. Compare <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#307" aria-description="Citation for case: Gouled v. United States">255 U.S. 298, 307</a></span>. In <i>Stroud</i> v. <i>United States,</i> <span class="citation" data-id="99464"><a href="/opinion/99464/stroud-v-united-states/" aria-description="Citation for case: Stroud v. United States">251 U.S. 15</a></span>, and <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U.S. 57</a></span>, the letter and articles admitted were not obtained by unlawful search and seizure. They were voluntary dilosures by the defendant. Compare <i>Smith</i> v. <i>United States,</i> 2 F. (2d) 715; <i>United States</i> v. <i>Lee,</i> <span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/" aria-description="Citation for case: United States v. Lee">274 U.S. 559</a></span>.</p>
<p>[12]  The point is thus stated by counsel for the telephone companies, who have filed a brief as <i>amici curiae:</i> "Criminals will not escape detection and conviction merely because evidence obtained by tapping wires of a public telephone system is inadmissible, if it should be so held; but, in any event, it is better that a few criminals escape than that the privacies of life of all the people be exposed to the agents of the government, who will act at their own discretion, the honest and the dishonest, unauthorized and unrestrained by the courts. Legislation making wire tapping a crime will not suffice if the courts nevertheless hold the evidence to be lawful."</p>
<p>[13]  In the following states it is a criminal offense to intercept a message sent by telegraph and/or telephone: Alabama, Code, 1923, § 5256; Arizona, Revised Statutes, 1913, Penal Code, § 692; Arkansas, Crawford &amp; Moses Digest, 1921, § 10246; California, Deering's Penal Code, 1927, § 640; Colorado, Compiled Laws, 1921, § 6969; Connecticut, General Statutes, 1918, § 6292; Idaho, Compiled Statutes, 1919, §§ 8574, 8586; Illinois, Revised Statutes, 1927, c. 134, § 21; Iowa, Code, 1927, § 13121; Kansas, Revised Statutes, 1923, c. 17, § 1908; Michigan, Compiled Laws, 1915, § 15403; Montana, Penal Code, 1921, § 11518; Nebraska, Compiled Statutes, 1922, § 7115; Nevada, Revised Laws, 1912, §§ 4608, 6572(18); New York, Consolidated Laws, c. 40, § 1423(6); North Dakota, Compiled Laws, 1913, § 10231; Ohio, Page's General Code, 1926, § 13402; Oklahoma, Session Laws, 1923, c. 46; Oregon, Olson's Laws, 1920, § 2265; South Dakota, Revised Code, 1919, § 4312; Tennessee, Shannon's Code, 1919, §§ 1839, 1840; Utah, Compiled Laws, 1917, § 8433; Virginia, Code, 1924, § 4477(2), (3); Washington, Pierce's Code, 1921, § 8976(18); Wisconsin, Statutes, 1927, § 348.37; Wyoming, Compiled Statutes, 1920, § 7148. Compare <i>State</i> v. <i>Behringer,</i> <span class="citation" data-id="6474480"><a href="/opinion/6599138/state-v-behringer/" aria-description="Citation for case: State v. Behringer">19 Ariz. 502</a></span>; <i>State</i> v. <i>Nordskog,</i> <span class="citation" data-id="4732864"><a href="/opinion/4925570/state-v-nordskog/" aria-description="Citation for case: State v. Nordskog">76 Wash. 472</a></span>.
</p>
<p>In the following states it is a criminal offense for a company engaged in the transmission of messages by telegraph and/or telephone, or its employees, or, in many instances, persons conniving with them, to disclose or to assist in the disclosure of any message: Alabama, Code, 1923, §§ 5543, 5545; Arizona, Revised Statutes, 1913, Penal Code, §§ 621, 623, 691; Arkansas, Crawford &amp; Moses Digest, 1921, § 10250; California, Deering's Penal Code, 1927, §§ 619, 621, 639, 641; Colorado, Compiled Laws, 1921, §§ 6966, 6968, 6970; Connecticut, General Statutes, 1918, § 6292; Florida, Revised General Statutes, 1920, §§ 5754, 5755; Idaho, Compiled Statutes, 1919, §§ 8568, 8570; Illinois, Revised Statutes, 1927, c. 134, §§ 7, 7a; Indiana, Burns' Revised Statutes, 1926, § 2862; Iowa, Code, 1924, § 8305; Louisiana, Acts, 1918, c. 134, p. 228; Maine, Revised Statutes, 1916, c. 60, § 24; Maryland, Bagby's Code, 1926, § 489; Michigan, Compiled Statutes, 1915, § 15104; Minnesota, General Statutes, 1923, §§ 10423, 10424; Mississippi, Hemingway's Code, 1927, § 1174; Missouri, Revised Statutes, 1919, § 3605; Montana, Penal Code, 1921, § 11494; Nebraska, Compiled Statutes, 1922, § 7088; Nevada, Revised Laws, 1912, §§ 4603, 4605, 4609, 4631; New Jersey, Compiled Statutes, 1910, p. 5319; New York, Consolidated Laws, c. 40, §§ 552, 553; North Carolina, Consolidated Statutes, 1919, §§ 4497, 4498, 4499; North Dakota, Compiled Laws, 1913, § 10078; Ohio, Page's General Code, 1926, § 13388, 13419; Oklahoma, Session Laws, 1923, c. 46; Oregon, Olson's Laws, 1920, §§ 2260, 2266; Pennsylvania, Statutes, 1920, §§ 6306, 6308, 6309; Rhode Island, General Laws, 1923, § 6104; South Dakota, Revised Code, 1919, §§ 4346, 9801; Tennessee, Shannon's Code, 1919, §§ 1837, 1838; Utah, Compiled Laws, 1917, §§ 8403, 8405, 8434; Washington, Pierce's Code, 1921, §§ 8982, 8983, Wisconsin, Statutes, 1927, § 348.36.</p>
<p>The Alaskan Penal Code, Act of March 3, 1899, c. 429, <span class="citation no-link">30 Stat. 1253</span>, 1278, provides that "if any officer, agent, operator, clerk, or employee of any telegraph company, or any other person, shall wilfully divulge to any other person than the party from whom the same was received, or to whom the same was addressed, or his agent or attorney, any message received or sent, or intended to be sent, over any telegraph line, or the contents, substance, purport, effect, or meaning of such message, or any part thereof,. . . the person so offending shall be deemed guilty of a misdemeanor, and shall be punished by a fine not to exceed one thousand dollars or imprisonment not to exceed one year, or by both such fine and imprisonment, in the discretion of the court."</p>
<p>The Act of October 29, 1918, c. 197, <span class="citation no-link">40 Stat. 1017</span>, provided: "That whoever during the period of governmental operation of the telephone and telegraph systems of the United States . . . shall, without authority and without the knowledge and consent of the other users thereof, except as may be necessary for operation of the service, tap any telegraph or telephone line, or wilfully interfere with the operation of such telephone and telegraph systems or with the transmission of any telephone or telegraph message, or with the delivery of any such message, or whoever being employed in any such telephone or telegraph service shall divulge the contents of any such telephone or telegraph message to any person not duly authorized to receive the same, shall be fined not exceeding $1,000 or imprisoned for not more than one year, or both."</p>
<p>The Radio Act, February 23, 1927, c. 169, § 27, <span class="citation no-link">44 Stat. 1162</span>, 1172, provides that "no person not being authorized by the sender shall intercept any message and divulge or publish the contents, substance, purport, effect, or meaning of such intercepted message to any person."</p>
<p>[14]  The above figures relate to Case No. 493. In Nos. 532-533, the Government evidence fills 278 pages, of which 140 are recitals of the evidence obtained by wire-tapping.</p>
<p>[15]  According to the Government's brief, p. 41, "The Prohibition Unit of the Treasury disclaims it [wire-tapping] and the Department of Justice has frowned on it." See also "Prohibition Enforcement," 69th Congress, 2d Session, Senate Doc. No. 198, pp. IV, V, 13, 15, referred to Committee, January 25, 1927; also Same, Part 2.</p>
<p>[16]  See <i>Hannay</i> v. <i>Eve,</i> <span class="citation" data-id="84810"><a href="/opinion/84810/hannay-v-eve/#247" aria-description="Citation for case: Hannay v. Eve">3 Cranch, 242, 247</a></span>; <i>Bank of the </i><i>United States</i> v. <i>Owens,</i> <span class="citation" data-id="85646"><a href="/opinion/85646/president-of-the-bank-of-the-united-states-v-owens/#538" aria-description="Citation for case: President of the Bank of the United States v. Owens">2 Pet. 527, 538</a></span>; <i>Bartle</i> v. <i>Coleman,</i> <span class="citation" data-id="85698"><a href="/opinion/85698/bartle-v-nutt/#188" aria-description="Citation for case: Bartle v. Nutt">4 Pet. 184, 188</a></span>; <i>Kennett</i> v. <i>Chambers,</i> <span class="citation" data-id="86769"><a href="/opinion/86769/kennett-v-chambers/#52" aria-description="Citation for case: Kennett v. Chambers">14 How. 38, 52</a></span>; <i>Marshall</i> v. <i>Baltimore &amp; Ohio R.R. Co.,</i> <span class="citation" data-id="9416542"><a href="/opinion/86875/marshall-v-baltimore-ohio-railroad/#334" aria-description="Citation for case: Marshall v. Baltimore &amp; Ohio Railroad">16 How. 314, 334</a></span>; <i>Tool Co.</i> v. <i>Norris,</i> 2 Wall 45, 54; <i>The Ouachita Cotton,</i> <span class="citation" data-id="87951"><a href="/opinion/87951/the-ouachita-cotton/#532" aria-description="Citation for case: The Ouachita Cotton">6 Wall. 521, 532</a></span>; <i>Coppell</i> v. <i>Hall,</i> <span class="citation" data-id="88038"><a href="/opinion/88038/coppell-v-hall/" aria-description="Citation for case: Coppell v. Hall">7 Wall. 542</a></span>; <i>Forsyth</i> v. <i>Woods,</i> <span class="citation" data-id="88341"><a href="/opinion/88341/forsyth-v-woods/#486" aria-description="Citation for case: Forsyth v. Woods">11 Wall. 484, 486</a></span>; <i>Hanauer</i> v. <i>Doane,</i> <span class="citation" data-id="88397"><a href="/opinion/88397/hanauer-v-doane/#349" aria-description="Citation for case: Hanauer v. Doane">12 Wall. 342, 349</a></span>; <i>Trist</i> v. <i>Child,</i> <span class="citation" data-id="89027"><a href="/opinion/89027/trist-v-child/#448" aria-description="Citation for case: Trist v. Child">21 Wall. 441, 448</a></span>; <i>Meguire</i> v. <i>Corwine,</i> <span class="citation" data-id="90098"><a href="/opinion/90098/meguire-v-corwine/#111" aria-description="Citation for case: Meguire v. Corwine">101 U.S. 108, 111</a></span>; <i>Oscanyan</i> v. <i>Arms Co.,</i> <span class="citation" data-id="90320"><a href="/opinion/90320/oscanyan-v-arms-co/" aria-description="Citation for case: Oscanyan v. Arms Co.">103 U.S. 261</a></span>; <i>Irwin</i> v. <i>Williar,</i> <span class="citation" data-id="91053"><a href="/opinion/91053/irwin-v-williar/#510" aria-description="Citation for case: Irwin v. Williar">110 U.S. 499, 510</a></span>; <i>Woodstock Iron Co.</i> v. <i>Richmond &amp; Danville Extension Co.,</i> <span class="citation" data-id="92439"><a href="/opinion/92439/woodstock-iron-co-v-richmond-danville-extension-co/" aria-description="Citation for case: Woodstock Iron Co. v. Richmond &amp; Danville Extension Co.">129 U.S. 643</a></span>; <i>Gibbs</i> v. <i>Consolidated Gas Co.,</i> <span class="citation" data-id="92483"><a href="/opinion/92483/gibbs-v-consolidated-gas-co-of-baltimore/#411" aria-description="Citation for case: Gibbs v. Consolidated Gas Co. of Baltimore">130 U.S. 396, 411</a></span>; <i>Embrey</i> v. <i>Jemison,</i> <span class="citation" data-id="92547"><a href="/opinion/92547/embrey-v-jemison/#348" aria-description="Citation for case: Embrey v. Jemison">131 U.S. 336, 348</a></span>; <i>West</i> v. <i>Camden,</i> <span class="citation" data-id="92798"><a href="/opinion/92798/west-v-camden/#521" aria-description="Citation for case: West v. Camden">135 U.S. 507, 521</a></span>; <i>McMullen</i> v. <i>Hoffman,</i> <span class="citation" data-id="95090"><a href="/opinion/95090/mcmullen-v-hoffman/#654" aria-description="Citation for case: McMullen v. Hoffman">174 U.S. 639, 654</a></span>; <i>Hazelton</i> v. <i>Sheckells,</i> <span class="citation" data-id="96460"><a href="/opinion/96460/hazelton-v-sheckells/" aria-description="Citation for case: Hazelton v. Sheckells">202 U.S. 71</a></span>; <i>Crocker</i> v. <i>United States,</i> <span class="citation" data-id="98638"><a href="/opinion/98638/crocker-v-united-states/#78" aria-description="Citation for case: Crocker v. United States">240 U.S. 74, 78</a></span>. Compare <i>Holman</i> v. <i>Johnson,</i> 1 Cowp. 341.</p>
<p>[17]  See <i>Creath's Administrator</i> v. <i>Sims,</i> <span class="citation" data-id="86416"><a href="/opinion/86416/creaths-administrator-v-sims/#204" aria-description="Citation for case: Creath&#x27;s Administrator v. Sims">5 How. 192, 204</a></span>; <i>Kennett</i> v. <i>Chambers,</i> <span class="citation" data-id="86769"><a href="/opinion/86769/kennett-v-chambers/#49" aria-description="Citation for case: Kennett v. Chambers">14 How. 38, 49</a></span>; <i>Randall</i> v. <i>Howard,</i> <span class="citation" data-id="87533"><a href="/opinion/87533/randall-v-howard/#586" aria-description="Citation for case: Randall v. Howard">2 Black, 585, 586</a></span>; <i>Wheeler</i> v. <i>Sage,</i> <span class="citation" data-id="87601"><a href="/opinion/87601/wheeler-v-sage/#530" aria-description="Citation for case: Wheeler v. Sage">1 Wall. 518, 530</a></span>; <i>Dent</i> v. <i>Ferguson,</i> <span class="citation" data-id="92567"><a href="/opinion/92567/dent-v-ferguson/#64" aria-description="Citation for case: Dent v. Ferguson">132 U.S. 50, 64</a></span>; <i>Pope Manufacturing Co.</i> v. <i>Gormully,</i> <span class="citation" data-id="93318"><a href="/opinion/93318/pope-manufacturing-co-v-gormully/#236" aria-description="Citation for case: Pope Manufacturing Co. v. Gormully">144 U.S. 224, 236</a></span>; <i>Miller</i> v. <i>Ammon,</i> <span class="citation" data-id="93392"><a href="/opinion/93392/miller-v-ammon/#425" aria-description="Citation for case: Miller v. Ammon">145 U.S. 421, 425</a></span>; <i>Hazelton</i> v. <i>Sheckells,</i> <span class="citation" data-id="96460"><a href="/opinion/96460/hazelton-v-sheckells/#79" aria-description="Citation for case: Hazelton v. Sheckells">202 U.S. 71, 79</a></span>. <i>Compare </i><i>International News Service</i> v. <i>Associated Press,</i> <span class="citation" data-id="9418368"><a href="/opinion/99248/international-news-service-v-associated-press/#245" aria-description="Citation for case: International News Service v. Associated Press">248 U.S. 215, 245</a></span>.</p>
<p>[18]  Compare <i>State</i> v. <i>Simmons,</i> <span class="citation" data-id="7887295"><a href="/opinion/7936833/state-v-simmons/#264" aria-description="Citation for case: State v. Simmons">39 Kan. 262, 264-265</a></span>; <i>State</i> v. <i>Miller,</i> <span class="citation" data-id="6616565"><a href="/opinion/6734774/state-v-miller/#163" aria-description="Citation for case: State v. Miller">44 Mo. App. 159, 163-164</a></span>; <i>In re Robinson,</i> <span class="citation" data-id="6646653"><a href="/opinion/6763902/in-re-robinson/" aria-description="Citation for case: In re Robinson">29 Neb. 135</a></span>; <i>Harris</i> v. <i>State,</i> 15 Tex. App. 629, 634-635, 639.</p>
<p>[19]  See <i>Armstrong</i> v. <i>Toler,</i> <span class="citation" data-id="85492"><a href="/opinion/85492/armstrong-v-toler/" aria-description="Citation for case: Armstrong v. Toler">11 Wheat. 258</a></span>; <i>Brooks</i> v. <i>Martin,</i> <span class="citation" data-id="9416695"><a href="/opinion/87628/brooks-v-martin/" aria-description="Citation for case: Brooks v. Martin">2 Wall. 70</a></span>; <i>Planters' Bank</i> v. <i>Union Bank,</i> <span class="citation" data-id="9416906"><a href="/opinion/88700/planters-bank-v-union-bank/#499" aria-description="Citation for case: Planters&#x27; Bank v. Union Bank">16 Wall. 483, 499-500</a></span>; <i>Houston &amp; Texas Central R.R. Co.</i> v. <i>Texas,</i> <span class="citation" data-id="9841847"><a href="/opinion/95218/houston-texas-central-railroad-v-texas/#99" aria-description="Citation for case: Houston &amp; Texas Central Railroad v. Texas">177 U.S. 66, 99</a></span>; <i>Bothwell</i> v. <i>Buckbee, Mears Co.,</i> <span class="citation" data-id="101177"><a href="/opinion/101177/bothwell-v-buckbee-mears-co/" aria-description="Citation for case: Bothwell v. Buckbee-Mears Co">275 U.S. 274</a></span>.</p>
<p>[20]  See <i>Lutton</i> v. <i>Benin,</i> 11 Mod. 50; <i>Barlow</i> v. <i><span class="citation" data-id="88038"><a href="/opinion/88038/coppell-v-hall/" aria-description="Citation for case: Coppell v. Hall">Hall</a></span>,</i> 2 Anst. 461; <i>Wells</i> v. <i>Gurney,</i> 8 Barn. &amp; Cress. 769; <i>Ilsley</i> v. <i>Nichols,</i> <span class="citation no-link">12 Pick. 270</span>; <i>Carpenter</i> v. <i>Spooner,</i> <span class="citation" data-id="8357529"><a href="/opinion/8387511/carpenter-v-spooner/" aria-description="Citation for case: Carpenter v. Spooner">2 Sandf. 717</a></span>; <i>Metcalf</i> v. <i>Clark,</i> <span class="citation" data-id="5460681"><a href="/opinion/5615894/metcalf-v-clark/" aria-description="Citation for case: Metcalf v. Clark">41 Barb. 45</a></span>; <i>Williams</i> ads. <i>Reed,</i> <span class="citation" data-id="8058110"><a href="/opinion/8097589/williams-v-reed/" aria-description="Citation for case: Williams v. Reed">29 N.J.L. 385</a></span>; <i>Hill</i> v. <i>Goodrich,</i> <span class="citation" data-id="6578342"><a href="/opinion/6698340/hill-v-goodrich/" aria-description="Citation for case: Hill v. Goodrich">32 Conn. 588</a></span>; <i>Townsend</i> v. <i>Smith,</i> <span class="citation" data-id="6602971"><a href="/opinion/6721916/townsend-v-smith/" aria-description="Citation for case: Townsend v. Smith">47 Wis. 623</a></span>; <i>Blandin</i> v. <i>Ostrander,</i> <span class="citation" data-id="8802105"><a href="/opinion/8817552/blandin-v-ostrander/" aria-description="Citation for case: Blandin v. Ostrander">239 Fed. 700</a></span>; <i>Harkin</i> v. <i>Brundage,</i> <span class="citation" data-id="101214"><a href="/opinion/101214/harkin-v-brundage/" aria-description="Citation for case: Harkin v. Brundage">276 U.S. 36</a></span>, <i>id.,</i> 604.</p>
<p>[21]  <i>Coppell</i> v. <i>Hall,</i> <span class="citation" data-id="88038"><a href="/opinion/88038/coppell-v-hall/#558" aria-description="Citation for case: Coppell v. Hall">7 Wall. 542, 558</a></span>; <i>Oscanyan</i> v. <i>Arms Co.,</i> <span class="citation" data-id="90320"><a href="/opinion/90320/oscanyan-v-arms-co/#267" aria-description="Citation for case: Oscanyan v. Arms Co.">103 U.S. 261, 267</a></span>; <i>Higgins</i> v. <i>McCrea,</i> <span class="citation" data-id="91577"><a href="/opinion/91577/higgins-v-mccrea/#685" aria-description="Citation for case: Higgins v. McCrea">116 U.S. 671, 685</a></span>. Compare <i>Evans</i> v. <i>Richardson,</i> 3 Mer. 469; <i>Norman</i> v. <i>Cole,</i> 3 Esp. 253; <i>Northwestern Salt Co.</i> v. <i>Electrolytic Alkali Co.,</i> [1913] 3 K.B. 422.</p>
<p>[*]  <i>Ex parte Jackson,</i> <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/" aria-description="Citation for case: Ex Parte Jackson">96 U.S. 727</a></span>. <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U.S. 616</a></span>. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U.S. 383</a></span>. <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U.S. 385</a></span>. <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>. <i>Amos</i> v. <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U.S. 313</a></span>.</p>

</div>
```

---
