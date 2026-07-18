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

## GROUP: content/cases/Heck v. Humphrey.md  (`case`, 5 assertions)

### content_page

```
---
title: "Heck v. Humphrey"
type: case
citation: "512 U.S. 477 (1994)"
parallel_cite: "114 S. Ct. 2364; 129 L. Ed. 2d 383"
neutral_cite: 1994 U.S. LEXIS 4824
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1994
date_decided: 1994-06-24
docket: 93-6188
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1994-06-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Heck v. Humphrey
  varies_by_point: false
  scope_note: "Good law: the favorable-termination rule for § 1983 damages claims that would imply the invalidity of a conviction."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/117864/heck-v-humphrey/"
  cluster_id: 117864
  opinion_id: 117864
  identity_checked: true
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Monroe v. Pape]]"]
aliases: []
tags: ["case", "section-1983", "favorable-termination", "heck-bar", "habeas", "conviction"]
holding: "A § 1983 damages claim whose success would necessarily imply the invalidity of an outstanding conviction or sentence is not cognizable unless the conviction has first been reversed, expunged, declared invalid, or called into question by habeas (the favorable-termination requirement)."
lake:
  record_id: Heck v. Humphrey
  status: verified
  projected_at: 2026-07-06
---

# Heck v. Humphrey

*512 U.S. 477 (1994)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Roy Heck was convicted in Indiana of voluntary manslaughter for killing his wife. While his conviction was being challenged, he brought a § 1983 damages action against prosecutors and a state police investigator, alleging they had conducted an unlawful investigation, knowingly destroyed [[Brady and Giglio|exculpatory]] evidence, and used an unlawful voice-identification procedure. He sought money damages, not release from custody — but the claims, if proven, would have implied that his still-valid conviction was unlawful.

## Issue
Whether a state prisoner may bring a § 1983 damages action that, if successful, would necessarily imply the invalidity of his outstanding conviction or sentence.

## Rule
Such a claim is barred until the conviction is invalidated. "We hold that, in order to recover damages for allegedly unconstitutional conviction or imprisonment, or for other harm caused by actions whose unlawfulness would render a conviction or sentence invalid, a § 1983 plaintiff must prove that the conviction or sentence has been reversed on direct appeal, expunged by executive order, declared invalid by a state tribunal authorized to make such determination, or called into question by a federal court's issuance of a writ of habeas corpus." — 512 U.S. at 486-487. ^pin-486

A § 1983 claim bearing that relationship to a conviction that has not been so invalidated is not cognizable and does not accrue. Analogizing to the common-law tort of malicious prosecution, the Court grounded this favorable-termination requirement in the need to avoid parallel civil attacks on outstanding criminal judgments.

## Application
Heck's allegations of an unlawful investigation and destroyed [[Brady and Giglio|exculpatory]] evidence, if established, would necessarily have implied that his manslaughter conviction was invalid. Because that conviction had not been reversed, expunged, declared invalid, or called into question by [[Common Legal Terms#habeas-corpus|habeas]], his § 1983 damages claim was not cognizable, and the courts below correctly dismissed it (the claim had not yet accrued).

## Conclusion
Affirmed. A § 1983 damages action that would necessarily imply the invalidity of an outstanding conviction or sentence cannot proceed unless the conviction has first been favorably terminated.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The "Heck bar" / favorable-termination requirement remains the controlling rule for § 1983 claims that would impugn a conviction, refining the [[Monroe v. Pape]] § 1983 cause of action; it has been elaborated (not overruled) by later decisions on accrual and the boundary with [[Common Legal Terms#habeas-corpus|habeas]] (e.g., *Spencer v. Kemna*; *Wallace v. Kato*). No negative treatment.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *Heck v. Humphrey*, 512 U.S. 477 (1994) — https://www.courtlistener.com/opinion/117864/heck-v-humphrey/ — pinpoint: 486-487.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "250bff67a4719d57", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "512 U.S. 477 (1994)", "court": "U.S. Supreme Court", "neutral_cite": "1994 U.S. LEXIS 4824", "official_citation_present": true, "parallel_cite": "114 S. Ct. 2364; 129 L. Ed. 2d 383", "title": "Heck v. Humphrey", "year": "1994"}}
{"assertion_id": "6c964906197fe34f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A § 1983 damages claim whose success would necessarily imply the invalidity of an outstanding conviction or sentence is not cognizable unless the conviction has first been reversed, expunged, declared invalid, or called into question by habeas (the favorable-termination requirement).", "title": "Heck v. Humphrey"}}
{"assertion_id": "c74eb90d00a37f68", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Key — Progeny / Refinement", "title": "Heck v. Humphrey"}}
{"assertion_id": "d76bcf9cfc290938", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1994-06-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Heck v. Humphrey", "field_i_validity": "good_law", "scope_note": "Good law: the favorable-termination rule for § 1983 damages claims that would imply the invalidity of a conviction.", "title": "Heck v. Humphrey", "varies_by_point": "false"}}
{"assertion_id": "e9829cb1aba02151", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Heck v. Humphrey"}}
```

### lake record — Heck v. Humphrey

