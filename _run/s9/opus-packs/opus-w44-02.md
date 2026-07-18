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

## GROUP: content/cases/Hudson v. Michigan.md  (`case`, 5 assertions)

### content_page

```
---
title: "Hudson v. Michigan"
type: case
citation: "547 U.S. 586 (2006)"
parallel_cite: "126 S. Ct. 2159; 165 L. Ed. 2d 56"
neutral_cite: 2006 U.S. LEXIS 4677
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2006
date_decided: 2006-06-15
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2006-06-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hudson v. Michigan
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145646/hudson-v-michigan/"
  cluster_id: 145646
  opinion_id: 145646
  identity_checked: true
homes:
  - page: "[[Knock-and-Announce]]"
    role: "Key — Progeny / Refinement"
related: ["[[Wilson v. Arkansas]]", "[[Richards v. Wisconsin]]", "[[Mapp v. Ohio]]", "[[United States v. Leon]]"]
aliases: []
tags: ["case", "fourth-amendment", "knock-and-announce", "exclusionary-rule", "warrant"]
holding: "A knock-and-announce violation does NOT require suppression of the evidence found inside; the interests protected by knock-and-announce…"
lake:
  record_id: Hudson v. Michigan
  status: verified
  projected_at: 2026-07-06
---

# Hudson v. Michigan

*547 U.S. 586 (2006)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police executing a valid search warrant at Hudson's home announced their presence but waited only a short time — about three to five seconds — before entering. They found drugs and a firearm. Hudson moved to suppress, arguing the premature entry violated the Fourth Amendment's [[Knock-and-Announce|knock-and-announce]] requirement.

## Issue
Whether a violation of the [[Knock-and-Announce|knock-and-announce]] rule requires suppression of the evidence found in the ensuing search.

## Rule
No. The interests protected by the [[Knock-and-Announce|knock-and-announce]] rule are not the interests served by suppression. "What the knock-and-announce rule has never protected, however, is one's interest in preventing the government from seeing or taking evidence described in a warrant." — 547 U.S. at 594. ^pin-594

"Since the interests that were violated in this case have nothing to do with the seizure of the evidence, the exclusionary rule is inapplicable." — *Id.* ^pin-594a

## Application
The police had a valid warrant and would have discovered and seized the drugs and firearm regardless of how long they waited at the door; the [[Knock-and-Announce|knock-and-announce]] violation protected only interests in privacy, dignity, and avoiding property damage — not Hudson's interest in keeping the police from finding the described evidence. Because suppression would not vindicate the interests the rule protects and its deterrence benefits did not outweigh its substantial social costs, the evidence was not suppressed.

## Conclusion
A [[Knock-and-Announce|knock-and-announce]] violation does not trigger the exclusionary rule; the denial of suppression was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Hudson* leaves the [[Knock-and-Announce|knock-and-announce]] requirement of [[Wilson v. Arkansas]] and [[Richards v. Wisconsin]] intact but withholds the exclusionary remedy for its violation, applying the cost-benefit, deterrence-focused approach of the modern exclusionary-rule cases.

## Appears on
- [[Knock-and-Announce]] — *Key — Progeny / Refinement*

## Sources
- *Hudson v. Michigan*, 547 U.S. 586 (2006) — https://www.courtlistener.com/opinion/145646/hudson-v-michigan/ — pinpoint: 594.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8ad90546fe31f68b", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "547 U.S. 586 (2006)", "court": "U.S. Supreme Court", "neutral_cite": "2006 U.S. LEXIS 4677", "official_citation_present": true, "parallel_cite": "126 S. Ct. 2159; 165 L. Ed. 2d 56", "title": "Hudson v. Michigan", "year": "2006"}}
{"assertion_id": "4bbc36484be8974d", "dimension": "support", "kind": "home_role", "locator": {"home": "Knock-and-Announce"}, "payload": {"home": "Knock-and-Announce", "role": "Key — Progeny / Refinement", "title": "Hudson v. Michigan"}}
{"assertion_id": "611085ecaa07d62c", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A knock-and-announce violation does NOT require suppression of the evidence found inside; the interests protected by knock-and-announce…", "title": "Hudson v. Michigan"}}
{"assertion_id": "7864cc9c8b19ba57", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Hudson v. Michigan"}}
{"assertion_id": "ad01324ddf3a0143", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2006-06-15", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Hudson v. Michigan", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Hudson v. Michigan", "varies_by_point": "false"}}
```

