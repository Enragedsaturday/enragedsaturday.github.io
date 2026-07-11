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

## GROUP: _overhaul2/lake/cases/Pearson v. Callahan.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Pearson v. Callahan"
type: case
citation: "555 U.S. 223 (2009)"
parallel_cite: "129 S. Ct. 808; 172 L. Ed. 2d 565"
neutral_cite: 2009 U.S. LEXIS 591
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2009
date_decided: 2009-01-21
docket: 07-751
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2009-01-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Pearson v. Callahan
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145918/pearson-v-callahan/"
  cluster_id: 145918
  opinion_id: 145918
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Saucier v. Katz]]", "[[Harlow v. Fitzgerald]]", "[[Graham v. Connor]]", "[[Rivas-Villegas v. Cortesluna]]"]
aliases: []
tags: ["case", "qualified-immunity", "section-1983", "saucier-sequence", "clearly-established"]
holding: "The Saucier two-step sequence, while often appropriate, is NO LONGER MANDATORY. Lower courts may exercise discretion over which prong…"
lake:
  record_id: Pearson v. Callahan
  status: verified
  projected_at: 2026-07-06
---

# Pearson v. Callahan

*555 U.S. 223 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers conducted a warrantless search of Callahan's home after an informant completed a controlled drug buy inside (a "consent-once-removed" theory). Callahan sued under § 1983. Applying the then-mandatory two-step sequence of [[Saucier v. Katz]], the Tenth Circuit held the search unconstitutional and the right clearly established, denying [[Qualified Immunity|qualified immunity]].

## Issue
Whether courts must always follow *Saucier*'s rigid two-step sequence — first deciding whether a constitutional violation occurred, then whether the right was clearly established.

## Rule
No. "On reconsidering the procedure required in *Saucier*, we conclude that, while the sequence set forth there is often appropriate, it should no longer be regarded as mandatory. The judges of the district courts and the courts of appeals should be permitted to exercise their sound discretion in deciding which of the two prongs of the qualified immunity analysis should be addressed first in light of the circumstances in the particular case at hand." — 555 U.S. at 236. ^pin-236

## Application
Exercising the discretion it announced, the Court bypassed the merits of the Fourth Amendment question and resolved the case on the "clearly established" prong: because the "consent-once-removed" doctrine had been accepted by two state supreme courts and three federal circuits when the officers acted, they could reasonably have believed their conduct was lawful, so the right was not clearly established and the officers were entitled to [[Qualified Immunity|qualified immunity]].