```json
{
  "schema_version": "s2.v1",
  "record_id": "Heck v. Humphrey",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Heck v. Humphrey",
    "case_name_short": "Heck",
    "case_name_full": "HECK v. HUMPHREY Et Al.",
    "input_case_name": "Heck v. Humphrey",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1994-06-24",
    "year": 1994,
    "docket": "93-6188",
    "cluster_id": 117864,
    "lead_opinion_id": 117864,
    "sibling_ids": [
      117864,
      9433019,
      9433020
    ],
    "absolute_url": "/opinion/117864/heck-v-humphrey/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 116323,
        "score": 20,
        "case_name": "Heck v. Humphrey"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "512 U.S. 477",
      "volume": "512",
      "reporter": "U.S.",
      "page": "477",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "114 S. Ct. 2364",
        "volume": "114",
        "reporter": "S. Ct.",
        "page": "2364",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 L. Ed. 2d 383",
        "volume": "129",
        "reporter": "L. Ed. 2d",
        "page": "383",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1994 U.S. LEXIS 4824",
        "volume": "1994",
        "reporter": "U.S. LEXIS",
        "page": "4824",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "512 U.S. 477",
        "volume": "512",
        "reporter": "U.S.",
        "page": "477",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "114 S. Ct. 2364",
        "volume": "114",
        "reporter": "S. Ct.",
        "page": "2364",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 L. Ed. 2d 383",
        "volume": "129",
        "reporter": "L. Ed. 2d",
        "page": "383",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1994 U.S. LEXIS 4824",
        "volume": "1994",
        "reporter": "U.S. LEXIS",
        "page": "4824",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "512 U.S. 477",
    "official_selection": {
      "court_class": "scotus",
      "selected": "512 U.S. 477",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-486",
      "page": null,
      "quote": "--- # Heck v. Humphrey *512 U.S. 477 (1994)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Roy Heck was convicted in Indiana of voluntary manslaughter for killing his wife. While his conviction was being challenged, he brought a \u00a7 1983 damages action against prosecutors and a state police investigator, alleging they had conducted an unlawful investigation, knowingly destroyed exculpatory evidence, and used an unlawful voice-identification procedure. He sought money damages, not release from custody \u2014 but the claims, if proven, would have implied that his still-valid conviction was unlawful. ## Issue Whether a state prisoner may bring a \u00a7 1983 damages action that, if successful, would necessarily imply the invalidity of his outstanding conviction or sentence. ## Rule Such a claim is barred until the conviction is invalidated.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1994-06-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Heck v. Humphrey",
    "varies_by_point": false,
    "scope_note": "Good law: the favorable-termination rule for \u00a7 1983 damages claims that would imply the invalidity of a conviction.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Trump v. J. G. G.",
          "cluster_id": 10373795,
          "cite": [
            "604 U.S. 670",
            "145 S. Ct. 1003"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Tinsley v. Town of Framingham",
          "cluster_id": 4786329,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "J. Wilkerson v. B. Wheeler",
          "cluster_id": 2752607,
          "cite": [
            "772 F.3d 834",
            "2014 U.S. App. LEXIS 21809",
            "2014 WL 6435497"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wallace v. Kato",
          "cluster_id": 145756,
          "cite": [
            "127 S. Ct. 1091",
            "549 U.S. 384"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael Lacey v. Joseph Arpaio",
          "cluster_id": 807646,
          "cite": [
            "693 F.3d 896"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hebbe v. Pliler",
          "cluster_id": 151811,
          "cite": [
            "627 F.3d 338"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spencer v. Kemna",
          "cluster_id": 118176,
          "cite": [
            "140 L. Ed. 2d 43",
            "118 S. Ct. 978",
            "523 U.S. 1",
            "1998 U.S. LEXIS 1597"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilkinson v. Dotson",
          "cluster_id": 142877,
          "cite": [
            "161 L. Ed. 2d 253",
            "125 S. Ct. 1242",
            "544 U.S. 74",
            "2005 U.S. LEXIS 2204"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edwards v. Balisok",
          "cluster_id": 118112,
          "cite": [
            "137 L. Ed. 2d 906",
            "117 S. Ct. 1584",
            "520 U.S. 641",
            "1997 U.S. LEXIS 3075"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Andrews v. Cervantes",
          "cluster_id": 1249170,
          "cite": [
            "493 F.3d 1047",
            "2007 WL 1932824"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mayle v. Felix",
          "cluster_id": 799989,
          "cite": [
            "162 L. Ed. 2d 582",
            "125 S. Ct. 2562",
            "545 U.S. 644",
            "2005 U.S. LEXIS 5016"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lawrence H. Ramming v. United States of America, John Thomas Cloud v. United States",
          "cluster_id": 776641,
          "cite": [
            "281 F.3d 158",
            "2001 WL 1734813"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adepegba v. Hammons",
          "cluster_id": 732324,
          "cite": [
            "103 F.3d 383",
            "1996 U.S. App. LEXIS 33974"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
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
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Muhammad v. Close",
          "cluster_id": 131168,
          "cite": [
            "158 L. Ed. 2d 32",
            "124 S. Ct. 1303",
            "540 U.S. 749",
            "2004 U.S. LEXIS 1627",
            "72 U.S.L.W. 4216"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Semtek International Inc. v. Lockheed Martin Corp.",
          "cluster_id": 2621076,
          "cite": [
            "149 L. Ed. 2d 32",
            "121 S. Ct. 1021",
            "531 U.S. 497",
            "2001 U.S. LEXIS 1951",
            "2001 Cal. Daily Op. Serv. 1569",
            "69 U.S.L.W. 4147",
            "2001 Colo. J. C.A.R. 1046",
            "14 Fla. L. Weekly Fed. S 109"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wayne LaFountain v. Shirlee Harry",
          "cluster_id": 868648,
          "cite": [
            "716 F.3d 944",
            "85 Fed. R. Serv. 3d 1166",
            "2013 WL 2221569",
            "2013 U.S. App. LEXIS 10274"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lloyd D. Alkire v. Judge Jane Irving",
          "cluster_id": 782133,
          "cite": [
            "330 F.3d 802",
            "55 Fed. R. Serv. 3d 1023",
            "2003 U.S. App. LEXIS 10834",
            "2003 WL 21251540"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Damous Nettles v. Randy Grounds",
          "cluster_id": 4241618,
          "cite": [
            "830 F.3d 922",
            "2016 U.S. App. LEXIS 13573",
            "2016 WL 4072465"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Manuel v. City of Joliet",
          "cluster_id": 4376986,
          "cite": [
            "580 U.S. 357",
            "137 S. Ct. 911",
            "197 L. Ed. 2d 312",
            "2017 U.S. LEXIS 2021",
            "26 Fla. L. Weekly Fed. S 476",
            "85 U.S.L.W. 4130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramirez v. Galaza",
          "cluster_id": 8437568,
          "cite": [
            "334 F.3d 850",
            "2003 WL 21478630"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony Dewalt v. Lamark Carter, Correctional Officer Young, Carol Biester",
          "cluster_id": 770154,
          "cite": [
            "224 F.3d 607",
            "2000 U.S. App. LEXIS 19806",
            "2000 WL 1137385"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colon v. Coughlin",
          "cluster_id": 7032950,
          "cite": [
            "58 F.3d 865",
            "1995 WL 383310"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jimmy Walker v. J.T. O'brien, and Joseph W. Finfrock v. Craig A. Hanks",
          "cluster_id": 769182,
          "cite": [
            "216 F.3d 626",
            "2000 U.S. App. LEXIS 14475"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nelson v. Campbell",
          "cluster_id": 134747,
          "cite": [
            "158 L. Ed. 2d 924",
            "124 S. Ct. 2117",
            "541 U.S. 637",
            "2004 U.S. LEXIS 3680"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
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
        "journal_ref": "Heck v. Humphrey:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(117864 OR 9433019 OR 9433020) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTgzNDUyODAwMDAwJnM9NDczMzE2OCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28117864+OR+9433019+OR+9433020%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      },
      "lane2_top_cited": {
        "query": "cites:(117864 OR 9433019 OR 9433020)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NzYmcz0xMzkwMjA5JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28117864+OR+9433019+OR+9433020%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(117864 OR 9433019 OR 9433020)",
        "reviewed": 99,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 99,
        "triage_read": 1,
        "triage_snippet_classified": 98
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(117864 OR 9433019 OR 9433020)",
    "indexed_citing_opinions": 2563,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 117864,
        "count": 2215,
        "count_source": "search"
      },
      {
        "opinion_id": 9433019,
        "count": 376,
        "count_source": "search"
      },
      {
        "opinion_id": 9433020,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 15484,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/heck-v-humphrey.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yLjA2NzczMTkmcz0yNDQwMDQ2JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28117864+OR+9433019+OR+9433020%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 117864,
        "cited_id": 91832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 95964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 103096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 104906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 104918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 107411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 108166,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 108578,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 108772,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 109097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 109387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 109405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 109815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 110022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 110236,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 110261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 110360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 110662,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 110753,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 111052,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 111093,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 111166,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 111224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 111611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 111721,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 112136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 112206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 112265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 112341,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 112534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 112566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 112733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 112771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 332456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 343322,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 610636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 1379591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 3299854,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 3319371,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 4926796,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117864,
        "cited_id": 5513412,
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
    "date_created": "2026-07-05T06:41:42Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T06:41:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T06:41:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T06:45:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T06:41:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Heck v. Humphrey

```
<div>
<center><b><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">512 U.S. 477</a></span> (1994)</b></center>
<center><h1>HECK<br>
v.<br>
HUMPHREY et al.</h1></center>
<center>No. 93-6188.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued April 18, 1994.</center>
<center>Decided June 24, 1994.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SEVENTH CIRCUIT
<p><span class="star-pagination">*478</span> Scalia,J., delivered the opinion of the court, in which Rehnquist, C.J., and Kennedy, Thomas, and Ginsburg, JJ., joined. Thomas, J., filed a concurring opinion, <i>post,</i> p. 490. Souter, J., filed an opinion concurring in the judgment, in which Blackmun, Stevens, and O'Connor, JJ., joined, <i>post,</i> p. 491.</p>
<p><i>Charles Rothfeld</i> argued the cause and filed briefs for petitioner.</p>
<p><i>Matthew R. Gutwein</i> argued the cause for respondents. With him on the brief were <i>Pamela Carter,</i> Attorney General of Indiana, and <i>Arend J. Abel</i> and <i>Dana Childress-Jones,</i>  Deputy Attorneys General.<sup>[*]</sup></p>
<p>Justice Scalia, delivered the opinion of the Court.</p>
<p>This case presents the question whether a state prisoner may challenge the constitutionality of his conviction in a suit for damages under <span class="citation no-link">42 U. S. C. § 1983</span>.</p>
<p></p>
<h2>I</h2>
<p>Petitioner Roy Heck was convicted in Indiana state court of voluntary manslaughter for the killing of Rickie Heck, his wife, and is serving a 15-year sentence in an Indiana prison. While the appeal from his conviction was pending, petitioner, <span class="star-pagination">*479</span> proceeding <i>pro se,</i> filed this suit in Federal District Court under <span class="citation no-link">42 U. S. C. § 1983</span>,<sup>[1]</sup> naming as defendants respondents James Humphrey and Robert Ewbank, Dearborn County prosecutors, and Michael Krinoph, an investigator with the Indiana State Police. The complaint alleged that respondents, acting under color of state law, had engaged in an "unlawful, unreasonable, and arbitrary investigation" leading to petitioner's arrest; "knowingly destroyed" evidence "which was exculpatory in nature and could have proved [petitioner's] innocence"; and caused "an illegal and unlawful voice identification procedure" to be used at petitioner's trial. App. 5-6. The complaint sought, among other things, compensatory and punitive monetary damages. It did not ask for injunctive relief, and petitioner has not sought release from custody in this action.</p>
<p>The District Court dismissed the action without prejudice, because the issues it raised "directly implicate the legality of [petitioner's] confinement," <span class="citation no-link"><i>id.,</i> at 13</span>. While petitioner's appeal to the Seventh Circuit was pending, the Indiana Supreme Court upheld his conviction and sentence on direct appeal, <i>Heck</i> v. <i>State,</i> <span class="citation" data-id="9725362"><a href="/opinion/2143528/heck-v-state/#449" aria-description="Citation for case: Heck v. State">552 N. E. 2d 446, 449</a></span> (Ind. 1990); his first petition for a writ of habeas corpus in Federal District Court was dismissed because it contained unexhausted claims; and his second federal habeas petition was denied, and the denial affirmed by the Seventh Circuit.</p>
<p>When the Seventh Circuit reached petitioner's appeal from dismissal of his § 1983 complaint, it affirmed the judgment and approved the reasoning of the District Court: "If, regardless of the relief sought, the plaintiff [in a federal civil <span class="star-pagination">*480</span> rights action] is challenging the legality of his conviction,[2] so that if he won his case the state would be obliged to release him even if he hadn't sought that relief, the suit is classified as an application for habeas corpus and the plaintiff must exhaust his state remedies, on pain of dismissal if he fails to do so." <span class="citation" data-id="610636"><a href="/opinion/610636/roy-heck-v-james-humphrey-dearborn-county-prosecutor-robert-ewbank/#357" aria-description="Citation for case: Roy Heck v. James Humphrey, Dearborn County Prosecutor,...">997 F. 2d 355, 357</a></span> (1993). Heck filed a petition for certiorari, which we granted. <span class="citation multiple-matches"><a href="/c/U.%20S./510/1068/">510 U. S. 1068</a></span> (1994).</p>
<p></p>
<h2>II</h2>
<p>This case lies at the intersection of the two most fertile sources of federal-court prisoner litigationthe Civil Rights Act of 1871, Rev. Stat. § 1979, as amended, <span class="citation no-link">42 U. S. C. § 1983</span>, and the federal habeas corpus statute, <span class="citation no-link">28 U. S. C. § 2254</span>. Both of these provide access to a federal forum for claims of unconstitutional treatment at the hands of state officials, but they differ in their scope and operation. In general, exhaustion of state remedies "is <i>not</i> a prerequisite to an action under § 1983," <i>Patsy</i> v. <i>Board of Regents of Fla.,</i> <span class="citation" data-id="9428841"><a href="/opinion/110753/patsy-v-board-of-regents-of-fla/#501" aria-description="Citation for case: Patsy v. Board of Regents of Fla.">457 U. S. 496, 501</a></span> (1982) (emphasis added), even an action by a state prisoner, <span class="citation" data-id="9428841"><a href="/opinion/110753/patsy-v-board-of-regents-of-fla/#509" aria-description="Citation for case: Patsy v. Board of Regents of Fla."><i>id.,</i> at 509</a></span>. The federal habeas corpus statute, by <span class="star-pagination">*481</span> contrast, requires that state prisoners first seek redress in a state forum.<sup>[3]</sup> See <i>Rose</i> v. <i>Lundy,</i> <span class="citation" data-id="9428690"><a href="/opinion/110662/rose-v-lundy/" aria-description="Citation for case: Rose v. Lundy">455 U. S. 509</a></span> (1982).</p>
<p><i>Preiser</i> v. <i>Rodriguez,</i> <span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">411 U. S. 475</a></span> (1973), considered the potential overlap between these two provisions, and held that habeas corpus is the exclusive remedy for a state prisoner who challenges the fact or duration of his confinement and seeks immediate or speedier release, even though such a claim may come within the literal terms of § 1983. <i>Id.,</i>  at 488-490. We emphasize that <i><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">Preiser</a></span></i> did <i>not</i> create an exception to the "no exhaustion" rule of § 1983; it merely held that certain claims by state prisoners are not <i>cognizable</i>  under that provision, and must be brought in habeas corpus proceedings, which do contain an exhaustion requirement.</p>
<p>This case is clearly not covered by the holding of <i><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">Preiser</a></span>,</i>  for petitioner seeks not immediate or speedier release, but monetary damages, as to which he could not "have sought and obtained fully effective relief through federal habeas corpus proceedings." <span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/#488" aria-description="Citation for case: Preiser v. Rodriguez"><i>Id.,</i> at 488</a></span>. See also <span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/#494" aria-description="Citation for case: Preiser v. Rodriguez"><i>id.,</i> at 494</a></span>; <i>Allen</i>  v. <i>McCurry,</i> <span class="citation" data-id="9428105"><a href="/opinion/110360/allen-v-mccurry/#104" aria-description="Citation for case: Allen v. McCurry">449 U. S. 90, 104</a></span> (1980). In dictum, however, <i><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">Preiser</a></span></i> asserted that since a state prisoner seeking only damages "is attacking something other than the fact or length of . . . confinement, and . . . is seeking something other than immediate or more speedy release[,] . . . a damages action by a state prisoner could be brought under [§ 1983] in federal court without any requirement of prior exhaustion of state remedies." <span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/#494" aria-description="Citation for case: Preiser v. Rodriguez">411 U. S., at 494</a></span>. That statement may not be true, however, when establishing the basis for the damages claim necessarily demonstrates the invalidity of the <span class="star-pagination">*482</span> conviction. In that situation, the claimant <i>can</i> be said to be "attacking . . . the fact or length of . . . confinement," bringing the suit within the other dictum of <i><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">Preiser</a></span>:</i> "Congress has determined that habeas corpus is the appropriate remedy for state prisoners attacking the validity of the fact or length of their confinement, and that specific determination must override the general terms of § 1983." <i>Id.,</i> at 490. In the last analysis, we think the dicta of <i><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">Preiser</a></span></i> to be an unreliable, if not an unintelligible, guide: that opinion had no cause to address, and did not carefully consider, the damages question before us today.</p>
<p>Before addressing that question, we respond to petitioner's contention that it has already been answered, in <i>Wolff</i>  v. <i>McDonnell,</i> <span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/" aria-description="Citation for case: Wolff v. McDonnell">418 U. S. 539</a></span> (1974). See Reply Brief for Petitioner 1. First of all, if <i><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/" aria-description="Citation for case: Wolff v. McDonnell">Wolff</a></span></i> had answered the question we would not have expressly reserved it 10 years later, as we did in <i>Tower</i> v. <i>Glover,</i> <span class="citation" data-id="9842065"><a href="/opinion/111224/tower-v-glover/" aria-description="Citation for case: Tower v. Glover">467 U. S. 914</a></span> (1984). See <span class="citation" data-id="9842065"><a href="/opinion/111224/tower-v-glover/#923" aria-description="Citation for case: Tower v. Glover"><i>id.,</i>  at 923</a></span>. And secondly, a careful reading of <i><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/" aria-description="Citation for case: Wolff v. McDonnell">Wolff</a></span></i> itself does not support the contention. Like <i>Preiser, Wolff</i> involved a challenge to the procedures used by state prison officials to deprive prisoners of good-time credits. The § 1983 complaint sought restoration of good-time credits as well as "damages for the deprivation of civil rights resulting from the use of the allegedly unconstitutional procedures." <span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#553" aria-description="Citation for case: Wolff v. McDonnell"><i>Wolff, supra,</i> at 553</a></span>. The Court said, after holding the claim for good-time credits to be foreclosed by <i><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">Preiser</a></span>,</i> that the damages claim was nonetheless "properly before the District Court and required determination of the validity of the procedures employed for imposing sanctions, including loss of good time," <span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#554" aria-description="Citation for case: Wolff v. McDonnell">418 U. S., at 554</a></span>. Petitioner contends that this language authorized the plaintiffs in <i><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/" aria-description="Citation for case: Wolff v. McDonnell">Wolff</a></span></i> to recover damages measured by the actual loss of good time. We think not. In light of the earlier language characterizing the claim as one of "damages for the deprivation of civil rights," rather than damages for the deprivation of good-time credits, we think this passage recognized a § 1983 claim for using the <span class="star-pagination">*483</span> wrong procedures, not for reaching the wrong result (<i>i. e.,</i>  denying good-time credits). Nor is there any indication in the opinion, or any reason to believe, that using the wrong procedures necessarily vitiated the denial of good-time credits. Thus, the claim at issue in <i><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/" aria-description="Citation for case: Wolff v. McDonnell">Wolff</a></span></i> did <i>not</i> call into question the lawfulness of the plaintiff's continuing confinement. See <i>Fulford</i> v. <i>Klein,</i> <span class="citation" data-id="9462432"><a href="/opinion/332456/john-fulford-v-frank-klein-etc-etc/#381" aria-description="Citation for case: John Fulford v. Frank Klein, Etc., Etc.">529 F. 2d 377, 381</a></span> (1976), adhered to, <span class="citation" data-id="9463564"><a href="/opinion/343322/john-fulford-v-frank-klein-etc-etc/" aria-description="Citation for case: John Fulford v. Frank Klein, Etc., Etc.">550 F. 2d 342</a></span> (CA5 1977) (en banc); Schwartz, The <i><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">Preiser</a></span></i>  Puzzle: Continued Frustrating Conflict Between the Civil Rights and Habeas Corpus Remedies for State Prisoners, <span class="citation no-link">37 DePaul L. Rev. 85</span>, 120-121, 145-146 (1988).</p>
<p>Thus, the question posed by § 1983 damages claims that do call into question the lawfulness of conviction or confinement remains open. To answer that question correctly, we see no need to abandon, as the Seventh Circuit and those courts in agreement with it have done, our teaching that § 1983 contains no exhaustion requirement beyond what Congress has provided. <i>Patsy,</i> <span class="citation" data-id="9428841"><a href="/opinion/110753/patsy-v-board-of-regents-of-fla/#501" aria-description="Citation for case: Patsy v. Board of Regents of Fla.">457 U. S., at 501, 509</a></span>. The issue with respect to monetary damages challenging conviction is not, it seems to us, exhaustion; but rather, the same as the issue was with respect to injunctive relief challenging conviction in <i><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">Preiser</a></span>:</i> whether the claim is cognizable under § 1983 at all. We conclude that it is not.</p>
<p>"We have repeatedly noted that <span class="citation no-link">42 U. S. C. § 1983</span> creates a species of tort liability." <i>Memphis Community School Dist.</i> v. <i>Stachura,</i> <span class="citation" data-id="9430605"><a href="/opinion/111721/memphis-community-school-district-v-stachura/#305" aria-description="Citation for case: Memphis Community School District v. Stachura">477 U. S. 299, 305</a></span> (1986) (internal quotation marks omitted). "[O]ver the centuries the common law of torts has developed a set of rules to implement the principle that a person should be compensated fairly for injuries caused by the violation of his legal rights. These rules, defining the elements of damages and the prerequisites for their recovery, provide the appropriate starting point for the inquiry under § 1983 as well." <i>Carey</i> v. <i>Piphus,</i> <span class="citation" data-id="109815"><a href="/opinion/109815/carey-v-piphus/#257" aria-description="Citation for case: Carey v. Piphus">435 U. S. 247, 257-258</a></span> (1978). Thus, to determine whether there is any bar to the present suit, we look first to the common law of torts. Cf. <span class="citation" data-id="9430605"><a href="/opinion/111721/memphis-community-school-district-v-stachura/#306" aria-description="Citation for case: Memphis Community School District v. Stachura"><i>Stachura, supra,</i> at 306</a></span>.</p>
<p><span class="star-pagination">*484</span> The common-law cause of action for malicious prosecution provides the closest analogy to claims of the type considered here because, unlike the related cause of action for false arrest or imprisonment, it permits damages for confinement imposed pursuant to legal process. "If there is a false arrest claim, damages for that claim cover the time of detention up until issuance of process or arraignment, but not more." W. Keeton, D. Dobbs, R. Keeton, &amp; D. Owen, Prosser and Keeton on Law of Torts 888 (5th ed. 1984). But a successful malicious prosecution plaintiff may recover, in addition to general damages, "compensation for any arrest or imprisonment, including damages for discomfort or injury to his health, or loss of time and deprivation of the society." <i>Id.,</i>  at 887-888 (footnotes omitted). See also <i>Roberts</i> v. <i>Thomas,</i>  <span class="citation" data-id="7137384"><a href="/opinion/7225057/roberts-v-thomas/" aria-description="Citation for case: Roberts v. Thomas">135 Ky. 63</a></span>, <span class="citation" data-id="7137384"><a href="/opinion/7225057/roberts-v-thomas/" aria-description="Citation for case: Roberts v. Thomas">121 S. W. 961</a></span> (1909).</p>
<p>One element that must be alleged and proved in a malicious prosecution action is termination of the prior criminal proceeding in favor of the accused. Prosser and Keeton, <i>supra,</i> at 874; <i>Carpenter</i> v. <i>Nutter,</i> <span class="citation" data-id="3299854"><a href="/opinion/3300830/carpenter-v-nutter/" aria-description="Citation for case: Carpenter v. Nutter">127 Cal. 61</a></span>, <span class="citation" data-id="3299854"><a href="/opinion/3300830/carpenter-v-nutter/" aria-description="Citation for case: Carpenter v. Nutter">59 P. 301</a></span> (1899). This requirement "avoids parallel litigation over the issues of probable cause and guilt . . . and it precludes the possibility of the claimant <i>[sic]</i> succeeding in the tort action after having been convicted in the underlying criminal prosecution, in contravention of a strong judicial policy against the creation of two conflicting resolutions arising out of the same or identical transaction." 8 S. Speiser, C. Krause, &amp; A. Gans, American Law of Torts § 28:5, p. 24 (1991). Furthermore, "to permit a convicted criminal defendant to proceed with a malicious prosecution claim would permit a collateral attack on the conviction through the vehicle of a civil suit." <i>Ibid.</i><sup>[4]</sup> This Court has long expressed <span class="star-pagination">*485</span> similar concerns for finality and consistency and has generally declined to expand opportunities for collateral attack, see <i>Parke</i> v. <i>Raley,</i> <span class="citation" data-id="9432696"><a href="/opinion/112793/parke-v-raley/#29" aria-description="Citation for case: Parke v. Raley">506 U. S. 20, 29-30</a></span> (1992); <i>Teague</i> v. <i>Lane,</i> <span class="citation" data-id="9431581"><a href="/opinion/112206/teague-v-lane/#308" aria-description="Citation for case: Teague v. Lane">489 U. S. 288, 308</a></span> (1989); <i>Rooker</i> v. <i>Fidelity Trust Co.,</i>  <span class="star-pagination">*486</span> <span class="citation" data-id="100309"><a href="/opinion/100309/rooker-v-fidelity-trust-co/" aria-description="Citation for case: Rooker v. Fidelity Trust Co.">263 U. S. 413</a></span> (1923); <i>Voorhees</i> v. <i>Jackson,</i> <span class="citation no-link">10 Pet. 449</span>, 472-473 (1836). We think the hoary principle that civil tort actions are not appropriate vehicles for challenging the validity of outstanding criminal judgments applies to § 1983 damages actions that necessarily require the plaintiff to prove the unlawfulness of his conviction or confinement, just as it has always applied to actions for malicious prosecution.<sup>[5]</sup></p>
<p>We hold that, in order to recover damages for allegedly unconstitutional conviction or imprisonment, or for other harm caused by actions whose unlawfulness would render a conviction or sentence invalid,<sup>[6]</sup> a § 1983 plaintiff must prove <span class="star-pagination">*487</span> that the conviction or sentence has been reversed on direct appeal, expunged by executive order, declared invalid by a state tribunal authorized to make such determination, or called into question by a federal court's issuance of a writ of habeas corpus, <span class="citation no-link">28 U. S. C. § 2254</span>. A claim for damages bearing that relationship to a conviction or sentence that has <i>not</i>  been so invalidated is not cognizable under § 1983. Thus, when a state prisoner seeks damages in a § 1983 suit, the district court must consider whether a judgment in favor of the plaintiff would necessarily imply the invalidity of his conviction or sentence; if it would, the complaint must be dismissed unless the plaintiff can demonstrate that the conviction or sentence has already been invalidated. But if the district court determines that the plaintiff's action, even if successful, will <i>not</i> demonstrate the invalidity of any outstanding criminal judgment against the plaintiff, the action should be allowed to proceed,<sup>[7]</sup> in the absence of some other bar to the suit.<sup>[8]</sup></p>
<p><span class="star-pagination">*488</span> Respondents had urged us to adopt a rule that was in one respect broader than this: Exhaustion of state remedies should be required, they contended, not just when success in the § 1983 damages suit would necessarily show a conviction or sentence to be unlawful, but whenever "judgment in a § 1983 action would resolve a necessary element to a likely challenge to a conviction, even if the § 1983 court [need] not determine that the conviction is invalid." Brief for Respondents 26, n. 10. Such a broad sweep was needed, respondents contended, lest a judgment in a prisoner's favor in a federal-court § 1983 damages action claiming, for example, a Fourth Amendment violation, be given preclusive effect as to that subissue in a subsequent state-court postconviction proceeding. Preclusion might result, they asserted, if the State exercised sufficient control over the officials' defense in the § 1983 action. See <i>Montana</i> v. <i>United States,</i> <span class="citation" data-id="9427457"><a href="/opinion/110022/montana-v-united-states/#154" aria-description="Citation for case: Montana v. United States">440 U. S. 147, 154</a></span> (1979). While we have no occasion to rule on the matter at this time, it is at least plain that preclusion will not necessarily be an automatic, or even a permissible, effect.<sup>[9]</sup></p>
<p><span class="star-pagination">*489</span> In another respect, however, our holding sweeps more broadly than the approach respondents had urged. We do not engraft an exhaustion requirement upon § 1983, but rather deny the existence of a cause of action. Even a prisoner who has fully exhausted available state remedies has no cause of action under § 1983 unless and until the conviction or sentence is reversed, expunged, invalidated, or impugned by the grant of a writ of habeas corpus. That makes it unnecessary for us to address the statute-of-limitations issue wrestled with by the Court of Appeals, which concluded that a federal doctrine of equitable tolling would apply to the § 1983 cause of action while state challenges to the conviction or sentence were being exhausted. (The court distinguished our cases holding that state, not federal, tolling provisions apply in § 1983 actions, see <i>Board of Regents of Univ. of State of N. Y.</i> v.<i>Tomanio,</i> <span class="citation" data-id="9427922"><a href="/opinion/110261/board-of-regents-of-univ-of-state-of-ny-v-tomanio/" aria-description="Citation for case: Board of Regents of Univ. of State of NY v. Tomanio">446 U. S. 478</a></span> (1980); <i>Hardin</i> v. <i>Straub,</i> <span class="citation" data-id="112265"><a href="/opinion/112265/hardin-v-straub/" aria-description="Citation for case: Hardin v. Straub">490 U. S. 536</a></span> (1989), on the ground that petitioner's claim was "in part one for habeas corpus." <span class="citation" data-id="610636"><a href="/opinion/610636/roy-heck-v-james-humphrey-dearborn-county-prosecutor-robert-ewbank/#358" aria-description="Citation for case: Roy Heck v. James Humphrey, Dearborn County Prosecutor,...">997 F. 2d, at 358</a></span>.) Under our analysis the statute of limitations poses no difficulty while the state challenges are being pursued, since the § 1983 claim has not yet arisen. Just as a cause of action for malicious prosecution does not accrue until the criminal proceedings have terminated in the plaintiff's favor, 1 C. Corman, Limitation of Actions § 7.4.1, p. 532 (1991); <i>Carnes</i> v. <i>Atkins Bros. Co.,</i> <span class="citation" data-id="7166651"><a href="/opinion/7253317/carnes-v-atkins-bros/#31" aria-description="Citation for case: Carnes v. Atkins Bros.">123 La. 26, 31</a></span>, <span class="citation" data-id="7166651"><a href="/opinion/7253317/carnes-v-atkins-bros/#574" aria-description="Citation for case: Carnes v. Atkins Bros.">48 So. 572, 574</a></span> (1909), so also a § 1983 cause of action for damages <span class="star-pagination">*490</span> attributable to an unconstitutional conviction or sentence does not accrue until the conviction or sentence has been invalidated.<sup>[10]</sup></p>
<p>Applying these principles to the present action, in which both courts below found that the damages claims challenged the legality of the conviction, we find that the dismissal of the action was correct. The judgment of the Court of Appeals for the Seventh Circuit is</p>
<blockquote>
<i>Affirmed.</i>  Justice Thomas, concurring.</blockquote>
<p>The Court and Justice Souter correctly begin their analyses with the realization that "[t]his case lies at the intersection of . . . the Civil Rights Act of 1871, Rev. Stat. § 1979, as amended, <span class="citation no-link">42 U. S. C. § 1983</span>, and the federal habeas corpus statute, <span class="citation no-link">28 U. S. C. § 2254</span>." <i>Ante,</i> at 480; <i>post,</i> at 491. One need only read the respective opinions in this case to understand <span class="star-pagination">*491</span> the difficulty of the task before the Court today. Both the Court and Justice Souter embark on a similar enterpriseharmonizing "[t]he broad language of § 1983," a "general" statute, with "the specific federal habeas corpus statute." <i>Preiser</i> v. <i>Rodriguez,</i> <span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/#489" aria-description="Citation for case: Preiser v. Rodriguez">411 U. S. 475, 489</a></span> (1973).</p>
<p>I write separately to note that it is we who have put § 1983 and the habeas statute on what Justice Souter appropriately terms a "collision course." <i>Post,</i> at 492. It has long been recognized that we have expanded the prerogative writ of habeas corpus and § 1983 far beyond the limited scope either was originally intended to have. Cf., <i>e. g., </i><i>Wright</i>  v. <i>West,</i> <span class="citation" data-id="9432630"><a href="/opinion/112771/wright-v-west/#285" aria-description="Citation for case: Wright v. West">505 U. S. 277, 285-286</a></span> (1992) (opinion of Thomas, J.) (habeas); <i>Golden State Transit Corp.</i> v. <i>Los Angeles,</i> <span class="citation" data-id="9431857"><a href="/opinion/112341/golden-state-transit-corp-v-city-of-los-angeles/#117" aria-description="Citation for case: Golden State Transit Corp. v. City of Los Angeles">493 U. S. 103, 117</a></span> (1989) (Kennedy, J., dissenting) (§ 1983). Expanding the two historic statutes brought them squarely into conflict in the context of suits by state prisoners, as we made clear in <i><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">Preiser</a></span>.</i> </p>
<p>Given that the Court created the tension between the two statutes, it is proper for the Court to devise limitations aimed at ameliorating the conflict, provided that it does so in a principled fashion. Cf. <i>Malley</i> v. <i>Briggs,</i> <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#342" aria-description="Citation for case: Malley v. Briggs">475 U. S. 335, 342</a></span> (1986). Because the Court today limits the scope of § 1983 in a manner consistent both with the federalism concerns undergirding the explicit exhaustion requirement of the habeas statute, <i>ante,</i> at 483, and with the state of the common law at the time § 1983 was enacted, <i>ante,</i> at 484-486, and n. 4, I join the Court's opinion.</p>
<p>Justice Souter, with whom Justice Blackmun, Justice Stevens, and Justice O'Connor join, concurring in the judgment.</p>
<p>The Court begins its analysis as I would, by observing that "[t]his case lies at the intersection of the two most fertile sources of federal-court prisoner litigationthe Civil Rights Act of 1871, . . . <span class="citation no-link">42 U. S. C. § 1983</span>, and the federal habeas corpus statute, <span class="citation no-link">28 U. S. C. § 2254</span>," two statutes that <span class="star-pagination">*492</span> "provide access to a federal forum for claims of unconstitutional treatment at the hands of state officials," while "differ[ing] in their scope and operation." <i>Ante,</i> at 480. But instead of analyzing the statutes to determine which should yield to the other at this intersection, the Court appears to take the position that the statutes were never on a collision course in the first place because, like the common-law tort of malicious prosecution, § 1983 requires (and, presumably, has always required) plaintiffs seeking damages for unconstitutional conviction or confinement to show the favorable termination of the underlying proceeding. See <i>ante,</i> at 484-487.</p>
<p>While I do not object to referring to the common law when resolving the question this case presents, I do not think that the existence of the tort of malicious prosecution alone provides the answer. Common-law tort rules can provide a "starting point for the inquiry under § 1983," <i>Carey</i> v. <i>Piphus,</i> <span class="citation" data-id="109815"><a href="/opinion/109815/carey-v-piphus/#258" aria-description="Citation for case: Carey v. Piphus">435 U. S. 247, 258</a></span> (1978), but we have relied on the common law in § 1983 cases only when doing so was thought to be consistent with ordinary rules of statutory construction, as when common-law principles have textual support in other provisions of the Civil Rights Act of 1871, see, <i>e. g., id.,</i>  at 255-256 (damages under § 1983), or when those principles were so fundamental and widely understood at the time § 1983 was enacted that the 42d Congress could not be presumed to have abrogated them silently, see, <i>e. g., </i><i>Tenney</i> v. <i>Brandhove,</i> <span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/#376" aria-description="Citation for case: Tenney v. Brandhove">341 U. S. 367, 376</a></span> (1951) (immunity under § 1983); <i>Pierson</i> v. <i>Ray,</i> <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#553" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547, 553-554</a></span> (1967) (same). At the same time, we have consistently refused to allow commonlaw analogies to displace statutory analysis, declining to import even well-settled common-law rules into § 1983 "if [the statute's] history or purpose counsel against applying [such rules] in § 1983 actions." <i>Wyatt</i> v. <i>Cole,</i> <span class="citation" data-id="9432538"><a href="/opinion/112733/wyatt-v-cole/#164" aria-description="Citation for case: Wyatt v. Cole">504 U. S. 158, 164</a></span> (1992); see also <i>Tower</i> v. <i>Glover,</i> <span class="citation" data-id="9842065"><a href="/opinion/111224/tower-v-glover/#920" aria-description="Citation for case: Tower v. Glover">467 U. S. 914, 920-921</a></span> (1984). Cf. <i>Anderson</i> v. <i>Creighton,</i> <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#645" aria-description="Citation for case: Anderson v. Creighton">483 U. S. 635, 645</a></span> (1987) ("[W]e have never suggested that the precise contours of official immunity <span class="star-pagination">*493</span> [under § 1983] can and should be slavishly derived from the often arcane rules of the common law").<sup>[1]</sup></p>
<p>An examination of common-law sources arguably relevant in this case confirms the soundness of our hierarchy of principles for resolving questions concerning § 1983. If the common law were not merely a "starting point" for the analysis under § 1983, but its destination, then (unless we were to have some authority to choose common-law requirements we like and discard the others) principle would compel us to accept as elements of the § 1983 cause of action not only the malicious-prosecution tort's favorable-termination requirement, but other elements of the tort that cannot coherently be transplanted. In addition to proving favorable termination, <span class="star-pagination">*494</span> a plaintiff in a malicious-prosecution action, according to the same sources the Court relies upon, must prove the "[a]bsence of probable cause for the proceeding" as well as "`[m]alice,' or a primary purpose other than that of bringing an offender to justice." W. Keeton, D. Dobbs, R. Keeton, &amp; D. Owen, Prosser and Keeton on Law of Torts 871 (5th ed. 1984) (hereinafter Prosser and Keeton); see also 8 S. Speiser, C. Krause, &amp; A. Gans, American Law of Torts § 28:7, p. 38, § 28:11, p. 61 (1991). As § 1983 requirements, however, these elements would mean that even a § 1983 plaintiff whose conviction was invalidated as unconstitutional (premised, for example, on a confession coerced by an interrogation-room beating) could not obtain damages for the unconstitutional conviction and ensuing confinement if the defendant police officials (or perhaps the prosecutor) had probable cause to believe the plaintiff was guilty and intended to bring him to justice. Absent an independent statutory basis for doing so, importing into § 1983 the malicious-prosecution tort's favorable-termination requirement but not its probablecause requirement would be particularly odd since it is from the latter that the former derives. See Prosser and Keeton 874 ("The requirement that the criminal prosecution terminate in favor of the malicious prosecution plaintiff . . . is primarily important not as an independent element of the malicious prosecution action but only for what it shows about probable cause or guilt-in-fact"); M. Bigelow, Leading Cases on Law of Torts 196 (1875) ("The action for a malicious prosecution cannot be maintained until the prosecution has terminated; for otherwise the plaintiff might obtain judgment in the one case and yet be convicted in the other, which would of course disprove the averment of a want of probable cause").</p>
<p>If, in addition, the common law were the master of statutory analysis, not the servant (to switch metaphors), we would find ourselves with two masters to contend with here, for we would be subject not only to the tort of malicious <span class="star-pagination">*495</span> prosecution but to the tort of abuse of process as well, see <i>Wyatt</i> v. <span class="citation" data-id="9432538"><a href="/opinion/112733/wyatt-v-cole/#164" aria-description="Citation for case: Wyatt v. Cole"><i>Cole, supra,</i> at 164</a></span> (calling these two actions "the most closely analogous torts" to § 1983), the latter making it "unnecessary for the plaintiff to prove that the proceeding has terminated in his favor," Prosser and Keeton 897. The Court suggests that the tort of malicious prosecution provides "the closest analogy to claims of the type considered here" because "it permits damages for confinement imposed pursuant to legal process." <i>Ante,</i> at 484. But the same appears to be true for the tort of abuse of process. See Restatement (Second) of Torts § 682, Illustration 1 (1977) (indicating that a person who, by causing a court to issue a writ of capias against someone to whom he lent money, caused the borrower to be "arrested . . . and kept in prison" is properly held liable for the arrest and imprisonment if the lender's purpose in using legal process was wrongful (and regardless of favorable termination or want of probable cause)).<sup>[2]</sup></p>
<p>Furthermore, even if the tort of malicious prosecution were today marginally more analogous than other torts to the type of § 1983 claim in the class of cases before us (because it alone may permit damages for unlawful conviction or postconviction confinement, see n. 3, <i>infra</i> ), the Court overlooks a significant historical incongruity that calls into question the utility of the analogy to the tort of malicious <span class="star-pagination">*496</span> prosecution insofar as it is used exclusively to determine the scope of § 1983: the damages sought in the type of § 1983 claim involved here, damages for unlawful conviction or postconviction confinement, were not available at all in an action for malicious prosecution at the time of § 1983's enactment. A defendant's conviction, under Reconstruction-era common law, dissolved his claim for malicious prosecution because the conviction was regarded as irrebuttable evidence that the prosecution never lacked probable cause. See T. Cooley, Law of Torts 185 (1879) ("If the defendant is convicted in the first instance and appeals, and is acquitted in the appellate court, the conviction below is conclusive of probable cause"). Thus the definition of "favorable termination" with which the framers of § 1983 were aware (if they were aware of any definition) included none of the events relevant to the type of § 1983 claim involved in this case ("revers[al] on direct appeal, expunge[ment] by executive order, [a] declar[ation] [of] invalid[ity] by a state tribunal authorized to make such determination, or [the] call[ing] into question by a federal court's issuance of a writ of habeas corpus," <i>ante,</i> at 487), and it is easy to see why the analogy to the tort of malicious prosecution in this context has escaped the collective wisdom of the many courts and commentators to have addressed the issue previously, as well as the parties to this case. Indeed, relying on the tort of malicious prosecution to dictate the outcome of this case would logically drive one to the position, untenable as a matter of statutory interpretation (and, to be clear, disclaimed by the Court), that conviction of a crime wipes out a person's § 1983 claim for damages for unconstitutional conviction or postconviction confinement.<sup>[3]</sup></p>
<p><span class="star-pagination">*497</span> We are not, however, in any such strait, for our enquiry in this case may follow the interpretive methodology employed in <i>Preiser</i> v. <i>Rodriguez,</i> <span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">411 U. S. 475</a></span> (1973) (a methodology uniformly applied by the Courts of Appeals in analyzing analogous cases, see, <i>e. g., </i><i>Young</i> v. <i>Kenny,</i> <span class="citation" data-id="8981393"><a href="/opinion/8989269/young-v-kenny/#875" aria-description="Citation for case: Young v. Kenny">907 F. 2d 874, 875-876</a></span> (CA9 1990)). In <i><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">Preiser</a></span>,</i> we read the "general" § 1983 statute in light of the "specific federal habeas corpus statute," which applies only to "person[s] in custody," <span class="citation no-link">28 U. S. C. § 2254</span>(a), and the habeas statute's policy, embodied in its exhaustion requirement, § 2254(b), that state courts be given the first opportunity to review constitutional claims bearing upon a state prisoner's release from custody. <span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/#489" aria-description="Citation for case: Preiser v. Rodriguez">411 U. S., at 489</a></span>. Though in contrast to <i><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">Preiser</a></span></i> the state prisoner here seeks damages, not release from custody, the distinction makes no difference when the damages sought are for unconstitutional conviction or confinement. (As the Court explains, nothing in <i><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">Preiser</a></span></i> nor in <i>Wolff</i> v. <i>McDonnell,</i> <span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/" aria-description="Citation for case: Wolff v. McDonnell">418 U. S. 539</a></span> (1974), is properly read as holding that the relief sought in a § 1983 action dictates whether a state prisoner can proceed immediately to federal court. See <i>ante,</i>  <span class="star-pagination">*498</span> at 481-483.) Whether or not a federal-court § 1983 damages judgment against state officials in such an action would have preclusive effect in later litigation against the State, mounting damages against the defendant-officials for unlawful confinement (damages almost certainly to be paid by state indemnification) would, practically, compel the State to release the prisoner. Because allowing a state prisoner to proceed directly with a federal-court § 1983 attack on his conviction or sentence "would wholly frustrate explicit congressional intent" as declared in the habeas exhaustion requirement, <i>Preiser,</i> <span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/#489" aria-description="Citation for case: Preiser v. Rodriguez">411 U. S., at 489</a></span>, the statutory scheme must be read as precluding such attacks. This conclusion flows not from a preference about how the habeas and § 1983 statutes ought to have been written, but from a recognition that "Congress has determined that habeas corpus is the appropriate remedy for state prisoners attacking the validity of the fact or length of their confinement, [a] specific determination [that] must override the general terms of § 1983." <i>Id.,</i> at 490.</p>
<p>That leaves the question of how to implement what statutory analysis requires. It is at this point that the maliciousprosecution tort's favorable-termination requirement becomes helpful, not in dictating the elements of a § 1983 cause of action, but in suggesting a relatively simple way to avoid collisions at the intersection of habeas and § 1983. A state prisoner may seek federal-court § 1983 damages for unconstitutional conviction or confinement, but only if he has previously established the unlawfulness of his conviction or confinement, as on appeal or on habeas. This has the effect of requiring a state prisoner challenging the lawfulness of his confinement to follow habeas's rules before seeking § 1983 damages for unlawful confinement in federal court, and it is ultimately the Court's holding today. It neatly resolves a problem that has bedeviled lower courts, see <span class="citation" data-id="610636"><a href="/opinion/610636/roy-heck-v-james-humphrey-dearborn-county-prosecutor-robert-ewbank/#357" aria-description="Citation for case: Roy Heck v. James Humphrey, Dearborn County Prosecutor,...">997 F. 2d 355, 357-358</a></span> (CA7 1993) (decision below); <i>Young</i> v. <span class="citation" data-id="8981393"><a href="/opinion/8989269/young-v-kenny/#877" aria-description="Citation for case: Young v. Kenny"><i>Kenny, supra,</i>  at 877</a></span> (discussing cases), legal commentators, see Schwartz, The <i><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">Preiser</a></span></i> Puzzle, <span class="citation no-link">37 DePaul L. Rev. 85</span>, 86-87, n. 6 (1988) <span class="star-pagination">*499</span> (listing articles), and law students (some of whom doubtless have run up against a case like this in law-school exams). The favorable-termination requirement avoids the knotty statute-of-limitations problem that arises if federal courts dismiss § 1983 suits filed before an inmate pursues federal habeas, and (because the statute-of-limitations clock does not start ticking until an inmate's conviction is set aside) it does so without requiring federal courts to stay, and therefore to retain on their dockets, prematurely filed § 1983 suits. See <i>ante,</i> at 489.<sup>[4]</sup></p>
<p>It may be that the Court's analysis takes it no further than I would thus go, and that any objection I may have to the Court's opinion is to style, not substance. The Court acknowledges the habeas exhaustion requirement and explains that it is the reason that the habeas statute "intersect[s]" <span class="star-pagination">*500</span> in this case with § 1983, which does not require exhaustion, see <i>ante,</i> at 480; it describes the issue it faces as "the same" as that in <i>Preiser, ante,</i> at 483; it recites the principle that common-law tort rules "`provide the appropriate starting point for the inquiry under § 1983,' " <i>ibid.</i> (quoting <i>Carey</i> v. <i>Piphus,</i> <span class="citation" data-id="109815"><a href="/opinion/109815/carey-v-piphus/#257" aria-description="Citation for case: Carey v. Piphus">435 U. S., at 257-258</a></span>); and it does not transpose onto § 1983 elements of the malicious-prosecution tort that are incompatible with the policies of § 1983 and the habeas statute as relevant to claims by state prisoners. The Court's opinion can be read as saying nothing more than that now, after enactment of the habeas statute and because of it, prison inmates seeking § 1983 damages in federal court for unconstitutional conviction or confinement must satisfy a requirement analogous to the malicious-prosecution tort's favorable-termination requirement. Cf. <i>ante,</i> at 491 (Thomas, J., concurring).</p>
<p>That would be a sensible way to read the opinion, in part because the alternative would needlessly place at risk the rights of those outside the intersection of § 1983 and the habeas statute, individuals not "in custody" for habeas purposes. If these individuals (people who were merely fined, for example, or who have completed short terms of imprisonment, probation, or parole, or who discover (through no fault of their own) a constitutional violation after full expiration of their sentences), like state prisoners, were required to show the prior invalidation of their convictions or sentences in order to obtain § 1983 damages for unconstitutional conviction or imprisonment, the result would be to deny any federal forum for claiming a deprivation of federal rights to those who cannot first obtain a favorable state ruling. The reason, of course, is that individuals not "in custody" cannot invoke federal habeas jurisdiction, the only statutory mechanism besides § 1983 by which individuals may sue state officials in federal court for violating federal rights. That would be an untoward result.</p>
<p><span class="star-pagination">*501</span> It is one thing to adopt a rule that forces prison inmates to follow the federal habeas route with claims that fall within the plain language of § 1983 when that is necessary to prevent a requirement of the habeas statute from being undermined. That is what the Court did in <i>Preiser</i> v. <i>Rodriguez,</i>  <span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/#489" aria-description="Citation for case: Preiser v. Rodriguez">411 U. S., at 489-492</a></span>, and that is what the Court's rule would do for state prisoners. Harmonizing § 1983 and the habeas statute by requiring a state prisoner seeking damages for unconstitutional conviction to establish the previous invalidation of his conviction does not run afoul of what we have called, repeatedly, "[t]he very purpose of" § 1983: "to interpose the federal courts between the States and the people, as guardians of the people's federal rights." <i>Mitchum</i> v. <i>Foster,</i> <span class="citation" data-id="8980660"><a href="/opinion/8988576/mitchum-v-foster/#242" aria-description="Citation for case: Mitchum v. Foster">407 U. S. 225, 242</a></span> (1972); see also <i>Pulliam</i> v. <i>Allen,</i>  <span class="citation" data-id="9429586"><a href="/opinion/111166/pulliam-v-allen/#541" aria-description="Citation for case: Pulliam v. Allen">466 U. S. 522, 541</a></span> (1984); <i>Patsy</i> v. <i>Board of Regents of Fla.,</i>  <span class="citation" data-id="9428841"><a href="/opinion/110753/patsy-v-board-of-regents-of-fla/#503" aria-description="Citation for case: Patsy v. Board of Regents of Fla.">457 U. S. 496, 503</a></span> (1982). A prisoner caught at the intersection of § 1983 and the habeas statute can still have his attack on the lawfulness of his conviction or confinement heard in federal court, albeit one sitting as a habeas court; and, depending on the circumstances, he may be able to obtain § 1983 damages.</p>
<p>It would be an entirely different matter, however, to shut off federal courts altogether to claims that fall within the plain language of § 1983. "[I]rrespective of the common law support" for a general rule disfavoring collateral attacks, the Court lacks the authority to do any such thing absent unambiguous congressional direction where, as here, reading § 1983 to exclude claims from federal court would run counter to "§ 1983's history" and defeat the statute's "purpose." <i>Wyatt</i> v. <i>Cole,</i> <span class="citation" data-id="9432538"><a href="/opinion/112733/wyatt-v-cole/#158" aria-description="Citation for case: Wyatt v. Cole">504 U. S., at 158</a></span>. Consider the case of a former slave framed by Ku Klux Klan-controlled lawenforcement officers and convicted by a Klan-controlled state court of, for example, raping a white woman; and suppose that the unjustly convicted defendant did not (and could not) discover the proof of unconstitutionality until after his <span class="star-pagination">*502</span> release from state custody. If it were correct to say that § 1983 independently requires a person not in custody to establish the prior invalidation of his conviction, it would have been equally right to tell the former slave that he could not seek federal relief even against the law-enforcement officers who framed him unless he first managed to convince the state courts that his conviction was unlawful. That would be a result hard indeed to reconcile either with the purpose of § 1983 or with the origins of what was "popularly known as the Ku Klux Act," <i>Collins</i> v. <i>Hardyman,</i> <span class="citation" data-id="9420619"><a href="/opinion/104918/collins-v-hardyman/#657" aria-description="Citation for case: Collins v. Hardyman">341 U. S. 651, 657</a></span> (1951), the statute having been enacted in part out of concern that many state courts were "in league with those who were bent upon abrogation of federally protected rights," <i>Mitchum</i> v. <span class="citation" data-id="8980660"><a href="/opinion/8988576/mitchum-v-foster/#240" aria-description="Citation for case: Mitchum v. Foster"><i>Foster, supra,</i> at 240</a></span>; cf. Cong. Globe, 42d Cong., 1st Sess., 577 (1871) (Sen. Trumbull explaining that, under the Civil Rights Act of 1871, "the Federal Government has a right to set aside . . . action of the State authorities" that deprives a person of his Fourteenth Amendment rights). It would also be a result unjustified by the habeas statute or any other post-§ 1983 enactment.</p>
<p>Nor do I see any policy reflected in a congressional enactment that would justify denying to an individual today federal damages (a significantly less disruptive remedy than an order compelling release from custody) merely because he was unconstitutionally fined by a State, or to a person who discovers after his release from prison that, for example, state officials deliberately withheld exculpatory material. And absent such a statutory policy, surely the common law can give us no authority to narrow the "broad language" of § 1983, which speaks of deprivations of "any" constitutional rights, privileges, or immunities, by "[e]very" person acting under color of state law, and to which "we have given full effect [by] recognizing that § 1983 `provide[s] a remedy, to be broadly construed, against all forms of official violation of federally protected rights.' " <i>Dennis</i> v. <i>Higgins,</i> <span class="citation" data-id="9432192"><a href="/opinion/112534/dennis-v-higgins/#443" aria-description="Citation for case: Dennis v. Higgins">498 U. S. 439, 443, 445</a></span> (1991) (quoting <i>Monell</i> v. <i>New York City Dept. of Social Servs.,</i> <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#700" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658, 700-701</a></span> (1978)).</p>
<p><span class="star-pagination">*503</span> In sum, while the malicious-prosecution analogy provides a useful mechanism for implementing what statutory analysis requires, congressional policy as reflected in enacted statutes must ultimately be the guide. I would thus be clear that the proper resolution of this case (involving, of course, a state prisoner) is to construe § 1983 in light of the habeas statute and its explicit policy of exhaustion. I would not cast doubt on the ability of an individual unaffected by the habeas statute to take advantage of the broad reach of § 1983.</p>
<h2>NOTES</h2>
<p>[*]   A briefof <i>amici curiae</i> was filed for the State of Arizona et al.by <i>Grant Woods,</i> Attorney General of Arizona, <i>Paul J. McMurdie,</i> and <i>Linda L. Knowles,</i> and by the Attorneys General for their respective States as follows: <i>James H. Evans</i> of Alabama, <i>Winston Bryant</i> of Arkansas, <i>Daniel E. Lungren</i> of California,<i>Robert A. Butter worth</i> of Florida,<i>Larry EchoHawk</i> of Idaho, <i>Roland W. Burris</i> of Illinois, <i>Chris Gorman</i> of Kentucky,<i>Michael C. Moore</i> of Mississippi, <i>Joseph T. Mazurek</i> of Montana, <i>Frankie Sue Del Papa</i> of Nevada, <i>Deborah T. Poritz</i> of New Jersey, <i>Lee Fisher</i> of Ohio, <i>T. Travis Medlock</i> of South Carolina, <i>Mark W. Barnett</i> of South Dakota, <i>Dan Morales</i> of Texas, <i>Jan Graham</i> of Utah, and <i>Joseph B. Meyer</i> of Wyoming.</p>
<p>[1]  Section 1983 provides: "Every person who, under color of any statute, ordinance, regulation, custom, or usage, of any State or Territory or the District of Columbia, subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress."</p>
<p>[3]  Neither in his petition for certiorari nor in his principal brief on the merits did petitioner contest the description of his monetary claims (by both the District Court and the Court of Appeals) as challenging the legality of his conviction. Thus, the question we understood to be before us was whether money damages premised on an unlawful conviction could be pursued under § 1983. Petitioner sought to challenge this premise in his reply brief, contending that findings validating his damages claims would not invalidate his conviction. See Reply Brief for Petitioner 5-6. That argument comes too late. We did not take this case to review such a fact-bound issue, and we accept the characterization of the lower courts.
</p>
<p>We also decline to pursue, without implying the nonexistence of, another issue, suggested by the Court of Appeals' statement that, if petitioner's "conviction were proper, this suit would in all likelihood be barred by res judicata." <span class="citation" data-id="610636"><a href="/opinion/610636/roy-heck-v-james-humphrey-dearborn-county-prosecutor-robert-ewbank/#357" aria-description="Citation for case: Roy Heck v. James Humphrey, Dearborn County Prosecutor,...">997 F. 2d 355, 357</a></span> (CA7 1993). The res judicata effect of state-court decisions in § 1983 actions is a matter of state law. See <i>Migra</i>  v. <i>Warren City School Dist. Bd. of Ed.,</i> <span class="citation" data-id="9429481"><a href="/opinion/111093/migra-v-warren-city-school-district-board-of-education/" aria-description="Citation for case: Migra v. Warren City School District Board of Education">465 U. S. 75</a></span> (1984).</p>
<p>[4]  Title <span class="citation no-link">28 U. S. C. § 2254</span>(b) provides: "An application for a writ of habeas corpus in behalf of a person in custody pursuant to the judgment of a State court shall not be granted unless it appears that the applicant has exhausted the remedies available in the courts of the State, or that there is either an absence of available State corrective process or the existence of circumstances rendering such process ineffective to protect the rights of the prisoner."</p>
<p>[5]  Justice Souter criticizes our reliance on malicious prosecution's favorable termination requirement as illustrative of the common-law principle barring tort plaintiffs from mounting collateral attacks on their outstanding criminal convictions. Malicious prosecution is an inapt analogy, he says, because "[a] defendant's conviction, under Reconstruction-era common law, dissolved his claim for malicious prosecution because the conviction was regarded as irrebuttable evidence that the prosecution never lacked probable cause." <i>Post,</i> at 496, citing T. Cooley, Law of Torts 185 (1879). Chief Justice Cooley no doubt intended merely to set forth the general rule that a conviction defeated the malicious prosecution plaintiff's allegation (essential to his cause of action) that the prior proceeding was without probable cause. But this was not an absolute rule in all jurisdictions, see <i>Goodrich</i> v. <i>Warner,</i> <span class="citation" data-id="6576514"><a href="/opinion/6696530/goodrich-v-warner/#443" aria-description="Citation for case: Goodrich v. Warner">21 Conn. 432, 443</a></span> (1852); <i>Richter</i> v. <i>Koster,</i>  <span class="citation" data-id="7039978"><a href="/opinion/7132515/richter-v-koster/#441" aria-description="Citation for case: Richter v. Koster">45 Ind. 440, 441-442</a></span> (1874), and early on it was recognized that there must be exceptions to the rule in cases involving circumstances such as fraud, perjury, or mistake of law, see <i>Burt</i> v. <i>Place,</i> <span class="citation" data-id="5513412"><a href="/opinion/5666432/burt-v-place/" aria-description="Citation for case: Burt v. Place">4 Wend. 591</a></span> (N. Y. 1830); <i>Witham</i> v. <i>Gowen,</i> <span class="citation" data-id="4926796"><a href="/opinion/5108289/witham-v-gowen/" aria-description="Citation for case: Witham v. Gowen">14 Me. 362</a></span> (1837); <i>Olson</i> v. <i>Neal,</i> <span class="citation" data-id="7100901"><a href="/opinion/7189983/olson-v-neal/" aria-description="Citation for case: Olson v. Neal">63 Iowa 214</a></span>, <span class="citation" data-id="7100901"><a href="/opinion/7189983/olson-v-neal/" aria-description="Citation for case: Olson v. Neal">18 N. W. 863</a></span> (1884). Some cases even held that a "conviction, although it be afterwards reversed, is <i>prima facie</i> evidenceand that onlyof the existence of probable cause." <i>Neher</i> v. <i>Dobbs,</i> <span class="citation" data-id="6649345"><a href="/opinion/6766565/erb-v-eggleston/#868" aria-description="Citation for case: Erb v. Eggleston">41 Neb. 863, 868</a></span>, <span class="citation" data-id="6650357"><a href="/opinion/6767569/nehr-v-dobbs/#865" aria-description="Citation for case: Nehr v. Dobbs">66 N. W. 864, 865</a></span> (1896) (collecting cases). In <i>Crescent City Live Stock Co.</i> v. <i>Butchers' Union Slaughter-House Co.,</i> <span class="citation" data-id="91832"><a href="/opinion/91832/crescent-city-live-stock-co-v-batchers-union-slaughter-house-co/" aria-description="Citation for case: Crescent City Live Stock Co. v. Batchers&#x27; Union...">120 U. S. 141</a></span> (1887), we recognized that "[h]ow much weight as proof of probable cause shall be attributed to the judgment of the court in the original action, when subsequently reversed for error, may admit of some question." <span class="citation" data-id="91832"><a href="/opinion/91832/crescent-city-live-stock-co-v-batchers-union-slaughter-house-co/#149" aria-description="Citation for case: Crescent City Live Stock Co. v. Batchers&#x27; Union..."><i>Id.,</i> at 149</a></span>. We attempted to "reconcile the apparent contradiction in the authorities," <span class="citation" data-id="91832"><a href="/opinion/91832/crescent-city-live-stock-co-v-batchers-union-slaughter-house-co/#151" aria-description="Citation for case: Crescent City Live Stock Co. v. Batchers&#x27; Union..."><i>id.,</i> at 151</a></span>, by observing that the presumption of probable cause arising from a conviction can be rebutted only by showing that the conviction had been obtained by some type of fraud, <i><span class="citation" data-id="91832"><a href="/opinion/91832/crescent-city-live-stock-co-v-batchers-union-slaughter-house-co/" aria-description="Citation for case: Crescent City Live Stock Co. v. Batchers&#x27; Union...">ibid.</a></span></i> Although we ultimately held for the malicious prosecution defendant, our discussion in that case well establishes that the absolute rule Justice Souter contends for did not exist.
</p>
<p>Yet even if Justice Souter were correct in asserting that a prior conviction, although reversed, "dissolved [a] claim for malicious prosecution," <i>post,</i> at 496, our analysis would be unaffected. It would simply demonstrate that <i>no</i> common-law action, <i>not even</i> malicious prosecution, would permit a criminal proceeding to be impugned in a tort action, <i>even after</i>  the conviction had been reversed. That would, if anything, strengthen our belief that § 1983, which borrowed general tort principles, was not meant to permit such collateral attack.</p>
<p>[6]  Justice Souter's discussion of abuse of process, <i>post,</i> at 494-495, does not undermine this principle. It is true that favorable termination of prior proceedings is not an element of that cause of actionbut neither is an impugning of those proceedings one of its consequences. The gravamen of that tort is not the wrongfulness of the prosecution, but some extortionate perversion of lawfully initiated process to illegitimate ends. See, <i>e. g., </i><i>Donohoe Const. Co.</i> v. <i>Mount Vernon Associates,</i> <span class="citation" data-id="1379591"><a href="/opinion/1379591/donohoe-construction-co-v-mount-vernon-associates/#539" aria-description="Citation for case: Donohoe Construction Co. v. Mount Vernon Associates">235 Va. 531, 539-540</a></span>, <span class="citation" data-id="1379591"><a href="/opinion/1379591/donohoe-construction-co-v-mount-vernon-associates/#862" aria-description="Citation for case: Donohoe Construction Co. v. Mount Vernon Associates">369 S. E. 2d 857, 862</a></span> (1988); see also 8 S. Speiser, C. Krause, &amp; A. Gans, American Law of Torts §§ 28:32-28:34 (1991). Cognizable injury for abuse of process is limited to the harm caused by the misuse of process, and does not include harm (such as conviction and confinement) resulting from that process's being carried through to its lawful conclusion. Thus, one could no more seek compensatory damages for an outstanding criminal conviction in an action for abuse of process than in one for malicious prosecution. This limitation is illustrated by <i>McGann</i> v. <i>Allen,</i> <span class="citation" data-id="3319371"><a href="/opinion/3324074/mcgann-v-allen/#191" aria-description="Citation for case: McGann v. Allen">105 Conn. 177, 191</a></span>, <span class="citation" data-id="3319371"><a href="/opinion/3324074/mcgann-v-allen/#815" aria-description="Citation for case: McGann v. Allen">134 A. 810, 815</a></span> (1926), where the court held that expenses incurred by the plaintiff in defending herself against crimes charged against her were not compensable in a suit for abuse of process, since "[d]amage[s] for abuse of process must be confined to the damage flowing from such abuse, and be confined to the period of time involved in taking plaintiff, after her arrest, to [defendant's] store, and the detention there."</p>
<p>[7]  An example of this latter categorya § 1983 action that does not seek damages directly attributable to conviction or confinement but whose successful prosecution would necessarily imply that the plaintiff's criminal conviction was wrongfulwould be the following: A state defendant is convicted of and sentenced for the crime of resisting arrest, defined as intentionally preventing a peace officer from effecting a <i>lawful</i> arrest. (This is a common definition of that offense. See <i>People</i> v. <i>Peacock,</i> 68 N. Y. 2d 675, <span class="citation" data-id="5537625"><a href="/opinion/5688443/people-v-peacock/" aria-description="Citation for case: People v. Peacock">496 N. E. 2d 683</a></span> (1986); 4 C. Torcia, Wharton's Criminal Law § 593, p. 307 (14th ed. 1981).) He then brings a § 1983 action against the arresting officer, seeking damages for violation of his Fourth Amendment right to be free from unreasonable seizures. In order to prevail in this § 1983 action, he would have to negate an element of the offense of which he has been convicted. Regardless of the state law concerning res judicata, see n. 2, <i>supra,</i> the § 1983 action will not lie.</p>
<p>[8]  For example, a suit for damages attributable to an allegedly unreasonable search may lie even if the challenged search produced evidence that was introduced in a state criminal trial resulting in the § 1983 plaintiff's still-outstanding conviction. Because of doctrines like independent source and inevitable discovery, see <i>Murray</i> v. <i>United States,</i> <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#539" aria-description="Citation for case: Murray v. United States">487 U. S. 533, 539</a></span> (1988), and especially harmless error, see <i>Arizona</i> v. <i>Fulminante,</i>  <span class="citation" data-id="9432240"><a href="/opinion/112566/arizona-v-fulminante/#307" aria-description="Citation for case: Arizona v. Fulminante">499 U. S. 279, 307-308</a></span> (1991), such a § 1983 action, even if successful, would not <i>necessarily</i> imply that the plaintiff's conviction was unlawful. In order to recover compensatory damages, however, the § 1983 plaintiff must prove not only that the search was unlawful, but that it caused him actual, compensable injury, see <i>Memphis Community School Dist.</i> v. <i>Stachura,</i>  <span class="citation" data-id="9430605"><a href="/opinion/111721/memphis-community-school-district-v-stachura/#308" aria-description="Citation for case: Memphis Community School District v. Stachura">477 U. S. 299, 308</a></span> (1986), which, we hold today, does <i>not</i> encompass the "injury" of being convicted and imprisoned (until his conviction has been overturned).</p>
<p>[9]  For example, if a state criminal defendant brings a federal civil-rights lawsuit during the pendency of his criminal trial, appeal, or state habeas action, abstention may be an appropriate response to the parallel state-court proceedings. See <i>Colorado River Water Conservation Dist.</i>  v. <i>United States,</i> <span class="citation" data-id="9426321"><a href="/opinion/109405/colorado-river-water-conservation-district-v-united-states/" aria-description="Citation for case: Colorado River Water Conservation District v. United States">424 U. S. 800</a></span> (1976).
</p>
<p>Moreover, we do not decide whether abstention might be appropriate in cases where a state prisoner brings a § 1983 damages suit raising an issue that also could be grounds for relief in a state-court challenge to his conviction or sentence. Cf. <i>Tower</i> v. <i>Glover,</i> <span class="citation" data-id="9842065"><a href="/opinion/111224/tower-v-glover/#923" aria-description="Citation for case: Tower v. Glover">467 U. S. 914, 923</a></span> (1984).</p>
<p>[10]  State courts are bound to apply federal rules in determining the preclusive effect of federal-court decisions on issues of federal law. See P. Bator, D. Meltzer, P. Mishkin, &amp; D. Shapiro, Hart and Wechsler's The Federal Courts and the Federal System 1604 (3d ed. 1988) ("It is clear that where the federal court decided a federal question, federal res judicata rules govern"); <i>Deposit Bank</i> v. <i>Frankfort,</i> <span class="citation" data-id="95964"><a href="/opinion/95964/deposit-bank-v-frankfort/#514" aria-description="Citation for case: Deposit Bank v. Frankfort">191 U. S. 499, 514-518</a></span> (1903); <i>Stoll</i> v. <i>Gottlieb,</i> <span class="citation" data-id="103096"><a href="/opinion/103096/stoll-v-gottlieb/#170" aria-description="Citation for case: Stoll v. Gottlieb">305 U. S. 165, 170-171, 174-175</a></span> (1938). The federal rules on the subject of issue and claim preclusion, unlike those relating to exhaustion of state remedies, are "almost entirely judge-made." Hart &amp; Wechsler's, <i>supra,</i> at 1598; see also Burbank, Interjurisdictional Preclusion, Full Faith and Credit and Federal Common Law: A General Approach, <span class="citation no-link">71 Cornell L. Rev. 733</span>, 747-778 (1986). And in developing them the courts can, and indeed should, be guided by the federal policies reflected in congressional enactments. Cf.<i>Moragne</i> v. <i>States Marine Lines, Inc.,</i> <span class="citation" data-id="108166"><a href="/opinion/108166/moragne-v-states-marine-lines-inc/#390" aria-description="Citation for case: Moragne v. States Marine Lines, Inc.">398 U. S. 375, 390-391</a></span> (1970).See also <i>United States</i> v. <i>Mendoza,</i> <span class="citation" data-id="111052"><a href="/opinion/111052/united-states-v-mendoza/" aria-description="Citation for case: United States v. Mendoza">464 U. S. 154</a></span> (1984) (recognizing exception to general principles of res judicata in light of overriding federal policy concerns).Thus, the court-made preclusion rules may, as judicial application of the categorical mandate of § 1983may <i>not,</i> see <i>Patsy</i> v.<i>Board of Regents of Fla.,</i> 457 U. S.496,509 (1982),take account of the policy embodied in§ 2254(b)'s exhaustion requirement, see <i>Rose</i> v. <i>Lundy,</i> <span class="citation" data-id="9428690"><a href="/opinion/110662/rose-v-lundy/" aria-description="Citation for case: Rose v. Lundy">455 U. S. 509</a></span> (1982), that state courts be given the first opportunity to review constitutional claims bearing upon state prisoners' release from custody.</p>
<p>[1]  Justice Souter also adopts the common-law principle that one cannot use the device of a civil tort action to challenge the validity of an outstanding criminal conviction, but thinks it necessary to abandon that principle in those cases (of which no real-life example comes to mind) involving former state prisoners who, because they are no longer in custody, cannot bring postconviction challenges. <i>Post,</i> at 500. We think the principle barring collateral attacksa longstanding and deeply rooted feature of both the common law and our own jurisprudenceis not rendered inapplicable by the fortuity that a convicted criminal is no longer incarcerated. Justice Souter opines that disallowing a damages suit for a former state prisoner framed by Ku Klux Klan-dominated state officials is "hard indeed to reconcile . . . with the purpose of § 1983." <i>Post,</i> at 502. But if, as Justice Souter appears to suggest, the goal of our interpretive enterprise under § 1983 were to provide a remedy for all conceivable invasions of federal rights that freedmen may have suffered at the hands of officials of the former States of the Confederacy, the entire landscape of our § 1983 jurisprudence would look very different. We would not, for example, have adopted the rule that judicial officers have absolute immunity from liability for damages under § 1983, <i>Pierson</i> v. <i>Ray,</i> <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547</a></span> (1967), a rule that would prevent recovery by a former slave who had been tried and convicted before a corrupt state judge in league with the Ku Klux Klan.</p>
<p>[2]  Our recent opinion in <i>Wyatt</i> v. <i>Cole,</i> <span class="citation" data-id="9432538"><a href="/opinion/112733/wyatt-v-cole/" aria-description="Citation for case: Wyatt v. Cole">504 U. S. 158</a></span> (1992), summarized the manner in which the Court has analyzed the relationship between the common law and § 1983 in the context of immunity:
</p>
<p>"Section 1983 `creates a species of tort liability that on its face admits of no immunities.' <i>Imbler</i> v. <i>Pachtman,</i> <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#417" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409, 417</a></span> (1976). Nonetheless, we have accorded certain government officials either absolute or qualified immunity from suit if the `tradition of immunity was so firmly rooted in the common law and was supported by such strong policy reasons that "Congress would have specifically so provided had it wished to abolish the doctrine."` <i>Owen</i> v. <i>City of Independence,</i> <span class="citation" data-id="9427858"><a href="/opinion/110236/owen-v-city-of-independence/#637" aria-description="Citation for case: Owen v. City of Independence">445 U. S. 622, 637</a></span> (1980) (quoting <i>Pierson</i> v. <i>Ray,</i> <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#555" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547, 555</a></span> (1967)). If parties seeking immunity were shielded from tort liability when Congress enacted the Civil Rights Act of 1871§ 1 of which is codified at 42 U. S. C. § 1983we infer from legislative silence that Congress did not intend to abrogate such immunities when it imposed liability for actions taken under color of state law. See <i>Tower</i> v. <i>Glover,</i> <span class="citation" data-id="9842065"><a href="/opinion/111224/tower-v-glover/#920" aria-description="Citation for case: Tower v. Glover">467 U. S. 914, 920</a></span> (1984); <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#421" aria-description="Citation for case: Imbler v. Pachtman"><i>Imbler, supra,</i> at 421</a></span>; <i>Pulliam</i> v. <i>Allen,</i> <span class="citation" data-id="9429586"><a href="/opinion/111166/pulliam-v-allen/#529" aria-description="Citation for case: Pulliam v. Allen">466 U. S. 522, 529</a></span> (1984). Additionally, irrespective of the common law support, we will not recognize an immunity available at common law if § 1983's history or purpose counsel against applying it in § 1983 actions. <span class="citation" data-id="9842065"><a href="/opinion/111224/tower-v-glover/#920" aria-description="Citation for case: Tower v. Glover"><i>Tower, supra,</i> at 920</a></span>. See also <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#424" aria-description="Citation for case: Imbler v. Pachtman"><i>Imbler, supra,</i> at 424-429</a></span>." <i>Id.,</i> at 163-164. In his concurrence, Justice Kennedy stated: "It must be remembered that unlike the common-law judges whose doctrines we adopt, we are devising limitations to a remedial statute, enacted by the Congress, which `on its face does not provide for <i>any</i> immunities.' " <i>Id.,</i> at 171 (quoting <i>Malley</i> v. <i>Briggs,</i> <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#342" aria-description="Citation for case: Malley v. Briggs">475 U. S. 335, 342</a></span> (1986)) (emphasis added in <i><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/" aria-description="Citation for case: Malley v. Briggs">Malley</a></span></i> ).</p>
<p>[3]  As the Court observes, there are differences between the tort of abuse of process and that of malicious prosecution. <i>Ante,</i> at 486, n. 5. While "the gist of the tort [of malicious prosecution] is . . . . commencing an action or causing process to issue without justification," abuse of process involves "misusing, or misapplying process justified in itself for an end other than that which it was designed to accomplish." Prosser and Keeton 897. Neither common-law tort, however, precisely matches the statutory § 1983 claim for damages for unlawful conviction or confinement; and, depending on the nature of the underlying right alleged to have been violated (consider, for example, the right not to be selected for prosecution solely because of one's race), the tort of abuse of process might provide a better analogy to a § 1983 claim for unconstitutional conviction or confinement than the malicious-prosecution tort.</p>
<p>[4]  Some of the traditional common-law requirements appear to have liberalized over the years, see Prosser and Keeton 882 ("There is a considerable minority view which regards the conviction as creating only a presumption, which may be rebutted by any competent evidence showing that probable cause for the prosecution did not in fact exist"), strengthening the analogy the Court draws. But surely the Court is not of the view that a single tort in its late 20th-century form can conclusively (and retroactively) dictate the requirements of a 19th-century statute for a discrete category of cases. Defending the historical analogy, the Court suggests that Chief Justice Cooley did not mean what he clearly said and that, despite the Cooley treatise, the Reconstruction-era common law recognized a limited exception to the rule denying a malicious-prosecution plaintiff the benefit of the invalidation of his conviction: an exception for convictions "obtained by some type of fraud." <i>Ante,</i> at 485, n. 4 (citing <i>Crescent City Live Stock Co.</i> v. <i>Butchers' Union Slaughter-House Co.,</i> <span class="citation" data-id="91832"><a href="/opinion/91832/crescent-city-live-stock-co-v-batchers-union-slaughter-house-co/#151" aria-description="Citation for case: Crescent City Live Stock Co. v. Batchers&#x27; Union...">120 U. S. 141, 151</a></span> (1887)). Even if such a narrow exception existed, however, the tort of malicious prosecution as it stood during the mid-19th century would still make for a weak analogy to a statutory action under which, as even the Court accepts, defendants whose convictions were reversed as violating "any righ[t] . . . secured by the Constitution," <span class="citation no-link">42 U. S. C. § 1983</span>, may obtain damages for the unlawful confinement associated with the conviction (assuming, of course, no immunity bar). Nor, of course, would the existence of such an exception explain how one element of a maliciousprosecution action may be imported into § 1983, but not the others.</p>
<p>[]  The requirement that a state prisoner seeking § 1983 damages for unlawful conviction or confinement be successful in state court or on federal habeas strikes me as soundly rooted in the statutory scheme. Because "Congress has determined that habeas corpus is the appropriate remedy for state prisoners attacking the validity of the fact or length of their confinement, [a] specific determination [that] override[s] the general terms of § 1983," <i>Preiser</i> v. <i>Rodriguez,</i> <span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/#490" aria-description="Citation for case: Preiser v. Rodriguez">411 U. S. 475, 490</a></span> (1973), a state prisoner whose constitutional attacks on his confinement have been rejected by state courts cannot be said to be unlawfully confined unless a federal habeas court declares his "custody [to be] in violation of the Constitution or laws or treaties of the United States," <span class="citation no-link">28 U. S. C. § 2254</span>(a). An unsuccessful federal habeas petitioner cannot, therefore, consistently with the habeas statute, receive § 1983 damages for unlawful confinement. That is not to say, however, that a state prisoner whose request for release has been (or would be) rejected by state courts or by a federal habeas court is necessarily barred from seeking any § 1983 damages for violations of his constitutional rights. If a § 1983 judgment in his favor would not demonstrate the invalidity of his confinement he is outside the habeas statute and may seek damages for a constitutional violation even without showing "favorable termination." A state prisoner may, for example, seek damages for an unreasonable search that produced evidence lawfully or harmlessly admitted at trial, or even nominal damages for, say, a violation of his right to procedural due process, see <i>Carey</i> v. <i>Piphus,</i> <span class="citation" data-id="109815"><a href="/opinion/109815/carey-v-piphus/#266" aria-description="Citation for case: Carey v. Piphus">435 U. S. 247, 266</a></span> (1978). See <i>ante,</i> at 487, and n. 7.</p>

</div>
```

---

## GROUP: content/cases/Heien v. North Carolina.md  (`case`, 5 assertions)

### content_page

```
---
title: "Heien v. North Carolina"
type: case
citation: ""
parallel_cite: "135 S. Ct. 530; 190 L. Ed. 2d 475; 83 U.S.L.W. 4021; 25 Fla. L. Weekly Fed. S 20"
neutral_cite: 2014 U.S. LEXIS 8306
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2014
date_decided: 2014-12-15
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2014-12-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Heien v. North Carolina
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2760668/heien-v-north-carolina/"
  cluster_id: 2760668
  opinion_id: 9805193
  identity_checked: false
homes:
  - page: "[[Traffic Stops]]"
    role: "Key — Progeny / Refinement"
related: ["[[Delaware v. Prouse]]", "[[Brendlin v. California]]", "[[Whren v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "traffic-stop", "reasonable-suspicion", "mistake-of-law"]
holding: "A traffic stop is valid if based on an officer's objectively reasonable mistake of law (as well as a reasonable mistake of fact); a…"
lake:
  record_id: Heien v. North Carolina
  status: under_review
  projected_at: 2026-07-06
---

# Heien v. North Carolina

*574 U.S. 54 (2014)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A North Carolina officer, Sergeant Darisse, stopped a car because one of its two brake lights was out. North Carolina's vehicle code, however, arguably required only a single working "stop lamp," so the stop rested on a mistaken reading of the law. During the stop the occupants consented to a search, and officers found cocaine. The North Carolina Supreme Court held the stop valid because the officer's mistake of law was objectively reasonable.

## Issue
Whether a traffic stop is valid under the Fourth Amendment when it is based on an officer's reasonable mistake about what the law prohibits.

## Rule
Yes. Reasonable suspicion can rest on a reasonable mistake of law, as well as a reasonable mistake of fact, because the Fourth Amendment demands reasonableness, not perfection. "The question here is whether reasonable suspicion can rest on a mistaken understanding of the scope of a legal prohibition. We hold that it can." — 574 U.S. at 60 (135 S. Ct. at 536). ^pin-60

"To be reasonable is not to be perfect, and so the Fourth Amendment allows for some mistakes on the part of government officials, giving them 'fair leeway for enforcing the law in the community's protection.'" — *Id.* ^pin-60a

The mistake, however, must itself be objectively reasonable.

## Application
North Carolina's vehicle code was genuinely ambiguous about whether a car needed two working brake lights — a nearby provision required that "all originally equipped rear lamps" be functional — so Sergeant Darisse's belief that one broken brake light violated the law was objectively reasonable even though the statute did not in fact require it. Because that reasonable mistake of law supplied reasonable suspicion, the stop, and the consent search that followed, were valid.

## Conclusion
The traffic stop was valid because it rested on the officer's objectively reasonable mistake of law; the judgment upholding the stop was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Heien* holds that objectively reasonable mistakes of law, like reasonable mistakes of fact, can support reasonable suspicion for a stop — but the analysis is objective, so an officer's sloppiness or a misreading of an unambiguous statute will not qualify.

## Appears on
- [[Traffic Stops]] — *Key — Progeny / Refinement*

## Sources
- *Heien v. North Carolina*, 574 U.S. 54 (2014) — https://www.courtlistener.com/opinion/2760668/heien-v-north-carolina/ — pinpoint: 60 (135 S. Ct. at 536); cluster 2760668 → lead opinion 9805193.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e5826cfc3acb346f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2014 U.S. LEXIS 8306", "official_citation_present": false, "parallel_cite": "135 S. Ct. 530; 190 L. Ed. 2d 475; 83 U.S.L.W. 4021; 25 Fla. L. Weekly Fed. S 20", "title": "Heien v. North Carolina", "year": "2014"}}
{"assertion_id": "d2e2f9274e976228", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Key — Progeny / Refinement", "title": "Heien v. North Carolina"}}
{"assertion_id": "ed5dee1566c311f3", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A traffic stop is valid if based on an officer's objectively reasonable mistake of law (as well as a reasonable mistake of fact); a…", "title": "Heien v. North Carolina"}}
{"assertion_id": "2ec133898cea8398", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2014-12-15", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Heien v. North Carolina", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Heien v. North Carolina", "varies_by_point": "false"}}
{"assertion_id": "4bcfae6828145d8a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Heien v. North Carolina"}}
```

### lake record — Heien v. North Carolina

```json
{
  "schema_version": "s2.v1",
  "record_id": "Heien v. North Carolina",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Heien v. North Carolina",
    "case_name_short": "Heien",
    "case_name_full": "Nicholas Brady HEIEN, Petitioner v. NORTH CAROLINA.",
    "input_case_name": "Heien v. North Carolina",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2014-12-15",
    "year": 2014,
    "docket": null,
    "cluster_id": 2760668,
    "lead_opinion_id": 9805193,
    "sibling_ids": [
      2760668,
      9805193,
      9805194
    ],
    "absolute_url": "/opinion/2760668/heien-v-north-carolina/",
    "identity_method": "pending",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "135 S. Ct. 530",
        "volume": "135",
        "reporter": "S. Ct.",
        "page": "530",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "190 L. Ed. 2d 475",
        "volume": "190",
        "reporter": "L. Ed. 2d",
        "page": "475",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 U.S.L.W. 4021",
        "volume": "83",
        "reporter": "U.S.L.W.",
        "page": "4021",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 20",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "20",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2014 U.S. LEXIS 8306",
        "volume": "2014",
        "reporter": "U.S. LEXIS",
        "page": "8306",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "135 S. Ct. 530",
        "volume": "135",
        "reporter": "S. Ct.",
        "page": "530",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "190 L. Ed. 2d 475",
        "volume": "190",
        "reporter": "L. Ed. 2d",
        "page": "475",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 U.S. LEXIS 8306",
        "volume": "2014",
        "reporter": "U.S. LEXIS",
        "page": "8306",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 U.S.L.W. 4021",
        "volume": "83",
        "reporter": "U.S.L.W.",
        "page": "4021",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 20",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "20",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "scotus",
      "selected": null,
      "reason": "unlisted_reporter:Fla. L. Weekly Fed. S"
    }
  },
  "pinpoints": [
    {
      "id": "pin-60",
      "page": null,
      "quote": "so the stop rested on a mistaken reading of the law. During the stop the occupants consented to a search, and officers found cocaine. The North Carolina Supreme Court held the stop valid because the officer's mistake of law was objectively reasonable. ## Issue Whether a traffic stop is valid under the Fourth Amendment when it is based on an officer's reasonable mistake about what the law prohibits. ## Rule Yes. Reasonable suspicion can rest on a reasonable mistake of law, as well as a reasonable mistake of fact, because the Fourth Amendment demands reasonableness, not perfection.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-60a",
      "page": null,
      "quote": "To be reasonable is not to be perfect, and so the Fourth Amendment allows for some mistakes on the part of government officials, giving them 'fair leeway for enforcing the law in the community's protection.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2014-12-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Heien v. North Carolina",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Reed",
          "cluster_id": 10018647,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Reed",
          "cluster_id": 4731165,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Zachariah J. Marshall v. State of Indiana",
          "cluster_id": 4594526,
          "cite": [
            "117 N.E.3d 1254"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Barbeau",
          "cluster_id": 4543099,
          "cite": [
            "301 Neb. 293",
            "917 N.W.2d 913"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Baskins",
          "cluster_id": 4524209,
          "cite": [
            "818 S.E.2d 381",
            "260 N.C. App. 589"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Nicholson",
          "cluster_id": 4505529,
          "cite": [
            "813 S.E.2d 840",
            "371 N.C. 284"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Henry Bams",
          "cluster_id": 4396584,
          "cite": [
            "858 F.3d 937",
            "2017 WL 2380680",
            "2017 U.S. App. LEXIS 9735"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Catherine Nyree McCabe",
          "cluster_id": 4348155,
          "cite": [
            "890 N.W.2d 173",
            "2017 WL 474456",
            "2017 Minn. App. LEXIS 22"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cameron William Varley",
          "cluster_id": 4253887,
          "cite": [
            "501 S.W.3d 273",
            "2016 Tex. App. LEXIS 9816",
            "2016 WL 4540491"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hirschkorn",
          "cluster_id": 3219245,
          "cite": [
            "2016 ND 117",
            "881 N.W.2d 244",
            "2016 N.D. LEXIS 121",
            "2016 WL 3551359"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jeremy Darringer v. State of Indiana",
          "cluster_id": 3154500,
          "cite": [
            "46 N.E.3d 464",
            "2015 Ind. App. LEXIS 712",
            "2015 WL 7074714"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In Re Adoption of B.Y.",
          "cluster_id": 2826262,
          "cite": [
            "2015 UT 67",
            "356 P.3d 1215",
            "2015 WL 4730762"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Cahaly v. Paul LaRosa, III",
          "cluster_id": 2823574,
          "cite": [
            "796 F.3d 399",
            "2015 WL 4646922"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Marko",
          "cluster_id": 3008904,
          "cite": [
            "2015 COA 139",
            "434 P.3d 618"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
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
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reed Dempsey v. Bucknell University",
          "cluster_id": 4249767,
          "cite": [
            "834 F.3d 457",
            "2016 U.S. App. LEXIS 15334",
            "2016 WL 4434400"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
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
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "The People v. Rebecca Guthrie",
          "cluster_id": 2791646,
          "cite": [
            "25 N.Y.3d 130",
            "30 N.E.3d 880",
            "8 N.Y.S.3d 237"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Burnett",
          "cluster_id": 4581383,
          "cite": [
            "2019 CO 2",
            "432 P.3d 617"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Al-Sharif Scriven(075682)",
          "cluster_id": 4240125,
          "cite": [
            "226 N.J. 20",
            "140 A.3d 535",
            "2016 N.J. LEXIS 698"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
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
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bosarge v. Mississippi Bureau of Narcotics",
          "cluster_id": 2817283,
          "cite": [
            "796 F.3d 435",
            "2015 U.S. App. LEXIS 12193",
            "2015 WL 4282372"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cortez",
          "cluster_id": 6241264,
          "cite": [
            "543 S.W.3d 198"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mason v. Commonwealth",
          "cluster_id": 3200832,
          "cite": [
            "786 S.E.2d 148",
            "291 Va. 362",
            "2016 WL 2586178",
            "2016 Va. LEXIS 59"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Jayel Antrone Coleman",
          "cluster_id": 4347860,
          "cite": [
            "890 N.W.2d 284",
            "2017 WL 541063",
            "2017 Iowa Sup. LEXIS 11"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gaytan",
          "cluster_id": 2812404,
          "cite": [
            "2015 IL 116223"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Najee Finique Hairston v. Commonwealth of Virginia",
          "cluster_id": 4382075,
          "cite": [
            "67 Va. App. 552",
            "797 S.E.2d 794",
            "2017 Va. App. LEXIS 99"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ernest D. Shields",
          "cluster_id": 2808513,
          "cite": [
            "789 F.3d 733",
            "2015 U.S. App. LEXIS 10058",
            "2015 WL 3654318"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hill",
          "cluster_id": 4737513,
          "cite": [
            "162 N.E.3d 260",
            "443 Ill. Dec. 626",
            "2020 IL 124595"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Richard E. Houghton, Jr.",
          "cluster_id": 2816804,
          "cite": [
            "364 Wis. 2d 234",
            "2015 WI 79",
            "868 N.W.2d 143",
            "2015 Wisc. LEXIS 484"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hernandez",
          "cluster_id": 4347480,
          "cite": [
            "847 F.3d 1257",
            "2017 WL 526028",
            "2017 U.S. App. LEXIS 2324"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Diaz",
          "cluster_id": 8443247,
          "cite": [
            "854 F.3d 197",
            "2017 WL 1379188",
            "2017 U.S. App. LEXIS 6579"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Minnesota, Respondent/Cross-Appellant v. Bonnie Ann Lindquist, Appellant/Cross-Respondent.",
          "cluster_id": 2828527,
          "cite": [
            "869 N.W.2d 863",
            "2015 Minn. LEXIS 469"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shawn Northrup v. City of Toledo Police Dep't",
          "cluster_id": 2800431,
          "cite": [
            "785 F.3d 1128",
            "2015 FED App. 0092P",
            "2015 U.S. App. LEXIS 7868",
            "2015 WL 2217061"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mario Rodriguez-Escalera",
          "cluster_id": 4475216,
          "cite": [
            "884 F.3d 661"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hargraves v. District of Columbia",
          "cluster_id": 2977017,
          "cite": [
            "134 F. Supp. 3d 68",
            "2015 U.S. Dist. LEXIS 126401",
            "2015 WL 5611550"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Heien v. North Carolina:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2760668 OR 9805193 OR 9805194) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDM3MDkxMjAwMDAwJnM9NDI3MTg5OCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%282760668+OR+9805193+OR+9805194%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 13,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 14,
        "triage_snippet_classified": 186
      },
      "lane2_top_cited": {
        "query": "cites:(2760668 OR 9805193 OR 9805194)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMiZzPTk0NjgzNjgmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%282760668+OR+9805193+OR+9805194%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2760668 OR 9805193 OR 9805194)",
        "reviewed": 13,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 13,
        "triage_read": 0,
        "triage_snippet_classified": 13
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2760668 OR 9805193 OR 9805194)",
    "indexed_citing_opinions": 280,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2760668,
        "count": 239,
        "count_source": "search"
      },
      {
        "opinion_id": 9805193,
        "count": 44,
        "count_source": "search"
      },
      {
        "opinion_id": 9805194,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 620,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/heien-v-north-carolina.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc3OTk5JnM9NjQ3ODgyNCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%282760668+OR+9805193+OR+9805194%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2760668,
        "cited_id": 76272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 84913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 85007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 85416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 85835,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 108305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 110127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 111611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 111835,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 112475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 112517,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 137733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 145712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 145832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 145922,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 755171,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 772609,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 794005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 794904,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 885939,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 1107672,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 1201458,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 1205245,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 1253121,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 1294313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 1325858,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 1929805,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 2028985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 2050799,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 2179687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 2199548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 2227359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 2316698,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 2507522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 2584726,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 2633783,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2760668,
        "cited_id": 4714396,
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
    "date_created": "2026-07-05T06:45:48Z",
    "date_modified": "2026-07-06T07:55:53Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T06:45:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T06:49:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T06:55:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T06:49:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Heien v. North Carolina

```
<opinion type="majority">
<author id="p-10">Chief Justice ROBERTSdelivered the opinion of the Court.</author>
<p id="p-11">The Fourth Amendment prohibits "unreasonable searches and seizures." Under this standard, a search or seizure may be permissible even though the justification for the action includes a reasonable factual mistake. An officer might, for example, stop a motorist for traveling alone in a high-occupancy vehicle lane, only to discover upon approaching the car that two children are slumped over asleep in the back seat. The driver has not violated the law, but neither has the officer violated the Fourth Amendment.</p>
<p id="p-12">But what if the police officer's reasonable mistake is not one of fact but of law? In this case, an officer stopped a vehicle because one of its two brake lights was out, but a court later determined that a single working brake light was all the law required. The question presented is whether such a mistake of law can nonetheless give rise to the reasonable suspicion necessary to uphold the seizure under the Fourth Amendment. We hold that it can. Because the officer's mistake about the brake-light law was reasonable, the stop in this case was lawful under the Fourth Amendment.</p>
<p id="p-13">I</p>
<p id="p-14">On the morning of April 29, 2009, Sergeant Matt Darisse of the Surry County Sheriff's Department sat in his patrol car near Dobson, North Carolina, observing northbound traffic on Interstate 77. Shortly before 8 a.m., a Ford Escort passed by. Darisse thought the driver looked "very stiff and nervous," so he pulled onto the interstate and began following the Escort. A few miles down the road, the Escort braked as it approached a slower vehicle, but only the left brake light came on. Noting the faulty right brake light, Darisse activated his vehicle's lights and pulled the Escort over. App. 4-7, 15-16.</p>
<p id="p-15">Two men were in the car: Maynor Javier Vasquez sat behind the wheel, and petitioner Nicholas Brady Heien lay across the rear seat. Sergeant Darisse explained to Vasquez that as long as his license and registration checked out, he would receive only a warning ticket for the broken brake light. A records check revealed no problems with the documents, and Darisse gave Vasquez the warning ticket. But Darisse had become suspicious during the course of the stop-Vasquez appeared nervous, Heien remained lying down the entire time, and the two gave inconsistent answers about their destination. Darisse asked Vasquez if he would be willing to answer some questions. Vasquez assented, and Darisse asked whether the men were transporting various types of contraband. Told no, Darisse asked whether he could search the Escort. Vasquez said he had no objection, but told Darisse he should ask Heien, because Heien owned the car. Heien gave his consent, and Darisse, aided by a fellow officer who had since arrived, began a thorough search of the vehicle. In the side compartment of a duffle bag, Darisse found a sandwich bag containing cocaine. The officers arrested both men.</p>
<p id="p-16"><a class="page-label" data-citation-index="1" data-label="535" href="#p535" id="p535">*535</a><extracted-citation case-ids="4357764" index="0" url="https://cite.case.law/nc/366/271/#p272"><span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/" aria-description="Citation for case: State v. Heien">366 N.C. 271</a></span></extracted-citation>, 272-273, <extracted-citation index="1" url="https://cite.case.law/citations/?q=737%20S.E.2d%20351"><span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/" aria-description="Citation for case: State v. Heien">737 S.E.2d 351</a></span></extracted-citation>, 352-353 (2012); App. 5-6, 25, 37.</p>
<p id="p-17">The State charged Heien with attempted trafficking in cocaine. Heien moved to suppress the evidence seized from the car, contending that the stop and search had violated the Fourth Amendment of the United States Constitution. After a hearing at which both officers testified and the State played a video recording of the stop, the trial court denied the suppression motion, concluding that the faulty brake light had given Sergeant Darisse reasonable suspicion to initiate the stop, and that Heien's subsequent consent to the search was valid. Heien pleaded guilty but reserved his right to appeal the suppression decision. App. 1, 7-10, 12, 29, 43-44.</p>
<p id="p-18">The North Carolina Court of Appeals reversed. <extracted-citation case-ids="4278446" index="2" url="https://cite.case.law/nc-app/214/515/"><span class="citation" data-id="2507522"><a href="/opinion/2507522/state-v-heien/" aria-description="Citation for case: State v. Heien">214 N.C.App. 515</a></span></extracted-citation>, <extracted-citation index="3" url="https://cite.case.law/citations/?q=714%20S.E.2d%20827"><span class="citation" data-id="2507522"><a href="/opinion/2507522/state-v-heien/" aria-description="Citation for case: State v. Heien">714 S.E.2d 827</a></span></extracted-citation> (2011). The initial stop was not valid, the court held, because driving with only one working brake light was not actually a violation of North Carolina law. The relevant provision of the vehicle code provides that a car must be</p>
<blockquote id="p-19">"equipped with a stop lamp on the rear of the vehicle. The stop lamp shall display a red or amber light visible from a distance of not less than 100 feet to the rear in normal sunlight, and shall be actuated upon application of the service (foot) brake. The stop lamp may be incorporated into a unit with one or more other rear lamps." N.C. Gen.Stat. Ann. § 20-129(g) (2007).</blockquote>
<p id="p-20">Focusing on the statute's references to "a stop lamp" and "[t]he stop lamp" in the singular, the court concluded that a vehicle is required to have only one working brake light-which Heien's vehicle indisputably did. The justification for the stop was therefore "objectively unreasonable," and the stop violated the Fourth Amendment. <extracted-citation case-ids="4278446" index="4" url="https://cite.case.law/nc-app/214/515/"><span class="citation" data-id="2507522"><a href="/opinion/2507522/state-v-heien/" aria-description="Citation for case: State v. Heien">214 N.C.App., at 518</a></span>-522</extracted-citation>, <extracted-citation index="5" url="https://cite.case.law/citations/?q=714%20S.E.2d%20827"><span class="citation" data-id="2507522"><a href="/opinion/2507522/state-v-heien/" aria-description="Citation for case: State v. Heien">714 S.E.2d, at 829</a></span>-831</extracted-citation>.</p>
<p id="p-21">The State appealed, and the North Carolina Supreme Court reversed. <extracted-citation case-ids="4357764" index="6" url="https://cite.case.law/nc/366/271/#p272"><span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/" aria-description="Citation for case: State v. Heien">366 N.C. 271</a></span></extracted-citation>, <extracted-citation index="7" url="https://cite.case.law/citations/?q=737%20S.E.2d%20351"><span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/" aria-description="Citation for case: State v. Heien">737 S.E.2d 351</a></span></extracted-citation>. Noting that the State had chosen not to seek review of the Court of Appeals' interpretation of the vehicle code, the North Carolina Supreme Court assumed for purposes of its decision that the faulty brake light was not a violation. <span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/#275" aria-description="Citation for case: State v. Heien"><em>Id.,</em>at 275</a></span>, <extracted-citation index="8" url="https://cite.case.law/citations/?q=737%20S.E.2d%20351"><span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/" aria-description="Citation for case: State v. Heien">737 S.E.2d, at 354</a></span></extracted-citation>. But the court concluded that, for several reasons, Sergeant Darisse could have reasonably, even if mistakenly, read the vehicle code to require that both brake lights be in good working order. Most notably, a nearby code provision requires that "all originally equipped rear lamps" be functional. <span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/#282" aria-description="Citation for case: State v. Heien"><em>Id.,</em>at 282-283</a></span>, <extracted-citation index="9" url="https://cite.case.law/citations/?q=737%20S.E.2d%20351"><span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/" aria-description="Citation for case: State v. Heien">737 S.E.2d, at 358</a></span>-359</extracted-citation>(quoting N.C. Gen.Stat. Ann. § 20-129(d)). Because Sergeant Darisse's mistaken understanding of the vehicle code was reasonable, the stop was valid. "An officer may make a mistake, including a mistake of law, yet still act reasonably under the circumstances.... [W]hen an officer acts reasonably under the circumstances, he is not violating the Fourth Amendment." <em>Id.,</em>at 279, <extracted-citation index="10" url="https://cite.case.law/citations/?q=737%20S.E.2d%20351"><span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/" aria-description="Citation for case: State v. Heien">737 S.E.2d, at 356</a></span></extracted-citation>.</p>
<p id="p-22">The North Carolina Supreme Court remanded to the Court of Appeals to address Heien's other arguments for suppression (which are not at issue here). <span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/#283" aria-description="Citation for case: State v. Heien"><em>Id.,</em>at 283</a></span>, <extracted-citation index="11" url="https://cite.case.law/citations/?q=737%20S.E.2d%20351"><span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/" aria-description="Citation for case: State v. Heien">737 S.E.2d, at 359</a></span></extracted-citation>. The Court of Appeals rejected those arguments and affirmed the trial court's denial of his motion to suppress. --- N.C.App. ----, <extracted-citation index="12" url="https://cite.case.law/citations/?q=741%20S.E.2d%201"><span class="citation" data-id="8901380"><a href="/opinion/8913448/state-v-heien/" aria-description="Citation for case: State v. Heien">741 S.E.2d 1</a></span></extracted-citation> (2013). The North Carolina Supreme Court affirmed in turn. <extracted-citation case-ids="4320742" index="13" url="https://cite.case.law/nc/367/163/"><span class="citation" data-id="6724324"><a href="/opinion/6837178/state-v-heien/" aria-description="Citation for case: State v. Heien">367 N.C. 163</a></span></extracted-citation>, <extracted-citation index="14" url="https://cite.case.law/citations/?q=749%20S.E.2d%20278"><span class="citation multiple-matches"><a href="/c/S.E.2d/749/278/">749 S.E.2d 278</a></span></extracted-citation> (2013). We granted certiorari. 572 U.S. ----, <extracted-citation case-ids="12705668,12705579,12705580,12705616,12580278,12580279,12580280,12580281,12580282,12705662" index="15" url="https://cite.case.law/s-ct/134/1872/"><span class="citation multiple-matches"><a href="/c/S.Ct./134/1872/">134 S.Ct. 1872</a></span></extracted-citation>, <extracted-citation case-ids="12580384,12705610,12580398,12705623,12705616,12580273,12705617,12705621,12705622,12580439,12580280,12580283" index="16" url="https://cite.case.law/l-ed-2d/188/910/"><span class="citation multiple-matches"><a href="/c/L.Ed.2d/188/910/">188 L.Ed.2d 910</a></span></extracted-citation> (2014).</p>
<p id="p-23">II</p>
<p id="p-24">The Fourth Amendment provides:</p>
<blockquote id="p-25">"The right of the people to be secure in their persons, houses, papers, and <a class="page-label" data-citation-index="1" data-label="536" href="#p536" id="p536">*536</a>effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</blockquote>
<p id="p-26">A traffic stop for a suspected violation of law is a "seizure" of the occupants of the vehicle and therefore must be conducted in accordance with the Fourth Amendment. <em>Brendlin v. California,</em><extracted-citation case-ids="3573063" index="17" url="https://cite.case.law/us/551/249/#p255"><span class="citation" data-id="145712"><a href="/opinion/145712/brendlin-v-california/" aria-description="Citation for case: Brendlin v. California">551 U.S. 249</a></span></extracted-citation>, 255-259, <extracted-citation case-ids="3573063" index="18" url="https://cite.case.law/us/551/249/#p255"><span class="citation" data-id="145712"><a href="/opinion/145712/brendlin-v-california/" aria-description="Citation for case: Brendlin v. California">127 S.Ct. 2400</a></span></extracted-citation>, <extracted-citation case-ids="3573063" index="19" url="https://cite.case.law/us/551/249/#p255"><span class="citation" data-id="145712"><a href="/opinion/145712/brendlin-v-california/" aria-description="Citation for case: Brendlin v. California">168 L.Ed.2d 132</a></span></extracted-citation> (2007). All parties agree that to justify this type of seizure, officers need only "reasonable suspicion"-that is, "a particularized and objective basis for suspecting the particular person stopped" of breaking the law. <em>Prado</em> <em>Navarette v. California,</em>572 U.S. ----, ----, <extracted-citation case-ids="12579832,12706993" index="20" url="https://cite.case.law/s-ct/134/1683/"><span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/" aria-description="Citation for case: Prado Navarette v. California">134 S.Ct. 1683</a></span></extracted-citation>, 1687-88, <extracted-citation case-ids="12579832,12706993" index="21" url="https://cite.case.law/s-ct/134/1683/"><span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/" aria-description="Citation for case: Prado Navarette v. California">188 L.Ed.2d 680</a></span></extracted-citation> (2014)(internal quotation marks omitted). The question here is whether reasonable suspicion can rest on a mistaken understanding of the scope of a legal prohibition. We hold that it can.</p>
<p id="p-27">As the text indicates and we have repeatedly affirmed, "the ultimate touchstone of the Fourth Amendment is 'reasonableness.' " <em>Riley v. California,</em>573 U.S. ----, ----, <extracted-citation case-ids="12581677" index="22" url="https://cite.case.law/s-ct/134/2473/#p2482"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">134 S.Ct. 2473</a></span></extracted-citation>, 2482, <extracted-citation case-ids="12581677" index="23" url="https://cite.case.law/s-ct/134/2473/#p2482"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">189 L.Ed.2d 430</a></span></extracted-citation> (2014)(some internal quotation marks omitted). To be reasonable is not to be perfect, and so the Fourth Amendment allows for some mistakes on the part of government officials, giving them "fair leeway for enforcing the law in the community's protection." <em>Brinegar v. United States,</em><extracted-citation case-ids="3943769" index="24" url="https://cite.case.law/us/338/160/#p176"><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U.S. 160</a></span></extracted-citation>, 176, <extracted-citation case-ids="3943769" index="25" url="https://cite.case.law/us/338/160/#p176"><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">69 S.Ct. 1302</a></span></extracted-citation>, <extracted-citation index="26" url="https://cite.case.law/citations/?q=93%20L.%20Ed.%201879"><span class="citation no-link">93 L.Ed. 1879</span></extracted-citation> (1949). We have recognized that searches and seizures based on mistakes of fact can be reasonable. The warrantless search of a home, for instance, is reasonable if undertaken with the consent of a resident, and remains lawful when officers obtain the consent of someone who reasonably appears to be but is not in fact a resident. See <em>Illinois v. Rodriguez,</em><extracted-citation case-ids="6214176" index="27" url="https://cite.case.law/us/497/177/#p183"><span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/" aria-description="Citation for case: Illinois v. Rodriguez">497 U.S. 177</a></span></extracted-citation>, 183-186, <extracted-citation case-ids="6214176" index="28" url="https://cite.case.law/us/497/177/#p183"><span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/" aria-description="Citation for case: Illinois v. Rodriguez">110 S.Ct. 2793</a></span></extracted-citation>, <extracted-citation case-ids="6214176" index="29" url="https://cite.case.law/us/497/177/#p183"><span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/" aria-description="Citation for case: Illinois v. Rodriguez">111 L.Ed.2d 148</a></span></extracted-citation> (1990). By the same token, if officers with probable cause to arrest a suspect mistakenly arrest an individual matching the suspect's description, neither the seizure nor an accompanying search of the arrestee would be unlawful. See <em>Hill v. California,</em><extracted-citation case-ids="11714932" index="30" url="https://cite.case.law/us/401/797/#p802"><span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/" aria-description="Citation for case: Hill v. California">401 U.S. 797</a></span></extracted-citation>, 802-805, <extracted-citation case-ids="11714932" index="31" url="https://cite.case.law/us/401/797/#p802"><span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/" aria-description="Citation for case: Hill v. California">91 S.Ct. 1106</a></span></extracted-citation>, <extracted-citation case-ids="11714932" index="32" url="https://cite.case.law/us/401/797/#p802"><span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/" aria-description="Citation for case: Hill v. California">28 L.Ed.2d 484</a></span></extracted-citation> (1971). The limit is that "the mistakes must be those of reasonable men." <em>Brinegar,</em><em>supra,</em>at 176, <extracted-citation case-ids="3943769" index="33" url="https://cite.case.law/us/338/160/#p176"><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">69 S.Ct. 1302</a></span></extracted-citation>.</p>
<p id="p-28">But reasonable men make mistakes of law, too, and such mistakes are no less compatible with the concept of reasonable suspicion. Reasonable suspicion arises from the combination of an officer's understanding of the facts and his understanding of the relevant law. The officer may be reasonably mistaken on either ground. Whether the facts turn out to be not what was thought, or the law turns out to be not what was thought, the result is the same: the facts are outside the scope of the law. There is no reason, under the text of the Fourth Amendment or our precedents, why this same result should be acceptable when reached by way of a reasonable mistake of fact, but not when reached by way of a similarly reasonable mistake of law.</p>
<p id="p-29">The dissent counters that our cases discussing probable cause and reasonable suspicion, most notably <em>Ornelas v. United States,</em><extracted-citation case-ids="11746351" index="34" url="https://cite.case.law/us/517/690/#p696"><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/" aria-description="Citation for case: Ornelas v. United States">517 U.S. 690</a></span></extracted-citation>, 696-697, <extracted-citation case-ids="11746351" index="35" url="https://cite.case.law/us/517/690/#p696"><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/" aria-description="Citation for case: Ornelas v. United States">116 S.Ct. 1657</a></span></extracted-citation>, <extracted-citation case-ids="11746351" index="36" url="https://cite.case.law/us/517/690/#p696"><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/" aria-description="Citation for case: Ornelas v. United States">134 L.Ed.2d 911</a></span></extracted-citation> (1996), have contained "scarcely a peep" about mistakes of law. <em>Post,</em>at 542 - 543 (opinion of SOTOMAYOR, J.). It would have been surprising, of course, if they had, since none of those cases involved a mistake of law.</p>
<p id="p-30">Although such recent cases did not address mistakes of law, older precedents did. In fact, cases dating back two centuries <a class="page-label" data-citation-index="1" data-label="537" href="#p537" id="p537">*537</a>support treating legal and factual errors alike in this context. Customs statutes enacted by Congress not long after the founding authorized courts to issue certificates indemnifying customs officers against damages suits premised on unlawful seizures. See, <em>e.g.,</em>Act of Mar. 2, 1799, ch. 22, § 89, <extracted-citation index="37" url="https://cite.case.law/citations/?q=1%20Stat.%20695"><span class="citation no-link">1 Stat. 695</span></extracted-citation>-696. Courts were to issue such certificates on a showing that the officer had "reasonable cause"-a synonym for "probable cause"-for the challenged seizure. <em><span class="citation no-link">Ibid.</span></em>; see <em>Stacey v. Emery,</em><extracted-citation case-ids="3374947" index="38" url="https://cite.case.law/us/97/642/#p646"><span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/" aria-description="Citation for case: Stacey v. Emery">97 U.S. 642</a></span></extracted-citation>, 646, <extracted-citation case-ids="3374947" index="39" url="https://cite.case.law/us/97/642/#p646"><span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/" aria-description="Citation for case: Stacey v. Emery">24 L.Ed. 1035</a></span></extracted-citation> (1878); <em>United States v. Riddle,</em><extracted-citation case-ids="11644565,1446255" index="40" url="https://cite.case.law/cranch/5/311/"><span class="citation" data-id="84913"><a href="/opinion/84913/united-states-v-riddle/" aria-description="Citation for case: United States v. Riddle">5 Cranch 311</a></span></extracted-citation>, <extracted-citation case-ids="1446255" index="41" url="https://cite.case.law/us/9/311/"><span class="citation" data-id="84913"><a href="/opinion/84913/united-states-v-riddle/" aria-description="Citation for case: United States v. Riddle">3 L.Ed. 110</a></span></extracted-citation> (1809). In <em>United States v. Riddle,</em>a customs officer seized goods on the ground that the English shipper had violated the customs laws by preparing an invoice that undervalued the merchandise, even though the American consignee declared the true value to the customs collector. Chief Justice Marshall held that there had been no violation of the customs law because, whatever the shipper's intention, the consignee had not actually attempted to defraud the Government. Nevertheless, because "the construction of the law was liable to some question," he affirmed the issuance of a certificate of probable cause: "A doubt as to the true construction of the <em>law</em>is as reasonable a cause for seizure as a doubt respecting the fact." <span class="citation" data-id="84913"><a href="/opinion/84913/united-states-v-riddle/#313" aria-description="Citation for case: United States v. Riddle"><em>Id.,</em>at 313</a></span>.</p>
<p id="p-31">This holding-that reasonable mistakes of law, like those of fact, would justify certificates of probable cause-was reiterated in a number of 19th-century decisions. See, <em>e.g.,</em> <em>The Friendship,</em><extracted-citation case-ids="11652906" index="42" url="https://cite.case.law/f-cas/9/825/#p826"><span class="citation" data-id="8631400"><a href="/opinion/8651576/the-friendship/" aria-description="Citation for case: The Friendship">9 F.Cas. 825</a></span></extracted-citation>, 826 (No. 5,125)(C.C.D.Mass.1812) (Story, J.); <em>United States v.</em> <em>The Reindeer,</em><extracted-citation case-ids="6134818" index="43" url="https://cite.case.law/f-cas/27/758/#p768"><span class="citation" data-id="8639394"><a href="/opinion/8659539/united-states-v-the-reindeer/" aria-description="Citation for case: United States v. The Reindeer">27 F.Cas. 758</a></span></extracted-citation>, 768 (No. 16,145) (C.C.D.R.I.1848); <em>United States v.</em> <em>The Recorder,</em><extracted-citation case-ids="6134661" index="44" url="https://cite.case.law/f-cas/27/723/"><span class="citation" data-id="8639386"><a href="/opinion/8659531/united-states-v-the-recorder/" aria-description="Citation for case: United States v. The Recorder">27 F.Cas. 723</a></span></extracted-citation> (No. 16,130) (C.C.S.D.N.Y.1849). By the Civil War, there had been "numerous cases in which [a] captured vessel was in no fault, and had not, under a true construction of the law, presented even ground of suspicion, and yet the captor was exonerated because he acted under an honest mistake of the law." <em>The La Manche,</em><extracted-citation case-ids="6649440" index="45" url="https://cite.case.law/f-cas/14/965/#p972"><span class="citation" data-id="8633513"><a href="/opinion/8653675/the-la-manche/" aria-description="Citation for case: The La Manche">14 F.Cas. 965</a></span></extracted-citation>, 972 (No. 8,004)(D.Mass.1863).</p>
<p id="p-32"><em><span class="citation" data-id="84913"><a href="/opinion/84913/united-states-v-riddle/" aria-description="Citation for case: United States v. Riddle">Riddle</a></span></em>and its progeny are not directly on point. Chief Justice Marshall was not construing the Fourth Amendment, and a certificate of probable cause functioned much like a modern-day finding of qualified immunity, which depends on an inquiry distinct from whether an officer has committed a constitutional violation. See, <em>e.g.,</em><em>Carroll v. Carman, ante,</em>at 7, --- U.S. ----, <extracted-citation case-ids="12592389" index="46" url="https://cite.case.law/s-ct/135/348/#p352"><span class="citation" data-id="2750102"><a href="/opinion/2750102/carroll-v-carman/" aria-description="Citation for case: Carroll v. Carman">135 S.Ct. 348</a></span></extracted-citation>, 352, --- L.Ed.2d ---- (2014)(<em>per curiam</em>). But Chief Justice Marshall was nevertheless explaining the concept of probable cause, which, he noted elsewhere, "in all cases of seizure, has a fixed and well known meaning. It imports a seizure made under circumstances which warrant suspicion."<em>Locke v. United States,</em><extracted-citation case-ids="572700" index="47" url="https://cite.case.law/us/11/339/#p348"><span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/" aria-description="Citation for case: Locke v. United States">7 Cranch 339</a></span></extracted-citation>, 348, <extracted-citation case-ids="572700" index="48" url="https://cite.case.law/us/11/339/#p348"><span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/" aria-description="Citation for case: Locke v. United States">3 L.Ed. 364</a></span></extracted-citation> (1813). We have said the phrase "probable cause" bore this "fixed and well known meaning" in the Fourth Amendment, see <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States"><em>Brinegar, supra,</em>at 175</a></span>, and n. 14, <extracted-citation case-ids="3943769" index="49" url="https://cite.case.law/us/338/160/#p176"><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">69 S.Ct. 1302</a></span></extracted-citation>, and <em><span class="citation" data-id="84913"><a href="/opinion/84913/united-states-v-riddle/" aria-description="Citation for case: United States v. Riddle">Riddle</a></span></em>illustrates that it encompassed suspicion based on reasonable mistakes of both fact and law. No decision of this Court in the two centuries since has undermined that understanding.<footnotemark>*</footnotemark></p>
<p id="p-33"><a class="page-label" data-citation-index="1" data-label="538" href="#p538" id="p538">*538</a>The contrary conclusion would be hard to reconcile with a much more recent precedent. In <em>Michigan v. DeFillippo,</em><extracted-citation case-ids="6179569" index="50" url="https://cite.case.law/us/443/31/"><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">443 U.S. 31</a></span></extracted-citation>, <extracted-citation case-ids="6179569" index="51" url="https://cite.case.law/us/443/31/"><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">99 S.Ct. 2627</a></span></extracted-citation>, <extracted-citation case-ids="6179569" index="52" url="https://cite.case.law/us/443/31/"><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">61 L.Ed.2d 343</a></span></extracted-citation> (1979), we addressed the validity of an arrest made under a criminal law later declared unconstitutional. A Detroit ordinance that authorized police officers to stop and question individuals suspected of criminal activity also made it an offense for such an individual "to refuse to identify himself and produce evidence of his identity." <span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/#33" aria-description="Citation for case: Michigan v. DeFillippo"><em>Id.,</em>at 33</a></span>, <extracted-citation case-ids="6179569" index="53" url="https://cite.case.law/us/443/31/"><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">99 S.Ct. 2627</a></span></extracted-citation>. Detroit police officers sent to investigate a report of public intoxication arrested Gary DeFillippo after he failed to identify himself. A search incident to arrest uncovered drugs, and DeFillippo was charged with possession of a controlled substance. The Michigan Court of Appeals ordered the suppression of the drugs, concluding that the identification ordinance was unconstitutionally vague and that DeFillippo's arrest was therefore invalid. <span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/#34" aria-description="Citation for case: Michigan v. DeFillippo"><em>Id.,</em>at 34-35</a></span>, <extracted-citation case-ids="6179569" index="54" url="https://cite.case.law/us/443/31/"><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">99 S.Ct. 2627</a></span></extracted-citation>.</p>
<p id="p-34">Accepting the unconstitutionality of the ordinance as a given, we nonetheless reversed. At the time the officers arrested DeFillippo, we explained, "there was no controlling precedent that this ordinance was or was not constitutional, and hence the conduct observed violated a presumptively valid ordinance." <span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/#37" aria-description="Citation for case: Michigan v. DeFillippo"><em>Id.,</em>at 37</a></span>, <extracted-citation case-ids="6179569" index="55" url="https://cite.case.law/us/443/31/"><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">99 S.Ct. 2627</a></span></extracted-citation>. Acknowledging that the outcome might have been different had the ordinance been "grossly and flagrantly unconstitutional," we concluded that under the circumstances "there was abundant probable cause to satisfy the constitutional prerequisite for an arrest." <span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/#37" aria-description="Citation for case: Michigan v. DeFillippo"><em>Id.,</em>at 37-38</a></span>, <extracted-citation case-ids="6179569" index="56" url="https://cite.case.law/us/443/31/"><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">99 S.Ct. 2627</a></span></extracted-citation>.</p>
<p id="p-35">The officers were wrong in concluding that DeFillippo was guilty of a criminal offense when he declined to identify himself. That a court only <em>later</em>declared the ordinance unconstitutional does not change the fact that DeFillippo's conduct was lawful when the officers observed it. See <em>Danforth v. Minnesota,</em><extracted-citation case-ids="3675901" index="57" url="https://cite.case.law/us/552/264/#p271"><span class="citation" data-id="9046929"><a href="/opinion/9053440/danforth-v-minnesota/" aria-description="Citation for case: Danforth v. Minnesota">552 U.S. 264</a></span></extracted-citation>, 271, <extracted-citation case-ids="3675901" index="58" url="https://cite.case.law/us/552/264/#p271"><span class="citation" data-id="145832"><a href="/opinion/145832/danforth-v-minnesota/" aria-description="Citation for case: Danforth v. Minnesota">128 S.Ct. 1029</a></span></extracted-citation>, <extracted-citation case-ids="3675901" index="59" url="https://cite.case.law/us/552/264/#p271"><span class="citation" data-id="145832"><a href="/opinion/145832/danforth-v-minnesota/" aria-description="Citation for case: Danforth v. Minnesota">169 L.Ed.2d 859</a></span></extracted-citation> (2008). But the officers' assumption that the law was valid was reasonable, and their observations gave them "abundant probable cause" to arrest DeFillippo. <extracted-citation case-ids="6179569" index="60" url="https://cite.case.law/us/443/31/"><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">443 U.S., at 37</a></span></extracted-citation>, <extracted-citation case-ids="6179569" index="61" url="https://cite.case.law/us/443/31/"><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">99 S.Ct. 2627</a></span></extracted-citation>. Although DeFillippo could not be prosecuted under the identification ordinance, the search that turned up the drugs was constitutional.</p>
<p id="p-36">Heien struggles to recast <em><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">DeFillippo</a></span></em>as a case solely about the exclusionary rule, not the Fourth Amendment itself. In his view, the officers' mistake of law resulted in a violation the Fourth Amendment, but suppression of the drugs was not the proper remedy. We did say in a footnote that suppression of the evidence found on DeFillippo would serve none of the purposes of the exclusionary rule. See <span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/#38" aria-description="Citation for case: Michigan v. DeFillippo"><em>id.,</em>at 38, n. 3</a></span>, <extracted-citation case-ids="6179569" index="62" url="https://cite.case.law/us/443/31/"><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">99 S.Ct. 2627</a></span></extracted-citation>. But that literally marginal discussion does not displace our express holding that the arrest was constitutionally valid because the officers had probable cause. See <span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/#40" aria-description="Citation for case: Michigan v. DeFillippo"><em>id.,</em>at 40</a></span>, <extracted-citation case-ids="6179569" index="63" url="https://cite.case.law/us/443/31/"><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">99 S.Ct. 2627</a></span></extracted-citation>. Nor, contrary to Heien's suggestion, did either <em>United States v. Leon,</em><extracted-citation case-ids="11340969" index="64" url="https://cite.case.law/us/468/897/"><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U.S. 897</a></span></extracted-citation>, <extracted-citation case-ids="11340969" index="65" url="https://cite.case.law/us/468/897/"><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span></extracted-citation>, <extracted-citation case-ids="11340969" index="66" url="https://cite.case.law/us/468/897/"><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">82 L.Ed.2d 677</a></span></extracted-citation> (1984), or <em>Illinois v. Gates,</em><extracted-citation case-ids="6187462" index="67" url="https://cite.case.law/us/462/213/"><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">462 U.S. 213</a></span></extracted-citation>, <extracted-citation case-ids="6187462" index="68" url="https://cite.case.law/us/462/213/"><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">103 S.Ct. 2317</a></span></extracted-citation>, <extracted-citation case-ids="6187462" index="69" url="https://cite.case.law/us/462/213/"><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">76 L.Ed.2d 527</a></span></extracted-citation> (1983), somehow erase that holding and transform <em><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">DeFillippo</a></span></em>into an exclusionary rule decision. See Brief for Petitioner 28-29. In <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>,</em>we said <em><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">DeFillippo</a></span></em>paid "attention to the purposes underlying the exclusionary rule," but we also clarified that it did "not involv[e] the scope of the rule itself." <extracted-citation case-ids="11340969" index="70" url="https://cite.case.law/us/468/897/"><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U.S., at 911</a></span>-912</extracted-citation>, <extracted-citation case-ids="11340969" index="71" url="https://cite.case.law/us/468/897/"><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span></extracted-citation>. As for <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Gates</a></span>,</em>only Justice White's separate opinion (joined by no other Justice) discussed <em><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">DeFillippo</a></span>,</em>and it acknowledged that "<span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo"><em>DeFillippo</em></a></span>did <a class="page-label" data-citation-index="1" data-label="539" href="#p539" id="p539">*539</a>not modify the exclusionary rule itself" but instead "upheld the validity of an arrest." <extracted-citation case-ids="6187462" index="72" url="https://cite.case.law/us/462/213/"><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#256" aria-description="Citation for case: Illinois v. Gates">462 U.S., at 256</a></span>, n. 12</extracted-citation>, <extracted-citation case-ids="6187462" index="73" url="https://cite.case.law/us/462/213/"><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">103 S.Ct. 2317</a></span></extracted-citation>(opinion concurring in judgment).</p>
<p id="p-37">Heien is correct that in a number of decisions we have looked to the reasonableness of an officer's legal error in the course of considering the appropriate remedy for a constitutional violation, instead of whether there was a violation at all. See, <em>e.g.,</em><em>Davis v. United States,</em>564 U.S. ----, ----, <extracted-citation case-ids="5928256,12450488" index="74" url="https://cite.case.law/s-ct/131/2419/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">131 S.Ct. 2419</a></span></extracted-citation>, 2429-30, <extracted-citation case-ids="12450488,5928256" index="75" url="https://cite.case.law/l-ed-2d/180/285/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">180 L.Ed.2d 285</a></span></extracted-citation> (2011)(exclusionary rule); <em>Illinois v. Krull,</em><extracted-citation case-ids="1131469" index="76" url="https://cite.case.law/us/480/340/#p359"><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">480 U.S. 340</a></span></extracted-citation>, 359-360, <extracted-citation case-ids="1131469" index="77" url="https://cite.case.law/us/480/340/#p359"><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">107 S.Ct. 1160</a></span></extracted-citation>, <extracted-citation case-ids="1131469" index="78" url="https://cite.case.law/us/480/340/#p359"><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">94 L.Ed.2d 364</a></span></extracted-citation> (1987)(exclusionary rule); <em>Wilson v. Layne,</em><extracted-citation case-ids="11133554" index="79" url="https://cite.case.law/us/526/603/#p615"><span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">526 U.S. 603</a></span></extracted-citation>, 615, <extracted-citation case-ids="11133554" index="80" url="https://cite.case.law/us/526/603/#p615"><span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">119 S.Ct. 1692</a></span></extracted-citation>, <extracted-citation case-ids="11133554" index="81" url="https://cite.case.law/us/526/603/#p615"><span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">143 L.Ed.2d 818</a></span></extracted-citation> (1999)(qualified immunity); <em>Anderson v. Creighton,</em><extracted-citation case-ids="28199" index="82" url="https://cite.case.law/us/483/635/#p641"><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">483 U.S. 635</a></span></extracted-citation>, 641, <extracted-citation case-ids="28199" index="83" url="https://cite.case.law/us/483/635/#p641"><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">107 S.Ct. 3034</a></span></extracted-citation>, <extracted-citation case-ids="28199" index="84" url="https://cite.case.law/us/483/635/#p641"><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">97 L.Ed.2d 523</a></span></extracted-citation> (1987)(qualified immunity). In those cases, however, we had already found or assumed a Fourth Amendment violation. An officer's mistaken view that the conduct at issue did <em>not</em>give rise to such a violation-no matter how reasonable-could not change that ultimate conclusion. See Brief for Respondent 29-31; Brief for United States as <em>Amicus Curiae</em>30, n. 3. Any consideration of the reasonableness of an officer's mistake was therefore limited to the separate matter of remedy.</p>
<p id="p-38">Here, by contrast, the mistake of law relates to the antecedent question of whether it was reasonable for an officer to suspect that the defendant's conduct was illegal. If so, there was no violation of the Fourth Amendment in the first place. None of the cases Heien or the dissent cites precludes a court from considering a reasonable mistake of law in addressing that question. Cf. <em>Herring v. United States,</em><extracted-citation case-ids="3679252" index="85" url="https://cite.case.law/us/555/135/#p139"><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/" aria-description="Citation for case: Herring v. United States">555 U.S. 135</a></span></extracted-citation>, 139, <extracted-citation case-ids="3679252" index="86" url="https://cite.case.law/us/555/135/#p139"><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/" aria-description="Citation for case: Herring v. United States">129 S.Ct. 695</a></span></extracted-citation>, <extracted-citation case-ids="3679252" index="87" url="https://cite.case.law/us/555/135/#p139"><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/" aria-description="Citation for case: Herring v. United States">172 L.Ed.2d 496</a></span></extracted-citation> (2009)(assuming a Fourth Amendment violation while rejecting application of the exclusionary rule, but noting that "[w]hen a probable-cause determination was based on reasonable but mistaken assumptions, the person subjected to a search or seizure has not necessarily been the victim of a constitutional violation").</p>
<p id="p-39">Heien also contends that the reasons the Fourth Amendment allows some errors of fact do not extend to errors of law. Officers in the field must make factual assessments on the fly, Heien notes, and so deserve a margin of error. In Heien's view, no such margin is appropriate for questions of law: The statute here either requires one working brake light or two, and the answer does not turn on anything "an officer might suddenly confront in the field." Brief for Petitioner 21. But Heien's point does not consider the reality that an officer may "suddenly confront" a situation in the field as to which the application of a statute is unclear-however clear it may later become. A law prohibiting "vehicles" in the park either covers Segways or not, see A. Scalia &amp; B. Garner, Reading Law: The Interpretation of Legal Texts 36-38 (2012), but an officer will nevertheless have to make a quick decision on the law the first time one whizzes by.</p>
<p id="p-40">Contrary to the suggestion of Heien and <em>amici,</em>our decision does not discourage officers from learning the law. The Fourth Amendment tolerates only <em>reasonable</em>mistakes, and those mistakes-whether of fact or of law-must be <em>objectively</em>reasonable. We do not examine the subjective understanding of the particular officer involved. Cf. <em>Whren v. United States,</em><extracted-citation case-ids="11746960" index="88" url="https://cite.case.law/us/517/806/#p813"><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U.S. 806</a></span></extracted-citation>, 813, <extracted-citation case-ids="11746960" index="89" url="https://cite.case.law/us/517/806/#p813"><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S.Ct. 1769</a></span></extracted-citation>, <extracted-citation case-ids="11746960" index="90" url="https://cite.case.law/us/517/806/#p813"><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L.Ed.2d 89</a></span></extracted-citation> (1996). And the inquiry is not as forgiving as the one employed in the distinct context of deciding whether an officer is entitled to qualified immunity for a constitutional or statutory violation. Thus, an officer can gain no Fourth Amendment advantage through a sloppy <a class="page-label" data-citation-index="1" data-label="540" href="#p540" id="p540">*540</a>study of the laws he is duty-bound to enforce.</p>
<p id="p-41">Finally, Heien and <em>amici</em>point to the well-known maxim, "Ignorance of the law is no excuse," and contend that it is fundamentally unfair to let police officers get away with mistakes of law when the citizenry is accorded no such leeway. Though this argument has a certain rhetorical appeal, it misconceives the implication of the maxim. The true symmetry is this: Just as an individual generally cannot escape criminal liability based on a mistaken understanding of the law, so too the government cannot impose criminal liability based on a mistaken understanding of the law. If the law required two working brake lights, Heien could not escape a ticket by claiming he reasonably thought he needed only one; if the law required only one, Sergeant Darisse could not issue a valid ticket by claiming he reasonably thought drivers needed two. But just because mistakes of law cannot justify either the imposition or the avoidance of criminal liability, it does not follow that they cannot justify an investigatory stop. And Heien is not appealing a brake-light ticket; he is appealing a cocaine-trafficking conviction as to which there is no asserted mistake of fact or law.</p>
<p id="p-42">III</p>
<p id="p-43">Here we have little difficulty concluding that the officer's error of law was reasonable. Although the North Carolina statute at issue refers to "<em>a</em>stop lamp," suggesting the need for only a single working brake light, it also provides that "[t]he stop lamp may be incorporated into a unit with one or more <em>other</em>rear lamps." N.C. Gen.Stat. Ann. § 20-129(g)(emphasis added). The use of "other" suggests to the everyday reader of English that a "stop lamp" is a type of "rear lamp." And another subsection of the same provision requires that vehicles "have all originally equipped rear lamps or the equivalent in good working order," § 20-129(d), arguably indicating that if a vehicle has multiple "stop lamp[s]," all must be functional.</p>
<p id="p-44">The North Carolina Court of Appeals concluded that the "rear lamps" discussed in subsection (d) do not include brake lights, but, given the "other," it would at least have been reasonable to think they did. Both the majority and the dissent in the North Carolina Supreme Court so concluded, and we agree. See <extracted-citation case-ids="4357764" index="91" url="https://cite.case.law/nc/366/271/#p272"><span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/" aria-description="Citation for case: State v. Heien">366 N.C., at 282</a></span>-283</extracted-citation>, <extracted-citation index="92" url="https://cite.case.law/citations/?q=737%20S.E.2d%20351"><span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/" aria-description="Citation for case: State v. Heien">737 S.E.2d, at 358</a></span>-359</extracted-citation>; <span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/#283" aria-description="Citation for case: State v. Heien"><em>id.,</em>at 283</a></span>, <extracted-citation index="93" url="https://cite.case.law/citations/?q=737%20S.E.2d%20351"><span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/#359" aria-description="Citation for case: State v. Heien">737 S.E.2d, at 359</a></span></extracted-citation>(Hudson, J., dissenting) (calling the Court of Appeals' decision "surprising"). This "stop lamp" provision, moreover, had never been previously construed by North Carolina's appellate courts. See <span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/#283" aria-description="Citation for case: State v. Heien"><em>id.,</em>at 283</a></span>, <extracted-citation index="94" url="https://cite.case.law/citations/?q=737%20S.E.2d%20351"><span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/#359" aria-description="Citation for case: State v. Heien">737 S.E.2d, at 359</a></span></extracted-citation>(majority opinion). It was thus objectively reasonable for an officer in Sergeant Darisse's position to think that Heien's faulty right brake light was a violation of North Carolina law. And because the mistake of law was reasonable, there was reasonable suspicion justifying the stop.</p>
<p id="p-45">The judgment of the Supreme Court of North Carolina is</p>
<p id="p-46"><em>Affirmed.</em></p>
<p id="p-47">Justice KAGAN, with whom Justice GINSBURGjoins, concurring.</p>
<p id="p-48">I concur in full in the Court's opinion, which explains why certain mistakes of law can support the reasonable suspicion needed to stop a vehicle under the Fourth Amendment. In doing so, the Court correctly emphasizes that the "Fourth Amendment tolerates only ... <em>objectively</em>reasonable" mistakes of law. <em>Ante,</em>at 539. And the Court makes clear that the inquiry into whether an officer's mistake of law counts as objectively reasonable "is not as forgiving as the one employed in the distinct context of deciding whether an officer <a class="page-label" data-citation-index="1" data-label="541" href="#p541" id="p541">*541</a>is entitled to qualified immunity." <em><extracted-citation index="95" url="https://cite.case.law/citations/?q=737%20S.E.2d%20351">Ibid</extracted-citation></em><extracted-citation index="95" url="https://cite.case.law/citations/?q=737%20S.E.2d%20351">.</extracted-citation> I write separately to elaborate briefly on those important limitations.<footnotemark>1</footnotemark></p>
<p id="p-49">First, an officer's "subjective understanding" is irrelevant: As the Court notes, "[w]e do not examine" it at all. <em><span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/" aria-description="Citation for case: State v. Heien">Ibid.</a></span></em>That means the government cannot defend an officer's mistaken legal interpretation on the ground that the officer was unaware of or untrained in the law. And it means that, contrary to the dissenting opinion in the court below, an officer's reliance on "an incorrect memo or training program from the police department" makes no difference to the analysis. <extracted-citation case-ids="4357764" index="96" url="https://cite.case.law/nc/366/271/#p272"><span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/" aria-description="Citation for case: State v. Heien">366 N.C. 271</a></span></extracted-citation>, 284, <extracted-citation index="97" url="https://cite.case.law/citations/?q=737%20S.E.2d%20351"><span class="citation" data-id="6723434"><a href="/opinion/6836290/state-v-heien/" aria-description="Citation for case: State v. Heien">737 S.E.2d 351</a></span></extracted-citation>, 360 (2012)(Hudson, J., dissenting). Those considerations pertain to the officer's subjective understanding of the law and thus cannot help to justify a seizure.</p>
<p id="p-50">Second, the inquiry the Court permits today is more demanding than the one courts undertake before awarding qualified immunity. See Tr. of Oral Arg. 51 (Solicitor General stating that the two tests "require essentially the opposite" showings); Brief for Respondent 31-32 (making a similar point). Our modern qualified immunity doctrine protects "all but the plainly incompetent or those who knowingly violate the law." <em>Ashcroft v. al-Kidd,</em>563 U.S. ----, ----, <extracted-citation case-ids="5924024,12459540" index="98" url="https://cite.case.law/s-ct/131/2074/"><span class="citation" data-id="7262676"><a href="/opinion/7344719/ashcroft-v-al-kidd/" aria-description="Citation for case: Ashcroft v. al-Kidd">131 S.Ct. 2074</a></span></extracted-citation>, 2085, <extracted-citation case-ids="5924024,12459540" index="99" url="https://cite.case.law/s-ct/131/2074/"><span class="citation" data-id="7262676"><a href="/opinion/7344719/ashcroft-v-al-kidd/" aria-description="Citation for case: Ashcroft v. al-Kidd">179 L.Ed.2d 1149</a></span></extracted-citation> (2011)(quoting <em>Malley v. Briggs,</em><extracted-citation case-ids="6202676" index="100" url="https://cite.case.law/us/475/335/#p341"><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/" aria-description="Citation for case: Malley v. Briggs">475 U.S. 335</a></span></extracted-citation>, 341, <extracted-citation case-ids="6202676" index="101" url="https://cite.case.law/us/475/335/#p341"><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/" aria-description="Citation for case: Malley v. Briggs">106 S.Ct. 1092</a></span></extracted-citation>, <extracted-citation case-ids="6202676" index="102" url="https://cite.case.law/us/475/335/#p341"><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/" aria-description="Citation for case: Malley v. Briggs">89 L.Ed.2d 271</a></span></extracted-citation> (1986)). By contrast, Justice Story's opinion in <em>The Friendship,</em><extracted-citation case-ids="11652906" index="103" url="https://cite.case.law/f-cas/9/825/#p826"><span class="citation" data-id="8631400"><a href="/opinion/8651576/the-friendship/" aria-description="Citation for case: The Friendship">9 F.Cas. 825</a></span></extracted-citation>, 826 (No. 5,125)(C.C.D.Mass.1812) (cited <em>ante,</em> at 537), suggests the appropriate standard for deciding when a legal error can support a seizure: when an officer takes a reasonable view of a "vexata questio" on which different judges "h[o]ld opposite opinions." See Brief for United States as <em>Amicus Curiae</em> 26 (invoking that language). Or to make the same point without the Latin, the test is satisfied when the law at issue is "so doubtful in construction" that a reasonable judge could agree with the officer's view. <em>The Friendship,</em><extracted-citation case-ids="11652906" index="104" url="https://cite.case.law/f-cas/9/825/#p826"><span class="citation" data-id="8631400"><a href="/opinion/8651576/the-friendship/" aria-description="Citation for case: The Friendship">9 F.Cas., at 826</a></span></extracted-citation>.</p>
<p id="p-51">A court tasked with deciding whether an officer's mistake of law can support a seizure thus faces a straightforward question of statutory construction. If the statute is genuinely ambiguous, such that overturning the officer's judgment requires hard interpretive work, then the officer has made a reasonable mistake. But if not, not. As the Solicitor General made the point at oral argument, the statute must pose a "really difficult" or "very hard question of statutory interpretation." Tr. of Oral Arg. 50. And indeed, both North Carolina and the Solicitor General agreed that such cases will be "exceedingly rare." Brief for Respondent 17; Tr. of Oral Arg. 48.</p>
<p id="p-52">The Court's analysis of Sergeant Darisse's interpretation of the North Carolina law at issue here appropriately reflects these principles. As the Court explains, see <em>ante,</em>at 540, the statute requires every car on the highway to have "a stop lamp," in the singular.N.C. Gen.Stat. Ann. § 20-129(g) (2007). But the statute goes on to state that a stop lamp (or, in more modern terminology, brake light) "may be incorporated into a unit with one or more <em>other</em> <a class="page-label" data-citation-index="1" data-label="542" href="#p542" id="p542">*542</a>rear lamps," suggesting that a stop lamp itself qualifies as a rear lamp. <em><extracted-citation case-ids="11652906" index="105" url="https://cite.case.law/f-cas/9/825/#p826">Ibid.</extracted-citation></em> (emphasis added). And the statute further mandates that every car have "<em>all</em> originally equipped rear lamps ... in good working order." § 20-129(d)(emphasis added). The North Carolina Court of Appeals dealt with the statute's conflicting signals in one way (deciding that a brake light is <em>not</em> a rear lamp, and so only one needs to work); but a court could easily take the officer's view (deciding that a brake light <em>is</em>a rear lamp, and if a car comes equipped with more than one, as modern cars do, all must be in working order). The critical point is that the statute poses a quite difficult question of interpretation, and Sergeant Darisse's judgment, although overturned, had much to recommend it. I therefore agree with the Court that the traffic stop he conducted did not violate the Fourth Amendment.</p>
<footnote label="*">
<p id="p-80">The syllabus constitutes no part of the opinion of the Court but has been prepared by the Reporter of Decisions for the convenience of the reader. See <em>United States v. Detroit Timber &amp; Lumber Co.,</em><extracted-citation case-ids="8294520" index="106" url="https://cite.case.law/us/200/321/#p337"><span class="citation" data-id="96405"><a href="/opinion/96405/united-states-v-detroit-timber-lumber-co/" aria-description="Citation for case: United States v. Detroit Timber &amp; Lumber Co.">200 U.S. 321</a></span></extracted-citation>, 337, <extracted-citation case-ids="8294520" index="107" url="https://cite.case.law/us/200/321/#p337"><span class="citation" data-id="96405"><a href="/opinion/96405/united-states-v-detroit-timber-lumber-co/" aria-description="Citation for case: United States v. Detroit Timber &amp; Lumber Co.">26 S.Ct. 282</a></span></extracted-citation>, <extracted-citation case-ids="8294520" index="108" url="https://cite.case.law/us/200/321/#p337"><span class="citation" data-id="96405"><a href="/opinion/96405/united-states-v-detroit-timber-lumber-co/" aria-description="Citation for case: United States v. Detroit Timber &amp; Lumber Co.">50 L.Ed. 499</a></span></extracted-citation>.</p>
</footnote>
<footnote label="1">
<p id="p-82">I note in addition, as does the Court, that one kind of mistaken legal judgment-an error about the contours of the Fourth Amendment itself-can never support a search or seizure. See <em>ante,</em>at 539 ("An officer's mistaken view that" conduct does "<em>not</em>give rise to" a Fourth Amendment violation, "no matter how reasonable," cannot change a court's "ultimate conclusion" that such a violation has occurred). As the Solicitor General has explained, mistakes about the requirements of the Fourth Amendment "violate the Fourth Amendment even when they are reasonable." Brief for United States as <em>Amicus Curiae</em>30, n. 3; see Brief for Respondent 29 (stating the same view).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Heller v. New York.md  (`case`, 5 assertions)

### content_page

```
---
title: Heller v. New York
type: case
citation: "413 U.S. 483 (1973)"
parallel_cite: "93 S. Ct. 2789; 37 L. Ed. 2d 745"
neutral_cite: 1973 U.S. LEXIS 30
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1973
date_decided: 1973-06-25
docket: No. 71-1043
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
  opinion_url: "https://www.courtlistener.com/opinion/108853/heller-v-new-york/"
  cluster_id: 108853
  opinion_id: null
  identity_checked: true
lake:
  record_id: Heller v. New York
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Particularity]]"
    role: Key
related:
  - "[[The Warrant Requirement]]"
  - "[[Marcus v. Search Warrant]]"
  - "[[Roaden v. Kentucky]]"
  - "[[Stanford v. Texas]]"
  - "[[A Quantity of Copies of Books v. Kansas]]"
tags:
  - case
  - warrant-requirement
  - expressive-materials
  - prior-restraint
  - first-amendment
holding: "A single copy of an allegedly obscene film may be seized as evidence under a warrant issued by a neutral magistrate on a probable-cause determination without a prior adversary hearing on obscenity, provided a prompt post-seizure adversary hearing is available and, if the seizure would halt exhibition, the exhibitor is allowed to copy the film."
---

# Heller v. New York

*413 U.S. 483 (1973)* (No. 71-1043) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 108853 → lead opinion 108853; quote string-matched to the CL opinion text 2026-07-07. CAPTION TRAP: this is *Heller v. New York* (1973, obscene-film seizure), NOT *District of Columbia v. Heller* (2008, Second Amendment). S9 promotes. -->

## Background
A New York judge personally viewed the film "Blue Movie" during a public showing at a Manhattan theater, then issued a warrant under which a single copy of the film was seized as evidence and the theater's manager, Heller, was arrested. Heller was convicted of obscenity offenses. He challenged the seizure, arguing that taking the film without a prior adversary hearing on whether it was obscene amounted to an unconstitutional prior restraint on expression.

## Issue
Whether the Fourth and First Amendments require an adversary hearing on obscenity before a single copy of a film may be seized as evidence under a warrant.

## Rule
Seizing films to suppress or block their distribution is a prior restraint bearing a heavy presumption against constitutional validity, but seizing a single copy to preserve it as evidence — where continued exhibition is not thereby prevented — is a different matter. The Court held: "If such a seizure is pursuant to a warrant, issued after a determination of probable cause by a neutral magistrate, and, following the seizure, a prompt judicial determination of the obscenity issue in an adversary proceeding is available at the request of any interested party, the seizure is constitutionally permissible." — 413 U.S. at 492. ^pin-492

It added that if other copies are unavailable, the trial court should permit the seized film to be copied so exhibition can continue pending the obscenity determination; otherwise the film must be returned.

## Application
The judge's own viewing supplied probable cause; only a single evidentiary copy was seized; and nothing showed the seizure prevented continued exhibition. New York's procedure — a neutral magistrate's probable-cause determination plus an available prompt post-seizure adversary hearing — furnished adequate First Amendment safeguards, so no adversary hearing was required before the evidentiary seizure. A prior hearing would not have materially increased First Amendment protection given those safeguards.

## Conclusion
The judgment of the New York Court of Appeals was **[[Reading and Citing Cases#vacated|vacated]]** and the case **[[Reading and Citing Cases#on-remand|remanded]]**, for reconsideration of the substantive obscenity standards in light of *Miller v. California* and *Paris Adult Theatre I v. Slaton*. Burger, C.J., delivered the opinion of the Court; Douglas, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]]; Brennan, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], joined by Stewart and Marshall, JJ.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Heller v. New York* supplies the affirmative, officer-facing operational rule that complements the prior-restraint prohibitions of *[[Marcus v. Search Warrant]]* and *[[Roaden v. Kentucky]]*: how a single copy of expressive material may lawfully be seized as evidence under a warrant, with a prompt post-seizure adversary hearing as the safeguard. **Caption note:** it is unrelated to *District of Columbia v. Heller* (2008), the Second Amendment decision.

## Appears on
- [[Particularity]] — *Key*

## Sources
- [*Heller v. New York*, 413 U.S. 483 (1973)](https://www.courtlistener.com/opinion/108853/heller-v-new-york/) — pinpoint: 492 (Opinion of the Court, holding; Burger, C.J.); quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0052727998cfea88", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "413 U.S. 483 (1973)", "court": "U.S. Supreme Court", "neutral_cite": "1973 U.S. LEXIS 30", "official_citation_present": true, "parallel_cite": "93 S. Ct. 2789; 37 L. Ed. 2d 745", "title": "Heller v. New York", "year": "1973"}}
{"assertion_id": "1b35e94a150dfb12", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A single copy of an allegedly obscene film may be seized as evidence under a warrant issued by a neutral magistrate on a probable-cause determination without a prior adversary hearing on obscenity, provided a prompt post-seizure adversary hearing is available and, if the seizure would halt exhibition, the exhibitor is allowed to copy the film.", "title": "Heller v. New York"}}
{"assertion_id": "98b13d916411ddb6", "dimension": "support", "kind": "home_role", "locator": {"home": "Particularity"}, "payload": {"home": "Particularity", "role": "Key", "title": "Heller v. New York"}}
{"assertion_id": "021f87f827a80173", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Heller v. New York", "varies_by_point": "false"}}
{"assertion_id": "4acaacb0f9f8289c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Heller v. New York"}}
```

### lake record — Heller v. New York

```json
{
  "schema_version": "s2.v1",
  "record_id": "Heller v. New York",
  "status": "under_review",
  "identity": {
    "case_name": "Heller v. New York",
    "case_name_short": "Heller",
    "case_name_full": "Heller v. New York",
    "input_case_name": "Heller v. New York",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1973-06-25",
    "year": 1973,
    "docket": "No. 71-1043",
    "cluster_id": 108853,
    "lead_opinion_id": 9425413,
    "sibling_ids": [],
    "absolute_url": "/opinion/108853/heller-v-new-york/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "413 U.S. 483",
      "volume": "413",
      "reporter": "U.S.",
      "page": "483",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "93 S. Ct. 2789",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2789",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 L. Ed. 2d 745",
        "volume": "37",
        "reporter": "L. Ed. 2d",
        "page": "745",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1973 U.S. LEXIS 30",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "30",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "413 U.S. 483",
        "volume": "413",
        "reporter": "U.S.",
        "page": "483",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 S. Ct. 2789",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2789",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 L. Ed. 2d 745",
        "volume": "37",
        "reporter": "L. Ed. 2d",
        "page": "745",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. LEXIS 30",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "30",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "413 U.S. 483",
    "official_selection": {
      "court_class": "scotus",
      "selected": "413 U.S. 483",
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
    "date_created": "2026-07-06T13:44:22Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:44:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:44:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:44:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:44:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "heller-v-new-york--108853",
      "to_record_id": "Heller v. New York",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Heller v. New York

```
<opinion type="majority">
<author id="b528-10">Me. Chief Justice BuRGer</author>
<p id="ARM">delivered the opinion of of the Court.</p>
<p id="b528-11">We granted certiorari in this case to determine whether a judicial officer authorized to issue warrants, who has viewed a film and finds it to be obscene, can issue a constitutionally valid warrant for the film’s seizure as evidence in a prosecution against the exhibitor, without first conducting an adversary hearing on the issue of probable obscenity.</p>
<p id="b529-4"><page-number citation-index="1" label="485">*485</page-number>Petitioner was manager of a commercial movie theater in the Greenwich Village area of New York City. On July 29, 1969, a film called “Blue Movie” was exhibited there. The film depicts a nude couple engaged in ultimate sexual acts. Three police officers saw part of the film. Apparently on the basis of their observations, an assistant district attorney of New York County requested a judge of the New York Criminal Court to see a performance. On July 31, 1969, the judge, accompanied by a police inspector, purchased a ticket and saw the entire film. There were about 100 other persons in the audience. Neither the judge nor the police inspector recalled any signs restricting admission to adults.<footnotemark>1</footnotemark></p>
<p id="b529-5">At the end of the film, the judge, without any discussions with the police inspector, signed a search warrant for the seizure of the film and three “John Doe” warrants for the arrest of the theater manager, the projectionist, and the ticket taker, respectively. No one at the theater was notified or consulted prior to the issuance of the warrants. The judge signed the warrants because “it was, and is my opinion that that film is obscene, and was obscene as I saw it then under the definition of obscene, that is [in] . . . section 235.00 of the Penal Law.” Exhibition of an obscene film violates New York Penal Law § 235.05.<footnotemark>2</footnotemark></p>
<p id="b530-3"><page-number citation-index="1" label="486">*486</page-number>The warrants were immediately executed by police officers. Three reels, composing a single copy of the film, were seized. Petitioner, the theater manager, was arrested, as were the projectionist and the ticket taker.<footnotemark>3</footnotemark> No pretrial motion was made for the return of the film or for its suppression as evidence. Nor did petitioner make a pretrial claim that seizure of the film prevented its exhibition by use of another copy, and the record does not conclusively indicate whether such a copy was available. On September 16, 1969, 47 days after his arrest and the seizure of the movie, petitioner came to trial, a jury having been waived, before three judges of the New York City Criminal Court.</p>
<p id="b531-4"><page-number citation-index="1" label="487">*487</page-number>At trial, the prosecution’s case rested almost solely on testimony concerning the arrests and the seizure of the film, together with the introduction into evidence of the seized film itself. The film was exhibited to the trial judges. The defense offered three “expert” witnesses: an author, a professor of sociology, and a newspaper writer. These witnesses testified that the film had social, literary, and artistic importance in illustrating “a growing and important point of view about sexual behavior” as well as providing observations “about the political and social situation in this country today. . . .” Petitioner testified that the theater’s employees were instructed not to admit persons who appeared to be under 18 years of age, unless they “had identification” that they were 18. Petitioner also testified that there was a sign at the box office stating that “no one under 17 [would be] admitted.” Both at the end of the prosecution’s case and his own case, petitioner moved to dismiss the indictment on the ground that the seizure of the film, without a prior adversary hearing, violated the Fourteenth Amendment.</p>
<p id="b531-5">At the close of trial on September 17, 1969, petitioner was found guilty by all three judges of violating New York Penal Law § 235.05. On appeal, both the Supreme Court of the State of New York, Appellate Term, and the Court of Appeals of the State of New York viewed the film and affirmed petitioner’s conviction. The Court of Appeals, relying on this Court’s opinion in <em>Lee Art Theatre </em>v. <em>Virginia, </em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/#637" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">392 U. S. 636, 637</a></span> (1968), held that an adversary hearing was not required prior to seizure of the film, and that the judicial determination which occurred prior to seizure in this case was constitutionally sufficient. In so holding, the Court of Appeals explicitly disapproved, as going “beyond any requirement imposed on State courts by the Supreme <page-number citation-index="1" label="488">*488</page-number>Court,” <em>Astro Cinema Corp. </em>v. <em>Mackell, </em><span class="citation" data-id="288631"><a href="/opinion/288631/astro-cinema-corp-inc-john-justin-and-jess-rockman-v-thomas-j-mackell/" aria-description="Citation for case: Astro Cinema Corp. Inc., John Justin and Jess Rockman v....">422 F. 2d 293</a></span> (CA2 1970), and <em>Bethview Amusement Corp. </em>v. <em>Cahn, </em><span class="citation" data-id="8881513"><a href="/opinion/8895042/bethview-amusement-corp-v-cahn/" aria-description="Citation for case: Bethview Amusement Corp. v. Cahn">416 F. 2d 410</a></span> (CA2 1969), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./397/920/">397 U. S. 920</a></span> (1970), cases requiring an adversary hearing prior to any seizure of movie film. 29 N. Y. 2d 319, 323, <span class="citation" data-id="5526705"><a href="/opinion/5678748/people-v-heller/#653" aria-description="Citation for case: People v. Heller">277 N. E. 2d 651, 653</a></span> (1971).</p>
<p id="b532-5">We affirm this holding of the Court of Appeals of the State of New York. This Court has never held, or even implied, that there is an absolute First or Fourteenth Amendment right to a prior adversary hearing applicable to all cases where allegedly obscene material is seized. See <em>Times Film Corp. </em>v. <em>Chicago, </em><span class="citation" data-id="9422106"><a href="/opinion/106162/times-film-corp-v-city-of-chicago/" aria-description="Citation for case: Times Film Corp. v. City of Chicago">365 U. S. 43</a></span> (1961); <em>Kingsley Books, Inc. </em>v. <em>Brown, </em><span class="citation" data-id="9421490"><a href="/opinion/105544/kingsley-books-inc-v-brown/" aria-description="Citation for case: Kingsley Books, Inc. v. Brown">354 U. S. 436</a></span>, 440-442-(1957). In particular, there is no such absolute right where allegedly obscene material is seized, pursuant to a warrant, to preserve the material as evidence in a criminal prosecution. In <em>Lee Art Theatre </em>v. <em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">Virginia, supra,</a></span> </em>the Court went so far as to suggest that it was an open question whether a judge need “have viewed the motion picture before issuing the warrant.”<footnotemark>4</footnotemark> Here the judge viewed the entire film and, indeed, witnessed the alleged criminal act. It is not contested that the judge was a “neutral, detached magistrate,” that he had a full opportunity for independent judi<page-number citation-index="1" label="489">*489</page-number>cial determination of probable cause prior to issuing the warrant, and that he was able to “focus searchingly on the question of obscenity.” See <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#731" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717, 731-733</a></span> (1961). Cf. <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#449" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 449-453</a></span> (1971); <em>Giordenello </em>v. <em>United States, </em><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#485" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 485-486</a></span> (1958); <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14-15</a></span> (1948).</p>
<p id="b533-5">In <em>United States </em>v. <em>Thirty-seven Photographs, </em><span class="citation" data-id="9424558"><a href="/opinion/108332/united-states-v-thirty-seven-37-photographs/" aria-description="Citation for case: United States v. Thirty-Seven (37) Photographs">402 U. S. 363</a></span> (1971), and <em>Freedman </em>v. <em>Maryland, </em><span class="citation" data-id="9422964"><a href="/opinion/106987/freedman-v-maryland/" aria-description="Citation for case: Freedman v. Maryland">380 U. S. 51</a></span> (1965), we held that “ ‘because only a judicial determination in an adversary proceeding ensures the necessary sensitivity to freedom of expression, only a procedure requiring a judicial determination suffices to impose a valid <em>final restraint.’ ” </em><span class="citation" data-id="9424558"><a href="/opinion/108332/united-states-v-thirty-seven-37-photographs/#367" aria-description="Citation for case: United States v. Thirty-Seven (37) Photographs">402 U. S., at 367</a></span>, quoting <span class="citation" data-id="9422964"><a href="/opinion/106987/freedman-v-maryland/#58" aria-description="Citation for case: Freedman v. Maryland">380 U. S., at 58</a></span> (emphasis added). Those cases involved, respectively, seizure of imported materials by federal customs agents and state administrative licensing of motion pictures, both civil procedures directed at absolute suppression of the materials themselves. Even in those cases, we did not require that the adversary proceeding must take place prior to <em>initial </em>seizure. Rather, it was held that a judicial determination must occur “promptly so that administrative delay does not in itself become a form of censorship.”<footnotemark>5</footnotemark> <em>United States </em>v. <em>Thirty-seven Photographs, supra, </em>at 367; <em>Freedman </em>v. <em>Maryland, </em><page-number citation-index="1" label="490">*490</page-number><em>supra, </em>at 57—59. See <em>Blount </em>v. <em>Rizzi, </em><span class="citation" data-id="108228"><a href="/opinion/108228/blount-v-rizzi/#419" aria-description="Citation for case: Blount v. Rizzi">400 U. S. 410, 419-421</a></span> (1971); <em>Teitel Film Corp. </em>v. <em>Cusack, </em><span class="citation" data-id="107612"><a href="/opinion/107612/teitel-film-corp-v-cusack/#141" aria-description="Citation for case: Teitel Film Corp. v. Cusack">390 U. S. 139, 141-142</a></span> (1968); <em>Bantam Books, Inc. </em>v. <em>Sullivan, </em><span class="citation" data-id="9422525"><a href="/opinion/106530/bantam-books-inc-v-sullivan/#70" aria-description="Citation for case: Bantam Books, Inc. v. Sullivan">372 U. S. 58, 70-71</a></span> (1963).</p>
<p id="b534-5">In this case, of course, the film was not subjected to any form of “final restraint,” in the sense of being enjoined from exhibition or threatened with destruction. A copy of the film was temporarily detained in order to <em>preserve it as evidence. </em>There has been no showing that the seizure of a copy of the film precluded its continued exhibition. Nor, in this case, did temporary restraint in itself “become a form of censorship,” even making the doubtful assumption that no other copies of the film existed. Cf. <em>United States </em>v. <em>Thirty-seven Photographs, supra, </em>at 367; <em>Freedman </em>v. <span class="citation" data-id="9422964"><a href="/opinion/106987/freedman-v-maryland/#57" aria-description="Citation for case: Freedman v. Maryland"><em>Maryland, supra, </em>at 57-59</a></span>. A judicial determination of obscenity, following a fully adversary trial, occurred within 48 days of the temporary seizure. Petitioner made no pretrial motions seeking return of the film or challenging its seizure, nor did he request expedited judicial consideration of the obscenity issue, so it is entirely possible that a prompt judicial determination of the obscenity issue in an adversary proceeding could have been obtained if petitioner had desired.<footnotemark>6</footnotemark> Although we have refrained from establishing rigid, specific time deadlines in proceedings involving seizure of allegedly obscene material, we have definitely excluded from any consideration of “promptness” those delays caused by the choice of the defendant. See <em>United States </em>v. <em>Thirty-seven Photographs, supra, </em>at 373-374. In this case, the barrier to a prompt judicial determination of the <page-number citation-index="1" label="491">*491</page-number>obscenity issue in an adversary proceeding was not the State, but petitioner’s decision to waive pretrial motions and reserve the obscenity issue for trial. Cf. <em>Kingsley Books, Inc. </em>v. <em>Brown, </em><span class="citation" data-id="9421490"><a href="/opinion/105544/kingsley-books-inc-v-brown/#439" aria-description="Citation for case: Kingsley Books, Inc. v. Brown">354 U. S., at 439</a></span>.</p>
<p id="b535-5">Petitioner’s reliance on the Court’s decisions in <em>A Quantity of Books </em>v. <em>Kansas, </em><span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">378 U. S. 205</a></span> (1964), and <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717</a></span> (1961), is misplaced. Those cases concerned the seizure of large quantities of books for the sole purpose of their destruction,<footnotemark>7</footnotemark> and this Court held that, in those circumstances, a prior judicial determination of obscenity in an adversary proceeding was required to avoid “danger of abridgment of the right of the public in a free society to unobstructed circulation of nonobscene books.” <em>A Quantity of Books </em>v. <span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/#213" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas"><em>Kansas, supra, </em>at 213</a></span>. We do not disturb this holding. Courts will scrutinize any large-scale seizure of books, films, or other materials presumptively protected under the First Amendment to be certain that the requirements of <em><span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">A Quantity of Books</a></span> </em>and <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span> </em>are fully met. “ ‘Any system of prior restraints of expression comes to this Court bearing a heavy presumption against its constitutional validity.’ ” <em>New York Times Co. </em>v. <em>United States, </em><span class="citation" data-id="9424665"><a href="/opinion/108384/new-york-times-co-v-united-states/#714" aria-description="Citation for case: New York Times Co. v. United States">403 U. S. 713, <page-number citation-index="1" label="492">*492</page-number>714</a></span> (1971), quoting <em>Bantam Books, Inc. </em>v. <em>Sullivan, </em><span class="citation" data-id="9422525"><a href="/opinion/106530/bantam-books-inc-v-sullivan/#70" aria-description="Citation for case: Bantam Books, Inc. v. Sullivan">372 U. S., at 70</a></span>; <em>Organization for a Better Austin </em>v. <em>Keefe, </em><span class="citation" data-id="9424564"><a href="/opinion/108334/organization-for-a-better-austin-v-keefe/#419" aria-description="Citation for case: Organization for a Better Austin v. Keefe">402 U. S. 415, 419</a></span> (1971); <em>Carroll </em>v. <em>Princess Anne, </em><span class="citation" data-id="9423852"><a href="/opinion/107801/carroll-v-president-commissioners-of-princess-anne/#181" aria-description="Citation for case: Carroll v. President &amp; Commissioners of Princess Anne">393 U. S. 175, 181</a></span> (1968). See <em>Near </em>v. <em>Minnesota, </em><span class="citation" data-id="9418724"><a href="/opinion/101773/near-v-minnesota-ex-rel-olson/" aria-description="Citation for case: Near v. Minnesota Ex Rel. Olson">283 U. S. 697</a></span> (1931).</p>
<p id="b536-5">But seizing films to destroy them or to block their distribution or exhibition is a very different matter from seizing a single copy of a film for the <em>bona fide </em>purpose of preserving it as evidence in a criminal proceeding, particularly where, as here, there is no showing or pretrial claim that the seizure of the copy prevented continuing exhibition of the film.<footnotemark>8</footnotemark> If such a seizure is pursuant to a warrant, issued after a determination of probable cause by a neutral magistrate, and, following the seizure, a prompt<footnotemark>9</footnotemark> judicial determination of the obscenity issue in an adversary proceeding is available at the request of any interested party, the seizure is constitutionally permissible. In addition, on a showing to the trial court that other copies of the film are not available to the exhibitor, the court should permit the seized film to be copied so that showing can be <page-number citation-index="1" label="493">*493</page-number>continued pending a judicial determination of the obscenity issue in an adversary proceeding.<footnotemark>10</footnotemark> Otherwise, the film must be returned.<footnotemark>11</footnotemark></p>
<p id="b537-5">With such safeguards, we do not perceive that an adversary hearing <em>prior </em>to a seizure by lawful warrant would materially increase First Amendment protection. Cf. <em>Carroll </em>v. <span class="citation" data-id="9423852"><a href="/opinion/107801/carroll-v-president-commissioners-of-princess-anne/#183" aria-description="Citation for case: Carroll v. President &amp; Commissioners of Princess Anne"><em>Princess Anne, supra, </em>at 183-184</a></span>. The necessity for a prior judicial determination of probable cause will protect against gross abuses, while the availability of a prompt judicial determination in an adversary proceeding following the seizure assures that difficult marginal cases will be fully considered in light of First Amendment guarantees, with only a minimal interference with public circulation pending litigation. The procedure used by New York in this case provides such First Amendment safeguards, while also serving the public interests in full and fair prosecution for obscenity offenses. Counsel for New York has argued that movie films t^nd to “disappear” if adversary hearings are afforded prior to seizure. We take judicial notice that such films may be compact, readily transported for exhibition in other jurisdictions, easily destructible, and particularly susceptible to alteration by cutting and splicing critical parts of film.</p>
<p id="b538-3"><page-number citation-index="1" label="494">*494</page-number>Petitioner also challenged his conviction on substantive, as opposed to procedural, ground arguing that he was convicted under standards of obscenity both over-broad and unconstitutionally vague. In addition, petitioner argues that films shown only to consenting adults in private have a particular claim to constitutional protection. In <em>Miller </em>v. <em>California, ante, </em>p. 15, and <em>Paris Adult Theatre I </em>v. <em>Slaton, ante, </em>p. 49, decided June 21, 1973, we dealt with these substantive issues. A majority of this Court has now approved guidelines for the lawful state regulation of obscene material. The judgment of the Court of Appeals of the State of New York is therefore vacated and this case remanded for the sole purpose of affording the New York courts an opportunity to reconsider these substantive issues in light of <em>Miller </em>and <em>Paris Adult Theatre I. </em>See <em>United States v. 12 200-ft. Reels of Film, ante, </em>at 130 n. 7.</p>
<p id="b538-4">
<em>Vacated and remanded.</em>
</p>
<footnote label="1">
<p id="b529-6"> The prosecution presented no evidence that juveniles were actually present in the theater.</p>
</footnote>
<footnote label="2">
<p id="b529-7"> New York Penal Law §235.05 reads in relevant part:</p>
<blockquote id="b529-8">“A person is guilty of obscenity when, knowing its content and character, he:</blockquote>
<blockquote id="b529-9">“1. Promotes, or possesses with intent to promote, any obscene material; or</blockquote>
<blockquote id="b529-10">"2. Produces, presents or directs an obscene performance or participates in a portion thereof which is obscene or which contributes to its obscenity.</blockquote>
<blockquote id="AlN"><page-number citation-index="1" label="486">*486</page-number>“Obscenity is a class A misdemeanor.”</blockquote>
<p id="Apj">The terms used in § 235.05 are defined by New York Penal Law §235.00, which reads in relevant part:</p>
<blockquote id="A23">“The following definitions are applicable to sections 235.05, 235.10 and 235.15:</blockquote>
<blockquote id="AKL">“1. 'Obscene.' Any material or performance is ‘obscene’ if (a) considered as a whole, its predominant appeal is to prurient, shameful or morbid interest in nudity, sex, excretion, sadism or masochism, and (b) it goes substantially beyond customary limits of candor in describing or representing such matters, and (c) it is utterly without redeeming social value. Predominant appeal shall be judged with reference to ordinary adults unless it appears from the character of the material or the circumstances of its dissemination to be designed for children or other specially susceptible audience.</blockquote>
<blockquote id="A9l">“2. ‘Material’ means anything tangible which is capable of being used or adapted to arouse interest, whether through the medium of reading, observation, sound or in any other manner.</blockquote>
<blockquote id="AUeW">“3. ‘Performance’ means any play, motion picture, dance or other exhibition performed before an audience.</blockquote>
<blockquote id="ACv">“4. ‘Promote’ means to manufacture, issue, sell, give, provide, lend, mail, deliver, transfer, transmute, publish, distribute, circulate, disseminate, present, exhibit or advertise, or to offer or agree to do the same.”</blockquote>
</footnote>
<footnote label="3">
<p id="b530-11"> The cases against the ticket taker and projectionist were dismissed on the motion of the prosecutor.</p>
</footnote>
<footnote label="4">
<p id="b532-6"> “It is true that a judge may read a copy of a book in courtroom or chambers but not as easily arrange to see a motion picture there. However, we need not decide in this case whether the justice of the peace should have viewed the motion picture before issuing the warrant. The procedure under which the warrant issued solely upon the conclusory assertions of the police officer without any inquiry by the justice of the peace into the factual basis for the officer’s conclusions was not a procedure ‘designed to focus searchingly on the question of obscenity,’ <em>[Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717</a></span>], at 732, <em>and </em>therefore fell short of constitutional requirements demanding necessary sensitivity to freedom of expression. See <em>Freedman </em>v. <em>Maryland, </em><span class="citation" data-id="9422964"><a href="/opinion/106987/freedman-v-maryland/#58" aria-description="Citation for case: Freedman v. Maryland">380 U. S. 51, 58-59</a></span>.” <span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/#637" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">392 U. S., at 637</a></span>.</p>
</footnote>
<footnote label="5">
<p id="b533-6"> We further held “(1) there must be assurance, ‘by statute or authoritative judicial construction, that the censor will, within a specified brief period, either issue a license or go to court to restrain showing the film'; (2) ‘[a]ny restraint imposed in advance of a final judicial determination on the merits must similarly be limited to preservation of the status quo for the shortest fixed period compatible with sound judicial resolution’; and (3) ‘the procedure must also assure a prompt final judicial decision’ to minimize the impact of possibly erroneous administrative action. <em>[Freedman </em>v <em><span class="citation" data-id="9422964"><a href="/opinion/106987/freedman-v-maryland/" aria-description="Citation for case: Freedman v. Maryland">Maryland</a></span>, </em>380 U. S.], at 58-59.” <em>United States </em>v. <em>Thirty-seven Photographs, </em>402 U. S., at 367.</p>
</footnote>
<footnote label="6">
<p id="b534-6"> The State of New York has represented that it stands ready to grant “immediate” adversary hearings on pretrial motions challenging seizures of material arguably protected by the First Amendment. No such motion was made by petitioner.</p>
</footnote>
<footnote label="7">
<p id="b535-6"> In particular, <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span> </em>involved seizure by police officers acting pursuant to a general warrant of 11,000 copies of 280 publications. <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#723" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S., at 723</a></span>. Unlike this case, there was no independent judicial determination of obscenity by a neutral, detached magistrate, nor were the seizures made to preserve evidence for a criminal prosecution. <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#732" aria-description="Citation for case: Marcus v. Search Warrant of Property"><em>Id., </em>at 732</a></span>. The sole purpose was to seize the articles as contraband and to cause them “to be publicly destroyed, by burning or otherwise.” <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Id.,</a></span> </em>at 721 n. 6. In <em>A Quantity of Books </em>v. <em>Kansas, </em><span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">378 U. S. 205</a></span> (1964), 1,715 copies of 31 publications were seized by a county sheriff, also without any prior judicial determination of obscenity and, again, for the sole purpose of destroying the publications as contraband. <span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/#206" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas"><em>Id., </em>at 206-209</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b536-6"> In <em>Mishkin </em>v. <em>New York, 383 </em>U. <em>S. 502 </em>(1966), this Court refused to review the legality of a seizure of books challenged under <em>A Quantity of Books, supra, </em>primarily because the record did not reveal the number of books seized as evidence under the warrant or “whether the books seized . . . were on the threshold of dissemination.” <em>Id., </em>at 613. If <em><span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">A Quantity of Books</a></span> </em>applied to <em>all </em>seizures of obscene material, there would have been no need for the Court to abstain from review in <em><span class="citation" data-id="9423181"><a href="/opinion/107189/mishkin-v-new-york/" aria-description="Citation for case: Mishkin v. New York">Mishkin</a></span>, </em>since the parties had conceded that there was no prior adversary hearing. This is not to say that multiple copies of a single film may be seized as purely cumulative evidence, or that a State may circumvent Marcus or <em><span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">A Quantity of Books</a></span> </em>by incorporating, as an element of a criminal offense, the number of copies of the obscene materials involved.</p>
</footnote>
<footnote label="9">
<p id="b536-7"> By “prompt,” we mean the shortest period “compatible with sound judicial resolution.” See <em>United States </em>v. <em>Thirty-seven Photographs, </em>402 U. S., at 367; <em>Blount </em>v. <em>Rizzi, </em><span class="citation" data-id="108228"><a href="/opinion/108228/blount-v-rizzi/#417" aria-description="Citation for case: Blount v. Rizzi">400 U. S. 410, 417</a></span> (1971); <em>Freedman </em>v. <em>Maryland, </em><span class="citation multiple-matches"><a href="/c/U.%20S./380/61/">380 U. S. 61</a></span>, at 68-69 (1965).</p>
</footnote>
<footnote label="10">
<p id="b537-6"> At oral argument, counsel for petitioner agreed that a prompt opportunity to obtain a copy from the seized film at “an independent lab under circumstances that would assure that there was no tampering with the film” with the original returned within “24 hours” would “satisfy” his “First Amendment position.” Tr. of Oral Arg. 28. Petitioner never requested such a copy below.</p>
</footnote>
<footnote label="11">
<p id="b537-7"> Failure to permit copying of seized material adversely affects First Amendment interests; prompt copying of seized material should be permitted. If copying is denied, return of the seized material should be required. On the other hand, violations of Fourth Amendment standards would require that the seized material be excluded from evidence. See <em>Roaden </em>v. <em>Kentucky, post, </em>p. 496; <em>Lee Art Theatre </em>v. <em>Virginia, </em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/#637" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">392 U. S., at 637</a></span>. Cf. <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Herring v. United States.md  (`case`, 6 assertions)

### content_page

```
---
title: "Herring v. United States"
type: case
citation: "555 U.S. 135 (2009)"
parallel_cite: "129 S. Ct. 695; 172 L. Ed. 2d 496"
neutral_cite: 2009 U.S. LEXIS 581
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2009
date_decided: 2009-01-14
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2009-01-14
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Herring v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145922/herring-v-united-states/"
  cluster_id: 145922
  opinion_id: 145922
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Collective Knowledge and the Fellow-Officer Rule]]"
    role: "Key (non-exclusive; imputation limit)"
related: ["[[United States v. Leon]]", "[[Arizona v. Evans]]", "[[Mapp v. Ohio]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "good-faith", "deterrence"]
holding: "Suppression is warranted only where deterrence benefits outweigh costs; isolated, attenuated police negligence (a recordkeeping error)…"
lake:
  record_id: Herring v. United States
  status: verified
  projected_at: 2026-07-06
---

# Herring v. United States

*555 U.S. 135 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigator Anderson asked a neighboring county's warrant clerk whether there was any outstanding warrant for Bennie Herring; the clerk reported one and Anderson arrested Herring, and a search incident to the arrest produced methamphetamine and a pistol. Within minutes the clerk discovered the warrant had been recalled months earlier and never removed from the database — a negligent bookkeeping error. Herring moved to suppress the gun and drugs as the fruit of an arrest unsupported by a valid warrant.

## Issue
Whether the exclusionary rule requires suppression of evidence found incident to an arrest made in objectively reasonable reliance on a police recordkeeping error — a warrant that had been recalled but, through isolated negligence, was left listed as active.

## Rule
No. Suppression turns on the culpability of the police conduct and the deterrence to be gained, not on the mere fact of a Fourth Amendment violation. "To trigger the exclusionary rule, police conduct must be sufficiently deliberate that exclusion can meaningfully deter it, and sufficiently culpable that such deterrence is worth the price paid by the justice system." — 555 U.S. at 144. ^pin-144

"As laid out in our cases, the exclusionary rule serves to deter deliberate, reckless, or grossly negligent conduct, or in some circumstances recurring or systemic negligence." — *Id.* ^pin-144a

## Application
The error here was a single, isolated bookkeeping mistake attenuated from the arrest, not deliberate, reckless, or grossly negligent conduct and not shown to be routine or systemic. Because the police conduct was not culpable enough for exclusion to yield deterrence worth its cost, the methamphetamine and pistol found incident to Herring's arrest were not suppressed.

## Conclusion
The evidence was admissible; the judgment denying suppression was affirmed. Negligent, attenuated recordkeeping error does not trigger the exclusionary rule.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Herring* extends the cost-benefit, deterrence-focused approach of [[United States v. Leon]] and [[Arizona v. Evans]], tying exclusion to the culpability of the police conduct.

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *Herring v. United States*, 555 U.S. 135 (2009) — https://www.courtlistener.com/opinion/145922/herring-v-united-states/ — pinpoint: 144.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0a4d16c0624248a3", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "555 U.S. 135 (2009)", "court": "U.S. Supreme Court", "neutral_cite": "2009 U.S. LEXIS 581", "official_citation_present": true, "parallel_cite": "129 S. Ct. 695; 172 L. Ed. 2d 496", "title": "Herring v. United States", "year": "2009"}}
{"assertion_id": "498c1e64696a36b2", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Suppression is warranted only where deterrence benefits outweigh costs; isolated, attenuated police negligence (a recordkeeping error)…", "title": "Herring v. United States"}}
{"assertion_id": "a374ec4b545052ef", "dimension": "support", "kind": "home_role", "locator": {"home": "Collective Knowledge and the Fellow-Officer Rule"}, "payload": {"home": "Collective Knowledge and the Fellow-Officer Rule", "role": "Key (non-exclusive; imputation limit)", "title": "Herring v. United States"}}
{"assertion_id": "a4b829f6cde6003f", "dimension": "support", "kind": "home_role", "locator": {"home": "The Good-Faith Exception"}, "payload": {"home": "The Good-Faith Exception", "role": "Key — Progeny / Refinement", "title": "Herring v. United States"}}
{"assertion_id": "bf5c04ed573ca84d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2009-01-14", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Herring v. United States", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Herring v. United States", "varies_by_point": "false"}}
{"assertion_id": "cbc14f37434ef2f0", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Herring v. United States"}}
```

### lake record — Herring v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Herring v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Herring v. United States",
    "case_name_short": "Herring",
    "case_name_full": "Herring v. United States",
    "input_case_name": "Herring v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2009-01-14",
    "year": 2009,
    "docket": null,
    "cluster_id": 145922,
    "lead_opinion_id": 145922,
    "sibling_ids": [
      145922,
      9435413,
      9435414,
      9435415
    ],
    "absolute_url": "/opinion/145922/herring-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "555 U.S. 135",
      "volume": "555",
      "reporter": "U.S.",
      "page": "135",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "129 S. Ct. 695",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "695",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "172 L. Ed. 2d 496",
        "volume": "172",
        "reporter": "L. Ed. 2d",
        "page": "496",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2009 U.S. LEXIS 581",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "581",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "555 U.S. 135",
        "volume": "555",
        "reporter": "U.S.",
        "page": "135",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 S. Ct. 695",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "695",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "172 L. Ed. 2d 496",
        "volume": "172",
        "reporter": "L. Ed. 2d",
        "page": "496",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 U.S. LEXIS 581",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "581",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "555 U.S. 135",
    "official_selection": {
      "court_class": "scotus",
      "selected": "555 U.S. 135",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-144",
      "page": null,
      "quote": "--- # Herring v. United States *555 U.S. 135 (2009)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Investigator Anderson asked a neighboring county's warrant clerk whether there was any outstanding warrant for Bennie Herring; the clerk reported one and Anderson arrested Herring, and a search incident to the arrest produced methamphetamine and a pistol. Within minutes the clerk discovered the warrant had been recalled months earlier and never removed from the database \u2014 a negligent bookkeeping error. Herring moved to suppress the gun and drugs as the fruit of an arrest unsupported by a valid warrant. ## Issue Whether the exclusionary rule requires suppression of evidence found incident to an arrest made in objectively reasonable reliance on a police recordkeeping error \u2014 a warrant that had been recalled but, through isolated negligence, was left listed as active. ## Rule No. Suppression turns on the culpability of the police conduct and the deterrence to be gained, not on the mere fact of a Fourth Amendment violation.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-144a",
      "page": null,
      "quote": "As laid out in our cases, the exclusionary rule serves to deter deliberate, reckless, or grossly negligent conduct, or in some circumstances recurring or systemic negligence.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2009-01-14",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Herring v. United States",
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
        "journal_ref": "Herring v. United States:lane1_negative"
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
        "journal_ref": "Herring v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Seneca Warrior Steeprock",
          "cluster_id": 10102625,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane1_negative"
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
        "journal_ref": "Herring v. United States:lane2_top_cited"
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
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scroggins",
          "cluster_id": 71470,
          "cite": [
            "599 F.3d 433",
            "2010 U.S. App. LEXIS 4551",
            "2010 WL 724688"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
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
        "journal_ref": "Herring v. United States:lane2_top_cited"
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
        "journal_ref": "Herring v. United States:lane2_top_cited"
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
        "journal_ref": "Herring v. United States:lane2_top_cited"
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
        "journal_ref": "Herring v. United States:lane2_top_cited"
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
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fadwa Safar v. Lisa Tingle",
          "cluster_id": 4398025,
          "cite": [
            "859 F.3d 241",
            "2017 WL 2453257",
            "2017 U.S. App. LEXIS 10114"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
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
        "journal_ref": "Herring v. United States:lane2_top_cited"
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
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Handy",
          "cluster_id": 2559301,
          "cite": [
            "18 A.3d 179",
            "206 N.J. 39",
            "2011 N.J. LEXIS 566"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
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
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Burnett",
          "cluster_id": 4581383,
          "cite": [
            "2019 CO 2",
            "432 P.3d 617"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vilar",
          "cluster_id": 1039434,
          "cite": [
            "729 F.3d 62",
            "92 A.L.R. Fed. 2d 661",
            "2013 WL 4608948",
            "2013 U.S. App. LEXIS 18143"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ruehle",
          "cluster_id": 1266839,
          "cite": [
            "583 F.3d 600",
            "2009 U.S. App. LEXIS 21450",
            "2009 WL 3152971"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Talkington",
          "cluster_id": 2784485,
          "cite": [
            "301 Kan. 453",
            "345 P.3d 258",
            "2015 Kan. LEXIS 167",
            "2015 WL 968451"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dupree",
          "cluster_id": 152453,
          "cite": [
            "617 F.3d 724",
            "2010 U.S. App. LEXIS 16310",
            "2010 WL 3063290"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Leak (Slip Opinion)",
          "cluster_id": 3170709,
          "cite": [
            "2016 Ohio 154",
            "145 Ohio St. 3d 165",
            "47 N.E.3d 821"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Afana",
          "cluster_id": 2584726,
          "cite": [
            "233 P.3d 879"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bershchansky",
          "cluster_id": 8442239,
          "cite": [
            "788 F.3d 102",
            "2015 U.S. App. LEXIS 9383",
            "2015 WL 3513759"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Earl Davis",
          "cluster_id": 2968788,
          "cite": [
            "690 F.3d 226",
            "2012 WL 3518479",
            "2012 U.S. App. LEXIS 17217"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Farias-Gonzalez",
          "cluster_id": 78275,
          "cite": [
            "556 F.3d 1181",
            "2009 U.S. App. LEXIS 2060",
            "2009 WL 232328"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Comprehensive Drug Testing, Inc.",
          "cluster_id": 175207,
          "cite": [
            "621 F.3d 1162",
            "2010 WL 3529247"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robinson",
          "cluster_id": 2637645,
          "cite": [
            "224 P.3d 55",
            "47 Cal. 4th 1104",
            "104 Cal. Rptr. 3d 727",
            "2010 Cal. LEXIS 114"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Herring v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145922 OR 9435413 OR 9435414 OR 9435415) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTU4MzEwNDAwMDAwJnM9NDYyMTQ0NCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145922+OR+9435413+OR+9435414+OR+9435415%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(145922 OR 9435413 OR 9435414 OR 9435415)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NCZzPTE3MjA5NyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145922+OR+9435413+OR+9435414+OR+9435415%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145922 OR 9435413 OR 9435414 OR 9435415)",
        "reviewed": 88,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 88,
        "triage_read": 3,
        "triage_snippet_classified": 85
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145922 OR 9435413 OR 9435414 OR 9435415)",
    "indexed_citing_opinions": 826,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145922,
        "count": 639,
        "count_source": "search"
      },
      {
        "opinion_id": 9435413,
        "count": 200,
        "count_source": "search"
      },
      {
        "opinion_id": 9435414,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9435415,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1552,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/herring-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzMjk3NTYmcz0xMDQyMjQ1NyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145922+OR+9435413+OR+9435414+OR+9435415%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145922,
        "cited_id": 77746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 101320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 109302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 109925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 110267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 110317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 111263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 111835,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 117905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 118235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 145646,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 1662274,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 2574654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145922,
        "cited_id": 3580565,
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
    "date_created": "2026-07-05T06:58:33Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T06:58:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T06:58:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:03:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T06:58:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Herring v. United States

```
(Slip Opinion)              OCTOBER TERM, 2008                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                   HERRING v. UNITED STATES

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                THE ELEVENTH CIRCUIT

    No. 07–513.     Argued October 7, 2008—Decided January 14, 2009
Officers in Coffee County arrested petitioner Herring based on a war
  rant listed in neighboring Dale County’s database. A search incident
  to that arrest yielded drugs and a gun. It was then revealed that the
  warrant had been recalled months earlier, though this information
  had never been entered into the database. Herring was indicted on
  federal gun and drug possession charges and moved to suppress the
  evidence on the ground that his initial arrest had been illegal. As
  suming that there was a Fourth Amendment violation, the District
  Court concluded that the exclusionary rule did not apply and denied
  the motion to suppress. The Eleventh Circuit affirmed, finding that
  the arresting officers were innocent of any wrongdoing, and that Dale
  County’s failure to update the records was merely negligent. The
  court therefore concluded that the benefit of suppression would be
  marginal or nonexistent and that the evidence was admissible under
  the good-faith rule of United States v. Leon, 468 U. S. 897.
Held: When police mistakes leading to an unlawful search are the re
 sult of isolated negligence attenuated from the search, rather than
 systemic error or reckless disregard of constitutional requirements,
 the exclusionary rule does not apply. Pp. 4–13.
    (a) The fact that a search or arrest was unreasonable does not nec
 essarily mean that the exclusionary rule applies. Illinois v. Gates,
 462 U. S. 213, 223. The rule is not an individual right and applies
 only where its deterrent effect outweighs the substantial cost of let
 ting guilty and possibly dangerous defendants go free. Leon, 468
 U. S., at 908–909. For example, it does not apply if police acted “in
 objectively reasonable reliance” on an invalid warrant. Id., at 922.
 In applying Leon’s good-faith rule to police who reasonably relied on
 mistaken information in a court’s database that an arrest warrant
2                     HERRING v. UNITED STATES

                                  Syllabus

    was outstanding, Arizona v. Evans, 514 U. S. 1, 14–15, the Court left
    unresolved the issue confronted here: whether evidence should be
    suppressed if the police committed the error, id., at 16, n. 5. Pp. 4–7.
       (b) The extent to which the exclusionary rule is justified by its de
    terrent effect varies with the degree of law enforcement culpability.
    See, e.g., Leon, supra, at 911. Indeed, the abuses that gave rise to the
    rule featured intentional conduct that was patently unconstitutional.
    See, e.g., Weeks v. United States, 232 U. S 383. An error arising from
    nonrecurring and attenuated negligence is far removed from the core
    concerns that led to the rule’s adoption. Pp. 7–9.
       (c) To trigger the exclusionary rule, police conduct must be suffi
    ciently deliberate that exclusion can meaningfully deter it, and suffi
    ciently culpable that such deterrence is worth the price paid by the
    justice system. The pertinent analysis is objective, not an inquiry
    into the arresting officers’ subjective awareness. See, e.g., Leon, su
    pra, at 922, n. 23. Pp. 9–11.
       (d) The conduct here was not so objectively culpable as to require
    exclusion. The marginal benefits that might follow from suppressing
    evidence obtained in these circumstances cannot justify the substan
    tial costs of exclusion. Leon, supra, at 922. Pp. 11–13.
492 F. 3d 1212, affirmed.

  ROBERTS, C. J., delivered the opinion of the Court, in which SCALIA,
KENNEDY, THOMAS, and ALITO, JJ., joined. GINSBURG, J., filed a dissent
ing opinion, in which STEVENS, SOUTER, and BREYER, JJ., joined.
BREYER, J., filed a dissenting opinion, in which SOUTER, J., joined.
                        Cite as: 555 U. S. ____ (2009)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 07–513
                                   _________________


 BENNIE DEAN HERRING, PETITIONER v. UNITED 

                 STATES 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

          APPEALS FOR THE ELEVENTH CIRCUIT

                               [January 14, 2009] 


   CHIEF JUSTICE ROBERTS delivered the opinion of the
Court.
   The Fourth Amendment forbids “unreasonable searches
and seizures,” and this usually requires the police to have
probable cause or a warrant before making an arrest.
What if an officer reasonably believes there is an out
standing arrest warrant, but that belief turns out to be
wrong because of a negligent bookkeeping error by an
other police employee? The parties here agree that the
ensuing arrest is still a violation of the Fourth Amend
ment, but dispute whether contraband found during a
search incident to that arrest must be excluded in a later
prosecution.
   Our cases establish that such suppression is not an
automatic consequence of a Fourth Amendment violation.
Instead, the question turns on the culpability of the police
and the potential of exclusion to deter wrongful police
conduct. Here the error was the result of isolated negli
gence attenuated from the arrest. We hold that in these
circumstances the jury should not be barred from consid
ering all the evidence.
2               HERRING v. UNITED STATES

                     Opinion of the Court

                              I
   On July 7, 2004, Investigator Mark Anderson learned
that Bennie Dean Herring had driven to the Coffee County
Sheriff’s Department to retrieve something from his im
pounded truck. Herring was no stranger to law enforce
ment, and Anderson asked the county’s warrant clerk,
Sandy Pope, to check for any outstanding warrants for
Herring’s arrest. When she found none, Anderson asked
Pope to check with Sharon Morgan, her counterpart in
neighboring Dale County. After checking Dale County’s
computer database, Morgan replied that there was an
active arrest warrant for Herring’s failure to appear on a
felony charge. Pope relayed the information to Anderson
and asked Morgan to fax over a copy of the warrant as
confirmation. Anderson and a deputy followed Herring as
he left the impound lot, pulled him over, and arrested him.
A search incident to the arrest revealed methampheta
mine in Herring’s pocket, and a pistol (which as a felon he
could not possess) in his vehicle. App. 17–23.
   There had, however, been a mistake about the warrant.
The Dale County sheriff’s computer records are supposed
to correspond to actual arrest warrants, which the office
also maintains. But when Morgan went to the files to
retrieve the actual warrant to fax to Pope, Morgan was
unable to find it. She called a court clerk and learned that
the warrant had been recalled five months earlier. Nor
mally when a warrant is recalled the court clerk’s office or
a judge’s chambers calls Morgan, who enters the informa
tion in the sheriff’s computer database and disposes of the
physical copy. For whatever reason, the information about
the recall of the warrant for Herring did not appear in the
database. Morgan immediately called Pope to alert her to
the mixup, and Pope contacted Anderson over a secure
radio. This all unfolded in 10 to 15 minutes, but Herring
had already been arrested and found with the gun and
drugs, just a few hundred yards from the sheriff’s office.
                 Cite as: 555 U. S. ____ (2009)           3

                     Opinion of the Court

Id., at 26, 35–42, 54–55.
  Herring was indicted in the District Court for the Mid
dle District of Alabama for illegally possessing the gun
and drugs, violations of 18 U. S. C. §922(g)(1) and 21
U. S. C. §844(a). He moved to suppress the evidence on
the ground that his initial arrest had been illegal because
the warrant had been rescinded. The Magistrate Judge
recommended denying the motion because the arresting
officers had acted in a good-faith belief that the warrant
was still outstanding. Thus, even if there were a Fourth
Amendment violation, there was “no reason to believe that
application of the exclusionary rule here would deter the
occurrence of any future mistakes.” App. 70. The District
Court adopted the Magistrate Judge’s recommendation,
451 F. Supp. 2d 1290 (2005), and the Court of Appeals for
the Eleventh Circuit affirmed, 492 F. 3d 1212 (2007).
  The Eleventh Circuit found that the arresting officers in
Coffee County “were entirely innocent of any wrongdoing
or carelessness.” id., at 1218. The court assumed that
whoever failed to update the Dale County sheriff’s records
was also a law enforcement official, but noted that “the
conduct in question [wa]s a negligent failure to act, not a
deliberate or tactical choice to act.” Ibid. Because the
error was merely negligent and attenuated from the ar
rest, the Eleventh Circuit concluded that the benefit of
suppressing the evidence “would be marginal or nonexis
tent,” ibid. (internal quotation marks omitted), and the
evidence was therefore admissible under the good-faith
rule of United States v. Leon, 468 U. S. 897 (1984).
  Other courts have required exclusion of evidence ob
tained through similar police errors, e.g., Hoay v. State,
348 Ark. 80, 86–87, 71 S. W. 3d 573, 577 (2002), so we
granted Herring’s petition for certiorari to resolve the
conflict, 552 U. S. ___ (2008). We now affirm the Eleventh
Circuit’s judgment.
4               HERRING v. UNITED STATES 


                     Opinion of the Court 


                             II 

  When a probable-cause determination was based on
reasonable but mistaken assumptions, the person sub
jected to a search or seizure has not necessarily been the
victim of a constitutional violation. The very phrase
“probable cause” confirms that the Fourth Amendment
does not demand all possible precision. And whether the
error can be traced to a mistake by a state actor or some
other source may bear on the analysis. For purposes of
deciding this case, however, we accept the parties’ as
sumption that there was a Fourth Amendment violation.
The issue is whether the exclusionary rule should be
applied.
                              A
  The Fourth Amendment protects “[t]he right of the
people to be secure in their persons, houses, papers, and
effects, against unreasonable searches and seizures,” but
“contains no provision expressly precluding the use of
evidence obtained in violation of its commands,” Arizona v.
Evans, 514 U. S. 1, 10 (1995). Nonetheless, our decisions
establish an exclusionary rule that, when applicable,
forbids the use of improperly obtained evidence at trial.
See, e.g., Weeks v. United States, 232 U. S. 383, 398 (1914).
We have stated that this judicially created rule is “de
signed to safeguard Fourth Amendment rights generally
through its deterrent effect.” United States v. Calandra,
414 U. S. 338, 348 (1974).
  In analyzing the applicability of the rule, Leon admon
ished that we must consider the actions of all the police
officers involved. 468 U. S., at 923, n. 24 (“It is necessary
to consider the objective reasonableness, not only of the
officers who eventually executed a warrant, but also of the
officers who originally obtained it or who provided infor
mation material to the probable-cause determination”).
The Coffee County officers did nothing improper. Indeed,
                      Cite as: 555 U. S. ____ (2009)                     5

                          Opinion of the Court

the error was noticed so quickly because Coffee County
requested a faxed confirmation of the warrant.
  The Eleventh Circuit concluded, however, that some
body in Dale County should have updated the computer
database to reflect the recall of the arrest warrant. The
court also concluded that this error was negligent, but did
not find it to be reckless or deliberate. 492 F. 3d, at 1218.1
That fact is crucial to our holding that this error is not
enough by itself to require “the extreme sanction of exclu
sion.” Leon, supra, at 916.
                              B
   1. The fact that a Fourth Amendment violation oc
curred—i.e., that a search or arrest was unreasonable—
does not necessarily mean that the exclusionary rule
applies. Illinois v. Gates, 462 U. S. 213, 223 (1983). In
deed, exclusion “has always been our last resort, not our
first impulse,” Hudson v. Michigan, 547 U. S. 586, 591
(2006), and our precedents establish important principles
that constrain application of the exclusionary rule.
   First, the exclusionary rule is not an individual right
and applies only where it “ ‘result[s] in appreciable deter
rence.’ ” Leon, supra, at 909 (quoting United States v.
Janis, 428 U. S. 433, 454 (1976)). We have repeatedly
rejected the argument that exclusion is a necessary conse
quence of a Fourth Amendment violation. Leon, supra, at
905–906; Evans, supra, at 13–14; Pennsylvania Bd. of
Probation and Parole v. Scott, 524 U. S. 357, 363 (1998).
Instead we have focused on the efficacy of the rule in
——————
  1 At an earlier point in its opinion, the Eleventh Circuit described the
error as “ ‘at the very least negligent,’ ” 492 F. 3d 1212, 1217 (2007)
(quoting Michigan v. Tucker, 417 U. S. 433, 447 (1974)). But in the
next paragraph, it clarified that the error was “a negligent failure to
act, not a deliberate or tactical choice to act,” 492 F. 3d, at 1218. The
question presented treats the error as a “negligen[t]” one, see Pet. for
Cert. i; Brief in Opposition (I), and both parties briefed the case on that
basis.
6                   HERRING v. UNITED STATES

                          Opinion of the Court

deterring Fourth Amendment violations in the future. See
Calandra, supra, at 347–355; Stone v. Powell, 428 U. S.
465, 486 (1976).2
   In addition, the benefits of deterrence must outweigh
the costs. Leon, supra, at 910. “We have never suggested
that the exclusionary rule must apply in every circum
stance in which it might provide marginal deterrence.”
Scott, supra, at 368. “[T]o the extent that application of
the exclusionary rule could provide some incremental
deterrent, that possible benefit must be weighed against
[its] substantial social costs.” Illinois v. Krull, 480 U. S.
340, 352–353 (1987) (internal quotation marks omitted).
The principal cost of applying the rule is, of course, letting
guilty and possibly dangerous defendants go free—
something that “offends basic concepts of the criminal
justice system.” Leon, supra, at 908. “[T]he rule’s costly
toll upon truth-seeking and law enforcement objectives
presents a high obstacle for those urging [its] application.”
Scott, supra, at 364–365 (internal quotation marks omit
ted); see also United States v. Havens, 446 U. S. 620, 626–
627 (1980); United States v. Payner, 447 U. S. 727, 734
(1980).
   These principles are reflected in the holding of Leon:
When police act under a warrant that is invalid for lack of
probable cause, the exclusionary rule does not apply if the
police acted “in objectively reasonable reliance” on the
subsequently invalidated search warrant. 468 U. S., at
922. We (perhaps confusingly) called this objectively
——————
    2 JUSTICEGINSBURG’s dissent champions what she describes as “ ‘a
more majestic conception’ of . . . the exclusionary rule,” post, at 5
(quoting Arizona v. Evans, 514 U. S. 1, 18 (1995) (STEVENS, J., dissent
ing)), which would exclude evidence even where deterrence does not
justify doing so. Majestic or not, our cases reject this conception, see,
e.g., United States v. Leon, 468 U. S. 897, 921, n. 22 (1984), and perhaps
for this reason, her dissent relies almost exclusively on previous dis
sents to support its analysis.
                     Cite as: 555 U. S. ____ (2009)                   7

                         Opinion of the Court

reasonable reliance “good faith.” Ibid., n. 23. In a com
panion case, Massachusetts v. Sheppard, 468 U. S. 981
(1984), we held that the exclusionary rule did not apply
when a warrant was invalid because a judge forgot to
make “clerical corrections” to it. Id., at 991.
  Shortly thereafter we extended these holdings to war
rantless administrative searches performed in good-faith
reliance on a statute later declared unconstitutional.
Krull, supra, at 349–350. Finally, in Evans, 514 U. S. 1,
we applied this good-faith rule to police who reasonably
relied on mistaken information in a court’s database that
an arrest warrant was outstanding. We held that a mis
take made by a judicial employee could not give rise to
exclusion for three reasons: The exclusionary rule was
crafted to curb police rather than judicial misconduct;
court employees were unlikely to try to subvert the Fourth
Amendment; and “most important, there [was] no basis for
believing that application of the exclusionary rule in
[those] circumstances” would have any significant effect in
deterring the errors. Id., at 15. Evans left unresolved
“whether the evidence should be suppressed if police
personnel were responsible for the error,”3 an issue not
argued by the State in that case, id., at 16, n. 5, but one
that we now confront.
  2. The extent to which the exclusionary rule is justified
by these deterrence principles varies with the culpability
of the law enforcement conduct. As we said in Leon, “an

——————
   3 We thus reject JUSTICE BREYER’s suggestion that Evans was entirely

“premised on a distinction between judicial errors and police errors,”
post, at 1 (dissenting opinion). Were that the only rationale for our
decision, there would have been no reason for us expressly and care
fully to leave police error unresolved. In addition, to the extent Evans
is viewed as presaging a particular result here, it is noteworthy that
the dissent’s view in that case was that the distinction JUSTICE BREYER
regards as determinative was instead “artificial.” 514 U. S., at 29
(GINSBURG, J., dissenting).
8               HERRING v. UNITED STATES

                     Opinion of the Court

assessment of the flagrancy of the police misconduct con
stitutes an important step in the calculus” of applying the
exclusionary rule. 468 U. S., at 911. Similarly, in Krull
we elaborated that “evidence should be suppressed ‘only if
it can be said that the law enforcement officer had knowl
edge, or may properly be charged with knowledge, that the
search was unconstitutional under the Fourth Amend
ment.’ ” 480 U. S., at 348–349 (quoting United States v.
Peltier, 422 U. S. 531, 542 (1975)).
   Anticipating the good-faith exception to the exclusionary
rule, Judge Friendly wrote that “[t]he beneficent aim of
the exclusionary rule to deter police misconduct can be
sufficiently accomplished by a practice . . . outlawing
evidence obtained by flagrant or deliberate violation of
rights.” The Bill of Rights as a Code of Criminal Proce
dure, 53 Calif. L. Rev. 929, 953 (1965) (footnotes omitted);
see also Brown v. Illinois, 422 U. S. 590, 610–611 (1975)
(Powell, J., concurring in part) (“[T]he deterrent value of
the exclusionary rule is most likely to be effective” when
“official conduct was flagrantly abusive of Fourth Amend
ment rights”).
   Indeed, the abuses that gave rise to the exclusionary
rule featured intentional conduct that was patently un
constitutional. In Weeks, 232 U. S. 383, a foundational
exclusionary rule case, the officers had broken into the
defendant’s home (using a key shown to them by a
neighbor), confiscated incriminating papers, then returned
again with a U. S. Marshal to confiscate even more. Id., at
386. Not only did they have no search warrant, which the
Court held was required, but they could not have gotten
one had they tried. They were so lacking in sworn and
particularized information that “not even an order of court
would have justified such procedure.” Id., at 393–394.
Silverthorne Lumber Co. v. United States, 251 U. S. 385
(1920), on which petitioner repeatedly relies, was similar;
federal officials “without a shadow of authority” went to
                      Cite as: 555 U. S. ____ (2009)                      9

                           Opinion of the Court

the defendants’ office and “made a clean sweep” of every
paper they could find. Id., at 390. Even the Government
seemed to acknowledge that the “seizure was an outrage.”
Id., at 391.
   Equally flagrant conduct was at issue in Mapp v. Ohio,
367 U. S. 643 (1961), which overruled Wolf v. Colorado,
338 U. S. 25 (1949), and extended the exclusionary rule to
the States. Officers forced open a door to Ms. Mapp’s
house, kept her lawyer from entering, brandished what
the court concluded was a false warrant, then forced her
into handcuffs and canvassed the house for obscenity. 367
U. S., at 644–645. See Friendly, supra, at 953, and n. 127
(“[T]he situation in Mapp” featured a “flagrant or deliber
ate violation of rights”). An error that arises from nonre
curring and attenuated negligence is thus far removed
from the core concerns that led us to adopt the rule in the
first place. And in fact since Leon, we have never applied
the rule to exclude evidence obtained in violation of the
Fourth Amendment, where the police conduct was no more
intentional or culpable than this.
   3. To trigger the exclusionary rule, police conduct must
be sufficiently deliberate that exclusion can meaningfully
deter it, and sufficiently culpable that such deterrence is
worth the price paid by the justice system. As laid out in
our cases, the exclusionary rule serves to deter deliberate,
reckless, or grossly negligent conduct, or in some circum
stances recurring or systemic negligence. The error in this
case does not rise to that level.4
   Our decision in Franks v. Delaware, 438 U. S. 154
——————
   4 We do not quarrel with JUSTICE GINSBURG’s claim that “liability for

negligence . . . creates an incentive to act with greater care,” post, at 7,
and we do not suggest that the exclusion of this evidence could have no
deterrent effect. But our cases require any deterrence to “be weighed
against the ‘substantial social costs exacted by the exclusionary rule,’ ”
Illinois v. Krull, 480 U. S. 340, 352–353 (1987) (quoting Leon, 468 U. S.,
at 907), and here exclusion is not worth the cost.
10              HERRING v. UNITED STATES

                     Opinion of the Court

(1978), provides an analogy. Cf. Leon, supra, at 914. In
Franks, we held that police negligence in obtaining a
warrant did not even rise to the level of a Fourth Amend
ment violation, let alone meet the more stringent test for
triggering the exclusionary rule. We held that the Consti
tution allowed defendants, in some circumstances, “to
challenge the truthfulness of factual statements made in
an affidavit supporting the warrant,” even after the war
rant had issued. 438 U. S., at 155–156. If those false
statements were necessary to the Magistrate Judge’s
probable-cause determination, the warrant would be
“voided.” Ibid. But we did not find all false statements
relevant: “There must be allegations of deliberate false
hood or of reckless disregard for the truth,” and
“[a]llegations of negligence or innocent mistake are insuf
ficient.” Id., at 171.
   Both this case and Franks concern false information
provided by police. Under Franks, negligent police mis
communications in the course of acquiring a warrant do
not provide a basis to rescind a warrant and render a
search or arrest invalid. Here, the miscommunications
occurred in a different context—after the warrant had
been issued and recalled—but that fact should not require
excluding the evidence obtained.
   The pertinent analysis of deterrence and culpability is
objective, not an “inquiry into the subjective awareness of
arresting officers,” Reply Brief for Petitioner 4–5. See also
post, at 10, n. 7 (GINSBURG, J., dissenting). We have
already held that “our good-faith inquiry is confined to the
objectively ascertainable question whether a reasonably
well trained officer would have known that the search was
illegal” in light of “all of the circumstances.” Leon, 468
U. S., at 922, n. 23. These circumstances frequently in
clude a particular officer’s knowledge and experience, but
that does not make the test any more subjective than the
one for probable cause, which looks to an officer’s knowl
                  Cite as: 555 U. S. ____ (2009)           11

                      Opinion of the Court

edge and experience, Ornelas v. United States, 517 U. S.
690, 699–700 (1996), but not his subjective intent, Whren
v. United States, 517 U. S. 806, 812–813 (1996).
   4. We do not suggest that all recordkeeping errors by
the police are immune from the exclusionary rule. In this
case, however, the conduct at issue was not so objectively
culpable as to require exclusion. In Leon we held that “the
marginal or nonexistent benefits produced by suppressing
evidence obtained in objectively reasonable reliance on a
subsequently invalidated search warrant cannot justify
the substantial costs of exclusion.” 468 U. S., at 922. The
same is true when evidence is obtained in objectively
reasonable reliance on a subsequently recalled warrant.
   If the police have been shown to be reckless in maintain
ing a warrant system, or to have knowingly made false
entries to lay the groundwork for future false arrests,
exclusion would certainly be justified under our cases
should such misconduct cause a Fourth Amendment viola
tion. We said as much in Leon, explaining that an officer
could not “obtain a warrant on the basis of a ‘bare bones’
affidavit and then rely on colleagues who are ignorant of
the circumstances under which the warrant was obtained
to conduct the search.” Id., at 923, n. 24 (citing Whiteley v.
Warden, Wyo. State Penitentiary, 401 U. S. 560, 568
(1971)). Petitioner’s fears that our decision will cause
police departments to deliberately keep their officers
ignorant, Brief for Petitioner 37–39, are thus unfounded.
   The dissent also adverts to the possible unreliability of a
number of databases not relevant to this case. Post, at 8–
9. In a case where systemic errors were demonstrated, it
might be reckless for officers to rely on an unreliable
warrant system. See Evans, 514 U. S., at 17 (O’Connor,
J., concurring) (“Surely it would not be reasonable for the
police to rely . . . on a recordkeeping system . . . that rou
tinely leads to false arrests” (second emphasis added));
Hudson, 547 U. S., at 604 (KENNEDY, J., concurring) (“If a
12                  HERRING v. UNITED STATES

                          Opinion of the Court

widespread pattern of violations were shown . . . there
would be reason for grave concern” (emphasis added)).
But there is no evidence that errors in Dale County’s
system are routine or widespread. Officer Anderson testi
fied that he had never had reason to question information
about a Dale County warrant, App. 27, and both Sandy
Pope and Sharon Morgan testified that they could remem
ber no similar miscommunication ever happening on their
watch, id., at 33, 61–62. That is even less error than in
the database at issue in Evans, where we also found reli
ance on the database to be objectively reasonable. 514
U. S., at 15 (similar error “every three or four years”).
Because no such showings were made here, see 451
F. Supp. 2d, at 1292,5 the Eleventh Circuit was correct to
affirm the denial of the motion to suppress.
                        *     *     *
   Petitioner’s claim that police negligence automatically
triggers suppression cannot be squared with the principles
underlying the exclusionary rule, as they have been ex
plained in our cases. In light of our repeated holdings that
the deterrent effect of suppression must be substantial
and outweigh any harm to the justice system, e.g., Leon,
468 U. S., at 909–910, we conclude that when police mis
takes are the result of negligence such as that described
here, rather than systemic error or reckless disregard of
——————
  5 JUSTICE GINSBURG notes that at an earlier suppression hearing Mor
gan testified—apparently in confusion—that there had been miscom
munications “[s]everal times.” Post, at 3, n. 2 (quoting App. to Pet. for
Cert. 17a). When she later realized that she had misspoken, Morgan
emphatically corrected the record. App. 61–62. Noting this, the Dis
trict Court found that “Morgan’s ‘several times’ statement is confusing
and essentially unhelpful,” and concluded that there was “no credible
evidence of routine problems with disposing of recalled warrants.” 451
F. Supp. 2d, at 1292. This factual determination, supported by the
record and credited by the Court of Appeals, see 492 F. 3d, at 1219, is of
course entitled to deference.
                  Cite as: 555 U. S. ____ (2009)           13

                      Opinion of the Court

constitutional requirements, any marginal deterrence does
not “pay its way.” Id., at 907–908, n. 6 (internal quotation
marks omitted). In such a case, the criminal should not
“go free because the constable has blundered.” People v.
Defore, 242 N. Y. 13, 21, 150 N. E. 585, 587 (1926) (opinion
of the Court by Cardozo, J.).
   The judgment of the Court of Appeals for the Eleventh
Circuit is affirmed.
                                             It is so ordered.
                 Cite as: 555 U. S. ____ (2009)           1

                   GINSBURG, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 07–513
                         _________________


 BENNIE DEAN HERRING, PETITIONER v. UNITED 

                 STATES 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

          APPEALS FOR THE ELEVENTH CIRCUIT

                      [January 14, 2009] 


    JUSTICE GINSBURG, with whom JUSTICE STEVENS,
JUSTICE SOUTER, and JUSTICE BREYER join, dissenting.
    Petitioner Bennie Dean Herring was arrested, and
subjected to a search incident to his arrest, although no
warrant was outstanding against him, and the police
lacked probable cause to believe he was engaged in crimi
nal activity. The arrest and ensuing search therefore
violated Herring’s Fourth Amendment right “to be secure
. . . against unreasonable searches and seizures.” The
Court of Appeals so determined, and the Government does
not contend otherwise. The exclusionary rule provides
redress for Fourth Amendment violations by placing the
government in the position it would have been in had
there been no unconstitutional arrest and search. The
rule thus strongly encourages police compliance with the
Fourth Amendment in the future. The Court, however,
holds the rule inapplicable because careless recordkeeping
by the police—not flagrant or deliberate misconduct—
accounts for Herring’s arrest.
    I would not so constrict the domain of the exclusionary
rule and would hold the rule dispositive of this case: “[I]f
courts are to have any power to discourage [police] error of
[the kind here at issue], it must be through the application
of the exclusionary rule.” Arizona v. Evans, 514 U. S. 1,
22–23 (1995) (STEVENS, J., dissenting). The unlawful
2               HERRING v. UNITED STATES

                   GINSBURG, J., dissenting

search in this case was contested in court because the
police found methamphetamine in Herring’s pocket and a
pistol in his truck. But the “most serious impact” of the
Court’s holding will be on innocent persons “wrongfully
arrested based on erroneous information [carelessly main
tained] in a computer data base.” Id., at 22.
                               I
  A warrant for Herring’s arrest was recalled in February
2004, apparently because it had been issued in error. See
Brief for Petitioner 3, n. 1 (citing App. 63). The warrant
database for the Dale County Sheriff’s Department, how
ever, does not automatically update to reflect such
changes. App. 39–40, 43, 45. A member of the Dale
County Sheriff’s Department—whom the parties have not
identified—returned the hard copy of the warrant to the
County Circuit Clerk’s office, but did not correct the De
partment’s database to show that the warrant had been
recalled. Id., at 60. The erroneous entry for the warrant
remained in the database, undetected, for five months.
  On a July afternoon in 2004, Herring came to the Coffee
County Sheriff’s Department to retrieve his belongings
from a vehicle impounded in the Department’s lot. Id., at
17. Investigator Mark Anderson, who was at the Depart
ment that day, knew Herring from prior interactions:
Herring had told the district attorney, among others, of
his suspicion that Anderson had been involved in the
killing of a local teenager, and Anderson had pursued
Herring to get him to drop the accusations. Id., at 63–64.
Informed that Herring was in the impoundment lot,
Anderson asked the Coffee County warrant clerk whether
there was an outstanding warrant for Herring’s arrest.
Id., at 18. The clerk, Sandy Pope, found no warrant. Id.,
at 19.
  Anderson then asked Pope to call the neighboring Dale
County Sheriff’s Department to inquire whether a warrant
                     Cite as: 555 U. S. ____ (2009)                     3

                        GINSBURG, J., dissenting

to arrest Herring was outstanding there. Upon receiving
Pope’s phone call, Sharon Morgan, the warrant clerk for
the Dale County Department, checked her computer data
base. As just recounted, that Department’s database
preserved an error. Morgan’s check therefore showed—
incorrectly—an active warrant for Herring’s arrest. Id., at
41. Morgan gave the misinformation to Pope, ibid., who
relayed it to Investigator Anderson, id., at 35. Armed with
the report that a warrant existed, Anderson promptly
arrested Herring and performed an incident search min
utes before detection of the error.
  The Court of Appeals concluded, and the Government
does not contest, that the “failure to bring the [Dale
County Sheriff’s Department] records up to date [was] ‘at
the very least negligent.’ ” 492 F. 3d 1212, 1217 (CA11
2007) (quoting Michigan v. Tucker, 417 U. S. 433, 447
(1974)). And it is uncontested here that Herring’s arrest
violated his Fourth Amendment rights. The sole question
presented, therefore, is whether evidence the police ob
tained through the unlawful search should have been
suppressed.1 The Court holds that suppression was un
warranted because the exclusionary rule’s “core concerns”
are not raised by an isolated, negligent recordkeeping
error attenuated from the arrest. Ante, at 9, 12.2 In my
view, the Court’s opinion underestimates the need for a
forceful exclusionary rule and the gravity of recordkeeping
——————
  1 That   the recordkeeping error occurred in Dale County rather than
Coffee County is inconsequential in the suppression analysis. As the
Court notes, “we must consider the actions of all the police officers
involved.” Ante, at 4. See also United States v. Leon, 468 U. S. 897,
923, n. 24 (1984).
   2 It is not altogether clear how “isolated” the error was in this case.

When the Dale County Sheriff’s Department warrant clerk was first
asked: “[H]ow many times have you had or has Dale County had
problems, any problems with communicating about warrants,” she
responded: “Several times.” App. to Pet. for Cert. 17a (internal quota
tion marks omitted).
4                HERRING v. UNITED STATES

                    GINSBURG, J., dissenting

errors in law enforcement.
                               II 

                               A

  The Court states that the exclusionary rule is not a
defendant’s right, ante, at 5; rather, it is simply a remedy
applicable only when suppression would result in appre
ciable deterrence that outweighs the cost to the justice
system, ante, at 12. See also ante, at 9 (“[T]he exclusion
ary rule serves to deter deliberate, reckless, or grossly
negligent conduct, or in some circumstances recurring or
systemic negligence.”).
  The Court’s discussion invokes a view of the exclusion
ary rule famously held by renowned jurists Henry J.
Friendly and Benjamin Nathan Cardozo. Over 80 years
ago, Cardozo, then seated on the New York Court of Ap
peals, commented critically on the federal exclusionary
rule, which had not yet been applied to the States. He
suggested that in at least some cases the rule exacted too
high a price from the criminal justice system. See People
v. Defore, 242 N. Y. 13, 24–25, 150 N. E. 585, 588–589
(1926).    In words often quoted, Cardozo questioned
whether the criminal should “go free because the constable
has blundered.” Id., at 21, 150 N. E., at 587.
  Judge Friendly later elaborated on Cardozo’s query.
“The sole reason for exclusion,” Friendly wrote, “is that
experience has demonstrated this to be the only effective
method for deterring the police from violating the Consti
tution.” The Bill of Rights as a Code of Criminal Proce
dure, 53 Calif. L. Rev. 929, 951 (1965). He thought it
excessive, in light of the rule’s aim to deter police conduct,
to require exclusion when the constable had merely “blun
dered”—when a police officer committed a technical error
in an on-the-spot judgment, id., at 952, or made a “slight
and unintentional miscalculation,” id., at 953. As the
Court recounts, Judge Friendly suggested that deterrence
                 Cite as: 555 U. S. ____ (2009)            5

                   GINSBURG, J., dissenting

of police improprieties could be “sufficiently accomplished”
by confining the rule to “evidence obtained by flagrant or
deliberate violation of rights.” Ibid.; ante, at 8.
                             B
   Others have described “a more majestic conception” of
the Fourth Amendment and its adjunct, the exclusionary
rule. Evans, 514 U. S., at 18 (STEVENS, J., dissenting).
Protective of the fundamental “right of the people to be
secure in their persons, houses, papers, and effects,” the
Amendment “is a constraint on the power of the sovereign,
not merely on some of its agents.” Ibid. (internal quota
tion marks omitted); see Stewart, The Road to Mapp v.
Ohio and Beyond: The Origins, Development and Future
of the Exclusionary Rule in Search-and-Seizure Cases, 83
Colum. L. Rev. 1365 (1983). I share that vision of the
Amendment.
   The exclusionary rule is “a remedy necessary to ensure
that” the Fourth Amendment’s prohibitions “are observed
in fact.” Id., at 1389; see Kamisar, Does (Did) (Should)
The Exclusionary Rule Rest On A “Principled Basis”
Rather Than An “Empirical Proposition”? 16 Creighton
L. Rev. 565, 600 (1983). The rule’s service as an essential
auxiliary to the Amendment earlier inclined the Court to
hold the two inseparable. See Whiteley v. Warden, Wyo.
State Penitentiary, 401 U. S. 560, 568–569 (1971). Cf.
Olmstead v. United States, 277 U. S. 438, 469–471 (1928)
(Holmes, J., dissenting); id., at 477–479, 483–485
(Brandeis, J., dissenting).
   Beyond doubt, a main objective of the rule “is to deter—
to compel respect for the constitutional guaranty in the
only effectively available way—by removing the incentive
to disregard it.” Elkins v. United States, 364 U. S. 206,
217 (1960). But the rule also serves other important
purposes: It “enabl[es] the judiciary to avoid the taint of
partnership in official lawlessness,” and it “assur[es] the
6               HERRING v. UNITED STATES

                   GINSBURG, J., dissenting

people—all potential victims of unlawful government
conduct—that the government would not profit from its
lawless behavior, thus minimizing the risk of seriously
undermining popular trust in government.” United States
v. Calandra, 414 U. S. 338, 357 (1974) (Brennan, J., dis
senting). See also Terry v. Ohio, 392 U. S. 1, 13 (1968) (“A
rule admitting evidence in a criminal trial, we recognize,
has the necessary effect of legitimizing the conduct which
produced the evidence, while an application of the exclu
sionary rule withholds the constitutional imprimatur.”);
Kamisar, supra, at 604 (a principal reason for the exclu
sionary rule is that “the Court’s aid should be denied ‘in
order to maintain respect for law [and] to preserve the
judicial process from contamination’ ” (quoting Olmstead,
277 U. S., at 484 (Brandeis, J., dissenting)).
  The exclusionary rule, it bears emphasis, is often the
only remedy effective to redress a Fourth Amendment
violation. See Mapp v. Ohio, 367 U. S. 643, 652 (1961)
(noting “the obvious futility of relegating the Fourth
Amendment to the protection of other remedies”); Amster
dam, Perspectives on the Fourth Amendment, 58 Minn.
L. Rev. 349, 360 (1974) (describing the exclusionary rule
as “the primary instrument for enforcing the [F]ourth
[A]mendment”). Civil liability will not lie for “the vast
majority of [F]ourth [A]mendment violations—the fre
quent infringements motivated by commendable zeal, not
condemnable malice.” Stewart, 83 Colum. L. Rev., at
1389. Criminal prosecutions or administrative sanctions
against the offending officers and injunctive relief against
widespread violations are an even farther cry. See id., at
1386–1388.
                            III
  The Court maintains that Herring’s case is one in which
the exclusionary rule could have scant deterrent effect and
therefore would not “pay its way.” Ante, at 13 (internal
                 Cite as: 555 U. S. ____ (2009)            7

                    GINSBURG, J., dissenting

quotation marks omitted). I disagree.
                               A
   The exclusionary rule, the Court suggests, is capable of
only marginal deterrence when the misconduct at issue is
merely careless, not intentional or reckless. See ante, at 9,
11. The suggestion runs counter to a foundational premise
of tort law—that liability for negligence, i.e., lack of due
care, creates an incentive to act with greater care. The
Government so acknowledges. See Brief for United States
21; cf. Reply Brief 12.
   That the mistake here involved the failure to make a
computer entry hardly means that application of the
exclusionary rule would have minimal value. “Just as the
risk of respondeat superior liability encourages employers
to supervise . . . their employees’ conduct [more carefully],
so the risk of exclusion of evidence encourages policymak
ers and systems managers to monitor the performance of
the systems they install and the personnel employed to
operate those systems.” Evans, 514 U. S., at 29, n. 5
(GINSBURG, J., dissenting).
   Consider the potential impact of a decision applying the
exclusionary rule in this case. As earlier observed, see
supra, at 2, the record indicates that there is no electronic
connection between the warrant database of the Dale
County Sheriff’s Department and that of the County Cir
cuit Clerk’s office, which is located in the basement of the
same building. App. 39–40, 43, 45. When a warrant is
recalled, one of the “many different people that have ac
cess to th[e] warrants,” id., at 60, must find the hard copy
of the warrant in the “two or three different places” where
the department houses warrants, id., at 41, return it to
the Clerk’s office, and manually update the Department’s
database, see id., at 60. The record reflects no routine
practice of checking the database for accuracy, and the
failure to remove the entry for Herring’s warrant was not
8               HERRING v. UNITED STATES

                   GINSBURG, J., dissenting

discovered until Investigator Anderson sought to pursue
Herring five months later. Is it not altogether obvious
that the Department could take further precautions to
ensure the integrity of its database? The Sheriff’s De
partment “is in a position to remedy the situation and
might well do so if the exclusionary rule is there to remove
the incentive to do otherwise.” 1 W. LaFave, Search and
Seizure §1.8(e), p. 313 (4th ed. 2004). See also Evans, 514
U. S., at 21 (STEVENS, J., dissenting).
                             B
   Is the potential deterrence here worth the costs it im
poses? See ante, at 9. In light of the paramount impor
tance of accurate recordkeeping in law enforcement, I
would answer yes, and next explain why, as I see it,
Herring’s motion presents a particularly strong case for
suppression.
   Electronic databases form the nervous system of con
temporary criminal justice operations. In recent years,
their breadth and influence have dramatically expanded.
Police today can access databases that include not only the
updated National Crime Information Center (NCIC), but
also terrorist watchlists, the Federal Government’s em
ployee eligibility system, and various commercial data
bases. Brief for Electronic Privacy Information Center
(EPIC) et al. as Amicus Curiae 6. Moreover, States are
actively expanding information sharing between jurisdic
tions. Id., at 8–13. As a result, law enforcement has an
increasing supply of information within its easy electronic
reach. See Brief for Petitioner 36–37.
   The risk of error stemming from these databases is not
slim. Herring’s amici warn that law enforcement data
bases are insufficiently monitored and often out of date.
Brief for Amicus EPIC 13–28. Government reports de
                     Cite as: 555 U. S. ____ (2009)                     9

                        GINSBURG, J., dissenting

scribe, for example, flaws in NCIC databases,3 terrorist
watchlist databases,4 and databases associated with the
Federal Government’s employment eligibility verification
system.5
   Inaccuracies in expansive, interconnected collections of
electronic information raise grave concerns for individual
liberty. “The offense to the dignity of the citizen who is
arrested, handcuffed, and searched on a public street
simply because some bureaucrat has failed to maintain
an accurate computer data base” is evocative of the use
of general warrants that so outraged the authors of our
Bill of Rights. Evans, 514 U. S., at 23 (STEVENS, J.,
dissenting).
                              C
  The Court assures that “exclusion would certainly be
justified” if “the police have been shown to be reckless in
maintaining a warrant system, or to have knowingly
made false entries to lay the groundwork for future false
arrests.” Ante, at 11. This concession provides little
comfort.
  First, by restricting suppression to bookkeeping errors
that are deliberate or reckless, the majority leaves Her
ring, and others like him, with no remedy for violations of

——————
   3 See Dept. of Justice, Bureau of Justice Statistics, P. Brien, Improv

ing Access to and Integrity of Criminal History Records, NCJ 200581
(July 2005), available at http://www.ojp.usdoj.gov/bjs/pub/pdf/iaichr.pdf
(All Internet materials as visited Jan. 12, 2009, and included in Clerk
of Court’s case file.).
   4 See Dept. of Justice, Office of Inspector General, Audit of the U. S.

Department of Justice Terrorist Watchlist Nomination Processes, Audit
Rep. 08–16 (Mar. 2008), http://www.usdoj.gov/oig/reports/plus/a0816/
final.pdf.
   5 See Social Security Admin., Office of Inspector General, Congres

sional Response Report: Accuracy of the Social Security Administra
tion’s Numident File, A–08–06–26100 (Dec. 2006), http://www.ssa.gov/
oig/ADOBEPDF/A–08–06–26100.pdf.
10                  HERRING v. UNITED STATES

                        GINSBURG, J., dissenting

their constitutional rights. See supra, at 6. There can be
no serious assertion that relief is available under 42
U. S. C. §1983. The arresting officer would be sheltered by
qualified immunity, see Harlow v. Fitzgerald, 457 U. S.
800 (1982), and the police department itself is not liable
for the negligent acts of its employees, see Monell v. New
York City Dept. of Social Servs., 436 U. S. 658 (1978).
Moreover, identifying the department employee who com
mitted the error may be impossible.
   Second, I doubt that police forces already possess suffi
cient incentives to maintain up-to-date records. The Gov
ernment argues that police have no desire to send officers
out on arrests unnecessarily, because arrests consume
resources and place officers in danger. The facts of this
case do not fit that description of police motivation. Here
the officer wanted to arrest Herring and consulted the
Department’s records to legitimate his predisposition. See
App. 17–19.6
   Third, even when deliberate or reckless conduct is afoot,
the Court’s assurance will often be an empty promise: How
is an impecunious defendant to make the required show
ing? If the answer is that a defendant is entitled to dis
covery (and if necessary, an audit of police databases), see
Tr. of Oral Arg. 57–58, then the Court has imposed a
considerable administrative burden on courts and law
enforcement.7


——————
  6 It has been asserted that police departments have become suffi

ciently “professional” that they do not need external deterrence to avoid
Fourth Amendment violations. See Tr. of Oral Arg. 24–25; cf. Hudson
v. Michigan, 547 U. S. 586, 598–599 (2006). But professionalism is a
sign of the exclusionary rule’s efficacy—not of its superfluity.
  7 It is not clear how the Court squares its focus on deliberate conduct

with its recognition that application of the exclusionary rule does not
require inquiry into the mental state of the police. See ante, at 10;
Whren v. United States, 517 U. S. 806, 812–813 (1996).
                 Cite as: 555 U. S. ____ (2009)         11

                   GINSBURG, J., dissenting

                             IV
   Negligent recordkeeping errors by law enforcement
threaten individual liberty, are susceptible to deterrence
by the exclusionary rule, and cannot be remedied effec
tively through other means. Such errors present no occa
sion to further erode the exclusionary rule. The rule “is
needed to make the Fourth Amendment something real; a
guarantee that does not carry with it the exclusion of
evidence obtained by its violation is a chimera.” Ca
landra, 414 U. S., at 361 (Brennan, J., dissenting). In
keeping with the rule’s “core concerns,” ante, at 9, sup
pression should have attended the unconstitutional search
in this case.
                        *     *   *
   For the reasons stated, I would reverse the judgment of
the Eleventh Circuit.
                 Cite as: 555 U. S. ____ (2009)           1

                    BREYER, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 07–513
                         _________________


 BENNIE DEAN HERRING, PETITIONER v. UNITED 

                 STATES 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

          APPEALS FOR THE ELEVENTH CIRCUIT

                      [January 14, 2009] 


   JUSTICE BREYER, with whom JUSTICE SOUTER joins,
dissenting.
   I agree with JUSTICE GINSBURG and join her dissent. I
write separately to note one additional supporting factor
that I believe important. In Arizona v. Evans, 514 U. S. 1
(1995), we held that recordkeeping errors made by a court
clerk do not trigger the exclusionary rule, so long as the
police reasonably relied upon the court clerk’s recordkeep
ing. Id., at 14; id., at 16–17 (O’Connor, J., concurring).
The rationale for our decision was premised on a distinc
tion between judicial errors and police errors, and we gave
several reasons for recognizing that distinction.
   First, we noted that “the exclusionary rule was histori
cally designed as a means of deterring police misconduct,
not mistakes by court employees.” Id., at 14 (emphasis
added). Second, we found “no evidence that court employ
ees are inclined to ignore or subvert the Fourth Amend
ment or that lawlessness among these actors requires
application of the extreme sanction of exclusion.” Id., at
14–15. Third, we recognized that there was “no basis for
believing that application of the exclusionary rule. . .
[would] have a significant effect on court employees re
sponsible for informing the police that a warrant has been
quashed. Because court clerks are not adjuncts to the law
enforcement team engaged in the often competitive enter
2               HERRING v. UNITED STATES

                     BREYER, J., dissenting

prise of ferreting out crime, they have no stake in the
outcome of particular criminal prosecutions.” Id., at 15
(citation omitted). Taken together, these reasons explain
why police recordkeeping errors should be treated differ
ently than judicial ones.
   Other cases applying the “good faith” exception to the
exclusionary rule have similarly recognized the distinction
between police errors and errors made by others, such as
judicial officers or legislatures. See United States v. Leon,
468 U. S. 897 (1984) (police reasonably relied on magis
trate’s issuance of warrant); Massachusetts v. Sheppard,
468 U. S. 981 (1984) (same); Illinois v. Krull, 480 U. S. 340
(1987) (police reasonably relied on statute’s constitutional
ity).
   Distinguishing between police recordkeeping errors and
judicial ones not only is consistent with our precedent, but
also is far easier for courts to administer than THE CHIEF
JUSTICE’s case-by-case, multifactored inquiry into the
degree of police culpability. I therefore would apply the
exclusionary rule when police personnel are responsible
for a recordkeeping error that results in a Fourth Amend
ment violation.
   The need for a clear line, and the recognition of such a
line in our precedent, are further reasons in support of the
outcome that JUSTICE GINSBURG’s dissent would reach.

```

---
