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

## GROUP: _overhaul2/lake/cases/Illinois v. Andreas.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Illinois v. Andreas"
type: case
citation: "463 U.S. 765 (1983)"
parallel_cite: "103 S. Ct. 3319; 77 L. Ed. 2d 1003; 51 U.S.L.W. 5157"
neutral_cite: 1983 U.S. LEXIS 106
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-07-05
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1983-07-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Illinois v. Andreas
  varies_by_point: false
  scope_note: "Good law; the controlled-delivery / no-revival-of-privacy rule remains the governing standard for reopening a previously lawfully inspected container."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111013/illinois-v-andreas/"
  cluster_id: 111013
  opinion_id: 9429344
  identity_checked: true
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Related"
related: ["[[United States v. Jacobsen]]", "[[United States v. Place]]", "[[Texas v. Brown]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "controlled-delivery", "container", "plain-view"]
holding: "Reopening a container after a lawful controlled delivery is not a new search where no substantial likelihood exists that the contents changed during a gap in surveillance — the earlier lawful inspection already extinguished any privacy interest."
lake:
  record_id: Illinois v. Andreas
  status: verified
  projected_at: 2026-07-09
---

# Illinois v. Andreas

*463 U.S. 765 (1983)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Customs officers lawfully opened a shipped metal container and found marijuana inside a wooden table. They resealed it and made a controlled delivery to Andreas. After he took the container inside his apartment and, some 30–45 minutes later, brought it back out, police reopened it without a warrant and re-confirmed the contraband. Andreas moved to suppress, arguing the warrantless reopening was a new search.

## Issue
Whether reopening, without a warrant, a container whose contents were previously discovered in a lawful customs inspection — after a controlled delivery and a gap in surveillance — constitutes a Fourth Amendment "search."

## Rule
No, where the contents have not likely changed. "No protected privacy interest remains in contraband in a container once government officers lawfully have opened that container and identified its contents as illegal. The simple act of resealing the container to enable the police to make a controlled delivery does not operate to revive or restore the lawfully invaded privacy rights." — 463 U.S. at 771. ^pin-771

The Court set the operative test: "A workable, objective standard that limits the risk of intrusion on legitimate privacy interests is whether there is a substantial likelihood that the contents of the container have been changed during the gap in surveillance. We hold that absent a substantial likelihood that the contents have been changed, there is no legitimate expectation of privacy in the contents of a container previously opened under lawful authority." — [*Id.* at 773](https://www.courtlistener.com/opinion/111013/illinois-v-andreas/#:~:text=A%20workable%2C%20objective%20standard%20that). ^pin-773

## Application
The container's contents had already been identified as contraband in a lawful customs inspection, extinguishing any [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in them. Resealing for the controlled delivery did not revive that interest. Although there was a gap in surveillance while the container was inside Andreas's apartment, on these facts there was no substantial likelihood the contents had been changed, so reopening it to re-confirm the marijuana worked no new Fourth Amendment search.

## Conclusion
The warrantless reopening was not a search; suppression was unwarranted. The case extends plain-view reasoning to controlled deliveries: a privacy interest already lawfully extinguished is not revived by resealing absent a substantial likelihood the contents changed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Builds on the possessory/privacy analysis of [[United States v. Jacobsen]] (private-search and re-examination of already-revealed contents) and the plain-view line (cf. [[Texas v. Brown]]).

## Appears on
- [[Plain View Doctrine]] — *Related*

## Sources
- *Illinois v. Andreas*, 463 U.S. 765 (1983) — https://www.courtlistener.com/opinion/111013/illinois-v-andreas/ — pinpoints: 771, 773.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "fd044b050885f6f9", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Illinois v. Andreas"}, "payload": {"all": [{"cite": "463 U.S. 765", "page": "765", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "463"}, {"cite": "103 S. Ct. 3319", "page": "3319", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "103"}, {"cite": "77 L. Ed. 2d 1003", "page": "1003", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "77"}, {"cite": "1983 U.S. LEXIS 106", "page": "106", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1983"}, {"cite": "51 U.S.L.W. 5157", "page": "5157", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "51"}], "display": "463 U.S. 765", "official": {"cite": "463 U.S. 765", "page": "765", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "463"}, "official_selection_present": true, "record_id": "Illinois v. Andreas"}}
{"assertion_id": "9137c70583ed1d0a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-771", "record_id": "Illinois v. Andreas"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-771", "pinpoint_status": "slip-only", "quote": "## Rule No, where the contents have not likely changed.", "quote_fidelity": "mismatch", "record_id": "Illinois v. Andreas", "star_marker": null}}
{"assertion_id": "dba3d61d895f1d05", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-773", "record_id": "Illinois v. Andreas"}, "payload": {"fragment": "#:~:text=A%20workable%2C%20objective%20standard%20that", "page": null, "pin_id": "pin-773", "pinpoint_status": "star-verified", "quote": "A workable, objective standard that limits the risk of intrusion on legitimate privacy interests is whether there is a substantial likelihood that the contents of the container have been changed during the gap in surveillance. We hold that absent a substantial likelihood that the contents have been changed, there is no legitimate expectation of privacy in the contents of a container previously opened under lawful authority.", "quote_fidelity": "matched", "record_id": "Illinois v. Andreas", "star_marker": "773"}}
{"assertion_id": "bc6226d15b15ac94", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Illinois v. Andreas"}, "payload": {"as_of_content": "1983-07-05", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Illinois v. Andreas", "scope_note": "Good law; the controlled-delivery / no-revival-of-privacy rule remains the governing standard for reopening a previously lawfully inspected container.", "varies_by_point": false}}
```

### lake record — Illinois v. Andreas

```json
{
  "schema_version": "s2.v1",
  "record_id": "Illinois v. Andreas",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Illinois v. Andreas",
    "case_name_short": "Andreas",
    "case_name_full": "Illinois v. Andreas",
    "input_case_name": "Illinois v. Andreas",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-07-05",
    "year": 1983,
    "docket": null,
    "cluster_id": 111013,
    "lead_opinion_id": 9429344,
    "sibling_ids": [
      111013,
      9429344,
      9429345,
      9429346
    ],
    "absolute_url": "/opinion/111013/illinois-v-andreas/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "463 U.S. 765",
      "volume": "463",
      "reporter": "U.S.",
      "page": "765",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 3319",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "3319",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 2d 1003",
        "volume": "77",
        "reporter": "L. Ed. 2d",
        "page": "1003",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 5157",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "5157",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 106",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "106",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "463 U.S. 765",
        "volume": "463",
        "reporter": "U.S.",
        "page": "765",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 3319",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "3319",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 2d 1003",
        "volume": "77",
        "reporter": "L. Ed. 2d",
        "page": "1003",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 106",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "106",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 5157",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "5157",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "463 U.S. 765",
    "official_selection": {
      "court_class": "scotus",
      "selected": "463 U.S. 765",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-771",
      "page": null,
      "quote": "## Rule No, where the contents have not likely changed.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-773",
      "page": null,
      "quote": "A workable, objective standard that limits the risk of intrusion on legitimate privacy interests is whether there is a substantial likelihood that the contents of the container have been changed during the gap in surveillance. We hold that absent a substantial likelihood that the contents have been changed, there is no legitimate expectation of privacy in the contents of a container previously opened under lawful authority.",
      "star_marker": "773",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15944,
      "fragment": "#:~:text=A%20workable%2C%20objective%20standard%20that",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1983-07-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Illinois v. Andreas",
    "varies_by_point": false,
    "scope_note": "Good law; the controlled-delivery / no-revival-of-privacy rule remains the governing standard for reopening a previously lawfully inspected container.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Martinez, Roger Anthony",
          "cluster_id": 4580254,
          "cite": [
            "569 S.W.3d 621"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane1_negative"
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
        "journal_ref": "Illinois v. Andreas:lane1_negative"
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
        "journal_ref": "Illinois v. Andreas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Turpin",
          "cluster_id": 4423584,
          "cite": [
            "2017 Ohio 7435",
            "96 N.E.3d 1171"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grice",
          "cluster_id": 2792904,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grice",
          "cluster_id": 2772730,
          "cite": [
            "367 N.C. 753",
            "767 S.E.2d 312",
            "2015 N.C. LEXIS 69"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Deaver v. State",
          "cluster_id": 1466550,
          "cite": [
            "314 S.W.3d 481",
            "2010 WL 1633430"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ronnie Durant Deaver v. State",
          "cluster_id": 3129860,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane1_negative"
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
        "journal_ref": "Illinois v. Andreas:lane1_negative"
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
        "journal_ref": "Illinois v. Andreas:lane1_negative"
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
        "journal_ref": "Illinois v. Andreas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. William Colon",
          "cluster_id": 773257,
          "cite": [
            "250 F.3d 130",
            "2001 U.S. App. LEXIS 9205"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Camacho",
          "cluster_id": 2546036,
          "cite": [
            "3 P.3d 878",
            "98 Cal. Rptr. 2d 232",
            "23 Cal. 4th 824",
            "2000 Cal. Daily Op. Serv. 6235",
            "2000 Daily Journal DAR 8273",
            "2000 Cal. LEXIS 5605"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Superintendent, Mass. Correctional Institution at Walpole v. Hill",
          "cluster_id": 111476,
          "cite": [
            "86 L. Ed. 2d 356",
            "105 S. Ct. 2768",
            "472 U.S. 445",
            "1985 U.S. LEXIS 109",
            "53 U.S.L.W. 4778"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
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
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
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
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
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
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
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
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
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
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
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
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
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
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
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
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Garrison",
          "cluster_id": 111823,
          "cite": [
            "94 L. Ed. 2d 72",
            "107 S. Ct. 1013",
            "480 U.S. 79",
            "1987 U.S. LEXIS 559",
            "55 U.S.L.W. 4190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
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
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Derichsweiler v. State",
          "cluster_id": 2539048,
          "cite": [
            "348 S.W.3d 906",
            "2011 Tex. Crim. App. LEXIS 112",
            "2011 WL 255299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Savino v. City of New York",
          "cluster_id": 8437485,
          "cite": [
            "331 F.3d 63",
            "2003 U.S. App. LEXIS 10263",
            "2003 WL 21196682"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
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
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Roy L. Williams, Thomas F. O'malley, Andrew G. Massa, Joseph Lombardo",
          "cluster_id": 437518,
          "cite": [
            "737 F.2d 594"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Clark",
          "cluster_id": 1121458,
          "cite": [
            "857 P.2d 1099",
            "5 Cal. 4th 950",
            "22 Cal. Rptr. 2d 689",
            "93 Daily Journal DAR 11122",
            "93 Cal. Daily Op. Serv. 6528",
            "1993 Cal. LEXIS 4179"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Bridges",
          "cluster_id": 1060919,
          "cite": [
            "963 S.W.2d 487",
            "1997 Tenn. LEXIS 642",
            "1997 WL 804620"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cantrell v. Commonwealth",
          "cluster_id": 1344342,
          "cite": [
            "373 S.E.2d 328",
            "7 Va. App. 269",
            "5 Va. Law Rep. 734",
            "1988 Va. App. LEXIS 115"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe v. Broderick",
          "cluster_id": 2967256,
          "cite": [
            "225 F.3d 440",
            "2000 U.S. App. LEXIS 22165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Wallace",
          "cluster_id": 1441674,
          "cite": [
            "910 P.2d 695",
            "80 Haw. 382",
            "1996 Haw. LEXIS 6"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ralph Scopo, Jr.",
          "cluster_id": 665983,
          "cite": [
            "19 F.3d 777",
            "1994 U.S. App. LEXIS 5378",
            "1994 WL 90612"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Serafin Alfonso, Humberto Rayo, Fabian Mora, Primo Antonio Serrano-Tellez",
          "cluster_id": 450644,
          "cite": [
            "759 F.2d 728",
            "18 Fed. R. Serv. 1398",
            "1985 U.S. App. LEXIS 30539"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Andreas:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111013 OR 9429344 OR 9429345 OR 9429346) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03ODI0Mzg0MDAwMDAmcz0xNjc5NDI5JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111013+OR+9429344+OR+9429345+OR+9429346%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 13,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(111013 OR 9429344 OR 9429345 OR 9429346)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NCZzPTc1ODMxOCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111013+OR+9429344+OR+9429345+OR+9429346%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111013 OR 9429344 OR 9429345 OR 9429346)",
        "reviewed": 12,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 12,
        "triage_read": 0,
        "triage_snippet_classified": 12
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111013 OR 9429344 OR 9429345 OR 9429346)",
    "indexed_citing_opinions": 415,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111013,
        "count": 366,
        "count_source": "search"
      },
      {
        "opinion_id": 9429344,
        "count": 54,
        "count_source": "search"
      },
      {
        "opinion_id": 9429345,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429346,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 627,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/illinois-v-andreas.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcwNTMxNjQmcz00ODQxNDkxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111013+OR+9429344+OR+9429345+OR+9429346%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111013,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 109592,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 110100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 110314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 110933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 110974,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 321241,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 376712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 1365780,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111013,
        "cited_id": 2170254,
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
    "date_created": "2026-07-05T07:47:44Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:47:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:47:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:51:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:47:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Illinois v. Andreas

```
<opinion type="majority">
<author id="b814-10">Chief Justice Burger</author>
<p id="Adi">delivered the opinion of the Court.</p>
<p id="Aq8e">The question presented is whether a warrant was required to reopen a sealed container in which contraband drugs had been discovered in an earlier lawful border search, when the container was seized by the police after it had been delivered to respondent under police supervision.</p>
<p id="Api"><page-number citation-index="1" label="767">*767</page-number>hH</p>
<p id="A5Y-p">A large, locked metal container was shipped by air from Calcutta to respondent in Chicago. When the container arrived at O’Hare International Airport, a customs inspector opened it and found a wooden table approximately three feet in diameter and 8 to 10 inches thick. Marihuana was found concealed inside the table.</p>
<p id="A16B">The customs inspector informed the Drug Enforcement Administration of these facts and Special Agent Labek came to the airport later that day. Labek chemically tested the substance contained in the table, confirming that it was marihuana. The table and the container were resealed.</p>
<p id="A37">The next day, Labek put the container in a delivery van and drove to respondent’s building. He was met there by Chicago Police Inspector Lipsek. Posing as delivery men, Labek and Lipsek entered the apartment building and announced they had a package for respondent. Respondent came to the lobby and identified himself. In response to Lipsek’s comment about the weight of the package, respondent answered that it “wasn’t that heavy; that he had packaged it himself, that it only contained a table.” App. 14.</p>
<p id="AukF">At respondent’s request, the officers making the delivery left the container in the hallway outside respondent’s apartment. Labek stationed himself to keep the container in sight and observed respondent pull the container into his apartment. When Lipsek left to secure a warrant to enter and search respondent’s apartment, Labek maintained surveillance of the apartment; he saw respondent leave his apartment, walk to the end of the corridor, look out the window, and then return to the apartment. Labek remained in the building but did not keep the apartment door under constant surveillance.</p>
<p id="A20">Between 30 and 45 minutes after the delivery, but before Lipsek could return with a warrant, respondent reemerged from the apartment with the shipping container and was immediately arrested by Labek and taken to the police station. There, the officers reopened the container and seized the <page-number citation-index="1" label="768">*768</page-number>marihuana found inside the table. No search warrant had been obtained.</p>
<p id="b816-5">Respondent was charged with two counts of possession of controlled substances. Ill. Rev. Stat., ch. 56 <em>Vt, </em>¶¶ 704(e) and 705(e) (1981). Prior to trial, the trial court granted respondent’s motion to suppress the marihuana found in the table, relying on <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span> (1979), and <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977).</p>
<p id="b816-6">On appeal, the Appellate Court of Illinois, First Judicial District, affirmed. <span class="citation" data-id="2170254"><a href="/opinion/2170254/people-v-andreas/" aria-description="Citation for case: People v. Andreas">100 Ill. App. 3d 396</a></span>, <span class="citation" data-id="2170254"><a href="/opinion/2170254/people-v-andreas/" aria-description="Citation for case: People v. Andreas">426 N. E. 2d 1078</a></span> (1981). It relied primarily on <em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span> </em>and <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>in holding that respondent had a legitimate expectation of privacy in the contents of the shipping container. <span class="citation" data-id="2170254"><a href="/opinion/2170254/people-v-andreas/#399" aria-description="Citation for case: People v. Andreas">100 Ill. App. 3d, at 399-401</a></span>, <span class="citation" data-id="2170254"><a href="/opinion/2170254/people-v-andreas/#1080" aria-description="Citation for case: People v. Andreas">426 N. E. 2d, at 1080-1082</a></span>. It recognized that no warrant would be necessary if the police had made a “controlled delivery” of the container following a lawful search, but held that here the police had failed to make a “controlled delivery.”</p>
<p id="b816-7">A “controlled delivery,” in the view of the Illinois court, requires that the police maintain “dominion and control” over the container at all times; only by constant control, in that court’s view, can police be “absolutely sure” that its contents have not changed since the initial search. <span class="citation" data-id="2170254"><a href="/opinion/2170254/people-v-andreas/#402" aria-description="Citation for case: People v. Andreas"><em>Id., </em>at 402</a></span>, <span class="citation" data-id="2170254"><a href="/opinion/2170254/people-v-andreas/#1082" aria-description="Citation for case: People v. Andreas">426 N. E. 2d, at 1082</a></span>. Here, according to the court, the police could not have been “absolutely sure” of the container’s contents for two reasons: (1) Labek was not present when the container was resealed by the customs officers, and thus he knew of its contents only by “hearsay,” <em>ibid., </em><span class="citation" data-id="2170254"><a href="/opinion/2170254/people-v-andreas/#1083" aria-description="Citation for case: People v. Andreas">426 N. E. 2d, at 1083</a></span>, and (2) the container was out of sight for the 30 to 45 minutes while it was in respondent’s apartment; thus, in the court’s view, “there is no certainty that the contents of the package were the same before and after the package was brought into [respondent’s] apartment.” <em><span class="citation" data-id="2170254"><a href="/opinion/2170254/people-v-andreas/" aria-description="Citation for case: People v. Andreas">Ibid.</a></span> </em>Accordingly, the Illinois court held that the warrantless reopening of the container violated the Fourth Amendment.</p>
<p id="b817-4"><page-number citation-index="1" label="769">*769</page-number>We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./459/904/">459 U. S. 904</a></span> (1982), and we reverse.</p>
<p id="b817-5">II</p>
<p id="b817-6">The lawful discovery by common carriers or customs officers of contraband in transit<footnotemark>1</footnotemark> presents law enforcement authorities<footnotemark>2</footnotemark> with an opportunity to identify and prosecute the person or persons responsible for the movement of the contraband. To accomplish this, the police, rather than simply seizing the contraband and destroying it, make a so-called controlled delivery of the container to its consignee, allowing the container to continue its journey to the destination contemplated by the parties. The person dealing in the contraband can then be identified upon taking possession of and asserting dominion over the container.<footnotemark>3</footnotemark></p>
<p id="b818-4"><page-number citation-index="1" label="770">*770</page-number>The typical pattern of a controlled delivery was well described by one court:</p>
<blockquote id="b818-5">“Controlled deliveries of contraband apparently serve a useful function in law enforcement. They most ordinarily occur when a carrier, usually an airline, unexpectedly discovers what seems to be contraband while inspecting luggage to learn the identity of its owner, or when the contraband falls out of a broken or damaged piece of luggage, or when the carrier exercises its inspection privilege because some suspicious circumstance has caused it concern that it may unwittingly be transporting contraband. Frequently, after such a discovery, law enforcement agents restore the contraband to its container, then close or reseal the container, and authorize the carrier to deliver the container to its owner. When the owner appears to take delivery he is arrested and the container with the contraband is seized and then searched a second time for the contraband known to be there.” <em>United States </em>v. <em>Bulgier, </em><span class="citation" data-id="376712"><a href="/opinion/376712/united-states-v-sandra-bulgier/#476" aria-description="Citation for case: United States v. Sandra Bulgier">618 F. 2d 472, 476</a></span> (CA7), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/843/">449 U. S. 843</a></span> (1980).</blockquote>
<p id="b818-6">See also <em>McConnell </em>v. <em>State, </em><span class="citation" data-id="9603228"><a href="/opinion/1365780/mcconnell-v-state/" aria-description="Citation for case: McConnell v. State">595 P. 2d 147</a></span> (Alaska 1979).</p>
<p id="b818-7">Here, a customs agent lawfully discovered drugs concealed in a container and notified the appropriate law enforcement authorities. They took steps to arrange delivery of the container to respondent. A short time after delivering the container, the officers arrested respondent and reseized the container.<footnotemark>4</footnotemark> Respondent claims, and the Illinois court held, that the warrantless reopening of the container following its reseizure violated respondent’s right under the Fourth Amendment “to be secure . . . against unreasonable searches and seizures . . . .” We disagree.</p>
<p id="b819-4"><page-number citation-index="1" label="771">*771</page-number>The Fourth Amendment protects legitimate expectations of privacy rather than simply places. If the inspection by police does not intrude upon a legitimate expectation of privacy, there is no “search” subject to the Warrant Clause. See <em>Walter </em>v. <em>United States, </em><span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#663" aria-description="Citation for case: Walter v. United States">447 U. S. 649, 663-665</a></span> (1980) (Blackmun, J., dissenting). The threshold question, then, is whether an individual has a legitimate expectation of privacy in the contents of a previously lawfully searched container. It is obvious that the privacy interest in the contents of a container diminishes with respect to a container that law enforcement authorities have already lawfully opened and found to contain illicit drugs. No protected privacy interest remains in contraband in a container once government officers lawfully have opened that container and identified its contents as illegal. The simple act of resealing the container to enable the police to make a controlled delivery does not operate to revive or restore the lawfully invaded privacy rights.</p>
<p id="b819-5">This conclusion is supported by the reasoning underlying the “plain-view” doctrine. The plain-view doctrine authorizes seizure of illegal or evidentiary items visible to a police officer whose access to the object has some prior Fourth Amendment justification and who has probable cause to suspect that the item is connected with criminal activity. <em>Texas </em>v. <em>Brown, </em><span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#738" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 738</a></span>, and n. 4, 741-742 (1983) (plurality opinion); <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#746" aria-description="Citation for case: Texas v. Brown"><em>id., </em>at 746</a></span> (Powell, J., concurring in judgment); <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#748" aria-description="Citation for case: Texas v. Brown"><em>id., </em>at 748, 749-750</a></span> (Stevens, J., concurring in judgment). The plain-view doctrine is grounded on the proposition that once police are lawfully in a position to observe an item firsthand, its owner’s privacy interest in that item is lost; the owner may retain the incidents of title and possession but not privacy. That rationale applies here; once a container has been found to a certainty to contain illicit drugs,<footnotemark>5</footnotemark> the contra<page-number citation-index="1" label="772">*772</page-number>band becomes like objects physically within the plain view of the police, and the claim to privacy is lost. Consequently, the subsequent reopening of the container is not a “search” within the intendment of the Fourth Amendment.</p>
<p id="b820-5">However, the rigors and contingencies inescapable in an investigation into illicit drug traffic often make “perfect” controlled deliveries and the “absolute certainty” demanded by the Illinois court impossible to attain. Conducting such a surveillance undetected is likely to render it virtually impossible for police so perfectly to time their movements as to avoid detection and also be able to arrest the owner and reseize the container the instant he takes possession. Not infrequently, police may lose sight of the container they are trailing, as is the risk in the pursuit of a car or vessel.</p>
<p id="b820-6">During such a gap in surveillance, it is possible that the container will be put to other uses — for example, the contraband may be removed or other items may be placed inside. The likelihood that this will happen depends on all the facts and circumstances, including the nature and uses of the container, the length of the break in surveillance, and the setting in which the events occur. However, the mere fact that the police may be less than 100% certain of the contents of the container is insufficient to create a protected interest in the privacy of the container. See <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 764-765, n. 13</a></span>. The issue then becomes at what point after an interruption of control or surveillance, courts should recognize the individual’s expectation of privacy in the container as a legitimate right protected by the Fourth Amendment proscription against unreasonable searches.</p>
<p id="b820-7">In fashioning a standard, we must be mindful of three Fourth Amendment principles. First, the standard should be workable for application by rank-and-file, trained police officers. See <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#458" aria-description="Citation for case: New York v. Belton">453 U. S. 454, 458-460</a></span> (1981); <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#821" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 821</a></span> (1982). <page-number citation-index="1" label="773">*773</page-number>Second, it should be reasonable; for example, it would be absurd to recognize as legitimate an expectation of privacy where there is only a minimal probability that the contents of a particular container had been changed. Third, the standard should be objective, not dependent on the belief of individual police officers. See <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 21-22</a></span> (1968). A workable, objective standard that limits the risk of intrusion on legitimate privacy interests is whether there is a substantial likelihood that the contents of the container have been changed during the gap in surveillance. We hold that absent a substantial likelihood that the contents have been changed, there is no legitimate expectation of privacy in the contents of a container previously opened under lawful authority.</p>
<p id="b821-5">Ill</p>
<p id="b821-6">Applying these principles, we conclude there was no substantial likelihood here that the contents of the shipping container were changed during the brief period that it was out of sight of the surveilling officer. The unusual size of the container, its specialized purpose, and the relatively short break in surveillance combine to make it substantially unlikely that the respondent removed the table or placed new items inside the container while it was in his apartment. Thus, reopening the container did not intrude on any legitimate expectation of privacy and did not violate the Fourth Amendment.</p>
<p id="b821-7">The judgment of the Illinois Appellate Court is reversed, and the case is remanded for proceedings not inconsistent with this opinion.</p>
<p id="b821-8">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b817-7"> Common carriers have a common-law right to inspect packages they accept for shipment, based on their duty to refrain from carrying contraband. See <em>United States </em>v. <em>Pryba, </em>163 U. S. App. D. C. 389, 397-398, <span class="citation" data-id="321241"><a href="/opinion/321241/united-states-v-dennis-e-pryba/#399" aria-description="Citation for case: United States v. Dennis E. Pryba">502 F. 2d 391, 399-400</a></span> (1974). Although sheer volume prevents systematic inspection of all or even a large percentage of the cargo in their care, see, <em>e. g., McConnell </em>v. <em>State, </em><span class="citation" data-id="9603228"><a href="/opinion/1365780/mcconnell-v-state/#148" aria-description="Citation for case: McConnell v. State">595 P. 2d 147, 148</a></span>, and n. 1 (Alaska 1979), carriers do discover contraband in a variety of circumstances. Similarly, although the United States Government has the undoubted right to inspect all incoming goods at a port of entry, see <em>United States </em>v. <em>Ramsey, </em><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#616" aria-description="Citation for case: United States v. Ramsey">431 U. S. 606, 616-619</a></span> (1977), it would be impossible for customs officers to inspect every package. In the course of selective inspections, they inevitably discover contraband in transit.</p>
</footnote>
<footnote label="2">
<p id="b817-8"> When common carriers discover contraband in packages entrusted to their care, it is routine for them to notify the appropriate authorities. The arrival of police on the scene to confirm the presence of contraband and to determine what to do with it does not convert the private search by the carrier into a government search subject to the Fourth Amendment. <em>E. g., United States </em>v. <em>Edwards, </em><span class="citation" data-id="368278"><a href="/opinion/368278/united-states-v-raymond-edwards-united-states-of-america-v-david/" aria-description="Citation for case: United States v. Raymond Edwards, United States of...">602 F. 2d 458</a></span> (CA1 1979).</p>
</footnote>
<footnote label="3">
<p id="b817-9"> Of course, the mere fact that the consignee takes possession of the container would not alone establish guilt of illegal possession or importation of contraband. The recipient of the package would be free to offer evidence that the nature of the contents were unknown to him; the nature of the contents and the recipient’s awareness of them would be issues for the fact-finder.</p>
</footnote>
<footnote label="4">
<p id="b818-8"> Respondent has not claimed that the warrantless seizure of the container from the hallway of his apartment house following his arrest violated the Fourth Amendment; his claim goes only to the warrantless reopening of the container.</p>
</footnote>
<footnote label="5">
<p id="b819-6"> The Illinois Court held that Labek’s absence when the container was resealed by customs officers somehow made less than certain his knowledge of the container’s contents. This was plain error: where law enforcement authorities are cooperating in an investigation, as here, the knowl<page-number citation-index="1" label="772">*772</page-number>edge of one is presumed shared by all. See <em>Whiteley </em>v. <em>Warden, </em><span class="citation multiple-matches"><a href="/c/U.%20S./401/660/">401 U. S. 660</a></span>, 568 (1971).</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Illinois v. Caballes.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Illinois v. Caballes"
type: case
citation: "543 U.S. 405 (2005)"
parallel_cite: "125 S. Ct. 834; 160 L. Ed. 2d 842"
neutral_cite: 2005 U.S. LEXIS 769
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2005
date_decided: 2005-01-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2005-01-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Illinois v. Caballes
  varies_by_point: false
  scope_note: "Good law. Rodriguez v. United States (2015) applied the no-prolongation principle (a stop may not be extended even briefly for a dog sniff absent reasonable suspicion). Florida v. Jardines (2013) held a dog sniff at a home's curtilage is a search — a context boundary, not an overruling of the vehicle holding."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/137742/illinois-v-caballes/"
  cluster_id: 137742
  opinion_id: 137742
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Key — Anchor"
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Place]]", "[[Rodriguez v. United States]]", "[[Florida v. Jardines]]", "[[Kyllo v. United States]]", "[[Florida v. Harris]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "dog-sniff", "traffic-stop", "contraband"]
holding: "A dog sniff during a lawful traffic stop that does not prolong the stop needs no independent suspicion, because it reveals only contraband and does not implicate legitimate privacy interests."
lake:
  record_id: Illinois v. Caballes
  status: verified
  projected_at: 2026-07-09
---

# Illinois v. Caballes

*543 U.S. 405 (2005)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
An Illinois trooper stopped Caballes for speeding. While the trooper wrote a warning ticket, a second trooper arrived and walked a drug-detection dog around the car. The dog alerted at the trunk; a search revealed marijuana. The entire stop lasted under ten minutes and was not prolonged by the sniff. Caballes argued the dog sniff converted a routine traffic stop into an unjustified drug investigation.

## Issue
Whether the Fourth Amendment requires reasonable, articulable suspicion to justify a dog sniff of a vehicle's exterior conducted during an otherwise lawful traffic stop.

## Rule
A lawful stop must not be prolonged for the sniff: "A seizure that is justified solely by the interest in issuing a warning ticket to the driver can become unlawful if it is prolonged beyond the time reasonably required to complete that mission." — 543 U.S. at 407. ^pin-407

But a non-prolonging sniff invades no protected interest: "the use of a well-trained narcotics-detection dog — one that 'does not expose noncontraband items that otherwise would remain hidden from public view,' *Place*, 462 U.S., at 707 — during a lawful traffic stop, generally does not implicate legitimate privacy interests." — *Id.* at 409. ^pin-409

The holding: "A dog sniff conducted during a concededly lawful traffic stop that reveals no information other than the location of a substance that no individual has any right to possess does not violate the Fourth Amendment." — [*Id.* at 410](https://www.courtlistener.com/opinion/137742/illinois-v-caballes/#:~:text=A%20dog%20sniff%20conducted%20during). ^pin-410

## Application
The traffic stop was lawful at its inception and was not extended by the dog sniff, which occurred while the warning ticket was being written. Because a reliable narcotics dog discloses only the presence or absence of contraband — in which no person has a legitimate privacy interest — the sniff of the car's exterior implicated no constitutionally cognizable privacy interest and required no independent reasonable suspicion. The alert then supplied probable cause for the trunk search.

## Conclusion
A dog sniff during an unprolonged, lawful traffic stop is not a Fourth Amendment search and needs no separate suspicion; the marijuana was admissible. *Caballes* anchors the vehicle dog-sniff rule while preserving the limit that the stop may not be extended to conduct it.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Applies the dog-sniff reasoning of [[United States v. Place]] and contrasts the home-interior technology case [[Kyllo v. United States]]. The no-prolongation limit is enforced by [[Rodriguez v. United States]]; the home-[[Curtilage|curtilage]] boundary is set by [[Florida v. Jardines]]; dog-reliability/probable-cause questions are addressed in [[Florida v. Harris]].

## Appears on
- [[Traffic Stops]] — *Key — Anchor*
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*

## Sources
- *Illinois v. Caballes*, 543 U.S. 405 (2005) — https://www.courtlistener.com/opinion/137742/illinois-v-caballes/ — pinpoints: 407, 409, 410.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1e85f615a22e7ac8", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Illinois v. Caballes"}, "payload": {"all": [{"cite": "543 U.S. 405", "page": "405", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "543"}, {"cite": "125 S. Ct. 834", "page": "834", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "125"}, {"cite": "160 L. Ed. 2d 842", "page": "842", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "160"}, {"cite": "2005 U.S. LEXIS 769", "page": "769", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2005"}], "display": "543 U.S. 405", "official": {"cite": "543 U.S. 405", "page": "405", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "543"}, "official_selection_present": true, "record_id": "Illinois v. Caballes"}}
{"assertion_id": "8abb71bc53c47c90", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-410", "record_id": "Illinois v. Caballes"}, "payload": {"fragment": "#:~:text=A%20dog%20sniff%20conducted%20during", "page": null, "pin_id": "pin-410", "pinpoint_status": "star-verified", "quote": "A dog sniff conducted during a concededly lawful traffic stop that reveals no information other than the location of a substance that no individual has any right to possess does not violate the Fourth Amendment.", "quote_fidelity": "matched", "record_id": "Illinois v. Caballes", "star_marker": "410"}}
{"assertion_id": "8f50634be156f56d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-407", "record_id": "Illinois v. Caballes"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-407", "pinpoint_status": "slip-only", "quote": "--- # Illinois v. Caballes *543 U.S. 405 (2005)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An Illinois trooper stopped Caballes for speeding. While the trooper wrote a warning ticket, a second trooper arrived and walked a drug-detection dog around the car. The dog alerted at the trunk; a search revealed marijuana. The entire stop lasted under ten minutes and was not prolonged by the sniff. Caballes argued the dog sniff converted a routine traffic stop into an unjustified drug investigation. ## Issue Whether the Fourth Amendment requires reasonable, articulable suspicion to justify a dog sniff of a vehicle's exterior conducted during an otherwise lawful traffic stop. ## Rule A lawful stop must not be prolonged for the sniff:", "quote_fidelity": "mismatch", "record_id": "Illinois v. Caballes", "star_marker": null}}
{"assertion_id": "eefe1005106791d3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-409", "record_id": "Illinois v. Caballes"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-409", "pinpoint_status": "slip-only", "quote": "the use of a well-trained narcotics-detection dog — one that 'does not expose noncontraband items that otherwise would remain hidden from public view,' *Place*, 462 U.S., at 707 — during a lawful traffic stop, generally does not implicate legitimate privacy interests.", "quote_fidelity": "mismatch", "record_id": "Illinois v. Caballes", "star_marker": null}}
{"assertion_id": "22e384ccd2d7ec67", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Illinois v. Caballes"}, "payload": {"as_of_content": "2005-01-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Illinois v. Caballes", "scope_note": "Good law. Rodriguez v. United States (2015) applied the no-prolongation principle (a stop may not be extended even briefly for a dog sniff absent reasonable suspicion). Florida v. Jardines (2013) held a dog sniff at a home's curtilage is a search — a context boundary, not an overruling of the vehicle holding.", "varies_by_point": false}}
```

### lake record — Illinois v. Caballes

```json
{
  "schema_version": "s2.v1",
  "record_id": "Illinois v. Caballes",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Illinois v. Caballes",
    "case_name_short": "Caballes",
    "case_name_full": "Illinois v. Caballes",
    "input_case_name": "Illinois v. Caballes",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2005-01-24",
    "year": 2005,
    "docket": null,
    "cluster_id": 137742,
    "lead_opinion_id": 137742,
    "sibling_ids": [
      137742,
      9434728,
      9434729,
      9434730
    ],
    "absolute_url": "/opinion/137742/illinois-v-caballes/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "543 U.S. 405",
      "volume": "543",
      "reporter": "U.S.",
      "page": "405",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "125 S. Ct. 834",
        "volume": "125",
        "reporter": "S. Ct.",
        "page": "834",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "160 L. Ed. 2d 842",
        "volume": "160",
        "reporter": "L. Ed. 2d",
        "page": "842",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2005 U.S. LEXIS 769",
        "volume": "2005",
        "reporter": "U.S. LEXIS",
        "page": "769",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "543 U.S. 405",
        "volume": "543",
        "reporter": "U.S.",
        "page": "405",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "125 S. Ct. 834",
        "volume": "125",
        "reporter": "S. Ct.",
        "page": "834",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "160 L. Ed. 2d 842",
        "volume": "160",
        "reporter": "L. Ed. 2d",
        "page": "842",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2005 U.S. LEXIS 769",
        "volume": "2005",
        "reporter": "U.S. LEXIS",
        "page": "769",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "543 U.S. 405",
    "official_selection": {
      "court_class": "scotus",
      "selected": "543 U.S. 405",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-407",
      "page": null,
      "quote": "--- # Illinois v. Caballes *543 U.S. 405 (2005)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An Illinois trooper stopped Caballes for speeding. While the trooper wrote a warning ticket, a second trooper arrived and walked a drug-detection dog around the car. The dog alerted at the trunk; a search revealed marijuana. The entire stop lasted under ten minutes and was not prolonged by the sniff. Caballes argued the dog sniff converted a routine traffic stop into an unjustified drug investigation. ## Issue Whether the Fourth Amendment requires reasonable, articulable suspicion to justify a dog sniff of a vehicle's exterior conducted during an otherwise lawful traffic stop. ## Rule A lawful stop must not be prolonged for the sniff:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-409",
      "page": null,
      "quote": "the use of a well-trained narcotics-detection dog \u2014 one that 'does not expose noncontraband items that otherwise would remain hidden from public view,' *Place*, 462 U.S., at 707 \u2014 during a lawful traffic stop, generally does not implicate legitimate privacy interests.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-410",
      "page": null,
      "quote": "A dog sniff conducted during a concededly lawful traffic stop that reveals no information other than the location of a substance that no individual has any right to possess does not violate the Fourth Amendment.",
      "star_marker": "410",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 11448,
      "fragment": "#:~:text=A%20dog%20sniff%20conducted%20during",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2005-01-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Illinois v. Caballes",
    "varies_by_point": false,
    "scope_note": "Good law. Rodriguez v. United States (2015) applied the no-prolongation principle (a stop may not be extended even briefly for a dog sniff absent reasonable suspicion). Florida v. Jardines (2013) held a dog sniff at a home's curtilage is a search \u2014 a context boundary, not an overruling of the vehicle holding.",
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
        "journal_ref": "Illinois v. Caballes:lane1_negative"
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
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
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
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
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
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Muehler v. Mena",
          "cluster_id": 142878,
          "cite": [
            "161 L. Ed. 2d 299",
            "125 S. Ct. 1465",
            "544 U.S. 93",
            "2005 U.S. LEXIS 2755"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Chavez-Barragan",
          "cluster_id": 4260741,
          "cite": [
            "2016 CO 66",
            "379 P.3d 330",
            "2016 WL 5375502"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Erickson Meko Campbell",
          "cluster_id": 6357475,
          "cite": [
            "26 F.4th 860"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
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
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Branch",
          "cluster_id": 1026476,
          "cite": [
            "537 F.3d 328",
            "2008 U.S. App. LEXIS 17710",
            "2008 WL 3854500"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Felders v. Malcom",
          "cluster_id": 2679716,
          "cite": [
            "755 F.3d 870",
            "2014 WL 2782368",
            "2014 U.S. App. LEXIS 11627"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kevin M. Clark v. State of Indiana",
          "cluster_id": 1041668,
          "cite": [
            "994 N.E.2d 252",
            "2013 WL 5228498",
            "2013 Ind. LEXIS 700"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Caballes",
          "cluster_id": 2192166,
          "cite": [
            "851 N.E.2d 26",
            "221 Ill. 2d 282",
            "303 Ill. Dec. 128",
            "2006 Ill. LEXIS 625"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Elias",
          "cluster_id": 2539936,
          "cite": [
            "339 S.W.3d 667",
            "2011 Tex. Crim. App. LEXIS 448",
            "2011 WL 1267248"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
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
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4621444,
          "cite": [
            "2019 CO 36",
            "446 P.3d 397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin Davis (03-1451) and Keith Presley (03-1621)",
          "cluster_id": 792556,
          "cite": [
            "430 F.3d 345",
            "2005 U.S. App. LEXIS 25124",
            "2005 WL 3108503"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bew",
          "cluster_id": 2231907,
          "cite": [
            "886 N.E.2d 1002",
            "228 Ill. 2d 122",
            "319 Ill. Dec. 878",
            "2008 Ill. LEXIS 291"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Maynard",
          "cluster_id": 152441,
          "cite": [
            "615 F.3d 544",
            "392 U.S. App. D.C. 291",
            "2010 U.S. App. LEXIS 16417",
            "2010 WL 3063788"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lerma v. State",
          "cluster_id": 6241263,
          "cite": [
            "543 S.W.3d 184"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hernandez v. United States",
          "cluster_id": 4661436,
          "cite": [
            "939 F.3d 191"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cosby",
          "cluster_id": 2105166,
          "cite": [
            "898 N.E.2d 603",
            "231 Ill. 2d 262",
            "325 Ill. Dec. 556",
            "2008 Ill. LEXIS 890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
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
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Leyva",
          "cluster_id": 891705,
          "cite": [
            "2011 NMSC 9",
            "250 P.3d 861",
            "149 N.M. 435",
            "2011 NMSC 009"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Farrior",
          "cluster_id": 1026364,
          "cite": [
            "535 F.3d 210",
            "2008 U.S. App. LEXIS 16575",
            "2008 WL 2971779"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William Windham v. Harris County, Texas",
          "cluster_id": 4442638,
          "cite": [
            "875 F.3d 229"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Weaver",
          "cluster_id": 2546485,
          "cite": [
            "349 S.W.3d 521",
            "2011 Tex. Crim. App. LEXIS 1320",
            "2011 WL 4715178"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Caballes:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(137742 OR 9434728 OR 9434729 OR 9434730) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTkzOTkzNjAwMDAwJnM9NDgzMjU4NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28137742+OR+9434728+OR+9434729+OR+9434730%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 1,
        "triage_snippet_classified": 199
      },
      "lane2_top_cited": {
        "query": "cites:(137742 OR 9434728 OR 9434729 OR 9434730)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjImcz0yNjMxMTA5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28137742+OR+9434728+OR+9434729+OR+9434730%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(137742 OR 9434728 OR 9434729 OR 9434730)",
        "reviewed": 121,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 121,
        "triage_read": 1,
        "triage_snippet_classified": 120
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(137742 OR 9434728 OR 9434729 OR 9434730)",
    "indexed_citing_opinions": 1117,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 137742,
        "count": 818,
        "count_source": "search"
      },
      {
        "opinion_id": 9434728,
        "count": 312,
        "count_source": "search"
      },
      {
        "opinion_id": 9434729,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434730,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2012,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/illinois-v-caballes.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyOTYxNjcmcz0xMDM3NTI0OSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28137742+OR+9434728+OR+9434729+OR+9434730%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 137742,
        "cited_id": 76430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 111667,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 112459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 112631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 118250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 118354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 118391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 136990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 155490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 164282,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 485654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 671474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 749428,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 775355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 1882050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 2038990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 2106553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137742,
        "cited_id": 2207633,
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
    "date_created": "2026-07-05T07:51:31Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:51:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:51:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:54:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:51:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Illinois v. Caballes

```
<div>
<center><b><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">543 U.S. 405</a></span> (2005)</b></center>
<center><h1>ILLINOIS<br>
v.<br>
CABALLES.</h1></center>
<center>No. 03-923.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 10, 2004.</center>
<center>Decided January 24, 2005.</center>
CERTIORARI TO THE SUPREME COURT OF ILLINOIS.
<p>STEVENS, J., delivered the opinion of the Court, in which O'CONNOR, SCALIA, KENNEDY, THOMAS, and BREYER, JJ., joined. SOUTER, J., filed a dissenting opinion, <i>post,</i> p. 410. GINSBURG, J., filed a dissenting opinion, in which SOUTER, J., joined, <i>post,</i> p. 417. REHNQUIST, C. J., took no part in the decision of the case.</p>
<p><i>Lisa Madigan,</i> Attorney General of Illinois, argued the cause for petitioner. With her on the briefs were <i>Gary Feinerman,</i> Solicitor General, and <i>Linda D. Woloshin</i> and <i>Mary Fleming,</i> Assistant Attorneys General.</p>
<p><i>Assistant Attorney General Wray</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were former <i>Solicitor General Olson, Deputy Solicitor General Dreeben, James A. Feldman,</i> and <i>John A. Drennan.</i></p>
<p><span class="star-pagination">*406</span> <i>Ralph E. Meczyk</i> argued the cause for respondent. With him on the brief was <i>Lawrence H. Hyman.</i><sup>[*]</sup></p>
<p>JUSTICE STEVENS delivered the opinion of the Court.</p>
<p>Illinois State Trooper Daniel Gillette stopped respondent for speeding on an interstate highway. When Gillette radioed the police dispatcher to report the stop, a second trooper, Craig Graham, a member of the Illinois State Police Drug Interdiction Team, overheard the transmission and immediately headed for the scene with his narcotics-detection dog. When they arrived, respondent's car was on the shoulder of the road and respondent was in Gillette's vehicle. While Gillette was in the process of writing a warning ticket, Graham walked his dog around respondent's car. The dog alerted at the trunk. Based on that alert, the officers searched the trunk, found marijuana, and arrested respondent. The entire incident lasted less than 10 minutes.</p>
<p><span class="star-pagination">*407</span> Respondent was convicted of a narcotics offense and sentenced to 12 years' imprisonment and a $256,136 fine. The trial judge denied his motion to suppress the seized evidence and to quash his arrest. He held that the officers had not unnecessarily prolonged the stop and that the dog alert was sufficiently reliable to provide probable cause to conduct the search. Although the Appellate Court affirmed, the Illinois Supreme Court reversed, concluding that because the canine sniff was performed without any "`specific and articulable facts'" to suggest drug activity, the use of the dog "unjustifiably enlarg[ed] the scope of a routine traffic stop into a drug investigation." <span class="citation multiple-matches"><a href="/c/Ill.%202d/207/504/">207 Ill. 2d 504</a></span>, 510, <span class="citation multiple-matches"><a href="/c/N.%20E.%202d/802/202/">802 N. E. 2d 202</a></span>, 205 (2003).</p>
<p>The question on which we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./541/972/">541 U. S. 972</a></span> (2004), is narrow: "Whether the Fourth Amendment requires reasonable, articulable suspicion to justify using a drug-detection dog to sniff a vehicle during a legitimate traffic stop." Pet. for Cert. i. Thus, we proceed on the assumption that the officer conducting the dog sniff had no information about respondent except that he had been stopped for speeding; accordingly, we have omitted any reference to facts about respondent that might have triggered a modicum of suspicion.</p>
<p>Here, the initial seizure of respondent when he was stopped on the highway was based on probable cause and was concededly lawful. It is nevertheless clear that a seizure that is lawful at its inception can violate the Fourth Amendment if its manner of execution unreasonably infringes interests protected by the Constitution. <i>United States</i> v. <i>Jacobsen,</i> <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#124" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 124</a></span> (1984). A seizure that is justified solely by the interest in issuing a warning ticket to the driver can become unlawful if it is prolonged beyond the time reasonably required to complete that mission. In an earlier case involving a dog sniff that occurred during an unreasonably prolonged traffic stop, the Illinois Supreme Court held that use of the dog and the subsequent discovery <span class="star-pagination">*408</span> of contraband were the product of an unconstitutional seizure. <i>People</i> v. <i>Cox,</i> <span class="citation" data-id="9526758"><a href="/opinion/2038990/people-v-cox/" aria-description="Citation for case: People v. Cox">202 Ill. 2d 462</a></span>, <span class="citation" data-id="9526758"><a href="/opinion/2038990/people-v-cox/" aria-description="Citation for case: People v. Cox">782 N. E. 2d 275</a></span> (2002). We may assume that a similar result would be warranted in this case if the dog sniff had been conducted while respondent was being unlawfully detained.</p>
<p>In the state-court proceedings, however, the judges carefully reviewed the details of Officer Gillette's conversations with respondent and the precise timing of his radio transmissions to the dispatcher to determine whether he had improperly extended the duration of the stop to enable the dog sniff to occur. We have not recounted those details because we accept the state court's conclusion that the duration of the stop in this case was entirely justified by the traffic offense and the ordinary inquiries incident to such a stop.</p>
<p>Despite this conclusion, the Illinois Supreme Court held that the initially lawful traffic stop became an unlawful seizure solely as a result of the canine sniff that occurred outside respondent's stopped car. That is, the court characterized the dog sniff as the cause rather than the consequence of a constitutional violation. In its view, the use of the dog converted the citizen-police encounter from a lawful traffic stop into a drug investigation, and because the shift in purpose was not supported by any reasonable suspicion that respondent possessed narcotics, it was unlawful. In our view, conducting a dog sniff would not change the character of a traffic stop that is lawful at its inception and otherwise executed in a reasonable manner, unless the dog sniff itself infringed respondent's constitutionally protected interest in privacy. Our cases hold that it did not.</p>
<p>Official conduct that does not "compromise any legitimate interest in privacy" is not a search subject to the Fourth Amendment. <i>Jacobsen,</i> <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#123" aria-description="Citation for case: United States v. Jacobsen">466 U. S., at 123</a></span>. We have held that any interest in possessing contraband cannot be deemed "legitimate," and thus, governmental conduct that <i>only</i> reveals the possession of contraband "compromises no legitimate privacy interest." <i><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">Ibid.</a></span></i> This is because the expectation <span class="star-pagination">*409</span> "that certain facts will not come to the attention of the authorities" is not the same as an interest in "privacy that society is prepared to consider reasonable." <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#122" aria-description="Citation for case: United States v. Jacobsen"><i>Id.,</i> at 122</a></span> (punctuation omitted). In <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983), we treated a canine sniff by a well-trained narcotics-detection dog as <i>"sui generis"</i> because it "discloses only the presence or absence of narcotics, a contraband item." <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place"><i>Id.,</i> at 707</a></span>; see also <i>Indianapolis</i> v. <i>Edmond,</i> <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#40" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S. 32, 40</a></span> (2000). Respondent likewise concedes that "drug sniffs are designed, and if properly conducted are generally likely, to reveal only the presence of contraband." Brief for Respondent 17. Although respondent argues that the error rates, particularly the existence of false positives, call into question the premise that drug-detection dogs alert only to contraband, the record contains no evidence or findings that support his argument. Moreover, respondent does not suggest that an erroneous alert, in and of itself, reveals any legitimate private information, and, in this case, the trial judge found that the dog sniff was sufficiently reliable to establish probable cause to conduct a full-blown search of the trunk.</p>
<p>Accordingly, the use of a well-trained narcotics-detection dogone that "does not expose noncontraband items that otherwise would remain hidden from public view," <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> 462 U. S., at 707during a lawful traffic stop, generally does not implicate legitimate privacy interests. In this case, the dog sniff was performed on the exterior of respondent's car while he was lawfully seized for a traffic violation. Any intrusion on respondent's privacy expectations does not rise to the level of a constitutionally cognizable infringement.</p>
<p>This conclusion is entirely consistent with our recent decision that the use of a thermal-imaging device to detect the growth of marijuana in a home constituted an unlawful search. <i>Kyllo</i> v. <i>United States,</i> <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">533 U. S. 27</a></span> (2001). Critical to that decision was the fact that the device was capable of detecting lawful activityin that case, intimate details in a <span class="star-pagination">*410</span> home, such as "at what hour each night the lady of the house takes her daily sauna and bath." <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/#38" aria-description="Citation for case: Kyllo v. United States"><i>Id.,</i> at 38</a></span>. The legitimate expectation that information about perfectly lawful activity will remain private is categorically distinguishable from respondent's hopes or expectations concerning the nondetection of contraband in the trunk of his car. A dog sniff conducted during a concededly lawful traffic stop that reveals no information other than the location of a substance that no individual has any right to possess does not violate the Fourth Amendment.</p>
<p>The judgment of the Illinois Supreme Court is vacated, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>THE CHIEF JUSTICE took no part in the decision of this case.</p>
<p>JUSTICE SOUTER, dissenting.</p>
<p>I would hold that using the dog for the purposes of determining the presence of marijuana in the car's trunk was a search unauthorized as an incident of the speeding stop and unjustified on any other ground. I would accordingly affirm the judgment of the Supreme Court of Illinois, and I respectfully dissent.</p>
<p>In <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983), we categorized the sniff of the narcotics-seeking dog as <i>"sui generis"</i> under the Fourth Amendment and held it was not a search. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place"><i>Id.,</i> at 707</a></span>. The classification rests not only upon the limited nature of the intrusion, but on a further premise that experience has shown to be untenable, the assumption that trained sniffing dogs do not err. What we have learned about the fallibility of dogs in the years since <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> was decided would itself be reason to call for reconsidering <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i>'s decision against treating the intentional use of a trained dog as a search. The portent of this very case, however, adds insistence <span class="star-pagination">*411</span> to the call, for an uncritical adherence to <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> would render the Fourth Amendment indifferent to suspicionless and indiscriminate sweeps of cars in parking garages and pedestrians on sidewalks; if a sniff is not preceded by a seizure subject to Fourth Amendment notice, it escapes Fourth Amendment review entirely unless it is treated as a search. We should not wait for these developments to occur before rethinking <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i>'s analysis, which invites such untoward consequences.<sup>[1]</sup></p>
<p>At the heart both of <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> and the Court's opinion today is the proposition that sniffs by a trained dog are <i>sui generis</i> because a reaction by the dog in going alert is a response to nothing but the presence of contraband.<sup>[2]</sup> See <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">ibid.</a></span></i> ("[T]he sniff discloses only the presence or absence of narcotics, a contraband item"); <i>ante,</i> at 409 (assuming that "a canine sniff by a well-trained narcotics-detection dog" will only reveal "`the presence or absence of narcotics, a contraband item'" (quoting <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place"><i>Place, supra,</i> at 707</a></span>)). Hence, the argument goes, because the sniff can only reveal the presence of items devoid of any legal use, the sniff "does not implicate legitimate privacy interests" and is not to be treated as a search. <i>Ante,</i> at 409.</p>
<p>The infallible dog, however, is a creature of legal fiction. Although the Supreme Court of Illinois did not get into the sniffing averages of drug dogs, their supposed infallibility is belied by judicial opinions describing well-trained animals sniffing and alerting with less than perfect accuracy, whether <span class="star-pagination">*412</span> owing to errors by their handlers, the limitations of the dogs themselves, or even the pervasive contamination of currency by cocaine. See, <i>e. g., </i><i>United States</i> v. <i>Kennedy,</i> <span class="citation" data-id="749428"><a href="/opinion/749428/united-states-v-keiran-george-kennedy/#1378" aria-description="Citation for case: United States v. Keiran George Kennedy">131 F. 3d 1371, 1378</a></span> (CA10 1997) (describing a dog that had a 71% accuracy rate); <i>United States</i> v. <i>Scarborough,</i> <span class="citation" data-id="155490"><a href="/opinion/155490/united-states-v-scarborough/#1378" aria-description="Citation for case: United States v. Scarborough">128 F. 3d 1373, 1378, n. 3</a></span> (CA10 1997) (describing a dog that erroneously alerted 4 times out of 19 while working for the postal service and 8% of the time over its entire career); <i>United States</i> v. <i>Limares,</i> <span class="citation" data-id="775355"><a href="/opinion/775355/united-states-v-luis-c-limares/#797" aria-description="Citation for case: United States v. Luis C. Limares">269 F. 3d 794, 797</a></span> (CA7 2001) (accepting as reliable a dog that gave false positives between 7% and 38% of the time); <i>Laime</i> v. <i>State,</i> <span class="citation" data-id="9691597"><a href="/opinion/1882050/laime-v-state/#159" aria-description="Citation for case: Laime v. State">347 Ark. 142, 159</a></span>, <span class="citation" data-id="9691597"><a href="/opinion/1882050/laime-v-state/#476" aria-description="Citation for case: Laime v. State">60 S. W. 3d 464, 476</a></span> (2001) (speaking of a dog that made between 10 and 50 errors); <i>United States</i> v. <i>$242,484.00,</i> <span class="citation" data-id="8408430"><a href="/opinion/8437934/united-states-v-24248400/#511" aria-description="Citation for case: United States v. $242,484.00">351 F. 3d 499, 511</a></span> (CA11 2003) (noting that because as much as 80% of all currency in circulation contains drug residue, a dog alert "is of little value"), vacated on other grounds by rehearing en banc, <span class="citation" data-id="76430"><a href="/opinion/76430/united-states-v-24240400/" aria-description="Citation for case: United States v. $242,404.00">357 F. 3d 1225</a></span> (CA11 2004); <i>United States</i> v. <i>Carr,</i> <span class="citation" data-id="9486834"><a href="/opinion/671474/united-states-v-robert-joseph-carr-jr-in-no-93-1376-united-states-of/#1214" aria-description="Citation for case: United States v. Robert Joseph Carr, Jr., in No. 93-1376....">25 F. 3d 1194, 1214-1217</a></span> (CA3 1994) (Becker, J., concurring in part and dissenting in part) ("[A] substantial portion of United States currency ... is tainted with sufficient traces of controlled substances to cause a trained canine to alert to their presence"). Indeed, a study cited by Illinois in this case for the proposition that dog sniffs are "generally reliable" shows that dogs in artificial testing situations return false positives anywhere from 12.5% to 60% of the time, depending on the length of the search. See Reply Brief for Petitioner 13; Federal Aviation Admin., K. Garner et al., Duty Cycle of the Detector Dog: A Baseline Study 12 (Apr. 2001) (prepared by the Auburn U. Inst. for Biological Detection Systems). In practical terms, the evidence is clear that the dog that alerts hundreds of times will be wrong dozens of times.</p>
<p>Once the dog's fallibility is recognized, however, that ends the justification claimed in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> for treating the sniff as <i>sui generis</i> under the Fourth Amendment: the sniff alert does not necessarily signal hidden contraband, and opening the container or enclosed space whose emanations the dog has <span class="star-pagination">*413</span> sensed will not necessarily reveal contraband or any other evidence of crime. This is not, of course, to deny that a dog's reaction may provide reasonable suspicion, or probable cause, to search the container or enclosure; the Fourth Amendment does not demand certainty of success to justify a search for evidence or contraband. The point is simply that the sniff and alert cannot claim the certainty that <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> assumed, both in treating the deliberate use of sniffing dogs as <i>sui generis</i> and then taking that characterization as a reason to say they are not searches subject to Fourth Amendment scrutiny. And when that aura of uniqueness disappears, there is no basis in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i>'s reasoning, and no good reason otherwise, to ignore the actual function that dog sniffs perform. They are conducted to obtain information about the contents of private spaces beyond anything that human senses could perceive, even when conventionally enhanced. The information is not provided by independent third parties beyond the reach of constitutional limitations, but gathered by the government's own officers in order to justify searches of the traditional sort, which may or may not reveal evidence of crime but will disclose anything meant to be kept private in the area searched. Thus in practice the government's use of a trained narcotics dog functions as a limited search to reveal undisclosed facts about private enclosures, to be used to justify a further and complete search of the enclosed area. And given the fallibility of the dog, the sniff is the first step in a process that may disclose "intimate details" without revealing contraband, just as a thermal-imaging device might do, as described in <i>Kyllo</i> v. <i>United States,</i> <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">533 U. S. 27</a></span> (2001).<sup>[3]</sup></p>
<p><span class="star-pagination">*414</span> It makes sense, then, to treat a sniff as the search that it amounts to in practice, and to rely on the body of our Fourth Amendment cases, including <i><span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">Kyllo</a></span>,</i> in deciding whether such a search is reasonable. As a general proposition, using a dog to sniff for drugs is subject to the rule that the object of enforcing criminal laws does not, without more, justify suspicionless Fourth Amendment intrusions. See <i>Indianapolis</i> v. <i>Edmond,</i> <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#41" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S. 32, 41-42</a></span> (2000). Since the police claim to have had no particular suspicion that Caballes was violating any drug law,<sup>[4]</sup> this sniff search must stand or fall on its being ancillary to the traffic stop that led up to it. It is true that the police had probable cause to stop the car for an offense committed in the officer's presence, which Caballes concedes could have justified his arrest. See Brief for Respondent 31. There is no occasion to consider authority incident to arrest, however, see <i>Knowles</i> v. <i>Iowa,</i> <span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/" aria-description="Citation for case: Knowles v. Iowa">525 U. S. 113</a></span> (1998), for the police did nothing more than detain Caballes long enough to check his record and write a ticket. As a consequence, the reasonableness of the search must be assessed in relation to the actual delay the police chose to impose, and as JUSTICE GINSBURG points out in her opinion, <i>post,</i> at 419-420, the Fourth Amendment consequences of stopping for a traffic citation are settled law.</p>
<p><span class="star-pagination">*415</span> In <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#439" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 439-440</a></span> (1984), followed in <span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/#117" aria-description="Citation for case: Knowles v. Iowa"><i>Knowles, supra,</i> at 117</a></span>, we held that the analogue of the common traffic stop was the limited detention for investigation authorized by <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968). While <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> authorized a restricted incidental search for weapons when reasonable suspicion warrants such a safety measure, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#25" aria-description="Citation for case: Terry v. Ohio"><i>id.,</i> at 25-26</a></span>, the Court took care to keep a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop from automatically becoming a foot in the door for all investigatory purposes; the permissible intrusion was bounded by the justification for the detention, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio"><i>id.,</i> at 29-30</a></span>.<sup>[5]</sup> Although facts disclosed by enquiry within this limit might give grounds to go further, the government could not otherwise take advantage of a suspect's immobility to search for evidence unrelated to the reason for the detention. That has to be the rule unless <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> is going to become an open sesame for general searches, and that rule requires holding that the police do not have reasonable grounds to conduct sniff searches for drugs simply because they have stopped someone to receive a ticket for a highway offense. Since the police had no indication of illegal activity beyond the speed of the car in this case, the sniff search should be held unreasonable under the Fourth Amendment and its fruits should be suppressed.</p>
<p>Nothing in the case relied upon by the Court, <i>United States</i> v. <i>Jacobsen,</i> <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109</a></span> (1984), unsettled the limit of reasonable enquiry adopted in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</i> In <i><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">Jacobsen</a></span>,</i> the Court found that no Fourth Amendment search occurred when federal agents analyzed powder they had already lawfully obtained. The Court noted that because the test could only reveal whether the powder was cocaine, the owner had no legitimate privacy interest at stake. <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#123" aria-description="Citation for case: United States v. Jacobsen">466 U. S., at 123</a></span>. <span class="star-pagination">*416</span> As already explained, however, the use of a sniffing dog in cases like this is significantly different and properly treated as a search that does indeed implicate Fourth Amendment protection.</p>
<p>In <i><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">Jacobsen</a></span>,</i> once the powder was analyzed, that was effectively the end of the matter: either the powder was cocaine, a fact the owner had no legitimate interest in concealing, or it was not cocaine, in which case the test revealed nothing about the powder or anything else that was not already legitimately obvious to the police. But in the case of the dog sniff, the dog does not smell the disclosed contraband; it smells a closed container. An affirmative reaction therefore does not identify a substance the police already legitimately possess, but informs the police instead merely of a reasonable chance of finding contraband they have yet to put their hands on. The police will then open the container and discover whatever lies within, be it marijuana or the owner's private papers. Thus, while <i><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">Jacobsen</a></span></i> could rely on the assumption that the enquiry in question would either show with certainty that a known substance was contraband or would reveal nothing more, both the certainty and the limit on disclosure that may follow are missing when the dog sniffs the car.<sup>[6]</sup></p>
<p><span class="star-pagination">*417</span> The Court today does not go so far as to say explicitly that sniff searches by dogs trained to sense contraband always get a free pass under the Fourth Amendment, since it reserves judgment on the constitutional significance of sniffs assumed to be more intrusive than a dog's walk around a stopped car, <i>ante,</i> at 409. For this reason, I do not take the Court's reliance on <i><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">Jacobsen</a></span></i> as actually signaling recognition of a broad authority to conduct suspicionless sniffs for drugs in any parked car, about which JUSTICE GINSBURG is rightly concerned, <i>post,</i> at 422, or on the person of any pedestrian minding his own business on a sidewalk. But the Court's stated reasoning provides no apparent stopping point short of such excesses. For the sake of providing a workable framework to analyze cases on facts like these, which are certain to come along, I would treat the dog sniff as the familiar search it is in fact, subject to scrutiny under the Fourth Amendment.<sup>[7]</sup></p>
<p>JUSTICE GINSBURG, with whom JUSTICE SOUTER joins, dissenting.</p>
<p>Illinois State Police Trooper Daniel Gillette stopped Roy Caballes for driving 71 miles per hour in a zone with a posted <span class="star-pagination">*418</span> speed limit of 65 miles per hour. Trooper Craig Graham of the Drug Interdiction Team heard on the radio that Trooper Gillette was making a traffic stop. Although Gillette requested no aid, Graham decided to come to the scene to conduct a dog sniff. Gillette informed Caballes that he was speeding and asked for the usual documents  driver's license, car registration, and proof of insurance. Caballes promptly provided the requested documents but refused to consent to a search of his vehicle. After calling his dispatcher to check on the validity of Caballes' license and for outstanding warrants, Gillette returned to his vehicle to write Caballes a warning ticket. Interrupted by a radio call on an unrelated matter, Gillette was still writing the ticket when Trooper Graham arrived with his drug-detection dog. Graham walked the dog around the car, the dog alerted at Caballes' trunk, and, after opening the trunk, the troopers found marijuana. <span class="citation multiple-matches"><a href="/c/Ill.%202d/207/504/">207 Ill. 2d 504</a></span>, 506-507, <span class="citation multiple-matches"><a href="/c/N.%20E.%202d/802/202/">802 N. E. 2d 202</a></span>, 203 (2003).</p>
<p>The Supreme Court of Illinois held that the drug evidence should have been suppressed. <i>Id.,</i> at 506, 802 N. E. 2d, at 202. Adhering to its decision in <i>People</i> v. <i>Cox,</i> <span class="citation" data-id="9526758"><a href="/opinion/2038990/people-v-cox/" aria-description="Citation for case: People v. Cox">202 Ill. 2d 462</a></span>, <span class="citation" data-id="9526758"><a href="/opinion/2038990/people-v-cox/" aria-description="Citation for case: People v. Cox">782 N. E. 2d 275</a></span> (2002), the court employed a two-part test taken from <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), to determine the overall reasonableness of the stop. 207 Ill. 2d, at 508, 802 N. E. 2d, at 204. The court asked first "whether the officer's action was justified at its inception," and second "whether it was reasonably related in scope to the circumstances which justified the interference in the first place." <i>Ibid.</i> (quoting <i>People</i> v. <i>Brownlee,</i> <span class="citation" data-id="9718595"><a href="/opinion/2106553/people-v-brownlee/#518" aria-description="Citation for case: People v. Brownlee">186 Ill. 2d 501, 518-519</a></span>, <span class="citation" data-id="9718595"><a href="/opinion/2106553/people-v-brownlee/#565" aria-description="Citation for case: People v. Brownlee">713 N. E. 2d 556, 565</a></span> (1999) (in turn quoting <i>Terry,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 19-20</a></span>)). "[I]t is undisputed," the court observed, "that the traffic stop was properly initiated"; thus, the dispositive inquiry trained on the "second part of the <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> test," in which "[t]he State bears the burden of establishing that the conduct remained within the scope of the stop." 207 Ill. 2d, at 509, 802 N. E. 2d, at 204.</p>
<p><span class="star-pagination">*419</span> The court concluded that the State failed to offer sufficient justification for the canine sniff: "The police did not detect the odor of marijuana in the car or note any other evidence suggesting the presence of illegal drugs." <i>Ibid.</i> Lacking "specific and articulable facts" supporting the canine sniff, <i>ibid.</i> (quoting <i>Cox,</i> <span class="citation" data-id="9526758"><a href="/opinion/2038990/people-v-cox/#470" aria-description="Citation for case: People v. Cox">202 Ill. 2d, at 470-471</a></span>, <span class="citation" data-id="9526758"><a href="/opinion/2038990/people-v-cox/#281" aria-description="Citation for case: People v. Cox">782 N. E. 2d, at 281</a></span>), the court ruled, "the police impermissibly broadened the scope of the traffic stop in this case into a drug investigation." 207 Ill. 2d, at 509, 802 N. E. 2d, at 204.<sup>[1]</sup> I would affirm the Illinois Supreme Court's judgment and hold that the drug sniff violated the Fourth Amendment.</p>
<p>In <i>Terry</i> v. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio</a></span></i><i>,</i> the Court upheld the stop and subsequent frisk of an individual based on an officer's observation of suspicious behavior and his reasonable belief that the suspect was armed. See <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 27-28</a></span>. In a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i>-type investigatory stop, "the officer's action [must be] justified at its inception, and ... reasonably related in scope to the circumstances which justified the interference in the first place." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 20</a></span>. In applying <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> the Court has several times indicated that the limitation on "scope" is not confined to the duration of the seizure; it also encompasses the manner in which the seizure is conducted. See, <i>e. g., </i><i>Hiibel</i> v. <i>Sixth Judicial Dist. Court of Nev., Humboldt Cty.,</i> <span class="citation" data-id="9434645"><a href="/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/#188" aria-description="Citation for case: Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.">542 U. S. 177, 188</a></span> (2004) (an officer's request that an individual identify himself "has an immediate relation to the purpose, rationale, and practical demands of a <i>Terry</i> stop"); <i>United States</i> v. <i>Hensley,</i> <span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/#235" aria-description="Citation for case: United States v. Hensley">469 U. S. 221, 235</a></span> (1985) (examining, under <i>Terry,</i> <span class="star-pagination">*420</span> both "the length and intrusiveness of the stop and detention"); <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#500" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 500</a></span> (1983) (plurality opinion) ("[A]n investigative detention must be temporary and last no longer than is necessary to effectuate the purpose of the stop [and] the investigative methods employed should be the least intrusive means reasonably available to verify or dispel the officer's suspicion. . . .").</p>
<p>"A routine traffic stop," the Court has observed, "is a relatively brief encounter and `is more analogous to a so-called <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop . . . than to a formal arrest.'" <i>Knowles</i> v. <i>Iowa,</i> <span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/#117" aria-description="Citation for case: Knowles v. Iowa">525 U. S. 113, 117</a></span> (1998) (quoting <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#439" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 439</a></span> (1984)); see also <i>ante,</i> at 415 (SOUTER, J., dissenting) (The government may not "take advantage of a suspect's immobility to search for evidence unrelated to the reason for the detention.").<sup>[2]</sup> I would apply <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i>'s reasonable-relation test, as the Illinois Supreme Court did, to determine whether the canine sniff impermissibly expanded the scope of the initially valid seizure of Caballes.</p>
<p>It is hardly dispositive that the dog sniff in this case may not have lengthened the duration of the stop. Cf. <i>ante,</i> at 407 ("A seizure ... can become unlawful if it is prolonged beyond the time reasonably required to complete [the initial] mission."). <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> it merits repetition, instructs that any investigation must be "reasonably related in <i>scope</i> to the circumstances which justified the interference in the first place." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20</a></span> (emphasis added). The unwarranted <span class="star-pagination">*421</span> and nonconsensual expansion of the seizure here from a routine traffic stop to a drug investigation broadened the scope of the investigation in a manner that, in my judgment, runs afoul of the Fourth Amendment.<sup>[3]</sup></p>
<p>The Court rejects the Illinois Supreme Court's judgment and, implicitly, the application of <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> to a traffic stop converted, by calling in a dog, to a drug search. The Court so rules, holding that a dog sniff does not render a seizure that is reasonable in time unreasonable in scope. <i>Ante,</i> at 408. Dog sniffs that detect only the possession of contraband may be employed without offense to the Fourth Amendment, the Court reasons, because they reveal no lawful activity and hence disturb no legitimate expectation of privacy. <i>Ante,</i> at 408-409.</p>
<p>In my view, the Court diminishes the Fourth Amendment's force by abandoning the second <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> inquiry (was the police action "reasonably related in scope to the circumstances [justifiying] the [initial] interference"). <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20</a></span>. A drug-detection dog is an intimidating animal. Cf. <i>United States</i> v. <i>Williams,</i> <span class="citation" data-id="9437405"><a href="/opinion/164282/united-states-v-williams/#1276" aria-description="Citation for case: United States v. Williams">356 F. 3d 1268, 1276</a></span> (CA10 2004) (McKay, J., dissenting) ("drug dogs are not lap dogs"). Injecting such an animal into a routine traffic stop changes the character of the encounter between the police and the motorist. The stop becomes broader, more adversarial, and (in at least some cases) longer. Caballes  who, as far as Troopers Gillette and Graham knew, was guilty solely of driving six miles per hour over the speed limit  was exposed to the embarrassment and intimidation of being investigated, on a public thoroughfare, for drugs. Even if the drug sniff is not characterized as a Fourth Amendment "search," cf. <i><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Indianapolis</a></span></i> <span class="star-pagination">*422</span> v. <i>Edmond,</i> <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#40" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S. 32, 40</a></span> (2000); <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place">462 U. S. 696, 707</a></span> (1983), the sniff surely broadened the scope of the traffic-violation-related seizure.</p>
<p>The Court has never removed police action from Fourth Amendment control on the ground that the action is well calculated to apprehend the guilty. See, <i>e. g., </i><i>United States</i> v. <i>Karo,</i> <span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/#717" aria-description="Citation for case: United States v. Karo">468 U. S. 705, 717</a></span> (1984) (Fourth Amendment warrant requirement applies to police monitoring of a beeper in a house even if "the facts [justify] believing that a crime is being or will be committed and that monitoring the beeper wherever it goes is likely to produce evidence of criminal activity."); see also <i>Minnesota</i> v. <i>Carter,</i> <span class="citation" data-id="9433723"><a href="/opinion/118249/minnesota-v-carter/#110" aria-description="Citation for case: Minnesota v. Carter">525 U. S. 83, 110</a></span> (1998) (GINSBURG, J., dissenting) ("Fourth Amendment protection, reserved for the innocent only, would have little force in regulating police behavior toward either the innocent or the guilty."). Under today's decision, every traffic stop could become an occasion to call in the dogs, to the distress and embarrassment of the law-abiding population.</p>
<p>The Illinois Supreme Court, it seems to me, correctly apprehended the danger in allowing the police to search for contraband despite the absence of cause to suspect its presence. Today's decision, in contrast, clears the way for suspicionless, dog-accompanied drug sweeps of parked cars along sidewalks and in parking lots. Compare, <i>e. g., </i><i>United States</i> v. <i>Ludwig,</i> <span class="citation" data-id="658364"><a href="/opinion/658364/united-states-v-keith-rudolph-ludwig-national-association-of-criminal/#1526" aria-description="Citation for case: United States v. Keith Rudolph Ludwig, National...">10 F. 3d 1523, 1526-1527</a></span> (CA10 1993) (upholding a search based on a canine drug sniff of a parked car in a motel parking lot conducted without particular suspicion), with <i>United States</i> v. <i>Quinn,</i> <span class="citation" data-id="9475983"><a href="/opinion/485654/united-states-v-daniel-j-quinn/#159" aria-description="Citation for case: United States v. Daniel J. Quinn">815 F. 2d 153, 159</a></span> (CA1 1987) (officers must have reasonable suspicion that a car contains narcotics at the moment a dog sniff is performed), and <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#706" aria-description="Citation for case: United States v. Place">462 U. S., at 706-707</a></span> (Fourth Amendment not violated by a dog sniff of a piece of luggage that was seized, pre-sniff, based on suspicion of drugs). Nor would motorists have constitutional grounds for complaint should police with dogs, stationed at long traffic lights, circle cars waiting for the red signal to turn green.</p>
<p><span class="star-pagination">*423</span> Today's decision also undermines this Court's situation-sensitive balancing of Fourth Amendment interests in other contexts. For example, in <i>Bond</i> v. <i>United States,</i> <span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/#338" aria-description="Citation for case: Bond v. United States">529 U. S. 334, 338-339</a></span> (2000), the Court held that a bus passenger had an expectation of privacy in a bag placed in an overhead bin and that a police officer's physical manipulation of the bag constituted an illegal search. If canine drug sniffs are entirely exempt from Fourth Amendment inspection, a sniff could substitute for an officer's request to a bus passenger for permission to search his bag, with this significant difference: The passenger would not have the option to say "No."</p>
<p>The dog sniff in this case, it bears emphasis, was for drug detection only. A dog sniff for explosives, involving security interests not presented here, would be an entirely different matter. Detector dogs are ordinarily trained not as all-purpose sniffers, but for discrete purposes. For example, they may be trained for narcotics detection or for explosives detection or for agricultural products detection. See, <i>e. g.,</i> U. S. Customs &amp; Border Protection, Canine Enforcement Training Center Training Program Course Descriptions, http://www.cbp.gov/xp/cgov/border_security/canines/training_program.xml (all Internet materials as visited Dec. 16, 2004, and available in Clerk of Court's case file) (describing Customs training courses in narcotics detection); Transportation Security Administration, Canine and Explosives Program, http://www.tsa.gov/public/display?theme=32 (describing Transportation Security Administration's explosives detection canine program); U. S. Dept. of Agriculture, Animal and Plant Health Inspection Service, USDA's Detector Dogs: Protecting American Agriculture (Oct. 2001), available at http://www.aphis.usda.gov/oa/pubs/detdogs.pdf (describing USDA Beagle Brigade detector dogs trained to detect prohibited fruits, plants, and meat); see also Jennings, Origins and History of Security and Detector Dogs, in Canine Sports Medicine and Surgery 16, 18-19 (M. Bloomberg, J. Dee, &amp; R. Taylor eds. 1998) (describing narcotics-detector <span class="star-pagination">*424</span> dogs used by Border Patrol and Customs, and bomb detector dogs used by the Federal Aviation Administration and the Secret Service, but noting the possibility in some circumstances of cross training dogs for multiple tasks); S. Chapman, Police Dogs in North America 64, 70-79 (1990) (describing narcotics- and explosives-detection dogs and noting the possibility of cross training). There is no indication in this case that the dog accompanying Trooper Graham was trained for anything other than drug detection. See 207 Ill. 2d, at 507, 802 N. E. 2d, at 203 ("Trooper Graham arrived with his drug-detection dog. . . ."); Brief for Petitioner 3 ("Trooper Graham arrived with a drug-detection dog. . . .").</p>
<p>This Court has distinguished between the general interest in crime control and more immediate threats to public safety. In <i>Michigan Dept. of State Police</i> v. <i>Sitz,</i> <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U.S. 444</a></span> (1990), this Court upheld the use of a sobriety traffic checkpoint. Balancing the State's interest in preventing drunk driving, the extent to which that could be accomplished through the checkpoint program, and the degree of intrusion the stops involved, the Court determined that the State's checkpoint program was consistent with the Fourth Amendment. <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#455" aria-description="Citation for case: Michigan Department of State Police v. Sitz"><i>Id.,</i> at 455</a></span>. Ten years after <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span>,</i> in <i>Indianapolis</i> v. <i>Edmond,</i> <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S. 32</a></span>, this Court held that a drug interdiction checkpoint violated the Fourth Amendment. Despite the illegal narcotics traffic that the Nation is struggling to stem, the Court explained, a "general interest in crime control" did not justify the stops. <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#43" aria-description="Citation for case: City of Indianapolis v. Edmond"><i>Id.,</i> at 43-44</a></span> (internal quotation marks omitted). The Court distinguished the sobriety checkpoints in <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> on the ground that those checkpoints were designed to eliminate an "immediate, vehicle-bound threat to life and limb." <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#43" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S., at 43</a></span>.</p>
<p>The use of bomb-detection dogs to check vehicles for explosives without doubt has a closer kinship to the sobriety checkpoints in <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> than to the drug checkpoints in <i><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span>.</i> As the Court observed in <i><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span>:</i> "[T]he Fourth Amendment would almost certainly permit an appropriately tailored <span class="star-pagination">*425</span> roadblock set up to thwart an imminent terrorist attack. . . ." <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#44" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S., at 44</a></span>. Even if the Court were to change course and characterize a dog sniff as an independent Fourth Amendment search, see <i>ante,</i> p. 410 (SOUTER, J., dissenting), the immediate, present danger of explosives would likely justify a bomb sniff under the special needs doctrine. See, <i>e. g., ante,</i> at 417, n. 7 (SOUTER, J., dissenting); <i>Griffin</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#873" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868, 873</a></span> (1987) (permitting exceptions to the warrant and probable-cause requirements for a search when "special needs, beyond the normal need for law enforcement," make those requirements impracticable (quoting <i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#351" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 351</a></span> (1985) (Blackmun, J., concurring in judgment))).</p>
<p></p>
<h2>* * *</h2>
<p>For the reasons stated, I would hold that the police violated Caballes' Fourth Amendment rights when, without cause to suspect wrongdoing, they conducted a dog sniff of his vehicle. I would therefore affirm the judgment of the Illinois Supreme Court.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for the State of Arkansas et al. by <i>Mike Beebe,</i> Attorney General of Arkansas, <i>Lauren Elizabeth Heil,</i> Assistant Attorney General, and <i>Dan Schweitzer,</i> and by the Attorneys General for their respective States as follows: <i>Troy King</i> of Alabama, <i>Terry Goddard</i> of Arizona, <i>Christopher L. Morano</i> of Connecticut, <i>M. Jane Brady</i> of Delaware, <i>Thurbert E. Baker</i> of Georgia, <i>Mark J. Bennett</i> of Hawaii, <i>Lawrence G. Wasden</i> of Idaho, <i>Steve Carter</i> of Indiana, <i>Phill Kline</i> of Kansas, <i>Charles C. Foti</i> of Louisiana, <i>G. Steven Rowe</i> of Maine, <i>J. Joseph Curran, Jr.,</i> of Maryland, <i>Michael A. Cox</i> of Michigan, <i>Jon Bruning</i> of Nebraska, <i>Peter C. Harvey</i> of New Jersey, <i>Patricia A. Madrid</i> of New Mexico, <i>Roy Cooper</i> of North Carolina, <i>Wayne Stenehjem</i> of North Dakota, <i>Jim Petro</i> of Ohio, <i>Hardy Myers</i> of Oregon, <i>Henry D. McMaster</i> of South Carolina, <i>Lawrence E. Long</i> of South Dakota, <i>Greg Abbott</i> of Texas, <i>Mark L. Shurtleff</i> of Utah, <i>William H. Sorrell</i> of Vermont, <i>Jerry Kilgore</i> of Virginia, and <i>Patrick J. Crank</i> of Wyoming; and for the Illinois Association of Chiefs of Police et al. by <i>James G. Sotos.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the American Civil Liberties Union et al. by <i>Barry Sullivan, Jacob I. Corré, Steven R. Shapiro,</i> and <i>Harvey Grossman;</i> and for the National Association of Criminal Defense Lawyers by <i>Jeffrey T. Green, John Wesley Hall, Jr.,</i> and <i>David M. Siegel.</i></p>
<p>[1]  I also join JUSTICE GINSBURG's dissent, <i>post,</i> p. 417. Without directly reexamining the soundness of the Court's analysis of government dog sniffs in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> she demonstrates that investigation into a matter beyond the subject of the traffic stop here offends the rule in <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), the analysis I, too, adopt.</p>
<p>[2]  Another proffered justification for <i>sui generis</i> status is that a dog sniff is a particularly nonintrusive procedure. <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place">462 U. S. 696, 707</a></span> (1983). I agree with JUSTICE GINSBURG that the introduction of a dog to a traffic stop (let alone an encounter with someone walking down the street) can in fact be quite intrusive. <i>Post,</i> at 421-422.</p>
<p>[3]  <i><span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">Kyllo</a></span></i> was concerned with whether a search occurred when the police used a thermal-imaging device on a house to detect heat emanations associated with high-powered marijuana-growing lamps. In concluding that using the device was a search, the Court stressed that the "Government [may not] us[e] a device ... to explore details of the home that would previously have been unknowable without physical intrusion." <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/#40" aria-description="Citation for case: Kyllo v. United States">533 U.S., at 40</a></span>. Any difference between the dwelling in <i><span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">Kyllo</a></span></i> and the trunk of the car here may go to the issue of the reasonableness of the respective searches, but it has no bearing on the question of search or no search. Nor is it significant that <i><span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">Kyllo</a></span></i>'s imaging device would disclose personal details immediately, whereas they would be revealed only in the further step of opening the enclosed space following the dog's alert reaction; in practical terms the same values protected by the Fourth Amendment are at stake in each case. The justifications required by the Fourth Amendment may or may not differ as between the two practices, but if constitutional scrutiny is in order for the imager, it is in order for the dog.</p>
<p>[4]  Despite the remarkable fact that the police pulled over a car for going 71 miles an hour on I-80, the State maintains that excessive speed was the only reason for the stop, and the case comes to us on that assumption.</p>
<p>[5]  Thus, in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> itself, the Government officials had independent grounds to suspect that the luggage in question contained contraband before they employed the dog sniff. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#698" aria-description="Citation for case: United States v. Place">462 U. S., at 698</a></span> (describing how Place had acted suspiciously in line at the airport and had labeled his luggage with inconsistent and fictional addresses).</p>
<p>[6]  It would also be error to claim that some variant of the plain-view doctrine excuses the lack of justification for the dog sniff in this case. When an officer observes an object left by its owner in plain view, no search occurs because the owner has exhibited "no intention to keep [the object] to himself." <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 361</a></span> (1967) (Harlan, J., concurring). In contrast, when an individual conceals his possessions from the world, he has grounds to expect some degree of privacy. While plain view may be enhanced somewhat by technology, see, <i>e.g., </i><i>Dow Chemical Co.</i> v. <i>United States,</i> <span class="citation" data-id="9430504"><a href="/opinion/111667/dow-chemical-co-v-united-states-ex-rel-administrator/" aria-description="Citation for case: Dow Chemical Co. v. United States Ex Rel. Administrator">476 U. S. 227</a></span> (1986) (allowing for aerial surveillance of an industrial complex), there are limits. As <i>Kyllo</i> v. <i>United States,</i> <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/#33" aria-description="Citation for case: Kyllo v. United States">533 U. S. 27, 33</a></span> (2001), explained in treating the thermal-imaging device as outside the plain-view doctrine, "[w]e have previously reserved judgment as to how much technological enhancement of ordinary perception" turns mere observation into a Fourth Amendment search. While <i><span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">Kyllo</a></span></i> laid special emphasis on the heightened privacy expectations that surround the home, closed car trunks are accorded some level of privacy protection. See, <i>e. g., </i><i>New York</i> v. <i>Belton,</i> <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S. 454, 460, n. 4</a></span> (1981) (holding that even a search incident to arrest in a vehicle does not itself permit a search of the trunk). As a result, if Fourth Amendment protections are to have meaning in the face of superhuman, yet fallible, techniques like the use of trained dogs, those techniques must be justified on the basis of their reasonableness, lest everything be deemed in plain view.</p>
<p>[7]  I should take care myself to reserve judgment about a possible case significantly unlike this one. All of us are concerned not to prejudge a claim of authority to detect explosives and dangerous chemical or biological weapons that might be carried by a terrorist who prompts no individualized suspicion. Suffice it to say here that what is a reasonable search depends in part on demonstrated risk. Unreasonable sniff searches for marijuana are not necessarily unreasonable sniff searches for destructive or deadly material if suicide bombs are a societal risk.</p>
<p>[1]  The Illinois Supreme Court held insufficient to support a canine sniff Gillette's observations that (1) Caballes said he was moving to Chicago, but his only visible belongings were two sport coats in the backseat; (2) the car smelled of air freshener; (3) Caballes was dressed for business, but was unemployed; and (4) Caballes seemed nervous. Even viewed together, the court said, these observations gave rise to "nothing more than a vague hunch" of "possible wrongdoing." <span class="citation multiple-matches"><a href="/c/Ill.%202d/207/504/">207 Ill. 2d 504</a></span>, 509-510, <span class="citation multiple-matches"><a href="/c/N.%20E.%202d/802/202/">802 N. E. 2d 202</a></span>, 204-205 (2003). This Court proceeds on "the assumption that the officer conducting the dog sniff had no information about [Caballes]." <i>Ante,</i> at 407.</p>
<p>[2]  The <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span></i> Court cautioned that by analogizing a traffic stop to a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop, it did "not suggest that a traffic stop supported by probable cause may not exceed the bounds set by the Fourth Amendment on the scope of a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop." 468 U. S., at 439, n. 29. This Court, however, looked to <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> earlier in deciding that an officer acted reasonably when he ordered a motorist stopped for driving with expired license tags to exit his car, <i>Pennsylvania</i> v. <i>Mimms,</i> <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#109" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 109-110</a></span> (1977) <i>(per curiam)</i><i>,</i> and later reaffirmed the <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> analogy when evaluating a police officer's authority to search a vehicle during a routine traffic stop, <i>Knowles,</i> <span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/#117" aria-description="Citation for case: Knowles v. Iowa">525 U. S., at 117</a></span>.</p>
<p>[3]  The question whether a police officer inquiring about drugs without reasonable suspicion unconstitutionally broadens a traffic investigation is not before the Court. Cf. <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#434" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429, 434</a></span> (1991) (police questioning of a bus passenger, who might have just said "No," did not constitute a seizure).</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Illinois v. Gates.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Illinois v. Gates"
type: case
citation: "462 U.S. 213 (1983)"
parallel_cite: "103 S. Ct. 2317; 76 L. Ed. 2d 527; 51 U.S.L.W. 4709"
neutral_cite: 1983 U.S. LEXIS 54
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-06-08
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1983-06-08
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Illinois v. Gates
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110959/illinois-v-gates/"
  cluster_id: 110959
  opinion_id: 9429232
  identity_checked: true
homes:
  - page: "[[Probable Cause]]"
    role: "Key — Anchor"
  - page: "[[Probable Cause in the Affidavit]]"
    role: "Related (cross-doctrine)"
  - page: "[[The Proof Ladder]]"
    role: "Key — rung anchor"
related: ["[[Aguilar v. Texas]]", "[[Spinelli v. United States]]", "[[Brinegar v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "probable-cause", "informants", "totality-of-the-circumstances", "warrant"]
holding: "Probable cause from an informant's tip is judged by the **totality of the circumstances** — the issuing magistrate makes a practical,…"
lake:
  record_id: Illinois v. Gates
  status: verified
  projected_at: 2026-07-06
---

# Illinois v. Gates

*462 U.S. 213 (1983)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police received an anonymous letter stating that Lance and Susan Gates were drug dealers, detailing a method by which one would fly to Florida, load a car with drugs, and drive it back while the other flew home. Officers corroborated the largely innocent travel details and obtained a warrant; a search of the Gateses' car and home turned up marijuana and other contraband. The Illinois courts, applying the rigid two-pronged informant test, suppressed the evidence.

## Issue
Whether probable cause based on an informant's tip must satisfy the two independent prongs of the *[[Aguilar v. Texas|Aguilar]]*–*[[Spinelli v. United States|Spinelli]]* test, or is instead judged by the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]].

## Rule
Probable cause from a tip is judged by the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]. "For all these reasons, we conclude that it is wiser to abandon the 'two-pronged test' established by our decisions in Aguilar and Spinelli. In its place we reaffirm the totality-of-the-circumstances analysis that traditionally has informed probable-cause determinations." — 462 U.S. at 238. ^pin-238

"The task of the issuing magistrate is simply to make a practical, common-sense decision whether, given all the circumstances set forth in the affidavit before him, including the 'veracity' and 'basis of knowledge' of persons supplying hearsay information, there is a fair probability that contraband or evidence of a crime will be found in a particular place." — *Id.* ^pin-238a

## Application
Treating the informant's veracity and basis of knowledge as relevant but no longer independent, dispositive requirements, the Court found the anonymous letter, corroborated by the police investigation of the Gateses' predicted Florida travel, gave the magistrate a substantial basis to conclude there was a fair probability that contraband would be found in the car and home. The warrant was therefore supported by probable cause.

## Conclusion
The warrant was valid under the totality-of-the-circumstances test; the suppression was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of *Gates*. *Gates* itself **abandoned** the rigid two-pronged framework of [[Aguilar v. Texas]] and [[Spinelli v. United States]], replacing it with the flexible totality-of-the-circumstances standard.

## Appears on
- [[Probable Cause]] — *Key — Anchor*
- [[Probable Cause in the Affidavit]] — *Related (cross-doctrine)*
- [[The Proof Ladder]] — *Key — rung anchor*

## Sources
- *Illinois v. Gates*, 462 U.S. 213 (1983) — https://www.courtlistener.com/opinion/110959/illinois-v-gates/ — pinpoint: 238.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f42ba99a7ae2018d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Illinois v. Gates"}, "payload": {"all": [{"cite": "462 U.S. 213", "page": "213", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "462"}, {"cite": "103 S. Ct. 2317", "page": "2317", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "103"}, {"cite": "76 L. Ed. 2d 527", "page": "527", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "76"}, {"cite": "1983 U.S. LEXIS 54", "page": "54", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1983"}, {"cite": "51 U.S.L.W. 4709", "page": "4709", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "51"}], "display": "462 U.S. 213", "official": {"cite": "462 U.S. 213", "page": "213", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "462"}, "official_selection_present": true, "record_id": "Illinois v. Gates"}}
{"assertion_id": "0f6f4129eb09b654", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-238", "record_id": "Illinois v. Gates"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-238", "pinpoint_status": "slip-only", "quote": "--- # Illinois v. Gates *462 U.S. 213 (1983)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police received an anonymous letter stating that Lance and Susan Gates were drug dealers, detailing a method by which one would fly to Florida, load a car with drugs, and drive it back while the other flew home. Officers corroborated the largely innocent travel details and obtained a warrant; a search of the Gateses' car and home turned up marijuana and other contraband. The Illinois courts, applying the rigid two-pronged informant test, suppressed the evidence. ## Issue Whether probable cause based on an informant's tip must satisfy the two independent prongs of the *Aguilar*–*Spinelli* test, or is instead judged by the totality of the circumstances. ## Rule Probable cause from a tip is judged by the totality of the circumstances.", "quote_fidelity": "mismatch", "record_id": "Illinois v. Gates", "star_marker": null}}
{"assertion_id": "7f54b7f1f0ffaa97", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-238a", "record_id": "Illinois v. Gates"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-238a", "pinpoint_status": "slip-only", "quote": "The task of the issuing magistrate is simply to make a practical, common-sense decision whether, given all the circumstances set forth in the affidavit before him, including the 'veracity' and 'basis of knowledge' of persons supplying hearsay information, there is a fair probability that contraband or evidence of a crime will be found in a particular place.", "quote_fidelity": "mismatch", "record_id": "Illinois v. Gates", "star_marker": null}}
{"assertion_id": "ee55b8cad2891e32", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Illinois v. Gates"}, "payload": {"as_of_content": "1983-06-08", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Illinois v. Gates", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Illinois v. Gates

```json
{
  "schema_version": "s2.v1",
  "record_id": "Illinois v. Gates",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Illinois v. Gates",
    "case_name_short": "Gates",
    "case_name_full": "ILLINOIS v. GATES Et Ux.",
    "input_case_name": "Illinois v. Gates",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-06-08",
    "year": 1983,
    "docket": null,
    "cluster_id": 110959,
    "lead_opinion_id": 9429232,
    "sibling_ids": [
      110959,
      9429232,
      9429233,
      9429234,
      9429235
    ],
    "absolute_url": "/opinion/110959/illinois-v-gates/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9046341,
        "score": 20,
        "case_name": "Illinois v. Gates"
      },
      {
        "cluster_id": 9044083,
        "score": 20,
        "case_name": "Illinois v. Gates"
      },
      {
        "cluster_id": 9043404,
        "score": 20,
        "case_name": "Illinois v. Gates"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "462 U.S. 213",
      "volume": "462",
      "reporter": "U.S.",
      "page": "213",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 2317",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2317",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "76 L. Ed. 2d 527",
        "volume": "76",
        "reporter": "L. Ed. 2d",
        "page": "527",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4709",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4709",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 54",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "54",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "462 U.S. 213",
        "volume": "462",
        "reporter": "U.S.",
        "page": "213",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 2317",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2317",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "76 L. Ed. 2d 527",
        "volume": "76",
        "reporter": "L. Ed. 2d",
        "page": "527",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 54",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "54",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4709",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4709",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "462 U.S. 213",
    "official_selection": {
      "court_class": "scotus",
      "selected": "462 U.S. 213",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-238",
      "page": null,
      "quote": "--- # Illinois v. Gates *462 U.S. 213 (1983)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police received an anonymous letter stating that Lance and Susan Gates were drug dealers, detailing a method by which one would fly to Florida, load a car with drugs, and drive it back while the other flew home. Officers corroborated the largely innocent travel details and obtained a warrant; a search of the Gateses' car and home turned up marijuana and other contraband. The Illinois courts, applying the rigid two-pronged informant test, suppressed the evidence. ## Issue Whether probable cause based on an informant's tip must satisfy the two independent prongs of the *Aguilar*\u2013*Spinelli* test, or is instead judged by the totality of the circumstances. ## Rule Probable cause from a tip is judged by the totality of the circumstances.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-238a",
      "page": null,
      "quote": "The task of the issuing magistrate is simply to make a practical, common-sense decision whether, given all the circumstances set forth in the affidavit before him, including the 'veracity' and 'basis of knowledge' of persons supplying hearsay information, there is a fair probability that contraband or evidence of a crime will be found in a particular place.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1983-06-08",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Illinois v. Gates",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Illinois v. Gates:lane1_negative"
      },
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
        "journal_ref": "Illinois v. Gates:lane1_negative"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ornelas v. United States",
          "cluster_id": 118030,
          "cite": [
            "134 L. Ed. 2d 911",
            "116 S. Ct. 1657",
            "517 U.S. 690",
            "1996 U.S. LEXIS 3391"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sokolow",
          "cluster_id": 112239,
          "cite": [
            "104 L. Ed. 2d 1",
            "109 S. Ct. 1581",
            "490 U.S. 1",
            "1989 U.S. LEXIS 1694",
            "57 U.S.L.W. 4401"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Payne v. Tennessee",
          "cluster_id": 112643,
          "cite": [
            "115 L. Ed. 2d 720",
            "111 S. Ct. 2597",
            "501 U.S. 808",
            "1991 U.S. LEXIS 3821"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edward H. Phillips v. Awh Corporation, Hopeman Brothers, Inc., and Lofton Corporation, Defendants-Cross",
          "cluster_id": 791122,
          "cite": [
            "415 F.3d 1303"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Siegert v. Gilley",
          "cluster_id": 112594,
          "cite": [
            "114 L. Ed. 2d 277",
            "111 S. Ct. 1789",
            "500 U.S. 226",
            "1991 U.S. LEXIS 2909",
            "59 U.S.L.W. 4465"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jimeno",
          "cluster_id": 112595,
          "cite": [
            "114 L. Ed. 2d 297",
            "111 S. Ct. 1801",
            "500 U.S. 248",
            "1991 U.S. LEXIS 2910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "R. A. v. v. City of St. Paul",
          "cluster_id": 112774,
          "cite": [
            "120 L. Ed. 2d 305",
            "112 S. Ct. 2538",
            "505 U.S. 377",
            "1992 U.S. LEXIS 3863"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Pringle",
          "cluster_id": 131150,
          "cite": [
            "157 L. Ed. 2d 769",
            "124 S. Ct. 795",
            "540 U.S. 366",
            "2003 U.S. LEXIS 9198"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mills v. Maryland",
          "cluster_id": 112085,
          "cite": [
            "100 L. Ed. 2d 384",
            "108 S. Ct. 1860",
            "486 U.S. 367",
            "1988 U.S. LEXIS 2488",
            "56 U.S.L.W. 4503"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
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
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramos v. Louisiana",
          "cluster_id": 9231323,
          "cite": [
            "140 S. Ct. 1390",
            "206 L. Ed. 2d 583"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Gates:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110959 OR 9429232 OR 9429233 OR 9429234 OR 9429235) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzI5MTIzMjAwMDAwJnM9MTAxNDUzMzkmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110959+OR+9429232+OR+9429233+OR+9429234+OR+9429235%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 2,
        "triage_snippet_classified": 198
      },
      "lane2_top_cited": {
        "query": "cites:(110959 OR 9429232 OR 9429233 OR 9429234 OR 9429235)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04MjImcz0xMTExNzImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110959+OR+9429232+OR+9429233+OR+9429234+OR+9429235%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110959 OR 9429232 OR 9429233 OR 9429234 OR 9429235)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzQ0ODQ4MDAwMDAwJnM9MTAzODA1NDImdD1vJmQ9MjAyNi0wNy0wNiZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110959+OR+9429232+OR+9429233+OR+9429234+OR+9429235%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 2,
        "triage_snippet_classified": 198
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110959 OR 9429232 OR 9429233 OR 9429234 OR 9429235)",
    "indexed_citing_opinions": 10044,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110959,
        "count": 8815,
        "count_source": "search"
      },
      {
        "opinion_id": 9429232,
        "count": 1423,
        "count_source": "search"
      },
      {
        "opinion_id": 9429233,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429234,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429235,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 16734,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/illinois-v-gates.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk4MDM4Njcmcz0yMjk4NDE2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110959+OR+9429232+OR+9429233+OR+9429234+OR+9429235%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110959,
        "cited_id": 93933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 95004,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 101335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 103320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 103597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 104087,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 104668,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 106783,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107526,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107577,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 107900,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108379,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108497,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108737,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 108905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109303,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109349,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 109925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110236,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110425,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110916,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 110926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 312873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 326825,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 378896,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 1123854,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 2023247,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 2100482,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 2151397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 2333704,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 2433225,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110959,
        "cited_id": 2620876,
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
    "date_created": "2026-07-05T07:54:35Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:55:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:55:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:59:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:55:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Illinois v. Gates

```
<opinion type="majority">
<author id="b260-4"><page-number citation-index="1" label="216">*216</page-number>Justice Rehnquist</author>
<p id="AKb">delivered the opinion of the Court.</p>
<p id="A6a">Respondents Lance and Susan Gates were indicted for violation of state drug laws after police officers, executing a search warrant, discovered marihuana and other contraband in their automobile and home. Prior to trial the Gateses moved to suppress evidence seized during this search. The Illinois Supreme Court affirmed the decisions of lower state courts granting the motion. <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/" aria-description="Citation for case: People of Illinois v. Gates">85 Ill. 2d 376</a></span>, <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/" aria-description="Citation for case: People of Illinois v. Gates">423 N. E. 2d 887</a></span> (1981). ■ It held that the affidavit submitted in support of the State’s application for a warrant to search the Gateses’ prop<page-number citation-index="1" label="217">*217</page-number>erty was inadequate under this Court’s decisions in <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), and <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969).</p>
<p id="Alt">We granted certiorari to consider the application of the Fourth Amendment to a magistrate’s issuance of a search warrant on the basis of a partially corroborated anonymous informant’s tip. <span class="citation multiple-matches"><a href="/c/U.%20S./454/1140/">454 U. S. 1140</a></span> (1982). After receiving briefs and hearing oral argument on this question, however, we requested the parties to address an additional question:</p>
<blockquote id="A63">“[Wjhether the rule requiring the exclusion at a criminal trial of evidence obtained in violation of the Fourth Amendment, <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961); <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), should to any extent be modified, so as, for example, not to require the exclusion of evidence obtained in the reasonable belief that the search and seizure at issue was consistent with the Fourth Amendment.” <span class="citation" data-id="9429042"><a href="/opinion/110850/illinois-v-gates-et-ux/" aria-description="Citation for case: Illinois v. Gates Et Ux.">459 U. S. 1028</a></span> (1982).</blockquote>
<p id="Aelb">We decide today, with apologies to all, that the issue we framed for the parties was not presented to the Illinois courts and, accordingly, do not address it. Rather, we consider the question originally presented in the petition for certiorari, and conclude that the Illinois Supreme Court read the requirements of our Fourth Amendment decisions too restrictively. Initially, however, we set forth our reasons for not addressing the question regarding modification of the exclusionary rule framed in our order of November 29,1982. <em><span class="citation" data-id="9429042"><a href="/opinion/110850/illinois-v-gates-et-ux/" aria-description="Citation for case: Illinois v. Gates Et Ux.">Ibid.</a></span></em></p>
<p id="AqtE">HH</p>
<p id="A9_">Our certiorari jurisdiction over decisions from state courts derives from <span class="citation no-link">28 U. S. C. § 1257</span>, which provides that “[f]inal judgments or decrees rendered by the highest court of a State in which a decision could be had, may be reviewed by the Supreme Court as follows: ... (3) By writ of certiorari, . . . where any title, right, privilege or immunity is specially set up or claimed under the Constitution, treaties or statutes <page-number citation-index="1" label="218">*218</page-number>of... the United States.” The provision derives, albeit with important alterations, see, <em>e. g., </em>Act of Dec. 23, 1914, ch. 2, <span class="citation no-link">38 Stat. 790</span>; Act of June 25, 1948, § 1257, <span class="citation no-link">62 Stat. 929</span>, from the Judiciary Act of 1789, § 25, <span class="citation no-link">1 Stat. 85</span>.</p>
<p id="b262-5">Although we have spoken frequently on the meaning of §1257 and its predecessors, our decisions are in some respects not entirely clear. We held early on that § 25 of the Judiciary Act of 1789 furnished us with no jurisdiction unless a federal question had been both raised and decided in the state court below. As Justice Story wrote in <em>Crowell </em>v. <em>Randell, </em><span class="citation no-link">10 Pet. 368</span>, 392 (1836): “If both of these requirements do not appear on the record, the appellate jurisdiction fails.” See also <em>Owings </em>v. <em>Norwood’s Lessee, </em><span class="citation" data-id="84919"><a href="/opinion/84919/owings-v-norwoods-lessee/" aria-description="Citation for case: Owings v. Norwood&#x27;s Lessee">5 Cranch 344</a></span> (1809).<footnotemark>1</footnotemark></p>
<p id="b262-6">More recently, in <em>McGoldrick </em>v. <em>Compagnie Generale Transatlantique, </em><span class="citation" data-id="9419089"><a href="/opinion/103320/mcgoldrick-v-compagnie-generale-transatlantique/#434" aria-description="Citation for case: McGoldrick v. Compagnie Generale Transatlantique">309 U. S. 430, 434-435</a></span> (1940), the Court observed:</p>
<blockquote id="b262-7">“But it is also the settled practice of this Court, in the exercise of its appellate jurisdiction, that it is only in exceptional cases, and then only in cases coming from the federal courts, that it considers questions urged by a petitioner or appellant not pressed or passed upon in the courts below.... In cases coming here from state courts in which a state statute is assailed as unconstitutional, there are reasons of peculiar force which should lead us to refrain from deciding questions not presented or decided in the highest court of the state whose judicial action we are called upon to review. Apart from the <page-number citation-index="1" label="219">*219</page-number>reluctance with which every court should proceed to set aside legislation as unconstitutional on grounds not properly presented, due regard for the appropriate relationship of this Court to state courts requires us to decline to consider and decide questions affecting the validity of state statutes not urged or considered there. It is for these reasons that this Court, where the constitutionality of a statute has been upheld in the state court, consistently refuses to consider any grounds of attack not raised or decided in that court.”</blockquote>
<p id="b263-5">Finally, the Court seemed to reaffirm the jurisdictional character of the rule against our deciding claims “not pressed nor passed upon” in state court in <em>State Farm Mutual Automobile Ins. Co. </em>v. <em>Duel, </em><span class="citation" data-id="104087"><a href="/opinion/104087/state-farm-mutual-automobile-insurance-v-duel/#160" aria-description="Citation for case: State Farm Mutual Automobile Insurance v. Duel">324 U. S. 154, 160</a></span> (1945), where we explained that “[sjince the [State] Supreme Court did not pass on the question, we may not do so.” See also <em>Hill </em>v. <em>California, </em><span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/#805" aria-description="Citation for case: Hill v. California">401 U. S. 797, 805-806</a></span> (1971).</p>
<p id="b263-6">Notwithstanding these decisions, however, several of our more recent cases have treated the so-called “not pressed or passed upon below” rule as merely a prudential restriction. In <em>Terminiello </em>v. <em>Chicago, </em><span class="citation" data-id="9420312"><a href="/opinion/104668/terminiello-v-chicago/" aria-description="Citation for case: Terminiello v. Chicago">337 U. S. 1</a></span> (1949), the Court reversed a state criminal conviction on a ground not urged in state court, nor even in this Court. Likewise, in <em>Vachon </em>v. <em>New Hampshire, </em><span class="citation" data-id="9425500"><a href="/opinion/108905/vachon-v-new-hampshire/" aria-description="Citation for case: Vachon v. New Hampshire">414 U. S. 478</a></span> (1974), the Court summarily reversed a state criminal conviction on the ground, not raised in state court, or here, that it had been obtained in violation of the Due Process Clause of the Fourteenth Amendment. The Court indicated in a footnote, <span class="citation" data-id="9425500"><a href="/opinion/108905/vachon-v-new-hampshire/#479" aria-description="Citation for case: Vachon v. New Hampshire"><em>id., </em>at 479, n. 3</a></span>, that it possessed discretion to ignore the failure to raise in state court the question on which it decided the case.</p>
<p id="b263-7">In addition to this lack of clarity as to the character of the “not pressed or passed upon below” rule, we have recognized that it often may be unclear whether the particular federal question presented in this Court was raised or passed upon below. In <em>Dewey </em>v. <em>Des Moines, </em><span class="citation" data-id="95004"><a href="/opinion/95004/dewey-v-des-moines/#197" aria-description="Citation for case: Dewey v. Des Moines">173 U. S. 193, 197-198</a></span> (1899), the fullest treatment of the subject, the Court said <page-number citation-index="1" label="220">*220</page-number>that “[i]f the question were only an enlargement of the one mentioned in the assignment of errors, or if it were so connected with it in substance as to form but another ground or reason for alleging the invalidity of the [lower court’s] judgment, we should have no hesitation in holding the assignment sufficient to permit the question to be now raised and argued. Parties are not confined here to the same arguments which were advanced in the courts below upon a Federal question there discussed.”<footnotemark>2</footnotemark> We have not attempted, and likely would not have been able, to draw a clear-cut line between cases involving only an “enlargement” of questions presented below and those involving entirely new questions.</p>
<p id="b264-5">The application of these principles in the instant case is not entirely straightforward. It is clear in this case that respondents expressly raised, at every level of the Illinois judicial system, the claim that the Fourth Amendment had been violated by the actions of the Illinois police and that the evidence seized by the officers should be excluded from their trial. It also is clear that the State challenged, at every level of the Illinois court system, respondents’ claim that the substantive requirements of the Fourth Amendment had been violated. The State never, however, raised or addressed the question whether the federal exclusionary rule should be modified in any respect, and none of the opinions of the <page-number citation-index="1" label="221">*221</page-number>Illinois courts give any indication that the question was considered.</p>
<p id="b265-5">The case, of course, is before us on the State’s petition for a writ of certiorari. Since the Act of Dec. 23, 1914, ch. 2, <span class="citation no-link">38 Stat. 790</span>, jurisdiction has been vested in this Court to review state-court decisions even when a claimed federal right has been upheld. Our prior decisions interpreting the “not pressed or passed on below” rule have not, however, involved a State’s failure to raise a defense to a federal right or remedy asserted below. As explained below, however, we can see no reason to treat the State’s failure to have challenged an asserted federal claim differently from the failure of the proponent of a federal claim to have raised that claim.</p>
<p id="b265-6">We have identified several purposes underlying the “not pressed or passed upon” rule: for the most part, these are as applicable to the State’s failure to have opposed the assertion of a particular federal right, as to a party’s failure to have asserted the claim. First, “[questions not raised below are those on which the record is very likely to be inadequate since it certainly was not compiled with those questions in mind.” <em>Cardinale </em>v. <em>Louisiana, </em><span class="citation" data-id="107889"><a href="/opinion/107889/cardinale-v-louisiana/#439" aria-description="Citation for case: Cardinale v. Louisiana">394 U. S. 437, 439</a></span> (1969). Exactly the same difficulty exists when the State urges modification of an existing constitutional right or accompanying remedy. Here, for example, the record contains little, if anything, regarding the subjective good faith of the police officers that searched the Gateses’ property — which might well be an important consideration in determining whether to fashion a good-faith exception to the exclusionary rule. Our consideration of whether to modify the exclusionary rule plainly would benefit from a record containing such facts.</p>
<p id="b265-7">Likewise, “due regard for the appropriate relationship of this Court to state courts,” <em>McGoldrick </em>v. <em>Compagnie Generale Transatlantique, </em><span class="citation" data-id="9419089"><a href="/opinion/103320/mcgoldrick-v-compagnie-generale-transatlantique/#434" aria-description="Citation for case: McGoldrick v. Compagnie Generale Transatlantique">309 U. S., at 434-435</a></span>, demands that those courts be given an opportunity to consider the constitutionality of the actions of state officials, and, equally important, proposed changes in existing remedies for uncon<page-number citation-index="1" label="222">*222</page-number>stitutional actions. Finally, by requiring that the State first argue to the state courts that the federal exclusionary rule should be modified, we permit a state court, even if it agrees with the State as a matter of federal law, to rest its decision on an adequate and independent state ground. See <span class="citation" data-id="107889"><a href="/opinion/107889/cardinale-v-louisiana/#439" aria-description="Citation for case: Cardinale v. Louisiana"><em>Cardinale, supra, </em>at 439</a></span>. Illinois, for example, adopted an exclusionary rule as early as 1923, see <em>People </em>v. <em>Brocamp, </em><span class="citation" data-id="6980967"><a href="/opinion/7076213/people-v-brocamp/" aria-description="Citation for case: People v. Brocamp">307 Ill. 448</a></span>, <span class="citation" data-id="6980967"><a href="/opinion/7076213/people-v-brocamp/" aria-description="Citation for case: People v. Brocamp">138 N. E. 728</a></span> (1923), and might adhere to its view even if it thought we would conclude that the federal rule should be modified. In short, the reasons supporting our refusal to hear federal claims not raised in state court apply with equal force to the State’s failure to challenge the availability of a well-settled federal remedy. Whether the “not pressed or passed upon below” rule is jurisdictional, as our earlier decisions indicate, see <em>supra, </em>at 217-219, or prudential, as several of our later decisions assume, or whether its character might be different in cases like this from its character elsewhere, we need not decide. Whatever the character of the rule may be, consideration of the question presented in our order of November 29, 1982, would be contrary to the sound justifications for the “not pressed or passed upon below” rule, and we thus decide not to pass on the issue.</p>
<p id="b266-5">The fact that the Illinois courts affirmatively applied the federal exclusionary rule — suppressing evidence against respondents — does not affect our conclusion. In <em>Morrison </em>v. <em>Watson, </em><span class="citation" data-id="93933"><a href="/opinion/93933/morrison-v-watson/" aria-description="Citation for case: Morrison v. Watson">154 U. S. 111</a></span> (1894), the Court was asked to consider whether a state statute impaired the plaintiff in error’s contract with the defendant in error. It declined to hear the case because the question presented here had not been pressed or passed on below. The Court acknowledged that the lower court’s opinion had restated the conclusion, set forth in an earlier decision of that court, that the state statute did not impermissibly impair contractual obligations. Nonetheless, it held that there was no showing that “there was any real contest at any stage of this case upon the point,” <span class="citation" data-id="93933"><a href="/opinion/93933/morrison-v-watson/#115" aria-description="Citation for case: Morrison v. Watson"><em>id., </em>at 115</a></span>, and that without such a contest, the routine restate<page-number citation-index="1" label="223">*223</page-number>ment and application of settled law by an appellate court did not satisfy the “not pressed or passed upon below” rule. Similarly, in the present case, although the Illinois courts applied the federal exclusionary rule, there was never “any real contest” upon the point. The application of the exclusionary rule was merely a routine act, once a violation of the Fourth Amendment had been found, and not the considered judgment of the Illinois courts on the question whether application of a modified rule would be warranted on the facts of this case. In such circumstances, absent the adversarial dispute necessary to apprise the state court of the arguments for not applying the exclusionary rule, we will not consider the question whether the exclusionary rule should be modified.</p>
<p id="b267-5">Likewise, we do not believe that the State’s repeated opposition to respondents’ substantive Fourth Amendment claims suffices to have raised the question whether the exclusionary rule should be modified. The exclusionary rule is “a judicially created remedy designed to safeguard Fourth Amendment rights generally” and not “a personal constitutional right of the party aggrieved.” <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 348</a></span> (1974). The question whether the exclusionary rule’s remedy is appropriate in a particular context has long been regardéd as an issue separate from the question whether the Fourth Amendment rights of the party seeking to invoke the rule were violated by police conduct. See, <em>e. g., United States </em>v. <em>Havens, </em><span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/" aria-description="Citation for case: United States v. Havens">446 U. S. 620</a></span> (1980); <em>United States </em>v. <em>Ceccolini, </em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">435 U. S. 268</a></span> (1978); <em>United States </em>v. <em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">Calandra, supra;</a></span> Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U. S. 465</a></span> (1976). Because of this distinction, we cannot say that modification or abolition of the exclusionary rule is “so connected with [the substantive Fourth Amendment right at issue] as to form but another ground or reason for alleging the invalidity” of the judgment. <em>Dewey </em>v. <em>Des Moines, </em><span class="citation" data-id="95004"><a href="/opinion/95004/dewey-v-des-moines/#197" aria-description="Citation for case: Dewey v. Des Moines">173 U. S., at 197-198</a></span>. Rather, the rule’s modification was, for purposes of the “not pressed or passed upon below” rule, a separate claim that had to be specifically presented to the state courts.</p>
<p id="b268-4"><page-number citation-index="1" label="224">*224</page-number>Finally, weighty prudential considerations militate against our considering the question presented in our order of November 29, 1982. The extent of the continued vitality of the rules that have developed from our decisions in <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), and <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), is an issue of unusual significance. Sufficient evidence of this lies just in the comments on the issue that Members of this Court recently have made, <em>e. g., Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#415" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388, 415</a></span> (1971) (Burger, C. J., dissenting); <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#490" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 490</a></span> (1971) (Harlan, J., concurring); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#502" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 502</a></span> (Black, J., dissenting); <em>Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#537" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 537-539</a></span> (White, J., dissenting); <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#413" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387, 413-414</a></span> (1977) (Powell, J., concurring); <em>Robbins </em>v. <em>California, </em><span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#437" aria-description="Citation for case: Robbins v. California">453 U. S. 420, 437, 443-444</a></span> (1981) (Rehnquist, J., dissenting). Where difficult issues of great public importance are involved, there are strong reasons to adhere scrupulously to the customary limitations on our discretion. By doing so we “promote respect... for the Court’s adjudicatory process [and] the stability of [our] decisions.” <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#677" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 677</a></span> (Harlan, J., dissenting). Moreover, fidelity to the rule guarantees that a factual record will be available to us, thereby discouraging the framing of broad rules, seemingly sensible on one set of facts, which may prove ill-considered in other circumstances. In Justice Harlan’s words, adherence to the rule lessens the threat of “untoward practical ramifications,” <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#676" aria-description="Citation for case: Mapp v. Ohio"><em>id., </em>at 676</a></span> (dissenting opinion), not foreseen at the time of decision. The public importance of our decisions in <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>and <em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span> </em>and the emotions engendered by the debate surrounding these decisions counsel that we meticulously observe our customary procedural rules. By following this course, we promote respect for the procedures by which our decisions are rendered, as well as confidence in the stability of prior decisions. A wise exercise of the powers confided in this Court dictates that we reserve for another day the question whether the exclusionary rule should be modified.</p>
<p id="AcZz"><page-number citation-index="1" label="225">*225</page-number>l-H H — (</p>
<p id="Aao">We now turn to the question presented in the State’s original petition for certiorari, which requires us to decide whether respondents’ rights under the Fourth and Fourteenth Amendments were violated by the search of their car and house. A chronological statement of events usefully introduces the issues at stake. Bloomingdale, Ill., is a suburb of Chicago located in Du Page County. On May 3, 1978, the Bloomingdale Police Department received by mail an anonymous handwritten letter which read as follows:</p>
<blockquote id="AAU">“This letter is to inform you that you have a couple in your town who strictly make their living on selling drugs. They are Sue and Lance Gates, they live on Greenway, off Bloomingdale Rd. in the condominiums. Most of their buys are done in Florida. Sue his wife drives their car to Florida, where she leaves it to be loaded up with drugs, then Lance flys down and drives it back. Sue flys back after she drops the car off in Florida. May 3 she is driving down there again and Lance will be flying down in a few days to drive it back. At the time Lance drives the car back he has the trunk loaded with over $100,000.00 in drugs. Presently they have over $100,000.00 worth of drugs in their basement.</blockquote>
<blockquote id="A-m">“They brag about the fact they never have to work, and make their entire living on pushers.</blockquote>
<blockquote id="AJ_">“I guarantee if you watch them carefully you will make a big catch. They are friends with some big drugs dealers, who visit their house often.</blockquote>
<blockquote id="AHsi">“Lance &amp; Susan Gates</blockquote>
<blockquote id="AIH">“Greenway</blockquote>
<blockquote id="AygP">“in Condominiums”</blockquote>
<p id="Aml">The letter was referred by the Chief of Police of the Bloomingdale Police Department to Detective Mader, who decided to pursue the tip. Mader learned, from the office of the Illinois Secretary of State, that an Illinois driver’s license had <page-number citation-index="1" label="226">*226</page-number>been issued to one Lance Gates, residing at a stated address in Bloomingdale. He contacted a confidential informant, whose examination of certain financial records revealed a more recent address for the Gateses, and he also learned from a police officer assigned to O'Hare Airport that “L. Gates” had made a reservation on Eastern Airlines Flight 245 to West Palm Beach, Fla., scheduled to depart from Chicago on May 5 at 4:15 p. m.</p>
<p id="b270-5">Mader then made arrangements with an agent of the Drug Enforcement Administration for surveillance of the May 5 Eastern Airlines flight. The agent later reported to Mader that Gates had boarded the flight, and that federal agents in Florida had observed him arrive in West Palm Beach and take a taxi to the nearby Holiday Inn. They also reported that Gates went to a room registered to one Susan Gates and that, at 7 o’clock the next morning, Gates and an unidentified woman left the motel in a Mercury bearing Illinois license plates and drove northbound on an interstate highway frequently used by travelers to the Chicago area. In addition, the DEA agent informed Mader that the license plate number on the Mercury was registered to a Hornet station wagon owned by Gates. The agent also advised Mader that the driving time between West Palm Beach and Bloomingdale was approximately 22 to 24 hours.</p>
<p id="b270-6">Mader signed an affidavit setting forth the foregoing facts, and submitted it to a judge of the Circuit Court of Du Page County, together with a copy of the anonymous letter. The judge of that court thereupon issued a search warrant for the Gateses' residence and for their automobile. The judge, in deciding to issue the warrant, could have determined that the <em>modus operandi of </em>the Gateses had been substantially corroborated. As the anonymous letter predicted, Lance Gates had flown from Chicago to West Palm Beach late in the afternoon of May 5th, had checked into a hotel room registered in the name of his wife, and, at 7 o’clock the following morning, had headed north, accompanied by an unidentified woman, <page-number citation-index="1" label="227">*227</page-number>out of West Palm Beach on an interstate highway used by travelers from South Florida to Chicago in an automobile bearing a license plate issued to him.</p>
<p id="b271-5">At 5:15 a. m. on March 7, only 36 hours after he had flown out of Chicago, Lance Gates, and his wife, returned to their home in Bloomingdale, driving the car in which they had left West Palm Beach some 22 hours earlier. The Bloomingdale police were awaiting them, searched the trunk of the Mercury, and uncovered approximately 350 pounds of marihuana. A search of the Gateses’ home revealed marihuana, weapons, and other contraband. The Illinois Circuit Court ordered suppression of all these items, on the ground that the affidavit submitted to the Circuit Judge failed to support the necessary determination of probable cause to believe that the Gateses’ automobile and home contained the contraband in question. This decision was affirmed in turn by the Illinois Appellate Court, <span class="citation" data-id="2151397"><a href="/opinion/2151397/people-v-gates/" aria-description="Citation for case: People v. Gates">82 Ill. App. 3d 749</a></span>, <span class="citation" data-id="2151397"><a href="/opinion/2151397/people-v-gates/" aria-description="Citation for case: People v. Gates">403 N. E. 2d 77</a></span> (1980), and by a divided vote of the Supreme Court of Illinois. <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/" aria-description="Citation for case: People of Illinois v. Gates">85 Ill. 2d 376</a></span>, <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/" aria-description="Citation for case: People of Illinois v. Gates">423 N. E. 2d 887</a></span> (1981).</p>
<p id="b271-6">The Illinois Supreme Court concluded — and we are inclined to agree — that, standing alone, the anonymous letter sent to the Bloomingdale Police Department would not provide the basis for a magistrate’s determination that there was probable cause to believe contraband would be found in the Gateses’ car and home. The letter provides virtually nothing from which one might conclude that its author is either honest or his information reliable; likewise, the letter gives absolutely no indication of the basis for the writer’s predictions regarding the Gateses’ criminal activities. Something more was required, then, before a magistrate could conclude that there was probable cause to believe that contraband would be found in the Gateses’ home and car. See <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#109" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 109, n. 1</a></span>; <em>Nathanson </em>v. <em>United States, </em><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span> (1933).</p>
<p id="b271-7">The Illinois Supreme Court also properly recognized that Detective Mader’s affidavit might be capable of supplement<page-number citation-index="1" label="228">*228</page-number>ing the anonymous letter with information sufficient to permit a determination of probable cause. See <em>Whiteley </em>v. <em>Warden, </em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/#567" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560, 567</a></span> (1971). In holding that the affidavit in fact did not contain sufficient additional information to sustain a determination of probable cause, the Illinois court applied a “two-pronged test,” derived from our decision in <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969).<footnotemark>3</footnotemark> The Illinois Supreme Court, like some others, apparently understood <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>as requiring that the anonymous letter satisfy each of two independent requirements before it could be relied on. <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#383" aria-description="Citation for case: People of Illinois v. Gates">85 Ill. 2d, at 383</a></span>, <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#890" aria-description="Citation for case: People of Illinois v. Gates">423 N. E. 2d, at 890</a></span>. According to this view, the letter, as supplemented by Mader’s affidavit, first had to adequately reveal the “basis of knowledge” of the letterwriter — the particular means by which he came by the information given in his report. Second, it had to pro<page-number citation-index="1" label="229">*229</page-number>vide facts sufficiently establishing either the “veracity” of the affiant’s informant, or, alternatively, the “reliability” of the informant’s report in this particular case.</p>
<p id="b273-5">The Illinois court, alluding to an elaborate set of legal rules that have developed among various lower courts to enforce the “two-pronged test,”<footnotemark>4</footnotemark> found that the test had not been satisfied. First, the “veracity” prong was not satisfied because, “[t]here was simply no basis [for] concluding] that the anonymous person [who wrote the letter to the Bloomingdale Police Department] was credible.” <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#385" aria-description="Citation for case: People of Illinois v. Gates"><em>Id., </em>at 385</a></span>, <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#891" aria-description="Citation for case: People of Illinois v. Gates">423 N. E. 2d, at 891</a></span>. The court indicated that corroboration by police of details contained in the letter might never satisfy the “veracity” prong, and in any event, could not do so if, as in the present case, only “innocent” details are corroborated. <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#390" aria-description="Citation for case: People of Illinois v. Gates"><em>Id., </em>at 390</a></span>, <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#893" aria-description="Citation for case: People of Illinois v. Gates">423 N. E. 2d, at 893</a></span>. In addition, the letter gave no indication of the basis of its writer’s knowledge of the <page-number citation-index="1" label="230">*230</page-number>Gateses’ activities. The Illinois court understood <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>as permitting the detail contained in a tip to be used to infer that the informant had a reliable basis for his statements, but it thought that the anonymous letter failed to provide sufficient detail to permit such an inference. Thus, it concluded that no showing of probable cause had been made.</p>
<p id="b274-5">We agree with the Illinois Supreme Court that an informant’s “veracity,” “reliability,” and “basis of knowledge” are all highly relevant in determining the value of his report. We do not agree, however, that these elements should be understood as entirely separate and independent requirements to be rigidly exacted in every case,<footnotemark>5</footnotemark> which the opinion of the Supreme Court of Illinois would imply. Rather, as detailed below, they should be understood simply as closely intertwined issues that may usefully illuminate the commonsense, practical question whether there is “probable cause” to believe that contraband or evidence is located in a particular place.</p>
<p id="b274-6">Ill</p>
<p id="b274-7">This totality-of-the-circumstances approach is far more consistent with our prior treatment of probable cause<footnotemark>6</footnotemark> than <page-number citation-index="1" label="231">*231</page-number>is any rigid demand that specific “tests” be satisfied by every informant’s tip. Perhaps the central teaching of our decisions bearing on the probable-cause standard is that it is a “practical, nontechnical conception.” <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span> (1949). “In dealing with probable cause, ... as the very name implies, we deal with probabilities. These are not technical; they are the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act.” <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States"><em>Id., </em>at 175</a></span>. Our observation in <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#418" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 418</a></span> (1981), regarding “particularized suspicion,” is also applicable to the probable-cause standard:</p>
<blockquote id="b275-5">“The process does not deal with hard certainties, but with probabilities. Long before the law of probabilities was articulated as such, practical people formulated certain common-sense conclusions about human behavior; jurors as factfinders are permitted to do the same — and <page-number citation-index="1" label="232">*232</page-number>so are law enforcement officers. Finally, the evidence thus collected must be seen and weighed not in terms of library analysis by scholars, but as understood by those versed in the field of law enforcement.”</blockquote>
<p id="b276-5">As these comments illustrate, probable cause is a fluid concept — turning on the assessment of probabilities in particular factual contexts — not readily, or even usefully, reduced to a neat set of legal rules. Informants’ tips doubtless come in many shapes and sizes from many different types of persons. As we said in <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#147" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 147</a></span> (1972): “Informants’ tips, like all other clues and evidence coming to a policeman on the scene, may vary greatly in their value and reliability.” Rigid legal rules are ill-suited to an area of such diversity. “One simple rule will not cover every situation.” <em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">Ibid.</a></span></em><footnotemark><em>7</em></footnotemark></p>
<p id="b277-4"><page-number citation-index="1" label="233">*233</page-number>Moreover, the “two-pronged test” directs analysis into two largely independent channels — the informant’s “veracity” or “reliability” and his “basis of knowledge.” See nn. 4 and 5, <em>supra. </em>There are persuasive arguments against according these two elements such independent status. Instead, they are better understood as relevant considerations in the totality-of-the-circumstances analysis that traditionally has guided probable-cause determinations: a deficiency in one may be compensated for, in determining the overall reliability of a tip, by a strong showing as to the other, or by some other indicia of reliability. See, <em>e. g., Adams </em>v. <em>Williams, supra, </em>at 146-147; <em>United States </em>v. <em>Harris, </em><span class="citation" data-id="9883118"><a href="/opinion/108379/united-states-v-harris/" aria-description="Citation for case: United States v. Harris">403 U. S. 573</a></span> (1971).</p>
<p id="b277-5">If, for example, a particular informant is known for the unusual reliability of his predictions of certain types of criminal activities in a locality, his failure, in a particular case, to thoroughly set forth the basis of his knowledge surely should not serve as an absolute bar to a finding of probable cause based on his tip. See <em>United States </em>v. <em>Sellers, </em><span class="citation" data-id="312873"><a href="/opinion/312873/united-states-v-charles-e-sellers-jr/" aria-description="Citation for case: United States v. Charles E. Sellers, Jr.">483 F. 2d 37</a></span> (CA5 1973).<footnotemark>8</footnotemark> Likewise, if an unquestionably honest citizen comes forward with a report of criminal activity — which if fabricated would subject him to criminal liability — we have found <page-number citation-index="1" label="234">*234</page-number>rigorous scrutiny of the basis of his knowledge unnecessary. <em>Adams </em>v. <em>Williams, supra. </em>Conversely, even if we entertain some doubt as to an informant’s motives, his explicit and detailed description of alleged wrongdoing, along with a statement that the event was observed firsthand, entitles his tip to greater weight than might otherwise be the case. Unlike a totality-of-the-circumstances analysis, which permits a balanced assessment of the relative weights of all the various indicia of reliability (and unreliability) attending an informant’s tip, the “two-pronged test” has encouraged an excessively technical dissection of informants’ tips,<footnotemark>9</footnotemark> with undue at<page-number citation-index="1" label="235">*235</page-number>tention being focused on isolated issues that cannot sensibly be divorced from the other facts presented to the magistrate.</p>
<p id="b279-4">As early as <em>Locke </em>v. <em>United States, </em><span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/#348" aria-description="Citation for case: Locke v. United States">7 Cranch 339, 348</a></span> (1813), Chief Justice Marshall observed, in a closely related context: “[T]he term ‘probable cause,’ according to its usual acceptation, means less than evidence which would justify condemnation .... It imports a seizure made under circumstances which warrant suspicion.” More recently, we said that “the <em>quanta </em>... of proof” appropriate in ordinary judicial proceedings are inapplicable to the decision to issue a warrant. <em>Brinegar, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#173" aria-description="Citation for case: Brinegar v. United States">338 U. S., at 173</a></span>. Finely tuned standards such as proof beyond a reasonable doubt or by a preponderance of the evidence, useful in formal trials, have no place in the magistrate’s decision. While an effort to fix some general, numerically precise degree of certainty corresponding to “probable cause” may not be helpful, it is clear that “only the probability, and not a prima facie showing, of criminal activity is the standard of probable cause.” <em>Spinelli, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#419" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 419</a></span>. See Model Code of Pre-Arraignment Procedure §210.1(7) (Prop. Off. Draft 1972); 1 W. LaFave, Search and Seizure § 3.2(e) (1978).</p>
<p id="b279-5">We also have recognized that affidavits “are normally drafted by nonlawyers in the midst and haste of a criminal investigation. Technical requirements of elaborate specificity once exacted under common law pleadings have no proper place in this area.” <em>United States </em>v. <em>Ventresca, </em><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 108</a></span> (1965). Likewise, search and arrest warrants long have been issued by persons who are neither lawyers nor judges, and who certainly do not remain abreast of each judicial refinement of the nature of “probable cause.” See <em>Shadwick </em>v. <em>City of Tampa, </em><span class="citation" data-id="108582"><a href="/opinion/108582/shadwick-v-city-of-tampa/#348" aria-description="Citation for case: Shadwick v. City of Tampa">407 U. S. 345, 348-350</a></span> (1972). The rigorous inquiry into the <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>prongs and the complex superstructure of evidentiary and analytical rules that some have seen implicit in our <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>decision, cannot be reconciled with the fact that many warrants are — quite properly, 407 U. S., at 348-350 — issued on the basis of nontechnical, <page-number citation-index="1" label="236">*236</page-number>common-sense judgments of laymen applying a standard less demanding than those used in more formal legal proceedings. Likewise, given the informal, often hurried context in which it must be applied, the “built-in subtleties,” <em>Stanley </em>v. <em>State, </em><span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/#528" aria-description="Citation for case: Stanley v. State">19 Md. App. 507, 528</a></span>, <span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/#860" aria-description="Citation for case: Stanley v. State">313 A. 2d 847, 860</a></span> (1974), of the “two-pronged test” are particularly unlikely to assist magistrates in determining probable cause.</p>
<p id="b280-5">Similarly, we have repeatedly said that after-the-fact scrutiny by courts of the sufficiency of an affidavit should not take the form of <em>de novo </em>review. A magistrate's “determination of probable cause should be paid great deference by reviewing courts.” <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#419" aria-description="Citation for case: Spinelli v. United States"><em>Spinelli, supra, </em>at 419</a></span>. “A grudging or negative attitude by reviewing courts toward warrants,” <em>Ventresca, </em><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca">380 U. S., at 108</a></span>, is inconsistent with the Fourth Amendment’s strong preference for searches conducted pursuant to a warrant; “courts should not invalidate warrants] by interpreting affidavits] in a hypertechnical, rather than a commonsense, manner.” <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#109" aria-description="Citation for case: United States v. Ventresca"><em>Id., </em>at 109</a></span>.</p>
<p id="b280-6">If the affidavits submitted by police officers are subjected to the type of scrutiny some courts have deemed appropriate, police might well resort to warrantless searches, with the hope of relying on consent or some other exception to the Warrant Clause that might develop at the time of the search. In addition, the possession of a warrant by officers conducting an arrest or search greatly reduces the perception of unlawful or intrusive police conduct, by assuring “the individual whose property is searched or seized of the lawful authority of the executing officer, his need to search, and the limits of his power to search.” <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#9" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 9</a></span> (1977). Reflecting this preference for the warrant process, the traditional standard for review of an issuing magistrate’s probable-cause determination has been that so long as the magistrate had a “substantial basis for . . . concluding]” that a search would uncover evidence of wrongdoing, the Fourth Amendment requires no more. <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#271" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 271</a></span> (1960). See <em>United States </em>v. <page-number citation-index="1" label="237">*237</page-number><em>Harris, </em><span class="citation" data-id="9883118"><a href="/opinion/108379/united-states-v-harris/#577" aria-description="Citation for case: United States v. Harris">403 U. S., at 577-583</a></span>.<footnotemark>10</footnotemark> We think reaffirmation of this standard better serves the purpose of encouraging recourse to the warrant procedure and is more consistent with our traditional deference to the probable-cause determinations of magistrates than is the “two-pronged test.”</p>
<p id="b281-5">Finally, the direction taken by decisions following <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>poorly serves “[t]he most basic function of any government”: “to provide for the security of the individual and of his property.” <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#539" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 539</a></span> (1966) (White, J., dissenting). The strictures that inevitably accompany the “two-pronged test” cannot avoid seriously impeding the task of law enforcement, see, <em>e. g., </em>n. 9, <em>supra. </em>If, as the Illinois Supreme Court apparently thought, that test must be rigorously applied in every case, anonymous tips would be of greatly diminished value in police work. Ordinary citizens, like ordinary witnesses, see Advisory Committee’s Notes on Fed. Rule Evid. 701, 28 U. S. C. App., p. 570, generally do not provide extensive recitations of the basis of their everyday observations. Likewise, as the Illinois Supreme Court observed in this case, the veracity of persons supplying anonymous tips is by hypothesis largely unknown, and unknowable. As a result, anonymous tips seldom could survive a rigorous application of either of the <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>prongs. Yet, such tips, particularly when supplemented by <page-number citation-index="1" label="238">*238</page-number>independent police investigation, frequently contribute to the solution of otherwise “perfect crimes.” While a conscientious assessment of the basis for crediting such tips is required by the Fourth Amendment, a standard that leaves virtually no place for anonymous citizen informants is not.</p>
<p id="b282-5">For all these reasons, we conclude that it is wiser to abandon the “two-pronged test” established by our decisions in <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span> </em>and Spinelli.<footnotemark>11</footnotemark> In its place we reaffirm the totality-of-the-circumstances analysis that traditionally has informed probable-cause determinations. See <em>Jones </em>v. <em>United States, supra; United States </em>v. <em>Ventresca, </em><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102</a></span> (1965); <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949). The task of the issuing magistrate is simply to make a practical, commonsense decision whether, given all the circumstances set forth in the affidavit before him, including the “veracity” and “basis of knowledge” of persons supplying hearsay information, there is a fair probability that contraband or evidence of a crime will be found in a particular place. And the duty of a reviewing court is simply to ensure that the magistrate had a “substantial basis for . . . concluding]” that probable cause <page-number citation-index="1" label="239">*239</page-number>existed. <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#271" aria-description="Citation for case: Jones v. United States">362 U. S., at 271</a></span>. We are convinced that this flexible, easily applied standard will better achieve the accommodation of public and private interests that the Fourth Amendment requires than does the approach that has developed from <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span> </em>and <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>.</em></p>
<p id="b283-5">Our earlier cases illustrate the limits beyond which a magistrate may not venture in issuing a warrant. A sworn statement of an affiant that “he has cause to suspect and does believe” that liquor illegally brought into the United States is located on certain premises will not do. <em>Nathanson </em>v. <em>United States, </em><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span> (1933). An affidavit must provide the magistrate with a substantial basis for determining the existence of probable cause, and the wholly conclusory statement at issue in <em><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span> </em>failed to meet this requirement. An officer’s statement that “[a]ffiants have received reliable information from a credible person and do believe” that heroin is stored in a home, is likewise inadequate. <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964). As in <em><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span>, </em>this is a mere conclusory statement that gives the magistrate virtually no basis at all for making a judgment regarding probable cause. Sufficient information must be presented to the magistrate to allow that official to determine probable cause; his action cannot be a mere ratification of the bare conclusions of others. In order to ensure that such an abdication of the magistrate’s duty does not occur, courts must continue to conscientiously review the sufficiency of affidavits on which warrants are issued. But when we move beyond the “bare bones” affidavits present in cases such as <em><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span> </em>and <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>, </em>this area simply does not lend itself to a prescribed set of rules, like that which had developed from <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>. </em>Instead, the flexible, common-sense standard articulated in <em>Jones, Ventresca, </em>and <em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar</a></span> </em>better serves the purposes of the Fourth Amendment’s probable-cause requirement.</p>
<p id="b283-6">Justice Brennan’s dissent suggests in several places that the approach we take today somehow downgrades the <page-number citation-index="1" label="240">*240</page-number>role of the neutral magistrate, because <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span> </em>and <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>“preserve the role of magistrates as independent arbiters of probable cause . . . <em>Post, </em>at 287. Quite the contrary, we believe, is the case. The essential protection of the warrant requirement of the Fourth Amendment, as stated in <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (1948), is in “requiring that [the usual inferences which reasonable men draw from evidence] be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime.” <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States"><em>Id., </em>at 13-14</a></span>. Nothing in our opinion in any way lessens the authority of the magistrate to draw such reasonable inferences as he will from the material supplied to him by applicants for a warrant; indeed, he is freer than under the regime of <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span> </em>and <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>to draw such inferences, or to refuse to draw them if he is so minded.</p>
<p id="b284-6">The real gist of Justice Brennan’s criticism seems to be a second argument, somewhat at odds with the first, that magistrates should be restricted in their authority to make probable-cause determinations by the standards laid down in Aguilar and <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>, </em>and that such findings “should not be authorized unless there is some assurance that the information on which they are based has been obtained in a reliable way by an honest or credible person.” <em>Post, </em>at 283. However, under our opinion magistrates remain perfectly free to exact such assurances as they deem necessary, as well as those required by this opinion, in making probable-cause determinations. Justice Brennan would apparently prefer that magistrates be restricted in their findings of probable cause by the development of an elaborate body of case law dealing with the “veracity” prong of the <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>test, which in turn is broken down into two “spurs” — the informant’s “credibility” and the “reliability” of his information, together with the “basis of knowledge” prong of the <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>test. See n. 4, <em>supra. </em>That such a labyrinthine body of judicial refinement bears any relationship to familiar definitions of <page-number citation-index="1" label="241">*241</page-number>probable cause is hard to imagine. As previously noted, probable cause deals “with probabilities. These are not technical; they are the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act <em>"Brinegar v. United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S., at 175</a></span>.</p>
<p id="b285-5">Justice Brennan’s dissent also suggests that “[w]ords such as ‘practical,’ ‘nontechnical,’ and ‘common sense,’ as used in the Court’s opinion, are but code words for an overly permissive attitude towards police practices in derogation of the rights secured by the Fourth Amendment.” <em>Post, </em>at 290. An easy, but not a complete, answer to this rather florid statement would be that nothing we know about Justice Rutledge suggests that he would have used the words he chose in <em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar</a></span> </em>in such a manner. More fundamentally, no one doubts that “under our Constitution only measures consistent with the Fourth Amendment may be employed by government to cure [the horrors of drug trafficking],” <em>post, </em>at 290; but this agreement does not advance the inquiry as to which measures are, and which measures are not, consistent with the Fourth Amendment. “Fidelity” to the commands of the Constitution suggests balanced judgment rather than exhortation. The highest “fidelity” is not achieved by the judge who instinctively goes furthest in upholding even the most bizarre claim of individual constitutional rights, any more than it is achieved by a judge who instinctively goes furthest in accepting the most restrictive claims of governmental authorities. The task of this Court, as of other courts, is to “hold the balance true,” and we think we have done that in this case.</p>
<p id="b285-6">IV</p>
<p id="b285-7">Our decisions applying the totality-of-the-circumstances analysis outlined above have consistently recognized the value of corroboration of details of an informant’s tip by independent police work. In <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#269" aria-description="Citation for case: Jones v. United States">362 U. S., at 269</a></span>, we held that an affidavit relying on hearsay “is not to <page-number citation-index="1" label="242">*242</page-number>be deemed insufficient on that score, so long as a substantial basis for crediting the hearsay is presented.” We went on to say that even in making a warrantless arrest an officer “may rely upon information received through an informant, rather than upon his direct observations, so long as the informant’s statement is reasonably corroborated by other matters within the officer’s knowledge.” <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Ibid.</a></span> </em>Likewise, we recognized the probative value of corroborative efforts of police officials in <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span> </em>— the source of the “two-pronged test” — by observing that if the police had made some effort to corroborate the informant’s report at issue, “an entirely different case” would have been presented. <em>Aguilar, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#109" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 109, n. 1</a></span>.</p>
<p id="b286-5">Our decision in <em>Draper </em>v. <em>United States, </em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959), however, is the classic case on the value of corroborative efforts of police officials. There, an informant named Hereford reported that Draper would arrive in Denver on a train from Chicago on one of two days, and that he would be carrying a quantity of heroin. The informant also supplied a fairly detailed physical description of Draper, and predicted that he would be wearing a light colored raincoat, brown slacks, and black shoes, and would be walking “real fast.” <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#309" aria-description="Citation for case: Draper v. United States"><em>Id., </em>at 309</a></span>. Hereford gave no indication of the basis for his information.<footnotemark>12</footnotemark></p>
<p id="b286-6">On one of the stated dates police officers observed a man matching this description exit a train arriving from Chicago; his attire and luggage matched Hereford’s report and he was <page-number citation-index="1" label="243">*243</page-number>walking rapidly. We explained in <em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span> </em>that, by this point in his investigation, the arresting officer “had personally verified every facet of the information given him by Hereford except whether petitioner had accomplished his mission and had the three ounces of heroin on his person or in his bag. And surely, with every other bit of Hereford’s information being thus personally verified, [the officer] had ‘reasonable grounds’ to believe that the remaining unverified bit of Hereford’s information — that Draper would have the heroin with him — was likewise true,” <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#313" aria-description="Citation for case: Draper v. United States"><em>id., </em>at 313</a></span>.</p>
<p id="b287-5">The showing of probable cause in the present case was fully as compelling as that in <em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span>. </em>Even standing alone, the facts obtained through the independent investigation of Mader and the DEA at least suggested that the Gateses were involved in drug trafficking. In addition to being a popular vacation site, Florida is well known as a source of narcotics and other illegal drugs. See <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#562" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 562</a></span> (1980) (Powell, J., concurring in part and concurring in judgment); DEA, Narcotics Intelligence Estimate, The Supply of Drugs to the U. S. Illicit Market From Foreign and Domestic Sources in 1980, pp. 8-9. Lance Gates’ flight to West Palm Beach, his brief, overnight stay in a motel, and apparent immediate return north to Chicago in the family car, conveniently awaiting him in West Palm Beach, is as suggestive of a prearranged drug run, as it is of an ordinary vacation trip.</p>
<p id="b287-6">In addition, the judge could rely on the anonymous letter, which had been corroborated in major part by Mader's efforts — just as had occurred in <em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span>.</em><footnotemark><em>13</em></footnotemark><em> </em>The Supreme Court <page-number citation-index="1" label="244">*244</page-number>of Illinois reasoned that <em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span> </em>involved an informant who had given reliable information on previous occasions, while the honesty and reliability of the anonymous informant in this case were unknown to the Bloomingdale police. While this distinction might be an apt one at the time the Police Department received the anonymous letter, it became far less significant after Mader’s independent investigative work occurred. The corroboration of the letter’s predictions that the Gateses’ car would be in Florida, that Lance Gates would fly to Florida in the next day or so, and that he would drive the car north toward Bloomingdale all indicated, albeit not with certainty, that the informant’s other assertions also were true. “[Bjecause an informant is right about some things, he is more probably right about other facts,” <em>Spinelli, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#427" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 427</a></span> (White, J., concurring) — including the claim regarding the Gateses’ illegal activity. This may well not be the type of “reliability” or “veracity” necessary to satisfy some views of the “veracity prong” of <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>, </em>but we think it suffices for the practical, common-sense judgment called for in making a probable-cause determination. It is enough, for purposes of assessing probable cause, that “[corroboration through other sources of information reduced the <page-number citation-index="1" label="245">*245</page-number>chances of a reckless or prevaricating tale,” thus providing “a substantial basis for crediting the hearsay.” <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#269" aria-description="Citation for case: Jones v. United States">362 U. S., at 269, 271</a></span>.</p>
<p id="b289-5">Finally, the anonymous letter contained a range of details relating not just to easily obtained facts and conditions existing at the time of the tip, but to future actions of third parties ordinarily not easily predicted. The letterwriter’s accurate information as to the travel plans of each of the Gateses was of a character likely obtained only from the Gateses themselves, or from someone familiar with their not entirely ordinary travel plans. If the informant had access to accurate information of this type a magistrate could properly conclude that it was not unlikely that he also had access to reliable information of the Gateses’ alleged illegal activities.<footnotemark>14</footnotemark> Of <page-number citation-index="1" label="246">*246</page-number>course, the Gateses’ travel plans might have been learned from a talkative neighbor or travel agent; under the “two-pronged test” developed from <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>, </em>the character of the details in the anonymous letter might well not permit a sufficiently clear inference regarding the letterwriter’s “basis of knowledge.” But, as discussed previously, <em>supra, </em>at 235, probable cause does not demand the certainty we associate with formal trials. It is enough that there was a fair probability that the writer of the anonymous letter had obtained his entire story either from the Gateses or someone they trusted. And corroboration of major portions of the letter’s predictions provides just this probability. It is apparent, therefore, that the judge issuing the warrant had a “substantial basis for . . . conclud[ing]” that probable cause to search the Gateses’ home and car existed. The judgment of the Supreme Court of Illinois therefore must be</p>
<p id="b290-4">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b262-8"> The apparent rule of <em>Crowell </em>v. <em><span class="citation no-link">Randell</span> </em>that a federal claim have been <em>both </em>raised and addressed in state court was generally not understood in the literal fashion in which it was phrased. See R. Robertson &amp; F. Kirkham, Jurisdiction of the Supreme Court of the United States § 60 (1951). Instead, the Court developed the rule that a claim would not be considered here unless it had been <em>either </em>raised or squarely considered and resolved in state court. See, <em>e. g., McGoldrick </em>v. <em>Compagnie Generale Transatlantique, </em><span class="citation" data-id="9419089"><a href="/opinion/103320/mcgoldrick-v-compagnie-generale-transatlantique/#434" aria-description="Citation for case: McGoldrick v. Compagnie Generale Transatlantique">309 U. S. 430, 434-435</a></span> (1940); <em>State Farm Mutual Ins. Co. </em>v. <em>Duel, </em><span class="citation" data-id="104087"><a href="/opinion/104087/state-farm-mutual-automobile-insurance-v-duel/#160" aria-description="Citation for case: State Farm Mutual Automobile Insurance v. Duel">324 U. S. 154, 160</a></span> (1945).</p>
</footnote>
<footnote label="2">
<p id="b264-6"> In <em><span class="citation" data-id="95004"><a href="/opinion/95004/dewey-v-des-moines/" aria-description="Citation for case: Dewey v. Des Moines">Dewey</a></span>, </em>certain assessments had been levied against the owner of property abutting a street paved by the city; a state trial court ordered that the property be forfeited when the assessments were not paid, and in addition, held the plaintiff in error personally liable for the amount by which the assessments exceeded the value of the lots. In state court the plaintiff in error argued that the imposition of personal liability against him violated the Due Process Clause of the Fourteenth Amendment, because he had not received personal notice of the assessment proceedings. In this Court, he also attempted to argue that the assessment itself constituted a taking under the Fourteenth Amendment. The Court held that, beyond arising from a single factual occurrence, the two claims “are not in anywise necessarily connected,” <span class="citation" data-id="95004"><a href="/opinion/95004/dewey-v-des-moines/#198" aria-description="Citation for case: Dewey v. Des Moines">173 U. S., at 198</a></span>. Because of this, we concluded that the plaintiff in error’s taking claim could not be considered.</p>
</footnote>
<footnote label="3">
<p id="b272-5"> In <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>, </em>police officers observed Mr. Spinelli going to and from a particular apartment, which the telephone company said contained two telephones with stated numbers. The officers also were “informed by a confidential reliable informant that William Spinelli [was engaging in illegal gambling activities]” at the apartment, and that he used two phones, with numbers corresponding to those possessed by the police. <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#414" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 414</a></span>. The officers submitted an affidavit with this information to a magistrate and obtained a warrant to search Spinelli’s apartment. We held that the magistrate could have made his determination of probable cause only by “abdicating his constitutional function,” <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#416" aria-description="Citation for case: Spinelli v. United States"><em>id., </em>at 416</a></span>. The Government’s affidavit contained absolutely no information regarding the informant’s reliability. Thus, it did not satisfy Aguilar*s requirement that such affidavits contain “some of the underlying circumstances” indicating that “the informant . . . was ‘credible’” or that “his information [was] ‘reliable.’” <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#114" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108, 114</a></span> (1964). In addition, the tip failed to satisfy <em>Aguilar’s </em>requirement that it detail “some of the underlying circumstances from which the informant concluded that. . . narcotics were where he claimed they were.” <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Ibid.</a></span> </em>We also held that if the tip concerning Spinelli had contained “sufficient detail” to permit the magistrate to conclude “that he [was] relying on something more substantial than a casual rumor circulating in the underworld or an accusation based merely on an individual’s general reputation,” <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#416" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 416</a></span>, then he properly could have relied on it; we thought, however, that the tip lacked the requisite detail to permit this “self-verifying detail” analysis.</p>
</footnote>
<footnote label="4">
<p id="b273-6"> See, <em>e. g., Stanley </em>v. <em>State, </em><span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/" aria-description="Citation for case: Stanley v. State">19 Md. App. 507</a></span>, <span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/" aria-description="Citation for case: Stanley v. State">313 A. 2d 847</a></span> (1974). In summary, these rules posit that the “veracity” prong of the <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>test has two “spurs” — the informant’s “credibility” and the “reliability” of his information. Various interpretations are advanced for the meaning of the “reliability” spur of the “veracity” prong. Both the “basis of knowledge” prong and the “veracity” prong are treated as entirely separate requirements, which must be independently satisfied in every case in order to sustain a determination of probable cause. See n. 5, <em>infra. </em>Some ancillary doctrines are relied on to satisfy certain of the foregoing requirements. For example, the “self-verifying detail” of a tip may satisfy the “basis of knowledge” requirement, although not the “credibility” spur of the “veracity” prong. See <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#388" aria-description="Citation for case: People of Illinois v. Gates">85 Ill. 2d, at 388</a></span>, <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#892" aria-description="Citation for case: People of Illinois v. Gates">423 N. E. 2d, at 892</a></span>. Conversely, corroboration would seem not capable of supporting the “basis of knowledge” prong, but only the “veracity” prong. <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#390" aria-description="Citation for case: People of Illinois v. Gates"><em>Id., </em>at 390</a></span>, <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#893" aria-description="Citation for case: People of Illinois v. Gates">423 N. E. 2d, at 893</a></span>.</p>
<p id="b273-7">The decision in <em><span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/" aria-description="Citation for case: Stanley v. State">Stanley</a></span>, </em>while expressly approving and conscientiously attempting to apply the “two-pronged test” observes that “[t]he built-in subtleties [of the test] are such, however, that a slipshod application calls down upon us the fury of Murphy’s Law.” <span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/#528" aria-description="Citation for case: Stanley v. State">19 Md. App., at 528</a></span>, <span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/#860" aria-description="Citation for case: Stanley v. State">313 A. 2d, at 860</a></span> (footnote omitted). The decision also suggested that it is necessary to “evolve analogous guidelines [to hearsay rules employed in trial settings] for the reception of hearsay in a probable cause setting.” <span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/#522" aria-description="Citation for case: Stanley v. State"><em>Id., </em>at 522, n. 12</a></span>, <span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/#857" aria-description="Citation for case: Stanley v. State">313 A. 2d, at 857, n. 12</a></span>.</p>
</footnote>
<footnote label="5">
<p id="b274-8"> The entirely independent character that the <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>prongs have assumed is indicated both by the opinion of the Illinois Supreme Court in this case, and by decisions of other courts. One frequently cited decision, <em>Stanley </em>v. <em>State, supra, </em>at 530, <span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/#861" aria-description="Citation for case: Stanley v. State">313 A. 2d, at 861</a></span> (footnote omitted), remarks that “the dual requirements represented by the ‘two-pronged test’ are ‘analytically severable’ and an ‘overkill’ on one prong will not carry over to make up for a deficit on the other prong.” See also n. 9, <em>infra.</em></p>
</footnote>
<footnote label="6">
<p id="b274-9"> Our original phrasing of the so-called “two-pronged test” in <em>Aguilar </em>v. <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Texas, supra,</a></span> </em>suggests that the two prongs were intended simply as guides to a magistrate’s determination of probable cause, not as inflexible, independent requirements applicable in every case. In <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>, </em>we required only that</p>
<blockquote id="b274-10">“the magistrate must be informed of <em>some of the underlying circumstances </em>from which the informant concluded that . . . narcotics were where he claimed they were, and <em>some of the underlying circumstances </em>from which <page-number citation-index="1" label="231">*231</page-number>the officer concluded that the informant. . . was ‘credible’ or his information ‘reliable.’” <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#114" aria-description="Citation for case: Aguilar v. Texas"><em>Id., </em>at 114</a></span> (emphasis added).</blockquote>
<p id="b275-7">As our language indicates, we intended neither a rigid compartmentalization of the inquiries into an informant’s “veracity,” “reliability,” and “basis of knowledge,” nor that these inquiries be elaborate exegeses of an informant’s tip. Rather, we required only that some facts bearing on two particular issues be provided to the magistrate. Our decision in <em>Jaben </em>v. <em>United States, </em><span class="citation" data-id="9423037"><a href="/opinion/107058/jaben-v-united-states/" aria-description="Citation for case: Jaben v. United States">381 U. S. 214</a></span> (1965), demonstrated this latter point. We held there that a criminal complaint showed probable cause to believe the defendant had attempted to evade the payment of income taxes. We commented:</p>
<blockquote id="b275-8">“Obviously any reliance upon factual allegations necessarily entails some degree of reliability upon the credibility of the source.... Nor does it indicate that each factual allegation which the affiant puts forth must be independently documented, or that each and every fact which contributed to his conclusions be spelled out in the complaint. <em>. . . It simply requires that enough information be presented to the Commissioner to enable him to make the judgment that the charges are not capricious and are sufficiently supported to justify bringing into play the further steps of the criminal process.” Id., </em>at 224-225 (emphasis added).</blockquote>
</footnote>
<footnote label="7">
<p id="b276-6"> The diversity of informants’ tips, as well as the usefulness of the totality-of-the-circumstances approach to probable cause, is reflected in our prior decisions on the subject. In <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#271" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 271</a></span> (1960), we held that probable cause to search petitioners’ apartment was established by an affidavit based principally on an informant’s tip. The unnamed informant claimed to have purchased narcotics from petitioners at their apartment; the affiant stated that he had been given correct information from the informant on a prior occasion. This, and the fact that petitioners had admitted to police officers on another occasion that they were narcotics users, sufficed to support the magistrate’s determination of probable cause.</p>
<p id="b276-7">Likewise, in <em>Rugendorf v. United States, </em><span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">376 U. S. 528</a></span> (1964), the Court upheld a magistrate’s determination that there was probable cause to believe that certain stolen property would be found in petitioner’s apartment. The affidavit submitted to the magistrate stated that certain furs had been stolen, and that a confidential informant, who previously had furnished confidential information, said that he saw the furs in petitioner’s home. Moreover, another confidential informant, also claimed to be reliable, stated that one Schweihs had stolen the furs. Police reports indicated that petitioner had been seen in Schweihs’ company, and a third informant stated that petitioner was a fence for Schweihs.</p>
<p id="b276-8">Finally, in <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963), we held that information within the knowledge of officers who searched the Kers’ apartment provided them with probable cause to believe drugs would be found there. The officers were aware that one Murphy had previously sold marihuana <page-number citation-index="1" label="233">*233</page-number>to a police officer; the transaction had occurred in an isolated area, to which Murphy had led the police. The night after this transaction, police observed Mr. Ker and Murphy meet in the same location. Murphy approached Ker’s car, and, although police could see nothing change hands, Murphy’s <em>modus operandi </em>was identical to what it had been the night before. Moreover, when police followed Ker from the scene of the meeting with Murphy he managed to lose them after performing an abrupt U-turn. Finally, the police had a statement from an informant who had provided reliable information previously, that Ker was engaged in selling marihuana, and that his source was Murphy. We concluded that “[t]o say that this coincidence of information was sufficient to support a reasonable belief of the officers that Ker was illegally in possession of marijuana is to indulge in understatement.” <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#36" aria-description="Citation for case: Ker v. California"><em>Id., </em>at 36</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b277-7"> Compare <em>Stanley </em>v. <em>State, </em><span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/#530" aria-description="Citation for case: Stanley v. State">19 Md. App., at 530</a></span>, <span class="citation" data-id="2333704"><a href="/opinion/2333704/stanley-v-state/#861" aria-description="Citation for case: Stanley v. State">313 A. 2d, at 861</a></span>, reasoning that “[e]ven assuming ‘credibility’ amounting to sainthood, the judge still may not accept the bare conclusion ... of a sworn and known and trusted police-affiant.”</p>
</footnote>
<footnote label="9">
<p id="b278-5"> Some lower court decisions, brought to our attention by the State, reflect a rigid application of such rules. In <em>Bridger </em>v. <em>State, </em><span class="citation" data-id="2433225"><a href="/opinion/2433225/bridger-v-state/" aria-description="Citation for case: Bridger v. State">503 S. W. 2d 801</a></span> (Tex. Crim. App. 1974), .the affiant had received a confession of armed robbery from one of two suspects in the robbery; in addition, the suspect had given the officer $800 in cash stolen during the robbery. The suspect also told the officer that the gun used in the robbery was hidden in the other suspect’s apartment. A warrant issued on the basis of this was invalidated on the ground that the affidavit did not satisfactorily describe how the accomplice had obtained his information regarding the gun.</p>
<p id="b278-6">Likewise, in <em>People </em>v. <em>Palanza, </em><span class="citation" data-id="2023247"><a href="/opinion/2023247/people-v-palanza/" aria-description="Citation for case: People v. Palanza">55 Ill. App. 3d 1028</a></span>, <span class="citation" data-id="2023247"><a href="/opinion/2023247/people-v-palanza/" aria-description="Citation for case: People v. Palanza">371 N. E. 2d 687</a></span> (1978), the affidavit submitted in support of an application for a search warrant stated that an informant of proven and uncontested reliability had seen, in specifically described premises, “a quantity of a white crystalline substance which was represented to the informant by a white male occupant of the premises to be cocaine. Informant has observed cocaine on numerous occasions in the past and is thoroughly familiar with its appearance. The informant states that the white crystalline powder he observed in the above described premises appeared to him to be cocaine.” <span class="citation" data-id="2023247"><a href="/opinion/2023247/people-v-palanza/#1029" aria-description="Citation for case: People v. Palanza"><em>Id., </em>at 1029</a></span>, 371N. E. 2d, at 688. The warrant issued on the basis of the affidavit was invalidated because “[t]here is no indication as to how the informant or for that matter any other person could tell whether a white substance was cocaine and not some other substance such as sugar or salt.” <span class="citation" data-id="2023247"><a href="/opinion/2023247/people-v-palanza/#1030" aria-description="Citation for case: People v. Palanza"><em>Id., </em>at 1030</a></span>, <span class="citation" data-id="2023247"><a href="/opinion/2023247/people-v-palanza/#689" aria-description="Citation for case: People v. Palanza">371 N. E. 2d, at 689</a></span>.</p>
<p id="b278-7">Finally, in <em>People </em>v. <em>Brethauer, </em><span class="citation" data-id="9532437"><a href="/opinion/1123854/people-v-brethauer/" aria-description="Citation for case: People v. Brethauer">174 Colo. 29</a></span>, <span class="citation" data-id="9532437"><a href="/opinion/1123854/people-v-brethauer/" aria-description="Citation for case: People v. Brethauer">482 P. 2d 369</a></span> (1971), an informant, stated to have supplied reliable information in the past, claimed that L. S. D. and marihuana were located on certain premises. The informant supplied police with drugs, which were tested by police and confirmed to be illegal substances. The affidavit setting forth these, and other, facts was found defective under both prongs of <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>.</em></p>
</footnote>
<footnote label="10">
<p id="b281-6"> We also have said that “[a]lthough in a particular case it may not be easy to determine when an affidavit demonstrates the existence of probable cause, the resolution of doubtful or marginal cases in this area should be largely determined by the preference to be accorded to warrants,” <em>United States </em>v. <em>Ventresca, </em><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#109" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 109</a></span> (1965). This reflects both a desire to encourage use of the warrant process by police officers and a recognition that once a warrant has been obtained, intrusion upon interests protected by the Fourth Amendment is less severe than otherwise may be the case. Even if we were to accept the premise that the accurate assessment of probable cause would be furthered by the “two-pronged test,” which we do not, these Fourth Amendment policies would require a less rigorous standard than that which appears to have been read into <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span> </em>and <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>.</em></p>
</footnote>
<footnote label="11">
<p id="b282-6"> The Court’s decision in <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>has been the subject of considerable criticism, both by Members of this Court and others. Justice Blackmun, concurring in <em>United States </em>v. <em>Harris, </em><span class="citation" data-id="9883118"><a href="/opinion/108379/united-states-v-harris/#585" aria-description="Citation for case: United States v. Harris">403 U. S. 573, 585-586</a></span> (1971), noted his long-held view “that <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> . . </em>. was wrongly decided” by this Court. Justice Black similarly would have overruled that decision. <em>Id., </em>at 585. Likewise, a noted commentator has observed that “[t]he <em>Aguilar-Spinelli </em>formulation has provoked apparently ceaseless litigation.” 8A J. Moore, Moore’s Federal Practice ¶ 41.04, p. 41-43 (1982).</p>
<p id="b282-7">Whether the allegations submitted to the magistrate in <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span> </em>would, under the view we now take, have supported a finding of probable cause, we think it would not be profitable to decide. There are so many variables in the probable-cause equation that one determination will seldom be a useful “precedent” for another. Suffice it to say that while we in no way abandon Spinelli’s concern for the trustworthiness of informers and for the principle that it is the magistrate who must ultimately make a finding of probable cause, we reject the rigid categorization suggested by some of its language.</p>
</footnote>
<footnote label="12">
<p id="b286-7"> The tip in <em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span> </em>might well not have survived the rigid application of the “two-pronged test” that developed following <em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>. </em>The only reference to Hereford’s reliability was that he had “been engaged as a ‘special employee’ of the Bureau of Narcotics at Denver for about six months, and from time to time gave information to [the police for] small sums of money, and that [the officer] had always found the information given by Hereford to be accurate and reliable.” <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#309" aria-description="Citation for case: Draper v. United States">358 U. S., at 309</a></span>. Likewise, the tip gave no indication of how Hereford came by his information. At most, the detailed and accurate predictions in the tip indicated that, however Hereford obtained his information, it was reliable.</p>
</footnote>
<footnote label="13">
<p id="b287-7"> The Illinois Supreme Court thought that the verification of details contained in the anonymous letter in this case amounted only to “[t]he corroboration of innocent activity,” <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#390" aria-description="Citation for case: People of Illinois v. Gates">85 Ill. 2d 376, 390</a></span>, <span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#893" aria-description="Citation for case: People of Illinois v. Gates">423 N. E. 2d 887, 893</a></span> (1981), and that this was insufficient to support a finding of probable cause. We are inclined to agree, however, with the observation of Justice Moran in his dissenting opinion that “[i]n this case, just as in <em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span>, </em>seemingly innocent activity became suspicious in light of the initial tip.” <em>Id.., </em>at 396, <page-number citation-index="1" label="244">*244</page-number><span class="citation" data-id="9716974"><a href="/opinion/2100482/people-of-illinois-v-gates/#896" aria-description="Citation for case: People of Illinois v. Gates">423 N. E. 2d, at 896</a></span>. And it bears noting that <em>all </em>of the corroborating detail established in <em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span> </em>was of entirely innocent activity — a fact later pointed out by the Court in both <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#269" aria-description="Citation for case: Jones v. United States">362 U. S., at 269-270</a></span>, and <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#36" aria-description="Citation for case: Ker v. California">374 U. S., at 36</a></span>.</p>
<p id="b288-6">This is perfectly reasonable. As discussed previously, probable cause requires only a probability or substantial chance of criminal activity, not an actual showing of such activity. By hypothesis, therefore, innocent behavior frequently will provide the basis for a showing of probable cause; to require otherwise would be to <em>sub silentio </em>impose a drastically more rigorous definition of probable cause than the security of our citizens’ demands. We think the Illinois court attempted a too rigid classification of the types of conduct that may be relied upon in seeking to demonstrate probable cause. See <em>Brown </em>v. <em>Texas, </em><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#52" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 52, n. 2</a></span> (1979). In making a determination of probable cause the relevant inquiry is not whether particular conduct is “innocent” or “guilty,” but the degree of suspicion that attaches to particular types of noncriminal acts.</p>
</footnote>
<footnote label="14">
<p id="b289-6"> Justice Stevens’ dissent seizes on one inaccuracy in the anonymous informant’s letter — its statement that Sue Gates would fly from Florida to Illinois, when in fact she drove — and argues that the probative value of the entire tip was undermined by this allegedly “material mistake.” We have never required that informants used by the police be infallible, and can see no reason to impose such a requirement in this case. Probable cause, particularly when police have obtained a warrant, simply does not require the perfection the dissent finds necessary.</p>
<p id="b289-7">Likewise, there is no force to the dissent’s argument that the Gateses’ action in leaving their home unguarded undercut the informant’s claim that drugs were hidden there. Indeed, the line-by-line scrutiny that the dissent applies to the anonymous letter is akin to that which we find inappropriate in reviewing magistrates’ decisions. The dissent apparently attributes to the judge who issued the warrant in this case the rather implausible notion that persons dealing in drugs always stay at home, apparently out of fear that to leave might risk intrusion by criminals. If accurate, one could not help sympathizing with the self-imposed isolation of people so situated. In reality, however, it is scarcely likely that the judge ever thought that the anonymous tip “kept one spouse” at home, much less that he relied on the theory advanced by the dissent. The letter simply says that Sue would fly from Florida to Illinois, without indicating whether the Gateses made the bitter choice of leaving the drugs in their house, or those in their car, unguarded. The judge’s determination that there might be drugs or evidence of criminal activity in the Gateses’ home was well supported by the less speculative theory, noted in text, that if the informant <page-number citation-index="1" label="246">*246</page-number>could predict with considerable accuracy the somewhat unusual travel plans of the Gateses, he probably also had a reliable basis for his statements that the Gateses kept a large quantity of drugs in their home and frequently were visited by other drug traffickers there.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Illinois v. Krull.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Illinois v. Krull"
type: case
citation: "480 U.S. 340 (1987)"
parallel_cite: "107 S. Ct. 1160; 94 L. Ed. 2d 364; 55 U.S.L.W. 4291"
neutral_cite: 1987 U.S. LEXIS 1061
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-03-09
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-03-09
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Illinois v. Krull
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111835/illinois-v-krull/"
  cluster_id: 111835
  opinion_id: 111835
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Leon]]", "[[Massachusetts v. Sheppard]]", "[[Arizona v. Evans]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "good-faith", "statute"]
holding: "Good-faith reliance on a STATUTE later held unconstitutional does not trigger exclusion; excluding such evidence would have no deterrent…"
lake:
  record_id: Illinois v. Krull
  status: verified
  projected_at: 2026-07-06
---

# Illinois v. Krull

*480 U.S. 340 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A state agent conducted a warrantless inspection of Krull's wrecking yard, examining records under an Illinois statute that authorized warrantless inspection of licensed auto-parts dealers. The inspection turned up stolen vehicles. The day after the search, a federal court held the statutory inspection scheme unconstitutional because it vested officers with too much discretion. Krull moved to suppress the evidence found in reliance on the statute.

## Issue
Whether the [[The Good-Faith Exception|good-faith exception]] to the exclusionary rule applies to evidence obtained by an officer who acted in objectively reasonable reliance on a statute later held to be unconstitutional.

## Rule
Yes. The Court extended the [[The Good-Faith Exception|good-faith exception]] of *[[United States v. Leon|Leon]]* to reasonable reliance on a statute: "The application of the exclusionary rule to suppress evidence obtained by an officer acting in objectively reasonable reliance on a statute would have as little deterrent effect on the officer's actions as would the exclusion of evidence when an officer acts in objectively reasonable reliance on a warrant." — 480 U.S. at 349. ^pin-349

"Unless a statute is clearly unconstitutional, an officer cannot be expected to question the judgment of the legislature that passed the law." — *Id.* at 349–350. ^pin-349a

## Application
The agent inspected Krull's records in reliance on an Illinois statute that was presumptively valid and not clearly unconstitutional when he acted; the statute was struck down only the next day. Because suppressing evidence gathered in objectively reasonable reliance on the then-valid statute would not meaningfully deter police misconduct, the [[The Good-Faith Exception|good-faith exception]] applied and the evidence was admissible.

## Conclusion
The evidence was admissible under the [[The Good-Faith Exception|good-faith exception]]; the suppression was reversed. Reasonable reliance on a not-yet-invalidated statute does not trigger exclusion.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Krull* extends the [[The Good-Faith Exception|good-faith exception]] of [[United States v. Leon]] and [[Massachusetts v. Sheppard]] from reasonable reliance on a warrant to reasonable reliance on a statute later declared unconstitutional.

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *Illinois v. Krull*, 480 U.S. 340 (1987) — https://www.courtlistener.com/opinion/111835/illinois-v-krull/ — pinpoints: 349, 350.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3ccd753f69e1167b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Illinois v. Krull"}, "payload": {"all": [{"cite": "480 U.S. 340", "page": "340", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "480"}, {"cite": "107 S. Ct. 1160", "page": "1160", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "107"}, {"cite": "94 L. Ed. 2d 364", "page": "364", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "94"}, {"cite": "1987 U.S. LEXIS 1061", "page": "1061", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1987"}, {"cite": "55 U.S.L.W. 4291", "page": "4291", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "55"}], "display": "480 U.S. 340", "official": {"cite": "480 U.S. 340", "page": "340", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "480"}, "official_selection_present": true, "record_id": "Illinois v. Krull"}}
{"assertion_id": "4efdfa0cef624b2c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-349", "record_id": "Illinois v. Krull"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-349", "pinpoint_status": "slip-only", "quote": "--- # Illinois v. Krull *480 U.S. 340 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A state agent conducted a warrantless inspection of Krull's wrecking yard, examining records under an Illinois statute that authorized warrantless inspection of licensed auto-parts dealers. The inspection turned up stolen vehicles. The day after the search, a federal court held the statutory inspection scheme unconstitutional because it vested officers with too much discretion. Krull moved to suppress the evidence found in reliance on the statute. ## Issue Whether the good-faith exception to the exclusionary rule applies to evidence obtained by an officer who acted in objectively reasonable reliance on a statute later held to be unconstitutional. ## Rule Yes. The Court extended the good-faith exception of *Leon* to reasonable reliance on a statute:", "quote_fidelity": "mismatch", "record_id": "Illinois v. Krull", "star_marker": null}}
{"assertion_id": "fa8a6f3cb7b8b15b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-349a", "record_id": "Illinois v. Krull"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-349a", "pinpoint_status": "slip-only", "quote": "Unless a statute is clearly unconstitutional, an officer cannot be expected to question the judgment of the legislature that passed the law.", "quote_fidelity": "mismatch", "record_id": "Illinois v. Krull", "star_marker": null}}
{"assertion_id": "56621b27e529155b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Illinois v. Krull"}, "payload": {"as_of_content": "1987-03-09", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Illinois v. Krull", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Illinois v. Krull

```json
{
  "schema_version": "s2.v1",
  "record_id": "Illinois v. Krull",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Illinois v. Krull",
    "case_name_short": "Krull",
    "case_name_full": "ILLINOIS v. KRULL Et Al.",
    "input_case_name": "Illinois v. Krull",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-03-09",
    "year": 1987,
    "docket": null,
    "cluster_id": 111835,
    "lead_opinion_id": 111835,
    "sibling_ids": [
      111835,
      9430871,
      9430872,
      9430873
    ],
    "absolute_url": "/opinion/111835/illinois-v-krull/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "480 U.S. 340",
      "volume": "480",
      "reporter": "U.S.",
      "page": "340",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 1160",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1160",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 L. Ed. 2d 364",
        "volume": "94",
        "reporter": "L. Ed. 2d",
        "page": "364",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4291",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4291",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 1061",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "1061",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "480 U.S. 340",
        "volume": "480",
        "reporter": "U.S.",
        "page": "340",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 1160",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1160",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 L. Ed. 2d 364",
        "volume": "94",
        "reporter": "L. Ed. 2d",
        "page": "364",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 1061",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "1061",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4291",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4291",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "480 U.S. 340",
    "official_selection": {
      "court_class": "scotus",
      "selected": "480 U.S. 340",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-349",
      "page": null,
      "quote": "--- # Illinois v. Krull *480 U.S. 340 (1987)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A state agent conducted a warrantless inspection of Krull's wrecking yard, examining records under an Illinois statute that authorized warrantless inspection of licensed auto-parts dealers. The inspection turned up stolen vehicles. The day after the search, a federal court held the statutory inspection scheme unconstitutional because it vested officers with too much discretion. Krull moved to suppress the evidence found in reliance on the statute. ## Issue Whether the good-faith exception to the exclusionary rule applies to evidence obtained by an officer who acted in objectively reasonable reliance on a statute later held to be unconstitutional. ## Rule Yes. The Court extended the good-faith exception of *Leon* to reasonable reliance on a statute:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-349a",
      "page": null,
      "quote": "Unless a statute is clearly unconstitutional, an officer cannot be expected to question the judgment of the legislature that passed the law.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-03-09",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Illinois v. Krull",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
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
        "journal_ref": "Illinois v. Krull:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Raenard Romalle Douglas",
          "cluster_id": 10129058,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kruse",
          "cluster_id": 4643214,
          "cite": [
            "303 Neb. 799",
            "931 N.W.2d 148"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Fredericq",
          "cluster_id": 4613398,
          "cite": [
            "121 N.E.3d 166",
            "482 Mass. 70"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Johnny Vasquez-Algarin",
          "cluster_id": 3199633,
          "cite": [
            "821 F.3d 467",
            "2016 U.S. App. LEXIS 7889",
            "2016 WL 1730540"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Arredondo",
          "cluster_id": 6238731,
          "cite": [
            "199 Cal. Rptr. 3d 563",
            "245 Cal. App. 4th 186",
            "2016 Cal. App. LEXIS 153"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane1_negative"
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
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
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
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vernonia School District 47J v. Acton",
          "cluster_id": 117964,
          "cite": [
            "132 L. Ed. 2d 564",
            "115 S. Ct. 2386",
            "515 U.S. 646",
            "1995 U.S. LEXIS 4275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Burger",
          "cluster_id": 111927,
          "cite": [
            "96 L. Ed. 2d 601",
            "107 S. Ct. 2636",
            "482 U.S. 691",
            "1987 U.S. LEXIS 2725",
            "55 U.S.L.W. 4890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
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
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edwards v. Aguillard",
          "cluster_id": 111924,
          "cite": [
            "96 L. Ed. 2d 510",
            "107 S. Ct. 2573",
            "482 U.S. 578",
            "1987 U.S. LEXIS 2729",
            "55 U.S.L.W. 4860"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
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
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heien v. North Carolina",
          "cluster_id": 2760668,
          "cite": [
            "190 L. Ed. 2d 475",
            "135 S. Ct. 530",
            "2014 U.S. LEXIS 8306",
            "83 U.S.L.W. 4021",
            "25 Fla. L. Weekly Fed. S 20"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania Bd. of Probation and Parole v. Scott",
          "cluster_id": 118235,
          "cite": [
            "141 L. Ed. 2d 344",
            "118 S. Ct. 2014",
            "524 U.S. 357",
            "1998 U.S. LEXIS 4037"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Johnson",
          "cluster_id": 4889243,
          "cite": [
            "2021 CO 35"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Warshak",
          "cluster_id": 181032,
          "cite": [
            "631 F.3d 266",
            "2010 U.S. App. LEXIS 25415",
            "2010 WL 5071766"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Caballes",
          "cluster_id": 2192166,
          "cite": [
            "851 N.E.2d 26",
            "221 Ill. 2d 282",
            "303 Ill. Dec. 128",
            "2006 Ill. LEXIS 625"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of L. A. v. Patel",
          "cluster_id": 2811846,
          "cite": [
            "576 U.S. 409",
            "135 S. Ct. 2443",
            "192 L. Ed. 2d 435",
            "2015 U.S. LEXIS 4065",
            "83 U.S.L.W. 4520",
            "25 Fla. L. Weekly Fed. S 412"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Brown",
          "cluster_id": 4582900,
          "cite": [
            "302 Neb. 53",
            "921 N.W.2d 804"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. McCane",
          "cluster_id": 172450,
          "cite": [
            "573 F.3d 1037",
            "2009 U.S. App. LEXIS 16557",
            "2009 WL 2231658"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matthew Alexander v. Verizon Wireless Services, LL",
          "cluster_id": 4442643,
          "cite": [
            "875 F.3d 243"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
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
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jeffrey Meek",
          "cluster_id": 786002,
          "cite": [
            "366 F.3d 705",
            "2004 U.S. App. LEXIS 7470",
            "2004 WL 829899"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
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
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Tyrell J.",
          "cluster_id": 1258965,
          "cite": [
            "876 P.2d 519",
            "8 Cal. 4th 68",
            "32 Cal. Rptr. 2d 33",
            "94 Cal. Daily Op. Serv. 5846",
            "94 Daily Journal DAR 10633",
            "1994 Cal. LEXIS 3897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Earle v. Robert Benoit",
          "cluster_id": 508419,
          "cite": [
            "850 F.2d 836",
            "1988 U.S. App. LEXIS 9166",
            "1988 WL 67108"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robles",
          "cluster_id": 5607956,
          "cite": [
            "23 Cal. 4th 789",
            "3 P.3d 311",
            "2000 Daily Journal DAR 7789",
            "97 Cal. Rptr. 2d 914",
            "2000 Cal. Daily Op. Serv. 5894",
            "2000 Cal. LEXIS 5217"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
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
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Albert White",
          "cluster_id": 4438318,
          "cite": [
            "874 F.3d 490",
            "2017 FED App. 0242P",
            "2017 WL 4848911",
            "2017 U.S. App. LEXIS 21332"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warshak v. United States",
          "cluster_id": 1425282,
          "cite": [
            "532 F.3d 521",
            "2008 U.S. App. LEXIS 14717",
            "2008 WL 2698177"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Krull:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111835 OR 9430871 OR 9430872 OR 9430873) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDQ2NjgxNjAwMDAwJnM9MzE1MjI1NyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111835+OR+9430871+OR+9430872+OR+9430873%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111835 OR 9430871 OR 9430872 OR 9430873)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzImcz0yODEwNTI0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111835+OR+9430871+OR+9430872+OR+9430873%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111835 OR 9430871 OR 9430872 OR 9430873)",
        "reviewed": 33,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 33,
        "triage_read": 2,
        "triage_snippet_classified": 31
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111835 OR 9430871 OR 9430872 OR 9430873)",
    "indexed_citing_opinions": 656,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111835,
        "count": 549,
        "count_source": "search"
      },
      {
        "opinion_id": 9430871,
        "count": 123,
        "count_source": "search"
      },
      {
        "opinion_id": 9430872,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430873,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1170,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/illinois-v-krull.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2OTUyMDImcz05NDgwNzc4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111835+OR+9430871+OR+9430872+OR+9430873%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111835,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 107917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 109302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 109932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 110100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 110127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 110530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 111241,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 111263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 111785,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 391263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 427553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 438820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 2102923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 2108094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 2123138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 2128773,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 2499246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111835,
        "cited_id": 2620876,
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
    "date_created": "2026-07-05T07:59:14Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:59:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:59:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T08:03:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:59:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Illinois v. Krull

```
<div>
<center><b><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">480 U.S. 340</a></span> (1987)</b></center>
<center><h1>ILLINOIS<br>
v.<br>
KRULL ET AL.</h1></center>
<center>No. 85-608.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 5, 1986</center>
<center>Decided March 9, 1987</center>
CERTIORARI TO THE SUPREME COURT OF ILLINOIS
<p><span class="star-pagination">*341</span> <i>Michael J. Angarola</i> argued the cause for petitioner. On the brief were <i>Neil F. Hartigan,</i> Attorney General of Illinois, <span class="star-pagination">*342</span> <i>Roma J. Stewart,</i> Solicitor General, and <i>Mark L. Rotert,</i> Assistant Attorney General.</p>
<p><i>Paul J. Larkin, Jr.,</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. On the brief were <i>Solicitor General Fried, Assistant Attorney General Trott, Deputy Solicitor General Bryson, Andrew J. Pincus,</i> and <i>Robert J. Erickson.</i></p>
<p><i>Miriam F. Miquelon</i> argued the cause for respondents. With her on the brief was <i>Louis B. Garippo.</i><sup>[*]</sup></p>
<p>JUSTICE BLACKMUN delivered the opinion of the Court.</p>
<p>In <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U. S. 897</a></span> (1984), this Court ruled that the Fourth Amendment exclusionary rule does not apply to evidence obtained by police officers who acted in objectively reasonable reliance upon a search warrant issued by a neutral magistrate, but where the warrant was ultimately found to be unsupported by probable cause. See also <i>Massachusetts</i> v. <i>Sheppard,</i> <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">468 U. S. 981</a></span> (1984). The present case presents the question whether a similar exception to the exclusionary rule should be recognized when officers act in objectively reasonable reliance upon a <i>statute</i> authorizing warrantless administrative searches, but where the statute is ultimately found to violate the Fourth Amendment.</p>
<p></p>
<h2>I</h2>
<p>The State of Illinois, as part of its Vehicle Code, has a comprehensive statutory scheme regulating the sale of motor vehicles and vehicular parts. See Ill. Rev. Stat., ch. 95 1/2, ¶¶ 5-100 to 5-801 (1985). A person who sells motor vehicles, or deals in automotive parts, or processes automotive scrap metal, or engages in a similar business must obtain a license from the Illinois Secretary of State. ¶¶ 5-101, 5-102, 5-301. <span class="star-pagination">*343</span> A licensee is required to maintain a detailed record of all motor vehicles and parts that he purchases or sells, including the identification numbers of such vehicles and parts, and the dates of acquisition and disposition. ¶ 5-401.2. In 1981, the statute in its then form required a licensee to permit state officials to inspect these records "at any reasonable time during the night or day" and to allow "examination of the premises of the licensee's established place of business for the purpose of determining the accuracy of required records." Ill. Rev. Stat., ch. 95 1/2, ¶ 5-401(e) (1981).<sup>[1]</sup></p>
<p>Respondents in 1981 operated Action Iron &amp; Metal, Inc., an automobile wrecking yard located in the city of Chicago. Detective Leilan K. McNally of the Chicago Police Department regularly inspected the records of wrecking yards pursuant to the state statute. Tr. 12.<sup>[2]</sup> On the morning of July 5, 1981, he entered respondents' yard. <i>Id.,</i> at 7. He identified himself as a police officer to respondent Lucas, who was working at the yard, and asked to see the license and records of vehicle purchases. Lucas could not locate the license or records, but he did produce a paper pad on which approximately five vehicle purchases were listed. <i>Id.,</i> at 25-26. McNally then requested and received permission from Lucas to look at the cars in the yard. Upon checking with his mobile computer the serial numbers of several of the vehicles, McNally ascertained that three of them were stolen. Also, the identification number of a fourth had been removed. McNally seized the four vehicles and placed Lucas under arrest. <i>Id.,</i> at 8-9, 16-17. Respondent Krull, the holder of the license, and respondent Mucerino, who was present at the yard the day of the search, were arrested later. Respondents <span class="star-pagination">*344</span> were charged with various criminal violations of the Illinois motor vehicle statutes.</p>
<p>The state trial court (the Circuit Court of Cook County) granted respondents' motion to suppress the evidence seized from the yard. App. 20-21. Respondents had relied on a federal-court ruling, issued the day following the search, that ¶ 5-401(e), authorizing warrantless administrative searches of licensees, was unconstitutional. See <i>Bionic Auto Parts &amp; Sales, Inc.</i> v. <i>Fahner,</i> <span class="citation" data-id="2128773"><a href="/opinion/2128773/bionic-auto-parts-and-sales-inc-v-fahner/" aria-description="Citation for case: Bionic Auto Parts and Sales, Inc. v. Fahner">518 F. Supp. 582</a></span> (ND Ill. 1981), aff'd in part, vacated in part, and remanded in part, <span class="citation" data-id="427553"><a href="/opinion/427553/bionic-auto-parts-and-sales-inc-v-tyrone-c-fahner/" aria-description="Citation for case: Bionic Auto Parts and Sales, Inc. v. Tyrone C. Fahner">721 F. 2d 1072</a></span> (CA7 1983). The Federal District Court in that case had concluded that the statute permitted officers unbridled discretion in their searches and was therefore not " `a constitutionally adequate substitute for a warrant.' " <span class="citation" data-id="2128773"><a href="/opinion/2128773/bionic-auto-parts-and-sales-inc-v-fahner/#585" aria-description="Citation for case: Bionic Auto Parts and Sales, Inc. v. Fahner">518 F. Supp., at 585-586</a></span>, quoting <i>Donovan</i> v. <i>Dewey,</i> <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#603" aria-description="Citation for case: Donovan v. Dewey">452 U. S. 594, 603</a></span> (1981). The state trial court in the instant case agreed that the statute was invalid and concluded that its unconstitutionality "affects all pending prosecutions not completed." App. 20. On that basis, the trial court granted respondents' motion to suppress the evidence. <i>Id.,</i> at 20-21.<sup>[3]</sup></p>
<p>The Appellate Court of Illinois, First Judicial District, vacated the trial court's ruling and remanded the case for further proceedings. <i>Id.,</i> at 22. It observed that recent developments in the law indicated that Detective McNally's good-faith reliance on the state statute might be relevant in assessing the admissibility of evidence, but that the trial court should first make a factual determination regarding McNally's good faith. <i>Id.,</i> at 25. It also observed that the trial court might wish to reconsider its holding regarding the unconstitutionality of the statute in light of the decision by the United States Court of Appeals for the Seventh Circuit upholding the amended form of the Illinois statute. See <i>Bionic Auto Parts &amp; Sales, Inc.</i> v. <i>Fahner,</i> 721 F. 2d 1072 <span class="star-pagination">*345</span> (CA7 1983).<sup>[4]</sup> On remand, however, the state trial court adhered to its decision to grant respondents' motion to suppress. It stated that the relevant statute was the one in effect at the time McNally searched respondents' yard, and that this statute was unconstitutional for the reasons stated by the Federal District Court in <i>Bionic.</i> It further concluded that because the good faith of an officer is relevant, if at all, only when he acts pursuant to a warrant, Detective McNally's possible good-faith reliance upon the statute had no bearing on the case. App. 32-35.<sup>[5]</sup></p>
<p>The Supreme Court of Illinois affirmed.<sup>[6]</sup> <span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/" aria-description="Citation for case: People v. Krull">107 Ill. 2d 107</a></span>, <span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/" aria-description="Citation for case: People v. Krull">481 N. E. 2d 703</a></span> (1985). It first ruled that the state statute, as it existed at the time McNally searched respondents' yard, was unconstitutional. It noted that statutes authorizing warrantless administrative searches in heavily regulated industries had been upheld where such searches were necessary to promote enforcement of a substantial state interest, and where the statute " `in terms of [the] certainty and regularity of its application, provide[d] a constitutionally adequate substitute for a warrant.' " <span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/#116" aria-description="Citation for case: People v. Krull"><i>Id.,</i> at 116</a></span>, <span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/#707" aria-description="Citation for case: People v. Krull">481 N. E. 2d, at 707</a></span>, quoting <i>Donovan</i> v. <i>Dewey,</i> <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#603" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 603</a></span>. Although acknowledging that the statutory scheme authorizing <span class="star-pagination">*346</span> warrantless searches of licensees furthered a strong public interest in preventing the theft of automobiles and the trafficking in stolen automotive parts, the Illinois Supreme Court concluded that the statute violated the Fourth Amendment because it "vested State officials with too much discretion to decide who, when, and how long to search." <span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/#116" aria-description="Citation for case: People v. Krull">107 Ill. 2d, at 116</a></span>, <span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/#707" aria-description="Citation for case: People v. Krull">481 N. E. 2d, at 707</a></span>.</p>
<p>The court rejected the State's argument that the evidence seized from respondents' wrecking yard should nevertheless be admitted because the police officer had acted in good-faith reliance on the statute authorizing such searches. The court observed that in <i>Michigan</i> v. <i>DeFillippo,</i> <span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">443 U. S. 31</a></span> (1979), this Court had upheld an arrest and search made pursuant to an ordinance defining a criminal offense, where the ordinance was subsequently held to violate the Fourth Amendment. The Illinois court noted that this Court in <i><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">DeFillippo</a></span></i> had contrasted the ordinance then before it, defining a substantive criminal offense, with a procedural statute directly authorizing searches without a warrant or probable cause, and had stated that evidence obtained in searches conducted pursuant to the latter type of statute traditionally had not been admitted. <span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/#118" aria-description="Citation for case: People v. Krull">107 Ill. 2d, at 118</a></span>, <span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/#708" aria-description="Citation for case: People v. Krull">481 N. E. 2d, at 708</a></span>. Because the Illinois statute did not define a substantive criminal offense, but, instead, was a procedural statute directly authorizing warrantless searches, the Illinois Supreme Court concluded that good-faith reliance upon that statute could not be used to justify the admission of evidence under an exception to the exclusionary rule. <span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/#118" aria-description="Citation for case: People v. Krull"><i>Id.,</i> at 118-119</a></span>, <span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/#708" aria-description="Citation for case: People v. Krull">481 N. E. 2d, at 708</a></span>.</p>
<p>We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./475/1080/">475 U. S. 1080</a></span> (1986), to consider whether a good-faith exception to the Fourth Amendment exclusionary rule applies when an officer's reliance on the constitutionality of a statute is objectively reasonable, but the statute is subsequently declared unconstitutional.</p>
<p></p>
<h2>
<span class="star-pagination">*347</span> II</h2>
<p></p>
<h2>A</h2>
<p>When evidence is obtained in violation of the Fourth Amendment, the judicially developed exclusionary rule usually precludes its use in a criminal proceeding against the victim of the illegal search and seizure. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914); <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961). The Court has stressed that the "prime purpose" of the exclusionary rule "is to deter future unlawful police conduct and thereby effectuate the guarantee of the Fourth Amendment against unreasonable searches and seizures." <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#347" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 347</a></span> (1974). Application of the exclusionary rule "is neither intended nor able to `cure the invasion of the defendant's rights which he has already suffered.' " <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon">468 U. S., at 906</a></span>, quoting <i>Stone</i> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#540" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 540</a></span> (1976) (WHITE, J., dissenting). Rather, the rule "operates as `a judicially created remedy designed to safeguard Fourth Amendment rights generally through its deterrent effect, rather than a personal constitutional right of the party aggrieved.' " 468 U. S., at 906, quoting <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S., at 348</a></span>.</p>
<p>As with any remedial device, application of the exclusionary rule properly has been restricted to those situations in which its remedial purpose is effectively advanced. Thus, in various circumstances, the Court has examined whether the rule's deterrent effect will be achieved, and has weighed the likelihood of such deterrence against the costs of withholding reliable information from the truth-seeking process. See, <i>e. g., </i><i>United States</i> v. <i>Janis,</i> <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#454" aria-description="Citation for case: United States v. Janis">428 U. S. 433, 454</a></span> (1976) (evidence obtained by state officers in violation of Fourth Amendment may be used in federal civil proceeding because likelihood of deterring conduct of state officers does not outweigh societal costs imposed by exclusion); <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#351" aria-description="Citation for case: United States v. Calandra">414 U. S., at 351-352</a></span> (evidence obtained in contravention of Fourth Amendment may be used in grand jury proceedings because minimal advance in deterrence of police <span class="star-pagination">*348</span> misconduct is outweighed by expense of impeding role of grand jury).</p>
<p>In <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>,</i> the Court held that the exclusionary rule should not be applied to evidence obtained by a police officer whose reliance on a search warrant issued by a neutral magistrate was objectively reasonable, even though the warrant was ultimately found to be defective. On the basis of three factors, the Court concluded that there was no sound reason to apply the exclusionary rule as a means of deterring misconduct on the part of judicial officers who are responsible for issuing warrants. First, the exclusionary rule was historically designed "to deter police misconduct rather than to punish the errors of judges and magistrates." 468 U. S., at 916. Second, there was "no evidence suggesting that judges and magistrates are inclined to ignore or subvert the Fourth Amendment or that lawlessness among these actors requires application of the extreme sanction of exclusion." <i>Ibid.</i> Third, and of greatest importance to the Court, there was no basis "for believing that exclusion of evidence seized pursuant to a warrant will have a significant deterrent effect on the issuing judge or magistrate." <i>Ibid.</i> The Court explained: "Judges and magistrates are not adjuncts to the law enforcement team; as neutral judicial officers, they have no stake in the outcome of particular criminal prosecutions." <i>Id.,</i> at 917. Thus, the threat of exclusion of evidence could not be expected to deter such individuals from improperly issuing warrants, and a judicial ruling that a warrant was defective was sufficient to inform the judicial officer of the error made.</p>
<p>The Court then considered whether application of the exclusionary rule in that context could be expected to alter the behavior of law enforcement officers. In prior cases, the Court had observed that, because the purpose of the exclusionary rule is to deter police officers from violating the Fourth Amendment, evidence should be suppressed "only if it can be said that the law enforcement officer had knowledge, or may properly be charged with knowledge, that the <span class="star-pagination">*349</span> search was unconstitutional under the Fourth Amendment." <i>United States</i> v. <i>Peltier,</i> <span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#542" aria-description="Citation for case: United States v. Peltier">422 U. S. 531, 542</a></span> (1975); see also <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#447" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 447</a></span> (1974). Where the officer's conduct is objectively reasonable, the Court explained in <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>,</i></p>
<blockquote>" `[e]xcluding the evidence will not further the ends of the exclusionary rule in any appreciable way; for it is painfully apparent that . . . the officer is acting as a reasonable officer would and should act in similar circumstances. Excluding the evidence can in no way affect his future conduct unless it is to make him less willing to do his duty.' " <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#920" aria-description="Citation for case: United States v. Leon">468 U. S., at 920</a></span>, quoting <i>Stone</i> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#539" aria-description="Citation for case: Stone v. Powell">428 U. S., at 539-540</a></span> (WHITE, J., dissenting).</blockquote>
<p>The Court in <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i> concluded that a deterrent effect was particularly absent when an officer, acting in objective good faith, obtained a search warrant from a magistrate and acted within its scope. "In most such cases, there is no police illegality and thus nothing to deter," 468 U. S., at 920-921. It is the judicial officer's responsibility to determine whether probable cause exists to issue a warrant, and, in the ordinary case, police officers cannot be expected to question that determination. Because the officer's sole responsibility after obtaining a warrant is to carry out the search pursuant to it, applying the exclusionary rule in these circumstances could have no deterrent effect on a future Fourth Amendment violation by the officer. <i>Id.,</i> at 921.</p>
<p></p>
<h2>B</h2>
<p>The approach used in <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i> is equally applicable to the present case. The application of the exclusionary rule to suppress evidence obtained by an officer acting in objectively reasonable reliance on a statute would have as little deterrent effect on the officer's actions as would the exclusion of evidence when an officer acts in objectively reasonable reliance on a warrant. Unless a statute is clearly unconstitutional, an <span class="star-pagination">*350</span> officer cannot be expected to question the judgment of the legislature that passed the law. If the statute is subsequently declared unconstitutional, excluding evidence obtained pursuant to it prior to such a judicial declaration will not deter future Fourth Amendment violations by an officer who has simply fulfilled his responsibility to enforce the statute as written. To paraphrase the Court's comment in <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>:</i> "Penalizing the officer for the [legislature's] error, rather than his own, cannot logically contribute to the deterrence of Fourth Amendment violations." <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Ibid.</a></span></i><sup>[7]</sup></p>
<p>Any difference between our holding in <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i> and our holding in the instant case, therefore, must rest on a difference between the effect of the exclusion of evidence on judicial officers and the effect of the exclusion of evidence on legislators. Although these two groups clearly serve different functions in the criminal justice system, those differences are not controlling for purposes of this case. We noted in <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i> as an initial matter that the exclusionary rule was aimed at deterring police misconduct. 468 U. S., at 916. Thus, legislators, like judicial officers, are not the focus of the rule. Moreover, to the extent we consider the rule's effect on legislators, our initial inquiry, as set out in <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>,</i> is whether there is evidence to suggest that legislators "are inclined to ignore or subvert the Fourth Amendment." <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Ibid.</a></span></i> Although legislators are not "neutral judicial officers," as are judges and magistrates, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#917" aria-description="Citation for case: United States v. Leon"><i>id.,</i> at 917</a></span>, neither are they "adjuncts to the <span class="star-pagination">*351</span> law enforcement team." <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Ibid.</a></span></i> The role of legislators in the criminal justice system is to enact laws for the purpose of establishing and perpetuating that system. In order to fulfill this responsibility, legislators' deliberations of necessity are significantly different from the hurried judgment of a law enforcement officer "engaged in the often competitive enterprise of ferreting out crime." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948). Before assuming office, state legislators are required to take an oath to support the Federal Constitution. See U. S. Const., Art. VI, cl. 3. Indeed, by according laws a presumption of constitutional validity, courts presume that legislatures act in a constitutional manner. See <i>e. g., </i><i>McDonald</i> v. <i>Board of Election Comm'rs of Chicago,</i> <span class="citation" data-id="107917"><a href="/opinion/107917/mcdonald-v-board-of-election-commrs-of-chicago/#808" aria-description="Citation for case: McDonald v. Board of Election Comm&#x27;rs of Chicago">394 U. S. 802, 808-809</a></span> (1969); see generally 1 N. Singer, Sutherland on Statutory Construction § 2.01 (4th ed. 1985).</p>
<p>There is no evidence suggesting that Congress or state legislatures have enacted a significant number of statutes permitting warrantless administrative searches violative of the Fourth Amendment. Legislatures generally have confined their efforts to authorizing administrative searches of specific categories of businesses that require regulation, and the resulting statutes usually have been held to be constitutional. See, <i>e. g., </i><i>Donovan</i> v. <i>Dewey,</i> <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">452 U. S. 594</a></span> (1981); <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972); <i>Colonnade Catering Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970); <i>United States</i> v. <i>Jamieson-McKames Pharmaceuticals, Inc.,</i> <span class="citation" data-id="8913471"><a href="/opinion/8924178/united-states-v-jamieson-mckames-pharmaceuticals-inc/" aria-description="Citation for case: United States v. Jamieson-McKames Pharmaceuticals, Inc.">651 F. 2d 532</a></span> (CA8 1981), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./455/1016/">455 U. S. 1016</a></span> (1982); see also 3 W. LaFave, Search and Seizure § 10.2, pp. 132-134, n. 89.1 (Supp. 1986) (collecting cases). Thus, we are given no basis for believing that legislators are inclined to subvert their oaths and the Fourth Amendment and that "lawlessness among these actors requires application of the extreme sanction of exclusion." <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#916" aria-description="Citation for case: United States v. Leon">468 U. S., at 916</a></span>.</p>
<p>Even if we were to conclude that legislators are different in certain relevant respects from magistrates, because legislators are not officers of the judicial system, the next inquiry <span class="star-pagination">*352</span> necessitated by <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i> is whether exclusion of evidence seized pursuant to a statute subsequently declared unconstitutional will "have a significant deterrent effect," <i>ibid.,</i> on legislators enacting such statutes. Respondents have offered us no reason to believe that applying the exclusionary rule will have such an effect. Legislators enact statutes for broad, programmatic purposes, not for the purpose of procuring evidence in particular criminal investigations. Thus, it is logical to assume that the greatest deterrent to the enactment of unconstitutional statutes by a legislature is the power of the courts to invalidate such statutes. Invalidating a statute informs the legislature of its constitutional error, affects the admissibility of all evidence obtained subsequent to the constitutional ruling, and often results in the legislature's enacting a modified and constitutional version of the statute, as happened in this very case. There is nothing to indicate that applying the exclusionary rule to evidence seized pursuant to the statute prior to the declaration of its invalidity will act as a significant, additional deterrent.<sup>[8]</sup> Moreover, to the extent that application of the exclusionary rule could provide some incremental deterrent, that possible benefit must be weighed against the "substantial social costs exacted by the exclusionary <span class="star-pagination">*353</span> rule." <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#907" aria-description="Citation for case: United States v. Leon"><i>Id.,</i> at 907</a></span>.<sup>[9]</sup> When we indulge in such weighing, we are convinced that applying the exclusionary rule in this context is unjustified.</p>
<p>Respondents argue that the result in this case should be different from that in <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i> because a statute authorizing warrantless administrative searches affects an entire industry and a large number of citizens, while the issuance of a defective warrant affects only one person. This distinction is not persuasive. In determining whether to apply the exclusionary rule, a court should examine whether such application will advance the deterrent objective of the rule. Although the number of individuals affected may be considered when "weighing the costs and benefits," <i>ibid.,</i> of applying the exclusionary rule, the simple fact that many are affected by a statute is not sufficient to tip the balance if the deterrence of Fourth Amendment violations would not be advanced in any meaningful way.<sup>[10]</sup></p>
<p>We also do not believe that defendants will choose not to contest the validity of statutes if they are unable to benefit directly by the subsequent exclusion of evidence, thereby resulting in statutes that evade constitutional review. First, in <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>,</i> we explicitly rejected the argument that the goodfaith exception adopted in that case would "preclude review <span class="star-pagination">*354</span> of the constitutionality of the search or seizure" or would cause defendants to lose their incentive to litigate meritorious Fourth Amendment claims. We stated that "the magnitude of the benefit conferred on defendants by a successful [suppression] motion makes it unlikely that litigation of colorable claims will be substantially diminished." <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#924" aria-description="Citation for case: United States v. Leon"><i>Id.,</i> at 924</a></span>, and n. 25. In an effort to suppress evidence, a defendant has no reason not to argue that a police officer's reliance on a warrant or statute was not objectively reasonable and therefore cannot be considered to have been in good faith. Second, unlike a person searched pursuant to a warrant, a person subject to a statute authorizing searches without a warrant or probable cause may bring an action seeking a declaration that the statute is unconstitutional and an injunction barring its implementation. Indeed, that course of action was followed with respect to the statute at issue in this case. Several businesses brought a declaratory judgment suit in Federal District Court challenging ¶ 5-401(e) of the Illinois Vehicle Code (1981), and the provision was declared unconstitutional. See <i>Bionic Auto Parts &amp; Sales, Inc.</i> v. <i>Fahner,</i> <span class="citation" data-id="2128773"><a href="/opinion/2128773/bionic-auto-parts-and-sales-inc-v-fahner/#585" aria-description="Citation for case: Bionic Auto Parts and Sales, Inc. v. Fahner">518 F. Supp., at 585</a></span>. Subsequent to that declaration, respondents, in their state-court criminal trial, challenged the admissibility of evidence obtained pursuant to the statute. App. 13-17.<sup>[11]</sup></p>
<p><span class="star-pagination">*355</span> The Court noted in <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i> that the "good-faith" exception to the exclusionary rule would not apply "where the issuing magistrate wholly abandoned his judicial role in the manner condemned in <i>Lo-Ji Sales, Inc.</i> v. <i>New York,</i> <span class="citation" data-id="110100"><a href="/opinion/110100/lo-ji-sales-inc-v-new-york/" aria-description="Citation for case: Lo-Ji Sales, Inc. v. New York">442 U. S. 319</a></span> (1979)," or where the warrant was so facially deficient "that the executing officers cannot reasonably presume it to be valid." 468 U. S., at 923. Similar constraints apply to the exception to the exclusionary rule we recognize today. A statute cannot support objectively reasonable reliance if, in passing the statute, the legislature wholly abandoned its responsibility to enact constitutional laws. Nor can a law enforcement officer be said to have acted in good-faith reliance upon a statute if its provisions are such that a reasonable officer should have known that the statute was unconstitutional. Cf. <i>Harlow</i> v. <i>Fitzgerald,</i> <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 818</a></span> (1982) ("[G]overnment officials performing discretionary functions, generally are shielded from liability for civil damages insofar as their conduct does not violate clearly established statutory or constitutional rights of which a reasonable person would have known"). As we emphasized in <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>,</i> the standard of reasonableness we adopt is an objective one; the standard does not turn on the subjective good faith of individual officers. See <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#919" aria-description="Citation for case: United States v. Leon">468 U. S., at 919, n. 20</a></span>.<sup>[12]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*356</span> III</h2>
<p>Applying the principle enunciated in this case, we necessarily conclude that Detective McNally's reliance on the <span class="star-pagination">*357</span> Illinois statute was objectively reasonable.<sup>[13]</sup> On several occasions, this Court has upheld legislative schemes that authorized warrantless administrative searches of heavily regulated industries. See <i>Donovan</i> v. <i>Dewey,</i> <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">452 U. S. 594</a></span> (1981) (inspections of underground and surface mines pursuant to Federal Mine Safety and Health Act of 1977); <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972) (inspections of firearms dealers under Gun Control Act of 1968); <i>Colonnade Catering Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970) (inspections of liquor dealers under <span class="citation no-link">26 U. S. C. §§ 5146</span>(b) and 7606 (1964 ed.)). It has recognized that an inspection program may be a necessary component of regulation in certain industries, and has acknowledged that unannounced, warrantless inspections may be necessary "if the law is to be properly enforced and inspection made effective." <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S., at 316</a></span>; <i>Donovan</i> v. <i>Dewey,</i> <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#603" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 603</a></span>. Thus, the Court explained in <i><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">Donovan</a></span></i> that its prior decisions</p>
<blockquote>"make clear that a warrant may not be constitutionally required when Congress has reasonably determined that warrantless searches are necessary to further a regulatory scheme and the federal regulatory presence is sufficiently comprehensive and defined that the owner of commercial property cannot help but be aware that his <span class="star-pagination">*358</span> property will be subject to periodic inspections undertaken for specific purposes." <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#600" aria-description="Citation for case: Donovan v. Dewey"><i>Id.,</i> at 600</a></span>.</blockquote>
<p>In <i><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">Donovan</a></span>,</i> the Court pointed out that a valid inspection scheme must provide, "in terms of the certainty and regularity of its application . . . a constitutionally adequate substitute for a warrant." <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#603" aria-description="Citation for case: Donovan v. Dewey"><i>Id.,</i> at 603</a></span>. In <i>Marshall</i> v. <i>Barlow's, Inc.,</i> <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307</a></span> (1978), to be sure, the Court held that a warrantless administrative search under § 8(a) of the Occupational Safety and Health Act of 1970 was invalid, partly because the "authority to make warrantless searches devolve[d] almost unbridled discretion upon executive and administrative officers, particularly those in the field, as to when to search and whom to search." <i>Id.,</i> at 323.<sup>[14]</sup> In contrast, the Court in <i><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">Donovan</a></span></i> concluded that the Federal Mine Safety and Health Act of 1977 imposed a system of inspection that was sufficiently tailored to the problems of unsafe conditions in mines and was sufficiently pervasive that it checked the discretion of Government officers and established "a predictable and guided federal regulatory presence." <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#604" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 604</a></span>.</p>
<p>Under the standards established in these cases, Detective McNally's reliance on the Illinois statute authorizing warrantless inspections of licensees was objectively reasonable. In ruling on the statute's constitutionality, the Illinois Supreme Court recognized that the licensing and inspection scheme furthered a strong public interest, for it helped to "facilitate the discovery and prevention of automobile thefts." <span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/#116" aria-description="Citation for case: People v. Krull">107 Ill. 2d, at 116</a></span>, <span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/#707" aria-description="Citation for case: People v. Krull">481 N. E. 2d, at 707</a></span>. The court further concluded that it was "reasonable to assume that warrantless administrative <span class="star-pagination">*359</span> searches are necessary in order to adequately control the theft of automobiles and automotive parts." <i><span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/" aria-description="Citation for case: People v. Krull">Ibid.</a></span></i> The Court of Appeals for the Seventh Circuit, upholding the amended version of the statute, pointed out that used-car and automotive-parts dealers in Illinois "are put on notice that they are entering a field subject to extensive state regulation." See <i>Bionic Auto Parts &amp; Sales, Inc.</i> v. <i>Fahner,</i> <span class="citation" data-id="427553"><a href="/opinion/427553/bionic-auto-parts-and-sales-inc-v-tyrone-c-fahner/#1079" aria-description="Citation for case: Bionic Auto Parts and Sales, Inc. v. Tyrone C. Fahner">721 F. 2d, at 1079</a></span>. The Illinois statute was thus directed at one specific and heavily regulated industry, the authorized warrantless searches were necessary to the effectiveness of the inspection system, and licensees were put on notice that their businesses would be subject to inspections pursuant to the state administrative scheme.</p>
<p>According to the Illinois Supreme Court, the statute failed to pass constitutional muster solely because the statute "vested State officials with too much discretion to decide who, when, and how long to search." <span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/#116" aria-description="Citation for case: People v. Krull">107 Ill. 2d, at 116</a></span>, <span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/#707" aria-description="Citation for case: People v. Krull">481 N. E. 2d, at 707</a></span>. Assuming, as we do for purposes of this case, that the Illinois Supreme Court was correct in its constitutional analysis, this defect in the statute was not sufficiently obvious so as to render a police officer's reliance upon the statute objectively unreasonable. The statute provided that searches could be conducted "at any reasonable time during the night or day," and seemed to limit the scope of the inspections to the records the businesses were required to maintain and to the business premises "for the purposes of determining the accuracy of required records." Ill. Rev. Stat., ch. 95 1/2, ¶ 5-401(e) (1981). While statutory provisions that circumscribe officers' discretion may be important in establishing a statute's constitutionality,<sup>[15]</sup> the additional restrictions on discretion <span class="star-pagination">*360</span> that might have been necessary are not so obvious that an objectively reasonable police officer would have realized the statute was unconstitutional without them.<sup>[16]</sup> We therefore conclude that Detective McNally relied, in objective good faith, on a statute that appeared legitimately to allow a warrantless administrative search of respondents' business.<sup>[17]</sup></p>
<p><span class="star-pagination">*361</span> Accordingly, the judgment of the Supreme Court of Illinois is reversed, and the case is remanded to that court for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE MARSHALL, dissenting.</p>
<p>While I join in JUSTICE O'CONNOR's dissenting opinion, I do not find it necessary to discuss the Court's holdings in <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">414 U. S. 338</a></span> (1974), <i>Stone</i> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U. S. 465</a></span> (1976), and <i>United States</i> v. <i>Janis,</i> <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">428 U. S. 433</a></span> (1976). See <i>post,</i> at 368-369. Accordingly, I do not subscribe to that portion of the opinion.</p>
<p>JUSTICE O'CONNOR, with whom JUSTICE BRENNAN, JUSTICE MARSHALL, and JUSTICE STEVENS join, dissenting.</p>
<p>The Court today extends the good-faith exception to the Fourth Amendment exclusionary rule, <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U. S. 897</a></span> (1984), in order to provide a grace period for unconstitutional search and seizure legislation during which the State is permitted to violate constitutional requirements with impunity. <i>Leon's</i> rationale does not support this extension of its rule, and the Court is unable to give any independent reason in defense of this departure from established precedent. Accordingly, I respectfully dissent.</p>
<p>The Court, <i>ante,</i> at 348, accurately summarizes <i>Leon's</i> holding:</p>
<blockquote>"In <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>,</i> the Court held that the exclusionary rule should not be applied to evidence obtained by a police officer whose reliance on a search warrant issued by a neutral magistrate was objectively reasonable, even though the warrant was ultimately found to be defective."</blockquote>
<p><span class="star-pagination">*362</span> The Court also accurately summarizes the reasoning supporting this conclusion as based upon three factors: the historic purpose of the exclusionary rule, the absence of evidence suggesting that judicial officers are inclined to ignore Fourth Amendment limitations, and the absence of any basis for believing that the exclusionary rule significantly deters Fourth Amendment violations by judicial officers in the search warrant context. <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Ibid.</a></span></i> In my view, application of <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i>'s stated rationales leads to a contrary result in this case.</p>
<p>I agree that the police officer involved in this case acted in objective good faith in executing the search pursuant to Ill. Rev. Stat., ch. 95 1/2, ¶ 5-401(e) (1981) (repealed 1985). <i>Ante,</i> at 360. And, as the Court notes, <i>ante,</i> at 357, n. 13, the correctness of the Illinois Supreme Court's finding that this statute violated the Fourth Amendment is not in issue here. Thus, this case turns on the effect to be given to statutory authority for an unreasonable search.</p>
<p>Unlike the Court, I see a powerful historical basis for the exclusion of evidence gathered pursuant to a search authorized by an unconstitutional statute. Statutes authorizing unreasonable searches were the core concern of the Framers of the Fourth Amendment. This Court has repeatedly noted that reaction against the ancient Act of Parliament authorizing indiscriminate general searches by writ of assistance, 7 &amp; 8 Wm. III, c. 22, § 6 (1696), was the moving force behind the Fourth Amendment. <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 583-584</a></span>, and n. 21 (1980); <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 481-482</a></span> (1965); <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 624-630</a></span> (1886). James Otis' argument to the royal Superior Court in Boston against such overreaching laws is as powerful today as it was in 1761:</p>
<blockquote>". . . I will to my dying day oppose with all the powers and faculties God has given me, all such instruments of <span class="star-pagination">*363</span> slavery on the one hand, and villany on the other, as this writ of assistance is. . . .</blockquote>
<blockquote>.....</blockquote>
<blockquote>". . . It is a power, that places the liberty of every man in the hands of every petty officer. . . .</blockquote>
<blockquote>". . . No Acts of Parliament can establish such a writ; though it should be made in the very words of the petition, it would be void. An act against the constitution is void." 2 Works of John Adams 523-525 (C. Adams ed. 1850).</blockquote>
<p>See <i>Paxton's Case,</i> Quincy 51 (Mass. 1761). James Otis lost the case he argued; and, even had he won it, no exclusionary rule existed to prevent the admission of evidence gathered pursuant to a writ of assistance in a later trial. But, history's court has vindicated Otis. The principle that no legislative Act can authorize an unreasonable search became embodied in the Fourth Amendment.</p>
<p>Almost 150 years after Otis' argument, this Court determined that evidence gathered in violation of the Fourth Amendment would be excluded in federal court. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914). In <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), the rule was further extended to state criminal trials. This exclusionary rule has, of course, been regularly applied to evidence gathered under statutes that authorized unreasonable searches. See, <i>e. g., </i><i>Ybarra</i> v. <i>Illinois,</i> <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85</a></span> (1979) (statute authorized search and detention of persons found on premises being searched pursuant to warrant); <i>Torres</i> v. <i>Puerto Rico,</i> <span class="citation" data-id="9795098"><a href="/opinion/2620876/torres-v-puerto-rico/" aria-description="Citation for case: Torres v. Puerto Rico">442 U. S. 465</a></span> (1979) (statute authorized search of luggage of persons entering Puerto Rico); <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973) (statute authorized search of automobiles without probable cause within border areas); <i>Sibron</i> v. <i>New York,</i> <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span> (1968) (statute authorized frisk absent constitutionally required suspicion that officer was in danger); <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967) (permissive eavesdrop statute). <span class="star-pagination">*364</span> Indeed, <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> itself made clear that the exclusionary rule was intended to apply to evidence gathered by officers acting under "legislative . . . sanction." <i>Weeks</i> v. <i>United States, supra,</i> at 394.</p>
<p><i>Leon</i> on its face did not purport to disturb these rulings. " `Those decisions involved statutes which, by their own terms, authorized searches under circumstances which did not satisfy the traditional warrant and probable-cause requirements of the Fourth Amendment.' <i>Michigan</i> v. <i>DeFillippo,</i> <span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/#39" aria-description="Citation for case: Michigan v. DeFillippo">443 U. S., at 39</a></span>. The substantive Fourth Amendment principles announced in those cases are fully consistent with our holding here." <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#912" aria-description="Citation for case: United States v. Leon">468 U. S., at 912, n. 8</a></span>. In short, both the history of the Fourth Amendment and this Court's later interpretations of it, support application of the exclusionary rule to evidence gathered under the 20th-century equivalent of the Act authorizing the writ of assistance.</p>
<p>This history also supplies the evidence that <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i> demanded for the proposition that the relevant state actors, here legislators, might pose a threat to the values embodied in the Fourth Amendment. Legislatures have, upon occasion, failed to adhere to the requirements of the Fourth Amendment, as the cited cases illustrate. Indeed, as noted, the history of the Amendment suggests that legislative abuse was precisely the evil the Fourth Amendment was intended to eliminate. In stark contrast, the Framers did not fear that judicial officers, the state actors at issue in <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>,</i> posed a serious threat to Fourth Amendment values. James Otis is as clear on this point as he was in denouncing the unconstitutional Act of Parliament:</p>
<blockquote>"In the first place, may it please your Honors, I will admit that writs of one kind may be legal; that is, special writs, directed to special officers, and to search certain houses, &amp;c. specially set forth in the writ, may be granted by the Court of Exchequer at home, upon oath made before the Lord Treasurer by the person who asks it, that <span class="star-pagination">*365</span> he suspects such goods to be concealed in those very places he desires to search." 2 Works of John Adams 524 (C. Adams ed. 1850).</blockquote>
<p>The distinction drawn between the legislator and the judicial officer is sound. The judicial role is particularized, fact specific, and nonpolitical. Judicial authorization of a particular search does not threaten the liberty of everyone, but rather authorizes a single search under particular circumstances. The legislative Act, on the other hand, sweeps broadly, authorizing whole classes of searches, without any particularized showing. A judicial officer's unreasonable authorization of a search affects one person at a time; a legislature's unreasonable authorization of searches may affect thousands or millions and will almost always affect more than one. Certainly the latter poses a greater threat to liberty.</p>
<p>Moreover, the <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i> Court relied explicitly on the tradition of judicial independence in concluding that, until it was presented with evidence to the contrary, there was relatively little cause for concern that judicial officers might take the opportunity presented by the good-faith exception to authorize unconstitutional searches. "Judges and magistrates are not adjuncts to the law enforcement team; as neutral judicial officers, they have no stake in the outcome of particular criminal prosecutions." <i>United States</i> v. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#917" aria-description="Citation for case: United States v. Leon"><i>Leon, supra,</i> at 917</a></span>. Unlike police officers, judicial officers are not "engaged in the often competitive enterprise of ferreting out crime." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948). The legislature's objective in passing a law authorizing unreasonable searches, however, is explicitly to facilitate law enforcement. Fourth Amendment rights have at times proved unpopular; it is a measure of the Framers' fear that a passing majority might find it expedient to compromise Fourth Amendment values that these values were embodied in the Constitution itself. <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#544" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 544</a></span> (1897). Legislators by virtue of their political role are more often subjected <span class="star-pagination">*366</span> to the political pressures that may threaten Fourth Amendment values than are judicial officers.</p>
<p>Finally, I disagree with the Court that there is "no reason to believe that applying the exclusionary rule" will deter legislation authorizing unconstitutional searches. <i>Ante,</i> at 352. "The inevitable result of the Constitution's prohibition against unreasonable searches and seizures and its requirement that no warrant shall issue but upon probable cause is that police officers who obey its strictures will catch fewer criminals." Stewart, <span class="citation no-link">83 Colum. L. Rev. 1365</span>, 1393 (1983). Providing legislatures a grace period during which the police may freely perform unreasonable searches in order to convict those who might have otherwise escaped creates a positive incentive to promulgate unconstitutional laws. Cf. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S., at 392-393</a></span>. While I heartily agree with the Court that legislators ordinarily do take seriously their oaths to uphold the Constitution and that it is proper to presume that legislative Acts are constitutional, <i>ante,</i> at 351, it cannot be said that there is no reason to fear that a particular legislature might yield to the temptation offered by the Court's good-faith exception.</p>
<p>Accordingly, I find that none of <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i>'s stated rationales, see <i>ante,</i> at 348, supports the Court's decision in this case. History suggests that the exclusionary rule ought to apply to the unconstitutional legislatively authorized search, and this historical experience provides a basis for concluding that legislatures may threaten Fourth Amendment values. Even conceding that the deterrent value of the exclusionary rule in this context is arguable, I am unwilling to abandon both history and precedent weighing in favor of suppression. And if I were willing, I still could not join the Court's opinion because the rule it adopts is both difficult to administer and anomalous.</p>
<p>The scope of the Court's good-faith exception is unclear. Officers are to be held not "to have acted in good-faith reliance upon a statute if its provisions are such that a reasonable <span class="star-pagination">*367</span> officer should have known that the statute was unconstitutional. Cf. <i>Harlow</i> v. <i>Fitzgerald,</i> <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 818</a></span> (1982)." <i>Ante,</i> at 355. I think the Court errs in importing <i><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span></i>'s "clearly established law" test into this area, because it is not apparent how much constitutional law the reasonable officer is expected to know. In contrast, <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i> simply instructs courts that police officers may rely upon a facially valid search warrant. Each case is a fact-specific, self-terminating episode. Courts need not inquire into the officer's probable understanding of the state of the law except in the extreme instance of a search warrant upon which no reasonable officer would rely. Under the decision today, however, courts are expected to determine at what point a reasonable officer should be held to know that a statute has, under evolving legal rules, become "clearly" unconstitutional. The process of clearly establishing constitutional rights is a long, tedious, and uncertain one. Indeed, as the Court notes, <i>ante,</i> at 357, n. 13, the unconstitutionality of the Illinois statute is not clearly established to this day. The Court has granted certiorari on the question of the constitutionality of a similar statutory scheme in <i>New York</i> v. <i>Burger,</i> <span class="citation no-link">479 U. S. 482</span> (1986). Thus, some six years after the events in question in this case, the constitutionality of statutes of this kind remains a fair ground for litigation. Nothing justifies a grace period of such extraordinary length for an unconstitutional legislative act.</p>
<p>The difficulties in determining whether a particular statute violates clearly established rights are substantial. See 5 K. Davis, Administrative Law Treatise § 27:24, p. 130 (2d ed. 1984) ("The most important effect of [<i>Davis</i> v. <i>Scherer,</i> <span class="citation" data-id="9429708"><a href="/opinion/111241/davis-v-scherer/" aria-description="Citation for case: Davis v. Scherer">468 U. S. 183</a></span> (1984)] on future law relates to locating the line between established constitutional rights and clearly established constitutional rights. In assigning itself the task of drawing such a line the Court may be attempting the impossible. Law that can be clearly stated in the abstract usually becomes unclear when applied to variable and imperfectly <span class="star-pagination">*368</span> understood facts . . ."). The need for a rule so difficult of application outside the civil damages context is, in my view, dubious. The Court has determined that fairness to the defendant, as well as public policy, dictates that individual government officers ought not be subjected to damages suits for arguable constitutional violations. <i>Harlow</i> v. <i>Fitzgerald,</i> <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#807" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 807</a></span> (1982) (citing <i>Butz</i> v. <i>Economou,</i> <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#506" aria-description="Citation for case: Butz v. Economou">438 U. S. 478, 506</a></span> (1978)). But suppression of illegally obtained evidence does not implicate this concern.</p>
<p>Finally, I find the Court's ruling in this case at right angles, if not directly at odds, with the Court's recent decision in <i>Griffith</i> v. <i>Kentucky,</i> <span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/" aria-description="Citation for case: Griffith v. Kentucky">479 U. S. 314</a></span> (1987). In <i><span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/" aria-description="Citation for case: Griffith v. Kentucky">Griffith</a></span>,</i> the Court held that "basic norms of constitutional adjudication" and fairness to similarly situated defendants, <span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/#322" aria-description="Citation for case: Griffith v. Kentucky"><i>id.,</i> at 322</a></span>, require that we give our decisions retroactive effect to all cases not yet having reached final, and unappealable, judgment. While the extent to which our decisions ought to be applied retroactively has been the subject of much debate among Members of the Court for many years, <span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/#320" aria-description="Citation for case: Griffith v. Kentucky"><i>id.,</i> at 320-326</a></span>, there has never been any doubt that our decisions are applied to the parties in the case before the Court. <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#301" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293, 301</a></span> (1967). The novelty of the approach taken by the Court in this case is illustrated by the fact that under its decision today, no effective remedy is to be provided in the very case in which the statute at issue was held unconstitutional. I recognize that the Court today, as it has done in the past, divorces the suppression remedy from the substantive Fourth Amendment right. See <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#905" aria-description="Citation for case: United States v. Leon">468 U. S., at 905-908</a></span>. This Court has held that the exclusionary rule is a "judicially created remedy designed to safeguard Fourth Amendment rights generally through its deterrent effect, rather than a personal constitutional right of the party aggrieved." <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 348</a></span> (1974). Moreover, the exclusionary remedy is not made available in all instances when Fourth Amendment rights are implicated. See, <i>e. g., </i><i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span></i> <span class="star-pagination">*369</span> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U. S. 465</a></span> (1976) (barring habeas corpus review of Fourth Amendment suppression claims); <i>United States</i> v. <i>Janis,</i> <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">428 U. S. 433</a></span> (1976) (no suppression remedy for state Fourth Amendment violations in civil proceedings by or against the United States). Nevertheless, the failure to apply the exclusionary rule in the very case in which a state statute is held to have violated the Fourth Amendment destroys all incentive on the part of individual criminal defendants to litigate the violation of their Fourth Amendment rights. In my view, whatever "basic norms of constitutional adjudication," <i>Griffith</i> v. <span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/#322" aria-description="Citation for case: Griffith v. Kentucky"><i>Kentucky, supra,</i> at 322</a></span>, otherwise require, surely they mandate that a party appearing before the Court might conceivably benefit from a judgment in his favor. The Court attempts to carve out a proviso to its good-faith exception for those cases in which "the legislature wholly abandoned its responsibility to enact constitutional laws." <i>Ante,</i> at 355. Under what circumstances a legislature can be said to have "wholly abandoned" its obligation to pass constitutional laws is not apparent on the face of the Court's opinion. Whatever the scope of the exception, the inevitable result of the Court's decision to deny the realistic possibility of an effective remedy to a party challenging statutes not yet declared unconstitutional is that a chill will fall upon enforcement and development of Fourth Amendment principles governing legislatively authorized searches.</p>
<p>For all these reasons, I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]  <i>Robert K. Corbin,</i> Attorney General of Arizona, <i>Daniel B. Hales, James A. Murphy, Jack E. Yelverton, Fred E. Inbau, Wayne W. Schmidt,</i> and <i>James P. Manak</i> filed a brief for the State of Arizona et al. as <i>amici curiae</i> urging reversal.</p>
<p>[1]  Paragraph 5-401 of the 1981 compilation was repealed by 1983 Ill. Laws No. 83-1473, § 2, effective Jan. 1, 1985. Its current compilation replacement bears the same paragraph number.</p>
<p>[2]  Citations to the transcript refer to the Sept. 25, 1981, hearing on respondents' suppression motion held in the Circuit Court of Cook County. 2 Record 24.</p>
<p>[3]  The trial court also concluded that Lucas had not consented to the search. App. 20. That ruling is not now at issue here.</p>
<p>[4]  Following the decision of the District Court in <i>Bionic Auto Parts &amp; Sales, Inc.</i> v. <i>Fahner,</i> <span class="citation" data-id="2128773"><a href="/opinion/2128773/bionic-auto-parts-and-sales-inc-v-fahner/" aria-description="Citation for case: Bionic Auto Parts and Sales, Inc. v. Fahner">518 F. Supp. 582</a></span> (ND Ill. 1981), the Illinois Legislature amended the statute to limit the timing, frequency, and duration of the administrative search. 1982 Ill. Laws No. 82-984, codified, as amended, at Ill. Rev. Stat., ch. 95 1/2, ¶ 5-403 (1985). See n. 1, <i>supra.</i> On appeal, the Court of Appeals for the Seventh Circuit did not address the validity of the earlier form of the statute, for it held that the amended statute satisfied the requirements of the Fourth Amendment. See <i>Bionic Auto Parts &amp; Sales, Inc.</i> v. <i>Fahner,</i> <span class="citation" data-id="427553"><a href="/opinion/427553/bionic-auto-parts-and-sales-inc-v-tyrone-c-fahner/#1075" aria-description="Citation for case: Bionic Auto Parts and Sales, Inc. v. Tyrone C. Fahner">721 F. 2d 1072, 1075</a></span> (1983).</p>
<p>[5]  The trial court also indicated that McNally may have acted outside the scope of his statutory authority when he examined vehicles other than those listed on the pad offered by Lucas. App. 29; 5 Record 2, 8.</p>
<p>[6]  The State bypassed the Illinois intermediate appellate court and appealed directly to the Supreme Court of Illinois pursuant to Illinois Supreme Court Rule 603.</p>
<p>[7]  Indeed, the possibility of a deterrent effect may be even less when the officer acts pursuant to a statute rather than a warrant. In <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>,</i> the Court pointed out: "One could argue that applying the exclusionary rule in cases where the police failed to demonstrate probable cause in the warrant application deters future inadequate presentations or `magistrate shopping' and thus promotes the ends of the Fourth Amendment." 468 U. S., at 918. Although the Court in <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i> dismissed that argument as speculative, <i>ibid.,</i> the possibility that a police officer might modify his behavior does not exist at all when the officer relies on an existing statute that authorizes warrantless inspections and does not require any preinspection action, comparable to seeking a warrant, on the part of the officers.</p>
<p>[8]  It is possible, perhaps, that there are some legislators who, for political purposes, are possessed with a zeal to enact a particular unconstitutionally restrictive statute, and who will not be deterred by the fact that a court might later declare the law unconstitutional. But we doubt whether a legislator possessed with such fervor, and with such disregard for his oath to support the Constitution, would be significantly deterred by the possibility that the exclusionary rule would preclude the introduction of evidence in a certain number of prosecutions. Moreover, and of equal importance, just as we were not willing to assume in <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span></i> that the possibility of magistrates' acting as "rubber stamps for the police" was a problem of major proportions, see 468 U. S., at 916, n. 14, we are not willing to assume now that there exists a significant problem of legislators who perform their legislative duties with indifference to the constitutionality of the statutes they enact. If future empirical evidence ever should undermine that assumption, our conclusions may be revised accordingly. See <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#927" aria-description="Citation for case: United States v. Leon">468 U. S., at 927-928</a></span> (concurring opinion).</p>
<p>[9]  In <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>,</i> the Court pointed out: "An objectionable collateral consequence of this interference with the criminal justice system's truth-finding function is that some guilty defendants may go free or receive reduced sentences as a result of favorable plea bargains." <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#907" aria-description="Citation for case: United States v. Leon"><i>Id.,</i> at 907</a></span>.</p>
<p>[10]  Moreover, it is not always true that the issuance of defective warrants will affect only a few persons. For example, it is possible that before this Court's rather controversial decision in <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), see <i>Illinois</i> v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#238" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 238</a></span>, and n. 11 (1983), a number of magistrates believed that probable cause could be established solely on the uncorroborated allegations of a police officer and a significant number of warrants may have been issued on that basis. Until that view was adjusted by this Court's ruling, many persons may have been affected by the systematic granting of warrants based on erroneous views of the standards necessary to establish probable cause.</p>
<p>[11]  Other plaintiffs have challenged state statutes on Fourth Amendment grounds in declaratory judgment actions. See <i>California Restaurant Assn.</i> v. <i>Henning,</i> <span class="citation" data-id="2108094"><a href="/opinion/2108094/california-restaurant-assn-v-henning/" aria-description="Citation for case: California Restaurant Assn. v. Henning">173 Cal. App. 3d 1069</a></span>, <span class="citation" data-id="2108094"><a href="/opinion/2108094/california-restaurant-assn-v-henning/" aria-description="Citation for case: California Restaurant Assn. v. Henning">219 Cal. Rptr. 630</a></span> (1985) (organization of restaurant owners challenged constitutionality of state statute vesting authority in State Labor Commissioner to issue subpoenas compelling production of books and records); <i>Hawaii Psychiatric Soc.</i> v. <i>Ariyoshi,</i> <span class="citation" data-id="2398127"><a href="/opinion/2398127/hawaii-psychiatric-society-district-branch-of-the-american-psychiatric/" aria-description="Citation for case: Hawaii Psychiatric Society, District Branch of the...">481 F. Supp. 1028</a></span> (Haw. 1979) (action to enjoin enforcement of state statute that authorized issuance of administrative inspection warrants to search records of Medicaid providers); <i>Bilbrey</i> v. <i>Brown,</i> <span class="citation" data-id="438820"><a href="/opinion/438820/bilbrey-v-brown/" aria-description="Citation for case: Bilbrey v. Brown">738 F. 2d 1462</a></span> (CA9 1984) (parents sought declaration that school board guidelines authorizing warrantless searches by school principal and teacher were unconstitutional); see also <i>Mid-Atlantic Accessories Trade Assn.</i> v. <i>Maryland,</i> <span class="citation" data-id="1409370"><a href="/opinion/1409370/mid-atlantic-accessories-trade-assn-v-maryland/#848" aria-description="Citation for case: Mid-Atlantic Accessories Trade Ass&#x27;n v. Maryland">500 F. Supp. 834, 848-849</a></span> (Md. 1980) (challenging constitutionality of Maryland Drug Paraphernalia Act as violative of the Fourth Amendment and other constitutional provisions).
</p>
<p>The dissent takes issue with the rule announced in this case because it can result in having a defendant, who has successfully challenged the constitutionality of a statute, denied the benefits of suppression of evidence. <i>Post,</i> at 368-369. As the dissent itself recognizes, however, this identical concern was present in <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>.</i> The dissent offers no reason why this concern should be different when a defendant challenges the constitutionality of a statute rather than of a warrant.</p>
<p>[12]  The Illinois Supreme Court did not consider whether an officer's objectively reasonable reliance upon a statute justifies an exception to the exclusionary rule. Instead, as noted above, the court rested its holding on the existence of a "substantive-procedural dichotomy," which it would derive from this Court's opinion in <i>Michigan</i> v. <i>DeFillippo,</i> <span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">443 U. S. 31</a></span> (1979). See <span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/#118" aria-description="Citation for case: People v. Krull">107 Ill. 2d 107, 118</a></span>, <span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/#708" aria-description="Citation for case: People v. Krull">481 N. E. 2d 703, 708</a></span> (1985). We do not believe the distinction relied upon by the Illinois court is relevant in deciding whether the exclusionary rule should be applied in this case.
</p>
<p>This Court in <i><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">DeFillippo</a></span>,</i> which was decided before <i><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>,</i> drew a distinction between evidence obtained when officers rely upon a statute that defines a substantive crime, and evidence obtained when officers rely upon a statute that authorizes searches without a warrant or probable cause. The Court stated that evidence obtained in searches conducted pursuant to the latter type of statute traditionally had been excluded. <span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/#39" aria-description="Citation for case: Michigan v. DeFillippo">443 U. S., at 39</a></span>. None of the cases cited in <i><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">DeFillippo</a></span></i> in support of the distinction, however, addressed the question whether a good-faith exception to the exclusionary rule should be recognized when an officer's reliance on a statute was objectively reasonable. Rather, those cases simply evaluated the constitutionality of particular statutes, or their application, that authorized searches without a warrant or probable cause. See <i>Torres</i> v. <i>Puerto Rico,</i> <span class="citation" data-id="9795098"><a href="/opinion/2620876/torres-v-puerto-rico/" aria-description="Citation for case: Torres v. Puerto Rico">442 U. S. 465</a></span> (1979) (statute that allowed police to search luggage of any person arriving at an airport or pier in Puerto Rico, without any requirement of probable cause, violated Fourth Amendment); <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973) (search pursuant to statute that allowed United States Border Patrol to conduct warrantless searches within a "reasonable distance" from border, and regulation that defined such distance as 100 air miles, and without any requirement of probable cause violated Fourth Amendment); <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967) (statute that authorized court-ordered eavesdropping without requirement that information to be seized be particularized violated Fourth Amendment). See also <i>Sibron</i> v. <i>New York,</i> <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span> (1968) (search pursuant to statute that allowed officers to search an individual upon "reasonable suspicion" that he was engaged in criminal activity was unreasonable because it was conducted without probable cause). See <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#912" aria-description="Citation for case: United States v. Leon">468 U. S., at 912, n. 8</a></span>.</p>
<p>For purposes of deciding whether to apply the exclusionary rule, we see no valid reason to distinguish between statutes that define substantive criminal offenses and statutes that authorize warrantless administrative searches. In either situation, application of the exclusionary rule will not deter a violation of the Fourth Amendment by police officers, because the officers are merely carrying out their responsibilities in implementing the statute. Similarly, in either situation, there is no basis for assuming that the exclusionary rule is necessary or effective in deterring a legislature from passing an unconstitutional statute. There is no basis for applying the exclusionary rule to exclude evidence obtained when a law enforcement officer acts in objectively reasonable reliance upon a statute, regardless of whether the statute may be characterized as "substantive" or "procedural."</p>
<p>[13]  The question whether the Illinois statute in effect at the time of McNally's search was, in fact, unconstitutional is not before us. We are concerned here solely with whether the detective acted in good-faith reliance upon an apparently valid statute. The constitutionality of a statutory scheme authorizing warrantless searches of automobile junkyards will be considered in No. 86-80, <i>New York</i> v. <i><span class="citation no-link">Burger</span>,</i> cert. granted, <span class="citation multiple-matches"><a href="/c/U.%20S./479/812/">479 U. S. 812</a></span> (1986).</p>
<p>[14]  The Court expressly limited its holding in <i>Barlow's</i> to the inspection provisions of the Act. It noted that the "reasonableness of a warrantless search . . . will depend upon the specific enforcement needs and privacy guarantees of each statute," and that some statutes "apply only to a single industry, where regulations might already be so pervasive that a <i>Colonnade-Biswell</i> exception to the warrant requirement could apply." <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#321" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 321</a></span>.</p>
<p>[15]  For example, the amended version of the Illinois statute, upheld by the Court of Appeals for the Seventh Circuit, incorporated the following: (1) the inspections were to be initiated while business was being conducted; (2) each inspection was not to last more than 24 hours; (3) the licensee or his representative was entitled to be present during the inspection; and (4) no more than six inspections of one business location could be conducted within any 6-month period except pursuant to a search warrant or in response to public complaints about violations. Ill. Rev. Stat., ch. 95 1/2, ¶ 5-403 (1985).</p>
<p>[16]  Indeed, less than a year and a half before the search of respondents' yard, the Supreme Court of Indiana upheld an Indiana statute, authorizing warrantless administrative searches of automobile businesses, that was similar to the Illinois statute and did not include extensive restrictions on police officers' discretion. See <i>State</i> v. <i>Tindell,</i> <span class="citation" data-id="2123138"><a href="/opinion/2123138/state-v-tindell/" aria-description="Citation for case: State v. Tindell">272 Ind. 479</a></span>, <span class="citation" data-id="2123138"><a href="/opinion/2123138/state-v-tindell/" aria-description="Citation for case: State v. Tindell">399 N. E. 2d 746</a></span> (1980).</p>
<p>[17]  Respondents also argue that Detective McNally acted outside the scope of the statute, and that such action constitutes an alternative ground for suppressing the evidence even if we recognize, as we now do, a goodfaith exception when officers reasonably rely on statutes and act within the scope of those statutes. We have observed, see n. 5, <i>supra,</i> that the trial court indicated that McNally may have acted outside the scope of his statutory authority. In its brief to the Illinois Supreme Court, the State commented that "[McNally's] search was properly limited to examining the records and inventory of the Action Iron and Metal Company." Brief for Appellant in No. 60629 (Sup. Ct. Ill.), p. 26. The Illinois Supreme Court, however, made no reference to the trial court's discussion regarding the scope of McNally's authority; instead, it affirmed the suppression of the evidence on the ground that a good-faith exception was not applicable in the context of the statute before it.
</p>
<p>We anticipate that the Illinois Supreme Court on remand will consider whether the trial court made a definitive ruling regarding the scope of the statute, whether the State preserved its objection to any such ruling, and, if so, whether the trial court properly interpreted the statute. At this juncture, we decline the State's invitation to recognize an exception for an officer who erroneously, but in good faith, believes he is acting within the scope of a statute. Not only would such a ruling be premature, but it does not follow inexorably from today's decision. As our opinion makes clear, the question whether the exclusionary rule is applicable in a particular context depends significantly upon the actors who are making the relevant decision that the rule is designed to influence. The answer to this question might well be different when police officers act outside the scope of a statute, albeit in good faith. In that context, the relevant actors are not legislators or magistrates, but police officers who concededly are "engaged in the often competitive enterprise of ferreting out crime." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948).</p>

</div>
```

---
