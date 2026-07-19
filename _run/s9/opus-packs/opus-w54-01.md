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

## GROUP: content/cases/United States v. Payner.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Payner"
type: case
citation: "447 U.S. 727 (1980)"
parallel_cite: "100 S. Ct. 2439; 65 L. Ed. 2d 468"
neutral_cite: 1980 U.S. LEXIS 136
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1980
date_decided: 1980-08-11
docket: 78-1729
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1980-06-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Payner
  varies_by_point: false
  scope_note: A federal court may not use its supervisory power to evade the Fourth Amendment standing rules. Good law.
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110317/united-states-v-payner/"
  cluster_id: 110317
  opinion_id: 9428014
  identity_checked: true
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: "Key — Progeny"
related: ["[[Rakas v. Illinois]]", "[[Alderman v. United States]]", "[[Elkins v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "standing", "exclusionary-rule", "supervisory-power", "third-party"]
holding: "A federal court may not invoke its supervisory power to suppress evidence obtained through the deliberate violation of a third party's Fourth Amendment rights at the instance of a defendant whose own rights were not violated; the supervisory power cannot circumvent the standing requirement."
lake:
  record_id: United States v. Payner
  status: verified
  projected_at: 2026-07-09
---

# United States v. Payner

*447 U.S. 727 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
In the IRS "briefcase caper," agents arranged for an informant to steal a Bahamian banker's briefcase and photograph its documents, which led to evidence that Payner had falsified his tax return. The District Court found that the Government had deliberately and flagrantly violated the banker's (a third party's) Fourth Amendment rights, but it acknowledged that Payner himself lacked standing because his own rights were not invaded. It nonetheless suppressed the evidence under the federal courts' supervisory power, and the Sixth Circuit affirmed.

## Issue
Whether a federal court may invoke its supervisory power to suppress evidence obtained through the Government's deliberate violation of a third party's Fourth Amendment rights, at the instance of a defendant whose own rights were not violated and who therefore lacks standing.

## Rule
No. "We conclude that the supervisory power does not authorize a federal court to suppress otherwise admissible evidence on the ground that it was seized unlawfully from a third party not before the court. Our Fourth Amendment decisions have established beyond any doubt that the interest in deterring illegal searches does not justify the exclusion of tainted evidence at the instance of a party who was not the victim of the challenged practices." — 447 U.S. at 735 (citing *Rakas v. Illinois*, 439 U.S. 128, 137, and *Alderman v. United States*, 394 U.S. 165, 174–175). ^pin-735

The label does not matter: "The values assigned to the competing interests do not change because a court has elected to analyze the question under the supervisory power instead of the Fourth Amendment." — [*Id.* at 736](https://www.courtlistener.com/opinion/110317/united-states-v-payner/#:~:text=The%20values%20assigned%20to%20the). ^pin-736

## Application
However egregious the IRS conduct, Payner was not the victim of the unlawful search — it invaded the banker's rights, not his — so he had no standing, and the same deterrence-versus-cost balance the standing rule already strikes governed. The District Court's contrary weighing "amounts to a substitution of individual judgment for the controlling decisions of this Court." To let a court suppress on that basis "would confer on the judiciary discretionary power to disregard the considered limitations of the law it is charged with enforcing." — [*Id.* at 737](https://www.courtlistener.com/opinion/110317/united-states-v-payner/#:~:text=amounts%20to%20a%20substitution%20of). ^pin-737

## Conclusion
The supervisory power "does not extend so far"; the suppression order was reversed. A defendant who lacks [[Standing to Challenge a Search|Fourth Amendment standing]] cannot obtain exclusion through the supervisory power.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Payner* enforces the personal-rights standing rule of [[Alderman v. United States]] and [[Rakas v. Illinois]], holding the supervisory power cannot be used to evade it; it draws on the restrained-supervisory-power and deterrence rationale of [[Elkins v. United States]].

## Appears on
- [[Standing to Challenge a Search]] — *Key — Progeny*

## Sources
- *United States v. Payner*, 447 U.S. 727 (1980) — https://www.courtlistener.com/opinion/110317/united-states-v-payner/ — pinpoints: 735, 736, 737.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "69fd6902bfbcc7a2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "447 U.S. 727 (1980)", "court": "U.S. Supreme Court", "neutral_cite": "1980 U.S. LEXIS 136", "official_citation_present": true, "parallel_cite": "100 S. Ct. 2439; 65 L. Ed. 2d 468", "title": "United States v. Payner", "year": "1980"}}
{"assertion_id": "63f3ce8f485e2a32", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A federal court may not invoke its supervisory power to suppress evidence obtained through the deliberate violation of a third party's Fourth Amendment rights at the instance of a defendant whose own rights were not violated; the supervisory power cannot circumvent the standing requirement.", "title": "United States v. Payner"}}
{"assertion_id": "bf164226f8753349", "dimension": "support", "kind": "home_role", "locator": {"home": "Standing to Challenge a Search"}, "payload": {"home": "Standing to Challenge a Search", "role": "Key — Progeny", "title": "United States v. Payner"}}
{"assertion_id": "a7c31d5709d88f00", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1980-06-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Payner", "field_i_validity": "good_law", "scope_note": "A federal court may not use its supervisory power to evade the Fourth Amendment standing rules. Good law.", "title": "United States v. Payner", "varies_by_point": "false"}}
{"assertion_id": "aa9099b09526fb8d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Payner"}}
```

### lake record — United States v. Payner

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Payner",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Payner",
    "case_name_short": "Payner",
    "case_name_full": "United States v. Payner",
    "input_case_name": "United States v. Payner",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-08-11",
    "year": 1980,
    "docket": "78-1729",
    "cluster_id": 110317,
    "lead_opinion_id": 9428014,
    "sibling_ids": [
      110317,
      9428014,
      9428015
    ],
    "absolute_url": "/opinion/110317/united-states-v-payner/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "447 U.S. 727",
      "volume": "447",
      "reporter": "U.S.",
      "page": "727",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 2439",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "2439",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 2d 468",
        "volume": "65",
        "reporter": "L. Ed. 2d",
        "page": "468",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 136",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "136",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "447 U.S. 727",
        "volume": "447",
        "reporter": "U.S.",
        "page": "727",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 2439",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "2439",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 2d 468",
        "volume": "65",
        "reporter": "L. Ed. 2d",
        "page": "468",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 136",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "136",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "447 U.S. 727",
    "official_selection": {
      "court_class": "scotus",
      "selected": "447 U.S. 727",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-735",
      "page": null,
      "quote": "agents arranged for an informant to steal a Bahamian banker's briefcase and photograph its documents, which led to evidence that Payner had falsified his tax return. The District Court found that the Government had deliberately and flagrantly violated the banker's (a third party's) Fourth Amendment rights, but it acknowledged that Payner himself lacked standing because his own rights were not invaded. It nonetheless suppressed the evidence under the federal courts' supervisory power, and the Sixth Circuit affirmed. ## Issue Whether a federal court may invoke its supervisory power to suppress evidence obtained through the Government's deliberate violation of a third party's Fourth Amendment rights, at the instance of a defendant whose own rights were not violated and who therefore lacks standing. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-736",
      "page": null,
      "quote": "The values assigned to the competing interests do not change because a court has elected to analyze the question under the supervisory power instead of the Fourth Amendment.",
      "star_marker": "736",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 18359,
      "fragment": "#:~:text=The%20values%20assigned%20to%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-737",
      "page": null,
      "quote": "amounts to a substitution of individual judgment for the controlling decisions of this Court.",
      "star_marker": "737",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 19214,
      "fragment": "#:~:text=amounts%20to%20a%20substitution%20of",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1980-06-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Payner",
    "varies_by_point": false,
    "scope_note": "A federal court may not use its supervisory power to evade the Fourth Amendment standing rules. Good law.",
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
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Willie Walker, Jr. v. United States",
          "cluster_id": 4592520,
          "cite": [
            "201 A.3d 586"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Delaine and Malisa Fitzpat",
          "cluster_id": 889950,
          "cite": [
            "2012 MT 300",
            "367 Mont. 385",
            "291 P.3d 1106",
            "2012 Mont. LEXIS 368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Jordan Heath Dentler",
          "cluster_id": 4472853,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Teague",
          "cluster_id": 202526,
          "cite": [
            "469 F.3d 205",
            "2006 U.S. App. LEXIS 29293",
            "2006 WL 3423378"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Southerland, Vince",
          "cluster_id": 186774,
          "cite": [
            "373 U.S. App. D.C. 305",
            "466 F.3d 1083",
            "2006 U.S. App. LEXIS 26978",
            "2006 WL 3069122"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Clemmons v. Wolfe",
          "cluster_id": 3013934,
          "cite": [
            "377 F.3d 322",
            "2004 U.S. App. LEXIS 15613",
            "2004 WL 1689682"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Triumph Capital Group, Inc.",
          "cluster_id": 8751433,
          "cite": [
            "211 F.R.D. 31",
            "2002 U.S. Dist. LEXIS 21615",
            "2002 WL 31487754"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Badgett",
          "cluster_id": 1265814,
          "cite": [
            "895 P.2d 877",
            "10 Cal. 4th 330",
            "41 Cal. Rptr. 2d 635",
            "95 Cal. Daily Op. Serv. 4314",
            "95 Daily Journal DAR 7407",
            "1995 Cal. LEXIS 3320"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Richard A. Horn",
          "cluster_id": 674595,
          "cite": [
            "29 F.3d 754",
            "29 Fed. R. Serv. 3d 1525",
            "1994 U.S. App. LEXIS 18687",
            "1994 WL 378486"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. McMillan",
          "cluster_id": 3944785,
          "cite": [
            "631 N.E.2d 660",
            "91 Ohio App. 3d 1",
            "1993 Ohio App. LEXIS 4413"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thomas v. Arn",
          "cluster_id": 111545,
          "cite": [
            "88 L. Ed. 2d 435",
            "106 S. Ct. 466",
            "474 U.S. 140",
            "1985 U.S. LEXIS 146"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
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
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Powers v. Ohio",
          "cluster_id": 112570,
          "cite": [
            "113 L. Ed. 2d 411",
            "111 S. Ct. 1364",
            "499 U.S. 400",
            "1991 U.S. LEXIS 1857",
            "59 U.S.L.W. 4268",
            "91 Daily Journal DAR 3732",
            "91 Cal. Daily Op. Serv. 2259"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hasting",
          "cluster_id": 110933,
          "cite": [
            "76 L. Ed. 2d 96",
            "103 S. Ct. 1974",
            "461 U.S. 499",
            "1983 U.S. LEXIS 31",
            "51 U.S.L.W. 4572"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
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
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hudson v. Michigan",
          "cluster_id": 145646,
          "cite": [
            "165 L. Ed. 2d 56",
            "126 S. Ct. 2159",
            "547 U.S. 586",
            "2006 U.S. LEXIS 4677"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bank of Nova Scotia v. United States",
          "cluster_id": 112125,
          "cite": [
            "101 L. Ed. 2d 228",
            "108 S. Ct. 2369",
            "487 U.S. 250",
            "1988 U.S. LEXIS 2866",
            "56 U.S.L.W. 4714",
            "62 A.F.T.R.2d (RIA) 5738"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Young v. United States Ex Rel. Vuitton Et Fils S. A.",
          "cluster_id": 111893,
          "cite": [
            "95 L. Ed. 2d 740",
            "107 S. Ct. 2124",
            "481 U.S. 787",
            "1987 U.S. LEXIS 2261",
            "2 U.S.P.Q. 2d (BNA) 1809",
            "55 U.S.L.W. 4676"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
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
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Williams",
          "cluster_id": 112730,
          "cite": [
            "118 L. Ed. 2d 352",
            "112 S. Ct. 1735",
            "504 U.S. 36",
            "1992 U.S. LEXIS 2688"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lance W.",
          "cluster_id": 1421847,
          "cite": [
            "694 P.2d 744",
            "37 Cal. 3d 873",
            "210 Cal. Rptr. 631",
            "1985 Cal. LEXIS 241"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
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
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "G. Heileman Brewing Co., Inc. v. Joseph Oat Corporation",
          "cluster_id": 520636,
          "cite": [
            "871 F.2d 648",
            "13 Fed. R. Serv. 3d 8",
            "1989 U.S. App. LEXIS 4563",
            "1989 WL 30098"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Parks v. Commonwealth",
          "cluster_id": 1315235,
          "cite": [
            "270 S.E.2d 755",
            "221 Va. 492",
            "1980 Va. LEXIS 269"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Voigt",
          "cluster_id": 722380,
          "cite": [
            "89 F.3d 1050",
            "78 A.F.T.R.2d (RIA) 5577",
            "1996 U.S. App. LEXIS 16287",
            "1996 WL 380609"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lonchar v. Thomas",
          "cluster_id": 118015,
          "cite": [
            "134 L. Ed. 2d 440",
            "116 S. Ct. 1293",
            "517 U.S. 314",
            "1996 U.S. LEXIS 2167"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
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
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gaetano Modica",
          "cluster_id": 396890,
          "cite": [
            "663 F.2d 1173",
            "1981 U.S. App. LEXIS 16444"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Guillermo Novo Sampol, United States of America v. Alvin Ross Diaz, United States of America v. Ignacio Novo Sampol",
          "cluster_id": 384944,
          "cite": [
            "636 F.2d 621",
            "204 U.S. App. D.C. 349"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, in No. 81-1020 v. Jannotti, Harry P. United States of America, in No. 81-1021 v. Schwartz, George X",
          "cluster_id": 401021,
          "cite": [
            "673 F.2d 578",
            "1982 WL 602723"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States Department of Labor v. Triplett",
          "cluster_id": 112399,
          "cite": [
            "108 L. Ed. 2d 701",
            "110 S. Ct. 1428",
            "494 U.S. 715",
            "1990 U.S. LEXIS 1666"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin Eugene Wright",
          "cluster_id": 663707,
          "cite": [
            "16 F.3d 1429",
            "1994 U.S. App. LEXIS 2361",
            "1994 WL 38983"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hutchins",
          "cluster_id": 1394982,
          "cite": [
            "279 S.E.2d 788",
            "303 N.C. 321",
            "1981 N.C. LEXIS 1186"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Payner:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110317 OR 9428014 OR 9428015) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03NDkwODgwMDAwMDAmcz0zOTQ0Nzg1JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110317+OR+9428014+OR+9428015%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 11,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(110317 OR 9428014 OR 9428015)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzkmcz04OTc4OTU5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110317+OR+9428014+OR+9428015%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110317 OR 9428014 OR 9428015)",
        "reviewed": 11,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 11,
        "triage_read": 1,
        "triage_snippet_classified": 10
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110317 OR 9428014 OR 9428015)",
    "indexed_citing_opinions": 540,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110317,
        "count": 482,
        "count_source": "search"
      },
      {
        "opinion_id": 9428014,
        "count": 66,
        "count_source": "search"
      },
      {
        "opinion_id": 9428015,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 785,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-payner.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjYxNzY5ODgmcz00NTg3NTY5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110317+OR+9428014+OR+9428015%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110317,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 104603,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 105343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 105421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 106881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 107567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 107874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 108602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 108760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 108768,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 109005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 109437,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 109816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 110049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 341778,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 362527,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 1087965,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 1417027,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110317,
        "cited_id": 3580565,
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
    "date_created": "2026-07-06T02:12:06Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:12:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:12:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:17:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:12:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Payner

```
<opinion type="majority">
<author id="b770-10">Mr. Justice Powell</author>
<p id="Atf">delivered the opinion of the Court.</p>
<p id="b770-11">The question is whether the District Court properly suppressed the fruits of an unlawful search that did not invade the respondent’s Fourth Amendment rights.</p>
<p id="b770-12">I</p>
<p id="b770-13">Respondent Jack Payner was indicted in September 1976 on a charge of falsifying his 1972 federal income tax return in violation of <span class="citation no-link">18 U. S. C. § 1001</span>.<footnotemark>1</footnotemark> The indictment alleged that respondent denied maintaining a foreign bank account at a time when he knew that he had such an account at the Castle Bank and Trust Company of Nassau, Bahama Islands. The Government’s case rested heavily on a loan guarantee agreement dated April 28, 1972, in which respondent pledged <page-number citation-index="1" label="729">*729</page-number>the funds in his Castle Bank account as security for a $100,000 loan.</p>
<p id="b771-5">Respondent waived his right to jury trial and moved to suppress the guarantee agreement. With the consent of the parties, the United States District Court for the • Northern District of Ohio took evidence on the motion at a hearing consolidated with the trial on the merits. The court found respondent guilty as charged on the basis of all the evidence. The court also found, however, that the Government discovered the guarantee agreement by exploiting a flagrantly illegal search that occurred on January 15, 1973. The court therefore suppressed “all evidence introduced in the case by the Government with the exception of Jack Payner’s 1972 tax return . . . and the related testimony.” <span class="citation" data-id="1417027"><a href="/opinion/1417027/united-states-v-payner/#136" aria-description="Citation for case: United States v. Payner">434 F. Supp. 113, 136</a></span> (1977). As the tax return alone was insufficient to demonstrate knowing falsification, the District Court set aside respondent’s conviction.<footnotemark>2</footnotemark></p>
<p id="b771-6">The events leading up to the 1973 search are not in dispute. In 1965, the Internal Revenue Service launched an investigation into the financial activities of American citizens in the Bahamas. The project, known as “Operation Trade Winds,” was headquartered in Jacksonville, Fla. Suspicion focused on the Castle Bank in 1972, when investigators learned that a suspected narcotics trafficker had an account there. Special Agent Richard Jaffe of the Jacksonville office asked Norman Casper, a private investigator and occasional informant, to learn what he could about the Castle Bank and its depositors. To that end, Casper cultivated his friendship with Castle <page-number citation-index="1" label="730">*730</page-number>Bank vice president Michael Wolstencroft. Casper introduced Wolstencroft to Sybol Kennedy, a private investigator and former employee. When Casper discovered that the banker intended to spend a few days in Miami in January 1973, he devised a scheme to gain access to the bank records he knew Wolstencroft would be carrying in his briefcase. Agent Jaffe approved the basic outline of the plan.</p>
<p id="b772-5">Wolstencroft arrived in Miami on January 15 and went directly to Kennedy’s apartment. At about 7:30 p. m., the two left for dinner at a Key Biscayne restaurant. Shortly thereafter, Casper entered the apartment using a key supplied by Kennedy. He removed the briefcase and delivered it to Jaffe.' While the agent supervised the copying of approximately 400 documents taken from the briefcase, a “lookout” observed Kennedy and Wolstencroft at dinner. The observer notified Casper when the pair left the restaurant, and the briefcase was replaced. The documents photographed that evening included papers evidencing a close working relationship between the Castle Bank and the Bank of Perrine, Fla. Subpoenas issued to the Bank of Perrine ultimately uncovered the loan guarantee agreement at issue in this case.</p>
<p id="b772-6">The District Court found that the United States, acting through Jaffe, “knowingly and willfully participated in the unlawful seizure of Michael Wolstencroft’s briefcase....” <span class="citation" data-id="1417027"><a href="/opinion/1417027/united-states-v-payner/#120" aria-description="Citation for case: United States v. Payner"><em>Id., </em>at 120</a></span>. According to that court, “the Government affirmatively counsels its agents that the Fourth Amendment standing limitation permits them to purposefully conduct an unconstitutional search and seizure of one individual in order to obtain evidence against third parties. . . .” <span class="citation" data-id="1417027"><a href="/opinion/1417027/united-states-v-payner/#132" aria-description="Citation for case: United States v. Payner"><em>Id., </em>at 132-133</a></span>. The District Court also found that the documents seized from Wolstencroft provided the leads that ultimately led to the discovery of the critical loan guarantee agreement. <span class="citation" data-id="1417027"><a href="/opinion/1417027/united-states-v-payner/#123" aria-description="Citation for case: United States v. Payner"><em>Id., </em>at 123</a></span>.<footnotemark>3</footnotemark> Although the search did not impinge upon the <page-number citation-index="1" label="731">*731</page-number>respondent's Fourth Amendment rights, the District Court believed that the Due Process Clause of the Fifth Amendment and the inherent supervisory power of the federal courts required it to exclude evidence tainted by the Government’s “knowing and purposeful <em>bad faith hostility </em>to any person’s fundamental constitutional rights.” <span class="citation" data-id="1417027"><a href="/opinion/1417027/united-states-v-payner/#129" aria-description="Citation for case: United States v. Payner"><em>Id., </em>at 129</a></span>; see <span class="citation" data-id="1417027"><a href="/opinion/1417027/united-states-v-payner/#133" aria-description="Citation for case: United States v. Payner"><em>id., </em>at 133, 134-135</a></span>.</p>
<p id="b773-5">The Court of Appeals for the Sixth Circuit affirmed in a brief order endorsing the District Court’s use of its supervisory power. <span class="citation" data-id="362527"><a href="/opinion/362527/united-states-v-jack-payner/" aria-description="Citation for case: United States v. Jack Payner">590 F. 2d 206</a></span> (1979) <em>(per curiam). </em>The Court of Appeals did not decide the due process question. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./444/822/">444 U. S. 822</a></span> (1979), and we now reverse.</p>
<p id="b773-6">II</p>
<p id="b773-7">This Court discussed the doctrine of “standing to invoke the [Fourth Amendment] exclusionary rule” in some detail last Term. <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#138" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 138</a></span> (1978). We reaffirmed the established rule that a court may not exclude evidence under the Fourth Amendment unless it finds that an unlawful search or seizure violated the defendant’s own constitutional rights. <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#133" aria-description="Citation for case: Rakas v. Illinois"><em>Id., </em>at 133-140</a></span>. See, <em>e. g., Brown </em>v. <em>United States, </em><span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/#229" aria-description="Citation for case: Brown v. United States">411 U. S. 223, 229-230</a></span> (1973); <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#171" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 171-172</a></span> (1969); <em>Simmons </em>v. <em>United States, </em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#389" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 389</a></span> (1968). And the defendant’s Fourth Amendment rights are violated only when the challenged conduct invaded <em>his </em>legitimate expectation of privacy rather than that of a third party. <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 143</a></span>; <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#149" aria-description="Citation for case: Rakas v. Illinois"><em>id., </em>at 149-152</a></span> (Powell, J., concurring) ; <em>Combs </em>v. <em>United States, </em><span class="citation" data-id="108602"><a href="/opinion/108602/combs-v-united-states/#227" aria-description="Citation for case: Combs v. United States">408 U. S. 224, 227</a></span> (1972); <em>Mancusi </em>v. <em>DeForte, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#368" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364, 368</a></span> (1968).</p>
<p id="b773-8">The foregoing authorities establish, as the District Court recognized, that respondent lacks standing under the Fourth <page-number citation-index="1" label="732">*732</page-number>Amendment to suppress the documents illegally seized from Wolstencroft. <span class="citation" data-id="1417027"><a href="/opinion/1417027/united-states-v-payner/#126" aria-description="Citation for case: United States v. Payner">434 F. Supp., at 126</a></span>. The Court of Appeals did not disturb the District Court’s conclusion that “Jack Payner possessed no privacy interest in the Castle Bank documents that were seized from Wolstencroft.” <em>Ibid.; </em>see <span class="citation" data-id="362527"><a href="/opinion/362527/united-states-v-jack-payner/#207" aria-description="Citation for case: United States v. Jack Payner">590 F. 2d, at 207</a></span>. Nor do we. <em>United States </em>v. <em>Miller, </em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">425 U. S. 435</a></span> (1976), established that a depositor has no expectation of privacy and thus no “protectable Fourth Amendment interest” in copies of checks and deposit slips retained by his bank. <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#437" aria-description="Citation for case: United States v. Miller"><em>Id., </em>at 437</a></span>; see <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#442" aria-description="Citation for case: United States v. Miller"><em>id., </em>at 442</a></span>. Nothing in the record supports a contrary conclusion in this case.<footnotemark>4</footnotemark></p>
<p id="b775-4"><page-number citation-index="1" label="733">*733</page-number>The District Court and the Court of Appeals believed, however, that a federal court should use its supervisory power to suppress evidence tainted by gross illegalities that did not infringe the defendant’s constitutional rights. The United States contends that this approach- — as applied in this case— upsets the careful balance of interests embodied in the Fourth Amendment decisions of this Court. In the Government’s view, such an extension of the supervisory power would enable federal courts to exercise a standardless discretion in their application of the exclusionary rule to enforce the Fourth Amendment. We agree with the Government.</p>
<p id="b775-5">Ill</p>
<p id="b775-6">We certainly can understand the District Court’s commendable desire to deter deliberate intrusions into the privacy of persons who are unlikely to become defendants in a criminal prosecution. See <span class="citation" data-id="1417027"><a href="/opinion/1417027/united-states-v-payner/#135" aria-description="Citation for case: United States v. Payner">434 F. Supp., at 135</a></span>. No court should condone the unconstitutional and possibly criminal behavior of those who planned and executed this “briefcase caper.” <footnotemark>5</footnotemark> <page-number citation-index="1" label="734">*734</page-number>Indeed, the decisions of this Court are replete with denunciations of willfully lawless activities undertaken in the name of law enforcement. <em>E. g., Jackson </em>v. <em>Denno, </em><span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#386" aria-description="Citation for case: Jackson v. Denno">378 U. S. 368, 386</a></span> (1964); see <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#485" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 485</a></span> (1928) (Brandéis, J., dissenting). But our cases also show that these unexceptional principles do not command the exclusion of evidence in every case of illegality. Instead, they must be weighed against the considerable harm that would flow from indiscriminate application of an exclusionary rule.</p>
<p id="b776-5">Thus, the exclusionary rule “has been restricted to those areas where its remedial objectives are most efficaciously served.” <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 348</a></span> (1974). The Court has acknowledged that the suppression of probative but tainted evidence exacts a costly toll upon the ability of courts to ascertain the truth in a criminal case. <em>E. g., Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#137" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 137-138</a></span>; <em>United States </em>v. <em>Ceccolini, </em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#275" aria-description="Citation for case: United States v. Ceccolini">435 U. S. 268, 275-279</a></span> (1978); <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#489" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 489-491</a></span> (1976); see <em>Michigan </em>v. <em>Tucker, </em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#450" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 450-451</a></span> (1974).<footnotemark>6</footnotemark> Our cases have consistently recognized that unbending application of the exclusionary sanction to enforce ideals of governmental rectitude would impede unacceptably the truth-finding functions of judge and jury. <em>E. g., Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#485" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 485-489</a></span>; <em>United States </em>v. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>. After all, it is the defendant, and not the constable, who stands trial.</p>
<p id="b776-6">The same societal interests are at risk when a criminal defendant invokes the supervisory power to suppress evidence seized in violation of a third party’s constitutional rights. The supervisory power is applied with some caution even <page-number citation-index="1" label="735">*735</page-number>when the defendant asserts a violation of his own rights.<footnotemark>7</footnotemark> In <em>United States </em>v. <em>Caceres, </em><span class="citation" data-id="9427514"><a href="/opinion/110049/united-states-v-caceres/#754" aria-description="Citation for case: United States v. Caceres">440 U. S. 741, 754-757</a></span> (1979), we refused to exclude all evidence tainted by violations of an executive department’s rules. And in <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#216" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 216</a></span> (1960), the Court called for a restrained application of the supervisory power.</p>
<blockquote id="b777-5">“[A]ny apparent limitation upon the process of discovering truth in a federal trial ought to be imposed only upon the basis of considerations which outweigh the genera] need for untrammeled disclosure of competent and relevant evidence in a court of justice.” <em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">Ibid.</a></span></em></blockquote>
<p id="b777-6">See also <em>Nardone </em>v. <em>United States, </em><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#340" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 340</a></span> (1939).</p>
<p id="b777-7">We conclude that the supervisory power does not authorize a federal court to suppress otherwise admissible evidence on the ground that it was seized unlawfully from a third party not before the court. Our Fourth Amendment decisions have established beyond any doubt that the interest in deterring illegal searches does not justify the exclusion of tainted evidence at the instance of a party who was not the victim of the challenged practices. <em>Rakas </em>v. <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#137" aria-description="Citation for case: Rakas v. Illinois"><em>Illinois, supra, </em>at 137</a></span>; <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States">394 U. S., at 174-175</a></span>.<footnotemark>8</footnotemark> <page-number citation-index="1" label="736">*736</page-number>The values assigned to the competing interests do not change because a court has elected to analyze the question under the supervisory power instead of the Fourth Amendment. In either case, the need to deter the underlying conduct and the detrimental impact of excluding the evidence remain precisely the same.</p>
<p id="b778-5">The District Court erred, therefore, when it concluded that <page-number citation-index="1" label="737">*737</page-number>“society’s interest in deterring [bad faith] conduct by exclusion outweigh [s] society’s interest in furnishing the trier of fact with all relevant evidence.” <span class="citation" data-id="1417027"><a href="/opinion/1417027/united-states-v-payner/#135" aria-description="Citation for case: United States v. Payner">434 F. Supp., at 135</a></span>. This reasoning, which the Court of Appeals affirmed, amounts to a substitution of individual judgment for the controlling decisions of this Court.<footnotemark>9</footnotemark> Were we to accept this use of the supervisory power, we would confer on the judiciary discretionary power to disregard the considered limitations of the law it is charged with enforcing. We hold that the supervisory power does not extend so far.</p>
<p id="b779-5">The judgment of the Court of Appeals is</p>
<p id="b779-6">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b770-14"> Title <span class="citation no-link">18 U. S. C. § 1001</span> provides in relevant part:</p>
<blockquote id="b770-15">“Whoever, in any matter within the jurisdiction of any department or agency of the United States knowingly and willfully . . . makes any false, fictitious or fraudulent statements or representations, . . . shall be fined not more than $10,000 or imprisoned not more than five years, or both.”</blockquote>
</footnote>
<footnote label="2">
<p id="b771-7"> The unusual sequence of rulings was a byproduct of the consolidated hearing conducted by the District Court. The court initially failed to enter judgment on the merits. At the close of the evidence, it simply granted respondent’s motion to suppress. After the Court of Appeals for the Sixth Circuit dismissed the Government’s appeal for want of jurisdiction, the District Court vacated the order granting the motion to suppress and entered a verdict of guilty. The court then reinstated its suppression order and set aside the verdict. Respondent does not challenge these procedures.</p>
</footnote>
<footnote label="3">
<p id="b772-7"> The United States argued in the District Court and the Court of Appeals that the guarantee agreement was discovered through an independent investigation untainted by the briefcase search. The Government also <page-number citation-index="1" label="731">*731</page-number>denied that its agents willfully encouraged Casper’s illegal behavior. For purposes of this opinion, we need not question the District Court’s contrary findings on either point.</p>
</footnote>
<footnote label="4">
<p id="b774-5"><em> </em>We are not persuaded by respondent’s suggestion that the Bahamian law of bank secrecy creates an expectation of privacy not present in <em>United States </em>v. <em>Miller, </em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">425 U. S. 435</a></span> (1976). At the outset, it is not clear that secret information regarding this respondent’s account played any role in the investigation that led to the discovery of the critical loan guarantee agreement. See <em>swpra, </em>at 730. Even if the causal link were established, however, respondent’s claim lacks merit. He cites a provision, 1909 Bah. Acts, ch. 4, that is no longer in effect. Bank secrecy is now safeguarded by § 19 of the Banks Act, Bah. Islands Rev. Laws, ch. 96 (1965), as added, 1965 Bah. Acts, No. 65, which provides in relevant part:</p>
<blockquote id="b774-8">“(1) Except for the purpose of the performance of his duties or the exercise of his functions under this Act or when lawfully required to do so by any court of competent jurisdiction within the Colony or under the provisions of any law, no person shall disclose any information relating to the affairs of . . . the customer of a bank which he has acquired in the performance of his duties or the exercise of his functions under this Act.” See also the Banks and Trust Companies Regulation Act, 1965 Bah. Acts, No. 64, § 10, as amended, 1968 Bah. Acts, No. 34, 1969 Bah. Acts, No. 20, 1971 Bah. Acts, No. 15. The statute is hardly a blanket guarantee of privacy. Its application is limited; it is hedged with exceptions; and we have been directed to no authority construing its terms. Moreover, American depositors know that their own country requires them to report relationships with foreign financial institutions. <span class="citation no-link">31 U. S. C. §1121</span>; <span class="citation no-link">31 CFR §103.24</span> (1979). See generally <em>California Bankers Assn. </em>v. <em>Shultz, </em><span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#59" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S. 21, 59-63, 71-76</a></span> (1974). We conclude that respondent lacked a reasonable expectation of privacy in the Castle Bank records that documented his account.</blockquote>
</footnote>
<footnote label="5">
<p id="b775-7"> “The security of persons and property remains a fundamental value which law enforcement officers must respect. Nor should those who flout the rules escape unscathed.” <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#175" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 175</a></span> (1969). We note that in 1976 Congress investigated the improprieties revealed in this record. See Oversight Hearings into the Operations of the IRS before a Subcommittee of the House Committee on Government Operations (Operation Tradewinds, Project Haven, and Narcotics Traffickers Tax Program), 94th Cong., 1st Sess. (1975). As a result, the Commissioner of Internal Revenue “called off” Operation Trade Winds. Tr. of Oral Arg. 35. The Commissioner also adopted guidelines that require agents to instruct informants on the requirements of the law and to report known illegalities to a supervisory officer, who is in turn directed to notify appropriate state authorities. IR Manual §§ 9373.3 (3), 9373.4 (Manual Transmittal 9-21, Dec. 27, 1977). Although these measures appear on their face to be less positive than one might expect from an agency charged with upholding the law, they do indicate disapproval of the practices found to have been implemented in this case. We cannot assume that similar lawless conduct, if brought to the attention of <page-number citation-index="1" label="734">*734</page-number>responsible officials, would not be dealt with appropriately. To require in addition the suppression of highly probative evidence in a trial against a third party would penalize society unnecessarily.</p>
</footnote>
<footnote label="6">
<p id="b776-10"> See also <em>Kaufman </em>v. <em>United States, </em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#237" aria-description="Citation for case: Kaufman v. United States">394 U. S. 217, 237-238</a></span> (1969) (Black, J., dissenting); Oaks, Studying the Exclusionary Rule in Search and Seizure, <span class="citation no-link">37 U. Chi. L. Rev. 665</span>, 736-746, 755-756 (1970).</p>
</footnote>
<footnote label="7">
<p id="b777-8"> Federal courts may use their supervisory power in some circumstances to exclude evidence taken from the <em>defendant </em>by “willful disobedience of law.” <em>McNabb </em>v. <em>United States, </em><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/#345" aria-description="Citation for case: McNabb v. United States">318 U. S. 332, 345</a></span> (1943); see <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#223" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 223</a></span> (1960); <em>Rea </em>v. <em>United States, </em><span class="citation" data-id="9421227"><a href="/opinion/105343/rea-v-united-states/#216" aria-description="Citation for case: Rea v. United States">350 U. S. 214, 216-217</a></span> (1956); cf. <em>Hampton </em>v. <em>United States, </em><span class="citation" data-id="9426380"><a href="/opinion/109437/hampton-v-united-states/#495" aria-description="Citation for case: Hampton v. United States">425 U. S. 484, 495</a></span> (1976) (Powell, J., concurring in judgment). This Court has never held, however, that the supervisory power authorizes suppression of evidence obtained from third parties in violation of Constitution, statute, or rule. The supervisory power merely permits federal courts to supervise “the administration of criminal justice” among the parties before the bar. <em>McNabb </em>v. <em>United States, supra, </em>at 340.</p>
</footnote>
<footnote label="8">
<p id="b777-9"> “The deterrent values of preventing the incrimination of those whose rights the police have violated have been considered sufficient to justify the suppression of probative evidence even though the case against the defendant is weakened or destroyed. We adhere to that judgment. But <page-number citation-index="1" label="736">*736</page-number>we are not convinced that the additional benefits of extending the exclusionary rule to other defendants would justify further encroachment upon the public interest in prosecuting those accused of crime and having them acquitted or convicted on the basis of all the evidence which exposes the truth.” <em>Alderman </em>v. <em>United States, </em>394 U. S., at 174-175. See also <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#488" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 488-489</a></span> (1976); <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 348</a></span> (1974).</p>
<p id="AaX4">The dissent, <em>post, </em>at 746, urges that the balance of interests under the supervisory power differs from that considered in <em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">Alderman</a></span> </em>and like cases, because the supervisory power focuses upon the “need to protect the integrity of the federal courts.” Although the District Court in this case relied upon a deterrent rationale, we agree that the supervisory power serves the “twofold” purpose of deterring illegality and protecting judicial integrity. See <em>post, </em>at 744. As the dissent recognizes, however, the Fourth Amendment exclusionary rule serves precisely the same purposes. <em>Ibid., </em>citing, <em>inter alia, Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#218" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 218</a></span> (1979), and <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#659" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 659-660</a></span> (1961). Thus, the Fourth Amendment exclusionary rule, like the supervisory power, is applied in part “to protect the integrity of the <em>court, </em>rather than to vindicate the constitutional rights of the defendant. . . .” <em>Post, </em>at 747; see generally <em>Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 486</a></span>; <em>United States </em>v. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>.</p>
<p id="AxV">In this case, where the illegal conduct did not violate the respondent’s rights, the interest in preserving judicial integrity and in deterring such conduct is outweighed by the societal interest in presenting probative evidence to the trier to fact. See the first paragraph, <em>supra; </em>see also, <em>e. g., Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#485" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 485-486</a></span>. None of the cases cited by the dissent, <em>post, </em>at 7444745, supports a contrary view, since none of those cases involved criminal defendants who were not themselves the victims of the challenged practices. Thus, our decision today does not limit the traditional scope of the supervisory power in any way; nor does it render that power “superfluous.” <em>Post, </em>at 748. We merely reject its use as a substitute for established Fourth Amendment doctrine.</p>
</footnote>
<footnote label="9">
<p id="b779-10"> The same difficulty attends respondent’s claim to the protections of the Due Process Clause of the Fifth Amendment. The Court of Appeals expressly declined to consider the Due Process Clause. But even if we assume that the unlawful briefcase search was so outrageous as to offend fundamental “ ‘canons of decency and fairness/ ” <em>Rochin </em>v. <em>California, </em><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#169" aria-description="Citation for case: Rochin v. California">342 U. S. 165, 169</a></span> (1952), quoting <em>Malinshi </em>v. <em>New York, </em><span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#417" aria-description="Citation for case: Malinski v. New York">324 U. S. 401, 417</a></span> (1945) (opinion of Frankfurter, J.), the fact remains that “[t]he limitations of the Due Process Clause . . . come into play only when the Government activity in question violates some protected right of the <em>defendant,” Hampton </em>v. <em>United States, supra, </em>at 490 (plurality opinion).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Place.md  (`case`, 6 assertions)

### content_page

```
---
title: "United States v. Place"
type: case
citation: "462 U.S. 696 (1983)"
parallel_cite: "103 S. Ct. 2637; 77 L. Ed. 2d 110; 51 U.S.L.W. 4844"
neutral_cite: 1983 U.S. LEXIS 74
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-06-20
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1983-06-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Place
  varies_by_point: false
  scope_note: "Good law. The luggage dog-sniff-is-not-a-search holding was applied in Illinois v. Caballes (2005); Florida v. Jardines (2013) held a dog sniff at a home's curtilage IS a search (trespass), a boundary on context, not an overruling. The duration holding is developed by United States v. Sharpe (no rigid time limit) and Rodriguez v. United States (no prolongation)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110979/united-states-v-place/"
  cluster_id: 110979
  opinion_id: 9429264
  identity_checked: true
homes:
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Key — boundary"
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Limiting (duration)"
related: ["[[Illinois v. Caballes]]", "[[Florida v. Jardines]]", "[[Terry v. Ohio]]", "[[Rodriguez v. United States]]", "[[United States v. Sharpe]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "seizure", "dog-sniff", "luggage", "terry-stop", "duration"]
holding: "A canine sniff of luggage in a public place is sui generis and not a search; but a 90-minute investigative seizure of the luggage exceeded the permissible limits of a Terry stop."
lake:
  record_id: United States v. Place
  status: verified
  projected_at: 2026-07-06
---

# United States v. Place

*462 U.S. 696 (1983)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
DEA agents, suspicious of Place at LaGuardia, seized his luggage when he refused to consent to a search, told him they would take it to a judge, and transported it to another airport for a dog sniff. About 90 minutes after the seizure, a trained dog alerted to one bag. Agents held the bags over the weekend, got a warrant Monday, and found cocaine. Place moved to suppress.

## Issue
(1) Whether subjecting luggage in a public place to a trained narcotics dog's sniff is a Fourth Amendment "search." (2) Whether the 90-minute seizure of the luggage on reasonable suspicion was a permissible *[[Terry v. Ohio|Terry]]*-type investigative detention.

## Rule
**Dog sniff.** A canine sniff of luggage is unique and not a search: "the canine sniff is *sui generis*. We are aware of no other investigative procedure that is so limited both in the manner in which the information is obtained and in the content of the information revealed by the procedure. Therefore, we conclude that the particular course of investigation that the agents intended to pursue here — exposure of respondent's luggage, which was located in a public place, to a trained canine — did not constitute a 'search' within the meaning of the Fourth Amendment." — 462 U.S. at 707. ^pin-707

**Duration of the seizure.** *[[Terry v. Ohio|Terry]]* principles can justify a brief seizure of luggage on reasonable suspicion, but the detention here was too long: "Under this standard, it is clear that the police conduct here exceeded the permissible limits of a *Terry*-type investigative stop. The length of the detention of respondent's luggage alone precludes the conclusion that the seizure was reasonable in the absence of probable cause." — *Id.* at 709. ^pin-709

## Application
The dog sniff itself, performed on luggage in a public airport, disclosed only the presence or absence of contraband and so was not a search. But the seizure of the bags was unreasonable: agents knew of Place's arrival hours in advance and could have arranged for a dog, yet detained his luggage roughly 90 minutes without probable cause — a detention whose length alone took it beyond the bounds of a brief investigative stop. The cocaine, the fruit of that overlong seizure, was suppressed.

## Conclusion
The dog sniff was not a search, but the 90-minute seizure of the luggage exceeded *[[Terry v. Ohio|Terry]]* and was unreasonable absent probable cause. *Place* anchors the dog-sniff doctrine and limits the permissible duration of investigative property seizures.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Dog-sniff holding applied to vehicles in [[Illinois v. Caballes]]; bounded at the home's [[Curtilage|curtilage]] by [[Florida v. Jardines]]. Duration analysis developed by [[United States v. Sharpe]] (no rigid time limit; diligence test) and [[Rodriguez v. United States]] (a stop may not be prolonged even briefly for a sniff absent reasonable suspicion).

## Appears on
- [[Reasonable Expectation of Privacy]] — *Key — boundary*
- [[Terry Stops and Reasonable Suspicion]] — *Limiting (duration)*

## Sources
- *United States v. Place*, 462 U.S. 696 (1983) — https://www.courtlistener.com/opinion/110979/united-states-v-place/ — pinpoints: 707, 709.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4a048364df8b5a83", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "462 U.S. 696 (1983)", "court": "U.S. Supreme Court", "neutral_cite": "1983 U.S. LEXIS 74", "official_citation_present": true, "parallel_cite": "103 S. Ct. 2637; 77 L. Ed. 2d 110; 51 U.S.L.W. 4844", "title": "United States v. Place", "year": "1983"}}
{"assertion_id": "0708550558f74575", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Expectation of Privacy"}, "payload": {"home": "Reasonable Expectation of Privacy", "role": "Key — boundary", "title": "United States v. Place"}}
{"assertion_id": "81baf6af6217f4b8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A canine sniff of luggage in a public place is sui generis and not a search; but a 90-minute investigative seizure of the luggage exceeded the permissible limits of a Terry stop.", "title": "United States v. Place"}}
{"assertion_id": "e2b8d8d77c1d941d", "dimension": "support", "kind": "home_role", "locator": {"home": "Terry Stops and Reasonable Suspicion"}, "payload": {"home": "Terry Stops and Reasonable Suspicion", "role": "Limiting (duration)", "title": "United States v. Place"}}
{"assertion_id": "4836ffb6adf32f9b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1983-06-20", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Place", "field_i_validity": "good_law", "scope_note": "Good law. The luggage dog-sniff-is-not-a-search holding was applied in Illinois v. Caballes (2005); Florida v. Jardines (2013) held a dog sniff at a home's curtilage IS a search (trespass), a boundary on context, not an overruling. The duration holding is developed by United States v. Sharpe (no rigid time limit) and Rodriguez v. United States (no prolongation).", "title": "United States v. Place", "varies_by_point": "false"}}
{"assertion_id": "67b5fa0417ba07df", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Place"}}
```

### lake record — United States v. Place

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Place",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Place",
    "case_name_short": "Place",
    "case_name_full": "United States v. Place",
    "input_case_name": "United States v. Place",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-06-20",
    "year": 1983,
    "docket": null,
    "cluster_id": 110979,
    "lead_opinion_id": 9429264,
    "sibling_ids": [
      110979,
      9429264,
      9429265,
      9429266
    ],
    "absolute_url": "/opinion/110979/united-states-v-place/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "462 U.S. 696",
      "volume": "462",
      "reporter": "U.S.",
      "page": "696",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 2637",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2637",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 2d 110",
        "volume": "77",
        "reporter": "L. Ed. 2d",
        "page": "110",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4844",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4844",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 74",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "74",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "462 U.S. 696",
        "volume": "462",
        "reporter": "U.S.",
        "page": "696",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 2637",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2637",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 2d 110",
        "volume": "77",
        "reporter": "L. Ed. 2d",
        "page": "110",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 74",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "74",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4844",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4844",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "462 U.S. 696",
    "official_selection": {
      "court_class": "scotus",
      "selected": "462 U.S. 696",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-707",
      "page": null,
      "quote": "(2) Whether the 90-minute seizure of the luggage on reasonable suspicion was a permissible *Terry*-type investigative detention. ## Rule **Dog sniff.** A canine sniff of luggage is unique and not a search:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-709",
      "page": null,
      "quote": "Under this standard, it is clear that the police conduct here exceeded the permissible limits of a *Terry*-type investigative stop. The length of the detention of respondent's luggage alone precludes the conclusion that the seizure was reasonable in the absence of probable cause.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1983-06-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Place",
    "varies_by_point": false,
    "scope_note": "Good law. The luggage dog-sniff-is-not-a-search holding was applied in Illinois v. Caballes (2005); Florida v. Jardines (2013) held a dog sniff at a home's curtilage IS a search (trespass), a boundary on context, not an overruling. The duration holding is developed by United States v. Sharpe (no rigid time limit) and Rodriguez v. United States (no prolongation).",
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
        "journal_ref": "United States v. Place:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jerel Chinedu Igboji v. State",
          "cluster_id": 4789820,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane1_negative"
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
        "journal_ref": "United States v. Place:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Darrell Mark Babcock",
          "cluster_id": 4623035,
          "cite": [
            "924 F.3d 1180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Graham v. Connor",
          "cluster_id": 112257,
          "cite": [
            "104 L. Ed. 2d 443",
            "109 S. Ct. 1865",
            "490 U.S. 386",
            "1989 U.S. LEXIS 2467",
            "57 U.S.L.W. 4513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. Harris",
          "cluster_id": 145738,
          "cite": [
            "167 L. Ed. 2d 686",
            "127 S. Ct. 1769",
            "550 U.S. 372",
            "2007 U.S. LEXIS 4748"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hudson v. Palmer",
          "cluster_id": 111252,
          "cite": [
            "82 L. Ed. 2d 393",
            "104 S. Ct. 3194",
            "468 U.S. 517",
            "1984 U.S. LEXIS 143",
            "52 U.S.L.W. 5052"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Hodari D.",
          "cluster_id": 112579,
          "cite": [
            "113 L. Ed. 2d 690",
            "111 S. Ct. 1547",
            "499 U.S. 621",
            "1991 U.S. LEXIS 2397",
            "91 Cal. Daily Op. Serv. 2893",
            "59 U.S.L.W. 4335",
            "91 Daily Journal DAR 4665"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sharpe",
          "cluster_id": 111378,
          "cite": [
            "84 L. Ed. 2d 605",
            "105 S. Ct. 1568",
            "470 U.S. 675",
            "1985 U.S. LEXIS 74",
            "53 U.S.L.W. 4346"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hensley",
          "cluster_id": 111294,
          "cite": [
            "83 L. Ed. 2d 604",
            "105 S. Ct. 675",
            "469 U.S. 221",
            "1985 U.S. LEXIS 34",
            "53 U.S.L.W. 4053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Buie",
          "cluster_id": 112384,
          "cite": [
            "108 L. Ed. 2d 276",
            "110 S. Ct. 1093",
            "494 U.S. 325",
            "1990 U.S. LEXIS 1176"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Caballes",
          "cluster_id": 137742,
          "cite": [
            "160 L. Ed. 2d 842",
            "125 S. Ct. 834",
            "543 U.S. 405",
            "2005 U.S. LEXIS 769"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Indianapolis v. Edmond",
          "cluster_id": 118391,
          "cite": [
            "148 L. Ed. 2d 333",
            "121 S. Ct. 447",
            "531 U.S. 32",
            "2000 U.S. LEXIS 8084",
            "69 U.S.L.W. 4009",
            "14 Fla. L. Weekly Fed. S 9",
            "2000 Colo. J. C.A.R. 6401",
            "2000 Cal. Daily Op. Serv. 9549"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Place:lane2_top_cited"
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
        "journal_ref": "United States v. Place:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110979 OR 9429264 OR 9429265 OR 9429266) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTI2NTE1MjAwMDAwJnM9NDQ5OTAxOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110979+OR+9429264+OR+9429265+OR+9429266%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110979 OR 9429264 OR 9429265 OR 9429266)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00NDUmcz0yMzE2NjU4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110979+OR+9429264+OR+9429265+OR+9429266%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110979 OR 9429264 OR 9429265 OR 9429266)",
        "reviewed": 74,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 74,
        "triage_read": 1,
        "triage_snippet_classified": 73
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110979 OR 9429264 OR 9429265 OR 9429266)",
    "indexed_citing_opinions": 2066,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110979,
        "count": 1822,
        "count_source": "search"
      },
      {
        "opinion_id": 9429264,
        "count": 275,
        "count_source": "search"
      },
      {
        "opinion_id": 9429265,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429266,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3379,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-place.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNDI4NjImcz0xMDM1MDM5NyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110979+OR+9429264+OR+9429265+OR+9429266%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110979,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 107900,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 108099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110351,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110501,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 110926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 394856,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110979,
        "cited_id": 1652001,
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
    "date_created": "2026-07-06T02:17:45Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:18:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:18:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:21:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:18:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Place

```
<opinion type="majority">
<author id="b741-11">Justice O’Connor</author>
<p id="Abc">delivered the opinion of the Court.</p>
<p id="b741-12">This case presents the issue whether the Fourth Amendment prohibits law enforcement authorities from temporarily <page-number citation-index="1" label="698">*698</page-number>detaining personal luggage for exposure to a trained narcotics detection dog on the basis of reasonable suspicion that the luggage contains narcotics. Given the enforcement problems associated with the detection of narcotics trafficking and the minimal intrusion that a properly limited detention would entail, we conclude that the Fourth Amendment does not prohibit such a detention. On the facts of this case, however, we hold that the police conduct exceeded the bounds of a permissible investigative detention of the luggage.</p>
<p id="AHiy">pH</p>
<p id="ATD">Respondent Raymond J. Place’s behavior aroused the suspicions of law enforcement officers as he waited in line at the Miami International Airport to purchase a ticket to New York’s La Guardia Airport. As Place proceeded to the gate for his flight, the agents approached him and requested his airline ticket and some identification. Place complied with the request and consented to a search of the two suitcases he had checked. Because his flight was about to depart, however, the agents decided not to search the luggage.</p>
<p id="Ano">Prompted by Place’s parting remark that he had recognized that they were police, the agents inspected the address tags on the checked luggage and noted discrepancies in the two street addresses. Further investigation revealed that neither address existed and that the telephone number Place had given the airline belonged to a third address on the same street. On the basis of their encounter with Place and this information, the Miami agents called Drug Enforcement Administration (DEA) authorities in New York to relay their information about Place.</p>
<p id="AJD">Two DEA agents waited for Place at the arrival gate at La Guardia Airport in New York. There again, his behavior aroused the suspicion of the agents. After he had claimed his two bags and called a limousine, the agents decided to approach him. They identified themselves as federal narcotics agents, to which Place responded that he knew they were “cops” and had spotted them as soon as he had deplaned. <page-number citation-index="1" label="699">*699</page-number>One of the agents informed Place that, based on their own observations and information obtained from the Miami authorities, they believed that he might be carrying narcotics. After identifying the bags as belonging to him, Place stated that a number of police at the Miami Airport had surrounded him and searched his baggage. The agents responded that their information was to the contrary. The agents requested and received identification from Place — a New Jersey driver’s license, on which the agents later ran a computer check that disclosed no offenses, and his airline ticket receipt. When Place refused to consent to a search of his luggage, one of the agents told him that they were going to take the luggage to a federal judge to try to obtain a search warrant and that Place was free to accompany them. Place declined, but obtained from one of the agents telephone numbers at which the agents could be reached.</p>
<p id="b743-5">The agents then took the bags to Kennedy Airport, where they subjected the bags to a “sniff test” by a trained narcotics detection dog. The dog reacted positively to the smaller of the two bags but ambiguously to the larger bag. Approximately 90 minutes had elapsed since the seizure of respondent’s luggage. Because it was late on a Friday afternoon, the agents retained the luggage until Monday morning, when they secured a search warrant from a Magistrate for the smaller bag. Upon opening that bag, the agents discovered 1,125 grams of cocaine.</p>
<p id="b743-6">Place was indicted for possession of cocaine with intent to distribute in violation of <span class="citation no-link">21 U. S. C. § 841</span>(a)(1). In the District Court, Place moved to suppress the contents of the luggage seized from him at La Guardia Airport, claiming that the warrantless seizure of the luggage violated his Fourth Amendment rights.<footnotemark>1</footnotemark> The District Court denied the motion. <page-number citation-index="1" label="700">*700</page-number>Applying the standard of <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), to the detention of personal property, it concluded that detention of the bags could be justified if based on reasonable suspicion to believe that the bags contained narcotics. Finding reasonable suspicion, the District Court held that Place’s Fourth Amendment rights were not violated by seizure of the bags by the DEA agents. <span class="citation" data-id="1652001"><a href="/opinion/1652001/united-states-v-place/#1228" aria-description="Citation for case: United States v. Place">498 F. Supp. 1217, 1228</a></span> (EDNY 1980). Place pleaded guilty to the possession charge, reserving the right to appeal the denial of his motion to suppress.</p>
<p id="b744-5">On appeal of the conviction, the United States Court of Appeals for the Second Circuit reversed. <span class="citation" data-id="9468411"><a href="/opinion/394856/united-states-v-raymond-j-place/" aria-description="Citation for case: United States v. Raymond J. Place">660 F. 2d 44</a></span> (1981). The majority assumed both that <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>principles could be applied to justify a warrantless seizure of baggage on less than probable cause and that reasonable suspicion existed to justify the investigatory stop of Place. The majority concluded, however, that the prolonged seizure of Place’s baggage exceeded the permissible limits of a Terry-type investigative stop and consequently amounted to a seizure without probable cause in violation of the Fourth Amendment.</p>
<p id="b744-6">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./457/1104/">457 U. S. 1104</a></span> (1982), and now affirm.</p>
<p id="b744-7">) — I h — I</p>
<p id="AgL">The Fourth Amendment protects the “right of the people to be secure in their persons, houses, papers, <em>and effects, </em>against unreasonable searches and seizures.” (Emphasis added.) Although in the context of personal property, and particularly containers, the Fourth Amendment challenge is <page-number citation-index="1" label="701">*701</page-number>typically to the subsequent search of the container rather than to its initial seizure by the authorities, our cases reveal some general principles regarding seizures. In the ordinary case, the Court has viewed a seizure of personal property as <em>per se </em>unreasonable within the meaning of the Fourth Amendment unless it is accomplished pursuant to a judicial warrant issued upon probable cause and particularly describing the items to be seized.<footnotemark>2</footnotemark> See, <em>e. g., Marron </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 196</a></span> (1927). Where law enforcement authorities have probable cause to believe that a container holds contraband or evidence of a crime, but have not secured a warrant, the Court has interpreted the Amendment to permit seizure of the property, pending issuance of a warrant to examine its contents, if the exigencies of the circumstances demand it or some other recognized exception to the warrant requirement is present. See, <em>e. g., Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#761" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 761</a></span> (1979); <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977); <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971).<footnotemark>3</footnotemark> For example, “objects such as weapons or contraband found in a public place may be seized by the police without a warrant,” <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#587" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 587</a></span> (1980), because, under these circumstances, the risk of the item’s disappearance or use for its intended purpose before a <page-number citation-index="1" label="702">*702</page-number>warrant may be obtained outweighs the interest in possession. See also <em>G. M. Leasing Corp. </em>v. <em>United States, </em><span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#354" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 354</a></span> (1977).</p>
<p id="b746-5">In this case, the Government asks us to recognize the reasonableness under the Fourth Amendment of warrantless seizures of personal luggage from the custody of the owner on the basis of less than probable cause, for the purpose of pursuing a limited course of investigation, short of opening the luggage, that would quickly confirm or dispel the authorities’ suspicion. Specifically, we are asked to apply the principles of <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra,</a></span> </em>to permit such seizures on the basis of reasonable, articulable suspicion, premised on objective facts, that the luggage contains contraband or evidence of a crime. In our view, such application is appropriate.</p>
<p id="b746-6">In <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>the Court first recognized “the narrow authority of police officers who suspect criminal activity to make limited intrusions on an individual’s personal security based on less than probable cause.” <em>Michigan </em>v. <em>Summers, </em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#698" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 698</a></span> (1981). In approving the limited search for weapons, or “frisk,” of an individual the police reasonably believed to be armed and dangerous, the Court implicitly acknowledged the authority of the police to make a <em>forcible stop </em>of a person when the officer has reasonable, articulable suspicion that the person has been, is, or is about to be engaged in criminal activity. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 22</a></span>.<footnotemark>4</footnotemark> That implicit proposition was embraced openly in <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 146</a></span> (1972), where the Court relied on <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>to hold that the police officer lawfully made a forcible stop of the suspect to investigate an informant’s tip that the suspect was carry<page-number citation-index="1" label="703">*703</page-number>ing narcotics and a concealed weapon. See also <em>Michigan </em>v. <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers, supra</a></span> </em>(limited detention of occupants while authorities search premises pursuant to valid search warrant); <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">449 U. S. 411</a></span> (1981) (stop near border of vehicle suspected of transporting illegal aliens); <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975) (brief investigative stop near border for questioning about citizenship and immigration status).</p>
<p id="b747-4">The exception to the probable-cause requirement for limited seizures of the person recognized in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>and its progeny rests on a balancing of the competing interests to determine the reasonableness of the type of seizure involved within the meaning of “the Fourth Amendment’s general proscription against unreasonable searches and seizures.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20</a></span>. We must balance the nature and quality of the intrusion on the individual’s Fourth Amendment interests against the importance of the governmental interests alleged to justify the intrusion. When the nature and extent of the detention are minimally intrusive of the individual’s Fourth Amendment interests, the opposing law enforcement interests can support a seizure based on less than probable cause.</p>
<p id="b747-5">We examine first the governmental interest offered as a justification for a brief seizure of luggage from the suspect’s custody for the purpose of pursuing a limited course of investigation. The Government contends that, where the authorities possess specific and articulable facts warranting a reasonable belief that a traveler’s luggage contains narcotics, the governmental interest in seizing the luggage briefly to pursue further investigation is substantial. We agree. As observed in <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#561" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 561</a></span> (1980) (opinion of Powell, J.), “[t]he public has a compelling interest in detecting those who would traffic in deadly drugs for personal profit.”</p>
<p id="b747-6">Respondent suggests that, absent some special law enforcement interest such as officer safety, a generalized interest in law enforcement cannot justify an intrusion on an individual’s Fourth Amendment interests in the absence of <page-number citation-index="1" label="704">*704</page-number>probable cause. Our prior cases, however, do not support this proposition. In <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>we described the governmental interests supporting the initial seizure of the person as “effective crime prevention and detection; it is this interest which underlies the recognition that a police officer may in appropriate circumstances and in an appropriate manner approach a person for purposes of investigating possibly criminal behavior even though there is no probable cause to make an arrest.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 22</a></span>. Similarly, in <em>Michigan </em>v. <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>we identified three law enforcement interests that justified limited detention of the occupants of the premises during execution of a valid search warrant: “preventing flight in the event that incriminating evidence is found,” “minimizing the risk of harm” both to the officers and the occupants, and “orderly completion of the search.” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers">452 U. S., at 702-703</a></span>. Cf. <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#500" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 500</a></span> (1983) (plurality opinion) (“The predicate permitting seizures on suspicion short of probable cause is that law enforcement interests warrant a limited intrusion on the personal security of the suspect”). The test is whether those interests are sufficiently “substantial,” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#699" aria-description="Citation for case: Michigan v. Summers">452 U. S., at 699</a></span>, not whether they are independent of the interest in investigating crimes effectively and apprehending suspects. The context of a particular law enforcement practice, of course, may affect the determination whether a brief intrusion on Fourth Amendment interests on less than probable cause is essential to effective criminal investigation. Because of the inherently transient nature of drug courier activity at airports, allowing police to make brief investigative stops of persons at airports on reasonable suspicion of drug-trafficking substantially enhances the likelihood that police will be able to prevent the flow of narcotics into distribution channels.<footnotemark>5</footnotemark></p>
<p id="b749-4"><page-number citation-index="1" label="705">*705</page-number>Against this strong governmental interest, we must weigh the nature and extent of the intrusion upon the individual’s Fourth Amendment rights when the police briefly detain luggage for limited investigative purposes. On this point, respondent Place urges that the rationale for a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop of the person is wholly inapplicable to investigative detentions of personalty. Specifically, the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>exception to the probable-cause requirement is premised on the notion that a <em>Terry-type </em>stop of the person is substantially less intrusive of a person’s liberty interests than a formal arrest. In the property context, however, Place urges, there are no degrees of intrusion. Once the owner’s property is seized, the dispossession is absolute.</p>
<p id="b749-5">We disagree. The intrusion on possessory interests occasioned by a seizure of one’s personal effects can vary both in its nature and extent. The seizure may be made after the owner has relinquished control of the property to a third party or, as here, from the immediate custody and control of the owner.<footnotemark>6</footnotemark> Moreover, the police may confine their investi<page-number citation-index="1" label="706">*706</page-number>gation to an on-the-spot inquiry — for example, immediate exposure of the luggage to a trained narcotics detection dog<footnotemark>7</footnotemark>— or transport the property to another location. Given the fact that seizures of property can vary in intrusiveness, some brief detentions of personal effects may be so minimally intrusive of Fourth Amendment interests that strong countervailing governmental interests will justify a seizure based only on specific articulable facts that the property contains contraband or evidence of a crime.</p>
<p id="b750-5">In sum, we conclude that when an officer’s observations lead him reasonably to believe that a traveler is carrying luggage that contains narcotics, the principles of <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>and its progeny would permit the officer to detain the luggage briefly to investigate the circumstances that aroused his suspicion, provided that the investigative detention is properly limited in scope.</p>
<p id="b750-6">The purpose for which respondent’s luggage was seized, of course, was to <em>arrange </em>its exposure to a narcotics detection dog. Obviously, if this investigative procedure is itself a search requiring probable cause, the initial seizure of respondent’s luggage for the purpose of subjecting it to the sniff test — no matter how brief — could not be justified on less than probable cause. See <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20</a></span>; <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#421" aria-description="Citation for case: United States v. Cortez">449 U. S., at 421</a></span>; <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 881-882</a></span>; <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S., at 146</a></span>.</p>
<p id="b750-7">The Fourth Amendment “protects people from unreasonable government intrusions into their legitimate expectations <page-number citation-index="1" label="707">*707</page-number>of privacy.” <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#7" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 7</a></span>. We have affirmed that a person possesses a privacy interest in the contents of personal luggage that is protected by the Fourth Amendment. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick"><em>Id., </em>at 13</a></span>. A “canine sniff” by a well-trained narcotics detection dog, however, does not require opening the luggage. It does not expose noncontraband items that otherwise would remain hidden from public view, as does, for example, an officer’s rummaging through the contents of the luggage. Thus, the manner in which information is obtained through this investigative technique is much less intrusive than a typical search. Moreover, the sniff discloses only the presence or absence of narcotics, a contraband item. Thus, despite the fact that the sniff tells the authorities something about the contents of the luggage, the information obtained is limited. This limited disclosure also ensures that the owner of the property is not subjected to the embarrassment and inconvenience entailed in less discriminate and more intrusive investigative methods.</p>
<p id="Axx">In these respects, the canine sniff is <em>sui generis. </em>We are aware of no other investigative procedure that is so limited both in the manner in which the information is obtained and in the content of the information revealed by the procedure. Therefore, we conclude that the particular course of investigation that the agents intended to pursue here — exposure of respondent’s luggage, which was located in a public place, to a trained canine — did not constitute a “search” within the meaning of the Fourth Amendment.</p>
<p id="A6V"><em>S </em>HH H-Í</p>
<p id="AHj">There is no doubt that the agents made a “seizure of Place’s luggage for purposes of the Fourth Amendment when, following his refusal to consent to a search, the agent told Place that he was going to take the luggage to a federal judge to secure issuance of a warrant. As we observed in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>“[t]he manner in which the seizure . . . [was] con<page-number citation-index="1" label="708">*708</page-number>ducted is, of course, as vital a part of the inquiry as whether [it was] warranted at all.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#28" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 28</a></span>. We therefore examine whether the agents’ conduct in this case was such as to place the seizure within the general rule requiring probable cause for a seizure or within <em>Terry’s </em>exception to that rule.</p>
<p id="b752-5">At the outset, we must reject the Government’s suggestion that the point at which probable cause for seizure of luggage from the person’s presence becomes necessary is more distant than in the case of a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop of the person himself. The premise of the Government’s argument is that seizures of property are generally less intrusive than seizures of the person. While true in some circumstances, that premise is faulty on the facts we address in this case. The precise type of detention we confront here is seizure of personal luggage from the immediate possession of the suspect for the purpose of arranging exposure to a narcotics detection dog. Particularly in the case of detention of luggage within the traveler’s immediate possession, the police conduct intrudes on both the suspect’s possessory interest in his luggage as well as his liberty interest in proceeding with his itinerary. The person whose luggage is detained is technically still free to continue his travels or carry out other personal activities pending release of the luggage. Moreover, he is not subjected to the coercive atmosphere of a custodial confinement or to the public indignity of being personally detained. Nevertheless, such a seizure can effectively restrain the person since he is subjected to the possible disruption of his travel plans in order to remain with his luggage or to arrange for its return.<footnotemark>8</footnotemark> Therefore, when the police seize luggage from the <page-number citation-index="1" label="709">*709</page-number>suspect’s custody, we think the limitations applicable to investigative detentions of the person should define the permissible scope of an investigative detention of the person’s luggage on less than probable cause. Under this standard, it is clear that the police conduct here exceeded the permissible limits of a Terry-type investigative stop.</p>
<p id="b753-5">The length of the detention of respondent’s luggage alone precludes the conclusion that the seizure was reasonable in the absence of probable cause. Although we have recognized the reasonableness of seizures longer than the momentary ones involved in <em>Terry, Adams, </em>and <em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span>, </em>see <em>Michigan </em>v. <em>Summers, </em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692</a></span> (1981), the brevity of the invasion of the individual’s Fourth Amendment interests is an important factor in determining whether the seizure is so minimally intrusive as to be justifiable on reasonable suspicion. Moreover, in assessing the effect of the length of the detention, we take into account whether the police diligently pursue their investigation. We note that here the New York agents knew the time of Place’s scheduled arrival at La Guardia, had ample time to arrange for their additional investigation at that location, and thereby could have minimized the intrusion on respondent’s Fourth Amendment interests.<footnotemark>9</footnotemark> Thus, although we decline to adopt any outside time limitation for a permissible <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop,<footnotemark>10</footnotemark> we have never <page-number citation-index="1" label="710">*710</page-number>approved a seizure of the person for the prolonged 90-minute period involved here and cannot do so on the facts presented by this case. See <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span> (1979).</p>
<p id="b754-5">Although the 90-minute detention of respondent’s luggage is sufficient to render the seizure unreasonable, the violation was exacerbated by the failure of the agents to accurately inform respondent of the place to which they were transporting his luggage, of the length of time he might be dispossessed, and of what arrangements would be made for return of the luggage if the investigation dispelled the suspicion. In short, we hold that the detention of respondent’s luggage in this case went beyond the narrow authority possessed by police to detain briefly luggage reasonably suspected to contain narcotics.</p>
<p id="b754-6">
<em>&gt;</em>
</p>
<p id="AXDH">We conclude that, under all of the circumstances of this case, the seizure of respondent’s luggage was unreasonable under the Fourth Amendment. Consequently, the evidence obtained from the subsequent search of his luggage was inadmissible, and Place’s conviction must be reversed. The judgment of the Court of Appeals, accordingly, is affirmed.</p>
<p id="Ab0">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b743-7"> In support of his motion, respondent also contended that the detention of his person at both the Miami and La Guardia Airports was not based on reasonable suspicion and that the “sniff test” of his luggage was conducted in a manner that tainted the dog’s reaction. <span class="citation" data-id="1652001"><a href="/opinion/1652001/united-states-v-place/#1221" aria-description="Citation for case: United States v. Place">498 F. Supp. 1217, 1221, 1228</a></span> <page-number citation-index="1" label="700">*700</page-number>(EDNY 1980). The District Court rejected both contentions. As to the former, it concluded that the agents had reasonable suspicion to believe that Place was engaged in criminal activity when he was detained at the two airports and that the stops were therefore lawful. <span class="citation" data-id="1652001"><a href="/opinion/1652001/united-states-v-place/#1225" aria-description="Citation for case: United States v. Place"><em>Id., </em>at 1225, 1226</a></span>. On appeal, the Court of Appeals did not reach this issue, assuming the existence of reasonable suspicion. Respondent Place cross-petitioned in this Court on the issue of reasonable suspicion, and we denied certiorari. <em>Place </em>v. <em>United States, </em><span class="citation" data-id="9032763"><a href="/opinion/9039428/place-v-united-states/" aria-description="Citation for case: Place v. United States">457 U. S. 1106</a></span> (1982). We therefore have no occasion to address the issue here.</p>
</footnote>
<footnote label="2">
<p id="b745-5"> The Warrant Clause of the Fourth Amendment provides that “no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.”</p>
</footnote>
<footnote label="3">
<p id="b745-6"> In <em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>, </em>the Court explained:</p>
<blockquote id="b745-7">“The police acted properly — indeed commendably — in apprehending respondent and his luggage. They had ample probable cause to believe that respondent’s green suitcase contained marihuana. . . . Having probable cause to believe that contraband was being driven away in the taxi, the police were justified in stopping the vehicle . . . and seizing the suitcase they suspected contained contraband.” 442 U. S., at 761.</blockquote>
<p id="b745-8">The Court went on to hold that the police violated the Fourth Amendment in immediately searching the luggage rather than first obtaining a warrant authorizing the search. <em>Id., </em>at 766. That holding was not affected by our recent decision in <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#824" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 824</a></span> (1982).</p>
</footnote>
<footnote label="4">
<p id="b746-7"><em> </em>In his concurring opinion in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>Justice Harlan made this logical underpinning of the Court’s Fourth Amendment holding clear:</p>
<blockquote id="b746-8">“In the first place, if the frisk is justified in order to protect the officer during an encounter with a citizen, the officer must first have constitutional grounds to insist on an encounter, to make a <em>forcible </em>stop. ... I would make it perfectly clear that the right to frisk in this case depends upon the reasonableness of a forcible stop to investigate a suspected crime.” 892 U. S., at 32-33.</blockquote>
</footnote>
<footnote label="5">
<p id="b748-5"> Referring to the problem of intercepting drug couriers in the Nation’s airports, Justice Powell has observed:</p>
<blockquote id="b748-6">“Much of the drug traffic is highly organized and conducted by sophisticated criminal syndicates. The profits are enormous. And many drugs . . . may be easily concealed. As a result, the obstacles to detection of <page-number citation-index="1" label="705">*705</page-number>illegal conduct may be unmatched in any other area of law enforcement.” <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#561" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 561-562</a></span> (1980).</blockquote>
<p id="b749-8">See <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#519" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 519</a></span> (1983) (Blackmun, J., dissenting) (“The special need for flexibility in uncovering illicit drug couriers is hardly debatable”) (airport context).</p>
</footnote>
<footnote label="6">
<p id="b749-11"> One need only compare the facts of this case with those in <em>United States </em>v. <em>Van Leeuwen, </em><span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/" aria-description="Citation for case: United States v. Van Leeuwen">397 U. S. 249</a></span> (1970). There the defendant had voluntarily relinquished two packages of coins to the postal authorities. Several facts aroused the suspicion of the postal officials, who detained the packages, without searching them, for about 29 hours while certain lines of inquiry were pursued. The information obtained during this time was sufficient to give the authorities probable cause to believe that the packages contained counterfeit coins. After obtaining a warrant, the authorities opened the packages, found counterfeit coins therein, resealed the packages, and sent them on their way. Expressly limiting its holding to the facts of the case, the Court concluded that the 29-hour detention of the packages on reasonable suspicion that they contained contraband did not violate the Fourth Amendment. <span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/#253" aria-description="Citation for case: United States v. Van Leeuwen"><em>Id., </em>at 253</a></span>.</p>
<p id="b749-12">As one commentator has noted, <em>“Van Leeuwen </em>was an easy case for the Court because the defendant was unable to show that the invasion intruded <page-number citation-index="1" label="706">*706</page-number>upon either a privacy interest in the contents of the packages or a posses-sory interest in the packages themselves.” 3 W. LaFave, Search and Seizure § 9.6, p. 71 (Supp. 1982).</p>
</footnote>
<footnote label="7">
<p id="b750-11"> Cf. <em>Florida </em>v. <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#502" aria-description="Citation for case: Florida v. Royer"><em>Royer, supra, </em>at 502</a></span> (plurality opinion) (“We agree with the State that [the officers had] adequate grounds for suspecting Royer of carrying drugs and for temporarily detaining him <em>and his luggage </em>while they attempted to verify or dispel their suspicions in a manner that did not exceed the limits of an investigative detention”) (emphasis added).</p>
</footnote>
<footnote label="8">
<p id="b752-6"> “At least when the authorities do not make it absolutely clear how they plan to reunite the suspect and his possessions at some future time and place, seizure of the object is tantamount to seizure of the person. This is because that person must either remain on the scene or else seemingly surrender his effects permanently to the police.” 3 W. LaFave, Search and Seizure § 9.6, p. 72 (Supp. 1982).</p>
</footnote>
<footnote label="9">
<p id="b753-6"> Cf. <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#506" aria-description="Citation for case: Florida v. Royer">460 U. S., at 506</a></span> (plurality opinion) (“If [trained narcotics detection dogs] had been used, Royer and his luggage could have been momentarily detained while this investigative procedure was carried out”). This course of conduct also would have avoided the further substantial intrusion on respondent’s possessory interests caused by the removal of his luggage to another location.</p>
</footnote>
<footnote label="10">
<p id="b753-7"> Cf. ALI, Model Code of Pre-Arraignment Procedure § 110.2(1) (1975) (recommending a maximum of 20 minutes for a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop). We understand the desirability of providing law enforcement authorities with a clear rule to guide their conduct. Nevertheless, we question the wisdom of a rigid time limitation. Such a limit would undermine the equally important need to allow authorities to graduate their responses to the demands of any particular situation.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Ramirez.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Ramirez"
type: case
citation: "523 U.S. 65 (1998)"
parallel_cite: "118 S. Ct. 992; 140 L. Ed. 2d 191"
neutral_cite: 1998 U.S. LEXIS 1600
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1998
date_decided: 1998-03-04
docket: 96-1469
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1998-03-04
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Ramirez
  varies_by_point: false
  scope_note: "Controlling: a no-knock entry that damages property is judged by the same Richards reasonable-suspicion standard — no heightened showing is required because property is destroyed — though excessive or unnecessary destruction may independently violate the Fourth Amendment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118180/united-states-v-ramirez/"
  cluster_id: 118180
  opinion_id: 118180
  identity_checked: true
homes:
  - page: "[[Knock-and-Announce]]"
    role: "Progeny"
related: ["[[Richards v. Wisconsin]]", "[[Wilson v. Arkansas]]", "[[United States v. Banks]]", "[[Sabbath v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "knock-and-announce", "no-knock", "warrant-execution", "property-damage"]
holding: "The Fourth Amendment does not impose a higher standard on a no-knock entry merely because the entry causes property damage; the entry is judged by Richards' reasonable-suspicion test, although excessive or unnecessary destruction of property in a search may itself violate the Fourth Amendment."
lake:
  record_id: United States v. Ramirez
  status: verified
  projected_at: 2026-07-09
---

# United States v. Ramirez

*523 U.S. 65 (1998)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers had a warrant connected to the search for Alan Shelby, a violent prison escapee reported to be hiding in Hernan Ramirez's home and to have access to a supply of weapons. Executing the warrant early one morning, the police announced their presence and broke a single window in Ramirez's garage — pointing a weapon through it to discourage anyone from rushing to the guns. Believing a burglary was underway, Ramirez fired a shot, then surrendered. Shelby was not found, but officers recovered firearms, and Ramirez (a felon) was charged with being a felon in possession. The District Court and Ninth Circuit suppressed the evidence, finding insufficient [[Exigent Circumstances and Hot Pursuit|exigency]] to justify the property destruction.

## Issue
Does the Fourth Amendment (or 18 U.S.C. § 3109) hold officers to a higher standard for a no-knock entry when the entry results in the destruction of property?

## Rule
No. "[W]hether the Fourth Amendment holds officers to a higher standard . . . when a 'no-knock' entry results in the destruction of property[,] [w]e hold that it does not." — 523 U.S. at 68. ^pin-68

"Under *Richards*, a no-knock entry is justified if police have a 'reasonable suspicion' that knocking and announcing would be dangerous, futile, or destructive to the purposes of the investigation. Whether such a 'reasonable suspicion' exists depends in no way on whether police must destroy property in order to enter." — *Id.* at 71. ^pin-71

The manner of entry is still constrained by reasonableness: "Excessive or unnecessary destruction of property in the course of a search may violate the Fourth Amendment, even though the entry itself is lawful and the fruits of the search are not subject to suppression." — [*Id.*](https://www.courtlistener.com/opinion/118180/united-states-v-ramirez/#:~:text=Excessive%20or%20unnecessary%20destruction%20of) ^pin-71b

Section 3109 codifies the common-law exceptions and imposes no greater requirement.

## Application
The police had reasonable suspicion that knocking and announcing would be dangerous: Shelby was a violent escapee, reportedly armed, who had vowed not to do federal time. Breaking a single garage window to deter a rush to weapons was a reasonable, limited method of entry, not excessive or unnecessary destruction. Because the *[[Richards v. Wisconsin|Richards]]* standard was satisfied and the property damage was reasonable, neither the Fourth Amendment nor § 3109 was violated.

## Conclusion
No Fourth Amendment or § 3109 violation occurred; the judgment suppressing the evidence was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Ramirez* remains controlling: property damage does not raise the bar for a no-knock entry, which is governed by the reasonable-suspicion standard of [[Richards v. Wisconsin]] (building on [[Wilson v. Arkansas]]), while excessive destruction can independently offend the Fourth Amendment. It is taught with [[United States v. Banks]] (timing of forcible entry) and [[Sabbath v. United States]] (what counts as an entry). No negative treatment.

## Appears on
- [[Knock-and-Announce]] — *Progeny*

## Sources
- *United States v. Ramirez*, 523 U.S. 65 (1998) — https://www.courtlistener.com/opinion/118180/united-states-v-ramirez/ — pinpoints: 68, 71.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "90ff1c437b75566e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "523 U.S. 65 (1998)", "court": "U.S. Supreme Court", "neutral_cite": "1998 U.S. LEXIS 1600", "official_citation_present": true, "parallel_cite": "118 S. Ct. 992; 140 L. Ed. 2d 191", "title": "United States v. Ramirez", "year": "1998"}}
{"assertion_id": "2349d64bb15bd17f", "dimension": "support", "kind": "home_role", "locator": {"home": "Knock-and-Announce"}, "payload": {"home": "Knock-and-Announce", "role": "Progeny", "title": "United States v. Ramirez"}}
{"assertion_id": "f0b0b29a1678fed3", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Fourth Amendment does not impose a higher standard on a no-knock entry merely because the entry causes property damage; the entry is judged by Richards' reasonable-suspicion test, although excessive or unnecessary destruction of property in a search may itself violate the Fourth Amendment.", "title": "United States v. Ramirez"}}
{"assertion_id": "559350ab4be93a46", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Ramirez"}}
{"assertion_id": "790947983db693c6", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1998-03-04", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Ramirez", "field_i_validity": "good_law", "scope_note": "Controlling: a no-knock entry that damages property is judged by the same Richards reasonable-suspicion standard — no heightened showing is required because property is destroyed — though excessive or unnecessary destruction may independently violate the Fourth Amendment.", "title": "United States v. Ramirez", "varies_by_point": "false"}}
```

### lake record — United States v. Ramirez

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Ramirez",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Ramirez",
    "case_name_short": "Ramirez",
    "case_name_full": "United States v. Ramirez",
    "input_case_name": "United States v. Ramirez",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1998-03-04",
    "year": 1998,
    "docket": "96-1469",
    "cluster_id": 118180,
    "lead_opinion_id": 118180,
    "sibling_ids": [
      118180
    ],
    "absolute_url": "/opinion/118180/united-states-v-ramirez/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "523 U.S. 65",
      "volume": "523",
      "reporter": "U.S.",
      "page": "65",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "118 S. Ct. 992",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "992",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "140 L. Ed. 2d 191",
        "volume": "140",
        "reporter": "L. Ed. 2d",
        "page": "191",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1998 U.S. LEXIS 1600",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "1600",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "523 U.S. 65",
        "volume": "523",
        "reporter": "U.S.",
        "page": "65",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "118 S. Ct. 992",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "992",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "140 L. Ed. 2d 191",
        "volume": "140",
        "reporter": "L. Ed. 2d",
        "page": "191",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1998 U.S. LEXIS 1600",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "1600",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "523 U.S. 65",
    "official_selection": {
      "court_class": "scotus",
      "selected": "523 U.S. 65",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-68",
      "page": null,
      "quote": "--- # United States v. Ramirez *523 U.S. 65 (1998)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers had a warrant connected to the search for Alan Shelby, a violent prison escapee reported to be hiding in Hernan Ramirez's home and to have access to a supply of weapons. Executing the warrant early one morning, the police announced their presence and broke a single window in Ramirez's garage \u2014 pointing a weapon through it to discourage anyone from rushing to the guns. Believing a burglary was underway, Ramirez fired a shot, then surrendered. Shelby was not found, but officers recovered firearms, and Ramirez (a felon) was charged with being a felon in possession. The District Court and Ninth Circuit suppressed the evidence, finding insufficient exigency to justify the property destruction. ## Issue Does the Fourth Amendment (or 18 U.S.C. \u00a7 3109) hold officers to a higher standard for a no-knock entry when the entry results in the destruction of property? ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-71",
      "page": null,
      "quote": "Under *Richards*, a no-knock entry is justified if police have a 'reasonable suspicion' that knocking and announcing would be dangerous, futile, or destructive to the purposes of the investigation. Whether such a 'reasonable suspicion' exists depends in no way on whether police must destroy property in order to enter.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-71b",
      "page": null,
      "quote": "Excessive or unnecessary destruction of property in the course of a search may violate the Fourth Amendment, even though the entry itself is lawful and the fruits of the search are not subject to suppression.",
      "star_marker": "71",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 9732,
      "fragment": "#:~:text=Excessive%20or%20unnecessary%20destruction%20of",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1998-03-04",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Ramirez",
    "varies_by_point": false,
    "scope_note": "Controlling: a no-knock entry that damages property is judged by the same Richards reasonable-suspicion standard \u2014 no heightened showing is required because property is destroyed \u2014 though excessive or unnecessary destruction may independently violate the Fourth Amendment.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Southerland, Vince",
          "cluster_id": 186774,
          "cite": [
            "373 U.S. App. D.C. 305",
            "466 F.3d 1083",
            "2006 U.S. App. LEXIS 26978",
            "2006 WL 3069122"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Julio Cortez-Rocha",
          "cluster_id": 788904,
          "cite": [
            "394 F.3d 1115",
            "2005 U.S. App. LEXIS 1014",
            "2005 WL 107088"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Julio Cortez-Rocha",
          "cluster_id": 787787,
          "cite": [
            "383 F.3d 1093",
            "2004 U.S. App. LEXIS 19583",
            "2004 WL 2093451"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Deandre J. Scroggins",
          "cluster_id": 785508,
          "cite": [
            "361 F.3d 1075",
            "2004 WL 574495"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Robert Junior Wardrick",
          "cluster_id": 784262,
          "cite": [
            "350 F.3d 446",
            "2003 U.S. App. LEXIS 23669",
            "2003 WL 22789492"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane1_negative"
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
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hudson v. Michigan",
          "cluster_id": 145646,
          "cite": [
            "165 L. Ed. 2d 56",
            "126 S. Ct. 2159",
            "547 U.S. 586",
            "2006 U.S. LEXIS 4677"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
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
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "The PEOPLE of the State of Colorado v. Joshua M. AARNESS",
          "cluster_id": 10014025,
          "cite": [
            "150 P.3d 1271",
            "2006 WL 2998823"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Louis Lalonde v. County of Riverside, Robert Moquin, and Jason Horton, Opinion",
          "cluster_id": 767803,
          "cite": [
            "204 F.3d 947",
            "2000 Daily Journal DAR 2031",
            "2000 Cal. Daily Op. Serv. 1433",
            "2000 U.S. App. LEXIS 2778",
            "2000 WL 217552"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Banks",
          "cluster_id": 131146,
          "cite": [
            "157 L. Ed. 2d 343",
            "124 S. Ct. 521",
            "540 U.S. 31",
            "2003 U.S. LEXIS 8966"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James H. Spikes (96-3899) Marilyn Smith (96-3660)",
          "cluster_id": 758684,
          "cite": [
            "158 F.3d 913",
            "49 Fed. R. Serv. 1564",
            "1998 U.S. App. LEXIS 21399",
            "1998 WL 551966"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
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
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
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
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Aarness",
          "cluster_id": 2632419,
          "cite": [
            "150 P.3d 1271",
            "2006 WL 2998823"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
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
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McDonough",
          "cluster_id": 2483242,
          "cite": [
            "940 N.E.2d 1100",
            "239 Ill. 2d 260",
            "346 Ill. Dec. 496",
            "2010 Ill. LEXIS 1557"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Larry J. Leaf, Individually and as Personal Representative of the Estate of John P. Leaf, Deceased, Martha A. Leaf, John P. Leaf v. Ronald Shelnutt",
          "cluster_id": 789551,
          "cite": [
            "400 F.3d 1070",
            "2005 U.S. App. LEXIS 4513",
            "2005 WL 628217"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hardin",
          "cluster_id": 1427400,
          "cite": [
            "539 F.3d 404",
            "2008 U.S. App. LEXIS 18135",
            "2008 WL 3891265"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jones",
          "cluster_id": 2181223,
          "cite": [
            "846 A.2d 569",
            "179 N.J. 377",
            "2004 N.J. LEXIS 437"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ward",
          "cluster_id": 1614689,
          "cite": [
            "2000 WI 3",
            "604 N.W.2d 517",
            "231 Wis. 2d 723",
            "2000 Wisc. LEXIS 3"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cybernet, LLC v. Jonathan David",
          "cluster_id": 4738712,
          "cite": [
            "954 F.3d 162"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Basham",
          "cluster_id": 161661,
          "cite": [
            "268 F.3d 1199",
            "2001 U.S. App. LEXIS 22854",
            "2001 WL 1262098"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Stevens",
          "cluster_id": 1693561,
          "cite": [
            "597 N.W.2d 53",
            "460 Mich. 626"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Bynum",
          "cluster_id": 785581,
          "cite": [
            "362 F.3d 574",
            "2004 U.S. App. LEXIS 5703",
            "2004 WL 595136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKay",
          "cluster_id": 2600831,
          "cite": [
            "41 P.3d 59",
            "117 Cal. Rptr. 2d 236",
            "27 Cal. 4th 601",
            "2002 Cal. Daily Op. Serv. 2036",
            "2002 Daily Journal DAR 2485",
            "2002 Cal. LEXIS 624"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rudolph Keszthelyi",
          "cluster_id": 779578,
          "cite": [
            "308 F.3d 557",
            "2002 U.S. App. LEXIS 21631",
            "2002 F. App'x 0362P"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Steven Guest Denise B. Kelley Nelda Sturgill Deborah Cummings Randy Bowling Richard E. Kramer, on Behalf of Themselves and All Others Similarly Situated v. Simon L. Leis, Jr. Hamilton County Sheriff's Department Hamilton County Regional Electronic Computer Intelligence Task Force Dale Menkhaus James Nerlinger David L. Ausdenmoore, Michael O'Brien Noah O'Brien Anthony Blackmon Randall Dodds Darrell McAvoy Brian Kaeppner v. Simon L. Leis, Jr. Hamilton County Sheriff's Department Hamilton County Regional Electronic Computer Intelligence Task Force Dale Menkhaus James Nerlinger David L. Ausdenmoore",
          "cluster_id": 773807,
          "cite": [
            "255 F.3d 325",
            "2001 U.S. App. LEXIS 14597"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark Brown v. Battle Creek Police Dep't",
          "cluster_id": 4331219,
          "cite": [
            "844 F.3d 556",
            "2016 FED App. 0293P",
            "2016 U.S. App. LEXIS 22447",
            "2016 WL 7336612"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ramirez:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118180) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 178,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 5,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 178,
        "triage_read": 6,
        "triage_snippet_classified": 172
      },
      "lane2_top_cited": {
        "query": "cites:(118180)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NCZzPTI2Nzg2NzUmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118180%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118180)",
        "reviewed": 8,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 8,
        "triage_read": 0,
        "triage_snippet_classified": 8
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118180)",
    "indexed_citing_opinions": 242,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118180,
        "count": 242,
        "count_source": "search"
      }
    ],
    "citation_count": 410,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-ramirez.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY2NjAxMzEmcz00NzI4ODE4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118180%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118180,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118180,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118180,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118180,
        "cited_id": 107718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118180,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118180,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118180,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118180,
        "cited_id": 118103,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118180,
        "cited_id": 723873,
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
    "date_created": "2026-07-06T02:21:27Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:21:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:21:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:24:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:21:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Ramirez

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b191-7">
  Chief Justice Rehnquist
 </author>
<p id="AZ">
  delivered the opinion of the Court.
 </p>
<p id="b191-8">
  In
  <em>
   Richards
  </em>
  v.
  <em>
   Wisconsin,
  </em>
  <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/#394" aria-description="Citation for case: Richards v. Wisconsin">520 U. S. 385, 394</a></span> (1997), we held that so-called “no-knoek” entries are justified when police officers have a “reasonable suspicion” that knocking and announcing their presence before entering would “be dangerous or futile, or .. . inhibit the effective investigation of
  <span citation-index="1" class="star-pagination" label="68"> 
   *68
   </span>
  the crime.” In this ease, we must decide whether the Fourth Amendment holds officers to a higher standard than this when a “no-knoek” entry results in the destruction of property. We hold that it does not.
 </p>
<p id="b192-5">
  Alan Shelby was a prisoner serving concurrent state and federal sentences in the Oregon state prison system. On November 1,1994, the Tillamook County Sheriff’s Office took temporary custody of Shelby, expecting to transport him to the Tillamook County Courthouse, where he was scheduled to testify. On the way to the courthouse, Shelby slipped his handcuffs, knocked over a deputy sheriff, and escaped from custody.
 </p>
<p id="b192-6">
  It was not the first time Shelby had attempted escape. In 1991 he struck an officer, kicked out a jail door, assaulted a woman, stole her vehicle, and used it to ram a police vehicle. Another time he attempted escape by using a rope made from torn bedsheets. He was reported to have made threats to kill witnesses and police officers, to have tortured people with a hammer, and to have said that he would “ ‘not do federal time.’” App. to Pet. for Cert. 38a. It was also thought that Shelby had had access to large supplies of weapons.
 </p>
<p id="b192-7">
  Shortly after learning of Shelby’s escape, the authorities sent out a press release, seeking information that would lead to his recapture. On November 3, a reliable confidential informant told Bureau of Alcohol, Tobacco, and Firearms Agent George Kim that on the previous day he had seen a person he believed to be Shelby at respondent Hernán Ramirez’s home in Boring, Oregon. Kim and the informant then drove to an area near respondent’s home, from where Kim observed a man working outside who resembled Shelby.
 </p>
<p id="b192-8">
  Based on this information, a Deputy United States Marshal sought and received a “no-knock” warrant granting permission to enter and search Ramirez’s home. Around this time, the confidential informant also told authorities that respondent might have a stash of guns and drugs hidden in
  <span citation-index="1" class="star-pagination" label="69"> 
   *69
   </span>
  his garage. In the early morning of November 5, approximately 45 officers gathered to execute the warrant. The officers set up a portable loudspeaker system and began announcing that they had a search warrant. Simultaneously, they broke a single window in the garage and pointed a gun through the opening, hoping thereby to dissuade any of the occupants from rushing to the weapons the officers believed might be in the garage.
 </p>
<p id="b193-5">
  Respondent and his family were asleep inside the house at the time this activity began. Awakened by the noise, respondent believed that they were being burglarized. He ran to his utility closet, grabbed a pistol, and fired it into the ceiling of his garage. The officers fired back and shouted “police.” At that point respondent realized that it was law enforcement officers who were trying to enter his home. He ran to the living room, threw his pistol away, and threw himself onto the floor. Shortly thereafter, he, his wife, and their child left the house and were taken into police custody. Respondent waived his
  <em>
   Miranda
  </em>
  rights, and then admitted that he had fired the weapon, that he owned both that gun and another gun that was inside the house, and that he was a convicted felon. Officers soon obtained another search warrant, which they used to return to the house and retrieve the two guns. Shelby was not found.
 </p>
<p id="b193-6">
  Respondent was subsequently indicted for being a felon in possession of firearms. <span class="citation no-link">18 U. S. C. § 922</span>(g)(1). The District Court granted his motion to suppress evidence regarding his possession of the weapons, ruling that the police officers had violated both the Fourth Amendment and <span class="citation no-link">18 U. S. C. § 8109</span> because there were “insufficient exigent circumstances” to justify the police officers’ destruction of property in their execution of the warrant. App. to Pet. for Cert. 34a.
 </p>
<p id="b193-7">
  The Court of Appeals for the Ninth Circuit affirmed. <span class="citation" data-id="9843168"><a href="/opinion/723873/united-states-of-america-plaintiff-appellant-v-hernan-ramirez/" aria-description="Citation for case: UNITED STATES of America, Plaintiff-Appellant, v. Hernan...">91 F. 3d 1297</a></span> (1996). Applying Circuit precedent, that court concluded that while a “mild exigency” is sufficient to justify a no-knoek entry that can be accomplished without the de
  <span citation-index="1" class="star-pagination" label="70"> 
   *70
   </span>
  struction of property, “ 'more specific inferences of exigency are necessary’ ” when property is destroyed.
  <span class="citation" data-id="9843168"><a href="/opinion/723873/united-states-of-america-plaintiff-appellant-v-hernan-ramirez/#1301" aria-description="Citation for case: UNITED STATES of America, Plaintiff-Appellant, v. Hernan..."><em>
   Id.,
  </em>
  at 1301</a></span>. It held that this heightened standard had not been met on the facts of this case. We granted certiorari and now reverse. <span class="citation multiple-matches"><a href="/c/U.%20S./521/1103/">521 U. S. 1103</a></span> (1997).
 </p>
<p id="b194-5">
  In two recent eases we have considered whether and to what extent “no-knock” entries implicate the protections of the Fourth Amendment. In
  <em>
   Wilson
  </em>
  v.
  <em>
   Arkansas,
  </em>
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927</a></span> (1995), we reviewed the Arkansas Supreme Court’s holding that the common-law requirement that police officers knock and announce their presence before entering played no role in Fourth Amendment analysis. We rejected that conclusion, and held instead that “in some circumstances an officer’s unannounced entry into a home might be unreasonable under the Fourth Amendment.”
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#934" aria-description="Citation for case: Wilson v. Arkansas"><em>
   Id.,
  </em>
  at 934</a></span>. We were careful to note, however, that there was no rigid rule requiring announcement in all instances, and left “to the lower courts the task of determining the circumstances under which an unannounced entry is reasonable under the Fourth Amendment.”
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#934" aria-description="Citation for case: Wilson v. Arkansas"><em>
   Id.,
  </em>
  at 934, 936</a></span>.
 </p>
<p id="b194-6">
  In
  <em>
   Richards
  </em>
  v.
  <em>
   Wisconsin,
  </em>
  <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">520 U. S. 385</a></span> (1997),
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  the Wisconsin Supreme Court held that police officers executing search warrants in felony drug investigations were never required to knock and announce their presence. We concluded that this blanket rule was overly broad and held instead that “[i]n order to justify a 'no-knock’ entry, the police must have a reasonable suspicion that knocking and announcing them presence, under the particular circumstances, would be dangerous or futile, or that it would inhibit the effective investigation of the crime by, for example, allowing the destruction of evidence.”
  <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/#394" aria-description="Citation for case: Richards v. Wisconsin"><em>
   Id.,
  </em>
  at 394</a></span>.
 </p>
<p id="b194-7">
  Neither of these cases explicitly addressed the question whether the lawfulness of a no-knock entry depends on whether property is damaged in the course of the entry. It
  <span citation-index="1" class="star-pagination" label="71"> 
   *71
   </span>
  is obvious from their holdings, however, that it does not. Under
  <em>
   <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">Richards</a></span>,
  </em>
  a no-knoek entry is justified if police have a “reasonable suspicion” that knocking and announcing would be dangerous, futile, or destructive to the purposes of the investigation. Whether such a “reasonable suspicion” exists depends in no way on whether police must destroy property in order to enter.
 </p>
<p id="A2r">
  This is not to say that the Fourth Amendment speaks not at all to the manner of executing a search warrant. The general touchstone of reasonableness which governs Fourth Amendment analysis, see
  <em>
   Pennsylvania
  </em>
  v.
  <em>
   Mimms,
  </em>
  <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#108" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 108-109</a></span> (1977)
  <em>
   (per curiam),
  </em>
  governs the method of execution of the warrant. Excessive or unnecessary destruction of property in the course of a search may violate the Fourth Amendment, even though the entry itself is lawful and the fruits of the search are not subject to suppression.
 </p>
<p id="b195-6">
  Applying these principles to the facts at hand, we conclude that no Fourth Amendment violation occurred. A reliable confidential informant had notified the police that Alan Shelby might be inside respondent’s home, and an officer had confirmed this possibility. Shelby was a prison escapee with a violent past who reportedly had access to a large supply of weapons. He had vowed that he would “‘not do federal time.’” The police certainly had a “reasonable suspicion” that knocking and announcing their presence might be dangerous to themselves or to others.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
</p>
<p id="b195-7">
  As for the manner in which the entry was accomplished, the police here broke a single window in respondent’s garage. They did so because they wished to discourage Shelby, or any other occupant of the house, from rushing to the weapons that the informant had told them respondent might have
  <span citation-index="1" class="star-pagination" label="72"> 
   *72
   </span>
  kept there. Their conduct was clearly reasonable and we conclude that there was no
  <em>
   Fourth
  </em>
  Amendment violation.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b196-5">
  Respondent also argues, however, that suppression is appropriate because the officers executing the warrant violated <span class="citation no-link">18 U. S. C. §3109</span>. This statutory argument fares no better. Section 3109 provides:
 </p>
<blockquote id="b196-6">
  "The officer may break open any outer or inner door or window of a house, or any part of a house, or anything therein, to execute a search warrant, if, after notice of his authority and purpose, he is refused admittance or when necessary to liberate himself or a person aiding him in the execution of the warrant.”
 </blockquote>
<p id="b196-7">
  Respondent contends that the statute specifies the only circumstances under which an officer may damage property in executing a search warrant, and that it therefore forbids all other property-damaging entries.
 </p>
<p id="b196-8">
  But by its terms § 3109 prohibits nothing. It merely authorizes officers to damage property in certain instances. Even accepting,
  <em>
   arguendo,
  </em>
  that the statute implicitly forbids some of what it does not expressly permit, it is of no help to respondent. In
  <em>
   Miller
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#313" aria-description="Citation for case: Miller v. United States">357 U. S. 301, 313</a></span> (1958), we noted that §3109’s "requirement of prior notice . .. before forcing entry ... codif[ied] a tradition embedded in Anglo-American law.” We repeated this point in
  <em>
   Sabbath
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="107718"><a href="/opinion/107718/sabbath-v-united-states/#591" aria-description="Citation for case: Sabbath v. United States">391 U. S. 585, 591, n. 8</a></span> (1968) (referring to §3109 as “codification” of the common law). In neither of
  <span citation-index="1" class="star-pagination" label="73"> 
   *73
   </span>
  these cases, however, did we expressly hold that §3109 also codified the exceptions to the common-law requirement of notice before entry. In
  <em>
   <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">Miller</a></span>
  </em>
  the Government made “no claim ... of the existence of circumstances excusing compliance” and the question was accordingly not before us. <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#309" aria-description="Citation for case: Miller v. United States">357 U. S., at 309</a></span>. In
  <em>
   <span class="citation" data-id="107718"><a href="/opinion/107718/sabbath-v-united-states/" aria-description="Citation for case: Sabbath v. United States">Sabbath</a></span>
  </em>
  the Government did make such a claim, but because the record did “not reveal any substantial basis for the failure of the agents ... to announce their authority” we did not decide the question. We did note, however, that “[e]xceptions to any possible constitutional rule relating to announcement and entry have been recognized . . . and there is little'reason why those limited exceptions might not also apply to § 3109, since they existed at common law, of which the statute is a codification.” <span class="citation" data-id="107718"><a href="/opinion/107718/sabbath-v-united-states/#591" aria-description="Citation for case: Sabbath v. United States">391 U. S., at 591, n. 8</a></span>.
 </p>
<p id="b197-5">
  In this case the question is squarely presented. We remove whatever doubt may remain on the subject and hold that §3109 codifies the exceptions to the common-law announcement requirement. If § 3109 codifies the common law in this area, and the common law in turn informs the Fourth Amendment, our decisions in
  <em>
   <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>
  </em>
  and
  <em>
   <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">Richards</a></span>
  </em>
  serve as guideposts in construing the statute. In
  <em>
   Wilson
  </em>
  v.
  <em>
   Arkansas,
  </em>
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927</a></span> (1995), we concluded that the common-law principle of announcement is “an element of the reasonableness inquiry under the Fourth Amendment,” but noted that the principle “was never stated as an inflexible rule requiring announcement under all circumstances.”
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#934" aria-description="Citation for case: Wilson v. Arkansas"><em>
   Id.,
  </em>
  at 934</a></span>. In
  <em>
   Richards
  </em>
  v.
  <em>
   Wisconsin,
  </em>
  <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">520 U. S. 385</a></span> (1997), we articulated the test used to determine whether exigent circumstances justify a particular no-knock entry.
  <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/#394" aria-description="Citation for case: Richards v. Wisconsin"><em>
   Id.,
  </em>
  at 394</a></span>. We therefore hold that § 3109 includes an exigent circumstances exception and that the exception’s applicability in a given instance is measured by the same standard we articulated in
  <em>
   <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">Richards</a></span>.
  </em>
  The police met that standard here and § 3109 was therefore not violated.
 </p>
<p id="b198-4">
<span citation-index="1" class="star-pagination" label="74"> 
   *74
   </span>
  We accordingly reverse the judgment of the Court of Appeals and remand this case for further proceedings consistent with this opinion.
 </p>
<p id="b198-5">
<em>
   It is so ordered.
  </em>
</p>



<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b194-8">
   It should be noted that our opinion in
   <em>
    <span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">Richards</a></span>
   </em>
   came down after the Court of Appeals issued its opinion in this case.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b195-8">
   It is of no consequence that Shelby was not found. “[I]n determining the lawfulness of entry and the existence of probable cause we may concern ourselves only with what the officers had reason to believe
   <em>
    at the time of their entry.” Ker
   </em>
   v.
   <em>
    California,
   </em>
   <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#40" aria-description="Citation for case: Ker v. California">374 U. S. 23, 40-41, n. 12</a></span> (1963) (opinion of Clark, J.) (emphasis in original).
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b196-9">
   After concluding that the Fourth Amendment had been violated in this case, the Ninth Circuit farther concluded that the guns should be excluded from evidence. Because we conclude that there was no Fourth Amendment violation, we need not decide whether, for example, there was sufficient causal relationship between the breaking of the window and the discovery of the guns to warrant suppression of the evidence. Cf.
   <em>
    Nix
   </em>
   v.
   <em>
    Williams,
   </em>
   <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">467 U. S. 431</a></span> (1984);
   <em>
    Wong Sun
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963).
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/United States v. Reddick.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Reddick
type: case
citation: "900 F.3d 636 (2018)"
parallel_cite: ""
neutral_cite: ""
court: 5th Cir.
court_level: coa
circuit: ca5
year: 2018
date_decided: 2018-08-17
docket: 17-41116
authority_weight: "Binding in-circuit — 5th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4527853/united-states-v-henry-reddick/"
  cluster_id: 4527853
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Reddick
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Private and Foreign Searches]]"
    role: "Key — hash-match split (5th Cir.)"
related:
  - "[[Fourth Amendment Framework]]"
  - "[[United States v. Jacobsen]]"
  - "[[Carpenter v. United States]]"
  - "[[Riley v. California]]"
tags:
  - case
  - fourth-amendment
  - private-search-doctrine
  - hash-value
  - child-pornography
  - digital-privacy
  - fifth-circuit
holding: "Under the private-search doctrine, the government does not conduct a Fourth Amendment search when it merely receives and reviews the results of a search already performed by a private party, so where a private company hash-matched Reddick's uploaded files to known child-pornography images and reported them, the officer's warrantless viewing of the flagged images exposed nothing beyond what the private search had already revealed and did not violate the Fourth Amendment."
aliases:
  - United States v. Reddick
  - "United States v. Reddick (5th Cir. 2018)"
---

# United States v. Reddick

*900 F.3d 636 (5th Cir. 2018)* (No. 17-41116) · U.S. Court of Appeals for the Fifth Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4527853 → lead opinion 4305106 (Ho, J.; 900 F.3d 636, decided 2018-08-17); Rule quote string-matched to the CL opinion text 2026-07-07 (reporter page-label *637). S9 promotes. -->

## Background
Henry Reddick uploaded files to Microsoft's cloud-storage service. Microsoft's automated systems computed the "hash values" of those files — short, distinctive alphanumeric identifiers derived from a file's contents — and compared them against a database of hash values of known child-pornography images. When the values matched, Microsoft reported the files to the National Center for Missing and Exploited Children, which forwarded the report to law enforcement. Detective Ilse then opened and viewed the flagged image files without first obtaining a warrant, confirmed they were child pornography, and that evidence supported the ensuing prosecution. Reddick moved to suppress, arguing the warrantless viewing was an unlawful search; the district court denied the motion, and he appealed.

## Issue
Whether a law-enforcement officer conducts a Fourth Amendment search when, without a warrant, he opens and views digital files whose hash values a private party has already matched against known child-pornography images and reported to authorities.

## Rule
The Fourth Amendment restrains only government action, so when a private party has already searched an item the government does not conduct a new search by examining what that private search already exposed — it acquires no information as to which the owner's expectation of privacy remained intact. Applying that private-search doctrine, the panel held: "Under the private search doctrine, the Fourth Amendment is not implicated where the government does not conduct the search itself, but only receives and utilizes information uncovered by a search conducted by a private party." — 900 F.3d at 637. ^pin-637

## Application
Microsoft's automated hash-value comparison had already identified Reddick's files as matching known child pornography and had frustrated whatever expectation of privacy he retained in them before any officer became involved — a hash match identifies a file with near-certainty. When Detective Ilse opened the files, he learned nothing that the private hash-match had not already established, so his viewing worked no additional intrusion on any privacy interest that survived, and the Fourth Amendment was not implicated. The court therefore affirmed on this broader private-search ground rather than the narrower rationale the district court had invoked.

## Conclusion
**Affirmed.** James C. Ho, Circuit Judge, wrote for the panel.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Reddick* applies the *[[United States v. Jacobsen|Jacobsen]]* private-search doctrine to automated hash-value matching: because a private company's hash comparison exposes a file's status before any officer looks, the officer's confirmatory viewing adds nothing the Fourth Amendment protects. Note the live cross-circuit tension over how far the doctrine reaches when no human at the private company ever viewed the specific file — the Ninth Circuit has diverged on that point — so teach *Reddick* as the Fifth Circuit's confirmatory-viewing rule, not a settled national standard.

## Appears on
- [[Private and Foreign Searches]] — *Key — hash-match split (5th Cir.)*

## Sources
- [*United States v. Reddick*, 900 F.3d 636 (5th Cir. 2018)](https://www.courtlistener.com/opinion/4527853/united-states-v-henry-reddick/) — pinpoint: 637 (private-search-doctrine holding; Ho, J.; the CL opinion text carries the reporter page-label *637). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "df9b6788f3c45275", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "900 F.3d 636 (2018)", "court": "5th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Reddick", "year": "2018"}}
{"assertion_id": "163433f91c32147f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Under the private-search doctrine, the government does not conduct a Fourth Amendment search when it merely receives and reviews the results of a search already performed by a private party, so where a private company hash-matched Reddick's uploaded files to known child-pornography images and reported them, the officer's warrantless viewing of the flagged images exposed nothing beyond what the private search had already revealed and did not violate the Fourth Amendment.", "title": "United States v. Reddick"}}
{"assertion_id": "3651a26812f23e8e", "dimension": "support", "kind": "home_role", "locator": {"home": "Private and Foreign Searches"}, "payload": {"home": "Private and Foreign Searches", "role": "Key — hash-match split (5th Cir.)", "title": "United States v. Reddick"}}
{"assertion_id": "504c26d90122de76", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Reddick", "varies_by_point": "false"}}
{"assertion_id": "f33d9865fedf975c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 5th Cir.", "title": "United States v. Reddick"}}
```

### lake record — United States v. Reddick

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Reddick",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Henry Reddick",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee v. Henry Franklin REDDICK, Defendant-Appellant",
    "input_case_name": "United States v. Reddick",
    "court": "5th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca5",
    "state": null,
    "date_decided": "2018-08-17",
    "year": 2018,
    "docket": "17-41116",
    "cluster_id": 4527853,
    "lead_opinion_id": 4305106,
    "sibling_ids": [],
    "absolute_url": "/opinion/4527853/united-states-v-henry-reddick/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "900 F.3d 636",
      "volume": "900",
      "reporter": "F.3d",
      "page": "636",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "900 F.3d 636",
        "volume": "900",
        "reporter": "F.3d",
        "page": "636",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "900 F.3d 636",
    "official_selection": {
      "court_class": "coa",
      "selected": "900 F.3d 636",
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
    "date_created": "2026-07-07T01:40:32Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:40:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:40:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:40:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:40:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-reddick--4527853",
      "to_record_id": "United States v. Reddick",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Reddick

```
     Case: 17-41116    Document: 00514605839        Page: 1   Date Filed: 08/17/2018




        IN THE UNITED STATES COURT OF APPEALS
                 FOR THE FIFTH CIRCUIT
                                                                     United States Court of Appeals
                                                                              Fifth Circuit


                                    No. 17-41116
                                                                            FILED
                                                                      August 17, 2018
                                                                       Lyle W. Cayce
UNITED STATES OF AMERICA,                                                   Clerk

             Plaintiff - Appellee

v.

HENRY FRANKLIN REDDICK,

             Defendant - Appellant




                Appeal from the United States District Court
                     for the Southern District of Texas


Before KING, SOUTHWICK, and HO, Circuit Judges.
JAMES C. HO, Circuit Judge:
      Private businesses and police investigators rely regularly on “hash
values” to fight the online distribution of child pornography. Hash values are
short, distinctive identifiers that enable computer users to quickly compare the
contents of one file to another. They allow investigators to identify suspect
material from enormous masses of online data, through the use of specialized
software programs—and to do so rapidly and automatically, without the need
for human searchers.
      Hash values have thus become a powerful tool for combating the online
distribution of unlawful aberrant content.         The question in this appeal is
whether and when the use of hash values by law enforcement is consistent with
    Case: 17-41116    Document: 00514605839     Page: 2   Date Filed: 08/17/2018



                                 No. 17-41116
the Fourth Amendment. For the Fourth Amendment concerns not efficiency,
but the liberty of the people “to be secure in their persons, houses, papers, and
effects, against unreasonable searches and seizures.” There is no precedent in
our circuit concerning the validity of these investigative tools under the Fourth
Amendment, and to our knowledge no other circuit has confronted the precise
question before us.   This case therefore presents an opportunity to apply
established Fourth Amendment principles in this new context.
      One touchstone of our Fourth Amendment jurisprudence is that the
Constitution secures the right of the people against unreasonable searches and
seizures conducted by the government—not searches and seizures conducted
by private parties. Under the private search doctrine, the Fourth Amendment
is not implicated where the government does not conduct the search itself, but
only receives and utilizes information uncovered by a search conducted by a
private party.
      The private search doctrine decides this case.        A private company
determined that the hash values of files uploaded by Mr. Reddick corresponded
to the hash values of known child pornography images. The company then
passed this information on to law enforcement. This qualifies as a “private
search” for Fourth Amendment purposes. And the government’s subsequent
law enforcement actions in reviewing the images did not effect an intrusion on
Mr. Reddick’s privacy that he did not already experience as a result of the
private search. Accordingly, we affirm the judgment of the district court.
                                       I.
      In technical terms, a hash value is “an algorithmic calculation that yields
an alphanumeric value for a file.” United States v. Stevenson, 727 F.3d 826,
828 (8th Cir. 2013). More simply, a hash value is a string of characters
obtained by processing the contents of a given computer file and assigning a
sequence of numbers and letters that correspond to the file’s contents. In the
                                       2
    Case: 17-41116    Document: 00514605839     Page: 3   Date Filed: 08/17/2018



                                 No. 17-41116
words of one commentator, “[t]he concept behind hashing is quite elegant: take
a large amount of data, such as a file or all the bits on a hard drive, and use a
complex mathematical algorithm to generate a relatively compact numerical
identifier (the hash value) unique to that data.” Richard P. Salgado, Fourth
Amendment Search and the Power of the Hash, 119 Harv. L. Rev. F. 38, 38
(2005).
      Hash values are regularly used to compare the contents of two files
against each other.    “If two nonidentical files are inputted into the hash
program, the computer will output different results. If the two identical files
are inputted, however, the hash function will generate identical output.” Orin
S. Kerr, Searches and Seizures in a Digital World, 119 Harv. L. Rev. 531, 541
(2005). Hash values have been used to fight child pornography distribution,
by comparing the hash values of suspect files against a list of the hash values
of known child pornography images currently in circulation. This process
allows potential child pornography images to be identified rapidly, without the
need to involve human investigators at every stage.
                                       II.
      Henry Reddick uploaded digital image files to Microsoft SkyDrive, a
cloud hosting service.     SkyDrive uses a program called PhotoDNA to
automatically scan the hash values of user-uploaded files and compare them
against the hash values of known images of child pornography.             When
PhotoDNA detects a match between the hash value of a user-uploaded file and
a known child pornography hash value, it creates a “CyberTip” and sends the
file—along with the uploader’s IP address information—to the National Center
for Missing and Exploited Children (NCMEC).
      In early 2015, Microsoft sent CyberTips to NCMEC based on the hash
values of files that Reddick had uploaded to SkyDrive. Based on location data
derived from the IP address information accompanying the files, NCMEC
                                       3
    Case: 17-41116      Document: 00514605839     Page: 4    Date Filed: 08/17/2018



                                  No. 17-41116
subsequently forwarded the CyberTips to the Corpus Christi Police
Department.     Upon receiving the CyberTips, police detective Michael Ilse
opened each of the suspect files and confirmed that each contained child
pornography. Shortly thereafter, Detective Ilse applied for and received a
warrant to search Reddick’s home and seize his computer and related
materials. This search uncovered additional evidence of child pornography in
Reddick’s possession.
      Reddick was indicted for possession of child pornography in violation of
18 U.S.C. § 2252(a)(2) and (b)(1). Following his indictment, Reddick initially
pled not guilty and moved to suppress all the evidence of child pornography.
He alleged that Detective Ilse’s warrantless opening of the files associated with
the CyberTips was an unlawful search. He further claimed that any evidence
of child pornography found in his home should be suppressed under the
exclusionary rule, since the initial review of the suspect files was improper.
      The district court denied his motion. Reddick subsequently pled guilty,
while retaining the right to appeal the denial of his suppression motion. In
denying Reddick’s motion, the district court “assume[d] without deciding that
Officer Ilse’s viewing of the file images . . . invaded a constitutional expectation
of privacy, exceeded the scope of Microsoft Skydrive’s hash value search, and
did not fall into any exception to the warrant requirement.”            The court
nevertheless concluded that “the evidence here support[ed] the good faith
exception to the exclusionary rule.”         Accordingly, the court found no
justification to suppress the evidence of child pornography found in Reddick’s
home.
      As a general rule, “[w]e may affirm the district court’s ruling on a motion
to suppress ‘based on any rationale supported by the record.’” United States v.
Wise, 877 F.3d 209, 215 (5th Cir. 2017) (citation omitted). Consistent with this
rule, we affirm the denial of the motion to suppress on a ground broader than
                                         4
     Case: 17-41116       Document: 00514605839          Page: 5     Date Filed: 08/17/2018



                                       No. 17-41116
the one invoked by the district court—namely, that under the private search
doctrine, Officer Ilse’s viewing of the file images did not violate the Fourth
Amendment.
                                             III.
       Under the private search doctrine, “the critical inquiry under the Fourth
Amendment is whether the authorities obtained information with respect to
which the defendant’s expectation of privacy has not already been frustrated.”
United States v. Runyan, 275 F.3d 449, 461 (5th Cir. 2001). The question
presented here, then, is whether, by the time Detective Ilse viewed the suspect
image files, Reddick’s expectation of privacy in his computer files had already
been thwarted by a private third party. 1
       The Supreme Court’s decision in United States v. Jacobsen, 466 U.S. 109
(1984), guides our analysis.          In Jacobsen, employees of Federal Express
observed that one of its packages had been damaged in transit. They opened
the package and discovered a white powder.                  In response, the employees
contacted the Drug Enforcement Administration.                     DEA agents conducted
chemical field tests on the white powder and determined that the power was
cocaine. The government then used the test results to obtain a warrant and
arrest the package’s intended recipients, who subsequently challenged the
government’s actions as unconstitutional.
       The Court held that the agents’ actions did not violate the Fourth
Amendment. “Once frustration of the original expectation of privacy occurs,
the Fourth Amendment does not prohibit governmental use of the now-
nonprivate information.” Id. at 117. Any expectation of privacy the recipients


       1  We assume without deciding that Reddick indeed had a legitimate expectation of
privacy in the computer files at issue. As the district court correctly noted, “the most useful
evidence on which to make the determination” of whether Reddick’s expectation of privacy
was reasonable—“the end user agreement governing Reddick’s use of Microsoft Skydrive”—
is not in the record.
                                              5
    Case: 17-41116    Document: 00514605839     Page: 6   Date Filed: 08/17/2018



                                No. 17-41116
might have had in the package’s contents was abrogated when the Federal
Express employees opened and searched the package and discovered the white
powder. The government’s subsequent use of that information—its test to
discern the powder’s chemical composition—infringed no expectation of
privacy that had not already been infringed.
      So too here.   When Reddick uploaded files to SkyDrive, Microsoft’s
PhotoDNA program automatically reviewed the hash values of those files and
compared them against an existing database of known child pornography hash
values. In other words, his “package” (that is, his set of computer files) was
inspected and deemed suspicious by a private actor. Accordingly, whatever
expectation of privacy Reddick might have had in the hash values of his files
was frustrated by Microsoft’s private search.
      When Detective Ilse first received Reddick’s files, he already knew that
their hash values matched the hash values of child pornography images known
to NCMEC. As our court has previously noted, hash value comparison “allows
law enforcement to identify child pornography with almost absolute certainty,”
since hash values are “specific to the makeup of a particular image’s data.”
United States v. Larman, 547 F. App’x 475, 477 (5th Cir. 2013) (unpublished).
See also United States v. Sosa-Pintor, 2018 WL 3409657, at *1 (5th Cir. July
11, 2018) (unpublished) (describing a file’s hash value as its “unique digital
fingerprint”).
      Accordingly, when Detective Ilse opened the files, there was no
“significant expansion of the search that had been conducted previously by a
private party” sufficient to constitute “a separate search.” Walter v. United
States, 447 U.S. 649, 657 (1980). His visual review of the suspect images—a
step which merely dispelled any residual doubt about the contents of the files—
was akin to the government agents’ decision to conduct chemical tests on the
white powder in Jacobsen. “A chemical test that merely discloses whether or
                                      6
    Case: 17-41116   Document: 00514605839     Page: 7   Date Filed: 08/17/2018



                                No. 17-41116
not a particular substance is cocaine does not compromise any legitimate
interest in privacy.” 466 U.S. at 123. This principle readily applies here—
opening the file merely confirmed that the flagged file was indeed child
pornography, as suspected. As in Jacobsen, “the suspicious nature of the
material made it virtually certain that the substance tested was in fact
contraband.” Id. at 125.
      Significantly, there is no allegation that Detective Ilse conducted a
search of any of Mr. Reddick’s files other than those flagged as child
pornography.   Contrast a Tenth Circuit decision authored by then-Judge
Gorsuch. See United States v. Ackerman, 831 F.3d 1292 (10th Cir. 2016). In
Ackerman, an investigator conducted a search of an email and three
attachments whose hash values did not correspond to known child
pornography images. 831 F.3d at 1306. The Tenth Circuit reversed the district
court’s denial of a motion to suppress accordingly. Id. at 1309. Here, by
contrast, Detective Ilse reviewed only those files whose hash values
corresponded to the hash values of known child pornography images, as
ascertained by the PhotoDNA program. So his review did not sweep in any
“(presumptively) private correspondence that could have contained much
besides potential contraband.” Id. at 1307.
                                    ***
      The exact issues presented by this case may be novel. But the governing
constitutional principles set forth by the Supreme Court are not.          The
government effectively learned nothing from Detective Ilse’s viewing of the
files that it had not already learned from the private search. Accordingly,
under the private search doctrine, the government did not violate Reddick’s
Fourth Amendment rights. We affirm the judgment of the district court.




                                      7

```

---