## Conclusion
The *Saucier* two-step sequence is no longer mandatory; reversing on the clearly-established prong, the Court held the officers were entitled to [[Qualified Immunity|qualified immunity]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Pearson* freed lower courts to address the qualified-immunity prongs in either order; it **limited** [[Saucier v. Katz]] by removing the mandatory sequencing while preserving *Saucier*'s two-part test.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *Pearson v. Callahan*, 555 U.S. 223 (2009) — https://www.courtlistener.com/opinion/145918/pearson-v-callahan/ — pinpoint: 236.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a60dda296cf9972b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Pearson v. Callahan"}, "payload": {"all": [{"cite": "555 U.S. 223", "page": "223", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "555"}, {"cite": "129 S. Ct. 808", "page": "808", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "129"}, {"cite": "172 L. Ed. 2d 565", "page": "565", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "172"}, {"cite": "2009 U.S. LEXIS 591", "page": "591", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2009"}], "display": "555 U.S. 223", "official": {"cite": "555 U.S. 223", "page": "223", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "555"}, "official_selection_present": true, "record_id": "Pearson v. Callahan"}}
{"assertion_id": "58f603d317e03b1c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-236", "record_id": "Pearson v. Callahan"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-236", "pinpoint_status": "slip-only", "quote": "theory). Callahan sued under § 1983. Applying the then-mandatory two-step sequence of [[Saucier v. Katz]], the Tenth Circuit held the search unconstitutional and the right clearly established, denying qualified immunity. ## Issue Whether courts must always follow *Saucier*'s rigid two-step sequence — first deciding whether a constitutional violation occurred, then whether the right was clearly established. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "Pearson v. Callahan", "star_marker": null}}
{"assertion_id": "99c4c46a983db030", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Pearson v. Callahan"}, "payload": {"as_of_content": "2009-01-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Pearson v. Callahan", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Pearson v. Callahan

```json
{
  "schema_version": "s2.v1",
  "record_id": "Pearson v. Callahan",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Pearson v. Callahan",
    "case_name_short": "Pearson",
    "case_name_full": "PEARSON Et Al. v. CALLAHAN",
    "input_case_name": "Pearson v. Callahan",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2009-01-21",
    "year": 2009,
    "docket": "07-751",
    "cluster_id": 145918,
    "lead_opinion_id": 145918,
    "sibling_ids": [
      145918
    ],
    "absolute_url": "/opinion/145918/pearson-v-callahan/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "555 U.S. 223",
      "volume": "555",
      "reporter": "U.S.",
      "page": "223",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "129 S. Ct. 808",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "808",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "172 L. Ed. 2d 565",
        "volume": "172",
        "reporter": "L. Ed. 2d",
        "page": "565",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2009 U.S. LEXIS 591",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "591",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "555 U.S. 223",
        "volume": "555",
        "reporter": "U.S.",
        "page": "223",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 S. Ct. 808",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "808",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "172 L. Ed. 2d 565",
        "volume": "172",
        "reporter": "L. Ed. 2d",
        "page": "565",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 U.S. LEXIS 591",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "591",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "555 U.S. 223",
    "official_selection": {
      "court_class": "scotus",
      "selected": "555 U.S. 223",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-236",
      "page": null,
      "quote": "theory). Callahan sued under \u00a7 1983. Applying the then-mandatory two-step sequence of [[Saucier v. Katz]], the Tenth Circuit held the search unconstitutional and the right clearly established, denying qualified immunity. ## Issue Whether courts must always follow *Saucier*'s rigid two-step sequence \u2014 first deciding whether a constitutional violation occurred, then whether the right was clearly established. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2009-01-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Pearson v. Callahan",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Nat'l Rifle Ass'n of Am. v. Vullo",
          "cluster_id": 10635063,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane1_negative"
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
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
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
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tolan v. Cotton",
          "cluster_id": 2672535,
          "cite": [
            "188 L. Ed. 2d 895",
            "134 S. Ct. 1861",
            "2014 U.S. LEXIS 3112",
            "82 U.S.L.W. 4358",
            "572 U.S. 650",
            "88 Fed. R. Serv. 3d 765",
            "24 Fla. L. Weekly Fed. S 731",
            "2014 WL 1757856"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
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
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moss v. U.S. Secret Service",
          "cluster_id": 1450162,
          "cite": [
            "572 F.3d 962",
            "2009 U.S. App. LEXIS 15694",
            "2009 WL 2052985"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walker v. Schult",
          "cluster_id": 868764,
          "cite": [
            "717 F.3d 119",
            "2013 U.S. App. LEXIS 10397",
            "2013 WL 2249159"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Padgett v. Wright",
          "cluster_id": 1345341,
          "cite": [
            "587 F.3d 983",
            "2009 U.S. App. LEXIS 25614",
            "2009 WL 3925042"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
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
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
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
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
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
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "White v. Pauly",
          "cluster_id": 4374579,
          "cite": [
            "580 U.S. 73",
            "196 L. Ed. 2d 463",
            "2017 U.S. LEXIS 5",
            "137 S. Ct. 548",
            "26 Fla. L. Weekly Fed. S 409",
            "85 U.S.L.W. 4027",
            "2017 WL 69170"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jonathon Castro v. County of Los Angeles",
          "cluster_id": 4247081,
          "cite": [
            "833 F.3d 1060",
            "2016 U.S. App. LEXIS 14950",
            "2016 WL 4268955"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tracy v. Freshwater",
          "cluster_id": 177179,
          "cite": [
            "623 F.3d 90",
            "2010 U.S. App. LEXIS 21238",
            "2010 WL 4008747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
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
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
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
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alfredo Miranda v. County of Lake",
          "cluster_id": 4525558,
          "cite": [
            "900 F.3d 335"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
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
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony Martin v. Susan Duffy",
          "cluster_id": 4396964,
          "cite": [
            "858 F.3d 239",
            "2017 WL 2366997"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lucas Burgess v. Gene Fischer",
          "cluster_id": 2641010,
          "cite": [
            "735 F.3d 462",
            "2013 WL 5873323",
            "2013 U.S. App. LEXIS 22279"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Everson v. Leis",
          "cluster_id": 1464717,
          "cite": [
            "556 F.3d 484",
            "2009 U.S. App. LEXIS 3288",
            "2009 WL 414625"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Randall v. Scott",
          "cluster_id": 149841,
          "cite": [
            "610 F.3d 701",
            "76 Fed. R. Serv. 3d 1566",
            "30 I.E.R. Cas. (BNA) 1544",
            "2010 U.S. App. LEXIS 13377",
            "93 Empl. Prac. Dec. (CCH) 43,922",
            "2010 WL 2595585"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kisor v. Wilkie",
          "cluster_id": 4632953,
          "cite": [
            "588 U.S. 558",
            "139 S. Ct. 2400",
            "204 L. Ed. 2d 841",
            "2019 U.S. LEXIS 4397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
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
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Atherton v. District of Columbia Office of the Mayor",
          "cluster_id": 187408,
          "cite": [
            "567 F.3d 672",
            "386 U.S. App. D.C. 144",
            "2009 U.S. App. LEXIS 11734",
            "2009 WL 1515373"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pearson v. Callahan:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145918) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzIzNDIwODAwMDAwJnM9MTAwMzgyNTImdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145918%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(145918)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NzAmcz00Mzg3MjI3JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28145918%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145918)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzM3NTkwNDAwMDAwJnM9MTAzMTk5ODgmdD1vJmQ9MjAyNi0wNy0wNiZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145918%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 1,
        "triage_snippet_classified": 199
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145918)",
    "indexed_citing_opinions": 3408,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145918,
        "count": 3408,
        "count_source": "search"
      }
    ],
    "citation_count": 14077,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/pearson-v-callahan.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0Nzg2MzYmcz0xMDY0OTA1NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145918%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145918,
        "cited_id": 102605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 104029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 109680,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 109932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 111481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 112643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 112671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 117958,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 118149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 121169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 131161,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 134724,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 136067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 137736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 145669,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 145707,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 145738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 200739,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 481056,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 766110,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 769027,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 769072,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 770728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 771767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 781742,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 783639,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 784028,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 786761,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 789303,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 791266,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 792791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 796788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 1190202,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 1384819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 1425860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 1457999,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 2197206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 2337194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145918,
        "cited_id": 2581092,
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
    "date_created": "2026-07-05T16:40:00Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:40:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:40:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:42:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:40:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Pearson v. Callahan

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

                   PEARSON ET AL. v. CALLAHAN

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                 THE TENTH CIRCUIT

   No. 07–751.      Argued October 14, 2008—Decided January 21, 2009
After the Utah Court of Appeals vacated respondent’s conviction for
  possession and distribution of drugs, which he sold to an undercover
  informant he had voluntarily admitted into his house, he brought
  this 42 U. S. C. §1983 damages action in federal court, alleging that
  petitioners, the officers who supervised and conducted the war
  rantless search of the premises that led to his arrest after the sale,
  had violated the Fourth Amendment. The District Court granted
  summary judgment in favor of the officers. Noting that other courts
  had adopted the “consent-once-removed” doctrine—which permits a
  warrantless police entry into a home when consent to enter has al
  ready been granted to an undercover officer who has observed con
  traband in plain view—the court concluded that the officers were en
  titled to qualified immunity because they could reasonably have
  believed that the doctrine authorized their conduct. Following the
  procedure mandated in Saucier v. Katz, 533 U. S. 194, the Tenth Cir
  cuit held that petitioners were not entitled to qualified immunity.
  The court disapproved broadening the consent-once-removed doctrine
  to situations in which the person granted initial consent was not an
  undercover officer, but merely an informant. It further held that the
  Fourth Amendment right to be free in one’s home from unreasonable
  searches and arrests was clearly established at the time of respon
  dent’s arrest, and determined that, under this Court’s clearly estab
  lished precedents, warrantless entries into a home are per se unrea
  sonable unless they satisfy one of the two established exceptions for
  consent and exigent circumstances. The court concluded that peti
  tioners could not reasonably have believed that their conduct was
  lawful because they knew that (1) they had no warrant; (2) respon
  dent had not consented to their entry; and (3) his consent to the entry
2                      PEARSON v. CALLAHAN

                                 Syllabus

    of an informant could not reasonably be interpreted to extend to
    them. In granting certiorari, this Court directed the parties to ad
    dress whether Saucier should be overruled in light of widespread
    criticism directed at it.
Held:
    1. The Saucier procedure should not be regarded as an inflexible
 requirement. Pp. 5–19.
       (a) Saucier mandated, see 533 U. S., at 194, a two-step sequence
 for resolving government officials’ qualified immunity claims: A court
 must decide (1) whether the facts alleged or shown by the plaintiff
 make out a violation of a constitutional right, and (2) if so, whether
 that right was “clearly established” at the time of the defendant’s al
 leged misconduct, id., at 201. Qualified immunity applies unless the
 official's conduct violated such a right. Anderson v. Creighton, 483
 U. S. 635, 640. Pp. 5–7.
       (b) Stare decisis does not prevent this Court from determining
 whether the Saucier procedure should be modified or abandoned.
 Revisiting precedent is particularly appropriate where, as here, a de
 parture would not upset settled expectations, see, e.g., United States
 v. Gaudin, 515 U. S. 506, 521; the precedent consists of a rule that is
 judge-made and adopted to improve court operations, not a statute
 promulgated by Congress, see, e.g., State Oil Co. v. Khan, 522 U. S. 3,
 20; and the precedent has “been questioned by Members of th[is]
 Court in later decisions, and [has] defied consistent application by
 the lower courts,” Payne v. Tennessee, 501 U. S. 808, 829–830. Re
 spondent’s argument that Saucier should not be reconsidered unless
 the Court concludes that it was “badly reasoned” or that its rule has
 proved “unworkable,” see Payne, supra, at 827, is rejected. Those
 standards are out of place in the present context, where a consider
 able body of new experience supports a determination that a manda
 tory, two-step rule for resolving all qualified immunity claims should
 not be retained. Pp. 7–10.
       (c) Reconsideration of the Saucier procedure demonstrates that,
 while the sequence set forth therein is often appropriate, it should no
 longer be regarded as mandatory in all cases. Pp. 10–19.
          (i) The Court continues to recognize that the Saucier protocol is
 often beneficial. In some cases, a discussion of why the relevant facts
 do not violate clearly established law may make it apparent that in
 fact the relevant facts do not make out a constitutional violation at
 all. And Saucier was correct in noting that the two-step procedure
 promotes the development of constitutional precedent and is espe
 cially valuable for questions that do not frequently arise in cases in
 which a qualified immunity defense is unavailable. See 533 U. S., at
 194. Pp. 10–11.
                   Cite as: 555 U. S. ____ (2009)                     3

                              Syllabus

        (ii) Nevertheless, experience in this Court and the lower fed
eral courts has pointed out the rigid Saucier procedure’s shortcom
ings. For example, it may result in a substantial expenditure of
scarce judicial resources on difficult questions that have no effect on
the case’s outcome, and waste the parties’ resources by forcing them
to assume the costs of litigating constitutional questions and endure
delays attributable to resolving those questions when the suit other
wise could be disposed of more readily. Moreover, although the
procedure’s first prong is intended to further the development of
constitutional precedent, opinions following that procedure often fail
to make a meaningful contribution to such development. Further,
when qualified immunity is asserted at the pleading stage, the
answer to whether there was a violation may depend on a kalei
doscope of facts not yet fully developed. And the first step may create
a risk of bad decisionmaking, as where the briefing of constitutional
questions is woefully inadequate. Application of the Saucier rule also
may make it hard for affected parties to obtain appellate review of
constitutional decisions having a serious prospective effect on their
operations. For example, where a court holds that a defendant has
committed a constitutional violation, but then holds that the viola
tion was not clearly established, the defendant, as the winning party,
may have his right to appeal the adverse constitutional holding chal
lenged. Because rigid adherence to Saucier departs from the general
rule of constitutional avoidance, cf., e.g., Scott v. Harris, 550 U. S.
372, 388, the Court may appropriately decline to mandate the order
of decision that the lower courts must follow, see, e.g., Strickland v.
Washington, 466 U. S. 668, 697. This flexibility properly reflects the
Court’s respect for the lower federal courts. Because the two-step
Saucier procedure is often, but not always, advantageous, those
judges are in the best position to determine the order of decisionmak
ing that will best facilitate the fair and efficient disposition of each
case. Pp. 11–17.
        (iii) Misgivings concerning today’s decision are unwarranted.
It does not prevent the lower courts from following Saucier; it simply
recognizes that they should have the discretion to decide whether
that procedure is worthwhile in particular cases. Moreover, it will
not retard the development of constitutional law, result in a prolif
eration of damages claims against local governments, or spawn new
litigation over the standards for deciding whether to reach the par
ticular case’s merits. Pp. 17–19.
   2. Petitioners are entitled to qualified immunity because it was not
clearly established at the time of the search that their conduct was
unconstitutional.      When the entry occurred, the consent-once
4                       PEARSON v. CALLAHAN

                                 Syllabus

    removed doctrine had been accepted by two State Supreme Courts
    and three Federal Courts of Appeals, and not one of the latter had is
    sued a contrary decision. Petitioners were entitled to rely on these
    cases, even though their own Federal Circuit had not yet ruled on
    consent-once-removed entries. See Wilson v. Layne, 526 U. S. 603,
    618. Pp. 19–20.
494 F. 3d 891, reversed.

    ALITO, J., delivered the opinion for a unanimous Court.
                       Cite as: 555 U. S. ____ (2009)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 07–751
                                  _________________


CORDELL PEARSON, ET AL., PETITIONERS v. AFTON
               CALLAHAN
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE TENTH CIRCUIT
                              [January 21, 2009]

  JUSTICE ALITO delivered the opinion of the Court.
   This is an action brought by respondent under Rev.
Stat. §1979, 42 U. S. C. §1983, against state law enforce
ment officers who conducted a warrantless search of his
house incident to his arrest for the sale of methampheta
mine to an undercover informant whom he had voluntarily
admitted to the premises. The Court of Appeals held that
petitioners were not entitled to summary judgment on
qualified immunity grounds. Following the procedure we
mandated in Saucier v. Katz, 533 U. S. 194 (2001), the
Court of Appeals held, first, that respondent adduced facts
sufficient to make out a violation of the Fourth Amend
ment and, second, that the unconstitutionality of the
officers’ conduct was clearly established. In granting
review, we required the parties to address the additional
question whether the mandatory procedure set out in
Saucier should be retained.
   We now hold that the Saucier procedure should not be
regarded as an inflexible requirement and that petitioners
are entitled to qualified immunity on the ground that it
was not clearly established at the time of the search that
2                 PEARSON v. CALLAHAN

                    Opinion of the Court

their conduct was unconstitutional. We therefore reverse.
                             I

                            A

  The Central Utah Narcotics Task Force is charged with
investigating illegal drug use and sales. In 2002, Brian
Bartholomew, who became an informant for the task force
after having been charged with the unlawful possession of
methamphetamine, informed Officer Jeffrey Whatcott that
respondent Afton Callahan had arranged to sell Bar
tholomew methamphetamine later that day.
  That evening, Bartholomew arrived at respondent’s
residence at about 8 p.m. Once there, Bartholomew went
inside and confirmed that respondent had methampheta
mine available for sale. Bartholomew then told respon
dent that he needed to obtain money to make his purchase
and left.
  Bartholomew met with members of the task force at
about 9 p.m. and told them that he would be able to buy a
gram of methamphetamine for $100. After concluding
that Bartholomew was capable of completing the planned
purchase, the officers searched him, determined that he
had no controlled substances on his person, gave him a
marked $100 bill and a concealed electronic transmitter to
monitor his conversations, and agreed on a signal that he
would give after completing the purchase.
  The officers drove Bartholomew to respondent’s trailer
home, and respondent’s daughter let him inside. Respon
dent then retrieved a large bag containing methampheta
mine from his freezer and sold Bartholomew a gram of
methamphetamine, which he put into a small plastic bag.
Bartholomew gave the arrest signal to the officers who
were monitoring the conversation, and they entered the
trailer through a porch door. In the enclosed porch, the
officers encountered Bartholomew, respondent, and two
other persons, and they saw respondent drop a plastic bag,
                 Cite as: 555 U. S. ____ (2009)          3

                     Opinion of the Court

which they later determined contained methampheta
mine. The officers then conducted a protective sweep
of the premises. In addition to the large bag of meth-
amphetamine, the officers recovered the marked bill
from respondent and a small bag containing meth-
amphetamine from Bartholomew, and they found drug
syringes in the residence. As a result, respondent was
charged with the unlawful possession and distribution of
methamphetamine.
                              B
  The trial court held that the warrantless arrest and
search were supported by exigent circumstances. On
respondent’s appeal from his conviction, the Utah attorney
general conceded the absence of exigent circumstances,
but urged that the inevitable discovery doctrine justified
introduction of the fruits of the warrantless search. The
Utah Court of Appeals disagreed and vacated respondent’s
conviction. See State v. Callahan, 2004 LIT App. 164, 93
P. 3d 103. Respondent then brought this damages action
under 42 U. S. C. §1983 in the United States District
Court for the District of Utah, alleging that the officers
had violated the Fourth Amendment by entering his home
without a warrant. See Callahan v. Millard Cty., No.
2:04–CV–00952, 2006 WL 1409130 (2006).
  In granting the officers’ motion for summary judgment,
the District Court noted that other courts had adopted the
“consent-once-removed” doctrine, which permits a war
rantless entry by police officers into a home when consent
to enter has already been granted to an undercover officer
or informant who has observed contraband in plain view.
Believing that this doctrine was in tension with our inter
vening decision in Georgia v. Randolph, 547 U. S. 103
(2006), the District Court concluded that “the simplest
approach is to assume that the Supreme Court will ulti
mately reject the [consent-once-removed] doctrine and find
4                 PEARSON v. CALLAHAN

                     Opinion of the Court

that searches such as the one in this case are not reason
able under the Fourth Amendment.” 2006 WL 1409130,
at *8. The Court then held that the officers were entitled
to qualified immunity because they could reasonably have
believed that the consent-once-removed doctrine author
ized their conduct.
   On appeal, a divided panel of the Tenth Circuit held
that petitioners’ conduct violated respondent’s Fourth
Amendment rights. Callahan v. Millard Cty., 494 F. 3d
891, 895–899 (2007). The panel majority stated that “[t]he
‘consent-once-removed’ doctrine applies when an under
cover officer enters a house at the express invitation of
someone with authority to consent, establishes probable
cause to arrest or search, and then immediately summons
other officers for assistance.” Id., at 896. The majority
took no issue with application of the doctrine when the
initial consent was granted to an undercover law enforce
ment officer, but the majority disagreed with decisions
that “broade[n] this doctrine to grant informants the same
capabilities as undercover officers.” Ibid.
   The Tenth Circuit panel further held that the Fourth
Amendment right that it recognized was clearly estab
lished at the time of respondent’s arrest. Id., at 898–899.
“In this case,” the majority stated, “the relevant right is
the right to be free in one’s home from unreasonable
searches and arrests.” Id., at 898. The Court determined
that, under the clearly established precedents of this
Court and the Tenth Circuit, “warrantless entries into a
home are per se unreasonable unless they satisfy the
established exceptions.” Id., at 898–899. In the panel’s
words, “the Supreme Court and the Tenth Circuit have
clearly established that to allow police entry into a home,
the only two exceptions to the warrant requirement are
consent and exigent circumstances.” Id., at 899. Against
that backdrop, the panel concluded, petitioners could not
reasonably have believed that their conduct was lawful
                 Cite as: 555 U. S. ____ (2009)            5

                     Opinion of the Court

because petitioners “knew (1) they had no warrant; (2)
[respondent] had not consented to their entry; and (3)
[respondent’s] consent to the entry of an informant could
not reasonably be interpreted to extend to them.” Ibid.
  In dissent, Judge Kelly argued that “no constitutional
violation occurred in this case” because, by inviting Bar
tholomew into his house and participating in a narcotics
transaction there, respondent had compromised the pri
vacy of the residence and had assumed the risk that Bar
tholomew would reveal their dealings to the police. Id., at
903. Judge Kelly further concluded that, even if petition
ers’ conduct had been unlawful, they were nevertheless
entitled to qualified immunity because the constitutional
right at issue—“the right to be free from the warrantless
entry of police officers into one’s home to effectuate an
arrest after one has granted voluntary, consensual entry
to a confidential informant and undertaken criminal
activity giving rise to probable cause”—was not “clearly
established” at the time of the events in question. Id., at
903–904.
  As noted, the Court of Appeals followed the Saucier
procedure. The Saucier procedure has been criticized by
Members of this Court and by lower court judges, who
have been required to apply the procedure in a great
variety of cases and thus have much firsthand experience
bearing on its advantages and disadvantages. Accord
ingly, in granting certiorari, we directed the parties to
address the question whether Saucier should be overruled.
552 U. S. ___ (2008).
                               II 

                               A

  The doctrine of qualified immunity protects government
officials “from liability for civil damages insofar as their
conduct does not violate clearly established statutory or
constitutional rights of which a reasonable person would
6                  PEARSON v. CALLAHAN

                      Opinion of the Court

have known.” Harlow v. Fitzgerald, 457 U. S. 800, 818
(1982). Qualified immunity balances two important inter
ests—the need to hold public officials accountable when
they exercise power irresponsibly and the need to shield
officials from harassment, distraction, and liability when
they perform their duties reasonably. The protection of
qualified immunity applies regardless of whether the
government official’s error is “a mistake of law, a mistake
of fact, or a mistake based on mixed questions of law and
fact.”    Groh v. Ramirez, 540 U. S. 551, 567 (2004)
(KENNEDY, J., dissenting) (citing Butz v. Economou, 438
U. S. 478, 507 (1978) (noting that qualified immunity
covers “mere mistakes in judgment, whether the mistake
is one of fact or one of law”)).
   Because qualified immunity is “an immunity from suit
rather than a mere defense to liability . . . it is effectively
lost if a case is erroneously permitted to go to trial.”
Mitchell v. Forsyth, 472 U. S. 511, 526 (1985) (emphasis
deleted). Indeed, we have made clear that the “driving
force” behind creation of the qualified immunity doctrine
was a desire to ensure that “ ‘insubstantial claims’ against
government officials [will] be resolved prior to discovery.”
Anderson v. Creighton, 483 U. S. 635, 640, n. 2 (1987).
Accordingly, “we repeatedly have stressed the importance
of resolving immunity questions at the earliest possible
stage in litigation.” Hunter v. Bryant, 502 U. S. 224, 227
(1991) (per curiam).
   In Saucier, 533 U. S. 194, this Court mandated a two
step sequence for resolving government officials’ qualified
immunity claims. First, a court must decide whether the
facts that a plaintiff has alleged (see Fed. Rules Civ. Proc.
12(b)(6), (c)) or shown (see Rules 50, 56) make out a viola
tion of a constitutional right. 533 U. S., at 201. Second, if
the plaintiff has satisfied this first step, the court must
decide whether the right at issue was “clearly established”
at the time of defendant’s alleged misconduct. Ibid.
                 Cite as: 555 U. S. ____ (2009)            7

                     Opinion of the Court

Qualified immunity is applicable unless the official’s
conduct violated a clearly established constitutional right.
Anderson, supra, at 640.
    Our decisions prior to Saucier had held that “the better
approach to resolving cases in which the defense of quali
fied immunity is raised is to determine first whether the
plaintiff has alleged a deprivation of a constitutional right
at all.” County of Sacramento v. Lewis, 523 U. S. 833, 841,
n. 5 (1998). Saucier made that suggestion a mandate. For
the first time, we held that whether “the facts alleged
show the officer’s conduct violated a constitutional right
. . . must be the initial inquiry” in every qualified immu
nity case. 533 U. S., at 20 (emphasis added). Only after
completing this first step, we said, may a court turn to
“the next, sequential step,” namely, “whether the right
was clearly established.” Ibid.
    This two-step procedure, the Saucier Court reasoned, is
necessary to support the Constitution’s “elaboration from
case to case” and to prevent constitutional stagnation.
Ibid. “The law might be deprived of this explanation were
a court simply to skip ahead to the question whether the
law clearly established that the officer's conduct was
unlawful in the circumstances of the case.” Ibid.
                              B
  In considering whether the Saucier procedure should be
modified or abandoned, we must begin with the doctrine of
stare decisis. Stare decisis “promotes the evenhanded,
predictable, and consistent development of legal princi
ples, fosters reliance on judicial decisions, and contributes
to the actual and perceived integrity of the judicial proc
ess.” Payne v. Tennessee, 501 U. S. 808, 827 (1991). Al
though “[w]e approach the reconsideration of [our] deci
sions . . . with the utmost caution,” “[s]tare decisis is not
an inexorable command.” State Oil Co. v. Khan, 522 U. S.
3, 20 (1997) (internal quotation marks omitted). Revisit
8                  PEARSON v. CALLAHAN

                     Opinion of the Court

ing precedent is particularly appropriate where, as here, a
departure would not upset expectations, the precedent
consists of a judge-made rule that was recently adopted to
improve the operation of the courts, and experience has
pointed up the precedent’s shortcomings.
   “Considerations in favor of stare decisis are at their
acme in cases involving property and contract rights,
where reliance interests are involved; the opposite is true
in cases . . . involving procedural and evidentiary rules”
that do not produce such reliance. Payne, supra, at 828
(citations omitted). Like rules governing procedures and
the admission of evidence in the trial courts, Saucier’s
two-step protocol does not affect the way in which parties
order their affairs. Withdrawing from Saucier’s categori
cal rule would not upset settled expectations on anyone’s
part. See United States v. Gaudin, 515 U. S. 506, 521
(1995).
   Nor does this matter implicate “the general presumption
that legislative changes should be left to Congress.” Khan,
supra, at 20. We recognize that “considerations of stare
decisis weigh heavily in the area of statutory construction,
where Congress is free to change this Court’s interpreta
tion of its legislation.” Illinois Brick Co. v. Illinois, 431
U. S. 720, 736 (1977). But the Saucier rule is judge made
and implicates an important matter involving internal
Judicial Branch operations. Any change should come from
this Court, not Congress.
   Respondent argues that the Saucier procedure should
not be reconsidered unless we conclude that its justifica
tion was “badly reasoned” or that the rule has proved to be
“unworkable,” see Payne, supra, at 827, but those stan
dards, which are appropriate when a constitutional or
statutory precedent is challenged, are out of place in the
present context. Because of the basis and the nature of
the Saucier two-step protocol, it is sufficient that we now
have a considerable body of new experience to consider
                  Cite as: 555 U. S. ____ (2009)            9

                      Opinion of the Court

regarding the consequences of requiring adherence to this
inflexible procedure. This experience supports our present
determination that a mandatory, two-step rule for resolv
ing all qualified immunity claims should not be retained.
   Lower court judges, who have had the task of applying
the Saucier rule on a regular basis for the past eight
years, have not been reticent in their criticism of Saucier’s
“rigid order of battle.” See, e.g., Purtell v. Mason, 527
F. 3d 615, 622 (CA7 2008) (“This ‘rigid order of battle’ has
been criticized on practical, procedural, and substantive
grounds”); Leval, Judging Under the Constitution: Dicta
About Dicta, 81 N. Y. U. L. Rev. 1249, 1275, 1277 (2006)
(referring to Saucier’s mandatory two-step framework as
“a new and mischievous rule” that amounts to “a puzzling
misadventure in constitutional dictum”). And application
of the rule has not always been enthusiastic. See Higazy
v. Templeton, 505 F. 3d 161, 179, n. 19 (CA2 2007) (“We do
not reach the issue of whether [plaintiff’s] Sixth Amend
ment rights were violated, because principles of judicial
restraint caution us to avoid reaching constitutional ques
tions when they are unnecessary to the disposition of a
case”); Cherrington v. Skeeter, 344 F. 3d 631, 640 (CA6
2003) (“[I]t ultimately is unnecessary for us to decide
whether the individual Defendants did or did not heed the
Fourth Amendment command . . . because they are enti
tled to qualified immunity in any event”); Pearson v.
Ramos, 237 F. 3d 881, 884 (CA7 2001) (“Whether [the
Saucier] rule is absolute may be doubted”).
   Members of this Court have also voiced criticism of the
Saucier rule. See Morse v. Frederick, 551 U. S. ___, ___
(2007) (slip op., at 8) (BREYER, J., concurring in judgment
in part and dissenting in part) (“I would end the failed
Saucier experiment now”); Bunting v. Mellen, 541 U. S.
1019 (2004) (STEVENS, J., joined by GINSBURG and
BREYER, JJ., respecting denial of certiorari) (criticizing the
“unwise judge-made rule under which courts must decide
10                 PEARSON v. CALLAHAN

                     Opinion of the Court

whether the plaintiff has alleged a constitutional violation
before addressing the question whether the defendant
state actor is entitled to qualified immunity”); Id., at 1025
(SCALIA, J., joined by Rehnquist, C. J., dissenting from
denial of certiorari) (“We should either make clear that
constitutional determinations are not insulated from our
review . . . or else drop any pretense at requiring the
ordering in every case” (emphasis in original)); Brosseau v.
Haugen, 543 U. S. 194, 201–202 (2004) (BREYER, J., joined
by SCALIA and GINSBURG, JJ., concurring) (urging Court
to reconsider Saucier’s “rigid ‘order of battle,’ ” which
“requires courts unnecessarily to decide difficult constitu
tional questions when there is available an easier basis for
the decision (e.g., qualified immunity) that will satisfacto
rily resolve the case before the court”); Saucier, 533 U. S.,
at 210 (GINSBURG, J., concurring in judgment) (“The two
part test today’s decision imposes holds large potential to
confuse”).
   Where a decision has “been questioned by Members of
the Court in later decisions and [has] defied consistent
application by the lower courts,” these factors weigh in
favor of reconsideration. Payne, 501 U. S., at 829–830; see
also Crawford v. Washington, 541 U. S. 36, 60 (2004).
Collectively, the factors we have noted make our present
reevaluation of the Saucier two-step protocol appropriate.
                            III
   On reconsidering the procedure required in Saucier, we
conclude that, while the sequence set forth there is often
appropriate, it should no longer be regarded as manda
tory. The judges of the district courts and the courts of
appeals should be permitted to exercise their sound discre
tion in deciding which of the two prongs of the qualified
immunity analysis should be addressed first in light of the
circumstances in the particular case at hand.
                 Cite as: 555 U. S. ____ (2009) 
         11

                     Opinion of the Court 


                              A

   Although we now hold that the Saucier protocol should
not be regarded as mandatory in all cases, we continue to
recognize that it is often beneficial. For one thing, there
are cases in which there would be little if any conservation
of judicial resources to be had by beginning and ending
with a discussion of the “clearly established” prong. “[I]t
often may be difficult to decide whether a right is clearly
established without deciding precisely what the constitu
tional right happens to be.” Lyons v. Xenia, 417 F. 3d 565,
581 (CA6 2005) (Sutton, J., concurring). In some cases, a
discussion of why the relevant facts do not violate clearly
established law may make it apparent that in fact the
relevant facts do not make out a constitutional violation at
all. In addition, the Saucier Court was certainly correct in
noting that the two-step procedure promotes the develop
ment of constitutional precedent and is especially valu-
able with respect to questions that do not frequently
arise in cases in which a qualified immunity defense is
unavailable.
                              B
   At the same time, however, the rigid Saucier procedure
comes with a price. The procedure sometimes results in a
substantial expenditure of scarce judicial resources on
difficult questions that have no effect on the outcome of
the case. There are cases in which it is plain that a consti
tutional right is not clearly established but far from obvi
ous whether in fact there is such a right. District courts
and courts of appeals with heavy caseloads are often
understandably unenthusiastic about what may seem to
be an essentially academic exercise.
   Unnecessary litigation of constitutional issues also
wastes the parties’ resources. Qualified immunity is “an
immunity from suit rather than a mere defense to liabil
ity.” Mitchell, 472 U. S., at 526 (emphasis deleted). Sau
12                    PEARSON v. CALLAHAN

                         Opinion of the Court

cier’s two-step protocol “disserve[s] the purpose of quali
fied immunity” when it “forces the parties to endure addi
tional burdens of suit—such as the costs of litigating
constitutional questions and delays attributable to resolv
ing them—when the suit otherwise could be disposed of
more readily.” Brief for Nat. Assn. of Criminal Defense
Lawyers as Amicus Curiae 30.
   Although the first prong of the Saucier procedure is
intended to further the development of constitutional
precedent, opinions following that procedure often fail to
make a meaningful contribution to such development. For
one thing, there are cases in which the constitutional
question is so fact-bound that the decision provides little
guidance for future cases. See Scott v. Harris, 550 U. S.
372, 388 (2007) (BREYER, J., concurring) (counseling
against the Saucier two-step protocol where the question
is “so fact dependent that the result will be confusion
rather than clarity”); Buchanan v. Maine, 469 F. 3d 158,
168 (CA1 2006) (“We do not think the law elaboration
purpose will be well served here, where the Fourth
Amendment inquiry involves a reasonableness question
which is highly idiosyncratic and heavily dependent on the
facts”).
   A decision on the underlying constitutional question in a
§1983 damages action or a Bivens v. Six Unknown Fed.
Narcotics Agents, 403 U. S. 388 (1971),1 action may have
scant value when it appears that the question will soon be
decided by a higher court. When presented with a consti
tutional question on which this Court had just granted
certiorari, the Ninth Circuit elected to “bypass Saucier’s
first step and decide only whether [the alleged right] was

——————
  1 See  Harlow v. Fitzgerald, 457 U. S. 800, 818, and n. 30 (1982) (not
ing that the Court’s decisions equate the qualified immunity of state
officials sued under 42 U. S. C. §1983 with the immunity of federal
officers sued directly under the Constitution).
                 Cite as: 555 U. S. ____ (2009)           13

                     Opinion of the Court

clearly established.” Motley v. Parks, 432 F. 3d 1072,
1078, and n. 5 (2005) (en banc). Similar considerations
may come into play when a court of appeals panel con
fronts a constitutional question that is pending before the
court en banc or when a district court encounters a consti
tutional question that is before the court of appeals.
   A constitutional decision resting on an uncertain inter
pretation of state law is also of doubtful precedential
importance. As a result, several courts have identified an
“exception” to the Saucier rule for cases in which resolu
tion of the constitutional question requires clarification of
an ambiguous state statute. Egolf v. Witmer, 526 F. 3d
104, 109–111 (CA3 2008); accord, Tremblay v. McClellan,
350 F. 3d 195, 200 (CA1 2003); Ehrlich v. Glastonbury,
348 F. 3d 48, 57–60 (CA2 2003). Justifying the decision to
grant qualified immunity to the defendant without first
resolving, under Saucier’s first prong, whether the defen
dant’s conduct violated the Constitution, these courts have
observed that Saucier’s “underlying principle” of encourag
ing federal courts to decide unclear legal questions in
order to clarify the law for the future “is not meaningfully
advanced . . . when the definition of constitutional rights
depends on a federal court’s uncertain assumptions about
state law.” Egolf, supra, at 110; accord, Tremblay, supra,
at 200; Ehrlich, supra, at 58.
   When qualified immunity is asserted at the pleading
stage, the precise factual basis for the plaintiff’s claim or
claims may be hard to identify. See Lyons, supra, at 582
(Sutton, J., concurring); Kwai Fun Wong v. United States,
373 F. 3d 952, 957 (CA9 2004); Mollica v. Volker, 229 F. 3d
366, 374 (CA2 2000). Accordingly, several courts have
recognized that the two-step inquiry “is an uncomfortable
exercise where . . . the answer [to] whether there was a
violation may depend on a kaleidoscope of facts not yet
fully developed” and have suggested that “[i]t may be that
Saucier was not strictly intended to cover” this situation.
14                PEARSON v. CALLAHAN

                     Opinion of the Court

Dirrane v. Brookline Police Dept., 315 F. 3d 65, 69–70
(CA1 2002); see also Robinette v. Jones, 476 F. 3d 585, 592,
n. 8 (CA8 2007) (declining to follow Saucier because “the
parties have provided very few facts to define and limit
any holding” on the constitutional question).
   There are circumstances in which the first step of the
Saucier procedure may create a risk of bad decisionmak
ing. The lower courts sometimes encounter cases in which
the briefing of constitutional questions is woefully inade
quate. See Lyons, 417 F. 3d, at 582 (Sutton, J., concur
ring) (noting the “risk that constitutional questions may
be prematurely and incorrectly decided in cases where
they are not well presented”); Mollica, supra, at 374.
   Although the Saucier rule prescribes the sequence in
which the issues must be discussed by a court in its opin
ion, the rule does not—and obviously cannot—specify the
sequence in which judges reach their conclusions in their
own internal thought processes. Thus, there will be cases
in which a court will rather quickly and easily decide that
there was no violation of clearly established law before
turning to the more difficult question whether the relevant
facts make out a constitutional question at all. In such
situations, there is a risk that a court may not devote as
much care as it would in other circumstances to the deci
sion of the constitutional issue. See Horne v. Coughlin,
191 F. 3d, 244, 247 (CA2 1999) (“Judges risk being insuffi
ciently thoughtful and cautious in uttering pronounce
ments that play no role in their adjudication”); Leval
1278–1279.
   Rigid adherence to the Saucier rule may make it hard
for affected parties to obtain appellate review of constitu
tional decisions that may have a serious prospective effect
on their operations. Where a court holds that a defendant
committed a constitutional violation but that the violation
was not clearly established, the defendant may face a
difficult situation. As the winning party, the defendant’s
                      Cite as: 555 U. S. ____ (2009)                    15

                          Opinion of the Court

right to appeal the adverse holding on the constitutional
question may be contested. See Bunting, 541 U. S., at
1025 (SCALIA, J., dissenting from denial of certiorari)
(“The perception of unreviewability undermines adherence
to the sequencing rule we . . . created” in Saucier);2 see
also Kalka v. Hawk, 215 F. 3d 90, 96, n. 9 (CADC 2000)
(noting that “[n]ormally, a party may not appeal from a
favorable judgment” and that the Supreme Court “has
apparently never granted the certiorari petition of a party
who prevailed in the appellate court”). In cases like Bun
ting, the “prevailing” defendant faces an unenviable
choice: “compl[y] with the lower court’s advisory dictum
without opportunity to seek appellate [or certiorari] re
view,” or “def[y] the views of the lower court, adher[e] to
practices that have been declared illegal, and thus invit[e]
new suits” and potential “punitive damages.” Horne,
supra, at 247–248.
   Adherence to Saucier’s two-step protocol departs from
the general rule of constitutional avoidance and runs
counter to the “older, wiser judicial counsel ‘not to pass on
questions of constitutionality . . . unless such adjudication
is unavoidable.’ ” Scott, 550 U. S., at 388 (BREYER, J.,

——————
  2 In Bunting, the Court of Appeals followed the Saucier two-step pro

tocol and first held that the Virginia Military Institute’s use of the word
“God” in a “supper roll call” ceremony violated the Establishment
Clause, but then granted the defendants qualified immunity because
the law was not clearly established at the relevant time. Mellen v.
Bunting, 327 F. 3d 355, 365–376 (CA4 2003), cert. denied, 541 U. S.
1019 (2004). Although they had a judgment in their favor below, the
defendants asked this Court to review the adverse constitutional
ruling. Dissenting from the denial of certiorari, JUSTICE SCALIA, joined
by Chief Justice Rehnquist, criticized “a perceived procedural tangle of
the Court’s own making.” 541 U. S., at 1022. The “tangle” arose from
the Court’s “ ‘settled refusal’ to entertain an appeal by a party on an
issue as to which he prevailed” below, a practice that insulates from
review adverse merits decisions that are “locked inside” favorable
qualified immunity rulings. Id., at 1023, 1024.
16                 PEARSON v. CALLAHAN

                      Opinion of the Court

concurring) (quoting Spector Motor Service, Inc. v.
McLaughlin, 323 U. S. 101, 105 (1944)); see Ashwander v.
TVA, 297 U. S. 288, 347 (1936) (Brandeis, J., concurring)
(“The Court will not pass upon a constitutional question
although properly presented by the record, if there is also
present some other ground upon which the case may be
disposed of ”).
   In other analogous contexts, we have appropriately
declined to mandate the order of decision that the lower
courts must follow. For example, in Strickland v. Wash
ington, 466 U. S. 668 (1984), we recognized a two-part test
for determining whether a criminal defendant was denied
the effective assistance of counsel: The defendant must
demonstrate (1) that his counsel’s performance fell below
what could be expected of a reasonably competent practi
tioner; and (2) that he was prejudiced by that substandard
performance. Id., at 687. After setting forth and applying
the analytical framework that courts must use in evaluat
ing claims of ineffective assistance of counsel, we left it to
the sound discretion of lower courts to determine the order
of decision. Id., at 697 (“Although we have discussed the
performance component of an ineffectiveness claim prior
to the prejudice component, there is no reason for a court
deciding an ineffective assistance claim to approach the
inquiry in the same order or even to address both compo
nents of the inquiry if the defendant makes an insufficient
showing on one”).
   In United States v. Leon, 468 U. S. 897 (1984), we cre
ated an exception to the exclusionary rule when officers
reasonably rely on a facially valid search warrant. Id., at
913. In that context, we recognized that a defendant
challenging a search will lose if either: (1) the warrant
issued was supported by probable cause; or (2) it was not,
but the officers executing it reasonably believed that it
was. Again, after setting forth and applying the analytical
framework that courts must use in evaluating the good
                  Cite as: 555 U. S. ____ (2009)            17

                      Opinion of the Court

faith exception to the Fourth Amendment warrant re
quirement, we left it to the sound discretion of the lower
courts to determine the order of decision. Id., at 924, 925
(“There is no need for courts to adopt the inflexible prac
tice of always deciding whether the officers’ conduct mani
fested objective good faith before turning to the question
whether the Fourth Amendment has been violated”).
   This flexibility properly reflects our respect for the lower
federal courts that bear the brunt of adjudicating these
cases. Because the two-step Saucier procedure is often,
but not always, advantageous, the judges of the district
courts and the courts of appeals are in the best position to
determine the order of decisionmaking will best facilitate
the fair and efficient disposition of each case.
                               C
   Any misgivings concerning our decision to withdraw
from the mandate set forth in Saucier are unwarranted.
Our decision does not prevent the lower courts from fol
lowing the Saucier procedure; it simply recognizes that
those courts should have the discretion to decide whether
that procedure is worthwhile in particular cases. More
over, the development of constitutional law is by no means
entirely dependent on cases in which the defendant may
seek qualified immunity. Most of the constitutional issues
that are presented in §1983 damages actions and Bivens
cases also arise in cases in which that defense is not avail
able, such as criminal cases and §1983 cases against a
municipality, as well as §1983 cases against individuals
where injunctive relief is sought instead of or in addition
to damages. See Lewis, 523 U. S., at 841, n. 5 (noting that
qualified immunity is unavailable “in a suit to enjoin
future conduct, in an action against a municipality, or in
litigating a suppression motion”).
   We also do not think that relaxation of Saucier’s man
date is likely to result in a proliferation of damages claims
18                  PEARSON v. CALLAHAN

                      Opinion of the Court

against local governments. Compare Brief for Nat. Assn.
of Counties et al., as Amici Curiae 29, 30 (“[T]o the extent
that a rule permitting courts to bypass the merits makes it
more difficult for civil rights plaintiffs to pursue novel
claims, they will have greater reason to press custom,
policy, or practice [damages] claims against local govern
ments”). It is hard to see how the Saucier procedure could
have a significant effect on a civil rights plaintiff’s decision
whether to seek damages only from a municipal employee
or also from the municipality. Whether the Saucier proce
dure is mandatory or discretionary, the plaintiff will pre
sumably take into account the possibility that the individ
ual defendant will be held to have qualified immunity, and
presumably the plaintiff will seek damages from the mu
nicipality as well as the individual employee if the benefits
of doing so (any increase in the likelihood of recovery or
collection of damages) outweigh the litigation costs.
   Nor do we think that allowing the lower courts to exer
cise their discretion with respect to the Saucier procedure
will spawn “a new cottage industry of litigation . . . over
the standards for deciding whether to reach the merits in
a given case.” Brief for Nat. Assn. of Counties et al. as
Amici Curiae 29, 30. It does not appear that such a “cot
tage industry” developed prior to Saucier, and we see no
reason why our decision today should produce such a
result.
                             IV
  Turning to the conduct of the officers here, we hold that
petitioners are entitled to qualified immunity because the
entry did not violate clearly established law. An officer
conducting a search is entitled to qualified immunity
where clearly established law does not show that the
search violated the Fourth Amendment. See Anderson,
483 U. S., at 641. This inquiry turns on the “objective
legal reasonableness of the action, assessed in light of the
                  Cite as: 555 U. S. ____ (2009)           19

                      Opinion of the Court

legal rules that were clearly established at the time it was
taken.” Wilson v. Layne, 526 U. S. 603, 614 (1999) (inter
nal quotation marks omitted); see Hope v. Pelzer, 536 U. S.
730, 739 (2002) (“[Q]ualified immunity operates to ensure
that before they are subjected to suit, officers are on notice
their conduct is unlawful” (internal quotation marks
omitted)).
   When the entry at issue here occurred in 2002, the
“consent-once-removed” doctrine had gained acceptance in
the lower courts. This doctrine had been considered by
three Federal Courts of Appeals and two State Supreme
Courts starting in the early 1980’s. See, e.g., United
States v. Diaz, 814 F. 2d 454, 459 (CA7), cert. denied, 484
U. S. 857 (1987); United States v. Bramble, 103 F. 3d 1475
(CA9 1996); United States v. Pollard, 215 F. 3d 643, 648–
649 (CA6), cert. denied, 531 U. S. 999 (2000); State v.
Henry, 133 N. J. 104, 627 A. 2d 125 (1993); State v. Johns
ton, 184 Wis. 2d 794, 518 N. W. 2d 759 (1994). It had been
accepted by every one of those courts. Moreover, the
Seventh Circuit had approved the doctrine’s application to
cases involving consensual entries by private citizens
acting as confidential informants. See United States v.
Paul, 808 F. 2d, 645, 648 (1986). The Sixth Circuit
reached the same conclusion after the events that gave
rise to respondent’s suit, see United States v. Yoon, 398
F. 3d 802, 806–808, cert. denied, 546 U. S. 977 (2005), and
prior to the Tenth Circuit’s decision in the present case, no
court of appeals had issued a contrary decision.
   The officers here were entitled to rely on these cases,
even though their own Federal Circuit had not yet ruled
on “consent-once-removed” entries. The principles of
qualified immunity shield an officer from personal liability
when an officer reasonably believes that his or her conduct
complies with the law. Police officers are entitled to rely
on existing lower court cases without facing personal
liability for their actions. In Wilson, we explained that a
20                 PEARSON v. CALLAHAN

                      Opinion of the Court

Circuit split on the relevant issue had developed after the
events that gave rise to suit and concluded that “[i]f judges
thus disagree on a constitutional question, it is unfair to
subject police to money damages for picking the losing side
of the controversy.” 526 U. S., at 618. Likewise, here,
where the divergence of views on the consent-once
removed doctrine was created by the decision of the Court
of Appeals in this case, it is improper to subject petitioners
to money damages for their conduct.
   Because the unlawfulness of the officers’ conduct in this
case was not clearly established, petitioners are entitled to
qualified immunity. We therefore reverse the judgment of
the Court of Appeals.
                                              It is so ordered.

```

---

## GROUP: _overhaul2/lake/cases/Pembaur v. City of Cincinnati.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Pembaur v. City of Cincinnati"
type: case
citation: "475 U.S. 469 (1986)"
parallel_cite: "106 S. Ct. 1292; 89 L. Ed. 2d 452; 54 U.S.L.W. 4289"
neutral_cite: 1986 U.S. LEXIS 33
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1986
date_decided: 1986-03-25
docket: 84-1160
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1986-03-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Pembaur v. City of Cincinnati
  varies_by_point: false
  scope_note: "Plurality on the single-decision point; the rule that a final policymaker's single decision can be municipal policy is settled law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111615/pembaur-v-city-of-cincinnati/"
  cluster_id: 111615
  opinion_id: 9430387
  identity_checked: true
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Monell v. Department of Social Services]]", "[[City of Canton v. Harris]]"]
aliases: []
tags: ["case", "section-1983", "municipal-liability", "policy-or-custom", "final-policymaker", "monell"]
holding: "A single decision by a municipal official with final policymaking authority for the relevant subject matter can be the 'official policy' that triggers Monell liability."
lake:
  record_id: Pembaur v. City of Cincinnati
  status: verified
  projected_at: 2026-07-06
