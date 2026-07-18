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

## GROUP: content/cases/United States v. Leon.md  (`case`, 6 assertions)

### content_page

```
---
title: "United States v. Leon"
type: case
citation: "468 U.S. 897 (1984)"
parallel_cite: "104 S. Ct. 3405; 82 L. Ed. 2d 677"
neutral_cite: 1984 U.S. LEXIS 153
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-09-18
docket: 82-1771
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-07-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Leon
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111262/united-states-v-leon/"
  cluster_id: 111262
  opinion_id: 9429766
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Anchor"
  - page: "[[Franks Challenges]]"
    role: "Related (cross-doctrine)"
related: ["[[Massachusetts v. Sheppard]]", "[[Herring v. United States]]", "[[Davis v. United States (2011)|Davis v. United States]]", "[[Franks v. Delaware]]", "[[Illinois v. Gates]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "good-faith-exception", "search-warrant", "deterrence"]
holding: "Good-faith exception: evidence obtained by officers in objectively reasonable reliance on a search warrant later found unsupported by…"
lake:
  record_id: United States v. Leon
  status: verified
  projected_at: 2026-07-09
---

# United States v. Leon

*468 U.S. 897 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Acting on a confidential informant's tip of unproven reliability, Burbank police conducted surveillance and investigation, then obtained a facially valid search warrant from a state judge; the searches produced large quantities of drugs. The District Court held the affidavit insufficient to establish probable cause but recognized that the officers had acted in good faith, and granted suppression; the Ninth Circuit affirmed.

## Issue
Whether the Fourth Amendment exclusionary rule should be modified so as not to bar the prosecution's use, in its case-in-chief, of evidence obtained by officers acting in objectively reasonable reliance on a search warrant issued by a detached and neutral magistrate but ultimately found to be unsupported by probable cause.

## Rule
The exclusionary rule does not bar such evidence. Because the rule's purpose is to deter police misconduct, and suppressing evidence obtained on a warrant deters the magistrate's error rather than the officer's, the Court held: "We conclude that the marginal or nonexistent benefits produced by suppressing evidence obtained in objectively reasonable reliance on a subsequently invalidated search warrant cannot justify the substantial costs of exclusion." — 468 U.S. at 922. ^pin-922

Good faith is measured objectively, and the exception does **not** apply in four situations: (1) where "the magistrate or judge in issuing a warrant was misled by information in an affidavit that the affiant knew was false or would have known was false except for his reckless disregard of the truth" ([[Franks v. Delaware]]); (2) where "the issuing magistrate wholly abandoned his judicial role"; (3) where the affidavit is "so lacking in indicia of probable cause as to render official belief in its existence entirely unreasonable"; and (4) where a warrant is so facially deficient — in failing to particularize the place or things — "that the executing officers cannot reasonably presume it to be valid." — [*Id.* at 923](https://www.courtlistener.com/opinion/111262/united-states-v-leon/#:~:text=the%20magistrate%20or%20judge%20in). ^pin-923

## Application
On these facts the evidence was admissible. The officers obtained a warrant from a neutral magistrate and executed it within its terms; whatever the affidavit's shortcomings on probable cause, their reliance on the judge's determination was objectively reasonable. None of the four disqualifying circumstances was present — there was no *[[Franks v. Delaware|Franks]]* falsehood, the magistrate did not abandon his judicial role, the affidavit was not so bare as to make belief in probable cause entirely unreasonable, and the warrant was not facially deficient. Excluding the evidence would punish the officers for the magistrate's error and yield no appreciable deterrent benefit, so suppression was unwarranted.

## Conclusion
Evidence seized in objectively reasonable reliance on a later-invalidated warrant need not be suppressed; the Ninth Circuit's judgment affirming suppression was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Leon* establishes the [[The Good-Faith Exception|good-faith exception]], extended the same day to a [[Particularity|particularity]] defect in [[Massachusetts v. Sheppard]], to a statute later held unconstitutional in [[Illinois v. Krull]], and to police recordkeeping errors in [[Herring v. United States]] and binding-precedent reliance in [[Davis v. United States (2011)|Davis v. United States]]; its limits track the four enumerated exceptions.

## Appears on
- [[The Exclusionary Rule]] — *Key — Anchor*
- [[Franks Challenges]] — *Related (cross-doctrine)*

## Sources
- *United States v. Leon*, 468 U.S. 897 (1984) — https://www.courtlistener.com/opinion/111262/united-states-v-leon/ — pinpoints: 922, 923.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "dd3942d5240b0c54", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "468 U.S. 897 (1984)", "court": "U.S. Supreme Court", "neutral_cite": "1984 U.S. LEXIS 153", "official_citation_present": true, "parallel_cite": "104 S. Ct. 3405; 82 L. Ed. 2d 677", "title": "United States v. Leon", "year": "1984"}}
{"assertion_id": "9cf3808e8781428c", "dimension": "support", "kind": "home_role", "locator": {"home": "Franks Challenges"}, "payload": {"home": "Franks Challenges", "role": "Related (cross-doctrine)", "title": "United States v. Leon"}}
{"assertion_id": "a2583c3904cb55c2", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Good-faith exception: evidence obtained by officers in objectively reasonable reliance on a search warrant later found unsupported by…", "title": "United States v. Leon"}}
{"assertion_id": "fe7b3ccfad127935", "dimension": "support", "kind": "home_role", "locator": {"home": "The Good-Faith Exception"}, "payload": {"home": "The Good-Faith Exception", "role": "Key — Anchor", "title": "United States v. Leon"}}
{"assertion_id": "511d95fd3cf5a834", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1984-07-05", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Leon", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Leon", "varies_by_point": "false"}}
{"assertion_id": "8fe284cbce5672a6", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Leon"}}
```

