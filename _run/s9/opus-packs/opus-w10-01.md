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

## GROUP: _overhaul2/lake/cases/Bivens v. Six Unknown Named Agents.json  (`lake-record`, 4 assertions)

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
{"assertion_id": "f9a24f74b7d46324", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Bivens v. Six Unknown Named Agents"}, "payload": {"all": [{"cite": "403 U.S. 388", "page": "388", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "403"}, {"cite": "91 S. Ct. 1999", "page": "1999", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "91"}, {"cite": "29 L. Ed. 2d 619", "page": "619", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "29"}, {"cite": "1971 U.S. LEXIS 23", "page": "23", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1971"}], "display": "403 U.S. 388", "official": {"cite": "403 U.S. 388", "page": "388", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "403"}, "official_selection_present": true, "record_id": "Bivens v. Six Unknown Named Agents"}}
{"assertion_id": "73a5f08ef5cb40e1", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-392", "record_id": "Bivens v. Six Unknown Named Agents"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-392", "pinpoint_status": "slip-only", "quote": "--- # Bivens v. Six Unknown Named Agents *403 U.S. 388 (1971)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Webster Bivens alleged that agents of the Federal Bureau of Narcotics, acting without a warrant or probable cause, entered his apartment, arrested him for narcotics offenses, manacled him in front of his wife and children, threatened to arrest the entire family, searched the apartment, and later subjected him to a visual strip search. He sued the agents for damages, claiming the entry, arrest, and search violated the Fourth Amendment. The lower courts dismissed because no federal statute authorized a damages suit against federal officers for such a violation. ## Issue Whether a victim of an unconstitutional search and seizure by federal officers may sue them for money damages directly under the Fourth Amendment, even though no statute creates the cause of action. ## Rule Yes. The Fourth Amendment itself supports a damages remedy against federal officers who violate it. Invoking *Bell v. Hood*, the Court reasoned that", "quote_fidelity": "mismatch", "record_id": "Bivens v. Six Unknown Named Agents", "star_marker": null}}
{"assertion_id": "ffcad4f2d3278357", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-397", "record_id": "Bivens v. Six Unknown Named Agents"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-397", "pinpoint_status": "slip-only", "quote": "Having concluded that petitioner's complaint states a cause of action under the Fourth Amendment . . . we hold that petitioner is entitled to recover money damages for any injuries he has suffered as a result of the agents' violation of the Amendment.", "quote_fidelity": "mismatch", "record_id": "Bivens v. Six Unknown Named Agents", "star_marker": null}}
{"assertion_id": "24eaee1bdb773f15", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Bivens v. Six Unknown Named Agents"}, "payload": {"as_of_content": "1971-06-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Bivens v. Six Unknown Named Agents", "scope_note": "Core holding (4A damages against federal officers) remains good law; the Court has declined to extend Bivens to new contexts (Ziglar v. Abbasi (2017); Egbert v. Boule (2022)).", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/California v. Prysock.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "California v. Prysock"
type: case
citation: "453 U.S. 355 (1981)"
parallel_cite: "101 S. Ct. 2806; 69 L. Ed. 2d 696; 49 U.S.L.W. 3964"
neutral_cite: 1981 U.S. LEXIS 131
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1981
date_decided: 1981-06-29
docket: 80-1846
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1981-06-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: California v. Prysock
  varies_by_point: false
  scope_note: "Reaffirmed and applied by Duckworth v. Eagan (1989) and Florida v. Powell (2010); good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110556/california-v-prysock/"
  cluster_id: 110556
  opinion_id: 9428478
  identity_checked: false
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny"
related: ["[[Duckworth v. Eagan]]", "[[Florida v. Powell]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "warning-adequacy"]
holding: "Miranda warnings need not be a verbatim recital of the language in Miranda; a warning that reasonably conveys the suspect's rights is adequate — no talismanic incantation is required."
lake:
  record_id: California v. Prysock
  status: under_review
  projected_at: 2026-07-06
---

# California v. Prysock

*451 U.S. 355 (1981)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Randall Prysock, a juvenile murder suspect, was given [[Miranda and Custodial Interrogation|Miranda warnings]] before questioning. He was told he had the right to a lawyer before and during questioning and the right to have a lawyer appointed at no cost if he could not afford one. The California Court of Appeal held the warnings defective because the appointed-counsel advice was not expressly tied to a point *before* questioning, and suppressed his statements.

## Issue
Whether [[Miranda and Custodial Interrogation|Miranda warnings]] are inadequate simply because the advice about the right to appointed counsel was not given in the precise language or sequence used in *[[Miranda v. Arizona|Miranda]]* itself.

## Rule
No. [[Miranda and Custodial Interrogation|Miranda warnings]] need not track an exact script; a warning that reasonably conveys the rights suffices. "This Court has never indicated that the 'rigidity' of *Miranda* extends to the precise formulation of the warnings given a criminal defendant." — 451 U.S. at 359. ^pin-359

"*Miranda* itself indicated that no talismanic incantation was required to satisfy its strictures." — *Id.* ^pin-359a

Reviewing courts examine the warnings actually given to determine whether they reasonably conveyed the right to appointed counsel, rather than demanding "a verbatim recital of the words of the *Miranda* opinion." — *Id.*

## Application
The warnings given Prysock told him he had the right to a lawyer before and during questioning and the right to have a lawyer appointed without cost. Nothing in those warnings linked the appointment of counsel to a future time *after* interrogation (the defect that had invalidated warnings in cases like *People v. Bolinski*). Read as a whole, the warnings conveyed that Prysock could have appointed counsel present prior to and during questioning, so they satisfied *[[Miranda v. Arizona|Miranda]]*.

## Conclusion
The warnings were adequate. The judgment of the California Court of Appeal was reversed and the case [[Reading and Citing Cases#on-remand|remanded]]. Miranda compliance turns on whether the warnings reasonably convey the rights, not on verbatim recital.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. The "reasonably conveys" rule was reaffirmed and applied in [[Duckworth v. Eagan]] (warnings adequate despite "if and when you go to court" language) and [[Florida v. Powell]] (warnings need not be verbatim).

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny*

## Sources
- *California v. Prysock*, 451 U.S. 355 (1981) (per curiam) — https://www.courtlistener.com/opinion/110556/california-v-prysock/ — pinpoint: 359.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1a7568d1a902c39e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "California v. Prysock"}, "payload": {"all": [{"cite": "453 U.S. 355", "page": "355", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "453"}, {"cite": "101 S. Ct. 2806", "page": "2806", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "101"}, {"cite": "69 L. Ed. 2d 696", "page": "696", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "69"}, {"cite": "1981 U.S. LEXIS 131", "page": "131", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1981"}, {"cite": "49 U.S.L.W. 3964", "page": "3964", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "49"}], "display": "453 U.S. 355", "official": {"cite": "453 U.S. 355", "page": "355", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "453"}, "official_selection_present": true, "record_id": "California v. Prysock"}}
{"assertion_id": "66c73a7414e5a9de", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-359", "record_id": "California v. Prysock"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-359", "pinpoint_status": "slip-only", "quote": "--- # California v. Prysock *451 U.S. 355 (1981)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Randall Prysock, a juvenile murder suspect, was given Miranda warnings before questioning. He was told he had the right to a lawyer before and during questioning and the right to have a lawyer appointed at no cost if he could not afford one. The California Court of Appeal held the warnings defective because the appointed-counsel advice was not expressly tied to a point *before* questioning, and suppressed his statements. ## Issue Whether Miranda warnings are inadequate simply because the advice about the right to appointed counsel was not given in the precise language or sequence used in *Miranda* itself. ## Rule No. Miranda warnings need not track an exact script; a warning that reasonably conveys the rights suffices.", "quote_fidelity": "mismatch", "record_id": "California v. Prysock", "star_marker": null}}
{"assertion_id": "d0d5657caa2baf88", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-359a", "record_id": "California v. Prysock"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-359a", "pinpoint_status": "slip-only", "quote": "*Miranda* itself indicated that no talismanic incantation was required to satisfy its strictures.", "quote_fidelity": "mismatch", "record_id": "California v. Prysock", "star_marker": null}}
{"assertion_id": "655e68420fc44dba", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "California v. Prysock"}, "payload": {"as_of_content": "1981-06-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "California v. Prysock", "scope_note": "Reaffirmed and applied by Duckworth v. Eagan (1989) and Florida v. Powell (2010); good law.", "varies_by_point": false}}
```

### lake record — California v. Prysock

```json
{
  "schema_version": "s2.v1",
  "record_id": "California v. Prysock",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "California v. Prysock",
    "case_name_short": "Prysock",
    "case_name_full": "California v. Prysock",
    "input_case_name": "California v. Prysock",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1981-06-29",
    "year": 1981,
    "docket": "80-1846",
    "cluster_id": 110556,
    "lead_opinion_id": 9428478,
    "sibling_ids": [
      110556,
      9428478,
      9428479
    ],
    "absolute_url": "/opinion/110556/california-v-prysock/",
    "identity_method": "name+docket",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 110503,
        "score": 20,
        "case_name": "California v. Prysock"
      }
    ],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "453 U.S. 355",
      "volume": "453",
      "reporter": "U.S.",
      "page": "355",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "101 S. Ct. 2806",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "2806",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 2d 696",
        "volume": "69",
        "reporter": "L. Ed. 2d",
        "page": "696",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 U.S.L.W. 3964",
        "volume": "49",
        "reporter": "U.S.L.W.",
        "page": "3964",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1981 U.S. LEXIS 131",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "131",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "453 U.S. 355",
        "volume": "453",
        "reporter": "U.S.",
        "page": "355",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 S. Ct. 2806",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "2806",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 2d 696",
        "volume": "69",
        "reporter": "L. Ed. 2d",
        "page": "696",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1981 U.S. LEXIS 131",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "131",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 U.S.L.W. 3964",
        "volume": "49",
        "reporter": "U.S.L.W.",
        "page": "3964",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "453 U.S. 355",
    "official_selection": {
      "court_class": "scotus",
      "selected": "453 U.S. 355",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-359",
      "page": null,
      "quote": "--- # California v. Prysock *451 U.S. 355 (1981)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Randall Prysock, a juvenile murder suspect, was given Miranda warnings before questioning. He was told he had the right to a lawyer before and during questioning and the right to have a lawyer appointed at no cost if he could not afford one. The California Court of Appeal held the warnings defective because the appointed-counsel advice was not expressly tied to a point *before* questioning, and suppressed his statements. ## Issue Whether Miranda warnings are inadequate simply because the advice about the right to appointed counsel was not given in the precise language or sequence used in *Miranda* itself. ## Rule No. Miranda warnings need not track an exact script; a warning that reasonably conveys the rights suffices.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-359a",
      "page": null,
      "quote": "*Miranda* itself indicated that no talismanic incantation was required to satisfy its strictures.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1981-06-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "California v. Prysock",
    "varies_by_point": false,
    "scope_note": "Reaffirmed and applied by Duckworth v. Eagan (1989) and Florida v. Powell (2010); good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Larry Loucious",
          "cluster_id": 4347647,
          "cite": [
            "847 F.3d 1146",
            "2017 WL 510457",
            "2017 U.S. App. LEXIS 2166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Luis Fernando Ortiz",
          "cluster_id": 4472662,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ramirez",
          "cluster_id": 3958382,
          "cite": [
            "732 N.E.2d 1064",
            "135 Ohio App. 3d 89"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thomas v. State",
          "cluster_id": 1112339,
          "cite": [
            "625 So. 2d 1149",
            "1992 Ala. Crim. App. LEXIS 243",
            "1992 WL 92475"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Mattson",
          "cluster_id": 1345979,
          "cite": [
            "789 P.2d 983",
            "50 Cal. 3d 826",
            "268 Cal. Rptr. 802",
            "1990 Cal. LEXIS 1844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Valdivia",
          "cluster_id": 5807063,
          "cite": [
            "180 Cal. App. 3d 657",
            "226 Cal. Rptr. 144",
            "1986 Cal. App. LEXIS 1537"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Missouri v. Seibert",
          "cluster_id": 137002,
          "cite": [
            "159 L. Ed. 2d 643",
            "124 S. Ct. 2601",
            "542 U.S. 600",
            "2004 U.S. LEXIS 4578"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Duckworth v. Eagan",
          "cluster_id": 112322,
          "cite": [
            "106 L. Ed. 2d 166",
            "109 S. Ct. 2875",
            "492 U.S. 195",
            "1989 U.S. LEXIS 3196",
            "57 U.S.L.W. 4942"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Musselwhite",
          "cluster_id": 1225502,
          "cite": [
            "17 Cal. 4th 1216",
            "954 P.2d 475",
            "98 Daily Journal DAR 4745",
            "98 Cal. Daily Op. Serv. 3452",
            "74 Cal. Rptr. 2d 212",
            "1998 Cal. LEXIS 2622"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rupe",
          "cluster_id": 1159824,
          "cite": [
            "683 P.2d 571",
            "101 Wash. 2d 664",
            "1984 Wash. LEXIS 1675"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Wader",
          "cluster_id": 1447881,
          "cite": [
            "854 P.2d 80",
            "5 Cal. 4th 610",
            "20 Cal. Rptr. 2d 788",
            "93 Daily Journal DAR 8799",
            "93 Cal. Daily Op. Serv. 5245",
            "1993 Cal. LEXIS 3188"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Louisias",
          "cluster_id": 5845572,
          "cite": [
            "29 A.D.3d 1017",
            "815 N.Y.S.2d 727"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
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
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Wash",
          "cluster_id": 1158185,
          "cite": [
            "861 P.2d 1107",
            "6 Cal. 4th 215",
            "24 Cal. Rptr. 2d 421",
            "93 Cal. Daily Op. Serv. 8554",
            "93 Daily Journal DAR 14629",
            "1993 Cal. LEXIS 5807"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Thompson",
          "cluster_id": 1138459,
          "cite": [
            "785 P.2d 857",
            "50 Cal. 3d 134",
            "266 Cal. Rptr. 309",
            "1990 Cal. LEXIS 518"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Penry v. State",
          "cluster_id": 1565146,
          "cite": [
            "691 S.W.2d 636",
            "1985 Tex. Crim. App. LEXIS 1198"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Price v. State.",
          "cluster_id": 1707117,
          "cite": [
            "725 So. 2d 1063",
            "1998 WL 560257"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ex Parte Siebert",
          "cluster_id": 1816780,
          "cite": [
            "555 So. 2d 780",
            "1989 WL 163740"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Foust",
          "cluster_id": 2689896,
          "cite": [
            "2004 Ohio 7006",
            "105 Ohio St. 3d 137",
            "823 N.E.2d 836"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Terrance Anderson",
          "cluster_id": 558038,
          "cite": [
            "929 F.2d 96",
            "1991 U.S. App. LEXIS 5371",
            "1991 WL 43249"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nollie Lee Martin v. Louie L. Wainwright",
          "cluster_id": 457158,
          "cite": [
            "770 F.2d 918",
            "78 A.L.R. Fed. 515",
            "1985 U.S. App. LEXIS 21452"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Kelly",
          "cluster_id": 2612432,
          "cite": [
            "800 P.2d 516",
            "51 Cal. 3d 931",
            "275 Cal. Rptr. 160",
            "90 Cal. Daily Op. Serv. 8544",
            "1990 Cal. LEXIS 5814"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stanley Street",
          "cluster_id": 77537,
          "cite": [
            "472 F.3d 1298",
            "2006 WL 3734533"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Colon-Cruz",
          "cluster_id": 2153683,
          "cite": [
            "562 N.E.2d 797",
            "408 Mass. 533",
            "1990 Mass. LEXIS 472"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Lemaricus Devall Davidson",
          "cluster_id": 4331383,
          "cite": [
            "509 S.W.3d 156",
            "2016 Tenn. LEXIS 913"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garrett v. State",
          "cluster_id": 2460932,
          "cite": [
            "682 S.W.2d 301",
            "1984 Tex. Crim. App. LEXIS 735"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cruz, Jose, United States of America v. Alverio, Julian Miguel",
          "cluster_id": 546224,
          "cite": [
            "910 F.2d 1072"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hensley",
          "cluster_id": 2686689,
          "cite": [
            "59 Cal. 4th 788",
            "330 P.3d 296",
            "175 Cal. Rptr. 3d 213",
            "2014 WL 3747139",
            "2014 Cal. LEXIS 5317"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ex Parte Gardner",
          "cluster_id": 1785392,
          "cite": [
            "959 S.W.2d 189",
            "1998 Tex. Crim. App. LEXIS 14",
            "1996 WL 692075"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Billy Joe Battie v. W. J. Estelle, Jr., Director, Texas Department of Corrections",
          "cluster_id": 392853,
          "cite": [
            "655 F.2d 692",
            "1981 U.S. App. LEXIS 17825"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Prysock:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110556 OR 9428478 OR 9428479) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00NzQwNzY4MDAwMDAmcz0xNTY1MTQ2JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110556+OR+9428478+OR+9428479%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110556 OR 9428478 OR 9428479)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NyZzPTU0NDczNyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110556+OR+9428478+OR+9428479%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110556 OR 9428478 OR 9428479)",
        "reviewed": 10,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 10,
        "triage_read": 0,
        "triage_snippet_classified": 10
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110556 OR 9428478 OR 9428479)",
    "indexed_citing_opinions": 288,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110556,
        "count": 252,
        "count_source": "search"
      },
      {
        "opinion_id": 9428478,
        "count": 39,
        "count_source": "search"
      },
      {
        "opinion_id": 9428479,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 537,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/california-v-prysock.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY0MzgxNjYmcz00NjU3Nzk3JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110556+OR+9428478+OR+9428479%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110556,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110556,
        "cited_id": 109997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110556,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110556,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110556,
        "cited_id": 276591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110556,
        "cited_id": 291232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110556,
        "cited_id": 291907,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110556,
        "cited_id": 296899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110556,
        "cited_id": 375540,
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
    "date_created": "2026-07-04T23:22:08Z",
    "date_modified": "2026-07-06T07:29:13Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:22:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:22:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:26:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:22:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — California v. Prysock

```
<opinion type="majority">
<author id="b397-7">Per Curiam.</author>
<p id="b397-8">This case presents the question whether the warnings given to respondent prior to a recorded conversation with a police officer satisfied the requirements of <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Although ordinarily this Court would not be inclined to review a case involving application of that precedent to a particular set of facts, see <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="109997"><a href="/opinion/109997/fare-acting-chief-probation-officer-v-michael-c/#1314" aria-description="Citation for case: Fare, Acting Chief Probation Officer v. Michael C.">439 U. S. 1310, 1314</a></span> (1978) (Rehnquist, J., in chambers, opinion of Court at <span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707</a></span> (1979)), the opinion of the California Court of Appeal essentially laid down a flat rule requiring that the content of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings be a virtual incantation of the precise language contained in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>opinion. Because such a rigid rule was not mandated by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>or any other decision of this Court, and is not required to serve the purposes of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>we grant the motion <page-number citation-index="1" label="356">*356</page-number>of respondent for leave to proceed <em>in forma -pauperis </em>and the petition for certiorari and reverse.</p>
<p id="b398-5">On January 30, 1978, Mrs. Donna Iris Erickson was brutally murdered. Later that evening respondent and a co-defendant were apprehended for commission of the offense. Respondent was brought to a substation of the Tulare County Sheriff's Department and advised of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. He declined to talk and, since he was a minor, his parents were notified. Respondent’s parents arrived and after meeting with them respondent decided to answer police questions. An officer questioned respondent, on tape, with respondent’s parents present. The tape reflects that the following warnings were given prior to any questioning:</p>
<blockquote id="b398-6">“Sgt. Byrd: . . . Mr. Randall James Prysock, earlier today I advised you of your legal rights and at that time you advised me you did not wish to talk to me, is that correct?</blockquote>
<blockquote id="b398-7">“Randall P.: Yeh.</blockquote>
<blockquote id="b398-8">“Sgt. Byrd: And, uh, during, at the first interview your folks were not present, they are now present. I want to go through your legal rights again with you and after each legal right I would like for you to answer whether you understand it or not. . . . Your legal rights, Mr. Prysock, is [sic] follows: Number One, you have the right to remain silent. This means you don’t have to talk to me at all unless you so desire. Do you understand this?</blockquote>
<blockquote id="b398-9">“Randall P.: Yeh.</blockquote>
<blockquote id="b398-10">“Sgt. Byrd: If you give up your right to remain silent, anything you say can and will be used as evidence against you in a court of law. Do you understand this?</blockquote>
<blockquote id="b398-11">“Randall P.: Yes.</blockquote>
<blockquote id="b398-12">“Sgt. Byrd: You have the right to talk to a lawyer before you are questioned, have him present with you while you are being questioned, and all during the questioning. Do you understand this?</blockquote>
<blockquote id="b399-5"><page-number citation-index="1" label="357">*357</page-number>“Randall P.: Yes.</blockquote>
<blockquote id="b399-6">“Sgt. Byrd: You also, being a juvenile, you have the right to have your parents present, which they are. Do you understand this?</blockquote>
<blockquote id="b399-7">“Randall P.: Yes.</blockquote>
<blockquote id="b399-8">“Sgt. Byrd: Even if they weren’t here, you’d have this right. Do you understand this?</blockquote>
<blockquote id="b399-9">“Randall P.: Yes.</blockquote>
<blockquote id="b399-10">“Sgt. Byrd: You all, uh, — if,—you have the right to have a lawyer appointed to represent you at no cost to yourself. Do you understand this?</blockquote>
<blockquote id="b399-11">“Randall P.: Yes.</blockquote>
<blockquote id="b399-12">“Sgt. Byrd: Now, having all these legal rights in mind, do you wish to talk to me at this time?</blockquote>
<blockquote id="b399-13">“Randall P.: Yes.” App. A to Pet. for Cert, i-iii.</blockquote>
<p id="b399-14">At this point, at the request of Mrs. Prysock, a conversation took place with the tape recorder turned off. According to Sgt. Byrd, Mrs. Prysock asked if respondent could still have an attorney at a later time if he gave a statement now without one. Sgt. Byrd assured Mrs. Prysock that respondent would have an attorney when he went to court and that “he could have one at this time if he wished one.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span> </em>at ll.<footnotemark>1</footnotemark></p>
<p id="b400-4"><page-number citation-index="1" label="358">*358</page-number>At trial in the Superior Court of Tulare County the court denied respondent’s motion to suppress the taped statement. Respondent was convicted by a jury of first-degree murder with two special circumstances — torture and robbery. Cal. Penal Code Ann. §§ 187, 190.2, 12022 (b) (West Supp. 1981). He was also convicted of robbery with the use of a dangerous weapon, §§ 211, 12022 (b), burglary with the use of a deadly weapon, §§ 459, 12022 (b), automobile theft, Cal. Veh. Code Ann. § 10851 (West Supp. 1981), escape from a youth facility, Cal. Welf. &amp; Inst. Code Ann. § 871 (West 1972), and destruction of evidence, Cal. Penal Code Ann. § 135 (West 1970).</p>
<p id="b400-5">The Court of Appeal for the Fifth Appellate District reversed respondent’s convictions and ordered a new trial because of what it thought to be error under <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>App. A to Pet. for Cert. 4. The Court of Appeal ruled that respondent’s recorded incriminating statements, given with his parents present, had to be excluded from consideration by the jury because respondent was not properly advised of his right to the services of a free attorney before and during interrogation. Although respondent was indisputably informed that he had “the right to talk to a lawyer before you are questioned, have him present with you while you are being questioned, and all during the questioning,” and further informed that he had “the right to have a lawyer appointed to represent you at no cost to yourself,” the Court of Appeal ruled that these warnings were inadequate because respondent <page-number citation-index="1" label="359">*359</page-number>was not explicitly informed of his right to have an attorney appointed before further questioning. The Court of Appeal stated that “[o]ne of <em>[Miranda’s,] </em>virtues is its precise requirements which are so easily met,” and quoted from <em>Harryman </em>v. <em>Estelle, </em><span class="citation" data-id="9466546"><a href="/opinion/375540/burley-clifton-harryman-v-w-j-estelle-jr-director-texas-department/#873" aria-description="Citation for case: Burley Clifton Harryman v. W. J. Estelle, Jr., Director,...">616 F. 2d 870, 873-874</a></span> (CA5), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/860/">449 U. S. 860</a></span> (1980), that “ 'the rigidity of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rules and the way in which they are to be applied was conceived of and continues to be recognized as the decision’s greatest strength.’ ” App. A to Pet. for Cert. 12. Relying on two previous decisions of the California Court of Appeal, <em>People </em>v. <em>Bolinski, </em><span class="citation no-link">260 Cal. App. 2d 706</span>, <span class="citation" data-id="2210787"><a href="/opinion/2210787/people-v-bolinski/" aria-description="Citation for case: People v. Bolinski">67 Cal. Rptr. 347</a></span> (1968), and <em>People </em>v. <em>Stewart, </em><span class="citation" data-id="2209476"><a href="/opinion/2209476/people-v-stewart/" aria-description="Citation for case: People v. Stewart">267 Cal. App. 2d 366</a></span>, <span class="citation" data-id="2209476"><a href="/opinion/2209476/people-v-stewart/" aria-description="Citation for case: People v. Stewart">73 Cal. Rptr. 484</a></span> (1968), the court ruled that the requirements of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>were not met in this case.<footnotemark>2</footnotemark> The California Supreme Court denied a petition for hearing, with two justices dissenting. App. D to Pet. for Cert.</p>
<p id="b401-5">This Court has never indicated that the “rigidity” of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>extends to the precise formulation of the warnings given a criminal defendant. See, <em>e. g., United States </em>v. <em>Lamia, </em><span class="citation" data-id="291232"><a href="/opinion/291232/united-states-v-robert-anthony-lamia/#375" aria-description="Citation for case: United States v. Robert Anthony Lamia">429 F. 2d 373, 375-376</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./400/907/">400 U. S. 907</a></span> (1970). This Court and others <em>have </em>stressed as one virtue of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>the fact that the giving of the warnings obviates the need for a case-by-case inquiry into the actual voluntariness of the admissions of the accused. See <em>Fare </em>v. <em>Michael C., </em>42 U. S., at 718; <em>Harryman </em>v. <em><span class="citation" data-id="9466546"><a href="/opinion/375540/burley-clifton-harryman-v-w-j-estelle-jr-director-texas-department/" aria-description="Citation for case: Burley Clifton Harryman v. W. J. Estelle, Jr., Director,...">Estelle, supra.</a></span> </em>Nothing in these observations suggests any desirable rigidity in the <em>form </em>of the required warnings.</p>
<p id="b401-6">Quite the contrary, <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>itself indicated that no talis-manic incantation was required to satisfy its strictures. The Court in that case stated that “[t]he warnings required and the waiver necessary in accordance with our opinion today <page-number citation-index="1" label="360">*360</page-number>are, <em>in the absence of a fully effective equivalent, </em>prerequisites to the admissibility of any statement made by a defendant.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#476" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 476</a></span> (emphasis supplied). See also <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona"><em>id., </em>at 479</a></span>. Just last Term in considering when <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>applied we noted that that decision announced procedural safeguards including “the now familiar <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings <em>... or their equivalent.” Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#297" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 297</a></span> (1980) (emphasis supplied).</p>
<p id="b402-5">Other courts considering the precise question presented by this case — whether a criminal defendant was adequately informed of his right to the presence of appointed counsel prior to and during interrogation — have not required a verbatim recital of the words of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>opinion but rather have examined the warnings given to determine if the reference to the right to appointed counsel was linked with some future point in time after the police interrogation. In <em>United States </em>v. <em>Garcia, </em><span class="citation" data-id="291907"><a href="/opinion/291907/united-states-v-irene-rubio-garcia/" aria-description="Citation for case: United States v. Irene Rubio Garcia">431 F. 2d 134</a></span> (CA9 1970) <em>(per </em>curiam), for example, the court found inadequate advice to the defendant that she could “have an attorney appointed to represent you when you first appear before the U. S. Commissioner or the Court.” <em>People </em>v. <em><span class="citation" data-id="2210787"><a href="/opinion/2210787/people-v-bolinski/" aria-description="Citation for case: People v. Bolinski">Bolinski, supra,</a></span> </em>relied upon by the court below, is a case of this type. Two separate sets of warnings were ruled inadequate. In the first, the defendant was advised that <em>“if he was charged </em>... he would be appointed counsel.” <span class="citation" data-id="2210787"><a href="/opinion/2210787/people-v-bolinski/#718" aria-description="Citation for case: People v. Bolinski">260 Cal. App. 2d, at 718</a></span>, <span class="citation" data-id="2210787"><a href="/opinion/2210787/people-v-bolinski/#355" aria-description="Citation for case: People v. Bolinski">67 Cal. Rptr., at 355</a></span> (emphasis supplied). In the second, the defendant, then in Illinois and about to be moved to California, was advised that “ 'the court would appoint [an attorney] <em>in Riverside County </em>[, California].’ ” <em>Id., </em>at 723, <span class="citation" data-id="2210787"><a href="/opinion/2210787/people-v-bolinski/#359" aria-description="Citation for case: People v. Bolinski">67 Cal. Rptr., at 359</a></span> (emphasis supplied). In both instances the reference to appointed counsel was linked to a future point in time after police interrogation, and therefore did not fully advise the suspect of his right to appointed counsel before such interrogation.</p>
<p id="b402-6">Here, in contrast, nothing in the warnings given respondent suggested any limitation on the right to the presence of <page-number citation-index="1" label="361">*361</page-number>appointed counsel different from the clearly conveyed rights to a lawyer in general, including the right “to a lawyer before you are questioned, . . . while you are being questioned, and all during the questioning.” App. A to Pet. for Cert. 9-10; ii. Like <em>United States </em>v. <em>Noa, </em><span class="citation" data-id="1447295"><a href="/opinion/1447295/levy-v-kimball/" aria-description="Citation for case: Levy v. Kimball">443 P. 2d 144</a></span> (CA9 1971), where the warnings given were substantially similar to those given here and defendant’s argument was the same as that adopted by the Court of Appeal, “[t]his is not a case in which the defendant was not informed of his right to the presence of an attorney during questioning ... or in which the offer of an appointed attorney was associated with a future time in court . . . .” <span class="citation" data-id="1447295"><a href="/opinion/1447295/levy-v-kimball/#146" aria-description="Citation for case: Levy v. Kimball"><em>Id., </em>at 146</a></span>.</p>
<p id="b403-5">It is clear that the police in this case fully conveyed to respondent his rights as required by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>He was told of his right to have a lawyer present prior to and during interrogation, and his right to have a lawyer appointed at no cost if he coüld not afford one. These warnings conveyed to respondent his right to have a lawyer appointed if he could not afford one prior to and during interrogation. The Court of Appeal erred in holding that the warnings were inadequate simply because of the order in which they were given.<footnotemark>3</footnotemark></p>
<p id="b404-4"><page-number citation-index="1" label="362">*362</page-number>Because respondent was given the warnings required by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>the decision of the California Court of Appeal to the contrary is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b404-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b399-15"> The tape reflects the following concerning the off-the-record discussion:</p>
<blockquote id="b399-16">“Sgt. Byrd: . . . Okay, Mrs. Prysock, you asked to get off the tape During that time you asked, decided you wanted some time to think about getting, whether to hire a lawyer or not.</blockquote>
<blockquote id="b399-17">“Mrs. P.: ’Cause I didn’t understand it.</blockquote>
<blockquote id="b399-18">“Sgt. Byrd: And you have decided now that you want to go ahead and you do not wish a lawyer present at this time?</blockquote>
<blockquote id="b399-19">“Mrs. P.: That’s right.</blockquote>
<blockquote id="b399-20">“Sgt. Byrd: And I have not persuaded you in any way, is that correct?</blockquote>
<blockquote id="b399-21">“Mrs. P.: No, you have not.</blockquote>
<blockquote id="b399-22">“Sgt. Byrd: And, Mr. Prysock is that correct that I have done nothing to persuade you not to, to hire a lawyer or to go on with this?</blockquote>
<blockquote id="b399-23">“Mr. P.: That’s right.</blockquote>
<blockquote id="b400-6"><page-number citation-index="1" label="358">*358</page-number>“Sgt. Byrd: Okay, everything we’re doing here is strictly in accordance with Randall and yourselves, is that correct?</blockquote>
<blockquote id="b400-7">“Mr. P.: That is correct.</blockquote>
<blockquote id="b400-8">“Sgt. Byrd: Okay. Uh, all right, Randy, I can’t remember where I left off, I think I asked you, uh, with your legal rights in mind, do you wish to talk to me at this time? This is with everything I told you, all your legal rights, your right to an attorney, your right, and your right to remain silent, and all these, I mean do you wish to talk to me at this time about the case?</blockquote>
<blockquote id="b400-9">“Randall P.: Yes.” App. A to Pet. for Cert, iii-iv.</blockquote>
</footnote>
<footnote label="2">
<p id="b401-7"> Contrary to respondent’s suggestion, it is clear that the decision below was based on federal law. The Court of Appeal stated that it was reversing and ordering a new trial “because of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>error.” <em>Id., </em>at 4.</p>
</footnote>
<footnote label="3">
<p id="b403-6"> The dissent, arguing that the Court of Appeal opinion is unfairly criticized as requiring mimicking of <em>Miranda, post, </em>at 365-366, ignores substantial portions of the opinion below and substitutes arguments of its own for those articulated by the Court of Appeal. For example, the dissent makes no mention of the lower court’s stress on the “precise requirements” of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>or its “rigidity” in this area, and ignores the portion of the opinion in which the court quotes from <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and then criticizes the officer for not repeating the exact language in advising respondent of his rights. See App. A to Pet. for Cert. 12-14. The Court of Appeal did conclude that respondent was not advised of his right to appointed counsel prior to and during interrogation, but this was <em>because </em>the officer did not parrot the language of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>The more substantive reasons suggested by the dissent are implausible. The reference to “appointed” counsel has never been considered as suggesting that the availability of counsel was postponed, and Mrs. Prysock’s off-the-record conversation was occasioned by her fear that waiving the right to counsel at interrogation <page-number citation-index="1" label="362">*362</page-number>would occasion a waiver of the right to counsel later in court, Ápp. A to Pet. for Cert. 11, clearly indicating that the officer conveyed the right to counsel at interrogation.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Coolidge v. New Hampshire.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Coolidge v. New Hampshire"
type: case
citation: "403 U.S. 443 (1971)"
parallel_cite: "91 S. Ct. 2022; 29 L. Ed. 2d 564"
neutral_cite: 1971 U.S. LEXIS 25
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1971
date_decided: 1971-06-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 1971-06-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Coolidge v. New Hampshire
  varies_by_point: true
  scope_note: "Horton v. California (1990) abandoned the inadvertence requirement of the Coolidge plurality's plain-view formulation; the prior-justification and immediately-apparent requirements survive."
  point_overrides:
    - point: legacy-limited-coolidge-v-new-hampshire
      point_label: Legacy limited treatment point
      field_i_validity: caution
      as_of_treatment: 2026-06-30
      s3_binding_status: provisional
      by:
        - name: Horton v. California
          cluster_id: 112448
          cite: 496 U.S. 128
          field_ii: limited
      scope_note: "Horton v. California (1990) abandoned the inadvertence requirement of the Coolidge plurality's plain-view formulation; the prior-justification and immediately-apparent requirements survive."
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108377/coolidge-v-new-hampshire/"
  cluster_id: 108377
  opinion_id: 108377
  identity_checked: true
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Key — Anchor"
  - page: "[[The Neutral and Detached Magistrate]]"
    role: "Related (cross-doctrine)"
related: ["[[Horton v. California]]", "[[Arizona v. Hicks]]", "[[Texas v. Brown]]"]
aliases: []
tags: ["case", "fourth-amendment", "plain-view", "warrant-requirement", "inadvertence", "immediately-apparent"]
holding: "ORIGIN of the modern plain-view doctrine (Stewart plurality). Plain view justifies a warrantless seizure only where the incriminating…"
lake:
  record_id: Coolidge v. New Hampshire
  status: verified
  projected_at: 2026-07-06
---

# Coolidge v. New Hampshire

*403 U.S. 443 (1971)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)* — inadvertence prong abandoned by [[Horton v. California]]
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating a murder, police seized Coolidge's car from his driveway under a warrant issued by the state attorney general (who was leading the prosecution) and later searched it, vacuuming up incriminating particles. The Court invalidated the warrant because it was not issued by a neutral and detached magistrate, then addressed whether the seizure could be sustained under the [[Plain View Doctrine|plain-view doctrine]].

## Issue
What conditions justify a warrantless seizure of evidence under the "plain view" doctrine.

## Rule
Plain view supplements a prior justified intrusion; it does not authorize a planned warrantless seizure on its own. "What the 'plain view' cases have in common is that the police officer in each of them had a prior justification for an intrusion in the course of which he came inadvertently across a piece of evidence incriminating the accused." — 403 U.S. 443, 466. ^pin-466

"[T]he extension of the original justification is legitimate only where it is immediately apparent to the police that they have evidence before them; the 'plain view' doctrine may not be used to extend a general exploratory search from one object to another until something incriminating at last emerges." — *Id.* ^pin-466a

*(The plurality's inadvertence requirement was later abandoned by [[Horton v. California]]; the prior-justification and immediately-apparent requirements remain.)*

## Application
The police knew about Coolidge's car well in advance and seized it from the driveway pursuant to an invalid warrant — a planned seizure of a known, anticipated object, not an inadvertent discovery during a lawful intrusion. Because the seizure was neither inadvertent nor supported by a valid warrant, the [[Plain View Doctrine|plain-view doctrine]] did not save it on these facts.

## Conclusion
The warrantless seizure of the car could not be justified as plain view; the evidence should have been suppressed. *Coolidge* states the modern plain-view framework (Stewart plurality).

## Treatment & subsequent history
- **Status:** limited *(as of 2026-06-30)* — **Binding — SCOTUS** for the surviving requirements.
- **Inadvertence requirement abandoned by** [[Horton v. California]] (1990): a plain-view seizure need not be inadvertent so long as the officer is lawfully present and the incriminating character is immediately apparent. *Coolidge*'s prior-justification and immediately-apparent requirements continue to govern; [[Arizona v. Hicks]] confirmed that "immediately apparent" requires probable cause.

## Appears on
- [[Plain View Doctrine]] — *Key — Anchor*
- [[The Neutral and Detached Magistrate]] — *Related (cross-doctrine)*

## Sources
- *Coolidge v. New Hampshire*, 403 U.S. 443 (1971) — https://www.courtlistener.com/opinion/108377/coolidge-v-new-hampshire/ — pinpoint: 466.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0380471b78aab7ef", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Coolidge v. New Hampshire"}, "payload": {"all": [{"cite": "403 U.S. 443", "page": "443", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "403"}, {"cite": "91 S. Ct. 2022", "page": "2022", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "91"}, {"cite": "29 L. Ed. 2d 564", "page": "564", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "29"}, {"cite": "1971 U.S. LEXIS 25", "page": "25", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1971"}], "display": "403 U.S. 443", "official": {"cite": "403 U.S. 443", "page": "443", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "403"}, "official_selection_present": true, "record_id": "Coolidge v. New Hampshire"}}
{"assertion_id": "4217e56fda2d824b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-466a", "record_id": "Coolidge v. New Hampshire"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-466a", "pinpoint_status": "slip-only", "quote": "[T]he extension of the original justification is legitimate only where it is immediately apparent to the police that they have evidence before them; the 'plain view' doctrine may not be used to extend a general exploratory search from one object to another until something incriminating at last emerges.", "quote_fidelity": "mismatch", "record_id": "Coolidge v. New Hampshire", "star_marker": null}}
{"assertion_id": "e212cbb4e684ae92", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-466", "record_id": "Coolidge v. New Hampshire"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-466", "pinpoint_status": "slip-only", "quote": "doctrine. ## Rule Plain view supplements a prior justified intrusion; it does not authorize a planned warrantless seizure on its own.", "quote_fidelity": "mismatch", "record_id": "Coolidge v. New Hampshire", "star_marker": null}}
{"assertion_id": "aecac23ce6b9f996", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Coolidge v. New Hampshire"}, "payload": {"as_of_content": "1971-06-21", "as_of_treatment": "2026-06-30", "field_i_validity": "caution", "record_id": "Coolidge v. New Hampshire", "scope_note": "Horton v. California (1990) abandoned the inadvertence requirement of the Coolidge plurality's plain-view formulation; the prior-justification and immediately-apparent requirements survive.", "varies_by_point": true}}
```

### lake record — Coolidge v. New Hampshire

```json
{
  "schema_version": "s2.v1",
  "record_id": "Coolidge v. New Hampshire",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Coolidge v. New Hampshire",
    "case_name_short": "Coolidge",
    "case_name_full": "Coolidge v. New Hampshire",
    "input_case_name": "Coolidge v. New Hampshire",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1971-06-21",
    "year": 1971,
    "docket": null,
    "cluster_id": 108377,
    "lead_opinion_id": 108377,
    "sibling_ids": [
      108377,
      9424643,
      9424644,
      9424645,
      9424646,
      9424647
    ],
    "absolute_url": "/opinion/108377/coolidge-v-new-hampshire/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "403 U.S. 443",
      "volume": "403",
      "reporter": "U.S.",
      "page": "443",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "91 S. Ct. 2022",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "2022",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "29 L. Ed. 2d 564",
        "volume": "29",
        "reporter": "L. Ed. 2d",
        "page": "564",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1971 U.S. LEXIS 25",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "25",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "403 U.S. 443",
        "volume": "403",
        "reporter": "U.S.",
        "page": "443",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 S. Ct. 2022",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "2022",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "29 L. Ed. 2d 564",
        "volume": "29",
        "reporter": "L. Ed. 2d",
        "page": "564",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1971 U.S. LEXIS 25",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "25",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "403 U.S. 443",
    "official_selection": {
      "court_class": "scotus",
      "selected": "403 U.S. 443",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-466",
      "page": null,
      "quote": "doctrine. ## Rule Plain view supplements a prior justified intrusion; it does not authorize a planned warrantless seizure on its own.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-466a",
      "page": null,
      "quote": "[T]he extension of the original justification is legitimate only where it is immediately apparent to the police that they have evidence before them; the 'plain view' doctrine may not be used to extend a general exploratory search from one object to another until something incriminating at last emerges.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "1971-06-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Coolidge v. New Hampshire",
    "varies_by_point": true,
    "scope_note": "Horton v. California (1990) abandoned the inadvertence requirement of the Coolidge plurality's plain-view formulation; the prior-justification and immediately-apparent requirements survive.",
    "point_overrides": [
      {
        "point": "legacy-limited-coolidge-v-new-hampshire",
        "point_label": "Legacy limited treatment point",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "provisional",
        "by": [
          {
            "name": "Horton v. California",
            "cluster_id": 112448,
            "cite": "496 U.S. 128",
            "field_ii": "limited"
          }
        ],
        "scope_note": "Horton v. California (1990) abandoned the inadvertence requirement of the Coolidge plurality's plain-view formulation; the prior-justification and immediately-apparent requirements survive."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "Horton v. California",
          "cluster_id": 112448,
          "cite": "496 U.S. 128",
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
          "name": "Martin v. State",
          "cluster_id": 10740496,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Coolidge v. New Hampshire:lane1_negative"
      },
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
        "journal_ref": "Coolidge v. New Hampshire:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Bock (A169480)",
          "cluster_id": 10134134,
          "cite": [
            "310 Or. App. 329",
            "485 P.3d 931"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Coolidge v. New Hampshire:lane1_negative"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Payton v. New York",
          "cluster_id": 110235,
          "cite": [
            "63 L. Ed. 2d 639",
            "100 S. Ct. 1371",
            "445 U.S. 573",
            "1980 U.S. LEXIS 13"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adams v. Williams",
          "cluster_id": 108571,
          "cite": [
            "32 L. Ed. 2d 612",
            "92 S. Ct. 1921",
            "407 U.S. 143",
            "1972 U.S. LEXIS 2206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gerstein v. Pugh",
          "cluster_id": 109186,
          "cite": [
            "43 L. Ed. 2d 54",
            "95 S. Ct. 854",
            "420 U.S. 103",
            "1975 U.S. LEXIS 29",
            "19 Fed. R. Serv. 2d 1499"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ross",
          "cluster_id": 110719,
          "cite": [
            "72 L. Ed. 2d 572",
            "102 S. Ct. 2157",
            "456 U.S. 798",
            "1982 U.S. LEXIS 18",
            "50 U.S.L.W. 4580"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Robinson",
          "cluster_id": 108893,
          "cite": [
            "38 L. Ed. 2d 427",
            "94 S. Ct. 467",
            "414 U.S. 218",
            "1973 U.S. LEXIS 21",
            "66 Ohio Op. 2d 202"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Belton",
          "cluster_id": 110559,
          "cite": [
            "69 L. Ed. 2d 768",
            "101 S. Ct. 2860",
            "453 U.S. 454",
            "1981 U.S. LEXIS 13"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Opperman",
          "cluster_id": 109537,
          "cite": [
            "49 L. Ed. 2d 1000",
            "96 S. Ct. 3092",
            "428 U.S. 364",
            "1976 U.S. LEXIS 15"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Place",
          "cluster_id": 110979,
          "cite": [
            "77 L. Ed. 2d 110",
            "103 S. Ct. 2637",
            "462 U.S. 696",
            "1983 U.S. LEXIS 74",
            "51 U.S.L.W. 4844"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Brown",
          "cluster_id": 110901,
          "cite": [
            "75 L. Ed. 2d 502",
            "103 S. Ct. 1535",
            "460 U.S. 730",
            "1983 U.S. LEXIS 143",
            "51 U.S.L.W. 4361"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
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
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Chadwick",
          "cluster_id": 109714,
          "cite": [
            "53 L. Ed. 2d 538",
            "97 S. Ct. 2476",
            "433 U.S. 1",
            "1977 U.S. LEXIS 133"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Coolidge v. New Hampshire:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108377 OR 9424643 OR 9424644 OR 9424645 OR 9424646 OR 9424647) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTY3MTIzMjAwMDAwJnM9NDY1ODI3NyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108377+OR+9424643+OR+9424644+OR+9424645+OR+9424646+OR+9424647%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108377 OR 9424643 OR 9424644 OR 9424645 OR 9424646 OR 9424647)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzgzJnM9MTA5NTA0JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108377+OR+9424643+OR+9424644+OR+9424645+OR+9424646+OR+9424647%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108377 OR 9424643 OR 9424644 OR 9424645 OR 9424646 OR 9424647)",
        "reviewed": 99,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 99,
        "triage_read": 2,
        "triage_snippet_classified": 97
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108377 OR 9424643 OR 9424644 OR 9424645 OR 9424646 OR 9424647)",
    "indexed_citing_opinions": 5998,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108377,
        "count": 5499,
        "count_source": "search"
      },
      {
        "opinion_id": 9424643,
        "count": 661,
        "count_source": "search"
      },
      {
        "opinion_id": 9424644,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9424645,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9424646,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9424647,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 9038,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/coolidge-v-new-hampshire.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNDA0NTgmcz0xMDU1NjA2MyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28108377+OR+9424643+OR+9424644+OR+9424645+OR+9424646+OR+9424647%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108377,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 100621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 101118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 101180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 103100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107952,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 107982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 108186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 108301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 108302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 108335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 263859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 291194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 293653,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 1139971,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108377,
        "cited_id": 1501475,
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
    "date_created": "2026-07-05T01:09:56Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: limited -> caution",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T01:10:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T01:10:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:31Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T01:10:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Coolidge v. New Hampshire (truncated)

```
<div>
<center><b><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U.S. 443</a></span> (1971)</b></center>
<center><h1>COOLIDGE<br>
v.<br>
NEW HAMPSHIRE.</h1></center>
<center>No. 323.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 12, 1971</center>
<center>Decided June 21, 1971</center>
CERTIORARI TO THE SUPREME COURT OF NEW HAMPSHIRE.
<p><span class="star-pagination">*445</span> <i>Archibald Cox,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./400/814/">400 U. S. 814</a></span>, argued the cause for petitioner. With him on the briefs were <i>Matthias J. Reynolds, John A. Graf,</i> and <i>Robert L. Chiesa.</i></p>
<p><i>Alexander J. Kalinski</i> argued the cause for respondent. With him on the brief was <i>Warren B. Rudman,</i> Attorney General of New Hampshire.</p>
<p>MR. JUSTICE STEWART delivered the opinion of the Court.<sup>[*]</sup></p>
<p>We are called upon in this case to decide issues under the Fourth and Fourteenth Amendments arising in the context of a state criminal trial for the commission of a particularly brutal murder. As in every case, our single duty is to determine the issues presented in accord with the Constitution and the law.</p>
<p>Pamela Mason, a 14-year-old girl, left her home in Manchester, New Hampshire, on the evening of January 13, 1964, during a heavy snowstorm, apparently in response to a man's telephone call for a babysitter. Eight days later, after a thaw, her body was found by the side of a major north-south highway several miles away. She had been murdered. The event created great alarm in the area, and the police immediately began a massive investigation.</p>
<p>On January 28, having learned from a neighbor that the petitioner, Edward Coolidge, had been away from home on the evening of the girl's disappearance, the police went to his house to question him. They asked <span class="star-pagination">*446</span> him, among other things, if he owned any guns, and he produced three, two shotguns and a rifle. They also asked whether he would take a lie-detector test concerning his account of his activities on the night of the disappearance. He agreed to do so on the following Sunday, his day off. The police later described his attitude on the occasion of this visit as fully "cooperative." His wife was in the house throughout the interview.</p>
<p>On the following Sunday, a policeman called Coolidge early in the morning and asked him to come down to the police station for the trip to Concord, New Hampshire, where the lie-detector test was to be administered. That evening, two plainclothes policemen arrived at the Coolidge house, where Mrs. Coolidge was waiting with her mother-in-law for her husband's return. These two policemen were not the two who had visited the house earlier in the week, and they apparently did not know that Coolidge had displayed three guns for inspection during the earlier visit. The plainclothesmen told Mrs. Coolidge that her husband was in "serious trouble" and probably would not be home that night. They asked Coolidge's mother to leave, and proceeded to question Mrs. Coolidge. During the course of the interview they obtained from her four guns belonging to Coolidge, and some clothes that Mrs. Coolidge thought her husband might have been wearing on the evening of Pamela Mason's disappearance.</p>
<p>Coolidge was held in jail on an unrelated charge that night, but he was released the next day.<sup>[1]</sup> During the ensuing two and a half weeks, the State accumulated a quantity of evidence to support the theory that it was he who had killed Pamela Mason. On February 19, the results of the investigation were presented at a meeting between the police officers working on the case and the <span class="star-pagination">*447</span> State Attorney General, who had personally taken charge of all police activities relating to the murder, and was later to serve as chief prosecutor at the trial. At this meeting, it was decided that there was enough evidence to justify the arrest of Coolidge on the murder charge and a search of his house and two cars. At the conclusion of the meeting, the Manchester police chief made formal application, under oath, for the arrest and search warrants. The complaint supporting the warrant for a search of Coolidge's Pontiac automobile, the only warrant that concerns us here, stated that the affiant "has probable cause to suspect and believe, and does suspect and believe, and herewith offers satisfactory evidence, that there are certain objects and things used in the Commission of said offense, now kept, and concealed in or upon a certain vehicle, to wit: 1951 Pontiac two-door sedan. . . ." The warrants were then signed and issued by the Attorney General himself, acting as a justice of the peace. Under New Hampshire law in force at that time, all justices of the peace were authorized to issue search warrants. N. H. Rev. Stat. Ann. § 595:1 (repealed 1969).</p>
<p>The police arrested Coolidge in his house on the day the warrant issued. Mrs. Coolidge asked whether she might remain in the house with her small child, but was told that she must stay elsewhere, apparently in part because the police believed that she would be harassed by reporters if she were accessible to them. When she asked whether she might take her car, she was told that both cars had been "impounded," and that the police would provide transportation for her. Some time later, the police called a towing company, and about two and a half hours after Coolidge had been taken into custody the cars were towed to the police station. It appears that at the time of the arrest the cars were parked in the Coolidge driveway, and that although dark had fallen <span class="star-pagination">*448</span> they were plainly visible both from the street and from inside the house where Coolidge was actually arrested. The 1951 Pontiac was searched and vacuumed on February 21, two days after it was seized, again a year later, in January 1965, and a third time in April 1965.</p>
<p>At Coolidge's subsequent jury trial on the charge of murder, vacuum sweepings, including particles of gun powder, taken from the Pontiac were introduced in evidence against him, as part of an attempt by the State to show by microscopic analysis that it was highly probable that Pamela Mason had been in Coolidge's car.<sup>[2]</sup> Also introduced in evidence was one of the guns taken by the police on their Sunday evening visit to the Coolidge housea .22-caliber Mossberg rifle, which the prosecution claimed was the murder weapon. Conflicting ballistics testimony was offered on the question whether the bullets found in Pamela Mason's body had been fired from this rifle. Finally, the prosecution introduced vacuum sweepings of the clothes taken from the Coolidge house that same Sunday evening, and attempted to show through microscopic analysis that there was a high probability that the clothes had been in contact with Pamela Mason's body. Pretrial motions to suppress all this evidence were referred by the trial judge to the New Hampshire Supreme Court, which ruled the evidence admissible. 106 N. H. 186, <span class="citation" data-id="2286547"><a href="/opinion/2286547/state-v-coolidge/" aria-description="Citation for case: State v. Coolidge">208 A. 2d 322</a></span>. The jury found Coolidge guilty and he was sentenced to life imprisonment. The New Hampshire Supreme Court affirmed the judgment of conviction, 109 N. H. 403, <span class="citation" data-id="2326188"><a href="/opinion/2326188/state-v-coolidge/" aria-description="Citation for case: State v. Coolidge">260 A. 2d 547</a></span>, and we granted certiorari to consider the constitutional questions raised by the admission of this evidence against Coolidge at his trial. <span class="citation multiple-matches"><a href="/c/U.%20S./399/926/">399 U. S. 926</a></span>.</p>
<p></p>
<h2>
<span class="star-pagination">*449</span> I</h2>
<p>The petitioner's first claim is that the warrant authorizing the seizure and subsequent search of his 1951 Pontiac automobile was invalid because not issued by a "neutral and detached magistrate." Since we agree with the petitioner that the warrant was invalid for this reason, we need not consider his further argument that the allegations under oath supporting the issuance of the warrant were so conclusory as to violate relevant constitutional standards. Cf. <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span>; <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span>.</p>
<p>The classic statement of the policy underlying the warrant requirement of the Fourth Amendment is that of Mr. Justice Jackson, writing for the Court in <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, 13-14:</p>
<blockquote>"The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime. Any assumption that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers. . . . When the right of privacy must reasonably yield to the right of search is, as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent."</blockquote>
<p>Cf. <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#464" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 464</a></span>; <i>Giordenello</i> v. <i>United States, supra,</i> at 486. <i>Wong Sun</i> v. <span class="star-pagination">*450</span> <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#481" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 481-482</a></span>; <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#356" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 356-357</a></span>.</p>
<p>In this case, the determination of probable cause was made by the chief "government enforcement agent" of the Statethe Attorney Generalwho was actively in charge of the investigation and later was to be chief prosecutor at the trial. To be sure, the determination was formalized here by a writing bearing the title "Search Warrant," whereas in <i><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Johnson</a></span></i> there was no piece of paper involved, but the State has not attempted to uphold the warrant on any such artificial basis. Rather, the State argues that the Attorney General, who was unquestionably authorized as a justice of the peace to issue warrants under then-existing state law, did in fact act as a "neutral and detached magistrate." Further, the State claims that <i>any</i> magistrate, confronted with the showing of probable cause made by the Manchester chief of police, would have issued the warrant in question. To the first proposition it is enough to answer that there could hardly be a more appropriate setting than this for a <i>per se</i> rule of disqualification rather than a case-by-case evaluation of all the circumstances. Without disrespect to the state law enforcement agent here involved, the whole point of the basic rule so well expressed by Mr. Justice Jackson is that prosecutors and policemen simply cannot be asked to maintain the requisite neutrality with regard to their own investigationsthe "competitive enterprise" that must rightly engage their single-minded attention.<sup>[3]</sup> Cf. <i>Mancusi</i> v. <i>DeForte,</i> <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#371" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364, 371</a></span>. As for the proposition that the existence of probable cause renders noncompliance with the warrant procedure an irrelevance, <span class="star-pagination">*451</span> it is enough to cite <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33</a></span>, decided in 1925:</p>
<blockquote>"Belief, however well founded, that an article sought is concealed in a dwelling house furnishes no justification for a search of that place without a warrant. And such searches are held unlawful notwithstanding facts unquestionably showing probable cause."</blockquote>
<p>See also <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#497" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 497-498</a></span>; <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span>. ("[T]he rights . . . against unlawful search and seizure are to be protected even if the same result might have been achieved in a lawful way.")</p>
<p>But the New Hampshire Supreme Court, in upholding the conviction, relied upon the theory that even if the warrant procedure here in issue would clearly violate the standards imposed on the Federal Government by the Fourth Amendment, it is not forbidden the States under the Fourteenth. This position was premised on a passage from the opinion of this Court in <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span>, 31:</p>
<blockquote>"Preliminary to our examination of the search and seizures involved here, it might be helpful for us to indicate what was not decided in <i>Mapp</i> [v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>]. First, it must be recognized that the `principles governing the admissibility of evidence in federal criminal trials have not been restricted . . . to those derived solely from the Constitution. In the exercise of its supervisory authority over the administration of criminal justice in the federal courts . . . this Court has . . . formulated rules of evidence to be applied in federal criminal prosecutions.' <i>McNabb</i> v. <i>United States,</i> <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">318 U. S. 332</a></span>, 341 . . . <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span>,</i> however, established no assumption by this Court of supervisory authority over state courts . . . and, consequently, it implied no total <span class="star-pagination">*452</span> obliteration of state laws relating to arrests and searches in favor of federal law. <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> sounded no death knell for our federalism; rather, it echoed the sentiment of <i>Elkins</i> v. <i>United States, supra,</i> at 221, that `a healthy federalism depends upon the avoidance of needless conflict between state and federal courts' by itself urging that `[f]ederal-state cooperation in the solution of crime under constitutional standards will be promoted, if only by recognition of their now mutual obligation to respect <i>the same fundamental criteria</i> in their approaches.' <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#658" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 658</a></span>." (Emphasis in <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ker</a></span>.</i>)</blockquote>
<p>It is urged that the New Hampshire statutes which at the time of the searches here involved permitted a law enforcement officer himself to issue a warrant was one of those "workable rules governing arrests, searches and seizures to meet `the practical demands of effective criminal investigation and law enforcement' in the States," <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#34" aria-description="Citation for case: Ker v. California"><i>id.,</i> at 34</a></span>, authorized by <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ker</a></span>.</i></p>
<p>That such a procedure was indeed workable from the point of view of the police is evident from testimony at the trial in this case:</p>
<blockquote>"The Court: You mean that another police officer issues these [search warrants]?</blockquote>
<blockquote>"The Witness: Yes. Captain Couture and Captain Shea and Captain Loveren are J. P.'s.</blockquote>
<blockquote>"The Court: Well, let me ask you, Chief, your answer is to the effect that you never go out of the department for the Justice of the Peace?</blockquote>
<blockquote>"The Witness: It hasn't been ourpolicy to go out of the department.</blockquote>
<blockquote>"Q. Right. Your policy and experience, is to have a fellow police officer take the warrant in the capacity of Justice of the Peace?</blockquote>
<blockquote>"A. That has been our practice."</blockquote>
<p><span class="star-pagination">*453</span> But it is too plain for extensive discussion that this now abandoned New Hampshire method of issuing "search warrants" violated a fundamental premise of both the Fourth and Fourteenth Amendmentsa premise fully developed and articulated long before this Court's decisions in <i>Ker</i> v. <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">California, supra</a></span></i><i>,</i> and <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>. As Mr. Justice Frankfurter put it in <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span>, 27-28:</p>
<blockquote>"The security of one's privacy against arbitrary intrusion by the policewhich is at the core of the Fourth Amendmentis basic to a free society. It is therefore implicit in `the concept of ordered liberty' and as such enforceable against the States through the Due Process Clause. The knock at the door, whether by day or by night, as a prelude to a search, without authority of law but solely on the authority of the police, did not need the commentary of recent history to be condemned . . . ."</blockquote>
<p>We find no escape from the conclusion that the seizure and search of the Pontiac automobile cannot constitutionally rest upon the warrant issued by the state official who was the chief investigator and prosecutor in this case. Since he was not the neutral and detached magistrate required by the Constitution, the search stands on no firmer ground than if there had been no warrant at all. If the seizure and search are to be justified, they must, therefore, be justified on some other theory.</p>
<p></p>
<h2>II</h2>
<p>The State proposes three distinct theories to bring the facts of this case within one or another of the exceptions to the warrant requirement. In considering them, we must not lose sight of the Fourth Amendment's fundamental guarantee. Mr. Justice Bradley's admonition in his opinion for the Court almost a century ago in <i>Boyd</i> <span class="star-pagination">*454</span> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 635</a></span>, is worth repeating here:</p>
<blockquote>"It may be that it is the obnoxious thing in its mildest and least repulsive form; but illegitimate and unconstitutional practices get their first footing in that way, namely, by silent approaches and slight deviations from legal modes of procedure. This can only be obviated by adhering to the rule that constitutional provisions for the security of person and property should be liberally construed. A close and literal construction deprives them of half their efficacy, and leads to gradual depreciation of the right, as if it consisted more in sound than in substance. It is the duty of courts to be watchful for the constitutional rights of the citizen, and against any stealthy encroachments thereon."<sup>[4]</sup></blockquote>
<p>Thus the most basic constitutional rule in this area is that "searches conducted outside the judicial process, without prior approval by judge or magistrate, are <i>per se</i> <span class="star-pagination">*455</span> unreasonable under the Fourth Amendmentsubject only to a few specifically established and well-delineated exceptions."<sup>[5]</sup> The exceptions are "jealously and carefully drawn,"<sup>[6]</sup> and there must be "a showing by those who seek exemption . . . that the exigencies of the situation made that course imperative."<sup>[7]</sup> "[T]he burden is on those seeking the exemption to show the need for it."<sup>[8]</sup> In times of unrest, whether caused by crime or racial conflict or fear of internal subversion, this basic law and the values that it represents may appear unrealistic or "extravagant" to some. But the values were those of the authors of our fundamental constitutional concepts. In times not altogether unlike our own they wonby legal and constitutional means in England,<sup>[9]</sup> and by revolution on this continenta right of personal security against arbitrary intrusions by official power. If times have changed, reducing everyman's scope to do as he pleases in an urban and industrial world, the changes have made the values served by the Fourth Amendment more, not less, important.<sup>[10]</sup></p>
<p></p>
<h2>A</h2>
<p>The State's first theory is that the seizure on February 19 and subsequent search of Coolidge's Pontiac were "incident" to a valid arrest. We assume that the arrest of Coolidge inside his house was valid, so that the first condition of a warrantless "search incident" is met. <i>Whiteley</i> v. <i>Warden,</i> <span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560</a></span>, 567 n. 11. And since the events in issue took place in 1964, we assess the State's argument <span class="star-pagination">*456</span> in terms of the law as it existed before <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span>, which substantially restricted the "search incident" exception to the warrant requirement, but did so only prospectively. <i>Williams</i> v. <i>United States,</i> <span class="citation" data-id="9424503"><a href="/opinion/108301/williams-v-united-states/" aria-description="Citation for case: Williams v. United States">401 U. S. 646</a></span>. But even under pre-<span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California"><i>Chimel</i></a></span> law, the State's position is untenable.</p>
<p>The leading case in the area before <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> was <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>, which was taken to stand "for the proposition, <i>inter alia,</i> that a warrantless search `incident to a lawful arrest' may generally extend to the area that is considered to be in the `possession' or under the `control' of the person arrested." <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#760" aria-description="Citation for case: Chimel v. California"><i>Chimel, supra,</i> at 760</a></span>. In this case, Coolidge was arrested inside his house; his car was outside in the driveway. The car was not touched until Coolidge had been removed from the scene. It was then seized and taken to the station, but it was not actually searched until two days later.</p>
<p>First, it is doubtful whether the police could have carried out a contemporaneous search of the car under <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> standards. For this Court has repeatedly held that, even under <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span>,</i> "[a] search may be incident to an arrest ` "only if it is substantially contemporaneous with the arrest and is confined to the <i>immediate</i> vicinity of the arrest. . . ." ' " <i>Vale</i> v. <i>Louisiana,</i> <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#33" aria-description="Citation for case: Vale v. Louisiana">399 U. S. 30, 33</a></span>, quoting from <i>Shipley</i> v. <i>California,</i> <span class="citation" data-id="9424104"><a href="/opinion/107982/shipley-v-california/#819" aria-description="Citation for case: Shipley v. California">395 U. S. 818, 819</a></span>, quoting from <i>Stoner</i> v. <i>California,</i> <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#486" aria-description="Citation for case: Stoner v. California">376 U. S. 483, 486</a></span>. (Emphasis in <i><span class="citation" data-id="9424104"><a href="/opinion/107982/shipley-v-california/" aria-description="Citation for case: Shipley v. California">Shipley</a></span>.</i>) Cf. <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S., at 30-31</a></span>; <i>James</i> v. <i>Louisiana,</i> <span class="citation" data-id="107102"><a href="/opinion/107102/james-v-louisiana/" aria-description="Citation for case: James v. Louisiana">382 U. S. 36</a></span>. These cases make it clear beyond any question that a lawful pre-<span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California"><i>Chimel</i></a></span> arrest of a suspect outside his house could never by itself justify a warrantless search inside the house. There is nothing in search-incident doctrine (as opposed to the special rules for automobiles and evidence in "plain view," to be considered below) that suggests <span class="star-pagination">*457</span> a different result where the arrest is made inside the house and the search outside and at some distance away.<sup>[11]</sup></p>
<p>Even assuming, <i>arguendo,</i> that the police might have searched the Pontiac in the driveway when they arrested Coolidge in the house, <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span>, makes plain that they could not legally seize the car, remove it, and search it at their leisure without a warrant. In circumstances virtually identical to those here, MR. JUSTICE BLACK'S opinion for a unanimous Court held that "[o]nce an accused is under arrest and in custody, then a search [of his car] made at another place, without a warrant, is simply not incident to the arrest." <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States"><i>Id.,</i> at 367</a></span>. <i>Dyke</i> v. <i>Taylor Implement Mfg. Co.,</i> <span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S. 216</a></span> Cf. <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#47" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 47</a></span>. Search-incident doctrine, in short, has no applicability to this case.<sup>[12]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*458</span> B</h2>
<p>The second theory put forward by the State to justify a warrantless seizure and search of the Pontiac car is that under <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>, the police may make a warrantless search of an automobile whenever they have probable cause to do so, and, under our decision last Term in <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span>, whenever the police may make a legal contemporaneous search under <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>,</i> they may also seize the car, take it to the police station, and search it there. But even granting that the police had probable cause to search the car, the application of the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case to these facts would extend it far beyond its original rationale.</p>
<p><i>Carroll</i> did indeed hold that "contraband goods concealed and illegally transported in an automobile or other vehicle may be searched for without a warrant,"<sup>[13]</sup> provided that "the seizing officer shall have reasonable or probable cause for believing that the automobile which he stops and seizes has contraband liquor therein which is being illegally transported."<sup>[14]</sup> Such searches had been explicitly authorized by Congress, and, as we have pointed out elsewhere,<sup>[15]</sup> in the conditions of the time "[a]n automobile . . . was an almost indispensable instrumentality in large-scale violation of the National Prohibition Act, and the car itself therefore was treated somewhat as an offender and became contraband." In two later cases,<sup>[16]</sup> each involving an occupied automobile stopped on the open highway and searched for contraband <span class="star-pagination">*459</span> liquor, the Court followed and reaffirmed <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>.</i><sup>[17]</sup> And last Term in <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers, supra,</a></span></i> we did so again.</p>
<p>The underlying rationale of <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> and of all the cases that have followed it is that there is</p>
<blockquote>"a necessary difference between a search of a store, dwelling house or other structure in respect of which a proper official warrant readily may be obtained, and a search of a ship, motor boat, wagon or automobile, <span class="star-pagination">*460</span> for contraband goods, where <i>it is not practicable to secure a warrant</i> because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S., at 153</a></span>. (Emphasis supplied.)</blockquote>
<p>As we said in <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney"><i>Chambers, supra,</i> at 51</a></span>, "exigent circumstances" justify the warrantless search of "an automobile <i>stopped on the highway,</i>" where there is probable cause, because the car is "movable, the occupants are alerted, and the car's contents may never be found again if a warrant must be obtained." "[T]he opportunity to search is fleeting . . . ." (Emphasis supplied.)</p>
<p>In this case, the police had known for some time of the probable role of the Pontiac car in the crime. Coolidge was aware that he was a suspect in the Mason murder, but he had been extremely cooperative throughout the investigation, and there was no indication that he meant to flee. He had already had ample opportunity to destroy any evidence he thought incriminating. There is no suggestion that, on the night in question, the car was being used for any illegal purpose, and it was regularly parked in the driveway of his house. The opportunity for search was thus hardly "fleeting." The objects that the police are assumed to have had probable cause to search for in the car were neither stolen nor contraband nor dangerous.</p>
<p>When the police arrived at the Coolidge house to arrest him, two officers were sent to guard the back door while the main party approached from the front. Coolidge was arrested inside the house, without resistance of any kind on his part, after he had voluntarily admitted the officers at both front and back doors. There was no way in which he could conceivably have gained access to the automobile after the police arrived on his property. When Coolidge had been taken away, the police informed Mrs. Coolidge, the only other adult occupant of the <span class="star-pagination">*461</span> house, that she and her baby had to spend the night elsewhere and that she could not use either of the Coolidge cars. Two police officers then drove her in a police car to the house of a relative in another town, and they stayed with her there until around midnight, long after the police had had the Pontiac towed to the station house. The Coolidge premises were guarded throughout the night by two policemen.<sup>[18]</sup></p>
<p>The word "automobile" is not a talisman in whose presence the Fourth Amendment fades away and disappears. <span class="star-pagination">*462</span> And surely there is nothing in this case to invoke the meaning and purpose of the rule of <i>Carroll</i> v. <i>United States</i>no alerted criminal bent on flight, no fleeting opportunity on an open highway after a hazardous chase, no contraband or stolen goods or weapons, no confederates waiting to move the evidence, not even the inconvenience of a special police detail to guard the immobilized automobile. In short, by no possible stretch of the legal imagination can this be made into a case where "it is not practicable to secure a warrant," <i>Carroll,supra,</i> at 153, and the "automobile exception," despite its label, is simply irrelevant.<sup>[19]</sup></p>
<p><span class="star-pagination">*463</span> Since <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> would not have justified a warrantless search of the Pontiac at the time Coolidge was arrested, the later search at the station house was plainly illegal, at least so far as the automobile exception is concerned. <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers, supra,</a></span></i> is of no help to the State, since that case held only that, where the police may stop and search an automobile under <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>,</i> they may also seize it and search it later at the police station.<sup>[20]</sup> Rather, this case is controlled by <i>Dyke</i> v. <i>Taylor Implement Mfg. Co., supra</i><i>.</i> There the police lacked probable cause to seize or search the defendant's automobile at the time of his <span class="star-pagination">*464</span> arrest, and this was enough by itself to condemn the subsequent search at the station house. Here there was probable cause, but no exigent circumstances justified the police in proceeding without a warrant. As in <i><span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">Dyke</a></span>,</i> the later search at the station house was therefore illegal.<sup>[21]</sup></p>
<p></p>
<h2>C</h2>
<p>The State's third theory in support of the warrantless seizure and search of the Pontiac car is that the car itself was an "instrumentality of the crime," and as such might be seized by the police on Coolidge's property because it was in plain view. Supposing the seizure to be thus lawful, the case of <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span>, is said to support a subsequent warrantless search at the station house, with or without probable cause. Of course, the distinction between an "instrumentality of crime" and "mere evidence" was done away with by <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span>, and we may assume that the police had probable cause to seize the automobile.<sup>[22]</sup> But, for the reasons that follow, we hold that the "plain view" exception to the warrant requirement is inapplicable to this case. Since the seizure was therefore <span class="star-pagination">*465</span> illegal, it is unnecessary to consider the applicability of <i><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">Cooper, supra,</a></span></i> to the subsequent search.<sup>[23]</sup></p>
<p>It is well established that under certain circumstances the police may seize evidence in plain view without a warrant. But it is important to keep in mind that, in the vast majority of cases, <i>any</i> evidence seized by the police will be in plain view, at least at the moment of seizure. The problem with the "plain view" doctrine has been to identify the circumstances in which plain view has legal significance rather than being simply the normal concomitant of any search, legal or illegal.</p>
<p>An example of the applicability of the "plain view" doctrine is the situation in which the police have a warrant to search a given area for specified objects, and in the course of the search come across some other article of incriminating character. Cf. <i>Go-Bart Importing Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#358" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 358</a></span>; <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#465" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 465</a></span>; <i>Steele</i> v. <i>United States,</i> <span class="citation" data-id="100621"><a href="/opinion/100621/steele-v-united-states-no-1/" aria-description="Citation for case: Steele v. United States No. 1">267 U. S. 498</a></span>; <i>Stanley</i> v. <i>Georgia,</i> <span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/#571" aria-description="Citation for case: Stanley v. Georgia">394 U. S. 557, 571</a></span> (STEWART, J., concurring in result). Where the initial intrusion that brings the police within plain view of such an article is supported, not by a warrant, but by one of the recognized exceptions to the warrant requirement, the seizure is also legitimate. Thus the police may inadvertently come across evidence while in "hot pursuit" of a fleeing suspect. <i>Warden</i> v. <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden, supra</a></span></i><i>;</i> cf. <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span>. And an object that comes into view during a search incident to arrest that is appropriately limited in scope under existing law may be seized without a warrant.<sup>[24]</sup><i>Chimel</i> v. <i>California,</i> 395 <span class="star-pagination">*466</span> U. S., at 762-763. Finally, the "plain view" doctrine has been applied where a police officer is not searching for evidence against the accused, but nonetheless inadvertently comes across an incriminating object. <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">390 U. S. 234</a></span>; <i>Frazier</i> v. <i>Cupp,</i> <span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731</a></span>; <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#43" aria-description="Citation for case: Ker v. California">374 U. S., at 43</a></span>. Cf. <i>Lewis</i> v. <i>United States,</i> <span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/" aria-description="Citation for case: Lewis v. United States">385 U. S. 206</a></span>.</p>
<p>What the "plain view" cases have in common is that the police officer in each of them had a prior justification for an intrusion in the course of which he came inadvertently across a piece of evidence incriminating the accused. The doctrine serves to supplement the prior justificationwhether it be a warrant for another object, hot pursuit, search incident to lawful arrest, or some other legitimate reason for being present unconnected with a search directed against the accusedand permits the warrantless seizure. Of course, the extension of the original justification is legitimate only where it is immediately apparent to the police that they have evidence before them; the "plain view" doctrine may not be used to extend a general exploratory search from one object to another until something incriminating at last emerges. <span class="star-pagination">*467</span> Cf. <i>Stanley</i> v. <span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/#571" aria-description="Citation for case: Stanley v. Georgia"><i>Georgia, supra,</i> at 571-572</a></span> (STEWART, J., concurring in result).</p>
<p>The rationale for the "plain view" exception is evident if we keep in mind the two distinct constitutional protections served by the warrant requirement. First, the magistrate's scrutiny is intended to eliminate altogether searches not based on probable cause. The premise here is that <i>any</i> intrusion in the way of search or seizure is an evil, so that no intrusion at all is justified without a careful prior determination of necessity. See, <i>e. g., </i><i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>; <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span>; <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span>; <i>Chimel</i> v. <i>California,</i> 395 U. S., at 761-762. The second, distinct objective is that those searches deemed necessary should be as limited as possible. Here, the specific evil is the "general warrant" abhorred by the colonists, and the problem is not that of intrusion <i>per se,</i> but of a general, exploratory rummaging in a person's belongings. See, <i>e. g., </i><i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States">116 U. S., at 624-630</a></span>; <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#195" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 195-196</a></span>; <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476</a></span>. The warrant accomplishes this second objective by requiring a "particular description" of the things to be seized.</p>
<p>The "plain view" doctrine is not in conflict with the first objective because plain view does not occur until a search is in progress. In each case, this initial intrusion is justified by a warrant or by an exception such as "hot pursuit" or search incident to a lawful arrest, or by an extraneous valid reason for the officer's presence. And, given the initial intrusion, the seizure of an object in plain view is consistent with the second objective, since it does not convert the search into a general or exploratory one. As against the minor peril to Fourth Amendment protections, there is a major gain in effective law enforcement. Where, once an otherwise lawful search is in progress, the police inadvertently come upon <span class="star-pagination">*468</span> a piece of evidence, it would often be a needless inconvenience, and sometimes dangerousto the evidence or to the police themselvesto require them to ignore it until they have obtained a warrant particularly describing it.</p>
<p>The limits on the doctrine are implicit in the statement of its rationale. The first of these is that plain view <i>alone</i> is never enough to justify the warrantless seizure of evidence. This is simply a corollary of the familiar principle discussed above, that no amount of probable cause can justify a warrantless search or seizure absent "exigent circumstances." Incontrovertible testimony of the senses that an incriminating object is on premises belonging to a criminal suspect may establish the fullest possible measure of probable cause. But even where the object is contraband, this Court has repeatedly stated and enforced the basic rule that the police may not enter and make a warrantless seizure. <i>Taylor</i> v. <i>United States,</i> <span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">286 U. S. 1</a></span>; <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>; <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>; <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#497" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 497-498</a></span>; <i>Chapman</i> v. <i>United States,</i> <span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span>; <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span>.<sup>[25]</sup></p>
<p><span class="star-pagination">*469</span> The second limitation is that the discovery of evidence in plain view must be inadvertent.<sup>[26]</sup> The rationale of the exception to the warrant requirement, as just stated, <span class="star-pagination">*470</span> is that a plain-view seizure will not turn an initially valid (and therefore limited) search into a "general" one, while the inconvenience of procuring a warrant to cover an inadvertent discovery is great. But where the discovery is anticipated, where the police know in advance the location of the evidence and intend to seize it, the situation is altogether different. The requirement of a warrant to seize imposes no inconvenience whatever, or at least none which is constitutionally cognizable in a legal system that regards warrantless searches as "<i>per se</i> <span class="star-pagination">*471</span> unreasonable" in the absence of "exigent circumstances."</p>
<p>If the initial intrusion is bottomed upon a warrant that fails to mention a particular object, though the police know its location and intend to seize it, then there is a violation of the express constitutional requirement of "Warrants . . . particularly describing . . . [the] things to be seized." The initial intrusion may, of course, be legitimated not by a warrant but by one of the exceptions to the warrant requirement, such as hot pursuit or search incident to lawful arrest. But to extend the scope of such an intrusion to the seizure of objectsnot contraband nor stolen nor dangerous in themselveswhich the police know in advance they will find in plain view and intend to seize, would fly in the face of the basic rule that no amount of probable cause can justify a warrantless seizure.<sup>[27]</sup></p>
<p><span class="star-pagination">*472</span> In the light of what has been said, it is apparent that the "plain view" exception cannot justify the police seizure of the Pontiac car in this case. The police had ample opportunity to obtain a valid warrant; they knew the automobile's exact description and location well in advance; they intended to seize it when they came upon Coolidge's property. And this is not a case involving contraband or stolen goods or objects dangerous in themselves.<sup>[28]</sup></p>
<p><span class="star-pagination">*473</span> The seizure was therefore unconstitutional, and so was the subsequent search at the station house. Since evidence obtained in the course of the search was admitted at Coolidge's trial, the judgment must be reversed and the case remanded to the New Hampshire Supreme Court. <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>.</p>
<p></p>
<h2>D</h2>
<p>In his dissenting opinion today, MR. JUSTICE WHITE marshals the arguments that can be made against our interpretation of the "automobile" and "plain view" exceptions to the warrant requirement. Beyond the <span class="star-pagination">*474</span> unstartling proposition that when a line is drawn there is often not a great deal of difference between the situations closest to it on either side, there is a single theme that runs through what he has to say about the two exceptions. Since that theme is a recurring one in controversies over the proper meaning and scope of the Fourth Amendment, it seems appropriate to treat his views in this separate section, rather than piecemeal.</p>
<p>Much the most important part of the conflict that has been so notable in this Court's attempts over a hundred years to develop a coherent body of Fourth Amendment law has been caused by disagreement over the importance of requiring law enforcement officers to secure warrants. Some have argued that a determination by a magistrate of probable cause as a precondition of any search or seizure is so essential that the Fourth Amendment is violated whenever the police might reasonably have obtained a warrant but failed to do so. Others have argued with equal force that a test of reasonableness, applied after the fact of search or seizure when the police attempt to introduce the fruits in evidence, affords ample safeguard for the rights in question, so that "[t]he relevant test is not whether it is reasonable to procure a search warrant, but whether the search was reasonable."<sup>[29]</sup></p>
<p>Both sides to the controversy appear to recognize a distinction between searches and seizures that take place on a man's propertyhis home or officeand those carried out elsewhere. It is accepted, at least as a matter of principle, that a search or seizure carried out on a suspect's premises without a warrant is <i>per se</i> unreasonable, unless the police can show that it falls within one of a carefully defined set of exceptions based on the <span class="star-pagination">*475</span> presence of "exigent circumstances."<sup>[30]</sup> As to other kinds of intrusions, however, there has been disagreement about the basic rules to be applied, as our cases concerning automobile searches, electronic surveillance, street searches and administrative searches make clear.<sup>[31]</sup></p>
<p>With respect to searches and seizures carried out on a suspect's premises, the conflict has been over the question of what qualifies as an "exigent circumstance." It might appear that the difficult inquiry would be when it is that the police can enter upon a person's property to seize his "person . . . papers, and effects," without prior judicial approval. The question of the scope of search and seizure once the police are on the premises would appear to be subsidiary to the basic issue of when intrusion is permissible. But the law has not developed in this fashion.</p>
<p>The most common situation in which Fourth Amendment issues have arisen has been that in which the police enter the suspect's premises, arrest him, and then carry out a warrantless search and seizure of evidence. Where there is a warrant for the suspect's arrest, the evidence seized may later be challenged either on the ground that the warrant was improperly issued because there was not probable cause,<sup>[32]</sup> or on the ground that the police search and seizure went beyond that which they could carry out as an incident to the execution of the arrest warrant.<sup>[33]</sup> Where the police act without an <span class="star-pagination">*476</span> arrest warrant, the suspect may argue that an arrest warrant was necessary, that there was no probable cause to arrest,<sup>[34]</sup> or that even if the arrest was valid, the search and seizure went beyond permissible limits.<sup>[35]</sup> Perhaps because each of these lines of attack offers a plethora of litigable issues, the more fundamental question of when the police may arrest a man in his house without a warrant has been little considered in the federal courts. This Court has chosen on a number of occasions to assume the validity of an arrest and decide the case before it on the issue of the scope of permissible warrantless search. <i>E. g., </i><i>Chimel</i> v. <i>California, supra</i><i>.</i> The more common inquiry has therefore been: "Assuming a valid police entry for purposes of arrest, what searches and seizures may the police carry out without prior authorization by a magistrate?"</p>
<p>Two very broad, and sharply contrasting answers to this question have been assayed by this Court in the past. The answer of <i>Trupiano</i> v. <i>United States, supra</i><i>,</i> was that <i>no</i> searches and seizures could be legitimated by the mere fact of valid entry for purposes of arrest, so long as there was no showing of special difficulties in obtaining a warrant for search and seizure. The contrasting answer in <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span>, and <i>United States</i> v. <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz, supra</a></span></i><i>,</i> was that a valid entry for purposes of arrest served to legitimate warrantless searches and seizures throughout the premises where the arrest occurred, however spacious those premises might be.</p>
<p>The approach taken in <i>Harris</i> and <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> was open to the criticism that it made it so easy for the police to arrange to search a man's premises without a warrant <span class="star-pagination">*477</span> that the Constitution's protection of a man's "effects" became a dead letter. The approach taken in <i><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span>,</i> on the other hand, was open to the criticism that it was absurd to permit the police to make an entry in the dead of night for purposes of seizing the "person" by main force, and then refuse them permission to seize objects lying around in plain sight. It is arguable that if the very substantial intrusion implied in the entry and arrest are "reasonable" in Fourth Amendment terms, then the less intrusive search incident to arrest must also be reasonable.</p>
<p>This argument against the <i><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span></i> approach is of little force so long as it is assumed that the police must, in the absence of one of a number of defined exceptions based on "exigent circumstances," obtain an arrest warrant before entering a man's house to seize his person. If the Fourth Amendment requires a warrant to enter and seize the person, then it makes sense as well to require a warrant to seize other items that may be on the premises. The situation is different, however, if the police are under no circumstances required to obtain an arrest warrant before entering to arrest a person they have probable cause to believe has committed a felony. If no warrant is ever required to legitimate the extremely serious intrusion of a midnight entry to seize the person, then it can be argued plausibly that a warrant should never be required to legitimate a very sweeping search incident to such an entry and arrest. If the arrest without a warrant is <i>per se</i> reasonable under the Fourth Amendment, then it is difficult to perceive why a search incident in the style of <i>Harris</i> and <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> is not <i>per se</i> reasonable as well.</p>
<p>It is clear, then, that the notion that the warrantless entry of a man's house in order to arrest him on probable cause is <i>per se</i> legitimate is in fundamental conflict with the basic principle of Fourth Amendment law that <span class="star-pagination">*478</span> searches and seizures inside a man's house without warrant are <i>per se</i> unreasonable in the absence of some one of a number of well defined "exigent circumstances." This conflict came to the fore in <i>Chimel</i> v. <i>California, supra</i><i>.</i></p>
<p>The Court there applied the basic rule that the "search incident to arrest" is an exception to the warrant requirement and that its scope must therefore be strictly defined in terms of the justifying "exigent circumstances." The exigency in question arises from the dangers of harm to the arresting officer and of destruction of evidence within the reach of the arrestee. Neither exigency can conceivably justify the far-ranging searches authorized under <i>Harris</i> and <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span>.</i> The answer of the dissenting opinion of MR. JUSTICE WHITE in <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>,</i> supported by no decision of this Court, was that a warrantless entry for the purpose of arrest on probable cause is legitimate and reasonable no matter what the circumstances. 395 U. S., at 776-780. From this it was said to follow that the full-scale search incident to arrest was also reasonable since it was a lesser intrusion. 395 U. S., at 772-775.</p>
<p>The same conflict arises in this case. Since the police knew of the presence of the automobile and planned all along to seize it, there was no "exigent circumstance" to justify their failure to obtain a warrant. The application of the basic rule of Fourth Amendment law therefore requires that the fruits of the warrantless seizure be suppressed. MR. JUSTICE WHITE's dissenting opinion, however, argues once again that so long as the police could reasonably make a warrantless nighttime entry onto Coolidge's property in order to arrest him, with no showing at all of an emergency, then it is absurd to prevent them from seizing his automobile as evidence of the crime.</p>
<p>MR. JUSTICE WHITE takes a basically similar approach to the question whether the search of the automobile in <span class="star-pagination">*479</span> this case can be justified under <i>Carroll</i> v. <i>United States, supra</i><i>,</i> and <i>Chambers</i> v. <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Maroney, supra</a></span></i><i>. Carroll,</i> on its face, appears to be a classic example of the doctrine that warrantless searches are <i>per se</i> unreasonable in the absence of exigent circumstances. Every word in the opinion indicates the Court's adherence to the underlying rule and its care in delineating a limited exception. Read thus, the case quite evidently does not extend to the situation at bar. Yet if we take the viewpoint of a judge called on only to decide in the abstract, after the fact, whether the police have behaved "reasonably" under all the circumstancesin short if we simply ignore the warrant requirement<span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States"><i>Carroll</i></a></span> comes to stand for something more. The stopping of a vehicle on the open highway and a subsequent search amount to a major interference in the lives of the occupants. <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> held such an interference to be reasonable without a warrant, given probable cause. It may be thought to follow <i>a fortiori</i> that the seizure and search herewhere there was no stopping and the vehicle was unoccupiedwere also reasonable, since the intrusion was less substantial, although there were no exigent circumstances whatever. Using reasoning of this sort, it is but a short step to the position that it is <i>never</i> necessary for the police to obtain a warrant before searching and seizing an automobile, provided that they have probable cause. And MR. JUSTICE WHITE appears to adopt exactly this view when he proposes that the Court should "treat searches of automobiles as we do the arrest of a person."</p>
<p>If we were to accept MR. JUSTICE WHITE'S view that warrantless entry for purposes of arrest and warrantless seizure and search of automobiles are <i>per se</i> reasonable, so long as the police have probable cause, it would be difficult to see the basis for distinguishing searches of houses and seizures of effects. If it is reasonable for the police to make a warrantless nighttime entry for the purpose <span class="star-pagination">*480</span> of arresting a person in his bed, then surely it must be reasonable as well to make a warrantless entry to search for and seize vital evidence of a serious crime. If the police may, without a warrant, seize and search an unoccupied vehicle parked on the owner's private property, not being used for any illegal purpose, then it is hard to see why they need a warrant to seize and search a suitcase, a trunk, a shopping bag, or any other portable container in a house, garage, or back yard.</p>
<p>The fundamental objection, then, to the line of argument adopted by MR. JUSTICE WHITE in his dissent in this case and in <i>Chimel</i> v. <i>California, supra</i><i>,</i> is that it proves too much. If we were to agree with MR. JUSTICE WHITE that the police may, whenever they have probable cause, make a warrantless entry for the purpose of making an arrest, and that seizures and searches of automobiles are likewise <i>per se</i> reasonable given probable cause, then by the same logic <i>any</i> search or seizure could be carried out without a warrant, and we would simply have read the Fourth Amendment out of the Constitution. Indeed, if MR. JUSTICE WHITE is correct that it has generally been assumed that the Fourth Amendment is not violated by the warrantless entry of a man's house for purposes of arrest, it might be wise to re-examine the assumption. Such a re-examination "would confront us with a grave constitutional question, namely, whether the forceful nighttime entry into a dwelling to arrest a person reasonably believed within, upon probable cause that he had committed a felony, under circumstances where no reason appears why an arrest warrant could not have been sought, is consistent with the Fourth Amendment." <i>Jones</i> v. <i>United States,</i> 357 U. S., at 499-500.</p>
<p>None of the cases cited by MR. JUSTICE WHITE disposes of this "grave constitutional question." The case of <i>Warden</i> v. <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden, supra</a></span></i><i>,</i> where the Court elaborated <span class="star-pagination">*481</span> a "hot pursuit" justification for the police entry into the defendant's house without a warrant for his arrest, certainly stands by negative implication for the proposition that an arrest warrant is required in the absence of exigent circumstances. See also <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#728" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 728</a></span>; <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#481" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 481-482</a></span>. The Court of Appeals for the District of Columbia Circuit, sitting <i>en banc,</i> has unanimously reached the same conclusion.<sup>[36]</sup> But we find it unnecessary to decide the question in this case. The rule that "searches conducted outside the judicial process, without prior approval by judge or magistrate, are <i>per se</i> unreasonable under the Fourth Amendmentsubject only to a few specifically established and well-delineated exceptions,"<sup>[37]</sup> is not so frail that its continuing vitality depends on the fate of a supposed doctrine of warrantless arrest. The warrant requirement has been a valued part of our constitutional law for decades, and it has determined the result in scores and scores of cases in courts all over this country. It is not an inconvenience to be somehow "weighed" against the claims of police efficiency. It is, or should be, an important working part of our machinery of government, operating as a matter of course to check the "well-intentioned but mistakenly over-zealous executive officers"<sup>[38]</sup> who are a part of any system of law enforcement. If it is to be a true guide to constitutional police action, rather than just a pious phrase, then "[t]he exceptions cannot be enthroned into the rule." <i>United States</i> v. <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#80" aria-description="Citation for case: United States v. Rabinowitz"><i>Rabinowitz, supra,</i> at 80</a></span> (Frankfurter, J., dissenting). The confinement of the exceptions to their appropriate scope was the function of <i>Chimel</i> v. <i>California, supra</i><i>,</i> where we dealt with the <span class="star-pagination">*482</span> assumption that a search "incident" to a lawful arrest may encompass all of the premises where the arrest occurs, however spacious. The "plain view" exception is intimately linked with the search-incident exception, as the cases discussed in Part C above have repeatedly shown. To permit warrantless plain-view seizures without limit would be to undo much of what was decided in <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>,</i> as the similar arguments put forward in dissent in the two cases indicate clearly enough.</p>
<p>Finally, a word about <i>Trupiano</i> v. <i>United States, supra</i><i>.</i> Our discussion of "plain view" in Part C above corresponds with that given in <i><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span>.</i> Here, as in <i><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span>,</i> the determining factors are advance police knowledge of the existence and location of the evidence, police intention to seize it, and the ample opportunity for obtaining a warrant. See <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S., at 707</a></span>-708 and n. 27, <i>supra.</i> However, we do not "reinstate" <i><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span>,</i> since we cannot adopt all its implications. To begin with, in <i>Chimel</i> v. <i>California, supra</i><i>,</i> we held that a search of the person of an arrestee and of the area under his immediate control could be carried out without a warrant. We did not indicate there, and do not suggest here, that the police must obtain a warrant if they anticipate that they will find specific evidence during the course of such a search. See n. 24, <i>supra.</i> And as to the automobile exception, we do not question the decisions of the Court in <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span>, and <i>Chambers</i> v. <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Maroney, supra</a></span></i><i>,</i> although both are arguably inconsistent with <i><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span>.</i></p>
<p>MR. JUSTICE WHITE'S dissent characterizes the coexistence of <i>Chimel, Cooper, Chambers,</i> and this case as "punitive," "extravagant," "inconsistent," "without apparent reason," "unexplained," and "inexplicable." <i>Post,</i> at 517, 519, 521. It is urged upon us that we have here a "ready opportunity, one way or another, <span class="star-pagination">*483</span> to bring clarity and certainty to a body of law that lower courts and law enforcement officials often find confusing." <i>Post,</i> at 521. Presumably one of the ways in which MR. JUSTICE WHITE believes we might achieve clarity and certainty would be the adoption of his proposal that we treat entry for purposes of arrest and seizure of an automobile alike as <i>per se</i> reasonable on probable cause. Such an approach might dispose of this case clearly and certainly enough, but, as we have tried to show above, it would cast into limbo the whole notion of a Fourth Amendment warrant requirement. And it is difficult to take seriously MR. JUSTICE WHITE'S alternative suggestion that clarity and certainty, as well as coherence and credibility, might also be achieved by modifying <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> and overruling <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span></i> and <i><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">Cooper</a></span>.</i> Surely, quite apart from his strong disagreement on the merits, he would take vehement exception to any such cavalier treatment of this Court's decisions.</p>
<p>Of course, it would be nonsense to pretend that our decision today reduces Fourth Amendment law to complete order and harmony. The decisions of the Court over the years point in differing directions and differ in emphasis. No trick of logic will make them all perfectly consistent. But it is no less nonsense to suggest, as does MR. JUSTICE WHITE, <i>post,</i> at 521, 520, that we cease today "to strive for clarity and consistency of analysis," or that we have "abandoned any attempt" to find reasoned distinctions in this area. The time is long past when men believed that development of the law must always proceed by the smooth incorporation of new situations into a single coherent analytical framework. We need accept neither the "clarity and certainty" of a Fourth Amendment without a warrant requirement nor the facile consistency obtained by wholesale overruling of recently decided cases. A remark by <span class="star-pagination">*484</span> MR. JUSTICE HARLAN concerning the Fifth Amendment is applicable as well to the Fourth:</p>
<blockquote>"There are those, I suppose, who would put the `liberal construction' approach of cases like <i>Miranda</i> [v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>,] and <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886), side-by-side with the balancing approach of <i>Schmerber</i> [v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span>,] and perceive nothing more subtle than a set of constructional antinomies to be utilized as convenient bootstraps to one result or another. But I perceive in these cases the essential tension that springs from the uncertain mandate which this provision of the Constitution gives to this Court." <i>California</i> v. <i>Byers,</i> <span class="citation" data-id="9424566"><a href="/opinion/108335/california-v-byers/#449" aria-description="Citation for case: California v. Byers">402 U. S. 424, 449-450</a></span> (concurring in judgment).</blockquote>
<p>We are convinced that the result reached in this case is correct, and that the principle it reflectsthat the police must obtain a warrant when they intend to seize an object outside the scope of a valid search incident to arrestcan be easily understood and applied by courts and law enforcement officers alike. It is a principle that should work to protect the citizen without overburdening the police, and a principle that preserves and protects the guarantees of the Fourth Amendment.</p>
<p></p>
<h2>III</h2>
<p>Because of the prospect of a new trial, the efficient administration of justice counsels consideration of the second substantial question under the Fourth and Fourteenth Amendments presented by this case. The petitioner contends that when the police obtained a rifle and articles of his clothing from his home on the night of Sunday, February 2, 1964, while he was being interrogated at the police station, they engaged in a search and seizure violative of the Constitution. In order to <span class="star-pagination">*485</span> understand this contention, it is necessary to review in some detail the circumstances of the February 2 episode.</p>
<p></p>
<h2>A</h2>
<p>The lie-detector test administered to Coolidge in Concord on the afternoon of the 2d was inconclusive as to his activities on the night of Pamela Mason's disappearance, but during the course of the test Coolidge confessed to stealing $375 from his employer. After the group returned from Concord to Manchester, the interrogation about Coolidge's movements on the night of the disappearance continued, and Coolidge apparently made a number of statements which the police immediately checked out as best they could. The decision to send two officers to the Coolidge house to speak with Mrs. Coolidge was apparently motivated in part by a desire to check his story against whatever she might say, and in part by the need for some corroboration of his admission to the theft from his employer. The trial judge found as a fact, and the record supports him, that at the time of the visit the police knew very little about the weapon that had killed Pamela Mason. The bullet that had been retrieved was of small caliber, but the police were unsure whether the weapon was a rifle or a pistol. During the extensive investigation following the discovery of the body, the police had made it a practice to ask all those questioned whether they owned any guns, and to ask the owners for permission to run tests on those that met the very general description of the murder weapon. The trial judge found as a fact that when the police visited Mrs. Coolidge on the night of the 2d, they were unaware of the previous visit during which Coolidge had shown other officers three guns, and that they were not motivated by a desire to find the murder weapon.</p>
<p><span class="star-pagination">*486</span> The two plainclothesmen asked Mrs. Coolidge whether her husband had been at home on the night of the murder victim's disappearance, and she replied that he had not. They then asked her if her husband owned any guns. According to her testimony at the pretrial suppression hearing, she replied, "Yes, I will get them in the bedroom." One of the officers replied, "We will come with you." The three went into the bedroom where Mrs. Coolidge took all four guns out of the closet. Her account continued:</p>
<blockquote>"A. I believe I asked if they wanted the guns. One gentleman said, `No'; then the other gentleman turned around and said, `We might as well take them.' I said, `If you would like them, you may take them.'</blockquote>
<blockquote>"Q. Did you go further and say, `We have nothing to hide.'?</blockquote>
<blockquote>"A. I can't recall if I said that then or before. I don't recall.</blockquote>
<blockquote>"Q. But at some time you indicated to them that as far as you were concerned you had nothing to hide, and they might take what they wanted?</blockquote>
<blockquote>"A. That was it.</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. Did you feel at that time that you had something to hide?</blockquote>
<blockquote>"A. No."</blockquote>
<p>The two policemen also asked Mrs. Coolidge what her husband had been wearing on the night of the disappearance. She then produced four pairs of trousers and indicated that her husband had probably worn either of two of them on that evening. She also brought out a hunting jacket. The police gave her a receipt for the guns and the clothing, and, after a search of the Coolidge cars not here in issue, took the various articles to the police station.</p>
<p></p>
<h2>
<span class="star-pagination">*487</span> B</h2>
<p>The first branch of the petitioner's argument is that when Mrs. Coolidge brought out the guns and clothing, and then handed them over to the police, she was acting as an "instrument" of the officials, complying with a "demand" made by them. Consequently, it is argued, Coolidge was the victim of a search and seizure within the constitutional meaning of those terms. Since we cannot accept this interpretation of the facts, we need not consider the petitioner's further argument that Mrs. Coolidge could not or did not "waive" her husband's constitutional protection against unreasonable searches and seizures.</p>
<p>Had Mrs. Coolidge, wholly on her own initiative, sought out her husband's guns and clothing and then taken them to the police station to be used as evidence against him, there can be no doubt under existing law that the articles would later have been admissible in evidence. Cf. <i>Burdeau</i> v. <i>McDowell,</i> <span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465</a></span>. The question presented here is whether the conduct of the police officers at the Coolidge house was such as to make her actions their actions for purposes of the Fourth and Fourteenth Amendments and their attendant exclusionary rules. The test, as the petitioner's argument suggests, is whether Mrs. Coolidge, in light of all the circumstances of the case, must be regarded as having acted as an "instrument" or agent of the state when she produced her husband's belongings. Cf. <i>United States</i> v. <i>Goldberg,</i> <span class="citation" data-id="263859"><a href="/opinion/263859/united-states-v-morris-c-goldberg-also-known-as-moe-goldberg-and-m-c/" aria-description="Citation for case: United States v. Morris C. Goldberg, Also Known as Moe...">330 F. 2d 30</a></span> (CA3), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./377/953/">377 U. S. 953</a></span> (1964); <i>People</i> v. <i>Tarantino,</i> <span class="citation" data-id="9536654"><a href="/opinion/1139971/people-v-tarantino/" aria-description="Citation for case: People v. Tarantino">45 Cal. 2d 590</a></span>, <span class="citation" data-id="9536654"><a href="/opinion/1139971/people-v-tarantino/" aria-description="Citation for case: People v. Tarantino">290 P. 2d 505</a></span> (1955); see <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U. S. 28</a></span>; <i>Gambino</i> v. <i>United States,</i> <span class="citation" data-id="101180"><a href="/opinion/101180/gambino-v-united-states/" aria-description="Citation for case: Gambino v. United States">275 U. S. 310</a></span>.</p>
<p>In a situation like the one before us there no doubt always exist forces pushing the spouse to cooperate with <span class="star-pagination">*488</span> the police. Among these are the simple but often powerful convention of openness and honesty, the fear that secretive behavior will intensify suspicion, and uncertainty as to what course is most likely to be helpful to the absent spouse. But there is nothing constitutionally suspect in the existence, without more, of these incentives to full disclosure or active cooperation with the police. The exclusionary rules were fashioned "to prevent, not to repair," and their target is official misconduct. They are "to compel respect for the constitutional guaranty in the only effectively available wayby removing the incentive to disregard it." <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#217" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 217</a></span>. But it is no part of the policy underlying the Fourth and Fourteenth Amendments to discourage citizens from aiding to the utmost of their ability in the apprehension of criminals. If, then, the exclusionary rule is properly applicable to the evidence taken from the Coolidge house on the night of February 2, it must be upon the basis that some type of unconstitutional police conduct occurred.</p>
<p>Yet it cannot be said that the police should have obtained a warrant for the guns and clothing before they set out to visit Mrs. Coolidge, since they had no intention of rummaging around among Coolidge's effects or of dispossessing him of any of his property. Nor can it be said that they should have obtained Coolidge's permission for a seizure they did not intend to make. There was nothing to compel them to announce to the suspect that they intended to question his wife about his movements on the night of the disappearance or about the theft from his employer. Once Mrs. Coolidge had admitted them, the policemen were surely acting normally and properly when they asked her, as they had asked those questioned earlier in the investigation, including Coolidge himself, about any guns there might be in the house. The question <span class="star-pagination">*489</span> concerning the clothes Coolidge had been wearing on the night of the disappearance was logical and in no way coercive. Indeed, one might doubt the competence of the officers involved had they not asked exactly the questions they did ask. And surely when Mrs. Coolidge of her own accord produced the guns and clothes for inspection, rather than simply describing them, it was not incumbent on the police to stop her or avert their eyes.</p>
<p>The crux of the petitioner's argument must be that when Mrs. Coolidge asked the policemen whether they wanted the guns, they should have replied that they could not take them, or have first telephoned Coolidge at the police station and asked his permission to take them, or have asked her whether she had been authorized by her husband to release them. Instead, after one policeman had declined the offer, the other turned and said, "We might as well take them," to which Mrs. Coolidge replied, "If you would like them, you may take them."</p>
<p>In assessing the claim that this course of conduct amounted to a search and seizure, it is well to keep in mind that Mrs. Coolidge described her own motive as that of clearing her husband, and that she believed that she had nothing to hide. She had seen her husband himself produce his guns for two other policemen earlier in the week, and there is nothing to indicate that she realized that he had offered only three of them for inspection on that occasion. The two officers who questioned her behaved, as her own testimony shows, with perfect courtesy. There is not the slightest implication of an attempt on their part to coerce or dominate her, or, for that matter, to direct her actions by the more subtle techniques of suggestion that are available to officials in circumstances like these. To hold that the conduct of the police here was a search and seizure would be to hold, in effect, that a criminal suspect has constitutional protection against <span class="star-pagination">*490</span> the adverse consequences of a spontaneous, good-faith effort by his wife to clear him of suspicion.<sup>[39]</sup></p>
<p>The judgment is reversed and the case is remanded to the Supreme Court of New Hampshire for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE HARLAN, concurring.</p>
<p>From the several opinions that have been filed in this case it is apparent that the law of search and seizure is due for an overhauling. State and federal law enforcement officers and prosecutorial authorities must find quite intolerable the present state of uncertainty, which extends even to such an everyday question as the circumstances under which police may enter a man's property to arrest him and seize a vehicle believed to have been used during the commission of a crime.</p>
<p>I would begin this process of re-evaluation by overruling <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), and <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963). The former of these cases made the federal "exclusionary rule" applicable to the States. The latter forced the States to follow all the ins and outs of this Court's Fourth Amendment decisions, handed down in federal cases.</p>
<p>In combination <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> and <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ker</a></span></i> have been primarily responsible for bringing about serious distortions and incongruities in this field of constitutional law. Basically these have had two aspects, as I believe an examination of our more recent opinions and certiorari docket will show. First, the States have been put in a federal mold with respect to this aspect of criminal law enforcement, thus depriving the country of the opportunity to observe <span class="star-pagination">*491</span> the effects of different procedures in similar settings. See, <i>e. g.,</i> Oaks, Studying the Exclusionary Rule in Search and Seizure, <span class="citation no-link">37 U. Chi. L. Rev. 665</span> (1970), suggesting that the assumed "deterrent value" of the exclusionary rule has never been adequately demonstrated or disproved, and pointing out that because of <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> all comparative statistics are 10 years old and no new ones can be obtained. Second, in order to leave some room for the States to cope with their own diverse problems, there has been generated a tendency to relax federal requirements under the Fourth Amendment, which now govern state procedures as well. For an illustration of that tendency in another constitutional field, again resulting from the infelicitous "incorporation" doctrine, see <i>Williams</i> v. <i>Florida,</i> <span class="citation" data-id="9424326"><a href="/opinion/108186/williams-v-florida/" aria-description="Citation for case: Williams v. Florida">399 U. S. 78</a></span> (1970). Until we face up to the basic constitutional mistakes of <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> and <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ker</a></span>,</i> no solid progress in setting things straight in search and seizure law will, in my opinion, occur.</p>
<p>But for <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> and <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ker</a></span>,</i> I would have little difficulty in voting to sustain this conviction, for I do not think that anything the State did in this case could be said to offend those values which are "at the core of the Fourth Amendment." <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span> (1949); cf. <i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">347 U. S. 128</a></span> (1954); <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952).</p>
<p>Because of <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> and <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ker</a></span>,</i> however, this case must be judged in terms of federal standards, and on that basis I concur, although not without difficulty, in Parts I, II-D, and III of the Court's opinion and in the judgment of the Court.<sup>[*]</sup> It must be recognized that the case is a close one. The reason I am tipped in favor of MR. JUSTICE <span class="star-pagination">*492</span> STEWART'S position is that a contrary result in this case would, I fear, go far toward relegating the warrant requirement of the Fourth Amendment to a position of little consequence in federal search and seizure law, a course which seems to me opposite to the one we took in <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), two Terms ago.</p>
<p>Recent scholarship has suggested that in emphasizing the warrant requirement over the reasonableness of the search the Court has "stood the fourth amendment on its head" from a historical standpoint. T. Taylor, Two Studies in Constitutional Interpretation 23-24 (1969). This issue is perhaps most clearly presented in the case of a warrantless entry into a man's home to arrest him on probable cause. The validity of such entry was left open in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499-500</a></span> (1958), and although my Brothers WHITE and STEWART both feel that their contrary assumptions on this point are at the root of their disagreement in this case, <i>ante,</i> at 477-479; <i>post,</i> at 510-512, 521, the Court again leaves the issue open. <i>Ante,</i> at 481. In my opinion it does well to do so. This matter should not be decided in a state case not squarely presenting the issue and where it was not fully briefed and argued. I intimate no view on this subject, but until it is ripe for decision, I hope in a federal case, I am unwilling to lend my support to setting back the trend of our recent decisions.</p>
<p>MR. CHIEF JUSTICE BURGER, dissenting in part and concurring in part.</p>
<p>I join the dissenting opinion of MR. JUSTICE WHITE and in Parts II and III of MR. JUSTICE BLACK'S concurring and dissenting opinion. I also agree with most of what is said in Part I of MR. JUSTICE BLACK'S opinion, but I am not prepared to accept the proposition that the Fifth Amendment requires the exclusion of evidence <span class="star-pagination">*493</span> seized in violation of the Fourth Amendment. I join in Part III of MR. JUSTICE STEWART'S opinion.</p>
<p>This case illustrates graphically the monstrous price we pay for the exclusionary rule in which we seem to have imprisoned ourselves. See my dissent in <i>Bivens</i> v. <i>Six Unknown Named Agents of Federal Bureau of Narcotics, ante,</i> p. 411.</p>
<p>On the merits of the case I find not the slightest basis in the record to reverse this conviction. Here again the Court reaches out, strains, and distorts rules that were showing some signs of stabilizing, and directs a new trial which will be held more than seven years after the criminal acts charged.</p>
<p>Mr. Justice Stone, of the Minnesota Supreme Court, called the kind of judicial functioning in which the Court indulges today "bifurcating elements too infinitesimal to be split."</p>
<p>MR. JUSTICE BLACK, concurring and dissenting.</p>
<p>After a jury trial in a New Hampshire state court, petitioner was convicted of murder and sentenced to life imprisonment. Holding that certain evidence introduced by the State was seized during an "unreasonable" search and that the evidence was inadmissible under the judicially created exclusionary rule of the Fourth Amendment, the majority reverses that conviction. Believing that the search and seizure here was reasonable and that the Fourth Amendment properly construed contains no such exclusionary rule, I dissent.</p>
<p>The relevant facts are these. Pamela Mason, a 14-year-old school girl, lived with her mother and younger brother in Manchester, New Hampshire. She occasionally worked after school as a babysitter and sought such work by posting a notice on a bulletin board in a local laundromat. On January 13, 1964, she arrived home from school about 4:15 p. m. Pamela's mother told her <span class="star-pagination">*494</span> that a man had called seeking a babysitter for that evening and said that he would call again later. About 4:30 p. m., after Pamela's mother had left for her job as a waitress at a nearby restaurant, Pamela received a phone call. Her younger brother, who answered the call but did not overhear the conversation, later reported that the caller was a man. After the call, Pamela prepared dinner for her brother and herself, then left the house about 6 p. m. Her family never again saw her alive. Eight days later, on January 21, 1964, Pamela's frozen body was discovered in a snowdrift beside an interstate highway a few miles from her home. Her throat had been slashed and she had been shot in the head. Medical evidence showed that she died some time between 8 and 10 p. m. on January 13, the night she left home.</p>
<p>A manhunt ensued. Two witnesses informed the police that about 9:30 p. m. on the night of the murder they had stopped to offer assistance to a man in a 1951 Pontiac automobile which was parked beside the interstate highway near the point where the little girl's dead body was later found. Petitioner came under suspicion seven days after the body was discovered when one of his neighbors reported to the police that petitioner had been absent from his home between 5 and 11 p. m. on January 13, the night of the murder. Petitioner owned a 1951 Pontiac automobile that matched the description of the car which the two witnesses reported seeing parked where the girl's body had been found. The police first talked with petitioner at his home on the evening of January 28, fifteen days after the girl was killed, and arranged for him to come to the police station the following Sunday, February 2, 1964. He went to the station that Sunday and answered questions concerning his activities on the night of the murder, telling the police that he had been shopping in a neighboring town at the <span class="star-pagination">*495</span> time the murder was committed. During questioning, petitioner confessed to having committed an unrelated larceny from his employer and was held overnight at the police station in connection with that offense. On the next day, he was permitted to go home.</p>
<p>While petitioner was being questioned at the police station on February 2, two policemen went to petitioner's home to talk with his wife. They asked what firearms the petitioner owned and his wife produced two shotguns and two rifles which she voluntarily offered to the police. Upon examination the University of Rhode Island Criminal Investigation Laboratory concluded that one of the firearms, a Mossberg .22-caliber rifle, had fired the bullet found in the murdered girl's brain.</p>
<p>Petitioner admitted that he was a frequent visitor to the laundromat where Pamela posted her babysitting notice and that he had been there on the night of the murder. The following day a knife belonging to petitioner, which could have inflicted the murdered girl's knife wounds, was found near that laundromat. The police also learned that petitioner had unsuccessfully contacted four different persons before the girl's body had been discovered in an attempt to fabricate an alibi for the night of January 13.</p>
<p>On February 19, 1964, all this evidence was presented to the state attorney general who was authorized under New Hampshire law to issue arrest and search warrants. The attorney general considered the evidence and issued a warrant for petitioner's arrest and four search warrants including a warrant for the seizure and search of petitioner's Pontiac automobile.</p>
<p>On the day the warrants issued, the police went to the petitioner's residence and placed him under arrest. They took charge of his 1951 Pontiac which was parked in plain view in the driveway in front of the house, and, two hours later, towed the car to the police station. <span class="star-pagination">*496</span> During the search of the automobile at the station, the police obtained vacuum sweepings of dirt and other fine particles which matched like sweepings taken from the clothes of the murdered girl. Based on the similarity between the sweepings taken from petitioner's automobile and those taken from the girl's clothes, experts who testified at trial concluded that Pamela had been in the petitioner's car. The rifle given to the police by petitioner's wife was also received in evidence.</p>
<p>Petitioner challenges his conviction on the ground that the rifle obtained from his wife and the vacuum sweepings taken from his car were seized in violation of the Fourth Amendment and were improperly admitted at trial. With respect to the rifle voluntarily given to the police by petitioner's wife, the majority holds that it was properly received in evidence. I agree. But the Court reverses petitioner's conviction on the ground that the sweepings taken from his car were seized during an illegal search and for this reason the admission of the sweepings into evidence violated the Fourth Amendment. I dissent.</p>
<p></p>
<h2>I</h2>
<p>The Fourth Amendment prohibits unreasonable searches and seizures. The Amendment says nothing about consequences. It certainly nowhere provides for the exclusion of evidence as the remedy for violation. The Amendment states: "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." No examination of that text can find an exclusionary rule by a mere process of construction. Apparently the first suggestion that the Fourth Amendment somehow embodied a rule of evidence came <span class="star-pagination">*497</span> in Justice Bradley's majority opinion in <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886). The holding in that case was that ordinarily a person may not be compelled to produce his private books and papers for use against him as proof of crime. That decision was a sound application of accepted principles of common law and the command of the Fifth Amendment that no person shall be compelled to be a witness against himself. But Justice Bradley apparently preferred to formulate a new exclusionary rule from the Fourth Amendment rather than rely on the already existing exclusionary rule contained in the language of the Fifth Amendment. His opinion indicated that compulsory production of such evidence at trial violated the Fourth Amendment. Mr. Justice Miller, with whom Chief Justice Waite joined, concurred solely on the basis of the Fifth Amendment, and explicitly refused to go along with Justice Bradley's novel reading of the Fourth Amendment. It was not until 1914, some 28 years after <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> and when no member of the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> Court remained, that the Court in <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, stated that the Fourth Amendment itself barred the admission of evidence seized in violation of the Fourth Amendment. The <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> opinion made no express confession of a break with the past. But if it was merely a proper reading of the Fourth Amendment, it seems strange that it took this Court nearly 125 years to discover the true meaning of those words. The truth is that the source of the exclusionary rule simply cannot be found in the Fourth Amendment. That Amendment did not when adopted, and does not now, contain any constitutional rule barring the admission of illegally seized evidence.</p>
<p>In striking contrast to the Fourth Amendment, the Fifth Amendment states in express, unambiguous terms that no person "shall be compelled in any criminal case <span class="star-pagination">*498</span> to be a witness against himself." The Fifth Amendment in and of itself directly and explicitly commands its own exclusionary rulea defendant cannot be compelled to give evidence against himself. Absent congressional action taken pursuant to the Fourth Amendment, if evidence is to be excluded, it must be under the Fifth Amendment, not the Fourth. That was the point so ably made in the concurring opinion of Justice Miller, joined by Chief Justice Waite, in <i>Boyd</i> v. <i>United States, supra</i><i>,</i> and that was the thrust of my concurring opinion in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#661" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 661</a></span> (1961).</p>
<p>The evidence seized by breaking into Mrs. Mapp's house and the search of all her possessions, was excluded from evidence, not by the Fourth Amendment which contains no exclusionary rule, but by the Fifth Amendment which does. The introduction of such evidence compels a man to be a witness against himself, and evidence so compelled must be excluded under the Fifth Amendment, not because the Court says so, but because the Fifth Amendment commands it.</p>
<p>The Fourth Amendment provides a constitutional means by which the Government can act to obtain evidence to be used in criminal prosecutions. The people are obliged to yield to a proper exercise of authority under that Amendment.<sup>[1]</sup> Evidence properly seized under the Fourth Amendment, of course, is admissible at trial. But nothing in the Fourth Amendment provides that evidence seized in violation of that Amendment must be excluded.</p>
<p>The majority holds that evidence it views as improperly seized in violation of its ever changing concept of the Fourth Amendment is inadmissible. The majority <span class="star-pagination">*499</span> treats the exclusionary rule as a judge-made rule of evidence designed and utilized to enforce the majority's own notions of proper police conduct. The Court today announces its new rules of police procedure in the name of the Fourth Amendment, then holds that evidence seized in violation of the new "guidelines" is automatically inadmissible at trial. The majority does not purport to rely on the Fifth Amendment to exclude the evidence in this case. Indeed, it could not. The majority prefers instead to rely on "changing times" and the Court's role as it sees it, as the administrator in charge of regulating the contacts of officials with citizens. The majority states that in the absence of a better means of regulation, it applies a court-created rule of evidence.</p>
<p>I readily concede that there is much recent precedent for the majority's present announcement of yet another new set of police operating procedures. By invoking this rulemaking power found not in the words but somewhere in the "spirit" of the Fourth Amendment, the Court has expanded that Amendment beyond recognition. And each new step is justified as merely a logical extension of the step before.</p>
<p>It is difficult for me to believe the Framers of the Bill of Rights intended that the police be required to prove a defendant's guilt in a "little trial" before the issuance of a search warrant. But see <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964); <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969). No such proceeding was required before or after the adoption of the Fourth Amendment, until this Court decided <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> and <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>.</i> Likewise, eavesdroppers were deemed to be competent witnesses in both English and American courts up until this Court in its Fourth Amendment "rulemaking" capacity undertook to lay down rules for electronic surveillance. <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#70" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 70</a></span> (1967) (BLACK, J., dissenting); <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#364" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 364</a></span> (1967) (BLACK, J., dissenting). <span class="star-pagination">*500</span> The reasonableness of a search incident to an arrest, extending to areas under the control of the defendant and areas where evidence may be found, was an established tenet of English common law, and American constitutional law after adoption of the Fourth Amendment that is, until <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969). The broad, abstract, and ambiguous concept of "privacy" is now unjustifiably urged as a comprehensive substitute for the Fourth Amendment's guarantee against "unreasonable searches and seizures." <i>Griswold</i> v. <i>Connecticut,</i> <span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/" aria-description="Citation for case: Griswold v. Connecticut">381 U. S. 479</a></span> (1965).</p>
<p>Our Government is founded upon a written Constitution. The draftsmen expressed themselves in careful and measured terms corresponding with the immense importance of the powers delegated to them. The Framers of the Constitution, and the people who adopted it, must be understood to have used words in their natural meaning, and to have intended what they said. The Constitution itself contains the standards by which the seizure of evidence challenged in the present case and the admissibility of that evidence at trial is to be measured in the absence of congressional legislation. It is my conclusion that both the seizure of the rifle offered by petitioner's wife and the seizure of the automobile at the time of petitioner's arrest were consistent with the Fourth Amendment and that the evidence so obtained under the circumstances shown in the record in this case could not be excluded under the Fifth Amendment.</p>
<p></p>
<h2>II</h2>
<p>The majority holds that the warrant authorizing the seizure and search of petitioner's automobile was constitutionally defective and void. With respect to search warrants, the Fourth Amendment provides that "no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place <span class="star-pagination">*501</span> to be searched, and the persons or things to be seized." The majority concedes that the police did show probable cause for the issuance of the warrant. The majority does not contest that the warrant particularly described the place to be searched, and the thing to be seized.</p>
<p>But compliance with state law and the requirements of the Fourth Amendment apparently is not enough. The majority holds that the state attorney general's connection with the investigation automatically rendered the search warrant invalid. In the first place, there is no language in the Fourth Amendment which provides any basis for the disqualification of the state attorney general to act as a magistrate. He is a state official of high office. The Fourth Amendment does not indicate that his position of authority over state law enforcement renders him ineligible to issue warrants upon a showing of probable cause supported by oath or affirmation. The majority's argument proceeds on the "little trial" theory that the magistrate is to sit as a judge and weigh the evidence and practically determine guilt or innocence before issuing a warrant. There is nothing in the Fourth Amendment to support such a magnified view of the magistrate's authority. The state attorney general was not barred by the Fourth Amendment or any other constitutional provision from issuing the warrant.</p>
<p>In the second place, the New Hampshire Supreme Court held in effect that the state attorney general's participation in the investigation of the case at the time he issued the search warrant was "harmless error" if it was error at all. I agree. It is difficult to imagine a clearer showing of probable cause. There was no possibility of prejudice because there was no room for discretion. Indeed, it could be said that a refusal to issue a warrant on the showing of probable cause made in this case would have been an abuse of discretion. In light <span class="star-pagination">*502</span> of the showing made by the police, there is no reasonable possibility that the state attorney general's own knowledge of the investigation contributed to the issuance of the warrant. I see no error in the state attorney general's action. But even if there was error, it was harmless beyond reasonable doubt. See <i>Harrington</i> v. <i>California,</i> <span class="citation" data-id="9424056"><a href="/opinion/107952/harrington-v-california/" aria-description="Citation for case: Harrington v. California">395 U. S. 250</a></span> (1969); <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967).</p>
<p>Therefore, it is my conclusion that the warrant authorizing the seizure and search of petitioner's automobile was constitutional under the Fourth Amendment, and that the evidence obtained during that search cannot be excluded under the Fifth Amendment. Moreover, I am of the view that, even if the search warrant had not issued, the search in this case nonetheless would have been constitutional under all three of the principles considered and rejected by the majority.</p>
<p></p>
<h2>III</h2>
<p>It is impo

[...TRUNCATED 112441 of 232441 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Elkins v. United States.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Elkins v. United States"
type: case
citation: "364 U.S. 206 (1960)"
parallel_cite: "80 S. Ct. 1437; 4 L. Ed. 2d 1669"
neutral_cite: 1960 U.S. LEXIS 1989
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1960
date_decided: 1960-06-27
docket: 126
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1960-06-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Elkins v. United States
  varies_by_point: false
  scope_note: "Good law. Decided the term before Mapp v. Ohio, which extended the exclusionary rule to the states and largely mooted the silver-platter problem; Elkins's deterrence rationale for the exclusionary rule remains foundational and is widely cited."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106107/elkins-v-united-states/"
  cluster_id: 106107
  opinion_id: 9422064
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Anchor (silver-platter abolition; deterrence rationale)"
related: ["[[Weeks v. United States]]", "[[Mapp v. Ohio]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "silver-platter", "deterrence", "federalism"]
holding: "The 'silver-platter' doctrine is abolished: evidence obtained by state officers in a search that would violate the Fourth Amendment if conducted by federal officers is inadmissible in a federal criminal trial, because the exclusionary rule's purpose is to deter unconstitutional searches by removing the incentive to make them."
lake:
  record_id: Elkins v. United States
  status: verified
  projected_at: 2026-07-06
---

# Elkins v. United States

*364 U.S. 206 (1960)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
State officers searched Elkins and seized evidence that a federal court had found was obtained unlawfully; the state prosecution was dropped. Federal officers then obtained the items and Elkins was prosecuted federally. Under the then-prevailing "silver-platter" doctrine, evidence unconstitutionally seized by *state* officers (without federal participation) could still be handed to federal prosecutors and used in federal court. Elkins objected to its admission.

## Issue
Whether evidence obtained through an unreasonable search and seizure by state officers, without federal involvement, may be admitted against a defendant in a federal criminal trial.

## Rule
No. The silver-platter doctrine is abolished. "[W]e re-examine here the validity of what has come to be called the silver platter doctrine. … [W]e conclude that this doctrine can no longer be accepted." — 364 U.S. at 208. ^pin-208

The exclusionary rule rests on deterrence: "The rule is calculated to prevent, not to repair. Its purpose is to deter — to compel respect for the constitutional guaranty in the only effectively available way — by removing the incentive to disregard it." — *Id.* at 217. ^pin-217

"[W]e hold that evidence obtained by state officers during a search which, if conducted by federal officers, would have violated the defendant's immunity from unreasonable searches and seizures under the Fourth Amendment is inadmissible over the defendant's timely objection in a federal criminal trial." — *Id.* at 223. ^pin-223

## Application
Because the items used against Elkins had been seized by state officers in a manner that would have violated the Fourth Amendment had federal officers done it, they could not be admitted in his federal prosecution. The Court added that a federal court must make an independent inquiry into the lawfulness of the state seizure under federal standards, regardless of any state-court ruling.

## Conclusion
The silver-platter doctrine was rejected; the unconstitutionally state-seized evidence was inadmissible in federal court, and the judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Elkins* was decided the term before *[[Mapp v. Ohio]]* (1961), which made the exclusionary rule binding on the states and so largely mooted the silver-platter problem. *Elkins*'s articulation of the exclusionary rule's **deterrence purpose** remains foundational and is repeatedly invoked in later good-faith and cost-benefit cases.

## Appears on
- [[The Exclusionary Rule]] — *Anchor (silver-platter abolition; deterrence rationale)*

## Sources
- *Elkins v. United States*, 364 U.S. 206 (1960) — https://www.courtlistener.com/opinion/106107/elkins-v-united-states/ — pinpoints: 208, 217, 223.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "467615dec7d381aa", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Elkins v. United States"}, "payload": {"all": [{"cite": "364 U.S. 206", "page": "206", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "364"}, {"cite": "80 S. Ct. 1437", "page": "1437", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "80"}, {"cite": "4 L. Ed. 2d 1669", "page": "1669", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "4"}, {"cite": "1960 U.S. LEXIS 1989", "page": "1989", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1960"}], "display": "364 U.S. 206", "official": {"cite": "364 U.S. 206", "page": "206", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "364"}, "official_selection_present": true, "record_id": "Elkins v. United States"}}
{"assertion_id": "261022b40c7717bd", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-208", "record_id": "Elkins v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-208", "pinpoint_status": "slip-only", "quote": "doctrine, evidence unconstitutionally seized by *state* officers (without federal participation) could still be handed to federal prosecutors and used in federal court. Elkins objected to its admission. ## Issue Whether evidence obtained through an unreasonable search and seizure by state officers, without federal involvement, may be admitted against a defendant in a federal criminal trial. ## Rule No. The silver-platter doctrine is abolished.", "quote_fidelity": "mismatch", "record_id": "Elkins v. United States", "star_marker": null}}
{"assertion_id": "88ff90da02d7f531", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-217", "record_id": "Elkins v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-217", "pinpoint_status": "slip-only", "quote": "The rule is calculated to prevent, not to repair. Its purpose is to deter — to compel respect for the constitutional guaranty in the only effectively available way — by removing the incentive to disregard it.", "quote_fidelity": "mismatch", "record_id": "Elkins v. United States", "star_marker": null}}
{"assertion_id": "df7b82ff9f3930b0", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-223", "record_id": "Elkins v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-223", "pinpoint_status": "slip-only", "quote": "[W]e hold that evidence obtained by state officers during a search which, if conducted by federal officers, would have violated the defendant's immunity from unreasonable searches and seizures under the Fourth Amendment is inadmissible over the defendant's timely objection in a federal criminal trial.", "quote_fidelity": "mismatch", "record_id": "Elkins v. United States", "star_marker": null}}
{"assertion_id": "8941cd0ae6194019", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Elkins v. United States"}, "payload": {"as_of_content": "1960-06-27", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Elkins v. United States", "scope_note": "Good law. Decided the term before Mapp v. Ohio, which extended the exclusionary rule to the states and largely mooted the silver-platter problem; Elkins's deterrence rationale for the exclusionary rule remains foundational and is widely cited.", "varies_by_point": false}}
```

### lake record — Elkins v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Elkins v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Elkins v. United States",
    "case_name_short": "Elkins",
    "case_name_full": "ELKINS Et Al. v. UNITED STATES",
    "input_case_name": "Elkins v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1960-06-27",
    "year": 1960,
    "docket": "126",
    "cluster_id": 106107,
    "lead_opinion_id": 9422064,
    "sibling_ids": [
      106107,
      9422064,
      9422065
    ],
    "absolute_url": "/opinion/106107/elkins-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "364 U.S. 206",
      "volume": "364",
      "reporter": "U.S.",
      "page": "206",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "80 S. Ct. 1437",
        "volume": "80",
        "reporter": "S. Ct.",
        "page": "1437",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 L. Ed. 2d 1669",
        "volume": "4",
        "reporter": "L. Ed. 2d",
        "page": "1669",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1960 U.S. LEXIS 1989",
        "volume": "1960",
        "reporter": "U.S. LEXIS",
        "page": "1989",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "364 U.S. 206",
        "volume": "364",
        "reporter": "U.S.",
        "page": "206",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 S. Ct. 1437",
        "volume": "80",
        "reporter": "S. Ct.",
        "page": "1437",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 L. Ed. 2d 1669",
        "volume": "4",
        "reporter": "L. Ed. 2d",
        "page": "1669",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1960 U.S. LEXIS 1989",
        "volume": "1960",
        "reporter": "U.S. LEXIS",
        "page": "1989",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "364 U.S. 206",
    "official_selection": {
      "court_class": "scotus",
      "selected": "364 U.S. 206",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-208",
      "page": null,
      "quote": "doctrine, evidence unconstitutionally seized by *state* officers (without federal participation) could still be handed to federal prosecutors and used in federal court. Elkins objected to its admission. ## Issue Whether evidence obtained through an unreasonable search and seizure by state officers, without federal involvement, may be admitted against a defendant in a federal criminal trial. ## Rule No. The silver-platter doctrine is abolished.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-217",
      "page": null,
      "quote": "The rule is calculated to prevent, not to repair. Its purpose is to deter \u2014 to compel respect for the constitutional guaranty in the only effectively available way \u2014 by removing the incentive to disregard it.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-223",
      "page": null,
      "quote": "[W]e hold that evidence obtained by state officers during a search which, if conducted by federal officers, would have violated the defendant's immunity from unreasonable searches and seizures under the Fourth Amendment is inadmissible over the defendant's timely objection in a federal criminal trial.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1960-06-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Elkins v. United States",
    "varies_by_point": false,
    "scope_note": "Good law. Decided the term before Mapp v. Ohio, which extended the exclusionary rule to the states and largely mooted the silver-platter problem; Elkins's deterrence rationale for the exclusionary rule remains foundational and is widely cited.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Elkins v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Turner v. United States",
          "cluster_id": 4480399,
          "cite": [
            "885 F.3d 949"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Allen",
          "cluster_id": 4409967,
          "cite": [
            "864 F.3d 63",
            "2017 U.S. App. LEXIS 12942",
            "2017 WL 3040201"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Long",
          "cluster_id": 4371038,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Terry v. Ohio",
          "cluster_id": 107729,
          "cite": [
            "20 L. Ed. 2d 889",
            "88 S. Ct. 1868",
            "392 U.S. 1",
            "1968 U.S. LEXIS 1345",
            "44 Ohio Op. 2d 383"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wong Sun v. United States",
          "cluster_id": 106515,
          "cite": [
            "9 L. Ed. 2d 441",
            "83 S. Ct. 407",
            "371 U.S. 471",
            "1963 U.S. LEXIS 2431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gideon v. Wainwright",
          "cluster_id": 106545,
          "cite": [
            "9 L. Ed. 2d 799",
            "83 S. Ct. 792",
            "372 U.S. 335",
            "1963 U.S. LEXIS 1942",
            "93 A.L.R. 2d 733",
            "23 Ohio Op. 2d 258"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chimel v. California",
          "cluster_id": 107979,
          "cite": [
            "23 L. Ed. 2d 685",
            "89 S. Ct. 2034",
            "395 U.S. 752",
            "1969 U.S. LEXIS 1166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Monroe v. Pape",
          "cluster_id": 106170,
          "cite": [
            "5 L. Ed. 2d 492",
            "81 S. Ct. 473",
            "365 U.S. 167",
            "1961 U.S. LEXIS 1687"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nixon",
          "cluster_id": 109101,
          "cite": [
            "41 L. Ed. 2d 1039",
            "94 S. Ct. 3090",
            "418 U.S. 683",
            "1974 U.S. LEXIS 93"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malloy v. Hogan",
          "cluster_id": 106862,
          "cite": [
            "12 L. Ed. 2d 653",
            "84 S. Ct. 1489",
            "378 U.S. 1",
            "1964 U.S. LEXIS 993"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Calandra",
          "cluster_id": 108898,
          "cite": [
            "38 L. Ed. 2d 561",
            "94 S. Ct. 613",
            "414 U.S. 338",
            "1974 U.S. LEXIS 145",
            "66 Ohio Op. 2d 320"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ker v. California",
          "cluster_id": 106641,
          "cite": [
            "10 L. Ed. 2d 726",
            "83 S. Ct. 1623",
            "374 U.S. 23",
            "1963 U.S. LEXIS 2473",
            "24 Ohio Op. 2d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Linkletter v. Walker",
          "cluster_id": 107084,
          "cite": [
            "14 L. Ed. 2d 601",
            "85 S. Ct. 1731",
            "381 U.S. 618",
            "1965 U.S. LEXIS 2283",
            "5 Ohio Misc. 49",
            "33 Ohio Op. 2d 118"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alderman v. United States",
          "cluster_id": 107872,
          "cite": [
            "22 L. Ed. 2d 176",
            "89 S. Ct. 961",
            "394 U.S. 165",
            "1969 U.S. LEXIS 3287"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richmond Newspapers, Inc. v. Virginia",
          "cluster_id": 110339,
          "cite": [
            "65 L. Ed. 2d 973",
            "100 S. Ct. 2814",
            "448 U.S. 555",
            "1980 U.S. LEXIS 18",
            "6 Media L. Rep. (BNA) 1833"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Preston v. United States",
          "cluster_id": 106771,
          "cite": [
            "11 L. Ed. 2d 777",
            "84 S. Ct. 881",
            "376 U.S. 364",
            "1964 U.S. LEXIS 1578"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106107 OR 9422064 OR 9422065) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjkwMDM4NDAwMDAwJnM9MzEzNTU2MyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106107+OR+9422064+OR+9422065%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 4,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 5,
        "triage_snippet_classified": 195
      },
      "lane2_top_cited": {
        "query": "cites:(106107 OR 9422064 OR 9422065)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05OTEmcz0xMDU3NjE4JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106107+OR+9422064+OR+9422065%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106107 OR 9422064 OR 9422065)",
        "reviewed": 33,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 33,
        "triage_read": 1,
        "triage_snippet_classified": 32
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106107 OR 9422064 OR 9422065)",
    "indexed_citing_opinions": 1628,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106107,
        "count": 1501,
        "count_source": "search"
      },
      {
        "opinion_id": 9422064,
        "count": 178,
        "count_source": "search"
      },
      {
        "opinion_id": 9422065,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2501,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/elkins-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2OTk2MTkmcz05NDgxNjY5JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106107+OR+9422064+OR+9422065%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106107,
        "cited_id": 89675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 101180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 101963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104006,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105584,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105789,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105857,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 234366,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 234773,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 235212,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 239614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 239813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 240496,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 242217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 246433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 248020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 249351,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1118348,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1122381,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1174129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1178849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1199500,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1209203,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1237532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1328981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1380217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1401576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1472688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1475515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1476789,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1480891,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1483661,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1489412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1490225,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1493506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1498347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1501575,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1501987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1502497,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1505389,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1508855,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1508963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1509635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1545838,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1548044,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1549055,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1660499,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1670307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1680451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1837215,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1921065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1934063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2019054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2022531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2030212,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2030951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2041058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2041065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2146371,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2190973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2199709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2228330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2352643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2466177,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2615411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2619395,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3233534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3246119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3302902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3307559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3311672,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3321660,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3412636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3484807,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3487094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3517292,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3529427,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3534889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3553875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3571966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3580565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3588018,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3646527,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3672959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3682031,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3780866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3812264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3827556,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3842073,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3848320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3924432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3948208,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3980535,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3990360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 4002892,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 4012045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 4012941,
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
    "date_created": "2026-07-05T03:11:05Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T03:11:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T03:11:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T03:16:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T03:11:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Elkins v. United States

```
<opinion type="majority">
<author id="b280-14">Mr. Justice Stewart</author>
<p id="APZ">delivered the opinion of the Court.</p>
<p id="b280-15">The petitioners were indicted in the United States District Court in Oregon for the offense of intercepting and divulging telephone communications and of conspiracy to do so. <span class="citation no-link">47 U. S. C. §§ 501</span>, 605; <span class="citation no-link">18 U. S. C. § 371</span>. Before trial the petitioners made a motion to suppress as evidence several tape and wire recordings and <page-number citation-index="1" label="207">*207</page-number>a recording machine, which had originally been seized by state law enforcement officers in the home of petitioner Clark under circumstances which, two Oregon courts had found, had rendered the search and seizure unlawful.<footnotemark>1</footnotemark> At the hearing on the motion the district judge assumed without deciding that the articles had been obtained as the result of an unreasonable search and seizure, but denied the motion to suppress because there was no evidence that any “agent of the United States had any knowledge or information or suspicion of any kind that this search was being contemplated or was eventually made by the State officers until they read about it in the newspaper.” At the trial the articles in question were admitted in evidence against the petitioners, and they were convicted.</p>
<p id="b282-5"><page-number citation-index="1" label="208">*208</page-number>The convictions were affirmed by the Court of Appeals for the Ninth Circuit, <span class="citation" data-id="248020"><a href="/opinion/248020/james-butler-elkins-and-raymond-frederick-clark-v-united-states/" aria-description="Citation for case: James Butler Elkins and Raymond Frederick Clark v. United...">266 F. 2d 588</a></span>. That court agreed with the district judge that it was unnecessary to determine whether or not the original state search and seizure had been lawful, because there had been no participation by federal officers. “Hence the unlawfulness of the State search and seizure, if indeed they were unlawful, did not entitle defendants to an order of the .District Court suppressing the property seized.” <span class="citation" data-id="248020"><a href="/opinion/248020/james-butler-elkins-and-raymond-frederick-clark-v-united-states/#594" aria-description="Citation for case: James Butler Elkins and Raymond Frederick Clark v. United...">266 F. 2d, at 594</a></span>.</p>
<p id="b282-6">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./361/810/">361 U. S. 810</a></span>, to consider a question of importance in the administration of federal justice. The question is this: May articles obtained as the result of an unreasonable search and seizure by state officers, without involvement of federal officers, be introduced in evidence against a defendant over his timely objection in a federal criminal trial? In a word, we re-examine here the validity of what has come to be called the silver platter doctrine.<footnotemark>2</footnotemark> For the reasons that follow we conclude that this doctrine can no longer be accepted.</p>
<p id="b282-7">To put the issue in historic perspective, the appropriate starting point must be <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. <page-number citation-index="1" label="209">*209</page-number>383</a></span>, decided in 1914. It was there that the Court established the rule which excludes in a federal criminal prosecution evidence obtained by federal agents in violation of the defendant's Fourth Amendment rights. The foundation for that decision was set out in forthright words:</p>
<blockquote id="b283-5">“The effect of the Fourth Amendment is to put the courts of the United States and Federal officials, in the exercise of their power and authority, under limitations and restraints as to the exercise of such power and authority, and to forever secure the people, their persons, houses, papers and effects against all unreasonable searches and seizures under the guise of law. This protection reaches all alike, whether accused of crime or not, and the duty of giving to it force and effect is obligatory upon all entrusted under our Federal system with the enforcement of the laws. The tendency of those who execute the criminal laws of the country to obtain conviction by means of unlawful seizures and enforced confessions, the latter often obtained after subjecting accused persons to unwarranted practices destructive of rights secured by the Federal Constitution, should find no sanction in the judgments of the courts which are charged at all times with the support of the Constitution and to which people of all conditions have a right to appeal for the maintenance of such fundamental rights.</blockquote>
<blockquote id="b283-6">“. . . If letters and private documents can thus be seized and held and used in evidence against a citizen accused of an offense, the protection of the Fourth Amendment declaring his right to be secure against such searches and seizures is of no value, and, so far as those thus placed are concerned, might as well be stricken from the Constitution. The efforts <page-number citation-index="1" label="210">*210</page-number>of the courts and their officials to bring the guilty to punishment, praiseworthy as they are, are not to be aided by the sacrifice of those great principles established by years of endeavor and suffering which have resulted in their embodiment in the fundamental law of the land.” <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#391" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 391-393</a></span>.</blockquote>
<p id="b284-6">To the exclusionary rule of <em>Weeks </em>v. <em>United States </em>there has been unquestioning adherence for now almost half a century. See <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>; <em>Gouled </em>v. <em>United States, </em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span>; <em>Amos </em>v. <em>United States, </em><span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U. S. 313</a></span>; <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span>; <em>Go-Bart Co. </em>v. <em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span>; <em>Grau </em>v. <em>United States, </em><span class="citation" data-id="101963"><a href="/opinion/101963/grau-v-united-states/" aria-description="Citation for case: Grau v. United States">287 U. S. 124</a></span>; <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>; <em>United States v. Jeffers, </em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span>.</p>
<p id="b284-7">But the <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>case also announced, unobtrusively but nonetheless definitely, another evidentiary rule. Some of the articles used as evidence against Weeks had been unlawfully seized by local police officers acting on their own account. The Court held that the admission of this evidence was not error for the reason that “the Fourth Amendment is not directed to individual misconduct of such officials. Its limitations reach the Federal Government and its agencies.” <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#398" aria-description="Citation for case: Weeks v. United States">232 U. S., at 398</a></span>. Despité the limited discussion of this second ruling in the <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>opinion, the right of the prosecutor in a federal criminal trial to avail himself of evidence unlawfully seized by state officers apparently went unquestioned for the next thirty-five years. See, <em>e. g., Byars </em>v. <em>United States, </em><span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#33" aria-description="Citation for case: Byars v. United States">273 U. S. 28, 33</a></span>; <em>Feldman </em>v. <em>United States, </em><span class="citation" data-id="9419517"><a href="/opinion/104006/feldman-v-united-states/#492" aria-description="Citation for case: Feldman v. United States">322 U. S. 487, 492</a></span>.<footnotemark>3</footnotemark></p>
<p id="b285-4"><page-number citation-index="1" label="211">*211</page-number>That such a rule would engender practical difficulties in an era of expanding federal criminal jurisdiction could not, perhaps, have been foreseen. In any event the difficulties soon appeared. They arose from the entirely commendable practice of state and federal agents to cooperate with each other in the investigation and detection of criminal activity. When in a federal criminal prosecution evidence which had been illegally seized by state officers was sought to be introduced, the question inevitably arose whether there had been such participation by federal agents in the search and seizure as to make applicable the exclusionary rule of <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>. </em>See <em>Flagg </em>v. <em>United States, </em><span class="citation" data-id="8799726"><a href="/opinion/8815246/flagg-v-united-states/#483" aria-description="Citation for case: Flagg v. United States">233 Fed. 481, 483</a></span>; <em>United States </em>v. <em>Slusser, </em><span class="citation" data-id="8819339"><a href="/opinion/8834327/united-states-v-slusser/#820" aria-description="Citation for case: United States v. Slusser">270 Fed. 818, 820</a></span>; <em>United States </em>v. <em>Falloco, </em><span class="citation" data-id="8823350"><a href="/opinion/8838257/united-states-v-falloco/#82" aria-description="Citation for case: United States v. Falloco">277 Fed. 75, 82</a></span>; <em>Legman </em>v. <em>United States, </em><span class="citation" data-id="8834058"><a href="/opinion/8848718/legman-v-united-states/#476" aria-description="Citation for case: Legman v. United States">295 Fed. 474, 476-478</a></span>; <em>Marron </em>v. <em>United States, </em><span class="citation" data-id="1508855"><a href="/opinion/1508855/marron-v-united-states/#259" aria-description="Citation for case: Marron v. United States">8 F. 2d 251, 259</a></span>; <em>United States </em>v. <em>Brown, </em><span class="citation" data-id="1508963"><a href="/opinion/1508963/united-states-v-brown/#631" aria-description="Citation for case: United States v. Brown">8 F. 2d 630, 631</a></span>.</p>
<p id="b285-5">This Court first came to grips with the problem in <em>Byars </em>v. <em>United States, </em><span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U. S. 28</a></span>. There it was held that when the participation of the federal agent in the search was “under color of his federal office” and the search “in substance and effect was a joint operation of the local and federal officers,” then the evidence .must be excluded, because “the effect is the same as though [the federal agent] had engaged in the undertaking as one exclusively his own.” <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#33" aria-description="Citation for case: Byars v. United States">273 U. S., at 33</a></span>. In <em>Gambino </em>v. <em>United States, </em><span class="citation" data-id="101180"><a href="/opinion/101180/gambino-v-united-states/" aria-description="Citation for case: Gambino v. United States">275 U. S. 310</a></span>, the Court went further. There state officers had seized liquor from the defendants’ automobile after an unlawful search in which no federal officers had participated. The liquor was admitted in evidence against the defendants in their subsequent federal trial for violation of the National Prohibition Act. This <page-number citation-index="1" label="212">*212</page-number>Court reversed the judgments of conviction, holding that the illegally seized evidence should have been excluded. Pointing out that there was “no suggestion that the defendants were committing, at the time of the arrest, search and seizure, any state offense; or that they had done so in the past; or that the [state] troopers believed that they had,” the Court found that “[t]he wrongful arrest, search and seizure were made solely on behalf of the United States.” <span class="citation" data-id="101180"><a href="/opinion/101180/gambino-v-united-states/#314" aria-description="Citation for case: Gambino v. United States">275 U. S., at 314, 316</a></span>.</p>
<p id="b286-5">Despite these decisions, or perhaps because of them, cases kept arising in which the federal courts were faced with determining whether there had been such participation by federal officers in a lawless state search as to make inadmissible in evidence that which had been seized. And it is fair to say that in their approach to this recurring question, no less than in their disposition of concrete cases, the federal courts did not find themselves in complete harmony, nor even internally self-consistent.<footnotemark>4</footnotemark> No less difficulty was experienced by the courts in determining whether, even in the absence of actual participation by federal agents, the state officers’ illegal search and seizure had nevertheless been made “solely on behalf of the United States.” <footnotemark>5</footnotemark></p>
<p id="b286-6">But difficult and unpredictable as may have been their application to concrete cases, the controlling principles seemed clear up to 1949. Evidence which had been seized by federal officers in violation of the Fourth Amendment <page-number citation-index="1" label="213">*213</page-number>could not be used in a federal criminal prosecution. Evidence which had been obtained by state agents in an unreasonable search and seizure was admissible, because, as <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>had pointed out, the Fourth Amendment was not “directed to” the “misconduct of such officials.” But if federal agents had participated in an unreasonable search and seizure by state officers, or if the state officers had acted solely on behalf of the United States, the evidence was not admissible in a federal prosecution.</p>
<p id="b287-5">Then came <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span>. With the ultimate determination in <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span> </em>— that the Due Process Clause of the Fourteenth Amendment does not itself require state courts to adopt the exclusionary rule with respect to evidence illegally seized by state agents — we are not here directly concerned. But nothing could be of greater relevance to the present inquiry than the underlying constitutional doctrine which <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span> </em>established. For there it was unequivocally determined by a unanimous Court that the Federal Constitution, by virtue of the Fourteenth Amendment, prohibits unreasonable searches and seizures by state officers. “The security of one’s privacy against arbitrary intrusion by the police ... is . . . implicit in ‘the concept of ordered liberty’ and as such enforceable against the States through the Due Process Clause.” <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27-28</a></span>. The Court has subsequently found frequent occasion to reiterate this statement from <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>. </em>See <em>Stefanelli </em>v. <em>Minard, </em><span class="citation" data-id="9420643"><a href="/opinion/104937/stefanelli-v-minard/#119" aria-description="Citation for case: Stefanelli v. Minard">342 U. S. 117, 119</a></span>; <em>Irvine </em>v. <em>California, 347 </em>U. S. 128, 132; <em>Frank </em>v. <em>Maryland, </em><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#362" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360, 362-363</a></span>.</p>
<p id="b287-6">The foundation upon which the admissibility of state-seized evidence in a federal trial originally rested — that unreasonable state searches did not violate the Federal Constitution — thus disappeared in 1949. This removal of the doctrinal underpinning for the admissibility rule has apparently escaped the attention of most of the federal courts, which have continued to approve the admission of <page-number citation-index="1" label="214">*214</page-number>evidence illegally seized by state officers without so much as even discussing the impact of Wolf.<footnotemark>6</footnotemark> Only two of the courts of appeals which have adhered to the admissibility rule appear to have recognized that <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span> </em>casts doubt upon its continuing validity. <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="235212"><a href="/opinion/235212/robert-laverne-jones-v-united-states/" aria-description="Citation for case: Robert Laverne Jones v. United States">217 F. 2d 381</a></span> (C. A. 8th Cir.); <em>United States </em>v. <em>Benanti, </em><span class="citation" data-id="242217"><a href="/opinion/242217/united-states-v-salvatore-benanti/" aria-description="Citation for case: United States v. Salvatore Benanti">244 F. 2d 389</a></span> (C. A. 2d Cir.), reversed on other grounds, <span class="citation" data-id="105584"><a href="/opinion/105584/benanti-v-united-states/" aria-description="Citation for case: Benanti v. United States">355 U. S. 96</a></span>. Cf. <em>Kendall </em>v. <em>United States, </em><span class="citation" data-id="249351"><a href="/opinion/249351/paul-a-kendall-and-ruth-elder-kendall-v-united-states/#165" aria-description="Citation for case: Paul A. Kendall and Ruth Elder Kendall v. United States">272 F. 2d 163, 165</a></span> (C. A. 5th Cir.). The Court of Appeals for the District of Columbia has been alone in squarely holding “that the Weeks and the Wolf decisions, considered together, make all evidence obtained by unconstitutional search and seizure unacceptable in federal courts.” <em>Hanna </em>v. <em>United States, </em>104 U. S. App. D. C. 205, 209, <span class="citation" data-id="246433"><a href="/opinion/246433/samuel-j-hanna-v-united-states/#727" aria-description="Citation for case: Samuel J. Hanna v. United States">260 F. 2d 723, 727</a></span>.</p>
<p id="b288-6">Yet this Court’s awareness that the constitutional doctrine of <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span> </em>operated to undermine the logical foundation of the <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>admissibility rule has been manifest from the very day that <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span> </em>was decided. In <em>Lustig </em>v. <em>United States, </em><span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/" aria-description="Citation for case: Lustig v. United States">338 U. S. 74</a></span>, decided that day, the prevailing opinion carefully left open the question of the continuing validity of the admissibility rule. “Where there is participation on the part of federal officers,” the opinion said, “it is not necessary to consider what would be the result if the search had been conducted entirely by State officers.” 338 U. S., at 79. And in <em>Benanti </em>v. <em>United States, </em><span class="citation" data-id="105584"><a href="/opinion/105584/benanti-v-united-states/" aria-description="Citation for case: Benanti v. United States">355 U. S. 96</a></span>, the Court was at pains to point out that “[i]t has remained an open question in this Court whether evidence obtained solely by state agents in an illegal search may be admissible in federal court . . . .” <span class="citation" data-id="105584"><a href="/opinion/105584/benanti-v-united-states/#102" aria-description="Citation for case: Benanti v. United States">355 U. S., at 102, note 10</a></span>. There the question has stood for 11 years.</p>
<p id="b289-4"><page-number citation-index="1" label="215">*215</page-number>If resolution of the issue were to be dictated solely by principles of logic, it is clear what our decision would have to be. For surely no distinction can logically be drawn between evidence obtained in violation of the Fourth Amendment and that obtained in violation of the Fourteenth. The Constitution is flouted equally in either case. To the victim it matters not whether his constitutional right has been invaded by a federal agent or by a state officer.<footnotemark>7</footnotemark> It would be a curiously ambivalent rule that would require the courts of the United States to differentiate between unconstitutionally seized evidence upon so arbitrary a basis. Such a distinction indeed would appear to reflect an indefensibly selective evaluation of the provisions of the Constitution. Moreover, it would seem logically impossible to justify a policy that would bar from a federal trial what state officers had obtained in violation of a federal statute, yet would admit that which they had seized in violation of the Constitu-tionffitself. Cf. <em>Benanti </em>v. <em>United States, </em><span class="citation" data-id="105584"><a href="/opinion/105584/benanti-v-united-states/" aria-description="Citation for case: Benanti v. United States">355 U. S. 96</a></span>.</p>
<p id="b290-4"><page-number citation-index="1" label="216">*216</page-number>Mere logical symmetry and abstract reasoning are perhaps not enough, however, to support a doctrine that would exclude relevant evidence from the trial of a federal criminal case. It is true that there is not involved here an absolute or qualified testimonial privilege such as that accorded a spouse, a patient, or a penitent, which irrevocably bars otherwise admissible evidence because of the <em>status </em>of the witness or his relationship to the defendant. Cf. <em>Hawkins </em>v. <em>United States, </em><span class="citation" data-id="9421718"><a href="/opinion/105789/hawkins-v-united-states/" aria-description="Citation for case: Hawkins v. United States">358 U. S. 74</a></span>. A rule which would exclude evidence if, and only if, government officials in a particular case had chosen to engage in unlawful <em>conduct </em>is of a different order. Yet, any apparent limitation upon the process of discovering truth in a federal trial ought to be imposed only upon the basis of considerations which outweigh the general need for untrammeled disclosure . of competent and relevant evidence in a court of justice.</p>
<p id="b290-5">What is here invoked is the Court’s supervisory power over the administration of criminal justice in the federal courts, under which the Court has “from the very beginning -of its history, formulated rules of evidence to be applied in federal criminal prosecutions.” <em>McNabb </em>v. <em>United States, </em><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/#341" aria-description="Citation for case: McNabb v. United States">318 U. S. 332, 341</a></span>. In devising such evi-dentiary rules, we are to be governed by “principles of the common law as they may be interpreted ... in the light of reason and experience.” Rule 26, Fed. Rules Crim. Proc. Determination of the issue before us must ultimately depend, therefore, upon evaluation of the exclusionary rule itself in the context here presented.</p>
<p id="b290-6">The exclusionary rule has for decades been the subject of ardent controversy. The arguments of its antagonists and of its proponents have been so many times marshalled as to require no lengthy elaboration here. Most of what has been said in opposition to the rule was distilled in a single Cardozo sentence — “The criminal is to go free because the constable has blundered.” <em>People </em>v. <em>Defore, </em><page-number citation-index="1" label="217">*217</page-number><span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#21" aria-description="Citation for case: People v. Defore">242 N. Y. 13, 21</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#587" aria-description="Citation for case: People v. Defore">150 N. E. 585, 587</a></span>. The same point was made at somewhat greater length in the often quoted words of Professor Wigmore: “Titus, you have been found guilty of conducting a lottery; Flavius, you have confessedly violated the constitution. Titus ought to suffer imprisonment for crime, and Flavius for contempt. But no! We shall let you <em>both </em>go free. We shall not punish Flavius directly, but shall do so by reversing Titus’ conviction. This is our way of teaching people like Flavius to behave, and of teaching people like Titus to behave, and incidentally of securing respect for the Constitution. Our way of upholding the Constitution is not to strike at the man who breaks it, but to let off somebody else who broke something else.” 8 Wigmore, Evidence (3d ed. 1940), § 2184.</p>
<p id="b291-5">Yet, however felicitous their phrasing, these objections hardly answer the basic postulate of the exclusionary rule itself. The rule is calculated to prevent, not to repair. Its purpose is to deter — to compel respect for the constitutional guaranty in the only effectively available way— by removing the incentive to disregard it. See <em>Eleuteri </em>v. Rickman, 26 N. J. 506, 513, <span class="citation" data-id="1934063"><a href="/opinion/1934063/eleuteri-v-richman/#50" aria-description="Citation for case: Eleuteri v. Richman">141 A. 2d 46, 50</a></span>. Mr. Justice Jackson summed it up well:</p>
<blockquote id="b291-6">“Only occasional and more flagrant abuses come to the attention of the courts, and then only those where the search and seizure yields incriminating evidence and the defendant is at least sufficiently compromised to be indicted. If the officers raid a home, an office, or stop and search an automobile but find nothing incriminating, this invasion of the personal liberty of the innocent too often finds no practical redress. There may be, and I am convinced that there are, many unlawful searches of homes and automobiles of innocent people which turn up nothing incriminating, in which no arrest is made, about <page-number citation-index="1" label="218">*218</page-number>which courts do nothing, and about which we never hear.</blockquote>
<blockquote id="b292-5">“Courts can protect the innocent against such invasions only indirectly and through the medium of excluding evidence obtained against those who frequently are guilty.” <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#181" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 181</a></span> (dissenting opinion).</blockquote>
<p id="b292-6">Empirical statistics are not available to show that the inhabitants of states which follow the exclusionary rule suffer less from lawless searches and seizures than do those of states which admit evidence unlawfully obtained. Since as a practical matter it is never easy to prove a negative, it is hardly likely that conclusive factual data could ever be assembled. For much the same reason, it cannot positively be demonstrated that enforcement of the criminal law is either more or less effective under either rule.</p>
<p id="b292-7">But pragmatic evidence of a sort is not wanting. The federal courts themselves have operated under the exclusionary rule of <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>for almost half a century; yet it has not been suggested either that the Federal Bureau of Investigation has thereby been rendered ineffective, or that the administration of criminal justice in the federal courts has thereby been disrupted.<footnotemark>8</footnotemark> Moreover, the expe<page-number citation-index="1" label="219">*219</page-number>rience of the states is impressive. Not more than half the states continue totally to adhere to the rule that evidence is freely admissible no matter how it was obtained.<footnotemark>9</footnotemark> Most of the others have adopted the exclusionary rule in its entirety; the rest have adopted it in part.<footnotemark>10</footnotemark> The movement towards the rule of exclusion has been halting but seemingly inexorable.<footnotemark>11</footnotemark> Since the <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span> </em>decision one state has switched its position in that direction by legislation,<footnotemark>12</footnotemark> and two others by judicial decision.<footnotemark>13</footnotemark> Another state, uncommitted until 1955, in that year adopted the rule <page-number citation-index="1" label="220">*220</page-number>of exclusion.<footnotemark>14</footnotemark> Significantly, most of the exclusionary states which have had to consider the issue have held that evidence obtained by <em>federal </em>officers in a search and seizure unlawful under the Fourth Amendment must be suppressed in a prosecution in the <em>state </em>courts. <em>State </em>v. <em>Arregui, </em><span class="citation" data-id="3412636"><a href="/opinion/3416496/state-v-arregui/" aria-description="Citation for case: State v. Arregui">44 Idaho 43</a></span>, <span class="citation" data-id="3412636"><a href="/opinion/3416496/state-v-arregui/" aria-description="Citation for case: State v. Arregui">254 P. 788</a></span>; <em>Walters </em>v. <em>Commonwealth, </em><span class="citation" data-id="7148071"><a href="/opinion/7235652/walters-v-commonwealth/" aria-description="Citation for case: Walters v. Commonwealth">199 Ky. 182</a></span>, <span class="citation" data-id="7148071"><a href="/opinion/7235652/walters-v-commonwealth/" aria-description="Citation for case: Walters v. Commonwealth">250 S. W. 839</a></span>; <em>Little </em>v. <em>State, </em><span class="citation" data-id="3517292"><a href="/opinion/3544745/little-v-state/" aria-description="Citation for case: Little v. State">171 Miss. 818</a></span>, <span class="citation" data-id="3517292"><a href="/opinion/3544745/little-v-state/" aria-description="Citation for case: Little v. State">159 So. 103</a></span>; <em>State </em>v. <em>Rebasti, </em><span class="citation" data-id="3534889"><a href="/opinion/3557416/state-v-rebasti/" aria-description="Citation for case: State v. Rebasti">306 Mo. 336</a></span>, <span class="citation" data-id="3534889"><a href="/opinion/3557416/state-v-rebasti/" aria-description="Citation for case: State v. Rebasti">267 S. W. 858</a></span>; <em>State </em>v. <em>Hiteshew, </em><span class="citation" data-id="4012045"><a href="/opinion/4234880/state-v-hiteshew/" aria-description="Citation for case: State v. Hiteshew">42 Wyo. 147</a></span>, <span class="citation" data-id="4012045"><a href="/opinion/4234880/state-v-hiteshew/" aria-description="Citation for case: State v. Hiteshew">292 P. 2</a></span>; see <em>Ramirez </em>v. <em>State, </em><span class="citation" data-id="3924432"><a href="/opinion/4158808/ramirez-v-state/" aria-description="Citation for case: Ramirez v. State">123 Tex. Cr. R. 254</a></span>, <span class="citation" data-id="3924432"><a href="/opinion/4158808/ramirez-v-state/" aria-description="Citation for case: Ramirez v. State">58 S. W. 2d 829</a></span>. Compare <em>Rea </em>v. <em>United States, </em><span class="citation" data-id="9421227"><a href="/opinion/105343/rea-v-united-states/" aria-description="Citation for case: Rea v. United States">350 U. S. 214</a></span>.</p>
<p id="b294-6">The experience in California has been most illuminating. In 1955 the Supreme Court of that State resolutely turned its back on many years of precedent and adopted the exclusionary rule. <em>People </em>v. <em>Cahan, </em><span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/" aria-description="Citation for case: People v. Cahan">44 Cal. 2d 434</a></span>, <span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/" aria-description="Citation for case: People v. Cahan">282 P. 2d 905</a></span>. “We have been compelled to reach that conclusion because other remedies have completely failed to secure compliance with the constitutional provisions on the part of police officers with the attendant result that the courts under the ■ old rule have been constantly required to participate in, and in effect condone, the lawless activities of law enforcement officers. . . . Experience has demonstrated, however, that neither administrative, criminal nor civil remedies are effective in suppressing lawless searches and seizures. The innocent suffer with the guilty, and we cannot close our eyes to the effect the rule we adopt will have on the rights of those not before the court.” <span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/#445" aria-description="Citation for case: People v. Cahan">44 Cal. 2d 434, at 445, 447</a></span>, <span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/#911" aria-description="Citation for case: People v. Cahan">282 P. 2d 905, at 911-912, 913</a></span>.</p>
<p id="b294-7">The ■ chief law enforcement officer of California was quoted as having made this practical evaluation of the <em><span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/" aria-description="Citation for case: People v. Cahan">Cahan</a></span> </em>decision less than two years later:</p>
<blockquote id="b294-8">“The over-all effects of the Cahan decision, particularly in view of the rules now worked out by the Supreme Court, have been excellent. A much <page-number citation-index="1" label="221">*221</page-number>greater education, is called for on the part of all peace officers of California. As a result, I am confident they will be much better police officers. I think there is more cooperation with the District Attorneys and this will make for better administration of criminal justice.” <footnotemark>15</footnotemark></blockquote>
<p id="b295-5">Impressive as is this experience of individual states, even more is to be said for adoption of the exclusionary rule in the particular context here presented — a context which brings into focus considerations of federalism. The very essence of a healthy federalism depends upon the avoidance of needless conflict between state and federal courts. Yet when a federal court sitting in an exclusionary state admits evidence lawlessly seized by state agents, it not only frustrates state policy, but frustrates that policy in a particularly inappropriate and ironic way. For by admitting the unlawfully seized evidence the federal court serves to defeat the state’s effort to assure obedience to the Federal Constitution. In states which have not adopted the exclusionary rule, on the other hand, it would work no conflict with local policy for a federal court to decline to receive evidence unlawfully seized by state officers. The question with which we deal today affects not at all the freedom of the states to develop and apply their own sanctions in their own way. Cf. <em>Wolf </em>v. Colorado, <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span>.</p>
<p id="b295-6">Free and open cooperation between state and federal law enforcement officers is to be commended and encouraged. Yet that kind of cooperation is hardly promoted by a rule that implicitly invites federal officers to withdraw from such association and at least tacitly to ericour-<page-number citation-index="1" label="222">*222</page-number>age state officers in the disregard of constitutionally protected freedom. If, on the other hand, it is understood that the fruit of an unlawful search by state agents will be inadmissible in a federal trial, there can be no inducement to subterfuge and evasion with respect to federal-state cooperation in criminal investigation. Instead, forthright cooperation under constitutional standards will be promoted and fostered.</p>
<p id="b296-6">It must always be remembered that what the Constitution forbids is not all searches and seizures, but unreasonable searches and seizures. Without pausing to analyze individual decisions, it can fairly be said that in applying the Fourth Amendment this Court has seldom shown itself unaware of the practical demands of effective criminal investigation and law enforcement. Indeed, there are those who think that some of the Court’s decisions have tipped the balance too heavily against the protection of that individual privacy which it was the purpose of the Fourth Amendment to guarantee. See <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#155" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 155, 183, 195</a></span> (dissenting opinions); <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#66" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 66, 68</a></span> (dissenting opinions). In any event, while individual cases have sometimes evoked “fluctuating differences of view,” <em>Abel </em>v. <em>United States, </em><span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#235" aria-description="Citation for case: Abel v. United States">362 U. S. 217, 235</a></span>, it can hardly be said that in the over-all pattern of Fourth Amendment decisions this Court has been either unrealistic or visionary.</p>
<p id="b296-7">These, then, are the considerations of reason and experience which point to the rejection of a doctrine that would freely admit in a federal criminal trial evidence seized by state agents in violation of the defendant’s constitutional rights. But there is another consideration— the imperative of judicial integrity. It was of this that Mr. Justice Holmes and Mr. Justice Brandéis so eloquently spoke in <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#469" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, at 469, 471</a></span>, more than 30 years ago. “For those who <page-number citation-index="1" label="223">*223</page-number>agree with me,” said Mr. Justice Holmes, “no distinction can be taken between the Government as prosecutor and the Government as judge.” <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#470" aria-description="Citation for case: Olmstead v. United States">277 U. S., at 470</a></span>. (Dissenting opinion.) “In a government of laws,” said Mr. Justice Brandéis, “existence of the government will be imperilled if it fails to observe the law scrupulously. Our Government is the potent, the omnipresent teacher. For good or for ill, it teaches the whole people by its example. Crime is contagious. If the Government becomes a lawbreaker, it breeds contempt for law; it invites every man to become a law unto himself; it invites anarchy. To declare that in the administration of the criminal law the end justifies the means — to declare that the Government may commit crimes in order to secure the conviction of a private criminal — would bring terrible retribution. Against that pernicious doctrine this Court should resolutely set its face.” <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#485" aria-description="Citation for case: Olmstead v. United States">277 U. S., at 485</a></span>. (Dissenting opinion.)</p>
<p id="b297-5">This basic principle was accepted by the Court in <em>McNabb </em>v. <em>United States, </em><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">318 U. S. 332</a></span>. There it was held that “a conviction resting on evidence secured through such a flagrant disregard of the procedure which Congress has commanded cannot be allowed to stand without making the courts themselves accomplices in willful disobedience of law.” <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/#345" aria-description="Citation for case: McNabb v. United States">318 U. S., at 345</a></span>. Even less should the federal courts be accomplices in the willful disobedience of a Constitution they are sworn to uphold.</p>
<p id="b297-6">For these reasons we hold that evidence obtained by state officers during a search which, if conducted by federal officers, would have violated the defendant’s immunity from unreasonable searches and seizures under the Fourth Amendment is inadmissible over the defendant’s timely objection in a federal criminal trial.<footnotemark>16</footnotemark> In deter<page-number citation-index="1" label="224">*224</page-number>mining whether there has been an unreasonable search and seizure by state officers, a federal court must make an independent inquiry, whether or not there has been such an inquiry by a state court, and irrespective of how any such inquiry may have turned out. The test is one of federal law, neither enlarged by what one state court may have countenanced, nor diminished by what another may have colorably suppressed.</p>
<p id="b298-4">The judgment of the Court of Appeals is set aside, and the case is remanded to the District Court for further proceedings consistent with this opinion.</p>
<p id="b298-5">
<em>Vacated and remanded.</em>
</p>
<p id="b298-6">APPENDIX TO OPINION OF THE COURT.</p>
<p id="b298-7">Table <em>I. </em>— Admissibility, <em>in state courts, of evidence illegally seized by state officers.</em></p>
<p id="b298-9">
<em>State Pre-Weeks Pre-Wolf Post-Wolf</em>
</p>
<p id="b298-10">Alabama_ Admissible_ Admissible_ Partially</p>
<p id="b298-11">excludable</p>
<p id="b298-12">Arizona_ _ Admissible_ Admissible</p>
<p id="b298-13">Arkansas_ Admissible_ Admissible_ Admissible</p>
<p id="b298-14">California_ Admissible_ Admissible_ Excludable</p>
<p id="b298-15">Colorado_ _ Admissible_ Admissible</p>
<p id="b298-16">Connecticut_ Admissible_ Admissible_ Admissible</p>
<p id="b298-17">Delaware_ _ Admissible_ Excludable</p>
<p id="b298-18">Florida_ _ Excludable_ Excludable</p>
<p id="b298-19">Georgia_■_ Admissible_ Admissible_ Admissible</p>
<p id="b298-20">Idaho_ Admissible_ Excludable_ Excludable</p>
<p id="b298-21">Illinois_ Admissible.-. Excludable_ Excludable</p>
<p id="b298-22">Indiana_ _ Excludable_ Excludable</p>
<p id="b298-23">Iowa_ Excludable... Admissible_ Admissible</p>
<p id="b298-24">Kansas_ Admissible_ Admissible_ Admissible</p>
<p id="b298-25">Kentucky_ _ Excludable_ Excludable</p>
<p id="b298-26">Louisiana_ _ Admissible... Admissible</p>
<p id="b298-27">Maine_ Admissible_ Admissible_ Admissible</p>
<p id="AMr">Maryland_ Admissible_ Partially Partially excludable excludable</p>
<p id="b298-30">Massachusetts_ Admissible_ Admissible_ Admissible</p>
<p id="b299-4"><page-number citation-index="1" label="225">*225</page-number>Table <em>I. </em>— Admissibility, <em>in state courts, of evidence illegally seized by state officers </em>— Continued.</p>
<p id="b299-5">
<em>State Pre-Weeks Pre-Wolf Post-Wolf</em>
</p>
<p id="b299-6">Michigan_ Admissible_ Excludable_ Partially . excludable</p>
<p id="b299-8">Minnesota- Admissible. __ Admissible... Admissible</p>
<p id="b299-9">Mississippi_ _ Excludable_ Excludable</p>
<p id="b299-10">Missouri- Admissible_ Excludable... Excludable</p>
<p id="b299-11">Montana- Admissible_ Excludable_ Excludable</p>
<p id="b299-12">Nebraska- Admissible... Admissible_ Admissible</p>
<p id="b299-13">Nevada- - Admissible_ Admissible</p>
<p id="b299-14">New Hampshire_ Admissible_ Admissible_ Admissible</p>
<p id="b299-15">New Jersey_ _ Admissible_ Admissible</p>
<p id="b299-16">New Mexico_ _- Admissible_ Admissible</p>
<p id="b299-17">New York- Admissible... Admissible_ Admissible</p>
<p id="b299-18">North Carolina_ Admissible_ Admissible_ Excludable</p>
<p id="b299-19">North Dakota_ _ Admissible_ Admissible</p>
<p id="b299-20">Ohio- - Admissible_ Admissible</p>
<p id="b299-21">Oklahoma_ Admissible_ Excludable_ Excludable</p>
<p id="b299-22">Oregon- Admissible_ Excludable_ Excludable</p>
<p id="b299-23">Pennsylvania_ _ Admissible... Admissible</p>
<p id="b299-24">Rhode Island_ _ _ Excludable</p>
<p id="b299-25">South Carolina- Admissible_ Admissible_ Admissible</p>
<p id="b299-26">South Dakota_ Admissible. __ Excludable_ Partially excludable</p>
<p id="b299-28">Tennessee_... Admissible_ Excludable... Excludable</p>
<p id="b299-29">Texas- - Excludable_ Excludable</p>
<p id="b299-30">Utah- - Admissible_ Admissible</p>
<p id="b299-31">Vermont- Admissible_ Admissible_ Admissible</p>
<p id="b299-32">Virginia_ _ Admissible_ Admissible</p>
<p id="b299-33">Washington- Admissible... Excludable... Excludable</p>
<p id="b299-34">West Virginia_ Admissible_ Excludable_ Excludable</p>
<p id="b299-35">Wisconsin_ _ Excludable_ Excludable</p>
<p id="b299-36">Wyoming_ _ Excludable... Excludable</p>
<p id="b299-37">To admit — 27 To admit — 29 To admit — 24</p>
<p id="b299-38">To exclude — 1 To exclude— To exclude—</p>
<p id="b299-39">18. 26<footnotemark>*</footnotemark></p>
<p id="b299-40">Undecided— Undecided— Undecided—</p>
<p id="b299-41">20. 1. 0.</p>
<p id="b300-5"><page-number citation-index="1" label="226">*226</page-number>Table <em>II. </em>— Representative <em>cases by state, considering the admissibility of evidence illegally seized by state officers.</em></p>
<p id="b300-6">Alabama</p>
<p id="b300-7">Pre-Weeks: <em>Shields </em>v. <em>State, </em><span class="citation" data-id="6515773"><a href="/opinion/6639159/shields-v-state/" aria-description="Citation for case: Shields v. State">104 Ala. 35</a></span>, <span class="citation no-link">16 So. 85</span> (admissible).</p>
<p id="b300-8">Pre-Wolf: <em>Banks </em>v. <em>State, </em><span class="citation" data-id="3233534"><a href="/opinion/3232762/banks-v-state/" aria-description="Citation for case: Banks v. State">207 Ala. 179</a></span>, <span class="citation multiple-matches"><a href="/c/So./93/293/">93 So. 293</a></span> (admissible).</p>
<p id="b300-9">Post-Wolf: Cf. <em>Oldham </em>v. <em>State, </em><span class="citation" data-id="1118348"><a href="/opinion/1118348/oldham-v-state/" aria-description="Citation for case: Oldham v. State">259 Ala. 507</a></span>, <span class="citation" data-id="1118348"><a href="/opinion/1118348/oldham-v-state/" aria-description="Citation for case: Oldham v. State">67 So. 2d 55</a></span> (admissible) .</p>
<p id="b300-10">(Ala. Code, 1940 (Supp. 1955), Tit. 29, § 210, requires the exclusion of illegally obtained evidence in the trial of certain alcohol control cases.)</p>
<p id="b300-11">Arizona</p>
<p id="b300-12">Pre-Weeks: no holding.</p>
<p id="b300-13">Pre-Wolf: <em>Argetakis </em>v. <em>State, </em><span class="citation" data-id="6474949"><a href="/opinion/6599573/argetakis-v-state/" aria-description="Citation for case: Argetakis v. State">24 Ariz. 599</a></span>, <span class="citation" data-id="6474949"><a href="/opinion/6599573/argetakis-v-state/" aria-description="Citation for case: Argetakis v. State">212 P. 372</a></span> (admissible) .</p>
<p id="b300-14">Post-Wolf: <em>State </em>v. <em>Thomas, </em><span class="citation" data-id="1199500"><a href="/opinion/1199500/state-v-thomas/" aria-description="Citation for case: State v. Thomas">78 Ariz. 52</a></span>, <span class="citation" data-id="1199500"><a href="/opinion/1199500/state-v-thomas/" aria-description="Citation for case: State v. Thomas">275 P. 2d 408</a></span> (admissible).</p>
<p id="b300-15">Arkansas</p>
<p id="b300-16">Pre-Weeks: <em>Starchman </em>v. <em>State, </em><span class="citation" data-id="6543624"><a href="/opinion/6665982/starchman-v-state/" aria-description="Citation for case: Starchman v. State">62 Ark. 538</a></span>, <span class="citation" data-id="6543624"><a href="/opinion/6665982/starchman-v-state/" aria-description="Citation for case: Starchman v. State">36 S. W. 940</a></span> (admissible) .</p>
<p id="b300-17">Pre-Wolf: <em>Benson </em>v. <em>State, </em><span class="citation" data-id="7811152"><a href="/opinion/7866973/benson-v-state/" aria-description="Citation for case: Benson v. State">149 Ark. 633</a></span>, <span class="citation" data-id="7811152"><a href="/opinion/7866973/benson-v-state/" aria-description="Citation for case: Benson v. State">233 S. W. 758</a></span> (admissible) .</p>
<p id="b300-19">Post-Wolf: <em>Lane, Smith &amp; Barg </em>v. <em>State, </em><span class="citation" data-id="1780082"><a href="/opinion/1780082/lane-smith-barg-v-state/" aria-description="Citation for case: Lane, Smith &amp; Barg v. State">217 Ark. 114</a></span>, <span class="citation" data-id="1780082"><a href="/opinion/1780082/lane-smith-barg-v-state/" aria-description="Citation for case: Lane, Smith &amp; Barg v. State">229 S. W. 2d 43</a></span> (admissible).</p>
<p id="b300-20">California</p>
<p id="b300-21">Pre-Weeks: <em>People </em>v. <em>Le Doux, </em><span class="citation" data-id="3302902"><a href="/opinion/3303561/people-v-le-doux/" aria-description="Citation for case: People v. Le Doux">155 Cal. 535</a></span>, <span class="citation" data-id="3302902"><a href="/opinion/3303561/people-v-le-doux/" aria-description="Citation for case: People v. Le Doux">102 P. 517</a></span> (admissible).</p>
<p id="b300-22">Pre-Wolf: <em>People </em>v. <em>Mayen, </em><span class="citation" data-id="3307559"><a href="/opinion/3307673/people-v-mayen/" aria-description="Citation for case: People v. Mayen">188 Cal. 237</a></span>, <span class="citation" data-id="3307559"><a href="/opinion/3307673/people-v-mayen/" aria-description="Citation for case: People v. Mayen">205 P. 435</a></span> (admissible) .</p>
<p id="b300-23">Post-Wolf: <em>People </em>v. <em>Cahan, </em><span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/" aria-description="Citation for case: People v. Cahan">44 Cal. 2d 434</a></span>, <span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/" aria-description="Citation for case: People v. Cahan">282 P. 2d 905</a></span> (excludable) .</p>
<p id="b300-24">Colorado</p>
<p id="b300-25">Pre-Weeks: no holding.</p>
<p id="b300-26">Pre-Wolf: <em>Massantonio </em>v. <em>People, </em><span class="citation" data-id="3311672"><a href="/opinion/3316610/massantonio-v-people/" aria-description="Citation for case: Massantonio v. People">77 Colo. 392</a></span>, <span class="citation" data-id="3311672"><a href="/opinion/3316610/massantonio-v-people/" aria-description="Citation for case: Massantonio v. People">236 P. 1019</a></span> (admissible) .</p>
<p id="b300-27">Post-Wolf: <em>Williams </em>v. <em>People, </em><span class="citation" data-id="1174129"><a href="/opinion/1174129/williams-v-people/" aria-description="Citation for case: Williams v. People">136 Colo. 164</a></span>, <span class="citation" data-id="1174129"><a href="/opinion/1174129/williams-v-people/" aria-description="Citation for case: Williams v. People">315 P. 2d 189</a></span> (admissible).</p>
<p id="b300-28">Connecticut</p>
<p id="b300-29">Pre-Weeks: <em>State </em>v. <em>Griswold, </em><span class="citation" data-id="6583651"><a href="/opinion/6703553/state-v-griswold/" aria-description="Citation for case: State v. Griswold">67 Conn. 290</a></span>, <span class="citation" data-id="6583651"><a href="/opinion/6703553/state-v-griswold/" aria-description="Citation for case: State v. Griswold">34 A. 1046</a></span> (admissible) .</p>
<p id="b300-30">Pre-Wolf: <em>State </em>v. <em>Reynolds, </em><span class="citation" data-id="3321660"><a href="/opinion/3326264/state-v-reynolds/" aria-description="Citation for case: State v. Reynolds">101 Conn. 224</a></span>, <span class="citation" data-id="3321660"><a href="/opinion/3326264/state-v-reynolds/" aria-description="Citation for case: State v. Reynolds">125 A. 636</a></span> (admissible) .</p>
<p id="b300-31">Post-Wolf: no holding.</p>
<p id="b300-32">Delaware</p>
<p id="b300-33">Pre-Weeks: no holding.</p>
<p id="b300-34">Pre-Wolf: <em>State </em>v. <em>Chuchola, </em><span class="citation" data-id="6556679"><a href="/opinion/6677615/state-v-chuchola/" aria-description="Citation for case: State v. Chuchola">32 Del. 133</a></span>, <span class="citation" data-id="6556679"><a href="/opinion/6677615/state-v-chuchola/" aria-description="Citation for case: State v. Chuchola">120 A. 212</a></span> (admissible).</p>
<p id="b300-35">Post-Wolf: <em>Rickards </em>v. <em>State, </em><span class="citation" data-id="9757678"><a href="/opinion/2352643/rickards-v-state/" aria-description="Citation for case: Rickards v. State">45 Del. 573</a></span>, <span class="citation" data-id="9757678"><a href="/opinion/2352643/rickards-v-state/" aria-description="Citation for case: Rickards v. State">77 A. 2d 199</a></span> (excludable) .</p>
<p id="b301-5"><page-number citation-index="1" label="227">*227</page-number>Florida</p>
<p id="AxT">Pre-Weeks: no holding.</p>
<p id="AR">Pre-Wolf: <em>Atz </em>v. <em>Andrews, </em><span class="citation" data-id="4921024"><a href="/opinion/5103176/atz-v-andrews/" aria-description="Citation for case: Atz v. Andrews">84 Fla. 43</a></span>, <span class="citation" data-id="4921024"><a href="/opinion/5103176/atz-v-andrews/" aria-description="Citation for case: Atz v. Andrews">94 So. 329</a></span> (excludable).</p>
<p id="A7C">Post-Wolf: <em>Byrd </em>v. <em>State, </em><span class="citation" data-id="1837215"><a href="/opinion/1837215/byrd-v-state/" aria-description="Citation for case: Byrd v. State">80 So. 2d 694</a></span> (Sup. Ct. Florida) (excludable).</p>
<p id="Atl">Georgia</p>
<p id="A6Y">Pre-Weeks: <em>Williams </em>v. <em>State, </em><span class="citation" data-id="5567449"><a href="/opinion/5717379/williams-v-state/" aria-description="Citation for case: Williams v. State">100 Ga. 511</a></span>, <span class="citation" data-id="5567449"><a href="/opinion/5717379/williams-v-state/" aria-description="Citation for case: Williams v. State">28 S. E. 624</a></span> (admissible) .</p>
<p id="ANs">Pre-Wolf: <em>Jackson </em>v. <em>State, </em><span class="citation" data-id="5584660"><a href="/opinion/5734032/jackson-v-state/" aria-description="Citation for case: Jackson v. State">156 Ga. 647</a></span>, <span class="citation" data-id="5584660"><a href="/opinion/5734032/jackson-v-state/" aria-description="Citation for case: Jackson v. State">119 S. E. 525</a></span> (admissible) .</p>
<p id="AaQ">Post-Wolf: <em>Atterberry </em>v. <em>State, </em><span class="citation" data-id="1209203"><a href="/opinion/1209203/atterberry-v-state/" aria-description="Citation for case: Atterberry v. State">212 Ga. 778</a></span>, <span class="citation no-link">95 S. E. 2d 787</span> (admissible).</p>
<p id="AhG">Idaho</p>
<p id="AR4">Pre-Weeks: <em>State </em>v. <em>Bond, </em><span class="citation" data-id="5169254"><a href="/opinion/5337571/state-v-bond/" aria-description="Citation for case: State v. Bond">12 Idaho 424</a></span>, <span class="citation" data-id="5169254"><a href="/opinion/5337571/state-v-bond/" aria-description="Citation for case: State v. Bond">86 P. 43</a></span> (admissible).</p>
<p id="AGk">Pre-Wolf: <em>State </em>v. <em>Arregui, </em><span class="citation" data-id="3412636"><a href="/opinion/3416496/state-v-arregui/" aria-description="Citation for case: State v. Arregui">44 Idaho 43</a></span>, <span class="citation" data-id="3412636"><a href="/opinion/3416496/state-v-arregui/" aria-description="Citation for case: State v. Arregui">254 P. 788</a></span> (excludable.)</p>
<p id="Ac1">Post-Wolf: no holding.</p>
<p id="AeLy">Illinois</p>
<p id="AsJ">Pre-Weeks: <em>Siebert </em>v. <em>People, </em><span class="citation" data-id="6965240"><a href="/opinion/7061242/siebert-v-people/" aria-description="Citation for case: Siebert v. People">143 Ill. 571</a></span>, <span class="citation" data-id="6965240"><a href="/opinion/7061242/siebert-v-people/" aria-description="Citation for case: Siebert v. People">32 N. E. 431</a></span> (admissible).</p>
<p id="Aux">Pre-Wolf: <em>People </em>v. <em>Castree, </em><span class="citation" data-id="6981353"><a href="/opinion/7076578/people-v-castree/" aria-description="Citation for case: People v. Castree">311 Ill. 392</a></span>, <span class="citation" data-id="6981353"><a href="/opinion/7076578/people-v-castree/" aria-description="Citation for case: People v. Castree">143 N. E. 112</a></span> (excludable) .</p>
<p id="AD5H">Post-Wolf: <em>City of Chicago </em>v. Lord, <span class="citation" data-id="2030212"><a href="/opinion/2030212/city-of-chicago-v-lord/" aria-description="Citation for case: City of Chicago v. Lord">7 Ill. 2d 379</a></span>, <span class="citation" data-id="2030212"><a href="/opinion/2030212/city-of-chicago-v-lord/" aria-description="Citation for case: City of Chicago v. Lord">130 N. E. 2d 504</a></span> (excludable).</p>
<p id="Av2">Indiana</p>
<p id="ALv">Pre-Weeks: no holding.</p>
<p id="AKW">Pre-Wolf: <em>Flum </em>v. <em>State, </em><span class="citation" data-id="7057995"><a href="/opinion/7149435/flum-v-state/" aria-description="Citation for case: Flum v. State">193 Ind. 585</a></span>, <span class="citation" data-id="7057995"><a href="/opinion/7149435/flum-v-state/" aria-description="Citation for case: Flum v. State">141 N. E. 353</a></span> (excludable).</p>
<p id="ASJ">Post-Wolf: <em>Rohlfing </em>v. <em>State, </em><span class="citation" data-id="9523527"><a href="/opinion/2030951/rohlfing-v-state/" aria-description="Citation for case: Rohlfing v. State">230 Ind. 236</a></span>, <span class="citation" data-id="9523527"><a href="/opinion/2030951/rohlfing-v-state/" aria-description="Citation for case: Rohlfing v. State">102 N. E. 2d 199</a></span> (excludable) .</p>
<p id="Ash">Iowa</p>
<p id="AV8">Pre-Weeks: <em>State </em>v. <em>Sheridan, </em><span class="citation" data-id="7110547"><a href="/opinion/7199309/state-v-sheridan/" aria-description="Citation for case: State v. Sheridan">121 Iowa 164</a></span>, <span class="citation" data-id="7110547"><a href="/opinion/7199309/state-v-sheridan/" aria-description="Citation for case: State v. Sheridan">96 N. W. 730</a></span> (excludable) .</p>
<p id="ADP">Pre-Wolf: <em>State </em>v. <em>Rowley, </em><span class="citation" data-id="7120701"><a href="/opinion/7208995/state-v-rowley/" aria-description="Citation for case: State v. Rowley">197 Iowa 977</a></span>, <span class="citation no-link">195 N. W. 881</span> (admissible) .</p>
<p id="ASf">Post-Wolf: <em>State </em>v. <em>Smith, </em><span class="citation" data-id="2190973"><a href="/opinion/2190973/state-v-smith/" aria-description="Citation for case: State v. Smith">247 Iowa 500</a></span>, <span class="citation" data-id="2190973"><a href="/opinion/2190973/state-v-smith/" aria-description="Citation for case: State v. Smith">73 N. W. 2d 189</a></span> (admissible) .</p>
<p id="AE1Z">Kansas</p>
<p id="Aic">Pre-Weeks: <em>State </em>v. <em>Miller, </em><span class="citation" data-id="7891978"><a href="/opinion/7941374/state-v-miller/" aria-description="Citation for case: State v. Miller">63 Kan. 62</a></span>, <span class="citation" data-id="7891978"><a href="/opinion/7941374/state-v-miller/" aria-description="Citation for case: State v. Miller">64 P. 1033</a></span> (admissible).</p>
<p id="ApS">Pre-Wolf: <em>State </em>v. <em>Johnson, </em><span class="citation" data-id="7907024"><a href="/opinion/7955587/state-v-johnson/" aria-description="Citation for case: State v. Johnson">116 Kan. 58</a></span>, <span class="citation" data-id="7907024"><a href="/opinion/7955587/state-v-johnson/" aria-description="Citation for case: State v. Johnson">226 P. 245</a></span> (admissible).</p>
<p id="Aqo">Post-Wolf: <em>State </em>v. <em>Peasley, </em><span class="citation" data-id="1122381"><a href="/opinion/1122381/state-v-peasley/" aria-description="Citation for case: State v. Peasley">179 Kan. 314</a></span>, <span class="citation" data-id="1122381"><a href="/opinion/1122381/state-v-peasley/" aria-description="Citation for case: State v. Peasley">295 P. 2d 627</a></span> (admissible) :</p>
<p id="AOms">Kentucky</p>
<p id="AmZ">Pre-Weeks: no holding.</p>
<p id="AKM">Pre-Wolf: <em>Youman v. Commonwealth, </em><span class="citation" data-id="7146240"><a href="/opinion/7233831/youman-v-commonwealth/" aria-description="Citation for case: Youman v. Commonwealth">189 Ky. 152</a></span>, <span class="citation" data-id="7146240"><a href="/opinion/7233831/youman-v-commonwealth/" aria-description="Citation for case: Youman v. Commonwealth">224 S. W. 860</a></span> (excludable).</p>
<p id="AqA"><page-number citation-index="1" label="228">*228</page-number>Post-Wolf: <em>Johnson </em>v. <em>Commonwealth, </em><span class="citation" data-id="5021031"><a href="/opinion/5198082/johnson-v-commonwealth/" aria-description="Citation for case: Johnson v. Commonwealth">296 S. W. 2d 210</a></span> (Ct. App. Kentucky) (excludable).</p>
<p id="AKP">Louisiana</p>
<p id="ARs">Pre-Weeks: no holding.</p>
<p id="A8q">Pre-Wolf: <em>State </em>v. <em>Fleckinger, </em><span class="citation no-link">162 La. 337</span>, <span class="citation" data-id="7172750"><a href="/opinion/7258573/state-v-fleckinger/" aria-description="Citation for case: State v. Fleckinger">93 So. 115</a></span> (admissible).</p>
<p id="A0Z">Post-Wolf: <em>State </em>v. <em>Mastricovo, </em><span class="citation" data-id="1660499"><a href="/opinion/1660499/state-v-mastricovo/" aria-description="Citation for case: State v. Mastricovo">221 La. 312</a></span>, <span class="citation" data-id="1660499"><a href="/opinion/1660499/state-v-mastricovo/" aria-description="Citation for case: State v. Mastricovo">59 So. 2d 403</a></span> (admissible) .</p>
<p id="ATk">Maine</p>
<p id="AHE">Pre-Weeks: <em>State </em>v. <em>Gorham, </em><span class="citation" data-id="4932917"><a href="/opinion/5114261/state-v-gorham/" aria-description="Citation for case: State v. Gorham">65 Me. 270</a></span> (admissible) (semble).</p>
<p id="AuxD">Pre-Wolf: <em>State </em>v. <em>Schoppe, </em><span class="citation" data-id="4938095"><a href="/opinion/5119383/state-v-schoppe/" aria-description="Citation for case: State v. Schoppe">113 Me. 10</a></span>, <span class="citation" data-id="4938095"><a href="/opinion/5119383/state-v-schoppe/" aria-description="Citation for case: State v. Schoppe">92 A. 867</a></span> (admissible) <em>(semble),</em></p>
<p id="ApT">Post-Wolf: <em>no </em>holding.</p>
<p id="Ag9">MARYLAND</p>
<p id="AZq">Pre-Weeks: <em>Lawrence </em>v. <em>State, </em><span class="citation" data-id="3487094"><a href="/opinion/3489145/lawrence-v-state/" aria-description="Citation for case: Lawrence v. State">103 Md. 17</a></span>, <span class="citation" data-id="3487094"><a href="/opinion/3489145/lawrence-v-state/" aria-description="Citation for case: Lawrence v. State">63 A. 96</a></span> (admissible).</p>
<p id="Az4">Pre-Wolf: <em>Meisinger </em>v. <em>State, </em><span class="citation" data-id="3484807"><a href="/opinion/3486914/meisinger-v-state/" aria-description="Citation for case: Meisinger v. State">155 Md. 195</a></span>, <span class="citation" data-id="3484807"><a href="/opinion/3486914/meisinger-v-state/" aria-description="Citation for case: Meisinger v. State">141 A. 536</a></span> (admissible) .</p>
<p id="AGnC">Post-Wolf: <em>Stevens </em>v. <em>State, </em><span class="citation" data-id="1921065"><a href="/opinion/1921065/stevens-v-state/" aria-description="Citation for case: Stevens v. State">202 Md. 117</a></span>, <span class="citation" data-id="1921065"><a href="/opinion/1921065/stevens-v-state/" aria-description="Citation for case: Stevens v. State">95 A. 2d 877</a></span> (admissible). (Flack’s Md. Ann. Code, 1951, Art. 35, § 5 requires the exclusion of illegally obtained evidence in the trial of most misdemeanors.)</p>
<p id="Aaa">Massachusetts</p>
<p id="AWR">Pre-Weeks: <em>Commonwealth </em>v. <em>Dana, </em><span class="citation" data-id="6407794"><a href="/opinion/6534076/commonwealth-v-dana/" aria-description="Citation for case: Commonwealth v. Dana">43 Mass. 329</a></span> (admissible).</p>
<p id="A6P">Pre-Wolf: <em>Commonwealths. Wilkins, </em><span class="citation" data-id="6436025"><a href="/opinion/6562275/commonwealth-v-wilkins/" aria-description="Citation for case: Commonwealth v. Wilkins">243 Mass. 356</a></span>, <span class="citation no-link">138 N. E. 11</span> (admissible).</p>
<p id="As2">Post-Wolf: no holding.</p>
<p id="Av5">Michigan</p>
<p id="AzD">Pre-Weeks: <em>People </em>v. <em>Aldorfer, </em><span class="citation" data-id="7946344"><a href="/opinion/7992842/people-v-aldorfer/" aria-description="Citation for case: People v. Aldorfer">164 Mich. 676</a></span>, <span class="citation" data-id="7946344"><a href="/opinion/7992842/people-v-aldorfer/" aria-description="Citation for case: People v. Aldorfer">130 N. W. 351</a></span> (admissible).</p>
<p id="A2T">Pre-Wolf: <em>People </em>v. <em>Marxhausen, </em><span class="citation" data-id="7950359"><a href="/opinion/7996598/people-v-marxhausen/" aria-description="Citation for case: People v. Marxhausen">204 Mich. 559</a></span>, <span class="citation" data-id="7950359"><a href="/opinion/7996598/people-v-marxhausen/" aria-description="Citation for case: People v. Marxhausen">171 N. W. 557</a></span> (excludable).</p>
<p id="AZL">Post-Wolf: <em>People </em>v. <em>Hildabridle, </em><span class="citation" data-id="9527923"><a href="/opinion/2041058/people-v-hildabridle/" aria-description="Citation for case: People v. Hildabridle">353 Mich. 562</a></span>, <span class="citation" data-id="9527923"><a href="/opinion/2041058/people-v-hildabridle/" aria-description="Citation for case: People v. Hildabridle">92 N. W. 2d 6</a></span> (excludable).</p>
<p id="AUa">(Art. II, § 10 of the Michigan Constitution of 1908, as amended, sets forth a limited class of items which are not excludable. See <em>People </em>v. <em>Gonzales, </em><span class="citation" data-id="9741641"><a href="/opinion/2228330/people-v-gonzales/" aria-description="Citation for case: People v. Gonzales">356 Mich. 247</a></span>, 97 N.- W. 2d 16.)</p>
<p id="A-b">Minnesota</p>
<p id="Ar0">Pre-Weeks: <em>State </em>v. <em>Strait, </em><span class="citation" data-id="7973247"><a href="/opinion/8017916/state-v-strait/" aria-description="Citation for case: State v. Strait">94 Minn. 384</a></span>, <span class="citation" data-id="7973247"><a href="/opinion/8017916/state-v-strait/" aria-description="Citation for case: State v. Strait">102 N. W. 913</a></span> (admissible).</p>
<p id="A_m">Pre-Wolf: <em>State </em>v. <em>Pluth, </em><span class="citation" data-id="7981382"><a href="/opinion/8025591/state-v-pluth/" aria-description="Citation for case: State v. Pluth">157 Minn. 145</a></span>, <span class="citation" data-id="7981382"><a href="/opinion/8025591/state-v-pluth/" aria-description="Citation for case: State v. Pluth">195 N. W. 789</a></span> (admissible).</p>
<p id="AAR">Post-Wolf: no holding.</p>
<p id="b303-5"><page-number citation-index="1" label="229">*229</page-number>Mississippi</p>
<p id="b303-6">Pre-Weeks: no holding.</p>
<p id="b303-7">Pre-Wolf: <em>Tucker </em>v. <em>State, </em><span class="citation" data-id="7994199"><a href="/opinion/8037845/tucker-v-state/" aria-description="Citation for case: Tucker v. State">128 Miss. 211</a></span>, <span class="citation" data-id="7994199"><a href="/opinion/8037845/tucker-v-state/" aria-description="Citation for case: Tucker v. State">90 So. 845</a></span> (excludable).</p>
<p id="b303-8">Post-Wolf: <em>Nobles </em>v. <em>State, </em><span class="citation" data-id="7996204"><a href="/opinion/8039738/nobles-v-state/" aria-description="Citation for case: Nobles v. State">222 Miss. 827</a></span>, <span class="citation" data-id="7996204"><a href="/opinion/8039738/nobles-v-state/" aria-description="Citation for case: Nobles v. State">77 So. 2d 288</a></span> (excludable) .</p>
<p id="b303-9">Missouri</p>
<p id="b303-10">Pre-Weeks: <em>State </em>v. <em>Pomeroy, </em><span class="citation" data-id="8011909"><a href="/opinion/8054876/state-v-pomeroy/" aria-description="Citation for case: State v. Pomeroy">130 Mo. 489</a></span>, <span class="citation" data-id="8011909"><a href="/opinion/8054876/state-v-pomeroy/" aria-description="Citation for case: State v. Pomeroy">32 S. W. 1002</a></span> (admissible) .</p>
<p id="b303-11">Pre-Wolf: <em>State </em>v. <em>Owens, </em><span class="citation" data-id="3529427"><a href="/opinion/3553710/state-v-owens/" aria-description="Citation for case: State v. Owens">302 Mo. 348</a></span>, <span class="citation" data-id="3529427"><a href="/opinion/3553710/state-v-owens/" aria-description="Citation for case: State v. Owens">259 S. W. 100</a></span> (excludable) .</p>
<p id="b303-12">Post-Wolf: <em>State </em>v. <em>Hunt, </em><span class="citation" data-id="2466177"><a href="/opinion/2466177/state-v-hunt/" aria-description="Citation for case: State v. Hunt">280 S. W. 2d 37</a></span> (Sup. Ct. Missouri) (excludable).</p>
<p id="b303-13">Montana</p>
<p id="b303-14">Pre-Weeks: <em>State </em>v. <em>Fuller, </em><span class="citation" data-id="8020864"><a href="/opinion/8063090/state-v-fuller/" aria-description="Citation for case: State v. Fuller">34 Mont. 12</a></span>, <span class="citation" data-id="8020864"><a href="/opinion/8063090/state-v-fuller/" aria-description="Citation for case: State v. Fuller">85 P. 369</a></span> (admissible).</p>
<p id="b303-15">Pre-Wolf: <em>State ex rel. King </em>v. <em>District Court, </em><span class="citation" data-id="8024014"><a href="/opinion/8066072/state-ex-rel-king-v-district-court/" aria-description="Citation for case: State ex rel. King v. District Court">70 Mont. 191</a></span>, <span class="citation" data-id="8024014"><a href="/opinion/8066072/state-ex-rel-king-v-district-court/" aria-description="Citation for case: State ex rel. King v. District Court">224 P. 862</a></span> (excludable).</p>
<p id="b303-16">Post-Wolf: no holding.</p>
<p id="b303-17">Nebraska</p>
<p id="b303-18">Pre-Weeks: <em>Geiger </em>v. <em>State, </em><span class="citation" data-id="6642402"><a href="/opinion/6759719/geiger-v-state/" aria-description="Citation for case: Geiger v. State">6 Neb. 545</a></span> (admissible).</p>
<p id="b303-19">Pre-Wolf: <em>Billings </em>v. <em>State, </em><span class="citation" data-id="8032854"><a href="/opinion/8074092/billings-v-state/" aria-description="Citation for case: Billings v. State">109 Neb. 596</a></span>, <span class="citation" data-id="8032854"><a href="/opinion/8074092/billings-v-state/" aria-description="Citation for case: Billings v. State">191 N. W. 721</a></span> (admissible) .</p>
<p id="b303-20">Post-Wolf: <em>Haswell </em>v. <em>State, </em><span class="citation" data-id="2041065"><a href="/opinion/2041065/haswell-v-state/" aria-description="Citation for case: Haswell v. State">167 Neb. 169</a></span>, <span class="citation" data-id="2041065"><a href="/opinion/2041065/haswell-v-state/" aria-description="Citation for case: Haswell v. State">92 N. W. 2d 161</a></span> (admissible).</p>
<p id="b303-21">Nevada</p>
<p id="b303-22">Pre-Weeks:- no holding.</p>
<p id="b303-23">Pre-Wolf: <em>State </em>v. <em>Chin Gim, </em><span class="citation" data-id="8042834"><a href="/opinion/8083180/state-v-chin-gim/" aria-description="Citation for case: State v. Chin Gim">47 Nev. 431</a></span>, <span class="citation" data-id="8042834"><a href="/opinion/8083180/state-v-chin-gim/" aria-description="Citation for case: State v. Chin Gim">224 P. 798</a></span> (admissible) .</p>
<p id="b303-24">Post-Wolf: no holding.</p>
<p id="b303-25">New Hampshire</p>
<p id="b303-26">Pre-Weeks: <em>State </em>v. <em>Flynn, </em>36 N. H. 64 (admissible).</p>
<p id="b303-27">Pre-Wolf: <em>State </em>v. <em>Agalos, </em>79 N. H. 241, <span class="citation" data-id="3553875"><a href="/opinion/3573624/state-v-agalos/" aria-description="Citation for case: State v. Agalos">107 A. 314</a></span> (admissible) .</p>
<p id="b303-28">Post-Wolf: <em>State </em>v. <em>Mara, </em>96 N. H. 463, <span class="citation" data-id="2302903"><a href="/opinion/2302903/state-v-mara/" aria-description="Citation for case: State v. Mara">78 A. 2d 922</a></span> (admissible) .</p>
<p id="b303-29">New Jersey</p>
<p id="b303-30">Pre-Weeks: no holding</p>
<p id="b303-31">Pre-Wolf: <em>State </em>v. <em>Black, </em>5 N. J. Misc. 48, <span class="citation" data-id="8506298"><a href="/opinion/8533787/state-v-black/" aria-description="Citation for case: State v. Black">135 A. 685</a></span> (admissible) .</p>
<p id="b303-32">Post-Wolf: <em>Eleuteri </em>v. <em>Richman, </em>26 N. J. 506, <span class="citation" data-id="1934063"><a href="/opinion/1934063/eleuteri-v-richman/" aria-description="Citation for case: Eleuteri v. Richman">141 A. 2d 46</a></span> (admissible).</p>
<p id="b303-33">(N. J. Rev. Stat. 33:1-62 provides for the return of items illegally seized in the investigation of certain alcohol control offenses.)</p>
<p id="b304-4"><page-number citation-index="1" label="230">*230</page-number>New Mexico</p>
<p id="b304-5">Pre-Weeks: no holding.</p>
<p id="b304-6">Pre-Wolf: <em>State </em>v. <em>Dillon, </em>34 N. M. 366, <span class="citation" data-id="3571966"><a href="/opinion/3591159/state-v-dillon/" aria-description="Citation for case: State v. Dillon">281 P. 474</a></span> (admissible) .</p>
<p id="b304-7">Post-Wolf: <em>Breithaupt </em>v. <em>Abram, </em>58 N. M. 385, <span class="citation" data-id="6469115"><a href="/opinion/6594277/breithaupt-v-abram/" aria-description="Citation for case: Breithaupt v. Abram">271 P. 2d 827</a></span> (admissible).</p>
<p id="b304-8">New Yoke</p>
<p id="b304-9">Pre-Weeks: <em>People </em>v. <em>Adams, </em><span class="citation" data-id="5650086"><a href="/opinion/5795142/people-v-adams/" aria-description="Citation for case: People v. Adams">176 N. Y. 351</a></span>, <span class="citation" data-id="3588018"><a href="/opinion/3606309/people-v-adams/" aria-description="Citation for case: People v. . Adams">68 N. E. 636</a></span> (admissible) .</p>
<p id="b304-10">Pre-Wolf: <em>People </em>v. <em>Defore, </em><span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">242 N. Y. 13</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">150 N. E. 585</a></span> (admissible).</p>
<p id="b304-11">Post-Wolf: <em>People </em>v. <em>Variano, </em>5 N. Y. 2d 391, <span class="citation" data-id="5517425"><a href="/opinion/5670276/people-v-variano/" aria-description="Citation for case: People v. Variano">157 N. E. 2d 857</a></span> (admissible).</p>
<p id="b304-12">North Carolina</p>
<p id="b304-13">Pre-Weeks: <em>State </em>v. <em>Wallace, </em><span class="citation" data-id="6695783"><a href="/opinion/6809677/state-v-wallace/" aria-description="Citation for case: State v. Wallace">162 N. C. 622</a></span>, <span class="citation" data-id="3672959"><a href="/opinion/3926369/s-v-wallace/" aria-description="Citation for case: S. v. . Wallace">78 S. E. 1</a></span> (admissible).</p>
<p id="b304-14">Pre-Wolf: <em>State </em>v. <em>Simmons, </em><span class="citation" data-id="3646527"><a href="/opinion/3900534/state-v-simmons/" aria-description="Citation for case: State v. . Simmons">183 N. C. 684</a></span>, <span class="citation" data-id="3646527"><a href="/opinion/3900534/state-v-simmons/" aria-description="Citation for case: State v. . Simmons">110 S. E. 591</a></span> (admissible).</p>
<p id="b304-15">Post-Wolf: <em>State </em>v. <em>Mills, </em><span class="citation" data-id="1328981"><a href="/opinion/1328981/state-v-mills/" aria-description="Citation for case: State v. Mills">246 N. C. 237</a></span>, <span class="citation" data-id="1328981"><a href="/opinion/1328981/state-v-mills/" aria-description="Citation for case: State v. Mills">98 S. E. 2d 329</a></span> (excludable) .</p>
<p id="b304-16">(N. C. Gen. Stat. § 15-27 requires the exclusion of illegally obtained evidence.)</p>
<p id="b304-17">North Dakota</p>
<p id="b304-18">Pre-Weeks: no holding.</p>
<p id="b304-19">Pre-Wolf: <em>State </em>v. <em>Fahn, </em><span class="citation" data-id="3682031"><a href="/opinion/3934924/state-v-fahn/" aria-description="Citation for case: State v. Fahn">53 N. D. 203</a></span>, <span class="citation" data-id="3682031"><a href="/opinion/3934924/state-v-fahn/" aria-description="Citation for case: State v. Fahn">205 N. W. 67</a></span> (admissible).</p>
<p id="b304-20">Post-Wolf: no holding.</p>
<p id="b304-21">Ohio</p>
<p id="b304-22">Pre-Weeks: no holding.</p>
<p id="b304-23">Pre-Wolf: <em>State </em>v. <em>Lindway, </em><span class="citation" data-id="3780866"><a href="/opinion/4024496/state-v-lindway/" aria-description="Citation for case: State v. Lindway">131 Ohio St. 166</a></span>, <span class="citation" data-id="3780866"><a href="/opinion/4024496/state-v-lindway/" aria-description="Citation for case: State v. Lindway">2 N. E. 2d 490</a></span> (admissible).</p>
<p id="b304-24">Post-Wolf: <em>State </em>v. <em>Mapp, </em><span class="citation no-link">170 Ohio St. 427</span>, <span class="citation no-link">166 N. E. 2d 387</span> (admissible).</p>
<p id="b304-25">Oklahoma</p>
<p id="b304-26">Pre-Weeks: <em>Silva </em>v. <em>State, </em><span class="citation" data-id="3827556"><a href="/opinion/4069690/silva-v-state/" aria-description="Citation for case: Silva v. State">6 Okla. Cr. 97</a></span>, <span class="citation" data-id="3827556"><a href="/opinion/4069690/silva-v-state/" aria-description="Citation for case: Silva v. State">116 P. 199</a></span> (admissible).</p>
<p id="b304-27">Pre-Wolf: <em>Gore </em>v. <em>State, </em><span class="citation" data-id="3812264"><a href="/opinion/4054922/gore-v-state/" aria-description="Citation for case: Gore v. State">24 Okla. Cr. 394</a></span>, <span class="citation" data-id="3812264"><a href="/opinion/4054922/gore-v-state/" aria-description="Citation for case: Gore v. State">218 P. 545</a></span> (excludable) .</p>
<p id="b304-28">Post-Wolf: <em>Hamel </em>v. <em>State, </em><span class="citation" data-id="2619395"><a href="/opinion/2619395/hamel-v-state/" aria-description="Citation for case: Hamel v. State">317 P. 2d 285</a></span> (Okla. Crim.) (ex-cludable) .</p>
<p id="b304-29">Oregon</p>
<p id="b304-30">Pre-Weeks: <em>State </em>v. <em>McDaniel, </em><span class="citation" data-id="6898602"><a href="/opinion/6999518/state-v-mcdaniel/" aria-description="Citation for case: State v. McDaniel">39 Ore. 161</a></span>, <span class="citation" data-id="6898602"><a href="/opinion/6999518/state-v-mcdaniel/" aria-description="Citation for case: State v. McDaniel">65 P. 520</a></span> (admissible).</p>
<p id="b304-31">Pre-Wolf: See <em>State </em>v. <em>Laundy, </em><span class="citation" data-id="6907613"><a href="/opinion/7007488/state-v-laundy/" aria-description="Citation for case: State v. Laundy">103 Ore. 443</a></span>, <span class="citation" data-id="6907613"><a href="/opinion/7007488/state-v-laundy/" aria-description="Citation for case: State v. Laundy">204 P. 958</a></span> (excludable), although see <em>State </em>v. <em>Folkes, </em><span class="citation" data-id="3842073"><a href="/opinion/4083033/state-v-folkes/" aria-description="Citation for case: State v. Folkes">174 Ore. 568</a></span>, <span class="citation" data-id="3842073"><a href="/opinion/4083033/state-v-folkes/" aria-description="Citation for case: State v. Folkes">150 P. 2d 17</a></span> (not noticing <em>State v. Laundy).</em></p>
<p id="b304-32">Post-Wolf: <em>State </em>v. <em>Hoover, </em><span class="citation" data-id="2615411"><a href="/opinion/2615411/state-v-hoover/" aria-description="Citation for case: State v. Hoover">219 Ore. 288</a></span>, <span class="citation" data-id="2615411"><a href="/opinion/2615411/state-v-hoover/" aria-description="Citation for case: State v. Hoover">347 P. 2d 69</a></span> (questioning <em>Laundy).</em></p>
<p id="b305-5"><page-number citation-index="1" label="231">*231</page-number>Pennsylvania</p>
<p id="b305-6">Pre-Weeks: no holding.</p>
<p id="b305-7">Pre-Wolf: <em>Commonwealth </em>v. <em>Dabbierio, </em><span class="citation" data-id="3848320"><a href="/opinion/4089084/commonwealth-v-dabbierio/" aria-description="Citation for case: Commonwealth v. Dabbierio">290 Pa. 174</a></span>, <span class="citation" data-id="3848320"><a href="/opinion/4089084/commonwealth-v-dabbierio/" aria-description="Citation for case: Commonwealth v. Dabbierio">138 A. 679</a></span> (admissible).</p>
<p id="b305-8">Post-Wolf: <em>Commonwealth </em>v. <em>Chaitt, </em><span class="citation" data-id="9735584"><a href="/opinion/2199709/commonwealth-v-chaitt/" aria-description="Citation for case: Commonwealth v. Chaitt">380 Pa. 532</a></span>, <span class="citation" data-id="9735584"><a href="/opinion/2199709/commonwealth-v-chaitt/" aria-description="Citation for case: Commonwealth v. Chaitt">112 A. 2d 379</a></span> (admissible).</p>
<p id="b305-9">Rhode Island</p>
<p id="b305-10">Pre-Weeks: no holding.</p>
<p id="b305-11">Pre-Wolf: no holding.</p>
<p id="b305-12">Post-Wolf: <em>State </em>v. <em>Hillman, </em>84 R. I. 396, <span class="citation" data-id="1493506"><a href="/opinion/1493506/state-v-hillman/" aria-description="Citation for case: State v. Hillman">125 A. 2d 94</a></span> (applying common law rule, but noticing the enactment of the statutory rule).</p>
<p id="b305-13">(R. I. Gen. Laws, 1956, § 9-19-25 requires the exclusion of illegally obtained evidence.)</p>
<p id="b305-14">South Carolina</p>
<p id="b305-15">Pre-Weeks: <em>State </em>v. <em>Atkinson, </em>40 S. C. 363, <span class="citation" data-id="6678093"><a href="/opinion/6793472/state-v-atkinson/" aria-description="Citation for case: State v. Atkinson">18 S. E. 1021</a></span> (admissible) .</p>
<p id="b305-16">Pre-Wolf: <em>State </em>v. <em>Green, </em>121 S. C. 230, <span class="citation no-link">114 S. E. 317</span> (admissible) .</p>
<p id="b305-17">Post-Wolf: <em>State </em>v. <em>Anderson, </em>230 S. C. 191, <span class="citation" data-id="1380217"><a href="/opinion/1380217/state-v-anderson/" aria-description="Citation for case: State v. Anderson">95 S. E. 2d 164</a></span> (admissible).</p>
<p id="b305-18">South Dakota</p>
<p id="b305-19">Pre-Weeks: <em>State </em>v. <em>Madison, </em>23 S. D. 584, <span class="citation" data-id="6687221"><a href="/opinion/6802175/state-v-madison/" aria-description="Citation for case: State v. Madison">122 N. W. 647</a></span> (admissible) .</p>
<p id="b305-20">Pre-Wolf: <em>State </em>v. <em>Gooder, </em>57 S. D. 619, <span class="citation" data-id="6692555"><a href="/opinion/6806990/state-v-gooder/" aria-description="Citation for case: State v. Gooder">234 N. W. 610</a></span> (excludable) .</p>
<p id="b305-21">Post-Wolf: <em>State </em>v. <em>Poppenga, </em>76 S. D. 592, <span class="citation" data-id="1680451"><a href="/opinion/1680451/state-v-poppenga/" aria-description="Citation for case: State v. Poppenga">83 N. W. 2d 518</a></span> (excludable).</p>
<p id="b305-22">S. D. Code, 1939, § 34.1102 provides for a limited return to the common-law rule of admissibility. See <em>State </em>v. <em>Lane, </em>76 S. D. 544, 82 N. W. 2d. 286.</p>
<p id="b305-23">Tennessee</p>
<p id="b305-24">Pre-Weeks: <em>Cohn </em>v. <em>State, </em><span class="citation" data-id="8300564"><a href="/opinion/8332572/cohn-v-state/" aria-description="Citation for case: Cohn v. State">120 Tenn. 61</a></span>, <span class="citation" data-id="3980535"><a href="/opinion/4208407/parriss-v-hughes/" aria-description="Citation for case: Parriss v. Hughes">109 S. W. 1149</a></span> (admissible).</p>
<p id="b305-25">Pre-Wolf: <em>Hughes </em>v. <em>State, </em><span class="citation" data-id="8302107"><a href="/opinion/8334068/hughes-v-state/" aria-description="Citation for case: Hughes v. State">145 Tenn. 544</a></span>, <span class="citation no-link">238 S. W. 588</span> (excludable).</p>
<p id="b305-26">Post-Wolf: <em>Lindsey </em>v. <em>State, </em><span class="citation" data-id="8302925"><a href="/opinion/8334836/lindsey-v-state/" aria-description="Citation for case: Lindsey v. State">191 Tenn. 51</a></span>, <span class="citation" data-id="8302925"><a href="/opinion/8334836/lindsey-v-state/" aria-description="Citation for case: Lindsey v. State">231 S. W. 2d 380</a></span> (excludable).</p>
<p id="b305-27">Texas</p>
<p id="b305-28">Pre-Weeks: no holding.</p>
<p id="b305-29">Pre-Wolf: <em>Chapin </em>v. <em>State, </em><span class="citation" data-id="3948208"><a href="/opinion/4179831/chapin-v-state/" aria-description="Citation for case: Chapin v. State">107 Tex. Cr. R. 477</a></span>, <span class="citation" data-id="3948208"><a href="/opinion/4179831/chapin-v-state/" aria-description="Citation for case: Chapin v. State">296 S. W. 1095</a></span> (excludable).</p>
<p id="b306-5"><page-number citation-index="1" label="232">*232</page-number>Post-Wolf: <em>Williamson </em>v. <em>State, </em><span class="citation" data-id="1670307"><a href="/opinion/1670307/williamson-v-state/" aria-description="Citation for case: Williamson v. State">156 Tex. Cr. R. 520</a></span>, <span class="citation" data-id="1670307"><a href="/opinion/1670307/williamson-v-state/" aria-description="Citation for case: Williamson v. State">244 S. W. 2d 202</a></span> (excludable).</p>
<p id="b306-6">(Vernon’s Tex. Stat., 1948 (Code Crim. Proc., Art. 72a) requires the exclusion of illegally obtained evidence.)</p>
<p id="b306-7">Utah</p>
<p id="b306-8">Pre-Weeks: no holding.</p>
<p id="b306-9">Pre-Wolf: <em>State </em>v. <em>Aime, </em><span class="citation" data-id="8657438"><a href="/opinion/8674530/state-v-aime/" aria-description="Citation for case: State v. Aime">62 Utah 476</a></span>, <span class="citation" data-id="8657438"><a href="/opinion/8674530/state-v-aime/" aria-description="Citation for case: State v. Aime">220 P. 704</a></span> (admissible). Post-Wolf: no holding.</p>
<p id="b306-10">Vermont</p>
<p id="b306-11">Pre-Weeks: <em>State </em>v. <em>Mathers, </em><span class="citation" data-id="6583727"><a href="/opinion/6703627/state-v-mathers/" aria-description="Citation for case: State v. Mathers">64 Vt. 101</a></span>, <span class="citation no-link">23 A. 590</span> (admissible).</p>
<p id="AR3">Pre-Wolf: <em>State </em>v. <em>Stacy, </em><span class="citation" data-id="3990360"><a href="/opinion/4216163/state-v-stacy/" aria-description="Citation for case: State v. Stacy">104 Vt. 379</a></span>, <span class="citation no-link">160 A. 257</span> (admissible).</p>
<p id="ANu">Post-Wolf: <em>In re Raymo, </em><span class="citation" data-id="1505389"><a href="/opinion/1505389/in-re-raymos-petition/" aria-description="Citation for case: In Re Raymo&#x27;s Petition">121 Vt. 246</a></span>, <span class="citation" data-id="1505389"><a href="/opinion/1505389/in-re-raymos-petition/" aria-description="Citation for case: In Re Raymo&#x27;s Petition">154 A. 2d 487</a></span> (admissible).</p>
<p id="b306-12">Virginia</p>
<p id="b306-13">Pre-Weeks: no holding.</p>
<p id="b306-14">Pre-Wolf: <em>Hall v. Commonwealth, </em><span class="citation" data-id="6815460"><a href="/opinion/6919821/hall-v-commonwealth/" aria-description="Citation for case: Hall v. Commonwealth">138 Va. 727</a></span>, <span class="citation" data-id="6815460"><a href="/opinion/6919821/hall-v-commonwealth/" aria-description="Citation for case: Hall v. Commonwealth">121 S. E. 154</a></span> (admissible).</p>
<p id="b306-15">Post-Wolf: no holding.</p>
<p id="b306-16">Washington</p>
<p id="b306-17">Pre-Weeks: <em>State </em>v. <em>Royce, </em><span class="citation" data-id="4726508"><a href="/opinion/4919818/state-v-royce/" aria-description="Citation for case: State v. Royce">38 Wash. 111</a></span>, <span class="citation" data-id="4726508"><a href="/opinion/4919818/state-v-royce/" aria-description="Citation for case: State v. Royce">80 P. 268</a></span> (admissible).</p>
<p id="AmZF">Pre-Wolf: <em>State </em>v. <em>Gibbons, </em><span class="citation" data-id="4720844"><a href="/opinion/4914645/state-v-gibbons/" aria-description="Citation for case: State v. Gibbons">118 Wash. 171</a></span>, <span class="citation" data-id="4720844"><a href="/opinion/4914645/state-v-gibbons/" aria-description="Citation for case: State v. Gibbons">203 P. 390</a></span> (excludable) .</p>
<p id="b306-18">Post-Wolf: <em>State </em>v. <em>Cyr, </em><span class="citation" data-id="1178849"><a href="/opinion/1178849/state-v-cyr/" aria-description="Citation for case: State v. Cyr">40 Wash. 2d 840</a></span>, <span class="citation" data-id="1178849"><a href="/opinion/1178849/state-v-cyr/" aria-description="Citation for case: State v. Cyr">246 P. 2d 480</a></span> (excludable) .</p>
<p id="b306-19">West Virginia</p>
<p id="b306-20">Pre-Weeks: <em>State </em>v. <em>Edwards, </em><span class="citation" data-id="8175125"><a href="/opinion/8212628/state-v-edwards/" aria-description="Citation for case: State v. Edwards">51 W. Va. 220</a></span>, <span class="citation" data-id="8175125"><a href="/opinion/8212628/state-v-edwards/" aria-description="Citation for case: State v. Edwards">41 S. E. 429</a></span> (admissible).</p>
<p id="b306-21">Pre-Wolf: <em>State </em>v. <em>Wills, </em><span class="citation" data-id="8179537"><a href="/opinion/8216688/state-v-wills/" aria-description="Citation for case: State v. Wills">91 W. Va. 659</a></span>, <span class="citation" data-id="8179537"><a href="/opinion/8216688/state-v-wills/" aria-description="Citation for case: State v. Wills">114 S. E. 261</a></span> (excludable) .</p>
<p id="b306-22">Post-Wolf: <em>State </em>v. <em>Calandros, </em><span class="citation" data-id="9621257"><a href="/opinion/1401576/state-v-calandros/" aria-description="Citation for case: State v. Calandros">140 W. Va. 720</a></span>, <span class="citation" data-id="9621257"><a href="/opinion/1401576/state-v-calandros/" aria-description="Citation for case: State v. Calandros">86 S. E. 2d 242</a></span> (excludable).</p>
<p id="b306-23">Wisconsin</p>
<p id="b306-24">Pre-Weeks: no holding.</p>
<p id="b306-25">Pre-Wolf: <em>Hoyer </em>v. <em>State, </em><span class="citation" data-id="8194030"><a href="/opinion/8229755/hoyer-v-state/" aria-description="Citation for case: Hoyer v. State">180 Wis. 407</a></span>, <span class="citation" data-id="8194030"><a href="/opinion/8229755/hoyer-v-state/" aria-description="Citation for case: Hoyer v. State">193 N. W. 89</a></span> (excludable).</p>
<p id="A8H">Post-Wolf: <em>State </em>v. <em>Kroening, </em><span class="citation" data-id="9520934"><a href="/opinion/2022531/state-v-kroening/" aria-description="Citation for case: State v. Kroening">274 Wis. 266</a></span>, <span class="citation no-link">79 N. W. 2d 810</span> (excludable).</p>
<p id="b306-26">Wyoming</p>
<p id="b306-27">Pre-Weeks: no holding.</p>
<p id="b306-28">Pre-Wolf: <em>State </em>v. <em>George, </em><span class="citation" data-id="4012941"><a href="/opinion/4235695/state-v-george/" aria-description="Citation for case: State v. George">32 Wyo. 223</a></span>, <span class="citation" data-id="4012941"><a href="/opinion/4235695/state-v-george/" aria-description="Citation for case: State v. George">231 P. 683</a></span> (excludable).</p>
<p id="ANj">Post-Wolf: no holding.</p>
<footnote label="1">
<p id="b281-5"> The state officers, having received information that petitioners had in their possession obscene motion pictures, procured a search warrant to search petitioner Clark’s home. The affidavit upon which the warrant was based recited that “upon information and belief” it was thought that Clark possessed obscene pictures and accompanying sound recordings. The search revealed no obscene pictures, but various paraphernalia believed to have been used in making wiretaps were found and seized.</p>
<p id="b281-6">Following an appropriate motion, the Multnomah County District Court held the search warrant invalid and ordered suppression of the evidence. This action came, however, after the return of an indictment by a state grand jury, and the local district attorney challenged the power of the district court to suppress evidence once an indictment was in. Accordingly, the question was later argued anew on a motion to suppress in the Circuit Court for. Multnomah County, a court of general criminal jurisdiction. That court held the search unlawful and granted the motion to suppress. The state indictment was subsequently dismissed.</p>
<p id="b281-7">During the course of these state proceedings federal officers,- acting under a federal search warrant, obtained the articles from the safe-deposit box of a local bank where the state officials had placed them. Shortly after the state case was abandoned, a federal indictment was returned, and the instant prosecution followed.</p>
</footnote>
<footnote label="2">
<p id="b282-8"> The “silver platter” label stems from a phrase first turned in the prevailing opinion in <em>Lustig </em>v. <em>United States, </em><span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/#79" aria-description="Citation for case: Lustig v. United States">338 U. S. 74, 79</a></span>. The doctrine has been the subject of much comment in legal periodicals. See, <em>e.g., </em>Allen, The Wolf Casé: Search and Seizure, Federalism, and the Civil Liberties, 45 Ill. L. Rev. 1, 14-25; Galler, The Exclusion of Illegal State Evidence in Federal Courts, 49 J. Crim. L., Criminology <em>&amp; </em>Police Science 455; Kohn, Admissibility in Federal Court of Evidence Illegally Seized by State Officers, 1959 Wash. U. L. Q. 229; Kamisar, <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span> </em>and <em><span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/" aria-description="Citation for case: Lustig v. United States">Lustig</a></span> </em>Ten Years Later: Illegal State Evidence in State and Federal Courts, <span class="citation no-link">43 Minn. L. Rev. 1083</span>; Parsons, State-Federal Crossfire in Search and Seizure and Self Incrimination, 42 Cornell L. Q. 346, 347-368; Comment, The <em>Benanti </em>Case: State Wiretap Evidence and the Federal Exclusionary Rule, 57 Col. L. Rev. 1159; Comment, Judicial Control of Illegal Search and Seizure, 58 Yale L. J. 144; Notes, 51 Col. L. Rev. 128, <span class="citation no-link">27 Geo. Wash. L. Rev. 392</span>. 5 N. Y. L. F. 301. 6 U. C. L. A. Rev. 703.</p>
</footnote>
<footnote label="3">
<p id="b284-8"> See, <em>e. g., Rettich </em>v. <em>United States, </em><span class="citation" data-id="1489412"><a href="/opinion/1489412/rettich-v-united-states/" aria-description="Citation for case: Rettich v. United States">84 F. 2d 118</a></span> (C. A. 1st Cir.); <em>Milburne </em>v. <em>United States, </em><span class="citation" data-id="6863032"><a href="/opinion/6965605/milburne-v-united-states/" aria-description="Citation for case: Milburne v. United States">77 F. 2d 310</a></span> (C. A. 2d Cir.); <em>Miller </em>v. <em>United States, </em><span class="citation" data-id="1549055"><a href="/opinion/1549055/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">50 F. 2d 505</a></span> (C. A. 3d Cir.); <em>Riggs </em>v. <em>United States, </em><span class="citation" data-id="9335930"><a href="/opinion/9340586/riggs-v-states/" aria-description="Citation for case: Riggs v. States">299 Fed. 273</a></span> (C. A. 4th Cir.); <em>Timonen </em>v. <em>United States, </em><span class="citation" data-id="8829031"><a href="/opinion/8843810/timonen-v-united-states/" aria-description="Citation for case: Timonen v. United States">286 Fed. 935</a></span> (C. A. 6th Cir.); <em>Fowler </em>v. <em>United States, </em><span class="citation" data-id="1472688"><a href="/opinion/1472688/fowler-v-united-states/" aria-description="Citation for case: Fowler v. United States">62 F. 2d 656</a></span> (C. A. 7th Cir.) (dictum); <em>Elam </em>v. <em>United States, </em><span class="citation" data-id="1509635"><a href="/opinion/1509635/elam-v-united-states/" aria-description="Citation for case: Elam v. United States">7 F. 2d 887</a></span> (C. A. 8th <page-number citation-index="1" label="211">*211</page-number>Cir.); <em>Brown </em>v. <em>United States, </em><span class="citation" data-id="1490225"><a href="/opinion/1490225/brown-v-united-states/" aria-description="Citation for case: Brown v. United States">12 F. 2d 926</a></span> (C. A. 9th Cir.); <em>Gilbert </em>v. <em>United States, </em><span class="citation" data-id="1498347"><a href="/opinion/1498347/gilbert-v-united-states/" aria-description="Citation for case: Gilbert v. United States">163 F. 2d 325</a></span> (C. A. 10th Cir.); <em>Shelton </em>v. <em>United States, </em>83 U. S. App. D. C. 257, <span class="citation" data-id="1476789"><a href="/opinion/1476789/shelton-v-united-states/" aria-description="Citation for case: Shelton v. United States">169 F. 2d 665</a></span>, overruled by <em>Hanna </em>v. <em>United States, </em>104 U. S. App. D. C. 205, <span class="citation" data-id="246433"><a href="/opinion/246433/samuel-j-hanna-v-united-states/" aria-description="Citation for case: Samuel J. Hanna v. United States">260 F. 2d 723</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b286-7"> Compare <em>Sutherland </em>v. <em>United States, </em><span class="citation" data-id="1501987"><a href="/opinion/1501987/sutherland-v-united-states/" aria-description="Citation for case: Sutherland v. United States">92 F. 2d 305</a></span> (C. A. 4th Cir.); <em>Ward </em>v. <em>United States, </em><span class="citation" data-id="9636747"><a href="/opinion/1475515/ward-v-united-states/" aria-description="Citation for case: Ward v. United States">96 F. 2d 189</a></span> (C. A.. 5th Cir.); <em>Fowler v. United States, </em><span class="citation" data-id="1472688"><a href="/opinion/1472688/fowler-v-united-states/" aria-description="Citation for case: Fowler v. United States">62 F. 2d 656</a></span> (C. A. 7th Cir.); <em>United States </em>v. <em>Butler, </em><span class="citation" data-id="1548044"><a href="/opinion/1548044/united-states-v-butler/" aria-description="Citation for case: United States v. Butler">156 F. 2d 897</a></span> (C. A. 10th Cir.); with <em>Kitt </em>v. <em>United States, </em><span class="citation" data-id="1480891"><a href="/opinion/1480891/kitt-v-united-states/" aria-description="Citation for case: Kitt v. United States">132 F. 2d 920</a></span> (C. A. 4th Cir.); <em>Sloane </em>v. <em>United States, </em><span class="citation" data-id="1501575"><a href="/opinion/1501575/sloane-v-united-states/" aria-description="Citation for case: Sloane v. United States">47 F. 2d 889</a></span> (C. A. 10th Cir.).</p>
</footnote>
<footnote label="5">
<p id="b286-9"> Compare <em>United States v. Jankowski, </em><span class="citation" data-id="9642206"><a href="/opinion/1502497/united-states-v-jankowski/" aria-description="Citation for case: United States v. Jankowski">28 F. 2d 800</a></span> (C. A. 2d Cir.); <em>Marsh </em>v. <em>United States, </em><span class="citation" data-id="1483661"><a href="/opinion/1483661/marsh-v-united-states/" aria-description="Citation for case: Marsh v. United States">29 F. 2d 172</a></span> (C. A. 2d Cir.); with <em>United States </em>v. <em>Butler, </em><span class="citation" data-id="1548044"><a href="/opinion/1548044/united-states-v-butler/" aria-description="Citation for case: United States v. Butler">156 F. 2d 897</a></span> (C. A. 10th Cir.).</p>
</footnote>
<footnote label="6">
<p id="b288-7"> See, e. <em>g., Burjord </em>v. <em>United States, </em><span class="citation" data-id="234366"><a href="/opinion/234366/burford-v-united-states/#125" aria-description="Citation for case: Burford v. United States">214 F. 2d 124, 125</a></span> (C. A. <em>5th </em>Cir.); <em>Ford </em>v. <em>United States, </em><span class="citation" data-id="239813"><a href="/opinion/239813/ralph-ford-v-united-states/#837" aria-description="Citation for case: Ralph Ford v. United States">234 F. 2d 835, 837</a></span> (C. A. 6th Cir.); <em>United States </em>v. <em>Moses, </em><span class="citation" data-id="239614"><a href="/opinion/239614/united-states-v-marvin-moses/" aria-description="Citation for case: United States v. Marvin Moses">234 F. 2d 124</a></span> (C. A. 7th Cir.); <em>Williams </em>v. <em>United States, 215 </em>F. 2d 695, 696 (C. A. 9th Cir.); <em>Gallegos </em>v. <em>United States, </em><span class="citation" data-id="240496"><a href="/opinion/240496/toby-anthony-gallegos-v-united-states-of-america-j-b-mingo-v-united/#696" aria-description="Citation for case: Toby Anthony Gallegos v. United States of America, J. B....">237 F. 2d 694, 696-697</a></span> (C. A. 10th Cir.).</p>
</footnote>
<footnote label="7">
<p id="b289-5"> Long before the Court established that the Fourteenth Amendment protects the security of one’s privacy against arbitrary intrusion by state officers, Mr. Justice (then Judge) Cardozo perceived a basic incongruity in a rule which excludes evidence unlawfully obtained by federal officers, but admits in the same court evidence unlawfully obtained by state agents. “The Federal rule as it stands is either too strict or too lax. A Federal prosecutor may take no benefit from evidence collected through the trespass of a Federal officer. . . . He does not have to be so scrupulous about evidence brought to him by others. How finely the line is drawn is seen when we recall that marshals in the service of the nation are on one side of it, and police in the service of.the States on the other. The nation may keep what the servants of the States supply. . . . We must go farther or not so far. The professed object of the trespass rather than the official character of the trespasser should test the rights of government. . . A government would be disingenuous, if, in determining the use that should be made of evidence drawn from such a source, it drew a line between them. This would be true whether they had acted in concert, or apart.” <em>People </em>v. <em>Defore, </em><span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#22" aria-description="Citation for case: People v. Defore">242 N. Y. 13, 22-23</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#588" aria-description="Citation for case: People v. Defore">150 N. E. 585, 588</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b292-8"> The Director of the Federal Bureau of Investigation has written as follows:</p>
<p id="b292-9">“One of the quickest ways for any law enforcement officer to bring public disrepute upon himself, his organization and the entire profession is to be found guilty of a violation of civil rights. Our people may tolerate many mistakes of both intent and performance, but, with unerring instinct, they know that when any person is intentionally deprived of his constitutional rights those responsible have committed no ordinary offense. A crime of this nature, if subtly encouraged by failure to condemn and punish, certainly leads down the road to totalitarianism.</p>
<p id="b292-10">“Civil rights violations are all the more regrettable because they are so unnecessary. Professional standards in law enforcement pro<page-number citation-index="1" label="219">*219</page-number>vide for fighting crime with intelligence rather than force. ... In matters of scientific crime detection, the services of our FBI Laboratory are available to every duly constituted law enforcement officer in the nation. Full use of these and other facilities should make it entirely unnecessary for any officer to feel the need to use dishonorable methods.</p>
<p id="AqV-">“Complete protection of civil rights should be a primary concern of every officer. These rights are basic in the law and our obligation to uphold it leaves no room for any other course of action. Although the great majority in our profession have long since adopted that policy, we cannot yet be entirely proud of our record. Incidents which give justification to charges of civil rights violations by law enforcement officers still occur. . . . This state of affairs ought to be taken as a challenge to all of us. Every progressive police administrator and officer must do everything in his power to bring about such an improvement that our conduct and our record will conclusively prove each of these charges to be false.” FBI Law Enforcement Bulletin, September, 1952, pp. 1-2.</p>
</footnote>
<footnote label="9">
<p id="b293-7"> See Appendix, <em>post, </em>pp. 224^-225.</p>
</footnote>
<footnote label="10">
<p id="b293-8"> See Appendix, <em>post, </em>pp. 224-225.</p>
</footnote>
<footnote label="11">
<p id="b293-9"> For a discussion of recent developments in British Commonwealth jurisdictions, see Cowen, The Admissibility of Evidence Procured Through Illegal Searches and Seizures in British Commonwealth Jurisdictions, 5 Vanderbilt L. Rev. 523 (1952). The author concludes upon a survey of Commonwealth decisions “that there is no uniform rule on the admissibility of evidence procured through illegal searches and seizures.” <em>Id., </em>at 546.</p>
</footnote>
<footnote label="12">
<p id="b293-10"> North Carolina. See Appendix, <em>post, </em>p. 230.</p>
</footnote>
<footnote label="13">
<p id="b293-11"> Delaware and California. See Appendix, <em>post, </em>p. 226.</p>
</footnote>
<footnote label="14">
<p id="b294-9"> Rhode Island. See Appendix, <em>post, </em>p. 231.</p>
</footnote>
<footnote label="15">
<p id="b295-7"> Excerpt from letter of Governor Edmund G. Brown, then Attorney General of the State of California, to the Stanford Law Review, quoted in Note, <span class="citation no-link">9 Stan. L. Rev. 515</span>, 538 (1957). See also Barrett, Exclusion of Evidence Obtained by Illegal Searches — A Comment on People vs. Cahan, <span class="citation no-link">43 Cal. L. Rev. 565</span>, 586-588 (1955).</p>
</footnote>
<footnote label="16">
<p id="b297-7"> See Rule 41(e), Fed. Rules Crim. Proc. The defendant, of course, must have “standing” to object. See <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span>.</p>
</footnote>
<footnote label="*">
<p id="b299-42">Alaska and Hawaii both hold illegally obtained evidence to be ex-cludable, although it does not appear that either has passed anew on this question since attaining statehood.</p>
</footnote>
</opinion>
```

---