---

# Pembaur v. City of Cincinnati

*475 U.S. 469 (1986)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Sheriff's deputies tried to serve capiases on two employees of Dr. Bernard Pembaur's medical clinic who had failed to appear before a grand jury. When Pembaur barred the deputies from entering, they telephoned the County Prosecutor, who instructed them to "go in and get" the witnesses. The deputies chopped down the door with an axe and entered. Pembaur sued the county and city under § 1983, claiming the warrantless entry was an official policy.

## Issue
Whether a municipality may be held liable under § 1983 for a single decision — here, the County Prosecutor's instruction to enter — made by an official with final authority to establish policy on that subject, even though the municipality had no pre-existing rule directing the conduct.

## Rule
Yes. *[[Monell v. Department of Social Services|Monell]]* liability does not require a rule applied in many cases; a single decision by an authorized policymaker is enough. "municipal liability under § 1983 attaches where — and only where — a deliberate choice to follow a course of action is made from among various alternatives by the official or officials responsible for establishing final policy with respect to the subject matter in question." — 475 U.S. at 483-484. ^pin-483

Liability attaches only when the decision is made by an official who possesses **final policymaking authority** for the area in question; whether an official has such authority is a question of state law.

## Application
The County Prosecutor was the official to whom the deputies were directed to turn for instruction, and on these facts he was treated as the final policymaker on how to execute the capiases. His specific direction to force entry was therefore a "deliberate choice" by a policymaking official, and the resulting entry was an act of official county policy — sufficient to support municipal liability for that single decision, without proof of any broader pattern or custom.

