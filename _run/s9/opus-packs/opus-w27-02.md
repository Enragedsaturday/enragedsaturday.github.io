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

## GROUP: content/cases/Bivens v. Six Unknown Named Agents.md  (`case`, 5 assertions)

### content_page

```
---
title: "Bivens v. Six Unknown Named Agents"
type: case
citation: "403 U.S. 388 (1971)"
parallel_cite: "91 S. Ct. 1999; 29 L. Ed. 2d 619"
neutral_cite: 1971 U.S. LEXIS 23
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1971
date_decided: 1971-06-21
docket: 301
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1971-06-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Bivens v. Six Unknown Named Agents
  varies_by_point: false
  scope_note: "Core holding (4A damages against federal officers) remains good law; the Court has declined to extend Bivens to new contexts (Ziglar v. Abbasi (2017); Egbert v. Boule (2022))."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/"
  cluster_id: 108375
  opinion_id: 108375
  identity_checked: true
homes:
  - page: "[[Suing Federal Officers]]"
    role: "Key — Anchor"
related: ["[[Monroe v. Pape]]", "[[Hanlon v. Berger]]", "[[Harlow v. Fitzgerald]]"]
aliases: ["Bivens v. Six Unknown Named Agents of Federal Bureau of Narcotics", "Bivens v. Six Unknown Fed. Narcotics Agents"]
tags: ["case", "section-1983", "bivens", "federal-officer-liability", "fourth-amendment", "damages-remedy"]
holding: "A victim of a Fourth Amendment violation by federal officers acting under color of federal authority may recover money damages directly under the Constitution — the implied federal-officer analog to § 1983."
lake:
  record_id: Bivens v. Six Unknown Named Agents
  status: verified
  projected_at: 2026-07-06
---

# Bivens v. Six Unknown Named Agents

*403 U.S. 388 (1971)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Webster Bivens alleged that agents of the Federal Bureau of Narcotics, acting without a warrant or probable cause, entered his apartment, arrested him for narcotics offenses, manacled him in front of his wife and children, threatened to arrest the entire family, searched the apartment, and later subjected him to a visual strip search. He sued the agents for damages, claiming the entry, arrest, and search violated the Fourth Amendment. The lower courts dismissed because no federal statute authorized a damages suit against federal officers for such a violation.

## Issue
Whether a victim of an unconstitutional search and seizure by federal officers may sue them for money damages directly under the Fourth Amendment, even though no statute creates the cause of action.

## Rule
Yes. The Fourth Amendment itself supports a damages remedy against federal officers who violate it. Invoking *Bell v. Hood*, the Court reasoned that "where federally protected rights have been invaded, it has been the rule from the beginning that courts will be alert to adjust their remedies so as to grant the necessary relief." — 403 U.S. at 392. ^pin-392

"Having concluded that petitioner's complaint states a cause of action under the Fourth Amendment . . . we hold that petitioner is entitled to recover money damages for any injuries he has suffered as a result of the agents' violation of the Amendment." — *Id.* at 397. ^pin-397

## Application
Because federal agents had allegedly conducted a warrantless, suspicionless entry, arrest, and search, Bivens had stated a Fourth Amendment claim; the absence of a statute did not bar relief, since damages are the ordinary remedy for an invasion of personal liberty and the agents could not claim that their conduct, if unconstitutional, was authorized by any valid grant of federal authority. The Court [[Reading and Citing Cases#on-remand|remanded]] for further proceedings, including the agents' immunity defenses.

## Conclusion
Reversed and [[Reading and Citing Cases#on-remand|remanded]]. A damages action lies directly under the Fourth Amendment against federal officers who conduct an unconstitutional search and seizure — establishing the federal-officer counterpart to a § 1983 suit against state actors.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Bivens* remains the foundational federal-officer damages remedy and the analog to the state-actor remedy recognized in [[Monroe v. Pape]]; it was the vehicle for the *Bivens* claim in [[Hanlon v. Berger]], and federal officers sued under it raise the same qualified-immunity defense framed in [[Harlow v. Fitzgerald]]. The Court has not overruled *Bivens*, but in recent decades it has sharply **limited** the remedy by declining to extend it to new contexts (e.g., *[[Ziglar v. Abbasi]]* (2017); *[[Egbert v. Boule]]* (2022)) — the implied cause of action is essentially confined to contexts like the one in *Bivens* itself.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Anchor*

## Sources
- *Bivens v. Six Unknown Named Agents*, 403 U.S. 388 (1971) — https://www.courtlistener.com/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/ — pinpoints: 392, 397.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "06a92e2fd481fd36", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "403 U.S. 388 (1971)", "court": "U.S. Supreme Court", "neutral_cite": "1971 U.S. LEXIS 23", "official_citation_present": true, "parallel_cite": "91 S. Ct. 1999; 29 L. Ed. 2d 619", "title": "Bivens v. Six Unknown Named Agents", "year": "1971"}}
{"assertion_id": "1b110264148030ea", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A victim of a Fourth Amendment violation by federal officers acting under color of federal authority may recover money damages directly under the Constitution — the implied federal-officer analog to § 1983.", "title": "Bivens v. Six Unknown Named Agents"}}
{"assertion_id": "26586d8abd83582f", "dimension": "support", "kind": "home_role", "locator": {"home": "Suing Federal Officers"}, "payload": {"home": "Suing Federal Officers", "role": "Key — Anchor", "title": "Bivens v. Six Unknown Named Agents"}}
{"assertion_id": "418bdfc476e584fa", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Bivens v. Six Unknown Named Agents"}}
{"assertion_id": "5b6a3a2e3fd01a78", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1971-06-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Bivens v. Six Unknown Named Agents", "field_i_validity": "good_law", "scope_note": "Core holding (4A damages against federal officers) remains good law; the Court has declined to extend Bivens to new contexts (Ziglar v. Abbasi (2017); Egbert v. Boule (2022)).", "title": "Bivens v. Six Unknown Named Agents", "varies_by_point": "false"}}
```

### lake record — Bivens v. Six Unknown Named Agents