### lake record — United States v. Leon

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Leon",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Leon",
    "case_name_short": "Leon",
    "case_name_full": "UNITED STATES v. LEON Et Al.",
    "input_case_name": "United States v. Leon",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-09-18",
    "year": 1984,
    "docket": "82-1771",
    "cluster_id": 111262,
    "lead_opinion_id": 9429766,
    "sibling_ids": [
      111262,
      9429766,
      9429767,
      9429768,
      9429769
    ],
    "absolute_url": "/opinion/111262/united-states-v-leon/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "468 U.S. 897",
      "volume": "468",
      "reporter": "U.S.",
      "page": "897",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 3405",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3405",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 677",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "677",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 153",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "153",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "468 U.S. 897",
        "volume": "468",
        "reporter": "U.S.",
        "page": "897",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 3405",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3405",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 677",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "677",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 153",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "153",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "468 U.S. 897",
    "official_selection": {
      "court_class": "scotus",
      "selected": "468 U.S. 897",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-922",
      "page": null,
      "quote": "--- # United States v. Leon *468 U.S. 897 (1984)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting on a confidential informant's tip of unproven reliability, Burbank police conducted surveillance and investigation, then obtained a facially valid search warrant from a state judge; the searches produced large quantities of drugs. The District Court held the affidavit insufficient to establish probable cause but recognized that the officers had acted in good faith, and granted suppression; the Ninth Circuit affirmed. ## Issue Whether the Fourth Amendment exclusionary rule should be modified so as not to bar the prosecution's use, in its case-in-chief, of evidence obtained by officers acting in objectively reasonable reliance on a search warrant issued by a detached and neutral magistrate but ultimately found to be unsupported by probable cause. ## Rule The exclusionary rule does not bar such evidence. Because the rule's purpose is to deter police misconduct, and suppressing evidence obtained on a warrant deters the magistrate's error rather than the officer's, the Court held:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-923",
      "page": null,
      "quote": "the magistrate or judge in issuing a warrant was misled by information in an affidavit that the affiant knew was false or would have known was false except for his reckless disregard of the truth",
      "star_marker": "923",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 48236,
      "fragment": "#:~:text=the%20magistrate%20or%20judge%20in",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-07-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Leon",
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
        "journal_ref": "United States v. Leon:lane1_negative"
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
        "journal_ref": "United States v. Leon:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Batson v. Kentucky",
          "cluster_id": 111662,
          "cite": [
            "90 L. Ed. 2d 69",
            "106 S. Ct. 1712",
            "476 U.S. 79",
            "1986 U.S. LEXIS 150",
            "54 U.S.L.W. 4425"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
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
        "journal_ref": "United States v. Leon:lane2_top_cited"
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
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murray v. Carrier",
          "cluster_id": 111727,
          "cite": [
            "91 L. Ed. 2d 397",
            "106 S. Ct. 2639",
            "477 U.S. 478",
            "1986 U.S. LEXIS 66",
            "54 U.S.L.W. 4820"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
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
        "journal_ref": "United States v. Leon:lane2_top_cited"
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
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyles v. Whitley",
          "cluster_id": 117923,
          "cite": [
            "131 L. Ed. 2d 490",
            "115 S. Ct. 1555",
            "514 U.S. 419",
            "1995 U.S. LEXIS 2845"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
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
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. Witt",
          "cluster_id": 111303,
          "cite": [
            "83 L. Ed. 2d 841",
            "105 S. Ct. 844",
            "469 U.S. 412",
            "1985 U.S. LEXIS 43",
            "53 U.S.L.W. 4108"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kimmelman v. Morrison",
          "cluster_id": 111724,
          "cite": [
            "91 L. Ed. 2d 305",
            "106 S. Ct. 2574",
            "477 U.S. 365",
            "1986 U.S. LEXIS 63",
            "54 U.S.L.W. 4789"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
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
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Elstad",
          "cluster_id": 111364,
          "cite": [
            "84 L. Ed. 2d 222",
            "105 S. Ct. 1285",
            "470 U.S. 298",
            "1985 U.S. LEXIS 60",
            "53 U.S.L.W. 4244"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 117863,
          "cite": [
            "129 L. Ed. 2d 362",
            "114 S. Ct. 2350",
            "512 U.S. 452",
            "1994 U.S. LEXIS 4827"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
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
        "journal_ref": "United States v. Leon:lane2_top_cited"
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
        "journal_ref": "United States v. Leon:lane2_top_cited"
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
        "journal_ref": "United States v. Leon:lane2_top_cited"
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
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vasquez v. Hillery",
          "cluster_id": 111552,
          "cite": [
            "88 L. Ed. 2d 598",
            "106 S. Ct. 617",
            "474 U.S. 254",
            "1986 U.S. LEXIS 40",
            "54 U.S.L.W. 4068"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wright v. West",
          "cluster_id": 112771,
          "cite": [
            "120 L. Ed. 2d 225",
            "112 S. Ct. 2482",
            "505 U.S. 277",
            "1992 U.S. LEXIS 3689"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
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
        "journal_ref": "United States v. Leon:lane2_top_cited"
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
        "journal_ref": "United States v. Leon:lane2_top_cited"
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
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brower Ex Rel. Estate of Caldwell v. County of Inyo",
          "cluster_id": 112218,
          "cite": [
            "103 L. Ed. 2d 628",
            "109 S. Ct. 1378",
            "489 U.S. 593",
            "1989 U.S. LEXIS 1569",
            "57 U.S.L.W. 4321"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mickens v. Taylor",
          "cluster_id": 118492,
          "cite": [
            "152 L. Ed. 2d 291",
            "122 S. Ct. 1237",
            "535 U.S. 162",
            "2002 U.S. LEXIS 2146"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murray v. United States",
          "cluster_id": 112136,
          "cite": [
            "101 L. Ed. 2d 472",
            "108 S. Ct. 2529",
            "487 U.S. 533",
            "1988 U.S. LEXIS 2881",
            "56 U.S.L.W. 4801"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Leon:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111262 OR 9429766 OR 9429767 OR 9429768 OR 9429769) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjgwMjIwODAwMDAwJnM9OTM4ODM0MSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111262+OR+9429766+OR+9429767+OR+9429768+OR+9429769%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111262 OR 9429766 OR 9429767 OR 9429768 OR 9429769)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03NzYmcz0yMzE2Njk4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111262+OR+9429766+OR+9429767+OR+9429768+OR+9429769%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111262 OR 9429766 OR 9429767 OR 9429768 OR 9429769)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzAzNzIxNjAwMDAwJnM9OTQ1NTgxNiZ0PW8mZD0yMDI2LTA3LTA2JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111262+OR+9429766+OR+9429767+OR+9429768+OR+9429769%29&type=o",
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
    "complete_query": "cites:(111262 OR 9429766 OR 9429767 OR 9429768 OR 9429769)",
    "indexed_citing_opinions": 5262,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111262,
        "count": 4543,
        "count_source": "search"
      },
      {
        "opinion_id": 9429766,
        "count": 808,
        "count_source": "search"
      },
      {
        "opinion_id": 9429767,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429768,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429769,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 9241,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-leon.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk1MTI1OCZzPTEwNjYyNTI5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111262+OR+9429766+OR+9429767+OR+9429768+OR+9429769%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111262,
        "cited_id": 85272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 100621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 100949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 105242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 106287,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107577,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108379,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109303,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 109925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 111112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 111172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 294030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 296213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 333763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 339292,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 378896,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 1237532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 2058560,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
        "cited_id": 2620876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111262,
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
    "date_created": "2026-07-06T01:20:53Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:21:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:21:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:24:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:21:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Leon

```
<opinion type="majority">
<author id="b942-4"><page-number citation-index="1" label="900">*900</page-number>Justice White</author>
<p id="AaUZ">delivered the opinion of the Court.</p>
<p id="b942-5">This ease presents the question whether the Fourth Amendment exclusionary rule should be modified so as not to bar the use in the prosecution’s case in chief of evidence obtained by officers acting in reasonable reliance on a search warrant issued by a detached and neutral magistrate but ultimately found to be unsupported by probable cause. To resolve this question, we must consider once again the tension between the sometimes competing goals of, on the one hand, deterring official misconduct and removing inducements to unreasonable invasions of privacy and, on the other, establishing procedures under which criminal defendants are “ac<page-number citation-index="1" label="901">*901</page-number>quitted or convicted on the basis of all the evidence which exposes the truth.” <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#175" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 175</a></span> (1969).</p>
<p id="b943-5">I</p>
<p id="b943-6">In August 1981, a confidential informant of unproven reliability informed an officer of the Burbank Police Department that two persons known to him as “Armando” and “Patsy” were selling large quantities of cocaine and methaqualone from their residence at 620 Price Drive in Burbank, Cal. The informant also indicated that he had witnessed a sale of methaqualone by “Patsy” at the residence approximately five months earlier and had observed at that time a shoebox containing a large amount of cash that belonged to “Patsy.” He further declared that “Armando” and “Patsy” generally kept only small quantities of drugs at their residence and stored the remainder at another location in Burbank.</p>
<p id="b943-7">On the basis of this information, the Burbank police initiated an extensive investigation focusing first on the Price Drive residence and later on two other residences as well. Cars parked at the Price Drive residence were determined to belong to respondents Armando Sanchez, who had previously been arrested for possession of marihuana, and Patsy Stewart, who had no criminal record. During the course of the investigation, officers observed an automobile belonging to respondent Ricardo Del Castillo, who had previously been arrested for possession of 50 pounds of marihuana, arrive at the Price Drive residence. The driver of that car entered the house, exited shortly thereafter carrying a small paper sack, and drove away. A check of Del Castillo’s probation records led the officers to respondent Alberto Leon, whose telephone number Del Castillo had listed as his employer’s. Leon had been arrested in 1980 on drug charges, and a companion had informed the police at that time that Leon was heavily involved in the importation of drugs into this country. Before the current investigation began, the Burbank officers had <page-number citation-index="1" label="902">*902</page-number>learned that an informant had told a Glendale police officer that Leon stored a large quantity of methaqualone at his residence in Glendale. During the course of this investigation, the Burbank officers learned that Leon was living at 716 South Sunset Canyon in Burbank.</p>
<p id="b944-5">Subsequently, the officers observed several persons, at least one of whom had prior drug involvement, arriving at the Price Drive residence and leaving with small packages; observed a variety of other material activity at the two residences as well as at a condominium at 7902 Via Magdalena; and witnessed a variety of relevant activity involving respondents’ automobiles. The officers also observed respondents Sanchez and Stewart board separate flights for Miami. The pair later returned to Los Angeles together, consented to a search of their luggage that revealed only a small amount of marihuana, and left the airport. Based on these and other observations summarized in the affidavit, App. 34, Officer Cyril Rombach of the Burbank Police Department, an experienced and well-trained narcotics investigator, prepared an application for a warrant to search 620 Price Drive, 716 South Sunset Canyon, 7902 Via Magdalena, and automobiles registered to each of the respondents for an extensive list of items believed to be related to respondents’ drug-trafficking activities. Officer Rombach’s extensive application was reviewed by several Deputy District Attorneys.</p>
<p id="b944-6">A facially valid search warrant was issued in September 1981 by a State Superior Court Judge. The ensuing searches produced large quantities of drugs at the Via Magdalena and Sunset Canyon addresses and a small quantity at the Price Drive residence. Other evidence was discovered at each of the residences and in Stewart’s and Del Castillo’s automobiles. Respondents were indicted by a grand jury in the District Court for the Central District of California and charged with conspiracy to possess and distribute cocaine and a variety of substantive counts.</p>
<p id="b945-4"><page-number citation-index="1" label="903">*903</page-number>The respondents then filed motions to suppress the evidence seized pursuant to the warrant.<footnotemark>1</footnotemark> The District Court held an evidentiary hearing and, while recognizing that the case was a close one, see <em>id., </em>at 131, granted the motions to suppress in part. It concluded that the affidavit was insufficient to establish probable cause,<footnotemark>2</footnotemark> but did not suppress all of the evidence as to all of the respondents because none of the respondents had standing to challenge all of the searches.<footnotemark>3</footnotemark> In <page-number citation-index="1" label="904">*904</page-number>response to a request from the Government, the court made clear that Officer Rombach had acted in good faith, but it rejected the Government’s suggestion that the Fourth Amendment exclusionary rule should not apply where evidence is seized in reasonable, good-faith reliance on a search warrant.<footnotemark>4</footnotemark></p>
<p id="b946-5">The District Court denied the Government’s motion for reconsideration, id., at 147, and a divided panel of the Court of Appeals for the Ninth Circuit affirmed, judgt. order reported at <span class="citation multiple-matches"><a href="/c/F.%202d/701/187/">701 F. 2d 187</a></span> (1983). The Court of Appeals first concluded that Officer Rombach’s affidavit could not establish probable cause to search the Price Drive residence. To the extent that the affidavit set forth facts demonstrating the basis of the informant’s knowledge of criminal activity, the information included was fatally stale. The affidavit, moreover, failed to establish the informant’s credibility. Accordingly, the Court of Appeals concluded that the information provided by the informant was inadequate under both prongs of the two-part test established in <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), and <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969).<footnotemark>5</footnotemark> The officers’ independent investigation neither cured the staleness nor corroborated the details of the informant’s declarations. The Court of Appeals then considered whether the affidavit formed a proper basis for the <page-number citation-index="1" label="905">*905</page-number>search of the Sunset Canyon residence. In its view, the affidavit included no facts indicating the basis for the informants’ statements concerning respondent Leon’s criminal activities and was devoid of information establishing the informants’ reliability. Because these deficiencies had not been cured by the police investigation, the District Court properly suppressed the fruits of the search. The Court of Appeals refused the Government’s invitation to recognize a good-faith exception to the Fourth Amendment exclusionary rule. App. to Pet. for Cert. 4a.</p>
<p id="b947-5">The Government’s petition for certiorari expressly declined to seek review of the lower courts’ determinations that the search warrant was unsupported by probable cause and presented only the question “[w]hether the Fourth Amendment exclusionary rule should be modified so as not to bar the admission of evidence seized in reasonable, good-faith reliance on a search warrant that is subsequently held to be defective.” We granted certiorari to consider the propriety of such a modification. <span class="citation multiple-matches"><a href="/c/U.%20S./463/1206/">463 U. S. 1206</a></span> (1983). Although it undoubtedly is within our power to consider the question whether probable cause existed under the “totality of the circumstances” test announced last Term in <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213</a></span> (1983), that question has not been briefed or argued; and it is also within our authority, which we choose to exercise, to take the case as it comes to us, accepting the Court of Appeals’ conclusion that probable cause was lacking under the prevailing legal standards. See this Court’s Rule 21.1(a).</p>
<p id="b947-6">We have concluded that, in the Fourth Amendment context, the exclusionary rule can be modified somewhat without jeopardizing its ability to perform its intended functions. Accordingly, we reverse the judgment of the Court of Appeals.</p>
<p id="b947-7">II</p>
<p id="b947-8">Language in opinions of this Court and of individual Justices has sometimes implied that the exclusionary rule is a necessary corollary of the Fourth Amendment, <em>Mapp </em>v. <page-number citation-index="1" label="906">*906</page-number><em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#651" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 651, 655-657</a></span> (1961); <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#462" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 462-463</a></span> (1928), or that the rule is required by the conjunction of the Fourth and Fifth Amendments. <em>Mapp </em>v. <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#661" aria-description="Citation for case: Mapp v. Ohio"><em>Ohio, supra, </em>at 661-662</a></span> (Black, J., concurring); <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33-34</a></span> (1925). These implications need not detain us long. The Fifth Amendment theory has not withstood critical analysis or the test of time, see <em>Andresen </em>v. <em>Maryland, </em><span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">427 U. S. 463</a></span> (1976), and the Fourth Amendment “has never been interpreted to proscribe the introduction of illegally seized evidence in all proceedings or against all persons.” <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 486</a></span> (1976).</p>
<p id="b948-5">A</p>
<p id="b948-6">The Fourth Amendment contains no provision expressly precluding the use of evidence obtained in violation of its commands, and an examination of its origin and purposes makes clear that the use of fruits of a past unlawful search or seizure “work[s] no new Fourth Amendment wrong.” <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#354" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 354</a></span> (1974). The wrong condemned by the Amendment is “fully accomplished” by the unlawful search or seizure itself, <em>ibid., </em>and the exclusionary rule is neither intended nor able to “cure the invasion of the defendant’s rights which he has already suffered.” <em>Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#540" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 540</a></span> (White, J., dissenting). The rule thus operates as “a judicially created remedy designed to safeguard Fourth Amendment rights generally through its deterrent effect, rather than a personal constitutional right of the party aggrieved.” <em>United States </em>v. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>.</p>
<p id="b948-7">Whether the exclusionary sanction is appropriately imposed in a particular case, our decisions make clear, is “an issue separate from the question whether the Fourth Amendment rights of the party seeking to invoke the rule were violated by police conduct.” <em>Illinois </em>v. <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#223" aria-description="Citation for case: Illinois v. Gates"><em>Gates, supra, </em>at 223</a></span>. Only the former question is currently before us, and it must <page-number citation-index="1" label="907">*907</page-number>be resolved by weighing the costs and benefits of preventing the use in the prosecution’s case in chief of inherently trustworthy tangible evidence obtained in reliance on a search warrant issued by a detached and neutral magistrate that ultimately is found to be defective.</p>
<p id="b949-5">The substantial social costs exacted by the exclusionary rule for the vindication of Fourth Amendment rights have long been a source of concern. “Our cases have consistently recognized that unbending application of the exclusionary sanction to enforce ideals of governmental rectitude would impede unacceptably the truth-finding functions of judge and jury.” <em>United States </em>v. <em>Payner, </em><span class="citation" data-id="9428014"><a href="/opinion/110317/united-states-v-payner/#734" aria-description="Citation for case: United States v. Payner">447 U. S. 727, 734</a></span> (1980). An objectionable collateral consequence of this interference with the criminal justice system’s truth-finding function is that some guilty defendants may go free or receive reduced sentences as a result of favorable plea bargains.<footnotemark>6</footnotemark> Particu<page-number citation-index="1" label="908">*908</page-number>larly when law enforcement officers have acted in objective good faith or their transgressions have been minor, the magnitude of the benefit conferred on such guilty defendants offends basic concepts of the criminal justice system. <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#490" aria-description="Citation for case: Stone v. Powell">428 U. S., at 490</a></span>. Indiscriminate application of the exclusionary rule, therefore, may well “generate] disrespect for the law and administration of justice.” <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#491" aria-description="Citation for case: Stone v. Powell">Id., at 491</a></span>. Accordingly, “[a]s with any remedial device, the application of the rule has been restricted to those areas where its remedial objectives are thought most efficaciously served.” <em>United States </em>v. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>; see <em>Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 486-487</a></span>; <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#447" aria-description="Citation for case: United States v. Janis">428 U. S. 433, 447</a></span> (1976).</p>
<p id="b950-5">B</p>
<p id="b950-6">Close attention to those remedial objectives has characterized our recent decisions concerning the scope of the Fourth Amendment exclusionary rule. The Court has, to be sure, not seriously questioned, “in the absence of a more efficacious sanction, the continued application of the rule to suppress ev<page-number citation-index="1" label="909">*909</page-number>idence from the [prosecution’s] case where a Fourth Amendment violation has been substantial and deliberate. ...” <em>Franks </em>v. <em>Delaware, </em><span class="citation" data-id="9427321"><a href="/opinion/109925/franks-v-delaware/#171" aria-description="Citation for case: Franks v. Delaware">438 U. S. 154, 171</a></span> (1978); <em>Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#492" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 492</a></span>. Nevertheless, the balancing approach that has evolved in various contexts — including criminal trials — “forcefully suggests] that the exclusionary rule be more generally modified to permit the introduction of evidence obtained in the reasonable good-faith belief that a search or seizure was in accord with the Fourth Amendment.” <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#255" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 255</a></span> (WHITE, J., concurring in judgment).</p>
<p id="b951-5">In <em>Stone </em>v. <em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Powell, supra,</a></span> </em>the Court emphasized the costs of the exclusionary rule, expressed its view that limiting the circumstances under which Fourth Amendment claims could be raised in federal habeas corpus proceedings would not reduce the rule’s deterrent effect, <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#489" aria-description="Citation for case: Stone v. Powell"><em>id., </em>at 489-495</a></span>, and held that a state prisoner who has been afforded a full and fair opportunity to litigate a Fourth Amendment claim may not obtain federal habeas relief on the ground that unlawfully obtained evidence had been introduced at his trial. Cf. <em>Rose </em>v. <em>Mitchell, </em><span class="citation" data-id="9427696"><a href="/opinion/110143/rose-v-mitchell/#560" aria-description="Citation for case: Rose v. Mitchell">443 U. S. 545, 560-563</a></span> (1979). Proposed extensions of the exclusionary rule to proceedings other than the criminal trial itself have been evaluated and rejected under the same analytic approach. In <em>United States </em>v. <em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">Calandra</a></span>, </em>for example, we declined to allow grand jury witnesses to refuse to answer questions based on evidence obtained from an unlawful search or seizure since “[a]ny incremental deterrent effect which might be achieved by extending the rule to grand jury proceedings is uncertain at best.” <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S., at 348</a></span>. Similarly, in <em>United States </em>v. <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis, supra,</a></span> </em>we permitted the use in federal civil proceedings of evidence illegally seized by state officials since the likelihood of deterring police misconduct through such an extension of the exclusionary rule was insufficient to outweigh its substantial social costs. In so doing, we declared that, “[i]f . . . the exclusionary rule does not result in appreciable deterrence, then, clearly, its use in the instant situation is unwarranted.” <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#454" aria-description="Citation for case: United States v. Janis"><em>Id., </em>at 454</a></span>.</p>
<p id="b952-4"><page-number citation-index="1" label="910">*910</page-number>As cases considering the use of unlawfully obtained evidence in criminal trials themselves make clear, it does not follow from the emphasis on the exclusionary rule’s deterrent value that “anything which deters illegal searches is thereby commanded by the Fourth Amendment.” <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States">394 U. S., at 174</a></span>. In determining whether persons aggrieved solely by the introduction of damaging evidence unlawfully obtained from their co-conspirators or codefendants could seek suppression, for example, we found that the additional benefits of such an extension of the exclusionary rule would not outweigh its costs. <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States"><em>Id., </em>at 174-175</a></span>. Standing to invoke the rule has thus been limited to cases in which the prosecution seeks to use the fruits of an illegal search or seizure against the victim of police misconduct. <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978); <em>Brown </em>v. <em>United States, </em><span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/" aria-description="Citation for case: Brown v. United States">411 U. S. 223</a></span> (1973); <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#491" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 491-492</a></span> (1963). Cf. <em>United States </em>v. <em>Payner, </em><span class="citation" data-id="9428014"><a href="/opinion/110317/united-states-v-payner/" aria-description="Citation for case: United States v. Payner">447 U. S. 727</a></span> (1980).</p>
<p id="b952-5">Even defendants with standing to challenge the introduction in their criminal trials of unlawfully obtained evidence cannot prevent every conceivable use of such evidence. Evidence obtained in violation of the Fourth Amendment and inadmissible in the prosecution’s case in chief may be used to impeach a defendant’s direct testimony. <em>Walder </em>v. <em>United States, </em><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span> (1954). See also <em>Oregon </em>v. <em>Hass, </em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714</a></span> (1975); <em>Harris </em>v. <em>New York, </em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971). A similar assessment of the “incremental furthering” of the ends of the exclusionary rule led us to conclude in <em>United States </em>v. <em>Havens, </em><span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#627" aria-description="Citation for case: United States v. Havens">446 U. S. 620, 627</a></span> (1980), that evidence inadmissible in the prosecution’s case in chief or otherwise as substantive evidence of guilt may be used to impeach statements made by a defendant in response to “proper cross-examination reasonably suggested by the defendant’s direct examination.” <span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#627" aria-description="Citation for case: United States v. Havens"><em>Id., </em>at 627-628</a></span>.</p>
<p id="b952-6">When considering the use of evidence obtained in violation of the Fourth Amendment in the prosecution’s case in chief, moreover, we have declined to adopt a <em>per se </em>or “but for” rule <page-number citation-index="1" label="911">*911</page-number>that would render inadmissible any evidence that came to light through a chain of causation that began with an illegal arrest. <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975); <em>Wong Sun </em>v. <em>United States, supra, </em>at 487-488. We also have held that a witness’ testimony may be admitted even when his identity was discovered in an unconstitutional search. <em>United States </em>v. <em>Ceccolini, </em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">435 U. S. 268</a></span> (1978). The perception underlying these decisions — that the connection between police misconduct and evidence of crime may be sufficiently attenuated to permit the use of that evidence at trial — is a product of considerations relating to the exclusionary rule and the constitutional principles it is designed to protect. <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#217" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 217-218</a></span> (1979); <em>United States </em>v. <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#279" aria-description="Citation for case: United States v. Ceccolini"><em>Ceccolini, supra, </em>at 279</a></span>.<footnotemark>7</footnotemark> In short, the “dissipation of the taint” concept that the Court has applied in deciding whether exclusion is appropriate in a particular case “attempts to mark the point at which the detrimental consequences of illegal police action become so attenuated that the deterrent effect of the exclusionary rule no longer justifies its cost.” <em>Brown </em>v. <em>Illinois, supra, </em>at 609 (Powell, J., concurring in part). Not surprisingly in view of this purpose, an assessment of the flagrancy of the police misconduct constitutes an important step in the calculus. <em>Dunaway </em>v. <em>New York, supra, </em>at 218; <em>Brown </em>v. <em>Illinois, supra, </em>at 603-604.</p>
<p id="b953-5">The same attention to the purposes underlying the exclusionary rule also has characterized decisions not involving the scope of the rule itself. We have not required suppression of the fruits of a search incident to an arrest made in good-faith reliance on a substantive criminal statute that subsequently <page-number citation-index="1" label="912">*912</page-number>is declared unconstitutional. <em>Michigan </em>v. <em>DeFillippo, </em><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/" aria-description="Citation for case: Michigan v. DeFillippo">443 U. S. 31</a></span> (1979).<footnotemark>8</footnotemark> Similarly, although the Court has been unwilling to conclude that new Fourth Amendment principles are always to have only prospective effect, <em>United States </em>v. <em>Johnson, </em><span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/#560" aria-description="Citation for case: United States v. Johnson">457 U. S. 537, 560</a></span> (1982),<footnotemark>9</footnotemark> no Fourth Amendment decision marking a “clear break with the past” has been applied retroactively. See <em>United States </em>v. <em>Peltier, </em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/" aria-description="Citation for case: United States v. Peltier">422 U. S. 531</a></span> (1975); <em>Desist </em>v. <em>United States, </em><span class="citation" data-id="9423951"><a href="/opinion/107875/desist-v-united-states/" aria-description="Citation for case: Desist v. United States">394 U. S. 244</a></span> (1969); <em>Linkletter </em>v. <em>Walker, </em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618</a></span> (1965).<footnotemark>10</footnotemark> The propriety <page-number citation-index="1" label="913">*913</page-number>of retroactive application of a newly announced Fourth Amendment principle, moreover, has been assessed largely in terms of the contribution retroactivity might make to the deterrence of police misconduct. <em>United States </em>v. <span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/#560" aria-description="Citation for case: United States v. Johnson"><em>Johnson, supra, </em>at 560-561</a></span>; <em>United States </em>v. <span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#536" aria-description="Citation for case: United States v. Peltier"><em>Peltier, supra, </em>at 536-539, 542</a></span>.</p>
<p id="b955-9">As yet, we have not recognized any form of good-faith exception to the Fourth Amendment exclusionary rule.<footnotemark>11</footnotemark> But the balancing approach that has evolved during the years of experience with the rule provides strong support for the modification currently urged upon us. As we discuss below, our evaluation of the costs and benefits of suppressing reliable physical evidence seized by officers reasonably relying on a warrant issued by a detached and neutral magistrate leads to the conclusion that such evidence should be admissible in the prosecution’s case in chief.</p>
<p id="b955-10">HH HH</p>
<p id="b955-3">A</p>
<p id="b955-4">Because a search warrant “provides the detached scrutiny of a neutral magistrate, which is a more reliable safeguard <page-number citation-index="1" label="914">*914</page-number>against improper searches than the hurried judgment of a law enforcement officer ‘engaged in the often competitive enterprise of ferreting out crime,’ ” <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#9" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 9</a></span> (1977) (quoting <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948)), we have expressed a strong preference for warrants and declared that “in a doubtful or marginal case a search under a warrant may be sustainable where without one it would fall.” <em>United States </em>v. <em>Ventresca, </em><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#106" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 106</a></span> (1965). See <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#111" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 111</a></span>. Reasonable minds frequently may differ on the question whether a particular affidavit establishes probable cause, and we have thus concluded that the preference for warrants is most appropriately effectuated by according “great deference” to a magistrate’s determination. <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#419" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 419</a></span>. See <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#236" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 236</a></span>; <em>United States </em>v. <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca"><em>Ventresca, supra, </em>at 108-109</a></span>.</p>
<p id="b956-5">Deference to the magistrate, however, is not boundless. It is clear, first, that the deference accorded to a magistrate’s finding of probable cause does not preclude inquiry into the knowing or reckless falsity of the affidavit on which that determination was based. <em>Franks </em>v. <em>Delaware, </em><span class="citation" data-id="9427321"><a href="/opinion/109925/franks-v-delaware/" aria-description="Citation for case: Franks v. Delaware">438 U. S. 154</a></span> (1978).<footnotemark>12</footnotemark> Second, the courts must also insist that the magistrate purport to “perform his ‘neutral and detached’ function and not serve merely as a rubber stamp for the police.” <em>Aguilar </em>v. <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#111" aria-description="Citation for case: Aguilar v. Texas"><em>Texas, supra, </em>at 111</a></span>. See <em>Illinois </em>v. <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#239" aria-description="Citation for case: Illinois v. Gates"><em>Gates, supra, </em>at 239</a></span>. A magistrate failing to “manifest that neutrality and detachment demanded of a judicial officer when presented with a warrant application” and who acts instead as “an adjunct law enforcement officer” cannot provide valid authorization for an otherwise unconstitutional search. <em>Lo-Ji Sales, Inc. </em>v. <em>New York, </em><span class="citation" data-id="110100"><a href="/opinion/110100/lo-ji-sales-inc-v-new-york/#326" aria-description="Citation for case: Lo-Ji Sales, Inc. v. New York">442 U. S. 319, 326-327</a></span> (1979).</p>
<p id="b957-4"><page-number citation-index="1" label="915">*915</page-number>Third, reviewing courts will not defer to a warrant based on an affidavit that does not “provide the magistrate with a substantial basis for determining the existence of probable cause.” <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#239" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 239</a></span>. “Sufficient information must be presented to the magistrate to allow that official to determine probable cause; his action cannot be a mere ratification of the bare conclusions of others.” <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Ibid.</a></span> </em>See <em>Aguilar </em>v. <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#114" aria-description="Citation for case: Aguilar v. Texas"><em>Texas, supra, </em>at 114-115</a></span>; <em>Giordenello </em>v. <em>United States, 357 </em>U. S. 480 (1958); <em>Nathanson </em>v. <em>United States, </em><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span> (1933).<footnotemark>13</footnotemark> Even if the warrant application was supported by more than a “bare bones” affidavit, a reviewing court may properly conclude that, notwithstanding the deference that magistrates deserve, the warrant was invalid because the magistrate’s probable-cause determination reflected an improper analysis of the totality of the circumstances, <em>Illinois </em>v. <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#238" aria-description="Citation for case: Illinois v. Gates"><em>Gates, supra, </em>at 238-239</a></span>, or because the form of the warrant was improper in some respect.</p>
<p id="b957-5">Only in the first of these three situations, however, has the Court set forth a rationale for suppressing evidence obtained pursuant to a search warrant; in the other areas, it has simply excluded such evidence without considering whether <page-number citation-index="1" label="916">*916</page-number>Fourth Amendment interests will be advanced. To the extent that proponents of exclusion rely on its behavioral effects on judges and magistrates in these areas, their reliance is misplaced. First, the exclusionary rule is designed to deter police misconduct rather than to punish the errors of judges and magistrates. Second, there exists no evidence suggesting that judges and magistrates are inclined to ignore or subvert the Fourth Amendment or that lawlessness among these actors requires application of the extreme sanction of exclusion.<footnotemark>14</footnotemark></p>
<p id="b958-5">Third, and most important, we discern no basis, and are offered none, for believing that exclusion of evidence seized pursuant to a warrant will have a significant deterrent effect on the issuing judge or magistrate.<footnotemark>15</footnotemark> Many of the factors <page-number citation-index="1" label="917">*917</page-number>that indicate that the exclusionary rule cannot provide an effective “special” or “general” deterrent for individual offending law enforcement officers<footnotemark>16</footnotemark> apply as well to judges or magistrates. And, to the extent that the rule is thought to operate as a “systemic” deterrent on a wider audience,<footnotemark>17</footnotemark> it clearly can have no such effect on individuals empowered to issue search warrants. Judges and magistrates are not adjuncts to the law enforcement team; as neutral judicial officers, they have no stake in the outcome of particular criminal prosecutions. The threat of exclusion thus cannot be expected significantly to deter them. Imposition of the exclusionary sanction is not necessary meaningfully to inform judicial officers of their errors, and we cannot conclude that admitting evidence obtained pursuant to a warrant while at the same time declaring that the warrant was somehow defective will in any way reduce judicial officers’ professional incentives to comply with the Fourth Amendment, encourage them to repeat their mistakes, or lead to the granting of all colorable warrant requests.<footnotemark>18</footnotemark></p>
<p id="b960-4"><page-number citation-index="1" label="918">*918</page-number>B</p>
<p id="b960-5">If exclusion of evidence obtained pursuant to a subsequently invalidated warrant is to have any deterrent effect, therefore, it must alter the behavior of individual law enforcement officers or the policies of their departments. One could argue that applying the exclusionary rule in cases where the police failed to demonstrate probable cause in the warrant application deters future inadequate presentations or “magistrate shopping” and thus promotes the ends of the Fourth Amendment. Suppressing evidence obtained pursuant to a technically defective warrant supported by probable cause also might encourage officers to scrutinize more closely the form of the warrant and to point out suspected judicial errors. We find such arguments speculative and conclude that suppression of evidence obtained pursuant to a warrant should be ordered only on a case-by-case basis and only in those unusual cases in which exclusion will further the purposes of the exclusionary rule.<footnotemark>19</footnotemark></p>
<p id="b960-6">We have frequently questioned whether the exclusionary rule can have any deterrent effect when the offending officers acted in the objectively reasonable belief that their conduct did not violate the Fourth Amendment. “No empirical researcher, proponent or opponent of the rule, has yet been able to establish with any assurance whether the rule has a deterrent effect. . . .” <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#452" aria-description="Citation for case: United States v. Janis">428 U. S., at 452, n. 22</a></span>. But even assuming that the rule effectively <page-number citation-index="1" label="919">*919</page-number>deters some police misconduct and provides incentives for the law enforcement profession as a whole to conduct itself in accord with the Fourth Amendment, it cannot be expected, and should not be applied, to deter objectively reasonable law enforcement activity.</p>
<p id="b961-5">As we observed in <em>Michigan </em>v. <em>Tucker, </em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#447" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 447</a></span> (1974), and reiterated in <em>United States </em>v. <em>Peltier, </em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/" aria-description="Citation for case: United States v. Peltier">422 U. S., at 539</a></span>:</p>
<blockquote id="b961-6">“The deterrent purpose of the exclusionary rule necessarily assumes that the police have engaged in willful, or at the very least negligent, conduct which has deprived the defendant of some right. By refusing to admit evidence gained as a result of such conduct, the courts hope to instill in those particular investigating officers, or in their future counterparts, a greater degree of care toward the rights of an accused. Where the official action was pursued in complete good faith, however, the deterrence rationale loses much of its force.”</blockquote>
<p id="b961-7">The <em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/" aria-description="Citation for case: United States v. Peltier">Peltier</a></span> </em>Court continued, <em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/" aria-description="Citation for case: United States v. Peltier">id.,</a></span> </em>at 542:</p>
<blockquote id="b961-8">“If the purpose of the exclusionary rule is to deter unlawful police conduct, then evidence obtained from a search should be suppressed only if it can be said that the law enforcement officer had knowledge, or may properly be charged with knowledge, that the search was unconstitutional under the Fourth Amendment.”</blockquote>
<p id="b961-9">See also <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#260" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 260-261</a></span> (White, J., concurring in judgment); <em>United States </em>v. <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#459" aria-description="Citation for case: United States v. Janis"><em>Janis, supra, </em>at 459</a></span>; <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#610" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 610-611</a></span> (Powell, J., concurring in part).<footnotemark>20</footnotemark> In short, where the officer’s conduct is objectively reasonable,</p>
<blockquote id="b962-4"><page-number citation-index="1" label="920">*920</page-number>“excluding the evidence will not further the ends of the exclusionary rule in any appreciable way; for it is painfully apparent that. . . the officer is acting as a reasonable officer would and should act in similar circumstances. Excluding the evidence can in no way affect his future conduct unless it is to make him less willing to do his duty.” <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#539" aria-description="Citation for case: Stone v. Powell">428 U. S., at 539-540</a></span> (White, J., dissenting).</blockquote>
<p id="b962-5">This is particularly true, we believe, when an officer acting with objective good faith has obtained a search warrant from a judge or magistrate and acted within its scope.<footnotemark>21</footnotemark> In most <page-number citation-index="1" label="921">*921</page-number>such cases, there is no police illegality and thus nothing to deter. It is the magistrate’s responsibility to determine whether the officer’s allegations establish probable cause and, if so, to issue a warrant comporting in form with the requirements of the Fourth Amendment. In the ordinary case, an officer cannot be expected to question the magistrate’s probable-cause determination or his judgment that the form of the warrant is technically sufficient. “[Ojnce the warrant issues, there is literally nothing more the policeman can do in seeking to comply with the law.” <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#498" aria-description="Citation for case: Stone v. Powell"><em>Id., </em>at 498</a></span> (Burger, C. J., concurring). Penalizing the officer for the magistrate’s error, rather than his own, cannot logically contribute to the deterrence of Fourth Amendment violations.<footnotemark>22</footnotemark></p>
<p id="b964-4"><page-number citation-index="1" label="922">*922</page-number>c</p>
<p id="b964-5">We conclude that the marginal or nonexistent benefits produced by suppressing evidence obtained in objectively reasonable reliance on a subsequently invalidated search warrant cannot justify the substantial costs of exclusion. We do not suggest, however, that exclusion is always inappropriate in cases where an officer has obtained a warrant and abided by its terms. “[Searches pursuant to a warrant will rarely require any deep inquiry into reasonableness,” <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#267" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 267</a></span> (White, J., concurring in judgment), for “a warrant issued by a magistrate normally suffices to establish” that a law enforcement officer has “acted in good faith in conducting the search.” <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#823" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 823, n. 32</a></span> (1982). Nevertheless, the officer’s reliance on the magistrate’s probable-cause determination and on the technical sufficiency of the warrant he issues must be objectively reasonable, cf. <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#815" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 815-819</a></span> (1982),<footnotemark>23</footnotemark> and it is clear that in some eircum-<page-number citation-index="1" label="923">*923</page-number>stances the officer<footnotemark>24</footnotemark> will have no reasonable grounds for believing that the warrant was properly issued.</p>
<p id="b965-5">Suppression therefore remains an appropriate remedy if the magistrate or judge in issuing a warrant was misled by information in an affidavit that the affiant knew was false or would have known was false except for his reckless disregard of the truth. <em>Franks </em>v. <em>Delaware, </em><span class="citation" data-id="9427321"><a href="/opinion/109925/franks-v-delaware/" aria-description="Citation for case: Franks v. Delaware">438 U. S. 154</a></span> (1978). The exception we recognize today will also not apply in cases where the issuing magistrate wholly abandoned his judicial role in the manner condemned in <em>Lo-Ji Sales, Inc. </em>v. <em>New York, </em><span class="citation" data-id="110100"><a href="/opinion/110100/lo-ji-sales-inc-v-new-york/" aria-description="Citation for case: Lo-Ji Sales, Inc. v. New York">442 U. S. 319</a></span> (1979); in such circumstances, no reasonably well trained officer should rely on the warrant. Nor would an officer manifest objective good faith in relying on a warrant based on an affidavit “so lacking in indicia of probable cause as to render official belief in its existence entirely unreasonable.” <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#610" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 610-611</a></span> (Powell, J., concurring in part); see <em>Illinois </em>v. <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#263" aria-description="Citation for case: Illinois v. Gates"><em>Gates, supra, </em>at 263-264</a></span> (White, J., concurring in judgment). Finally, depending on the circumstances of the particular case, a warrant may be so facially <em>deficient </em>— i. <em>e., </em>in failing to particularize the place to be searched or the things to be seized— that the executing officers cannot reasonably presume it to be valid. Cf. <em>Massachusetts </em>v. <em>Sheppard, post, </em>at 988-991.</p>
<p id="b965-6">In so limiting the suppression remedy, we leave untouched the probable-cause standard and the various requirements for a valid warrant. Other objections to the modification of <page-number citation-index="1" label="924">*924</page-number>the Fourth Amendment exclusionary rule we consider to be insubstantial. The good-faith exception for searches conducted pursuant to warrants is not intended to signal our unwillingness strictly to enforce the requirements of the Fourth Amendment, and we do not believe that it will have this effect. As we have already suggested, the good-faith exception, turning as it does on objective reasonableness, should not be difficult to apply in practice. When officers have acted pursuant to a warrant, the prosecution should ordinarily be able to establish objective good faith without a substantial expenditure of judicial time.</p>
<p id="b966-5">Nor are we persuaded that application of a good-faith exception to searches conducted pursuant to warrants will preclude review of the constitutionality of the search or seizure, deny needed guidance from the courts, or freeze Fourth Amendment law in its present state.<footnotemark>25</footnotemark> There is no need for courts to adopt the inflexible practice of always deciding whether the officers’ conduct manifested objective good faith before turning to the question whether the Fourth Amendment has been violated. Defendants seeking suppression of the fruits of allegedly unconstitutional searches or seizures undoubtedly raise live controversies which Art. Ill empowers federal courts to adjudicate. As cases addressing questions of good-faith immunity under <span class="citation no-link">42 U. S. C. § 1983</span>, compare <em>O’Connor </em>v. Donaldson, <span class="citation" data-id="9842006"><a href="/opinion/109303/oconnor-v-donaldson/" aria-description="Citation for case: O&#x27;Connor v. Donaldson">422 U. S. 563</a></span> (1975), with <em>Procunier </em>v. <em>Navarette, </em><span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/#566" aria-description="Citation for case: Procunier v. Navarette">434 U. S. 555, 566, n. 14</a></span> (1978), and cases involving the harmless-error doctrine, compare <em>Milton </em>v. <em>Wainwright, </em><span class="citation" data-id="9424959"><a href="/opinion/108585/milton-v-wainwright/#372" aria-description="Citation for case: Milton v. Wainwright">407 U. S. 371, 372</a></span> (1972), with <em>Coleman </em>v. <em>Alabama, </em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span> (1970), make clear, courts have consid<page-number citation-index="1" label="925">*925</page-number>erable discretion in conforming their decisionmaking processes to the exigencies of particular cases.</p>
<p id="b967-5">If the resolution of a particular Fourth Amendment question is necessary to guide future action by law enforcement officers and magistrates, nothing will prevent reviewing courts from deciding that question before turning to the good-faith issue.<footnotemark>26</footnotemark> Indeed, it frequently will be difficult to determine whether the officers acted reasonably without resolving the Fourth Amendment issue. Even if the Fourth Amendment question is not one of broad import, reviewing courts could decide in particular cases that magistrates under their supervision need to be informed of their errors and so evaluate the officers’ good faith only after finding a violation. In other circumstances, those courts could reject suppression motions posing no important Fourth Amendment questions by turning immediately to a consideration of the officers’ good faith. We have no reason to believe that our Fourth Amendment jurisprudence would suffer by allowing reviewing courts to exercise an informed discretion in making this choice.</p>
<p id="b967-8">I<em>V</em></p>
<p id="b967-6">When the principles we have enunciated today are applied to the facts of this case, it is apparent that the judgment of the Court of Appeals cannot stand. The Court of Appeals applied the prevailing legal standards to Officer Rombach’s warrant application and concluded that the application could not support the magistrate’s probable-cause determination. In so doing, the court clearly informed the magistrate that he <page-number citation-index="1" label="926">*926</page-number>had erred in issuing the challenged warrant. This aspect of the court’s judgment is not under attack in this proceeding.</p>
<p id="b968-5">Having determined that the warrant should not have issued, the Court of Appeals understandably declined to adopt a modification of the Fourth Amendment exclusionary rule that this Court had not previously sanctioned. Although the modification finds strong support in our previous cases, the Court of Appeals’ commendable self-restraint is not to be criticized. We have now reexamined the purposes of the exclusionary rule and the propriety of its application in cases where officers have relied on a subsequently invalidated search warrant. Our conclusion is that the rule’s purposes will only rarely be served by applying it in such circumstances.</p>
<p id="b968-6">In the absence of an allegation that the magistrate abandoned his detached and neutral role, suppression is appropriate only if the officers were dishonest or reckless in preparing their affidavit or could not have harbored an objectively reasonable belief in the existence of probable cause. Only respondent Leon has contended that no reasonably well trained police officer could have believed that there existed probable cause to search his house; significantly, the other respondents advance no comparable argument. Officer Rombach’s application for a warrant clearly was supported by much more than a “bare bones” affidavit. The affidavit related the results of an extensive investigation and, as the opinions of the divided panel of the Court of Appeals make clear, provided evidence sufficient to create disagreement among thoughtful and competent judges as to the existence of probable cause. Under these circumstances, the officers’ reliance on the magistrate’s determination of probable cause was objectively reasonable, and application of the extreme sanction of exclusion is inappropriate.</p>
<p id="b968-7">Accordingly, the judgment of the Court of Appeals is</p>
<p id="b968-8">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b945-5"> Respondent Leon moved to suppress the evidence found on his person at the time of his arrest and the evidence seized from his residence at 716 South Sunset Canyon. Respondent Stewart’s motion covered the fruits of searches of her residence at 620 Price Drive and the condominium at 7902 Via Magdalena and statements she made during the search of her residence. Respondent Sanchez sought to suppress the evidence discovered during the search of his residence at 620 Price Drive and statements he made shortly thereafter. He also joined Stewart’s motion to suppress evidence seized from the condominium. Respondent Del Castillo apparently sought to suppress all of the evidence seized in the searches. App. 78-80. The respondents also moved to suppress evidence seized in the searches of their automobiles.</p>
</footnote>
<footnote label="2">
<p id="b945-6"> “I just cannot find this warrant sufficient for a showing of probable cause.</p>
<blockquote id="b945-7">“There is no question of the reliability and credibility of the informant as not being established.</blockquote>
<blockquote id="b945-8">“Some details given tended to corroborate, maybe, the reliability of [the informant’s] information about the previous transaction, but if it is not a stale transaction, it comes awfully close to it; and all the other material I think is as consistent with innocence as it is with guilt.</blockquote>
<blockquote id="b945-9">“So I just do not think this affidavit can withstand the test. I find, then, that there is no probable cause in this case for the issuance of the search warrant. . . .” <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#127" aria-description="Citation for case: Coleman v. Alabama"><em>Id., </em>at 127</a></span>.</blockquote>
</footnote>
<footnote label="3">
<p id="b945-10"> The District Court concluded that Sanchez and Stewart had standing to challenge the search of 620 Price Drive; that Leon had standing to contest the legality of the search of 716 South Sunset Canyon; that none of the respondents had established a legitimate expectation of privacy in the condominium at 7902 Via Magdalena; and that Stewart and Del Castillo each had standing to challenge the searches of their automobiles. The <page-number citation-index="1" label="904">*904</page-number>Government indicated that it did not intend to introduce evidence seized from the other respondents’ vehicles. <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#127" aria-description="Citation for case: Coleman v. Alabama"><em>Id., </em>at 127-129</a></span>. Finally, the court suppressed statements given by Sanchez and Stewart. <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#129" aria-description="Citation for case: Coleman v. Alabama"><em>Id., </em>at 129-130</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b946-9"><em> “On </em>the issue of good faith, obviously that is not the law of the Circuit, and I am not going to apply that law.</p>
<blockquote id="b946-10">“I will say certainly in my view, there is not any question about good faith. [Officer Rombach] went to a Superior Court judge and got a warrant; obviously laid a meticulous trail. Had surveilled for a long period of time, and I believe his testimony — and I think he said he consulted with three Deputy District Attorneys before proceeding himself, and I certainly have no doubt about the fact that that is true.” <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#140" aria-description="Citation for case: Coleman v. Alabama"><em>Id., </em>at 140</a></span>.</blockquote>
</footnote>
<footnote label="5">
<p id="b946-11"> In <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213</a></span> (1983), decided last Term, the Court abandoned the two-pronged <em>Aguilar-Spinelli </em>test for determining whether an informant’s tip suffices to establish probable cause for the issuance of a warrant and substituted in its place a “totality of the circumstances” approach.</p>
</footnote>
<footnote label="6">
<p id="b949-6"> Researchers have only recently begun to study extensively the effects of the exclusionary rule on the disposition of felony arrests. One study suggests that the rule results in the nonprosecution or nonconviction of between 0.6% and 2.35% of individuals arrested for felonies. Davies, A Hard Look at What We Know (and Still Need to Learn) About the “Costs” of the Exclusionary Rule: The NIJ Study and Other Studies of “Lost” Arrests, 1988 A. B. F. Res. J. 611, 621. The estimates are higher for particular crimes the prosecution of which depends heavily on physical evidence. Thus, the cumulative loss due to nonproseeution or noneonviction of individuals arrested on felony drug charges is probably in the range of 2.8% to 7.1%. <em>Id., </em>at 680. Davies’ analysis of California data suggests that screening by police and prosecutors results in the release because of illegal searches or seizures of as many as 1.4% of all felony arrestees, id., at 650, that 0.9% of felony arrestees are released, because of illegal searches or seizures, at the preliminary hearing or after trial, <em>id., </em>at 653, and that roughly 0.05% of all felony arrestees benefit from reversals on appeal because of illegal searches. <em>Id., </em>at 654. See also K. Brosi, A Cross-City Comparison of Felony Case Processing 16, 18-19 (1979); U. S. General Accounting Office, Report of the Comptroller General of the United States, Impact of the Exclusionary Rule on Federal Criminal Prosecutions 10-11, 14 (1979); F. Feeney, F. Dill, &amp; A. Weir, Arrests Without Convictions: How Often They Occur and Why 203-206 (National Institute of Justice <page-number citation-index="1" label="908">*908</page-number>1983); National Institute of Justice, The Effects of the Exclusionary Rule: A Study in California 1-2 (1982); Nardulli, The Societal Cost of the Exclusionary Rule: An Empirical Assessment, 1983 A. B. F. Res. J. 585, 600. The exclusionary rule also has been found to affect the plea-bargaining process. S. Schlesinger, Exclusionary Injustice: The Problem of Illegally Obtained Evidence 63 (1977). But see Davies, <em>supra, </em>at 668-669; Nardulli, <em>supra, </em>at 604-606.</p>
<p id="b950-8">Many of these researchers have concluded that the impact of the exclusionary rule is insubstantial, but the small percentages with which they deal mask a large absolute number of felons who are released because the cases against them were based in part on illegal searches or seizures. “[A]ny rule of evidence that denies the jury access to clearly probative and reliable evidence must bear a heavy burden of justification, and must be carefully limited to the circumstances in which it will pay its way by deterring official unlawlessness.” <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#257" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 257-258</a></span> (White, J., concurring in judgment). Because we find that the rule can have no substantial deterrent effect in the sorts of situations under consideration in this case, see <em>infra, </em>at 916-921, we conclude that it cannot pay its way in those situations.</p>
</footnote>
<footnote label="7">
<p id="b953-6"> <em>“Brown’s, </em>focus on ‘the causal connection between the illegality and the confession’ reflected the two policies behind the use of the exclusionary rule to effectuate the Fourth Amendment. Where there is a close causal connection between the illegal seizure and the confession, not only is exclusion of the evidence more likely to deter similar police misconduct in the future, but use of the evidence is more likely to compromise the integrity of the courts.” <em>Dunaway </em>v. <em>New York, </em>442 U. S., at 217-218 (citation omitted).</p>
</footnote>
<footnote label="8">
<p id="b954-5"> We have held, however, that the exclusionary rule requires suppression of evidence obtained in searches carried out pursuant to statutes, not yet declared unconstitutional, purporting to authorize searches and seizures without probable cause or search warrants. See, <em>e. g., Ybarra </em>v. <em>Illinois, </em><span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85</a></span> (1979); <em>Torres </em>v. <em>Puerto Rico, </em><span class="citation" data-id="9795098"><a href="/opinion/2620876/torres-v-puerto-rico/" aria-description="Citation for case: Torres v. Puerto Rico">442 U. S. 465</a></span> (1979); <em>Almeida-Sanchez </em>v. <em>United States, </em><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973); <em>Sibron </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span> (1968); <em>Berger </em>v. <em>New York, </em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967). “Those decisions involved statutes which, by their own terms, authorized searches under circumstances which did not satisfy the traditional warrant and probable-cause requirements of the Fourth Amendment.” <em>Michigan </em>v. <em>DeFillippo, </em><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/#39" aria-description="Citation for case: Michigan v. DeFillippo">443 U. S., at 39</a></span>. The substantive Fourth Amendment principles announced in those eases are fully consistent with our holding here.</p>
</footnote>
<footnote label="9">
<p id="AARi"> The Court held in <em>United States </em>v. <em>Johnson, </em>that a construction of the sFourth Amendment that did not constitute a “clear break with the past” is to be applied to all convictions not yet final when the decision was handed down. The limited holding, see 457 U. S., at 562, turned in part on the Court’s judgment that “[fjailure to accord <em>any </em>retroactive effect to Fourth Amendment rulings would ‘encourage police or other courts to disregard the plain purport of our decisions and to adopt a let’s-wait-until-it’s-decided approach.’” <em>Id., </em>at 561 (emphasis in original) (quoting <em>Desist </em>v. <em>United States, </em><span class="citation" data-id="9423951"><a href="/opinion/107875/desist-v-united-states/#277" aria-description="Citation for case: Desist v. United States">394 U. S. 244, 277</a></span> (1969) (Fortas, J., dissenting)). Contrary to respondents’ assertions, nothing in <em>Johnson </em>precludes adoption of a good-faith exception tailored to situations in which the police have reasonably relied on a warrant issued by a detached and neutral magistrate but later found to be defective.</p>
</footnote>
<footnote label="10">
<p id="b954-7"> Our retroactivity decisions have, for the most part, turned on our assessments of “(a) the purpose to be served by the new standards, (b) the extent of the reliance by law enforcement authorities on the old standards, and (c) the effect on the administration of justice of a retroactive application of the new standards.” <em>Stovall </em>v. <em>Denno, </em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#297" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293, 297</a></span> (1967). As we observed earlier this Term:</p>
<blockquote id="b955-5"><page-number citation-index="1" label="913">*913</page-number>“In considering the reliance factor, this Court’s cases have looked primarily to whether law enforcement authorities and state courts have justifiably relied on a prior rule of law said to be different from that announced by the decision whose retroactivity is at issue. Unjustified ‘reliance’ is no bar to retroactivity. This inquiry is often phrased in terms of whether the new decision was foreshadowed by earlier cases or was a ‘clear break with the past.’” <em>Solem </em>v. <em>Stumes, </em><span class="citation" data-id="9429516"><a href="/opinion/111112/solem-v-stumes/#645" aria-description="Citation for case: Solem v. Stumes">465 U. S. 638, 645-646</a></span> (1984).</blockquote>
</footnote>
<footnote label="11">
<p id="b955-6">Members of the Court have, however, urged reconsideration of the scope of the exclusionary rule. See, <em>e. g., Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#496" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 496</a></span> (1976) (Burgee, C. J., concurring); <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#536" aria-description="Citation for case: Stone v. Powell"><em>id., </em>at 536</a></span> (White, J., dissenting); <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#254" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 254-267</a></span> (White, J., concurring in judgment); <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#609" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590, 609-612</a></span> (1975) (Powell, J., concurring in part); <em>Schneckloth </em>v. <em>Bustamante, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#261" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 261-271</a></span> (1973) (Powell, J., concurring); <em>California </em>v. <em>Minjares, </em><span class="citation multiple-matches"><a href="/c/U.%20S./443/916/">443 U. S. 916</a></span> (1979) (Rehnquist, J., dissenting from denial of stay). One Court of Appeals, no doubt influenced by these individual urgings, has adopted a form of good-faith exception to the exclusionary rule. <em>United States </em>v. <em>Williams, </em><span class="citation" data-id="378896"><a href="/opinion/378896/united-states-v-jo-ann-williams/" aria-description="Citation for case: United States v. Jo Ann Williams">622 F. 2d 830</a></span> (CA5 1980) (en banc), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/1127/">449 U. S. 1127</a></span> (1981).</p>
</footnote>
<footnote label="12">
<p id="b956-6"> Indeed, <em>“it </em>would be an unthinkable imposition upon [the magistrate’s] authority if a warrant affidavit, revealed after the fact to contain a deliberately or recklessly false statement, were to stand beyond impeachment.” <span class="citation" data-id="9427321"><a href="/opinion/109925/franks-v-delaware/#165" aria-description="Citation for case: Franks v. Delaware">438 U. S., at 165</a></span>.</p>
</footnote>
<footnote label="13">
<p id="b957-6"> See also <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89</a></span> (1964), in which the Court concluded that “the record . . . does not contain a single objective fact to support a belief by the officers that the petitioner was engaged in criminal activity at the time they arrested him.” <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#95" aria-description="Citation for case: Beck v. Ohio"><em>Id., </em>at 95</a></span>. Although the Court was willing to assume that the arresting officers acted in good faith, it concluded:</p>
<blockquote id="b957-7">“‘[G]ood faith on the part of the arresting officers is not enough.’ <em>Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#102" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 102</a></span>. If subjective good faith alone were the test, the protections of the Fourth Amendment would evaporate, and the people would be ‘secure in their persons, houses, papers, and effects,’ only in the discretion of the police.” <em>Id., </em>at 97.</blockquote>
<p id="b957-8">We adhere to this view and emphasize that nothing in this opinion is intended to suggest a lowering of the probable-cause standard. On the contrary, we deal here only with the remedy to be applied to a concededly unconstitutional search.</p>
</footnote>
<footnote label="14">
<p id="b958-6">Although there are assertions that some magistrates become rubber stamps for the police and others may be unable effectively to screen police conduct, see, <em>e.g.,2 </em>W. LaFave, Search and Seizure §4.1 (1978); Kamisar, Does (Did) (Should) The Exclusionary Rule Rest on a “Principled Basis” Rather than an “Empirical Proposition”?, <span class="citation no-link">16 Creighton L. Rev. 565</span>, 569-571 (1983); Schroeder, Deterring Fourth Amendment Violations: Alternatives to the Exclusionary Rule, 69 Geo. L. J. 1361, 1412 (1981), we are not convinced that this is a problem of major proportions. See L. Tiffany, D. McIntyre, &amp; D. Rotenberg, Detection of Crime 119 (1967); Israel, Criminal Procedure, the Burger Court, and the Legacy of the Warren Court, <span class="citation no-link">75 Mich. L. Rev. 1319</span>, 1414, n. 396 (1977); P. Johnson, New Approaches to Enforcing the Fourth Amendment 8-10 (Working Paper, Sept. 1978), quoted in Y. Kamisar, W. LaFave, &amp; J. Israel, Modern Criminal Procedure 229-230 (5th ed. 1980); R. Van Duizend, L. Sutton, &amp; C. Carter, The Search Warrant Process, eh. 7 (Review Draft, National Center for State Courts, 1983).</p>
</footnote>
<footnote label="15">
<p id="b958-7"> As the Supreme Judicial Court of Massachusetts recognized in <em>Commonwealth </em>v. <em>Sheppard, </em><span class="citation" data-id="9541069"><a href="/opinion/2058560/commonwealth-v-sheppard/#506" aria-description="Citation for case: Commonwealth v. Sheppard">387 Mass. 488, 506</a></span>, <span class="citation" data-id="9541069"><a href="/opinion/2058560/commonwealth-v-sheppard/#735" aria-description="Citation for case: Commonwealth v. Sheppard">441 N. E. 2d 725, 735</a></span> (1982):</p>
<blockquote id="b958-8">“The exclusionary rule may not be well tailored to deterring judicial misconduct. If applied to judicial misconduct, the rule would be just as costly as it is when it is applied to police misconduct, but it may be ill-fitted to the job-created motivations of judges. . . . [IJdeally a judge is impartial as to whether a particular piece of evidence is admitted or a particular defendant convicted. Hence, in the abstract, suppression of a particular piece of evidence may not be as effective a disincentive to a neutral judge as it would be to the police. It may be that a ruling by an appellate court that a <page-number citation-index="1" label="917">*917</page-number>search warrant was unconstitutional would be sufficient to deter similar conduct in the future by magistrates.”</blockquote>
<p id="b959-6">But see <em>United States </em>v. <em>Karathanos, </em><span class="citation" data-id="9462518"><a href="/opinion/333763/united-states-v-steve-karathanos-and-john-karathanos/#33" aria-description="Citation for case: United States v. Steve Karathanos and John Karathanos">531 F. 2d 26, 33-34</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./428/910/">428 U. S. 910</a></span> (1976).</p>
</footnote>
<footnote label="16">
<p id="b959-7"> See, e. <em>g., Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#498" aria-description="Citation for case: Stone v. Powell">428 U. S., at 498</a></span> (Burger, C. J., concurring); Oaks, Studying the Exclusionary Rule in Search and Seizure, <span class="citation no-link">37 U. Chi. L. Rev. 665</span>, 709-710 (1970).</p>
</footnote>
<footnote label="17">
<p id="b959-8">See, <em>e. g., Dunaway </em>v. <em>New York, </em><span class="citation multiple-matches"><a href="/c/U.%20S./442/220/">442 U. S. 220</a></span>, 221 (1979) (Stevens, J., concurring); Mertens &amp; Wasserstrom, The Good Faith Exception to the Exclusionary Rule: Deregulating the Police and Derailing the Law, 70 Geo. L. J. 365, 399-401 (1981).</p>
</footnote>
<footnote label="18">
<p id="b959-9"> Limiting the application of the exclusionary sanction may well increase the care with which magistrates scrutinize warrant applications. We doubt that magistrates are more desirous of avoiding the exclusion of evidence obtained pursuant to warrants they have issued than of avoiding invasions of privacy.</p>
<p id="b959-10">Federal magistrates, moreover, are subject to the direct supervision of district courts. They may be removed for “incompeteney, misconduct, neglect of duty, or physical or mental disability.” <span class="citation no-link">28 U. S. C. §631</span>(i). If a magistrate serves merely as a “rubber stamp” for the police or is <page-number citation-index="1" label="918">*918</page-number>unable to exercise mature judgment, closer supervision or removal provides a more effective remedy than the exclusionary rule.</p>
</footnote>
<footnote label="19">
<p id="b960-8"> Our discussion of the deterrent effect of excluding evidence obtained in reasonable reliance on a subsequently invalidated warrant assumes, of course, that the officers properly executed the warrant and searched only those places and for those objects that it was reasonable to believe were covered by the warrant. Cf. <em>Massachusetts </em>v. <em>Sheppard, post, </em>at 989, n. 6 (“[I]t was not unreasonable for the police in this case to rely on the judge’s assurances that the warrant authorized the search they had requested”).</p>
</footnote>
<footnote label="20">
<p id="b961-10"> We emphasize that the standard of reasonableness we adopt is an objective one. Many objections to a good-faith exception assume that the exception will turn on the subjective good faith of individual officers. “Grounding the modification in objective reasonableness, however, retains <page-number citation-index="1" label="920">*920</page-number>the value of the exclusionary rule as an incentive for the law enforcement profession as a whole to conduct themselves in accord with the Fourth Amendment.” <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#261" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 261, n. 15</a></span> (White, J., concurring in judgment); see <em>Dunaway </em>v. <em>New York, </em>442 U. S., at 221 (Stevens, J., concurring). The objective standard we adopt, moreover, requires officers to have a reasonable knowledge of what the law prohibits. <em>United States </em>v. <em>Peltier, </em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#542" aria-description="Citation for case: United States v. Peltier">422 U. S. 531, 542</a></span> (1975). As Professor Jerold Israel has observed:</p>
<blockquote id="b962-7">“The key to the [exclusionary] rule’s effectiveness as a deterrent lies, I believe, in the impetus it has provided to police training programs that make officers aware of the limits imposed by the fourth amendment and emphasize the need to operate within those limits. [An objective good-faith exception] is not likely to result in the elimination of such programs, which are now viewed as an important aspect of police professionalism. Neither is it likely to alter the tenor of those programs; the possibility that illegally obtained evidence may be admitted in borderline cases is unlikely to encourage police instructors to pay less attention to fourth amendment limitations. Finally, [it] should not encourage officers to pay less attention to what they are taught, as the requirement that the officer act in ‘good faith’ is inconsistent with closing one’s mind to the possibility of illegality.” Israel, <em>supra </em>n. 14, at 1412-1413 (footnotes omitted).</blockquote>
</footnote>
<footnote label="21">
<p id="b962-8"> According <em>to </em>the Attorney General’s Task Force on Violent Crime, Final Report (1981), the situation in which an officer relies on a duly authorized warrant</p>
<blockquote id="b962-9">“is a particularly compelling example of good faith. A warrant is a judicial mandate to an officer to conduct a search or make an arrest, and the officer has a sworn duty to carry out its provisions. Accordingly, we believe that <page-number citation-index="1" label="921">*921</page-number>there should be a rule which states that evidence obtained pursuant to and within the scope of a warrant is prima facie the result of good faith on the part of the officer seizing the evidence.” <em>Id., </em>at 55.</blockquote>
</footnote>
<footnote label="22">
<p id="b963-6"> To the extent that Justice Stevens’ conclusions concerning the integrity of the courts, <em>post, </em>at 976-978, rest on a foundation other than his judgment, which we reject, concerning the effects of our decision on the deterrence of police illegality, we find his argument unpersuasive. “Judicial integrity clearly does not mean that the courts must never admit evidence obtained in violation of the Fourth Amendment.” <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#458" aria-description="Citation for case: United States v. Janis">428 U. S. 433, 458, n. 35</a></span> (1976). “While courts, of course, must ever be concerned with preserving the integrity of the judicial process, this concern has limited force as a justification for the exclusion of highly probative evidence.” <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#485" aria-description="Citation for case: Stone v. Powell">428 U. S., at 485</a></span>. Our cases establish that the question whether the use of illegally obtained evidence in judicial proceedings represents judicial participation in a Fourth Amendment violation and offends the integrity of the courts</p>
<blockquote id="b963-7">“is essentially the same as the inquiry into whether exclusion would serve a deterrent purpose. . . . The analysis showing that exclusion in this case has no demonstrated deterrent effect and is unlikely to have any significant such effect shows, by the same reasoning, that the admission of the evidence is unlikely to encourage violations of the Fourth Amendment.” <em>United States </em>v. <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#459" aria-description="Citation for case: United States v. Janis"><em>Janis, supra, </em>at 459, n. 35</a></span>.</blockquote>
<p id="b963-8">Absent unusual circumstances, when a Fourth Amendment violation has occurred because the police have reasonably relied on a warrant issued by a detached and neutral magistrate but ultimately found to be defective, “the <page-number citation-index="1" label="922">*922</page-number>integrity of the courts is not implicated.” <em>Illinois </em>v. <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#259" aria-description="Citation for case: Illinois v. Gates"><em>Gates, supra, </em>at 259, n. 14</a></span> (White, J., concurring in judgment). See <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#485" aria-description="Citation for case: Stone v. Powell">428 U. S., at 485, n. 23</a></span>; <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#540" aria-description="Citation for case: Stone v. Powell"><em>id., </em>at 540</a></span> (White, J., dissenting); <em>United States </em>v. <em>Peltier, </em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#536" aria-description="Citation for case: United States v. Peltier">422 U. S. 531, 536-539</a></span> (1975).</p>
</footnote>
<footnote label="23">
<p id="b964-7"> In <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span>, </em>we eliminated the subjective component of the qualified immunity public officials enjoy in suits seeking damages for alleged deprivations of constitutional rights. The situations are not perfectly analogous, but we also eschew inquiries into the subjective beliefs of law enforcement officers who seize evidence pursuant to a subsequently invalidated warrant. Although we have suggested that, “[o]n occasion, the motive with which the officer conducts an illegal search may have some relevance in determining the propriety of applying the exclusionary rule,” <em>Scott </em>v. <em>United States, </em><span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#139" aria-description="Citation for case: Scott v. United States">436 U. S. 128, 139, n. 13</a></span> (1978), we believe that “sending state and federal courts on an expedition into the minds of police officers would produce a grave and fruitless misallocation of judicial resources.” <em>Massachusetts </em>v. <em>Painten, </em><span class="citation" data-id="9423573"><a href="/opinion/107577/massachusetts-v-painten/#565" aria-description="Citation for case: Massachusetts v. Painten">389 U. S. 560, 565</a></span> (1968) (White, J., dissenting). Accordingly, our good-faith inquiry is confined to the objectively ascertainable question whether a reasonably well trained officer would have known that the search was illegal despite the magistrate’s authorization. In making this determination, all of the circumstances— <page-number citation-index="1" label="923">*923</page-number>including whether the warrant application had previously been rejected by a different magistrate — may be considered.</p>
</footnote>
<footnote label="24">
<p id="b965-8"> References to “officer” throughout this opinion should not be read too narrowly. It is necessary to consider the objective reasonableness, not only of the officers who eventually executed a warrant, but also of the officers who originally obtained it or who provided information material to the probable-cause determination. Nothing in our opinion suggests, for example, that an officer could obtain a warrant on the basis of a “bare bones” affidavit and then rely on colleagues who are ignorant of the circumstances under which the warrant was obtained to conduct the search. See <em>Whiteley </em>v. <em>Warden, </em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/#568" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560, 568</a></span> (1971).</p>
</footnote>
<footnote label="25">
<p id="b966-6"> The argument that defendants will lose their incentive to litigate meritorious Fourth Amendment claims as a result of the good-faith exception we adopt today is unpersuasive. Although the exception might discourage presentation of insubstantial suppression motions, the magnitude of the benefit conferred on defendants by a successful motion makes it unlikely that litigation of colorable claims will be substantially diminished.</p>
</footnote>
<footnote label="26">
<p id="b967-7"> It has been suggested, in fact, that “the recognition of a ‘penumbral zone,’ within which an inadvertent mistake would not call for exclusion, . . . will make it less tempting forjudges to bend fourth amendment standards to avoid releasing a possibly dangerous criminal because of a minor and unintentional miscalculation by the police.” Sehroeder, <em>supra </em>n. 14, at 1420-1421 (footnote omitted); see Ashdown, Good Faith, the Exclusionary Remedy, and Rule-Oriented Adjudication in the Criminal Process, <span class="citation no-link">24 Wm. &amp; Mary L. Rev. 335</span>, 383-384 (1983).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Martinez-Fuerte.md  (`case`, 6 assertions)

### content_page

```
---
title: "United States v. Martinez-Fuerte"
type: case
citation: "428 U.S. 543 (1976)"
parallel_cite: "96 S. Ct. 3074; 49 L. Ed. 2d 1116"
neutral_cite: 1976 U.S. LEXIS 87
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-07-06
docket: 74-1560
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-07-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Martinez-Fuerte
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109541/united-states-v-martinez-fuerte/"
  cluster_id: 109541
  opinion_id: 109541
  identity_checked: true
homes:
  - page: "[[Border Searches]]"
    role: "Key — Anchor"
  - page: "[[Checkpoints and Roadblocks]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Brignoni-Ponce]]", "[[Almeida-Sanchez v. United States]]", "[[Michigan Dept. of State Police v. Sitz]]", "[[City of Indianapolis v. Edmond]]"]
aliases: []
tags: ["case", "fourth-amendment", "border-searches", "immigration-checkpoint", "fixed-checkpoint", "individualized-suspicion"]
holding: "Brief stops at fixed/permanent interior immigration checkpoints are constitutional without any individualized suspicion; routine…"
lake:
  record_id: United States v. Martinez-Fuerte
  status: verified
  projected_at: 2026-07-09
---

# United States v. Martinez-Fuerte

*428 U.S. 543 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
At the San Clemente, California fixed immigration checkpoint on Interstate 5 — a permanent, clearly marked installation well inside the border — Border Patrol agents stopped passing vehicles for brief questioning about citizenship and referred some cars to a secondary inspection area. Martinez-Fuerte and other defendants were prosecuted for transporting illegal aliens found through these stops. They challenged the checkpoint stops and the secondary referrals as unreasonable seizures.

## Issue
Whether routine stops for brief questioning at a permanent immigration checkpoint, and selective referral of motorists to a secondary inspection area, are consistent with the Fourth Amendment when conducted without individualized suspicion or a warrant.

## Rule
Yes. "In summary, we hold that stops for brief questioning routinely conducted at permanent checkpoints are consistent with the Fourth Amendment and need not be authorized by warrant." — 428 U.S. at 566. ^pin-566

No individualized suspicion is required for the initial stop: "Accordingly, we hold that the stops and questioning at issue may be made in the absence of any individualized suspicion at reasonably located checkpoints." — [*Id.* at 562](https://www.courtlistener.com/opinion/109541/united-states-v-martinez-fuerte/#:~:text=Accordingly%2C%20we%20hold%20that%20the). ^pin-562

Nor must referral to secondary inspection meet the roving-patrol standard: "We further believe that it is constitutional to refer motorists selectively to the secondary inspection area at the San Clemente checkpoint on the basis of criteria that would not sustain a roving-patrol stop. Thus, even if it be assumed that such referrals are made largely on the basis of apparent Mexican ancestry, we perceive no constitutional violation." — *Id.* at 563. ^pin-563

## Application
On these facts the checkpoint procedures were reasonable. The San Clemente checkpoint was fixed and permanent, so motorists had advance notice and the stops were brief, predictable, and minimally intrusive — unlike the roving patrols that *[[United States v. Brignoni-Ponce|Brignoni-Ponce]]* required to be supported by reasonable suspicion. The public interest in policing the border, and the impracticality of demanding individualized suspicion for each of the many vehicles passing a high-volume checkpoint, justified the suspicionless stops; the decision to seize was governed by the location of the checkpoint and the judgment of higher-ranking officials, not the unbridled discretion of the field officer. Because the intrusion of a secondary referral was also minimal, that referral did not require reasonable suspicion. The stops and referrals of these defendants were therefore constitutional.

## Conclusion
Routine stops and secondary referrals at permanent immigration checkpoints are reasonable under the Fourth Amendment without individualized suspicion or a warrant; Martinez-Fuerte's conviction was affirmed and the contrary judgments reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Martinez-Fuerte* is the foundational fixed-checkpoint case, distinguished from roving patrols ([[United States v. Brignoni-Ponce]], [[Almeida-Sanchez v. United States]]) and later defining the suspicionless-checkpoint line applied in [[Michigan Dept. of State Police v. Sitz]] (sobriety checkpoints upheld) and limited in [[City of Indianapolis v. Edmond]] (general crime-control checkpoints struck down).

## Appears on
- [[Border Searches]] — *Key — Anchor*

## Sources
- *United States v. Martinez-Fuerte*, 428 U.S. 543 (1976) — https://www.courtlistener.com/opinion/109541/united-states-v-martinez-fuerte/ — pinpoints: 562, 563, 566.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f4d4da00864ae0b9", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "428 U.S. 543 (1976)", "court": "U.S. Supreme Court", "neutral_cite": "1976 U.S. LEXIS 87", "official_citation_present": true, "parallel_cite": "96 S. Ct. 3074; 49 L. Ed. 2d 1116", "title": "United States v. Martinez-Fuerte", "year": "1976"}}
{"assertion_id": "454f4f1f5cb325b6", "dimension": "support", "kind": "home_role", "locator": {"home": "Border Searches"}, "payload": {"home": "Border Searches", "role": "Key — Anchor", "title": "United States v. Martinez-Fuerte"}}
{"assertion_id": "4ef4f9fb4dd09162", "dimension": "support", "kind": "home_role", "locator": {"home": "Checkpoints and Roadblocks"}, "payload": {"home": "Checkpoints and Roadblocks", "role": "Related (cross-doctrine)", "title": "United States v. Martinez-Fuerte"}}
{"assertion_id": "e42bd31c78a22352", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Brief stops at fixed/permanent interior immigration checkpoints are constitutional without any individualized suspicion; routine…", "title": "United States v. Martinez-Fuerte"}}
{"assertion_id": "03ac139ec7a06832", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Martinez-Fuerte"}}
{"assertion_id": "8dcd607ef03609b1", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1976-07-06", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Martinez-Fuerte", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Martinez-Fuerte", "varies_by_point": "false"}}
```

### lake record — United States v. Martinez-Fuerte

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Martinez-Fuerte",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Martinez-Fuerte",
    "case_name_short": "Martinez-Fuerte",
    "case_name_full": "UNITED STATES v. MARTINEZ-FUERTE Et Al.",
    "input_case_name": "United States v. Martinez-Fuerte",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-07-06",
    "year": 1976,
    "docket": "74-1560",
    "cluster_id": 109541,
    "lead_opinion_id": 109541,
    "sibling_ids": [
      109541,
      9426591,
      9426592
    ],
    "absolute_url": "/opinion/109541/united-states-v-martinez-fuerte/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "428 U.S. 543",
      "volume": "428",
      "reporter": "U.S.",
      "page": "543",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 3074",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "3074",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 1116",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "1116",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 87",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "87",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "428 U.S. 543",
        "volume": "428",
        "reporter": "U.S.",
        "page": "543",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 3074",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "3074",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 1116",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "1116",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 87",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "87",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "428 U.S. 543",
    "official_selection": {
      "court_class": "scotus",
      "selected": "428 U.S. 543",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-566",
      "page": null,
      "quote": "--- # United States v. Martinez-Fuerte *428 U.S. 543 (1976)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background At the San Clemente, California fixed immigration checkpoint on Interstate 5 \u2014 a permanent, clearly marked installation well inside the border \u2014 Border Patrol agents stopped passing vehicles for brief questioning about citizenship and referred some cars to a secondary inspection area. Martinez-Fuerte and other defendants were prosecuted for transporting illegal aliens found through these stops. They challenged the checkpoint stops and the secondary referrals as unreasonable seizures. ## Issue Whether routine stops for brief questioning at a permanent immigration checkpoint, and selective referral of motorists to a secondary inspection area, are consistent with the Fourth Amendment when conducted without individualized suspicion or a warrant. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-562",
      "page": null,
      "quote": "Accordingly, we hold that the stops and questioning at issue may be made in the absence of any individualized suspicion at reasonably located checkpoints.",
      "star_marker": "562",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 36917,
      "fragment": "#:~:text=Accordingly%2C%20we%20hold%20that%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-563",
      "page": null,
      "quote": "We further believe that it is constitutional to refer motorists selectively to the secondary inspection area at the San Clemente checkpoint on the basis of criteria that would not sustain a roving-patrol stop. Thus, even if it be assumed that such referrals are made largely on the basis of apparent Mexican ancestry, we perceive no constitutional violation.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-07-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Martinez-Fuerte",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Cobb",
          "cluster_id": 9352626,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cobb",
          "cluster_id": 6466320,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ashworth",
          "cluster_id": 4243394,
          "cite": [
            "790 S.E.2d 173",
            "248 N.C. App. 649",
            "2016 N.C. App. LEXIS 816"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Warren",
          "cluster_id": 2806866,
          "cite": [
            "87 Mass. App. Ct. 476"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kenneth Lee Douds v. State",
          "cluster_id": 2983813,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Price",
          "cluster_id": 2728832,
          "cite": [
            "233 N.C. App. 386",
            "757 S.E.2d 309",
            "2014 WL 1366446",
            "2014 N.C. App. LEXIS 317"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bell v. Wolfish",
          "cluster_id": 110075,
          "cite": [
            "60 L. Ed. 2d 447",
            "99 S. Ct. 1861",
            "441 U.S. 520",
            "1979 U.S. LEXIS 100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whren v. United States",
          "cluster_id": 118036,
          "cite": [
            "135 L. Ed. 2d 89",
            "116 S. Ct. 1769",
            "517 U.S. 806",
            "1996 U.S. LEXIS 3720"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mendenhall",
          "cluster_id": 110264,
          "cite": [
            "64 L. Ed. 2d 497",
            "100 S. Ct. 1870",
            "446 U.S. 544",
            "1980 U.S. LEXIS 102"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Delaware v. Prouse",
          "cluster_id": 110045,
          "cite": [
            "59 L. Ed. 2d 660",
            "99 S. Ct. 1391",
            "440 U.S. 648",
            "1979 U.S. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dunaway v. New York",
          "cluster_id": 110096,
          "cite": [
            "60 L. Ed. 2d 824",
            "99 S. Ct. 2248",
            "442 U.S. 200",
            "1979 U.S. LEXIS 126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Mimms",
          "cluster_id": 109751,
          "cite": [
            "54 L. Ed. 2d 331",
            "98 S. Ct. 330",
            "434 U.S. 106",
            "1977 U.S. LEXIS 157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Texas",
          "cluster_id": 110128,
          "cite": [
            "61 L. Ed. 2d 357",
            "99 S. Ct. 2637",
            "443 U.S. 47",
            "1979 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ybarra v. Illinois",
          "cluster_id": 110158,
          "cite": [
            "62 L. Ed. 2d 238",
            "100 S. Ct. 338",
            "444 U.S. 85",
            "1979 U.S. LEXIS 151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Summers",
          "cluster_id": 110534,
          "cite": [
            "69 L. Ed. 2d 340",
            "101 S. Ct. 2587",
            "452 U.S. 692",
            "1981 U.S. LEXIS 118",
            "49 U.S.L.W. 4776"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. Delgado",
          "cluster_id": 111148,
          "cite": [
            "80 L. Ed. 2d 247",
            "104 S. Ct. 1758",
            "466 U.S. 210",
            "1984 U.S. LEXIS 57",
            "52 U.S.L.W. 4436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Bertine",
          "cluster_id": 111788,
          "cite": [
            "93 L. Ed. 2d 739",
            "107 S. Ct. 738",
            "479 U.S. 367",
            "1987 U.S. LEXIS 286",
            "55 U.S.L.W. 4105"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arkansas v. Sanders",
          "cluster_id": 110119,
          "cite": [
            "61 L. Ed. 2d 235",
            "99 S. Ct. 2586",
            "442 U.S. 753",
            "1979 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
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
        "journal_ref": "United States v. Martinez-Fuerte:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109541 OR 9426591 OR 9426592) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzAyNzM5MjAwMDAwJnM9MjQ4NDY3MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109541+OR+9426591+OR+9426592%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 11,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 11,
        "triage_snippet_classified": 189
      },
      "lane2_top_cited": {
        "query": "cites:(109541 OR 9426591 OR 9426592)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02MDQmcz0xMTEzODImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109541+OR+9426591+OR+9426592%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109541 OR 9426591 OR 9426592)",
        "reviewed": 21,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 21,
        "triage_read": 0,
        "triage_snippet_classified": 21
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109541 OR 9426591 OR 9426592)",
    "indexed_citing_opinions": 1385,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109541,
        "count": 1267,
        "count_source": "search"
      },
      {
        "opinion_id": 9426591,
        "count": 162,
        "count_source": "search"
      },
      {
        "opinion_id": 9426592,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2153,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-martinez-fuerte.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg0Njk5OTYmcz05NDMwNzA2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109541+OR+9426591+OR+9426592%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109541,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 109313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 109332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 109504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 109522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 319859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 320555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 320688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 326898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109541,
        "cited_id": 1802688,
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
    "date_created": "2026-07-06T01:26:35Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:26:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:26:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:29:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:26:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Martinez-Fuerte

```
<div>
<center><b><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U.S. 543</a></span> (1976)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
MARTINEZ-FUERTE ET AL.</h1></center>
<center>No. 74-1560.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued April 26, 1976.</center>
<center>Decided July 6, 1976.<sup>[*]</sup></center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><span class="star-pagination">*544</span> <i>Mark L. Evans</i> argued the cause for the United States in both cases. With him on the briefs were <i>Solicitor General Bork, Assistant Attorney General Thornburgh,</i> and <i>Sidney M. Glazer.</i></p>
<p><i>Ballard Bennett,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./423/1030/">423 U. S. 1030</a></span>, argued the cause and filed briefs for petitioner in No. 75-5387.</p>
<p><i>Charles M. Sevilla,</i> by appointment of the Court, <span class="citation" data-id="8998003"><a href="/opinion/9005294/payton-v-united-states-court-of-appeals-for-the-seventh-circuit/" aria-description="Citation for case: Payton v. United States Court of Appeals for the Seventh...">423 U. S. 922</a></span>, argued the cause for respondents in No. 74-1560. With him on the brief was <i>Michael J. McCabe.</i><sup>[]</sup></p>
<p><span class="star-pagination">*545</span> MR. JUSTICE POWELL delivered the opinion of the Court.</p>
<p>These cases involve criminal prosecutions for offenses relating to the transportation of illegal Mexican aliens. Each defendant was arrested at a permanent checkpoint operated by the Border Patrol away from the international border with Mexico, and each sought the exclusion of certain evidence on the ground that the operation of the checkpoint was incompatible with the Fourth Amendment. In each instance whether the Fourth Amendment was violated turns primarily on whether a vehicle may be stopped at a fixed checkpoint for brief questioning of its occupants even though there is no reason to believe the particular vehicle contains illegal aliens. We reserved this question last Term in <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891</a></span>, 897 n. 3 (1975). We hold today that such stops are consistent with the Fourth Amendment. We also hold that the operation of a fixed checkpoint need not be authorized in advance by a judicial warrant.</p>
<p></p>
<h2>I</h2>
<p></p>
<h2>A</h2>
<p>The respondents in No. 74-1560 are defendants in three separate prosecutions resulting from arrests made on three different occasions at the permanent immigration checkpoint on Interstate 5 near San Clemente, Cal. Interstate 5 is the principal highway between San Diego and Los Angeles, and the San Clemente checkpoint is 66 road miles north of the Mexican border. We previously have described the checkpoint as follows:</p>
<blockquote>" `Approximately one mile south of the checkpoint is a large black on yellow sign with flashing yellow lights over the highway stating "ALL VEHICLES, STOP AHEAD, 1 MILE." Three-quarters of a <span class="star-pagination">*546</span> mile further north are two black on yellow signs suspended over the highway with flashing lights stating "WATCH FOR BRAKE LIGHTS." At the checkpoint, which is also the location of a State of California weighing station, are two large signs with flashing red lights suspended over the highway. These signs each state "STOP HEREU. S. OFFICERS." Placed on the highway are a number of orange traffic cones funneling traffic into two lanes where a Border Patrol agent in full dress uniform, standing behind a white on red "STOP" sign checks traffic. Blocking traffic in the unused lanes are official U. S. Border Patrol vehicles with flashing red lights. In addition, there is a permanent building which houses the Border Patrol office and temporary detention facilities. There are also floodlights for nighttime operation.' " <i>United States</i> v. <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#893" aria-description="Citation for case: United States v. Ortiz"><i>Ortiz, supra,</i> at 893</a></span>, quoting <i>United States</i> v. <i>Baca,</i> <span class="citation" data-id="1802688"><a href="/opinion/1802688/united-states-v-baca/#410" aria-description="Citation for case: United States v. Baca">368 F. Supp. 398, 410-411</a></span> (SD Cal. 1973).</blockquote>
<p>The "point" agent standing between the two lanes of traffic visually screens all northbound vehicles, which the checkpoint brings to a virtual, if not a complete, halt.<sup>[1]</sup> Most motorists are allowed to resume their progress without any oral inquiry or close visual examination. In a relatively small number of cases the "point" agent will conclude that further inquiry is in order. He directs these cars to a secondary inspection area, where their occupants are asked about their citizenship and immigration status. The Government informs us that at San <span class="star-pagination">*547</span> Clemente the average length of an investigation in the secondary inspection area is three to five minutes. Brief for United States 53. A direction to stop in the secondary inspection area could be based on something suspicious about a particular car passing through the checkpoint, but the Government concedes that none of the three stops at issue in No. 74-1560 was based on any articulable suspicion. During the period when these stops were made, the checkpoint was operating under a magistrate's "warrant of inspection," which authorized the Border Patrol to conduct a routine-stop operation at the San Clemente location.<sup>[2]</sup></p>
<p>We turn now to the particulars of the stops involved in No. 74-1560. and the procedural history of the case. Respondent Amado Martinez-Fuerte approached the checkpoint driving a vehicle containing two female passengers. The women were illegal Mexican aliens who had entered the United States at the San Ysidro port of entry by using false papers and rendezvoused with Martinez-Fuerte in San Diego to be transported northward. At the checkpoint their car was directed to the secondary inspection area. Martinez-Fuerte produced documents showing him to be a lawful resident alien, but his passengers admitted being present in the country unlawfully. He was charged, <i>inter alia,</i> with two counts of illegally transporting aliens in violation <span class="star-pagination">*548</span> of <span class="citation no-link">8 U. S. C. § 1324</span> (a) (2). He moved before trial to suppress all evidence stemming from the stop on the ground that the operation of the checkpoint was in violation of the Fourth Amendment.<sup>[3]</sup> The motion to suppress was denied, and he was convicted on both counts after a jury trial.</p>
<p>Respondent Jose Jiminez-Garcia attempted to pass through the checkpoint while driving a car containing one passenger. He had picked the passenger up by prearrangement in San Ysidro after the latter had been smuggled across the border. Questioning at the secondary inspection area revealed the illegal status of the passenger, and Jiminez-Garcia was charged in two counts with illegally transporting an alien. <span class="citation no-link">8 U. S. C. § 1324</span> (a) (2), and conspiring to commit that offense, <span class="citation no-link">18 U. S. C. § 371</span>. His motion to suppress the evidence derived from the stop was granted.</p>
<p>Respondents Raymond Guillen and Fernando Medrano-Barragan approached the checkpoint with Guillen driving and Medrano-Barragan and his wife as passengers. Questioning at the secondary inspection area revealed that Medrano-Barragan and his wife were illegal aliens. A subsequent search of the car uncovered three other illegal aliens in the trunk. Medrano-Barragan had led the other aliens across the border at the beach near Tijuana, Mexico, where they rendezvoused with Guillen, a United States citizen. Guillen and Medrano-Barragan were jointly indicted on four counts of illegally transporting <span class="star-pagination">*549</span> aliens. <span class="citation no-link">8 U. S. C. § 1324</span> (a) (2), four counts of inducing the illegal entry of aliens, § 1324 (a) (4), and one conspiracy count, <span class="citation no-link">18 U. S. C. § 371</span>. The District Court granted the defendants' motion to suppress.</p>
<p>Martinez-Fuerte appealed his conviction, and the Government appealed the granting of the motions to suppress in the respective prosecutions of Jiminez-Garcia and of Guillen and Medrano-Barragan.<sup>[4]</sup> The Court of Appeals for the Ninth Circuit consolidated the three appeals, which presented the common question whether routine stops and interrogations at checkpoints are consistent with the Fourth Amendment.<sup>[5]</sup> The Court of Appeals held, with one judge dissenting, that these stops violated the Fourth Amendment, concluding that a stop for inquiry is constitutional only if the Border Patrol reasonably suspects the presence of illegal aliens on the basis of articulable facts. It reversed Martinez-Fuerte's conviction, and affirmed the orders to suppress in the other cases. <span class="citation multiple-matches"><a href="/c/F.%202d/514/308/">514 F. 2d 308</a></span> (1975). We reverse and remand.</p>
<p></p>
<h2>B</h2>
<p>Petitioner in No. 75-5387, Rodolfo Sifuentes, was arrested at the permanent immigration checkpoint on U. S. Highway 77 near Sarita. Tex. Highway 77 originates in Brownsville, and it is one of the two major highways running north from the lower Rio Grande valley. The Sarita checkpoint is about 90 miles north of Brownsville, <span class="star-pagination">*550</span> and 65-90 miles from the nearest points of the Mexican border. The physical arrangement of the checkpoint resembles generally that at San Clemente, but the checkpoint is operated differently in that the officers customarily stop all northbound motorists for a brief inquiry. Motorists whom the officers recognize as local inhabitants, however, are waved through the checkpoint without inquiry. Unlike the San Clemente checkpoint the Sarita operation was conducted without a judicial warrant.</p>
<p>Sifuentes drove up to the checkpoint without any visible passengers. When an agent approached the vehicle, however, he observed four passengers, one in the front seat and the other three in the rear, slumped down in the seats. Questioning revealed that each passenger was an illegal alien, although Sifuentes was a United States citizen. The aliens had met Sifuentes in the United States, by prearrangement, after swimming across the Rio Grande.</p>
<p>Sifuentes was indicted on four counts of illegally transporting aliens. <span class="citation no-link">8 U. S. C. § 1324</span> (a) (2). He moved on Fourth Amendment grounds to suppress the evidence derived from the stop. The motion was denied and he was convicted after a jury trial. Sifuentes renewed his Fourth Amendment argument on appeal, contending primarily that stops made without reason to believe a car is transporting aliens illegally are unconstitutional. The United States Court of Appeals for the Fifth Circuit affirmed the conviction, <span class="citation multiple-matches"><a href="/c/F.%202d/517/1402/">517 F. 2d 1402</a></span> (1975), relying on its opinion in <i>United States</i> v. <i>Santibanez,</i> <span class="citation" data-id="328159"><a href="/opinion/328159/united-states-v-jose-rodriguez-santibanez/" aria-description="Citation for case: United States v. Jose Rodriguez Santibanez">517 F. 2d 922</a></span> (1975). There the Court of Appeals had ruled that routine checkpoint stops are consistent with the Fourth Amendment. We affirm.<sup>[6]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*551</span> II</h2>
<p>The Courts of Appeals for the Ninth and the Fifth Circuits are in conflict on the constitutionality of a law enforcement technique considered important by those charged with policing the Nation's borders. Before turning to the constitutional question, we examine the context in which it arises.</p>
<p></p>
<h2>A</h2>
<p>It has been national policy for many years to limit immigration into the United States. Since July 1, 1968, the annual quota for immigrants from all independent countries of the Western Hemisphere, including Mexico, has been 120,000 persons. Act of Oct. 3, 1965, § 21 (e), <span class="citation no-link">79 Stat. 921</span>. Many more aliens than can be accommodated under the quota want to live and work in the United States. Consequently, large numbers of aliens seek illegally to enter or to remain in the United States. We noted last Term that "[e]stimates of the number of illegal immigrants [already] in the United States vary widely. A conservative estimate in 1972 produced a figure of about one million, but the Immigration and Naturalization Service now suggests there may be as many as 10 or 12 million aliens illegally in the country." <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975) (footnote omitted). It is estimated that 85% of the illegal immigrants are from Mexico, drawn by the fact that economic opportunities are significantly greater in the United States than they are in Mexico. <i>United States</i> v. <i>Baca,</i> <span class="citation" data-id="1802688"><a href="/opinion/1802688/united-states-v-baca/#402" aria-description="Citation for case: United States v. Baca">368 F. Supp., at 402</a></span>.</p>
<p><span class="star-pagination">*552</span> Interdicting the flow of illegal entrants from Mexico poses formidable law enforcement problems. The principal problem arises from surreptitious entries. <span class="citation" data-id="1802688"><a href="/opinion/1802688/united-states-v-baca/#405" aria-description="Citation for case: United States v. Baca"><i>Id.,</i> at 405</a></span>. The United States shares a border with Mexico that is almost 2,000 miles long, and much of the border area is uninhabited desert or thinly populated arid land. Although the Border Patrol maintains personnel, electronic equipment, and fences along portions of the border, it remains relatively easy for individuals to enter the United States without detection. It also is possible for an alien to enter unlawfully at a port of entry by the use of falsified papers or to enter lawfully but violate restrictions of entry in an effort to remain in the country unlawfully.<sup>[7]</sup> Once within the country, the aliens seek to travel inland to areas where employment is believed to be available, frequently meeting by prearrangement with friends or professional smugglers who transport them in private vehicles. <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#879" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 879</a></span>.</p>
<p>The Border Patrol conducts three kinds of inland traffic-checking operations in an effort to minimize illegal immigration. Permanent checkpoints, such as those at San Clemente and Sarita, are maintained at or near intersections of important roads leading away from the border. They operate on a coordinated basis designed to avoid circumvention by smugglers and others who transport the illegal aliens. Temporary checkpoints, which operate like permanent ones, occasionally are established in other strategic locations. Finally, roving patrols are maintained to supplement the checkpoint system. See <i>Almeida-Sanchez</i> v. <i>United</i> <span class="star-pagination">*553</span> <i>States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#268" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 268</a></span> (1973).<sup>[8]</sup> In fiscal 1973, 175,-511 deportable aliens were apprehended throughout the Nation by "line watch" agents stationed at the border itself. Traffic-checking operations in the interior apprehended approximately 55,300 more deportable aliens.<sup>[9]</sup> Most of the traffic-checking apprehensions were at checkpoints, though precise figures are not available. <i>United States</i> v. <span class="citation" data-id="1802688"><a href="/opinion/1802688/united-states-v-baca/#405" aria-description="Citation for case: United States v. Baca"><i>Baca, supra,</i> at 405, 407</a></span>, and n. 2.</p>
<p></p>
<h2>B</h2>
<p>We are concerned here with permanent checkpoints, the locations of which are chosen on the basis of a number of factors. The Border Patrol believes that to assure effectiveness, a checkpoint must be (i) distant enough from the border to avoid interference with traffic in populated areas near the border, (ii) close to the confluence of two or more significant roads leading away from the border, (iii) situated in terrain that restricts vehicle passage around the checkpoint, (iv) on a stretch of highway compatible with safe operation, and (v) beyond the 25-mile zone in which "border passes," see n. 7, <i>supra,</i> are valid. <i>United States</i> v. <span class="citation" data-id="1802688"><a href="/opinion/1802688/united-states-v-baca/#406" aria-description="Citation for case: United States v. Baca"><i>Baca, supra,</i> at 406</a></span>.</p>
<p><span class="star-pagination">*554</span> The record in No. 74-1560 provides a rather complete picture of the effectiveness of the San Clemente checkpoint. Approximately 10 million cars pass the checkpoint location each year, although the checkpoint actually is in operation only about 70% of the time.<sup>[10]</sup> In calendar year 1973, approximately 17,000 illegal aliens were apprehended there. During an eight-day period in 1974 that included the arrests involved in No. 74-1560, roughly 146,000 vehicles passed through the checkpoint during 124 1/6 hours of operation. Of these, 820 vehicles were referred to the secondary inspection area, where Border Patrol agents found 725 deportable aliens in 171 vehicles. In all but two cases, the aliens were discovered without a conventional search of the vehicle. A similar rate of apprehensions throughout the year would have resulted in an annual total of over 33,000, although the Government contends that many illegal aliens pass through the checkpoint undetected. The record in No. 75-5387 does not provide comparable statistical information regarding the Sarita checkpoint. While it appears that fewer illegal aliens are apprehended there, it may be assumed that fewer pass by undetected, as every motorist is questioned.</p>
<p></p>
<h2>III</h2>
<p>The Fourth Amendment imposes limits on search-and-seizure powers in order to prevent arbitrary and oppressive interference by enforcement officials with the privacy and personal security of individuals. See <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 878</a></span>; <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#895" aria-description="Citation for case: United States v. Ortiz">422 U. S., at 895</a></span>; <i>Camara</i> v. <i>Municipal Court,</i> <span class="star-pagination">*555</span> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528</a></span> (1967). In delineating the constitutional safeguards applicable in particular contexts, the Court has weighed the public interest against the Fourth Amendment interest of the individual, <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 878</a></span>; <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20-21</a></span> (1968), a process evident in our previous cases dealing with Border Patrol traffic-checking operations.</p>
<p>In <i>Almeida-Sanchez</i> v. <i>United States, supra</i><i>,</i> the question was whether a roving-patrol unit constitutionally could search a vehicle for illegal aliens simply because it was in the general vicinity of the border. We recognized that important law enforcement interests were at stake but held that searches by roving patrols impinged so significantly on Fourth Amendment privacy interests that a search could be conducted without consent only if there was probable cause to believe that a car contained illegal aliens, at least in the absence of a judicial warrant authorizing random searches by roving patrols in a given area. Compare <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#273" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S., at 273</a></span>, with <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#283" aria-description="Citation for case: Almeida-Sanchez v. United States"><i>id.,</i> at 283-285</a></span> (POWELL, J., concurring), and <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#288" aria-description="Citation for case: Almeida-Sanchez v. United States"><i>id.,</i> at 288</a></span> (WHITE, J., dissenting). We held in <i>United States</i> v. <i><span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">Ortiz, supra</a></span></i><i>,</i> that the same limitations applied to vehicle searches conducted at a permanent checkpoint.</p>
<p>In <i>United States</i> v. <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce, supra</a></span></i><i>,</i> however, we recognized that other traffic-checking practices involve a different balance of public and private interests and appropriately are subject to less stringent constitutional safeguards. The question was under what circumstances a roving patrol could stop motorists in the general area of the border for brief inquiry into their residence status. We found that the interference with Fourth Amendment interests involved in such a stop was "modest," 422 U. S., at 880, while the inquiry served significant law enforcement needs. We therefore held that a roving-patrol stop need not be justified by probable <span class="star-pagination">*556</span> cause and may be undertaken if the stopping officer is "aware of specific articulable facts, together with rational inferences from those facts, that reasonably warrant suspicion" that a vehicle contains illegal aliens. <i>Id.,</i> at 884.<sup>[11]</sup></p>
<p></p>
<h2>IV</h2>
<p>It is agreed that checkpoint stops are "seizures" within the meaning of the Fourth Amendment. The defendants contend primarily that the routine stopping of vehicles at a checkpoint is invalid because <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> must be read as proscribing any stops in the absence of reasonable suspicion. Sifuentes alternatively contends in No. 75-5387 that routine checkpoint stops are permissible only when the practice has the advance judicial authorization of a warrant. There was a warrant authorizing the stops at San Clemente but none at Sarita. As we reach the issue of a warrant requirement only if reasonable suspicion is not required, we turn first to whether reasonable suspicion is a prerequisite to a valid stop, a question to be resolved by balancing the interests at stake.</p>
<p></p>
<h2>A</h2>
<p>Our previous cases have recognized that maintenance of a traffic-checking program in the interior is necessary because the flow of illegal aliens cannot be controlled effectively at the border. We note here only the substantiality of the public interest in the practice of routine stops for inquiry at permanent checkpoints, a practice which the Government identifies as the most important of the traffic-checking operations. Brief for United States in No. 74-1560, pp. 19-20.<sup>[12]</sup> These checkpoints <span class="star-pagination">*557</span> are located on important highways; in their absence such highways would offer illegal aliens a quick and safe route into the interior. Routine checkpoint inquiries apprehend many smugglers and illegal aliens who succumb to the lure of such highways. And the prospect of such inquiries forces others onto less efficient roads that are less heavily traveled, slowing their movement and making them more vulnerable to detection by roving patrols. Cf. <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#883" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 883-885</a></span>.</p>
<p>A requirement that stops on major routes inland always be based on reasonable suspicion would be impractical because the flow of traffic tends to be too heavy to allow the particularized study of a given car that would enable it to be identified as a possible carrier of illegal aliens. In particular, such a requirement would largely eliminate any deterrent to the conduct of well-disguised smuggling operations, even though smugglers are known to use these highways regularly.</p>
<p></p>
<h2>B</h2>
<p>While the need to make routine checkpoint stops is great, the consequent intrusion on Fourth Amendment interests is quite limited. The stop does intrude to a limited extent on motorists' right to "free passage without <span class="star-pagination">*558</span> interruption," <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#154" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 154</a></span> (1925), and arguably on their right to personal security. But it involves only a brief detention of travelers during which</p>
<blockquote>" `[a]ll that is required of the vehicle's occupants is a response to a brief question or two and possibly the production of a document evidencing a right to be in the United States.' " <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#880" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 880</a></span>.</blockquote>
<p>Neither the vehicle nor its occupants are searched, and visual inspection of the vehicle is limited to what can be seen without a search. This objective intrusionthe stop itself, the questioning, and the visual inspection also existed in roving-patrol stops. But we view checkpoint stops in a different light because the subjective intrusionthe generating of concern or even fright on the part of lawful travelersis appreciably less in the case of a checkpoint stop. In <i><span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">Ortiz</a></span>,</i> we noted:</p>
<blockquote>"[T]he circumstances surrounding a checkpoint stop and search are far less intrusive than those attending a roving-patrol stop. Roving patrols often operate at night on seldom-traveled roads, and their approach may frighten motorists. At traffic checkpoints the motorist can see that other vehicles are being stopped, he can see visible signs of the officers' authority, and he is much less likely to be frightened or annoyed by the intrusion." 422 U. S., at 894-895.</blockquote>
<p>In <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span>,</i> we recognized that Fourth Amendment analysis in this context also must take into account the overall degree of interference with legitimate traffic. 422 U. S., at 882-883. We concluded there that random roving-patrol stops could not be tolerated because they "would subject the residents of . . . [border] areas to <span class="star-pagination">*559</span> potentially unlimited interference with their use of the highways, solely at the discretion of Border Patrol officers.. . . [They] could stop motorists at random for questioning, day or night, anywhere within 100 air miles of the 2,000-mile border, on a city street, a busy highway, or a desert road . . . ." <i>Ibid.</i> There also was a grave danger that such unreviewable discretion would be abused by some officers in the field. <i>Ibid.</i></p>
<p>Routine checkpoint stops do not intrude similarly on the motoring public. First, the potential interference with legitimate traffic is minimal. Motorists using these highways are not taken by surprise as they know, or may obtain knowledge of, the location of the checkpoints and will not be stopped elsewhere. Second, checkpoint operations both appear to and actually involve less discretionary enforcement activity. The regularized manner in which established checkpoints are operated is visible evidence, reassuring to law-abiding motorists, that the stops are duly authorized and believed to serve the public interest. The location of a fixed checkpoint is not chosen by officers in the field, but by officials responsible for making overall decisions as to the most effective allocation of limited enforcement resources. We may assume that such officials will be unlikely to locate a checkpoint where it bears arbitrarily or oppressively on motorists as a class. And since field officers may stop only those cars passing the checkpoint, there is less room for abusive or harassing stops of individuals than there was in the case of roving-patrol stops. Moreover, a claim that a particular exercise of discretion in locating or operating a checkpoint is unreasonable is subject to post-stop judicial review.<sup>[13]</sup></p>
<p><span class="star-pagination">*560</span> The defendants arrested at the San Clemente checkpoint suggest that its operation involves a significant extra element of intrusiveness in that only a small percentage of cars are referred to the secondary inspection area, thereby "stigmatizing" those diverted and reducing the assurances provided by equal treatment of all motorists. We think defendants overstate the consequences. Referrals are made for the sole purpose of conducting a routine and limited inquiry into residence status that cannot feasibly be made of every motorist where the traffic is heavy. The objective intrusion of the stop and inquiry thus remains minimal. Selective referral may involve some annoyance, but it remains true that the stops should not be frightening or offensive because of their public and relatively routine nature. Moreover, selective referralsrather than questioning the occupants of every cartend to advance some Fourth Amendment interests by minimizing the intrusion on the general motoring public.</p>
<p></p>
<h2>C</h2>
<p>The defendants note correctly that to accommodate public and private interests some quantum of individualized suspicion is usually a prerequisite to a constitutional search or seizure.<sup>[14]</sup> See <i>Terry</i> v. <i>Ohio,</i> 392 <span class="star-pagination">*561</span> U. S., at 21, and n. 18. But the Fourth Amendment imposes no irreducible requirement of such suspicion. This is clear from <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967). See also <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#283" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S., at 283-285</a></span> (POWELL, J., concurring); <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#288" aria-description="Citation for case: Almeida-Sanchez v. United States"><i>id.,</i> at 288</a></span> (WHITE, J., dissenting); <i>Colonnade Catering Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970); <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972); <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#154" aria-description="Citation for case: Carroll v. United States">267 U. S., at 154</a></span>. In <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> the Court required an "area" warrant to support the reasonableness of inspecting private residences within a particular area for building code violations, but recognized that "specific knowledge of the condition of the particular dwelling" was not required to enter any given residence. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#538" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 538</a></span>. In so holding, the Court examined the government interests advanced to justify such routine intrusions "upon the constitutionally protected interests of the private citizen," <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>id.,</i> at 534-535</a></span>, and concluded that under the circumstances the government interest outweighed those of the private citizen.</p>
<p>We think the same conclusion is appropriate here, where we deal neither with searches nor with the sanctity of private dwellings, ordinarily afforded the most stringent Fourth Amendment protection. See, <i>e. g., </i><i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span> (1948). As we have noted earlier, one's expectation of privacy in an automobile and of freedom in its operation are significantly different from the traditional expectation of privacy and freedom in one's residence. <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">422 U. S., at 896</a></span> n. 2; see <i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590-591</a></span> (1974) (plurality <span class="star-pagination">*562</span> opinion). And the reasonableness of the procedures followed in making these checkpoint stops makes the resulting intrusion on the interests of motorists minimal. On the other hand, the purpose of the stops is legitimate and in the public interest, and the need for this enforcement technique is demonstrated by the records in the cases before us. Accordingly, we hold that the stops and questioning at issue may be made in the absence of any individualized suspicion at reasonably located checkpoints.<sup>[15]</sup></p>
<p><span class="star-pagination">*563</span> We further believe that it is constitutional to refer motorists selectively to the secondary inspection area at the San Clemente checkpoint on the basis of criteria that would not sustain a roving-patrol stop. Thus, even if it be assumed that such referrals are made largely on the basis of apparent Mexican ancestry,<sup>[16]</sup> we perceive no constitutional violation. Cf. <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#885" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 885-887</a></span>. As the intrusion here is sufficiently minimal that no particularized reason need exist to justify it, we think it follows that the Border Patrol <span class="star-pagination">*564</span> officers must have wide discretion in selecting the motorists to be diverted for the brief questioning involved.<sup>[17]</sup></p>
<p></p>
<h2>V</h2>
<p>Sifuentes' alternative argument is that routine stops at a checkpoint are permissible only if a warrant has given judicial authorization to the particular checkpoint location and the practice of routine stops. A warrant requirement in these circumstances draws some support from <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span>,</i> where the Court held that, absent consent, an "area" warrant was required to make a building code inspection, even though the search could be conducted absent cause to believe that there were violations in the building searched.<sup>[18]</sup></p>
<p>We do not think, however, that <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> is an apt <span class="star-pagination">*565</span> model. It involved the search of private residences, for which a warrant traditionally has been required. See, <i>e. g., </i><i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span> (1948). As developed more fully above, the strong Fourth Amendment interests that justify the warrant requirement in that context are absent here. The degree of intrusion upon privacy that may be occasioned by a search of a house hardly can be compared with the minor interference with privacy resulting from the mere stop for questioning as to residence. Moreover, the warrant requirement in <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> served specific Fourth Amendment interests to which a warrant requirement here would make little contribution. The Court there said:</p>
<blockquote>"[W]hen [an] inspector [without a warrant] demands entry, the occupant has no way of knowing whether enforcement of the municipal code involved requires inspection of his premises, no way of knowing the lawful limits of the inspector's power to search, and no way of knowing whether the inspector himself is acting under proper authorization." <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 532</a></span>.</blockquote>
<p>A warrant provided assurance to the occupant on these scores. We believe that the visible manifestations of the field officers' authority at a checkpoint provide substantially the same assurances in this case.</p>
<p>Other purposes served by the requirement of a warrant also are inapplicable here. One such purpose is to prevent hindsight from coloring the evaluation of the reasonableness of a search or seizure. Cf. <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#455" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 455-456, n. 22</a></span> (1976) (MARSHALL, J., dissenting). The reasonableness of checkpoint stops, however, turns on factors such as the location and method of operation of the checkpoint, factors that are not susceptible to the distortion of hindsight, and therefore will be open to post-stop review notwithstanding <span class="star-pagination">*566</span> the absence of a warrant. Another purpose for a warrant requirement is to substitute the judgment of the magistrate for that of the searching or seizing officer. <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#316" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 316-318</a></span> (1972). But the need for this is reduced when the decision to "seize" is not entirely in the hands of the officer in the field, and deference is to be given to the administrative decisions of higher ranking officials.</p>
<p></p>
<h2>VI</h2>
<p>In summary, we hold that stops for brief questioning routinely conducted at permanent checkpoints are consistent with the Fourth Amendment and need not be authorized by warrant.<sup>[19]</sup> The principal protection of Fourth <span class="star-pagination">*567</span> Amendment rights at checkpoints lies in appropriate limitations on the scope of the stop. See <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 24-27</a></span>; <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 881-882</a></span>. We have held that checkpoint searches are constitutional only if justified by consent or probable cause to search. <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891</a></span> (1975). And our holding today is limited to the type of stops described in this opinion. "[A]ny further detention . . . must be based on consent or probable cause." <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#882" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 882</a></span>. None of the defendants in these cases argues that the stopping officers exceeded these limitations. Consequently, we affirm the judgment of the Court of Appeals for the Fifth Circuit, which had affirmed the conviction of Sifuentes. We reverse the judgment of the Court of Appeals for the Ninth Circuit and remand the case with directions to affirm the conviction of Martinez-Fuerte and to remand the other cases to the District Court for further proceedings.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE BRENNAN, with whom MR. JUSTICE MARSHALL joins, dissenting.</p>
<p>Today's decision is the ninth this Term marking the continuing evisceration of Fourth Amendment protections against unreasonable searches and seizures. Early in the Term, <i>Texas</i> v. <i>White,</i> <span class="citation" data-id="9426226"><a href="/opinion/109332/texas-v-white/" aria-description="Citation for case: Texas v. White">423 U. S. 67</a></span> (1975), permitted the warrantless search of an automobile in police custody despite the unreasonableness of the custody <span class="star-pagination">*568</span> and opportunity to obtain a warrant. <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976), held that regardless of whether opportunity exists to obtain a warrant, an arrest in a public place for a previously committed felony never requires a warrant, a result certainly not fairly supported by either history or precedent. See <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#433" aria-description="Citation for case: United States v. Watson"><i>id.,</i> at 433</a></span> (MARSHALL, J., dissenting). <i>United States</i> v. <i>Santana,</i> <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">427 U. S. 38</a></span> (1976), went further and approved the warrantless arrest for a felony of a person standing on the front porch of her residence. <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">425 U. S. 435</a></span> (1976), narrowed the Fourth Amendment's protection of privacy by denying the existence of a protectible interest in the compilation of checks, deposit slips, and other records pertaining to an individual's bank account. <i>Stone</i> v. <i>Powell, ante,</i> p. 465, precluded the assertion of Fourth Amendment claims in federal collateral relief proceedings. <i>United States</i> v. <i>Janis, ante,</i> p. 433, held that evidence unconstitutionally seized by a state officer is admissible in a civil proceeding by or against the United States. <i>South Dakota</i> v. <i>Opperman, ante,</i> p. 364, approved sweeping inventory searches of automobiles in police custody irrespective of the particular circumstances of the case. Finally, in <i>Andresen</i> v. <i>Maryland,</i> <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">427 U. S. 463</a></span> (1976), the Court, in practical effect, weakened the Fourth Amendment prohibition against general warrants.</p>
<p>Consistent with this purpose to debilitate Fourth Amendment protections, the Court's decision today virtually empties the Amendment of its reasonableness requirement by holding that law enforcement officials manning fixed checkpoint stations who make standardless seizures of persons do not violate the Amendment. This holding cannot be squared with this Court's recent decisions in <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891</a></span> (1975); <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975); <span class="star-pagination">*569</span> and <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973). I dissent.</p>
<p>While the requisite justification for permitting a search or seizure may vary in certain contexts, compare <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89</a></span> (1964), with <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), and <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967), even in the exceptional situations permitting intrusions on less than probable cause, it has long been settled that justification must be measured by objective standards. Thus in the seminal decision justifying intrusions on less-than-probable cause, <i>Terry</i> v. <i>Ohio, supra</i><i>,</i> the Court said:</p>
<blockquote>"The scheme of the Fourth Amendment becomes meaningful only when it is assured that at some point the conduct of those charged with enforcing the laws can be subjected to the more detached, neutral scrutiny of a judge who must evaluate the reasonableness of a particular search or seizure in light of the particular circumstances. And in making that assessment it is imperative that the facts be judged against an <i>objective standard</i> . . . . Anything less would invite intrusions upon constitutionally guaranteed rights based on nothing more substantial than inarticulate hunches, a result this Court has consistently refused to sanction." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 21-22</a></span> (emphasis added, footnote omitted).</blockquote>
<blockquote>"This demand for specificity in the information upon which police action is predicated is the central teaching of this Court's Fourth Amendment jurisprudence." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 21</a></span> n. 18.</blockquote>
<p><i>Terry</i> thus made clear what common sense teaches: Conduct, to be reasonable, must pass muster under objective standards applied to specific facts.</p>
<p>We are told today, however, that motorists without number may be individually stopped, questioned, visually <span class="star-pagination">*570</span> inspected, and then further detained without even a showing of articulable suspicion, see <i>ante,</i> at 547, let alone the heretofore constitutional minimum of reasonable suspicion, a result that permits search and seizure to rest upon "nothing more substantial than inarticulate hunches." This defacement of Fourth Amendment protections is arrived at by a balancing process that overwhelms the individual's protection against unwarranted official intrusion by a governmental interest said to justify the search and seizure. But that method is only a convenient cover for condoning arbitrary official conduct, for the governmental interests relied on as warranting intrusion here are the same as those in <i><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">Almeida-Sanchez</a></span></i> and <i><span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">Ortiz</a></span>,</i> which required a showing of probable cause for roving-patrol and fixed checkpoint searches, and <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span>,</i> which required at least a showing of reasonable suspicion based on specific articulable facts to justify roving-patrol stops. Absent some difference in the nature of the intrusion, the same minimal requirement should be imposed for checkpoint stops.</p>
<p>The Court assumes, and I certainly agree, that persons stopped at fixed checkpoints, whether or not referred to a secondary detention area, are "seized" within the meaning of the Fourth Amendment. Moreover, since the vehicle and its occupants are subjected to a "visual inspection," the intrusion clearly exceeds mere physical restraint, for officers are able to see more in a stopped vehicle than in vehicles traveling at normal speeds down the highway. As the Court concedes, <i>ante,</i> at 558, the checkpoint stop involves essentially the same intrusions as a roving-patrol stop, yet the Court provides no principled basis for distinguishing checkpoint stops.</p>
<p>Certainly that basis is not provided in the Court's reasoning that the subjective intrusion here is appreciably less than in the case of a stop by a roving patrol. <span class="star-pagination">*571</span> <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> nowhere bases the requirement of reasonable suspicion upon the subjective nature of the intrusion. In any event, the subjective aspects of checkpoint stops, even if different from the subjective aspects of roving-patrol stops, just as much require some principled restraint on law enforcement conduct. The motorist whose conduct has been nothing but innocent and this is overwhelmingly the casesurely resents his own detention and inspection. And checkpoints, unlike roving stops, detain thousands of motorists, a dragnetlike procedure offensive to the sensibilities of free citizens. Also, the delay occasioned by stopping hundreds of vehicles on a busy highway is particularly irritating.</p>
<p>In addition to overlooking these dimensions of subjective intrusion, the Court, without explanation, also ignores one major source of vexation. In abandoning any requirement of a minimum of reasonable suspicion, or even articulable suspicion, the Court in every practical sense renders meaningless, as applied to checkpoint stops, the <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> holding that "standing alone [Mexican appearance] does not justify stopping all Mexican-Americans to ask if they are aliens."<sup>[1]</sup> 422 <span class="star-pagination">*572</span> U. S., at 887. Since the objective is almost entirely the Mexican illegally in the country, checkpoint officials, uninhibited by any objective standards and therefore free to stop any or all motorists without explanation or excuse, wholly on whim, will perforce target motorists of Mexican appearance. The process will then inescapably discriminate against citizens of Mexican ancestry and Mexican aliens lawfully in this country for no other reason than that they unavoidably possess the same "suspicious" physical and grooming characteristics of illegal Mexican aliens.</p>
<p>Every American citizen of Mexican ancestry and every Mexican alien lawfully in this country must know after today's decision that he travels the fixed checkpoint highways at the risk of being subjected not only to a stop, but also to detention and interrogation, both prolonged and to an extent far more than for non-Mexican appearing motorists. To be singled out for referral and to be detained and interrogated must be upsetting to any motorist. One wonders what actual experience supports my Brethren's conclusion that referrals "should not be frightening or offensive because of their public and relatively routine nature." <i>Ante,</i> at 560.<sup>[2]</sup> In point of fact, referrals, <span class="star-pagination">*573</span> viewed in context, are not relatively routine; thousands are otherwise permitted to pass. But for the arbitrarily selected motorists who must suffer the delay and humiliation of detention and interrogation, the experience can obviously be upsetting.<sup>[3]</sup> And that experience is particularly vexing for the motorist of Mexican ancestry who is selectively referred, knowing that the officers' target is the Mexican alien. That deep resentment will be stirred by a sense of unfair discrimination is not difficult to foresee.<sup>[4]</sup></p>
<p><span class="star-pagination">*574</span> In short, if a balancing process is required, the balance should be struck, as in <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span>,</i> to require that Border Patrol officers act upon at least reasonable suspicion in making checkpoint stops. In any event, even if a different balance were struck, the Court cannot, without ignoring the Fourth Amendment requirement of reasonableness, justify wholly unguided seizures by officials manning the checkpoints. The Court argues, however, that practicalities necessitate otherwise: "A requirement that stops on major routes inland always be based on reasonable suspicion would be impractical because the flow of traffic tends to be too heavy to allow the particularized study of a given car that would enable it to be identified as a possible carrier of illegal aliens." <i>Ante,</i> at 557.</p>
<p>As an initial matter, whatever force this argument may have, it cannot apply to the secondary detentions that occurred in No. 74-1560. Once a vehicle has been slowed and observed at a checkpoint, ample opportunity <span class="star-pagination">*575</span> exists to formulate the reasonable suspicion which, if it actually exists, would justify further detention. Indeed, though permitting roving stops based on reasonable suspicion, <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> required that "any further detention or search must be based on [the greater showing of] consent or probable cause." 422 U. S., at 882. The Court today, however, does not impose a requirement of even reasonable suspicion for these secondary stops.</p>
<p>The Court's rationale is also not persuasive because several of the factors upon which officers may rely in establishing reasonable suspicion are readily ascertainable, regardless of the flow of traffic. For example, with checkpoint stops as with roving-patrol stops, "[a]spects of the vehicle itself may justify suspicion." <i>Id.,</i> at 885. Thus it is relevant that the vehicle is a certain type of station wagon, appears to be heavily loaded, contains an extraordinary number of persons, or contains persons trying to hide. See <i>ibid.</i> If such factors are satisfactory to permit the imposition of a reasonable-suspicion requirement in the more demanding circumstances of a roving patrol, where officers initially deal with a vehicle traveling, not at a crawl, but at highway speeds, they clearly should suffice in the circumstances of a checkpoint stop.</p>
<p>Finally, the Court's argument fails for more basic reasons. There is no principle in the jurisprudence of fundamental rights which permits constitutional limitations to be dispensed with merely because they cannot be conveniently satisfied. Dispensing with reasonable suspicion as a prerequisite to stopping and inspecting motorists because the inconvenience of such a requirement would make it impossible to identify a given car as a possible carrier of aliens is no more justifiable than dispensing with probable cause as prerequisite to the search of an individual because the inconvenience of <span class="star-pagination">*576</span> such a requirement would make it impossible to identify a given person in a high-crime area as a possible carrier of concealed weapons. "The needs of law enforcement stand in constant tension with the Constitution's protections of the individual against certain exercises of official power. It is precisely the predictability of these pressures that counsels a resolute loyalty to constitutional safeguards." <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#273" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S., at 273</a></span>.</p>
<p>The Court also attempts to justify its approval of standardless conduct on the ground that checkpoint stops "involve less discretionary enforcement activity" than roving stops. <i>Ante,</i> at 559. This view is at odds with its later more revealing statement that "officers must have wide discretion in selecting the motorists to be diverted for the brief questioning involved." <i>Ante,</i> at 564. Similarly unpersuasive is the statement that "since field officers may stop only those cars passing the checkpoint, there is less room for abusive or harassing stops of individuals than there was in the case of roving-patrol stops." <i>Ante,</i> at 559.<sup>[5]</sup> The Fourth Amendment standard <span class="star-pagination">*577</span> of reasonableness admits of neither intrusion at the discretion of law enforcement personnel nor abusive or harassing stops, however infrequent. Action based merely on whatever may pique the curiosity of a particular officer is the antithesis of the objective standards requisite to reasonable conduct and to avoiding abuse and harassment. Such action, which the Court now permits, has expressly been condemned as contrary to basic Fourth Amendment principles. Certainly today's holding is far removed from the proposition emphatically affirmed in <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#317" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 317</a></span> (1972), that "those charged with . . . investigative and prosecutorial duty should not be the sole judges of when to utilize constitutionally sensitive means in pursuing their tasks. The historical judgment, which the Fourth Amendment accepts, is that unreviewed executive discretion may yield too readily to pressures to obtain incriminating evidence and overlook potential invasions of privacy . . . ." Indeed, it is far removed from the even more recent affirmation that "the central concern of the Fourth Amendment is to protect liberty and privacy from arbitrary and oppressive interference by government officials." <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#895" aria-description="Citation for case: United States v. Ortiz">422 U. S., at 895</a></span>.<sup>[6]</sup></p>
<p><span class="star-pagination">*578</span> The cornerstone of this society, indeed of any free society, is orderly procedure. The Constitution, as originally adopted, was therefore, in great measure, a procedural document. For the same reasons the drafters of the Bill of Rights largely placed their faith in procedural limitations on government action. The Fourth Amendment's requirement that searches and seizures be reasonable enforces this fundamental understanding in erecting its buffer against the arbitrary treatment of citizens by government. But to permit, as the Court does today, police discretion to supplant the objectivity of reason and, thereby, expediency to reign in the place of order, is to undermine Fourth Amendment safeguards and threaten erosion of the cornerstone of our system of a government, for, as Mr. Justice Frankfurter reminded us, "[t]he history of American freedom is, in no small measure, the history of procedure." <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#414" aria-description="Citation for case: Malinski v. New York">324 U. S. 401, 414</a></span> (1945).</p>
<h2>NOTES</h2>
<p>[*]  Together with No. 75-5387, <i>Sifuentes</i> v. <i>United States,</i> on certiorari to the United States Court of Appeals for the Fifth Circuit.</p>
<p>[]  <i>Melvin L. Wulf, Joel M. Gora, Vilma S. Martinez, Sanford J. Rosen,</i> and <i>Jerome B. Falk, Jr.,</i> filed a brief for the American Civil Liberties Union et al. as <i>amici curiae</i> urging affirmance in No. 74-1560.</p>
<p>[1]  The parties disagree as to whether vehicles not referred to the secondary inspection area are brought to a complete halt or merely "roll" slowly through the checkpoint. Resolution of this dispute is not necessary here, as we may assume, <i>arguendo,</i> that all motorists passing through the checkpoint are so slowed as to have been "seized."</p>
<p>[2]  The record does not reveal explicitly why a warrant was sought. Shortly before the warrant application, however, the Court of Appeals for the Ninth Circuit had held unconstitutional a routine stop and search conducted at a permanent checkpoint without such a warrant. See <i>United States</i> v. <i>Bowen,</i> <span class="citation" data-id="9460842"><a href="/opinion/320688/united-states-v-john-lee-bowen/" aria-description="Citation for case: United States v. John Lee Bowen">500 F. 2d 960</a></span> (1974), aff'd on other grounds, <span class="citation" data-id="109313"><a href="/opinion/109313/bowen-v-united-states/" aria-description="Citation for case: Bowen v. United States">422 U. S. 916</a></span> (1975); <i>United States</i> v. <i>Juarez-Rodriguez,</i> <span class="citation" data-id="319859"><a href="/opinion/319859/united-states-v-camilo-juarez-rodriguez/" aria-description="Citation for case: United States v. Camilo Juarez-Rodriguez">498 F. 2d 7</a></span> (1974). Soon after the warrant issued, the Court of Appeals also held unconstitutional routine checkpoint stops conducted without a warrant. See <i>United States</i> v. <i>Esquer-Rivera,</i> <span class="citation" data-id="320555"><a href="/opinion/320555/united-states-v-laura-elena-esquer-rivera-united-states-of-america-v/" aria-description="Citation for case: United States v. Laura Elena Esquer-Rivera, United States...">500 F. 2d 313</a></span> (1974). See also n. 15, <i>infra.</i></p>
<p>[3]  Each of the defendants in No. 74-1560 and the defendant in No. 75-5387 sought to suppress, among other things, the testimony of one or more illegal aliens. We noted in <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span>, 876 n. 2 (1975), that "[t]here may be room to question whether voluntary testimony of a witness at trial, as opposed to a Government agent's testimony about objects seized or statements overheard, is subject to suppression . . . ." The question again is not before us.</p>
<p>[4]  The prosecution of Martinez-Fuerte was before a different District Judge than were the other cases.</p>
<p>[5]  The principal question before the Court of Appeals was the constitutional significance of the "warrant of inspection" under which the checkpoint was operating when the defendants were stopped. See n. 15, <i>infra.</i> The Government, however, preserved the question whether routine checkpoint stops could be made absent a warrant.</p>
<p>[6]  We initially granted the Government's petition for a writ of certiorari in No. 74-1560, <span class="citation multiple-matches"><a href="/c/U.%20S./423/822/">423 U. S. 822</a></span>, and later granted Sifuentes' petition in No. 75-5387 and directed that the cases be argued in tandem. <span class="citation multiple-matches"><a href="/c/U.%20S./423/945/">423 U. S. 945</a></span>. Subsequently we granted the motion of the Solicitor General to consolidate the cases for oral argument. <span class="citation multiple-matches"><a href="/c/U.%20S./425/931/">425 U. S. 931</a></span>.</p>
<p>[7]  The latter occurs particularly where "border passes" are issued to simplify passage between interrelated American and Mexican communities along the border. These passes authorize travel within 25 miles of the border for a 72-hour period. See <span class="citation no-link">8 CFR § 212.6</span> (1976).</p>
<p>[8]  All these operations are conducted pursuant to statutory authorizations empowering Border Patrol agents to interrogate those believed to be aliens as to their right to be in the United States and to inspect vehicles for aliens. <span class="citation no-link">8 U. S. C. §§ 1357</span> (a) (1), (a) (3). Under current regulations the authority conferred by § 1357 (a) (3) may be exercised anywhere within 100 air miles of the border. <span class="citation no-link">8 CFR § 287.1</span> (a) (1976).</p>
<p>[9]  As used in these statistics, the term "deportable alien" means "a person who has been found to be deportable by an immigration judge, or who admits his deportability upon questioning by official agents." <i>United States</i> v. <i>Baca,</i> <span class="citation" data-id="1802688"><a href="/opinion/1802688/united-states-v-baca/#404" aria-description="Citation for case: United States v. Baca">368 F. Supp. 398, 404</a></span> (SD Cal. 1973). Most illegal aliens are simply deported without prosecution. The Government routinely prosecutes persons though to be smugglers, many of whom are lawfully in the United States.</p>
<p>[10]  The Sarita checkpoint is operated a comparable proportion of the time. "Down" periods are caused by personnel shortages, weather conditions, andat San Clementepeak traffic loads.</p>
<p>[11]  On the facts of the case, we concluded that the stop was impermissible because reasonable suspicion was lacking.</p>
<p>[12]  The defendants argue at length that the public interest in maintaining checkpoints is less than is asserted by the Government because the flow of illegal immigrants could be reduced by means other than checkpoint operations. As one alternative they suggest legislation prohibiting the knowing employment of illegal aliens. The logic of such elaborate less-restrictive-alternative arguments could raise insuperable barriers to the exercise of virtually all search-and-seizure powers. In any event, these arguments tend to go to the general proposition that all traffic-checking procedures are impermissible, a premise our previous cases reject. The defendants do not suggest persuasively that the particular law enforcement needs served by checkpoints could be met without reliance on routine checkpoint stops. Compare <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#883" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 883</a></span> (effectiveness of roving patrols not defeated by reasonable suspicion requirement), with <i>infra,</i> this page.</p>
<p>[13]  The choice of checkpoint locations must be left largely to the discretion of Border Patrol officials, to be exercised in accordance with statutes and regulations that may be applicable. See n. 15, <i>infra.</i> Many incidents of checkpoint operation also must be committed to the discretion of such officials. But see <i>infra,</i> at 565-566.</p>
<p>[14]  Stops for questioning, not dissimilar to those involved here, are used widely at state and local levels to enforce laws regarding drivers' licenses, safety requirements, weight limits, and similar matters. The fact that the purpose of such laws is said to be administrative is of limited relevance in weighing their intrusiveness on one's right to travel; and the logic of the defendant's position, if realistically pursued, might prevent enforcement officials from stopping motorists for questioning on these matters in the absence of reasonable suspicion that a law was being violated. As such laws are not before us, we intimate no view respecting them other than to note that this practice of stopping automobiles briefly for questioning has a long history evidencing its utility and is accepted by motorists as incident to highway use.</p>
<p>[15]  As a judicial warrant authorized the Border Patrol to make routine stops at the San Clemente checkpoint, the principal question addressed by the Court of Appeals for the Ninth Circuit in No. 74-1560 was whether routine checkpoint stops were constitutional when authorized by warrant. Cf. n. 5, <i>supra.</i> The Court of Appeals held alternatively that a warrant never could authorize such stops, <span class="citation multiple-matches"><a href="/c/F.%202d/514/308/">514 F. 2d 308</a></span>, 318 (1975), and that it was unreasonable to issue a warrant authorizing routine stops at the San Clemente location. <i>Id.,</i> at 321-322. In reaching the latter conclusion, the Court of Appeals relied on (i) "the [low] frequency with which illegal aliens pass through the San Clemente checkpoint," (ii) the distance of the checkpoint from the border, and (iii) the interference with legitimate traffic. <i>Ibid.</i> We need not address these holdings specifically, as we conclude that no warrant is needed. But we deem the argument by the defendants in No. 74-1560 in support of the latter holding to raise the question whether, even though a warrant is not required, it is unreasonable to locate a checkpoint at San Clemente.
</p>
<p>We answer this question in the negative. As indicated above, the choice of checkpoint locations is an administrative decision that must be left largely within the discretion of the Border Patrol, see n. 13, <i>supra;</i> cf. <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#538" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 538</a></span> (1967). We think the decision to locate a checkpoint at San Clemente was reasonable. The location meets the criteria prescribed by the Border Patrol to assure effectiveness, see <i>supra,</i> at 553, and the evidence supports the view that the needs of law enforcement are furthered by this location. The absolute number of apprehensions at the checkpoint is high, see <i>supra,</i> at 554, confirming Border Patrol judgment that significant numbers of illegal aliens regularly use Interstate 5 at this point. Also, San Clemente was selected as the location where traffic is lightest between San Diego and Los Angeles, thereby minimizing interference with legitimate traffic.</p>
<p>No question has been raised about the reasonableness of the location of the Sarita checkpoint.</p>
<p>[16]  The Government suggests that trained Border Patrol agents rely on factors in addition to apparent Mexican ancestry when selectively diverting motorists. Brief for United States in No. 75-5387, p. 9; see <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#884" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 884-885</a></span>. This assertion finds support in the record. Less than 1% of the motorists passing the checkpoint are stopped for questioning, whereas American citizens of Mexican ancestry and legally resident Mexican citizens constitute a significantly larger proportion of the population of southern California. The 1970 census figures, which may not fully reflect illegal aliens, show the population of California to be approximately 19,958,000 of whom some 3,102,000, or 16%, are Spanish-speaking or of Spanish surname. The equivalent percentages for metropolitan San Diego and Los Angeles are 13% and 18% respectively. U. S. Department of Commerce, 1970 Census of Population, vol. 1, pt. 6, Tables 48, 140. If the statewide population ratio is applied to the approximately 146,000 vehicles passing through the checkpoint during the eight days surrounding the arrests in No. 74-1560, roughly 23,400 would be expected to contain persons of Spanish or Mexican ancestry, yet only 820 were referred to the secondary area. This appears to refute any suggestion that the Border Patrol relies extensively on apparent Mexican ancestry standing alone in referring motorists to the secondary area.</p>
<p>[17]  Of the 820 vehicles referred to the secondary inspection area during the eight days surrounding the arrests involved in No. 74-1560, roughly 20% contained illegal aliens. <i>Supra,</i> at 554. Thus, to the extent that the Border Patrol relies on apparent Mexican ancestry at this checkpoint, see n. 16, <i>supra,</i> that reliance clearly is relevant to the law enforcement need to be served. Cf. <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#886" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 886-887</a></span>, where we noted that "[t]he likelihood that any given person of Mexican ancestry is an alien is high enough to make Mexican appearance a relevant factor . . . ," although we held that apparent Mexican ancestry by itself could not create the reasonable suspicion required for a roving-patrol stop. Different considerations would arise if, for example, reliance were put on apparent Mexican ancestry at a checkpoint operated near the Canadian border.</p>
<p>[18]  There also is some support for a warrant requirement in the concurring and dissenting opinions in <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973), which commanded the votes of five Justices. See <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#283" aria-description="Citation for case: Almeida-Sanchez v. United States"><i>id.,</i> at 283-285</a></span> (POWELL, J., concurring); <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#288" aria-description="Citation for case: Almeida-Sanchez v. United States"><i>id.,</i> at 288</a></span> (WHITE, J., dissenting). The burden of these opinions, however, was that an "area" warrant could serve as a substitute for the individualized probable cause to search that otherwise was necessary to sustain roving-patrol searches. As particularized suspicion is not necessary here, the warrant function discussed in <i><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">Almeida-Sanchez</a></span></i> is not an issue in these cases.</p>
<p>[19]  MR. JUSTICE BRENNAN'S dissenting opinion reflects unwarranted concern in suggesting that today's decision marks a radical new intrusion on citizens' rights: It speaks of the "evisceration of Fourth Amendment protections," and states that the Court "virtually empties the Amendment of its reasonableness requirement." <i>Post,</i> at 567, 568. Since 1952, Act of June 27, 1952, <span class="citation no-link">66 Stat. 233</span>, Congress has expressly authorized persons believed to be aliens to be interrogated as to residence, and vehicles "within a reasonable distance" from the border to be searched for aliens. See n. 8, <i>supra.</i> The San Clemente checkpoint has been operating at or near its present location throughout the intervening 24 years. Our prior cases have limited significantly the reach of this congressional authorization, requiring probable cause for any vehicle search in the interior and reasonable suspicion for inquiry stops by roving patrols. See <i>supra,</i> at 555-556. Our holding today, approving routine stops for brief questioning (a type of stop familiar to all motorists) is confined to permanent checkpoints. We understand, of course, that neither longstanding congressional authorization nor widely prevailing practice justifies a constitutional violation. We do suggest, however, that against this background and in the context of our recent decisions, the rhetoric of the dissent reflects unjustified concern.
</p>
<p>The dissenting opinion further warns:</p>
<p>"Every American citizen of Mexican ancestry and every Mexican alien lawfully in this country must know after today's decision that he travels the fixed checkpoint highways at [his] risk . . . ." <i>Post,</i> at 572.</p>
<p>For the reason stated in n. 16, <i>supra,</i> this concern is misplaced. Moreover, upon a proper showing, courts would not be powerless to prevent the misuse of checkpoints to harass those of Mexican ancestry.</p>
<p>[1]  <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span>,</i> which involved roving-patrol stops, said:
</p>
<p>"[Mexican ancestry] alone would justify neither a reasonable belief that they were aliens, nor a reasonable belief that the car concealed other aliens who were illegally in the country. Large numbers of native-born and naturalized citizens have the physical characteristics identified with Mexican ancestry, and even in the border area a relatively small proportion of them are aliens. The likelihood that any given person of Mexican ancestry is an alien is high enough to make Mexican appearance a relevant factor, but standing alone it does not justify stopping all Mexican-Americans to ask if they are aliens." 422 U. S., at 886-887 (footnote omitted).</p>
<p>Today we are told that secondary referrals may be based on criteria that would not sustain a roving-patrol stop, and specifically that such referrals may be based largely on Mexican ancestry. <i>Ante,</i> at 563. Even if the difference between <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> and this decision is only a matter of degree, we are not told what justifies the different treatment of Mexican appearance or why greater emphasis is permitted in the less demanding circumstances of a checkpoint. That law in this country should tolerate use of one's ancestry as probative of possible criminal conduct is repugnant under any circumstances.</p>
<p>[2]  The Court's view that "selective referralsrather than questioning the occupants of every cartend to advance some Fourth Amendment interests by minimizing the intrusion on the general motoring public," <i>ante,</i> at 560, stands the Fourth Amendment on its head. The starting point of this view is the unannounced assumption that intrusions are generally permissible; hence, any minimization of intrusions serves Fourth Amendment interests. Under the Fourth Amendment, however, the status quo is nonintrusion, for as a general matter, it is unreasonable to subject the average citizen or his property to search or seizure. Thus, minimization of intrusion only lessens the aggravation to Fourth Amendment interest; it certainly does not further those interests.</p>
<p>[3]  <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891</a></span> (1975), expressly recognized that such selectivity is a source of embarrassment: "Nor do checkpoint procedures significantly reduce the likelihood of embarrassment. Motorists whose cars are searched, unlike those who are only questioned, may not be reassured by seeing that the Border Patrol searches other cars as well." <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#895" aria-description="Citation for case: United States v. Ortiz"><i>Id.,</i> at 895</a></span>.</p>
<p>[4]  Though today's decision would clearly permit detentions to be based solely on Mexican ancestry, the Court takes comfort in what appears to be the Border Patrol practice of not relying on Mexican ancestry standing alone in referring motorists for secondary detentions. <i>Ante,</i> at 563 n. 16. See also <i>ante,</i> at 566-567, n. 19. Good faith on the part of law enforcement officials, however, has never sufficed in this tribunal to substitute as a safeguard for personal freedoms or to remit our duty to effectuate constitutional guarantees. Indeed, with particular regard to the Fourth Amendment, <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 22</a></span> (1968), held that "simple `"good faith on the part of the arresting officer is not enough." . . . If subjective good faith alone were the test, the protections of the Fourth Amendment would evaporate, and the people would be "secure in their persons, houses, papers, and effects," only in the discretion of the police.' <i>Beck</i> v. <i>Ohio,</i> [<span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89</a></span>,] 97 [1964]."
</p>
<p>Even if good faith is assumed, the affront to the dignity of American citizens of Mexican ancestry and Mexican aliens lawfully within the country is in no way diminished. The fact still remains that people of Mexican ancestry are targeted for examination at checkpoints and that the burden of checkpoint intrusions will lie heaviest on them. That, as the Court observes, <i>ante,</i> at 563 n. 16, "[l]ess than 1% of the motorists passing the checkpoint are stopped for questioning," whereas approximately 16% of the population of California is Spanish-speaking or of Spanish surname, has little bearing on this pointor, for that matter, on the integrity of Border Patrol practices. There is no indication how many of the 16% have physical and grooming characteristics identifiable as Mexican. There is no indication what portion of the motoring public in California is of Spanish or Mexican ancestry. Given the socioeconomic status of this portion, it is likely that the figure is significantly less than 16%. Neither is there any indication that those of Mexican ancestry are not subjected to lengthier initial stops than others, even if they are not secondarily detained. Finally, there is no indication of the ancestral makeup of the 1% who are referred for secondary detention. If, as is quite likely the case, it is overwhelmingly Mexican, the sense of discrimination which will be felt is only enhanced.</p>
<p>[5]  As an empirical proposition, this observation is hardly self-evident. No small number of vehicles pass through a checkpoint. Indeed, better than 1,000 pass through the San Clemente checkpoint during each hour of operation. <i>Ante,</i> at 554. Thus there is clearly abundant opportunity for abuse and harassment at checkpoints through lengthier detention and questioning of some individuals or arbitrary secondary detentions. Such practices need not be confined to those of Mexican ancestry. And given that it is easier to deal with a vehicle which has already been slowed than it is to observe and then chase and apprehend a vehicle travelling at highway speeds, if anything, there is more, not less, room for abuse or harassment at checkpoints. Indeed, in <i><span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">Ortiz</a></span>,</i> the Court was "not persuaded that the checkpoint limits to any meaningful extent the officer's discretion to select cars for search." 422 U. S., at 895. <i>A fortiori,</i> discretion can be no more limited simply because the activity is detention or questioning rather than searching.</p>
<p>[6]  <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967), does not support the Court's result. Contrary to the Court's characterization, <i>ante,</i> at 561, the searches condoned there were not "routine intrusions." The Court required that administrative searches proceed according to reasonable standards satisfied with respect to each particular dwelling searched. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#538" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 538</a></span>. The search of any dwelling at the whim of administrative personal was not permitted. The Court, however, imposes no such standards today. Instead, any vehicle and its passengers are subject to detention at a fixed checkpoint, and "no particularized reason need exist to justify" the detention. <i>Ante,</i> at 563. To paraphrase an apposite observation by the Court in <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#270" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 270</a></span> (1973), "[checkpoints] thus embodied precisely the evil the Court saw in <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> when it insisted that the `discretion of the official in the field' be circumscribed . . . ."</p>

</div>
```

---

## GROUP: content/cases/United States v. Matlock.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Matlock"
type: case
citation: "415 U.S. 164 (1974)"
parallel_cite: "94 S. Ct. 988; 39 L. Ed. 2d 242"
neutral_cite: 1974 U.S. LEXIS 8
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1974
date_decided: 1974-02-20
docket: 72-1355
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1974-02-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Matlock
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108967/united-states-v-matlock/"
  cluster_id: 108967
  opinion_id: 9425606
  identity_checked: true
homes:
  - page: "[[Consent Searches]]"
    role: "Key — Anchor"
related: ["[[Illinois v. Rodriguez]]", "[[Georgia v. Randolph]]", "[[Fernandez v. California]]", "[[Schneckloth v. Bustamonte]]", "[[Frazier v. Cupp]]"]
aliases: []
tags: ["case", "fourth-amendment", "consent-search", "third-party-consent", "common-authority", "joint-access"]
holding: "COMMON AUTHORITY: consent of one who possesses common authority over premises or effects is valid against an absent, nonconsenting…"
lake:
  record_id: United States v. Matlock
  status: verified
  projected_at: 2026-07-09
---

# United States v. Matlock

*415 U.S. 164 (1974)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Matlock was arrested in the front yard of a house where he lived with Mrs. Gayle Graff and her family. Officers did not ask Matlock for consent; instead Mrs. Graff consented to a search of the house, including the east bedroom she said she jointly occupied with him. In a diaper bag in the bedroom closet, officers found $4,995 in cash — evidence of a bank robbery. At the [[Common Legal Terms#suppression-hearing|suppression hearing]] the District Court excluded, as hearsay, Mrs. Graff's out-of-court statements that she and Matlock shared the bedroom, and suppressed the money.

## Issue
Whether a third party's voluntary consent to search shared premises is valid against an absent, nonconsenting co-occupant, and what the Government must show about that party's authority over the premises.

## Rule
A co-occupant with common authority may consent for the absent one. "The consent of one who possesses common authority over premises or effects is valid as against the absent, nonconsenting person with whom that authority is shared." — 415 U.S. at 170. ^pin-170

The prosecution "may show that permission to search was obtained from a third party who possessed common authority over or other sufficient relationship to the premises or effects sought to be inspected." — [*Id.* at 171](https://www.courtlistener.com/opinion/108967/united-states-v-matlock/#:~:text=may%20show%20that%20permission%20to). ^pin-171

Common authority is not a property concept; it rests on shared use: it "rests rather on mutual use of the property by persons generally having joint access or control for most purposes, so that it is reasonable to recognize that any of the co-inhabitants has the right to permit the inspection in his own right and that the others have assumed the risk that one of their number might permit the common area to be searched." — [*Id.* at 171](https://www.courtlistener.com/opinion/108967/united-states-v-matlock/#:~:text=rests%20rather%20on%20mutual%20use) n.7. ^pin-171a

## Application
On these facts the validity of the consent turned on whether Mrs. Graff had common authority over the east bedroom, and the District Court had wrongly kept out the evidence bearing on that question. The excluded statements and other proof tended to show that she and Matlock jointly occupied and used the bedroom; if she did share mutual use with joint access or control, her consent was valid against the absent Matlock, who had assumed the risk that a co-occupant might permit a search of the common area. Because the suppression rested on the erroneous exclusion of that evidence (including Mrs. Graff's admissions and her statements as relevant to her authority), the Court reversed and [[Reading and Citing Cases#on-remand|remanded]] for the lower courts to decide, on the full record, whether the Government had carried its burden of proving common authority.

## Conclusion
[[Consent Searches|Third-party consent]] by a co-occupant with common authority is valid against an absent co-occupant; the suppression order was reversed and the case [[Reading and Citing Cases#on-remand|remanded]] to determine whether Mrs. Graff possessed common authority over the bedroom.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Matlock* is the anchor for [[Consent Searches|third-party consent]]: [[Illinois v. Rodriguez]] extends it to officers' reasonable mistakes about *apparent* authority; [[Georgia v. Randolph]] carves out the *physically present, expressly objecting* co-occupant; and [[Fernandez v. California]] limits *[[Georgia v. Randolph|Randolph]]* to a present objector.

## Appears on
- [[Consent Searches]] — *Key — Anchor*

## Sources
- *United States v. Matlock*, 415 U.S. 164 (1974) — https://www.courtlistener.com/opinion/108967/united-states-v-matlock/ — pinpoints: 170, 171, 171 n.7.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ed2dfdc3b455a7e6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "415 U.S. 164 (1974)", "court": "U.S. Supreme Court", "neutral_cite": "1974 U.S. LEXIS 8", "official_citation_present": true, "parallel_cite": "94 S. Ct. 988; 39 L. Ed. 2d 242", "title": "United States v. Matlock", "year": "1974"}}
{"assertion_id": "8a24cf3b453b5083", "dimension": "support", "kind": "home_role", "locator": {"home": "Consent Searches"}, "payload": {"home": "Consent Searches", "role": "Key — Anchor", "title": "United States v. Matlock"}}
{"assertion_id": "fad2469d93633ad5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "COMMON AUTHORITY: consent of one who possesses common authority over premises or effects is valid against an absent, nonconsenting…", "title": "United States v. Matlock"}}
{"assertion_id": "b1c2a31106f04fa5", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1974-02-20", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Matlock", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Matlock", "varies_by_point": "false"}}
{"assertion_id": "e621f22f475069d6", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Matlock"}}
```

### lake record — United States v. Matlock

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Matlock",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Matlock",
    "case_name_short": "Matlock",
    "case_name_full": "United States v. Matlock",
    "input_case_name": "United States v. Matlock",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1974-02-20",
    "year": 1974,
    "docket": "72-1355",
    "cluster_id": 108967,
    "lead_opinion_id": 9425606,
    "sibling_ids": [
      108967,
      9425606,
      9425607,
      9425608
    ],
    "absolute_url": "/opinion/108967/united-states-v-matlock/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "415 U.S. 164",
      "volume": "415",
      "reporter": "U.S.",
      "page": "164",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "94 S. Ct. 988",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "988",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "39 L. Ed. 2d 242",
        "volume": "39",
        "reporter": "L. Ed. 2d",
        "page": "242",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1974 U.S. LEXIS 8",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "8",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "415 U.S. 164",
        "volume": "415",
        "reporter": "U.S.",
        "page": "164",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 S. Ct. 988",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "988",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "39 L. Ed. 2d 242",
        "volume": "39",
        "reporter": "L. Ed. 2d",
        "page": "242",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1974 U.S. LEXIS 8",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "8",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "415 U.S. 164",
    "official_selection": {
      "court_class": "scotus",
      "selected": "415 U.S. 164",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-170",
      "page": null,
      "quote": "--- # United States v. Matlock *415 U.S. 164 (1974)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Matlock was arrested in the front yard of a house where he lived with Mrs. Gayle Graff and her family. Officers did not ask Matlock for consent; instead Mrs. Graff consented to a search of the house, including the east bedroom she said she jointly occupied with him. In a diaper bag in the bedroom closet, officers found $4,995 in cash \u2014 evidence of a bank robbery. At the suppression hearing the District Court excluded, as hearsay, Mrs. Graff's out-of-court statements that she and Matlock shared the bedroom, and suppressed the money. ## Issue Whether a third party's voluntary consent to search shared premises is valid against an absent, nonconsenting co-occupant, and what the Government must show about that party's authority over the premises. ## Rule A co-occupant with common authority may consent for the absent one.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-171",
      "page": null,
      "quote": "may show that permission to search was obtained from a third party who possessed common authority over or other sufficient relationship to the premises or effects sought to be inspected.",
      "star_marker": "171",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 10811,
      "fragment": "#:~:text=may%20show%20that%20permission%20to",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-171a",
      "page": null,
      "quote": "rests rather on mutual use of the property by persons generally having joint access or control for most purposes, so that it is reasonable to recognize that any of the co-inhabitants has the right to permit the inspection in his own right and that the others have assumed the risk that one of their number might permit the common area to be searched.",
      "star_marker": "170",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 32667,
      "fragment": "#:~:text=rests%20rather%20on%20mutual%20use",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1974-02-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Matlock",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Evelyn",
          "cluster_id": 4786331,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. H. K. D. S. (A163158)",
          "cluster_id": 10133573,
          "cite": [
            "305 Or. App. 86",
            "469 P.3d 770"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jones",
          "cluster_id": 4517594,
          "cite": [
            "193 A.3d 957"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Washington v. Amanda Marie Torres",
          "cluster_id": 4389851,
          "cite": [
            "198 Wash. App. 864",
            "397 P.3d 900"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thomas Rigterink v. State of Florida",
          "cluster_id": 3196514,
          "cite": [
            "193 So. 3d 846",
            "41 Fla. L. Weekly Supp. 177",
            "2016 WL 1592714",
            "2016 Fla. LEXIS 835"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Glenda Smith v. City of Wyoming",
          "cluster_id": 3194781,
          "cite": [
            "821 F.3d 697",
            "2016 FED App. 0094P",
            "2016 U.S. App. LEXIS 6833",
            "2016 WL 1533998"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane1_negative"
      },
      {
        "citing_case": {
          "name": "CIAN PRIDGEN v. UNITED STATES.",
          "cluster_id": 3192171,
          "cite": [
            "134 A.3d 297",
            "2016 D.C. App. LEXIS 91",
            "2016 WL 1392012"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane1_negative"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raddatz",
          "cluster_id": 110315,
          "cite": [
            "65 L. Ed. 2d 424",
            "100 S. Ct. 2406",
            "447 U.S. 667",
            "1980 U.S. LEXIS 49"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bourjaily v. United States",
          "cluster_id": 111938,
          "cite": [
            "97 L. Ed. 2d 144",
            "107 S. Ct. 2775",
            "483 U.S. 171",
            "1987 U.S. LEXIS 2874",
            "22 Fed. R. Serv. 1105",
            "55 U.S.L.W. 4962"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patrick v. State",
          "cluster_id": 1713584,
          "cite": [
            "906 S.W.2d 481",
            "1995 WL 379872"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Orange Jell Beechum",
          "cluster_id": 358983,
          "cite": [
            "582 F.2d 898",
            "1978 U.S. App. LEXIS 8198",
            "3 Fed. R. Serv. 1185"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Medina v. California",
          "cluster_id": 112775,
          "cite": [
            "120 L. Ed. 2d 353",
            "112 S. Ct. 2572",
            "505 U.S. 437",
            "1992 U.S. LEXIS 3696"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Balentine v. State",
          "cluster_id": 1662103,
          "cite": [
            "71 S.W.3d 763",
            "2002 WL 496960"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Frye",
          "cluster_id": 5607916,
          "cite": [
            "18 Cal. 4th 894",
            "98 Cal. Daily Op. Serv. 5949",
            "959 P.2d 183",
            "98 Daily Journal DAR 8259",
            "77 Cal. Rptr. 2d 25",
            "1998 Cal. LEXIS 4688"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jenkins",
          "cluster_id": 1195356,
          "cite": [
            "997 P.2d 1044",
            "95 Cal. Rptr. 2d 377",
            "22 Cal. 4th 900"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oles v. State",
          "cluster_id": 1762668,
          "cite": [
            "993 S.W.2d 103",
            "1999 Tex. Crim. App. LEXIS 53",
            "1999 WL 330266"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Montoya",
          "cluster_id": 1202376,
          "cite": [
            "753 P.2d 729",
            "12 Brief Times Rptr. 482",
            "1988 Colo. LEXIS 39",
            "1988 WL 25119"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bruce A. Campbell v. United States District Court for the Northern District of California",
          "cluster_id": 320998,
          "cite": [
            "501 F.2d 196"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Stone",
          "cluster_id": 4958214,
          "cite": [
            "2021 COA 104"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ford v. State",
          "cluster_id": 2187417,
          "cite": [
            "305 S.W.3d 530",
            "2009 Tex. Crim. App. LEXIS 1440",
            "2009 WL 3365661"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Donald James and David Anthony Butler, United States of America v. Henry Smith and Kenneth Wayne Whitmore",
          "cluster_id": 362801,
          "cite": [
            "590 F.2d 575",
            "1979 U.S. App. LEXIS 17005",
            "3 Fed. R. Serv. 785"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Matlock:lane2_top_cited"
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
        "journal_ref": "United States v. Matlock:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108967 OR 9425606 OR 9425607 OR 9425608) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDQxNjcwNDAwMDAwJnM9Mjg5ODIxNiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108967+OR+9425606+OR+9425607+OR+9425608%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(108967 OR 9425606 OR 9425607 OR 9425608)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMzAmcz0yMDk0NzcyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108967+OR+9425606+OR+9425607+OR+9425608%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108967 OR 9425606 OR 9425607 OR 9425608)",
        "reviewed": 60,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 60,
        "triage_read": 0,
        "triage_snippet_classified": 60
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108967 OR 9425606 OR 9425607 OR 9425608)",
    "indexed_citing_opinions": 2399,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108967,
        "count": 2188,
        "count_source": "search"
      },
      {
        "opinion_id": 9425606,
        "count": 255,
        "count_source": "search"
      },
      {
        "opinion_id": 9425607,
        "count": 1,
        "count_source": "search"
      },
      {
        "opinion_id": 9425608,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3649,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-matlock.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxNzE1NDImcz0xMDMxNjc5MSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28108967+OR+9425606+OR+9425607+OR+9425608%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108967,
        "cited_id": 97847,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 104184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 107394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 108212,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 108429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 233305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 264623,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 267102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 268073,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 276553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 278916,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 288276,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 292123,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 292716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 298539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 303962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 310284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 1359720,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 1656389,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 1976399,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 2059444,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108967,
        "cited_id": 3868069,
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
    "date_created": "2026-07-06T01:32:24Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:33:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:33:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:37:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:33:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Matlock

```
<opinion type="majority">
<author id="b233-11">MR. Justice White</author>
<p id="A8b">delivered the opinion of the Court.</p>
<p id="b233-12">In <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973), the Court reaffirmed the principle that the search of property, without warrant and without probable cause, <page-number citation-index="1" label="166">*166</page-number>but with proper consent voluntarily given, is valid under the Fourth Amendment. The question now before us is whether the evidence presented by the United States with respect to the voluntary consent of a third party to search the living quarters of the respondent was legally sufficient to render the seized materials admissible in evidence at the respondent's criminal trial.</p>
<p id="b234-5">I</p>
<p id="b234-6">Respondent Matlock was indicted in February 1971 for the robbery of a federally insured bank in Wisconsin, in violation of <span class="citation no-link">18 U. S. C. § 2113</span>. A week later, he filed a motion to suppress evidence seized by law enforcement officers from a home in the town of Pardeeville, Wisconsin, in which he had been living. Suppression hearings followed. As found by the District Court, the facts were that respondent was arrested in the yard in front of the Pardeeville home on November 12, 1970. The home was leased from the owner by Mr. and Mrs. Marshall. Living in the home were Mrs. Marshall, several of her children, including her daughter Mrs. Gayle Graff, Gayle's three-year-old son, and respondent. Although the officers were aware at the time of the arrest that respondent lived in the house, they did not ask him which room he occupied or whether he would consent to a search. Three of the arresting officers went to the door of the house and were admitted by Mrs. Graff, who was dressed in a robe and was holding her son in her arms. The officers told her they were looking for money and a gun and asked if they could search the house. Although denied by Mrs. Graff at the suppression hearings, it was found that she consented voluntarily to the search of the house, including the east bedroom on the second floor which she said was jointly occupied by Matlock and herself. The east bedroom was searched and the evidence at issue here, $4,995 in cash, was found in a diaper <page-number citation-index="1" label="167">*167</page-number>bag in the only closet in the room.<footnotemark>1</footnotemark> The issue came to be whether Mrs. Graff's relationship to the east bedroom was sufficient to make her consent to the search valid against respondent Matlock.</p>
<p id="b235-5">The District Court ruled that before the seized evidence could be admitted at trial the Government'had to prove, first, that it reasonably appeared to the searching officers “just prior to the search, that facts exist which will render the consenter’s consent binding on the putative defendant,” and, second, that “just prior to the search, facts do exist which render the consenter’s consent binding on the putative defendant.” There was no requirement that express permission from respondent to Mrs. Graff to allow the officers to search be shown; it was sufficient to show her authority to consent in her own right, by reason of her relationship to the premises. The first requirement was held satisfied because of respondent’s presence in the yard of the house at the time of his arrest, because of Gayle Graff’s residence in the house for some time and her presence in the house just prior to the search, and because of her statement to the officers that she and ‘ the respondent occupied the east bedroom.<footnotemark>2</footnotemark></p>
<p id="b235-6">The District Court concluded, however, that the Government had failed to satisfy the second requirement and <page-number citation-index="1" label="168">*168</page-number>had not satisfactorily proved Mrs. Graff's actual authority to consent to the search. To arrive at this result, the District Court held that although Gayle Graff’s statements to the officers that she and the respondent occupied the east bedroom were admissible to prove the good-faith belief of the officers, they were nevertheless extrajudicial statements inadmissible to prove the truth of the facts therein averred. The same was true of Mrs. Graff’s additional statements to the officers later on November 12 that she and the respondent had been sleeping together in the east bedroom regularly, including the early morning of November 12, and that she and respondent shared the use of a dresser in the room. There was also testimony that both Gayle Graff and respondent, at various times and places and to various persons, had made statements that they were wife and husband. These statements were deemed inadmissible to prove that respondent and Gayle Graff were married, which they were not, or that they were sleeping together .as a husband and wife might be expected to do. Having excluded these declarations, the District Court then concluded that the remaining evidence was insufficient to prove “to a reasonable certainty, by the greater weight of the credible evidence, that at the time of the search, and for some period of reasonable length theretofore, Gayle Graff and the defendant were living together in the east bedroom.” The remaining evidence, briefly stated, was that Mrs. Graff and respondent had lived together in a one-bedroom apartment in Florida from April to August 1970; that they lived at the Marshall home in Pardeeville from August to November 12, 1970; that they were several times seen going up or down stairs in the house together; and that the east bedroom, which respondent was shown to have rented from Mr. and Mrs. Marshall, contained evidence that it was also lived in by <page-number citation-index="1" label="169">*169</page-number>a man and a woman.<footnotemark>3</footnotemark> The District Court thought these items of evidence created an “inference” or at least a “mild inference” that respondent and Gayle Graff at times slept together in the east bedroom, but it deemed them insufficient to satisfy the Government’s burden of proof. The District Court also rejected the Government’s claim that it was required to prove only that at the time of the search the officers could reasonably have concluded that Gayle Graff’s relationship to the east bedroom was sufficient to make her consent binding on respondent.</p>
<p id="b237-5">The Court of Appeals affirmed the judgment of the District Court in all respects. <span class="citation" data-id="310284"><a href="/opinion/310284/united-states-v-william-earl-matlock/" aria-description="Citation for case: United States v. William Earl Matlock">476 F. 2d 1083</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./412/917/">412 U. S. 917</a></span>, and now reverse the Court of Appeals.</p>
<p id="b237-6">II</p>
<p id="b237-7">It has been assumed by the parties and the courts below that the voluntary consent of any joint occupant of a residence to search the premises jointly occupied is valid against the co-occupant, permitting evidence discovered in the search to be used against him at a criminal trial. This basic proposition was accepted by the Seventh Circuit in this case, <span class="citation" data-id="310284"><a href="/opinion/310284/united-states-v-william-earl-matlock/#1086" aria-description="Citation for case: United States v. William Earl Matlock">476 F. 2d, at 1086</a></span>, as it had been in prior cases,<footnotemark>4</footnotemark> and has generally been ap<page-number citation-index="1" label="170">*170</page-number>plied in similar circumstances by other courts of appeals,<footnotemark>5</footnotemark> and various state courts.<footnotemark>6</footnotemark> This Court left open, in <em>Amos </em>v. <em>United States, </em><span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/#317" aria-description="Citation for case: Amos v. United States">255 U. S. 313, 317</a></span> (1921), the question whether a wife’s permission to search the residence in which she lived with her husband could “waive his constitutional rights,” but more recent authority here clearly indicates that the consent of one who possesses common authority over premises or effects is valid as against the absent, nonconsenting person with whom that authority is shared. In <em>Frazier </em>v. <em>Cupp, </em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/#740" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731, 740</a></span> (1969), the Court “dismissed rather quickly” the contention that the consent of the petitioner’s cousin to the search of a duffel bag, which was being used jointly by both men and had been left in the cousin’s home, would not justify the seizure of petitioner’s cloth<page-number citation-index="1" label="171">*171</page-number>ing found inside; joint use of the bag rendered the cousin’s authority to consent to its search clear. Indeed, the Court was unwilling to engage in the “metaphysical subtleties” raised by Frazier’s claim that his cousin only had permission to use one compartment within the bag. By allowing the cousin the use of the bag, and by leaving it in his house, Frazier was held to have assumed the risk that his cousin would allow someone else to look inside. <em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/" aria-description="Citation for case: Frazier v. Cupp">Ibid.</a></span> </em>More generally, in <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#245" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S., at 245-246</a></span>, we noted that our prior recognition of the constitutional validity of “third party consent” searches in cases like <em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/" aria-description="Citation for case: Frazier v. Cupp">Frazier</a></span> </em>and <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#487" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 487-490</a></span> (1971), supported the view that a consent search is fundamentally different in nature from the waiver of a trial right. These cases at least make clear that when the prosecution seeks to justify a warrantless search by proof of voluntary consent, it is not limited to proof that consent was given by the defendant, but may show that permission to search was obtained from a third party who possessed common authority over or other sufficient relationship to the premises or effects sought to be inspected.<footnotemark>7</footnotemark> The <page-number citation-index="1" label="172">*172</page-number>issue now before us is whether the Government made the requisite showing in this case.</p>
<p id="b240-4">Ill</p>
<p id="b240-5">The District Court excluded from evidence at the suppression hearings, as inadmissible hearsay, the out-of-court statements of Mrs. Graff with respect to her and respondent’s joint occupancy and use of the east bedroom, as well as the evidence that both respondent and Mrs. Graff at various times and to various persons had represented themselves as husband and wife. The Court of Appeals affirmed the ruling. Both courts were in error.</p>
<p id="b240-6">As an initial matter we fail to understand why, on any approach to the case, the out-of-court representations of respondent himself that he and Gayle Graff were husband and wife were considered to be inadmissible against him. Whether or not Mrs. Graff’s statements were hearsay, the respondent’s own out-of-court admissions would surmount all objections based on the hearsay rule both at the suppression hearings and at the trial itself, and would be admissible for whatever inferences the trial judge could reasonably draw concerning joint occupancy of the east bedroom. See 4 J. Wigmore, Evidence § 1048 (J. Chadbourn rev. 1972); C. McCormick, Evidence § 262 (2d ed. 1972).<footnotemark>8</footnotemark></p>
<p id="b240-7">As for Mrs. Graff’s statements to the searching officers, it should be recalled that the rules of evidence normally applicable in criminal trials do not operate with full force at hearings before the judge to determine the admissi<page-number citation-index="1" label="173">*173</page-number>bility of evidence.<footnotemark>9</footnotemark> In <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949), it was objected that hearsay had been used at the hearing on a challenge to the admissibility of evidence seized when a car was searched and that other evidence used at the hearing was held inadmissible at the trial itself. The Court sustained the trial court’s rulings. It distinguished between the rules applicable to proceedings to determine probable cause for arrest and search and those governing the criminal trial itself— “There is a large difference between the two things to be proved, as well as between the tribunals which determine them, and therefore a like difference in the <em>quanta </em>and modes of proof required to establish them.” <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#173" aria-description="Citation for case: Brinegar v. United States"><em>Id., </em>at 173</a></span>. That certain evidence was admitted in preliminary proceedings but excluded at the trial — and the Court thought both rulings proper- — was thought merely to “illustrate the difference in standards and latitude allowed in passing upon the distinct issues of probable cause and guilt.” <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#174" aria-description="Citation for case: Brinegar v. United States"><em>Id., </em>at 174</a></span>.</p>
<p id="b241-5">That the same rules of evidence governing criminal jury trials are not generally thought to govern hearings before a judge to determine evidentiary questions was confirmed on November 20, 1972, when the Court transmitted to Congress the proposed Federal Rules of Evidence. Rule 104 (a) provides that preliminary questions concerning admissibility are matters for <page-number citation-index="1" label="174">*174</page-number>the judge and that in performing this function he is not bound by the Rules of Evidence except those with respect to privileges.<footnotemark>10</footnotemark> Essentially the same language on the scope of the proposed Rules is repeated in Rule 1101 (d)(1).<footnotemark>11</footnotemark> The Rules in this respect reflect the general views of various authorities on evidence. 5 J. Wigmore, Evidence § 1385 (3d ed. 1940); C. McCormick, Evidence §53, p. 122 n. 91 (2d ed. 1972). See also Maguire &amp; Epstein, Rules of Evidence in Preliminary Controversies as to Admissibility, 36 Yale L. J. 1101 (1927).</p>
<p id="b242-5">Search warrants are repeatedly issued on <em>ex parte </em>affidavits containing out-of-court statements of identified and unidentified persons. <em>United States </em>v. <em>Ventresca, </em><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 108</a></span> (1965). An arrest and search without a warrant were involved in <em>McCray </em>v. <em>Illinois, </em><span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300</a></span> (1967). At the initial suppression hearing, the police proved probable cause for the arrest by testifying to the out-of-court statements of an unidentified informer. The Government would have been obligated to produce the informer and to put him on the stand had it wanted to use his testimony at defendant's trial, but we sustained the use of his out-of-court statements at the suppression hearing, as well as the Govern-<page-number citation-index="1" label="175">*175</page-number>merit’s refusal to identify him. In the course of the opinion, we specifically rejected the claim that defendant’s right to confrontation under the Sixth Amendment and Due Process Clause of the Fourteenth Amendment had in any way been violated. We also made clear that there was no contrary rule governing proceedings in the federal courts.</p>
<p id="b243-5">There is, therefore, much to be said for the proposition that in proceedings where the judge himself is considering the admissibility of evidence, the exclusionary rules, aside from rules of privilege, should not be applicable; and the judge should receive the evidence and give it such weight as his judgment and experience counsel.<footnotemark>12</footnotemark> However that may be, certainly there should be no automatic rule against the reception of hearsay evidence in such proceedings, and it seems equally clear to us that the trial judge should not have excluded Mrs. Graff’s statements in the circumstances present here.</p>
<p id="b243-6">In the first place, the court was quite satisfied that the statements had in fact been made. Second, there is nothing in the record to raise serious doubts about the truthfulness of the statements themselves. Mrs. Graff harbored no hostility or bias against respondent that might call her statements into question. Indeed, she testified on his behalf at the suppression hearings. Mrs. Graff responded to inquiry at the time of the search that she and respondent occupied the east bedroom together. A few minutes later, having led the officers to the bedroom, she stated that she and respondent shared the one dresser in the room and that the woman’s clothing in the <page-number citation-index="1" label="176">*176</page-number>room was hers. Later the same day, she stated to the officers that she and respondent had slept together regularly in the room, including the early morning of that very day. These statements were consistent with one another. They were also corroborated by other evidence received at the suppression hearings: Mrs. Graff and respondent had lived together in Florida for several months immediately prior to coming to Wisconsin, where they lived in the house in question and where they were seen going upstairs together in the evening; respondent was the tenant of the east bedroom and that room bore every evidence that it was also occupied by a woman; respondent indicated in prior statements to various people that he and Mrs. Graff were husband and wife. Under these circumstances there was no apparent reason for the judge to distrust the evidence and to exclude Mrs. Graff’s declarations from his own consideration for whatever they might be worth in resolving, one way or another, the issues raised at the suppression hearings.</p>
<p id="b244-5">If there is remaining doubt about the matter, it should be dispelled by another consideration: cohabitation out of wedlock would not seem to be a relationship that one would falsely confess. Respondent and Gayle Graff were not married, and cohabitation out of wedlock is a crime in the State of Wisconsin.<footnotemark>13</footnotemark> Mrs. Graff’s statements were against her penal interest and they carried their own indicia of reliability. This was sufficient in itself, we think, to warrant admitting them to evidence for consideration by the trial judge. This <page-number citation-index="1" label="177">*177</page-number>is the case even if they would be inadmissible hearsay at respondent's trial either because statements against penal interest are to be excluded under <em>Donnelly </em>v. <em>United States, </em><span class="citation" data-id="97847"><a href="/opinion/97847/donnelly-v-united-states/#272" aria-description="Citation for case: Donnelly v. United States">228 U. S. 243, 272-277</a></span> (1913), or because, if Rule 804 (b) (4) of the proposed Federal Rules of Evidence becomes the law, such declarations would be admissible only if the declarant is unavailable at the time of the trial.</p>
<p id="b245-5">Finally, we note that Mrs. Graff was a witness for the respondent at the suppression hearings. As such, she was available for cross-examination,-and the risk of prejudice, if there was any, from the use of hearsay was reduced. Indeed, she entirely denied that she either gave consent or made the November 12 statements to the officers that the District Court excluded from evidence. When asked whether in fact she and respondent had lived together, she claimed her privilege against self-incrimination and declined to answer.</p>
<p id="b245-6">IV</p>
<p id="b245-7">It appears to us, given the admissibility of Mrs. Graff’s and respondent’s out-of-court statements, that the Government sustained its burden of proving by the preponderance of the evidence that Mrs. Graff’s voluntary consent to search the east bedroom was legally sufficient to warrant admitting into evidence the $4,995 found in the diaper bag.<footnotemark>14</footnotemark> But we prefer that the District Court <page-number citation-index="1" label="178">*178</page-number>first reconsider the sufficiency of the evidence in the light of this decision and opinion. The judgment of the Court of Appeals is reversed and the case is remanded to the Court of Appeals with directions to remand the case to the District Court for further proceedings consistent with this opinion.</p>
<p id="b246-5">
<em>So ordered.</em>
</p>
<footnote label="1">
<p id="b235-7"> There were other seizures in the house and the east bedroom on November 12, but none of them is at issue here.</p>
</footnote>
<footnote label="2">
<p id="b235-8"> Mrs. Graff was not advised that she had a right to refuse to consent to the search. The District Court expressed no view as to whether the absence of such advice would render her consent invalid, since it found that her consent, however voluntary, would not bind the respondent with regard to the search of his room. <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973), has since made clear, of course, that it is not essential for the prosecution to show that the consenter knew of the right to refuse consent in order to establish that the consent was voluntary.</p>
</footnote>
<footnote label="3">
<p id="b237-8"> When the officers searched the east bedroom, two pillows were on the double bed, which had been slept in, men’s and women's clothes were in the closet, and men’s and women’s clothes were also in separate drawers of the dresser.</p>
</footnote>
<footnote label="4">
<p id="b237-9"><em> E. g., United States </em>v. <em>Stone, </em><span class="citation" data-id="9459007"><a href="/opinion/307293/united-states-v-ervin-w-stone/#173" aria-description="Citation for case: United States v. Ervin W. Stone">471 F. 2d 170, 173</a></span> (1972), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./411/931/">411 U. S. 931</a></span> (1973); <em>United States </em>v. <em>Wixom, </em><span class="citation" data-id="296244"><a href="/opinion/296244/united-states-v-roswell-william-wixom/#624" aria-description="Citation for case: United States v. Roswell William Wixom">441 F. 2d 623, 624-625</a></span> (1971); <em>United States </em>v. <em>Airdo, </em><span class="citation" data-id="276553"><a href="/opinion/276553/united-states-v-dominic-daniel-alrdo/#106" aria-description="Citation for case: United States v. Dominic Daniel Alrdo">380 F. 2d 103, 106-107</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./389/913/">389 U. S. 913</a></span> (1967). Each of these cases cited with approval <em>United States </em>v. <em>Sferas, </em><span class="citation" data-id="233305"><a href="/opinion/233305/united-states-v-sferas-two-cases-united-states-v-skally/#74" aria-description="Citation for case: United States v. Sferas (Two Cases). United States v. Skally">210 F. 2d 69, 74</a></span> (CA7), cert. denied <em>sub nom. Skally </em>v. <em>United States, </em><span class="citation" data-id="8925459"><a href="/opinion/8935196/skally-v-united-states/" aria-description="Citation for case: Skally v. United States">347 U. S. 935</a></span> (1954), which expressed the rule "that where two persons have equal rights <page-number citation-index="1" label="170">*170</page-number>to the use or occupation of premises, either may give consent to a search, and the evidence thus disclosed can be used against either.”</p>
</footnote>
<footnote label="5">
<p id="AKp"><em> E. g., United States </em>v. <em>Ellis, </em><span class="citation" data-id="303962"><a href="/opinion/303962/united-states-v-robert-w-ellis/#967" aria-description="Citation for case: United States v. Robert W. Ellis">461 F. 2d 962, 967-968</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./409/866/">409 U. S. 866</a></span> (1972); <em>United States </em>v. <em>Cataldo, </em><span class="citation" data-id="292716"><a href="/opinion/292716/united-states-v-joseph-cataldo-and-james-lucakos-aka-james-lucas-tn/#40" aria-description="Citation for case: United States v. Joseph Cataldo and James Lucakos, A/K/A...">433 F. 2d 38, 40</a></span> (CA2 1970), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./401/977/">401 U. S. 977</a></span> (1971); <em>United States ex rel. Cabey </em>v. <em>Mazurkiewicz, </em><span class="citation" data-id="9456020"><a href="/opinion/292123/united-states-of-america-ex-rel-william-cabey-h-2519-v-joseph/#842" aria-description="Citation for case: United States of America Ex Rel. William Cabey H-2519 v....">431 F. 2d 839, 842-843</a></span> (CA3 1970); <em>United States </em>v. <em>Thompson, </em><span class="citation" data-id="288276"><a href="/opinion/288276/united-states-v-john-thompson/#375" aria-description="Citation for case: United States v. John Thompson">421 F. 2d 373, 375-376</a></span> (CA5), vacated on other grounds, <span class="citation" data-id="108212"><a href="/opinion/108212/thompson-v-united-states/" aria-description="Citation for case: Thompson v. United States">400 U. S. 17</a></span> (1970); <em>Gurleski </em>v. <em>United States, </em><span class="citation" data-id="9454142"><a href="/opinion/282906/michael-joseph-gurleski-and-dorothy-villafranca-v-united-states-of/#260" aria-description="Citation for case: Michael Joseph Gurleski and Dorothy Villafranca v. United...">405 F. 2d 253, 260-262</a></span> (CA5 1968), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./395/981/">395 U. S. 981</a></span> (1969); <em>Wright </em>v. <em>United States, </em><span class="citation" data-id="278916"><a href="/opinion/278916/lynn-edward-wright-v-united-states/#998" aria-description="Citation for case: Lynn Edward Wright v. United States">389 F. 2d 996, 998-999</a></span> (CA8 1968); <em>Roberts </em>v. <em>United States, </em><span class="citation" data-id="264623"><a href="/opinion/264623/raymond-ralph-roberts-v-united-states/#894" aria-description="Citation for case: Raymond Ralph Roberts v. United States">332 F. 2d 892, 894-898</a></span> (CA8 1964), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./380/980/">380 U. S. 980</a></span> (1965); <em>United States </em>v. <em>Wilson, </em><span class="citation" data-id="298539"><a href="/opinion/298539/united-states-v-raymond-craig-wilson-united-states-of-america-v-wilbert/#5" aria-description="Citation for case: United States v. Raymond Craig Wilson, United States of...">447 F. 2d 1, 5-6</a></span> (CA9 1971); <em>Nelson </em>v. <em>California, </em><span class="citation" data-id="268073"><a href="/opinion/268073/chester-nelson-v-people-of-the-state-of-california-robert-a-heinze/#77" aria-description="Citation for case: Chester Nelson v. People of the State of California,...">346 F. 2d 73, 77</a></span> (CA9), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./382/964/">382 U. S. 964</a></span> (1965); <em>Burge </em>v. <em>United States, </em><span class="citation" data-id="9450504"><a href="/opinion/267102/richard-w-burge-v-united-states/#413" aria-description="Citation for case: Richard W. Burge v. United States">342 F. 2d 408, 413</a></span> (CA9), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./382/829/">382 U. S. 829</a></span> (1965).</p>
</footnote>
<footnote label="6">
<p id="b238-8"><em> E. g., People </em>v. <em>Howard, </em><span class="citation" data-id="1377086"><a href="/opinion/1377086/people-v-howard/#651" aria-description="Citation for case: People v. Howard">166 Cal. App. 2d 638, 651</a></span>, <span class="citation" data-id="1377086"><a href="/opinion/1377086/people-v-howard/#114" aria-description="Citation for case: People v. Howard">334 P. 2d 105, 114</a></span> (1958); <em>People </em>v. <em>Gorg, </em><span class="citation" data-id="1359720"><a href="/opinion/1359720/people-v-gorg/#783" aria-description="Citation for case: People v. Gorg">45 Cal. 2d 776, 783</a></span>, <span class="citation" data-id="1359720"><a href="/opinion/1359720/people-v-gorg/#473" aria-description="Citation for case: People v. Gorg">291 P. 2d 469, 473</a></span> (1955); <em>People </em>v. <em>Haskell, </em><span class="citation" data-id="1976399"><a href="/opinion/1976399/the-people-v-haskell/#28" aria-description="Citation for case: The PEOPLE v. Haskell">41 Ill. 2d 25, 28-29</a></span>, <span class="citation" data-id="1976399"><a href="/opinion/1976399/the-people-v-haskell/#432" aria-description="Citation for case: The PEOPLE v. Haskell">241 N. E. 2d 430, 432</a></span> (1968); <em>People </em>v. <em>Walker, </em><span class="citation" data-id="2059444"><a href="/opinion/2059444/the-people-v-walker/#27" aria-description="Citation for case: The People v. Walker">34 Ill. 2d 23, 27-28</a></span>, <span class="citation" data-id="2059444"><a href="/opinion/2059444/the-people-v-walker/#555" aria-description="Citation for case: The People v. Walker">213 N. E. 2d 552, 555</a></span> (1966); <em>Commonwealth ex rel. Cabey </em>v. <em>Rundle, </em><span class="citation" data-id="6259595"><a href="/opinion/6389909/commonwealth-ex-rel-cabey-v-rundle/" aria-description="Citation for case: Commonwealth ex rel. Cabey v. Rundle">432 Pa. 466</a></span>, <span class="citation" data-id="6259595"><a href="/opinion/6389909/commonwealth-ex-rel-cabey-v-rundle/" aria-description="Citation for case: Commonwealth ex rel. Cabey v. Rundle">248 A. 2d 197</a></span> (1968); <em>State </em>v. <em>Cairo, </em>74 R. I. 377, 385-386, <span class="citation" data-id="3868069"><a href="/opinion/4108204/state-v-cairo/#845" aria-description="Citation for case: State v. Cairo">60 A. 2d 841, 845</a></span> (1948); <em>Burge </em>v. <em>State, </em><span class="citation" data-id="1656389"><a href="/opinion/1656389/burge-v-state/#722" aria-description="Citation for case: Burge v. State">443 S. W. 2d 720, 722-723</a></span> (Ct. Crim. App. Tex.), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./396/934/">396 U. S. 934</a></span> (1969).</p>
</footnote>
<footnote label="7">
<p id="b239-5"> Common authority is, of course, not to be implied from the mere property interest a third party has in the property. The authority which justifies the third-party consent does not rest upon the law of property, with its attendant historical and legal refinements, see <em>Chapman </em>v. <em>United States, </em><span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span> (1961) (landlord could not validly consent to the search of a house he had rented to another), <em>Stoner </em>v. <em>California, </em><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">376 U. S. 483</a></span> (1964) (night hotel clerk could not validly consent to search of customer’s room) but rests rather on mutual use of the property by persons generally having joint access or control for most purposes, so that it is reasonable to recognize that any of the co-inhabitants has the right to permit the inspection in his own right and that the others have assumed the risk that one of their number might permit the common area to be searched.</p>
</footnote>
<footnote label="8">
<p id="b240-8"> Rule 801 (d) (2) (A) of the proposed Federal Rules of Evidence, approved by the Court on November 20, 1972, and transmitted to Congress, expressly provides that a party’s own statements offered against him at trial are not hearsay.</p>
</footnote>
<footnote label="9">
<p id="b241-6"> <em>Bridges </em>v. <em>Wixon, </em>326 U, S. 135, 153-154 (1945), upon which respondent and the Court of Appeals relied, involved the use of hearsay as substantive evidence bearing on the question of Bridges' membership in the Communist Party, a charge upon which a deportation order had been based. In addition to the fact that the use of unsworn, unsigned statements violated the rules of the Board of Immigration Appeals, the evidence was admitted to prove charges which directly jeopardized “the liberty of an individual,” <em>id., </em>at 154, and not for the purpose of determining a preliminary question of admissibility, as in this case.</p>
</footnote>
<footnote label="10">
<p id="b242-6"> Rule 104 (a) provides:</p>
<p id="b242-7">“(a) Questions of admissibility generally. Preliminary questions concerning the qualification of a person to be a witness, the existence of a privilege, or the admissibility of evidence shall be determined by the judge, subject to the provisions of subdivision (b). In making his determination he is not bound by the rules of evidence except those with respect to privileges.”</p>
</footnote>
<footnote label="11">
<p id="b242-8"> Rule 1101 (d)(1) provides:</p>
<p id="b242-9">“Rules inapplicable. The rules (other than those with respect to privileges) do not apply in the following situations:</p>
<p id="b242-10">“(1) <em>Preliminary questions of fact. </em>The determination of questions of fact preliminary to admissibility of evidence when the issue is to be determined by the judge under Rule 104 (a).”</p>
</footnote>
<footnote label="12">
<p id="b243-7"> “Should the exclusionary law of evidence, 'the child of the jury system’ in Thayer’s phrase, be applied to this hearing before the judge? Sound sense backs the view that it should not, and that the judge should be empowered to hear any relevant evidence, such as affidavits or other reliable hearsay.” C. McCormick, Evidence §53, p. 122 n. 91 (2d ed. 1972).</p>
</footnote>
<footnote label="13">
<p id="b244-6"> <span class="citation no-link">Wis. Stat. § 944.20</span> (1971) provides:</p>
<p id="b244-7">'‘Whoever does any of the following may be fined not more than $500 or imprisoned not more than one year in county jail or both: ... (3) Openly cohabits and associates with a person he knows is not his spouse under circumstances that imply sexual intercourse.”</p>
</footnote>
<footnote label="14">
<p id="b245-8"> Accordingly, we do not reach another major contention of the United States in bringing this case here: that the Government in any event had only to satisfy the District Court that the searching officers reasonably believed that Mrs. Graff had sufficient authority over the premises to consent to the search.</p>
<p id="b245-9">The Government also contends that the Court of Appeals imposed an unduly strict standard of proof on the Government by ruling that its case must be proved “to a reasonable certainty, by the great weight of the credible evidence.” But the District Court required only that the proof be by the <em>greater </em>weight of the evidence and the <page-number citation-index="1" label="178">*178</page-number>Court of Appeals merely affirmed the District Court's judgment. There was an inadvertence in articulating the applicable burden of proof, but it seems to have been occasioned by a similar inadvertence by the Government in presenting its case. In any event, the controlling burden of proof at suppression hearings should impose no greater burden than proof by a preponderance of the evidence. See <em>Lego </em>v. <em>Twomey, </em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#488" aria-description="Citation for case: Lego v. Twomey">404 U. S. 477, 488-489</a></span> (1972). We do not understand the Government to contend that the standard employed by the District Court was in error, and we have no occasion to consider whether it was.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Mendenhall.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Mendenhall"
type: case
citation: "446 U.S. 544 (1980)"
parallel_cite: "100 S. Ct. 1870; 64 L. Ed. 2d 497"
neutral_cite: 1980 U.S. LEXIS 102
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1980
date_decided: 1980-06-30
docket: 78-1821
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1980-05-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Mendenhall
  varies_by_point: false
  scope_note: "The 'free to leave' test was announced in Justice Stewart's opinion (joined on the seizure point only by Justice Rehnquist) but was later adopted by the full Court and is the governing standard."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110264/united-states-v-mendenhall/"
  cluster_id: 110264
  opinion_id: 9427929
  identity_checked: true
homes:
  - page: "[[Seizure of the Person]]"
    role: "Key — Anchor"
related: ["[[Terry v. Ohio]]", "[[Florida v. Bostick]]", "[[California v. Hodari D.]]", "[[United States v. Drayton]]", "[[Schneckloth v. Bustamonte]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure-of-the-person", "free-to-leave", "consensual-encounter", "drug-courier-profile"]
holding: "The 'free to leave' benchmark: a person is seized only if, under all the circumstances, a reasonable person would not have believed himself free to leave."
lake:
  record_id: United States v. Mendenhall
  status: verified
  projected_at: 2026-07-06
---

# United States v. Mendenhall

*446 U.S. 544 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
DEA agents at the Detroit airport approached Sylvia Mendenhall in the public concourse because she fit a drug-courier profile. They identified themselves, asked to see her ticket and identification (which were in different names), and then asked her to accompany them to a nearby DEA office, where she consented to a search of her person that produced heroin. She moved to suppress, arguing she had been unlawfully seized.

## Issue
When does a police-citizen encounter become a Fourth Amendment "seizure" of the person — that is, by what standard is a person who is approached and questioned by officers deemed "seized"?

## Rule
A person is seized only when a reasonable person would not feel free to leave. "We conclude that a person has been 'seized' within the meaning of the Fourth Amendment only if, in view of all of the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave." — 446 U.S. at 554. ^pin-554

The inquiry is objective and totality-based. "Examples of circumstances that might indicate a seizure, even where the person did not attempt to leave, would be the threatening presence of several officers, the display of a weapon by an officer, some physical touching of the person of the citizen, or the use of language or tone of voice indicating that compliance with the officer's request might be compelled." — *Id.* ^pin-554a

## Application
On these facts the initial encounter was not a seizure. The agents approached Mendenhall in a public airport concourse, identified themselves, and *asked* — rather than demanded — to see her ticket and identification; they did not display weapons, touch her, or use a commanding tone. Under all those circumstances, a reasonable person would have believed she was free to leave, so no seizure occurred when she was approached and questioned. Her later agreement to accompany the agents to the office, and her consent to the search there, were voluntary. Because there was no seizure at the outset and the search was consensual, the heroin was not the product of an unlawful seizure.

## Conclusion
No Fourth Amendment seizure occurred when the agents approached and questioned Mendenhall, and her consent to the ensuing search was voluntary; the Sixth Circuit's suppression order was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The "free to leave" formulation appeared in Justice Stewart's opinion (joined on the seizure point only by Justice Rehnquist) but was **later adopted by the full Court** and is the governing test. It was refined in [[Florida v. Bostick]] and [[United States v. Drayton]] (where a person would not want to leave regardless — e.g., a bus passenger — the question is whether a reasonable person would feel free to decline the officers' requests or otherwise terminate the encounter), and in [[California v. Hodari D.]] (a show-of-authority seizure is not complete until the suspect submits).

## Appears on
- [[Seizure of the Person]] — *Key — Anchor*

## Sources
- *United States v. Mendenhall*, 446 U.S. 544 (1980) — https://www.courtlistener.com/opinion/110264/united-states-v-mendenhall/ — pinpoint: 554.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8f187cefea4b21d2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "446 U.S. 544 (1980)", "court": "U.S. Supreme Court", "neutral_cite": "1980 U.S. LEXIS 102", "official_citation_present": true, "parallel_cite": "100 S. Ct. 1870; 64 L. Ed. 2d 497", "title": "United States v. Mendenhall", "year": "1980"}}
{"assertion_id": "824e91f9ffc82a44", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Key — Anchor", "title": "United States v. Mendenhall"}}
{"assertion_id": "b1c7d6f36c5a4823", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The 'free to leave' benchmark: a person is seized only if, under all the circumstances, a reasonable person would not have believed himself free to leave.", "title": "United States v. Mendenhall"}}
{"assertion_id": "2333f1cf2e0b3c01", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1980-05-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Mendenhall", "field_i_validity": "good_law", "scope_note": "The 'free to leave' test was announced in Justice Stewart's opinion (joined on the seizure point only by Justice Rehnquist) but was later adopted by the full Court and is the governing standard.", "title": "United States v. Mendenhall", "varies_by_point": "false"}}
{"assertion_id": "d278ed780d4b4ba2", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Mendenhall"}}
```

### lake record — United States v. Mendenhall

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Mendenhall",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Mendenhall",
    "case_name_short": "Mendenhall",
    "case_name_full": "United States v. Mendenhall",
    "input_case_name": "United States v. Mendenhall",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-06-30",
    "year": 1980,
    "docket": "78-1821",
    "cluster_id": 110264,
    "lead_opinion_id": 9427929,
    "sibling_ids": [
      110264,
      9427929,
      9427930,
      9427931
    ],
    "absolute_url": "/opinion/110264/united-states-v-mendenhall/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "446 U.S. 544",
      "volume": "446",
      "reporter": "U.S.",
      "page": "544",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 1870",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1870",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "64 L. Ed. 2d 497",
        "volume": "64",
        "reporter": "L. Ed. 2d",
        "page": "497",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 102",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "102",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "446 U.S. 544",
        "volume": "446",
        "reporter": "U.S.",
        "page": "544",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 1870",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1870",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "64 L. Ed. 2d 497",
        "volume": "64",
        "reporter": "L. Ed. 2d",
        "page": "497",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 102",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "102",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "446 U.S. 544",
    "official_selection": {
      "court_class": "scotus",
      "selected": "446 U.S. 544",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-554",
      "page": null,
      "quote": "? ## Rule A person is seized only when a reasonable person would not feel free to leave.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-554a",
      "page": null,
      "quote": "Examples of circumstances that might indicate a seizure, even where the person did not attempt to leave, would be the threatening presence of several officers, the display of a weapon by an officer, some physical touching of the person of the citizen, or the use of language or tone of voice indicating that compliance with the officer's request might be compelled.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1980-05-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Mendenhall",
    "varies_by_point": false,
    "scope_note": "The 'free to leave' test was announced in Justice Stewart's opinion (joined on the seizure point only by Justice Rehnquist) but was later adopted by the full Court and is the governing standard.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "United States v. Mendenhall:lane1_negative"
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
        "journal_ref": "United States v. Mendenhall:lane1_negative"
      },
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
        "journal_ref": "United States v. Mendenhall:lane1_negative"
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
        "journal_ref": "United States v. Mendenhall:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Evelyn",
          "cluster_id": 4786331,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane1_negative"
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
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
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
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
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
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
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
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harmelin v. Michigan",
          "cluster_id": 112646,
          "cite": [
            "115 L. Ed. 2d 836",
            "111 S. Ct. 2680",
            "501 U.S. 957",
            "1991 U.S. LEXIS 3816"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Bostick",
          "cluster_id": 112631,
          "cite": [
            "115 L. Ed. 2d 389",
            "111 S. Ct. 2382",
            "501 U.S. 429",
            "1991 U.S. LEXIS 3625",
            "59 U.S.L.W. 4708",
            "91 Daily Journal DAR 7328",
            "91 Cal. Daily Op. Serv. 4671",
            "1991 WL 105224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
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
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
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
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
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
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kolender v. Lawson",
          "cluster_id": 110926,
          "cite": [
            "75 L. Ed. 2d 903",
            "103 S. Ct. 1855",
            "461 U.S. 352",
            "1983 U.S. LEXIS 159",
            "51 U.S.L.W. 4532"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
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
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
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
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
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
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ohio v. Robinette",
          "cluster_id": 118066,
          "cite": [
            "136 L. Ed. 2d 347",
            "117 S. Ct. 417",
            "519 U.S. 33",
            "1996 U.S. LEXIS 6971"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. Delgado",
          "cluster_id": 111148,
          "cite": [
            "80 L. Ed. 2d 247",
            "104 S. Ct. 1758",
            "466 U.S. 210",
            "1984 U.S. LEXIS 57",
            "52 U.S.L.W. 4436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
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
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Chesternut",
          "cluster_id": 112095,
          "cite": [
            "100 L. Ed. 2d 565",
            "108 S. Ct. 1975",
            "486 U.S. 567",
            "1988 U.S. LEXIS 2582",
            "56 U.S.L.W. 4558"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brower Ex Rel. Estate of Caldwell v. County of Inyo",
          "cluster_id": 112218,
          "cite": [
            "103 L. Ed. 2d 628",
            "109 S. Ct. 1378",
            "489 U.S. 593",
            "1989 U.S. LEXIS 1569",
            "57 U.S.L.W. 4321"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
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
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dowthitt v. State",
          "cluster_id": 1777832,
          "cite": [
            "931 S.W.2d 244",
            "1996 Tex. Crim. App. LEXIS 93",
            "1996 WL 347772"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "National Treasury Employees Union v. Von Raab",
          "cluster_id": 112220,
          "cite": [
            "103 L. Ed. 2d 685",
            "109 S. Ct. 1384",
            "489 U.S. 656",
            "1989 U.S. LEXIS 6033",
            "1989 CCH OSHD 28,589",
            "4 I.E.R. Cas. (BNA) 246",
            "57 U.S.L.W. 4338",
            "49 Empl. Prac. Dec. (CCH) 38,792"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reid v. Georgia",
          "cluster_id": 110336,
          "cite": [
            "65 L. Ed. 2d 890",
            "100 S. Ct. 2752",
            "448 U.S. 438",
            "1980 U.S. LEXIS 148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
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
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Montoya De Hernandez",
          "cluster_id": 111509,
          "cite": [
            "87 L. Ed. 2d 381",
            "105 S. Ct. 3304",
            "473 U.S. 531",
            "1985 U.S. LEXIS 120",
            "53 U.S.L.W. 5048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McGee v. Commonwealth",
          "cluster_id": 1067400,
          "cite": [
            "487 S.E.2d 259",
            "25 Va. App. 193",
            "1997 Va. App. LEXIS 444"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Mendenhall:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110264 OR 9427929 OR 9427930 OR 9427931) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTg3MDgxNjAwMDAwJnM9NDc0NjIxMCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110264+OR+9427929+OR+9427930+OR+9427931%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110264 OR 9427929 OR 9427930 OR 9427931)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01Mjkmcz0xNjcwODU1JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110264+OR+9427929+OR+9427930+OR+9427931%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110264 OR 9427929 OR 9427930 OR 9427931)",
        "reviewed": 98,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 98,
        "triage_read": 3,
        "triage_snippet_classified": 95
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110264 OR 9427929 OR 9427930 OR 9427931)",
    "indexed_citing_opinions": 3716,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110264,
        "count": 3292,
        "count_source": "search"
      },
      {
        "opinion_id": 9427929,
        "count": 497,
        "count_source": "search"
      },
      {
        "opinion_id": 9427930,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427931,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6316,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-mendenhall.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNjk1Mzcmcz0xMDU5MzEzNyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110264+OR+9427929+OR+9427930+OR+9427931%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110264,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 101075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 108153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 108330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 109422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 109776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 269987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 344429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 345757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 365570,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110264,
        "cited_id": 2364698,
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
    "date_created": "2026-07-06T01:37:11Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:37:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:37:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:42:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:37:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Mendenhall

```
<opinion type="majority">
<author id="b604-9">Mr. Justice Stewart</author>
<p id="Adm">announced the judgment of the Court and delivered an opinion, in which Mr. Justice Rehnquist joined.<footnotemark>†</footnotemark></p>
<p id="b604-10">The respondent was brought to trial in the United States District Court for the Eastern District of Michigan on a <page-number citation-index="1" label="547">*547</page-number>charge of possessing heroin with intent to distribute it. She moved to suppress the introduction at trial of the heroin as evidence against her on the ground that it had been acquired from her through an unconstitutional search and seizure by agents of the Drug Enforcement Administration (DEA). The District Court denied the respondent’s motion, and she was convicted after a trial upon stipulated facts. The Court of Appeals reversed, finding the search of the respondent’s person to have been unlawful. We granted certiorari to consider whether any right of the respondent guaranteed by the Fourth Amendment was violated in the circumstances presented by this case. <span class="citation multiple-matches"><a href="/c/U.%20S./444/822/">444 U. S. 822</a></span>.</p>
<p id="b605-5">I</p>
<p id="b605-6">At the hearing in the trial court on the respondent’s motion to suppress, it was established how the heroin she was charged with possessing had been obtained from her. The respondent arrived at the Detroit Metropolitan Airport on a commercial airline flight from Los Angeles early in the morning on February 10, 1976. As she disembarked from the airplane, she was observed by two agents of the DEA, who were present at the airport for the purpose of detecting unlawful traffic in narcotics. After observing the respondent’s conduct, which appeared to the agents to be characteristic of persons unlawfully carrying narcotics,<footnotemark>1</footnotemark> the agents approached her as she was walking through the concourse, identified themselves as federal <page-number citation-index="1" label="548">*548</page-number>agents, and asked to see her identification and airline ticket. The respondent produced her driver’s license, which was in the name of Sylvia Mendenhall, and, in answer to a question of one of the agents, stated that -she resided at the address appearing on the license. The airline ticket was issued in the name of “Annette Ford.” When asked why the ticket bore a name different from her own, the respondent stated that she “just felt like using that name.” In response to a further question, the respondent indicated that she had been in California only two days. Agent Anderson then specifically identified himself as a federal narcotics agent and, according to his testimony, the respondent “became quite shaken, extremely nervous. She had a hard time speaking.”</p>
<p id="b606-5">After returning the airline ticket and driver’s license to her, Agent Anderson asked the respondent if she would accompany him to the airport DEA office for further questions. She did so, although the record does not indicate a verbal response to the request. The office, which was located up one flight of stairs about 50 feet from where the respondent had first been approached, consisted of a reception area adjoined by three other rooms. At the office the agent asked the respondent if she would allow a search of her person and handbag and told her that she had the right to decline the search if she desired. She responded: “Go ahead.” She then handed Agent Anderson her purse, which contained a receipt for an airline ticket that had been issued to “F. Bush” three days earlier for a flight from Pittsburgh through Chicago to Los Angeles. The agent asked whether this was the ticket that she had used for her flight to California, and the respondent stated that it was.</p>
<p id="b606-6">A female police officer then arrived to conduct the search of the respondent’s person. She asked the agents if the respondent had consented to be searched. The agents said that she had, and the respondent followed the policewoman into a private room. There the policewoman again asked the respondent if she consented to the search, and the respondent <page-number citation-index="1" label="549">*549</page-number>replied that- she did. The policewoman explained that the search would require that the respondent remove her clothing. The respondent stated that she had a plane to catch and was assured by the policewoman that if she were carrying no narcotics, there would be no problem. The respondent then began to disrobe without further comment. As the respondent removed her clothing, she took from her undergarments two small packages, one of which appeared to contain heroin, and handed both to the policewoman. The agents then arrested the respondent for possessing heroin.</p>
<p id="b607-5">It was on the basis of this evidence that the District Court denied the respondent’s motion to suppress. The court concluded that the agents’ conduct in initially approaching the respondent and asking to see her ticket and identification was a permissible investigative stop under the standards of <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span>, and <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span>, finding that this conduct was based on specific and articulable facts that justified a suspicion of criminal activity. The court also found that the respondent had not been placed under arrest or otherwise detained when she was asked to accompany the agents to the DEA office, but had accompanied the agents “ ‘voluntarily in a spirit of apparent cooperation.’ ” It was the court’s view that no arrest occurred until after the heroin had been found. Finally, the trial court found that the respondent “gave her consent to the search [in the DEA office] and . . . such consent was freely and voluntarily given.”</p>
<p id="b607-6">The Court of Appeals reversed the respondent’s subsequent conviction, stating only that “the court concludes that this case is indistinguishable from <em>United States </em>v. <em>McCaleb,” </em><span class="citation" data-id="344429"><a href="/opinion/344429/united-states-v-robert-ross-mccaleb-and-brenda-page/" aria-description="Citation for case: United States v. Robert Ross McCaleb and Brenda Page">552 F. 2d 717</a></span> (CA6 1977).<footnotemark>2</footnotemark> In <em>McCaleb </em>the Court of Appeals had suppressed heroin seized by DEA agents at the Detroit Airport in circumstances substantially similar to those in the <page-number citation-index="1" label="550">*550</page-number>present case.<footnotemark>3</footnotemark> The Court of Appeals there disapproved the Government’s reliance on the so-called “drug courier profile,” and held that the agents could not reasonably have suspected criminal activity in that case, for the reason that “the activities of the [persons] observed by DEA agents, were consistent with innocent behavior,” <span class="citation" data-id="344429"><a href="/opinion/344429/united-states-v-robert-ross-mccaleb-and-brenda-page/#720" aria-description="Citation for case: United States v. Robert Ross McCaleb and Brenda Page"><em>id., </em>at 720</a></span>. The Court of Appeals further concluded in <em>McCaleb </em>that, even if the initial approach had been permissible, asking the suspects to accompany the agents to a private room for further questioning constituted an arrest requiring probable cause. Finally, the court in <em>McCaleb </em>held that the consent to the search in that case had not been voluntarily given, principally because it was the fruit of what the court believed to have been an unconstitutional detention.</p>
<p id="b608-5">On rehearing en banc of the present case, the Court of Appeals reaffirmed its original decision, stating simply that the respondent had not validly consented to the search “within the meaning of <em>[McCaleb].” </em><span class="citation" data-id="9465699"><a href="/opinion/365570/united-states-v-sylvia-l-mendenhall-and-david-a-camacho/#707" aria-description="Citation for case: United States v. Sylvia L. Mendenhall and David A. Camacho">596 F. 2d 706, 707</a></span>.</p>
<p id="b608-6">II</p>
<p id="b608-7">The Fourth Amendment provides that “the right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated. . . .” There is no question in this case that the respondent possessed this constitutional right of personal security as she walked through the Detroit Airport, for “the Fourth Amendment protects people, not places,” <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span>. Here the Government concedes that its agents had neither a warrant nor probable cause to believe that the respondent was carrying narcotics when <page-number citation-index="1" label="551">*551</page-number>the agents conducted a search of the respondent’s person. It is the Government’s position, however, that the search was conducted pursuant to the respondent’s consent,<footnotemark>4</footnotemark> and thus was excepted from the requirements of both a warrant and probable cause. See <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span>. Evidently, the Court of Appeals concluded that the respondent’s apparent consent to the search was in fact not voluntarily given and was in any event the product of earlier official conduct violative of the Fourth Amendment. We must first consider, therefore, whether such conduct occurred, either on the concourse or in the DEA office at the airport.</p>
<p id="b609-5">A</p>
<p id="b609-6">The Fourth Amendment’s requirement that searches and seizures be founded upon an objective justification, governs all seizures of the person, “including seizures that involve only a brief detention short of traditional arrest. <em>Davis </em>v. <em>Mississippi, </em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969); <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 16-19</a></span> (1968).” <em>United States </em>v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce"><em>Brignoni-Ponce, supra, </em>at 878</a></span>.<footnotemark>5</footnotemark> Accordingly, if the respondent was “seized” when the DEA <page-number citation-index="1" label="552">*552</page-number>agents approached her on the concourse and asked questions of her, the agents’ conduct in doing so was constitutional only if they reasonably suspected the respondent of wrongdoing. But “[o]bviously, not all personal intercourse between policemen and citizens involves 'seizures’ of persons. Only when the officer, by means of physical force or show of authority, has in some way restrained the liberty of a citizen may we conclude that a 'seizure’ has occurred.” <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 19, n. 16</a></span>.</p>
<p id="b610-5">The distinction between an intrusion amounting to a “seizure” of the person and an encounter that intrudes upon no constitutionally protected interest is illustrated by the facts of <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio</a></span>, </em>which the Court recounted as follows: “Officer McFadden approached the three men, identified himself as a police officer and asked for their names. . . . When the men 'mumbled something’ in response to his inquiries, Officer McFadden grabbed petitioner Terry, spun him around so that they were facing the other two, with Terry between McFadden and the others, and patted down the outside of his clothing.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#6" aria-description="Citation for case: Terry v. Ohio"><em>Id., </em>at 6-7</a></span>. Obviously the officer “seized” Terry and subjected him to a “search” when he took hold of him, spun him around, and patted down the outer surfaces of his clothing, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio"><em>id., </em>at 19</a></span>. What was not determined in that case, however, was that a seizure had taken place before the officer physically restrained Terry for purposes of searching his per<page-number citation-index="1" label="553">*553</page-number>son for weapons. The Court “assume [d] that up to that point no intrusion upon constitutionally protected rights had occurred.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio"><em>Id., </em>at 19, n. 16</a></span>. The Court’s assumption appears entirely correct in view of the fact, noted in the concurring opinion of Mr. Justice White, that “[t]here is nothing in the Constitution which prevents a policeman from addressing questions to anyone on the streets,” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#34" aria-description="Citation for case: Terry v. Ohio"><em>id., </em>at 34</a></span>. Police officers enjoy “the liberty (again, possessed by every citizen) to address questions to other persons,” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#31" aria-description="Citation for case: Terry v. Ohio"><em>id., </em>at 31, 32-33</a></span> (Harlan, J., concurring), although “ordinarily the person addressed has an equal right to ignore his interrogator and walk away.” <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ibid.</a></span></em></p>
<p id="b611-5">Similarly, the Court in <em>Sibron </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span>, a case decided the same day as <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio</a></span>, </em>indicated that not every encounter between a police officer and a citizen is an intrusion requiring an objective justification. In that case, a police officer, before conducting what was later found to have been an unlawful search, approached Sibron in a restaurant and told him to come outside, which Sibron did. The Court had no occasion to decide whether there was a “seizure” of Sibron inside the restaurant antecedent to the seizure that accompanied the search. The record was “barren of any indication whether Sibron accompanied [the officer] outside in submission to a show of force or authority which left him no choice, or <em>whether he went voluntarily in a spirit of apparent cooperation </em>with the officer’s investigation.” 392 U. S., at 63 (emphasis added). Plainly, in the latter event, there was no seizure until the police officer in some way demonstrably curtailed Sibron’s liberty.</p>
<p id="b611-6">We adhere to the view that a person is “seized” only when, by means of physical force or a show of authority, his freedom of movement is restrained. Only when such restraint is imposed is there any foundation whatever for invoking constitutional safeguards. The purpose of the Fourth Amendment is not to eliminate all contact between the police and the citizenry, but “to prevent arbitrary and oppressive inter<page-number citation-index="1" label="554">*554</page-number>ference by enforcement officials with the privacy and personal security of individuals.” <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#554" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 554</a></span>. As long as the person to whom questions are put remains free to disregard the questions and walk away, there has been no intrusion upon that person’s liberty or privacy as would under the Constitution require some particularized and objective justification.</p>
<p id="b612-5">Moreover, characterizing every street encounter between a citizen and the police as a “seizure,” while not enhancing any interest secured by the Fourth Amendment, would impose wholly unrealistic restrictions upon a wide variety, of legitimate law enforcement practices. The Court has on other occasions referred to the acknowledged need for police questioning as a tool in the effective enforcement of the criminal laws. “Without such investigation, those who were innocent might be falsely accused, those who were guilty might wholly escape prosecution, and many crimes would go unsolved. In short, the security of all would be diminished. <em>Haynes </em>v. <em>Washington, </em><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#515" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503, 515</a></span>.” <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#225" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S., at 225</a></span>.</p>
<p id="b612-6">We conclude that a person has been “seized” within the meaning of the Fourth Amendment only if, in view of all of the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave.<footnotemark>6</footnotemark> Examples of circumstances that might indicate a seizure, even where the person did not attempt to leave, would be the threatening presence of several officers, the display of a weapon by an officer, some physical touching of the person of the citizen, or the use of language or tone of voice indicating that compliance with the officer’s request might be compelled. See <em>Terry </em>v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio"><em>Ohio, supra, </em>at 19, n. 16</a></span>; <em>Dunaway </em>v. <page-number citation-index="1" label="555">*555</page-number><em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#207" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 207</a></span>, and n. 6; 3 W. LaFave, Search and Seizure 53-55 (1978). In the absence of some such evidence, otherwise inoffensive contact between a member of the public and the police cannot, as a matter of law, amount to a seizure of that person.</p>
<p id="b613-5">On the facts of this case, no “seizure” of the respondent occurred. The events took place in the public concourse. The agents wore no uniforms and displayed no weapons. They did not summon the respondent to their presence, but instead approached her and identified themselves as federal agents. They requested, but did not demand to see the respondent’s identification and ticket. Such conduct, without more, did not amount to an intrusion upon any constitutionally protected interest. The respondent was not seized simply by reason of the fact that the agents approached her, asked her if she would show them her ticket and identification, and posed to her a few questions. Nor was it enough to establish a seizure that the person asking the questions was a law enforcement official. See <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#31" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 31, 32-33</a></span> (Harlan, J., concurring). See also ALI, Model Code of Pre-Arraignment Procedure § 110.1 (1) and commentary, at 257-261 (1975). In short, nothing in the record suggests that the respondent had any objective reason to believe that she was not free to end the conversation in the concourse and proceed on her way, and for that reason we conclude that the agents’ initial approach to her was not a seizure.</p>
<p id="b613-6">Our conclusion that no seizure occurred is not affected the fact that the respondent was not expressly told by the agents that she was free to decline to cooperate with their inquiry, for the voluntariness of her responses does not depend upon her having been so informed. See <em>Schneckloth </em>v. <em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Bustamonte, supra.</a></span> </em>We also reject the argument that the only inference to be drawn from the fact that the respondent acted in a manner so contrary to her self-interest is that she was compelled to answer the agents’ questions. It may happen that a person makes statements to law enforcement <page-number citation-index="1" label="556">*556</page-number>officials that he later regrets, but the issue in such cases is not whether the statement was self-protective, but rather whether it was made voluntarily.</p>
<p id="b614-5">The Court’s decision last Term in <em>Brown </em>v. <em>Texas, </em><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">443 U. S. 47</a></span>, on which the respondent relies, is not apposite. It could not have been plainer under the circumstances there presented that Brown was forcibly detained by the officers. In that case, two police officers approached Brown in an alley, and asked him to identify himself and to explain his reason for being there. Brown “refused to identify himself and angrily asserted that the officers had no right to stop him,” <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#49" aria-description="Citation for case: Brown v. Texas"><em>id., </em>at 49</a></span>. Up to this point there was no seizure. But after continuing to protest the officers’ power to interrogate him, Brown was first frisked, and then arrested for violation of a state statute making it a criminal offense for a person to refuse to give his name and address to an officer “who has lawfully stopped him and requested the information.” The Court simply held in that case that because the officers had no reason to suspect Brown of wrongdoing, there was no basis for detaining him, and therefore no permissible foundation for applying the state statute in the circumstances there presented. <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#52" aria-description="Citation for case: Brown v. Texas"><em>Id., </em>at 52-53</a></span>.</p>
<p id="b614-6">The Court’s decisions involving investigatory stops of automobiles do not point in any different direction. In <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span>, the Court held that a roving patrol of law enforcement officers could stop motorists in the general area of an international border for brief inquiry into their residence status only if the officers reasonably suspected that the vehicle might contain aliens who were illegally in the country. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce"><em>Id., </em>at 881-882</a></span>. The Government did not contend in that case that the persons whose automobiles were detained were not seized. Indeed, the Government acknowledged that the occupants of a detained vehicle were required to respond to the officers’ questions and on some occasions to produce documents evidencing their eligibility to be in the United States. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#880" aria-description="Citation for case: United States v. Brignoni-Ponce"><em>Id., </em>at 880</a></span>. Moreover, stopping or diverting an automobile in transit, with the attendant opportunity for <page-number citation-index="1" label="557">*557</page-number>a visual inspection of areas of the passenger compartment not otherwise observable, is materially more intrusive than a question put to a passing pedestrian, and the fact that the former amounts to a seizure tells very little about the constitutional status of the latter. See also <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648</a></span>; <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 556-559</a></span>.</p>
<p id="b615-4">B</p>
<p id="b615-5">Although we have concluded that the initial encounter between the DEA agents and the respondent on the concourse at the Detroit Airport did not constitute an unlawful seizure, it is still arguable that the respondent’s Fourth Amendment protections were violated when she went from the concourse to the DEA office. Such a violation might in turn infect the subsequent search of the respondent’s person.</p>
<p id="b615-6">The District Court specifically found that the respondent accompanied the agents to the office <em>“ </em>'voluntarily in a spirit of apparent cooperation,’ ” quoting <em>Sibron </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#63" aria-description="Citation for case: Sibron v. New York">392 U. S., at 63</a></span>. Notwithstanding this determination by the trial court, the Court of Appeals evidently concluded that the agents’ request that the respondent accompany them converted the situation into an arrest requiring probable cause in order to be found lawful. But because the trial court’s finding was sustained by the record, the Court of Appeals was mistaken in substituting for that finding its view of the evidence. See <em>Jackson </em>v. <em>United States, </em>122 U. S. App. D. C. 324, <span class="citation" data-id="9451218"><a href="/opinion/269987/henry-w-jackson-v-united-states/" aria-description="Citation for case: Henry W. Jackson v. United States">353 F. 2d 862</a></span> (1965).</p>
<p id="b615-7">The question whether the respondent’s consent to accompany the agents was in fact voluntary or was the product of duress or coercion, express or implied, is to be determined by the totality of all the circumstances, <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#227" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S., at 227</a></span>, and is a matter which the Government has the burden of proving. <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#222" aria-description="Citation for case: Schneckloth v. Bustamonte"><em>Id., </em>at 222</a></span>, citing <em>Bumper </em>v. <em>North Carolina, </em><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#548" aria-description="Citation for case: Bumper v. North Carolina">391 U. S. 543, 548</a></span>. The respondent herself did not testify at the hearing. The Government’s evidence showed that the respondent was not told that she <page-number citation-index="1" label="558">*558</page-number>had to go to the office, but was simply asked if she would accompany the officers. There were neither threats nor any show of force. The respondent had been questioned only briefly, and her ticket and identification were returned to her before she was asked to accompany the officers.</p>
<p id="b616-4">On the other hand, it is argued that the incident would reasonably have appeared coercive to the respondent, who was 22 years old and had not been graduated from high school. It is additionally suggested that the respondent, a female and a Negro, may have felt unusually threatened by the officers, who were white males. While these factors were not irrelevant, see <em>Schneckloth </em>v. <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#226" aria-description="Citation for case: Schneckloth v. Bustamonte"><em>Bustamonte, supra, </em>at 226</a></span>, neither were they decisive, and the totality of the evidence in this case was plainly adequate to support the District Court’s finding that the respondent voluntarily consented to accompany the officers to the DEA office.</p>
<p id="b616-5">C</p>
<p id="b616-6">Because the search of the respondent’s person was not preceded by an impermissible seizure of her person, it cannot be contended that her apparent consent to the subsequent search was infected by an unlawful detention. There remains to be considered whether the respondent’s consent to the search was for any other reason invalid. The District Court explicitly credited the officers’ testimony and found that the “consent was freely and voluntarily given,” citing <em>Schneckloth </em>v. <em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Bustamonte, supra.</a></span> </em>There was more than enough evidence in this case to sustain that view. First, we note that the respondent, who was 22 years old and had an llth-grade education, was plainly capable of a knowing consent. Second, it is especially significant that the respondent was twice expressly told that she was free to decline to consent to the search, and only thereafter explicitly consented to it. Although the Constitution does not require “proof of knowledge of a right to refuse as the <em>sine qua non </em>of an effective consent to a search,” <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#234" aria-description="Citation for case: Schneckloth v. Bustamonte"><em>id., </em>at 234</a></span> (footnote omitted), such knowledge <page-number citation-index="1" label="559">*559</page-number>was highly relevant to the determination that there had been consent. And, perhaps more important for present purposes, the fact that the officers themselves informed the respondent that she was free to withhold her consent substantially lessened the probability that their conduct could reasonably have appeared to her to be coercive.</p>
<p id="b617-5">Counsel for the respondent has argued that she did in fact resist the search, relying principally on the testimony that when she- was told that the search would require the removal of her clothing, she stated to the female police officer that “she had a plane to catch.” But the trial court was entitled to view the statement as simply an expression of concern that the search be conducted quickly. The respondent had twice unequivocally indicated her consent to the search, and when assured by the police officer that there would be no problem-, if nothing were turned up by the search, she began to undress without further comment.</p>
<p id="b617-6">Counsel for the respondent has also argued that because she was within the DEA office when she consented to the search, her consent may have resulted from the inherently coercive nature of those surroundings. But in view of the District Court’s finding that the respondent’s presence in the office was voluntary, the fact that she was there is little or no evidence that she was in any way coerced. And in response to the argument that the respondent would not voluntarily have consented to a search that was likely to disclose the narcotics that she carried, we repeat that the question is not whether the respondent acted in her ultimate self-interest, but whether she acted voluntarily.<footnotemark>7</footnotemark></p>
<p id="b617-7">Ill</p>
<p id="b617-8">We conclude that the District Court’s determination that the respondent consented to the search of her person “freely <page-number citation-index="1" label="560">*560</page-number>and voluntarily” was sustained by the evidence and that the Court of Appeals was, therefore, in error in setting it aside. Accordingly, the judgment of the Court of Appeals is reversed, and the case is remanded to that court for further proceedings.</p>
<p id="b618-5">
<em>It is so ordered.</em>
</p>
<footnote label="†">
<p id="b604-13">The Chief Justice, Mr. Justice Blachmun, and Mr. Justice Powell also join all but Part II-A of this opinion.</p>
</footnote>
<footnote label="1">
<p id="b605-7"> The agent testified that 'the respondent’s behavior fit the so-called “drug courier profile” — an informally compiled abstract of characteristics thought typical of persons carrying illicit drugs. In this case the agents thought it relevant that (1) the respondent was arriving on a flight from Los Angeles, a city believed by the agents to be the place of origin for much of the heroin brought to Detroit; (2) the respondent was the last person to leave the plane, “appeared to be very nervous,” and “completely scanned the whole area where [the agents] were standing”; (3) after leaving the plane the respondent proceeded past the baggage area without claiming any luggage; and (4) the respondent changed airlines for her flight out of Detroit.</p>
</footnote>
<footnote label="2">
<p id="b607-7"> The opinion of the Court of Appeals and the opinion of the District Court are both unreported.</p>
</footnote>
<footnote label="3">
<p id="b608-8"> The <em>McCaleb </em>case, however, involved a circumstance not present here. Although the persons searched in that case were advised of their right to decline to give consent to the search of their luggage, they were also informed that if they refused they would be detained while the agents sought a search warrant. <span class="citation" data-id="344429"><a href="/opinion/344429/united-states-v-robert-ross-mccaleb-and-brenda-page/#719" aria-description="Citation for case: United States v. Robert Ross McCaleb and Brenda Page">552 F. 2d, at 719</a></span>. The Court of Appeals in this case evidently considered the distinction irrelevant.</p>
</footnote>
<footnote label="4">
<p id="b609-7"> The Government has made several alternative arguments in this ease.</p>
</footnote>
<footnote label="5">
<p id="b609-8"> In the District Court and the Court of Appeals, the parties evidently assumed that the respondent was seized when she was approached on the airport concourse and was asked if she would show her identification and airline ticket. In its brief on the merits and oral argument in this Court, however, the Government has argued that no seizure occurred, and the respondent has joined the argument. While the Court ordinarily does not consider matters neither raised before nor decided by the courts below, see <em>Adickes </em>v. <em>Kress &amp; Co., </em><span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/#147" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">398 U. S. 144, 147, n. 2</a></span>, it has done so in exceptional circumstances. See <em>Youakim </em>v. <em>Miller, </em><span class="citation" data-id="109422"><a href="/opinion/109422/youakim-v-miller/#234" aria-description="Citation for case: Youakim v. Miller">425 U. S. 231, 234</a></span>; <em>Duignan </em>v. <em>United States, </em><span class="citation" data-id="101075"><a href="/opinion/101075/duignan-v-united-states/#200" aria-description="Citation for case: Duignan v. United States">274 U. S. 195, 200</a></span>. We consider the Government’s contention that there was no seizure of the respondent in this case, because the contrary assumption, embraced by the trial court and the Court of Appeals, rests on a serious misapprehension of federal constitutional law. And because the determination of the question is essential to the correct disposition of the other issues in the case, we shall treat it as “fairly comprised” by the questions presented in the petition for cer-tiorari. This Court’s Rule 23 (1) (c). See <em>Procunier </em>v. <em>Navarette, </em><span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/#559" aria-description="Citation for case: Procunier v. Navarette">434 <page-number citation-index="1" label="552">*552</page-number>U. S. 555, 559-560, n. 6</a></span>; <em>Blonder-Tongue Laboratories, Inc. </em>v. <em>University of Illinois Foundation, </em><span class="citation" data-id="108330"><a href="/opinion/108330/blonder-tongue-laboratories-inc-v-university-of-illinois-foundation/#320" aria-description="Citation for case: Blonder-Tongue Laboratories, Inc. v. University of...">402 U. S. 313, 320-321, n. 6</a></span>.</p>
<p id="AgI">The evidentiary record in the trial court is adequate to permit consideration of the contention. The material facts are not disputed. A major question throughout the controversy has been whether the respondent was at any time detained by the DEA agents. Counsel for the respondent has argued that she was arrested while proceeding through the concourse. The trial court and the Court of Appeals characterized the incident as an “investigatory stop.” But the correctness of the legal characterization of the facts appearing in the record is a matter for this Court to determine. See <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#226" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 226</a></span>; <em>Bumper </em>v. <em>North Carolina, </em><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#548" aria-description="Citation for case: Bumper v. North Carolina">391 U. S. 543, 548-550</a></span>.</p>
</footnote>
<footnote label="6">
<p id="b612-7"> We agree with the District Court that the subjective intention of the DEA agent in this case to detain the respondent, had she attempted to leave, is irrelevant except insofar as that may have been conveyed to the respondent.</p>
</footnote>
<footnote label="7">
<p id="b617-9"> It is arguable that the respondent may have thought she was acting in her self-interest, by voluntarily cooperating with the officers in the hope of receiving more lenient treatment.</p>
</footnote>
</opinion>
```

---