## Conclusion
Reversed and [[Reading and Citing Cases#on-remand|remanded]]. A municipality can be liable under § 1983 for a single act of an official with final policymaking authority for the relevant subject matter; the lower court erred in requiring a repeated practice or general policy.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Pembaur* elaborates the policy-or-custom requirement of [[Monell v. Department of Social Services]] by recognizing single-decision liability, and sits alongside the failure-to-train branch developed in [[City of Canton v. Harris]]. The "final policymaking authority" inquiry it framed remains the governing test (later refined in *City of St. Louis v. Praprotnik* and *McMillian v. Monroe County*).

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *Pembaur v. City of Cincinnati*, 475 U.S. 469 (1986) — https://www.courtlistener.com/opinion/111615/pembaur-v-city-of-cincinnati/ — pinpoint: 483-484.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "31baefddffd057b3", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Pembaur v. City of Cincinnati"}, "payload": {"all": [{"cite": "475 U.S. 469", "page": "469", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "475"}, {"cite": "106 S. Ct. 1292", "page": "1292", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "106"}, {"cite": "89 L. Ed. 2d 452", "page": "452", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "89"}, {"cite": "1986 U.S. LEXIS 33", "page": "33", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1986"}, {"cite": "54 U.S.L.W. 4289", "page": "4289", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "54"}], "display": "475 U.S. 469", "official": {"cite": "475 U.S. 469", "page": "469", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "475"}, "official_selection_present": true, "record_id": "Pembaur v. City of Cincinnati"}}
{"assertion_id": "823a5b1862ff7f75", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-483", "record_id": "Pembaur v. City of Cincinnati"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-483", "pinpoint_status": "slip-only", "quote": "the witnesses. The deputies chopped down the door with an axe and entered. Pembaur sued the county and city under § 1983, claiming the warrantless entry was an official policy. ## Issue Whether a municipality may be held liable under § 1983 for a single decision — here, the County Prosecutor's instruction to enter — made by an official with final authority to establish policy on that subject, even though the municipality had no pre-existing rule directing the conduct. ## Rule Yes. *Monell* liability does not require a rule applied in many cases; a single decision by an authorized policymaker is enough.", "quote_fidelity": "mismatch", "record_id": "Pembaur v. City of Cincinnati", "star_marker": null}}
{"assertion_id": "b92930afc7e7b420", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Pembaur v. City of Cincinnati"}, "payload": {"as_of_content": "1986-03-25", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Pembaur v. City of Cincinnati", "scope_note": "Plurality on the single-decision point; the rule that a final policymaker's single decision can be municipal policy is settled law.", "varies_by_point": false}}
```

### lake record — Pembaur v. City of Cincinnati

```json
{
  "schema_version": "s2.v1",
  "record_id": "Pembaur v. City of Cincinnati",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Pembaur v. City of Cincinnati",
    "case_name_short": "Pembaur",
    "case_name_full": "PEMBAUR v. CITY OF CINCINNATI Et Al.",
    "input_case_name": "Pembaur v. City of Cincinnati",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1986-03-25",
    "year": 1986,
    "docket": "84-1160",
    "cluster_id": 111615,
    "lead_opinion_id": 9430387,
    "sibling_ids": [
      111615,
      9430387,
      9430388,
      9430389,
      9430390,
      9430391
    ],
    "absolute_url": "/opinion/111615/pembaur-v-city-of-cincinnati/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "475 U.S. 469",
      "volume": "475",
      "reporter": "U.S.",
      "page": "469",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "106 S. Ct. 1292",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 2d 452",
        "volume": "89",
        "reporter": "L. Ed. 2d",
        "page": "452",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4289",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4289",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. LEXIS 33",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "33",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "475 U.S. 469",
        "volume": "475",
        "reporter": "U.S.",
        "page": "469",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 S. Ct. 1292",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 2d 452",
        "volume": "89",
        "reporter": "L. Ed. 2d",
        "page": "452",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. LEXIS 33",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "33",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4289",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4289",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "475 U.S. 469",
    "official_selection": {
      "court_class": "scotus",
      "selected": "475 U.S. 469",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-483",
      "page": null,
      "quote": "the witnesses. The deputies chopped down the door with an axe and entered. Pembaur sued the county and city under \u00a7 1983, claiming the warrantless entry was an official policy. ## Issue Whether a municipality may be held liable under \u00a7 1983 for a single decision \u2014 here, the County Prosecutor's instruction to enter \u2014 made by an official with final authority to establish policy on that subject, even though the municipality had no pre-existing rule directing the conduct. ## Rule Yes. *Monell* liability does not require a rule applied in many cases; a single decision by an authorized policymaker is enough.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1986-03-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Pembaur v. City of Cincinnati",
    "varies_by_point": false,
    "scope_note": "Plurality on the single-decision point; the rule that a final policymaker's single decision can be municipal policy is settled law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Baptiste v. Executive Office of Health & Human Services",
          "cluster_id": 4731494,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Harris County, Texas and Kevin Vailes v. Barbara Coats, Individually, as Personal Representative of the Estate of Jamail Amron, and as Heir to the Estate of Jamail Amron, And Ali Amron, Individually and as Heir to the Estate of Jamail Amron, Barbara Coats",
          "cluster_id": 4725124,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gregory Baldwin v. City of Estherville, Iowa",
          "cluster_id": 4629600,
          "cite": [
            "929 N.W.2d 691"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cherry Knoll, L.L.C. v. HDR Engineering, Incorpora",
          "cluster_id": 4612302,
          "cite": [
            "922 F.3d 309"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Keyon Harrison v. Curt Vanderkooi",
          "cluster_id": 4522518,
          "cite": [
            "918 N.W.2d 785",
            "502 Mich. 751"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Herbert Liverman v. City of Petersburg",
          "cluster_id": 4330488,
          "cite": [
            "844 F.3d 400",
            "41 I.E.R. Cas. (BNA) 1449",
            "2016 U.S. App. LEXIS 22282",
            "100 Empl. Prac. Dec. (CCH) 45,713",
            "2016 WL 7240179"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Causey v. the State",
          "cluster_id": 3148713,
          "cite": [
            "334 Ga. App. 170",
            "778 S.E.2d 800"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lloyd v. Birkman",
          "cluster_id": 7315423,
          "cite": [
            "127 F. Supp. 3d 725",
            "2015 U.S. Dist. LEXIS 117410",
            "2015 WL 5202687"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jonathon Castro v. County of Los Angeles",
          "cluster_id": 2826317,
          "cite": [
            "797 F.3d 654",
            "2015 U.S. App. LEXIS 14132",
            "2015 WL 4731366"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Salvato Ex Rel. Estate of Salvato v. Miley",
          "cluster_id": 2812003,
          "cite": [
            "790 F.3d 1286"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jonathon Castro v. County of Los Angeles",
          "cluster_id": 2798029,
          "cite": [
            "785 F.3d 336",
            "2015 U.S. App. LEXIS 7240",
            "2015 WL 1948146"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane1_negative"
      },
      {
        "citing_case": {
          "name": "City of Canton v. Harris",
          "cluster_id": 112209,
          "cite": [
            "103 L. Ed. 2d 412",
            "109 S. Ct. 1197",
            "489 U.S. 378",
            "1989 U.S. LEXIS 1200",
            "57 U.S.L.W. 4270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of the County Commissioners of Bryan County v. Brown",
          "cluster_id": 118104,
          "cite": [
            "137 L. Ed. 2d 626",
            "117 S. Ct. 1382",
            "520 U.S. 397",
            "1997 U.S. LEXIS 2793",
            "65 U.S.L.W. 4286",
            "10 Fla. L. Weekly Fed. S 405",
            "12 I.E.R. Cas. (BNA) 1217",
            "97 Cal. Daily Op. Serv. 3033",
            "97 Daily Journal DAR 5311"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of St. Louis v. Praprotnik",
          "cluster_id": 112017,
          "cite": [
            "99 L. Ed. 2d 107",
            "108 S. Ct. 915",
            "485 U.S. 112",
            "1988 U.S. LEXIS 1069"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Starr v. Baca",
          "cluster_id": 8441026,
          "cite": [
            "652 F.3d 1202",
            "2011 U.S. App. LEXIS 15283",
            "2011 WL 2988827"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. City of Harker Heights",
          "cluster_id": 112699,
          "cite": [
            "117 L. Ed. 2d 261",
            "112 S. Ct. 1061",
            "503 U.S. 115",
            "1992 U.S. LEXIS 1376"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lee v. City of Los Angeles",
          "cluster_id": 7092482,
          "cite": [
            "250 F.3d 668",
            "2001 WL 468408"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lee v. City Of Los Angeles",
          "cluster_id": 773312,
          "cite": [
            "250 F.3d 668",
            "2001 Cal. Daily Op. Serv. 3507",
            "2001 Daily Journal DAR 4351",
            "56 Fed. R. Serv. 698",
            "2001 U.S. App. LEXIS 8150"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jonathon Castro v. County of Los Angeles",
          "cluster_id": 4247081,
          "cite": [
            "833 F.3d 1060",
            "2016 U.S. App. LEXIS 14950",
            "2016 WL 4268955"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jett v. Dallas Independent School District",
          "cluster_id": 112313,
          "cite": [
            "105 L. Ed. 2d 598",
            "109 S. Ct. 2702",
            "491 U.S. 701",
            "1989 U.S. LEXIS 3130",
            "57 U.S.L.W. 4858",
            "50 Fair Empl. Prac. Cas. (BNA) 27",
            "50 Empl. Prac. Dec. (CCH) 39,070"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Murray",
          "cluster_id": 111728,
          "cite": [
            "91 L. Ed. 2d 434",
            "106 S. Ct. 2661",
            "477 U.S. 527",
            "1986 U.S. LEXIS 67",
            "54 U.S.L.W. 4833"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Piotrowski v. City of Houston",
          "cluster_id": 22972,
          "cite": [
            "237 F.3d 567",
            "2001 U.S. App. LEXIS 603",
            "2001 WL 6712"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Philomene Long, Surviving Spouse and Heir-At-Law of John Thomas Idlet, Deceased v. County of Los Angeles",
          "cluster_id": 793848,
          "cite": [
            "442 F.3d 1178",
            "2006 U.S. App. LEXIS 7552",
            "2006 WL 770615"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kneipp v. Tedder",
          "cluster_id": 726573,
          "cite": [
            "95 F.3d 1199",
            "159 A.L.R. Fed. 619",
            "1996 U.S. App. LEXIS 24401"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
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
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Grieveson v. Anderson",
          "cluster_id": 1443143,
          "cite": [
            "538 F.3d 763",
            "2008 WL 3823872"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lucas Burgess v. Gene Fischer",
          "cluster_id": 2641010,
          "cite": [
            "735 F.3d 462",
            "2013 WL 5873323",
            "2013 U.S. App. LEXIS 22279"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edwards v. City of Goldsboro",
          "cluster_id": 764384,
          "cite": [
            "178 F.3d 231",
            "15 I.E.R. Cas. (BNA) 333",
            "43 Fed. R. Serv. 3d 890",
            "1999 U.S. App. LEXIS 9088"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kathleen Hansen v. Ronald L. Black",
          "cluster_id": 529383,
          "cite": [
            "885 F.2d 642",
            "1989 U.S. App. LEXIS 13906",
            "1989 WL 106525"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cion Peralta v. T. Dillard",
          "cluster_id": 2655912,
          "cite": [
            "744 F.3d 1076",
            "2014 WL 878830",
            "2014 U.S. App. LEXIS 4226"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
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
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Trevino v. Gates",
          "cluster_id": 7040066,
          "cite": [
            "99 F.3d 911",
            "96 Daily Journal DAR 13300",
            "45 Fed. R. Serv. 1143",
            "96 Cal. Daily Op. Serv. 8007",
            "1996 U.S. App. LEXIS 28299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gibson v. County of Washoe, Nevada",
          "cluster_id": 777732,
          "cite": [
            "290 F.3d 1175",
            "2002 Cal. Daily Op. Serv. 4392",
            "2002 Daily Journal DAR 5649",
            "2002 U.S. App. LEXIS 9604"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Laurie Tsao v. Desert Palace, Inc.",
          "cluster_id": 810771,
          "cite": [
            "698 F.3d 1128",
            "2012 WL 5200336"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Edward Hoefling, Jr. v. City of Miami",
          "cluster_id": 3171918,
          "cite": [
            "811 F.3d 1271",
            "93 Fed. R. Serv. 3d 1022",
            "2016 U.S. App. LEXIS 1177",
            "2016 WL 285358"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McTernan v. City of York, Pa.",
          "cluster_id": 1192469,
          "cite": [
            "564 F.3d 636",
            "2009 U.S. App. LEXIS 8884",
            "2009 WL 1111097"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pembaur v. City of Cincinnati:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111615 OR 9430387 OR 9430388 OR 9430389 OR 9430390 OR 9430391) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDMwNDM4NDAwMDAwJnM9Mjc5ODAyOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111615+OR+9430387+OR+9430388+OR+9430389+OR+9430390+OR+9430391%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 11,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 12,
        "triage_snippet_classified": 188
      },
      "lane2_top_cited": {
        "query": "cites:(111615 OR 9430387 OR 9430388 OR 9430389 OR 9430390 OR 9430391)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03Mzcmcz00OTgwNTEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111615+OR+9430387+OR+9430388+OR+9430389+OR+9430390+OR+9430391%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111615 OR 9430387 OR 9430388 OR 9430389 OR 9430390 OR 9430391)",
        "reviewed": 43,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 43,
        "triage_read": 0,
        "triage_snippet_classified": 43
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111615 OR 9430387 OR 9430388 OR 9430389 OR 9430390 OR 9430391)",
    "indexed_citing_opinions": 2453,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111615,
        "count": 2209,
        "count_source": "search"
      },
      {
        "opinion_id": 9430387,
        "count": 260,
        "count_source": "search"
      },
      {
        "opinion_id": 9430388,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430389,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430390,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430391,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6111,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/pembaur-v-city-of-cincinnati.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5NDczODImcz0xMDA0OTcyMSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111615+OR+9430387+OR+9430388+OR+9430389+OR+9430390+OR+9430391%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111615,
        "cited_id": 105382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 108330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 108406,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 109387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 109476,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 109776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 110061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 110236,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 110553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 110754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 111112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 111219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 111355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 111441,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 111480,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 276331,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 343372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 370304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 373791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 381330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 382937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 415320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 429458,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 437247,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111615,
        "cited_id": 443017,
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
    "date_created": "2026-07-05T16:42:52Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:43:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:43:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:46:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:43:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Pembaur v. City of Cincinnati

```
<opinion type="majority">
<author id="b553-7">Justice Brennan</author>
<p id="AfU">delivered the opinion of the Court, except as to Part II-B.</p>
<p id="b553-8">In <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658</a></span> (1978), the Court concluded that municipal liability-under <span class="citation no-link">42 U. S. C. § 1983</span> is limited to deprivations of federally protected rights caused by action taken “pursuant to official municipal policy of some nature . . . .” <span class="citation no-link"><em>Id., </em>at 691</span>. The question presented is whether, and in what circumstances, a decision by municipal policymakers on a single occasion may satisfy this requirement.</p>
<p id="b553-9">I</p>
<p id="b553-10">Bertold Pembaur is a licensed Ohio physician and the sole proprietor of the Rockdale Medical Center, located in the city of Cincinnati in Hamilton County. Most of Pembaur’s patients are welfare recipients who rely on government assistance to pay for medical care. During the spring of 1977, Simon Leis, the Hamilton County Prosecutor, began investigating charges that Pembaur fraudulently had accepted payments from state welfare agencies for services not actually provided to patients. A grand jury was convened, and the case was assigned to Assistant Prosecutor William Whalen. <page-number citation-index="1" label="472">*472</page-number>In April, the grand jury charged Pembaur in a six-count indictment.</p>
<p id="b554-5">During the investigation, the grand jury issued subpoenas for the appearance of two of Pembaur’s employees. When these employees failed to appear as directed, the Prosecutor obtained capiases for their arrest and detention from the Court of Common Pleas of Hamilton County.<footnotemark>1</footnotemark></p>
<p id="b554-6">On May 19,1977, two Hamilton County Deputy Sheriffs attempted to serve the capiases at Pembaur’s clinic. Although the reception area is open to the public, the rest of the clinic may be entered only through a door next to the receptionist’s window. Upon arriving, the Deputy Sheriffs identified themselves to the receptionist and sought to pass through this door, which was apparently open. The receptionist blocked their way and asked them to wait for the doctor. When Pembaur appeared a moment later, he and the receptionist closed the door, which automatically locked from the inside, and wedged a piece of wood between it and the wall. Returning to the receptionist’s window, the Deputy Sheriffs identified themselves to Pembaur, showed him the capiases and explained why they were there. Pembaur refused to let them enter, claiming that the police had no legal authority to be there and requesting that they leave. He told them that he had called the Cincinnati police, the local media, and his lawyer. The Deputy Sheriffs decided not to take further action until the Cincinnati police arrived.</p>
<p id="b554-7">Shortly thereafter, several Cincinnati police officers appeared. The Deputy Sheriffs explained the situation to them and asked that they speak to Pembaur. The Cincinnati police told Pembaur that the papers were lawful and that he should allow the Deputy Sheriffs to enter. When Pembaur refused, the Cincinnati police called for a superior officer. When he too failed to persuade Pembaur to open the door, <page-number citation-index="1" label="473">*473</page-number>the Deputy Sheriffs decided to call their supervisor for further instructions. Their supervisor told them to call Assistant Prosecutor Whalen and to follow his instructions. The Deputy Sheriffs then telephoned Whalen and informed him of the situation. Whalen conferred with County Prosecutor Leis, who told Whalen to instruct the Deputy Sheriffs to "go in and get [the witnesses].” Whalen in turn passed these instructions along to the Deputy Sheriffs.</p>
<p id="b555-5">After a final attempt to persuade Pembaur voluntarily to allow them to enter, the Deputy Sheriffs tried unsuccessfully to force the door. City police officers, who had been advised of the County Prosecutor’s instructions to “go in and get” the witnesses, obtained an axe and chopped down the door. The Deputy Sheriffs then entered and searched the clinic. Two individuals who fit descriptions of the witnesses sought were detained, but turned out not to be the right persons.</p>
<p id="b555-6">After this incident, the Prosecutor obtained an additional indictment against Pembaur for obstructing police in the performance of an authorized act. Although acquitted of all other charges, Pembaur was convicted for this offense. The Ohio Court of Appeals reversed, reasoning that Pembaur was privileged under state law to exclude the deputies because the search of his office violated the Fourth Amendment. <em>State </em>v. <em>Pembaur, </em>No. C-790380 (Hamilton County Court of Appeals, Nov. 3, 1982). The Ohio Supreme Court reversed and reinstated the conviction. <em>State </em>v. <em>Pembaur, </em><span class="citation" data-id="6758271"><a href="/opinion/6867449/state-v-pembaur/" aria-description="Citation for case: State v. Pembaur">9 Ohio St. 3d 136</a></span>, <span class="citation" data-id="6758271"><a href="/opinion/6867449/state-v-pembaur/" aria-description="Citation for case: State v. Pembaur">459 N. E. 2d 217</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./467/1219/">467 U. S. 1219</a></span> (1984). The Supreme Court held that the state-law privilege applied only to bad-faith conduct by law enforcement officials, and that, under the circumstances of this case, Pembaur was obliged to acquiesce to the search and seek redress later in a civil action for damages. <span class="citation" data-id="6758271"><a href="/opinion/6867449/state-v-pembaur/#138" aria-description="Citation for case: State v. Pembaur">9 Ohio St. 3d, at 138</a></span>, <span class="citation" data-id="6758271"><a href="/opinion/6867449/state-v-pembaur/#219" aria-description="Citation for case: State v. Pembaur">459 N. E. 2d, at 219</a></span>.</p>
<p id="b555-7">On April 20, 1981, Pembaur filed the present action in the United States District Court for the Southern District of Ohio against the city of Cincinnati, the County of Hamilton, <page-number citation-index="1" label="474">*474</page-number>the Cincinnati Police Chief, the Hamilton County Sheriff, the members of the Hamilton Board of County Commissioners (in their official capacities only), Assistant Prosecutor Whalen, and nine city and county police officers.<footnotemark>2</footnotemark> Pembaur sought damages under <span class="citation no-link">42 U. S. C. § 1983</span>, alleging that the county and city police had violated his rights under the Fourth and Fourteenth Amendments. His theory was that, absent exigent circumstances, the Fourth Amendment prohibits police from searching an individual’s home or business without a search warrant even to execute an arrest warrant for a third person. We agreed with that proposition in <em>Steagald </em>v. <em>United States, </em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">451 U. S. 204</a></span> (1981), decided the day after Pembaur filed this lawsuit. Pembaur sought $10 million in actual and $10 million in punitive damages, plus costs and attorney’s fees.</p>
<p id="b556-4">Much of the testimony at the 4-day trial concerned the practices of the Hamilton County Police in serving capiases. Frank Webb, one of the Deputy Sheriffs present at the clinic on May 19, testified that he had previously served capiases on the property of third persons without a search warrant, but had never been required to use force to gain access. Assistant Prosecutor Whalen was also unaware of a prior instance in which police had been denied access to a third person’s property in serving a capias and had used force to gain entry. Lincoln Stokes, the County Sheriff, testified that the Department had no written policy respecting the serving of capiases on the property of third persons and that the proper response in any given situation would depend upon the circumstances. He too could not recall a specific instance in <page-number citation-index="1" label="475">*475</page-number>which entrance had been denied and forcibly gained. Sheriff Stokes did testify, however, that it was the practice in his Department to refer questions to the County Prosecutor for instructions under appropriate circumstances and that “it was the proper thing to do” in this case.</p>
<p id="b557-5">The District Court awarded judgment to the defendants and dismissed the complaint in its entirety. The court agreed that the entry and search of Pembaur’s clinic violated the Fourth Amendment under <em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">Steagald, supra,</a></span> </em>but held <em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">Steagald</a></span> </em>inapplicable since it was decided nearly four years after the incident occurred. Because it construed the law in the Sixth Circuit in 1977 to permit law enforcement officials to enter the premises of a third person to serve a capias, the District Court held that the individual municipal officials were all immune under <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800</a></span> (1982).</p>
<p id="b557-6">The claims against the county and the city were dismissed on the ground that the individual officers were not acting pursuant to the kind of “official policy” that is the predicate for municipal liability under <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span>. </em>With respect to Hamilton County, the court explained that, even assuming that the entry and search were pursuant to a governmental policy, “it was not a policy of Hamilton County <em>per se” </em>because “[t]he Hamilton County Board of County Commissioners, acting on behalf of the county, simply does not establish or control the policies of the Hamilton County Sheriff.” With respect to the city of Cincinnati, the court found that “the only policy or custom followed . . . was that of aiding County Sheriff’s Deputies in the performance of their duties.” The court found that any participation by city police in the entry and search of The clinic resulted from decisions by individual officers as to the permissible scope of assistance they could provide, and not from a city policy to provide this particular kind of assistance.</p>
<p id="b557-7">On appeal, Pembaur challenged only the dismissal of his claims against Whalen, Hamilton County, and the city of Cin<page-number citation-index="1" label="476">*476</page-number>cinnati. The Court of Appeals for the Sixth Circuit upheld the dismissal of Pembaur’s claims against Whalen and Hamilton County, but reversed the dismissal of his claim against the city of Cincinnati on the ground that the District Court’s findings concerning the policies followed by the Cincinnati police were clearly erroneous. <span class="citation multiple-matches"><a href="/c/F.%202d/746/337/">746 F. 2d 337</a></span> (1984).<footnotemark>3</footnotemark></p>
<p id="b558-5">The Court of Appeals affirmed the District Court’s dismissal of Pembaur’s claim against Hamilton County, but on different grounds. The court held that the County Board’s lack of control over the Sheriff would not preclude county liability if “the nature and duties of the Sheriff are such that his acts may fairly be said to represent the county’s official policy with respect to the specific subject matter.” <em>Id., </em>at 340-341. Based upon its examination of Ohio law, the Court of Appeals found it “clea[r]” that the Sheriff and the Prosecutor were both county officials authorized to establish “the official policy of Hamilton County” with respect to matters of law enforcement. <em>Id., </em>at 341. Notwithstanding these conclusions, however, the court found that Pembaur’s claim against the county had been properly dismissed:</p>
<blockquote id="b558-6">“We believe that Pembaur failed to prove the existence of a county policy in this case. Pembaur claims that the deputy sheriffs acted pursuant to the policies of the Sheriff and Prosecutor by forcing entry into the medical center. Pembaur has failed to establish, however, anything more than that, on this <em>one occasion, </em>the Prosecutor and the Sheriff decided to force entry into his office. . . . That single, discrete decision is insufficient, <page-number citation-index="1" label="477">*477</page-number>by itself, to establish that the Prosecutor, the Sheriff, or both were implementing a governmental policy.” <em>Ibid. </em>(footnote omitted) (emphasis in original).</blockquote>
<p id="Anh">Pembaur petitioned for certiorari to review only the dismissal of his claim against Hamilton County. The decision of the Court of Appeals conflicts with holdings in several other Courts of Appeals,<footnotemark>4</footnotemark> and we granted the petition to resolve the conflict. <span class="citation multiple-matches"><a href="/c/U.%20S./472/1016/">472 U. S. 1016</a></span> (1985). We reverse.</p>
<p id="Afh">h-i t — I</p>
<p id="ASX7">A</p>
<p id="AB7">Our analysis must begin with the proposition that “Congress did not intend municipalities to be held liable unless action pursuant to official municipal policy of some nature caused a constitutional tort.” <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#691" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 691</a></span>.<footnotemark>5</footnotemark> As we read its opinion, the Court of Appeals held that a single decision to <page-number citation-index="1" label="478">*478</page-number>take particular action, although made by municipal policymakers, cannot establish the kind of “official policy” required by <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>as a predicate to municipal liability under § 1983.<footnotemark>6</footnotemark> The Court of Appeals reached this conclusion without referring to <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>— indeed, without any explanation at all. However, examination of the opinion in <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>clearly demonstrates that the Court of Appeals misinterpreted its holding.</p>
<p id="b560-5"><em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>is a case about responsibility. In the first part of the opinion, we held that local government units could be made liable under § 1983 for deprivations of federal rights, overruling a contrary holding in <em>Monroe </em>v. <em>Pape, </em><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167</a></span> (1961). In the second part of the opinion, we recognized a limitation on this liability and concluded that a municipality cannot be made liable by application of the doctrine of <em>respondeat superior. </em>See <em>Monell, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#691" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 691</a></span>. In part, this conclusion rested upon the language of §1983, which imposes liability only on a person who “subjects, or causes to be subjected,” any individual to a deprivation of federal rights; we noted that this language “cannot easily be read to impose liability vicariously on government bodies solely on the basis of the existence of an employer-employee relationship -with a tortfeasor.” <em>Id., </em>at 692. Primarily, <page-number citation-index="1" label="479">*479</page-number>however, our conclusion rested upon the legislative history, which disclosed that, while Congress never questioned its power to impose civil liability on municipalities for their <em>own </em>illegal acts, Congress did doubt its constitutional power to impose such liability in order to oblige municipalities to control the conduct of <em>others. Id., </em>at 665-683.<footnotemark>7</footnotemark> We found that, because of these doubts, Congress chose not to create such obligations in § 1983. Recognizing that this would be the effect of a federal law of <em>respondeat superior, </em>we concluded that § 1983 could not be interpreted to incorporate doctrines of vicarious liability. <em>Id., </em>at 692-694, and n. 57.</p>
<p id="b561-5">The conclusion that tortious conduct, to be the basis for municipal liability under §1983, must be pursuant to a municipality’s “official policy” is contained in this discussion. The “official policy” requirement was intended to distinguish acts of the <em>municipality </em>from acts of <em>employees </em>of the municipality, and thereby make clear that municipal liability is limited to action for which the municipality is actually responsi<page-number citation-index="1" label="480">*480</page-number>ble.<footnotemark>8</footnotemark> <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>reasoned that recovery from a municipality is limited to acts that are, properly speaking, acts “of the municipality” — that is, acts which the municipality has officially sanctioned or ordered.</p>
<p id="b562-5">With this understanding, it is plain that municipal liability may be imposed for a single decision by municipal policymakers under appropriate circumstances. No one has ever doubted, for instance, that a municipality may be liable under § 1983 for a single decision by its properly constituted legislative body — whether or not that body had taken similar action in the past or intended to do so in the future — because even a single decision by such a body unquestionably constitutes an act of official government policy. See, <em>e. g., Owen </em>v. <em>City of Independence, </em><span class="citation" data-id="9427858"><a href="/opinion/110236/owen-v-city-of-independence/" aria-description="Citation for case: Owen v. City of Independence">445 U. S. 622</a></span> (1980) (City Council passed resolution firing plaintiff without a pretermination hearing); <em>Newport </em>v. <em>Fact Concerts, Inc., </em><span class="citation" data-id="9428471"><a href="/opinion/110553/city-of-newport-v-fact-concerts-inc/" aria-description="Citation for case: City of Newport v. Fact Concerts, Inc.">453 U. S. 247</a></span> (1981) (City Council canceled license permitting concert because of dispute over content of performance). But the power to establish policy is no more the exclusive province of the legislature at the local level than at the state or national level. Monell’s language makes clear that it expressly envisioned other officials “whose acts or edicts may fairly be said to represent official policy,” <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs."><em>Monell, supra, </em>at 694</a></span>, and whose decisions therefore may give rise to municipal liability under § 1983.</p>
<p id="b562-6">Indeed, any other conclusion would be inconsistent with the principles underlying § 1983. To be sure, “official policy” often refers to formal rules or understandings — often but not always committed to writing — that are intended to, and do, establish fixed plans of action to be followed under similar cir<page-number citation-index="1" label="481">*481</page-number>cumstances consistently and over time. That was the case in <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>itself, which involved a written rule requiring pregnant employees to take unpaid leaves of absence before such leaves were medically necessary. However, as in <em>Owen </em>and <em><span class="citation" data-id="9428471"><a href="/opinion/110553/city-of-newport-v-fact-concerts-inc/" aria-description="Citation for case: City of Newport v. Fact Concerts, Inc.">Newport</a></span>, </em>a government frequently chooses a course of action tailored to a particular situation and not intended to control decisions in later situations. If the decision to adopt that particular course of action is properly made by that government’s authorized decisionmakers, it surely represents an act of official government “policy” as that term is commonly understood.<footnotemark>9</footnotemark> More importantly, where action is directed by those who establish governmental policy, the municipality is equally responsible whether that action is to be taken only once or to be taken repeatedly. To deny compensation to the victim would therefore be contrary to the fundamental purpose of § 1983.</p>
<p id="b563-5">B</p>
<p id="b563-6">Having said this much, we hasten to emphasize that not every decision by municipal officers automatically subjects the municipality to §1983 liability. Municipal liability attaches only where the decisionmaker possesses final authority to establish municipal policy with respect to the action ordered.<footnotemark>10</footnotemark> The fact that a particular official — even a policy-<page-number citation-index="1" label="482">*482</page-number>making official — has discretion in the exercise of particular functions does not, without more, give rise to municipal liability based on an exercise of that discretion. See, <em>e. g., Oklahoma City </em>v. <em>Tuttle, </em>471 U. S., at 822-824.<footnotemark>11</footnotemark> The offi<page-number citation-index="1" label="483">*483</page-number>cial must also be responsible for establishing final government policy respecting such activity before the municipality can be held liable.<footnotemark>12</footnotemark> Authority to make municipal policy may be granted directly by a legislative enactment or may be delegated by an official who possesses such authority, and of course, whether an official had final policymaking authority is a question of state law. However, like other governmental entities, municipalities often spread policymaking authority among various officers and official bodies. As a result, particular officers may have authority to establish binding county policy respecting particular matters and to adjust that policy for the county in changing circumstances. To hold a municipality liable for actions ordered by such officers exercising their policymaking authority is no more an application of the theory of <em>respondeat superior </em>than was holding the municipalities liable for the decisions of the City Councils in <em>Owen </em>and <em><span class="citation" data-id="9428471"><a href="/opinion/110553/city-of-newport-v-fact-concerts-inc/" aria-description="Citation for case: City of Newport v. Fact Concerts, Inc.">Newport</a></span>. </em>In each case municipal liability attached to a single decision to take unlawful action made by municipal policymakers. We hold that municipal liability under §1983 attaches where — and only where — a deliberate choice to follow a course of action is made from among various alternatives by the official or officials responsible for establishing final policy with respect to the subject matter in ques<page-number citation-index="1" label="484">*484</page-number>tion. See <em>Tuttle, supra, </em>at 823 (“‘policy’ generally implies a course of action consciously chosen from among various alternatives”).</p>
<p id="b566-5">C</p>
<p id="b566-6">Applying this standard to the case before us, we have little difficulty concluding that the Court of Appeals erred in dismissing petitioner’s claim against the county. The Deputy Sheriffs who attempted to serve the capiases at petitioner’s clinic found themselves in a difficult situation. Unsure of the proper course of action to follow, they sought instructions from their supervisors. The instructions they received were to follow the orders of the County Prosecutor. The Prosecutor made a considered decision based on his understanding of the law and commanded the officers forcibly to enter petitioner’s clinic. That decision directly caused the violation of petitioner’s Fourth Amendment rights.</p>
<p id="b566-7">Respondent argues that the County Prosecutor lacked authority to establish municipal policy respecting law enforcement practices because only the County Sheriff may establish policy respecting such practices. Respondent suggests that the County Prosecutor was merely rendering “legal advice” when he ordered the Deputy Sheriffs to “go in and get” the witnesses. Consequently, the argument concludes, the action of the individual Deputy Sheriffs in following this advice and forcibly entering petitioner’s clinic was not pursuant to a properly established municipal policy.</p>
<p id="b566-8">We might be inclined to agree with respondent if we thought that the Prosecutor had only rendered “legal advice.” However, the Court of Appeals concluded, based upon its examination of Ohio law, that both the County Sheriff and the County Prosecutor could establish county policy under appropriate circumstances, a conclusion that we do not question here.<footnotemark>13</footnotemark> <span class="citation no-link">Ohio Rev. Code Ann. § 309.09</span>(A) (1979) <page-number citation-index="1" label="485">*485</page-number>provides that county officers may “require . . . instructions from [the County Prosecutor] in matters connected with their official duties.” Pursuant to standard office procedure, the Sheriff’s Office referred this matter to the Prosecutor and then followed his instructions. The Sheriff testified that his Department followed this practice under appropriate circumstances and that it was “the proper thing to do” in this case. We decline to accept respondent’s invitation to overlook this delegation of authority by disingenuously labeling the Prosecutor’s clear command mere “legal advice.” In ordering the Deputy Sheriffs to enter petitioner’s clinic the County Prosecutor was acting as the final decisionmaker for the county, and the county may therefore be held liable under § 1983.</p>
<p id="b567-5">The decision of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b567-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b554-8"> A capias is a writ of attachment commanding a county official to bring a subpoenaed witness who has failed to appear before the court to testify and to answer for civil contempt. See <span class="citation no-link">Ohio Rev. Code Ann. § 2317.21</span> (1981).</p>
</footnote>
<footnote label="2">
<p id="b556-5"> Hamilton County Prosecutor Leis was not made a defendant because counsel for petitioner believed that Leis was absolutely immune. Tr., Mar. 14-Mar. 17, p. 267. We express no view as to the correctness of this evaluation. Cf. <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#430" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409, 430-431</a></span> (1976) (leaving open the question of a prosecutor’s immunity when he acts “in the role of an administrator or investigative officer rather than that of an advocate”).</p>
</footnote>
<footnote label="3">
<p id="b558-7"> The court found that there was a city policy respecting the use of force in serving capiases as well as a policy of aiding county police. It based this conclusion on the testimony of Cincinnati Chief of Police Myron Leistler, who stated that it was the policy of his Department to take whatever steps were necessary, including the forcing of doors, to serve an arrest document. 746 F. 2d, at 341-342; see also, Tr., Mar. 14-Mar. 17, pp. 43-45, 46-47. The court remanded the case for a determination whether Pembaur’s injury was incurred as a result of the execution of this policy. 746 F. 2d, at 342.</p>
</footnote>
<footnote label="4">
<p id="A7f"> See, <em>e. g., McKinley </em>v. <em>City of Eloy, </em><span class="citation" data-id="8916800"><a href="/opinion/8927003/mckinley-v-city-of-eloy/#1116" aria-description="Citation for case: McKinley v. City of Eloy">705 F. 2d 1110, 1116-1117</a></span> (CA9 1983); <em>Berdin </em>v. <em>Duggan, </em><span class="citation" data-id="415320"><a href="/opinion/415320/thomas-berdin-cross-appellants-v-john-duggan-cross-appellees/#913" aria-description="Citation for case: Thomas Berdin, Cross-Appellants v. John Duggan,...">701 F. 2d 909, 913-914</a></span> (CA11), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./464/893/">464 U. S. 893</a></span> (1983); <em>Van Ooteghem </em>v. <em>Gray, </em><span class="citation" data-id="8911969"><a href="/opinion/8922923/van-ooteghem-v-gray/#494" aria-description="Citation for case: Van Ooteghem v. Gray">628 F. 2d 488, 494-495</a></span> (CA5 1980), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./455/909/">455 U. S. 909</a></span> (1982); <em>Quinn </em>v. <em>Syracuse Model Neighborhood Corp., </em><span class="citation" data-id="8910812"><a href="/opinion/8921905/quinn-v-syracuse-model-neighborhood-corp/#448" aria-description="Citation for case: Quinn v. Syracuse Model Neighborhood Corp.">613 F. 2d 438, 448</a></span> (CA2 1980). See also <em>Sanders </em>v. <em>St. Louis County, 724 </em>F. 2d 665, 668 (CA8 1983) <em>(per curiam) </em>(“It may be that one act of a senior county official is enough to establish the liability of the county, if that official was in a position to establish policy and if that official himself directly violated another’s constitutional rights”). But see <em>Losch </em>v. <em>Borough of Parkesburg, Pa., </em><span class="citation" data-id="437247"><a href="/opinion/437247/frank-a-losch-v-borough-of-parkesburg-pennsylvania-lester-j-thomas/#910" aria-description="Citation for case: Frank A. Losch v. Borough of Parkesburg, Pennsylvania...">736 F. 2d 903, 910-911</a></span> (CA3 1984) (“[E]ven if [the Police Chief] were the final authority with regard to police activities, . . . there is no regulation or evidence of any repeated action by [the chief]. . . that can transmute his actions in the Losch incident into a general Borough policy”).</p>
</footnote>
<footnote label="5">
<p id="AFGz"> There is no question in this case that petitioner suffered a constitutional deprivation. The Court of Appeals found, and respondent concedes, that the entry and search of petitioner’s clinic violated the Fourth Amendment under <em>Steagald </em>v. <em>United States, </em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">451 U. S. 204</a></span> (1981). See 746 F. 2d, at 340, n. 1; Brief for Respondents 11. Respondent never challenged and has in fact also conceded that <em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">Steagald</a></span> </em>applies retroactively to this case. See Tr. of Oral Arg. 26-27. We decide this case in light of respondent’s concessions.</p>
</footnote>
<footnote label="6">
<p id="b560-6"> The opinion below also can be read as holding that municipal liability cannot be imposed for a single incident of unconstitutional <em>conduct </em>by municipal employees whether or not that conduct is pursuant to municipal <em>policy. </em>Such a conclusion is unsupported by either the language or reasoning of <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span>, </em>or by any of our subsequent decisions. As we explained last Term in <em>Oklahoma City </em>v. <em>Tuttle, </em><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S. 808</a></span> (1985), once a municipal policy is established, “it requires only one application ... to satisfy fully Monell’s requirement that a municipal corporation be held liable only for constitutional violations resulting from the municipality’s official policy.” <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#822" aria-description="Citation for case: City of Oklahoma v. Tuttle"><em>Id., </em>at 822</a></span> (plurality opinion); see also, <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#831" aria-description="Citation for case: City of Oklahoma v. Tuttle"><em>id., </em>at 831-832</a></span> (Brennan, J., concurring in part and concurring in judgment.). The only issue before us, then, is whether petitioner satisfied Monell’s requirement that the tor-tious conduct be pursuant to “official municipal policy.”</p>
</footnote>
<footnote label="7">
<p id="b561-6"> This legislative history is discussed at length in <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>and need only be summarized here. The distinction between imposing liability on municipalities for their own violations and imposing liability to force municipalities to prevent violations by others was made by Members of the House of Representatives who successfully opposed the “Sherman amendment” to the Civil Rights Act of 1871, <span class="citation no-link">17 Stat. 13</span>, the precursor of § 1983. The Sherman amendment sought to impose civil liability on municipalities for damage done to the person or property of its inhabitants by private persons “riotously and tumultuously assembled.” Cong. Globe, 42d Cong., 1st Sess., 749 (1871) (quoted in <em>Monell, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#664" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 664</a></span>). Opponents of the amendment argued that, in effect, it imposed an obligation on local governments to keep the peace, and that the Federal Government could not constitutionally require local governments to keep the peace if state law did not. This argument succeeded in blocking passage of the amendment. However, even the opponents of the Sherman amendment recognized Congress’ power to impose civil liability on a local government already obligated to keep the peace by state law if that government failed to do so and thereby violated the Fourteenth Amendment. See <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#665" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs."><em>id., </em>at 665-683</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b562-7"> Thus, our statement of the conclusion juxtaposes the policy requirement with imposing liability on the basis of <em>respondeat superior:</em></p>
<blockquote id="b562-8">“We conclude, therefore, that a local government may not be sued under § 1983 for an injury inflicted solely by its employees or agents. Instead, it is when execution of a government’s policy. . . , whether made by its lawmakers or by those whose edicts or acts may fairly be said to represent official policy, inflicts the injury that the government as an entity is responsible under § 1983.” <em>Id., </em>at 694.</blockquote>
</footnote>
<footnote label="9">
<p id="b563-7"> While the dictionary is not the source definitively to resolve legal questions, we note that this description of “policy” is consistent with the word’s ordinary definition. For example, Webster’s defines the word as “a specific decision or set of decisions designed to carry out such a chosen course of action.” Webster’s Third New International Dictionary 1754 (1981). Similarly, the Oxford English Dictionary defines “policy” as “[a] course of action adopted and pursued by a government, party, ruler, statesman, etc.; any course of action adopted as advantageous or expedient.” VII Oxford English Dictionary 1071 (1933). See also, Webster’s New Twentieth Century Dictionary 1392 (2d ed. 1979) (“any governing principle, plan, or course of action”); Random House Dictionary 1113 (1966) (“a course of action adopted and pursued by a government, ruler, political party, etc.”).</p>
</footnote>
<footnote label="10">
<p id="b563-8"> Section 1983 also refers to deprivations under color of a state “custom or usage,” and the Court in <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>noted accordingly that “local govern<page-number citation-index="1" label="482">*482</page-number>ments, like every other § 1983 ‘person,’. . . may be sued for constitutional deprivations visited pursuant to governmental ‘custom’ even though such a custom has not received formal approval through the body’s official deci-sionmaking channels.” <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#690" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 690-691</a></span>. A § 1983 plaintiff thus may be able to recover from a municipality without adducing evidence of an affirmative decision by policymakers if able to prove that the challenged action was pursuant to a state “custom or usage.” Because there is no allegation that the action challenged here was pursuant to a local “custom,” this aspect of <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>is not at issue in this case.</p>
</footnote>
<footnote label="11">
<p id="b564-6"> Respondent argues that the holding in <em><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">Tuttle</a></span> </em>is far broader than this. It relies on the statement near the end of Justice Rehnquist’s plurality opinion that “[p]roof of a single incident of unconstitutional activity is not sufficient to impose liability under <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>unless proof of the incident includes proof that it was caused by an <em>existing, </em>unconstitutional municipal policy, which policy can be attributed to a municipal policymaker.” <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#823" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S., at 823-824</a></span> (emphasis added). Respondent contends that a policy cannot be said to be “existing” unless similar action has been taken in the past.</p>
<p id="b564-7">This reading of the <em><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">Tuttle</a></span> </em>plurality is strained, and places far too much weight on a single word. The plaintiff in <em><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">Tuttle</a></span> </em>alleged that a police officer’s use of excessive force deprived her decedent of life without due process of law. The plaintiff proved only a single instance of unconstitutional action by a nonpolieymaking employee of the city. She argued that the city had “caused” the constitutional deprivation by adopting a “policy” of inadequate training. The trial judge instructed the jury that a single, unusually excessive use of force may warrant an inference that it was attributable to grossly inadequate training, and that the municipality could be held liable on this basis. We reversed the judgment against the city. Although there was no opinion for the Court on this question, both the plurality and the opinion concurring in the judgment found plaintiff’s submission inadequate because she failed to establish that the unconstitutional act was taken <em>pursuant to </em>a municipal policy rather than simply resulting from such a policy in a “but for” sense. <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#822" aria-description="Citation for case: City of Oklahoma v. Tuttle"><em>Id., </em>at 822-824</a></span> (plurality opinion), 829-830 (Brennan, J., concurring in part and concurring in judgment). That conclusion is entirely consistent with our holding today that the policy which ordered or authorized an unconstitutional act can be established by a single decision by proper municipal policymakers.'</p>
</footnote>
<footnote label="12">
<p id="b565-5"> Thus, for example, the County Sheriff may have discretion to hire and fire employees without also being the county official responsible for establishing county employment policy. If this were the case, the Sheriff’s decisions respecting employment would not give rise to municipal liability, although similar decisions with respect to law enforcement practices, over which the Sheriff <em>is </em>the official policymaker, <em>would </em>give rise to municipal liability. Instead, if county employment policy was set by the Board of County Commissioners, only that body’s decisions would provide a basis for county liability. This would be true even if the Board left the Sheriff discretion to hire and fire employees and the Sheriff exercised that discretion in an unconstitutional manner; the decision to act unlawfully would not be a decision of the Board. However, if the Board delegated its power to establish final employment policy to the Sheriff, the Sheriff’s decisions <em>would </em>represent county policy and could give rise to municipal liability.</p>
</footnote>
<footnote label="13">
<p id="b566-9"> We generally accord great deference to the interpretation and application of state law by the courts of appeals. <em>United States </em>v. <em>S.A. Empresa de Viacao Aerea Rio Grandense, </em><span class="citation" data-id="111219"><a href="/opinion/111219/united-states-v-sa-empresa-de-viacao-aerea-rio-grandense/#815" aria-description="Citation for case: United States v. S.A. Empresa De Viacao Aerea Rio Grandense">467 U. S. 797, 815, n. 12</a></span> (1984); <em>Brockett </em><page-number citation-index="1" label="485">*485</page-number>v. <em>Spokane Arcades, Inc., </em><span class="citation" data-id="9430103"><a href="/opinion/111480/brockett-v-spokane-arcades-inc/#499" aria-description="Citation for case: Brockett v. Spokane Arcades, Inc.">472 U. S. 491, 499-500</a></span> (1985) (citing cases); see also <em>Bishop </em>v. <em>Wood, </em><span class="citation" data-id="9426440"><a href="/opinion/109476/bishop-v-wood/#345" aria-description="Citation for case: Bishop v. Wood">426 U. S. 341, 345-347</a></span> (1976).</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Pennsylvania v. Bruder.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Pennsylvania v. Bruder"
type: case
citation: "488 U.S. 9 (1988)"
parallel_cite: "109 S. Ct. 205; 102 L. Ed. 2d 172"
neutral_cite: 1988 U.S. LEXIS 4816
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1988
date_decided: 1988-10-31
docket: 88-161
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1988-10-31
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Pennsylvania v. Bruder
  varies_by_point: false
  scope_note: "Good law; per curiam application of Berkemer v. McCarty — ordinary traffic stops are non-custodial, so roadside DUI questioning needs no Miranda warnings before arrest."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112152/pennsylvania-v-bruder/"
  cluster_id: 112152
  opinion_id: 112152
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Related (custody)"
related: ["[[Berkemer v. McCarty]]", "[[Miranda v. Arizona]]", "[[California v. Beheler]]", "[[Oregon v. Mathiason]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "custody", "traffic-stop", "dui", "per-curiam"]
holding: "Ordinary roadside questioning of a motorist detained during a routine traffic stop — including DUI field-sobriety questioning before arrest — is not custodial interrogation, so Miranda warnings are not required and the roadside responses are admissible (applying Berkemer v. McCarty)."
lake:
  record_id: Pennsylvania v. Bruder
  status: verified
  projected_at: 2026-07-06
---

# Pennsylvania v. Bruder

*488 U.S. 9 (1988)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officer Shallis observed Bruder driving erratically and running a red light, and stopped him. Smelling alcohol and seeing Bruder's stumbling movements, the officer administered field sobriety tests and asked whether he had been drinking; Bruder admitted he had and recited the alphabet. He was then arrested for driving under the influence. The Pennsylvania Superior Court held that his roadside statements were the product of un-warned custodial interrogation and suppressed them for lack of [[Miranda and Custodial Interrogation|Miranda warnings]].

## Issue
Whether roadside questioning of a motorist during an ordinary traffic stop — here, DUI sobriety questioning before arrest — is custodial interrogation requiring [[Miranda and Custodial Interrogation|Miranda warnings]].

## Rule
No. The decision was "contrary to [[Berkemer v. McCarty]]," which held that the "'noncoercive aspect of ordinary traffic stops prompts us to hold that persons temporarily detained pursuant to such stops are not "in custody" for the purposes of *Miranda*.'" — 488 U.S. at 10 (quoting *Berkemer*, 468 U.S. 420, 440 (1984)). Because such a motorist's freedom is not curtailed "to a degree associated with formal arrest," "he was not entitled to a recitation of his constitutional rights prior to arrest, and his roadside responses to questioning were admissible." — *Id.* ^pin-10

"*Berkemer*'s rule, that ordinary traffic stops do not involve custody for purposes of *Miranda*, governs this case." — *Id.* at 11. ^pin-11

## Application
The uncontested facts showed "the same noncoercive aspects as the *Berkemer* detention: 'a single police officer ask[ing] respondent a modest number of questions and request[ing] him to perform a simple balancing test at a location visible to passing motorists.'" Because the stop was the ordinary, brief, public sort that *[[Berkemer v. McCarty|Berkemer]]* deemed non-custodial, Bruder was not "in custody" during the roadside questioning and no [[Miranda and Custodial Interrogation|Miranda warnings]] were required; his roadside statements were therefore admissible.

## Conclusion
Ordinary traffic stops are non-custodial for Miranda purposes; Bruder's pre-arrest roadside statements were admissible. The judgment of the Pennsylvania Superior Court was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- No negative treatment. *Bruder* is a straightforward application of [[Berkemer v. McCarty]] in the [[Miranda v. Arizona]] custody line; it relies on the "degree associated with formal arrest" custody standard from [[California v. Beheler]] and the station-house analog of [[Oregon v. Mathiason]]. (Custody can still arise if a stop escalates beyond the ordinary; *Bruder* addresses only the routine roadside encounter.)

## Appears on
- [[Miranda and Custodial Interrogation]] — *Related (custody)*

## Sources
- *Pennsylvania v. Bruder*, 488 U.S. 9 (1988) (per curiam) — https://www.courtlistener.com/opinion/112152/pennsylvania-v-bruder/ — pinpoints: 10, 11.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "43fc3f52de04819e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Pennsylvania v. Bruder"}, "payload": {"all": [{"cite": "488 U.S. 9", "page": "9", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "488"}, {"cite": "109 S. Ct. 205", "page": "205", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "109"}, {"cite": "102 L. Ed. 2d 172", "page": "172", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "102"}, {"cite": "1988 U.S. LEXIS 4816", "page": "4816", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1988"}], "display": "488 U.S. 9", "official": {"cite": "488 U.S. 9", "page": "9", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "488"}, "official_selection_present": true, "record_id": "Pennsylvania v. Bruder"}}
{"assertion_id": "10e61e7c72e8ee22", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-10", "record_id": "Pennsylvania v. Bruder"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-10", "pinpoint_status": "slip-only", "quote": "--- # Pennsylvania v. Bruder *488 U.S. 9 (1988)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officer Shallis observed Bruder driving erratically and running a red light, and stopped him. Smelling alcohol and seeing Bruder's stumbling movements, the officer administered field sobriety tests and asked whether he had been drinking; Bruder admitted he had and recited the alphabet. He was then arrested for driving under the influence. The Pennsylvania Superior Court held that his roadside statements were the product of un-warned custodial interrogation and suppressed them for lack of Miranda warnings. ## Issue Whether roadside questioning of a motorist during an ordinary traffic stop — here, DUI sobriety questioning before arrest — is custodial interrogation requiring Miranda warnings. ## Rule No. The decision was", "quote_fidelity": "mismatch", "record_id": "Pennsylvania v. Bruder", "star_marker": null}}
{"assertion_id": "3cec67497223ed57", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-11", "record_id": "Pennsylvania v. Bruder"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-11", "pinpoint_status": "slip-only", "quote": "*Berkemer*'s rule, that ordinary traffic stops do not involve custody for purposes of *Miranda*, governs this case.", "quote_fidelity": "mismatch", "record_id": "Pennsylvania v. Bruder", "star_marker": null}}
{"assertion_id": "38c38c48210498f6", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Pennsylvania v. Bruder"}, "payload": {"as_of_content": "1988-10-31", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Pennsylvania v. Bruder", "scope_note": "Good law; per curiam application of Berkemer v. McCarty — ordinary traffic stops are non-custodial, so roadside DUI questioning needs no Miranda warnings before arrest.", "varies_by_point": false}}
```

### lake record — Pennsylvania v. Bruder

```json
{
  "schema_version": "s2.v1",
  "record_id": "Pennsylvania v. Bruder",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Pennsylvania v. Bruder",
    "case_name_short": "Bruder",
    "case_name_full": "Pennsylvania v. Bruder",
    "input_case_name": "Pennsylvania v. Bruder",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1988-10-31",
    "year": 1988,
    "docket": "88-161",
    "cluster_id": 112152,
    "lead_opinion_id": 112152,
    "sibling_ids": [
      112152,
      9431478,
      9431479,
      9431480
    ],
    "absolute_url": "/opinion/112152/pennsylvania-v-bruder/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "488 U.S. 9",
      "volume": "488",
      "reporter": "U.S.",
      "page": "9",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 205",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "205",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "102 L. Ed. 2d 172",
        "volume": "102",
        "reporter": "L. Ed. 2d",
        "page": "172",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1988 U.S. LEXIS 4816",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "4816",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "488 U.S. 9",
        "volume": "488",
        "reporter": "U.S.",
        "page": "9",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 205",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "205",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "102 L. Ed. 2d 172",
        "volume": "102",
        "reporter": "L. Ed. 2d",
        "page": "172",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 U.S. LEXIS 4816",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "4816",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "488 U.S. 9",
    "official_selection": {
      "court_class": "scotus",
      "selected": "488 U.S. 9",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-10",
      "page": null,
      "quote": "--- # Pennsylvania v. Bruder *488 U.S. 9 (1988)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officer Shallis observed Bruder driving erratically and running a red light, and stopped him. Smelling alcohol and seeing Bruder's stumbling movements, the officer administered field sobriety tests and asked whether he had been drinking; Bruder admitted he had and recited the alphabet. He was then arrested for driving under the influence. The Pennsylvania Superior Court held that his roadside statements were the product of un-warned custodial interrogation and suppressed them for lack of Miranda warnings. ## Issue Whether roadside questioning of a motorist during an ordinary traffic stop \u2014 here, DUI sobriety questioning before arrest \u2014 is custodial interrogation requiring Miranda warnings. ## Rule No. The decision was",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-11",
      "page": null,
      "quote": "*Berkemer*'s rule, that ordinary traffic stops do not involve custody for purposes of *Miranda*, governs this case.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1988-10-31",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Pennsylvania v. Bruder",
    "varies_by_point": false,
    "scope_note": "Good law; per curiam application of Berkemer v. McCarty \u2014 ordinary traffic stops are non-custodial, so roadside DUI questioning needs no Miranda warnings before arrest.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Tantillo",
          "cluster_id": 9413972,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Earl",
          "cluster_id": 9404588,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Missouri v. Harvey D. Harris",
          "cluster_id": 4650068,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Cawthron",
          "cluster_id": 4500714,
          "cite": [
            "97 N.E.3d 671",
            "479 Mass. 612"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane1_negative"
      },
      {
        "citing_case": {
          "name": "National Ass'n of Telecommunications Officers & Advisors v. Federal Communications Commission",
          "cluster_id": 4407120,
          "cite": [
            "862 F.3d 18",
            "2017 WL 2883738",
            "2017 U.S. App. LEXIS 12139"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Becla",
          "cluster_id": 6589084,
          "cite": [
            "74 Mass. App. Ct. 142",
            "904 N.E.2d 783",
            "2009 Mass. App. LEXIS 436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Smith v. Ohio",
          "cluster_id": 112392,
          "cite": [
            "108 L. Ed. 2d 464",
            "110 S. Ct. 1288",
            "494 U.S. 541",
            "1990 U.S. LEXIS 1198"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hildwin v. Florida",
          "cluster_id": 112269,
          "cite": [
            "104 L. Ed. 2d 728",
            "109 S. Ct. 2055",
            "490 U.S. 638",
            "1989 U.S. LEXIS 2698"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Stansbury v. California",
          "cluster_id": 117843,
          "cite": [
            "128 L. Ed. 2d 293",
            "114 S. Ct. 1526",
            "511 U.S. 318",
            "1994 U.S. LEXIS 3293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thompson v. Keohane",
          "cluster_id": 117982,
          "cite": [
            "133 L. Ed. 2d 383",
            "116 S. Ct. 457",
            "516 U.S. 99",
            "1995 U.S. LEXIS 8315",
            "95 Cal. Daily Op. Serv. 8968"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Muniz",
          "cluster_id": 112464,
          "cite": [
            "110 L. Ed. 2d 528",
            "110 S. Ct. 2638",
            "496 U.S. 582",
            "1990 U.S. LEXIS 3211"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Ortiz, Octavio",
          "cluster_id": 2945879,
          "cite": [
            "382 S.W.3d 367",
            "2012 Tex. Crim. App. LEXIS 1386",
            "2012 WL 5348503"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Carlson",
          "cluster_id": 1219515,
          "cite": [
            "808 P.2d 1002",
            "311 Or. 201",
            "1991 Ore. LEXIS 22"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Mannion",
          "cluster_id": 1486747,
          "cite": [
            "725 A.2d 196",
            "1999 Pa. Super. 25",
            "1999 Pa. Super. LEXIS 58"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Easler",
          "cluster_id": 1421141,
          "cite": [
            "489 S.E.2d 617",
            "327 S.C. 121",
            "1997 S.C. LEXIS 146"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCambridge v. State",
          "cluster_id": 2465567,
          "cite": [
            "778 S.W.2d 70",
            "1989 WL 104638"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Fish",
          "cluster_id": 1392390,
          "cite": [
            "893 P.2d 1023",
            "321 Or. 48",
            "1995 Ore. LEXIS 30"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ah Loo",
          "cluster_id": 2632163,
          "cite": [
            "10 P.3d 728",
            "94 Haw. 207",
            "2000 Haw. LEXIS 322"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Timothy E. Dobbs",
          "cluster_id": 4765836,
          "cite": [
            "945 N.W.2d 609",
            "392 Wis. 2d 505",
            "2020 WI 64"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Turner",
          "cluster_id": 2286044,
          "cite": [
            "772 A.2d 970",
            "2001 Pa. Super. 79",
            "2001 Pa. Super. LEXIS 275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mary E. Martinez, A/K/A Esperanza Lozada and Clara J. Araujo",
          "cluster_id": 597896,
          "cite": [
            "983 F.2d 968",
            "37 Fed. R. Serv. 968",
            "1992 U.S. App. LEXIS 33785",
            "1992 WL 387386"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Fritschen",
          "cluster_id": 1351455,
          "cite": [
            "802 P.2d 558",
            "247 Kan. 592",
            "1990 Kan. LEXIS 190"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Leib",
          "cluster_id": 2177823,
          "cite": [
            "588 A.2d 922",
            "403 Pa. Super. 223",
            "1991 Pa. Super. LEXIS 383"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Wimbush",
          "cluster_id": 1926596,
          "cite": [
            "750 A.2d 807",
            "561 Pa. 368",
            "2000 Pa. LEXIS 918"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Wynne",
          "cluster_id": 606744,
          "cite": [
            "993 F.2d 760",
            "1993 U.S. App. LEXIS 11403",
            "1993 WL 158552"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Burton",
          "cluster_id": 1249245,
          "cite": [
            "651 N.W.2d 143",
            "252 Mich. App. 130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Terrell v. Morris, Superintendent, Southern Ohio Correctional Facility",
          "cluster_id": 112335,
          "cite": [
            "107 L. Ed. 2d 1",
            "110 S. Ct. 4",
            "493 U.S. 1",
            "1989 U.S. LEXIS 4756",
            "58 U.S.L.W. 3236"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hasenflue",
          "cluster_id": 6162310,
          "cite": [
            "252 A.D.2d 829",
            "675 N.Y.S.2d 464",
            "1998 N.Y. App. Div. LEXIS 8593"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Bruder:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112152 OR 9431478 OR 9431479 OR 9431480) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 97,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 8,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 97,
        "triage_read": 8,
        "triage_snippet_classified": 89
      },
      "lane2_top_cited": {
        "query": "cites:(112152 OR 9431478 OR 9431479 OR 9431480)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOCZzPTEzNjYzMDMmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112152+OR+9431478+OR+9431479+OR+9431480%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 22,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112152 OR 9431478 OR 9431479 OR 9431480)",
        "reviewed": 2,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 2,
        "triage_read": 1,
        "triage_snippet_classified": 1
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112152 OR 9431478 OR 9431479 OR 9431480)",
    "indexed_citing_opinions": 125,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112152,
        "count": 105,
        "count_source": "search"
      },
      {
        "opinion_id": 9431478,
        "count": 22,
        "count_source": "search"
      },
      {
        "opinion_id": 9431479,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431480,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 190,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/pennsylvania-v-bruder.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjQwMDE1MDgmcz0zMDc4NDczJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112152+OR+9431478+OR+9431479+OR+9431480%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112152,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 110593,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 111022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 111023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 111157,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 111962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 112024,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 1981202,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 2169088,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112152,
        "cited_id": 2258133,
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
    "date_created": "2026-07-05T16:50:48Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:50:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:50:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:54:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:50:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Pennsylvania v. Bruder

```
<div>
<center><b><span class="citation" data-id="9431478"><a href="/opinion/112152/pennsylvania-v-bruder/" aria-description="Citation for case: Pennsylvania v. Bruder">488 U.S. 9</a></span> (1988)</b></center>
<center><h1>PENNSYLVANIA<br>
v.<br>
BRUDER</h1></center>
<center>No. 88-161.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Decided October 31, 1988</center>
ON PETITION FOR WRIT OF CERTIORARI TO THE SUPERIOR COURT OF PENNSYLVANIA
<p>PER CURIAM.</p>
<p>Because the decision of the Pennsylvania Superior Court in this case is contrary to <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420</a></span> (1984), we grant the petition for a writ of certiorari and reverse.</p>
<p>In the early morning of January 19, 1985, Officer Steve Shallis of the Newton Township, Pennsylvania, Police Department observed respondent Thomas Bruder driving very erratically along State Highway 252. Among other traffic violations, he ignored a red light. Shallis stopped Bruder's vehicle. Bruder left his vehicle, approached Shallis, and when asked for his registration card, returned to his car to obtain it. Smelling alcohol and observing Bruder's stumbling movements, Shallis administered field sobriety tests, <span class="star-pagination">*10</span> including asking Bruder to recite the alphabet. Shallis also inquired about alcohol. Bruder answered that he had been drinking and was returning home. Bruder failed the sobriety tests, whereupon Shallis arrested him, placed him in the police car, and gave him <i>Miranda</i> warnings. Bruder was later convicted of driving under the influence of alcohol. At his trial, his statements and conduct prior to his arrest were admitted into evidence. On appeal, the Pennsylvania Superior Court reversed, <span class="citation" data-id="9746375"><a href="/opinion/2258133/commonwealth-v-bruder/" aria-description="Citation for case: Commonwealth v. Bruder">365 Pa. Super. 106</a></span>, <span class="citation" data-id="9746375"><a href="/opinion/2258133/commonwealth-v-bruder/" aria-description="Citation for case: Commonwealth v. Bruder">528 A. 2d 1385</a></span> (1987), on the ground that the above statements Bruder had uttered during the roadside questioning were elicited through custodial interrogation and should have been suppressed for lack of <i>Miranda</i> warnings. The Pennsylvania Supreme Court denied the State's appeal application.</p>
<p>In <i>Berkemer</i> v. <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">McCarty, supra</a></span></i><i>,</i> which involved facts strikingly similar to those in this case, the Court concluded that the "noncoercive aspect of ordinary traffic stops prompts us to hold that persons temporarily detained pursuant to such stops are not `in custody' for the purposes of <i>Miranda.</i>" <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#440" aria-description="Citation for case: Berkemer v. McCarty"><i>Id.,</i> at 440</a></span>. The Court reasoned that although the stop was unquestionably a seizure within the meaning of the Fourth Amendment, such traffic stops typically are brief, unlike a prolonged station house interrogation. Second, the Court emphasized that traffic stops commonly occur in the "public view," in an atmosphere far "less `police dominated' than that surrounding the kinds of interrogation at issue in <i>Miranda</i> itself." <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#438" aria-description="Citation for case: Berkemer v. McCarty"><i>Id.,</i> at 438-439</a></span>. The detained motorist's "freedom of action [was not] curtailed to `a degree associated with formal arrest.' " <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Id.,</a></span></i> at 440 (citing <i>California</i> v. <i>Beheler,</i> <span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1125" aria-description="Citation for case: California v. Beheler">463 U. S. 1121, 1125</a></span> (1983)). Accordingly, he was not entitled to a recitation of his constitutional rights prior to arrest, and his roadside responses to questioning were admissible.<sup>[1]</sup></p>
<p><span class="star-pagination">*11</span> The facts in this record, which Bruder does not contest, reveal the same noncoercive aspects as the <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span></i> detention: "a single police officer ask[ing] respondent a modest number of questions and request[ing] him to perform a simple balancing test at a location visible to passing motorists." <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#442" aria-description="Citation for case: Berkemer v. McCarty">468 U. S., at 442</a></span> (footnote omitted).<sup>[2]</sup> Accordingly, <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span></i>'s rule, that ordinary traffic stops do not involve custody for purposes of <i>Miranda,</i> governs this case.<sup>[3]</sup> The judgment of the Pennsylvania Superior Court that evidence was inadmissible for lack of <i>Miranda</i> warnings is reversed.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE MARSHALL, dissenting.</p>
<p>I agree with JUSTICE STEVENS that the Court should not disturb the decision of the court below, and accordingly I join his dissent. I write separately to note my continuing belief that it is unfair to litigants and damaging to the integrity and accuracy of this Court's decisions to reverse a decision summarily without the benefit of full briefing on the merits of <span class="star-pagination">*12</span> the question decided. <i>Rhodes</i> v. <i>Stewart, ante,</i> p. 1 (MARSHALL, J., dissenting); <i>Buchanan</i> v. <i>Stanships, Inc.,</i> <span class="citation" data-id="9431231"><a href="/opinion/112024/buchanan-v-stanships-inc/#269" aria-description="Citation for case: Buchanan v. Stanships, Inc.">485 U. S. 265, 269</a></span> (1988) (MARSHALL, J., dissenting); <i>Commissioner</i> v. <i>McCoy,</i> <span class="citation" data-id="9431140"><a href="/opinion/111962/commissioner-v-mccoy/#7" aria-description="Citation for case: Commissioner v. McCoy">484 U. S. 3, 7</a></span> (1987) (MARSHALL, J., dissenting). I therefore dissent from the Court's decision today to reverse summarily the decision below.</p>
<p>JUSTICE STEVENS, with whom JUSTICE MARSHALL joins, dissenting.</p>
<p>The Court explains why it reverses the decision of the Superior Court of Pennsylvania in this drunken driving case, but it does not explain why it granted certiorari.</p>
<p>In <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#440" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 440-442</a></span> (1984), the Court concluded that <i>Miranda</i> warnings are not required during a traffic stop unless the citizen is taken into custody; that there is no bright-line rule for determining when detentions short of formal arrest constitute custody; and that "the only relevant inquiry is how a reasonable man in the suspect's position would have understood his situation," <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#442" aria-description="Citation for case: Berkemer v. McCarty">468 U. S., at 442</a></span>. The rule applied in Pennsylvania is strikingly similar to this Court's statement in <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span>.</i> As the Pennsylvania Superior Court explained in this case:</p>
<blockquote>"In Pennsylvania, `custodial interrogation does not require that police make a formal arrest, nor that the police intend to make an arrest. . . . Rather, the test of custodial interrogation is whether the individual being interrogated reasonably believes his freedom of action is being restricted.' <i>Commonwealth</i> v. <i>Meyer,</i> <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/#307" aria-description="Citation for case: Commonwealth v. Meyer">488 Pa. 297, 307</a></span>, <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/#521" aria-description="Citation for case: Commonwealth v. Meyer">412 A. 2d 517, 521</a></span> (1980) (quoting <i>Commonwealth</i> v. <i>Brown,</i> <span class="citation" data-id="2169088"><a href="/opinion/2169088/commonwealth-v-brown/#570" aria-description="Citation for case: Commonwealth v. Brown">473 Pa. 562, 570</a></span>, <span class="citation" data-id="2169088"><a href="/opinion/2169088/commonwealth-v-brown/#1264" aria-description="Citation for case: Commonwealth v. Brown">375 A. 2d 1260, 1264</a></span> (1977). . . .</blockquote>
<blockquote>"In <i>Commonwealth</i> v. <i><span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/" aria-description="Citation for case: Commonwealth v. Meyer">Meyer</a></span></i><i>,</i> the Pennsylvania Supreme Court ruled that the driver of a car involved in an accident who was suspected of driving under the influence of alcohol and who was told by police to wait at the scene until additional police arrived was in custody for <span class="star-pagination">*13</span> purposes of <i>Miranda.</i> The <i><span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/" aria-description="Citation for case: Commonwealth v. Meyer">Meyer</a></span></i> court reasoned that because the defendant had a reasonable belief that his freedom of action had been restricted, statements elicited before he received his <i>Miranda</i> warnings should have been suppressed. <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/#307" aria-description="Citation for case: Commonwealth v. Meyer">488 Pa. at 307</a></span>, <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/#522" aria-description="Citation for case: Commonwealth v. Meyer">412 A. 2d at 522</a></span>." <span class="citation" data-id="9746375"><a href="/opinion/2258133/commonwealth-v-bruder/#111" aria-description="Citation for case: Commonwealth v. Bruder">365 Pa. Super. 106, 111-112</a></span>, <span class="citation" data-id="9746375"><a href="/opinion/2258133/commonwealth-v-bruder/#1387" aria-description="Citation for case: Commonwealth v. Bruder">528 A. 2d 1385, 1387</a></span> (1987).</blockquote>
<p>In its <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span></i> opinion, this Court cited the Pennsylvania Supreme Court's opinion in <i>Commonwealth</i> v. <i>Meyer,</i> <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/" aria-description="Citation for case: Commonwealth v. Meyer">488 Pa. 297</a></span>, <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/" aria-description="Citation for case: Commonwealth v. Meyer">412 A. 2d 517</a></span> (1980), with approval. <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#441" aria-description="Citation for case: Berkemer v. McCarty">468 U. S., at 441, n. 34</a></span>. Thus, there appears to be no significant difference between the rule of law that is generally applied to traffic stops in Pennsylvania and the rule that this Court would approve in other States.</p>
<p>There is, however, a difference of opinion on the question whether the rule was correctly applied in this case. The Superior Court of Pennsylvania was divided on the issue. See 365 Pa. Super., at 117, <span class="citation" data-id="9746375"><a href="/opinion/2258133/commonwealth-v-bruder/#1390" aria-description="Citation for case: Commonwealth v. Bruder">528 A. 2d, at 1390</a></span> (Rowley, J., concurring and dissenting). It was therefore quite appropriate for the prosecutor to seek review in the Supreme Court of Pennsylvania. That court summarily denied review without opinion. See <span class="citation no-link">518 Pa. 635</span>, <span class="citation no-link">542 A. 2d 1365</span> (1988). That action was quite appropriate for the highest court of a large State like Pennsylvania because such a court is obviously much too busy to review every arguable misapplication of settled law in cases of this kind.</p>
<p>For reasons that are unclear to me, however, this Court seems to welcome the opportunity to perform an error-correcting function in cases that do not merit the attention of the highest court of a sovereign State. See, <i>e. g., </i><i>Florida</i> v. <i>Meyers,</i> <span class="citation" data-id="9429577"><a href="/opinion/111157/florida-v-meyers/" aria-description="Citation for case: Florida v. Meyers">466 U. S. 380</a></span> (1984) <i>(per curiam)</i><i>; </i><i>Illinois</i> v. <i>Batchelder,</i> <span class="citation" data-id="9429372"><a href="/opinion/111022/illinois-v-batchelder/" aria-description="Citation for case: Illinois v. Batchelder">463 U. S. 1112</a></span> (1983) <i>(per curiam)</i><i>.</i> Although there are cases in which "there are special and important reasons" for correcting an error that is committed by another court, see this Court's Rule 17.1, this surely is not such a case. The Court does not suggest that this case involves an <span class="star-pagination">*14</span> important and unsettled question of federal law or that there is confusion among the state and federal courts concerning what legal rules govern the application of <i>Miranda</i> to ordinary traffic stops. Rather, the Court simply holds that the Superior Court of Pennsylvania misapplied our decision in <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span></i> to "[t]he facts in this record." <i>Ante,</i> at 11. In my judgment this Court's scarce resources would be far better spent addressing cases that are of some general importance "beyond the facts and parties involved," <i>Boag</i> v. <i>MacDougall,</i> <span class="citation" data-id="9428558"><a href="/opinion/110593/boag-v-macdougall/#368" aria-description="Citation for case: Boag v. MacDougall">454 U. S. 364, 368</a></span> (1982) (REHNQUIST, J., dissenting), than in our acting as "self-appointed . . . supervisors of the administration of justice in the state judicial systems," <i>Florida</i> v. <i>Meyers,</i> <span class="citation" data-id="9429577"><a href="/opinion/111157/florida-v-meyers/#385" aria-description="Citation for case: Florida v. Meyers">466 U. S., at 385</a></span> (STEVENS, J., dissenting).</p>
<p>Accordingly, because I would not disturb the decision of the Supreme Court of Pennsylvania  which, incidentally, is the court to which the petitioner asks us to direct the writ of certiorari  I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[1]  We did not announce an absolute rule for all motorist detentions, observing that lower courts must be vigilant that police do not "delay formally arresting detained motorists, and . . . subject them to sustained and intimidating interrogation at the scene of their initial detention." <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#440" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 440</a></span> (1984).</p>
<p>[2]  Reliance on the Pennsylvania Supreme Court's decision in <i>Commonwealth</i> v. <i>Meyer,</i> <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/" aria-description="Citation for case: Commonwealth v. Meyer">488 Pa. 297</a></span>, <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/" aria-description="Citation for case: Commonwealth v. Meyer">412 A. 2d 517</a></span> (1980), to which we referred in <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span>,</i> see <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#441" aria-description="Citation for case: Berkemer v. McCarty">468 U. S., at 441</a></span>, and n. 34, is inapposite. <i><span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/" aria-description="Citation for case: Commonwealth v. Meyer">Meyer</a></span></i> involved facts which we implied might properly remove its result from <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span></i>'s application to ordinary traffic stops; specifically, the motorist in <i><span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/" aria-description="Citation for case: Commonwealth v. Meyer">Meyer</a></span></i> could be found to have been placed in custody for purposes of <i>Miranda</i> safeguards because he was detained for over half an hour, and subjected to questioning while in the patrol car. Thus, we acknowledged <i><span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/" aria-description="Citation for case: Commonwealth v. Meyer">Meyer</a></span></i>'s relevance to the unusual traffic stop that involves prolonged detention. We expressly disapproved, however, the attempt to extrapolate from this sensitivity to uncommon detention circumstances any general proposition that custody exists whenever motorists think that their freedom of action has been restricted, for such a rationale would eviscerate <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span></i> altogether. See <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#436" aria-description="Citation for case: Berkemer v. McCarty"><i>Berkemer, supra,</i> at 436-437</a></span>.</p>
<p>[3]  We thus do not reach the issue whether recitation of the alphabet in response to custodial questioning is testimonial and hence inadmissible under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966).</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Pennsylvania v. Labron.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Pennsylvania v. Labron"
type: case
citation: "518 U.S. 938 (1996)"
parallel_cite: "116 S. Ct. 2485; 135 L. Ed. 2d 1031"
neutral_cite: 1996 U.S. LEXIS 4268
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1996
date_decided: 1996-07-01
docket: 95-1691
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1996-07-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Pennsylvania v. Labron
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118063/pennsylvania-v-labron/"
  cluster_id: 118063
  opinion_id: 118063
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[Carroll v. United States]]", "[[California v. Carney]]", "[[Chambers v. Maroney]]"]
aliases: ["Pennsylvania v. Kilgore"]
tags: ["case", "fourth-amendment", "automobile-exception", "ready-mobility", "per-curiam"]
holding: "No separate exigency requirement beyond ready mobility: if a car is readily mobile and PC exists to believe it contains contraband, the…"
lake:
  record_id: Pennsylvania v. Labron
  status: verified
  projected_at: 2026-07-09
---

# Pennsylvania v. Labron

*518 U.S. 938 (1996)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
In two consolidated cases, the Supreme Court of Pennsylvania suppressed evidence on the theory that the automobile exception requires both probable cause *and* separate [[Exigent Circumstances and Hot Pursuit|exigent circumstances]]. In *Labron*, police watched Labron conduct street drug transactions in Philadelphia, arrested the suspects, searched the trunk of the car from which the drugs had been produced, and found cocaine. (In the companion *Kilgore* case, police searched a pickup truck after a controlled buy.)

## Issue
Whether the automobile exception requires a separate showing of [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] beyond the vehicle's ready mobility and probable cause to believe it contains contraband.

## Rule
No separate [[Exigent Circumstances and Hot Pursuit|exigency]] is required. "If a car is readily mobile and probable cause exists to believe it contains contraband, the Fourth Amendment thus permits police to search the vehicle without more." — 518 U.S. at 940. ^pin-940

A vehicle's "ready mobility" is itself "an exigency sufficient to excuse failure to obtain a search warrant once probable cause to conduct the search is clear." — [*Id.*](https://www.courtlistener.com/opinion/118063/pennsylvania-v-labron/#:~:text=ready%20mobility) ^pin-940a

## Application
Police had seen Labron place drugs in the trunk of the car they searched — supplying probable cause — and the car was readily mobile. Because ready mobility plus probable cause is all the automobile exception requires, the warrantless search of the trunk did not violate the Fourth Amendment, and the Pennsylvania Supreme Court's contrary rule (demanding separate [[Exigent Circumstances and Hot Pursuit|exigent circumstances]]) rested on an incorrect reading of the exception.

## Conclusion
The automobile exception requires only ready mobility and probable cause, not a separate [[Exigent Circumstances and Hot Pursuit|exigency]]; the Pennsylvania judgments were reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Labron* confirms the "ready-mobility" rationale traced from [[Carroll v. United States]] through [[California v. Carney]].

## Appears on
- [[Automobile Exception]] — *Key — Progeny / Refinement*

## Sources
- *Pennsylvania v. Labron*, 518 U.S. 938 (1996) (per curiam) — https://www.courtlistener.com/opinion/118063/pennsylvania-v-labron/ — pinpoint: 940.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "dd32baa0925ff42b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Pennsylvania v. Labron"}, "payload": {"all": [{"cite": "518 U.S. 938", "page": "938", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "518"}, {"cite": "116 S. Ct. 2485", "page": "2485", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "116"}, {"cite": "135 L. Ed. 2d 1031", "page": "1031", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "135"}, {"cite": "1996 U.S. LEXIS 4268", "page": "4268", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1996"}], "display": "518 U.S. 938", "official": {"cite": "518 U.S. 938", "page": "938", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "518"}, "official_selection_present": true, "record_id": "Pennsylvania v. Labron"}}
{"assertion_id": "125eeea03eb63509", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-940", "record_id": "Pennsylvania v. Labron"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-940", "pinpoint_status": "slip-only", "quote": "--- # Pennsylvania v. Labron *518 U.S. 938 (1996)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In two consolidated cases, the Supreme Court of Pennsylvania suppressed evidence on the theory that the automobile exception requires both probable cause *and* separate exigent circumstances. In *Labron*, police watched Labron conduct street drug transactions in Philadelphia, arrested the suspects, searched the trunk of the car from which the drugs had been produced, and found cocaine. (In the companion *Kilgore* case, police searched a pickup truck after a controlled buy.) ## Issue Whether the automobile exception requires a separate showing of exigent circumstances beyond the vehicle's ready mobility and probable cause to believe it contains contraband. ## Rule No separate exigency is required.", "quote_fidelity": "mismatch", "record_id": "Pennsylvania v. Labron", "star_marker": null}}
{"assertion_id": "59064c97d843e010", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-940a", "record_id": "Pennsylvania v. Labron"}, "payload": {"fragment": "#:~:text=ready%20mobility", "page": null, "pin_id": "pin-940a", "pinpoint_status": "star-verified", "quote": "ready mobility", "quote_fidelity": "matched", "record_id": "Pennsylvania v. Labron", "star_marker": "940"}}
{"assertion_id": "1780adf8335d54ae", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Pennsylvania v. Labron"}, "payload": {"as_of_content": "1996-07-01", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Pennsylvania v. Labron", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Pennsylvania v. Labron

```json
{
  "schema_version": "s2.v1",
  "record_id": "Pennsylvania v. Labron",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Pennsylvania v. Labron",
    "case_name_short": "Labron",
    "case_name_full": "Pennsylvania v. Labron",
    "input_case_name": "Pennsylvania v. Labron",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1996-07-01",
    "year": 1996,
    "docket": "95-1691",
    "cluster_id": 118063,
    "lead_opinion_id": 118063,
    "sibling_ids": [
      118063,
      9433386,
      9433387
    ],
    "absolute_url": "/opinion/118063/pennsylvania-v-labron/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "518 U.S. 938",
      "volume": "518",
      "reporter": "U.S.",
      "page": "938",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "116 S. Ct. 2485",
        "volume": "116",
        "reporter": "S. Ct.",
        "page": "2485",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 L. Ed. 2d 1031",
        "volume": "135",
        "reporter": "L. Ed. 2d",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1996 U.S. LEXIS 4268",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "4268",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "518 U.S. 938",
        "volume": "518",
        "reporter": "U.S.",
        "page": "938",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "116 S. Ct. 2485",
        "volume": "116",
        "reporter": "S. Ct.",
        "page": "2485",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 L. Ed. 2d 1031",
        "volume": "135",
        "reporter": "L. Ed. 2d",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1996 U.S. LEXIS 4268",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "4268",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "518 U.S. 938",
    "official_selection": {
      "court_class": "scotus",
      "selected": "518 U.S. 938",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-940",
      "page": null,
      "quote": "--- # Pennsylvania v. Labron *518 U.S. 938 (1996)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In two consolidated cases, the Supreme Court of Pennsylvania suppressed evidence on the theory that the automobile exception requires both probable cause *and* separate exigent circumstances. In *Labron*, police watched Labron conduct street drug transactions in Philadelphia, arrested the suspects, searched the trunk of the car from which the drugs had been produced, and found cocaine. (In the companion *Kilgore* case, police searched a pickup truck after a controlled buy.) ## Issue Whether the automobile exception requires a separate showing of exigent circumstances beyond the vehicle's ready mobility and probable cause to believe it contains contraband. ## Rule No separate exigency is required.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-940a",
      "page": null,
      "quote": "ready mobility",
      "star_marker": "940",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 6615,
      "fragment": "#:~:text=ready%20mobility",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1996-07-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Pennsylvania v. Labron",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Knight",
          "cluster_id": 4499332,
          "cite": [
            "419 P.3d 637",
            "55 Kan. App. 2d 642"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane1_negative"
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
        "journal_ref": "Pennsylvania v. Labron:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bernard West v. United States",
          "cluster_id": 2735560,
          "cite": [
            "100 A.3d 1076",
            "2014 D.C. App. LEXIS 382",
            "2014 WL 4636023"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Meekins v. State",
          "cluster_id": 2544137,
          "cite": [
            "340 S.W.3d 454",
            "2011 Tex. Crim. App. LEXIS 592",
            "2011 WL 1663151"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Black",
          "cluster_id": 1814285,
          "cite": [
            "987 So. 2d 1177",
            "2006 WL 2457818"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Tyrone Werts v. Donald T. Vaughn the District Attorney of the County of Philadelphia the Attorney General of the State of Pennsylvania",
          "cluster_id": 770608,
          "cite": [
            "228 F.3d 178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Dyson",
          "cluster_id": 2621047,
          "cite": [
            "144 L. Ed. 2d 442",
            "119 S. Ct. 2013",
            "527 U.S. 465",
            "1999 U.S. LEXIS 4200"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wayne Gaskin, AKA \"Atiba,\" and Al Castle",
          "cluster_id": 785776,
          "cite": [
            "364 F.3d 438",
            "2004 U.S. App. LEXIS 7440",
            "2004 WL 818734"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rocha",
          "cluster_id": 4345763,
          "cite": [
            "295 Neb. 716",
            "890 N.W.2d 178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Allen",
          "cluster_id": 4673511,
          "cite": [
            "2019 CO 88"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. William L. Witt(074468)",
          "cluster_id": 2993869,
          "cite": [
            "223 N.J. 409",
            "126 A.3d 850",
            "2015 N.J. LEXIS 890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Thompson",
          "cluster_id": 1836924,
          "cite": [
            "842 So. 2d 330",
            "2003 WL 1826561"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Powell",
          "cluster_id": 1736,
          "cite": [
            "175 L. Ed. 2d 1009",
            "130 S. Ct. 1195",
            "559 U.S. 50",
            "2010 U.S. LEXIS 1898"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Kazmierczak",
          "cluster_id": 1965440,
          "cite": [
            "605 N.W.2d 667",
            "461 Mich. 411",
            "2000 WL 146099"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Keehn v. State",
          "cluster_id": 2341745,
          "cite": [
            "279 S.W.3d 330",
            "2009 Tex. Crim. App. LEXIS 425",
            "2009 WL 774854"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Guzman",
          "cluster_id": 1785574,
          "cite": [
            "959 S.W.2d 631",
            "1998 Tex. Crim. App. LEXIS 12",
            "1998 WL 28103"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. White",
          "cluster_id": 118287,
          "cite": [
            "143 L. Ed. 2d 748",
            "119 S. Ct. 1555",
            "526 U.S. 559",
            "1999 U.S. LEXIS 3172"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Brownlee",
          "cluster_id": 2106553,
          "cite": [
            "713 N.E.2d 556",
            "186 Ill. 2d 501",
            "239 Ill. Dec. 25",
            "1999 Ill. LEXIS 686"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marco Burton",
          "cluster_id": 777431,
          "cite": [
            "288 F.3d 91",
            "2002 U.S. App. LEXIS 7851",
            "2002 WL 753492"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Turner",
          "cluster_id": 4326929,
          "cite": [
            "2016 Ohio 7983"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cooke",
          "cluster_id": 2196499,
          "cite": [
            "751 A.2d 92",
            "163 N.J. 657",
            "2000 N.J. LEXIS 529"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dixon v. State",
          "cluster_id": 1400372,
          "cite": [
            "206 S.W.3d 613",
            "2006 Tex. Crim. App. LEXIS 1006",
            "2006 WL 1408451"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Myers v. State",
          "cluster_id": 852726,
          "cite": [
            "839 N.E.2d 1146",
            "2005 Ind. LEXIS 1135",
            "2005 WL 3484607"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Labron:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118063 OR 9433386 OR 9433387) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTMzOTEzNjAwMDAwJnM9MjU2NzQzMCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118063+OR+9433386+OR+9433387%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(118063 OR 9433386 OR 9433387)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04MSZzPTc3ODkxMiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118063+OR+9433386+OR+9433387%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118063 OR 9433386 OR 9433387)",
        "reviewed": 23,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 23,
        "triage_read": 0,
        "triage_snippet_classified": 23
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118063 OR 9433386 OR 9433387)",
    "indexed_citing_opinions": 389,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118063,
        "count": 330,
        "count_source": "search"
      },
      {
        "opinion_id": 9433386,
        "count": 64,
        "count_source": "search"
      },
      {
        "opinion_id": 9433387,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 669,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/pennsylvania-v-labron.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg0Njk5OTYmcz05NDMwNzA2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118063+OR+9433386+OR+9433387%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118063,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 111430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 111625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 111872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 111928,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 112175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 112205,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 112464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 112475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 117905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 1473518,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 1752565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 1983319,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 1984308,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 2073495,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 2089408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 2089468,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 2100000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 2165222,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118063,
        "cited_id": 2316698,
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
    "date_created": "2026-07-05T16:54:56Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:55:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:55:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:58:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:55:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Pennsylvania v. Labron

```
<div>
<center><b><span class="citation" data-id="9433386"><a href="/opinion/118063/pennsylvania-v-labron/" aria-description="Citation for case: Pennsylvania v. Labron">518 U.S. 938</a></span> (1996)</b></center>
<center><h1>PENNSYLVANIA<br>
v.<br>
LABRON</h1></center>
<center>No. 95-1691.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Decided July 1, 1996.<sup>[*]</sup></center>
ON PETITION FOR WRIT OF CERTIORARI TO THE SUPREME COURT OF PENNSYLVANIA
<p>Per Curiam.</p>
<p>In these two cases, the Supreme Court of Pennsylvania held that the Fourth Amendment, as applied to the States through the Fourteenth, requires police to obtain a warrant <span class="star-pagination">*939</span> before searching an automobile unless exigent circumstances are present. Because the holdings rest on an incorrect reading of the automobile exception to the Fourth Amendment's warrant requirement, we grant the petitions for certiorari and reverse.</p>
<p>In <i>Labron,</i> No. 95-1691, police observed respondent Labron and others engaging in a series of drug transactions on a street in Philadelphia. The police arrested the suspects, searched the trunk of a car from which the drugs had been produced, and found bags containing cocaine. The Pennsylvania Supreme Court agreed with the trial court (but not with the intermediate court of appeals, <span class="citation no-link">428 Pa. Super. 616</span>, <span class="citation no-link">626 A. 2d 646</span> (1993), whose judgment it reversed) that this evidence should be suppressed. <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/" aria-description="Citation for case: Commonwealth v. Labron">543 Pa. 86</a></span>, <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/" aria-description="Citation for case: Commonwealth v. Labron">669 A. 2d 917</a></span> (1995). After surveying our precedents on the automobile exception as well as some of its own decisions, the court "conclude[d] that this Commonwealth's jurisprudence of the automobile exception has long required both the existence of probable cause and the presence of exigent circumstances to justify a warrantless search." <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#100" aria-description="Citation for case: Commonwealth v. Labron"><i>Id.,</i> at 100</a></span>, <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#924" aria-description="Citation for case: Commonwealth v. Labron">669 A. 2d, at 924</a></span>. Satisfied the police had time to secure a warrant, <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#100" aria-description="Citation for case: Commonwealth v. Labron"><i>id.,</i> at 100-103</a></span>, 699 A. 2d, at 924-925, the court held that "the warrantless search of this stationary vehicle violated constitutional guarantees," <i>id.,</i> at 101, <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#924" aria-description="Citation for case: Commonwealth v. Labron">669 A. 2d, at 924</a></span>.</p>
<p>In <i>Kilgore,</i> No. 95-1738, an undercover informant agreed to buy drugs from respondent Randy Lee Kilgore's accomplice, Kelly Jo Kilgore. To obtain the drugs, Kelly Jo drove from the parking lot where the deal was made to a farmhouse where she met with Randy Kilgore and obtained the drugs. After the drugs were delivered and the Kilgores were arrested, police searched the farmhouse with the consent of its owner and also searched Randy Kilgore's pickup truck; they had seen the Kilgores walking to and from the truck, which was parked in the driveway of the farmhouse. The search turned up cocaine on the truck's floor. The trial court denied Randy Kilgore's motion to suppress the cocaine, holding the officers had probable cause to make the search. <span class="star-pagination">*940</span> The appellate court affirmed. <span class="citation" data-id="2165222"><a href="/opinion/2165222/commonwealth-v-kilgore/" aria-description="Citation for case: Commonwealth v. Kilgore">437 Pa. Super. 491</a></span>, <span class="citation" data-id="2165222"><a href="/opinion/2165222/commonwealth-v-kilgore/" aria-description="Citation for case: Commonwealth v. Kilgore">650 A. 2d 462</a></span> (1994). The Supreme Court of Pennsylvania reversed, citing <i>Labron</i> and holding that although there was probable cause to search the truck, <span class="citation" data-id="9714930"><a href="/opinion/2089408/commonwealth-v-kilgore/#444" aria-description="Citation for case: Commonwealth v. Kilgore">544 Pa. 439, 444</a></span>, <span class="citation" data-id="9714930"><a href="/opinion/2089408/commonwealth-v-kilgore/#313" aria-description="Citation for case: Commonwealth v. Kilgore">677 A. 2d 311, 313</a></span> (1995), the search violated the Fourth Amendment because no exigent circumstances justified the failure to obtain a warrant, <span class="citation" data-id="9714930"><a href="/opinion/2089408/commonwealth-v-kilgore/#445" aria-description="Citation for case: Commonwealth v. Kilgore"><i>id.,</i> at 445</a></span>, <span class="citation" data-id="9714930"><a href="/opinion/2089408/commonwealth-v-kilgore/#313" aria-description="Citation for case: Commonwealth v. Kilgore">677 A. 2d, at 313-314</a></span>.</p>
<p>The Supreme Court of Pennsylvania held the rule permitting warrantless searches of automobiles is limited to cases where "`unforeseen circumstances involving the search of an automobile [are] coupled with the presence of probable cause.' " <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#100" aria-description="Citation for case: Commonwealth v. Labron">543 Pa., at 100</a></span>, <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#924" aria-description="Citation for case: Commonwealth v. Labron">669 A. 2d, at 924</a></span>, quoting <i>Commonwealth</i> v. <i>White,</i> <span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/#53" aria-description="Citation for case: Commonwealth v. White">543 Pa. 45, 53</a></span>, <span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/#901" aria-description="Citation for case: Commonwealth v. White">669 A. 2d 896, 901</a></span> (1995) (emphasis deleted). This was incorrect. Our first cases establishing the automobile exception to the Fourth Amendment's warrant requirement were based on the automobile's "ready mobility," an exigency sufficient to excuse failure to obtain a search warrant once probable cause to conduct the search is clear. <i>California</i> v. <i>Carney,</i> <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#390" aria-description="Citation for case: California v. Carney">471 U. S. 386, 390-391</a></span> (1985) (tracing the history of the exception); <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925). More recent cases provide a further justification: the individual's reduced expectation of privacy in an automobile, owing to its pervasive regulation. <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#391" aria-description="Citation for case: California v. Carney"><i>Carney, supra,</i> at 391-392</a></span>. If a car isreadily mobile and probable cause exists to believe it contains contraband, the Fourth Amendment thus permits police to search the vehicle without more. <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#393" aria-description="Citation for case: California v. Carney"><i>Carney, supra,</i> at 393</a></span>. As the state courts found, there was probable cause in both of these cases: Police had seen respondent Labron put drugs in the trunk of the car they searched and had seen respondent Kilgore act in ways that suggested he had drugs in his truck. We conclude the searches of the automobiles in these cases did not violate the Fourth Amendment.</p>
<p>Respondent Labron claims we have no jurisdiction to review the judgment in his case because the Pennsylvania Supreme Court's opinion rests on an adequate and independent <span class="star-pagination">*941</span> state ground, viz., "this Commonwealth's jurisprudence of the automobile exception." 543 Pa., at 100, 669 A. 2d, at 924. We disagree. The language we have quoted is not a "plain statement" sufficient to tell us "the federal cases [were] being used only for the purpose of guidance, and d[id] not themselves compel the result that the court ha[d] reached." <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1041" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1041</a></span> (1983). The Pennsylvania Supreme Court did discuss several of its own decisions; as it noted, however, some of those cases relied on an analysis of our cases on the automobile exception, see, <i>e. g.,</i> 543 Pa., at 95, 669 A. 2d, at 921 (observing <i>Commonwealth</i> v. <i>Holzer,</i> <span class="citation" data-id="9711114"><a href="/opinion/2073495/commonwealth-v-holzer/#103" aria-description="Citation for case: Commonwealth v. Holzer">480 Pa. 93, 103</a></span>, <span class="citation" data-id="9711114"><a href="/opinion/2073495/commonwealth-v-holzer/#106" aria-description="Citation for case: Commonwealth v. Holzer">389 A. 2d 101, 106</a></span> (1978), cited <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971)); 543 Pa., at 100, 669 A. 2d, at 924 (stating <i>Commonwealth</i> v. <i><span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/" aria-description="Citation for case: Commonwealth v. White">White, supra</a></span></i><i>,</i> rested in part upon the Pennsylvania Supreme Court's analysis of <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970)). The law of the Commonwealth thus appears to us "interwoven with the federal law, and . . . the adequacy and independence of any possible state law ground is not clear from the face of the opinion." <i>Michigan</i> v. <i>Long,</i>  <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long">463 U. S., at 1040-1041</a></span>. Our jurisdiction in Labron's case is secure. <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Ibid.</a></span></i> The opinion in respondent Kilgore's case, meanwhile, rests on an explicit conclusion that the officers' conduct violated the Fourth Amendment; we have jurisdiction to review this judgment as well.</p>
<p>Respondent Labron's motion to proceed <i>in forma pauperis</i>  is granted. The petitions for writs of certiorari are granted, the judgments of the Supreme Court of Pennsylvania are reversed, and the cases are remanded for further proceedings not inconsistent with this opinion.</p>
<blockquote>
<i>It is so ordered.</i>  Justice Stevens, with whom Justice Ginsburg joins, dissenting.</blockquote>
<p>The decisions that the Court summarily reverses today are two of a trilogy of cases decided by the Pennsylvania Supreme <span class="star-pagination">*942</span> Court within three days of each other. See <span class="citation" data-id="9714930"><a href="/opinion/2089408/commonwealth-v-kilgore/" aria-description="Citation for case: Commonwealth v. Kilgore">544 Pa. 439</a></span>, <span class="citation" data-id="9714930"><a href="/opinion/2089408/commonwealth-v-kilgore/" aria-description="Citation for case: Commonwealth v. Kilgore">677 A. 2d 311</a></span> (1995); <i>Commonwealth</i> v. <i>White,</i> <span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/" aria-description="Citation for case: Commonwealth v. White">543 Pa. 45</a></span>, <span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/" aria-description="Citation for case: Commonwealth v. White">669 A. 2d 896</a></span> (1995); <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/" aria-description="Citation for case: Commonwealth v. Labron">543 Pa. 86</a></span>, <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/" aria-description="Citation for case: Commonwealth v. Labron">669 A. 2d 917</a></span> (1995).<sup>[1]</sup> In each case, that court concluded that citizens of Pennsylvania are protected from warrantless searches and seizures of their automobiles absent exigent circumstances. But a fair reading of both <i>White</i> (the holding of which the Commonwealth has not challenged in this Court) and <i>Labron</i> (which the Court reverses today) demonstrates that their judgments almost certainly rested upon the Pennsylvania court's independent consideration of its own Constitution. For that reason, I do not believe that we have jurisdiction over the decision in <i>Labron,</i> just as we would not have jurisdiction in <i>White.</i> See <span class="citation no-link">28 U. S. C. § 1257</span>(a).<sup>[2]</sup> Furthermore, when considered in light of those two more carefully reasoned decisions, there is no reason for this Court to disturb the state court's finding in <i>Kilgore,</i> since the result will almost certainly be affirmed on remand.</p>
<p>In its <i>per curiam</i> decision, this Court concludes that because the decision in <i>Labron</i> cited state decisions which in turn referred to two 25-year-old cases of this Court, any reference to state law is "`interwoven with the federal law.' " <i>Ante,</i> at 941 (quoting <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1040</a></span> (1983)). These references, however, seem to me a rather short thread with which to weavelet alone upon which to hangour jurisdiction.</p>
<p><span class="star-pagination">*943</span> In my opinion, the best reading of <i>Labron</i> `s plain language is that it relied on adequate and independent state grounds. The majority decision below includes references to four sources of federal law: the Federal Constitution and three federal cases. None of the references demonstrates that the decision rested upon anything other than state law.</p>
<p>The decision begins with the proposition, not at issue here, that "the Fourth Amendment to the United States Constitution and Article I, § 8 of the Pennsylvania Constitution generally require that searches be predicated upon a warrant issued by a neutral and detached magistrate." 543 Pa., at 93, 669 A. 2d, at 920 (citations omitted). It then reviews the history of the so-called "automobile exception" to the warrant requirement by quoting several passages from our decision in <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), which first established the exception, and then quotes a passage from <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 52</a></span> (1970),<sup>[3]</sup> which appears to support the proposition under federal law that the Court emphasizes here today (that the existence of probable cause is sufficient in and of itself to justify a search of a vehicle). 543 Pa., at 94-95, 669 A. 2d, at 920-921.</p>
<p>Rather than follow the developments of federal law, however, the decision then specifically and immediately notes that "[w]hen reviewing warrantless automobile searches <i>in this Commonwealth,</i> we have constantly held that `there is no "automobile exception" as such and [that] the constitutional protections are applicable to searches and seizures of a person's car.' <i>Commonwealth</i> v. <i>Holzer,</i> <span class="citation" data-id="9711114"><a href="/opinion/2073495/commonwealth-v-holzer/#103" aria-description="Citation for case: Commonwealth v. Holzer">480 Pa. 93, 103</a></span>, <span class="citation" data-id="9711114"><a href="/opinion/2073495/commonwealth-v-holzer/#106" aria-description="Citation for case: Commonwealth v. Holzer">389 A. 2d 101, 106</a></span> (1978) (citing <i>Coolidge</i> v. <i>New Hampshire,</i>  <span class="star-pagination">*944</span> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> .. . (1971))." <i>Id.,</i> at 95, 669 A. 2d, at 921 (emphasis added). From that point onward, the only reference to federal law in the decision's remaining 30 citations is a recognition that <i>White,</i> the sole decision of this trio of "exigent circumstance" cases that is not before our Court, was "based upon" that Court's analysis of <i>Chambers.</i> 543 Pa., at 99-100, 669 A. 2d, at 923-924. Every other citation in <i>Labron</i> is to Pennsylvania law.</p>
<p>Because <i>White</i> was issued on the same day as <i>Labron</i> and reached an identical conclusion regarding the "exigent circumstances" rule, that decision is worth reviewing. In <i>White,</i> the court hesitated before considering the merits of the case "to address the Commonwealth's claim that White has waived his claim that the search of his automobile was illegal under Article I, Section 8 of the Pennsylvania Constitution because he did not set forth his state constitutional claims in the manner required." The Commonwealth's claim, the court found, was "meritless." "White clearly raises a claim under the Pennsylvania Constitution, cites cases in support of his claim, and relates the cases to the claim. That is sufficient." 543 Pa., at 50, 669 A. 2d, at 899.</p>
<p>Having established the importance of the state constitutional claim to the defendant's argument, <i>White</i> went on to discuss the "exigent circumstance" exception at issue here in light of both federal and state law. And although the court's analysis relied upon our decision in <i>Chambers</i> v. <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Maroney</a></span></i><i>,</i> it cited none of the subsequent cases in which this Court has effectively converted the "automobile exception" into an absolute rule allowing searches in the presence of probable cause. See 543 Pa., at 49-53, 669 A. 2d, at 899-901; n. 6, <i>infra</i> (noting that the Pennsylvania courts' failure to refer to this Court's subsequent decisions in this area may be intentional rather than ignorant). Stressing the independent evaluation it makes of its State Constitution, the Pennsylvania court also rejected our decision in <i>New York</i> v. <i>Belton,</i>  <span class="star-pagination">*945</span> <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981), on state constitutional grounds. See 543 Pa., at 54-58, 669 A. 2d, at 901-903.<sup>[4]</sup></p>
<p>Notably, the Commonwealth has not asked this Court to review the Pennsylvania court's decision in <i>White,</i> even though the search in that case would be affirmed under the Commonwealth's and this Court's understanding of Pennsylvania's holding regarding exigent circumstances. I also note that lower state courts have explicitly read <i>White</i> as establishing a state constitutional right, not a federal right. <i>Commonwealth</i> v. <i>Haskins,</i> <span class="citation" data-id="2089468"><a href="/opinion/2089468/commonwealth-v-haskins/#545" aria-description="Citation for case: Commonwealth v. Haskins">450 Pa. Super. 540, 545</a></span>, <span class="citation" data-id="2089468"><a href="/opinion/2089468/commonwealth-v-haskins/#330" aria-description="Citation for case: Commonwealth v. Haskins">677 A. 2d 328, 330</a></span> (1996) ("In order to search an automobile without a warrant, the police must still show the existence of both probable cause and exigent circumstances. <i>Commonwealth</i>  v. <i>White,</i> <span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/" aria-description="Citation for case: Commonwealth v. White">543 Pa. 45</a></span>, <span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/" aria-description="Citation for case: Commonwealth v. White">669 A. 2d 896</a></span> (1995). . . . In <i>White,</i> our Supreme Court reiterated that the Pennsylvania Constitution requires such a showing"); see also <i>Commonwealth</i> v. <i>Yedinak,</i> <span class="citation" data-id="9716881"><a href="/opinion/2100000/commonwealth-v-yedinak/#359" aria-description="Citation for case: Commonwealth v. Yedinak">450 Pa. Super. 352, 359, n. 5</a></span>, <span class="citation" data-id="9716881"><a href="/opinion/2100000/commonwealth-v-yedinak/#1220" aria-description="Citation for case: Commonwealth v. Yedinak">676 A. 2d 1217, 1220, n. 5</a></span> (1996) ("The Pennsylvania Supreme Court recently held that the Pennsylvania Constitution provides greater protection than the United States Constitution with regard to automobile searches in <i>Commonwealth</i> v. <i>White</i> ").</p>
<p>The lower courts' understanding regarding the state-law nature of <i>White</i> and my understanding of the state-law nature of <i>Labron</i> as wellis almost perfectly reflected in the dissents to each case that were penned by Justice Castille. In both instances, Justice Castille recognizes, even more explicitly than the majority, that the decisions were based on state law.</p>
<p>In <i>Labron,</i> for instance, his main point was that the defendant had no standing to challenge the constitutionality of <span class="star-pagination">*946</span> the search of a car that he did not own. In making his argument, however, he noted that "the majority correctly characterizes <i>Pennsylvania law</i> regarding the `automobile exception' to the warrant requirement." 543 Pa., at 104, 669 A. 2d, at 926 (emphasis added). And although he reviewed decisions of this Court on standing to claim violations of the Fourth Amendment, he went on to note: "<i>Under Article I, Section 8 of the Pennsylvania Constitution,</i> however, this Court looks to several additional factors to determine whether a criminal defendant has standing to challenge the admission of evidence against him." <i>Id.,</i> at 106, 669 A. 2d, at 927 (emphasis added).</p>
<p>In <i>White,</i> Justice Castille stated that he believed that "the automobile exception to the warrant requirements of <i>this Commonwealth</i> should be a <i>per se</i> rule regardless of how much time police may have to obtain a warrant," 543 Pa., at 70, 669 A. 2d, at 909 (emphasis added), and he further concluded that he would "urge the adoption of a bright line rule that would allow warrantless searches of all automobiles for which police have independent probable cause," <i>id.,</i> at 71, 669 A. 2d, at 909-910. Of course, if Justice Castille were interpreting federal, rather than state, law, he would not have the luxury of "urging the adoption" of a particular rule.<sup>[5]</sup></p>
<p>Having reviewed the range of the Pennsylvania courts' statements regarding the source of the "exigent circumstances" rule, it is worthwhile to review this Court's understanding of when a state decision is based on adequate and independent state grounds. In <i>Michigan</i> v. <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span>,</i> the Court adopted a "plain statement" rule for determining whether a state decision rested on "independent and adequate" statelaw grounds. "[B]ecause of [our] respect for state courts, <span class="star-pagination">*947</span> and [a] desire to avoid advisory opinions, . . . we [did] not wish to continue to decide issues of state law that go beyond the opinion that we review, or to require state courts to reconsider cases to clarify the grounds of their decisions." <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long">463 U. S., at 1040</a></span>. When "a state court decision fairly appears to rest <i>primarily</i> on federal law, or to be interwoven with the federal law, and when the adequacy and independence of any possible state law ground is not clear from the face of the opinion," we held, we would conclude that the State decided as it did because federal law required it to do so. <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long"><i>Id.,</i>  at 1040-1041</a></span>.</p>
<p>Given the explicit and nearly exclusive references to state law that I review above, it seems to me that the Court's decision to take jurisdiction in <i>Labron</i> not only extends <i>Michigan</i> v. <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span></i> beyond its original scope, but stands its rationale on its head. <i>Labron</i> does not rest "primarily" on federal law; as Justice Castille understood it, as the briefing in <i>White</i> understood it, and as the Commonwealth's decision to stay out of <i>White</i> demonstrates, every indication is that the rule adopted in <i>Labron</i> and <i>White</i> rests primarily on state law. Nor are these holdings "interwoven" with federal law: Both <i>Labron</i> and <i>White</i> cite only two federal cases, both over a quarter-century old; rather than implicitly conclude that the absence of any reference to more recent decisions is due to poor legal research, I would trust the Pennsylvania courts' ability to understand and choose to deviate from our federal law. Certainly it would be a more respectful approach, in a case where the question is as close as it is in this case, to conclude that the State had made a conscious decision to depart from the jurisprudence of this Court rather than an error of law.<sup>[6]</sup></p>
<p><span class="star-pagination">*948</span> The nature of the Pennsylvania court's reliance on federal law in these cases, therefore, is quite different from that which spurred the Court to conclude in <i>Michigan</i> v. <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span></i>  that the judgment of the Michigan Supreme Court had not relied on adequate and independent state grounds. There, as the Court noted, the decision below "referred twice to the State Constitution in its opinion, but otherwise relied <i>exclusively</i> on federal law." <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1037" aria-description="Citation for case: Michigan v. Long">463 U. S., at 1037</a></span> (emphasis <span class="star-pagination">*949</span> added). The dissents below also relied explicitly and <i>exclusively</i> on decisions of this Court. <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1037" aria-description="Citation for case: Michigan v. Long"><i>Id.,</i> at 1037, n. 2</a></span>; <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#473" aria-description="Citation for case: People v. Long">413 Mich. 461, 473-486</a></span>, <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#870" aria-description="Citation for case: People v. Long">320 N. W. 2d 866, 870-875</a></span> (1982) (Coleman, C. J., dissenting, Moody, J., concurring in part and dissenting in part). Indeed, the critical holding of the Court was that the Michigan "Court of Appeals erroneously applied the principles of <i>Terry</i> v. <i>Ohio.</i> " <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#471" aria-description="Citation for case: People v. Long"><i>Id.,</i> at 471</a></span>, <span class="citation" data-id="9677713"><a href="/opinion/1752565/people-v-long/#869" aria-description="Citation for case: People v. Long">320 N. W. 2d, at 869</a></span> (citation omitted).<sup>[7]</sup> The opinion in these cases presents almost precisely the opposite situation: The decision refers to the Federal Constitution once, but otherwise relies <i>exclusively</i> on state law.</p>
<p>For these reasons, just as the decision in <i>White</i> would not merit summary reversal were it before this Court, the decision in <i>Labron</i> should not be summarily reversed. Although <i>Labron</i> and <i>White</i> both touch upon, and even place some historical reliance upon, federal search and seizure law, each also recognizes the broad interpretation that the Pennsylvania court has given its own constitutional prohibition against warrantless searches. I therefore seriously question <span class="star-pagination">*950</span> whether respect for the reasoning, independence, and resources of the Pennsylvania court will be advanced by today's decision.</p>
<p>While <i>Kilgore</i> relies more explicitly on the Federal Constitution than the other two decisions, it decided the identical issue that was decided in <i>Labron</i> and <i>White</i> only three days before those decisions issued. The reference to the Federal Constitution upon which the Court rests its jurisdiction only one of two references to federal lawmust be read in the context of the other two decisions, each of which relied heavily upon the Commonwealth's own Constitution. In light of <i>Labron</i> and <i>White,</i> the judgment in <i>Kilgore</i> will almost certainly remain the same on remand. In such a circumstance, the rationales supporting the rule of <i>Michigan</i>  v. <i>Long</i> simply do not support the decision to reverse. The petition in <i>Kilgore</i> should simply be denied.</p>
<p>On many prior occasions, I have noted the unfortunate effects of the rule of <i>Michigan</i> v. <i>Long.</i> See, <i>e. g., </i><i>Harris</i> v. <i>Reed,</i> <span class="citation" data-id="9431577"><a href="/opinion/112205/harris-v-reed/#266" aria-description="Citation for case: Harris v. Reed">489 U. S. 255, 266-267</a></span> (1989) (concurring opinion); <i>Delaware</i> v. <i>Van Arsdall,</i> <span class="citation" data-id="9430412"><a href="/opinion/111625/delaware-v-van-arsdall/#689" aria-description="Citation for case: Delaware v. Van Arsdall">475 U. S. 673, 689-708</a></span> (1986) (dissenting opinion); <i>Montana</i> v. <i>Hall,</i> <span class="citation" data-id="9430940"><a href="/opinion/111872/montana-v-hall/#411" aria-description="Citation for case: Montana v. Hall">481 U. S. 400, 411</a></span> (1987) <i>(per curiam)</i> (dissenting opinion); <i>Ponte</i> v. <i>Real,</i> <span class="citation" data-id="9430022"><a href="/opinion/111430/ponte-v-real/#501" aria-description="Citation for case: Ponte v. Real">471 U. S. 491, 501-503</a></span> (1985) (opinion concurring in part); see also <i>Arizona</i>  v. <i>Evans,</i> <span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#24" aria-description="Citation for case: Arizona v. Evans">514 U. S. 1, 24, 31-34</a></span> (1995) (Ginsburg, J., dissenting). Because the state-law ground supporting these judgments is so much clearer than has been true on most prior occasions, see n. 5, <i>supra,</i> these decisions exacerbate those effects to a nearly intolerable degree. Particularly in light of my understanding of this Court's primary role"to protect the rights of the individual that are embodied in the Federal Constitution," <i><span class="citation" data-id="9431577"><a href="/opinion/112205/harris-v-reed/" aria-description="Citation for case: Harris v. Reed">Harris</a></span>,</i> 489 U. S., at 267the decision to summarily reverse state decisions resting tenuously at best on federal grounds is imprudent and entirely inconsistent "with the sound administration of this Court's discretionary docket." <i>Ponte,</i> <span class="citation" data-id="9430022"><a href="/opinion/111430/ponte-v-real/#502" aria-description="Citation for case: Ponte v. Real">471 U. S., at 502-503</a></span>.</p>
<p><span class="star-pagination">*951</span> The Pennsylvania court has in these and other cases expressly indicated its intent to extend the protections of its Constitution beyond those available under the Federal Constitution, see, <i>e. g., </i><i>Commonwealth</i> v. <i>Edmunds,</i> <span class="citation" data-id="9752984"><a href="/opinion/2316698/commonwealth-v-edmunds/" aria-description="Citation for case: Commonwealth v. Edmunds">526 Pa. 374</a></span>, <span class="citation" data-id="9752984"><a href="/opinion/2316698/commonwealth-v-edmunds/" aria-description="Citation for case: Commonwealth v. Edmunds">586 A. 2d 887</a></span> (1991) (setting forth test for establishing rights under Pennsylvania Constitution); <i>Commonwealth</i> v. <i>Rosenfelt,</i> <span class="citation" data-id="9636411"><a href="/opinion/1473518/commonwealth-v-rosenfelt/#634" aria-description="Citation for case: Commonwealth v. Rosenfelt">443 Pa. Super. 616, 634-637</a></span>, <span class="citation" data-id="9636411"><a href="/opinion/1473518/commonwealth-v-rosenfelt/#1140" aria-description="Citation for case: Commonwealth v. Rosenfelt">662 A. 2d 1131, 1140-1141</a></span> (1995) (reviewing state cases extending greater protections under the Pennsylvania Constitution). The <i>per curiam</i> decision that the Court issues today merely makes that task harder by requiring the Commonwealth to purge its decisions of any reliance on the latter, despite the value of the insights that our decisions can provide on related issues of law. By "unceremoniously reversing its judgment," <i>Van Arsdall,</i> <span class="citation" data-id="9430412"><a href="/opinion/111625/delaware-v-van-arsdall/#701" aria-description="Citation for case: Delaware v. Van Arsdall">475 U. S., at 701</a></span> (Stevens, J., dissenting), we also demonstrate a lack of respect for the Pennsylvania court and the sophistication of its state search and seizure law. See <span class="citation" data-id="9430412"><a href="/opinion/111625/delaware-v-van-arsdall/#699" aria-description="Citation for case: Delaware v. Van Arsdall"><i>id.,</i> at 699</a></span>.</p>
<p>These harms are particularly unnecessary given the likely result on remand. To reinvigorate the privacy protections extended to Pennsylvania citizens under <i>Labron, Kilgore,</i>  and <i>White,</i> the Pennsylvania Supreme Court need only set forth the appropriate talismanic language and state, even more clearly than it already has, that the "<i>Commonwealth's</i>  jurisprudence of the automobile exception [requires] both the existence of probable cause and the presence of exigent circumstances to justify a warrantless search." <i>Labron,</i> <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#100" aria-description="Citation for case: Commonwealth v. Labron">543 Pa., at 100</a></span>, <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#924" aria-description="Citation for case: Commonwealth v. Labron">669 A. 2d, at 924</a></span> (emphasis added).<sup>[8]</sup> While the <span class="star-pagination">*952</span> result will be identical, resources and respect will have been unnecessarily lost.</p>
<p>I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]   Together with No. 95-1738, <i>Pennsylvania</i> v. <i>Kilgore,</i> also on petition for writ of certiorari to the same court.</p>
<p>[1]  Each decision was issued by a different division of the Pennsylvania Supreme Court.</p>
<p>[2]  Even if, as the Court concludes, <i>ante,</i> at 941, some element of residual doubt suggests that Pennsylvania's Supreme Court drew inspiration from our interpretations of the Federal Constitution, I do not think that reliance sufficient to justify expending this Court's timeor that of the Pennsylvania Supreme Courtsimply to scour the state decisions of all references to the Federal Constitution. See <i>infra,</i> at 943-950.</p>
<p>[3]  As the Pennsylvania Supreme Court noted, in <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span></i> we held that "`[f]or constitutional purposes, [there is] no difference between on the one hand seizing and holding a car before presenting the probable cause issue to a magistrate and on the other hand carrying out an immediate search without a warrant.' " <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#95" aria-description="Citation for case: Commonwealth v. Labron">543 Pa. 86, 95</a></span>, <span class="citation" data-id="9705192"><a href="/opinion/1984308/commonwealth-v-labron/#921" aria-description="Citation for case: Commonwealth v. Labron">669 A. 2d 917, 921</a></span> (1995) (quoting <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney">399 U. S., at 52</a></span>).</p>
<p>[4]  Although the court's main opinion in <i>Commonwealth</i> v.<i>White</i> also asked whether the search would have been permissible as a search incident to an arrest, the dissent later noted that the only question presented in the appeal was whether "exigent circumstances" were necessary to permit a warrantless search of a car based on probable cause. See 543 Pa., at 72-73, 669 A. 2d, at 910.</p>
<p>[5]  Justice Castille also specifically noted that the <i><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span></i> decision was not raised by the parties,and that the majority's discussion of it was dicta, further emphasizing that his emphasis on Pennsylvania law was related to the sole issue that he believed presented: whether a warrantless search of an automobile requires both probable cause and an exigent circumstance.</p>
<p>[6]  Indeed, the author of <i>Labron</i> noted in <i>White</i> that "the history of Article I, Section 8 and case-law interpreting it reveal a history of according a limited expectation of privacy in an automobile independently under the Pennsylvania Constitution. Therefore, the question before us today is not whether we wish to extend additional privacy protections to the Appellant but whether we wish to follow the United States Supreme Court and sharply curtail a privacy interest long recognized by this Court." <i>Commonwealth</i> v. <i>White,</i> <span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/#62" aria-description="Citation for case: Commonwealth v. White">543 Pa., at 62</a></span>, <span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/#905" aria-description="Citation for case: Commonwealth v. White">669 A. 2d, at 905</a></span>.
</p>
<p>To this end, I find it particularly interesting that only two Pennsylvania courts have cited the decision in <i>California</i> v. <i>Carney,</i> <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/" aria-description="Citation for case: California v. Carney">471 U. S. 386</a></span> (1985), upon which the <i>per curiam</i> decision relies as modern support for its interpretation of federal constitutional law. See <i>Commonwealth</i> v. <i>Rosenfelt,</i>  <span class="citation" data-id="9636411"><a href="/opinion/1473518/commonwealth-v-rosenfelt/#632" aria-description="Citation for case: Commonwealth v. Rosenfelt">443 Pa. Super. 616, 632-634</a></span>, <span class="citation" data-id="9636411"><a href="/opinion/1473518/commonwealth-v-rosenfelt/#1139" aria-description="Citation for case: Commonwealth v. Rosenfelt">662 A. 2d 1131, 1139</a></span> (1995); <i>Commonwealth</i>  v. <i>Camacho,</i> <span class="citation" data-id="1928985"><a href="/opinion/1928985/commonwealth-v-camacho/" aria-description="Citation for case: Commonwealth v. Camacho">425 Pa. Super. 567</a></span>, <span class="citation" data-id="1928985"><a href="/opinion/1928985/commonwealth-v-camacho/" aria-description="Citation for case: Commonwealth v. Camacho">625 A. 2d 1242</a></span> (1995). Each of those decisions expressly noted the presence of conflict between federal and state law on this issue.</p>
<p>In <i><span class="citation" data-id="1928985"><a href="/opinion/1928985/commonwealth-v-camacho/" aria-description="Citation for case: Commonwealth v. Camacho">Camacho</a></span>,</i> the Superior Court noted "the discrepancy between some of the Commonwealth's past cases and federal cases which speak to automobile searches" in cases like those at issue here. <span class="citation" data-id="1928985"><a href="/opinion/1928985/commonwealth-v-camacho/#576" aria-description="Citation for case: Commonwealth v. Camacho"><i>Id.,</i> at 576, n. 2</a></span>, <span class="citation" data-id="1928985"><a href="/opinion/1928985/commonwealth-v-camacho/#1247" aria-description="Citation for case: Commonwealth v. Camacho">625 A. 2d, at 1247, n. 2</a></span>. After reviewing the holding in <i><span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/" aria-description="Citation for case: California v. Carney">Carney</a></span>,</i> the court noted that the state cases concluding that there was no <i>per se</i> "`automobile exception' " were "simply dated and not in keeping with the tenor of current law." 425 Pa. Super., at 577, n. 2, <span class="citation" data-id="1928985"><a href="/opinion/1928985/commonwealth-v-camacho/#1247" aria-description="Citation for case: Commonwealth v. Camacho">625 A. 2d, at 1247, n. 2</a></span>.</p>
<p>The court in <i><span class="citation" data-id="9636411"><a href="/opinion/1473518/commonwealth-v-rosenfelt/" aria-description="Citation for case: Commonwealth v. Rosenfelt">Rosenfelt</a></span></i> reached an alternative explanation for the conflictand a result identical to that reached in the cases reversed by the Court today. There, the defendant agreed that the search of the vehicle was not illegal under federal law. Citing <i><span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/" aria-description="Citation for case: California v. Carney">Carney</a></span>,</i> the court noted that the federal "automobile exception" had "jettison[ed]" the requirement of exigency, essentially converting the exception into a <i>per se</i> rule allowing a search once probable cause exists. See 443 Pa. Super., at 633, 644-645, <span class="citation" data-id="9636411"><a href="/opinion/1473518/commonwealth-v-rosenfelt/#1139" aria-description="Citation for case: Commonwealth v. Rosenfelt">662 A. 2d, at 1139, 1145</a></span>. Noting that the State Constitution could extend greater protections to Pennsylvania citizens than did the Federal Constitution, but that its Supreme Court had not yet decided whether that was the case, the Superior Court went on to review the issue on its own and found a state constitutional violation. <i><span class="citation" data-id="9636411"><a href="/opinion/1473518/commonwealth-v-rosenfelt/" aria-description="Citation for case: Commonwealth v. Rosenfelt">Ibid.</a></span></i> After it decided the cases at issue here, the Pennsylvania Supreme Court denied the Commonwealth's appeal. See <span class="citation no-link">544 Pa. 605</span>, <span class="citation no-link">674 A. 2d 1070</span> (1996) (table).</p>
<p>[7]  On the many subsequent occasions in which this Court has taken jurisdiction over state decisions over which there was some dispute about the nature of the relationship between federal and state law, the state opinions were far more "interwoven" with federal law than is true in these cases. See, <i>e. g., </i><i>Illinois</i> v. <i>Rodriguez,</i> <span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/#182" aria-description="Citation for case: Illinois v. Rodriguez">497 U. S. 177, 182</a></span> (1990) (decision below did not "rely on (or even mention) any specific provision" of State Constitution); <i>Pennsylvania</i> v. <i>Muniz,</i> <span class="citation" data-id="9432075"><a href="/opinion/112464/pennsylvania-v-muniz/#588" aria-description="Citation for case: Pennsylvania v. Muniz">496 U. S. 582, 588, n. 4</a></span> (1990) (state constitutional provision construed to provide protections identical to Federal Constitution); <i>Florida</i> v. <i>Riley,</i> <span class="citation" data-id="9431518"><a href="/opinion/112175/florida-v-riley/#448" aria-description="Citation for case: Florida v. Riley">488 U. S. 445, 448, n. 1</a></span> (1989) (decision below mentioned State Constitution only twice, but "focused exclusively on federal cases dealing with the Fourth Amendment"); <i>Michigan</i> v. <i>Chesternut,</i>  <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#571" aria-description="Citation for case: Michigan v. Chesternut">486 U. S. 567, 571, n. 3</a></span> (1988) (decision below "said nothing to suggest that the Michigan Constitution's seizure provision provided an independent source of relief, and the court's entire analysis rested expressly on the Fourth Amendment and federal cases"); <i>Kentucky</i> v. <i>Stincer,</i> <span class="citation" data-id="9431052"><a href="/opinion/111928/kentucky-v-stincer/#735" aria-description="Citation for case: Kentucky v. Stincer">482 U. S. 730, 735, n. 7</a></span> (1987) (decision below "consistently referred to respondent's rights under the . . . Federal Constitution as supporting its ruling"); <i>Maryland</i> v. <i>Garrison,</i> <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#83" aria-description="Citation for case: Maryland v. Garrison">480 U. S. 79, 83-84</a></span> (1987) (State Constitution construed <i>in pari materia</i> with Federal Constitution).</p>
<p>[8]  State courts have, of course, done this on many occasions in the past. See, <i>e. g., </i><i>Ponte</i> v. <i>Real,</i> <span class="citation" data-id="9430022"><a href="/opinion/111430/ponte-v-real/#503" aria-description="Citation for case: Ponte v. Real">471 U. S. 491, 503, n. 4</a></span> (1985) (Stevens, J., concurring in part) (listing various cases in which reversals by this Court were followed by state-court decisions affirming the original holding on statelaw grounds); <i>Montana</i> v. <i>Hall,</i> <span class="citation" data-id="9430940"><a href="/opinion/111872/montana-v-hall/#411" aria-description="Citation for case: Montana v. Hall">481 U. S. 400, 411</a></span> (1987) <i>(per curiam)</i>  (Stevens, J., dissenting) (same).</p>

</div>
```

---