```json
{
  "schema_version": "s2.v1",
  "record_id": "Bivens v. Six Unknown Named Agents",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Bivens v. Six Unknown Named Agents of Federal Bureau of Narcotics",
    "case_name_short": "Bivens",
    "case_name_full": "Bivens v. Six Unknown Named Agents of Federal Bureau of Narcotics",
    "input_case_name": "Bivens v. Six Unknown Named Agents",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1971-06-21",
    "year": 1971,
    "docket": "301",
    "cluster_id": 108375,
    "lead_opinion_id": 108375,
    "sibling_ids": [
      108375,
      9883113,
      9883114,
      9883115,
      9883116,
      9883117
    ],
    "absolute_url": "/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "403 U.S. 388",
      "volume": "403",
      "reporter": "U.S.",
      "page": "388",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "91 S. Ct. 1999",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "1999",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "29 L. Ed. 2d 619",
        "volume": "29",
        "reporter": "L. Ed. 2d",
        "page": "619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1971 U.S. LEXIS 23",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "23",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "403 U.S. 388",
        "volume": "403",
        "reporter": "U.S.",
        "page": "388",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 S. Ct. 1999",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "1999",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "29 L. Ed. 2d 619",
        "volume": "29",
        "reporter": "L. Ed. 2d",
        "page": "619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1971 U.S. LEXIS 23",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "23",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "403 U.S. 388",
    "official_selection": {
      "court_class": "scotus",
      "selected": "403 U.S. 388",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-392",
      "page": null,
      "quote": "--- # Bivens v. Six Unknown Named Agents *403 U.S. 388 (1971)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Webster Bivens alleged that agents of the Federal Bureau of Narcotics, acting without a warrant or probable cause, entered his apartment, arrested him for narcotics offenses, manacled him in front of his wife and children, threatened to arrest the entire family, searched the apartment, and later subjected him to a visual strip search. He sued the agents for damages, claiming the entry, arrest, and search violated the Fourth Amendment. The lower courts dismissed because no federal statute authorized a damages suit against federal officers for such a violation. ## Issue Whether a victim of an unconstitutional search and seizure by federal officers may sue them for money damages directly under the Fourth Amendment, even though no statute creates the cause of action. ## Rule Yes. The Fourth Amendment itself supports a damages remedy against federal officers who violate it. Invoking *Bell v. Hood*, the Court reasoned that",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-397",
      "page": null,
      "quote": "Having concluded that petitioner's complaint states a cause of action under the Fourth Amendment . . . we hold that petitioner is entitled to recover money damages for any injuries he has suffered as a result of the agents' violation of the Amendment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1971-06-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Bivens v. Six Unknown Named Agents",
    "varies_by_point": false,
    "scope_note": "Core holding (4A damages against federal officers) remains good law; the Court has declined to extend Bivens to new contexts (Ziglar v. Abbasi (2017); Egbert v. Boule (2022)).",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane1_negative"
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
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Monell v. New York City Dept. of Social Servs.",
          "cluster_id": 109881,
          "cite": [
            "56 L. Ed. 2d 611",
            "98 S. Ct. 2018",
            "436 U.S. 658",
            "1978 U.S. LEXIS 100",
            "16 Empl. Prac. Dec. (CCH) 8345",
            "17 Fair Empl. Prac. Cas. (BNA) 873"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
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
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harlow v. Fitzgerald",
          "cluster_id": 110763,
          "cite": [
            "73 L. Ed. 2d 396",
            "102 S. Ct. 2727",
            "457 U.S. 800",
            "1982 U.S. LEXIS 139"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neitzke v. Williams",
          "cluster_id": 112254,
          "cite": [
            "104 L. Ed. 2d 338",
            "109 S. Ct. 1827",
            "490 U.S. 319",
            "1989 U.S. LEXIS 2231",
            "57 U.S.L.W. 4493"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
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
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
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
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      },
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
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anderson v. Creighton",
          "cluster_id": 111953,
          "cite": [
            "97 L. Ed. 2d 523",
            "107 S. Ct. 3034",
            "483 U.S. 635",
            "1987 U.S. LEXIS 2894",
            "55 U.S.L.W. 5092"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schneckloth v. Bustamonte",
          "cluster_id": 108800,
          "cite": [
            "36 L. Ed. 2d 854",
            "93 S. Ct. 2041",
            "412 U.S. 218",
            "1973 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Steel Co. v. Citizens for a Better Environment",
          "cluster_id": 2620886,
          "cite": [
            "140 L. Ed. 2d 210",
            "118 S. Ct. 1003",
            "523 U.S. 83",
            "1998 U.S. LEXIS 1601",
            "66 U.S.L.W. 4174",
            "98 Daily Journal DAR 2102",
            "11 Fla. L. Weekly Fed. S 369",
            "1998 Colo. J. C.A.R. 1025",
            "98 Cal. Daily Op. Serv. 1512",
            "28 Envtl. L. Rep. (Envtl. Law Inst.) 20434",
            "46 ERC (BNA) 1097"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
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
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mitchell v. Forsyth",
          "cluster_id": 111481,
          "cite": [
            "86 L. Ed. 2d 411",
            "105 S. Ct. 2806",
            "472 U.S. 511",
            "1985 U.S. LEXIS 113",
            "53 U.S.L.W. 4798",
            "2 Fed. R. Serv. 3d 221"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lewis v. Casey",
          "cluster_id": 118054,
          "cite": [
            "135 L. Ed. 2d 606",
            "116 S. Ct. 2174",
            "518 U.S. 343",
            "1996 U.S. LEXIS 4220"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mt. Healthy City School District Board of Education v. Doyle",
          "cluster_id": 109574,
          "cite": [
            "50 L. Ed. 2d 471",
            "97 S. Ct. 568",
            "429 U.S. 274",
            "1977 U.S. LEXIS 29",
            "1 I.E.R. Cas. (BNA) 76"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ben Gary Triestman v. Federal Bureau of Prisons, United States of America",
          "cluster_id": 796150,
          "cite": [
            "470 F.3d 471",
            "2006 U.S. App. LEXIS 29858",
            "2006 WL 3499975"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Los Angeles v. Lyons",
          "cluster_id": 110916,
          "cite": [
            "75 L. Ed. 2d 675",
            "103 S. Ct. 1660",
            "461 U.S. 95",
            "1983 U.S. LEXIS 152",
            "51 U.S.L.W. 4424"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hill v. Lappin",
          "cluster_id": 181820,
          "cite": [
            "630 F.3d 468",
            "2010 U.S. App. LEXIS 26261",
            "2010 WL 5288892"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Porter v. Nussle",
          "cluster_id": 118483,
          "cite": [
            "152 L. Ed. 2d 12",
            "122 S. Ct. 983",
            "534 U.S. 516",
            "2002 U.S. LEXIS 1373"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Allen v. McCurry",
          "cluster_id": 110360,
          "cite": [
            "66 L. Ed. 2d 308",
            "101 S. Ct. 411",
            "449 U.S. 90",
            "1980 U.S. LEXIS 156",
            "49 U.S.L.W. 4015"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Federal Deposit Insurance v. Meyer",
          "cluster_id": 112931,
          "cite": [
            "127 L. Ed. 2d 308",
            "114 S. Ct. 996",
            "510 U.S. 471",
            "1994 U.S. LEXIS 1866",
            "94 Cal. Daily Op. Serv. 1298",
            "93 Daily Journal DAR 2365",
            "62 U.S.L.W. 4138",
            "7 Fla. L. Weekly Fed. S 761",
            "63 Empl. Prac. Dec. (CCH) 42,847"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul v. Davis",
          "cluster_id": 109402,
          "cite": [
            "47 L. Ed. 2d 405",
            "96 S. Ct. 1155",
            "424 U.S. 693",
            "1976 U.S. LEXIS 112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
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
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
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
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hafer v. Melo",
          "cluster_id": 112657,
          "cite": [
            "116 L. Ed. 2d 301",
            "112 S. Ct. 358",
            "502 U.S. 21",
            "1991 U.S. LEXIS 6502",
            "57 Empl. Prac. Dec. (CCH) 41,059"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bivens v. Six Unknown Named Agents:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108375 OR 9883113 OR 9883114 OR 9883115 OR 9883116 OR 9883117) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjI2OTEyMDAwMDAwJnM9NDkwMjYzNiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108375+OR+9883113+OR+9883114+OR+9883115+OR+9883116+OR+9883117%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108375 OR 9883113 OR 9883114 OR 9883115 OR 9883116 OR 9883117)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMDQxJnM9NzA4MDk5OSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28108375+OR+9883113+OR+9883114+OR+9883115+OR+9883116+OR+9883117%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108375 OR 9883113 OR 9883114 OR 9883115 OR 9883116 OR 9883117)",
        "reviewed": 153,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 153,
        "triage_read": 0,
        "triage_snippet_classified": 153
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108375 OR 9883113 OR 9883114 OR 9883115 OR 9883116 OR 9883117)",
    "indexed_citing_opinions": 5558,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108375,
        "count": 4988,
        "count_source": "search"
      },
      {
        "opinion_id": 9883113,
        "count": 640,
        "count_source": "search"
      },
      {
        "opinion_id": 9883114,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9883115,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9883116,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9883117,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 18304,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/bivens-v-six-unknown-named-agents.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk1MTI1OCZzPTEwNjYxNTg4JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108375+OR+9883113+OR+9883114+OR+9883115+OR+9883116+OR+9883117%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108375,
        "cited_id": 90667,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 91076,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 92059,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 92766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 93880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 95333,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 95662,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 96087,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 96819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 97862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 100989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 101032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 101911,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 102063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 102125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 103012,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 103201,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 103531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 103794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 104250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 104272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 104468,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 105224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 105511,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 105933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 106628,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 106845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 107547,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 107898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 107963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 108261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 108273,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 260072,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 284380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 1116658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 1461249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 1518638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 1674567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 2390269,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
        "cited_id": 3576215,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108375,
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
    "date_created": "2026-07-04T22:57:48Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:05:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:05:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:09:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:05:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Bivens v. Six Unknown Named Agents

```
<div>
<center><b><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. 388</a></span> (1971)</b></center>
<center><h1>BIVENS<br>
v.<br>
SIX UNKNOWN NAMED AGENTS OF FEDERAL BUREAU OF NARCOTICS.</h1></center>
<center>No. 301.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 12, 1971</center>
<center>Decided June 21, 1971</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SECOND CIRCUIT.
<p><i>Stephen A. Grant</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Jerome Feit</i> argued the cause for respondents. On the brief were <i>Solicitor General Griswold, Assistant Attorney General Ruckelshaus,</i> and <i>Robert V. Zener.</i></p>
<p><i>Melvin L. Wulf</i> filed a brief for the American Civil Liberties Union as <i>amicus curiae</i> urging reversal.</p>
<p><span class="star-pagination">*389</span> MR. JUSTICE BRENNAN delivered the opinion of the Court.</p>
<p>The Fourth Amendment provides that:</p>
<blockquote>"The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated . . . ."</blockquote>
<p>In <i>Bell</i> v. <i>Hood,</i> <span class="citation" data-id="9419809"><a href="/opinion/104272/bell-v-hood/" aria-description="Citation for case: Bell v. Hood">327 U. S. 678</a></span> (1946), we reserved the question whether violation of that command by a federal agent acting under color of his authority gives rise to a cause of action for damages consequent upon his unconstitutional conduct. Today we hold that it does.</p>
<p>This case has its origin in an arrest and search carried out on the morning of November 26, 1965. Petitioner's complaint alleged that on that day respondents, agents of the Federal Bureau of Narcotics acting under claim of federal authority, entered his apartment and arrested him for alleged narcotics violations. The agents manacled petitioner in front of his wife and children, and threatened to arrest the entire family. They searched the apartment from stem to stern. Thereafter, petitioner was taken to the federal courthouse in Brooklyn, where he was interrogated, booked, and subjected to a visual strip search.</p>
<p>On July 7, 1967, petitioner brought suit in Federal District Court. In addition to the allegations above, his complaint asserted that the arrest and search were effected without a warrant, and that unreasonable force was employed in making the arrest; fairly read, it alleges as well that the arrest was made without probable cause.<sup>[1]</sup> Petitioner claimed to have suffered great humiliation, <span class="star-pagination">*390</span> embarrassment, and mental suffering as a result of the agents' unlawful conduct, and sought $15,000 damages from each of them. The District Court, on respondents' motion, dismissed the complaint on the ground, <i>inter alia,</i> that it failed to state a cause of action.<sup>[2]</sup> <span class="citation" data-id="1461249"><a href="/opinion/1461249/bivens-v-6-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. 6 Unknown Named Agents of Federal Bureau of...">276 F. Supp. 12</a></span> (EDNY 1967). The Court of Appeals, one judge concurring specially,<sup>[3]</sup> affirmed on that basis. <span class="citation" data-id="9454464"><a href="/opinion/284380/webster-bivens-v-six-unknown-named-agents-of-the-federal-bureau-of/" aria-description="Citation for case: Webster Bivens v. Six Unknown Named Agents of the Federal...">409 F. 2d 718</a></span> (CA2 1969). We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./399/905/">399 U. S. 905</a></span> (1970). We reverse.</p>
<p></p>
<h2>I</h2>
<p>Respondents do not argue that petitioner should be entirely without remedy for an unconstitutional invasion of his rights by federal agents. In respondents' view, however, the rights that petitioner assertsprimarily rights of privacyare creations of state and not of federal law. Accordingly, they argue, petitioner may obtain money damages to redress invasion of these rights only by an action in tort, under state law, in the state courts. In this scheme the Fourth Amendment would serve merely to limit the extent to which the agents could defend <span class="star-pagination">*391</span> the state law tort suit by asserting that their actions were a valid exercise of federal power: if the agents were shown to have violated the Fourth Amendment, such a defense would be lost to them and they would stand before the state law merely as private individuals. Candidly admitting that it is the policy of the Department of Justice to remove all such suits from the state to the federal courts for decision,<sup>[4]</sup> respondents nevertheless urge that we uphold dismissal of petitioner's complaint in federal court, and remit him to filing an action in the state courts in order that the case may properly be removed to the federal court for decision on the basis of state law.</p>
<p>We think that respondents' thesis rests upon an unduly restrictive view of the Fourth Amendment's protection against unreasonable searches and seizures by federal agents, a view that has consistently been rejected by this Court. Respondents seek to treat the relationship between a citizen and a federal agent unconstitutionally exercising his authority as no different from the relationship <span class="star-pagination">*392</span> between two private citizens. In so doing, they ignore the fact that power, once granted, does not disappear like a magic gift when it is wrongfully used. An agent actingalbeit unconstitutionallyin the name of the United States possesses a far greater capacity for harm than an individual trespasser exercising no authority other than his own. Cf. <i>Amos</i> v. <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/#317" aria-description="Citation for case: Amos v. United States">255 U. S. 313, 317</a></span> (1921); <i>United States</i> v. <i>Classic,</i> <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/#326" aria-description="Citation for case: United States v. Classic">313 U. S. 299, 326</a></span> (1941). Accordingly, as our cases make clear, the Fourth Amendment operates as a limitation upon the exercise of federal power regardless of whether the State in whose jurisdiction that power is exercised would prohibit or penalize the identical act if engaged in by a private citizen. It guarantees to citizens of the United States the absolute right to be free from unreasonable searches and seizures carried out by virtue of federal authority. And "where federally protected rights have been invaded, it has been the rule from the beginning that courts will be alert to adjust their remedies so as to grant the necessary relief." <i>Bell</i> v. <i>Hood,</i> <span class="citation" data-id="9419809"><a href="/opinion/104272/bell-v-hood/#684" aria-description="Citation for case: Bell v. Hood">327 U. S., at 684</a></span> (footnote omitted); see <i>Bemis Bros. Bag Co.</i> v. <i>United States,</i> <span class="citation" data-id="102063"><a href="/opinion/102063/bemis-bro-bag-co-v-united-states/#36" aria-description="Citation for case: Bemis Bro. Bag Co. v. United States">289 U. S. 28, 36</a></span> (1933) (Cardozo, J.); <i>The Western Maid,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./257/419/">257 U. S. 419</a></span>, 433 (1922) (Holmes, J.).</p>
<p><i>First.</i> Our cases have long since rejected the notion that the Fourth Amendment proscribes only such conduct as would, if engaged in by private persons, be condemned by state law. Thus in <i>Gambino</i> v. <i>United States,</i> <span class="citation" data-id="101180"><a href="/opinion/101180/gambino-v-united-states/" aria-description="Citation for case: Gambino v. United States">275 U. S. 310</a></span> (1927), petitioners were convicted of conspiracy to violate the National Prohibition Act on the basis of evidence seized by state police officers incident to petitioners' arrest by those officers solely for the purpose of enforcing federal law. <span class="citation" data-id="101180"><a href="/opinion/101180/gambino-v-united-states/#314" aria-description="Citation for case: Gambino v. United States"><i>Id.,</i> at 314</a></span>. Notwithstanding the lack of probable cause for the arrest, <span class="citation" data-id="101180"><a href="/opinion/101180/gambino-v-united-states/#313" aria-description="Citation for case: Gambino v. United States"><i>id.,</i> at 313</a></span>, it would have been permissible under state law if effected <span class="star-pagination">*393</span> by private individuals.<sup>[5]</sup> It appears, moreover, that the officers were under direction from the Governor to aid in the enforcement of federal law. <span class="citation" data-id="101180"><a href="/opinion/101180/gambino-v-united-states/#315" aria-description="Citation for case: Gambino v. United States"><i>Id.,</i> at 315-317</a></span>. Accordingly, if the Fourth Amendment reached only to conduct impermissible under the law of the State, the Amendment would have had no application to the case. Yet this Court held the Fourth Amendment applicable and reversed petitioners' convictions as having been based upon evidence obtained through an unconstitutional search and seizure. Similarly, in <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U. S. 28</a></span> (1927), the petitioner was convicted on the basis of evidence seized under a warrant issued, without probable cause under the Fourth Amendment, by a state court judge for a state law offense. At the invitation of state law enforcement officers, a federal prohibition agent participated in the search. This Court explicitly refused to inquire whether the warrant was "good under the state law . . . since in no event could it constitute the basis for a <i>federal</i> search and seizure." <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#29" aria-description="Citation for case: Byars v. United States"><i>Id.,</i> at 29</a></span> (emphasis added).<sup>[6]</sup> And our recent decisions regarding electronic surveillance have made it clear beyond peradventure that the Fourth Amendment is not tied to the <span class="star-pagination">*394</span> niceties of local trespass laws. <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967); <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967); <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 511</a></span> (1961). In light of these cases, respondents' argument that the Fourth Amendment serves only as a limitation on federal defenses to a state law claim, and not as an independent limitation upon the exercise of federal power, must be rejected.</p>
<p><i>Second.</i> The interests protected by state laws regulating trespass and the invasion of privacy, and those protected by the Fourth Amendment's guarantee against unreasonable searches and seizures, may be inconsistent or even hostile. Thus, we may bar the door against an unwelcome private intruder, or call the police if he persists in seeking entrance. The availability of such alternative means for the protection of privacy may lead the State to restrict imposition of liability for any consequent trespass. A private citizen, asserting no authority other than his own, will not normally be liable in trespass if he demands, and is granted, admission to another's house. See W. Prosser, The Law of Torts § 18, pp. 109-110 (3d ed. 1964); 1 F. Harper &amp; F. James, The Law of Torts § 1.11 (1956). But one who demands admission under a claim of federal authority stands in a far different position. Cf. <i>Amos</i> v. <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/#317" aria-description="Citation for case: Amos v. United States">255 U. S. 313, 317</a></span> (1921). The mere invocation of federal power by a federal law enforcement official will normally render futile any attempt to resist an unlawful entry or arrest by resort to the local police; and a claim of authority to enter is likely to unlock the door as well. See <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#386" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 386</a></span> (1914); <i>Amos</i> v. <i>United States, supra</i><i>.</i><sup>[7]</sup> "In such cases there is no safety for the citizen, <span class="star-pagination">*395</span> except in the protection of the judicial tribunals, for rights which have been invaded by the officers of the government, professing to act in its name. There remains to him but the alternative of resistance, which may amount to crime." <i>United States</i> v. <i>Lee,</i> <span class="citation" data-id="90667"><a href="/opinion/90667/united-states-v-lee/#219" aria-description="Citation for case: United States v. Lee">106 U. S. 196, 219</a></span> (1882).<sup>[8]</sup> Nor is it adequate to answer that state law may take into account the different status of one clothed with the authority of the Federal Government. For just as state law may not authorize federal agents to violate the Fourth Amendment, <i>Byars</i> v. <i>United States, supra</i><i>; </i><i>Weeks</i> v. <i>United States, supra</i><i>; </i><i>In re Ayers,</i> <span class="citation" data-id="9417465"><a href="/opinion/92059/in-re-ayers/#507" aria-description="Citation for case: In Re Ayers">123 U. S. 443, 507</a></span> (1887), neither may state law undertake to limit the extent to which federal authority can be exercised. <i>In re Neagle,</i> <span class="citation" data-id="9417530"><a href="/opinion/92766/in-re-neagle/" aria-description="Citation for case: In Re Neagle">135 U. S. 1</a></span> (1890). The inevitable consequence of this dual limitation on state power is that the federal question becomes not merely a possible defense to the state law action, but an independent claim both necessary and sufficient to make out the plaintiff's cause of action. Cf. <i>Boilermakers</i> v. <i>Hardeman,</i> <span class="citation" data-id="9424456"><a href="/opinion/108273/international-brotherhood-of-boilermakers-iron-shipbuilders-blacksmiths/#241" aria-description="Citation for case: International Brotherhood of Boilermakers, Iron...">401 U. S. 233, 241</a></span> (1971).</p>
<p><i>Third.</i> That damages may be obtained for injuries consequent upon a violation of the Fourth Amendment by federal officials should hardly seem a surprising proposition. Historically, damages have been regarded as the ordinary remedy for an invasion of personal interests in liberty. See <i>Nixon</i> v. <i>Condon,</i> <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/" aria-description="Citation for case: Nixon v. Condon">286 U. S. 73</a></span> (1932); <span class="star-pagination">*396</span> <i>Nixon</i> v. <i>Herndon,</i> <span class="citation" data-id="101032"><a href="/opinion/101032/nixon-v-herndon/#540" aria-description="Citation for case: Nixon v. Herndon">273 U. S. 536, 540</a></span> (1927); <i>Swafford</i> v. <i>Templeton,</i> <span class="citation" data-id="95662"><a href="/opinion/95662/swafford-v-templeton/" aria-description="Citation for case: Swafford v. Templeton">185 U. S. 487</a></span> (1902); <i>Wiley</i> v. <i>Sinkler,</i> <span class="citation" data-id="95333"><a href="/opinion/95333/wiley-v-sinkler/" aria-description="Citation for case: Wiley v. Sinkler">179 U. S. 58</a></span> (1900); J. Landynski, Search and Seizure and the Supreme Court 28 <i>et seq.</i> (1966); N. Lasson, History and Development of the Fourth Amendment to the United States Constitution 43 <i>et seq.</i> (1937); Katz, The Jurisprudence of Remedies: Constitutional Legality and the Law of Torts in <i>Bell</i> v. <i><span class="citation" data-id="9419809"><a href="/opinion/104272/bell-v-hood/" aria-description="Citation for case: Bell v. Hood">Hood</a></span>,</i> <span class="citation no-link">117 U. Pa. L. Rev. 1</span>, 8-33 (1968); cf. <i>West</i> v. <i>Cabell,</i> <span class="citation" data-id="93880"><a href="/opinion/93880/west-v-cabell/" aria-description="Citation for case: West v. Cabell">153 U. S. 78</a></span> (1894); <i>Lammon</i> v. <i>Feusier,</i> <span class="citation" data-id="91076"><a href="/opinion/91076/lammon-v-feusier/" aria-description="Citation for case: Lammon v. Feusier">111 U. S. 17</a></span> (1884). Of course, the Fourth Amendment does not in so many words provide for its enforcement by an award of money damages for the consequences of its violation. But "it is . . . well settled that where legal rights have been invaded, and a federal statute provides for a general right to sue for such invasion, federal courts may use any available remedy to make good the wrong done." <i>Bell</i> v. <i>Hood,</i> <span class="citation" data-id="9419809"><a href="/opinion/104272/bell-v-hood/#684" aria-description="Citation for case: Bell v. Hood">327 U. S., at 684</a></span> (footnote omitted). The present case involves no special factors counselling hesitation in the absence of affirmative action by Congress. We are not dealing with a question of "federal fiscal policy," as in <i>United States</i> v. <i>Standard Oil Co.,</i> <span class="citation" data-id="9420054"><a href="/opinion/104468/united-states-v-standard-oil-co-of-california/#311" aria-description="Citation for case: United States v. Standard Oil Co. Of California">332 U. S. 301, 311</a></span> (1947). In that case we refused to infer from the Government-soldier relationship that the United States could recover damages from one who negligently injured a soldier and thereby caused the Government to pay his medical expenses and lose his services during the course of his hospitalization. Noting that Congress was normally quite solicitous where the federal purse was involved, we pointed out that "the United States [was] the party plaintiff to the suit. And the United States has power at any time to create the liability." <span class="citation" data-id="9420054"><a href="/opinion/104468/united-states-v-standard-oil-co-of-california/#316" aria-description="Citation for case: United States v. Standard Oil Co. Of California"><i>Id.,</i> at 316</a></span>; see <i>United States</i> v. <i>Gilman,</i> <span class="citation" data-id="105224"><a href="/opinion/105224/united-states-v-gilman/" aria-description="Citation for case: United States v. Gilman">347 U. S. 507</a></span> (1954). Nor are we asked in this case to impose liability upon a congressional employee for actions contrary to no constitutional <span class="star-pagination">*397</span> prohibition, but merely said to be in excess of the authority delegated to him by the Congress. <i>Wheeldin</i> v. <i>Wheeler,</i> <span class="citation" data-id="9422624"><a href="/opinion/106628/wheeldin-v-wheeler/" aria-description="Citation for case: Wheeldin v. Wheeler">373 U. S. 647</a></span> (1963). Finally, we cannot accept respondents' formulation of the question as whether the availability of money damages is necessary to enforce the Fourth Amendment. For we have here no explicit congressional declaration that persons injured by a federal officer's violation of the Fourth Amendment may not recover money damages from the agents, but must instead be remitted to another remedy, equally effective in the view of Congress. The question is merely whether petitioner, if he can demonstrate an injury consequent upon the violation by federal agents of his Fourth Amendment rights, is entitled to redress his injury through a particular remedial mechanism normally available in the federal courts. Cf. <i>J. I. Case Co.</i> v. <i>Borak,</i> <span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/#433" aria-description="Citation for case: J. I. Case Co. v. Borak">377 U. S. 426, 433</a></span> (1964); <i>Jacobs</i> v. <i>United States,</i> <span class="citation" data-id="102125"><a href="/opinion/102125/jacobs-v-united-states/#16" aria-description="Citation for case: Jacobs v. United States">290 U. S. 13, 16</a></span> (1933). "The very essence of civil liberty certainly consists in the right of every individual to claim the protection of the laws, whenever he receives an injury." <i>Marbury</i> v. <i>Madison,</i> <span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/#163" aria-description="Citation for case: Marbury v. Madison">1 Cranch 137, 163</a></span> (1803). Having concluded that petitioner's complaint states a cause of action under the Fourth Amendment, <i>supra,</i> at 390-395, we hold that petitioner is entitled to recover money damages for any injuries he has suffered as a result of the agents' violation of the Amendment.</p>
<p></p>
<h2>II</h2>
<p>In addition to holding that petitioner's complaint had failed to state facts making out a cause of action, the District Court ruled that in any event respondents were immune from liability by virtue of their official position. <span class="citation" data-id="1461249"><a href="/opinion/1461249/bivens-v-6-unknown-named-agents-of-federal-bureau-of-narcotics/#15" aria-description="Citation for case: Bivens v. 6 Unknown Named Agents of Federal Bureau of...">276 F. Supp., at 15</a></span>. This question was not passed upon by the Court of Appeals, and accordingly we do not consider <span class="star-pagination">*398</span> it here. The judgment of the Court of Appeals is reversed and the case is remanded for further proceedings consistent with this opinion.</p>
<p><i>So ordered.</i></p>
<p>MR. JUSTICE HARLAN, concurring in the judgment.</p>
<p>My initial view of this case was that the Court of Appeals was correct in dismissing the complaint, but for reasons stated in this opinion I am now persuaded to the contrary. Accordingly, I join in the judgment of reversal.</p>
<p>Petitioner alleged, in his suit in the District Court for the Eastern District of New York, that the defendants, federal agents acting under color of federal law, subjected him to a search and seizure contravening the requirements of the Fourth Amendment. He sought damages in the amount of $15,000 from each of the agents. Federal jurisdiction was claimed, <i>inter alia,</i><sup>[1]</sup> under <span class="citation no-link">28 U. S. C. § 1331</span> (a) which provides:</p>
<blockquote>"The district courts shall have original jurisdiction of all civil actions wherein the matter in controversy exceeds the sum or value of $10,000 exclusive of interest and costs, and arises under the Constitution, laws, or treaties of the United States."</blockquote>
<p>The District Court dismissed the complaint for lack of federal jurisdiction under <span class="citation no-link">28 U. S. C. § 1331</span> (a) and failure to state a claim for which relief may be granted. <span class="citation" data-id="1461249"><a href="/opinion/1461249/bivens-v-6-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. 6 Unknown Named Agents of Federal Bureau of...">276 F. Supp 12</a></span> (EDNY 1967). On appeal, the Court of Appeals concluded, on the basis of this Court's decision in <i>Bell</i> v. <i>Hood,</i> <span class="citation" data-id="9419809"><a href="/opinion/104272/bell-v-hood/" aria-description="Citation for case: Bell v. Hood">327 U. S. 678</a></span> (1946), that petitioner's claim for damages did "[arise] under the Constitution" <span class="star-pagination">*399</span> within the meaning of <span class="citation no-link">28 U. S. C. § 1331</span> (a); but the District Court's judgment was affirmed on the ground that the complaint failed to state a claim for which relief can be granted. <span class="citation" data-id="9454464"><a href="/opinion/284380/webster-bivens-v-six-unknown-named-agents-of-the-federal-bureau-of/" aria-description="Citation for case: Webster Bivens v. Six Unknown Named Agents of the Federal...">409 F. 2d 718</a></span> (CA2 1969).</p>
<p>In so concluding, Chief Judge Lumbard's opinion reasoned, in essence, that: (1) the framers of the Fourth Amendment did not appear to contemplate a "wholly new federal cause of action founded directly on the Fourth Amendment," <span class="citation" data-id="9454464"><a href="/opinion/284380/webster-bivens-v-six-unknown-named-agents-of-the-federal-bureau-of/#721" aria-description="Citation for case: Webster Bivens v. Six Unknown Named Agents of the Federal..."><i>id.,</i> at 721</a></span>, and (2) while the federal courts had power under a general grant of jurisdiction to imply a federal remedy for the enforcement of a constitutional right, they should do so only when the absence of alternative remedies renders the constitutional command a "mere `form of words.' " <span class="citation" data-id="9454464"><a href="/opinion/284380/webster-bivens-v-six-unknown-named-agents-of-the-federal-bureau-of/#723" aria-description="Citation for case: Webster Bivens v. Six Unknown Named Agents of the Federal..."><i>Id.,</i> at 723</a></span>. The Government takes essentially the same position here. Brief for Respondents 4-5. And two members of the Court add the contention that we lack the constitutional power to accord Bivens a remedy for damages in the absence of congressional action creating "a federal cause of action for damages for an unreasonable search in violation of the Fourth Amendment." Opinion of MR. JUSTICE BLACK, <i>post,</i> at 427; see also opinion of THE CHIEF JUSTICE, <i>post,</i> at 418, 422.</p>
<p>For the reasons set forth below, I am of the opinion that federal courts do have the power to award damages for violation of "constitutionally protected interests" and I agree with the Court that a traditional judicial remedy such as damages is appropriate to the vindication of the personal interests protected by the Fourth Amendment.</p>
<p></p>
<h2>I</h2>
<p>I turn first to the contention that the constitutional power of federal courts to accord Bivens damages for his claim depends on the passage of a statute creating a "federal cause of action." Although the point is not <span class="star-pagination">*400</span> entirely free of ambiguity,<sup>[2]</sup> I do not understand either the Government or my dissenting Brothers to maintain that Bivens' contention that he is entitled to be free from the type of official conduct prohibited by the Fourth Amendment depends on a decision by the State in which he resides to accord him a remedy. Such a position would be incompatible with the presumed availability of federal equitable relief, if a proper showing can be made in terms of the ordinary principles governing equitable remedies. See <i>Bell</i> v. <i>Hood,</i> <span class="citation" data-id="9419809"><a href="/opinion/104272/bell-v-hood/#684" aria-description="Citation for case: Bell v. Hood">327 U. S. 678, 684</a></span> (1946). However broad a federal court's discretion concerning equitable remedies, it is absolutely clearat least after <i>Erie R. Co.</i> v. <i>Tompkins,</i> <span class="citation" data-id="9418969"><a href="/opinion/103012/erie-railroad-v-tompkins/" aria-description="Citation for case: Erie Railroad v. Tompkins">304 U. S. 64</a></span> (1938)that in a nondiversity suit a federal court's power to grant even equitable relief depends on the presence of a substantive right derived from federal law. Compare <i>Guaranty Trust Co.</i> v. <i>York,</i> <span class="citation" data-id="9419693"><a href="/opinion/104182/guaranty-trust-co-v-york/#105" aria-description="Citation for case: Guaranty Trust Co. v. York">326 U. S. 99, 105-107</a></span> (1945), with <i>Holmberg</i> v. <i>Armbrecht,</i> <span class="citation" data-id="9419776"><a href="/opinion/104250/holmberg-v-armbrecht/#395" aria-description="Citation for case: Holmberg v. Armbrecht">327 U. S. 392, 395</a></span> (1946). See also H. Hart &amp; H. Wechsler, The Federal Courts and the Federal System 818-819 (1953).</p>
<p>Thus the interest which Bivens claimsto be free from official conduct in contravention of the Fourth Amendmentis a federally protected interest. See generally Katz, The Jurisprudence of Remedies: Constitutional Legality and the Law of Torts in <i>Bell</i> v. <i><span class="citation" data-id="9419809"><a href="/opinion/104272/bell-v-hood/" aria-description="Citation for case: Bell v. Hood">Hood</a></span>,</i> <span class="citation no-link">117 U. Pa. L. Rev. 1</span>, 33-34 (1968).<sup>[3]</sup> Therefore, the question <span class="star-pagination">*401</span> of judicial <i>power</i> to grant Bivens damages is not a problem of the "source" of the "right"; instead, the question is whether the power to authorize damages as a judicial <span class="star-pagination">*402</span> remedy for the vindication of a federal constitutional right is placed by the Constitution itself exclusively in Congress' hands.</p>
<p></p>
<h2>II</h2>
<p>The contention that the federal courts are powerless to accord a litigant damages for a claimed invasion of his federal constitutional rights until Congress explicitly authorizes the remedy cannot rest on the notion that the decision to grant compensatory relief involves a resolution of policy considerations not susceptible of judicial discernment. Thus, in suits for damages based on violations of federal statutes lacking any express authorization of a damage remedy, this Court has authorized such relief where, in its view, damages are necessary to effectuate the congressional policy underpinning the substantive provisions of the statute. <i>J. I. Case Co.</i> v. <i>Borak,</i> <span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">377 U. S. 426</a></span> (1964); <i>Tunstall</i> v. <i>Brotherhood of Locomotive Firemen &amp; Enginemen,</i> <span class="citation" data-id="104039"><a href="/opinion/104039/tunstall-v-brotherhood-of-locomotive-firemen-enginemen/#213" aria-description="Citation for case: Tunstall v. Brotherhood of Locomotive Firemen &amp; Enginemen">323 U. S. 210, 213</a></span> (1944). Cf. <i>Wyandotte Transportation Co.</i> v. <i>United States,</i> <span class="citation" data-id="9423532"><a href="/opinion/107547/wyandotte-transportation-co-v-united-states/#201" aria-description="Citation for case: Wyandotte Transportation Co. v. United States">389 U. S. 191, 201-204</a></span> (1967).<sup>[4]</sup></p>
<p><span class="star-pagination">*403</span> If it is not the nature of the remedy which is thought to render a judgment as to the appropriateness of damages inherently "legislative," then it must be the nature of the legal interest offered as an occasion for invoking otherwise appropriate judicial relief. But I do not think that the fact that the interest is protected by the Constitution rather than statute or common law justifies the assertion that federal courts are powerless to grant damages in the absence of explicit congressional action authorizing the remedy. Initially, I note that it would be at least anomalous to conclude that the federal judiciary while competent to choose among the range of traditional judicial remedies to implement statutory and common-law policies, and even to generate substantive rules governing primary behavior in furtherance of broadly formulated policies articulated by statute or Constitution, see <i>Textile Workers</i> v. <i>Lincoln Mills,</i> <span class="citation" data-id="9421446"><a href="/opinion/105511/textile-workers-v-lincoln-mills-of-ala/" aria-description="Citation for case: Textile Workers v. Lincoln Mills of Ala.">353 U. S. 448</a></span> (1957); <i>United States</i> v. <i>Standard Oil Co.,</i> <span class="citation" data-id="9420054"><a href="/opinion/104468/united-states-v-standard-oil-co-of-california/#304" aria-description="Citation for case: United States v. Standard Oil Co. Of California">332 U. S. 301, 304-311</a></span> (1947); <i>Clearfield Trust Co.</i> v. <i>United States,</i> <span class="citation" data-id="103794"><a href="/opinion/103794/clearfield-trust-co-v-united-states/" aria-description="Citation for case: Clearfield Trust Co. v. United States">318 U. S. 363</a></span> (1943)is powerless to accord a damages <span class="star-pagination">*404</span> remedy to vindicate social policies which, by virtue of their inclusion in the Constitution, are aimed predominantly at restraining the Government as an instrument of the popular will.</p>
<p>More importantly, the presumed availability of federal equitable relief against threatened invasions of constitutional interests appears entirely to negate the contention that the status of an interest as constitutionally protected divests federal courts of the power to grant damages absent express congressional authorization. Congress provided specially for the exercise of equitable remedial powers by federal courts, see Act of May 8, 1792, § 2, <span class="citation no-link">1 Stat. 276</span>; C. Wright, Law of Federal Courts 257 (2d ed., 1970), in part because of the limited availability of equitable remedies in state courts in the early days of the Republic. See <i>Guaranty Trust Co.</i> v. <i>York,</i> <span class="citation" data-id="9419693"><a href="/opinion/104182/guaranty-trust-co-v-york/#104" aria-description="Citation for case: Guaranty Trust Co. v. York">326 U. S. 99, 104-105</a></span> (1945). And this Court's decisions make clear that, at least absent congressional restrictions, the scope of equitable remedial discretion is to be determined according to the distinctive historical traditions of equity as an institution, <i>Holmberg</i> v. <i>Armbrecht,</i> <span class="citation" data-id="9419776"><a href="/opinion/104250/holmberg-v-armbrecht/#395" aria-description="Citation for case: Holmberg v. Armbrecht">327 U. S. 392, 395-396</a></span> (1946); <i>Sprague</i> v. <i>Ticonic National Bank,</i> <span class="citation" data-id="103201"><a href="/opinion/103201/sprague-v-ticonic-national-bank/#165" aria-description="Citation for case: Sprague v. Ticonic National Bank">307 U. S. 161, 165-166</a></span> (1939). The reach of a federal district court's "inherent equitable powers," <i>Textile Workers</i> v. <i>Lincoln Mills,</i> <span class="citation" data-id="9421446"><a href="/opinion/105511/textile-workers-v-lincoln-mills-of-ala/#460" aria-description="Citation for case: Textile Workers v. Lincoln Mills of Ala.">353 U. S. 448, 460</a></span> (Burton, J., concurring in result), is broad indeed, <i>e. g., </i><i>Swann</i> v. <i>Charlotte-Mecklenburg Board of Education,</i> <span class="citation" data-id="9424427"><a href="/opinion/108261/baird-v-state-bar-of-arizona/" aria-description="Citation for case: Baird v. State Bar of Arizona">401 U. S. 1</a></span> (1971); nonetheless, the federal judiciary is not empowered to grant equitable relief in the absence of congressional action extending jurisdiction over the subject matter of the suit. See <i>Textile Workers</i> v. <span class="citation" data-id="9421446"><a href="/opinion/105511/textile-workers-v-lincoln-mills-of-ala/#460" aria-description="Citation for case: Textile Workers v. Lincoln Mills of Ala."><i>Lincoln Mills, supra,</i> at 460</a></span> (Burton, J., concurring in result); Katz, 117 U. Pa. L. Rev., at 43.<sup>[5]</sup></p>
<p><span class="star-pagination">*405</span> If explicit congressional authorization is an absolute prerequisite to the power of a federal court to accord compensatory relief regardless of the necessity or appropriateness of damages as a remedy simply because of the status of a legal interest as constitutionally protected, then it seems to me that explicit congressional authorization is similarly prerequisite to the exercise of equitable remedial discretion in favor of constitutionally protected interests. Conversely, if a general grant of jurisdiction to the federal courts by Congress is thought adequate to empower a federal court to grant equitable relief for all areas of subject-matter jurisdiction enumerated therein, see <span class="citation no-link">28 U. S. C. § 1331</span> (a), then it seems to me that the same statute is sufficient to empower a federal court to grant a traditional remedy at law.<sup>[6]</sup> Of course, the special historical traditions governing the federal equity system, see <i>Sprague</i> v. <i>Ticonic National Bank,</i> 307 U. S. 161 <span class="star-pagination">*406</span> (1939), might still bear on the comparative appropriateness of granting equitable relief as opposed to money damages. That possibility, however, relates, not to whether the federal courts have the power to afford one type of remedy as opposed to the other, but rather to the criteria which should govern the exercise of our power. To that question, I now pass.</p>
<p></p>
<h2>III</h2>
<p>The major thrust of the Government's position is that, where Congress has not expressly authorized a particular remedy, a federal court should exercise its power to accord a traditional form of judicial relief at the behest of a litigant, who claims a constitutionally protected interest has been invaded, only where the remedy is "essential," or "indispensable for vindicating constitutional rights." Brief for Respondents 19, 24. While this "essentiality" test is most clearly articulated with respect to damages remedies, apparently the Government believes the same test explains the exercise of equitable remedial powers. <i>Id.,</i> at 17-18. It is argued that historically the Court has rarely exercised the power to accord such relief in the absence of an express congressional authorization and that "[i]f Congress had thought that federal officers should be subject to a law different than state law, it would have had no difficulty in saying so, as it did with respect to state officers . . . ." <i>Id.,</i> at 20-21; see <span class="citation no-link">42 U. S. C. § 1983</span>. Although conceding that the standard of determining whether a damage remedy should be utilized to effectuate statutory policies is one of "necessity" or "appropriateness," see <i>J. I. Case Co.</i> v. <i>Borak,</i> <span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/#432" aria-description="Citation for case: J. I. Case Co. v. Borak">377 U. S. 426, 432</a></span> (1964); <i>United States</i> v. <i>Standard Oil Co.,</i> <span class="citation" data-id="9420054"><a href="/opinion/104468/united-states-v-standard-oil-co-of-california/#307" aria-description="Citation for case: United States v. Standard Oil Co. Of California">332 U. S. 301, 307</a></span> (1947), the Government contends that questions concerning congressional discretion to modify judicial remedies relating to constitutionally protected interests warrant a more stringent constraint on <span class="star-pagination">*407</span> the exercise of judicial power with respect to this class of legally protected interests. Brief for Respondents 21-22.</p>
<p>These arguments for a more stringent test to govern the grant of damages in constitutional cases<sup>[7]</sup> seem to be adequately answered by the point that the judiciary has a particular responsibility to assure the vindication of constitutional interests such as those embraced by the Fourth Amendment. To be sure, "it must be remembered that legislatures are ultimate guardians of the liberties and welfare of the people in quite as great a degree as the courts." <i>Missouri, Kansas &amp; Texas R. Co.</i> v. <i>May,</i> <span class="citation" data-id="9417943"><a href="/opinion/96087/missouri-kansas-texas-railway-co-v-may/#270" aria-description="Citation for case: Missouri, Kansas &amp; Texas Railway Co. v. May">194 U. S. 267, 270</a></span> (1904). But it must also be recognized that the Bill of Rights is particularly intended to vindicate the interests of the individual in the face of the popular will as expressed in legislative majorities; at the very least, it strikes me as no more appropriate to await express congressional authorization of traditional judicial relief with regard to these legal interests than with respect to interests protected by federal statutes.</p>
<p>The question then, is, as I see it, whether compensatory relief is "necessary" or "appropriate" to the vindication of the interest asserted. Cf. <i>J. I. Case Co.</i> v. <span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/#432" aria-description="Citation for case: J. I. Case Co. v. Borak"><i>Borak, supra,</i> at 432</a></span>; <i>United States</i> v. <i>Standard Oil Co., supra,</i> at 307; Hill, Constitutional Remedies, 69 Col. L. Rev. 1109, 1155 (1969); Katz, 117 U. Pa. L. Rev., at 72. In resolving that question, it seems to me that the range of policy considerations we may take into account is at least as broad as the range of those a legislature would consider with respect to an express statutory authorization of a traditional remedy. In this regard I agree with the Court that the appropriateness of according Bivens <span class="star-pagination">*408</span> compensatory relief does not turn simply on the deterrent effect liability will have on federal official conduct.<sup>[8]</sup> Damages as a traditional form of compensation for invasion of a legally protected interest may be entirely appropriate even if no substantial deterrent effects on future official lawlessness might be thought to result. Bivens, after all, has invoked judicial processes claiming entitlement to compensation for injuries resulting from allegedly lawless official behavior, if those injuries are properly compensable in money damages. I do not think a court of lawvested with the power to accord a remedyshould deny him his relief simply because he cannot show that future lawless conduct will thereby be deterred.</p>
<p>And I think it is clear that Bivens advances a claim of the sort that, if proved, would be properly compensable in damages. The personal interests protected by the Fourth Amendment are those we attempt to capture by the notion of "privacy"; while the Court today properly points out that the type of harm which officials can inflict when they invade protected zones of an individual's life <span class="star-pagination">*409</span> are different from the types of harm private citizens inflict on one another, the experience of judges in dealing with private trespass and false imprisonment claims supports the conclusion that courts of law are capable of making the types of judgment concerning causation and magnitude of injury necessary to accord meaningful compensation for invasion of Fourth Amendment rights.<sup>[9]</sup></p>
<p>On the other hand, the limitations on state remedies for violation of common-law rights by private citizens argue in favor of a federal damages remedy. The injuries inflicted by officials acting under color of law, while no less compensable in damages than those inflicted by private parties, are substantially different in kind, as the Court's opinion today discusses in detail. See <i>Monroe</i> v. <i>Pape,</i> <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#195" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167, 195</a></span> (1961) (HARLAN, J., concurring). It seems to me entirely proper that these injuries be compensable according to uniform rules of federal law, especially in light of the very large element of federal law which must in any event control the scope of official defenses to liability. See <i>Wheeldin</i> v. <i>Wheeler,</i> <span class="citation" data-id="9422624"><a href="/opinion/106628/wheeldin-v-wheeler/#652" aria-description="Citation for case: Wheeldin v. Wheeler">373 U. S. 647, 652</a></span> (1963); <i>Monroe</i> v. <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#194" aria-description="Citation for case: Monroe v. Pape"><i>Pape, supra,</i> at 194-195</a></span> (HARLAN, J., concurring); <i>Howard</i> v. <i>Lyons,</i> <span class="citation" data-id="9421862"><a href="/opinion/105933/howard-v-lyons/" aria-description="Citation for case: Howard v. Lyons">360 U. S. 593</a></span> (1959). Certainly, there is very little to be gained from the standpoint of federalism by preserving different rules of liability for federal officers dependent on the State where the injury occurs. Cf. <i>United States</i> v. <i>Standard Oil Co.,</i> <span class="citation" data-id="9420054"><a href="/opinion/104468/united-states-v-standard-oil-co-of-california/#305" aria-description="Citation for case: United States v. Standard Oil Co. Of California">332 U. S. 301, 305-311</a></span> (1947).</p>
<p>Putting aside the desirability of leaving the problem of federal official liability to the vagaries of common-law actions, it is apparent that some form of damages is the only possible remedy for someone in Bivens' alleged <span class="star-pagination">*410</span> position. It will be a rare case indeed in which an individual in Bivens' position will be able to obviate the harm by securing injunctive relief from any court. However desirable a direct remedy against the Government might be as a substitute for individual official liability, the sovereign still remains immune to suit. Finally, assuming Bivens' innocence of the crime charged, the "exclusionary rule" is simply irrelevant. For people in Bivens' shoes, it is damages or nothing.</p>
<p>The only substantial policy consideration advanced against recognition of a federal cause of action for violation of Fourth Amendment rights by federal officials is the incremental expenditure of judicial resources that will be necessitated by this class of litigation. There is, however, something ultimately self-defeating about this argument. For if, as the Government contends, damages will rarely be realized by plaintiffs in these cases because of jury hostility, the limited resources of the official concerned, etc., then I am not ready to assume that there will be a significant increase in the expenditure of judicial resources on these claims. Few responsible lawyers and plaintiffs are likely to choose the course of litigation if the statistical chances of success are truly <i>de minimis.</i> And I simply cannot agree with my Brother BLACK that the possibility of "frivolous" claimsif defined simply as claims with no legal meritwarrants closing the courthouse doors to people in Bivens' situation. There are other ways, short of that, of coping with frivolous lawsuits.</p>
<p>On the other hand, ifas I believe is the case with respect, at least, to the most flagrant abuses of official powerdamages to some degree will be available when the option of litigation is chosen, then the question appears to be how Fourth Amendment interests rank on a scale of social values compared with, for example, the interests of stockholders defrauded by misleading proxies. <span class="star-pagination">*411</span> See <i>J. I. Case Co.</i> v. <i><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">Borak, supra</a></span></i><i>.</i> Judicial resources, I am well aware, are increasingly scarce these days. Nonetheless, when we automatically close the courthouse door solely on this basis, we implicitly express a value judgment on the comparative importance of classes of legally protected interests. And current limitations upon the effective functioning of the courts arising from budgetary inadequacies should not be permitted to stand in the way of the recognition of otherwise sound constitutional principles.</p>
<p>Of course, for a variety of reasons, the remedy may not often be sought. See generally Foote, Tort Remedies for Police Violations of Individual Rights, <span class="citation no-link">39 Minn. L. Rev. 493</span> (1955). And the countervailing interests in efficient law enforcement of course argue for a protective zone with respect to many types of Fourth Amendment violations. Cf. <i>Barr</i> v. <i>Matteo,</i> <span class="citation" data-id="9764526"><a href="/opinion/2390269/barr-v-matteo/" aria-description="Citation for case: Barr v. Matteo">360 U. S. 564</a></span> (1959) (opinion of HARLAN, J.). But, while I express no view on the immunity defense offered in the instant case, I deem it proper to venture the thought that at the very least such a remedy would be available for the most flagrant and patently unjustified sorts of police conduct. Although litigants may not often choose to seek relief, it is important, in a civilized society, that the judicial branch of the Nation's government stand ready to afford a remedy in these circumstances. It goes without saying that I intimate no view on the merits of petitioner's underlying claim.</p>
<p>For these reasons, I concur in the judgment of the Court.</p>
<p>MR. CHIEF JUSTICE BURGER, dissenting.</p>
<p>I dissent from today's holding which judicially creates a damage remedy not provided for by the Constitution and not enacted by Congress. We would more surely preserve the important values of the doctrine of separation <span class="star-pagination">*412</span> of powersand perhaps get a better resultby recommending a solution to the Congress as the branch of government in which the Constitution has vested the legislative power. Legislation is the business of the Congress, and it has the facilities and competence for that taskas we do not. Professor Thayer, speaking of the limits on judicial power, albeit in another context, had this to say:<sup>[1]</sup></p>
<blockquote>"And if it be true that the holders of legislative power are careless or evil, yet the constitutional duty of the court remains untouched; it cannot rightly attempt to protect the people, by undertaking a function not its own. On the other hand, by adhering rigidly to its own duty, the court will help, as nothing else can, to fix the spot where responsibility lies, and to bring down on that precise locality the thunderbolt of popular condemnation. . . . For that coursethe true course of judicial duty always will powerfully help to bring the people and their representatives to a sense of their own responsibility."</blockquote>
<p>This case has significance far beyond its facts and its holding. For more than 55 years this Court has enforced a rule under which evidence of undoubted reliability and probative value has been suppressed and excluded from criminal cases whenever it was obtained in violation of the Fourth Amendment. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914); <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#633" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 633</a></span> (1886) (dictum). This rule was extended to the States in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961).<sup>[2]</sup><span class="star-pagination">*413</span> The rule has rested on a theory that suppression of evidence in these circumstances was imperative to deter law enforcement authorities from using improper methods to obtain evidence.</p>
<p>The deterrence theory underlying the suppression doctrine, or exclusionary rule, has a certain appeal in spite of the high price society pays for such a drastic remedy. Notwithstanding its plausibility, many judges and lawyers and some of our most distinguished legal scholars have never quite been able to escape the force of Cardozo's statement of the doctrine's anomalous result:</p>
<blockquote>"The criminal is to go free because the constable has blundered. . . . A room is searched against the law, and the body of a murdered man is found. . . . The privacy of the home has been infringed, and the murderer goes free." <i>People</i> v. <i>Defore,</i> <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#21" aria-description="Citation for case: People v. Defore">242 N. Y. 13, 21, 23-24</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#587" aria-description="Citation for case: People v. Defore">150 N. E. 585, 587, 588</a></span> (1926).<sup>[3]</sup></blockquote>
<p>The plurality opinion in <i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#136" aria-description="Citation for case: Irvine v. California">347 U. S. 128, 136</a></span> (1954), catalogued the doctrine's defects:</p>
<blockquote>"Rejection of the evidence does nothing to punish the wrong-doing official, while it may, and likely will, release the wrong-doing defendant. It deprives society of its remedy against one lawbreaker because he has been pursued by another. It protects one against whom incriminating evidence is discovered, but does nothing to protect innocent persons who are the victims of illegal but fruitless searches."</blockquote>
<p>From time to time members of the Court, recognizing the validity of these protests, have articulated varying <span class="star-pagination">*414</span> alternative justifications for the suppression of important evidence in a criminal trial. Under one of these alternative theories the rule's foundation is shifted to the "sporting contest" thesis that the government must "play the game fairly" and cannot be allowed to profit from its own illegal acts. <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#469" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 469, 471</a></span> (1928) (dissenting opinions); see <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#13" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 13</a></span> (1968). But the exclusionary rule does not ineluctably flow from a desire to ensure that government plays the "game" according to the rules. If an effective alternative remedy is available, concern for official observance of the law does not require adherence to the exclusionary rule. Nor is it easy to understand how a court can be thought to endorse a violation of the Fourth Amendment by allowing illegally seized evidence to be introduced against a defendant if an effective remedy is provided against the government.</p>
<p>The exclusionary rule has also been justified on the theory that the relationship between the Self-Incrimination Clause of the Fifth Amendment and the Fourth Amendment requires the suppression of evidence seized in violation of the latter. <i>Boyd</i> v. <i>United States, supra,</i> at 633 (dictum); <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#47" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 47, 48</a></span> (1949) (Rutledge, J., dissenting); <i>Mapp</i> v. <i>Ohio, supra,</i> at 661-666 (BLACK, J., concurring).</p>
<p>Even ignoring, however, the decisions of this Court that have held that the Fifth Amendment applies only to "testimonial" disclosures, <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#221" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 221-223</a></span> (1967); <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span>, 764 and n. 8 (1966), it seems clear that the Self-Incrimination Clause does not protect a person from the seizure of evidence that is incriminating. It protects a person only from being the conduit by which the police acquire evidence. Mr. Justice Holmes once put it succinctly, "A party is privileged from producing the <span class="star-pagination">*415</span> evidence but not from its production." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="97862"><a href="/opinion/97862/johnson-v-united-states/#458" aria-description="Citation for case: Johnson v. United States">228 U. S. 457, 458</a></span> (1913).</p>
<p>It is clear, however, that neither of these theories undergirds the decided cases in this Court. Rather the exclusionary rule has rested on the deterrent rationalethe hope that law enforcement officials would be deterred from unlawful searches and seizures if the illegally seized, albeit trustworthy, evidence was suppressed often enough and the courts persistently enough deprived them of any benefits they might have gained from their illegal conduct.</p>
<p>This evidentiary rule is unique to American jurisprudence. Although the English and Canadian legal systems are highly regarded, neither has adopted our rule. See Martin, The Exclusionary Rule Under Foreign Law Canada, 52 J. Crim. L. C. &amp; P. S. 271, 272 (1961); Williams, The Exclusionary Rule Under Foreign Law England, 52 J. Crim. L. C. &amp; P. S. 272 (1961).</p>
<p>I do not question the need for some remedy to give meaning and teeth to the constitutional guarantees against unlawful conduct by government officials. Without some effective sanction, these protections would constitute little more than rhetoric. Beyond doubt the conduct of some officials requires sanctions as cases like <i><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">Irvine</a></span></i> indicate. But the hope that this objective could be accomplished by the exclusion of reliable evidence from criminal trials was hardly more than a wistful dream. Although I would hesitate to abandon it until some meaningful substitute is developed, the history of the suppression doctrine demonstrates that it is both conceptually sterile and practically ineffective in accomplishing its stated objective. This is illustrated by the paradox that an unlawful act against a totally innocent personsuch as petitioner claims to behas been left without an effective remedy, and hence the Court finds <span class="star-pagination">*416</span> it necessary now55 years laterto construct a remedy of its own.</p>
<p>Some clear demonstration of the benefits and effectiveness of the exclusionary rule is required to justify it in view of the high price it extracts from societythe release of countless guilty criminals. See Allen, Federalism and the Fourth Amendment: A Requiem for Wolf, <span class="citation no-link">1961 Sup. Ct. Rev. 1</span>, 33 n. 172. But there is no empirical evidence to support the claim that the rule actually deters illegal conduct of law enforcement officials. Oaks, Studying the Exclusionary Rule in Search and Seizure, <span class="citation no-link">37 U. Chi. L. Rev. 665</span>, 667 (1970).</p>
<p>There are several reasons for this failure. The rule does not apply any direct sanction to the individual official whose illegal conduct results in the exclusion of evidence in a criminal trial. With rare exceptions law enforcement agencies do not impose direct sanctions on the individual officer responsible for a particular judicial application of the suppression doctrine. <i>Id.,</i> at 710. Thus there is virtually nothing done to bring about a change in his practices. The immediate sanction triggered by the application of the rule is visited upon the prosecutor whose case against a criminal is either weakened or destroyed. The doctrine deprives the police in no real sense; except that apprehending wrongdoers is their business, police have no more stake in successful prosecutions than prosecutors or the public.</p>
<p>The suppression doctrine vaguely assumes that law enforcement is a monolithic governmental enterprise. For example, the dissenters in <i>Wolf</i> v. <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#44" aria-description="Citation for case: Wolf v. Colorado"><i>Colorado, supra,</i> at 44</a></span>, argued that:</p>
<blockquote>"Only by exclusion can we impress upon the zealous <i>prosecutor</i> that violation of the Constitution will do him no good. And only when that point is driven home can the <i>prosecutor</i> be expected to emphasize <span class="star-pagination">*417</span> the importance of observing the constitutional demands in <i>his instructions to the police.</i>" (Emphasis added.)</blockquote>
<p>But the prosecutor who loses his case because of police misconduct is not an official in the police department; he can rarely set in motion any corrective action or administrative penalties. Moreover, he does not have control or direction over police procedures or police actions that lead to the exclusion of evidence. It is the rare exception when a prosecutor takes part in arrests, searches, or seizures so that he can guide police action.</p>
<p>Whatever educational effect the rule conceivably might have in theory is greatly diminished in fact by the realities of law enforcement work. Policemen do not have the time, inclination, or training to read and grasp the nuances of the appellate opinions that ultimately define the standards of conduct they are to follow. The issues that these decisions resolve often admit of neither easy nor obvious answers, as sharply divided courts on what is or is not "reasonable" amply demonstrate.<sup>[4]</sup> Nor can judges, in all candor, forget that opinions sometimes lack helpful clarity.</p>
<p>The presumed educational effect of judicial opinions is also reduced by the long time lapseoften several years between the original police action and its final judicial evaluation. Given a policeman's pressing responsibilities, it would be surprising if he ever becomes aware of the final result after such a delay. Finally, the exclusionary <span class="star-pagination">*418</span> rule's deterrent impact is diluted by the fact that there are large areas of police activity that do not result in criminal prosecutionshence the rule has virtually no applicability and no effect in such situations. Oaks, <i>supra,</i> at 720-724.</p>
<p>Today's holding seeks to fill one of the gaps of the suppression doctrineat the price of impinging on the legislative and policy functions that the Constitution vests in Congress. Nevertheless, the holding serves the useful purpose of exposing the fundamental weaknesses of the suppression doctrine. Suppressing unchallenged truth has set guilty criminals free but demonstrably has neither deterred deliberate violations of the Fourth Amendment nor decreased those errors in judgment that will inevitably occur given the pressures inherent in police work having to do with serious crimes.</p>
<p>Although unfortunately ineffective, the exclusionary rule has increasingly been characterized by a single, monolithic, and drastic judicial response to all official violations of legal norms. Inadvertent errors of judgment that do not work any grave injustice will inevitably occur under the pressure of police work. These honest mistakes have been treated in the same way as deliberate and flagrant <i><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">Irvine</a></span></i>-type violations of the Fourth Amendment. For example, in <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#309" aria-description="Citation for case: Miller v. United States">357 U. S. 301, 309-310</a></span> (1958), reliable evidence was suppressed because of a police officer's failure to say a "few more words" during the arrest and search of a known narcotics peddler.</p>
<p>This Court's decision announced today in <i>Coolidge</i> v. <i>New Hampshire, post,</i> p. 443, dramatically illustrates the extent to which the doctrine represents a mechanically inflexible response to widely varying degrees of police error and the resulting high price that society pays. I dissented in <i>Coolidge</i> primarily because I do not believe the Fourth Amendment had been violated. Even on the Court's contrary premise, however, whatever violation <span class="star-pagination">*419</span> occurred was surely insufficient in nature and extent to justify the drastic result dictated by the suppression doctrine. A fair trial by jury has resolved doubts as to Coolidge's guilt. But now his conviction on retrial is placed in serious question by the remand for a new trialyears after the crimein which evidence that the New Hampshire courts found relevant and reliable will be withheld from the jury's consideration. It is hardly surprising that such results are viewed with incomprehension by nonlawyers in this country and lawyers, judges, and legal scholars the world over.</p>
<p>Freeing either a tiger or a mouse in a schoolroom is an illegal act, but no rational person would suggest that these two acts should be punished in the same way. From time to time judges have occasion to pass on regulations governing police procedures. I wonder what would be the judicial response to a police order authorizing "shoot to kill" with respect to every fugitive. It is easy to predict our collective wrath and outrage. We, in common with all rational minds, would say that the police response must relate to the gravity and need; that a "shoot" order might conceivably be tolerable to prevent the escape of a convicted killer but surely not for a car thief, a pickpocket or a shoplifter.</p>
<p>I submit that society has at least as much right to expect rationally graded responses from judges in place of the universal "capital punishment" we inflict on all evidence when police error is shown in its acquisition. See ALI, Model Code of Pre-Arraignment Procedure § SS 8.02 (2), p. 23 (Tent. Draft No. 4, 1971), reprinted in the Appendix to this opinion. Yet for over 55 years, and with increasing scope and intensity as today's <i>Coolidge</i> holding shows, our legal system has treated vastly dissimilar cases as if they were the same. Our adherence to the exclusionary rule, our resistance to change, and our refusal even to acknowledge the need <span class="star-pagination">*420</span> for effective enforcement mechanisms bring to mind Holmes' well-known statement:</p>
<blockquote>"It is revolting to have no better reason for a rule of law than that so it was laid down in the time of Henry IV. It is still more revolting if the grounds upon which it was laid down have vanished long since, and the rule simply persists from blind imitation of the past." Holmes, The Path of the Law, <span class="citation no-link">10 Harv. L. Rev. 457</span>, 469 (1897).</blockquote>
<p>In characterizing the suppression doctrine as an anomalous and ineffective mechanism with which to regulate law enforcement, I intend no reflection on the motivation of those members of this Court who hoped it would be a means of enforcing the Fourth Amendment. Judges cannot be faulted for being offended by arrests, searches, and seizures that violate the Bill of Rights or statutes intended to regulate public officials. But we can and should be faulted for clinging to an unworkable and irrational concept of law. My criticism is that we have taken so long to find better ways to accomplish these desired objectives. And there are better ways.</p>
<p>Instead of continuing to enforce the suppression doctrine inflexibly, rigidly, and mechanically, we should view it as one of the experimental steps in the great tradition of the common law and acknowledge its shortcomings. But in the same spirit we should be prepared to discontinue what the experience of over half a century has shown neither deters errant officers nor affords a remedy to the totally innocent victims of official misconduct.</p>
<p>I do not propose, however, that we abandon the suppression doctrine until some meaningful alternative can be developed. In a sense our legal system has become the captive of its own creation. To overrule <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> and <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i><i>,</i> even assuming the Court was now prepared to <span class="star-pagination">*421</span> take that step, could raise yet new problems. Obviously the public interest would be poorly served if law enforcement officials were suddenly to gain the impression, however erroneous, that all constitutional restraints on police had somehow been removedthat an open season on "criminals" had been declared. I am concerned lest some such mistaken impression might be fostered by a flat overruling of the suppression doctrine cases. For years we have relied upon it as the exclusive remedy for unlawful official conduct; in a sense we are in a situation akin to the narcotics addict whose dependence on drugs precludes any drastic or immediate withdrawal of the supposed prop, regardless of how futile its continued use may be.</p>
<p>Reasonable and effective substitutes can be formulated if Congress would take the lead, as it did for example in 1946 in the Federal Tort Claims Act. I see no insuperable obstacle to the elimination of the suppression doctrine if Congress would provide some meaningful and effective remedy against unlawful conduct by government officials.</p>
<p>The problems of both error and deliberate misconduct by law enforcement officials call for a workable remedy. Private damage actions against individual police officers concededly have not adequately met this requirement, and it would be fallacious to assume today's work of the Court in creating a remedy will really accomplish its stated objective. There is some validity to the claims that juries will not return verdicts against individual officers except in those unusual cases where the violation has been flagrant or where the error has been complete, as in the arrest of the wrong person or the search of the wrong house. There is surely serious doubt, for example, that a drug peddler caught packaging his wares will be able to arouse much sympathy in a jury on the ground that the police officer did not announce his identity and <span class="star-pagination">*422</span> purpose fully or because he failed to utter a "few more words." See <i>Miller</i> v. <i>United States, supra</i><i>.</i> Jurors may well refuse to penalize a police officer at the behest of a person they believe to be a "criminal" and probably will not punish an officer for honest errors of judgment. In any event an actual recovery depends on finding nonexempt assets of the police officer from which a judgment can be satisfied.</p>
<p>I conclude, therefore, that an entirely different remedy is necessary but it is one that in my view is as much beyond judicial power as the step the Court takes today. Congress should develop an administrative or quasijudicial remedy against the government itself to afford compensation and restitution for persons whose Fourth Amendment rights have been violated. The venerable doctrine of <i>respondeat superior</i> in our tort law provides an entirely appropriate conceptual basis for this remedy. If, for example, a security guard privately employed by a department store commits an assault or other tort on a customer such as an improper search, the victim has a simple and obvious remedyan action for money damages against the guard's employer, the department store. W. Prosser, The Law of Torts § 68, pp. 470-480 (3d ed. 1964).<sup>[5]</sup> Such a statutory scheme would have the added advantage of providing some remedy to the completely innocent persons who are sometimes the victims of illegal police conductsomething that the suppression doctrine, of course, can never accomplish.</p>
<p>A simple structure would suffice.<sup>[6]</sup> For example, Congress could enact a statute along the following lines:</p>
<p>(a) a waiver of sovereign immunity as to the illegal <span class="star-pagination">*423</span> acts of law enforcement officials committed in the performance of assigned duties;</p>
<p>(b) the creation of a cause of action for damages sustained by any person aggrieved by conduct of governmental agents in violation of the Fourth Amendment or statutes regulating official conduct;</p>
<p>(c) the creation of a tribunal, quasi-judicial in nature or perhaps patterned after the United States Court of Claims, to adjudicate all claims under the statute;</p>
<p>(d) a provision that this statutory remedy is in lieu of the exclusion of evidence secured for use in criminal cases in violation of the Fourth Amendment; and</p>
<p>(e) a provision directing that no evidence, otherwise admissible, shall be excluded from any criminal proceeding because of violation of the Fourth Amendment.</p>
<p>I doubt that lawyers serving on such a tribunal would be swayed either by undue sympathy for officers or by the prejudice against "criminals" that has sometimes moved lay jurors to deny claims. In addition to awarding damages, the record of the police conduct that is condemned would undoubtedly become a relevant part of an officer's personnel file so that the need for additional training or disciplinary action could be identified or his future usefulness as a public official evaluated. Finally, appellate judicial review could be made available on much the same basis that it is now provided as to district courts and regulatory agencies. This would leave to the courts the ultimate responsibility for determining and articulating standards.</p>
<p>Once the constitutional validity of such a statute is established,<sup>[7]</sup> it can reasonably be assumed that the States <span class="star-pagination">*424</span> would develop their own remedial systems on the federal model. Indeed there is nothing to prevent a State from enacting a comparable statutory scheme without waiting for the Congress. Steps along these lines would move our system toward more responsible law enforcement on the one hand and away from the irrational and drastic results of the suppression doctrine on the other. Independent of the alternative embraced in this dissenting opinion, I believe the time has come to re-examine the scope of the exclusionary rule and consider at least some narrowing of its thrust so as to eliminate the anomalies it has produced.</p>
<p>In a country that prides itself on innovation, inventive genius, and willingness to experiment, it is a paradox that we should cling for more than a half century to a legal mechanism that was poorly designed and never really worked. I can only hope now that the Congress will manifest a willingness to view realistically the hard evidence of the half-century history of the suppression doctrine revealing thousands of cases in which the criminal was set free because the constable blundered and virtually no evidence that innocent victims of police error such as petitioner claims to behave been afforded meaningful redress.</p>
<p></p>
<h2>APPENDIX TO OPINION OF BURGER, C. J., DISSENTING</h2>
<p>It is interesting to note that studies over a period of years led the American Law Institute to propose the following in its tentative draft of a model pre-arraignment code:</p>
<blockquote>"(2) <i>Determination.</i> Unless otherwise required by the Constitution of the United States or of this State, a motion to suppress evidence based upon a <span class="star-pagination">*425</span> violation of any of the provisions of this code shall be granted <i>only if the court finds that such violation was substantial.</i> In determining whether a violation is substantial the court shall consider all the circumstances, including:</blockquote>
<blockquote>"(a) the importance of the particular interest violated;</blockquote>
<blockquote>"(b) the extent of deviation from lawful conduct;</blockquote>
<blockquote>"(c) the extent to which the violation was willful;</blockquote>
<blockquote>"(d) the extent to which privacy was invaded;</blockquote>
<blockquote>"(e) the extent to which exclusion will tend to prevent violations of this Code;</blockquote>
<blockquote>"(f) whether, but for the violation, the things seized would have been discovered; and</blockquote>
<blockquote>"(g) the extent to which the violation prejudiced the moving party's ability to support his motion, or to defend himself in the proceeding in which the things seized are sought to be offered in evidence against him.</blockquote>
<blockquote>"(3) <i>Fruits of Prior Unlawful Search.</i> If a search or seizure is carried out in such a manner that things seized in the course of the search would be subject to a motion to suppress under subsection (1), and if as a result of such search or seizure other evidence is discovered subsequently and offered against a defendant, such evidence shall be subject to a motion to suppress unless the prosecution establishes that such evidence would probably have been discovered by law enforcement authorities irrespective of such search or seizure, and the court finds that exclusion of such evidence is not necessary to deter violations of this Code."</blockquote>
<p>ALI, Model Code of Pre-Arraignment Procedure §§ SS 8.02 (2), (3), pp. 23-24 (Tent. Draft No. 4, 1971) (emphasis supplied).</p>
<p><span class="star-pagination">*426</span> The Reporters' views on the exclusionary rule are also reflected in their comment on the proposed section:</p>
<blockquote>"The Reporters wish to emphasize that they are not, as a matter of policy, wedded to the exclusionary rule as the sole or best means of enforcing the Fourth Amendment. See Oaks, <i>Studying the Exclusionary Rule in Search and Seizure,</i> 37 U. of Chi. L. Rev. 665 (1970). Paragraph (2) embodies what the Reporters hope is a more flexible approach to the problem, subject of course to constitutional requirements." <i>Id.,</i> comment, at 26-27.</blockquote>
<p>This is but one of many expressions of disenchantment with the exclusionary rule; see also:</p>
<p>1. Barrett, Exclusion of Evidence Obtained by Illegal SearchesA Comment on People vs. Cahan, <span class="citation no-link">43 Calif. L. Rev. 565</span> (1955).</p>
<p>2. Burns, <i>Mapp</i> v. <i>Ohio:</i> An All-American Mistake, <span class="citation no-link">19 DePaul L. Rev. 80</span> (1969).</p>
<p>3. Friendly, The Bill of Rights as a Code of Criminal Procedure, <span class="citation no-link">53 Calif. L. Rev. 929</span>, 951-954 (1965).</p>
<p>4. F. Inbau, J. Thompson, &amp; C. Sowle, Cases and Comments on Criminal Justice: Criminal Law Administration 1-84 (3d ed. 1968).</p>
<p>5. LaFave, Improving Police Performance Through the Exclusionary Rule (pts. 1 &amp; 2), <span class="citation no-link">30 Mo. L. Rev. 391</span>, 566 (1965).</p>
<p>6. LaFave &amp; Remington, Controlling the Police: The Judge's Role in Making and Reviewing Law Enforcement Decisions, <span class="citation no-link">63 Mich. L. Rev. 987</span> (1965).</p>
<p>7. N. Morris &amp; G. Hawkins, The Honest Politician's Guide to Crime Control 101 (1970).</p>
<p>8. Oaks, Studying the Exclusionary Rule in Search and Seizure, <span class="citation no-link">37 U. Chi. L. Rev. 665</span> (1970).</p>
<p><span class="star-pagination">*427</span> 9. Plumb, Illegal Enforcement of the Law, 24 Cornell L. Q. 337 (1939).</p>
<p>10. Schaefer, The Fourteenth Amendment and Sanctity of the Person, <span class="citation no-link">64 Nw. U. L. Rev. 1</span> (1969).</p>
<p>11. Waite, Judges and the Crime Burden, <span class="citation no-link">54 Mich. L. Rev. 169</span> (1955).</p>
<p>12. Waite, EvidencePolice Regulation by Rules of Evidence, <span class="citation no-link">42 Mich. L. Rev. 679</span> (1944).</p>
<p>13. Wigmore, Using Evidence Obtained by Illegal Search and Seizure, 8 A. B. A. J. 479 (1922).</p>
<p>14. 8 J. Wigmore, Evidence § 2184a (McNaughton rev. 1961).</p>
<p>MR. JUSTICE BLACK, dissenting.</p>
<p>In my opinion for the Court in <i>Bell</i> v. <i>Hood,</i> <span class="citation" data-id="9419809"><a href="/opinion/104272/bell-v-hood/" aria-description="Citation for case: Bell v. Hood">327 U. S. 678</a></span> (1946), we did as the Court states, reserve the question whether an unreasonable search made by a federal officer in violation of the Fourth Amendment gives the subject of the search a federal cause of action for damages against the officers making the search. There can be no doubt that Congress could create a federal cause of action for damages for an unreasonable search in violation of the Fourth Amendment. Although Congress has created such a federal cause of action against <i>state</i> officials acting under color of state law,<sup>[*]</sup> it has never created such a cause of action against federal officials. If it wanted to do so, Congress could, of course, create a remedy against <span class="star-pagination">*428</span> federal officials who violate the Fourth Amendment in the performance of their duties. But the point of this case and the fatal weakness in the Court's judgment is that neither Congress nor the State of New York has enacted legislation creating such a right of action. For us to do so is, in my judgment, an exercise of power that the Constitution does not give us.</p>
<p>Even if we had the legislative power to create a remedy, there are many reasons why we should decline to create a cause of action where none has existed since the formation of our Government. The courts of the United States as well as those of the States are choked with lawsuits. The number of cases on the docket of this Court have reached an unprecedented volume in recent years. A majority of these cases are brought by citizens with substantial complaintspersons who are physically or economically injured by torts or frauds or governmental infringement of their rights; persons who have been unjustly deprived of their liberty or their property; and persons who have not yet received the equal opportunity in education, employment, and pursuit of happiness that was the dream of our forefathers. Unfortunately, there have also been a growing number of frivolous lawsuits, particularly actions for damages against law enforcement officers whose conduct has been judicially sanctioned by state trial and appellate courts and in many instances even by this Court. My fellow Justices on this Court and our brethren throughout the federal judiciary know only too well the time-consuming task of conscientiously poring over hundreds of thousands of pages of factual allegations of misconduct by police, judicial, and corrections officials. Of course, there are instances of legitimate grievances, but legislators might well desire to devote judicial resources to other problems of a more serious nature.</p>
<p><span class="star-pagination">*429</span> We sit at the top of a judicial system accused by some of nearing the point of collapse. Many criminal defendants do not receive speedy trials and neither society nor the accused are assured of justice when inordinate delays occur. Citizens must wait years to litigate their private civil suits. Substantial changes in correctional and parole systems demand the attention of the lawmakers and the judiciary. If I were a legislator I might well find these and other needs so pressing as to make me believe that the resources of lawyers and judges should be devoted to them rather than to civil damage actions against officers who generally strive to perform within constitutional bounds. There is also a real danger that such suits might deter officials from the <i>proper</i> and honest performance of their duties.</p>
<p>All of these considerations make imperative careful study and weighing of the arguments both for and against the creation of such a remedy under the Fourth Amendment. I would have great difficulty for myself in resolving the competing policies, goals, and priorities in the use of resources, if I thought it were my job to resolve those questions. But that is not my task. The task of evaluating the pros and cons of creating judicial remedies for particular wrongs is a matter for Congress and the legislatures of the States. Congress has not provided that any federal court can entertain a suit against a federal officer for violations of Fourth Amendment rights occurring in the performance of his duties. A strong inference can be drawn from creation of such actions against state officials that Congress does not desire to permit such suits against federal officials. Should the time come when Congress desires such lawsuits, it has before it a model of valid legislation, <span class="citation no-link">42 U. S. C. § 1983</span>, to create a damage remedy against federal officers. Cases could be cited to support the legal proposition which <span class="star-pagination">*430</span> I assert, but it seems to me to be a matter of common understanding that the business of the judiciary is to interpret the laws and not to make them.</p>
<p>I dissent.</p>
<p>MR. JUSTICE BLACKMUN, dissenting.</p>
<p>I, too, dissent. I do so largely for the reasons expressed in Chief Judge Lumbard's thoughtful and scholarly opinion for the Court of Appeals. But I also feel that the judicial legislation, which the Court by its opinion today concededly is effectuating, opens the door for another avalanche of new federal cases. Whenever a suspect imagines, or chooses to assert, that a Fourth Amendment right has been violated, he will now immediately sue the federal officer in federal court. This will tend to stultify proper law enforcement and to make the day's labor for the honest and conscientious officer even more onerous and more critical. Why the Court moves in this direction at this time of our history, I do not know. The Fourth Amendment was adopted in 1791, and in all the intervening years neither the Congress nor the Court has seen fit to take this step. I had thought that for the truly aggrieved person other quite adequate remedies have always been available. If not, it is the Congress and not this Court that should act.</p>
<h2>NOTES</h2>
<p>[1]  Petitioner's complaint does not explicitly state that the agents had no probable cause for his arrest, but it does allege that the arrest was "done unlawfully, unreasonably and contrary to law." App. 2. Petitioner's affidavit in support of his motion for summary judgment swears that the search was "without cause, consent or warrant," and that the arrest was "without cause, reason or warrant." App. 28.</p>
<p>[2]  The agents were not named in petitioner's complaint, and the District Court ordered that the complaint be served upon "those federal agents who it is indicated by the records of the United States Attorney participated in the November 25, 1965, arrest of the [petitioner]." App. 3. Five agents were ultimately served.</p>
<p>[3]  Judge Waterman, concurring, expressed the thought that "the federal courts can . . . entertain this cause of action irrespective of whether a statute exists specifically authorizing a federal suit against federal officers for damages" for acts such as those alleged. In his view, however, the critical point was recognition that some cause of action existed, albeit a state-created one, and in consequence he was willing <i>"as of now"</i> to concur in the holding of the Court of Appeals. <span class="citation" data-id="9454464"><a href="/opinion/284380/webster-bivens-v-six-unknown-named-agents-of-the-federal-bureau-of/#726" aria-description="Citation for case: Webster Bivens v. Six Unknown Named Agents of the Federal...">409 F. 2d, at 726</a></span> (emphasis in original).</p>
<p>[4]  "[S]ince it is the present policy of the Department of Justice to remove to the federal courts all suits in state courts against federal officers for trespass or false imprisonment, a claim for relief, whether based on state common law or directly on the Fourth Amendment, will ultimately be heard in a federal court." Brief for Respondents 13 (citations omitted); see <span class="citation no-link">28 U. S. C. § 1442</span> (a); <i>Willingham</i> v. <i>Morgan,</i> <span class="citation" data-id="9424070"><a href="/opinion/107963/willingham-v-morgan/" aria-description="Citation for case: Willingham v. Morgan">395 U. S. 402</a></span> (1969). In light of this, it is difficult to understand our Brother BLACKMUN'S complaint that our holding today "opens the door for another avalanche of new federal cases." <i>Post,</i> at 430. In estimating the magnitude of any such "avalanche," it is worth noting that a survey of comparable actions against state officers under <span class="citation no-link">42 U. S. C. § 1983</span> found only 53 reported cases in 17 years (1951-1967) that survived a motion to dismiss. Ginger &amp; Bell, Police Misconduct LitigationPlaintiff's Remedies, 15 Am. Jur. Trials 555, 580-590 (1968). Increasing this figure by 900% to allow for increases in rate and unreported cases, every federal district judge could expect to try one such case every 13 years.</p>
<p>[5]  New York at that time followed the common-law rule that a private person may arrest another if the latter has in fact committed a felony, and that if such is the case the presence or absence of probable cause is irrelevant to the legality of the arrest. See <i>McLoughlin</i> v. <i>New York Edison Co.,</i> <span class="citation" data-id="3576215"><a href="/opinion/3595140/mcloughlin-v-new-york-edison-co/" aria-description="Citation for case: McLoughlin v. New York Edison Co.">252 N. Y. 202</a></span>, <span class="citation" data-id="3576215"><a href="/opinion/3595140/mcloughlin-v-new-york-edison-co/" aria-description="Citation for case: McLoughlin v. New York Edison Co.">169 N. E. 277</a></span> (1929): cf. N. Y. Code Crim. Proc. § 183 (1958) for codification of the rule. Conspiracy to commit a federal crime was at the time a felony. Act of March 4, 1909, § 37, <span class="citation no-link">35 Stat. 1096</span>.</p>
<p>[6]  Conversely, we have in some instances rejected Fourth Amendment claims despite facts demonstrating that federal agents were acting in violation of local law. <i>McGuire</i> v. <i>United States,</i> <span class="citation" data-id="100989"><a href="/opinion/100989/mcguire-v-united-states/" aria-description="Citation for case: McGuire v. United States">273 U. S. 95</a></span> (1927) (trespass <i>ab initio</i>); <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924) ("open fields" doctrine); cf. <i>Burdeau</i> v. <i>McDowell,</i> <span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465</a></span> (1921) (possession of stolen property).</p>
<p>[7]  Similarly, although the Fourth Amendment confines an officer executing a search warrant strictly within the bounds set by the warrant, <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 196</a></span> (1927); see <i>Stanley</i> v. <i>Georgia,</i> <span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/#570" aria-description="Citation for case: Stanley v. Georgia">394 U. S. 557, 570-572</a></span> (1969) (STEWART, J., concurring in result), a private individual lawfully in the home of another will not normally be liable for trespass beyond the bounds of his invitation absent clear notice to that effect. See 1 F. Harper &amp; F. James, The Law of Torts § 1.11 (1956).</p>
<p>[8]  Although no State has undertaken to limit the common-law doctrine that one may use reasonable force to resist an unlawful arrest by a private person, at least two States have outlawed resistance to an unlawful arrest sought to be made by a person known to be an officer of the law. R. I. Gen. Laws § 12-7-10 (1969); <i>State</i> v. <i>Koonce,</i> 89 N. J. Super. 169, 180-184, <span class="citation" data-id="1518638"><a href="/opinion/1518638/state-v-koonce/#433" aria-description="Citation for case: State v. Koonce">214 A. 2d 428, 433-436</a></span> (1965).</p>
<p>[1]  Petitioner also asserted federal jurisdiction under <span class="citation no-link">42 U. S. C. § 1983</span> and <span class="citation no-link">28 U. S. C. § 1343</span> (3), and <span class="citation no-link">28 U. S. C. § 1343</span> (4). Neither will support federal jurisdiction over the claim. See <i>Bivens</i> v. <i>Six Unknown Named Agents,</i> <span class="citation" data-id="9454464"><a href="/opinion/284380/webster-bivens-v-six-unknown-named-agents-of-the-federal-bureau-of/" aria-description="Citation for case: Webster Bivens v. Six Unknown Named Agents of the Federal...">409 F. 2d 718</a></span>, 720 n. 1 (CA2 1969).</p>
<p>[2]  See n. 3, <i>infra.</i></p>
<p>[3]  The Government appears not quite ready to concede this point. Certain points in the Government's argument seem to suggest that the "state-created rightfederal defense" model reaches not only the question of the power to accord a federal damages remedy, but also the claim to any judicial remedy in any court. Thus, we are pointed to Lasson's observation concerning Madison's version of the Fourth Amendment as introduced into the House:
</p>
<p>"The observation may be made that the language of the proposal did not purport to <i>create</i> the right to be secure from unreasonable search and seizures but merely stated it as a right which already existed."</p>
<p>N. Lasson, History and Development of the Fourth Amendment to the United States Constitution 100 n. 77 (1937), quoted in Brief for Respondents 11 n. 7. And, on the problem of federal equitable vindication of constitutional rights without regard to the presence of a "state-created right," see Hart, The Relations Between State and Federal Law, 54 Col. L. Rev. 489, 523-524 (1954), quoted in Brief for Respondents 17.</p>
<p>On this point, the choice of phraseology in the Fourth Amendment itself is singularly unpersuasive. The leading argument against a "Bill of Rights" was the fear that individual liberties not specified expressly would be taken as excluded. See generally, Lasson, <i>supra,</i> at 79-105. This circumstance alone might well explain why the authors of the Bill of Rights would opt for language which presumes the existence of a fundamental interest in liberty, albeit originally derived from the common law. See <i>Entick</i> v. <i>Carrington,</i> 19 How. St. Tr. 1029, 95 Eng. Rep. 807 (1765).</p>
<p>In truth, the legislative record as a whole behind the Bill of Rights is silent on the rather refined doctrinal question whether the framers considered the rights therein enumerated as dependent in the first instance on the decision of a State to accord legal status to the personal interests at stake. That is understandable since the Government itself points out that general federal-question jurisdiction was not extended to the federal district courts until 1875. Act of March 3, 1875, § 1, <span class="citation no-link">18 Stat. 470</span>. The most that can be drawn from this historical fact is that the authors of the Bill of Rights assumed the adequacy of common-law remedies to vindicate the federally protected interest. One must first combine this assumption with contemporary modes of jurisprudential thought which appeared to link "rights" and "remedies" in a 1:1 correlation, cf. <i>Marbury</i> v. <i>Madison,</i> <span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/#163" aria-description="Citation for case: Marbury v. Madison">1 Cranch 137, 163</a></span> (1803), before reaching the conclusion that the framers are to be understood today as having created no federally protected interests. And, of course, that would simply require the conclusion that federal equitable relief would not lie to protect those interests guarded by the Fourth Amendment.</p>
<p>Professor Hart's observations concerning the "imperceptible steps" between <i>In re Ayers,</i> <span class="citation" data-id="9417465"><a href="/opinion/92059/in-re-ayers/" aria-description="Citation for case: In Re Ayers">123 U. S. 443</a></span> (1887), and <i>Ex parte Young,</i> <span class="citation" data-id="9418117"><a href="/opinion/96819/ex-parte-young/" aria-description="Citation for case: Ex Parte Young">209 U. S. 123</a></span> (1908), see Hart, <i>supra,</i> fail to persuade me that the source of the legal interest asserted here is other than the Federal Constitution itself. <i>In re Ayers</i> concerned the precise question whether the Eleventh Amendment barred suit in a federal court for an injunction compelling a state officer to perform a contract to which the State was a party. Having concluded that the suit was inescapably a suit against the State under the Eleventh Amendment, the Court spoke of the presence of state-created rights as a distinguishing factor supporting the exercise of federal jurisdiction in other contract clause cases. The absence of a state-created right in <i>In re Ayers</i> served to distinguish that case from the perspective of the State's immunity to suit; <i><span class="citation" data-id="9417465"><a href="/opinion/92059/in-re-ayers/" aria-description="Citation for case: In Re Ayers">Ayers</a></span></i> simply does not speak to the analytically distinct question whether the Constitution is in the relevant sense a source of legal protection for the "rights" enumerated therein.</p>
<p>[4]  The <i><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">Borak</a></span></i> case is an especially clear example of the exercise of federal judicial power to accord damages as an appropriate remedy in the absence of any express statutory authorization of a federal cause of action. There we "implied"from what can only be characterized as an "exclusively procedural provision" affording access to a federal forum, cf. <i>Textile Workers</i> v. <i>Lincoln Mills,</i> <span class="citation" data-id="9421446"><a href="/opinion/105511/textile-workers-v-lincoln-mills-of-ala/#462" aria-description="Citation for case: Textile Workers v. Lincoln Mills of Ala.">353 U. S. 448, 462-463</a></span> (1957) (Frankfurter, J., dissenting)a private cause of action for damages for violation of § 14 (a) of the Securities Exchange Act of 1934, <span class="citation no-link">48 Stat. 895</span>, 15 U. S. C. § 78n (a). See § 27, <span class="citation no-link">48 Stat. 902</span>, 15 U. S. C. § 78aa. We did so in an area where federal regulation has been singularly comprehensive and elaborate administrative enforcement machinery had been provided. The exercise of judicial power involved in <i><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">Borak</a></span></i> simply cannot be justified in terms of statutory construction, see Hill, Constitutional Remedies, 69 Col. L. Rev. 1109, 1120-1121 (1969); nor did the <i><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">Borak</a></span></i> Court purport to do so. See <span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/#432" aria-description="Citation for case: J. I. Case Co. v. Borak"><i>Borak, supra,</i> at 432-434</a></span>. The notion of "implying" a remedy, therefore, as applied to cases like <i><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">Borak</a></span></i><i>,</i> can only refer to a process whereby the federal judiciary exercises a choice among <i>traditionally available</i> judicial remedies according to reasons related to the substantive social policy embodied in an act of positive law. See <i>ibid.,</i> and <i>Bell</i> v. <span class="citation" data-id="9419809"><a href="/opinion/104272/bell-v-hood/#684" aria-description="Citation for case: Bell v. Hood"><i>Hood, supra,</i> at 684</a></span>.</p>
<p>[5]  With regard to a court's authority to grant an equitable remedy, the line between "subject matter" jurisdiction and remedial powers has undoubtedly been obscured by the fact that historically the "system of equity `derived its doctrines, as well as its powers, from its mode of giving relief.' " See <i>Guaranty Trust Co.</i> v. <i>York, supra,</i> at 105, quoting C. Langdell, Summary of Equity Pleading xxvii (1877). Perhaps this fact alone accounts for the suggestion sometimes made that a court's power to enjoin invasion of constitutionally protected interests derives directly from the Constitution. See <i>Bell</i> v. <i>Hood,</i> <span class="citation" data-id="1674567"><a href="/opinion/1674567/bell-v-hood/#819" aria-description="Citation for case: Bell v. Hood">71 F. Supp. 813, 819</a></span> (SD Cal. 1947).</p>
<p>[6]  Chief Judge Lumbard's opinion for the Court of Appeals in the instant case is, as I have noted, in accord with this conclusion:
</p>
<p>"Thus, even if the Constitution itself does not give rise to an inherent injunctive power to prevent its violation by governmental officials there are strong reasons for inferring the existence of this power under any general grant of jurisdiction to the federal courts by Congress." <span class="citation" data-id="9454464"><a href="/opinion/284380/webster-bivens-v-six-unknown-named-agents-of-the-federal-bureau-of/#723" aria-description="Citation for case: Webster Bivens v. Six Unknown Named Agents of the Federal...">409 F. 2d, at 723</a></span>.</p>
<p>The description of the remedy as "inferred" cannot, of course, be intended to assimilate the judicial decision to accord such a remedy to any process of statutory construction. Rather, as with the cases concerning remedies, implied from statutory schemes, see n. 4, <i>supra,</i> the description of the remedy as "inferred" can only bear on the reasons offered to explain a judicial decision to accord or not to accord a particular remedy.</p>
<p>[7]  I express no view on the Government's suggestion that congressional authority to simply discard the remedy the Court today authorizes might be in doubt; nor do I understand the Court's opinion today to express any view on that particular question.</p>
<p>[8]  And I think it follows from this point that today's decision has little, if indeed any, bearing on the question whether a federal court may properly devise remediesother than traditionally available forms of judicial relieffor the purpose of enforcing substantive social policies embodied in constitutional or statutory policies. Compare today's decision with <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), and <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914). The Court today simply recognizes what has long been implicit in our decisions concerning equitable relief and remedies implied from statutory schemes; <i>i. e.,</i> that a court of law vested with jurisdiction over the subject matter of a suit has the powerand therefore the dutyto make principled choices among traditional judicial remedies. Whether special prophylactic measureswhich at least arguably the exclusionary rule exemplifies, see Hill, The Bill of Rights and the Supervisory Power, 69 Col. L. Rev. 181, 182-185 (1969)are supportable on grounds other than a court's competence to select among traditional judicial remedies to make good the wrong done, cf. <i>Bell</i> v. <i>Hood, supra,</i> at 684, is a separate question.</p>
<p>[9]  The same, of course, may not be true with respect to other types of constitutionally protected interests, and therefore the appropriateness of money damages may well vary with the nature of the personal interest asserted. See <i>Monroe</i> v. <i>Pape,</i> <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167</a></span>, 196 n. 5 (HARLAN, J., concurring).</p>
<p>[1]  J. Thayer, O. Holmes, &amp; F. Frankfurter, John Marshall 88 (Phoenix ed. 1967).</p>
<p>[2]  The Court reached the issue of applying the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine to the States <i>sua sponte.</i></p>
<p>[3]  What Cardozo suggested as an example of the potentially far-reaching consequences of the suppression doctrine was almost realized in <i>Killough</i> v. <i>United States,</i> 114 U. S. App. D. C. 305, <span class="citation" data-id="9449118"><a href="/opinion/260072/james-w-killough-v-united-states/" aria-description="Citation for case: James W. Killough v. United States">315 F. 2d 241</a></span> (1962).</p>
<p>[4]  For example, in a case arising under <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp, supra</a></span></i><i>,</i> state judges at every level of the state judiciary may find the police conduct proper. On federal habeas corpus a district judge and a court of appeals might agree. Yet, in these circumstances, this Court, reviewing the case as much as 10 years later, might reverse by a narrow margin. In these circumstances it is difficult to conclude that the policeman has violated some rule that he should have known was a restriction on his authority.</p>
<p>[5]  Damage verdicts for such acts are often sufficient in size to provide an effective deterrent and stimulate employers to corrective action.</p>
<p>[6]  Electronic eavesdropping presents special problems. See <span class="citation no-link">18 U. S. C. §§ 2510-2520</span> (1964 ed., Supp. V).</p>
<p>[7]  Any such legislation should emphasize the interdependence between the waiver of sovereign immunity and the elimination of the judicially created exclusionary rule so that if the legislative determination to repudiate the exclusionary rule falls, the entire statutory scheme would fall.</p>
<p>[*]  "Every person who, under color of any statute, ordinance, regulation, custom, or usage, of any State or Territory, subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress." Rev. Stat. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>.</p>