### lake record — Hudson v. Michigan

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hudson v. Michigan",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hudson v. Michigan",
    "case_name_short": "Hudson",
    "case_name_full": "Hudson v. Michigan",
    "input_case_name": "Hudson v. Michigan",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2006-06-15",
    "year": 2006,
    "docket": null,
    "cluster_id": 145646,
    "lead_opinion_id": 145646,
    "sibling_ids": [
      145646,
      9434934,
      9434935,
      9434936
    ],
    "absolute_url": "/opinion/145646/hudson-v-michigan/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "547 U.S. 586",
      "volume": "547",
      "reporter": "U.S.",
      "page": "586",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "126 S. Ct. 2159",
        "volume": "126",
        "reporter": "S. Ct.",
        "page": "2159",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "165 L. Ed. 2d 56",
        "volume": "165",
        "reporter": "L. Ed. 2d",
        "page": "56",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2006 U.S. LEXIS 4677",
        "volume": "2006",
        "reporter": "U.S. LEXIS",
        "page": "4677",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "547 U.S. 586",
        "volume": "547",
        "reporter": "U.S.",
        "page": "586",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "126 S. Ct. 2159",
        "volume": "126",
        "reporter": "S. Ct.",
        "page": "2159",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "165 L. Ed. 2d 56",
        "volume": "165",
        "reporter": "L. Ed. 2d",
        "page": "56",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2006 U.S. LEXIS 4677",
        "volume": "2006",
        "reporter": "U.S. LEXIS",
        "page": "4677",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "547 U.S. 586",
    "official_selection": {
      "court_class": "scotus",
      "selected": "547 U.S. 586",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-594",
      "page": null,
      "quote": "--- # Hudson v. Michigan *547 U.S. 586 (2006)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police executing a valid search warrant at Hudson's home announced their presence but waited only a short time \u2014 about three to five seconds \u2014 before entering. They found drugs and a firearm. Hudson moved to suppress, arguing the premature entry violated the Fourth Amendment's knock-and-announce requirement. ## Issue Whether a violation of the knock-and-announce rule requires suppression of the evidence found in the ensuing search. ## Rule No. The interests protected by the knock-and-announce rule are not the interests served by suppression.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-594a",
      "page": null,
      "quote": "Since the interests that were violated in this case have nothing to do with the seizure of the evidence, the exclusionary rule is inapplicable.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2006-06-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hudson v. Michigan",
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
        "journal_ref": "Hudson v. Michigan:lane1_negative"
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
        "journal_ref": "Hudson v. Michigan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Christian",
          "cluster_id": 4643309,
          "cite": [
            "445 P.3d 183"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Sasiadek",
          "cluster_id": 7330153,
          "cite": [
            "310 F. Supp. 3d 371"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gomez",
          "cluster_id": 8443636,
          "cite": [
            "877 F.3d 76"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane1_negative"
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
        "journal_ref": "Hudson v. Michigan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Matthew Elliot Cohagan",
          "cluster_id": 4421478,
          "cite": [
            "162 Idaho 717",
            "404 P.3d 659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Brown",
          "cluster_id": 4316369,
          "cite": [
            "2016 COA 150",
            "417 P.3d 868"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Johnny James Tims v. State of Florida",
          "cluster_id": 4302086,
          "cite": [
            "204 So. 3d 536",
            "2016 Fla. App. LEXIS 14742"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Lajai Pridgette",
          "cluster_id": 4244999,
          "cite": [
            "831 F.3d 1253",
            "2016 U.S. App. LEXIS 14408",
            "2016 WL 4151222"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "McDonald v. City of Chicago",
          "cluster_id": 149702,
          "cite": [
            "177 L. Ed. 2d 894",
            "130 S. Ct. 3020",
            "561 U.S. 742",
            "2010 U.S. LEXIS 5523",
            "22 Fla. L. Weekly Fed. S 619",
            "78 U.S.L.W. 4844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Corley v. United States",
          "cluster_id": 145888,
          "cite": [
            "173 L. Ed. 2d 443",
            "129 S. Ct. 1558",
            "556 U.S. 303",
            "2009 U.S. LEXIS 2512"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. State",
          "cluster_id": 2106367,
          "cite": [
            "311 S.W.3d 452",
            "2010 Tex. Crim. App. LEXIS 685",
            "2010 WL 715253"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Terebesi v. Torreso",
          "cluster_id": 8441937,
          "cite": [
            "764 F.3d 217",
            "2014 U.S. App. LEXIS 16133",
            "2014 WL 4099309"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Price v. Sery",
          "cluster_id": 1272546,
          "cite": [
            "513 F.3d 962",
            "2008 U.S. App. LEXIS 1196",
            "2008 WL 170205"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Fayed",
          "cluster_id": 4741522,
          "cite": [
            "9 Cal. 5th 147",
            "260 Cal. Rptr. 3d 761",
            "460 P.3d 1149"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Justin Barrett Hill",
          "cluster_id": 795398,
          "cite": [
            "459 F.3d 966",
            "2006 U.S. App. LEXIS 20584",
            "2006 WL 2328721"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Frazier",
          "cluster_id": 842682,
          "cite": [
            "733 N.W.2d 713",
            "478 Mich. 231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Anstey",
          "cluster_id": 845579,
          "cite": [
            "719 N.W.2d 579",
            "476 Mich. 436"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ernest Edgar Black Jeff Wigington",
          "cluster_id": 3171438,
          "cite": [
            "811 F.3d 1259",
            "2016 U.S. App. LEXIS 1057",
            "2016 WL 278918"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Johnston",
          "cluster_id": 2276813,
          "cite": [
            "336 S.W.3d 649",
            "2011 Tex. Crim. App. LEXIS 388",
            "2011 WL 891324"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Reyes Fabian Olivera-Mendez",
          "cluster_id": 797553,
          "cite": [
            "484 F.3d 505",
            "2007 U.S. App. LEXIS 10492",
            "2007 WL 1296781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Michigan:lane2_top_cited"
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
        "journal_ref": "Hudson v. Michigan:lane3_recency"
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
        "journal_ref": "Hudson v. Michigan:lane3_recency"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145646 OR 9434934 OR 9434935 OR 9434936) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDY2MzgwODAwMDAwJnM9MzIxNDg4MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145646+OR+9434934+OR+9434935+OR+9434936%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 10,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 10,
        "triage_snippet_classified": 190
      },
      "lane2_top_cited": {
        "query": "cites:(145646 OR 9434934 OR 9434935 OR 9434936)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTAmcz04NDQzNjM2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28145646+OR+9434934+OR+9434935+OR+9434936%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145646 OR 9434934 OR 9434935 OR 9434936)",
        "reviewed": 52,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 52,
        "triage_read": 4,
        "triage_snippet_classified": 48
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145646 OR 9434934 OR 9434935 OR 9434936)",
    "indexed_citing_opinions": 714,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145646,
        "count": 582,
        "count_source": "search"
      },
      {
        "opinion_id": 9434934,
        "count": 143,
        "count_source": "search"
      },
      {
        "opinion_id": 9434935,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434936,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1223,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hudson-v-michigan.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwNDMzMDUmcz0xMDE2MDgzNSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145646+OR+9434934+OR+9434935+OR+9434936%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145646,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 101156,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 101963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 107102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 107225,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 107718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 107800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 107981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 107982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109572,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 109925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 110317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 111259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 111265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 111779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 111834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 112136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 112209,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 112350,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 112413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 112416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 112454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 117905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 118103,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 118180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 118235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 118380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 118466,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 121167,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 121169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 127919,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 131146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 161659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 770457,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 791612,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 793669,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 1237532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 1693561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 1854815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145646,
        "cited_id": 1934151,
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
    "date_created": "2026-07-05T07:37:58Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:38:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:38:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:43:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:38:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hudson v. Michigan

```
(Slip Opinion)              OCTOBER TERM, 2005                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                         HUDSON v. MICHIGAN

     CERTIORARI TO THE COURT OF APPEALS OF MICHIGAN

  No. 04–1360. Argued January 9, 2006—Reargued May 18, 2006—

                     Decided June 15, 2006 

Detroit police executing a search warrant for narcotics and weapons
 entered petitioner Hudson’s home in violation of the Fourth Amend
 ment’s “knock-and-announce” rule. The trial court granted Hudson’s
 motion to suppress the evidence seized, but the Michigan Court of
 Appeals reversed on interlocutory appeal. Hudson was convicted of
 drug possession. Affirming, the State Court of Appeals rejected Hud
 son’s renewed Fourth Amendment claim.
Held: The judgment is affirmed.
Affirmed.
     JUSTICE SCALIA delivered the opinion of the Court with respect to
  Parts I, II, and III, concluding that violation of the “knock-and
  announce” rule does not require suppression of evidence found in a
  search. Pp. 2–13.
     (a) Because Michigan has conceded that the entry here was a
  knock-and-announce violation, the only issue is whether the exclu
  sionary rule is appropriate for such a violation. Pp. 2–3.
     (b) This Court has rejected “[i]ndiscriminate application” of the ex
  clusionary rule, United States v. Leon, 468 U. S. 897, 908, holding it
  applicable only “where its deterrence benefits outweigh its ‘substan
  tial social costs,’ ” Pennsylvania Bd. of Probation and Parole v. Scott,
  524 U. S. 357, 363. Exclusion may not be premised on the mere fact
  that a constitutional violation was a “but-for” cause of obtaining the
  evidence. The illegal entry here was not the but-for cause, but even if
  it were, but-for causation can be too attenuated to justify exclusion.
  Attenuation can occur not only when the causal connection is remote,
  but also when suppression would not serve the interest protected by
  the constitutional guarantee violated. The interests protected by the
  knock-and-announce rule include human life and limb (because an
2                        HUDSON v. MICHIGAN

                                 Syllabus

    unannounced entry may provoke violence from a surprised resident),
    property (because citizens presumably would open the door upon an
    announcement, whereas a forcible entry may destroy it), and privacy
    and dignity of the sort that can be offended by a sudden entrance.
    But the rule has never protected one’s interest in preventing the gov
    ernment from seeing or taking evidence described in a warrant.
    Since the interests violated here have nothing to do with the seizure
    of the evidence, the exclusionary rule is inapplicable. Pp. 3–7.
       (c) The social costs to be weighed against deterrence are consider
    able here. In addition to the grave adverse consequence that exclud
    ing relevant incriminating evidence always entails—the risk of re
    leasing dangerous criminals—imposing such a massive remedy would
    generate a constant flood of alleged failures to observe the rule, and
    claims that any asserted justification for a no-knock entry had inade
    quate support. Another consequence would be police officers’ refrain
    ing from timely entry after knocking and announcing, producing pre
    ventable violence against the officers in some cases, and the
    destruction of evidence in others. Next to these social costs are the
    deterrence benefits. The value of deterrence depends on the strength
    of the incentive to commit the forbidden act. That incentive is mini
    mal here, where ignoring knock-and-announce can realistically be
    expected to achieve nothing but the prevention of evidence destruc
    tion and avoidance of life-threatening resistance, dangers which sus
    pend the requirement when there is “reasonable suspicion” that they
    exist, Richards v. Wisconsin, 520 U. S. 385, 394. Massive deterrence
    is hardly necessary. Contrary to Hudson’s argument that without
    suppression there will be no deterrence, many forms of police mis
    conduct are deterred by civil-rights suits, and by the consequences of
    increasing professionalism of police forces, including a new emphasis
    on internal police discipline. Pp. 8–13.
       JUSTICE SCALIA, joined by THE CHIEF JUSTICE, JUSTICE THOMAS, and
    JUSTICE ALITO, concluded in Part IV that Segura v. United States, 468
    U. S. 796, New York v. Harris, 495 U. S. 14, and United States v.
    Ramirez, 523 U. S. 65, confirm the conclusion that suppression is
    unwarranted in this case. Pp. 13–16.

   SCALIA, J., delivered the opinion of the Court with respect to Parts I,
II, and III, in which ROBERTS, C. J., and KENNEDY, THOMAS, and ALITO,
JJ., joined, and an opinion with respect to Part IV, in which ROBERTS,
C. J., and THOMAS and ALITO, JJ., joined. KENNEDY, J., filed an opinion
concurring in part and concurring in the judgment. BREYER, J., filed a
dissenting opinion, in which STEVENS, SOUTER, and GINSBURG, JJ.,
joined.
                       Cite as: 547 U. S. ____ (2006)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 04–1360
                                  _________________


BOOKER T. HUDSON, JR., PETITIONER v. MICHIGAN
  ON WRIT OF CERTIORARI TO THE COURT OF APPEALS OF 

                     MICHIGAN

                                [June 15, 2006] 


  JUSTICE SCALIA delivered the opinion of the Court,
except as to Part IV.
  We decide whether violation of the “knock-and
announce” rule requires the suppression of all evidence
found in the search.
                             I
  Police obtained a warrant authorizing a search for drugs
and firearms at the home of petitioner Booker Hudson.
They discovered both. Large quantities of drugs were
found, including cocaine rocks in Hudson’s pocket. A
loaded gun was lodged between the cushion and armrest of
the chair in which he was sitting. Hudson was charged
under Michigan law with unlawful drug and firearm
possession.
  This case is before us only because of the method of
entry into the house. When the police arrived to execute
the warrant, they announced their presence, but waited
only a short time—perhaps “three to five seconds,” App.
15—before turning the knob of the unlocked front door
and entering Hudson’s home. Hudson moved to suppress
all the inculpatory evidence, arguing that the premature
entry violated his Fourth Amendment rights.
2                   HUDSON v. MICHIGAN

                      Opinion of the Court

  The Michigan trial court granted his motion. On inter
locutory review, the Michigan Court of Appeals reversed,
relying on Michigan Supreme Court cases holding that
suppression is inappropriate when entry is made pursuant
to warrant but without proper “ ‘knock and announce.’ ”
App. to Pet. for Cert. 4 (citing People v. Vasquez, 461 Mich.
235, 602 N. W. 2d 376 (1999) (per curiam); People v. Ste
vens, 460 Mich. 626, 597 N. W. 2d 53 (1999)). The Michi
gan Supreme Court denied leave to appeal. 465 Mich.
932, 639 N. E. 2d 255 (2001). Hudson was convicted of
drug possession. He renewed his Fourth Amendment
claim on appeal, but the Court of Appeals rejected it and
affirmed the conviction. App. to Pet. for Cert. 1–2. The
Michigan Supreme Court again declined review. 472
Mich. 862, 692 N. W. 2d 385 (2005). We granted certio
rari. 545 U. S. ___ (2005).
                              II
  The common-law principle that law enforcement officers
must announce their presence and provide residents an
opportunity to open the door is an ancient one. See Wilson
v. Arkansas, 514 U. S. 927, 931–932 (1995). Since 1917,
when Congress passed the Espionage Act, this traditional
protection has been part of federal statutory law, see 40
Stat. 229, and is currently codified at 18 U. S. C. §3109. We
applied that statute in Miller v. United States, 357 U. S. 301
(1958), and again in Sabbath v. United States, 391 U. S. 585
(1968). Finally, in Wilson, we were asked whether the rule
was also a command of the Fourth Amendment. Tracing its
origins in our English legal heritage, 514 U. S., at 931–936,
we concluded that it was.
  We recognized that the new constitutional rule we had
announced is not easily applied. Wilson and cases follow
ing it have noted the many situations in which it is not
necessary to knock and announce. It is not necessary
when “circumstances presen[t] a threat of physical vio
                  Cite as: 547 U. S. ____ (2006)             3

                      Opinion of the Court

lence,” or if there is “reason to believe that evidence would
likely be destroyed if advance notice were given,” id., at
936, or if knocking and announcing would be “futile,”
Richards v. Wisconsin, 520 U. S. 385, 394 (1997). We re
quire only that police “have a reasonable suspicion . . . under
the particular circumstances” that one of these grounds for
failing to knock and announce exists, and we have acknowl
edged that “[t]his showing is not high.” Ibid.
   When the knock-and-announce rule does apply, it is not
easy to determine precisely what officers must do. How
many seconds’ wait are too few? Our “reasonable wait time”
standard, see United States v. Banks, 540 U. S. 31, 41
(2003), is necessarily vague. Banks (a drug case, like this
one) held that the proper measure was not how long it
would take the resident to reach the door, but how long it
would take to dispose of the suspected drugs—but that such
a time (15 to 20 seconds in that case) would necessarily be
extended when, for instance, the suspected contraband was
not easily concealed. Id., at 40–41. If our ex post evaluation
is subject to such calculations, it is unsurprising that, ex
ante, police officers about to encounter someone who may
try to harm them will be uncertain how long to wait.
   Happily, these issues do not confront us here. From the
trial level onward, Michigan has conceded that the entry
was a knock-and-announce violation. The issue here is
remedy. Wilson specifically declined to decide whether the
exclusionary rule is appropriate for violation of the knock-
and-announce requirement. 514 U. S., at 937, n. 4. That
question is squarely before us now.
                            III 

                             A

   In Weeks v. United States, 232 U. S. 383 (1914), we
adopted the federal exclusionary rule for evidence that was
unlawfully seized from a home without a warrant in viola
tion of the Fourth Amendment. We began applying the
4                   HUDSON v. MICHIGAN

                      Opinion of the Court

same rule to the States, through the Fourteenth Amend
ment, in Mapp v. Ohio, 367 U. S. 643 (1961).
   Suppression of evidence, however, has always been our
last resort, not our first impulse. The exclusionary rule
generates “substantial social costs,” United States v. Leon,
468 U. S. 897, 907 (1984), which sometimes include setting
the guilty free and the dangerous at large. We have there
fore been “cautio[us] against expanding” it, Colorado v.
Connelly, 479 U. S. 157, 166 (1986), and “have repeatedly
emphasized that the rule’s ‘costly toll’ upon truth-seeking
and law enforcement objectives presents a high obstacle
for those urging [its] application,” Pennsylvania Bd. of
Probation and Parole v. Scott, 524 U. S. 357, 364–365
(1998) (citation omitted). We have rejected “[i]ndiscrimi
nate application” of the rule, Leon, supra, at 908, and have
held it to be applicable only “where its remedial objectives
are thought most efficaciously served,” United States v.
Calandra, 414 U. S. 338, 348 (1974)—that is, “where its
deterrence benefits outweigh its ‘substantial social costs,’ ”
Scott, supra, at 363 (quoting Leon, supra, at 907).
   We did not always speak so guardedly. Expansive dicta
in Mapp, for example, suggested wide scope for the exclu
sionary rule. See, e.g., 367 U. S., at 655 (“[A]ll evidence
obtained by searches and seizures in violation of the Con
stitution is, by that same authority, inadmissible in a
state court”). Whiteley v. Warden, Wyo. State Penitentiary,
401 U. S. 560, 568–569 (1971), was to the same effect. But
we have long since rejected that approach. As explained
in Arizona v. Evans, 514 U. S. 1, 13 (1995): “In Whiteley,
the Court treated identification of a Fourth Amendment
violation as synonymous with application of the exclusion
ary rule to evidence secured incident to that violation.
Subsequent case law has rejected this reflexive application
of the exclusionary rule.” (Citation omitted.) We had said
as much in Leon, a decade earlier, when we explained that
“[w]hether the exclusionary sanction is appropriately
                  Cite as: 547 U. S. ____ (2006)            5

                      Opinion of the Court

imposed in a particular case, . . . is ‘an issue separate from
the question whether the Fourth Amendment rights of the
party seeking to invoke the rule were violated by police
conduct.’ ” 468 U. S., at 906 (quoting Illinois v. Gates, 462
U. S. 213, 223 (1983)).
   In other words, exclusion may not be premised on the
mere fact that a constitutional violation was a “but-for”
cause of obtaining evidence. Our cases show that but-for
causality is only a necessary, not a sufficient, condition for
suppression. In this case, of course, the constitutional
violation of an illegal manner of entry was not a but-for
cause of obtaining the evidence. Whether that prelimi
nary misstep had occurred or not, the police would have
executed the warrant they had obtained, and would have
discovered the gun and drugs inside the house. But even
if the illegal entry here could be characterized as a but-for
cause of discovering what was inside, we have “never held
that evidence is ‘fruit of the poisonous tree’ simply because
‘it would not have come to light but for the illegal actions
of the police.’ ” Segura v. United States, 468 U. S. 796, 815
(1984). See also id., at 829 (STEVENS, J., dissenting) (“We
have not . . . mechanically applied the [exclusionary] rule to
every item of evidence that has a causal connection with
police misconduct”). Rather, but-for cause, or “causation in
the logical sense alone,” United States v. Ceccolini, 435
U. S. 268, 274 (1978), can be too attenuated to justify exclu
sion, id., at 274–275. Even in the early days of the exclu
sionary rule, we declined to
    “hold that all evidence is ‘fruit of the poisonous tree’
    simply because it would not have come to light but for
    the illegal actions of the police. Rather, the more apt
    question in such a case is ‘whether, granting estab
    lishment of the primary illegality, the evidence to
    which instant objection is made has been come at by
    exploitation of that illegality or instead by means suf
6                  HUDSON v. MICHIGAN

                     Opinion of the Court

    ficiently distinguishable to be purged of the primary
    taint.’ ” Wong Sun v. United States, 371 U. S. 471, 487–
    488 (1963) (quoting J. Maguire, Evidence of Guilt 221
    (1959) (emphasis added)).
   Attenuation can occur, of course, when the causal con
nection is remote. See, e.g., Nardone v. United States, 308
U. S. 338, 341 (1939). Attenuation also occurs when, even
given a direct causal connection, the interest protected by
the constitutional guarantee that has been violated would
not be served by suppression of the evidence obtained.
“The penalties visited upon the Government, and in turn
upon the public, because its officers have violated the law
must bear some relation to the purposes which the law is
to serve.” Ceccolini, supra, at 279. Thus, in New York v.
Harris, 495 U. S. 14 (1990), where an illegal warrantless
arrest was made in Harris’ house, we held that
    “suppressing [Harris’] statement taken outside the
    house would not serve the purpose of the rule that
    made Harris’ in-house arrest illegal. The warrant re
    quirement for an arrest in the home is imposed to pro
    tect the home, and anything incriminating the police
    gathered from arresting Harris in his home, rather
    than elsewhere, has been excluded, as it should have
    been; the purpose of the rule has thereby been vindi
    cated.” Id., at 20.
For this reason, cases excluding the fruits of unlawful
warrantless searches, see, e.g., Boyd v. United States, 116
U. S. 616 (1886); Weeks, 232 U. S. 383; Silverthorne Lumber
Co. v. United States, 251 U. S. 385 (1920); Mapp, supra, say
nothing about the appropriateness of exclusion to vindi
cate the interests protected by the knock-and-announce
requirement. Until a valid warrant has issued, citizens
are entitled to shield “their persons, houses, papers, and
effects,” U. S. Const., Amdt. 4, from the government’s
scrutiny. Exclusion of the evidence obtained by a war
                 Cite as: 547 U. S. ____ (2006)           7

                     Opinion of the Court

rantless search vindicates that entitlement. The interests
protected by the knock-and-announce requirement are
quite different—and do not include the shielding of poten
tial evidence from the government’s eyes.
   One of those interests is the protection of human life
and limb, because an unannounced entry may provoke
violence in supposed self-defense by the surprised resi
dent. See, e.g., McDonald v. United States, 335 U. S. 451,
460–461 (1948) (Jackson, J., concurring). See also Sabbath,
391 U. S., at 589; Miller, 357 U. S., at 313, n. 12. Another
interest is the protection of property. Breaking a house (as
the old cases typically put it) absent an announcement
would penalize someone who “ ‘did not know of the process,
of which, if he had notice, it is to be presumed that he
would obey it . . . .’ ” Wilson, 514 U. S., at 931–932 (quot
ing Semayne’s Case, 5 Co. Rep. 91a, 91b, 77 Eng. Rep. 194,
195–196 (K. B. 1603)). The knock-and-announce rule gives
individuals “the opportunity to comply with the law and to
avoid the destruction of property occasioned by a forcible
entry.” Richards, 520 U. S., at 393, n. 5. See also Banks,
540 U. S., at 41. And thirdly, the knock-and-announce rule
protects those elements of privacy and dignity that can be
destroyed by a sudden entrance. It gives residents the
“opportunity to prepare themselves for” the entry of the
police. Richards, 520 U. S., at 393, n. 5. “The brief inter
lude between announcement and entry with a warrant
may be the opportunity that an individual has to pull on
clothes or get out of bed.” Ibid. In other words, it assures
the opportunity to collect oneself before answering the
door.
   What the knock-and-announce rule has never protected,
however, is one’s interest in preventing the government
from seeing or taking evidence described in a warrant.
Since the interests that were violated in this case have
nothing to do with the seizure of the evidence, the exclu
sionary rule is inapplicable.
8                  HUDSON v. MICHIGAN

                     Opinion of the Court

                               B
  Quite apart from the requirement of unattenuated
causation, the exclusionary rule has never been applied
except “where its deterrence benefits outweigh its ‘sub
stantial social costs,’ ” Scott, 524 U. S., at 363 (quoting
Leon, 468 U. S., at 907). The costs here are considerable.
In addition to the grave adverse consequence that exclu
sion of relevant incriminating evidence always entails
(viz., the risk of releasing dangerous criminals into soci
ety), imposing that massive remedy for a knock-and
announce violation would generate a constant flood of
alleged failures to observe the rule, and claims that any
asserted Richards justification for a no-knock entry, see
520 U. S., at 394, had inadequate support. Cf. United
States v. Singleton, 441 F. 3d 290, 293–294 (CA4 2006).
The cost of entering this lottery would be small, but the
jackpot enormous: suppression of all evidence, amounting
in many cases to a get-out-of-jail-free card. Courts would
experience as never before the reality that “[t]he exclu
sionary rule frequently requires extensive litigation to
determine whether particular evidence must be excluded.”
Scott, supra, at 366. Unlike the warrant or Miranda
requirements, compliance with which is readily deter
mined (either there was or was not a warrant; either the
Miranda warning was given, or it was not), what consti
tuted a “reasonable wait time” in a particular case, Banks,
supra, at 41 (or, for that matter, how many seconds the
police in fact waited), or whether there was “reasonable
suspicion” of the sort that would invoke the Richards
exceptions, is difficult for the trial court to determine and
even more difficult for an appellate court to review.
  Another consequence of the incongruent remedy Hudson
proposes would be police officers’ refraining from timely
entry after knocking and announcing. As we have ob
served, see supra, at 3, the amount of time they must wait
is necessarily uncertain. If the consequences of running
                  Cite as: 547 U. S. ____ (2006)             9

                      Opinion of the Court

afoul of the rule were so massive, officers would be in
clined to wait longer than the law requires—producing
preventable violence against officers in some cases, and
the destruction of evidence in many others. See Gates, 462
U. S., at 258. We deemed these consequences severe
enough to produce our unanimous agreement that a mere
“reasonable suspicion” that knocking and announcing
“under the particular circumstances, would be dangerous
or futile, or that it would inhibit the effective investigation
of the crime,” will cause the requirement to yield. Rich
ards, supra, at 394.
   Next to these “substantial social costs” we must consider
the deterrence benefits, existence of which is a necessary
condition for exclusion. (It is not, of course, a sufficient
condition: “[I]t does not follow that the Fourth Amend
ment requires adoption of every proposal that might deter
police misconduct.” Calandra, 414 U. S., at 350; see also
Leon, supra, at 910.) To begin with, the value of deter
rence depends upon the strength of the incentive to com
mit the forbidden act. Viewed from this perspective,
deterrence of knock-and-announce violations is not worth
a lot. Violation of the warrant requirement sometimes
produces incriminating evidence that could not otherwise
be obtained. But ignoring knock-and-announce can realis
tically be expected to achieve absolutely nothing except
the prevention of destruction of evidence and the avoid
ance of life-threatening resistance by occupants of the
premises—dangers which, if there is even “reasonable
suspicion” of their existence, suspend the knock-and
announce requirement anyway. Massive deterrence is
hardly required.
   It seems to us not even true, as Hudson contends, that
without suppression there will be no deterrence of knock-
and-announce violations at all. Of course even if this
assertion were accurate, it would not necessarily justify
suppression. Assuming (as the assertion must) that civil
10                 HUDSON v. MICHIGAN

                     Opinion of the Court

suit is not an effective deterrent, one can think of many
forms of police misconduct that are similarly “undeterred.”
When, for example, a confessed suspect in the killing of a
police officer, arrested (along with incriminating evidence)
in a lawful warranted search, is subjected to physical
abuse at the station house, would it seriously be suggested
that the evidence must be excluded, since that is the only
“effective deterrent”? And what, other than civil suit, is
the “effective deterrent” of police violation of an already-
confessed suspect’s Sixth Amendment rights by denying
him prompt access to counsel? Many would regard these
violated rights as more significant than the right not to be
intruded upon in one’s nightclothes—and yet nothing but
“ineffective” civil suit is available as a deterrent. And the
police incentive for those violations is arguably greater
than the incentive for disregarding the knock-and
announce rule.
  We cannot assume that exclusion in this context is
necessary deterrence simply because we found that it was
necessary deterrence in different contexts and long ago.
That would be forcing the public today to pay for the sins
and inadequacies of a legal regime that existed almost half
a century ago. Dollree Mapp could not turn to 42 U. S. C.
§1983 for meaningful relief; Monroe v. Pape, 365 U. S. 167
(1961), which began the slow but steady expansion of that
remedy, was decided the same Term as Mapp. It would be
another 17 years before the §1983 remedy was extended to
reach the deep pocket of municipalities, Monell v. New
York City Dept. of Social Servs., 436 U. S. 658 (1978).
Citizens whose Fourth Amendment rights were violated
by federal officers could not bring suit until 10 years after
Mapp, with this Court’s decision in Bivens v. Six Unknown
Fed. Narcotics Agents, 403 U. S. 388 (1971).
  Hudson complains that “it would be very hard to find a
lawyer to take a case such as this,” Tr. of Oral Arg. 7, but
42 U. S. C. §1988(b) answers this objection. Since some
                  Cite as: 547 U. S. ____ (2006)           11

                      Opinion of the Court

civil-rights violations would yield damages too small to
justify the expense of litigation, Congress has authorized
attorney’s fees for civil-rights plaintiffs. This remedy was
unavailable in the heydays of our exclusionary-rule juris
prudence, because it is tied to the availability of a cause of
action. For years after Mapp, “very few lawyers would
even consider representation of persons who had civil
rights claims against the police,” but now “much has
changed. Citizens and lawyers are much more willing to
seek relief in the courts for police misconduct.” M. Avery,
D. Rudovsky, & K. Blum, Police Misconduct: Law and
Litigation, p. v (3d ed. 2005); see generally N. Aron, Lib
erty and Justice for All: Public Interest Law in the 1980s
and Beyond (1989) (describing the growth of public-
interest law). The number of public-interest law firms and
lawyers who specialize in civil-rights grievances has
greatly expanded.
  Hudson points out that few published decisions to date
announce huge awards for knock-and-announce violations.
But this is an unhelpful statistic. Even if we thought that
only large damages would deter police misconduct (and
that police somehow are deterred by “damages” but indif
ferent to the prospect of large §1988 attorney’s fees), we do
not know how many claims have been settled, or indeed
how many violations have occurred that produced any
thing more than nominal injury. It is clear, at least, that
the lower courts are allowing colorable knock-and
announce suits to go forward, unimpeded by assertions of
qualified immunity. See, e.g., Green v. Butler, 420 F. 3d
689, 700–701 (CA7 2005) (denying qualified immunity in a
knock-and-announce civil suit); Holland ex rel. Overdorff
v. Harrington, 268 F. 3d 1179, 1193–1196 (CA10 2001)
(same); Mena v. Simi Valley, 226 F. 3d 1031, 1041–1042
(CA9 2000) (same); Gould v. Davis, 165 F. 3d 265, 270–271
(CA4 1998) (same). As far as we know, civil liability is an
effective deterrent here, as we have assumed it is in other
12                  HUDSON v. MICHIGAN

                      Opinion of the Court

contexts. See, e.g., Correctional Services Corp. v. Malesko,
534 U. S. 61, 70 (2001) (“[T]he threat of litigation and liabil
ity will adequately deter federal officers for Bivens purposes
no matter that they may enjoy qualified immunity” (as
violators of knock-and-announce do not)); see also Nix v.
Williams, 467 U. S. 431, 446 (1984).
   Another development over the past half-century that
deters civil-rights violations is the increasing professional
ism of police forces, including a new emphasis on internal
police discipline. Even as long ago as 1980 we felt it
proper to “assume” that unlawful police behavior would
“be dealt with appropriately” by the authorities, United
States v. Payner, 447 U. S. 727, 733–734, n. 5 (1980), but
we now have increasing evidence that police forces across
the United States take the constitutional rights of citizens
seriously. There have been “wide-ranging reforms in the
education, training, and supervision of police officers.” S.
Walker, Taming the System: The Control of Discretion in
Criminal Justice 1950–1990, p. 51 (1993). Numerous
sources are now available to teach officers and their su
pervisors what is required of them under this Court’s
cases, how to respect constitutional guarantees in various
situations, and how to craft an effective regime for inter
nal discipline. See, e.g., D. Waksman & D. Goodman, The
Search and Seizure Handbook (2d ed. 2006); A. Stone & S.
DeLuca, Police Administration: An Introduction (2d ed.
1994); E. Thibault, L. Lynch, & R. McBridge, Proactive
Police Management (4th ed. 1998). Failure to teach and
enforce constitutional requirements exposes municipalities
to financial liability. See Canton v. Harris, 489 U. S. 378,
388 (1989). Moreover, modern police forces are staffed
with professionals; it is not credible to assert that internal
discipline, which can limit successful careers, will not have
a deterrent effect. There is also evidence that the increas
ing use of various forms of citizen review can enhance
police accountability.
                 Cite as: 547 U. S. ____ (2006)           13

                     Opinion of SCALIA, J.

  In sum, the social costs of applying the exclusionary rule
to knock-and-announce violations are considerable; the
incentive to such violations is minimal to begin with, and
the extant deterrences against them are substantial—
incomparably greater than the factors deterring
warrantless entries when Mapp was decided. Resort to
the massive remedy of suppressing evidence of guilt is
unjustified.
                              IV
   A trio of cases—Segura v. United States, 468 U. S. 796
(1984); New York v. Harris, 495 U. S. 14 (1990); and United
States v. Ramirez, 523 U. S. 65 (1998)—confirms our con
clusion that suppression is unwarranted in this case.
   Like today’s case, Segura involved a concededly illegal
entry. Police conducting a drug crime investigation waited
for Segura outside an apartment building; when he ar
rived, he denied living there. The police arrested him and
brought him to the apartment where they suspected illegal
activity. An officer knocked. When someone inside
opened the door, the police entered, taking Segura with
them. They had neither a warrant nor consent to enter,
and they did not announce themselves as police—an entry
as illegal as can be. Officers then stayed in the apartment
for 19 hours awaiting a search warrant. 468 U. S., at 800–
801; id., at 818–819 (STEVENS, J., dissenting). Once
alerted that the search warrant had been obtained, the
police—still inside, having secured the premises so that no
evidence could be removed—conducted a search. Id., at
801. We refused to exclude the resulting evidence. We
recognized that only the evidence gained from the particu
lar violation could be excluded, see id., at 799, 804–805,
and therefore distinguished the effects of the illegal entry
from the effects of the legal search: “None of the informa
tion on which the warrant was secured was derived from
or related in any way to the initial entry into petitioners’
14                      HUDSON v. MICHIGAN

                          Opinion of SCALIA, J.

apartment . . . .” Id., at 814. It was therefore “beyond
dispute that the information possessed by the agents
before they entered the apartment constituted an inde
pendent source for the discovery and seizure of the evi
dence now challenged.” Ibid.
  If the search in Segura could be “wholly unrelated to the
prior entry,” ibid., when the only entry was warrantless, it
would be bizarre to treat more harshly the actions in this
case, where the only entry was with a warrant. If the
probable cause backing a warrant that was issued later in
time could be an “independent source” for a search that
proceeded after the officers illegally entered and waited, a
search warrant obtained before going in must have at least
this much effect.1
  In the second case, Harris, the police violated the defen
dant’s Fourth Amendment rights by arresting him at
home without a warrant, contrary to Payton v. New York,
445 U. S. 573 (1980). Once taken to the station house, he
gave an incriminating statement. See 495 U. S., at 15–16.
We refused to exclude it. Like the illegal entry which led
——————
  1 JUSTICE  BREYER’s insistence that the warrant in Segura was “ob
tained independently without use of any information found during the
illegal entry,” post, at 14 (dissenting opinion), entirely fails to distin
guish it from the warrant in the present case. Similarly inapposite is
his appeal to Justice Frankfurter’s statement in Wolf v. Colorado, 338
U. S. 25, 28 (1949), that the “knock at the door, . . . as a prelude to a
search, without authority of law . . . [is] inconsistent with the concep
tion of human rights enshrined in [our] history,” see post, at 17. “How
much the more offensive,” JUSTICE BREYER asserts, “when the search
takes place without any knock at all,” ibid. But a no-knock entry
“without authority of law” (i.e., without a search warrant) describes not
this case, but Segura—where the evidence was admitted anyway.
   JUSTICE BREYER’s assertion that Segura, unlike our decision in the
present case, had no effect on deterrence, see post, at 23, does not
comport with the views of the Segura dissent. See, e.g., 468 U. S., at
817 (STEVENS, J., dissenting) (“The Court’s disposition, I fear, will
provide government agents with an affirmative incentive to engage in
unconstitutional violations of the privacy of the home”).
                      Cite as: 547 U. S. ____ (2006)                     15

                           Opinion of SCALIA, J.

to discovery of the evidence in today’s case, the illegal
arrest in Harris began a process that culminated in acqui
sition of the evidence sought to be excluded. While Har
ris’s statement was “the product of an arrest and being in
custody,” it “was not the fruit of the fact that the arrest
was made in the house rather than someplace else.” Id.,
at 20. Likewise here: While acquisition of the gun and
drugs was the product of a search pursuant to warrant, it
was not the fruit of the fact that the entry was not pre
ceded by knock and announce.2
   United States v. Ramirez, supra, involved a claim that
police entry violated the Fourth Amendment because it was
effected by breaking a window. We ultimately concluded
that the property destruction was, under all the circum
stances, reasonable, but in the course of our discussion we
unanimously said the following: “[D]estruction of property
in the course of a search may violate the Fourth Amend
ment, even though the entry itself is lawful and the fruits of
the search are not subject to suppression.” Id., at 71. Had
the breaking of the window been unreasonable, the Court
said, it would have been necessary to determine whether
there had been a “sufficient causal relationship between the
breaking of the window and the discovery of the guns to
warrant suppression of the evidence.” Id., at 72, n. 3. What
clearer expression could there be of the proposition that an

——————
  2 Harris undermines two key points of the dissent. First, the claim

that “whether the interests underlying the knock-and-announce rule
are implicated in any given case is, in a sense, beside the point,” post, at
18. This is flatly refuted by Harris’s plain statement that the reason
for a rule must govern the sanctions for the rule’s violation. 495 U. S.,
at 17, 20; see also supra, at 6. Second, the dissent’s attempt to turn
Harris into a vindication of the sanctity of the home, see post, at 24.
The whole point of the case was that a confession that police obtained
by illegally removing a man from the sanctity of his home was admissi
ble against him.
16                 HUDSON v. MICHIGAN

                     Opinion of SCALIA, J.

impermissible manner of entry does not necessarily trigger
the exclusionary rule?
                      *    *    *
 For the foregoing reasons we affirm the judgment of the
Michigan Court of Appeals.
                                          It is so ordered.
                  Cite as: 547 U. S. ____ (2006)            1

                     Opinion of KENNEDY, J.

SUPREME COURT OF THE UNITED STATES
                          _________________

                          No. 04–1360
                          _________________


BOOKER T. HUDSON, JR., PETITIONER v. MICHIGAN
   ON WRIT OF CERTIORARI TO THE COURT OF APPEALS OF 

                      MICHIGAN

                         [June 15, 2006] 


  JUSTICE KENNEDY, concurring in part and concurring in
the judgment.
  Two points should be underscored with respect to to
day’s decision. First, the knock-and-announce require
ment protects rights and expectations linked to ancient
principles in our constitutional order. See Wilson v. Ar
kansas, 514 U. S. 927, 934 (1995). The Court’s decision
should not be interpreted as suggesting that violations of
the requirement are trivial or beyond the law’s concern.
Second, the continued operation of the exclusionary rule,
as settled and defined by our precedents, is not in doubt.
Today’s decision determines only that in the specific con
text of the knock-and-announce requirement, a violation is
not sufficiently related to the later discovery of evidence to
justify suppression.
  As to the basic right in question, privacy and security in
the home are central to the Fourth Amendment’s guaran
tees as explained in our decisions and as understood since
the beginnings of the Republic. This common understand
ing ensures respect for the law and allegiance to our insti
tutions, and it is an instrument for transmitting our Con
stitution to later generations undiminished in meaning
and force. It bears repeating that it is a serious matter if
law enforcement officers violate the sanctity of the home
by ignoring the requisites of lawful entry. Security must
not be subject to erosion by indifference or contempt.
2                  HUDSON v. MICHIGAN

                   Opinion of KENNEDY, J.

   Our system, as the Court explains, has developed proce
dures for training police officers and imposing discipline
for failures to act competently and lawfully. If those
measures prove ineffective, they can be fortified with more
detailed regulations or legislation. Supplementing these
safeguards are civil remedies, such as those available
under 42 U. S. C. §1983, that provide restitution for dis
crete harms. These remedies apply to all violations, in
cluding, of course, exceptional cases in which unan
nounced entries cause severe fright and humiliation.
   Suppression is another matter. Under our precedents
the causal link between a violation of the knock-and
announce requirement and a later search is too attenuated
to allow suppression. Cf. United States v. Ramirez, 523
U. S. 65, 72, n. 3 (1998) (application of the exclusionary
rule depends on the existence of a “sufficient causal rela
tionship” between the unlawful conduct and the discovery
of evidence). When, for example, a violation results from
want of a 20-second pause but an ensuing, lawful search
lasting five hours discloses evidence of criminality, the
failure to wait at the door cannot properly be described as
having caused the discovery of evidence.
   Today’s decision does not address any demonstrated
pattern of knock-and-announce violations. If a widespread
pattern of violations were shown, and particularly if those
violations were committed against persons who lacked the
means or voice to mount an effective protest, there would
be reason for grave concern. Even then, however, the
Court would have to acknowledge that extending the
remedy of exclusion to all the evidence seized following a
knock-and-announce violation would mean revising the
requirement of causation that limits our discretion in
applying the exclusionary rule. That type of extension
also would have significant practical implications, adding
to the list of issues requiring resolution at the criminal
trial questions such as whether police officers entered a
                 Cite as: 547 U. S. ____ (2006)           3

                    Opinion of KENNEDY, J.

home after waiting 10 seconds or 20.
  In this case the relevant evidence was discovered not
because of a failure to knock-and-announce, but because of
a subsequent search pursuant to a lawful warrant. The
Court in my view is correct to hold that suppression was
not required. While I am not convinced that Segura v.
United States, 468 U. S. 796 (1984), and New York v. Harris,
495 U. S. 14 (1990), have as much relevance here as
JUSTICE SCALIA appears to conclude, the Court’s holding is
fully supported by Parts I through III of its opinion. I ac
cordingly join those Parts and concur in the judgment.
                 Cite as: 547 U. S. ____ (2006)           1

                    BREYER, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 04–1360
                         _________________


BOOKER T. HUDSON, JR., PETITIONER v. MICHIGAN
  ON WRIT OF CERTIORARI TO THE COURT OF APPEALS OF 

                     MICHIGAN

                        [June 15, 2006] 


  JUSTICE BREYER, with whom JUSTICE STEVENS, JUSTICE
SOUTER, and JUSTICE GINSBURG join, dissenting.
   In Wilson v. Arkansas, 514 U. S. 927 (1995), a unani
mous Court held that the Fourth Amendment normally
requires law enforcement officers to knock and announce
their presence before entering a dwelling. Today’s opinion
holds that evidence seized from a home following a viola
tion of this requirement need not be suppressed
   As a result, the Court destroys the strongest legal incen
tive to comply with the Constitution’s knock-and-announce
requirement. And the Court does so without significant
support in precedent. At least I can find no such support
in the many Fourth Amendment cases the Court has
decided in the near century since it first set forth the
exclusionary principle in Weeks v. United States, 232 U. S.
383 (1914). See Appendix, infra.
   Today’s opinion is thus doubly troubling. It represents a
significant departure from the Court’s precedents. And it
weakens, perhaps destroys, much of the practical value of
the Constitution’s knock-and-announce protection.
                                I
  This Court has set forth the legal principles that ought
to have determined the outcome of this case in two sets of
basic Fourth Amendment cases. I shall begin by describ
2                  HUDSON v. MICHIGAN

                     BREYER, J., dissenting

ing that underlying case law.
                               A
   The first set of cases describes the constitutional knock-
and-announce requirement, a requirement that this Court
initially set forth only 11 years ago in Wilson v. Arkansas,
supra. Cf. Sabbath v. United States, 391 U. S. 585 (1968)
(suppressing evidence seized in violation of federal statu
tory knock-and-announce requirement); Miller v. United
States, 357 U. S. 301 (1958) (same). In Wilson, tracing the
lineage of the knock-and-announce rule back to the 13th
century, 514 U. S., at 932, we wrote that
    “[a]n examination of the common law of search and
    seizure leaves no doubt that the reasonableness of a
    search of a dwelling may depend in part on whether
    law enforcement officers announced their presence
    and authority prior to entering.” Id., at 931.
   We noted that this “basic principle” was agreed upon by
“[s]everal prominent founding-era commentators,” id., at
932, and “was woven quickly into the fabric of early
American law” via state constitutions and statutes, id., at
933. 	We further concluded that there was
    “little doubt that the Framers of the Fourth Amend
    ment thought that the method of an officer’s entry
    into a dwelling was among the factors to be considered
    in assessing the reasonableness of a search or sei
    zure.” Id., at 934.
  And we held that the “common-law ‘knock and an
nounce’ principle forms a part of the reasonableness in
quiry under the Fourth Amendment.” Id., at 929. Thus,
“a search or seizure of a dwelling might be constitutionally
defective if police officers enter without prior announce
ment.” Id., at 936; see United States v. Banks, 540 U. S.
31, 36 (2003); United States v. Ramirez, 523 U. S. 65, 70
(1998); Richards v. Wisconsin, 520 U. S. 385, 387 (1997).
                 Cite as: 547 U. S. ____ (2006)           3

                    BREYER, J., dissenting

                             B
  The second set of cases sets forth certain well-
established principles that are relevant here. They in
clude:
  Boyd v. United States, 116 U. S. 616 (1886). In this semi
nal Fourth Amendment case, decided 120 years ago, the
Court wrote, in frequently quoted language, that the
Fourth Amendment’s prohibitions apply
    “to all invasions on the part of the government and its
    employés of the sanctity of a man’s home and the pri
    vacies of life. It is not the breaking of his doors, and
    the rummaging of his drawers, that constitutes the
    essence of the offence; but it is the invasion of his in
    defeasible right of personal security, personal liberty
    and private property.” Id., at 630.
   Weeks, supra. This case, decided 28 years after Boyd,
originated the exclusionary rule. The Court held that the
Federal Government could not retain evidence seized
unconstitutionally and use that evidence in a federal
criminal trial. The Court pointed out that “[i]f letters and
private documents” could be unlawfully seized from a
home “and used in evidence against a citizen accused of an
offense, the protection of the Fourth Amendment declaring
his right to be secure against such searches and seizures is
of no value, and . . . might as well be stricken from the
Constitution.” 232 U. S., at 393.
   Silverthorne Lumber Co. v. United States, 251 U. S. 385
(1920). This case created an exception to (or a qualifica
tion of) Weeks’ exclusionary rule. The Court held that the
Government could not use information obtained during an
illegal search to subpoena documents that they illegally
viewed during that search. Writing for the Court, Justice
Holmes noted that the exclusionary rule “does not mean
that the facts [unlawfully] obtained become sacred and
inaccessible. If knowledge of them is gained from an
4                    HUDSON v. MICHIGAN

                      BREYER, J., dissenting

independent source they may be proved like any
others . . . .” 251 U. S., at 392. Silverthorne thus stands
for the proposition that the exclusionary rule does not
apply if the evidence in question (or the “fruits” of that
evidence) was obtained through a process unconnected
with, and untainted by, the illegal search. Cf. Nix v. Wil
liams, 467 U. S. 431, 444 (1984) (describing related “inevi
table discovery” exception).
   Wolf v. Colorado, 338 U. S. 25 (1949), and Mapp v. Ohio,
367 U. S. 643 (1961). Both of these cases considered
whether Weeks’ exclusionary rule applies to the States. In
Wolf, the Court held that it did not. It said that “[t]he
security of one’s privacy against arbitrary intrusion by the
police . . . is . . . implicit in ‘the concept of ordered liberty’
and as such enforceable against the States through the
Due Process Clause.” 338 U. S., at 27–28. But the Court
held that the exclusionary rule is not enforceable against
the States as “an essential ingredient of the right.” Id., at
29. In Mapp, the Court overruled Wolf. Experience, it
said, showed that alternative methods of enforcing the
Fourth Amendment’s requirements had failed. See 367
U. S., at 651–653; see, e.g., People v. Cahan, 44 Cal. 2d
434, 447, 282 P. 2d 905, 913 (1955) (Traynor, C. J.) (“Ex
perience [in California] has demonstrated, however, that
neither administrative, criminal nor civil remedies are
effective in suppressing lawless searches and seizures”).
The Court consequently held that “all evidence obtained
by searches and seizures in violation of the Constitution
is, by that same authority, inadmissible in a state court.”
Mapp, 367 U. S., at 655. “To hold otherwise,” the Court
added, would be “to grant the right but in reality to with
hold its privilege and enjoyment.” Id., at 656.
                              II
  Reading our knock-and-announce cases, Part I–A, su
pra, in light of this foundational Fourth Amendment case
                 Cite as: 547 U. S. ____ (2006)            5

                     BREYER, J., dissenting

law, Part I–B, supra, it is clear that the exclusionary rule
should apply. For one thing, elementary logic leads to
that conclusion. We have held that a court must “con-
side[r]” whether officers complied with the knock-and
announce requirement “in assessing the reasonableness of
a search or seizure.” Wilson, 514 U. S., at 934 (emphasis
added); see Banks, 540 U. S., at 36. The Fourth Amend
ment insists that an unreasonable search or seizure is,
constitutionally speaking, an illegal search or seizure.
And ever since Weeks (in respect to federal prosecutions)
and Mapp (in respect to state prosecutions), “the use of
evidence secured through an illegal search and seizure” is
“barred” in criminal trials. Wolf, supra, at 28 (citing
Weeks); see Mapp, supra, at 655.
  For another thing, the driving legal purpose underlying
the exclusionary rule, namely, the deterrence of unlawful
government behavior, argues strongly for suppression.
See Elkins v. United States, 364 U. S. 206, 217 (1960) (pur
pose of the exclusionary rule is “to deter—to compel re
spect for the constitutional guaranty . . . by removing the
incentive to disregard it”). In Weeks, Silverthorne, and
Mapp, the Court based its holdings requiring suppression
of unlawfully obtained evidence upon the recognition that
admission of that evidence would seriously undermine the
Fourth Amendment’s promise. All three cases recognized
that failure to apply the exclusionary rule would make
that promise a hollow one, see Mapp, supra, at 657, reduc
ing it to “a form of words,” Silverthorne, supra, at 392, “of
no value” to those whom it seeks to protect, Weeks, supra,
at 393. Indeed, this Court in Mapp held that the exclu
sionary rule applies to the States in large part due to its
belief that alternative state mechanisms for enforcing the
Fourth Amendment’s guarantees had proved “worthless
and futile.” 367 U. S., at 652.
  Why is application of the exclusionary rule any the less
necessary here? Without such a rule, as in Mapp, police
6                   HUDSON v. MICHIGAN

                     BREYER, J., dissenting

know that they can ignore the Constitution’s requirements
without risking suppression of evidence discovered after
an unreasonable entry. As in Mapp, some government
officers will find it easier, or believe it less risky, to pro
ceed with what they consider a necessary search immedi
ately and without the requisite constitutional (say, war
rant or knock-and-announce) compliance. Cf. Mericli, The
Apprehension of Peril Exception to the Knock and An
nounce Rule—Part I, 16 Search and Seizure L. Rep. 129,
130 (1989) (hereinafter Mericili) (noting that some “[d]rug
enforcement authorities believe that safety for the police
lies in a swift, surprising entry with overwhelming force—
not in announcing their official authority”).
   Of course, the State or the Federal Government may
provide alternative remedies for knock-and-announce
violations. But that circumstance was true of Mapp as
well. What reason is there to believe that those remedies
(such as private damages actions under 42 U. S. C. §1983),
which the Court found inadequate in Mapp, can ade
quately deter unconstitutional police behavior here? See
Kamisar, In Defense of the Search and Seizure Exclusion
ary Rule, 26 Harv. J. L. & Pub. Pol’y 119, 126–129 (2003)
(arguing that “five decades of post-Weeks ‘freedom’ from
the inhibiting effect of the federal exclusionary rule failed
to produce any meaningful alternative to the exclusionary
rule in any jurisdiction” and that there is no evidence that
“times have changed” post-Mapp).
   The cases reporting knock-and-announce violations are
legion. See, e.g., 34 Geo. L. J. Ann. Rev. Crim. Proc. 31–35
(2005) (collecting court of appeals cases); Annot., 85
A. L. R. 5th 1 (2001) (collecting state-court cases); Brief for
Petitioner 16–17 (collecting federal and state cases).
Indeed, these cases of reported violations seem sufficiently
frequent and serious as to indicate “a widespread pattern.”
Ante, at 2 (KENNEDY, J., concurring in part and concurring
in judgment). Yet the majority, like Michigan and the
                  Cite as: 547 U. S. ____ (2006)            7

                     BREYER, J., dissenting

United States, has failed to cite a single reported case in
which a plaintiff has collected more than nominal dam
ages solely as a result of a knock-and-announce violation.
Even Michigan concedes that, “in cases like the present
one . . . , damages may be virtually non-existent.” Brief for
Respondent 35, n. 66; And Michigan’s amici further con
cede that civil immunities prevent tort law from being an
effective substitute for the exclusionary rule at this time.
Brief for Criminal Justice Legal Foundation 10; see also
Hope v. Pelzer, 536 U. S. 730, 739 (2002) (difficulties of
overcoming qualified immunity defenses).
  As Justice Stewart, the author of a number of signifi
cant Fourth Amendment opinions, explained, the deter
rent effect of damage actions “can hardly be said to be
great,” as such actions are “expensive, time-consuming,
not readily available, and rarely successful.” Stewart, The
Road to Mapp v. Ohio and Beyond: The Origins, Develop
ment and Future of the Exclusionary Rule in Search-and-
Seizure Cases, 83 Colum. L. Rev. 1365, 1388 (1983). The
upshot is that the need for deterrence—the critical factor
driving this Court’s Fourth Amendment cases for close to a
century—argues with at least comparable strength for
evidentiary exclusion here.
  To argue, as the majority does, that new remedies, such
as 42 U. S. C. §1983 actions or better trained police, make
suppression unnecessary is to argue that Wolf, not Mapp,
is now the law. (The Court recently rejected a similar
argument in Dickerson v. United States, 530 U. S. 428, 441–
442 (2000).) To argue that there may be few civil suits
because violations may produce nothing “more than nomi
nal injury” is to confirm, not to deny, the inability of civil
suits to deter violations. See ante, at 11. And to argue
without evidence (and despite myriad reported cases of
violations, no reported case of civil damages, and Michi
gan’s concession of their nonexistence) that civil suits may
provide deterrence because claims may “have been settled”
8                   HUDSON v. MICHIGAN

                     BREYER, J., dissenting

is, perhaps, to search in desperation for an argument. See
ibid. Rather, the majority, as it candidly admits, has
simply “assumed” that, “[a]s far as [it] know[s], civil liabil
ity is an effective deterrent,” ibid., a support-free assump
tion that Mapp and subsequent cases make clear does not
embody the Court’s normal approach to difficult questions
of Fourth Amendment law.
   It is not surprising, then, that after looking at virtually
every pertinent Supreme Court case decided since Weeks, I
can find no precedent that might offer the majority sup
port for its contrary conclusion. The Court has, of course,
recognized that not every Fourth Amendment violation
necessarily triggers the exclusionary rule. Ante, at 4–5; cf.
Illinois v. Gates, 462 U. S. 213, 223 (1983) (application of
the exclusionary rule is a separate question from whether
the Fourth Amendment has been violated). But the class
of Fourth Amendment violations that do not result in
suppression of the evidence seized, however, is limited.
   The Court has declined to apply the exclusionary rule
only:
     (1) where there is a specific reason to believe that ap
    plication of the rule would “not result in appreciable
    deterrence,” United States v. Janis, 428 U. S. 433, 454
    (1976); see, e.g., United States v. Leon, 468 U. S. 897,
    919–920 (1984) (exception where searching officer exe
    cutes defective search warrant in “good faith”); Ari
    zona v. Evans, 514 U. S. 1, 14 (1995) (exception for
    clerical errors by court employees); Walder v. United
    States, 347 U. S. 62 (1954) (exception for impeach
    ment purposes), or
    (2) where admissibility in proceedings other than
    criminal trials was at issue, see, e.g., Pennsylvania
    Bd. of Probation and Parole v. Scott, 524 U. S. 357,
    364 (1998) (exception for parole revocation proceed
    ings); INS v. Lopez-Mendoza, 468 U. S. 1032, 1050
                  Cite as: 547 U. S. ____ (2006)             9

                     BREYER, J., dissenting

    (1984) (plurality opinion) (exception for deportation
    proceedings); Janis, supra, at 458 (exception for civil
    tax proceedings); United States v. Calandra, 414 U. S.
    338, 348–350 (1974) (exception for grand jury proceed
    ings); Stone v. Powell, 428 U. S. 465, 493–494 (1976)
    (exception for federal habeas proceedings).
   Neither of these two exceptions applies here. The sec
ond does not apply because this case is an ordinary crimi
nal trial. The first does not apply because (1) officers who
violate the rule are not acting “as a reasonable officer
would and should act in similar circumstances,” Leon,
supra, at 920, (2) this case does not involve government
employees other than police, Evans, supra, and (3), most
importantly, the key rationale for any exception, “lack of
deterrence,” is missing, see Pennsylvania Bd. of Probation,
supra, at 364 (noting that the rationale for not applying
the rule in noncriminal cases has been that the deterrence
achieved by having the rule apply in those contexts is
“minimal” because “application of the rule in the criminal
trial context already provides significant deterrence of
unconstitutional searches”); Michigan v. Tucker, 417 U. S.
433, 447 (1974) (noting that deterrence rationale would not
be served if rule applied to police officers acting in good
faith, as the “deterrent purpose of the exclusionary rule
necessarily assumes that the police have engaged in willful,
or at the very least negligent, conduct”). That critical latter
rationale, which underlies every exception, does not apply
here, as there is no reason to think that, in the case of
knock-and-announce violations by the police, “the exclu
sion of evidence at trial would not sufficiently deter future
errors,” Evans, supra, at 14, or “ ‘further the ends of the
exclusionary rule in any appreciable way,’ ” Leon, supra, at
919–920.
   I am aware of no other basis for an exception. The
Court has decided more than 300 Fourth Amendment
10                 HUDSON v. MICHIGAN

                     BREYER, J., dissenting

cases since Weeks. The Court has found constitutional
violations in nearly a third of them. See W. Greenhalgh,
The Fourth Amendment Handbook: A Chronological Sur
vey of Supreme Court Decisions 27–130 (2d ed. 2003)
(collecting and summarizing 332 post-Weeks cases decided
between 1914 and 2002). The nature of the constitutional
violation varies. In most instances officers lacked a war
rant; in others, officers possessed a warrant based on false
affidavits; in still others, the officers executed the search
in an unconstitutional manner. But in every case involv
ing evidence seized during an illegal search of a home
(federally since Weeks, nationally since Mapp), the Court,
with the exceptions mentioned, has either explicitly or
implicitly upheld (or required) the suppression of the
evidence at trial. See Appendix, infra. In not one of those
cases did the Court “questio[n], in the absence of a more
efficacious sanction, the continued application of the [ex
clusionary] rule to suppress evidence from the State’s
case” in a criminal trial. Franks v. Delaware, 438 U. S.
154, 171 (1978).
   I can find nothing persuasive in the majority’s opinion
that could justify its refusal to apply the rule. It certain-
ly is not a justification for an exception here (as the major
ity finds) to find odd instances in other areas of law that
do not automatically demand suppression. Ante, at 10
(suspect confesses, police beat him up afterwards; sus-
pect confesses, then police apparently arrest him, take
him to station, and refuse to tell him of his right to coun
sel). Nor can it justify an exception to say that some
police may knock at the door anyway (to avoid being
mistaken for a burglar), for other police (believing
quick entry is the most secure, effective entry) will not
voluntarily do so. Cf. Mericli 130 (describing Special
Weapons and Tactics (SWAT) team practices); R.
Balko, No SWAT (Apr. 6, 2006), available at
http://www.cato.org/pub_display.php?pub_id=6344 (all In
                  Cite as: 547 U. S. ____ (2006)           11

                     BREYER, J., dissenting

ternet materials as visited June 7, 2006, and available in
Clerk of Court’s case file).
   Neither can the majority justify its failure to respect the
need for deterrence, as set forth consistently in the Court’s
prior case law, through its claim of “substantial social
costs”—at least if it means that those “social costs” are
somehow special here. The only costs it mentions are
those that typically accompany any use of the Fourth
Amendment’s exclusionary principle: (1) that where the
constable blunders, a guilty defendant may be set free
(consider Mapp itself); (2) that defendants may assert
claims where Fourth Amendment rights are uncertain
(consider the Court’s qualified immunity jurisprudence),
and (3) that sometimes it is difficult to decide the merits of
those uncertain claims. See ante, at 8–9. In fact, the “no
knock” warrants that are provided by many States, by
diminishing uncertainty, may make application of the
knock-and-announce principle less “cost[ly]” on the whole
than application of comparable Fourth Amendment prin
ciples, such as determining whether a particular war
rantless search was justified by exigency. The majority’s
“substantial social costs” argument is an argument
against the Fourth Amendment’s exclusionary principle
itself. And it is an argument that this Court, until now,
has consistently rejected.
                            III
  The majority, Michigan, and the United States make
several additional arguments. In my view, those argu
ments rest upon misunderstandings of the principles
underlying this Court’s precedents.
                             A
   The majority first argues that “the constitutional viola
tion of an illegal manner of entry was not a but-for cause
of obtaining the evidence.” Ante, at 5. But taking causa
12                 HUDSON v. MICHIGAN

                     BREYER, J., dissenting

tion as it is commonly understood in the law, I do not see
how that can be so. See W. Keeton, D. Dobbs, R. Keeton,
& D. Owen, Prosser and Keeton on Law of Torts 266 (5th
ed. 1984). Although the police might have entered Hud
son’s home lawfully, they did not in fact do so. Their
unlawful behavior inseparably characterizes their actual
entry; that entry was a necessary condition of their pres
ence in Hudson’s home; and their presence in Hudson’s
home was a necessary condition of their finding and seiz
ing the evidence. At the same time, their discovery of
evidence in Hudson’s home was a readily foreseeable
consequence of their entry and their unlawful presence
within the home. Cf. 2 Restatement (Second) of Torts
§435 (1963–1964).
   Moreover, separating the “manner of entry” from the
related search slices the violation too finely. As noted,
Part I–A, supra, we have described a failure to comply
with the knock-and-announce rule, not as an independ
ently unlawful event, but as a factor that renders the
search “constitutionally defective.” Wilson, 514 U. S., at
936; see also id., at 934 (compliance with the knock-and
announce requirement is one of the “factors to be consid
ered in assessing the reasonableness of a search or seizure”
(emphasis added)); Ker v. California, 374 U. S. 23, 53 (1963)
(opinion of Brennan, J.) (“[A] lawful entry is the indispensa
ble predicate of a reasonable search”).
   The Court nonetheless accepts Michigan’s argument
that the requisite but-for-causation is not satisfied in this
case because, whether or not the constitutional violation
occurred (what the Court refers to as a “preliminary mis
step”), “the police would have executed the warrant they
had obtained, and would have discovered the gun and
drugs inside the house.” Ante, at 5. As support for this
proposition, Michigan rests on this Court’s inevitable
discovery cases.
   This claim, however, misunderstands the inevitable
                 Cite as: 547 U. S. ____ (2006)          13

                    BREYER, J., dissenting

discovery doctrine. Justice Holmes in Silverthorne, in
discussing an “independent source” exception, set forth the
principles underlying the inevitable discovery rule. See
supra, at 4. That rule does not refer to discovery that
would have taken place if the police behavior in question
had (contrary to fact) been lawful. The doctrine does not
treat as critical what hypothetically could have happened
had the police acted lawfully in the first place. Rather,
“independent” or “inevitable” discovery refers to discovery
that did occur or that would have occurred (1) despite (not
simply in the absence of) the unlawful behavior and (2)
independently of that unlawful behavior. The government
cannot, for example, avoid suppression of evidence seized
without a warrant (or pursuant to a defective warrant)
simply by showing that it could have obtained a valid
warrant had it sought one. See, e.g., Coolidge v. New
Hampshire, 403 U. S. 443, 450–451 (1971). Instead, it
must show that the same evidence “inevitably would have
been discovered by lawful means.” Nix v. Williams, 467
U. S., at 444 (emphasis added). “What a man could do is
not at all the same as what he would do.” Austin, Ifs And
Cans, 42 Proceedings of the British Academy 109, 111–112
(1956).
  The inevitable discovery exception rests upon the prin
ciple that the remedial purposes of the exclusionary rule
are not served by suppressing evidence discovered through
a “later, lawful seizure” that is “genuinely independent of
an earlier, tainted one.” Murray v. United States, 487
U. S. 533, 542 (1988) (emphasis added); see also id., at 545
(Marshall, J., joined by STEVENS and O’Connor, JJ., dis
senting) (“When the seizure of the evidence at issue is
‘wholly independent of’ the constitutional violation, then
exclusion arguably will have no effect on a law enforce
ment officer’s incentive to commit an unlawful search”).
  Case law well illustrates the meaning of this principle.
In Nix, supra, police officers violated a defendant’s Sixth
14                 HUDSON v. MICHIGAN

                    BREYER, J., dissenting

Amendment right by eliciting incriminating statements
from him after he invoked his right to counsel. Those
statements led to the discovery of the victim’s body. The
Court concluded that evidence obtained from the victim’s
body was admissible because it would ultimately or inevi
tably have been discovered by a volunteer search party
effort that was ongoing—whether or not the Sixth Amend
ment violation had taken place. Id., at 449. In other
words, the evidence would have been found despite, and
independent of, the Sixth Amendment violation.
   In Segura v. United States, 468 U. S. 796 (1984), one of
the “trio of cases” JUSTICE SCALIA says “confirms [the
Court’s] conclusion,” ante, at 13, the Court held that an
earlier illegal entry into an apartment did not require
suppression of evidence that police later seized when
executing a search warrant obtained on the basis of infor
mation unconnected to the initial entry. The Court rea
soned that the “evidence was discovered the day following
the entry, during the search conducted under a valid
warrant”—i.e., a warrant obtained independently without
use of any information found during the illegal entry—and
that “it was the product of that search, wholly unrelated to
the prior [unlawful] entry.” Segura, supra, at 814 (em
phasis added).
   In Murray, supra, the Court upheld the admissibility of
seized evidence where agents entered a warehouse with
out a warrant, and then later returned with a valid war
rant that was not obtained on the basis of evidence ob
served during the first (illegal) entry. The Court reasoned
that while the agents’ “[k]nowledge that the marijuana
was in the warehouse was assuredly acquired at the time
of the unlawful entry . . . it was also acquired at the time
of entry pursuant to the warrant, and if that later acquisi
tion was not the result of the earlier entry there is no rea
son why the independent source doctrine should not ap
ply.” Id., at 541 (emphasis added).
                 Cite as: 547 U. S. ____ (2006)          15

                    BREYER, J., dissenting

   Thus, the Court’s opinion reflects a misunderstanding of
what “inevitable discovery” means when it says, “[i]n this
case, of course, the constitutional violation of an illegal
manner of entry was not a but-for cause of obtaining the
evidence.” Ante, at 5. The majority rests this conclusion
on its next statement: “Whether that preliminary misstep
has occurred or not, the police . . . would have discovered
the gun and the drugs inside the house.” Ibid. Despite
the phrase “of course,” neither of these statements is
correct. It is not true that, had the illegal entry not oc
curred, “police would have discovered the guns and drugs
inside the house.” Without that unlawful entry they
would not have been inside the house; so there would have
been no discovery. See supra, at 12.
   Of course, had the police entered the house lawfully,
they would have found the gun and drugs. But that fact is
beside the point. The question is not what police might
have done had they not behaved unlawfully. The question
is what they did do. Was there set in motion an independ
ent chain of events that would have inevitably led to the
discovery and seizure of the evidence despite, and inde
pendent of, that behavior? The answer here is “no.”
                             B
   The majority, Michigan, and the United States point out
that the officers here possessed a warrant authorizing a
search. Ante, at 5. That fact, they argue, means that the
evidence would have been discovered independently or
somehow diminishes the need to suppress the evidence.
But I do not see why that is so. The warrant in question
was not a “no-knock” warrant, which many States (but not
Michigan) issue to assure police that a prior knock is not
necessary. Richards, 520 U. S., at 396, n. 7 (collecting
state statutes). It did not authorize a search that fails to
comply with knock-and-announce requirements. Rather,
it was an ordinary search warrant. It authorized a search
16                HUDSON v. MICHIGAN

                    BREYER, J., dissenting

that complied with, not a search that disregarded, the
Constitution’s knock-and-announce rule.
  Would a warrant that authorizes entry into a home on
Tuesday permit the police to enter on Monday? Would a
warrant that authorizes entry during the day authorize
the police to enter during the middle of the night? It is
difficult for me to see how the presence of a warrant that
does not authorize the entry in question has anything to
do with the “inevitable discovery” exception or otherwise
diminishes the need to enforce the knock-and-announce
requirement through suppression.
                             C
   The majority and the United States set forth a policy-
related variant of the causal connection theme: The
United States argues that the law should suppress evi
dence only insofar as a Fourth Amendment violation
causes the kind of harm that the particular Fourth
Amendment rule seeks to protect against. It adds that the
constitutional purpose of the knock-and-announce rule is
to prevent needless destruction of property (such as break
ing down a door) and to avoid unpleasant surprise. And it
concludes that the exclusionary rule should suppress
evidence of, say, damage to property, the discovery of a
defendant in an “intimate or compromising moment,” or
an excited utterance from the occupant caught by surprise,
but nothing more. Brief for United States as Amicus
Curiae 12, 28.
   The majority makes a similar argument. It says that
evidence should not be suppressed once the causal connec
tion between unlawful behavior and discovery of the evi
dence becomes too “attenuated.” Ante, at 5. But the ma
jority then makes clear that it is not using the word
“attenuated” to mean what this Court’s precedents have
typically used that word to mean, namely, that the discov
ery of the evidence has come about long after the unlawful
                 Cite as: 547 U. S. ____ (2006)          17

                    BREYER, J., dissenting

behavior took place or in an independent way, i.e., through
“ ‘means sufficiently distinguishable to be purged of the
primary taint.’ ” Wong Sun v. United States, 371 U. S. 471,
487–488 (1963); see Brown v. Illinois, 422 U. S. 590, 603–
604 (1975).
   Rather, the majority gives the word “attenuation” a new
meaning (thereby, in effect, making the same argument as
the United States). “Attenuation,” it says, “also occurs
when, even given a direct causal connection, the interest
protected by the constitutional guarantee that has been
violated would not be served by suppression of the evi
dence obtained.” Ante, at 6. The interests the knock-and
announce rule seeks to protect, the Court adds, are “hu
man life” (at stake when a householder is “surprised”),
“property” (such as the front door), and “those elements of
privacy and dignity that can be destroyed by a sudden
entrance,” namely, “the opportunity to collect oneself
before answering the door.” Ante, at 7. Since none of
those interests led to the discovery of the evidence seized
here, there is no reason to suppress it.
   There are three serious problems with this argument.
First, it does not fully describe the constitutional values,
purposes, and objectives underlying the knock-and
announce requirement. That rule does help to protect
homeowners from damaged doors; it does help to protect
occupants from surprise. But it does more than that. It
protects the occupants’ privacy by assuring them that
government agents will not enter their home without
complying with those requirements (among others) that
diminish the offensive nature of any such intrusion. Many
years ago, Justice Frankfurter wrote for the Court that
the “knock at the door, . . . as a prelude to a search, with
out authority of law . . . [is] inconsistent with the concep
tion of human rights enshrined in [our] history” and Con
stitution. Wolf, 338 U. S., at 28. How much the more
offensive when the search takes place without any knock
18                  HUDSON v. MICHIGAN

                     BREYER, J., dissenting

at all. Cf. Wilson, 514 U. S., at 931 (knock-and-announce
rule recognizes that “the common law generally protected
a man’s house as ‘his castle of defence and asylum’ ” (quot
ing 3 W. Blackstone, Commentaries *288)); Miller, 357
U. S., at 313 (federal knock-and-announce statute “codi
f[ied] a tradition embedded in Anglo-American law” that
reflected “the reverence of the law for the individual’s
right of privacy in his house”).
   Over a century ago this Court wrote that “it is not the
breaking of his doors” that is the “essence of the offence,”
but the “invasions on the part of the government . . . of the
sanctity of a man’s home and the privacies of life.” Boyd,
116 U. S., at 630. And just this Term we have reiterated
that “it is beyond dispute that the home is entitled to
special protection as the center of the private lives of our
people.” Georgia v. Randolph, 547 U. S. ___, ___ (2006)
(slip op., at 10) (quoting Minnesota v. Carter, 525 U. S. 83,
99 (1998) (KENNEDY, J., concurring)). The knock-and
announce requirement is no less a part of the “centuries
old principle” of special protection for the privacy of the
home than the warrant requirement. See 547 U. S., at ___
(slip op., at 10) (citing Miller, supra, at 307). The Court is
therefore wrong to reduce the essence of its protection to
“the right not to be intruded upon in one’s nightclothes.”
Ante, at 10; see Richards, 520 U. S., at 393, n. 5
(“[I]ndividual privacy interest[s]” protected by the rule
are “not inconsequential” and “should not be unduly
minimized”).
   Second, whether the interests underlying the knock-
and-announce rule are implicated in any given case is, in a
sense, beside the point. As we have explained, failure to
comply with the knock-and-announce rule renders the
related search unlawful. Wilson, supra, at 936. And
where a search is unlawful, the law insists upon suppres
sion of the evidence consequently discovered, even if that
evidence or its possession has little or nothing to do with
                 Cite as: 547 U. S. ____ (2006)           19

                     BREYER, J., dissenting

the reasons underlying the unconstitutionality of a search.
The Fourth Amendment does not seek to protect contra
band, yet we have required suppression of contraband
seized in an unlawful search. See, e.g., Kyllo v. United
States, 533 U. S. 27, 40 (2001); Coolidge, 403 U. S., at 473.
That is because the exclusionary rule protects more gen
eral “privacy values through deterrence of future police
misconduct.” James v. Illinois, 493 U. S. 307, 319 (1990).
The same is true here.
   Third, the majority’s interest-based approach departs
from prior law. Ordinarily a court will simply look to see
if the unconstitutional search produced the evidence. The
majority does not refer to any relevant case in which,
beyond that, suppression turned on the far more detailed
relation between, say, (1) a particular materially false
statement made to the magistrate who issued a (conse
quently) invalid warrant and (2) evidence found after a
search with that warrant. But cf. ante, at 15, n. 2 (plural
ity opinion) (citing New York v. Harris, 495 U. S. 14
(1990), as such a case in section of opinion that JUSTICE
KENNEDY does not join). And the majority’s failure does
not surprise me, for such efforts to trace causal connec
tions at retail could well complicate Fourth Amendment
suppression law, threatening its workability.
                             D
  The United States, in its brief and at oral argument, has
argued that suppression is “an especially harsh remedy
given the nature of the violation in this case.” Brief for
United States as Amicus Curiae 28; see also id., at 24.
This argument focuses upon the fact that entering a house
after knocking and announcing can, in some cases, prove
dangerous to a police officer. Perhaps someone inside has
a gun, as turned out to be the case here. The majority
adds that police officers about to encounter someone who
may try to harm them will be “uncertain” as to how long to
20                 HUDSON v. MICHIGAN

                     BREYER, J., dissenting

wait. Ante, at 9. It says that, “[i]f the consequences of
running afoul” of the knock-and-announce “rule were so
massive,” i.e., would lead to the exclusion of evidence, then
“officers would be inclined to wait longer than the law
requires—producing preventable violence against officers
in some cases.” Ante, at 8–9.
  To argue that police efforts to assure compliance with
the rule may prove dangerous, however, is not to argue
against evidence suppression. It is to argue against the
validity of the rule itself. Similarly, to argue that en
forcement means uncertainty, which in turn means the
potential for dangerous and longer-than-necessary delay,
is (if true) to argue against meaningful compliance with
the rule.
  The answer to the first argument is that the rule itself
does not require police to knock or to announce their pres
ence where police have a “reasonable suspicion” that doing
so “would be dangerous or futile” or “would inhibit the
effective investigation of the crime by, for example, allow
ing the destruction of evidence.” Richards, supra, at 394;
see Banks, 540 U. S., at 36–37; Wilson, supra, at 935–936.
  The answer to the second argument is that States can,
and many do, reduce police uncertainty while assuring a
neutral evaluation of concerns about risks to officers or the
destruction of evidence by permitting police to obtain a
“no-knock” search warrant from a magistrate judge,
thereby assuring police that a prior announcement is not
necessary. Richards, 520 U. S., at 396, n. 7 (collecting
state statutes). While such a procedure cannot remove all
uncertainty, it does provide an easy way for officers to
comply with the knock-and-announce rule.
  Of course, even without such a warrant, police maintain
the backup “authority to exercise independent judgment
concerning the wisdom of a no-knock entry at the time the
warrant is being executed.” Ibid. “[I]f circumstances
support a reasonable suspicion of exigency when the offi
                 Cite as: 547 U. S. ____ (2006)          21

                    BREYER, J., dissenting

cers arrive at the door, they may go straight in.” Banks,
supra, at 37. And “[r]easonable suspicion is a less de
manding standard than probable cause . . . .” Alabama v.
White, 496 U. S. 325, 330 (1990); see Terry v. Ohio, 392
U. S. 1, 21–22 (1968) (no Fourth Amendment violation
under the reasonable suspicion standard if “the facts
available to the officer at the moment of the seizure or the
search ‘warrant a man of reasonable caution in the belief’
that the action taken was appropriate”).
  Consider this very case. The police obtained a search
warrant that authorized a search, not only for drugs, but
also for guns. App. 5. If probable cause justified a search
for guns, why would it not also have justified a no-knock
warrant, thereby diminishing any danger to the officers?
Why (in a State such as Michigan that lacks no-knock
warrants) would it not have justified the very no-knock
entry at issue here? Indeed, why did the prosecutor not
argue in this very case that, given the likelihood of guns,
the no-knock entry was lawful? From what I have seen in
the record, he would have won. And had he won, there
would have been no suppression here.
  That is the right way to win. The very process of argu
ing the merits of the violation would help to clarify the
contours of the knock-and-announce rule, contours that
the majority believes are too fuzzy. That procedural fact,
along with no-knock warrants, back up authority to enter
without knocking regardless, and use of the “reasonable
suspicion” standard for doing so should resolve the gov
ernment’s problems with the knock-and-announce rule
while reducing the “uncertain[ty]” that the majority dis
cusses to levels beneath that found elsewhere in Fourth
Amendment law (e.g., exigent circumstances). Ante, at 8.
Regardless, if the Court fears that effective enforcement of
a constitutional requirement will have harmful conse
quences, it should face those fears directly by addressing
the requirement itself. It should not argue, “the require
22                 HUDSON v. MICHIGAN

                    BREYER, J., dissenting

ment is fine, indeed, a serious matter, just don’t enforce
it.”
                              E
   It should be apparent by now that the three cases upon
which JUSTICE SCALIA relies—Segura v. United States,
468 U. S. 796; New York v. Harris, 495 U. S. 14; and Ra
mirez, 523 U. S. 65—do not support his conclusion. See
ante, at 13–15. Indeed, JUSTICE KENNEDY declines to join
this section of the lead opinion because he fails to see the
relevance of Segura and Harris, though he does rely on
Ramirez. Ante, at 3 (opinion concurring in part and con
curring in judgment).
   JUSTICE SCALIA first argues that, if the “search in
Segura could be ‘wholly unrelated to the prior entry, . . .
when the only entry was warrantless, it would be bizarre
to treat more harshly the actions in this case, where the
only entry was with a warrant.” Ante, at 14. Then it says
that, “[i]f the probable cause backing a warrant that was
issued later in time could be an ‘independent source’ for a
search that proceeded after the officers illegally entered
and waited, a search warrant obtained before going in
must have at least this much effect.” Ibid. I do not under
stand these arguments. As I have explained, the presence
of a warrant that did not authorize a search that fails to
comply with knock-and-announce requirements is beside
the point. See Part III–B, supra. And the timing of the
warrant in Segura made no difference to the case. The
relevant fact about the warrant there was that it was
lawfully obtained and arguably set off an independent
chain of events that led the police to seize the evidence.
468 U. S., at 814; see also id., at 814–815 (“The valid
warrant search was a ‘means sufficiently distinguishable’
to purge the evidence of any ‘taint’ arising from the entry”
(citations omitted)). As noted, there is no such independ
ent event, or intervening chain of events that would purge
                 Cite as: 547 U. S. ____ (2006)          23

                    BREYER, J., dissenting

the taint of the illegal entry, present here. See supra, at
15. The search that produced the relevant evidence here
is the very search that the knock-and-announce violation
rendered unlawful. There simply is no “independent
source.”
   As importantly, the Court in Segura said nothing to
suggest it intended to create a major exclusionary rule
exception, notwithstanding the impact of such an excep
tion on deterrence. Indeed, such an exception would be
inconsistent with a critical rationale underlying the inde
pendent source and inevitable discovery rules, which was
arguably available in Segura, and which is clearly absent
here. That rationale concerns deterrence. The threat of
inadmissibility deters unlawful police behavior; and the
existence of an exception applicable where evidence is
found through an untainted independent route will rarely
undercut that deterrence. That is because the police can
rarely rely upon such an exception—at least not often
enough to change the deterrence calculus. See Murray,
487 U. S., at 540 (“We see the incentives differently. An
officer with probable cause sufficient to obtain a search
warrant would be foolish to enter the premises in an
unlawful manner. By doing so, he would risk suppression
of all evidence on the premises . . . ”); Nix, 467 U. S., at
445 (“A police officer who is faced with the opportunity to
obtain evidence illegally will rarely, if ever, be in a posi
tion to calculate whether the evidence sought would inevi
tably be discovered”); id., at 444 (“If the prosecution can
establish by a preponderance of the evidence that the
information ultimately or inevitably would have been
discovered by lawful means—here the volunteers’ search—
then the deterrence rationale has so little basis that the
evidence should be received”).
   Segura’s police officers would have been foolish to have
entered the apartment unlawfully with the ex ante hope
that an independent causal chain of events would later
24                 HUDSON v. MICHIGAN

                    BREYER, J., dissenting

occur and render admissible the evidence they found. By
way of contrast, today’s holding will seriously undermine
deterrence in knock-and-announce cases. Officers will
almost always know ex ante that they can ignore the
knock-and-announce requirement without risking the
suppression of evidence discovered after their unlawful
entry. That fact is obvious, and this Court has never
before today—not in Segura or any other post-Weeks (or
post-Mapp) case—refused to apply the exclusionary rule
where its absence would so clearly and so significantly
impair government officials’ incentive to comply with
comparable Fourth Amendment requirements.
  Neither does New York v. Harris, supra, support the
Court’s result. See ante, at 6, 14; but see ante, at 3 (opin
ion of KENNEDY, J.) (declining to join section relying on
Harris). In Harris, police officers arrested the defendant
at his home without a warrant, in violation of Payton v.
New York, 445 U. S. 573 (1980). Harris made several
incriminating statements: a confession in his home, a
written inculpatory statement at the stationhouse, and a
videotaped interview conducted by the district attorney at
the stationhouse. 495 U. S., at 16. The trial court sup
pressed the statements given by Harris in the house and
on the videotape, and the State did not challenge either of
those rulings. Ibid. The sole question in the case was
whether the written statement given later at the station-
house should also have been suppressed. The Court held
that this later, outside-the-home statement “was admissi
ble because Harris was in legal custody . . . and because
the statement, while the product of an arrest and being in
custody, was not the fruit of the fact that the arrest was
made in the house rather than someplace else.” Id., at 20.
Immediately after the Court stated its holding, it ex
plained:
     “To put the matter another way, suppressing the
                  Cite as: 547 U. S. ____ (2006)           25

                     BREYER, J., dissenting

    statement taken outside the house would not serve
    the purpose of the rule that made Harris’ in-house ar
    rest illegal. The warrant requirement for an arrest in
    the home is imposed to protect the home, and anything
    incriminating the police gathered from arresting Har
    ris in his home, rather than elsewhere, has been ex
    cluded, as it should have been; the purpose of the rule
    has thereby been vindicated.” Ibid. (emphasis added).
   How can JUSTICE SCALIA maintain that the evidence
here—a gun and drugs seized in the home—is “ ‘not the
fruit’ ” of the illegal entry? Ante, at 14. The officers’ fail
ure to knock and announce rendered the entire search
unlawful, Wilson, 514 U. S., at 936, and that unlawful
search led to the discovery of evidence in petitioner’s
home. Thus, Harris compels the opposite result than that
reached by the Court today. Like the Payton rule at issue
in Harris, the knock-and-announce rule reflects the “rev
erence of the law for the individual’s right of privacy in his
house.” Miller, 357 U. S., at 313; cf. Harris, 495 U. S., at
17 (“Payton itself emphasized that our holding in that case
stemmed from the ‘overriding respect for the sanctity of
the home that has been embedded in our traditions since
the origins of the Republic’ ”). Like the confession that was
“excluded, as it should have been,” in Harris, id., at 20, the
evidence in this case was seized in the home, immediately
following the illegal entry. And like Harris, nothing in
petitioner’s argument would require the suppression of
evidence obtained outside the home following a knock-and
announce violation should be suppressed, precisely be
cause officers have a remaining incentive to follow the rule
to avoid the suppression of any evidence obtained from the
very place they are searching. Cf. ibid. (“Even though we
decline to suppress statements made outside the home
following a Payton violation, the principle incentive to
obey Payton still obtains: the police know that a war
26                  HUDSON v. MICHIGAN

                      BREYER, J., dissenting

rantless entry will lead to the suppression of any evidence
found, or statements taken, inside the home”).
  I concede that United States v. Ramirez, 523 U. S. 65,
offers the majority its last best hope. Ante, at 14–15. But
not even that case can offer the majority significant sup
port. The majority focuses on the Court’s isolated state
ment that “destruction of property in the course of a
search may violate the Fourth Amendment, even though
the entry itself is lawful and the fruits of the search are not
subject to suppression.” Ramirez, supra, at 71 (emphasis
added). But even if I accept this dictum, the entry here is
unlawful, not lawful. Wilson, 514 U. S., at 931, 934. It is
one thing to say (in an appropriate case) that destruction
of property after proper entry has nothing to do with
discovery of the evidence, and to refuse to suppress. It
would be quite another thing to say that improper entry
had nothing to do with discovery of the evidence in this
case. Moreover, the deterrence analysis for the property
destruction cases (where, by definition, there will almost
always be quantifiable damages) might well differ.
                             IV
   There is perhaps one additional argument implicit in
the majority’s approach. The majority says, for example,
that the “cost” to a defendant of “entering this lottery,” i.e.,
of claiming a “knock-and-announce” violation, “would be
small, but the jackpot enormous”—namely, a potential
“get-out-of-jail-free card.” Ante, at 8. It adds that the
“social costs” of applying the exclusionary rule here are
not worth the deterrence benefits. Ante, at 13. Leaving
aside what I believe are invalid arguments based on
precedent or the majority’s own estimate that suppression
is not necessary to deter constitutional violations, one is
left with a simple unvarnished conclusion, namely, that in
this kind of case, a knock-and-announce case, “[r]esort to
the massive remedy of suppressing evidence of guilt is
                 Cite as: 547 U. S. ____ (2006)           27

                     BREYER, J., dissenting

unjustified.” Ibid. Why is that judicial judgment, taken
on its own, inappropriate? Could it not be argued that the
knock-and-announce rule, a subsidiary Fourth Amend
ment rule, is simply not important enough to warrant a
suppression remedy? Could the majority not simply claim
that the suppression game is not worth the candle?
  The answer, I believe, is “no.” That “no” reflects history,
a history that shows the knock-and-announce rule is
important. See Wilson, supra, at 931–936. That “no”
reflects precedent, precedent that shows there is no pre
existing legal category of exceptions to the exclusionary
rule into which the knock-and-announce cases might fit.
See supra, at 8–9. That “no” reflects empirical fact, ex
perience that provides confirmation of what common sense
suggests: without suppression there is little to deter
knock-and-announce violations. See supra, at 6–7.
  There may be instances in the law where text or history
or tradition leaves room for a judicial decision that rests
upon little more than an unvarnished judicial instinct.
But this is not one of them. Rather, our Fourth Amend
ment traditions place high value upon protecting privacy
in the home. They emphasize the need to assure that its
constitutional protections are effective, lest the Amend
ment ‘sound the word of promise to the ear but break it to
the hope.’ They include an exclusionary principle, which
since Weeks has formed the centerpiece of the criminal
law’s effort to ensure the practical reality of those prom
ises. That is why the Court should assure itself that any
departure from that principle is firmly grounded in logic,
in history, in precedent, and in empirical fact. It has not
done so. That is why, with respect, I dissent.
28                  HUDSON v. MICHIGAN

                Appendix to opinion of BREYER, J.

        APPENDIX TO OPINION OF BREYER, J.
  Fourth Amendment decisions from 1914 to present
requiring suppression of evidence seized (or remanding for
lower court to make suppression determination) in a pri
vate home following an illegal arrest or search:
      1. 	 eeks v. United States, 232 U. S. 383 (1914) (war
          W
          rantless search)
      2. 	 mos v. United States, 255 U. S. 313 (1921) (war
          A
          rantless arrest and search)
      3. 	 gnello v. United States, 269 U. S. 20 (1925) (war
          A
          rantless search)
      4. 	 yars v. United States, 273 U. S. 28 (1927) (inva
          B
          lid warrant)
      5. 	 nited States v. Berkeness, 275 U. S. 149 (1927)
          U
          (invalid warrant; insufficient affidavit)
      6. 	 aylor v. United States, 286 U. S. 1 (1932) (war
          T
          rantless search)
      7. 	 rau v. United States, 287 U. S. 124 (1932) (inva
          G
          lid warrant; insufficient affidavit)
      8. 	 athanson v. United States, 290 U. S. 41 (1933)
          N
          (invalid warrant; insufficient affidavit)
      9. 	 cDonald v. United States, 335 U. S. 451 (1948)
          M
          (warrantless arrest and search)
     10. 	Kremen v. United States, 353 U. S. 346 (1957) (per
          curiam) (warrantless search)
     11. 	Elkins v. United States, 364 U. S. 206 (1960)
          (search beyond scope of warrant)
     12. 	Silverman v. United States, 365 U. S. 505 (1961)
          (warrantless use of electronic device)
     13. 	Chapman v. United States, 365 U. S. 610 (1961)
          (warrantless search)
     14. 	Mapp v. Ohio, 367 U. S. 643 (1961) (warrantless
          search)
     15. 	Wong Sun v. United States, 371 U. S. 471 (1963)
          (warrantless search and arrest)
             Cite as: 547 U. S. ____ (2006)          29

           Appendix to opinion of BREYER, J.

16. 	Fahy v. Connecticut, 375 U. S. 85 (1963) (war
     rantless search)
17. 	Aguilar v. Texas, 378 U. S. 108 (1964) (invalid
     warrant; insufficient affidavit)
18. 	Stanford v. Texas, 379 U. S. 476 (1965) (invalid
     warrant; particularity defect)
19. 	James v. Louisiana, 382 U. S. 36 (1965) (per cu
     riam) (warrantless search)
20. 	Riggan v. Virginia, 384 U. S. 152 (1966) (per cu
     riam) (invalid warrant; insufficient affidavit)
21. 	Bumper v. North Carolina, 391 U. S. 543 (1968)
     (lack of valid consent to search)
22. 	Recznik v. City of Lorain, 393 U. S. 166 (1968)
     (per curiam) (warrantless search)
23. 	Chimel v. California, 395 U. S. 752 (1969) (invalid
     search incident to arrest)
24. 	Von Cleef v. New Jersey, 395 U. S. 814 (1969) (per
     curiam) (invalid search incident to arrest)
25. 	Shipley v. California, 395 U. S. 818 (1969) (per
     curiam) (invalid search incident to arrest)
26. 	Vale v. Louisiana, 399 U. S. 30 (1970) (invalid
     search incident to arrest)
27. 	Connally v. Georgia, 429 U. S. 245 (1977) (per cu
     riam) (invalid warrant; magistrate judge not neu
     tral)
28. 	Michigan v. Tyler, 436 U. S. 499 (1978) (war
     rantless search)
29. 	Mincey v. Arizona, 437 U. S. 385 (1978) (war
     rantless search)
30. 	Franks v. Delaware, 438 U. S. 154 (1978) (invalid
     warrant; obtained through perjury)
31. 	Payton v. New York, 445 U. S. 573 (1980) (war
     rantless arrest)
32. 	Steagald v. United States, 451 U. S. 204 (1981)
     (warrantless search)
33. 	Michigan v. Clifford, 464 U. S. 287 (1984) (war
30                  HUDSON v. MICHIGAN

                Appendix to opinion of BREYER, J.

          rantless search)
     34. 	Welsh v. Wisconsin, 466 U. S. 740 (1984) (war
          rantless entry into home without exigent circum
          stances)
     35. 	Thompson v. Louisiana, 469 U. S. 17 (1984) (per
          curiam) (warrantless search)
     36. 	Arizona v. Hicks, 480 U. S. 321 (1987) (unreason
          able search)
     37. 	Minnesota v. Olson, 495 U. S. 91 (1990) (war
          rantless entry into home)
     38. 	Flippo v. West Virginia, 528 U. S. 11 (1999) (per
          curiam) (warrantless search)
     39. 	Kyllo v. United States, 533 U. S. 27 (2001) (war
          rantless use of heat-imaging technology)
     40. 	Kirk v. Louisiana, 536 U. S. 635 (2002) (per cu
          riam) (warrantless arrest and search)
     41. 	Kaupp v. Texas, 538 U. S. 626 (2003) (per curiam)
          (warrantless search)

```

---

## GROUP: content/cases/Hudson v. Palmer.md  (`case`, 5 assertions)

### content_page

```
---
title: "Hudson v. Palmer"
type: case
citation: "468 U.S. 517 (1984)"
parallel_cite: "104 S. Ct. 3194; 82 L. Ed. 2d 393; 52 U.S.L.W. 5052"
neutral_cite: 1984 U.S. LEXIS 143
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-07-03
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-07-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hudson v. Palmer
  varies_by_point: false
  scope_note: "Good law; a prisoner has no Fourth Amendment reasonable expectation of privacy in his cell. (The companion holding on intentional property deprivations and adequate post-deprivation remedies — the Parratt-Hudson doctrine — is a Fourteenth Amendment due-process matter outside this Fourth Amendment home.)"
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111252/hudson-v-palmer/"
  cluster_id: 111252
  opinion_id: 9429735
  identity_checked: true
homes:
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Key — REP boundary"
related: ["[[Katz v. United States]]", "[[Maryland v. King]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "prisoner", "reasonable-expectation-of-privacy", "prison-cell"]
holding: "A prisoner has no reasonable expectation of privacy in his prison cell; the Fourth Amendment's proscription against unreasonable searches does not apply within the cell."
lake:
  record_id: Hudson v. Palmer
  status: verified
  projected_at: 2026-07-06
---

# Hudson v. Palmer

*468 U.S. 517 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A prison officer conducted a "shakedown" search of inmate Palmer's cell and locker and, Palmer alleged, destroyed some of his noncontraband personal property. Palmer sued under § 1983, claiming the search violated his Fourth Amendment privacy rights and the property destruction violated due process.

## Issue
Whether a prisoner has a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in his prison cell entitling him to Fourth Amendment protection against searches of the cell.

## Rule
No. "[W]e hold that society is not prepared to recognize as legitimate any subjective expectation of privacy that a prisoner might have in his prison cell and that, accordingly, the Fourth Amendment proscription against unreasonable searches does not apply within the confines of the prison cell. The recognition of privacy rights for prisoners in their individual cells simply cannot be reconciled with the concept of incarceration and the needs and objectives of penal institutions." — 468 U.S. at 526. ^pin-526

## Application
The officer's shakedown of Palmer's cell could not be a Fourth Amendment violation because Palmer had no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the cell at all. The close and continual surveillance necessary to maintain institutional security and internal order is fundamentally incompatible with any such expectation; a prisoner's cell is not a constitutionally protected private space. (Palmer's distinct claim that the officer destroyed his property was analyzed under the Due Process Clause, not the Fourth Amendment.)

## Conclusion
A prison cell is outside the Fourth Amendment's protection against unreasonable searches; the shakedown stated no Fourth Amendment claim. *Hudson* marks the outer boundary of the reasonable-expectation-of-privacy inquiry in the custodial setting.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Defines a boundary of the [[Katz v. United States]] reasonable-expectation-of-privacy test; the diminished privacy of those in custody also informs arrestee-search cases such as [[Maryland v. King]].

## Appears on
- [[Reasonable Expectation of Privacy]] — *Key — REP boundary*

## Sources
- *Hudson v. Palmer*, 468 U.S. 517 (1984) — https://www.courtlistener.com/opinion/111252/hudson-v-palmer/ — pinpoint: 526.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6eb385a3c6b070af", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "468 U.S. 517 (1984)", "court": "U.S. Supreme Court", "neutral_cite": "1984 U.S. LEXIS 143", "official_citation_present": true, "parallel_cite": "104 S. Ct. 3194; 82 L. Ed. 2d 393; 52 U.S.L.W. 5052", "title": "Hudson v. Palmer", "year": "1984"}}
{"assertion_id": "1018174988603cd6", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A prisoner has no reasonable expectation of privacy in his prison cell; the Fourth Amendment's proscription against unreasonable searches does not apply within the cell.", "title": "Hudson v. Palmer"}}
{"assertion_id": "ced090fdc5785ecd", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Expectation of Privacy"}, "payload": {"home": "Reasonable Expectation of Privacy", "role": "Key — REP boundary", "title": "Hudson v. Palmer"}}
{"assertion_id": "050771cd35865e21", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Hudson v. Palmer"}}
{"assertion_id": "65f8dcd04a77ade5", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1984-07-03", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Hudson v. Palmer", "field_i_validity": "good_law", "scope_note": "Good law; a prisoner has no Fourth Amendment reasonable expectation of privacy in his cell. (The companion holding on intentional property deprivations and adequate post-deprivation remedies — the Parratt-Hudson doctrine — is a Fourteenth Amendment due-process matter outside this Fourth Amendment home.)", "title": "Hudson v. Palmer", "varies_by_point": "false"}}
```

### lake record — Hudson v. Palmer

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hudson v. Palmer",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hudson v. Palmer",
    "case_name_short": "Hudson",
    "case_name_full": "Hudson v. Palmer",
    "input_case_name": "Hudson v. Palmer",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-07-03",
    "year": 1984,
    "docket": null,
    "cluster_id": 111252,
    "lead_opinion_id": 9429735,
    "sibling_ids": [
      111252,
      9429735,
      9429736,
      9429737
    ],
    "absolute_url": "/opinion/111252/hudson-v-palmer/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "468 U.S. 517",
      "volume": "468",
      "reporter": "U.S.",
      "page": "517",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 3194",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3194",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 393",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "393",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 5052",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "5052",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 143",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "143",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "468 U.S. 517",
        "volume": "468",
        "reporter": "U.S.",
        "page": "517",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 3194",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3194",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 393",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "393",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 143",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "143",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 5052",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "5052",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "468 U.S. 517",
    "official_selection": {
      "court_class": "scotus",
      "selected": "468 U.S. 517",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-526",
      "page": null,
      "quote": "search of inmate Palmer's cell and locker and, Palmer alleged, destroyed some of his noncontraband personal property. Palmer sued under \u00a7 1983, claiming the search violated his Fourth Amendment privacy rights and the property destruction violated due process. ## Issue Whether a prisoner has a reasonable expectation of privacy in his prison cell entitling him to Fourth Amendment protection against searches of the cell. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-07-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hudson v. Palmer",
    "varies_by_point": false,
    "scope_note": "Good law; a prisoner has no Fourth Amendment reasonable expectation of privacy in his cell. (The companion holding on intentional property deprivations and adequate post-deprivation remedies \u2014 the Parratt-Hudson doctrine \u2014 is a Fourteenth Amendment due-process matter outside this Fourth Amendment home.)",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4603999,
          "cite": [
            "119 N.E.3d 669",
            "481 Mass. 710"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "in the Interest of L.N.C & K.N.M., Children",
          "cluster_id": 4586474,
          "cite": [
            "573 S.W.3d 309"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Louisiana v. Keith C. Kisack",
          "cluster_id": 4435443,
          "cite": [
            "236 So. 3d 1201"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane1_negative"
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
        "journal_ref": "Hudson v. Palmer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Farmer v. Brennan",
          "cluster_id": 1087956,
          "cite": [
            "128 L. Ed. 2d 811",
            "114 S. Ct. 1970",
            "511 U.S. 825",
            "1994 U.S. LEXIS 4274"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hudson v. McMillian",
          "cluster_id": 112693,
          "cite": [
            "117 L. Ed. 2d 156",
            "112 S. Ct. 995",
            "503 U.S. 1",
            "1992 U.S. LEXIS 1372"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Daniels v. Williams",
          "cluster_id": 111555,
          "cite": [
            "88 L. Ed. 2d 662",
            "106 S. Ct. 662",
            "474 U.S. 327",
            "1986 U.S. LEXIS 43",
            "54 U.S.L.W. 4090"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
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
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whitley v. Albers",
          "cluster_id": 111610,
          "cite": [
            "89 L. Ed. 2d 251",
            "106 S. Ct. 1078",
            "475 U.S. 312",
            "1986 U.S. LEXIS 28",
            "54 U.S.L.W. 4236"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zinermon v. Burch",
          "cluster_id": 2620710,
          "cite": [
            "108 L. Ed. 2d 100",
            "110 S. Ct. 975",
            "494 U.S. 113",
            "1990 U.S. LEXIS 1171"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
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
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williamson County Regional Planning Commission v. Hamilton Bank of Johnson City",
          "cluster_id": 111501,
          "cite": [
            "87 L. Ed. 2d 126",
            "105 S. Ct. 3108",
            "473 U.S. 172",
            "1985 U.S. LEXIS 87",
            "53 U.S.L.W. 4969"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
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
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alden v. Maine",
          "cluster_id": 118318,
          "cite": [
            "144 L. Ed. 2d 636",
            "119 S. Ct. 2240",
            "527 U.S. 706",
            "1999 U.S. LEXIS 4374"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davidson v. Cannon",
          "cluster_id": 111556,
          "cite": [
            "88 L. Ed. 2d 677",
            "106 S. Ct. 668",
            "474 U.S. 344",
            "1986 U.S. LEXIS 44",
            "54 U.S.L.W. 4095"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
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
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania Department of Corrections v. Yeskey",
          "cluster_id": 118228,
          "cite": [
            "141 L. Ed. 2d 215",
            "118 S. Ct. 1952",
            "524 U.S. 206",
            "1998 U.S. LEXIS 3888"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan Department of State Police v. Sitz",
          "cluster_id": 112459,
          "cite": [
            "110 L. Ed. 2d 412",
            "110 S. Ct. 2481",
            "496 U.S. 444",
            "1990 U.S. LEXIS 3144",
            "58 U.S.L.W. 4781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
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
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clarence Erwin Copeland v. Mark MacHulis James Stephens",
          "cluster_id": 697696,
          "cite": [
            "57 F.3d 476",
            "1995 U.S. App. LEXIS 14483",
            "1995 WL 351078"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
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
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cleavinger v. Saxner",
          "cluster_id": 111547,
          "cite": [
            "88 L. Ed. 2d 507",
            "106 S. Ct. 496",
            "474 U.S. 193",
            "1985 U.S. LEXIS 148",
            "54 U.S.L.W. 4048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gee v. Pacheco",
          "cluster_id": 178001,
          "cite": [
            "627 F.3d 1178",
            "2010 WL 4909644"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Overton v. Bazzetta",
          "cluster_id": 130150,
          "cite": [
            "156 L. Ed. 2d 162",
            "123 S. Ct. 2162",
            "539 U.S. 126",
            "2003 U.S. LEXIS 4781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
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
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Samson v. California",
          "cluster_id": 145640,
          "cite": [
            "165 L. Ed. 2d 250",
            "126 S. Ct. 2193",
            "547 U.S. 843",
            "2006 U.S. LEXIS 4885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "L.R. Bretz v. Zollie Kelman, Jack R. Lande, Eugene R. Welborn",
          "cluster_id": 458756,
          "cite": [
            "773 F.2d 1026",
            "1985 U.S. App. LEXIS 23482"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hudson v. Palmer:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111252 OR 9429735 OR 9429736 OR 9429737) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDQ1Mjk5MjAwMDAwJnM9MzEzMjc0MSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111252+OR+9429735+OR+9429736+OR+9429737%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 4,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 4,
        "triage_snippet_classified": 196
      },
      "lane2_top_cited": {
        "query": "cites:(111252 OR 9429735 OR 9429736 OR 9429737)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02MDEmcz02NjE3MzQmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111252+OR+9429735+OR+9429736+OR+9429737%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111252 OR 9429735 OR 9429736 OR 9429737)",
        "reviewed": 37,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 37,
        "triage_read": 0,
        "triage_snippet_classified": 37
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111252 OR 9429735 OR 9429736 OR 9429737)",
    "indexed_citing_opinions": 2514,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111252,
        "count": 2245,
        "count_source": "search"
      },
      {
        "opinion_id": 9429735,
        "count": 301,
        "count_source": "search"
      },
      {
        "opinion_id": 9429736,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429737,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 8082,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hudson-v-palmer.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MTQ1MzQmcz0xMDAyNDc3NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111252+OR+9429735+OR+9429736+OR+9429737%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111252,
        "cited_id": 99464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 103017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 103870,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 104557,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 106425,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 106629,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 106889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 107122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 107630,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 107840,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108414,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108431,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108484,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 108995,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109008,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109016,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109080,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109402,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109476,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109921,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 109969,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110085,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110319,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110352,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110362,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110518,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110593,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110657,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110753,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110770,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110829,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110900,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 111121,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 111167,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 111195,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 111224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 111227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 306226,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 310105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 311474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 312857,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 321294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 327723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 328221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 328865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 340703,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 343130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 355329,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 356030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 392146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 393729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 395225,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 400069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 403393,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 403670,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 407932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 410403,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 413271,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 413393,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 414190,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 416902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 421697,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 431085,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 1302147,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 1304356,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 1384033,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 1443669,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 1460980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 1686657,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 1870743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111252,
        "cited_id": 1905445,
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
    "date_created": "2026-07-05T07:43:25Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:43:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:43:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:47:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:43:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hudson v. Palmer

```
<opinion type="majority">
<author id="A0R">Chief Justice Burger</author>
<p id="AGO">delivered the opinion of the Court.</p>
<p id="ApP">We granted certiorari in No. 82-1630 to decide whether a prison inmate has a reasonable expectation of privacy in his prison cell entitling him to the protection of the Fourth Amendment against unreasonable searches and seizures. We also granted certiorari in No. 82-6695, the cross-petition, to determine whether our decision in <em>Parratt </em>v. <em>Taylor, </em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">451 U. S. 527</a></span> (1981), which held that a negligent deprivation of property by state officials does not violate the Fourteenth Amendment if an adequate postdeprivation state remedy exists, should extend to intentional deprivations of property.</p>
<p id="Ach">I</p>
<p id="A0V">The facts underlying this dispute are relatively simple. Respondent Palmer is an inmate at the Bland Correctional Center in Bland, Va., serving sentences for forgery, uttering, grand larceny, and bank robbery convictions. On September 16, 1981, petitioner Hudson, an officer at the Correctional Center, with a fellow officer, conducted a “shakedown” search of respondent’s prison locker and cell for contraband. During the “shakedown,” the officers discovered a ripped pillowcase in a trash can near respondent’s cell bunk. Charges <page-number citation-index="1" label="520">*520</page-number>against Palmer were instituted under the prison disciplinary-procedures for destroying state property. After a hearing, Palmer was found guilty on the charge and was ordered to reimburse the State for the cost of the material destroyed; in addition, a reprimand was entered on his prison record.</p>
<p id="b562-5">Palmer subsequently brought this <em>pro se </em>action in United States District Court under <span class="citation no-link">42 U. S. C. § 1983</span>. Respondent claimed that Hudson had conducted the shakedown search of his cell and had brought a false charge against him solely to harass him, and that, in violation of his Fourteenth Amendment right not to be deprived of property without due process of law, Hudson had intentionally destroyed certain of his noncontraband personal property during the September 16 search. Hudson denied each allegation; he moved for and was granted summary judgment. The District Court accepted respondent’s allegations as true but held nonetheless, relying on <em>Parratt </em>v. <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Taylor, supra,</a></span> </em>that the alleged destruction of respondent’s property, even if intentional, did not violate the Fourteenth Amendment because there were state tort remedies available to redress the deprivation, App. 31<footnotemark>1</footnotemark> and that the alleged harassment did not "rise to the level of a constitutional deprivation,” <em>id., </em>at 32.</p>
<p id="b562-6">The Court of Appeals affirmed in part, reversed in part, and remanded for further proceedings. <span class="citation" data-id="413271"><a href="/opinion/413271/russell-thomas-palmer-jr-v-ted-s-hudson-officer/" aria-description="Citation for case: Russell Thomas Palmer, Jr. v. Ted S. Hudson, Officer">697 F. 2d 1220</a></span> (CA4 1983). The court affirmed the District Court’s holding that respondent was not deprived of his property without due process. The court acknowledged that we considered only a claim of negligent property deprivation in <em>Parratt </em>v. <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Taylor, supra.</a></span> </em>It agreed with the District Court, however, that the logic of <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span> </em>applies equally to unauthorized intentional deprivations of property by state officials: “[O]nce it is as<page-number citation-index="1" label="521">*521</page-number>sumed that a postdeprivation remedy can cure an unintentional but negligent act causing injury, inflicted by a state agent which is unamenable to prior review, then that principle applies as well to random and unauthorized intentional acts.” <span class="citation" data-id="413271"><a href="/opinion/413271/russell-thomas-palmer-jr-v-ted-s-hudson-officer/#1223" aria-description="Citation for case: Russell Thomas Palmer, Jr. v. Ted S. Hudson, Officer">697 F. 2d, at 1223</a></span>.<footnotemark>2</footnotemark> The Court of Appeals did not discuss the availability and adequacy of existing state-law remedies; it presumably accepted as correct the District Court’s statement of the remedies available under Virginia law.<footnotemark>3</footnotemark></p>
<p id="b563-5">The Court of Appeals reversed the summary judgment on respondent’s claim that the shakedown search was unreasonable. The court recognized that <em>Bell </em>v. <em>Wolfish, </em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#555" aria-description="Citation for case: Bell v. Wolfish">441 U. S. 520, 555-557</a></span> (1979), authorized irregular unannounced shakedown searches of prison cells. But the court held that an individual prisoner has a “limited privacy right” in his cell entitling him to protection against searches conducted solely to harass or to humiliate. <span class="citation" data-id="413271"><a href="/opinion/413271/russell-thomas-palmer-jr-v-ted-s-hudson-officer/#1225" aria-description="Citation for case: Russell Thomas Palmer, Jr. v. Ted S. Hudson, Officer">697 F. 2d, at 1225</a></span>.<footnotemark>4</footnotemark> The shakedown of a single prisoner’s property, said the court, is permissible <page-number citation-index="1" label="522">*522</page-number>only if “done pursuant to an established program of conducting random searches of single cells or groups of cells reasonably designed to deter or discover the possession of contraband” or upon reasonable belief that the particular prisoner possessed contraband. <span class="citation" data-id="413271"><a href="/opinion/413271/russell-thomas-palmer-jr-v-ted-s-hudson-officer/#1224" aria-description="Citation for case: Russell Thomas Palmer, Jr. v. Ted S. Hudson, Officer"><em>Id., </em>at 1224</a></span>. Because the Court of Appeals concluded that the record reflected a factual dispute over whether the search of respondent’s cell was routine or conducted to harass respondent, it held that summary judgment was inappropriate, and that a remand was necessary to determine the purpose of the cell search.</p>
<p id="b564-4">We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./463/1206/">463 U. S. 1206</a></span> (1983). We affirm in part and reverse in part.</p>
<p id="b564-5">II</p>
<p id="b564-6">A</p>
<p id="b564-7">The first question we address is whether respondent has a right of privacy in his prison cell entitling him to the protection of the Fourth Amendment against unreasonable searches.<footnotemark>5</footnotemark> As we have noted, the Court of Appeals held that the District Court’s summary judgment in petitioner’s favor was premature because respondent had a “limited privacy right” in his cell that might have been breached. The court concluded that, to protect this privacy right, shakedown searches of an individual’s cell should be performed only “pursuant to an established program of conducting ran<page-number citation-index="1" label="523">*523</page-number>dom searches . . . reasonably designed to deter or discover the possession of contraband” or upon reasonable belief that the prisoner possesses contraband. Petitioner contends that the Court of Appeals erred in holding that respondent had even a limited privacy right in his cell, and urges that we adopt the “bright line” rule that prisoners have no legitimate expectation of privacy in their individual cells that would entitle them to Fourth Amendment protection.</p>
<p id="b565-5">We have repeatedly held that prisons are not beyond the reach of the Constitution. No “iron curtain” separates one from the other. <em>Wolff </em>v. <em>McDonnell, </em><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#555" aria-description="Citation for case: Wolff v. McDonnell">418 U. S. 539, 555</a></span> (1974). Indeed, we have insisted that prisoners be accorded those rights not fundamentally inconsistent with imprisonment itself or incompatible with the objectives of incarceration. For example, we have held that invidious racial discrimination is as intolerable within a prison as outside, except as may be essential to “prison security and discipline.” <em>Lee </em>v. <em>Washington, </em><span class="citation" data-id="9423632"><a href="/opinion/107630/lee-v-washington/" aria-description="Citation for case: Lee v. Washington">390 U. S. 333</a></span> (1968) <em>(per curiam). </em>Like others, prisoners have the constitutional right to petition the Government for redress of their grievances, which includes a reasonable right of access to the courts. <em>Johnson </em>v. <em>Avery, </em><span class="citation" data-id="9423904"><a href="/opinion/107840/johnson-v-avery/" aria-description="Citation for case: Johnson v. Avery">393 U. S. 483</a></span> (1969).</p>
<p id="b565-6">Prisoners must be provided “reasonable opportunities” to exercise their religious freedom guaranteed under the First Amendment. <em>Cruz </em>v. <em>Beto, </em><span class="citation" data-id="9424773"><a href="/opinion/108484/cruz-v-beto/" aria-description="Citation for case: Cruz v. Beto">405 U. S. 319</a></span> (1972) <em>(per curiam). </em>Similarly, they retain those First Amendment rights of speech “not inconsistent with [their] status as . . . prisoners] or with the legitimate penological objectives of the corrections system.” <em>Pell </em>v. <em>Procunier, </em><span class="citation" data-id="9425783"><a href="/opinion/109079/pell-v-procunier/#822" aria-description="Citation for case: Pell v. Procunier">417 U. S. 817, 822</a></span> (1974). They enjoy the protection of due process. <em>Wolff </em>v. <em><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/" aria-description="Citation for case: Wolff v. McDonnell">McDonnell, supra;</a></span> Haines </em>v. <em>Kerner, </em><span class="citation" data-id="108432"><a href="/opinion/108432/haines-v-kerner/" aria-description="Citation for case: Haines v. Kerner">404 U. S. 519</a></span> (1972). And the Eighth Amendment ensures that they will not be subject to “cruel and unusual punishments.” <em>Estelle </em>v. <em>Gamble, </em><span class="citation" data-id="9426610"><a href="/opinion/109561/estelle-v-gamble/" aria-description="Citation for case: Estelle v. Gamble">429 U. S. 97</a></span> (1976). The continuing guarantee of these substantial rights to prison inmates is testimony to a belief that the way a society treats those who have trans<page-number citation-index="1" label="524">*524</page-number>gressed against it is evidence of the essential character of that society.</p>
<p id="b566-5">However, while persons imprisoned for crime enjoy many protections of the Constitution, it is also clear that imprisonment carries with it the circumscription or loss of many significant rights. See <em>Bell </em>v. <em>Wolfish, </em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#545" aria-description="Citation for case: Bell v. Wolfish">441 U. S., at 545</a></span>. These constraints on inmates, and in some cases the complete withdrawal of certain rights, are “justified by the considerations underlying our penal system.” <em>Price </em>v. <em>Johnston, </em><span class="citation" data-id="9420168"><a href="/opinion/104557/price-v-johnston/#285" aria-description="Citation for case: Price v. Johnston">334 U. S. 266, 285</a></span> (1948); see also <em>Bell </em>v. <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Wolfish, supra,</a></span> </em>at 545-546 and cases cited; <em>Wolff </em>v. <span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#555" aria-description="Citation for case: Wolff v. McDonnell"><em>McDonnell, supra, </em>at 555</a></span>. The curtailment of certain rights is necessary, as a practical matter, to accommodate a myriad of “institutional needs and objectives” of prison facilities, <em>Wolff </em>v. <span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#555" aria-description="Citation for case: Wolff v. McDonnell"><em>McDonnell, supra, </em>at 555</a></span>, chief among which is internal security, see <em>Pell </em>v. <span class="citation" data-id="9425783"><a href="/opinion/109079/pell-v-procunier/#823" aria-description="Citation for case: Pell v. Procunier"><em>Procunier, supra, </em>at 823</a></span>. Of course, these restrictions or retractions also serve, incidentally, as reminders that, under our system of justice, deterrence and retribution are factors in addition to correction.</p>
<p id="b566-6">We have not before been called upon to decide the specific question whether the Fourth Amendment applies within a prison cell,<footnotemark>6</footnotemark> but the nature of our inquiry is well defined. <page-number citation-index="1" label="525">*525</page-number>We must determine here, as in other Fourth Amendment contexts, if a “justifiable” expectation of privacy is at stake. <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967). The applicability of the Fourth Amendment turns on whether “the person invoking its protection can claim a ‘justifiable/ a ‘reasonable/ or a ‘legitimate expectation of privacy’ that has been invaded by government action.” <em>Smith </em>v. <em>Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#740" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735, 740</a></span> (1979), and cases cited. We must decide, in Justice Harlan’s words, whether a prisoner’s expectation of privacy in his prison cell is the kind of expectation that “society is prepared to recognize as ‘reasonable.’ ” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States"><em>Katz, supra, </em>at 360, 361</a></span> (concurring opinion).<footnotemark>7</footnotemark></p>
<p id="b567-5">Notwithstanding our caution in approaching claims that the Fourth Amendment is inapplicable in a given context, we <page-number citation-index="1" label="526">*526</page-number>hold that society is not prepared to recognize as legitimate any subjective expectation of privacy that a prisoner might have in his prison cell and that, accordingly, the Fourth Amendment proscription against unreasonable searches does not apply within the confines of the prison cell. The recognition of privacy rights for prisoners in their individual cells simply cannot be reconciled with the concept of incarceration and the needs and objectives of penal institutions.</p>
<p id="b568-5">Prisons, by definition, are places of involuntary confinement of persons who have a demonstrated proclivity for antisocial criminal, and often violent, conduct. Inmates have necessarily shown a lapse in ability to control and conform their behavior to the legitimate standards of society by the normal impulses of self-restraint; they have shown an inability to regulate their conduct in a way that reflects either a respect for law or an appreciation of the rights of others. Even a partial survey of the statistics on violent crime in our Nation’s prisons illustrates the magnitude of the problem. During 1981 and the first half of 1982, there were over 120 prisoners murdered by fellow inmates in state and federal prisons. A number of prison personnel were murdered by prisoners during this period. Over 29 riots or similar disturbances were reported in these facilities for the same time frame. And there were over 125 suicides in these institutions. See Prison Violence, 7 Corrections Compendium (Mar. 1983). Additionally, informal statistics from the United States Bureau of Prisons show that in the federal system during 1983, there were 11 inmate homicides, 359 inmate assaults on other inmates, 227 inmate assaults on prison staff, and 10 suicides. There were in the same system in 1981 and 1982 over 750 inmate assaults on other inmates and over 570 inmate assaults on prison personnel.</p>
<p id="b568-6">Within this volatile “community,” prison administrators are to take all necessary steps to ensure the safety of not only the prison staffs and administrative personnel, but also visitors. They are under an obligation to take reasonable <page-number citation-index="1" label="527">*527</page-number>measures to guarantee the safety of the inmates themselves. They must be ever alert to attempts to introduce drugs and other contraband into the premises which, we can judicially notice, is one of the most perplexing problems of prisons today; they must prevent, so far as possible, the flow of illicit weapons into the prison; they must be vigilant to detect escape plots, in which drugs or weapons may be involved, before the schemes materialize. In addition to these monumental tasks, it is incumbent upon these officials at the same time to maintain as sanitary an environment for the inmates as feasible, given the difficulties of the circumstances.</p>
<p id="b569-5">The administration of a prison, we have said, is “at best an extraordinarily difficult undertaking.” <em>Wolff </em>v. <em>McDonnell, </em><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#566" aria-description="Citation for case: Wolff v. McDonnell">418 U. S., at 566</a></span>; <em>Hewitt </em>v. <em>Helms, </em><span class="citation" data-id="9429000"><a href="/opinion/110829/hewitt-v-helms/#467" aria-description="Citation for case: Hewitt v. Helms">459 U. S. 460, 467</a></span> (1983). But it would be literally impossible to accomplish the prison objectives identified above if inmates retained a right of privacy in their cells. Virtually the only place inmates can conceal weapons, drugs, and other contraband is in their cells. Unfettered access to these cells by prison officials, thus, is imperative if drugs and contraband are to be ferreted out and sanitary surroundings are to be maintained.</p>
<p id="b569-6">Determining whether an expectation of privacy is “legitimate” or “reasonable” necessarily entails a balancing of interests. The two interests here are the interest of society in the security of its penal institutions and the interest of the prisoner in privacy within his cell. The latter interest, of course, is already limited by the exigencies of the circumstances: A prison “shares none of the attributes of privacy of a home, an automobile, an office, or a hotel room.” <em>Lanza </em>v. <em>New York, </em><span class="citation" data-id="9422429"><a href="/opinion/106425/lanza-v-new-york/#143" aria-description="Citation for case: Lanza v. New York">370 U. S. 139, 143-144</a></span> (1962). We strike the balance in favor of institutional security, which we have noted is “central to all other corrections goals,” <em>Pell </em>v. <em>Procunier, </em><span class="citation" data-id="9425783"><a href="/opinion/109079/pell-v-procunier/#823" aria-description="Citation for case: Pell v. Procunier">417 U. S., at 823</a></span>. A right of privacy in traditional Fourth Amendment terms is fundamentally incompatible with the close and continual surveillance of inmates and their cells <page-number citation-index="1" label="528">*528</page-number>required to ensure institutional security and internal order.<footnotemark>8</footnotemark> We are satisfied that society would insist that the prisoner's expectation of privacy always yield to what must be considered the paramount interest in institutional security. We believe that it is accepted by our society that “[l]oss of freedom of choice and privacy are inherent incidents of confinement.” <em>Bell </em>v. Wolfish, <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#537" aria-description="Citation for case: Bell v. Wolfish">441 U. S., at 537</a></span>.</p>
<p id="b570-5">The Court of Appeals was troubled by the possibility of searches conducted solely to harass inmates; it reasoned that a requirement that searches be conducted only pursuant to an established policy or upon reasonable suspicion would prevent such searches to the maximum extent possible. Of course, there is a risk of maliciously motivated searches, and of course, intentional harassment of even the most hardened criminals cannot be tolerated by a civilized society. However, we disagree with the court’s proposed solution. The uncertainty that attends random searches of cells renders these searches perhaps the most effective weapon of the prison administrator in the constant fight against the proliferation of knives and guns, illicit drugs, and other contraband. The Court of Appeals candidly acknowledged that “the device [of random cell searches] is of. . . obvious utility in achieving the goal of prison security.” <span class="citation" data-id="413271"><a href="/opinion/413271/russell-thomas-palmer-jr-v-ted-s-hudson-officer/#1224" aria-description="Citation for case: Russell Thomas Palmer, Jr. v. Ted S. Hudson, Officer">697 F. 2d, at 1224</a></span>.</p>
<p id="b571-4"><page-number citation-index="1" label="529">*529</page-number>A requirement that even random searches be conducted pursuant to an established plan would seriously undermine the effectiveness of this weapon. It is simply naive to believe that prisoners would not eventually decipher any plan officials might devise for “planned random searches,” and thus be able routinely to anticipate searches. The Supreme Court of Virginia identified the shortcomings of an approach such as that adopted by the Court of Appeals and the necessity of allowing prison administrators flexibility:</p>
<blockquote id="b571-5">“For one to advocate that prison searches must be conducted only pursuant to an enunciated general policy or when suspicion is directed at a particular inmate is to ignore the realities of prison operation. Random searches of inmates, individually or collectively, and their cells and lockers are valid and necessary to ensure the security of the institution and the safety of inmates and all others within its boundaries. This type of search allows prison officers flexibility and prevents inmates from anticipating, and thereby thwarting, a search for contraband.” <em>Marrero </em>v. <em>Commonwealth, </em><span class="citation" data-id="1302147"><a href="/opinion/1302147/marrero-v-commonwealth/#757" aria-description="Citation for case: Marrero v. Commonwealth">222 Va. 754, 757</a></span>, <span class="citation" data-id="1302147"><a href="/opinion/1302147/marrero-v-commonwealth/#811" aria-description="Citation for case: Marrero v. Commonwealth">284 S. E. 2d 809, 811</a></span> (1981).</blockquote>
<p id="b571-6">We share the concerns so well expressed by the Supreme Court and its view that wholly random searches are essential to the effective security of penal institutions. We, therefore, cannot accept even the concededly limited holding of the Court of Appeals.</p>
<p id="b571-7">Respondent acknowledges that routine shakedowns of prison cells are essential to the effective administration of prisons. Brief for Respondent and Cross-Petitioner 7, n. 5. He contends, however, that he is constitutionally entitled not to be subjected to searches conducted only to harass. The crux of his claim is that “because searches and seizures to harass are unreasonable, a prisoner has a reasonable expectation of privacy not to have his cell, locker, personal effects, person invaded for such a purpose.”, <em>Id., </em>at 24. This argu<page-number citation-index="1" label="530">*530</page-number>ment, which assumes the answer to the predicate question whether a prisoner has a legitimate expectation of privacy in his prison cell at all, is merely a challenge to the reasonableness of the particular search of respondent’s cell. Because we conclude that prisoners have no legitimate expectation of privacy and that the Fourth Amendment’s prohibition on unreasonable searches does not apply in prison cells, we need not address this issue.</p>
<p id="b572-5">Our holding that respondent does not have a reasonable expectation of privacy enabling him to invoke the protections of the Fourth Amendment does not mean that he is without a remedy for calculated harassment unrelated to prison needs. Nor does it mean that prison attendants can ride roughshod over inmates’ property rights with impunity. The Eighth Amendment always stands as a protection against “cruel and unusual punishments.” By the same token, there are adequate state tort and common-law remedies available to respondent to redress the alleged destruction of his personal property. See discussion <em>infra, </em>at 534-536.<footnotemark>9</footnotemark></p>
<p id="b572-6">B</p>
<p id="b572-7">In his complaint in the District Court, in addition to his claim that the shakedown search of his cell violated his Fourth and Fourteenth Amendment privacy rights, respondent alleged under <span class="citation no-link">42 U. S. C. § 1983</span> that petitioner intentionally destroyed certain of his personal property during the search. This destruction, respondent contended, deprived him of property without due process, in violation of the Due Process Clause of the Fourteenth Amendment. The District Court dismissed this portion of respondent’s complaint for failure to state a claim. Reasoning under <em>Parratt </em>v. <em>Taylor, </em><page-number citation-index="1" label="531">*531</page-number><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">451 U. S. 527</a></span> (1981), it held that even an intentional destruction of property by a state employee does not violate due process if the state provides a meaningful postdeprivation remedy. The Court of Appeals affirmed. The question presented for our review in Palmer’s cross-petition is whether our decision in <em>Parratt </em>v. <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Taylor</a></span> </em>should extend, as the Court of Appeals held, to intentional deprivations of property by state employees acting under color of state law.<footnotemark>10</footnotemark></p>
<p id="b573-5">In <em>Parratt </em>v. <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Taylor</a></span>, </em>a state prisoner sued prison officials under <span class="citation no-link">42 U. S. C. § 1988</span>, alleging that their negligent loss of a hobby kit he ordered from a mail-order catalog deprived him of property without due process of law, in violation of the Fourteenth Amendment. The Court of Appeals for the Eighth Circuit had affirmed the District Court’s summary judgment in the prisoner’s favor. We reversed, holding that the Due Process Clause of the Fourteenth Amendment is not violated when a state employee negligently deprives an individual of property, provided that the state makes available a meaningful postdeprivation remedy.<footnotemark>11</footnotemark></p>
<p id="b573-6">We viewed our decision in <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span> </em>as consistent with prior cases recognizing that</p>
<blockquote id="b573-7">“either the necessity of quick action by the State or the impracticality of providing any meaningful predeprivation process, when coupled with the availability of some <page-number citation-index="1" label="532">*532</page-number>meaningful means by which to assess the propriety of the State’s action at some time after the initial taking . . . satisfies] the requirements of procedural due process.” <span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/#539" aria-description="Citation for case: Parratt v. Taylor">451 U. S., at 539</a></span> (footnote omitted).</blockquote>
<p id="b574-5">We reasoned that where a loss of property is occasioned by a random, unauthorized act by a state employee, rather than by an established state procedure, the state cannot predict when the loss will occur. <span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/#541" aria-description="Citation for case: Parratt v. Taylor"><em>Id., </em>at 541</a></span>. Under these circumstances, we observed:</p>
<blockquote id="b574-6">“It is difficult to conceive of how the State could provide a meaningful hearing before the deprivation takes place. The loss of property, although attributable to the State as action under ‘color of law,’ is in almost all cases beyond the control of the State. Indeed, in most cases it is not only impracticable, but impossible, to provide a meaningful hearing before the deprivation.” <span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Ibid.</a></span><footnotemark>12</footnotemark></blockquote>
<p id="b574-7">Two Terms ago, we reaffirmed our holding in <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span> </em>in <em>Logan </em>v. <em>Zimmerman Brush Co., </em><span class="citation" data-id="9428680"><a href="/opinion/110657/logan-v-zimmerman-brush-co/" aria-description="Citation for case: Logan v. Zimmerman Brush Co.">455 U. S. 422</a></span> (1982), in the course of holding that postdeprivation remedies do not satisfy due process where a deprivation of property is caused by conduct pursuant to established state procedure, rather than random and unauthorized action.<footnotemark>13</footnotemark></p>
<p id="b575-4"><page-number citation-index="1" label="533">*533</page-number>While <em>Parrott </em>is necessarily limited by its facts to negligent deprivations of property, it is evident, as the Court of Appeals recognized, that its reasoning applies as well to intentional deprivations of property. The underlying rationale of <em>Parrott </em>is that when deprivations of property are effected through random and unauthorized conduct of a state employee, predeprivation procedures are simply “impracticable” since the state cannot know when such deprivations will occur. We can discern no logical distinction between negligent and intentional deprivations of property insofar as the “practicability” of affording predeprivation process is concerned. The state can no more anticipate and control in advance the random and unauthorized intentional conduct of its employees than it can anticipate similar negligent conduct. Arguably, intentional acts are even more difficult to anticipate because one bent on intentionally depriving a person of his property might well take affirmative steps to avoid signalling his intent.</p>
<p id="b575-5">If negligent deprivations of property do not violate the Due Process Clause because predeprivation process is impracticable, it follows that intentional deprivations do not violate that Clause provided, of course, that adequate state post-deprivation remedies are available. Accordingly, we hold that an unauthorized intentional deprivation of property by a state employee does not constitute a violation of the procedural requirements of the Due Process Clause of the Fourteenth Amendment if a meaningful postdeprivation remedy for the loss is available. For intentional, as for negligent deprivations of property by state employees, the state’s action is not complete until and unless it provides or refuses to provide a suitable postdeprivation remedy.<footnotemark>14</footnotemark></p>
<p id="b576-4"><page-number citation-index="1" label="534">*534</page-number>Respondent presses two arguments that require at least brief comment. First, he contends that, because an agent of the state who intends to deprive a person of his property <em>“can </em>provide predeprivation process, then as a matter of due process he must do so.” Brief for Respondent and Cross-Petitioner 8 (emphasis in original). This argument reflects a fundamental misunderstanding of <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span>. </em>There we held that postdeprivation procedures satisfy due process because the <em>state </em>cannot possibly know in advance of a negligent deprivation of property. Whether an individual employee himself is able to foresee a deprivation is simply of no consequence. The controlling inquiry is solely whether the state is in a position to provide for predeprivation process.</p>
<p id="b576-5">Respondent also contends, citing to <em>Logan </em>v. <em>Zimmerman Brush Co., supra, </em>that the deliberate destruction of his property by petitioner constituted a due process violation despite the availability of postdeprivation remedies. Brief for Respondent and Cross-Petitioner 8. In <em><span class="citation" data-id="9428680"><a href="/opinion/110657/logan-v-zimmerman-brush-co/" aria-description="Citation for case: Logan v. Zimmerman Brush Co.">Logan</a></span>, </em>we decided a question about which our decision in <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span> </em>left little doubt, that is, whether a postdeprivation state remedy satisfies due process where the property deprivation is effected pursuant to an established state procedure. We held that it does not. <em><span class="citation" data-id="9428680"><a href="/opinion/110657/logan-v-zimmerman-brush-co/" aria-description="Citation for case: Logan v. Zimmerman Brush Co.">Logan</a></span> </em>plainly has no relevance here. Respondent does not even allege that the asserted destruction of his property occurred pursuant to a state procedure.</p>
<p id="b576-6">Having determined that <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span> </em>extends to intentional deprivations of property, we need only decide whether the Commonwealth of Virginia provides respondent an adequate postdeprivation remedy for the alleged destruction of his property. Both the District Court and, at least implicitly, the Court of Appeals held that several common-law remedies <page-number citation-index="1" label="535">*535</page-number>available to respondent would provide adequate compensation for his property loss. We have no reason to question that determination, particularly given the speculative nature of respondent’s arguments.</p>
<p id="b577-5">Palmer does not seriously dispute the adequacy of the existing state-law remedies themselves. He asserts in this respect only that, because certain of his legal papers allegedly taken “may have contained things irreplacable <em>[sic], </em>and incompensable” or “may also have involved sentimental items which are of equally intangible value,” Brief for Respondent and Cross-Petitioner 10-11, n. 10, a suit in tort, for example, would not “necessarily” compensate him fully. If the loss is “incompensable,” this is as much so under § 1983 as it would be under any other remedy. In any event, that Palmer might not be able to recover under these remedies the full amount which he might receive in a § 1983 action is not, as we have said, determinative of the adequacy of the state remedies. See <em>Parratt, </em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/#544" aria-description="Citation for case: Parratt v. Taylor">451 U. S., at 544</a></span>.</p>
<p id="b577-6">Palmer contends also that relief under applicable state law “is far from certain and complete” because a state court might hold that petitioner, as a state employee, is entitled to sovereign immunity. Brief for Respondent and Cross-Petitioner 11. This suggestion is unconvincing. The District Court and the Court of Appeals held that respondent’s claim would not be barred by sovereign immunity. As the District Court noted, under Virginia law, “a State employee may be held liable for his intentional torts,” <em>Elder </em>v. <em>Holland, </em><span class="citation" data-id="1384033"><a href="/opinion/1384033/elder-v-holland/#19" aria-description="Citation for case: Elder v. Holland">208 Va. 15, 19</a></span>, <span class="citation" data-id="1384033"><a href="/opinion/1384033/elder-v-holland/#372" aria-description="Citation for case: Elder v. Holland">155 S. E. 2d 369, 372-373</a></span> (1967); see also <em>Short </em>v. <em>Griffitts, </em><span class="citation" data-id="1304356"><a href="/opinion/1304356/short-v-griffitts/" aria-description="Citation for case: Short v. Griffitts">220 Va. 53</a></span>, <span class="citation" data-id="1304356"><a href="/opinion/1304356/short-v-griffitts/" aria-description="Citation for case: Short v. Griffitts">255 S. E. 2d 479</a></span> (1979). Indeed, respondent candidly acknowledges that it is “probable that a Virginia trial court would rule that there should be no immunity bar in the present case.” Brief for Respondent and Cross-Petitioner 14.</p>
<p id="b577-7">Respondent attempts to cast doubt on the obvious breadth of <em><span class="citation" data-id="1384033"><a href="/opinion/1384033/elder-v-holland/" aria-description="Citation for case: Elder v. Holland">Elder</a></span> </em>through the naked assertion that “the phrase ‘may <page-number citation-index="1" label="536">*536</page-number>be held liable’ could have meant . . . only the possibility of liability under certain circumstances rather than a blanket rule . . . Brief for Respondent and Cross-Petitioner 13. We are equally unpersuaded by this speculation. The language of <em><span class="citation" data-id="1384033"><a href="/opinion/1384033/elder-v-holland/" aria-description="Citation for case: Elder v. Holland">Elder</a></span> </em>is unambiguous that employees of the Commonwealth do not enjoy sovereign immunity for their intentional torts, and <em><span class="citation" data-id="1384033"><a href="/opinion/1384033/elder-v-holland/" aria-description="Citation for case: Elder v. Holland">Elder</a></span> </em>has been so read by a number of federal courts, as respondent concedes, see Brief for Respondent and Cross-Petitioner 13, n. 13. See, <em>e. g., Holmes </em>v. <em>Wampler, </em><span class="citation" data-id="1870743"><a href="/opinion/1870743/holmes-v-wampler/#504" aria-description="Citation for case: Holmes v. Wampler">546 F. Supp. 500, 504</a></span> (ED Va. 1982); <em>Irshad </em>v. <em>Spann, </em><span class="citation" data-id="1460980"><a href="/opinion/1460980/al-mustafa-irshad-v-spann/#928" aria-description="Citation for case: Al-Mustafa Irshad v. Spann">543 F. Supp. 922, 928</a></span> (ED Va. 1982); <em>Frazier </em>v. <em>Collins, </em><span class="citation" data-id="1686657"><a href="/opinion/1686657/frazier-v-collins/#110" aria-description="Citation for case: Frazier v. Collins">544 F. Supp. 109, 110</a></span> (ED Va. 1982); <em>Whorley </em>v. <em>Karr, </em><span class="citation" data-id="1443669"><a href="/opinion/1443669/whorley-v-karr/#89" aria-description="Citation for case: Whorley v. Karr">534 F. Supp. 88, 89</a></span> (WD Va. 1981); <em>Daughtry </em>v. <em>Arlington County, Va., </em><span class="citation" data-id="1905445"><a href="/opinion/1905445/daughtry-v-arlington-county-va/" aria-description="Citation for case: Daughtry v. Arlington County, Va.">490 F. Supp. 307</a></span> (DC 1980).<footnotemark>15</footnotemark> In sum, it is evident here, as in <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span>, </em>that the State has provided an adequate postdeprivation remedy for the alleged destruction of property.</p>
<p id="b578-5">Ill</p>
<p id="b578-6">We hold that the Fourth Amendment has no applicability to a prison cell. We hold also that, even if petitioner intentionally destroyed respondent’s personal property during the challenged shakedown search, the destruction did not violate the Fourteenth Amendment since the Commonwealth of Virginia has provided respondent an adequate postdeprivation remedy.</p>
<p id="b578-7">Accordingly, the judgment of the Court of Appeals reversing and remanding the District Court’s judgment on respond<page-number citation-index="1" label="537">*537</page-number>ent’s claim under the Fourth and Fourteenth Amendments is reversed. The judgment affirming the District Court’s decision that respondent has not been denied due process under the Fourteenth Amendment is affirmed.</p>
<p id="b579-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b562-7"> The District Court determined that Palmer could proceed against Hudson in state court either for conversion or for detinue, and that under applicable Virginia law, see <em>Elder </em>v. <em>Holland, </em><span class="citation" data-id="1384033"><a href="/opinion/1384033/elder-v-holland/" aria-description="Citation for case: Elder v. Holland">208 Va. 15</a></span>, <span class="citation" data-id="1384033"><a href="/opinion/1384033/elder-v-holland/" aria-description="Citation for case: Elder v. Holland">155 S. E. 2d 369</a></span> (1967), Hudson would not be entitled to immunity for the alleged intentional tort.</p>
</footnote>
<footnote label="2">
<p id="b563-6"> The Court of Appeals observed that “there is no practical mechanism by which Virginia could prevent its guards from conducting personal vendettas against prisoners other than by punishing them after the fact.. . .” <span class="citation" data-id="413271"><a href="/opinion/413271/russell-thomas-palmer-jr-v-ted-s-hudson-officer/#1223" aria-description="Citation for case: Russell Thomas Palmer, Jr. v. Ted S. Hudson, Officer">697 F. 2d, at 1223</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b563-7"> See n. 1, <em>supra.</em></p>
</footnote>
<footnote label="4">
<p id="b563-8"> Petitioner maintains that the Court of Appeals’ decision rests at least in part upon a finding of an independent right of privacy for prisoners under the Fourteenth Amendment alone. Arguably, it is not entirely clear whether the Court of Appeals believed that the limited privacy right it recognized was guaranteed solely by the Fourth Amendment, and applicable to the States only through the Fourteenth Amendment, or whether the right emanated from the Fourteenth Amendment alone, or both. The court’s opinion, however, explicitly speaks to the “primary purpose of the Fourth and Fourteenth Amendments,” <span class="citation" data-id="413271"><a href="/opinion/413271/russell-thomas-palmer-jr-v-ted-s-hudson-officer/#1224" aria-description="Citation for case: Russell Thomas Palmer, Jr. v. Ted S. Hudson, Officer">697 F. 2d, at 1224</a></span>, and nowhere does it suggest an intention to draw a distinction between the Fourth and Fourteenth Amendment right of privacy in prison cells. Under the circumstances, we assume, since there is no suggestion to the contrary, that the court did not mean to imply in this context that any right of privacy that might exist under the Fourteenth Amendment alone exceeds that which exists under the Fourth Amendment.</p>
</footnote>
<footnote label="5">
<p id="b564-8"> The majority of the Courts of Appeals have held that a prisoner retains at least a minimal degree <em>of </em>Fourth Amendment protection in his cell. See <em>United States </em>v. <em>Chamorro, </em><span class="citation" data-id="407932"><a href="/opinion/407932/united-states-v-sergio-chamorro-aka-sergio-hernandez/" aria-description="Citation for case: United States v. Sergio Chamorro A/K/A Sergio Hernandez">687 F. 2d 1</a></span> (CA1 1982); <em>United States </em>v. <em>Hinckley, </em>217 U. S. App. D. C. 262, <span class="citation" data-id="400069"><a href="/opinion/400069/united-states-v-john-w-hinckley-jr-united-states-of-america-v-john-w/" aria-description="Citation for case: United States v. John W. Hinckley, Jr. United States of...">672 F. 2d 115</a></span> (1982); <em>United States </em>v. <em>Lilly, </em><span class="citation" data-id="9464833"><a href="/opinion/356030/united-states-v-sherry-marie-lilly-united-states-of-america-v-merrilyn/" aria-description="Citation for case: United States v. Sherry Marie Lilly, United States of...">576 F. 2d 1240</a></span> (CA5 1978); <em>United States </em>v. <em>Stumes, </em><span class="citation" data-id="343130"><a href="/opinion/343130/united-states-v-norman-stumes/" aria-description="Citation for case: United States v. Norman Stumes">549 F. 2d 831</a></span> (CA8 1977); <em>Bonner </em>v. <em>Coughlin, </em><span class="citation" data-id="9461858"><a href="/opinion/328221/alonzo-bonner-v-joseph-coughlin/" aria-description="Citation for case: Alonzo Bonner v. Joseph Coughlin">517 F. 2d 1311</a></span> (CA7 1975) (vacating District Court judgment), on rehearing, <span class="citation" data-id="9463304"><a href="/opinion/340703/alonzo-bonner-v-joseph-coughlin/" aria-description="Citation for case: Alonzo Bonner v. Joseph Coughlin">545 F. 2d 565</a></span> (1976) (en banc) (affirming District Court on other grounds), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./435/932/">435 U. S. 932</a></span> (1978). The Second and Ninth Circuits, however, have held that the Fourth Amendment does not apply in a prison cell. See <em>Christman </em>v. <em>Skinner, </em><span class="citation" data-id="9458823"><a href="/opinion/306226/miles-christman-v-albert-skinner/" aria-description="Citation for case: Miles Christman v. Albert Skinner">468 F. 2d 723</a></span> (CA2 1972); <em>United States </em>v. <em>Hitchcock, </em><span class="citation" data-id="305965"><a href="/opinion/305965/united-states-v-benjamin-hitchcock/" aria-description="Citation for case: United States v. Benjamin Hitchcock">467 F. 2d 1107</a></span> (CA9 1972), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./410/916/">410 U. S. 916</a></span> (1973).</p>
</footnote>
<footnote label="6">
<p id="b566-7"> In <em>Lanza </em>v. <em>New York, </em><span class="citation" data-id="9422429"><a href="/opinion/106425/lanza-v-new-york/#143" aria-description="Citation for case: Lanza v. New York">370 U. S. 139, 143-144</a></span> (1962), a plurality of the Court termed as “at best a novel argument” the assertion that a prison “is a place where [one] can claim constitutional immunity from search or seizure of his person, his papers, or his effects.” This observation, however, was plainly dictum. In fact, three Members of the Court specifically dissented from what they characterized as the Court’s “gratuitous exposition of several grave constitutional issues . . . .” <span class="citation" data-id="9422429"><a href="/opinion/106425/lanza-v-new-york/#150" aria-description="Citation for case: Lanza v. New York"><em>Id., </em>at 150</a></span> (Brennan, J., dissenting, joined by Warren, C. J., and Douglas, J.).</p>
<p id="b566-8">In upholding a room search rule against a Fourth Amendment challenge by pretrial detainees in <em>Bell </em>v. <em>Wolfish, </em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">441 U. S. 520</a></span> (1979), the Court acknowledged the plausibility of an argument that “a person confined in a detention facility has no reasonable expectation of privacy with respect to his room or cell and that therefore the Fourth Amendment provides no protection for such a person.” <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#556" aria-description="Citation for case: Bell v. Wolfish"><em>Id., </em>at 556-557</a></span>. However, as in <em><span class="citation" data-id="9422429"><a href="/opinion/106425/lanza-v-new-york/" aria-description="Citation for case: Lanza v. New York">Lanza</a></span>, </em>it was unnecessary to reach the issue of the Fourth Amendment’s general <page-number citation-index="1" label="525">*525</page-number>applicability in a prison cell. We simply assumed, <em>arguendo, </em>that a pretrial detainee retained at least a “diminished expectation of privacy.” <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#557" aria-description="Citation for case: Bell v. Wolfish">441 U. S., at 557</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b567-9"> In <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>Justice Harlan suggested that an expectation of privacy is “justifiable” if the person concerned has “exhibited an actual (subjective) expectation of privacy” and the expectation is one that “society is prepared to recognize as ‘reasonable.’ ” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States">389 U. S., at 360, 361</a></span> (concurring opinion). The Court has always emphasized the second of these two requirements. As Justice White said, writing for the plurality in <em>United States </em>v. <em>White, </em><span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/" aria-description="Citation for case: United States v. White">401 U. S. 745</a></span> (1971): “Our problem is not what the privacy expectations of particular defendants in particular situations may be or the extent to which they may in fact have relied on the discretion of their companions. . . . Our problem, in terms of the principles announced in <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>is what expectations of privacy are constitutionally ‘justifiable’. . . .” <em>Id., </em>at 751-752. In the same case, even Justice Harlan stressed the controlling importance of the second of these two requirements: “The analysis must, in my view, transcend the search for subjective expectations .... [W]e should not, as judges, merely recite the expectations and risks without examining the desirability of saddling them upon society.” <em>United States </em>v. <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#768" aria-description="Citation for case: United States v. White"><em>White, supra, </em>at 768, 786</a></span> (dissenting opinion).</p>
<p id="b567-10">The Court’s refusal to adopt a test of “subjective expectation” is understandable; constitutional rights are generally not defined by the subjective intent of those asserting the rights. The problems inherent in such a standard are self-evident. See, <em>e. g., Smith </em>v. <em>Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#740" aria-description="Citation for case: Smith v. Maryland">442 U. S., at 740-741, n. 5</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b570-6"> Respondent contends also that the destruction of his personal property constituted an unreasonable <em>seizure </em>of that property violative of the Fourth Amendment. Assuming that the Fourth Amendment protects against the destruction of property, in addition to its mere seizure, the same reasons that lead us to conclude that the Fourth Amendment’s proscription against unreasonable searches is inapplicable in a prison cell, apply with controlling force to seizures. Prison officials must be free to seize from cells any articles which, in their view, disserve legitimate institutional interests.</p>
<p id="b570-7">That the Fourth Amendment does not protect against seizures in a prison cell does not mean that an inmate’s property can be destroyed with impunity. We note, for example, that even apart from inmate grievance procedures, see n. 9, <em>infra, </em>respondent has adequate state remedies for the alleged destruction of his property. See discussion <em>infra, </em>at 534-536.</p>
</footnote>
<footnote label="9">
<p id="b572-8"> The Commonwealth has a new inmate grievance procedure that was effective as of October 12, 1982, see n. 14, <em>infra. </em>But it appears that at the time of the alleged deprivation of respondent’s property, a very similar procedure was in effect that would also have afforded respondent relief for any destruction of his property. See Reply Brief for Petitioner and Cross-Respondent 13, n. 14.</p>
</footnote>
<footnote label="10">
<p id="b573-8"> Four Circuits, including the Fourth Circuit in these cases, have held that <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span> </em>extends to intentional deprivations of property. See <em>Wolf-Lillie </em>v. <em>Sonquist, </em><span class="citation" data-id="414190"><a href="/opinion/414190/arlene-c-wolf-lillie-v-gerald-m-sonquist-kenosha-county-sheriff/" aria-description="Citation for case: Arlene C. Wolf-Lillie v. Gerald M. Sonquist, Kenosha...">699 F. 2d 864</a></span> (CA7 1983); <em>Engblom </em>v. <em>Carey, </em><span class="citation" data-id="8915132"><a href="/opinion/8925582/engblom-v-carey/" aria-description="Citation for case: Engblom v. Carey">677 F. 2d 957</a></span> (CA2 1982); <em>Rutledge </em>v. <em>Arizona Board of Regents, </em><span class="citation" data-id="8914062"><a href="/opinion/8924683/rutledge-v-arizona-board-of-regents/" aria-description="Citation for case: Rutledge v. Arizona Board of Regents">660 F. 2d 1345</a></span> (CA9 1981), aff’d <em>sub nom. Kush </em>v. <em>Rutledge, </em><span class="citation" data-id="110900"><a href="/opinion/110900/kush-v-rutledge/" aria-description="Citation for case: Kush v. Rutledge">460 U. S. 719</a></span> (1983). Three Circuits have held that it does not. <em>Brewer </em>v. <em>Blackwell, </em><span class="citation" data-id="410403"><a href="/opinion/410403/joseph-brewer-v-m-prentiss-blackwell/" aria-description="Citation for case: Joseph Brewer v. M. Prentiss Blackwell">692 F. 2d 387</a></span> (CA5 1982); <em>Weiss </em>v. <em>Lehman, </em><span class="citation" data-id="9469157"><a href="/opinion/403393/e-b-weiss-v-r-c-lehman-and-wayne-larue/" aria-description="Citation for case: E. B. Weiss v. R. C. Lehman and Wayne Larue">676 F. 2d 1320</a></span> (CA9 1982); <em>Madyun </em>v. <em>Thompson, </em><span class="citation" data-id="393729"><a href="/opinion/393729/yusuf-asad-madyun-v-james-r-thompson-governor/" aria-description="Citation for case: Yusuf Asad Madyun v. James R. Thompson, Governor">657 F. 2d 868</a></span> (CA7 1981).</p>
</footnote>
<footnote label="11">
<p id="b573-9"> Nebraska had provided respondent with a tort remedy for his alleged property deprivation. <span class="citation no-link">Neb. Rev. Stat. § 81-8</span>,209 <em>et seq. </em>(1976). We held that this remedy was entirely adequate to satisfy due process, even though we recognized that it might not provide respondent all the relief to which he might have been entitled under § 1983. <span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/#543" aria-description="Citation for case: Parratt v. Taylor">451 U. S., at 543-544</a></span>.</p>
</footnote>
<footnote label="12">
<p id="b574-8"> In reaching our conclusion in <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span>, </em>we expressly relied on then-judge Stevens’ opinion for the Seventh Circuit in <em>Bonner </em>v. <em>Coughlin, </em><span class="citation" data-id="9461858"><a href="/opinion/328221/alonzo-bonner-v-joseph-coughlin/" aria-description="Citation for case: Alonzo Bonner v. Joseph Coughlin">517 F. 2d 1311</a></span> (1975), modified en banc, <span class="citation" data-id="9463304"><a href="/opinion/340703/alonzo-bonner-v-joseph-coughlin/" aria-description="Citation for case: Alonzo Bonner v. Joseph Coughlin">545 F. 2d 565</a></span> (1976), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./435/932/">435 U. S. 932</a></span> (1978), holding that, where an individual has been negligently deprived of property by a state employee, the state’s action is not complete unless or until the state fails to provide an adequate postdeprivation remedy for the property loss. <span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/#541" aria-description="Citation for case: Parratt v. Taylor">451 U. S., at 541-542</a></span>.</p>
</footnote>
<footnote label="13">
<p id="b574-9"> In <em><span class="citation" data-id="9428680"><a href="/opinion/110657/logan-v-zimmerman-brush-co/" aria-description="Citation for case: Logan v. Zimmerman Brush Co.">Logan</a></span>, </em>we examined a claim that the terms of an Illinois statute deprived the petitioner of an opportunity to pursue his employment discrimination claim. We specifically distinguished the case from <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span> </em>by noting that <em>“Parratt. . . </em>was dealing with a. . . ‘random and unauthorized act by a state employee... [and was] not a result of some established state procedure.’” <span class="citation" data-id="9428680"><a href="/opinion/110657/logan-v-zimmerman-brush-co/" aria-description="Citation for case: Logan v. Zimmerman Brush Co.">455 U. S., at 435</a></span>-436 (quoting <em>Parratt, </em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/#541" aria-description="Citation for case: Parratt v. Taylor">451 U. S., at 541</a></span>). <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span>, </em>we said, “was not designed to reach ... a situation” where the <page-number citation-index="1" label="533">*533</page-number>deprivation is the result of an established state procedure. <span class="citation" data-id="9428680"><a href="/opinion/110657/logan-v-zimmerman-brush-co/#436" aria-description="Citation for case: Logan v. Zimmerman Brush Co.">455 U. S., at 436</a></span>.</p>
</footnote>
<footnote label="14">
<p id="b575-7"> Our holding that an intentional deprivation of property does not give rise to a violation of the Due Process Clause if the state provides an adequate postdeprivation remedy was foreshadowed by our discussion of <page-number citation-index="1" label="534">*534</page-number><em>Ingraham </em>v. <em>Wright, </em><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">430 U. S. 651</a></span> (1977), in <em><span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">Parratt</a></span>. </em>We noted that our analysis was “quite consistent” with that in <em><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">Ingraham</a></span>, </em>a case that, we observed, involved intentional conduct on behalf of state officials. <span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/#542" aria-description="Citation for case: Parratt v. Taylor">451 U. S., at 542</a></span>.</p>
</footnote>
<footnote label="15">
<p id="b578-8"> It is noteworthy that the Commonwealth has enacted the State Tort Claims Act, Va. Code §8.01-195.1 <em>et seq. </em>(Supp. 1983), which, in defined circumstances, waives sovereign immunity. Additionally, as of October 12, 1982, the State has in place an inmate grievance procedure that received the certification of the Attorney General of the United States as in compliance with the Civil Rights of Institutionalized Persons Act, 42 U. S. C. § 1997e. Although apparently neither of these avenues was open to this respondent, both are potential sources of relief for persons in respondent’s position in the future.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Illinois v. Andreas.md  (`case`, 5 assertions)

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
{"assertion_id": "c1b64e7bbfbc817b", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "463 U.S. 765 (1983)", "court": "U.S. Supreme Court", "neutral_cite": "1983 U.S. LEXIS 106", "official_citation_present": true, "parallel_cite": "103 S. Ct. 3319; 77 L. Ed. 2d 1003; 51 U.S.L.W. 5157", "title": "Illinois v. Andreas", "year": "1983"}}
{"assertion_id": "2e36a347a09c55e4", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Reopening a container after a lawful controlled delivery is not a new search where no substantial likelihood exists that the contents changed during a gap in surveillance — the earlier lawful inspection already extinguished any privacy interest.", "title": "Illinois v. Andreas"}}
{"assertion_id": "be9f2af83f984905", "dimension": "support", "kind": "home_role", "locator": {"home": "Plain View Doctrine"}, "payload": {"home": "Plain View Doctrine", "role": "Related", "title": "Illinois v. Andreas"}}
{"assertion_id": "04f31ac7866608d0", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Illinois v. Andreas"}}
{"assertion_id": "f917c9d2d149e0c6", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1983-07-05", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Illinois v. Andreas", "field_i_validity": "good_law", "scope_note": "Good law; the controlled-delivery / no-revival-of-privacy rule remains the governing standard for reopening a previously lawfully inspected container.", "title": "Illinois v. Andreas", "varies_by_point": "false"}}
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

## GROUP: content/cases/Illinois v. Krull.md  (`case`, 5 assertions)

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
{"assertion_id": "714029ad6b7af09c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "480 U.S. 340 (1987)", "court": "U.S. Supreme Court", "neutral_cite": "1987 U.S. LEXIS 1061", "official_citation_present": true, "parallel_cite": "107 S. Ct. 1160; 94 L. Ed. 2d 364; 55 U.S.L.W. 4291", "title": "Illinois v. Krull", "year": "1987"}}
{"assertion_id": "601e4cafe6d43d5a", "dimension": "support", "kind": "home_role", "locator": {"home": "The Good-Faith Exception"}, "payload": {"home": "The Good-Faith Exception", "role": "Key — Progeny / Refinement", "title": "Illinois v. Krull"}}
{"assertion_id": "7f3f18854dc2cf14", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Good-faith reliance on a STATUTE later held unconstitutional does not trigger exclusion; excluding such evidence would have no deterrent…", "title": "Illinois v. Krull"}}
{"assertion_id": "64ffba382056f2f8", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Illinois v. Krull"}}
{"assertion_id": "76ce044d02370202", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1987-03-09", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Illinois v. Krull", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Illinois v. Krull", "varies_by_point": "false"}}
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