</div>
```

---

## GROUP: content/cases/Board of County Commissioners of Bryan County v. Brown.md  (`case`, 5 assertions)

### content_page

```
---
title: Board of County Commissioners of Bryan County v. Brown
type: case
citation: "520 U.S. 397 (1997)"
parallel_cite: "117 S. Ct. 1382; 137 L. Ed. 2d 626; 65 U.S.L.W. 4286; 10 Fla. L. Weekly Fed. S 405; 12 I.E.R. Cas. (BNA) 1217; 97 Daily Journal DAR 5311"
neutral_cite: "1997 U.S. LEXIS 2793; 97 Cal. Daily Op. Serv. 3033"
court: U.S.
court_level: scotus
circuit: ""
year: 1997
date_decided: 1997-04-28
docket: 95-1100
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
  opinion_url: "https://www.courtlistener.com/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/"
  cluster_id: 118104
  opinion_id: null
  identity_checked: true
lake:
  record_id: Board of County Commissioners of Bryan County v. Brown
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Anchor
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Monell v. Department of Social Services]]"
tags:
  - case
  - section-1983
  - municipal-liability
  - monell
  - deliberate-indifference
  - failure-to-screen
holding: "A single municipal hiring decision can support § 1983 liability only on a stringent showing of deliberate indifference: the plaintiff must prove that adequate scrutiny of the applicant's background would have made the plainly obvious consequence of hiring him the specific constitutional injury the plaintiff suffered."
aliases:
  - Board of County Commissioners of Bryan County v. Brown
  - Bryan County v. Brown
  - "Board of County Commissioners of Bryan County v. Brown (1997)"
---

# Board of County Commissioners of Bryan County v. Brown

*520 U.S. 397 (1997)* (No. 95-1100) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 118104 → combined opinion 118104 (O'Connor, J.; 520 U.S. 397, decided Apr. 28, 1997). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*411`). S9 promotes. -->

## Background
Sheriff B.J. Moore of Bryan County, Oklahoma, hired his great-nephew, Stacy Burns, as a reserve deputy without reviewing the specifics of Burns's record, which included guilty pleas to assault and battery, resisting arrest, and various driving offenses. During a high-speed stop, Burns used an "arm bar" technique to pull Jill Brown from a truck, severely injuring her knees. Brown sued the County under 42 U.S.C. § 1983, contending that Sheriff Moore's decision to hire Burns without adequate screening was itself the municipal "policy" that caused her injury — a single-decision theory of *[[Monell v. Department of Social Services|Monell]]* liability. A jury found the County liable, and the Fifth Circuit affirmed.

## Issue
Whether a county may be held liable under § 1983 for a single hiring decision, on the theory that an official's inadequate scrutiny of the applicant's background caused a third party's constitutional injury.

## Rule
Municipal liability may not rest on *[[Common Legal Terms#respondeat-superior|respondeat superior]]*; a single facially lawful hiring decision can be the "moving force" behind an injury only under a rigorous culpability-and-causation standard. Stating that standard, the Court held: "A plaintiff must demonstrate that a municipal decision reflects deliberate indifference to the risk that a violation of a particular constitutional or statutory right will follow the decision." — 520 U.S. at 411. ^pin-411

## Application
Even assuming Sheriff Moore's screening of Burns was inadequate, that showed at most a generalized risk that an unfit officer might someday violate someone's rights — not [[Section 1983 Liability and Qualified Immunity|deliberate indifference]] to the risk of *this* injury. Liability required proof that a full review of Burns's background would have made his use of excessive force a "plainly obvious consequence" of hiring him. Burns's record of misdemeanors did not meet that bar, so the causal link between the hiring decision and Brown's specific injury was too weak to support municipal liability.

## Conclusion
The judgment was **reversed**. O'Connor, J., delivered the opinion of the Court (5–4); Souter, J. (joined by Stevens and Breyer, JJ.), and Breyer, J. (joined by Stevens and Ginsburg, JJ.), dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Bryan County* extends *[[City of Canton v. Harris]]*'s deliberate-indifference standard to hiring and, together with *[[Monell v. Department of Social Services|Monell]]*, makes single-incident municipal liability exceptionally hard to prove: the plaintiff must connect the specific applicant's known background to the specific violation as a "plainly obvious" consequence. Teach it as the outer limit of *[[Monell v. Department of Social Services|Monell]]* "policy" liability.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Anchor*

## Sources
- [*Board of County Commissioners of Bryan County v. Brown*, 520 U.S. 397 (1997)](https://www.courtlistener.com/opinion/118104/board-of-county-commissioners-of-bryan-county-v-brown/) — pinpoint: 411 (O'Connor, J., for the Court; the CL opinion text carries the reporter star `*411` in the paragraph stating the standard). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b53dabc8c909f082", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "520 U.S. 397 (1997)", "court": "U.S.", "neutral_cite": "1997 U.S. LEXIS 2793; 97 Cal. Daily Op. Serv. 3033", "official_citation_present": true, "parallel_cite": "117 S. Ct. 1382; 137 L. Ed. 2d 626; 65 U.S.L.W. 4286; 10 Fla. L. Weekly Fed. S 405; 12 I.E.R. Cas. (BNA) 1217; 97 Daily Journal DAR 5311", "title": "Board of County Commissioners of Bryan County v. Brown", "year": "1997"}}
{"assertion_id": "56bcdececef74879", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A single municipal hiring decision can support § 1983 liability only on a stringent showing of deliberate indifference: the plaintiff must prove that adequate scrutiny of the applicant's background would have made the plainly obvious consequence of hiring him the specific constitutional injury the plaintiff suffered.", "title": "Board of County Commissioners of Bryan County v. Brown"}}
{"assertion_id": "e807736bae4d67e0", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Anchor", "title": "Board of County Commissioners of Bryan County v. Brown"}}
{"assertion_id": "b38ce739bfec9cd6", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Board of County Commissioners of Bryan County v. Brown"}}
{"assertion_id": "e74eabb3fc583996", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Board of County Commissioners of Bryan County v. Brown", "varies_by_point": "false"}}
```

### lake record — Board of County Commissioners of Bryan County v. Brown

```json
{
  "schema_version": "s2.v1",
  "record_id": "Board of County Commissioners of Bryan County v. Brown",
  "status": "under_review",
  "identity": {
    "case_name": "Board of the County Commissioners of Bryan County v. Brown",
    "case_name_short": "Brown",
    "case_name_full": "BOARD OF THE COUNTY COMMISSIONERS OF BRYAN COUNTY, OKLAHOMA v. BROWN Et Al.",
    "input_case_name": "Board of County Commissioners of Bryan County v. Brown",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1997-04-28",
    "year": 1997,
    "docket": "95-1100",
    "cluster_id": 118104,
    "lead_opinion_id": 9842136,
    "sibling_ids": [],
    "absolute_url": "/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "520 U.S. 397",
      "volume": "520",
      "reporter": "U.S.",
      "page": "397",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "117 S. Ct. 1382",
        "volume": "117",
        "reporter": "S. Ct.",
        "page": "1382",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 L. Ed. 2d 626",
        "volume": "137",
        "reporter": "L. Ed. 2d",
        "page": "626",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 U.S.L.W. 4286",
        "volume": "65",
        "reporter": "U.S.L.W.",
        "page": "4286",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "10 Fla. L. Weekly Fed. S 405",
        "volume": "10",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "405",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 I.E.R. Cas. (BNA) 1217",
        "volume": "12",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "1217",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 Daily Journal DAR 5311",
        "volume": "97",
        "reporter": "Daily Journal DAR",
        "page": "5311",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1997 U.S. LEXIS 2793",
        "volume": "1997",
        "reporter": "U.S. LEXIS",
        "page": "2793",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 Cal. Daily Op. Serv. 3033",
        "volume": "97",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "3033",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "520 U.S. 397",
        "volume": "520",
        "reporter": "U.S.",
        "page": "397",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "117 S. Ct. 1382",
        "volume": "117",
        "reporter": "S. Ct.",
        "page": "1382",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 L. Ed. 2d 626",
        "volume": "137",
        "reporter": "L. Ed. 2d",
        "page": "626",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1997 U.S. LEXIS 2793",
        "volume": "1997",
        "reporter": "U.S. LEXIS",
        "page": "2793",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 U.S.L.W. 4286",
        "volume": "65",
        "reporter": "U.S.L.W.",
        "page": "4286",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "10 Fla. L. Weekly Fed. S 405",
        "volume": "10",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "405",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 I.E.R. Cas. (BNA) 1217",
        "volume": "12",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "1217",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 Cal. Daily Op. Serv. 3033",
        "volume": "97",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "3033",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 Daily Journal DAR 5311",
        "volume": "97",
        "reporter": "Daily Journal DAR",
        "page": "5311",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "520 U.S. 397",
    "official_selection": {
      "court_class": "scotus",
      "selected": "520 U.S. 397",
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
    "date_created": "2026-07-07T13:24:37Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:24:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:24:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:24:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:24:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "board-of-county-commissioners-of-bryan-county-v-brown--118104",
      "to_record_id": "Board of County Commissioners of Bryan County v. Brown",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Board of County Commissioners of Bryan County v. Brown

```
<opinion type="majority">
<author id="b491-9">Justice O’Connor</author>
<p id="AOj">delivered the opinion of the Court.</p>
<p id="b491-10">Respondent Jill Brown brought a claim for damages against petitioner Bryan County under Rev. Stat. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>. She alleged that a county police officer used <page-number citation-index="1" label="400">*400</page-number>excessive force in arresting her, and that the county itself was liable for her injuries based on its sheriff’s hiring and training decisions. She prevailed on her claims against the county following a jury trial, and the Court of Appeals for the Fifth Circuit affirmed the judgment against the county on the basis of the hiring claim alone. 67. F. 3d 1174 (1995). We granted certiorari. We conclude that the Court of Appeals’ decision cannot be squared with our recognition that, in enacting § 1983, Congress did not intend to impose liability on a municipality unless <em>deliberate </em>action attributable to the municipality itself is the “moving force” behind the plaintiff’s deprivation of federal rights. <em>Monell </em>v. <em>New York City Dept. of Social Servs., </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658, 694</a></span> (1978).</p>
<p id="b492-7">I</p>
<p id="b492-3">In the early morning hours of May 12, 1991, Jill Brown (hereinafter respondent) and her husband were driving from Grayson County, Texas, to their home in Bryan County, Oklahoma. After crossing into Oklahoma, they approached a police checkpoint. Mr. Brown, who was driving, decided to avoid the checkpoint and return to Texas. After seeing the Browns’ truck turn away from the checkpoint, Bryan County Deputy Sheriff Robert Morrison and Reserve Deputy Stacy Burns pursued the vehicle. Although the parties’ versions of events differ, at trial both deputies claimed that their patrol car reached speeds in excess of 100 miles per hour. Mr. Brown testified that he was unaware of the deputies’ attempts to overtake him. The chase finally ended four miles south of the police checkpoint.</p>
<p id="b492-4">After he got out of the squad car, Deputy Sheriff Morrison pointed his gun toward the Browns’ vehicle and ordered the Browns to raise their hands. Reserve Deputy Burns, who was unarmed, rounded the corner of the vehicle on the passenger’s side. Burns twice ordered respondent from the .vehicle. When she did not exit, he used an “arm bar” technique, grabbing respondent’s arm at the wrist and elbow, <page-number citation-index="1" label="401">*401</page-number>pulling her from the vehicle, and spinning her to the ground. Respondent’s knees were severely injured, and she later underwent corrective surgery. Ultimately, she may need knee replacements.</p>
<p id="b493-5">Respondent sought compensation for her injuries under <span class="citation no-link">42 U. S. C. § 1983</span> and state law from Burns, Bryan County Sheriff B. J. Moore, and the county itself. Respondent claimed, among other things, that Bryan County was liable for Burns’ alleged use of excessive force based on Sheriff Moore’s decision to hire Burns, the son of his nephew. Specifically, respondent claimed that Sheriff Moore had failed to adequately review Burns’ background. Burns had a record of driving infractions and had pleaded guilty to various driving-related and other misdemeanors, including assault and battery, resisting arrest, and public drunkenness. Oklahoma law does not preclude the hiring of an individual who has committed a misdemeanor to serve as a peace officer. See Okla. Stat., Tit. 70, § 3311(D)(2)(a) (1991) (requiring that the hiring agency certify that the prospective officer’s records do not reflect a felony conviction). At trial, Sheriff Moore testified that he had obtained Burns’ driving record and a report on Burns from the National Crime Information Center, but had not closely reviewed either. Sheriff Moore authorized Burns to make arrests, but not to carry a weapon or to operate a patrol car.</p>
<p id="b493-6">In a ruling not at issue here, the District Court dismissed respondent’s § 1983 claim against Sheriff Moore prior to trial. App. 28. Counsel for Bryan County stipulated that Sheriff Moore “was the policy maker for Bryan County regarding the Sheriff’s Department.” <em>Id., </em>at 30. At the close of respondent’s case and again at the close of all of the evidence, Bryan County moved for judgment as a matter of law. As to respondent’s claim that Sheriff Moore’s decision to hire Burns triggered municipal liability, the county argued that a single hiring decision by a municipal policymaker could not give rise to municipal liability under § 1983. <em>Id., </em>at 59-60. <page-number citation-index="1" label="402">*402</page-number>The District Court denied the county’s motions. The court also overruled the county’s objections to jury instructions on the § 1983 claim against the county. <em>Id., </em>at 125-126, 132.</p>
<p id="b494-5">To resolve respondent’s claims, the jury was asked to answer several interrogatories. The jury concluded that Stacy Burns had arrested respondent without probable cause and had used excessive force, and therefore found him liable for respondent’s injuries. It also found that the “hiring policy” and the “training policy” of Bryan County “in the case of Stacy Burns as instituted by its policymaker, B. J. Moore,” were each “so inadequate as to amount to deliberate indifference to the constitutional needs of the Plaintiff.” <em>Id., </em>at 135. The District Court entered judgment for respondent on the issue of Bryan County’s §1983 liability. The county appealed on several grounds, and the Court of Appeals for the Fifth Circuit affirmed. <span class="citation multiple-matches"><a href="/c/F.%203d/67/1174/">67 F. 3d 1174</a></span> (1995). The court held, among other things, that Bryan County was properly found liable under § 1983 based on Sheriff Moore’s decision to hire Burns. <em>Id., </em>at 1185. The court addressed only those points that it thought merited review; it did not address the jury’s determination of county liability based on inadequate training of Burns, <em>id., </em>at 1178, nor do we. We granted cer-tiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./517/1154/">517 U. S. 1154</a></span> (1996), to decide whether the county was properly held liable for respondent’s injuries based on Sheriff Moore’s single decision to hire Burns. We now reverse.</p>
<p id="b494-6">II</p>
<p id="b494-7">Title <span class="citation no-link">42 U. S. C. § 1983</span> provides in relevant part:</p>
<blockquote id="b494-8">“Every person who, under color of any statute, ordinance, regulation, custom, or usage, of any State or Territory or the District of Columbia, subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party in<page-number citation-index="1" label="403">*403</page-number>jured in an action at jaw, suit in equity, or other proper proceeding for redress.”</blockquote>
<p id="b495-6">We held in <em>Monell </em>v. <em>New York City Dept. of Social Servs., </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#689" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 689</a></span>, that municipalities and other local governmental bodies are “persons” within the meaning of § 1983. We also recognized that a municipality may not be held liable under § 1983 solely because it employs a tortfeasor. Our conclusion rested partly on the language of § 1983 itself. In' light of the statute’s imposition of liability on one who “subjects [a person], or causes [that person] to be subjected,” to a deprivation of federal rights, we concluded that it “cannot be easily read to impose liability vicariously on governing bodies solely on the basis of the existence of an employer-employee relationship with a tortfeasor.” <em>Id., </em>at 692. Our conclusion also rested upon the statute’s legislative history. As stated in <em>Pembaur </em>v. <em>Cincinnati, 475 </em>U. S. 469, 479 (1986), “while Congress never questioned its power to impose civil liability on municipalities for their <em>own </em>illegal acts, Congress did doubt its constitutional power to impose such liability in order to oblige municipalities to control the conduct of <em>others” </em>(citing <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#665" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs."><em>Monell, supra, </em>at 665-683</a></span>). We have consistently refused to hold municipalities liable under a theory of <em>respondeat superior. </em>See <em>Oklahoma City </em>v. <em>Tuttle, </em><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#818" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S. 808, 818</a></span> (1985) (plurality opinion); <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#828" aria-description="Citation for case: City of Oklahoma v. Tuttle"><em>id., </em>at 828</a></span> (opinion of Brennan, J.); <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#478" aria-description="Citation for case: Pembaur v. City of Cincinnati"><em>Pembaur, supra, </em>at 478-479</a></span>; <em>St. Louis </em>v. <em>Praprotnik, </em><span class="citation" data-id="9431224"><a href="/opinion/112017/city-of-st-louis-v-praprotnik/#122" aria-description="Citation for case: City of St. Louis v. Praprotnik">485 U. S. 112, 122</a></span> (1988) (plurality opinion); <span class="citation" data-id="9431224"><a href="/opinion/112017/city-of-st-louis-v-praprotnik/#137" aria-description="Citation for case: City of St. Louis v. Praprotnik"><em>id., </em>at 137</a></span> (opinion of Brennan, J.); <em>Canton </em>v. <em>Harris, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#392" aria-description="Citation for case: City of Canton v. Harris">489 U. S. 378, 392</a></span> (1989).</p>
<p id="b495-7">Instead, in <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>and subsequent cases, we have required a plaintiff seeking to impose liability on a municipality under §1983 to identify a municipal “policy” or “custom” that caused the plaintiff’s injury. See <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs."><em>Monell, supra, </em>at 694</a></span>; <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#480" aria-description="Citation for case: Pembaur v. City of Cincinnati"><em>Pembaur, supra, </em>at 480-481</a></span>; <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#389" aria-description="Citation for case: City of Canton v. Harris"><em>Canton, supra, </em>at 389</a></span>. Locating a “policy” ensures that a municipality is held liable only for those deprivations resulting from the decisions of its duly constituted legislative body or of those officials whose acts <page-number citation-index="1" label="404">*404</page-number>may fairly be said to be those of the municipality. <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs."><em>Monell, supra, </em>at 694</a></span>. Similarly, an act performed pursuant to a “custom” that has not been formally approved by an appropriate decisionmaker may fairly subject a municipality to liability on the theory that the relevant practice is so widespread as to have the force of law. <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 690</a></span>-691 (citing <em>Adickes </em>v. <em>S. H. Kress &amp; Co., </em><span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/#167" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">398 U. S. 144, 167-168</a></span> (1970)).</p>
<p id="b496-5">The parties join issue on whether, under <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>and subsequent cases, a single hiring decision by a county sheriff can be a “policy” that triggers municipal liability. Relying on our decision in <em><span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">Pembaur</a></span>, </em>respondent claims that a single act by a decisionmaker with final authority in the relevant area constitutes a “policy” attributable to the municipality itself. So long as a § 1983 plaintiff identifies a decision properly attributable to the municipality, respondent argues, there is no risk of imposing <em>respondeat superior </em>liability. Whether that decision was intended to govern only the situation at hand or to serve as a rule to be applied over time is immaterial. Rather, under respondent’s theory, identification of an act of a proper municipal decisionmaker is all that is required to ensure that the municipality is held liable only for its own conduct. The Court of Appeals accepted respondent’s approach.</p>
<p id="b496-6">As our § 1983 municipal liability jurisprudence illustrates, however, it is not enough for a § 1983 plaintiff merely to identify conduct properly attributable to the municipality. The plaintiff must also demonstrate that, through its <em>deliberate </em>conduct, the municipality was the “moving force” behind the injury alleged. That is, a plaintiff must show that the municipal action was taken with the requisite degree of culpability and must demonstrate a direct causal link between the municipal action and the deprivation of federal rights.</p>
<p id="b496-7">Where a plaintiff claims that a particular municipal action <em>itself </em>violates federal law, or directs an employee to do so, resolving these issues of fault and causation is straightfor<page-number citation-index="1" label="405">*405</page-number>ward. Section 1983 itself “contains no state-of-mind requirement independent of that necessary to state a violation” of the underlying federal right. <em>Daniels </em>v. <em>Williams, </em><span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/#330" aria-description="Citation for case: Daniels v. Williams">474 U. S. 327, 330</a></span> (1986). In any § 1983 suit, however, the plaintiff must establish the state of mind required to prove the underlying violation. Accordingly, proof that a municipality’s legislative body or authorized decisionmaker has intentionally deprived a plaintiff of a federally protected right necessarily establishes that the municipality acted culpably. Similarly, the conclusion that the action taken or directed by the municipality or its authorized decisionmaker itself violates federal law will also determine that the municipal action was the moving force behind the injury of which the plaintiff complains.</p>
<p id="b497-5">Sheriff Moore’s hiring decision was itself legal, and Sheriff Moore did not authorize Burns to use excessive force. Respondent’s claim, rather, is that a single facially lawful hiring decision can launch a series of events that ultimately cause a violation of federal rights. Where a plaintiff claims that the municipality has not directly inflicted an injury, but nonetheless has caused an employee to do so, rigorous standards of culpability and causation must be applied to ensure that the municipality is not held liable solely for the actions of its employee. See <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#391" aria-description="Citation for case: City of Canton v. Harris"><em>Canton, supra, </em>at 391-392</a></span>; <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#824" aria-description="Citation for case: City of Oklahoma v. Tuttle"><em>Tuttle, supra, </em>at 824</a></span> (plurality opinion). See also <em>Springfield </em>v. <em>Kibbe, </em><span class="citation" data-id="9430858"><a href="/opinion/111831/city-of-springfield-v-kibbe/#270" aria-description="Citation for case: City of Springfield v. Kibbe">480 U. S. 257, 270-271</a></span> (1987) <em>(per curiam) </em>(dissent from dismissal of writ as improvidently granted).</p>
<p id="b497-6">In relying heavily on <em><span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">Pembaur</a></span>, </em>respondent blurs the distinction between § 1983 cases that present no difficult questions of fault and causation and those that do. To the extent that we have recognized a cause of action under § 1983 based on a single decision attributable to a municipality, we have done so only where the evidence that the municipality had acted and that the plaintiff had suffered a deprivation of federal rights also proved fault and causation. For example, <em>Owen </em>v. <em>Independence, </em><span class="citation" data-id="9427858"><a href="/opinion/110236/owen-v-city-of-independence/" aria-description="Citation for case: Owen v. City of Independence">445 U. S. 622</a></span> (1980), and <em>Newport </em>v. <page-number citation-index="1" label="406">*406</page-number><em>Fact Concerts, Inc., </em><span class="citation" data-id="9428471"><a href="/opinion/110553/city-of-newport-v-fact-concerts-inc/" aria-description="Citation for case: City of Newport v. Fact Concerts, Inc.">453 U. S. 247</a></span> (1981), involved formal decisions of municipal legislative bodies. In <em><span class="citation" data-id="9427858"><a href="/opinion/110236/owen-v-city-of-independence/" aria-description="Citation for case: Owen v. City of Independence">Owen</a></span>, </em>the city council allegedly censured and discharged an employee without a hearing. <span class="citation" data-id="9427858"><a href="/opinion/110236/owen-v-city-of-independence/#627" aria-description="Citation for case: Owen v. City of Independence">445 U. S., at 627-629, 633</a></span>, and n. 13. In <em>Fact Concerts, </em>the city council canceled a license permitting a concert following a dispute over the performance’s content. <span class="citation" data-id="9428471"><a href="/opinion/110553/city-of-newport-v-fact-concerts-inc/#252" aria-description="Citation for case: City of Newport v. Fact Concerts, Inc.">453 U. S., at 252</a></span>. Neither decision reflected implementation of a generally applicable rule. But we did not question that each decision, duly promulgated by city lawmakers, could trigger municipal liability if the decision itself were found to be unconstitutional. Because fault and causation were obvious in each case, proof that the municipality’s decision was unconstitutional would suffice to establish that the municipality itself was liable for the plaintiff’s constitutional injury.</p>
<p id="b498-5">Similarly, <em>Pembaur </em>v. <em>Cincinnati </em>concerned a decision by a county prosecutor, acting as the county’s final decision-maker, <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#485" aria-description="Citation for case: Pembaur v. City of Cincinnati">475 U. S., at 485</a></span>, to direct county deputies to forcibly enter petitioner’s place of business to serve <em>capiases </em>upon third parties. Relying on <em><span class="citation" data-id="9427858"><a href="/opinion/110236/owen-v-city-of-independence/" aria-description="Citation for case: Owen v. City of Independence">Owen</a></span> </em>and <em><span class="citation" data-id="9428471"><a href="/opinion/110553/city-of-newport-v-fact-concerts-inc/" aria-description="Citation for case: City of Newport v. Fact Concerts, Inc.">Newport</a></span>, </em>we concluded that a final decisionmaker’s adoption of a course of action “tailored to a particular situation and not intended to control decisions in later situations” may, in some circumstances, give rise to municipal liability under § 1983. <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#481" aria-description="Citation for case: Pembaur v. City of Cincinnati">475 U. S., at 481</a></span>. In <em><span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">Pembaur</a></span>, </em>it was not disputed that the prosecutor had specifically directed the action resulting in the deprivation of petitioner’s rights. The conclusion that the decision was that of a final municipal decisionmaker and was therefore properly attributable to the municipality established municipal liability. No questions of fault or causation arose.</p>
<p id="b498-6">Claims not involving an allegation that the municipal action itself violated federal law, or directed or authorized the deprivation of federal rights, present much more difficult problems of proof. That a plaintiff has suffered a deprivation of federal rights at the hands of a municipal employee will not alone permit an inference of municipal culpability and causation; the plaintiff will simply have shown that the <page-number citation-index="1" label="407">*407</page-number><em>employee </em>acted culpably. We recognized these difficulties in <em>Canton </em>v. <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Harris</a></span>, </em>where we considered a claim that inadequate training of shift supervisors at a city jail led to a deprivation of a detainee’s constitutional rights. We held that, quite apart from the state of mind required to establish the underlying constitutional violation — in that case, a violation of due process, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#388" aria-description="Citation for case: City of Canton v. Harris">489 U. S., at 388-389</a></span>, n. 8 — a plaintiff seeking to establish municipal liability on the theory that a facially lawful municipal action has led an employee to violate a plaintiff’s rights must demonstrate that the municipal action was taken with “deliberate indifference” as to its known or obvious consequences. <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#388" aria-description="Citation for case: City of Canton v. Harris"><em>Id., </em>at 388</a></span>. A showing of simple or even heightened negligence will not suffice.</p>
<p id="b499-4">We concluded in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>that an “inadequate training” claim could be the basis for § 1983 liability in “limited circumstances.” <em>Id., </em>at 387. We spoke, however, of a deficient training “program,” necessarily intended to apply over time to multiple employees. <em>Id., </em>at 390. Existence of a “program” makes proof of fault and causation at least possible in an inadequate training case. If a program does not prevent constitutional violations, municipal decisionmakers may eventually be put on notice that a new program is called for. Their continued adherence to an approach that they know or should know has failed to prevent tortious conduct by employees may establish the conscious disregard for the consequences of their action — the “deliberate indifference” — necessary to trigger municipal liability. <em>Id., </em>at 390, n. 10 (“It could ... be that the police, in exercising their discretion, so often violate constitutional rights that the need for further training must have been plainly obvious to the city policymakers, who, nevertheless, are ‘deliberately indifferent’ to the need”); <em>id., </em>at 397 (O’Connor, J., concurring in part and dissenting in part) (“[Municipal liability for failure to train may be proper where it can be shown that policymakers were aware of, and acquiesced in, a pattern of constitutional violations . . .”). In addition, the existence of a pattern of <page-number citation-index="1" label="408">*408</page-number>tortious conduct by inadequately trained employees may tend to show that the lack of proper training, rather than a one-time negligent administration of the program or factors peculiar to the officer involved in a particular incident, is the “moving force” behind the plaintiff’s injury. See <em>id., </em>at 390-391.</p>
<p id="b500-5">Before trial, counsel for Bryan County stipulated that Sheriff Moore “was the policy maker for Bryan County regarding the Sheriff’s Department.” App. 30. Indeed, the county sought to avoid liability by claiming that its Board of Commissioners participated in no policy decisions regarding the conduct and operation of the office of the Bryan County Sheriff. <em>Id., </em>at 32. Accepting the county’s representations below, then, this case presents no difficult questions concerning whether Sheriff Moore has final authority to act for the municipality in hiring matters. Cf. <em>Jett </em>v. <em>Dallas Independent School Dist., </em><span class="citation" data-id="9842104"><a href="/opinion/112313/jett-v-dallas-independent-school-district/" aria-description="Citation for case: Jett v. Dallas Independent School District">491 U. S. 701</a></span> (1989); <em>St. Louis </em>v. <em>Praprotnik, </em><span class="citation" data-id="9431224"><a href="/opinion/112017/city-of-st-louis-v-praprotnik/" aria-description="Citation for case: City of St. Louis v. Praprotnik">485 U. S. 112</a></span> (1988). Respondent does not claim that she can identify any pattern of injuries linked to Sheriff Moore’s hiring practices. Indeed, respondent does not contend that Sheriff Moore’s hiring practices are generally defective. The only evidence on this point at trial suggested that Sheriff Moore had adequately screened the backgrounds of all prior deputies he hired. App. 106-110. Respondent instead seeks to trace liability to what can only be described as a deviation from Sheriff Moore’s ordinary hiring practices. Where a claim of municipal liability rests on a single decision, not itself representing a violation of federal law and not directing such a violation, the danger that a municipality will be held liable without fault is high. Because the decision necessarily governs a single case, there can be no notice to the municipal decisionmaker, based on previous violations of federally protected rights, that his approach is inadequate. Nor will it be readily apparent that the municipality’s action caused the injury in question, because the plaintiff can point to no other incident tending to make it more likely that the <page-number citation-index="1" label="409">*409</page-number>plaintiff’s own injury flows from the municipality’s action, rather than from some other intervening cause.</p>
<p id="b501-5">In <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span>, </em>we did not foreclose the possibility that evidence of a single violation of federal rights, accompanied by a showing that a municipality has failed to train its employees to handle recurring situations presenting an obvious potential for such a violation, could trigger municipal liability. <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#390" aria-description="Citation for case: City of Canton v. Harris">489 U. S., at 390</a></span>, and n. 10 (“[I]t may happen that in light of the duties assigned to specific officers or employees the need for more or different training is so obvious . . . that the policymakers of the city can reasonably be said to have been deliberately indifferent to the need”). Respondent purports to rely on <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span>, </em>arguing that Burns’ use of excessive force was the plainly obvious consequence of Sheriff Moore’s failure to screen Burns’ record. In essence, respondent claims that this showing of “obviousness” would demonstrate both that Sheriff Moore acted with conscious disregard for the consequences of his action and that the Sheriff’s action directly caused her injuries, and would thus substitute for the pattern of injuries ordinarily necessary to establish municipal culpability and causation.</p>
<p id="b501-6">The proffered analogy between failure-to-train cases and inadequate screening cases is not persuasive. In leaving open in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>the possibility that a plaintiff might succeed in carrying a failure-to-train claim without showing a pattern of constitutional violations, we simply hypothesized that, in a narrow range of circumstances, a violation of federal rights may be a highly predictable consequence of a failure to equip law enforcement officers with specific tools to handle recurring situations. The likelihood that the situation will recur and the predictability that an officer lacking specific tools to handle that situation will violate citizens’ rights could justify a finding that policymakers’ decision not to train the officer reflected “deliberate indifference” to the obvious consequence of the policymakers’ choice — namely, a violation of a specific constitutional or statutory right. The high degree <page-number citation-index="1" label="410">*410</page-number>of predictability may also support an inference of causation— that the municipality’s indifference led directly to the very consequence that was so predictable.</p>
<p id="b502-5">Where a plaintiff presents a § 1983 claim premised upon the inadequacy of an official’s review of a prospective applicant’s record, however, there is a particular danger that a municipality will be held liable for an injury not directly caused by a deliberate action attributable to the municipality itself. Every injury suffered at the hands of a municipal employee can be traced to a hiring decision in a “but-for” sense: But for the municipality’s decision to hire the employee, the plaintiff would not have suffered the injury. To prevent municipal liability for a hiring decision from collapsing into <em>re-spondeat superior </em>liability, a court must carefully test the link between the policymaker’s inadequate decision and the particular injury alleged.</p>
<p id="b502-6">In attempting to import the reasoning of <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>into the hiring context, respondent ignores the fact that predicting the consequence of a single hiring decision, even one based on an inadequate assessment of a record, is far more difficult than predicting what might flow from the failure to train a single law enforcement officer as to a specific skill necessary to the discharge of his duties. As our decision in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>makes clear, “deliberate indifference” is a stringent standard of fault, requiring proof that a municipal actor disregarded a known or obvious consequence of his action. Unlike the risk from a particular glaring omission in a training regimen, the risk from a single instance of inadequate screening of an applicant’s background is not “obvious” in the abstract; rather, it depends upon the background of the applicant. A lack of scrutiny may increase the likelihood that an unfit officer will be hired, and that the unfit officer will, when placed in a particular position to affect the rights of citizens, act improperly. But that is only a generalized showing of risk. The fact that inadequate scrutiny of an applicant’s background would make a violation of rights more <em>likely </em>cannot alone <page-number citation-index="1" label="411">*411</page-number>give rise to an inference that a policymaker’s failure to scrutinize the record of a particular applicant produced a specific constitutional violation. After all, a full screening of an applicant’s background might reveal no cause for concern at all; if so, a hiring official who failed to scrutinize the applicant’s background cannot be said to have consciously disregarded an obvious risk that the officer would subsequently inflict a particular constitutional injury.</p>
<p id="b503-5">We assume that a jury could properly find in this case that Sheriff Moore’s assessment of Burns’ background was inadequate. Sheriff Moore’s own testimony indicated that he did not inquire into the underlying conduct or the disposition of any of the misdemeanor charges reflected on Burns’ record before hiring him. But this showing of an instance of inadequate screening is not enough to establish “deliberate indifference.” In layman’s terms, inadequate screening of an applicant’s record may reflect “indifference” to the applicant’s background. For purposes of a legal inquiry into municipal liability under § 1983, however, that is not the <em>relevant </em>“indifference.” A plaintiff must demonstrate that a municipal decision reflects deliberate indifference to the risk that a violation of a particular constitutional or statutory right will follow the decision. Only where adequate scrutiny of an applicant’s background would lead a reasonable policymaker to conclude that the plainly obvious consequence of the decision to hire the applicant would be the deprivation of a third party’s federally protected right can the official’s failure to adequately scrutinize the applicant’s background constitute “deliberate indifference.”</p>
<p id="b503-6">Neither the District Court nor the Court of Appeals directly tested the link between Burns’ actual background and the risk that, if hired, he would use excessive force. The District Court instructed the jury on a theory analogous to that reserved in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span>. </em>The court required respondent to prove that Sheriff Moore’s inadequate screening of Burns’ background was “so likely to result in <em>violations of constitu</em><page-number citation-index="1" label="412">*412</page-number><em>tional rights” </em>that the Sheriff could “reasonably [be] said to have been deliberately indifferent to the <em>constitutional needs </em>of the Plaintiff.” App. 12B (emphasis added). The court also instructed the jury, without elaboration, that respondent was required to prove that the “inadequate hiring . . . policy directly caused the Plaintiff’s injury.” <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Ibid.</a></span></em></p>
<p id="b504-3">As discussed above, a finding of culpability simply cannot depend on the mere probability that any officer inadequately screened will inflict any constitutional injury. Rather, it must depend on a finding that <em>this </em>officer was highly likely to inflict the <em>particular </em>injury suffered by the plaintiff. The connection between the background of the particular applicant and the specific constitutional violation alleged must be strong. What the District Court’s instructions on culpability, and therefore the jury’s finding of municipal liability, failed to capture is whether Burns’ background made his use of excessive force in making an arrest a plainly obvious consequence of the hiring decision. The Court of Appeals’ af-firmance of the jury’s finding of municipal liability depended on its view that the jury could have found that “inadequate screening of <em>a deputy </em>could likely result in the violation of <em>citizens’ constitutional rights.” </em>67 F. 3d, at 1185 (emphasis added). Beyond relying on a risk of violations of unspecified constitutional rights, the Court of Appeals also posited that Sheriff Moore’s decision reflected indifference to “the public’s welfare.” <em>Id., at </em>1184.</p>
<p id="b504-4">Even assuming without deciding that proof of a single instance of inadequate screening could ever trigger municipal liability, the evidence in this case was insufficient to support a finding that, in hiring Burns, Sheriff Moore disregarded a known or obvious risk of injury. To test the link between Sheriff Moore’s hiring decision and respondent’s injury, we must ask whether a full review of Burns’ record reveals that Sheriff Moore should have concluded that Burns’ use of excessive force would be a plainly obvious consequence of the <page-number citation-index="1" label="413">*413</page-number>hiring decision.<footnotemark>1</footnotemark> On this point, respondent’s showing was inadequate. To be sure, Burns’ record reflected various misdemeanor infractions. Respondent claims that the record demonstrated such a strong propensity for violence that Burns’ application of excessive force was highly likely. The primary charges on which respondent relies, however, are those arising from a fight on a college campus where Burns was a student. In connection with this single incident, Burns was charged with assault and battery, resisting arrest, and public drunkenness.<footnotemark>2</footnotemark> In January 1990, when he pleaded <page-number citation-index="1" label="414">*414</page-number>guilty to those charges, Burns also pleaded guilty to various driving-related offenses, including nine moving violations and a charge of driving with a suspended license. In addition, Burns had previously pleaded guilty to being in actual physical control of a vehicle while intoxicated.</p>
<p id="b506-5">The fact that Burns had pleaded guilty to traffic offenses and other misdemeanors may well have made him an extremely poor candidate for reserve deputy. Had Sheriff Moore fully reviewed Burns’ record, he might have come to precisely that conclusion. But unless he would necessarily have reached that decision <em>because </em>Burns’ use of excessive force would have been a plainly obvious consequence of the hiring decision, Sheriff Moore’s inadequate scrutiny of Burns’ record cannot constitute “deliberate indifference” to respondent’s federally protected right to be free from a use of excessive force.</p>
<p id="b506-6">Justice Souter’s reading of the case is that the jury believed that Sheriff Moore in fact read Burns’ entire record. <em>Post, </em>at 426-427. That is plausible, but it is also irrelevant. It is not sufficient for respondent to show that Sheriff Moore read Burns’ record and therefore hired Burns with knowledge of his background. Such a decision may reflect indif<page-number citation-index="1" label="415">*415</page-number>ference to Burns’ <em>record, </em>but what is required is deliberate indifference to a plaintiff’s constitutional right. That is, whether Sheriff Moore failed to examine Burns’ record, partially examined it, or fully examined it, Sheriff Moore’s hiring decision could not have been “deliberately indifferent” unless in light of that record Burns’ use of excessive force would have been a plainly obvious consequence of the hiring decision. Because there was insufficient evidence on which a jury could base a finding that Sheriff Moore’s decision to hire Burns reflected conscious disregard of an obvious risk that a use of excessive force would follow, the District Court erred in submitting respondent’s inadequate screening claim to the jury.</p>
<p id="b507-5">III</p>
<p id="b507-6">Cases involving 'constitutional injuries allegedly traceable to an ill-considered hiring decision pose the greatest risk that a municipality will be held liable for an injury that it did not cause. In the broadest sense, every injury is traceable to a hiring decision. Where a court fails to adhere to rigorous requirements of culpability and causation, municipal liability collapses into <em>respondeat superior </em>liability. As we recognized in <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>and have repeatedly reaffirmed, Congress did not intend municipalities to be held liable unless <em>deliberate </em>action attributable to the municipality directly caused a deprivation of federal rights. A failure to apply stringent culpability and causation requirements raises serious federalism concerns, in that it risks constitutionalizing particular hiring requirements that States have themselves elected not to impose. Cf. <em>Canton </em>v. <em>Harris, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#392" aria-description="Citation for case: City of Canton v. Harris">489 U. S., at 392</a></span>. Bryan County is not liable for Sheriff Moore’s isolated decision to hire Burns without adequate screening, because respondent has not demonstrated that his decision reflected a conscious disregard for a high risk that Burns would use excessive force in violation of respondent’s federally pro<page-number citation-index="1" label="416">*416</page-number>tected right. We therefore vacate the judgment of the Court of Appeals and remand this case for further proceedings consistent with this opinion.</p>
<p id="b508-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b505-4"> In suggesting that our decision complicates this Court’s § 1983 municipal liability jurisprudence by altering the understanding of culpability, Justice Souter and Justice Breyer misunderstand our approach. <em>Post, </em>at 422; <em>post, </em>at 430, 433-434. We do not suggest that a plaintiff in an inadequate screening case must show a higher degree of culpability than the “deliberate indifference” required in <em>Canton </em>v. <em>Harris, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">489 U. S. 378</a></span> (1989); we need not do so, because, as discussed below, respondent has not made a showing of deliberate indifference here. See <em>infra </em>this page and 414. Furthermore, in assessing the risks of a decision to hire a particular individual, we draw no distinction between what is “so obvious” or “so likely to occur” and what is “plainly obvious.” The difficulty with the lower courts’ approach is that it fails to connect the background of the particular officer hired in this case to the particular constitutional violation the respondent suffered. <em>Supra, </em>at 412. Ensuring that lower courts link the background of the officer to the constitutional violation alleged does not complicate our municipal liability jurisprudence with degrees of “obviousness,” but seeks to ensure that a plaintiff in an inadequate screening ease establishes a policymaker’s deliberate indifference — that is, conscious disregard for the known and obvious consequences of his actions.</p>
</footnote>
<footnote label="2">
<p id="b505-5"> Justice Souter implies that Burns’ record reflected assault and battery charges arising from more than one incident. <em>Post, </em>at 428. There' has never been a serious dispute that a single misdemeanor assault and battery conviction arose out of a single campus fight. Nor did petitioner’s expert testify that the record reflected any assault charge without a disposition, see 9 Record 535-536, although Justice Souter appears to suggest otherwise, <em>post, </em>at 428-429, n. 6.</p>
<p id="b505-6">In fact, respondent’s own expert witness testified that Burns’ record reflected a single assault conviction. 7 Record 318; see also <em>id., </em>at 320. Petitioner has repeatedly so claimed. See, <em>e. g., </em>Suggestion for Rehearing En Banc in No. 93-5376 (CA5), p. 12 (“Burns had one misdemeanor assault <page-number citation-index="1" label="414">*414</page-number>convietion stemming from a campus fight”); Pet. for Rehearing of Substituted Opinion in No. 93-5376 (CA5), p. 11 (same); 3 Record 927 (Brief in Support of Defendants’ Motion for Judgment Notwithstanding the Verdict 10); Pet. for Cert. 16 (“Burns pled guilty to assault and battery” as a result of “one campus fight”).</p>
<p id="b506-8">Respondent has not once contested this characterization. See, <em>e. g., </em>3 Record 961 (Brief in Support of Plaintiff’s Response to Defendants’ Motion for Judgment Notwithstanding the Jury Verdict 4); Brief for Appellee/ Cross-Appellant Brown et al. in No. 93-5376 (CA5), pp. 3-4; Brief in Opposition 1. Indeed, since the characterization is reflected in the county’s petition for certiorari, under this Court’s Rule 15(2) respondent would have had an obligation in her brief in opposition to correct “any perceived misstatement” in the petition. She did not. Involvement in a single fraternity fracas does not demonstrate “a proclivity to violence against the person.” <em>Post, </em>at 429, n. 6.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Board of Education v. Earls.md  (`case`, 5 assertions)

### content_page

```
---
title: "Board of Education v. Earls"
type: case
citation: ""
parallel_cite: "536 U.S. 822; 122 S. Ct. 2559; 153 L. Ed. 2d 735; 2002 Daily Journal DAR 7275; 70 U.S.L.W. 4737; 15 Fla. L. Weekly Fed. S 483"
neutral_cite: "2002 U.S. LEXIS 4882; 2002 Cal. Daily Op. Serv. 5761"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2002
date_decided: 2002-06-27
docket: 01-332
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2002-06-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Board of Education v. Earls
  varies_by_point: false
  scope_note: "Extends Vernonia to non-athletes; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/121171/board-of-education-of-independent-school-district-no-92-of-pottawatomie/"
  cluster_id: 121171
  opinion_id: 121171
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Vernonia School District 47J v. Acton]]", "[[New Jersey v. T.L.O.]]", "[[Skinner v. Railway Labor Executives' Assn.]]"]
aliases: ["Board of Education of Independent School District No. 92 of Pottawatomie County v. Earls", "Earls"]
tags: ["case", "fourth-amendment", "special-needs", "drug-testing", "schools"]
holding: "Suspicionless drug testing of all students participating in competitive extracurricular activities is a reasonable special-needs search."
lake:
  record_id: Board of Education v. Earls
  status: verified
  projected_at: 2026-07-09
---

# Board of Education v. Earls

*536 U.S. 822 (2002)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
The Tecumseh, Oklahoma school district adopted a Student Activities Drug Testing Policy requiring all middle- and high-school students to submit to urinalysis drug testing in order to participate in any competitive extracurricular activity (choir, band, academic team, athletics, and the like). Lindsay Earls and other students who participated in such activities challenged the policy as an unreasonable search.

## Issue
Whether a public school's suspicionless drug testing of all students who participate in competitive extracurricular activities is a reasonable search under the Fourth Amendment.

## Rule
In the public-school special-needs context, the search need not rest on individualized suspicion: "In this context, the Fourth Amendment does not require a finding of individualized suspicion". — 536 U.S. at 837. ^pin-837

Applying the special-needs reasonableness balance, the Court upheld the policy: "we hold only that Tecumseh's Policy is a reasonable means of furthering the School District's important interest in preventing and deterring drug use among its schoolchildren." — [*Id.* at 838](https://www.courtlistener.com/opinion/121171/board-of-education-of-independent-school-district-no-92-of-pottawatomie/#:~:text=we%20hold%20only%20that%20Tecumseh%27s). ^pin-838

## Application
On these facts the testing reached students who voluntarily participated in extracurricular activities, the intrusion (a monitored but private urine sample, results kept confidential and not turned over to law enforcement) was limited, and the district faced a documented drug problem within its custodial responsibility over schoolchildren. Weighing those factors, the Court concluded the Tecumseh policy was a reasonable, effective means of addressing drug use and did not require individualized suspicion.

## Conclusion
The policy was a reasonable special-needs search; the judgment of the Tenth Circuit invalidating it was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Earls* **extends** [[Vernonia School District 47J v. Acton]] beyond student athletes to all participants in competitive extracurricular activities.

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *Board of Education v. Earls*, 536 U.S. 822 (2002) — https://www.courtlistener.com/opinion/121171/board-of-education-of-independent-school-district-no-92-of-pottawatomie/ — pinpoints: 837, 838.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a4dcbabe876ab6c5", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2002 U.S. LEXIS 4882; 2002 Cal. Daily Op. Serv. 5761", "official_citation_present": false, "parallel_cite": "536 U.S. 822; 122 S. Ct. 2559; 153 L. Ed. 2d 735; 2002 Daily Journal DAR 7275; 70 U.S.L.W. 4737; 15 Fla. L. Weekly Fed. S 483", "title": "Board of Education v. Earls", "year": "2002"}}
{"assertion_id": "52d4a05082cbec37", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Suspicionless drug testing of all students participating in competitive extracurricular activities is a reasonable special-needs search.", "title": "Board of Education v. Earls"}}
{"assertion_id": "d1a4b58d7249bde4", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Key — Progeny / Refinement", "title": "Board of Education v. Earls"}}
{"assertion_id": "12d3922fb1b92968", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2002-06-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Board of Education v. Earls", "field_i_validity": "good_law", "scope_note": "Extends Vernonia to non-athletes; good law.", "title": "Board of Education v. Earls", "varies_by_point": "false"}}
{"assertion_id": "9adc9bfb20e50872", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Board of Education v. Earls"}}
```

### lake record — Board of Education v. Earls

```json
{
  "schema_version": "s2.v1",
  "record_id": "Board of Education v. Earls",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Board of Education of Independent School District No. 92 of Pottawatomie County v. Earls",
    "case_name_short": "Earls",
    "case_name_full": "BOARD OF EDUCATION OF INDEPENDENT SCHOOL DISTRICT NO. 92 OF POTTAWATOMIE COUNTY Et Al. v. EARLS Et Al.",
    "input_case_name": "Board of Education v. Earls",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2002-06-27",
    "year": 2002,
    "docket": "01-332",
    "cluster_id": 121171,
    "lead_opinion_id": 121171,
    "sibling_ids": [
      121171,
      9434325,
      9434326,
      9434327,
      9434328
    ],
    "absolute_url": "/opinion/121171/board-of-education-of-independent-school-district-no-92-of-pottawatomie/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9271936,
        "score": 20,
        "case_name": "Board of Education of Independent School District No. 92 v. Earls"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "536 U.S. 822",
        "volume": "536",
        "reporter": "U.S.",
        "page": "822",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "122 S. Ct. 2559",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "2559",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "153 L. Ed. 2d 735",
        "volume": "153",
        "reporter": "L. Ed. 2d",
        "page": "735",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 Daily Journal DAR 7275",
        "volume": "2002",
        "reporter": "Daily Journal DAR",
        "page": "7275",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "70 U.S.L.W. 4737",
        "volume": "70",
        "reporter": "U.S.L.W.",
        "page": "4737",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "15 Fla. L. Weekly Fed. S 483",
        "volume": "15",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "483",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2002 U.S. LEXIS 4882",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "4882",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 Cal. Daily Op. Serv. 5761",
        "volume": "2002",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "5761",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "536 U.S. 822",
        "volume": "536",
        "reporter": "U.S.",
        "page": "822",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "122 S. Ct. 2559",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "2559",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "153 L. Ed. 2d 735",
        "volume": "153",
        "reporter": "L. Ed. 2d",
        "page": "735",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 U.S. LEXIS 4882",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "4882",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 Cal. Daily Op. Serv. 5761",
        "volume": "2002",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "5761",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 Daily Journal DAR 7275",
        "volume": "2002",
        "reporter": "Daily Journal DAR",
        "page": "7275",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "70 U.S.L.W. 4737",
        "volume": "70",
        "reporter": "U.S.L.W.",
        "page": "4737",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "15 Fla. L. Weekly Fed. S 483",
        "volume": "15",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "483",
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
      "id": "pin-837",
      "page": null,
      "quote": "--- # Board of Education v. Earls *536 U.S. 822 (2002)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background The Tecumseh, Oklahoma school district adopted a Student Activities Drug Testing Policy requiring all middle- and high-school students to submit to urinalysis drug testing in order to participate in any competitive extracurricular activity (choir, band, academic team, athletics, and the like). Lindsay Earls and other students who participated in such activities challenged the policy as an unreasonable search. ## Issue Whether a public school's suspicionless drug testing of all students who participate in competitive extracurricular activities is a reasonable search under the Fourth Amendment. ## Rule In the public-school special-needs context, the search need not rest on individualized suspicion:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-838",
      "page": null,
      "quote": "we hold only that Tecumseh's Policy is a reasonable means of furthering the School District's important interest in preventing and deterring drug use among its schoolchildren.",
      "star_marker": "838",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 37097,
      "fragment": "#:~:text=we%20hold%20only%20that%20Tecumseh%27s",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2002-06-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Board of Education v. Earls",
    "varies_by_point": false,
    "scope_note": "Extends Vernonia to non-athletes; good law.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Board of Education v. Earls:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mangino v. Incorporated Village of Patchogue",
          "cluster_id": 3164642,
          "cite": [
            "808 F.3d 951",
            "2015 U.S. App. LEXIS 22431",
            "2015 WL 9287019"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Christine Ann Kern",
          "cluster_id": 4472227,
          "cite": [
            "831 N.W.2d 149",
            "2013 WL 2278018",
            "2013 Iowa Sup. LEXIS 61"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re D.H.",
          "cluster_id": 5280981,
          "cite": [
            "306 S.W.3d 955"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gillman Ex Rel. Gillman v. School Board for Holmes County",
          "cluster_id": 1454556,
          "cite": [
            "567 F. Supp. 2d 1359",
            "2008 U.S. Dist. LEXIS 56589",
            "2008 WL 2854266"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Weikert",
          "cluster_id": 202888,
          "cite": [
            "504 F.3d 1",
            "2007 U.S. App. LEXIS 18845",
            "2007 WL 2265660"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane1_negative"
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
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nicholas Omar Midgette",
          "cluster_id": 796984,
          "cite": [
            "478 F.3d 616",
            "2007 U.S. App. LEXIS 4153",
            "2007 WL 572127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
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
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dubbs Ex Rel. Dubbs v. Head Start, Inc.",
          "cluster_id": 163684,
          "cite": [
            "336 F.3d 1194",
            "2003 U.S. App. LEXIS 14578",
            "2003 WL 21690533"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morse v. Frederick",
          "cluster_id": 145707,
          "cite": [
            "168 L. Ed. 2d 290",
            "127 S. Ct. 2618",
            "551 U.S. 393",
            "2007 U.S. LEXIS 8514"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Safford Unified School District 1 v. Redding",
          "cluster_id": 145852,
          "cite": [
            "174 L. Ed. 2d 354",
            "129 S. Ct. 2633",
            "557 U.S. 364",
            "2009 U.S. LEXIS 4735",
            "21 Fla. L. Weekly Fed. S 1011",
            "77 U.S.L.W. 4591"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bull v. City and County of San Francisco",
          "cluster_id": 1313115,
          "cite": [
            "595 F.3d 964",
            "2010 WL 431790"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Shukri Baker",
          "cluster_id": 618459,
          "cite": [
            "664 F.3d 467"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
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
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Christian Legal Soc. Chapter of Univ. of Cal., Hastings College of Law v. Martinez",
          "cluster_id": 150544,
          "cite": [
            "177 L. Ed. 2d 838",
            "130 S. Ct. 2971",
            "561 U.S. 661",
            "2010 U.S. LEXIS 5367"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
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
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicholas v. Goord",
          "cluster_id": 8439101,
          "cite": [
            "430 F.3d 652",
            "2005 WL 3150611"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Douglas McClish v. Richard B. Nugent",
          "cluster_id": 77659,
          "cite": [
            "483 F.3d 1231",
            "2007 U.S. App. LEXIS 8294",
            "2007 WL 1063337"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
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
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Ontario v. Quon",
          "cluster_id": 148797,
          "cite": [
            "177 L. Ed. 2d 216",
            "130 S. Ct. 2619",
            "560 U.S. 746",
            "2010 U.S. LEXIS 4972"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe v. Woodard",
          "cluster_id": 4578612,
          "cite": [
            "912 F.3d 1278"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. James Maximiliano Ochoa",
          "cluster_id": 4472474,
          "cite": [
            "792 N.W.2d 260",
            "2010 Iowa Sup. LEXIS 135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brittan Holland v. Kelly Rosen",
          "cluster_id": 4515181,
          "cite": [
            "895 F.3d 272"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brandon Michael Lifshitz",
          "cluster_id": 786321,
          "cite": [
            "369 F.3d 173",
            "2004 WL 1043468"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "No. 01-5098",
          "cluster_id": 782823,
          "cite": [
            "336 F.3d 1194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul Palmieri v. Pamela Lynch, AKA Pam Lynch, John Doe 1",
          "cluster_id": 788624,
          "cite": [
            "392 F.3d 73",
            "2004 U.S. App. LEXIS 25468",
            "2004 WL 2827676"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raymond Lee Scott",
          "cluster_id": 794629,
          "cite": [
            "450 F.3d 863",
            "2006 U.S. App. LEXIS 14182"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Paul G. Sczubelek",
          "cluster_id": 789683,
          "cite": [
            "402 F.3d 175",
            "2005 WL 638158"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(121171 OR 9434325 OR 9434326 OR 9434327 OR 9434328) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDM2NTQwODAwMDAwJnM9Nzc5NzQ1JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28121171+OR+9434325+OR+9434326+OR+9434327+OR+9434328%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 6,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(121171 OR 9434325 OR 9434326 OR 9434327 OR 9434328)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MiZzPTI1MDcxNjkmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28121171+OR+9434325+OR+9434326+OR+9434327+OR+9434328%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(121171 OR 9434325 OR 9434326 OR 9434327 OR 9434328)",
        "reviewed": 7,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 7,
        "triage_read": 0,
        "triage_snippet_classified": 7
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(121171 OR 9434325 OR 9434326 OR 9434327 OR 9434328)",
    "indexed_citing_opinions": 274,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 121171,
        "count": 243,
        "count_source": "search"
      },
      {
        "opinion_id": 9434325,
        "count": 37,
        "count_source": "search"
      },
      {
        "opinion_id": 9434326,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434327,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434328,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 499,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/board-of-education-v-earls.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY5MDY1Mjgmcz00Nzc4NDAyJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28121171+OR+9434325+OR+9434326+OR+9434327+OR+9434328%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 121171,
        "cited_id": 103870,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 106395,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 107841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 111754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 112220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 112779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 118100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 118414,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 118432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 772423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 2580272,
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
    "date_created": "2026-07-04T22:57:48Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:09:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:09:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:12:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:09:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Board of Education v. Earls

```
<div>
<center><b><span class="citation" data-id="9434325"><a href="/opinion/121171/board-of-education-of-independent-school-district-no-92-of-pottawatomie/" aria-description="Citation for case: Board of Education of Independent School District No. 92...">536 U.S. 822</a></span> (2002)</b></center>
<center><h1>BOARD OF EDUCATION OF INDEPENDENT SCHOOL DISTRICT NO. 92 OF POTTAWATOMIE COUNTY et al.<br>
v.<br>
EARLS et al.</h1></center>
<center>No. 01-332.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued March 19, 2002.</center>
<center>Decided June 27, 2002.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE TENTH CIRCUIT
<p><span class="star-pagination">*823</span> <span class="star-pagination">*824</span> Thomas, J., delivered the opinion of the Court, in which Rehnquist, C. J., and Scalia, Kennedy, and Breyer, JJ., joined. Breyer, J., filed a concurring opinion, <i>post,</i> p. 838. O'Connor, J., filed a dissenting opinion, in which Souter, J., joined, <i>post,</i> p. 842. Ginsburg, J., filed a dissenting <span class="star-pagination">*825</span> opinion, in which Stevens, O'Connor, and Souter, JJ., joined, <i>post,</i>  p. 842.</p>
<p><i>Linda Maria Meoli</i> argued the cause for petitioners. With her on the briefs were <i>Stephanie J. Mather</i> and <i>William P. Bleakley.</i> </p>
<p><i>Deputy Solicitor General Clement</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Solicitor General Olson, Assistant Attorney General McCallum, Gregory G. Garre, Leonard Schaitman,</i> and <i>Lowell V. Sturgill, Jr.</i> </p>
<p><i>Graham A. Boyd</i> argued the cause for respondents. With him on the brief was <i>Steven R. Shapiro.</i><sup>[*]</sup></p>
<p>Justice Thomas, delivered the opinion of the Court.</p>
<p>The Student Activities Drug Testing Policy implemented by the Board of Education of Independent School District No. 92 of Pottawatomie County (School District) requires all students who participate in competitive extracurricular activities to submit to drug testing. Because this Policy reasonably serves the School District's important interest in detecting and preventing drug use among its students, we hold that it is constitutional.</p>
<p></p>
<h2>
<span class="star-pagination">*826</span> I</h2>
<p>The city of Tecumseh, Oklahoma, is a rural community located approximately 40 miles southeast of Oklahoma City. The School District administers all Tecumseh public schools. In the fall of 1998, the School District adopted the Student Activities Drug Testing Policy (Policy), which requires all middle and high school students to consent to drug testing in order to participate in any extracurricular activity. In practice, the Policy has been applied only to competitive extracurricular activities sanctioned by the Oklahoma Secondary Schools Activities Association, such as the Academic Team, Future Farmers of America, Future Homemakers of America, band, choir, pom pon, cheerleading, and athletics. Under the Policy, students are required to take a drug test before participating in an extracurricular activity, must submit to random drug testing while participating in that activity, and must agree to be tested at any time upon reasonable suspicion. The urinalysis tests are designed to detect only the use of illegal drugs, including amphetamines, marijuana, cocaine, opiates, and barbituates, not medical conditions or the presence of authorized prescription medications.</p>
<p>At the time of their suit, both respondents attended Tecumseh High School. Respondent Lindsay Earls was a member of the show choir, the marching band, the Academic Team, and the National Honor Society. Respondent Daniel James sought to participate in the Academic Team.<sup>[1]</sup> Together with their parents, Earls and James brought a Rev. <span class="star-pagination">*827</span> Stat. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>, action against the School District, challenging the Policy both on its face and as applied to their participation in extracurricular activities.<sup>[2]</sup> They alleged that the Policy violates the Fourth Amendment as incorporated by the Fourteenth Amendment and requested injunctive and declarative relief. They also argued that the School District failed to identify a special need for testing students who participate in extracurricular activities, and that the "Drug Testing Policy neither addresses a proven problem nor promises to bring any benefit to students or the school." App. 9.</p>
<p>Applying the principles articulated in <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646</a></span> (1995), in which we upheld the suspicionless drug testing of school athletes, the United States District Court for the Western District of Oklahoma rejected respondents' claim that the Policy was unconstitutional and granted summary judgment to the School District. The court noted that "special needs" exist in the public school context and that, although the School District did "not show a drug problem of epidemic proportions," there was a history of drug abuse starting in 1970 that presented "legitimate cause for concern." <span class="citation" data-id="2580272"><a href="/opinion/2580272/earls-ex-rel-earls-v-board-of-education-of-tecumseh-public-school/#1287" aria-description="Citation for case: Earls Ex Rel. Earls v. Board of Education of Tecumseh...">115 F. Supp. 2d 1281, 1287</a></span> (2000). The District Court also held that the Policy was effective because "[i]t can scarcely be disputed that the drug problem among the student body is effectively addressed by making sure that the large number of students participating in competitive, extracurricular activities do not use drugs." <span class="citation" data-id="2580272"><a href="/opinion/2580272/earls-ex-rel-earls-v-board-of-education-of-tecumseh-public-school/#1295" aria-description="Citation for case: Earls Ex Rel. Earls v. Board of Education of Tecumseh..."><i>Id.,</i>  at 1295</a></span>.</p>
<p>The United States Court of Appeals for the Tenth Circuit reversed, holding that the Policy violated the Fourth Amendment. The Court of Appeals agreed with the District Court that the Policy must be evaluated in the "unique environment of the school setting," but reached a different conclusion <span class="star-pagination">*828</span> as to the Policy's constitutionality. <span class="citation multiple-matches"><a href="/c/F.%203d/242/1264/">242 F. 3d 1264</a></span>, 1270 (2001). Before imposing a suspicionless drug testing program, the Court of Appeals concluded that a school "must demonstrate that there is some identifiable drug abuse problem among a sufficient number of those subject to the testing, such that testing that group of students will actually redress its drug problem." <i>Id.,</i> at 1278. The Court of Appeals then held that because the School District failed to demonstrate such a problem existed among Tecumseh students participating in competitive extracurricular activities, the Policy was unconstitutional. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./534/1015/">534 U. S. 1015</a></span> (2001), and now reverse.</p>
<p></p>
<h2>II</h2>
<p>The Fourth Amendment to the United States Constitution protects "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures." Searches by public school officials, such as the collection of urine samples, implicate Fourth Amendment interests. See <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#652" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Vernonia, supra,</i> at 652</a></span>; cf. <i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#334" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 334</a></span> (1985). We must therefore review the School District's Policy for "reasonableness," which is the touchstone of the constitutionality of a governmental search.</p>
<p>In the criminal context, reasonableness usually requires a showing of probable cause. See, <i>e. g., </i><i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#619" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602, 619</a></span> (1989). The probable-cause standard, however, "is peculiarly related to criminal investigations" and may be unsuited to determining the reasonableness of administrative searches where the "Government seeks to <i>prevent</i> the development of hazardous conditions." <i>Treasury Employees</i> v. <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#667" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656, 667-668</a></span> (1989) (internal quotation marks and citations omitted) (collecting cases). The Court has also held that a warrant and finding of probable cause are unnecessary in the public school context because such requirements "`would unduly interfere with the maintenance of the swift and informal <span class="star-pagination">*829</span> disciplinary procedures [that are] needed.' " <i><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">Vernonia, supra,</a></span></i> at 653 (quoting <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#340" aria-description="Citation for case: New Jersey v. T. L. O."><i>T. L. O., supra,</i> at 340-341</a></span>).</p>
<p>Given that the School District's Policy is not in any way related to the conduct of criminal investigations, see Part IIB, <i>infra,</i> respondents do not contend that the School District requires probable cause before testing students for drug use. Respondents instead argue that drug testing must be based at least on some level of individualized suspicion. See Brief for Respondents 12-14. It is true that we generally determine the reasonableness of a search by balancing the nature of the intrusion on the individual's privacy against the promotion of legitimate governmental interests. See <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654</a></span> (1979). But we have long held that "the Fourth Amendment imposes no irreducible requirement of [individualized] suspicion." <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#561" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 561</a></span> (1976). "[I]n certain limited circumstances, the Government's need to discover such latent or hidden conditions, or to prevent their development, is sufficiently compelling to justify the intrusion on privacy entailed by conducting such searches without any measure of individualized suspicion." <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#668" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><i>Von Raab, supra,</i>  at 668</a></span>; see also <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#624" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><i>Skinner, supra,</i> at 624</a></span>. Therefore, in the context of safety and administrative regulations, a search unsupported by probable cause may be reasonable "when `special needs, beyond the normal need for law enforcement, make the warrant and probable-cause requirement impracticable.' " <i>Griffin</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#873" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868, 873</a></span> (1987) (quoting <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#351" aria-description="Citation for case: New Jersey v. T. L. O."><i>T. L. O., supra,</i> at 351</a></span> (Blackmun, J., concurring in judgment)); see also <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#653" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Vernonia, supra,</i> at 653</a></span>; <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#619" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><i>Skinner, supra,</i> at 619</a></span>.</p>
<p>Significantly, this Court has previously held that "special needs" inhere in the public school context. See <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#653" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Vernonia, supra,</i> at 653</a></span>; <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#339" aria-description="Citation for case: New Jersey v. T. L. O."><i>T. L. O., supra,</i> at 339-340</a></span>. While schoolchildren do not shed their constitutional rights when they enter the schoolhouse, see <i>Tinker</i> v. <i>Des Moines Independent Community School Dist.,</i> <span class="citation" data-id="9423907"><a href="/opinion/107841/tinker-v-des-moines-independent-community-school-district/#506" aria-description="Citation for case: Tinker v. Des Moines Independent Community School District">393 U. S. 503, 506</a></span> (1969), "Fourth <span class="star-pagination">*830</span> Amendment rights . . . are different in public schools than elsewhere; the `reasonableness' inquiry cannot disregard the schools' custodial and tutelary responsibility for children." <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#656" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 656</a></span>. In particular, a finding of individualized suspicion may not be necessary when a school conducts drug testing.</p>
<p>In <i>Vernonia,</i> this Court held that the suspicionless drug testing of athletes was constitutional. The Court, however, did not simply authorize all school drug testing, but rather conducted a fact-specific balancing of the intrusion on the children's Fourth Amendment rights against the promotion of legitimate governmental interests. See <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#652" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>id.,</i> at 652-653</a></span>. Applying the principles of <i>Vernonia</i> to the somewhat different facts of this case, we conclude that Tecumseh's Policy is also constitutional.</p>
<p></p>
<h2>A</h2>
<p>We first consider the nature of the privacy interest allegedly compromised by the drug testing. See <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#654" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>id.,</i> at 654</a></span>. As in <i>Vernonia,</i> the context of the public school environment serves as the backdrop for the analysis of the privacy interest at stake and the reasonableness of the drug testing policy in general. See <i><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">ibid.</a></span></i> ("Central . . . is the fact that the subjects of the Policy are (1) children, who (2) have been committed to the temporary custody of the State as schoolmaster"); see also <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#665" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>id.,</i> at 665</a></span> ("The most significant element in this case is the first we discussed: that the Policy was undertaken in furtherance of the government's responsibilities, under a public school system, as guardian and tutor of children entrusted to its care"); <i><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">ibid.</a></span></i> ("[W]hen the government acts as guardian and tutor the relevant question is whether the search is one that a reasonable guardian and tutor might undertake").</p>
<p>A student's privacy interest is limited in a public school environment where the State is responsible for maintaining discipline, health, and safety. Schoolchildren are routinely required to submit to physical examinations and vaccinations <span class="star-pagination">*831</span> against disease. See <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#656" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>id.,</i> at 656</a></span>. Securing order in the school environment sometimes requires that students be subjected to greater controls than those appropriate for adults. See <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#350" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 350</a></span> (Powell, J., concurring) ("Without first establishing discipline and maintaining order, teachers cannot begin to educate their students. And apart from education, the school has the obligation to protect pupils from mistreatment by other children, and also to protect teachers themselves from violence by the few students whose conduct in recent years has prompted national concern").</p>
<p>Respondents argue that because children participating in nonathletic extracurricular activities are not subject to regular physicals and communal undress, they have a stronger expectation of privacy than the athletes tested in <i>Vernonia.</i>  See Brief for Respondents 18-20. This distinction, however, was not essential to our decision in <i>Vernonia,</i> which depended primarily upon the school's custodial responsibility and authority.<sup>[3]</sup></p>
<p>In any event, students who participate in competitive extracurricular activities voluntarily subject themselves to many of the same intrusions on their privacy as do athletes.<sup>[4]</sup><span class="star-pagination">*832</span> Some of these clubs and activities require occasional offcampus travel and communal undress. All of them have their own rules and requirements for participating students that do not apply to the student body as a whole. <span class="citation" data-id="2580272"><a href="/opinion/2580272/earls-ex-rel-earls-v-board-of-education-of-tecumseh-public-school/#1289" aria-description="Citation for case: Earls Ex Rel. Earls v. Board of Education of Tecumseh...">115 F. Supp. 2d, at 1289-1290</a></span>. For example, each of the competitive extracurricular activities governed by the Policy must abide by the rules of the Oklahoma Secondary Schools Activities Association, and a faculty sponsor monitors the students for compliance with the various rules dictated by the clubs and activities. See <span class="citation" data-id="2580272"><a href="/opinion/2580272/earls-ex-rel-earls-v-board-of-education-of-tecumseh-public-school/#1290" aria-description="Citation for case: Earls Ex Rel. Earls v. Board of Education of Tecumseh..."><i>id.,</i> at 1290</a></span>. This regulation of extracurricular activities further diminishes the expectation of privacy among schoolchildren. Cf<i>. </i><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#657" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Vernonia, supra,</i> at 657</a></span> ("Somewhat like adults who choose to participate in a closely regulated industry, students who voluntarily participate in school athletics have reason to expect intrusions upon normal rights and privileges, including privacy" (internal quotation marks omitted)). We therefore conclude that the students affected by this Policy have a limited expectation of privacy.</p>
<p></p>
<h2>B</h2>
<p>Next, we consider the character of the intrusion imposed by the Policy. See <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#658" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Vernonia, supra,</i> at 658</a></span>. Urination is "an excretory function traditionally shielded by great privacy." <i>Skinner,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#626" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 626</a></span>. But the "degree of intrusion" on one's privacy caused by collecting a urine sample "depends upon the manner in which production of the urine sample is monitored." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#658" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Vernonia, supra,</i> at 658</a></span>.</p>
<p>Under the Policy, a faculty monitor waits outside the closed restroom stall for the student to produce a sample and must "listen for the normal sounds of urination in order to guard against tampered specimens and to insure an accurate chain of custody." App. 199. The monitor then pours the sample into two bottles that are sealed and placed into a mailing pouch along with a consent form signed by the student. This procedure is virtually identical to that reviewed in <i>Vernonia,</i> except that it additionally protects privacy by <span class="star-pagination">*833</span> allowing male students to produce their samples behind a closed stall. Given that we considered the method of collection in <i>Vernonia</i> a "negligible" intrusion, <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#658" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 658</a></span>, the method here is even less problematic.</p>
<p>In addition, the Policy clearly requires that the test results be kept in confidential files separate from a student's other educational records and released to school personnel only on a "need to know" basis. Respondents nonetheless contend that the intrusion on students' privacy is significant because the Policy fails to protect effectively against the disclosure of confidential information and, specifically, that the school "has been careless in protecting that information: for example, the Choir teacher looked at students' prescription drug lists and left them where other students could see them." Brief for Respondents 24. But the choir teacher is someone with a "need to know," because during off-campus trips she needs to know what medications are taken by her students. Even before the Policy was enacted the choir teacher had access to this information. See App. 132. In any event, there is no allegation that any other student did see such information. This one example of alleged carelessness hardly increases the character of the intrusion.</p>
<p>Moreover, the test results are not turned over to any law enforcement authority. Nor do the test results here lead to the imposition of discipline or have any academic consequences. Cf. <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#658" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Vernonia, supra,</i> at 658</a></span>, and n. 2. Rather, the only consequence of a failed drug test is to limit the student's privilege of participating in extracurricular activities. Indeed, a student may test positive for drugs twice and still be allowed to participate in extracurricular activities. After the first positive test, the school contacts the student's parent or guardian for a meeting. The student may continue to participate in the activity if within five days of the meeting the student shows proof of receiving drug counseling and submits to a second drug test in two weeks. For the second positive test, the student is suspended from participation in <span class="star-pagination">*834</span> all extracurricular activities for 14 days, must complete four hours of substance abuse counseling, and must submit to monthly drug tests. Only after a third positive test will the student be suspended from participating in any extracurricular activity for the remainder of the school year, or 88 school days, whichever is longer. See App. 201-202.</p>
<p>Given the minimally intrusive nature of the sample collection and the limited uses to which the test results are put, we conclude that the invasion of students' privacy is not significant.</p>
<p></p>
<h2>C</h2>
<p>Finally, this Court must consider the nature and immediacy of the government's concerns and the efficacy of the Policy in meeting them. See <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#660" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 660</a></span>. This Court has already articulated in detail the importance of the governmental concern in preventing drug use by schoolchildren. See <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#661" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>id.,</i> at 661-662</a></span>. The drug abuse problem among our Nation's youth has hardly abated since <i>Vernonia</i> was decided in 1995. In fact, evidence suggests that it has only grown worse.<sup>[5]</sup> As in <i>Vernonia,</i> "the necessity for the State to act is magnified by the fact that this evil is being visited not just upon individuals at large, but upon children for whom it has undertaken a special responsibility of care and direction." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#662" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Id.,</i> at 662</a></span>. The health and safety risks identified in <i>Vernonia</i> apply with equal force to Tecumseh's children. Indeed, the nationwide drug epidemic makes the war against drugs a pressing concern in every school.</p>
<p>Additionally, the School District in this case has presented specific evidence of drug use at Tecumseh schools. Teachers testified that they had seen students who appeared to be <span class="star-pagination">*835</span> under the influence of drugs and that they had heard students speaking openly about using drugs. See, <i>e. g.,</i> App. 72 (deposition of Dean Rogers); <i>id.,</i> at 115 (deposition of Sheila Evans). A drug dog found marijuana cigarettes near the school parking lot. Police officers once found drugs or drug paraphernalia in a car driven by a Future Farmers of America member. And the school board president reported that people in the community were calling the board to discuss the "drug situation." See 115 F. Supp. 2d, at 1285 1286. We decline to second-guess the finding of the District Court that "[v]iewing the evidence as a whole, it cannot be reasonably disputed that the [School District] was faced with a `drug problem' when it adopted the Policy." <i>Id.,</i> at 1287.</p>
<p>Respondents consider the proffered evidence insufficient and argue that there is no "real and immediate interest" to justify a policy of drug testing nonathletes. Brief for Respondents 32. We have recognized, however, that "[a] demonstrated problem of drug abuse . . . [is] notin all cases necessary to the validity of a testing regime," but that some showing does "shore up an assertion of special need for a suspicionless general search program." <i>Chandler</i> v. <i>Miller,</i>  <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#319" aria-description="Citation for case: Chandler v. Miller">520 U. S. 305, 319</a></span> (1997). The School District has provided sufficient evidence to shore up the need for its drug testing program.</p>
<p>Furthermore, this Court has not required a particularized or pervasive drug problem before allowing the government to conduct suspicionless drug testing. For instance, in <i><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span></i> the Court upheld the drug testing of customs officials on a purely preventive basis, without any documented history of drug use by such officials. See 489 U. S., at 673. In response to the lack of evidence relating to drug use, the Court noted generally that "drug abuse is one of the most serious problems confronting our society today," and that programs to prevent and detect drug use among customs officials could not be deemed unreasonable. <i>Id.,</i> at 674; cf. <i>Skinner,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#607" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 607</a></span>, and n. 1 (noting nationwide <span class="star-pagination">*836</span> studies that identified on-the-job alcohol and drug use by railroad employees). Likewise, the need to prevent and deter the substantial harm of childhood drug use provides the necessary immediacy for a school testing policy. Indeed, it would make little sense to require a school district to wait for a substantial portion of its students to begin using drugs before it was allowed to institute a drug testing program designed to deter drug use.</p>
<p>Given the nationwide epidemic of drug use, and the evidence of increased drug use in Tecumseh schools, it was entirely reasonable for the School District to enact this particular drug testing policy. We reject the Court of Appeals' novel test that "any district seeking to impose a random suspicionless drug testing policy as a condition to participation in a school activity must demonstrate that there is some identifiable drug abuse problem among a sufficient number of those subject to the testing, such that testing that group of students will actually redress its drug problem." 242 F. 3d, at 1278. Among other problems, it would be difficult to administer such a test. As we cannot articulate a threshold level of drug use that would suffice to justify a drug testing program for schoolchildren, we refuse to fashion what would in effect be a constitutional quantum of drug use necessary to show a "drug problem."</p>
<p>Respondents also argue that the testing of nonathletes does not implicate any safety concerns, and that safety is a "crucial factor" in applying the special needs framework. Brief for Respondents 25-27. They contend that there must be "surpassing safety interests," <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#634" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><i>Skinner, supra,</i> at 634</a></span>, or "extraordinary safety and national security hazards," <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#674" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><i>Von Raab, supra,</i> at 674</a></span>, in order to override the usual protections of the Fourth Amendment. See Brief for Respondents 25-26. Respondents are correct that safety factors into the special needs analysis, but the safety interest furthered by drug testing is undoubtedly substantial for all children, athletes and nonathletes alike. We know all too well that drug <span class="star-pagination">*837</span> use carries a variety of health risks for children, including death from overdose.</p>
<p>We also reject respondents' argument that drug testing must presumptively be based upon an individualized reasonable suspicion of wrongdoing because such a testing regime would be less intrusive. See <i>id.,</i> at 12-16. In this context, the Fourth Amendment does not require a finding of individualized suspicion, see <i>supra,</i> at 829, and we decline to impose such a requirement on schools attempting to prevent and detect drug use by students. Moreover, we question whether testing based on individualized suspicion in fact would be less intrusive. Such a regime would place an additional burden on public school teachers who are already tasked with the difficult job of maintaining order and discipline. A program of individualized suspicion might unfairly target members of unpopular groups. The fear of lawsuits resulting from such targeted searches may chill enforcement of the program, rendering it ineffective in combating drug use. See <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#663" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 663-664</a></span> (offering similar reasons for why "testing based on `suspicion' of drug use would not be better, but worse"). In any case, this Court has repeatedly stated that reasonableness under the Fourth Amendment does not require employing the least intrusive means, because "[t]he logic of such elaborate less-restrictivealternative arguments could raise insuperable barriers to the exercise of virtually all search-and-seizure powers." <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 556-557, n. 12</a></span>; see also <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#624" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><i>Skinner, supra,</i> at 624</a></span> ("[A] showing of individualized suspicion is not a constitutional floor, below which a search must be presumed unreasonable").</p>
<p>Finally, we find that testing students who participate in extracurricular activities is a reasonably effective means of addressing the School District's legitimate concerns in preventing, deterring, and detecting drug use. While in <i>Vernonia</i> there might have been a closer fit between the testing of athletes and the trial court's finding that the drug problem <span class="star-pagination">*838</span> was "fueled by the `role model' effect of athletes' drug use," such a finding was not essential to the holding. <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#663" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 663</a></span>; cf. <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#684" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>id.,</i> at 684-685</a></span> (O'Connor, J., dissenting) (questioning the extent of the drug problem, especially as applied to athletes). <i>Vernonia</i> did not require the school to test the group of students most likely to use drugs, but rather considered the constitutionality of the program in the context of the public school's custodial responsibilities. Evaluating the Policy in this context, we conclude that the drug testing of Tecumseh students who participate in extracurricular activities effectively serves the School District's interest in protecting the safety and health of its students.</p>
<p></p>
<h2>III</h2>
<p>Within the limits of the Fourth Amendment, local school boards must assess the desirability of drug testing schoolchildren. In upholding the constitutionality of the Policy, we express no opinion as to its wisdom. Rather, we hold only that Tecumseh's Policy is a reasonable means of furthering the School District's important interest in preventing and deterring drug use among its schoolchildren. Accordingly, we reverse the judgment of the Court of Appeals.</p>
<blockquote>
<i>It is so ordered.</i>  Justice Breyer, concurring. I agree with the Court that <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646</a></span> (1995), governs this case and requires reversal of the Tenth Circuit's decision. The school's drug testing program addresses a serious national problem by focusing upon demand, avoiding the use of criminal or disciplinary sanctions, and relying upon professional counseling and treatment. See App. 201-202. In my view, this program does not violate the Fourth Amendment's prohibition of "unreasonable searches and seizures." I reach this conclusion primarily for the reasons given by the Court, but I would <span class="star-pagination">*839</span> emphasize several underlying considerations, which I understand to be consistent with the Court's opinion.</blockquote>
<p></p>
<h2>I</h2>
<p>In respect to the school's need for the drug testing program, I would emphasize the following: First, the drug problem in our Nation's schools is serious in terms of size, the kinds of drugs being used, and the consequences of that use both for our children and the rest of us. See, <i>e. g.,</i> White House Nat. Drug Control Strategy 25 (Feb. 2002) (drug abuse leads annually to about 20,000 deaths, $160 billion in economic costs); Department of Health and Human Services, L. Johnston et al., Monitoring the Future: National Results on Adolescent Drug Use, Overview of Key Findings 5 (2001) (Monitoring the Future) (more than one-third of all students have used illegal drugs before completing the eighth grade; more than half before completing high school); <i><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">ibid.</a></span></i> (about 30% of all students use drugs <i>other than marijuana</i> prior to completing high school (emphasis added)); National Center on Addiction and Substance Abuse, Malignant Neglect: Substance Abuse and America's Schools 15 (Sept. 2001) (Malignant Neglect) (early use leads to later drug dependence); Nat. Drug Control Strategy, <i>supra,</i> at 1 (same).</p>
<p>Second, the government's emphasis upon supply side interdiction apparently has not reduced teenage use in recent years. Compare R. Perl, CRS Issue Brief for Congress, Drug Control: International Policy and Options CRS-1 (Dec. 12, 2001) (supply side programs account for 66% of the federal drug control budget), with Partnership for a Drug-Free America, 2001 Partnership Attitude Tracking Study: Key Findings 1 (showing increase in teenage drug use in early 1990's, peak in 1997, holding steady thereafter); 2000-2001 PRIDE National Summary: Alcohol, Tobacco, Illicit Drugs, Violence and Related Behaviors, Grades 6 thru 12 (Jul. 16, 2002), http://www.pridesurveys.com/main/supportfiles/ natsum00.pdf, p. 15 (slight rise in high school drug use in <span class="star-pagination">*840</span> 2000-2001); Monitoring the Future, Table 1 (lifetime prevalence of drug use increasing over last 10 years).</p>
<p>Third, public school systems must find effective ways to deal with this problem. Today's public expects its schools not simply to teach the fundamentals, but "to shoulder the burden of feeding students breakfast and lunch, offering before and after school child care services, and providing medical and psychological services," all in a school environment that is safe and encourages learning. Brief for National School Boards Association et al. as <i>Amici Curiae</i> 3-4. See also <i>Bethel School Dist. No. 403</i> v. <i>Fraser,</i> <span class="citation" data-id="9430701"><a href="/opinion/111754/bethel-school-district-no-403-v-fraser/#681" aria-description="Citation for case: Bethel School District No. 403 v. Fraser">478 U. S. 675, 681</a></span> (1986) (Schools "`prepare pupils for citizenship in the Republic [and] inculcate the habits and manners of civility as values in themselves conductive to happiness and as indispensable to the practice of self-government in the community and the nation' ") (quoting C. Beard &amp; M. Beard, New Basic History of the United States 228 (1968)). The law itself recognizes these responsibilities with the phrase <i>in loco parentis</i> a phrase that draws its legal force primarily from the needs of younger students (who here are necessarily grouped together with older high school students) and which reflects, not that a child or adolescent lacks an interest in privacy, but that a child's or adolescent's school-related privacy interest, when compared to the privacy interests of an adult, has different dimensions. Cf. <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#654" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Vernonia, supra,</i> at 654-655</a></span>. A public school system that fails adequately to carry out its responsibilities may well see parents send their children to private or parochial school insteadwith help from the State. See <i>Zelman</i> v. <i>Simmons-Harris, ante,</i> p. 639.</p>
<p>Fourth, the program at issue here seeks to discourage demand for drugs by changing the school's environment in order to combat the single most important factor leading schoolchildren to take drugs, namely, peer pressure. Malignant Neglect 4 (students "whose friends use illicit drugs are more than 10 times likelier to use illicit drugs than those whose friends do not"). It offers the adolescent a nonthreatening <span class="star-pagination">*841</span> reason to decline his friend's drug-use invitations, namely, that he intends to play baseball, participate in debate, join the band, or engage in any one of half a dozen useful, interesting, and important activities.</p>
<p></p>
<h2>II</h2>
<p>In respect to the privacy-related burden that the drug testing program imposes upon students, I would emphasize the following: First, not everyone would agree with this Court's characterization of the privacy-related significance of urine sampling as "`negligible.' " <i>Ante,</i> at 833 (quoting <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#658" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 658</a></span>). Some find the procedure no more intrusive than a routine medical examination, but others are seriously embarrassed by the need to provide a urine sample with someone listening "outside the closed restroom stall," <i>ante,</i> at 832. When trying to resolve this kind of close question involving the interpretation of constitutional values, I believe it important that the school board provided an opportunity for the airing of these differences at public meetings designed to give the entire community "the opportunity to be able to participate" in developing the drug policy. App. 87. The board used this democratic, participatory process to uncover and to resolve differences, giving weight to the fact that the process, in this instance, revealed little, if any, objection to the proposed testing program.</p>
<p>Second, the testing program avoids subjecting the entire school to testing. And it preserves an option for a conscientious objector. He can refuse testing while paying a price (nonparticipation) that is serious, but less severe than expulsion from the school.</p>
<p>Third, a contrary reading of the Constitution, as requiring "individualized suspicion" in this public school context, could well lead schools to push the boundaries of "individualized suspicion" to its outer limits, using subjective criteria that may "unfairly target members of unpopular groups," <i>ante,</i>  at 837, or leave those whose behavior is slightly abnormal <span class="star-pagination">*842</span> stigmatized in the minds of others. See Belsky, Random vs. Suspicion-Based Drug Testing in the Public SchoolsA Surprising Civil Liberties Dilemma, <span class="citation no-link">27 Okla. City U. L. Rev. 1</span>, 20-21 (forthcoming 2002) (listing court-approved factors justifying suspicion-based drug testing, including tiredness, overactivity, quietness, boisterousness, sloppiness, excessive meticulousness, and tardiness). If so, direct application of the Fourth Amendment's prohibition against "unreasonable searches and seizures" will further that Amendment's liberty-protecting objectives at least to the same extent as application of the mediating "individualized suspicion" test, where, as here, the testing program is neither criminal nor disciplinary in nature.</p>
<p></p>
<h2>* * *</h2>
<p>I cannot know whether the school's drug testing program will work. But, in my view, the Constitution does not prohibit the effort. Emphasizing the considerations I have mentioned, along with others to which the Court refers, I conclude that the school's drug testing program, constitutionally speaking, is not "unreasonable." And I join the Court's opinion.</p>
<p>Justice O'Connor, with whom Justice Souter joins, dissenting.</p>
<p>I dissented in <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646</a></span> (1995), and continue to believe that case was wrongly decided. Because <i>Vernonia</i> is now this Court's precedent, and because I agree that petitioners' program fails even under the balancing approach adopted in that case, I join Justice Ginsburg's dissent.</p>
<p>Justice Ginsburg, with whom Justice Stevens, Justice O'Connor, and Justice Souter join, dissenting.</p>
<p>Seven years ago, in <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i>  <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646</a></span> (1995), this Court determined that a school <span class="star-pagination">*843</span> district's policy of randomly testing the urine of its student athletes for illicit drugs did not violate the Fourth Amendment. In so ruling, the Court emphasized that drug use "increase[d] the risk of sports-related injury" and that Vernonia's athletes were the "leaders" of an aggressive local "drug culture" that had reached "`epidemic proportions.' " <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#649" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Id.,</i> at 649</a></span>. Today, the Court relies upon <i>Vernonia</i> to permit a school district with a drug problem its superintendent repeatedly described as "not . . . major," see App. 180, 186, 191, to test the urine of an academic team member solely by reason of her participation in a nonathletic, competitive extracurricular activityparticipation associated with neither special dangers from, nor particular predilections for, drug use.</p>
<p>"[T]he legality of a search of a student," this Court has instructed, "should depend simply on the reasonableness, under all the circumstances, of the search." <i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#341" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 341</a></span> (1985). Although "`special needs' inhere in the public school context," see <i>ante,</i> at 829 (quoting <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#653" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 653</a></span>), those needs are not so expansive or malleable as to render reasonable any program of student drug testing a school district elects to install. The particular testing program upheld today is not reasonable; it is capricious, even perverse: Petitioners' policy targets for testing a student population least likely to be at risk from illicit drugs and their damaging effects. I therefore dissent.</p>
<p></p>
<h2>I</h2>
<p></p>
<h2>A</h2>
<p>A search unsupported by probable cause nevertheless may be consistent with the Fourth Amendment "when special needs, beyond the normal need for law enforcement, make the warrant and probable-cause requirement impracticable." <i>Griffin</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#873" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868, 873</a></span> (1987) (internal quotation marks omitted). In <i>Vernonia,</i> this Court made clear that "such `special needs' .. . exist in the public school context." <span class="star-pagination">*844</span> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 653</a></span> (quoting <i>Griffin,</i> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#873" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S., at 873</a></span>). The Court observed:</p>
<blockquote>"[W]hile children assuredly do not `shed their constitutional rights . . . at the schoolhouse gate,' <i>Tinker</i> v. <i>Des</i>  <i>Moines Independent Community School Dist.,</i> <span class="citation" data-id="9423907"><a href="/opinion/107841/tinker-v-des-moines-independent-community-school-district/#506" aria-description="Citation for case: Tinker v. Des Moines Independent Community School District">393 U. S. 503, 506</a></span> (1969), the nature of those rights is what is appropriate for children in school. . . . Fourth Amendment rights, no less than First and Fourteenth Amendment rights, are different in public schools than elsewhere; the `reasonableness' inquiry cannot disregard the schools' custodial and tutelary responsibility for children." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#655" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 655-656</a></span> (other citations omitted). The <i>Vernonia</i> Court concluded that a public school district facing a disruptive and explosive drug abuse problem sparked by members of its athletic teams had "special needs" that justified suspicionless testing of district athletes as a condition of their athletic participation.</blockquote>
<p>This case presents circumstances dispositively different from those of <i>Vernonia.</i> True, as the Court stresses, Tecumseh students participating in competitive extracurricular activities other than athletics share two relevant characteristics with the athletes of <i>Vernonia.</i> First, both groups attend public schools. "[O]ur decision in <i>Vernonia,</i> " the Court states, "depended primarily upon the school's custodial responsibility and authority." <i>Ante,</i> at 831; see also <i>ante,</i>  at 840 (Breyer, J., concurring) (school districts act <i>in loco parentis</i> ). Concern for student health and safety is basic to the school's caretaking, and it is undeniable that "drug use carries a variety of health risks for children, including death from overdose." <i>Ante,</i> at 836-837 (majority opinion).</p>
<p>Those risks, however, are present for <i>all</i> schoolchildren. <i>Vernonia</i> cannot be read to endorse invasive and suspicionless drug testing of all students upon any evidence of drug use, solely because drugs jeopardize the life and health of those who use them. Many children, like many adults, engage <span class="star-pagination">*845</span> in dangerous activities on their own time; that the children are enrolled in school scarcely allows government to monitor all such activities. If a student has a reasonable subjective expectation of privacy in the personal items she brings to school, see <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#338" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 338-339</a></span>, surely she has a similar expectation regarding the chemical composition of her urine. Had the <i>Vernonia</i> Court agreed that public school attendance, in and of itself, permitted the State to test each student's blood or urine for drugs, the opinion in <i>Vernonia</i> could have saved many words. See, <i>e. g.,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#662" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 662</a></span> ("[I]t must not be lost sight of that [the Vernonia School District] program is directed . . . to drug use by school athletes, where the risk of immediate physical harm to the drug user or those with whom he is playing his sport is particularly high.").</p>
<p>The second commonality to which the Court points is the voluntary character of both interscholastic athletics and other competitive extracurricular activities. "By choosing to `go out for the team,' [school athletes] voluntarily subject themselves to a degree of regulation even higher than that imposed on students generally." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#657" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Id.,</i> at 657</a></span>. Comparably, the Court today observes, "students who participate in competitive extracurricular activities voluntarily subject themselves to" additional rules not applicable to other students. <i>Ante,</i> at 831.</p>
<p>The comparison is enlightening. While extracurricular activities are "voluntary" in the sense that they are not required for graduation, they are part of the school's educational program; for that reason, the petitioner (hereinafter School District) is justified in expending public resources to make them available. Participation in such activities is a key component of school life, essential in reality for students applying to college, and, for all participants, a significant contributor to the breadth and quality of the educational experience. See Brief for Respondents 6; Brief for American Academy of Pediatrics et al. as <i>Amici Curiae</i> 8-9. Students <span class="star-pagination">*846</span> "volunteer" for extracurricular pursuits in the same way they might volunteer for honors classes: They subject themselves to additional requirements, but they do so in order to take full advantage of the education offered them. Cf. <i>Lee</i>  v. <i>Weisman,</i> <span class="citation" data-id="9432656"><a href="/opinion/112779/lee-v-weisman/#595" aria-description="Citation for case: Lee v. Weisman">505 U. S. 577, 595</a></span> (1992) ("Attendance may not be required by official decree, yet it is apparent that a student is not free to absent herself from the graduation exercise in any real sense of the term `voluntary,' for absence would require forfeiture of those intangible benefits which have motivated the student through youth and all her high school years.").</p>
<p>Voluntary participation in athletics has a distinctly different dimension: Schools regulate student athletes discretely because competitive school sports by their nature require communal undress and, more important, expose students to physical risks that schools have a duty to mitigate. For the very reason that schools cannot offer a program of competitive athletics without intimately affecting the privacy of students, <i>Vernonia</i> reasonably analogized school athletes to "adults who choose to participate in a closely regulated industry." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#657" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 657</a></span> (internal quotation marks omitted). Industries fall within the closely regulated category when the nature of their activities requires substantial government oversight. See, <i>e. g., </i><i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell">406 U. S. 311, 315-316</a></span> (1972). Interscholastic athletics similarly require close safety and health regulation; a school's choir, band, and academic team do not.</p>
<p>In short, <i>Vernonia</i> applied, it did not repudiate, the principle that "the legality of a search of a student should depend simply on the reasonableness, <i>under all the circumstances,</i>  of the search." <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#341" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 341</a></span> (emphasis added). Enrollment in a public school, and election to participate in school activities beyond the bare minimum that the curriculum requires, are indeed factors relevant to reasonableness, but they do not on their own justify intrusive, suspicionless searches. <i>Vernonia,</i> accordingly, did not rest upon these <span class="star-pagination">*847</span> factors; instead, the Court performed what today's majority aptly describes as a "fact-specific balancing," <i>ante,</i> at 830. Balancing of that order, applied to the facts now before the Court, should yield a result other than the one the Court announces today.</p>
<p></p>
<h2>B</h2>
<p><i>Vernonia</i> initially considered "the nature of the privacy interest upon which the search [there] at issue intrude[d]." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#654" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 654</a></span>. The Court emphasized that student athletes' expectations of privacy are necessarily attenuated:</p>
<blockquote>"Legitimate privacy expectations are even less with regard to student athletes. School sports are not for the bashful. They require `suiting up' before each practice or event, and showering and changing afterwards. Public school locker rooms, the usual sites for these activities, are not notable for the privacy they afford. The locker rooms in Vernonia are typical: No individual dressing rooms are provided; shower heads are lined up along a wall, unseparated by any sort of partition or curtain; not even all the toilet stalls have doors. . . . [T]here is an element of communal undress inherent in athletic participation." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#657" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Id.,</i> at 657</a></span> (internal quotation marks omitted). Competitive extracurricular activities other than athletics, however, serve students of all manner: the modest and shy along with the bold and uninhibited. Activities of the kind plaintiff-respondent Lindsay Earls pursuedchoir, show choir, marching band, and academic teamafford opportunities to gain self-assurance, to "come to know faculty members in a less formal setting than the typical classroom," and to acquire "positive social supports and networks [that] play a critical role in periods of heightened stress." Brief for American Academy of Pediatrics et al. as <i>Amici Curiae</i> 13.</blockquote>
<p>On "occasional out-of-town trips," students like Lindsay Earls "must sleep together in communal settings and use <span class="star-pagination">*848</span> communal bathrooms." <span class="citation multiple-matches"><a href="/c/F.%203d/242/1264/">242 F. 3d 1264</a></span>, 1275 (CA10 2001). But those situations are hardly equivalent to the routine communal undress associated with athletics; the School District itself admits that when such trips occur, "public-like restroom facilities," which presumably include enclosed stalls, are ordinarily available for changing, and that "more modest students" find other ways to maintain their privacy. Brief for Petitioners 34.<sup>[1]</sup></p>
<p>After describing school athletes' reduced expectation of privacy, the <i>Vernonia</i> Court turned to "the character of the intrusion . . . complained of." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#658" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 658</a></span>. Observing that students produce urine samples in a bathroom stall with a coach or teacher outside, <i>Vernonia</i> typed the privacy interests compromised by the process of obtaining samples "negligible." <i><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">Ibid.</a></span></i> As to the required pretest disclosure of prescription medications taken, the Court assumed that "the School District would have permitted [a student] to provide the requested information in a confidential mannerfor example, in a sealed envelope delivered to the testing lab." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#660" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Id.,</i> at 660</a></span>. On that assumption, the Court concluded that Vernonia's athletes faced no significant invasion of privacy.</p>
<p>In this case, however, Lindsay Earls and her parents allege that the School District handled personal information collected under the policy carelessly, with little regard for its confidentiality. Information about students' prescription drug use, they assert, was routinely viewed by Lindsay's choir teacher, who left files containing the information unlocked and unsealed, where others, including students, could see them; and test results were given out to all activity sponsors whether or not they had a clear "need to know." See <span class="star-pagination">*849</span> Brief for Respondents 6, 24; App. 105-106, 131. But see <i>id.,</i>  at 199 (policy requires that "[t]he medication list shall be submitted to the lab in a sealed and confidential envelope and shall not be viewed by district employees").</p>
<p>In granting summary judgment to the School District, the District Court observed that the District's "[p]olicy expressly provides for confidentiality of test results, and the Court must assume that the confidentiality provisions will be honored." <span class="citation" data-id="2580272"><a href="/opinion/2580272/earls-ex-rel-earls-v-board-of-education-of-tecumseh-public-school/#1293" aria-description="Citation for case: Earls Ex Rel. Earls v. Board of Education of Tecumseh...">115 F. Supp. 2d 1281, 1293</a></span> (WD Okla. 2000). The assumption is unwarranted. Unlike <i>Vernonia,</i> where the District Court held a bench trial before ruling in the School District's favor, this case was decided by the District Court on summary judgment. At that stage, doubtful matters should not have been resolved in favor of the judgment seeker. See <i>United States</i> v. <i>Diebold, Inc.,</i> <span class="citation" data-id="106395"><a href="/opinion/106395/united-states-v-diebold-inc/#655" aria-description="Citation for case: United States v. Diebold, Inc.">369 U. S. 654, 655</a></span> (1962) <i>(per curiam)</i> ("On summary judgment the inferences to be drawn from the underlying facts contained in [affidavits, attached exhibits, and depositions] must be viewed in the light most favorable to the party opposing the motion."); see also 10A C. Wright, A. Miller, &amp; M. Kane, Federal Practice and Procedure § 2716, pp. 274-277 (3d ed. 1998).</p>
<p>Finally, the "nature and immediacy of the governmental concern," <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#660" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 660</a></span>, faced by the Vernonia School District dwarfed that confronting Tecumseh administrators. Vernonia initiated its drug testing policy in response to an alarming situation: "[A] large segment of the student body, particularly those involved in interscholastic athletics, was in a state of rebellion . . . fueled by alcohol and drug abuse as well as the student[s'] misperceptions about the drug culture." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#649" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Id.,</i> at 649</a></span> (internal quotation marks omitted). Tecumseh, by contrast, repeatedly reported to the Federal Government during the period leading up to the adoption of the policy that "types of drugs [other than alcohol and tobacco] including controlled dangerous substances, are present [in the schools] but have not identified themselves as major problems at this time." 1998-1999 Tecumseh <span class="star-pagination">*850</span> School's Application for Funds under the Safe and DrugFree Schools and Communities Program, reprinted at App. 191; accord, 1996-1997 Application, reprinted at App. 186; 1995-1996 Application, reprinted at App. 180.<sup>[2]</sup> As the Tenth Circuit observed, "without a demonstrated drug abuse problem among the group being tested, the efficacy of the District's solution to its perceived problem is . . . greatly diminished." 242 F. 3d, at 1277.</p>
<p>The School District cites <i>Treasury Employees</i> v. <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#673" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656, 673-674</a></span> (1989), in which this Court permitted random drug testing of customs agents absent "any perceived drug problem among Customs employees," given that "drug abuse is one of the most serious problems confronting our society today." See also <i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#607" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602, 607</a></span>, and n. 1 (1989) (upholding random drug and alcohol testing of railway employees based upon industry-wide, rather than railwayspecific, evidence of drug and alcohol problems). The tests in <i><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span></i> and <i>Railway Labor Executives,</i> however, were installed to avoid enormous risks to the lives and limbs of others, not dominantly in response to the health risks to users invariably present in any case of drug use. See <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#674" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 674</a></span> (drug use by customs agents involved in drug interdiction creates "extraordinary safety and national security hazards"); <i>Railway Labor Executives,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#628" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 628</a></span> (railway operators "discharge duties fraught with such risks of injury to others that even a momentary lapse of attention can have disastrous consequences"); see <span class="star-pagination">*851</span> also <i>Chandler</i> v. <i>Miller,</i> <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#321" aria-description="Citation for case: Chandler v. Miller">520 U. S. 305, 321</a></span> (1997) ("<i>Von Raab</i>  must be read in its unique context").</p>
<p>Not only did the Vernonia and Tecumseh districts confront drug problems of distinctly different magnitudes, they also chose different solutions: Vernonia limited its policy to athletes; Tecumseh indiscriminately subjected to testing all participants in competitive extracurricular activities. Urging that "the safety interest furthered by drug testing is undoubtedly substantial for all children, athletes and nonathletes alike," <i>ante,</i> at 836, the Court cuts out an element essential to the <i>Vernonia</i> judgment. Citing medical literature on the effects of combining illicit drug use with physical exertion, the <i>Vernonia</i> Court emphasized that "the particular drugs screened by [Vernonia's] Policy have been demonstrated to pose substantial physical risks to athletes." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#662" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 662</a></span>; see also <i><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">id.</a></span></i> , at 666 (Ginsburg, J., concurring) (<i>Vernonia</i> limited to "those seeking to engage with others in team sports"). We have since confirmed that these special risks were necessary to our decision in <i>Vernonia.</i> See <i>Chandler,</i> <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#317" aria-description="Citation for case: Chandler v. Miller">520 U. S., at 317</a></span> (<i>Vernonia</i> "emphasized the importance of deterring drug use by schoolchildren and the risk of injury a drug-using student athlete cast on himself and those engaged with him on the playing field"); see also <i>Ferguson</i> v. <i>Charleston,</i> <span class="citation" data-id="9434054"><a href="/opinion/118414/ferguson-v-city-of-charleston/#87" aria-description="Citation for case: Ferguson v. City of Charleston">532 U. S. 67, 87</a></span> (2001) (Kennedy, J., concurring) (Vernonia's policy had goal of "`[d]eterring drug use by our Nation's schoolchildren,' and particularly by student-athletes, because `the risk of immediate physical harm to the drug user or those with whom he is playing his sport is particularly high' ") (quoting <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#661" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 661-662</a></span>).</p>
<p>At the margins, of course, no policy of <i>random</i> drug testing is perfectly tailored to the harms it seeks to address. The School District cites the dangers faced by members of the band, who must "perform extremely precise routines with heavy equipment and instruments in close proximity to other students," and by Future Farmers of America, who <span class="star-pagination">*852</span> "are required to individually control and restrain animals as large as 1500 pounds." Brief for Petitioners 43. For its part, the United States acknowledges that "the linebacker faces a greater risk of serious injury if he takes the field under the influence of drugs than the drummer in the halftime band," but parries that "the risk of injury to a student who is under the influence of drugs while playing golf, cross country, or volleyball (sports covered by the policy in <i>Vernonia</i> ) is scarcely any greater than the risk of injury to a student . . . handling a 1500-pound steer (as [Future Farmers of America] members do) or working with cutlery or other sharp instruments (as [Future Homemakers of America] members do)." Brief for United States as <i>Amicus Curiae</i>  18. One can demur to the Government's view of the risks drug use poses to golfers, cf. <i>PGA TOUR, Inc.</i> v. <i>Martin,</i>  <span class="citation" data-id="9434091"><a href="/opinion/118432/pga-tour-inc-v-martin/#687" aria-description="Citation for case: PGA Tour, Inc. v. Martin">532 U. S. 661, 687</a></span> (2001) ("golf is a low intensity activity"), for golfers were surely as marginal among the linebackers, sprinters, and basketball players targeted for testing in Vernonia as steer-handlers are among the choristers, musicians, and academic-team members subject to urinalysis in Tecumseh.<sup>[3]</sup> Notwithstanding nightmarish images of out-of-control flatware, livestock run amok, and colliding tubas disturbing the peace and quiet of Tecumseh, the great majority of students the School District seeks to test in truth are engaged in activities that are not safety sensitive to an unusual degree. There is a difference between imperfect tailoring and no tailoring at all.</p>
<p>The Vernonia district, in sum, had two good reasons for testing athletes: Sports team members faced special health risks and they "were the leaders of the drug culture." <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#649" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 649</a></span>. No similar reason, and no other tenable justification, explains Tecumseh's decision to target <span class="star-pagination">*853</span> for testing all participants in every competitive extracurricular activity. See <i>Chandler,</i> <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#319" aria-description="Citation for case: Chandler v. Miller">520 U. S., at 319</a></span> (drug testing candidates for office held incompatible with Fourth Amendment because program was "not well designed to identify candidates who violate antidrug laws").</p>
<p>Nationwide, students who participate in extracurricular activities are significantly less likely to develop substance abuse problems than are their less-involved peers. See, <i>e. g.,</i>  N. Zill, C. Nord, &amp; L. Loomis, Adolescent Time Use, Risky Behavior, and Outcomes 52 (1995) (tenth graders "who reported spending no time in school-sponsored activities were . . . 49 percent more likely to have used drugs" than those who spent 1-4 hours per week in such activities). Even if students might be deterred from drug use in order to preserve their extracurricular eligibility, it is at least as likely that other students might forgo their extracurricular involvement in order to avoid detection of their drug use. Tecumseh's policy thus falls short doubly if deterrence is its aim: It invades the privacy of students who need deterrence least, and risks steering students at greatest risk for substance abuse away from extracurricular involvement that potentially may palliate drug problems.<sup>[4]</sup></p>
<p>To summarize, this case resembles <i>Vernonia</i> only in that the School Districts in both cases conditioned engagement in activities outside the obligatory curriculum on random subjection to urinalysis. The defining characteristics of the two programs, however, are entirely dissimilar. The Vernonia district sought to test a subpopulation of students distinguished by their reduced expectation of privacy, their special <span class="star-pagination">*854</span> susceptibility to drug-related injury, and their heavy involvement with drug use. The Tecumseh district seeks to test a much larger population associated with none of these factors. It does so, moreover, without carefully safeguarding student confidentiality and without regard to the program's untoward effects. A program so sweeping is not sheltered by <i>Vernonia;</i> its unreasonable reach renders it impermissible under the Fourth Amendment.</p>
<p></p>
<h2>II</h2>
<p>In <i><span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/" aria-description="Citation for case: Chandler v. Miller">Chandler</a></span>,</i> this Court inspected "Georgia's requirement that candidates for state office pass a drug test"; we held that the requirement "d[id] not fit within the closely guarded category of constitutionally permissible suspicionless searches." <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#309" aria-description="Citation for case: Chandler v. Miller">520 U. S., at 309</a></span>. Georgia's testing prescription, the record showed, responded to no "concrete danger," <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#319" aria-description="Citation for case: Chandler v. Miller"><i>id.,</i> at 319</a></span>, was supported by no evidence of a particular problem, and targeted a group not involved in "high-risk, safety-sensitive tasks," <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#321" aria-description="Citation for case: Chandler v. Miller"><i>id.,</i> at 321-322</a></span>. We concluded:</p>
<blockquote>"What is left, after close review of Georgia's scheme, is the image the State seeks to project. By requiring candidates for public office to submit to drug testing, Georgia displays its commitment to the struggle against drug abuse. . . . The need revealed, in short, is symbolic, not `special,' as that term draws meaning from our case law." <i><span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/" aria-description="Citation for case: Chandler v. Miller">Ibid.</a></span></i>  Close review of Tecumseh's policy compels a similar conclusion. That policy was not shown to advance the "`special needs' [existing] in the public school context [to maintain] . . . swift and informal disciplinary procedures . . . [and] order in the schools," <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#653" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 653</a></span> (internal quotation marks omitted). See <i>supra,</i> at 846-848, 849 853. What is left is the School District's undoubted purpose to heighten awareness of its abhorrence of, and strong stand against, drug abuse. But the desire to augment communication <span class="star-pagination">*855</span> of this message does not trump the right of persons even of children within the schoolhouse gateto be "secure in their persons . . . against unreasonable searches and seizures." U. S. Const., Amdt. 4.</blockquote>
<p>In <i><span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/" aria-description="Citation for case: Chandler v. Miller">Chandler</a></span>,</i> the Court referred to a pathmarking dissenting opinion in which "Justice Brandeis recognized the importance of teaching by example: `Our Government is the potent, the omnipresent teacher. For good or for ill, it teaches the whole people by its example.' " <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/" aria-description="Citation for case: Chandler v. Miller">520 U. S., at 322</a></span> (quoting <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#485" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 485</a></span> (1928)). That wisdom should guide decisionmakers in the instant case: The government is nowhere more a teacher than when it runs a public school.</p>
<p>It is a sad irony that the petitioning School District seeks to justify its edict here by trumpeting "the schools' custodial and tutelary responsibility for children." <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#656" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 656</a></span>. In regulating an athletic program or endeavoring to combat an exploding drug epidemic, a school's custodial obligations may permit searches that would otherwise unacceptably abridge students' rights. When custodial duties are not ascendant, however, schools' tutelary obligations to their students require them to "teach by example" by avoiding symbolic measures that diminish constitutional protections. "That [schools] are educating the young for citizenship is reason for scrupulous protection of Constitutional freedoms of the individual, if we are not to strangle the free mind at its source and teach youth to discount important principles of our government as mere platitudes." <i>West Virginia Bd. of Ed.</i> v. <i>Barnette,</i> <span class="citation" data-id="9419378"><a href="/opinion/103870/west-virginia-state-board-of-education-v-barnette/#637" aria-description="Citation for case: West Virginia State Board of Education v. Barnette">319 U. S. 624, 637</a></span> (1943).</p>
<p></p>
<h2>* * *</h2>
<p>For the reasons stated, I would affirm the judgment of the Tenth Circuit declaring the testing policy at issue unconstitutional.</p>
<h2>NOTES</h2>
<p>[*]   A brief of <i>amici curiae</i> urging reversal was filed for the Washington Legal Foundation et al. by <i>Richard Willard, Daniel J. Popeo,</i> and <i>Richard A. Samp.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the American Academy of Pediatrics et al. by <i>David T. Goldberg</i> and <i>Daniel N. Abrahamson;</i> for Jean Burkett et al. by <i>Craig Goldblatt;</i> for the Juvenile Law Center et al. by <i>Marsha L. Levick;</i> for the National Association of Criminal Defense Lawyers et al. by <i>John Wesley Hall, Jr., Lisa B. Kemler, Timothy Lynch,</i> and <i>Kevin B. Zeese;</i> and for the Rutherford Institute by <i>John W. Whitehead, Steven H. Aden,</i> and <i>Jamin B. Raskin.</i> </p>
<p>Briefs of <i>amici curiae</i> were filed for the Drug-Free Schools Coalition et al. by <i>David G. Evans;</i> for the National School Boards Association et al. by <i>Julie K. Underwood, Christopher B. Gilbert,</i> and <i>Thomas E. Wheeler;</i>  and for Professor Akhil Reed Amar et al. by <i>Julia M. Carpenter.</i> </p>
<p>[1]  The District Court noted that the School District's allegations concerning Daniel James called his standing to sue into question because his failing grades made him ineligible to participate in any interscholastic competition.See <span class="citation" data-id="2580272"><a href="/opinion/2580272/earls-ex-rel-earls-v-board-of-education-of-tecumseh-public-school/" aria-description="Citation for case: Earls Ex Rel. Earls v. Board of Education of Tecumseh...">115 F. Supp. 2d 1281, 1282, n. 1</a></span> (WD Okla. 2000).The court noted,however, that the disputeneed not be resolved because Lindsay Earls had standing, and therefore the court was required to address the constitution a lity of the drug testing policy. See <i><span class="citation" data-id="2580272"><a href="/opinion/2580272/earls-ex-rel-earls-v-board-of-education-of-tecumseh-public-school/" aria-description="Citation for case: Earls Ex Rel. Earls v. Board of Education of Tecumseh...">ibid.</a></span></i> Because we are likewise satisfied that Earls has standing, we need not address whether James also has standing.</p>
<p>[2]  The respondents did not challenge the Policy either as it applies to athletes or as it provides for drug testing upon reasonable, individualized suspicion. See App. 28.</p>
<p>[3]  Justice Ginsburg argues that <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i>  <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646</a></span> (1995), depended on the fact that the drug testing program applied only to student athletes. But even the passage cited by the dissent manifests the supplemental nature of this factor, as the Court in <i>Vernonia</i> stated that "[l]egitimate privacy expectations are <i>even less</i> with regard to student athletes." See <i>post,</i> at 847 (quoting <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#657" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 657</a></span>) (emphasis added). In upholding the drug testing program in <i>Vernonia,</i> we considered the school context "[c]entral" and "[t]he most significant element." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#654" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Id.,</i> at 654, 665</a></span>. This hefty weight on the side of the school's balance applies with similar force in this case even though we undertake a separate balancing with regard to this particular program.</p>
<p>[4]  Justice Ginsburg's observations with regard to extracurricular activities apply with equal force to athletics. See <i>post,</i> at 845 ("Participation in such [extracurricular] activities is a key component of school life, essential in reality for students applying to college, and, for all participants, a significant contributor to the breadth and quality of the educational experience").</p>
<p>[5]  For instance, the number of 12th graders using any illicitdrug increased from 48.4 percent in 1995 to 53.9 percent in 2001. The number of 12th graders reporting they had used marijuana jumped from 41.7 percent to 49.0 percent during that same period. See Department of Health and Human Services, Monitoring the Future: National Results on Adolescent Drug Use, Overview of Key Findings (2001) (Table 1).</p>
<p>[1]  According to Tecumseh's choir teacher, choir participants who chose not to wear their choir uniforms to school on the days of competitions could change either in "a rest room in a building" or on the bus, where "[m]any of them have figured out how to [change] without having [anyone] . . . see anything." 2 Appellants' App. in No. 00-6128 (CA10), p. 296.</p>
<p>[2]  The Court finds it sufficient that there be evidence of <i>some</i> drug use in Tecumseh's schools: "As we cannot articulate a threshold level of drug use that would suffice to justify a drug testing program for schoolchildren, we refuse to fashion what would in effect be a constitutional quantum of drug use necessary to show a `drug problem.' " <i>Ante,</i> at 836. One need not establish a bright-line "constitutional quantum of drug use" to recognize the relevance of the superintendent's reports characterizing drug use among Tecumseh's students as "not . . . [a] major proble[m]," App. 180, 186, 191.</p>
<p>[3]  Cross-country runners and volleyball players, by contrast, engage in substantial physical exertion. See <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i>  <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#663" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646, 663</a></span> (1995) (describing special dangers of combining drug use with athletics generally).</p>
<p>[4]  The Court notes that programs of individualized suspicion, unlike those using random testing, "might unfairly target members of unpopular groups." <i>Ante,</i> at 837; see also <i>ante,</i> at 841-842 (Breyer, J., concurring). Assuming, <i>arguendo,</i> that this is so, the School District here has not exchanged individualized suspicion for random testing. It has installed random testing in addition to, rather than in lieu of, testing "at any time when there is reasonable suspicion." App. 197.</p>

</div>
```

---

## GROUP: content/cases/Bobby v. Dixon.md  (`case`, 5 assertions)

### content_page

```
---
title: "Bobby v. Dixon"
type: case
citation: "565 U.S. 23 (2011)"
parallel_cite: "132 S. Ct. 26; 181 L. Ed. 2d 328"
neutral_cite: 2011 U.S. LEXIS 7926
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2011
date_decided: 2011-11-07
docket: 10-1540
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2011-11-07
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Bobby v. Dixon
  varies_by_point: false
  scope_note: "Per curiam AEDPA reversal; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/616807/bobby-v-dixon/"
  cluster_id: 616807
  opinion_id: 616807
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Related"
related: ["[[Oregon v. Elstad]]", "[[Missouri v. Seibert]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "two-step", "elstad", "seibert", "aedpa"]
holding: "A later Mirandized confession is admissible under Elstad — and Seibert's question-first bar does not apply — where there was no deliberate two-step strategy and no nexus between the earlier unwarned statement and the later warned confession; the Sixth Circuit's contrary habeas grant unreasonably applied clearly established law."
lake:
  record_id: Bobby v. Dixon
  status: verified
  projected_at: 2026-07-06
---

# Bobby v. Dixon

*565 U.S. 23 (2011)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Dixon was suspected in the disappearance and murder of Christopher Hammer. In a first, unwarned interrogation about a forgery, Dixon denied any involvement in Hammer's disappearance. Hours later, after learning an accomplice was talking, Dixon told police he wanted to tell them what happened, received [[Miranda and Custodial Interrogation|Miranda warnings]], waived, and confessed to the murder. The Ohio courts admitted the confession. The Sixth Circuit granted federal [[Common Legal Terms#habeas-corpus|habeas]] relief, holding the confession barred by a deliberate "question-first, warn-later" strategy under *[[Missouri v. Seibert]]*.

## Issue
Whether, on AEDPA review, the state court unreasonably applied clearly established federal law in admitting Dixon's warned murder confession given his earlier unwarned interrogation about a related forgery.

## Rule
No — admission was reasonable; *[[Missouri v. Seibert|Seibert]]*'s concern was absent and *[[Oregon v. Elstad|Elstad]]* governs. "[U]nlike in *Seibert*, there is no concern here that police gave Dixon *Miranda* warnings and then led him to repeat an earlier murder confession, because there was no earlier confession to repeat." — 565 U.S. at 31. ^pin-31

There was "simply 'no nexus' between Dixon's unwarned admission to forgery and his later, warned confession to murder," and a four-hour break separated the two interrogations, so the warned confession was not the tainted product of the earlier questioning. — *Id.* ^pin-31a

Under *[[Oregon v. Elstad]]*, where the earlier *[[Miranda v. Arizona|Miranda]]* lapse "involved no actual compulsion," a subsequent properly warned and voluntary confession is admissible.

## Application
Dixon's first interrogation produced only denials, not a confession to repeat, and he himself initiated the second session by declaring he wanted to tell police what happened — so police did not use the unwarned statement to soften him up. The two-step *[[Missouri v. Seibert|Seibert]]* dynamic (a single "continuum" that drained the midstream warnings of meaning) was therefore not present, and the Ohio Supreme Court reasonably found the warned murder confession admissible. The Sixth Circuit's grant of [[Common Legal Terms#habeas-corpus|habeas]] was an unreasonable application of clearly established law.

## Conclusion
The state court's admission of the confession was not contrary to, or an unreasonable application of, *[[Miranda v. Arizona|Miranda]]*, *[[Oregon v. Elstad|Elstad]]*, or *[[Missouri v. Seibert|Seibert]]*. The Sixth Circuit was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Bobby v. Dixon* marks the line between [[Oregon v. Elstad]] (a good-faith *[[Miranda v. Arizona|Miranda]]* lapse does not taint a later warned confession) and [[Missouri v. Seibert]] (a deliberate question-first strategy does): absent a deliberate two-step and a nexus, *[[Oregon v. Elstad|Elstad]]* controls.

## Appears on
- [[Miranda Waiver and Invocation]] — *Related*

## Sources
- *Bobby v. Dixon*, 565 U.S. 23 (2011) (per curiam) — https://www.courtlistener.com/opinion/616807/bobby-v-dixon/ — pinpoint: 31.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0d193cbd8152a507", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "565 U.S. 23 (2011)", "court": "U.S. Supreme Court", "neutral_cite": "2011 U.S. LEXIS 7926", "official_citation_present": true, "parallel_cite": "132 S. Ct. 26; 181 L. Ed. 2d 328", "title": "Bobby v. Dixon", "year": "2011"}}
{"assertion_id": "32deca338b333fc3", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A later Mirandized confession is admissible under Elstad — and Seibert's question-first bar does not apply — where there was no deliberate two-step strategy and no nexus between the earlier unwarned statement and the later warned confession; the Sixth Circuit's contrary habeas grant unreasonably applied clearly established law.", "title": "Bobby v. Dixon"}}
{"assertion_id": "c6d41488306afcfd", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Related", "title": "Bobby v. Dixon"}}
{"assertion_id": "1303b273e56470a8", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2011-11-07", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Bobby v. Dixon", "field_i_validity": "good_law", "scope_note": "Per curiam AEDPA reversal; good law.", "title": "Bobby v. Dixon", "varies_by_point": "false"}}
{"assertion_id": "94e32258c622e28c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Bobby v. Dixon"}}
```

### lake record — Bobby v. Dixon

```json
{
  "schema_version": "s2.v1",
  "record_id": "Bobby v. Dixon",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Bobby v. Dixon",
    "case_name_short": "Bobby",
    "case_name_full": "Bobby, Warden v. Dixon",
    "input_case_name": "Bobby v. Dixon",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2011-11-07",
    "year": 2011,
    "docket": "10-1540",
    "cluster_id": 616807,
    "lead_opinion_id": 616807,
    "sibling_ids": [
      616807
    ],
    "absolute_url": "/opinion/616807/bobby-v-dixon/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "565 U.S. 23",
      "volume": "565",
      "reporter": "U.S.",
      "page": "23",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "132 S. Ct. 26",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "26",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "181 L. Ed. 2d 328",
        "volume": "181",
        "reporter": "L. Ed. 2d",
        "page": "328",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2011 U.S. LEXIS 7926",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "7926",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "132 S. Ct. 26",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "26",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "181 L. Ed. 2d 328",
        "volume": "181",
        "reporter": "L. Ed. 2d",
        "page": "328",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "565 U.S. 23",
        "volume": "565",
        "reporter": "U.S.",
        "page": "23",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 U.S. LEXIS 7926",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "7926",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "565 U.S. 23",
    "official_selection": {
      "court_class": "scotus",
      "selected": "565 U.S. 23",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-31",
      "page": null,
      "quote": "strategy under *Missouri v. Seibert*. ## Issue Whether, on AEDPA review, the state court unreasonably applied clearly established federal law in admitting Dixon's warned murder confession given his earlier unwarned interrogation about a related forgery. ## Rule No \u2014 admission was reasonable; *Seibert*'s concern was absent and *Elstad* governs.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-31a",
      "page": null,
      "quote": "simply 'no nexus' between Dixon's unwarned admission to forgery and his later, warned confession to murder,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2011-11-07",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Bobby v. Dixon",
    "varies_by_point": false,
    "scope_note": "Per curiam AEDPA reversal; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Abbott",
          "cluster_id": 10366844,
          "cite": [
            "303 Ga. 297"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jose Vasquez v. State",
          "cluster_id": 2763816,
          "cite": [
            "453 S.W.3d 555",
            "2014 Tex. App. LEXIS 13776",
            "2014 WL 7365945"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. DeJong",
          "cluster_id": 2669581,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Paul H. Evans v. Secretary, Florida Department of Corrections",
          "cluster_id": 810858,
          "cite": [
            "699 F.3d 1249",
            "2012 WL 5200326",
            "2012 U.S. App. LEXIS 22072"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Antwion Thompson v. D. Runnel",
          "cluster_id": 815924,
          "cite": [
            "705 F.3d 1089",
            "2013 WL 263909",
            "2013 U.S. App. LEXIS 1585"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Krebs",
          "cluster_id": 4680693,
          "cite": [
            "452 P.3d 609",
            "255 Cal. Rptr. 3d 95",
            "8 Cal. 5th 265"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Young",
          "cluster_id": 4642880,
          "cite": [
            "250 Cal. Rptr. 3d 192",
            "445 P.3d 591",
            "7 Cal. 5th 905"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Wayne Holsey v. Warden, Georgia Diagonstic Prison",
          "cluster_id": 808587,
          "cite": [
            "694 F.3d 1230",
            "2012 WL 4017294",
            "2012 U.S. App. LEXIS 19370"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roy Blackmon v. Raymond Booker",
          "cluster_id": 809747,
          "cite": [
            "696 F.3d 536",
            "2012 WL 4774510",
            "2012 U.S. App. LEXIS 20898"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jarnagin",
          "cluster_id": 834830,
          "cite": [
            "277 P.3d 535",
            "351 Or. 703",
            "2012 WL 1437302",
            "2012 Ore. LEXIS 271"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Byron Black v. Ricky Bell",
          "cluster_id": 618946,
          "cite": [
            "664 F.3d 81",
            "2011 U.S. App. LEXIS 24798",
            "2011 WL 6224560"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wade Robertson v. Rise Pichon",
          "cluster_id": 4372525,
          "cite": [
            "849 F.3d 1173",
            "2017 WL 816886",
            "2017 U.S. App. LEXIS 3770"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Duvall",
          "cluster_id": 1037487,
          "cite": [
            "408 U.S. App. D.C. 73",
            "740 F.3d 604",
            "2013 WL 6501162",
            "2013 U.S. App. LEXIS 16874"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Clifton",
          "cluster_id": 4400956,
          "cite": [
            "892 N.W.2d 112",
            "296 Neb. 135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Peak v. Webb",
          "cluster_id": 625291,
          "cite": [
            "673 F.3d 465",
            "2012 U.S. App. LEXIS 5358",
            "2012 WL 833179"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kevin Moore v. Mary Berghuis",
          "cluster_id": 812911,
          "cite": [
            "700 F.3d 882",
            "2012 U.S. App. LEXIS 24627",
            "2012 WL 5971205"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vaughn Mitchell v. Duncan MacLaren",
          "cluster_id": 4645020,
          "cite": [
            "933 F.3d 526"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael D. Overstree v. Bill Wilson",
          "cluster_id": 804052,
          "cite": [
            "686 F.3d 404",
            "2012 WL 2819296",
            "2012 U.S. App. LEXIS 14106"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Verigan v. People",
          "cluster_id": 4506740,
          "cite": [
            "2018 CO 53",
            "420 P.3d 247"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Beeson",
          "cluster_id": 10133881,
          "cite": [
            "307 Or. App. 808",
            "479 P.3d 576"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nanavati v. Adecco USA, Inc.",
          "cluster_id": 7313087,
          "cite": [
            "99 F. Supp. 3d 1072",
            "2015 U.S. Dist. LEXIS 49053",
            "2015 WL 1738152"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "MERAS v. Sisto",
          "cluster_id": 798465,
          "cite": [
            "676 F.3d 1184",
            "2012 WL 1382857",
            "2012 U.S. App. LEXIS 8104"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adrian Reyes v. Greg Lewis",
          "cluster_id": 2827465,
          "cite": [
            "798 F.3d 815",
            "2015 U.S. App. LEXIS 14296",
            "2015 WL 4773374"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sakajust Scott v. Randall Hepp",
          "cluster_id": 9382680,
          "cite": [
            "62 F.4th 343"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mohamad Khweis",
          "cluster_id": 4788077,
          "cite": [
            "971 F.3d 453"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Felix Ruiz",
          "cluster_id": 4463512,
          "cite": [
            "179 A.3d 333",
            "170 N.H. 553"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(616807) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 65,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 65,
        "triage_read": 4,
        "triage_snippet_classified": 61
      },
      "lane2_top_cited": {
        "query": "cites:(616807)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xJnM9MzE2NzQ1MyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28616807%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(616807)",
        "reviewed": 5,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 5,
        "triage_read": 0,
        "triage_snippet_classified": 5
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(616807)",
    "indexed_citing_opinions": 67,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 616807,
        "count": 67,
        "count_source": "search"
      }
    ],
    "citation_count": 282,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/bobby-v-dixon.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU3NzUyMTEmcz0xMDM2Njg0NCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28616807%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 616807,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 616807,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 616807,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 616807,
        "cited_id": 111542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 616807,
        "cited_id": 112566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 616807,
        "cited_id": 112622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 616807,
        "cited_id": 137002,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 616807,
        "cited_id": 145873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 616807,
        "cited_id": 180733,
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
    "date_created": "2026-07-04T20:02:45Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:04:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:04:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:07:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:04:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Bobby v. Dixon

```
                 Cite as: 565 U. S. ____ (2011)            1

                          Per Curiam

SUPREME COURT OF THE UNITED STATES
     DAVID BOBBY, WARDEN v. ARCHIE DIXON
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE SIXTH CIRCUIT

            No. 10–1540. Decided November 7, 2011


  PER CURIAM.
  Under the Antiterrorism and Effective Death Penalty
Act, a state prisoner seeking a writ of habeas corpus from
a federal court “must show that the state court’s ruling on
the claim being presented in federal court was so lacking
in justification that there was an error well understood
and comprehended in existing law beyond any possibility
for fairminded disagreement.” Harrington v. Richter, 562
U. S. ___, ___ (2011) (slip op., at 13). The Court of Appeals
for the Sixth Circuit purported to identify three such
grievous errors in the Ohio Supreme Court’s affirmance of
respondent Archie Dixon’s murder conviction. Because it
is not clear that the Ohio Supreme Court erred at all,
much less erred so transparently that no fairminded jurist
could agree with that court’s decision, the Sixth Circuit’s
judgment must be reversed.
                         *    *    *
   Archie Dixon and Tim Hoffner murdered Chris Hammer
in order to steal his car. Dixon and Hoffner beat Hammer,
tied him up, and buried him alive, pushing the struggling
Hammer down into his grave while they shoveled dirt on
top of him. Dixon then used Hammer’s birth certificate
and social security card to obtain a state identification
card in Hammer’s name. After using that identification
card to establish ownership of Hammer’s car, Dixon sold
the vehicle for $2,800.
   Hammer’s mother reported her son missing the day
after his murder. While investigating Hammer’s disap­
2                     BOBBY v. DIXON

                         Per Curiam

pearance, police had various encounters with Dixon, three
of which are relevant here. On November 4, 1993, a police
detective spoke with Dixon at a local police station. It is
undisputed that this was a chance encounter—Dixon was
apparently visiting the police station to retrieve his own
car, which had been impounded for a traffic violation. The
detective issued Miranda warnings to Dixon and then
asked to talk to him about Hammer’s disappearance. See
Miranda v. Arizona, 384 U. S. 436 (1966). Dixon declined
to answer questions without his lawyer present and left
the station.
   As their investigation continued, police determined that
Dixon had sold Hammer’s car and forged Hammer’s signa­
ture when cashing the check he received in that sale.
Police arrested Dixon for forgery on the morning of No­
vember 9. Beginning at 11:30 a.m. detectives intermit­
tently interrogated Dixon over several hours, speaking
with him for about 45 minutes total. Prior to the interro­
gation, the detectives had decided not to provide Dixon
with Miranda warnings for fear that Dixon would again
refuse to speak with them.
   Dixon readily admitted to obtaining the identification
card in Hammer’s name and signing Hammer’s name on
the check, but said that Hammer had given him permis­
sion to sell the car. Dixon claimed not to know where
Hammer was, although he said he thought Hammer might
have left for Tennessee. The detectives challenged the
plausibility of Dixon’s tale and told Dixon that Tim
Hoffner was providing them more useful information. At
one point a detective told Dixon that “now is the time to
say” whether he had any involvement in Hammer’s disap­
pearance because “if Tim starts cutting a deal over there,
this is kinda like, a bus leaving. The first one that gets on
it is the only one that’s gonna get on.” App. to Pet. for
Cert. 183a. Dixon responded that, if Hoffner knew any­
thing about Hammer’s disappearance, Hoffner had not
                 Cite as: 565 U. S. ____ (2011)           3

                          Per Curiam

told him. Dixon insisted that he had told police everything
he knew and that he had “[n]othing whatsoever” to do
with Hammer’s disappearance. Id., at 186a. At approxi­
mately 3:30 p.m. the interrogation concluded, and the
detectives brought Dixon to a correctional facility where
he was booked on a forgery charge.
  The same afternoon, Hoffner led police to Hammer’s
grave. Hoffner claimed that Dixon had told him that
Hammer was buried there. After concluding their inter­
view with Hoffner and releasing him, the police had Dixon
transported back to the police station.
  Dixon arrived at the police station at about 7:30 p.m.
Prior to any police questioning, Dixon stated that he had
heard the police had found a body and asked whether
Hoffner was in custody. The police told Dixon that
Hoffner was not, at which point Dixon said, “I talked to
my attorney, and I want to tell you what happened.” State
v. Dixon, 101 Ohio St. 3d 328, 331, 2004–Ohio–1585, 805
N. E. 2d 1042, 1050. The police read Dixon his Miranda
rights, obtained a signed waiver of those rights, and spoke
with Dixon for about half an hour. At 8 p.m. the police,
now using a tape recorder, again advised Dixon of his
Miranda rights. In a detailed confession, Dixon admitted
to murdering Hammer but attempted to pin the lion’s
share of the blame on Hoffner.
  At Dixon’s trial, the Ohio trial court excluded both
Dixon’s initial confession to forgery and his later confes­
sion to murder. The State took an interlocutory appeal.
The State did not dispute that Dixon’s forgery confession
was properly suppressed, but argued that the murder
confession was admissible because Dixon had received
Miranda warnings prior to that confession. The Ohio
Court of Appeals agreed and allowed Dixon’s murder
confession to be admitted as evidence. Dixon was convict­
ed of murder, kidnaping, robbery, and forgery, and sen­
tenced to death.
4                      BOBBY v. DIXON

                         Per Curiam

   The Ohio Supreme Court affirmed Dixon’s convictions
and sentence. To analyze the admissibility of Dixon’s
murder confession, the court applied Oregon v. Elstad, 470
U. S. 298 (1985). The Ohio Supreme Court found that
Dixon’s confession to murder after receiving Miranda
warnings was admissible because that confession and his
prior, unwarned confession to forgery were both voluntary.
State v. Dixon, supra, at 332–334, 805 N. E. 2d, at 1050–
1052; see Elstad, supra, at 318 (“We hold today that a
suspect who has once responded to unwarned yet uncoer­
cive questioning is not thereby disabled from waiving his
rights and confessing after he has been given the requisite
Miranda warnings”).
   Dixon then filed a petition for a writ of habeas corpus
under 28 U. S. C. §2254 in the U. S. District Court for the
Northern District of Ohio. Dixon claimed, inter alia, that
the state court decisions allowing the admission of his
murder confession contravened clearly established federal
law. The District Court denied relief, but a divided panel
of the Sixth Circuit reversed. Dixon v. Houk, 627 F. 3d
553 (2010).
   The Sixth Circuit had authority to issue the writ of
habeas corpus only if the Ohio Supreme Court’s decision
“was contrary to, or involved an unreasonable application
of, clearly established Federal law,” as set forth in this
Court’s holdings, or was “based on an unreasonable de­
termination of the facts” in light of the state court record.
§2254(d); see Harrington, 562 U. S., at ___ (slip op., at 10).
The Sixth Circuit believed that the Ohio Supreme Court’s
decision contained three such egregious errors.
   First, according to the Sixth Circuit, the Miranda deci­
sion itself clearly established that police could not speak to
Dixon on November 9, because on November 4 Dixon had
refused to speak to police without his lawyer. That is
plainly wrong. It is undisputed that Dixon was not in
custody during his chance encounter with police on No­
                     Cite as: 565 U. S. ____ (2011)                   5

                              Per Curiam

vember 4. And this Court has “never held that a person
can invoke his Miranda rights anticipatorily, in a context
other than ‘custodial interrogation.’ ” McNeil v. Wisconsin,
501 U. S. 171, 182, n. 3 (1991); see also Montejo v. Louisi-
ana, 556 U. S. 778, ___ (2009) (slip. op., at 16) (“If the
defendant is not in custody then [Miranda and its proge­
ny] do not apply”).
  Second, the Sixth Circuit held that police violated the
Fifth Amendment by urging Dixon to “cut a deal” before
his accomplice Hoffner did so.1 The Sixth Circuit cited no
precedent of this Court—or any court—holding that this
common police tactic is unconstitutional. Cf., e.g., Elstad,
supra, at 317 (“[T]he Court has refused to find that a
defendant who confesses, after being falsely told that his
codefendant has turned State’s evidence, does so involun­
tarily”). Because no holding of this Court suggests, much
less clearly establishes, that police may not urge a suspect
to confess before another suspect does so, the Sixth Circuit
had no authority to issue the writ on this ground.2
——————
   1 In the Sixth Circuit’s view, the Ohio Supreme Court’s contrary con­

clusion that Dixon’s confession was voluntary “was based on an unrea­
sonable determination of the facts in light of the evidence presented in
the State court proceeding.” §2254(d)(2). The Sixth Circuit did not,
however, purport to identify any mistaken factual finding. It differed
with the Ohio Supreme Court only on the ultimate characterization of
Dixon’s confession as voluntary, and this Court’s cases make clear that
“the ultimate issue of ‘voluntariness’ is a legal question.” Miller v.
Fenton, 474 U. S. 104, 110 (1985); see also Arizona v. Fulminante, 499
U. S. 279, 287 (1991). This Court therefore addresses the question the
Sixth Circuit should have addressed: whether the Ohio Supreme
Court’s decision “was contrary to, or involved an unreasonable applica­
tion of, clearly established Federal law, as determined by the Supreme
Court of the United States.” §2254(d)(1).
   2 The only case the Sixth Circuit cited on this issue was Mincey v.

Arizona, 437 U. S. 385 (1978). Mincey involved the “virtually continu­
ous questioning of a seriously and painfully wounded man on the edge
of consciousness” who was in a hospital’s intensive care unit and who
6                          BOBBY v. DIXON

                              Per Curiam

   Third, the Sixth Circuit held that the Ohio Supreme
Court unreasonably applied this Court’s precedent in
Elstad. In that case, a suspect who had not received
Miranda warnings confessed to burglary as police took
him into custody. Approximately an hour later, after he
had received Miranda warnings, the suspect again con­
fessed to the same burglary. This Court held that the
later, warned confession was admissible because “there is
no warrant for presuming coercive effect where the sus­
pect’s initial inculpatory statement, though technically
in violation of Miranda, was voluntary. The relevant
inquiry is whether, in fact, the second [warned] statement
was also voluntarily made.” 470 U. S., at 318 (footnote
omitted).
   As the Ohio Supreme Court’s opinion explained, the
circumstances surrounding Dixon’s interrogations demon­
strate that his statements were voluntary. During Dixon’s
first interrogation, he received several breaks, was given
water and offered food, and was not abused or threatened.
He freely acknowledged that he had forged Hammer’s
name, even stating that the police were “welcome” to that
information, and he had no difficulty denying that he had
anything to do with Hammer’s disappearance. State v.
Dixon, 101 Ohio St. 3d, at 331, 805 N. E. 2d, at 1049.
Prior to his second interrogation, Dixon made an unsolic­
ited declaration that he had spoken with his attorney and
wanted to tell the police what had happened to Hammer.
Then, before giving his taped confession, Dixon twice
received Miranda warnings and signed a waiver-of-rights
form which stated that he was acting of his own free will.


——————
“clearly expressed his wish not to be interrogated” while in a “debilitat­
ed and helpless condition.” Id., at 399–401. There is simply nothing in
the facts or reasoning of Mincey suggesting that any of Dixon’s state­
ments were involuntary.
                     Cite as: 565 U. S. ____ (2011)                     7

                              Per Curiam

The Ohio Supreme Court recognized that Dixon’s first in-
terrogation involved “an intentional Miranda violation.”
The court concluded, however, that “as in Elstad, the
breach of the Miranda procedures here involved no actual
compulsion” and thus there was no reason to suppress
Dixon’s later, warned confession. 101 Ohio St. 3d, at 334,
805 N. E. 2d, at 1052 (citing Elstad, supra, at 318).
  The Sixth Circuit disagreed, believing that Dixon’s
confession was inadmissible under Elstad because it was
the product of a “deliberate question-first, warn-later
strategy.” 627 F. 3d, at 557. In so holding, the Sixth
Circuit relied heavily on this Court’s decision in Missouri
v. Seibert, 542 U. S. 600 (2004).3 In Seibert, police em­
ployed a two-step strategy to reduce the effect of Miranda
warnings: A detective exhaustively questioned Seibert
until she confessed to murder and then, after a 15- to 20­
minute break, gave Seibert Miranda warnings and led her
to repeat her prior confession. 542 U. S., at 604–606, 616
(plurality opinion). The Court held that Seibert’s second
confession was inadmissible as evidence against her even
though it was preceded by a Miranda warning. A plurali­
ty of the Court reasoned that “[u]pon hearing warnings
only in the aftermath of interrogation and just after mak­

——————
   3 Seibert was not decided until after the Ohio Supreme Court’s opin­

ion in this case, but was issued before this Court denied Dixon’s peti­
tion for certiorari seeking review of the Ohio Supreme Court’s decision.
It is thus an open question whether Seibert was “clearly established
Federal law” for purposes of §2254(d). See Smith v. Spisak¸ 558 U. S.
___, ___ (2010) (slip op., at 3). It is not necessary to decide that ques­
tion here because Seibert is entirely consistent with the Ohio Supreme
Court’s decision. Thus, if Seibert was clearly established law, the Ohio
Supreme Court’s decision was not “contrary to” or “an unreasonable
application of” Seibert. §2254(d). And if Seibert was not clearly estab­
lished law, Seibert’s explication of Elstad further demonstrates that the
Ohio Supreme Court’s decision was not contrary to or an unreasonable
application of Elstad.
8                      BOBBY v. DIXON

                          Per Curiam

ing a confession, a suspect would hardly think he had a
genuine right to remain silent, let alone persist in so
believing once the police began to lead him over the same
ground again.” 542 U. S., at 613; see also id., at 615 (de­
tailing a “series of relevant facts that bear on whether
Miranda warnings delivered midstream could be effective
enough to accomplish their object”). JUSTICE KENNEDY
concurred in the judgment, noting he “would apply a
narrower test applicable only in the infrequent case . . . in
which the two-step interrogation technique was used in a
calculated way to undermine the Miranda warning.” Id.,
at 622.
   In this case, no two-step interrogation technique of the
type that concerned the Court in Seibert undermined the
Miranda warnings Dixon received. In Seibert, the sus­
pect’s first, unwarned interrogation left “little, if anything,
of incriminating potential left unsaid,” making it “unnatu­
ral” not to “repeat at the second stage what had been said
before.” 542 U. S., at 616–617 (plurality opinion). But in
this case Dixon steadfastly maintained during his first,
unwarned interrogation that he had “[n]othing whatso­
ever” to do with Hammer’s disappearance. App. to Pet. for
Cert. 186a. Thus, unlike in Seibert, there is no concern
here that police gave Dixon Miranda warnings and then
led him to repeat an earlier murder confession, because
there was no earlier confession to repeat. Indeed, Dixon
contradicted his prior unwarned statements when he
confessed to Hammer’s murder. Nor is there any evidence
that police used Dixon’s earlier admission to forgery to
induce him to waive his right to silence later: Dixon de­
clared his desire to tell police what happened to Hammer
before the second interrogation session even began. As the
Ohio Supreme Court reasonably concluded, there was
simply “no nexus” between Dixon’s unwarned admission to
forgery and his later, warned confession to murder. 101
Ohio St. 3d, at 333, 805 N. E. 2d, at 1051.
                     Cite as: 565 U. S. ____ (2011)                    9

                              Per Curiam

   Moreover, in Seibert the Court was concerned that the
Miranda warnings did not “effectively advise the suspect
that he had a real choice about giving an admissible
statement” because the unwarned and warned interroga­
tions blended into one “continuum.” 542 U. S., at 612, 617.
Given all the circumstances of this case, that is not so
here. Four hours passed between Dixon’s unwarned inter­
rogation and his receipt of Miranda rights, during which
time he traveled from the police station to a separate jail
and back again; claimed to have spoken to his lawyer; and
learned that police were talking to his accomplice and
had found Hammer’s body. Things had changed. Under
Seibert, this significant break in time and dramatic
change in circumstances created “a new and distinct expe­
rience,” ensuring that Dixon’s prior, unwarned interroga­
tion did not undermine the effectiveness of the Miranda
warnings he received before confessing to Hammer’s mur­
der. 542 U. S., at 615; see also id., at 622 (KENNEDY, J.,
concurring in judgment) (“For example, a substantial
break in time and circumstances between the prewarning
statement and the Miranda warning may suffice in most
circumstances, as it allows the accused to distinguish the
two contexts and appreciate that the interrogation has
taken a new turn”).4
   The admission of Dixon’s murder confession was con­
sistent with this Court’s precedents: Dixon received Mi-


——————
   4 The Sixth Circuit also concluded that “the Ohio Supreme Court

erroneously placed the burden of proof on Dixon to prove that his
confession was coerced.” Dixon v. Houk, 627 F. 3d 553, 558 (2010). But
the Ohio Supreme Court clearly said that “the state carries the burden
of proving voluntariness.” State v. Dixon, 101 Ohio St. 3d 328, 332,
2004–Ohio–1585, 805 N. E. 2d 1042, 1050. That the court’s opinion
discusses the absence of evidence of coerciveness alongside the affirma­
tive evidence of voluntariness in no way indicates that the court shifted
the burden onto Dixon.
10                    BOBBY v. DIXON

                         Per Curiam

randa warnings before confessing to Hammer’s murder;
the effectiveness of those warnings was not impaired by
the sort of “two-step interrogation technique” condemned
in Seibert; and there is no evidence that any of Dixon’s
statements was the product of actual coercion. That does
not excuse the detectives’ decision not to give Dixon Mi-
randa warnings before his first interrogation. But the
Ohio courts recognized that failure and imposed the ap­
propriate remedy: exclusion of Dixon’s forgery confession
and the attendant statements given without the benefit of
Miranda warnings. Because no precedent of this Court
required Ohio to do more, the Sixth Circuit was without
authority to overturn the reasoned judgment of the State’s
highest court.
  The petition for a writ of certiorari and respondent’s
motion to proceed in forma pauperis are granted. The
judgment of the Court of Appeals for the Sixth Circuit is
reversed, and the case is remanded for further proceedings
consistent with this opinion.
                                           It is so ordered.

```

---
