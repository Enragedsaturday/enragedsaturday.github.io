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

## GROUP: content/cases/Kirk v. Louisiana.md  (`case`, 5 assertions)

### content_page

```
---
title: "Kirk v. Louisiana"
type: case
citation: "536 U.S. 635 (2002)"
parallel_cite: "122 S. Ct. 2458; 153 L. Ed. 2d 599; 2002 D.A.R. 7071"
neutral_cite: 2002 U.S. LEXIS 4682
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2002
date_decided: 2002-06-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2002-06-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Kirk v. Louisiana
  varies_by_point: false
  scope_note: "Good law. Per curiam. Reaffirms Payton v. New York: absent exigent circumstances, police may not make a warrantless entry into a home to arrest; they need either a warrant or probable cause plus exigent circumstances."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/121167/kirk-v-louisiana/"
  cluster_id: 121167
  opinion_id: 121167
  identity_checked: true
homes:
  - page: "[[Arrest in the Home]]"
    role: "Progeny"
related: ["[[Payton v. New York]]", "[[Steagald v. United States]]", "[[Welsh v. Wisconsin]]", "[[Kentucky v. King]]"]
aliases: []
tags: ["case", "fourth-amendment", "arrest-in-the-home", "warrant", "exigent-circumstances", "per-curiam"]
holding: "Absent exigent circumstances, police may not enter a home to make a warrantless arrest; a lawful home entry requires a warrant or probable cause plus exigent circumstances (reaffirming Payton)."
lake:
  record_id: Kirk v. Louisiana
  status: verified
  projected_at: 2026-07-06
---

# Kirk v. Louisiana

*536 U.S. 635 (2002)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After an anonymous tip that drugs were being sold from Kirk's apartment, officers watched the apartment, saw what appeared to be several drug purchases, and stopped one buyer on the street nearby. Fearing that evidence would be destroyed, they entered Kirk's apartment without a warrant, arrested him, frisked him (finding a cocaine vial in his underwear), and observed contraband in plain view; only then did they obtain a search warrant. The Louisiana Court of Appeal upheld the entry and search without deciding whether [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] existed, reasoning that the officers had probable cause to arrest and that the incriminating evidence was found on Kirk's person incident to the arrest.

## Issue
Whether police may make a warrantless entry into a home to arrest a suspect — and conduct a search incident to that arrest — without either a warrant or [[Exigent Circumstances and Hot Pursuit|exigent circumstances]], so long as they have probable cause to arrest.

## Rule
No. The Fourth Amendment draws a firm line at the home's threshold: under *[[Payton v. New York]]*, "[a]bsent exigent circumstances," the "firm line at the entrance to the house . . . may not reasonably be crossed without a warrant." — 536 U.S. at 636 (quoting *Payton*). ^pin-636

Accordingly, "police officers need either a warrant or probable cause plus exigent circumstances in order to make a lawful entry into a home. The Court of Appeal's ruling to the contrary, and consequent failure to assess whether exigent circumstances were present in this case, violated *Payton*." — *Id.* at 638. ^pin-638

## Application
The officers had neither an arrest warrant nor a search warrant when they entered Kirk's home, arrested him, and searched him. They invoked a fear that evidence would be destroyed, but the Louisiana court never determined whether such [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] actually existed; it treated the [[Exigent Circumstances and Hot Pursuit|exigency]] question as irrelevant because the cocaine and money were recovered from Kirk's person in a [[Search Incident to Arrest|search incident to arrest]]. That analysis inverted *[[Payton v. New York|Payton]]*: the lawfulness of the warrantless home entry — the predicate for the arrest and the search incident to it — turned precisely on whether [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] justified crossing the threshold. The Court reversed and [[Reading and Citing Cases#on-remand|remanded]] for the [[Exigent Circumstances and Hot Pursuit|exigency]] assessment, expressing no opinion on whether [[Exigent Circumstances and Hot Pursuit|exigency]] was in fact present or on the State's independent-source argument.

## Conclusion
A warrantless entry into a home to arrest requires probable cause plus [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] (or a warrant); because the state court never decided the [[Exigent Circumstances and Hot Pursuit|exigency]] question, its judgment violated *[[Payton v. New York|Payton]]* and was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Kirk* is a straightforward reaffirmation of [[Payton v. New York]]; it operates alongside [[Steagald v. United States]] (search warrant needed to arrest in a third party's home), [[Welsh v. Wisconsin]] ([[Exigent Circumstances and Hot Pursuit|exigency]] narrowly applied to minor offenses), and [[Kentucky v. King]] (police-created-[[Exigent Circumstances and Hot Pursuit|exigency]] limits).

## Appears on
- [[Arrest in the Home]] — *Progeny*

## Sources
- *Kirk v. Louisiana*, 536 U.S. 635 (2002) (per curiam) — https://www.courtlistener.com/opinion/121167/kirk-v-louisiana/ — pinpoints: 636, 638.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0cec432c664b5172", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "536 U.S. 635 (2002)", "court": "U.S. Supreme Court", "neutral_cite": "2002 U.S. LEXIS 4682", "official_citation_present": true, "parallel_cite": "122 S. Ct. 2458; 153 L. Ed. 2d 599; 2002 D.A.R. 7071", "title": "Kirk v. Louisiana", "year": "2002"}}
{"assertion_id": "1aa0e86479f6f823", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Absent exigent circumstances, police may not enter a home to make a warrantless arrest; a lawful home entry requires a warrant or probable cause plus exigent circumstances (reaffirming Payton).", "title": "Kirk v. Louisiana"}}
{"assertion_id": "46384f271240836f", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest in the Home"}, "payload": {"home": "Arrest in the Home", "role": "Progeny", "title": "Kirk v. Louisiana"}}
{"assertion_id": "035e4129bee47399", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2002-06-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Kirk v. Louisiana", "field_i_validity": "good_law", "scope_note": "Good law. Per curiam. Reaffirms Payton v. New York: absent exigent circumstances, police may not make a warrantless entry into a home to arrest; they need either a warrant or probable cause plus exigent circumstances.", "title": "Kirk v. Louisiana", "varies_by_point": "false"}}
{"assertion_id": "7eecbda434848931", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Kirk v. Louisiana"}}
```

### lake record — Kirk v. Louisiana

```json
{
  "schema_version": "s2.v1",
  "record_id": "Kirk v. Louisiana",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Kirk v. Louisiana",
    "case_name_short": "Kirk",
    "case_name_full": "Kirk v. Louisiana",
    "input_case_name": "Kirk v. Louisiana",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2002-06-24",
    "year": 2002,
    "docket": null,
    "cluster_id": 121167,
    "lead_opinion_id": 121167,
    "sibling_ids": [
      121167
    ],
    "absolute_url": "/opinion/121167/kirk-v-louisiana/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "536 U.S. 635",
      "volume": "536",
      "reporter": "U.S.",
      "page": "635",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "122 S. Ct. 2458",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "2458",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "153 L. Ed. 2d 599",
        "volume": "153",
        "reporter": "L. Ed. 2d",
        "page": "599",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 D.A.R. 7071",
        "volume": "2002",
        "reporter": "D.A.R.",
        "page": "7071",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2002 U.S. LEXIS 4682",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "4682",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "536 U.S. 635",
        "volume": "536",
        "reporter": "U.S.",
        "page": "635",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "122 S. Ct. 2458",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "2458",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "153 L. Ed. 2d 599",
        "volume": "153",
        "reporter": "L. Ed. 2d",
        "page": "599",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 U.S. LEXIS 4682",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "4682",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 D.A.R. 7071",
        "volume": "2002",
        "reporter": "D.A.R.",
        "page": "7071",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "536 U.S. 635",
    "official_selection": {
      "court_class": "scotus",
      "selected": "536 U.S. 635",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-636",
      "page": null,
      "quote": "--- # Kirk v. Louisiana *536 U.S. 635 (2002)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After an anonymous tip that drugs were being sold from Kirk's apartment, officers watched the apartment, saw what appeared to be several drug purchases, and stopped one buyer on the street nearby. Fearing that evidence would be destroyed, they entered Kirk's apartment without a warrant, arrested him, frisked him (finding a cocaine vial in his underwear), and observed contraband in plain view; only then did they obtain a search warrant. The Louisiana Court of Appeal upheld the entry and search without deciding whether exigent circumstances existed, reasoning that the officers had probable cause to arrest and that the incriminating evidence was found on Kirk's person incident to the arrest. ## Issue Whether police may make a warrantless entry into a home to arrest a suspect \u2014 and conduct a search incident to that arrest \u2014 without either a warrant or exigent circumstances, so long as they have probable cause to arrest. ## Rule No. The Fourth Amendment draws a firm line at the home's threshold: under *Payton v. New York*,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-638",
      "page": null,
      "quote": "police officers need either a warrant or probable cause plus exigent circumstances in order to make a lawful entry into a home. The Court of Appeal's ruling to the contrary, and consequent failure to assess whether exigent circumstances were present in this case, violated *Payton*.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2002-06-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Kirk v. Louisiana",
    "varies_by_point": false,
    "scope_note": "Good law. Per curiam. Reaffirms Payton v. New York: absent exigent circumstances, police may not make a warrantless entry into a home to arrest; they need either a warrant or probable cause plus exigent circumstances.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Arias",
          "cluster_id": 4600764,
          "cite": [
            "119 N.E.3d 257",
            "481 Mass. 604"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
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
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "NYIA GORE v. UNITED STATES",
          "cluster_id": 4248978,
          "cite": [
            "145 A.3d 540",
            "2016 D.C. App. LEXIS 313",
            "2016 WL 4411321"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Hogan v. City of Corpus Christi, Texas",
          "cluster_id": 1033766,
          "cite": [
            "722 F.3d 725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Fleming",
          "cluster_id": 2488640,
          "cite": [
            "76 So. 3d 417",
            "2011 La. LEXIS 3008",
            "2011 WL 6309435"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Forbes",
          "cluster_id": 5938198,
          "cite": [
            "71 A.D.3d 1519",
            "897 N.Y.S.2d 352"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gallagher v. City of Winlock Washington",
          "cluster_id": 8688333,
          "cite": [
            "287 F. App'x 568"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Martins",
          "cluster_id": 201656,
          "cite": [
            "413 F.3d 139",
            "2005 U.S. App. LEXIS 12704",
            "2005 WL 1502939"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Guy Christopher Brooks",
          "cluster_id": 786149,
          "cite": [
            "367 F.3d 1128",
            "2004 U.S. App. LEXIS 9349",
            "2004 WL 1066612"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Estrada v. State",
          "cluster_id": 1795405,
          "cite": [
            "116 S.W.3d 370",
            "2003 Tex. App. LEXIS 7427",
            "2003 WL 22023640"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kentucky v. King",
          "cluster_id": 216733,
          "cite": [
            "179 L. Ed. 2d 865",
            "131 S. Ct. 1849",
            "563 U.S. 452",
            "2011 U.S. LEXIS 3541"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cortez v. McCauley",
          "cluster_id": 167088,
          "cite": [
            "478 F.3d 1108",
            "2007 WL 503819"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Janet Feliciano v. City of Miami Beach",
          "cluster_id": 819741,
          "cite": [
            "707 F.3d 1244",
            "2013 WL 425445",
            "2013 U.S. App. LEXIS 2524"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Steelman",
          "cluster_id": 1891638,
          "cite": [
            "93 S.W.3d 102",
            "2002 Tex. Crim. App. LEXIS 206",
            "2002 WL 31398545"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cheryl D. Lyons v. City of Xenia, Christine Keith, Officer Matthew Foubert, Officer",
          "cluster_id": 791266,
          "cite": [
            "417 F.3d 565",
            "2005 U.S. App. LEXIS 16034",
            "2005 WL 1846994"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Coffin v. Stacy Brandau",
          "cluster_id": 3048939,
          "cite": [
            "642 F.3d 999",
            "2011 U.S. App. LEXIS 11353",
            "2011 WL 2162997"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Saleem Bashir v. Rockdale County, Georgia",
          "cluster_id": 77293,
          "cite": [
            "445 F.3d 1323",
            "2006 U.S. App. LEXIS 9311",
            "2006 WL 962608"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Clifton Myers A/K/A Samuel Jenkins, Clifton Myers",
          "cluster_id": 779561,
          "cite": [
            "308 F.3d 251",
            "2002 U.S. App. LEXIS 21264"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Loria v. Gorman",
          "cluster_id": 7108550,
          "cite": [
            "306 F.3d 1271"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Meeks",
          "cluster_id": 1057727,
          "cite": [
            "262 S.W.3d 710",
            "2008 Tenn. LEXIS 575",
            "2008 WL 4007429"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Burke v. Town of Walpole",
          "cluster_id": 201555,
          "cite": [
            "405 F.3d 66",
            "2005 U.S. App. LEXIS 7105",
            "2005 WL 949688"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin McClain George Brandt, III Jason Davis",
          "cluster_id": 793976,
          "cite": [
            "444 F.3d 556",
            "2006 U.S. App. LEXIS 32292"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Theodore E. Loria v. Charles Gorman, Individually and in His Capacity as a Police Officer for the City of Rochester, Robert Nitchman, Individually and in His Capacity as a Police Officer for the City of Rochester, City of Rochester, Mark Wiater, George Markert, Individually and in His Capacity as a Police Officer for the City of Rochester, Vasquez, Individually and in His Capacity as a Police Officer for the City of Rochester, Debra Stritzel, Individually and in Her Capacity as an Employee of the City of Rochester, Theodore E. Loria v. Dale Feor, Individually and in His Capacity as a Police Officer for the City of Rochester, City of Rochester",
          "cluster_id": 779429,
          "cite": [
            "306 F.3d 1271",
            "2002 U.S. App. LEXIS 20458"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robinson v. Com.",
          "cluster_id": 1058715,
          "cite": [
            "639 S.E.2d 217",
            "273 Va. 26",
            "2007 Va. LEXIS 14"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morse v. Cloutier",
          "cluster_id": 4421636,
          "cite": [
            "869 F.3d 16"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sandoval v. Las Vegas Metropolitan Police Department",
          "cluster_id": 2681571,
          "cite": [
            "756 F.3d 1154",
            "2014 WL 2936254",
            "2014 U.S. App. LEXIS 12395"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McBride",
          "cluster_id": 2483841,
          "cite": [
            "928 N.E.2d 1027",
            "14 N.Y.3d 440",
            "902 N.Y.S.2d 830"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Demetrius Pruitt",
          "cluster_id": 795278,
          "cite": [
            "458 F.3d 477",
            "2006 U.S. App. LEXIS 20555",
            "2006 WL 2320962"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bates v. Harvey",
          "cluster_id": 77969,
          "cite": [
            "518 F.3d 1233",
            "2008 U.S. App. LEXIS 4559",
            "2008 WL 565774"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(121167) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 128,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 10,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 128,
        "triage_read": 11,
        "triage_snippet_classified": 117
      },
      "lane2_top_cited": {
        "query": "cites:(121167)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MSZzPTI3MjMzMDUmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28121167%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(121167)",
        "reviewed": 6,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 6,
        "triage_read": 0,
        "triage_snippet_classified": 6
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(121167)",
    "indexed_citing_opinions": 164,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 121167,
        "count": 164,
        "count_source": "search"
      }
    ],
    "citation_count": 292,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/kirk-v-louisiana.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU3NTcmcz00NDczNzY2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28121167%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 121167,
        "cited_id": 110235,
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
    "date_created": "2026-07-05T10:11:46Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:12:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:12:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:16:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:12:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Kirk v. Louisiana

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b685-10">
  Per Curiam.
 </author>
<p id="b685-11">
  Police officers entered petitioner’s home, where they arrested and searched him. The officers had neither an arrest warrant nor a search warrant. Without deciding whether exigent circumstances had been present, the Louisiana Court of Appeal concluded that the warrantless entry, arrest, and search did not violate the Fourth Amendment of the Federal Constitution because there had been probable cause to arrest petitioner. 00-0190 (La. App. 11/15/00), <span class="citation" data-id="1704719"><a href="/opinion/1704719/state-v-kirk/" aria-description="Citation for case: State v. Kirk">773 So. 2d 259</a></span>. The court’s reasoning plainly violates our holding in
  <em>
   Payton
  </em>
<span citation-index="1" class="star-pagination" label="636"> 
   *636
   </span>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#590" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 590</a></span> (1980), that “[a]bsent exigent circumstances,” the “firm line at the entrance to the house ... may not reasonably be crossed without a warrant.” We thus grant the petition for a writ of certiorari and reverse the Court of Appeal’s conclusion that the officers’ actions were lawful, absent exigent circumstances.
  <a class="footnote" href="#fn*" id="fn*_ref">
   *
  </a>
</p>
<p id="b686-5">
  On an evening in March 1998, police officers observed petitioner’s apartment based on an anonymous citizen complaint that drug sales were occurring there. After witnessing what appeared to be several drug purchases and allowing the buyers to leave the scene, the officers stopped one of the buyers on the street outside petitioner’s residence. The officers later testified that “[b]ecause the stop took place within a block of the apartment, [they] feared that evidence would be destroyed and ordered that the apartment be entered.” 00-0190, at 2, <span class="citation" data-id="1704719"><a href="/opinion/1704719/state-v-kirk/#261" aria-description="Citation for case: State v. Kirk">773 So. 2d, at 261</a></span>. Thus, “[t]hey immediately knocked on the door of the apartment, arrested-the defendant, searched him thereto and discovered the cocaine and the money.”
  <em>
   Id.,
  </em>
  at 4, <span class="citation" data-id="1704719"><a href="/opinion/1704719/state-v-kirk/#263" aria-description="Citation for case: State v. Kirk">773 So. 2d, at 263</a></span>. Although the officers sought and obtained a search warrant while they detained petitioner in his home, they only obtained this warrant after they had entered his home, arrested him, frisked him, found a drug vial in his underwear, and observed contraband in plain view in the apartment.
 </p>
<p id="b686-6">
  Based on these events, petitioner was charged in a Louisiana court with possession of cocaine with intent to distribute. He filed a pretrial motion to suppress evidence obtained by the police as a result of their warrantless entry, arrest, and search. After holding a suppression hearing, the trial court denied this motion. Petitioner was convicted and sentenced to 15 years at hard labor.
 </p>
<p id="b686-7">
  On direct review to the Louisiana Court of Appeal, petitioner challenged the trial court's suppression ruling. He argued that the police were not justified in entering his home
  <span citation-index="1" class="star-pagination" label="637"> 
   *637
   </span>
  without a warrant absent exigent circumstances. The Court of Appeal acknowledged petitioner’s argument: “[Petitioner] makes a long argument that there were not exigent circumstances for entering the apartment without a warrant.”
  <em>
   Id.,
  </em>
  at 2, <span class="citation" data-id="1704719"><a href="/opinion/1704719/state-v-kirk/#261" aria-description="Citation for case: State v. Kirk">773 So. 2d, at 261</a></span>. The court, however, declined to decide whether exigent circumstances had been present, because “the evidence required to prove that the defendant possessed cocaine with the intent to distribute, namely the cocaine and the money, was not found in the apartment, but on his person.”
  <em>
   <span class="citation" data-id="1704719"><a href="/opinion/1704719/state-v-kirk/" aria-description="Citation for case: State v. Kirk">Ibid.</a></span>
  </em>
  The court concluded that because “[t]he officers had probable cause to arrest and properly searched the defendant incident thereto . . . [, t]he trial court properly denied the motion to suppress.”
  <em>
   Id.,
  </em>
  at 4, <span class="citation" data-id="1704719"><a href="/opinion/1704719/state-v-kirk/#263" aria-description="Citation for case: State v. Kirk">773 So. 2d, at 263</a></span>.
 </p>
<p id="b687-5">
  The Louisiana Supreme Court denied review by a vote of 4 to 3. In a written dissent, Chief Justice Calogero explained:
 </p>
<blockquote id="b687-6">
  “The Fourth Amendment to the United States constitution has drawn a firm line at the entrance to the home, and thus, the police need both probable cause to either arrest or search and exigent circumstances to justify a nonconsensual warrantless intrusion into private premises. . . . Here, the defendant was arrested inside an apartment, without a warrant, and the state has not demonstrated that exigent circumstances were present. Consequently, defendant’s arrest was unconstitutional, and his motion to suppress should have been granted.” App. to Pet. for Cert. 1-2.
 </blockquote>
<p id="b687-7">
  We agree with Chief Justice Calogero that the Court of Appeal clearly erred by concluding that petitioner’s arrest and the search “incident thereto,” 00-0190, at 4, <span class="citation" data-id="1704719"><a href="/opinion/1704719/state-v-kirk/#263" aria-description="Citation for case: State v. Kirk">773 So. 2d, at 263</a></span>, were constitutionally permissible. In
  <em>
   Payton,
  </em>
  we examined whether the Fourth Amendment was violated by a state statute that authorized officers to “enter a private residence without a warrant and with force, if necessary, to make a routine felony arrest.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#574" aria-description="Citation for case: Payton v. New York">445 U. S., at 574</a></span>. We deter
  <span citation-index="1" class="star-pagination" label="638"> 
   *638
   </span>
  mined that “the reasons for upholding warrantless arrests in a public place do not apply to warrantless invasions of the privacy of the home.”
  <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#576" aria-description="Citation for case: Payton v. New York"><em>
   Id.,
  </em>
  at 576</a></span>. We held that because “the Fourth Amendment has drawn a firm line at the entrance to the house ... [, a]bsent exigent circumstances, that threshold may not reasonably be crossed without a warrant.”
  <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#590" aria-description="Citation for case: Payton v. New York"><em>
   Id.,
  </em>
  at 590</a></span>. And we noted that an arrest warrant founded on probable cause, as well as a search warrant, would suffice for entry.
  <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#603" aria-description="Citation for case: Payton v. New York"><em>
   Id.,
  </em>
  at 603</a></span>.
 </p>
<p id="b688-5">
  Here, the police had neither an arrest warrant for petitioner, nor a search warrant for petitioner’s apartment, when they entered his home, arrested him, and searched him. The officers testified at the suppression hearing that the reason for their actions was a fear that evidence would be destroyed, but the Louisiana Court of Appeal did not determine that such exigent circumstances were present. Rather, the court, in respondent’s own words, determined “thát the defendant’s argument that there were no exigent circumstances to justify the warrantless entry of the apartment was irrelevant” to the constitutionality of the officers’ actions. Brief in Opposition 2-3. As
  <em>
   Payton
  </em>
  makes plain, police officers need either a warrant or probable cause plus exigent circumstances in order to make a lawful entry into a home. The Court of Appeal’s ruling to the contrary, and consequent failure to assess whether exigent circumstances were present in this case, violated
  <em>
   Payton.
  </em>
</p>
<p id="b688-6">
  Petitioner and respondent both dispute at length whether exigent circumstances were, in fact, present. We express no opinion on that question, nor on respondent’s argument that any Fourth Amendment violation was cured because the police had an “independent source” for the recovered evidence. Brief in Opposition 8. Rather, we reverse the Court of Appeal’s judgment that exigent circumstances were not required to justify the officers’ conduct, and remand for further proceedings not inconsistent with this opinion.
 </p>
<p id="b688-7">
<em>
   It is so ordered.
  </em>
</p>

<div class="footnotes"><div class="footnote" id="fn*" label="*">
<a class="footnote" href="#fn*_ref">
   *
  </a>
<p id="b686-8">
   We also grant petitioner's motion for leave to proceed
   <em>
    in forma pauperis.
   </em>
</p>
</div></div></opinion>
```

---

## GROUP: content/cases/Kisela v. Hughes.md  (`case`, 6 assertions)

### content_page

```
---
title: "Kisela v. Hughes"
type: case
citation: "584 U.S. 100 (2018)"
parallel_cite: "138 S. Ct. 1148; 200 L. Ed. 2d 449"
neutral_cite: 2018 U.S. LEXIS 2066
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2018
date_decided: 2018-04-02
docket: 17-467
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2018-04-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Kisela v. Hughes
  varies_by_point: false
  scope_note: "Good law (per curiam). Reaffirms and applies the Brosseau/Mullenix specificity rule: in excessive-force cases officers get qualified immunity unless existing precedent 'squarely governs' the specific facts. Sotomayor (joined by Ginsburg) dissented."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4482892/kisela-v-hughes/"
  cluster_id: 4482892
  opinion_id: 4260145
  identity_checked: true
homes:
  - page: "[[Use of Force]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Qualified Immunity]]"
    role: "Related (cross-doctrine)"
related: ["[[Graham v. Connor]]", "[[Tennessee v. Garner]]", "[[Mullenix v. Luna]]", "[[White v. Pauly]]", "[[City and County of San Francisco v. Sheehan]]", "[[Brosseau v. Haugen]]"]
aliases: []
tags: ["case", "use-of-force", "deadly-force", "qualified-immunity", "section-1983", "clearly-established-law", "mental-illness"]
holding: "An officer who shot a woman holding a large kitchen knife who had moved within striking distance of another woman and ignored commands to drop it was entitled to qualified immunity: clearly established law in excessive-force cases must be defined at a high level of specificity, and officers get immunity unless existing precedent 'squarely governs' the specific facts at issue."
lake:
  record_id: Kisela v. Hughes
  status: verified
  projected_at: 2026-07-06
---

# Kisela v. Hughes

*584 U.S. 100 (2018)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Tucson officer Andrew Kisela and two others responded to a 911 report of a woman hacking a tree with a kitchen knife and acting erratically. Within about a minute of arriving they saw Amy Hughes emerge from a house carrying a large knife and walk to within six feet of another woman, Sharon Chadwick. A chain-link fence separated the officers from the two women. The officers drew their guns and ordered Hughes at least twice to drop the knife; she appeared calm but did not comply. Kisela dropped to the ground and fired four shots through the fence, wounding Hughes (non-life-threatening). It later emerged the women were roommates and Chadwick said she never felt endangered. Hughes sued Kisela under § 1983 for excessive force.

## Issue
Whether Officer Kisela was entitled to [[Qualified Immunity|qualified immunity]] — i.e., whether his use of deadly force against Hughes violated clearly established law.

## Rule
The Court assumed without deciding that the shooting may have violated the Fourth Amendment and resolved the case on [[Qualified Immunity|qualified immunity]]. "Qualified immunity attaches when an official's conduct does not violate clearly established statutory or constitutional rights of which a reasonable person would have known." — 138 S. Ct. at 1152 (quoting *White v. Pauly*). ^pin-1152

Existing precedent "must have placed the statutory or constitutional question beyond debate," and the Court has "'repeatedly told courts — and the Ninth Circuit in particular — not to define clearly established law at a high level of generality.'" — *Id.*

Force law demands [[Particularity|particularity]]. "Use of excessive force is an area of the law 'in which the result depends very much on the facts of each case,' and thus police officers are entitled to qualified immunity unless existing precedent 'squarely governs' the specific facts at issue." — 138 S. Ct. at 1153 (quoting *Mullenix v. Luna*). ^pin-1153

The general rules of [[Tennessee v. Garner]] and [[Graham v. Connor]] "do not by themselves create clearly established law outside an 'obvious case.'" — *Id.*

## Application
On these facts the case was "far from an obvious case in which any competent officer would have known that shooting Hughes to protect Chadwick would violate the Fourth Amendment": Kisela had only seconds to assess the threat, faced a woman who had just been reported hacking a tree with a large knife, who had moved within a few feet of Chadwick, and who ignored at least two audible commands to drop the weapon. Nor did circuit precedent place the question beyond debate — the most analogous Ninth Circuit case (*Blanford v. Sacramento County*) favored Kisela, while the decisions the Court of Appeals relied on (*Deorle*, *Glenn*, *Harris v. Roderick*) were materially different, involving unarmed or compliant suspects. Because no clearly established law squarely governed the situation Kisela confronted, he was entitled to [[Qualified Immunity|qualified immunity]].

## Conclusion
Reversed. Kisela was entitled to [[Qualified Immunity|qualified immunity]] because clearly established law, defined at the proper level of specificity, did not put it beyond debate that his use of force was unconstitutional.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** ([[Common Legal Terms#per-curiam|per curiam]]; Sotomayor, J., joined by Ginsburg, J., dissenting).
- *Kisela* applies the specificity principle of [[Brosseau v. Haugen]] and [[Mullenix v. Luna]] and the "beyond debate" standard of [[White v. Pauly]] and [[City and County of San Francisco v. Sheehan]] to excessive-force [[Qualified Immunity|qualified immunity]]. It is frequently cited for the rule that officers get immunity "unless existing precedent 'squarely governs' the specific facts." No negative treatment.

## Appears on
- [[Use of Force]] — *Key — Progeny / Refinement*
- [[Section 1983 Liability and Qualified Immunity]] — *Related (cross-doctrine)*

## Sources
- *Kisela v. Hughes*, 584 U.S. 100 (2018) (per curiam) — https://www.courtlistener.com/opinion/4482892/kisela-v-hughes/ — pinpoints: 138 S. Ct. at 1152, 1153.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a4cf3e01791263c2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "584 U.S. 100 (2018)", "court": "U.S. Supreme Court", "neutral_cite": "2018 U.S. LEXIS 2066", "official_citation_present": true, "parallel_cite": "138 S. Ct. 1148; 200 L. Ed. 2d 449", "title": "Kisela v. Hughes", "year": "2018"}}
{"assertion_id": "2b052d72d6e976ef", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Related (cross-doctrine)", "title": "Kisela v. Hughes"}}
{"assertion_id": "a30787dcb0bb0284", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An officer who shot a woman holding a large kitchen knife who had moved within striking distance of another woman and ignored commands to drop it was entitled to qualified immunity: clearly established law in excessive-force cases must be defined at a high level of specificity, and officers get immunity unless existing precedent 'squarely governs' the specific facts at issue.", "title": "Kisela v. Hughes"}}
{"assertion_id": "ddf9f0d34a3de40e", "dimension": "support", "kind": "home_role", "locator": {"home": "Use of Force"}, "payload": {"home": "Use of Force", "role": "Key — Progeny / Refinement", "title": "Kisela v. Hughes"}}
{"assertion_id": "98335138846c6cd1", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Kisela v. Hughes"}}
{"assertion_id": "c3e3f0402c6ad223", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2018-04-02", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Kisela v. Hughes", "field_i_validity": "good_law", "scope_note": "Good law (per curiam). Reaffirms and applies the Brosseau/Mullenix specificity rule: in excessive-force cases officers get qualified immunity unless existing precedent 'squarely governs' the specific facts. Sotomayor (joined by Ginsburg) dissented.", "title": "Kisela v. Hughes", "varies_by_point": "false"}}
```

### lake record — Kisela v. Hughes

```json
{
  "schema_version": "s2.v1",
  "record_id": "Kisela v. Hughes",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Kisela v. Hughes",
    "case_name_short": "Kisela",
    "case_name_full": "Andrew KISELA v. Amy HUGHES.",
    "input_case_name": "Kisela v. Hughes",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2018-04-02",
    "year": 2018,
    "docket": "17-467",
    "cluster_id": 4482892,
    "lead_opinion_id": 4260145,
    "sibling_ids": [
      4260145
    ],
    "absolute_url": "/opinion/4482892/kisela-v-hughes/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "584 U.S. 100",
      "volume": "584",
      "reporter": "U.S.",
      "page": "100",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "138 S. Ct. 1148",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "1148",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "200 L. Ed. 2d 449",
        "volume": "200",
        "reporter": "L. Ed. 2d",
        "page": "449",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2018 U.S. LEXIS 2066",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "2066",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "584 U.S. 100",
        "volume": "584",
        "reporter": "U.S.",
        "page": "100",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "138 S. Ct. 1148",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "1148",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "200 L. Ed. 2d 449",
        "volume": "200",
        "reporter": "L. Ed. 2d",
        "page": "449",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2018 U.S. LEXIS 2066",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "2066",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "584 U.S. 100",
    "official_selection": {
      "court_class": "scotus",
      "selected": "584 U.S. 100",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1152",
      "page": null,
      "quote": "--- # Kisela v. Hughes *584 U.S. 100 (2018)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Tucson officer Andrew Kisela and two others responded to a 911 report of a woman hacking a tree with a kitchen knife and acting erratically. Within about a minute of arriving they saw Amy Hughes emerge from a house carrying a large knife and walk to within six feet of another woman, Sharon Chadwick. A chain-link fence separated the officers from the two women. The officers drew their guns and ordered Hughes at least twice to drop the knife; she appeared calm but did not comply. Kisela dropped to the ground and fired four shots through the fence, wounding Hughes (non-life-threatening). It later emerged the women were roommates and Chadwick said she never felt endangered. Hughes sued Kisela under \u00a7 1983 for excessive force. ## Issue Whether Officer Kisela was entitled to qualified immunity \u2014 i.e., whether his use of deadly force against Hughes violated clearly established law. ## Rule The Court assumed without deciding that the shooting may have violated the Fourth Amendment and resolved the case on qualified immunity.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1153",
      "page": null,
      "quote": "\u2014 *Id.* Force law demands particularity.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2018-04-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Kisela v. Hughes",
    "varies_by_point": false,
    "scope_note": "Good law (per curiam). Reaffirms and applies the Brosseau/Mullenix specificity rule: in excessive-force cases officers get qualified immunity unless existing precedent 'squarely governs' the specific facts. Sotomayor (joined by Ginsburg) dissented.",
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
        "journal_ref": "Kisela v. Hughes:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Heriberto Rodriguez v. County of Los Angeles",
          "cluster_id": 4502306,
          "cite": [
            "891 F.3d 776"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ana Sandoval v. County of San Diego",
          "cluster_id": 4847368,
          "cite": [
            "985 F.3d 657"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Frost v. New York City Police Department",
          "cluster_id": 4805103,
          "cite": [
            "980 F.3d 231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maurice Lewis v. City of Chicago",
          "cluster_id": 4583974,
          "cite": [
            "914 F.3d 472"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeffery Mays v. Ronald Sprinkle",
          "cluster_id": 4869132,
          "cite": [
            "992 F.3d 295"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Amy Corbitt v. Michael Vickers",
          "cluster_id": 4638184,
          "cite": [
            "929 F.3d 1304"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kirk Horshaw v. Mark Casper",
          "cluster_id": 4573724,
          "cite": [
            "910 F.3d 1027"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Vos v. City of Newport Beach",
          "cluster_id": 4506067,
          "cite": [
            "892 F.3d 1024"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morrow v. Meachum",
          "cluster_id": 8443910,
          "cite": [
            "917 F.3d 870"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony Martin v. Susan Duffy",
          "cluster_id": 4795803,
          "cite": [
            "977 F.3d 294"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Feminist Majority Foundation v. Richard Hurley",
          "cluster_id": 4574853,
          "cite": [
            "911 F.3d 674"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Naumovski v. Norris",
          "cluster_id": 4647449,
          "cite": [
            "934 F.3d 200"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jose Peroza-Benitez v. Darren Smith",
          "cluster_id": 4871933,
          "cite": [
            "994 F.3d 157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Raheem Jacobs v. Cumberland County",
          "cluster_id": 4906491,
          "cite": [
            "8 F.4th 187"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brittany Harris v. Kimberly Klare",
          "cluster_id": 4532638,
          "cite": [
            "902 F.3d 630"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jonathan Capp v. County of San Diego",
          "cluster_id": 4667181,
          "cite": [
            "940 F.3d 1046"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harmon v. City of Arlington",
          "cluster_id": 5292775,
          "cite": [
            "16 F.4th 1159"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James P. Crocker v. Deputy Sheriff Steven Eric Beatty",
          "cluster_id": 4875336,
          "cite": [
            "995 F.3d 1232"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torcivia v. Suffolk County, New York",
          "cluster_id": 5295971,
          "cite": [
            "17 F.4th 342"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gene Bell, Jr. v. City of Southfield, Mich.",
          "cluster_id": 6477591,
          "cite": [
            "37 F.4th 362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vega v. Semple",
          "cluster_id": 4764447,
          "cite": [
            "963 F.3d 259"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jerry Smith, Jr. v. Melvin Finkley",
          "cluster_id": 4970388,
          "cite": [
            "10 F.4th 725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sachin Gupta v. Chad Melloh",
          "cluster_id": 5303583,
          "cite": [
            "19 F.4th 990"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Corey Hughes v. Michael Rodriguez",
          "cluster_id": 6461702,
          "cite": [
            "31 F.4th 1211"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matthew King v. Hendricks County Commissioner",
          "cluster_id": 4740934,
          "cite": [
            "954 F.3d 981"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4260145) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjE3MDYyNDAwMDAwJnM9NDg2OTEzMiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%284260145%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(4260145)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDImcz02NDQ1OTcwJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%284260145%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(4260145)",
        "reviewed": 139,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 139,
        "triage_read": 1,
        "triage_snippet_classified": 138
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4260145)",
    "indexed_citing_opinions": 381,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4260145,
        "count": 381,
        "count_source": "search"
      }
    ],
    "citation_count": 1755,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/kisela-v-hughes.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyOTQ2NDEmcz0xMDM3NDUzMCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%284260145%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4260145,
        "cited_id": 110443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 112458,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 121169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 137736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 145738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 180078,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 217703,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 574389,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 610866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 746949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 775749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 790155,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 2620705,
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
    "date_created": "2026-07-05T10:16:31Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:16:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:16:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:19:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:16:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Kisela v. Hughes

```
                 Cite as: 584 U. S. ____ (2018)            1

                             Per Curiam

SUPREME COURT OF THE UNITED STATES
          ANDREW KISELA v. AMY HUGHES
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE NINTH CIRCUIT

               No. 17–467.    Decided April 2, 2018


  PER CURIAM.
  Petitioner Andrew Kisela, a police officer in Tucson,
Arizona, shot respondent Amy Hughes. Kisela and two
other officers had arrived on the scene after hearing a
police radio report that a woman was engaging in erratic
behavior with a knife. They had been there but a few
minutes, perhaps just a minute. When Kisela fired,
Hughes was holding a large kitchen knife, had taken steps
toward another woman standing nearby, and had refused
to drop the knife after at least two commands to do so.
The question is whether at the time of the shooting
Kisela’s actions violated clearly established law.
  The record, viewed in the light most favorable to
Hughes, shows the following. In May 2010, somebody in
Hughes’ neighborhood called 911 to report that a woman
was hacking a tree with a kitchen knife. Kisela and an-
other police officer, Alex Garcia, heard about the report
over the radio in their patrol car and responded. A few
minutes later the person who had called 911 flagged down
the officers; gave them a description of the woman with
the knife; and told them the woman had been acting errat-
ically. About the same time, a third police officer, Lindsay
Kunz, arrived on her bicycle.
  Garcia spotted a woman, later identified as Sharon
Chadwick, standing next to a car in the driveway of a
nearby house. A chain-link fence with a locked gate sepa-
rated Chadwick from the officers. The officers then saw
another woman, Hughes, emerge from the house carrying
a large knife at her side. Hughes matched the description
2                     KISELA v. HUGHES

                          Per Curiam

of the woman who had been seen hacking a tree. Hughes
walked toward Chadwick and stopped no more than six
feet from her.
   All three officers drew their guns. At least twice they
told Hughes to drop the knife. Viewing the record in the
light most favorable to Hughes, Chadwick said “take it
easy” to both Hughes and the officers. Hughes appeared
calm, but she did not acknowledge the officers’ presence or
drop the knife. The top bar of the chain-link fence blocked
Kisela’s line of fire, so he dropped to the ground and shot
Hughes four times through the fence. Then the officers
jumped the fence, handcuffed Hughes, and called para-
medics, who transported her to a hospital. There she was
treated for non-life-threatening injuries. Less than a
minute had transpired from the moment the officers saw
Chadwick to the moment Kisela fired shots.
   All three of the officers later said that at the time of the
shooting they subjectively believed Hughes to be a threat
to Chadwick. After the shooting, the officers discovered
that Chadwick and Hughes were roommates, that Hughes
had a history of mental illness, and that Hughes had been
upset with Chadwick over a $20 debt. In an affidavit
produced during discovery, Chadwick said that a few
minutes before the shooting her boyfriend had told her
Hughes was threatening to kill Chadwick’s dog, named
Bunny. Chadwick “came home to find” Hughes “somewhat
distressed,” and Hughes was in the house holding Bunny
“in one hand and a kitchen knife in the other.” Hughes
asked Chadwick if she “wanted [her] to use the knife on
the dog.” The officers knew none of this, though. Chad-
wick went outside to get $20 from her car, which is when
the officers first saw her. In her affidavit Chadwick said
that she did not feel endangered at any time. Ibid. Based
on her experience as Hughes’ roommate, Chadwick stated
that Hughes “occasionally has episodes in which she acts
inappropriately,” but “she is only seeking attention.” 2
                  Cite as: 584 U. S. ____ (2018)             3

                           Per Curiam

Record 108.
   Hughes sued Kisela under Rev. Stat. §1979, 42 U. S. C.
§1983, alleging that Kisela had used excessive force in
violation of the Fourth Amendment. The District Court
granted summary judgment to Kisela, but the Court of
Appeals for the Ninth Circuit reversed. 862 F. 3d 775
(2016).
   The Court of Appeals first held that the record, viewed
in the light most favorable to Hughes, was sufficient to
demonstrate that Kisela violated the Fourth Amendment.
See id., at 782. The court next held that the violation was
clearly established because, in its view, the constitutional
violation was obvious and because of Circuit precedent
that the court perceived to be analogous. Id., at 785.
Kisela filed a petition for rehearing en banc. Over the
dissent of seven judges, the Court of Appeals denied it.
Kisela then filed a petition for certiorari in this Court.
That petition is now granted.
   In one of the first cases on this general subject, Tennes-
see v. Garner, 471 U. S. 1 (1985), the Court addressed the
constitutionality of the police using force that can be deadly.
There, the Court held that “[w]here the officer has proba-
ble cause to believe that the suspect poses a threat of
serious physical harm, either to the officer or to others, it
is not constitutionally unreasonable to prevent escape by
using deadly force.” Id., at 11.
   In Graham v. Connor, 490 U. S. 386, 396 (1989), the
Court held that the question whether an officer has used
excessive force “requires careful attention to the facts and
circumstances of each particular case, including the sever-
ity of the crime at issue, whether the suspect poses an
immediate threat to the safety of the officers or others,
and whether he is actively resisting arrest or attempting
to evade arrest by flight.” “The ‘reasonableness’ of a par-
ticular use of force must be judged from the perspective of
a reasonable officer on the scene, rather than with the
4                    KISELA v. HUGHES

                         Per Curiam

20/20 vision of hindsight.” Ibid. And “[t]he calculus of
reasonableness must embody allowance for the fact that
police officers are often forced to make split-second judg-
ments—in circumstances that are tense, uncertain, and
rapidly evolving—about the amount of force that is neces-
sary in a particular situation.” Id., at 396–397.
    Here, the Court need not, and does not, decide whether
Kisela violated the Fourth Amendment when he used
deadly force against Hughes. For even assuming a Fourth
Amendment violation occurred—a proposition that is not
at all evident—on these facts Kisela was at least entitled
to qualified immunity.
    “Qualified immunity attaches when an official’s conduct
does not violate clearly established statutory or constitu-
tional rights of which a reasonable person would have
known.” White v. Pauly, 580 U. S. ___, ___ (2017) (per
curiam) (slip op., at 6) (alterations and internal quotation
marks omitted). “Because the focus is on whether the
officer had fair notice that her conduct was unlawful,
reasonableness is judged against the backdrop of the law
at the time of the conduct.” Brosseau v. Haugen, 543 U. S.
194, 198 (2004) (per curiam).
    Although “this Court’s caselaw does not require a case
directly on point for a right to be clearly established,
existing precedent must have placed the statutory or
constitutional question beyond debate.” White, 580 U. S.,
at ___ (slip op., at 6) (internal quotation marks omitted).
“In other words, immunity protects all but the plainly
incompetent or those who knowingly violate the law.”
Ibid. (internal quotation marks omitted). This Court has
“ ‘repeatedly told courts—and the Ninth Circuit in particu-
lar—not to define clearly established law at a high level of
generality.’ ”   City and County of San Francisco v.
Sheehan, 575 U. S. ___, ___ (2015) (slip op., at 13) (quoting
Ashcroft v. al-Kidd, 563 U. S. 731, 742 (2011)); see also
Brosseau, supra, at 198–199.
                  Cite as: 584 U. S. ____ (2018)             5

                           Per Curiam

   “[S]pecificity is especially important in the Fourth
Amendment context, where the Court has recognized that
it is sometimes difficult for an officer to determine how the
relevant legal doctrine, here excessive force, will apply to
the factual situation the officer confronts.” Mullenix v.
Luna, 577 U. S. ___, ___ (2015) (per curiam) (slip op., at 5)
(internal quotation marks omitted). Use of excessive force
is an area of the law “in which the result depends very
much on the facts of each case,” and thus police officers
are entitled to qualified immunity unless existing prece-
dent “squarely governs” the specific facts at issue. Id., at
___ (slip op., at 6) (internal quotation marks omitted and
emphasis deleted). Precedent involving similar facts can
help move a case beyond the otherwise “hazy border be-
tween excessive and acceptable force” and thereby provide
an officer notice that a specific use of force is unlaw-
ful. Id., at ___ (slip op., at 12) (internal quotation marks
omitted).
   “Of course, general statements of the law are not inher-
ently incapable of giving fair and clear warning to offic-
ers.” White, 580 U. S., at ___ (slip op., at 7) (internal
quotation marks omitted). But the general rules set forth
in “Garner and Graham do not by themselves create clearly
established law outside an ‘obvious case.’ ” Ibid. Where
constitutional guidelines seem inapplicable or too remote,
it does not suffice for a court simply to state that an officer
may not use unreasonable and excessive force, deny quali-
fied immunity, and then remit the case for a trial on the
question of reasonableness. An officer “cannot be said to
have violated a clearly established right unless the right’s
contours were sufficiently definite that any reasonable
official in the defendant’s shoes would have understood
that he was violating it.” Plumhoff v. Rickard, 572 U. S.
___, ___ (2014) (slip op., at 12). That is a necessary part of
the qualified-immunity standard, and it is a part of the
standard that the Court of Appeals here failed to imple-
6                    KISELA v. HUGHES

                         Per Curiam

ment in a correct way.
   Kisela says he shot Hughes because, although the offic-
ers themselves were in no apparent danger, he believed
she was a threat to Chadwick. Kisela had mere seconds to
assess the potential danger to Chadwick. He was con-
fronted with a woman who had just been seen hacking a
tree with a large kitchen knife and whose behavior was
erratic enough to cause a concerned bystander to call 911
and then flag down Kisela and Garcia. Kisela was sepa-
rated from Hughes and Chadwick by a chain-link fence;
Hughes had moved to within a few feet of Chadwick; and
she failed to acknowledge at least two commands to drop
the knife. Those commands were loud enough that Chad-
wick, who was standing next to Hughes, heard them. This
is far from an obvious case in which any competent officer
would have known that shooting Hughes to protect Chad-
wick would violate the Fourth Amendment.
   The Court of Appeals made additional errors in conclud-
ing that its own precedent clearly established that Kisela
used excessive force. To begin with, “even if a controlling
circuit precedent could constitute clearly established law
in these circumstances, it does not do so here.” Sheehan,
supra, at ___ (slip op., at 13). In fact, the most analogous
Circuit precedent favors Kisela. See Blanford v. Sacra-
mento County, 406 F. 3d 1110 (CA9 2005). In Blanford,
the police responded to a report that a man was walking
through a residential neighborhood carrying a sword and
acting in an erratic manner. Id., at 1112. There, as here,
the police shot the man after he refused their commands
to drop his weapon (there, as here, the man might not
have heard the commands). Id., at 1113. There, as here,
the police believed (perhaps mistakenly), that the man
posed an immediate threat to others. Ibid. There, the
Court of Appeals determined that the use of deadly force
did not violate the Fourth Amendment. Id., at 1119.
Based on that decision, a reasonable officer could have
                 Cite as: 584 U. S. ____ (2018)            7

                          Per Curiam

believed the same thing was true in the instant case.
  In contrast, not one of the decisions relied on by the
Court of Appeals—Deorle v. Rutherford, 272 F. 3d 1272
(CA9 2001), Glenn v. Washington County, 673 F. 3d 864
(CA9 2011), and Harris v. Roderick, 126 F. 3d 1189 (CA9
1997)—supports denying Kisela qualified immunity. As
for Deorle, this Court has already instructed the Court of
Appeals not to read its decision in that case too broadly in
deciding whether a new set of facts is governed by clearly
established law. Sheehan, 572 U. S., at ___–___ (slip op.,
at 13–14). Deorle involved a police officer who shot an
unarmed man in the face, without warning, even though
the officer had a clear line of retreat; there were no by-
standers nearby; the man had been “physically compliant
and generally followed all the officers’ instructions”; and
he had been under police observation for roughly 40
minutes. 272 F. 3d, at 1276, 1281–1282. In this case,
by contrast, Hughes was armed with a large knife; was
within striking distance of Chadwick; ignored the officers’
orders to drop the weapon; and the situation unfolded in
less than a minute. “Whatever the merits of the decision
in Deorle, the differences between that case and the case
before us leap from the page.” Sheehan, supra, at ___ (slip
op., at 14).
  Glenn, which the panel described as “[t]he most analo-
gous Ninth Circuit case,” 862 F. 3d, at 783, was decided
after the shooting at issue here. Thus, Glenn “could not
have given fair notice to [Kisela]” because a reasonable
officer is not required to foresee judicial decisions that do
not yet exist in instances where the requirements of the
Fourth Amendment are far from obvious. Brosseau, 543
U. S., at 200, n. 4. Glenn was therefore “of no use in the
clearly established inquiry.” Brosseau, supra, at 200, n. 4.
Other judges brought this mistaken or misleading citation
to the panel’s attention while Kisela’s petition for rehear-
ing en banc was pending before the Court of Appeals. 862
8                     KISELA v. HUGHES

                          Per Curiam

F.3d, at 795, n. 2 (Ikuta, J., dissenting from denial of
rehearing en banc). The panel then amended its opinion,
but nevertheless still attempted to “rely on Glenn as illus-
trative, not as indicative of the clearly established law in
2010.” Id., at 784, n. 2 (majority opinion). The panel
failed to explain the difference between “illustrative” and
“indicative” precedent, and none is apparent.
   The amended opinion also asserted, for the first time
and without explanation, that the Court of Appeals’ deci-
sion in Harris clearly established that the shooting here
was unconstitutional. Id., at 785. The new mention of
Harris replaced a reference in the panel’s first opinion to
Glenn—the case that postdated the shooting at issue here.
Compare 841 F. 3d 1081, 1090 (CA9 2016) (“As indicated
by Glenn and Deorle, . . . that right was clearly estab-
lished”), with 862 F. 3d, at 785 (“As indicated by Deorle
and Harris, . . . that right was clearly established”).
   The panel’s reliance on Harris “does not pass the
straight-face test.” 862 F. 3d, at 797 (opinion of Ikuta, J.).
In Harris, the Court of Appeals determined that an FBI
sniper, who was positioned safely on a hilltop, used exces-
sive force when he shot a man in the back while the man
was retreating to a cabin during what has been referred to
as the Ruby Ridge standoff. 126 F. 3d, at 1202–1203.
Suffice it to say, a reasonable police officer could miss the
connection between the situation confronting the sniper at
Ruby Ridge and the situation confronting Kisela in
Hughes’ front yard.
   For these reasons, the petition for certiorari is granted;
the judgment of the Court of Appeals is reversed; and the
case is remanded for further proceedings consistent with
this opinion.
                                              It is so ordered.
                 Cite as: 584 U. S. ____ (2018)           1

                  SOTOMAYOR, J., dissenting

SUPREME COURT OF THE UNITED STATES
          ANDREW KISELA v. AMY HUGHES
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE NINTH CIRCUIT

              No. 17–467.   Decided April 2, 2018


   JUSTICE SOTOMAYOR, with whom JUSTICE GINSBURG
joins, dissenting.
   Officer Andrew Kisela shot Amy Hughes while she was
speaking with her roommate, Sharon Chadwick, outside of
their home. The record, properly construed at this stage,
shows that at the time of the shooting: Hughes stood
stationary about six feet away from Chadwick, appeared
“composed and content,” Appellant’s Excerpts of Record
109 (Record), and held a kitchen knife down at her side
with the blade facing away from Chadwick. Hughes was
nowhere near the officers, had committed no illegal act,
was suspected of no crime, and did not raise the knife in
the direction of Chadwick or anyone else. Faced with
these facts, the two other responding officers held their
fire, and one testified that he “wanted to continue trying
verbal command[s] and see if that would work.” Id., at
120. But not Kisela. He thought it necessary to use deadly
force, and so, without giving a warning that he would
open fire, he shot Hughes four times, leaving her seriously
injured.
   If this account of Kisela’s conduct sounds unreasonable,
that is because it was. And yet, the Court today insulates
that conduct from liability under the doctrine of qualified
immunity, holding that Kisela violated no “clearly estab­
lished” law. See ante, at 5–6. I disagree. Viewing the
facts in the light most favorable to Hughes, as the Court
must at summary judgment, a jury could find that Kisela
violated Hughes’ clearly established Fourth Amendment
rights by needlessly resorting to lethal force. In holding
2                     KISELA v. HUGHES

                    SOTOMAYOR, J., dissenting

otherwise, the Court misapprehends the facts and misap­
plies the law, effectively treating qualified immunity as an
absolute shield. I therefore respectfully dissent.
                               I
   This case arrives at our doorstep on summary judgment,
so we must “view the evidence . . . in the light most favor­
able to” Hughes, the nonmovant, “with respect to the
central facts of this case.” Tolan v. Cotton, 572 U. S. ___,
___ (2014) (per curiam) (slip op., at 8). The majority pur­
ports to honor this well-settled principle, but its efforts fall
short. Although the majority sets forth most of the rele­
vant events that transpired, it conspicuously omits several
critical facts and draws premature inferences that bear on
the qualified-immunity inquiry. Those errors are fatal to
its analysis, because properly construing all of the facts in
the light most favorable to Hughes, and drawing all infer­
ences in her favor, a jury could find that the following
events occurred on the day of Hughes’ encounter with the
Tucson police.
   On May 21, 2010, Kisela and Officer-in-Training Alex
Garcia received a “ ‘check welfare’ ” call about a woman
chopping away at a tree with a knife. 862 F. 3d 775, 778
(CA9 2016). They responded to the scene, where they
were informed by the person who had placed the call (not
Chadwick) that the woman with the knife had been acting
“erratically.” Ibid. A third officer, Lindsay Kunz, later
joined the scene. The officers observed Hughes, who
matched the description given to the officers of the woman
alleged to have been cutting the tree, emerge from a house
with a kitchen knife in her hand. Hughes exited the front
door and approached Chadwick, who was standing outside
in the driveway.
   Hughes then stopped about six feet from Chadwick,
holding the kitchen knife down at her side with the blade
pointed away from Chadwick. Hughes and Chadwick
                 Cite as: 584 U. S. ____ (2018)            3

                   SOTOMAYOR, J., dissenting

conversed with one another; Hughes appeared “composed
and content,” Record 109, and did not look angry. See 862
F. 3d, at 778. At no point during this exchange did
Hughes raise the kitchen knife or verbally threaten to
harm Chadwick or the officers. Chadwick later averred
that, during the incident, she was never in fear of Hughes
and “was not the least bit threatened by the fact that
[Hughes] had a knife in her hand” and that Hughes “never
acted in a threatening manner.” Record 110–111. The
officers did not observe Hughes commit any crime, nor was
Hughes suspected of committing one. See 862 F. 3d, at
780.
   Nevertheless, the officers hastily drew their guns and
ordered Hughes to drop the knife. The officers gave that
order twice, but the commands came “in quick succession.”
Id., at 778. The evidence in the record suggests that
Hughes may not have heard or understood the officers’
commands and may not have been aware of the officers’
presence at all. Record 109–110, 195, 323–324 (Officer
Kunz’s testimony that “it seemed as though [Hughes]
didn’t even know we were there,” and “[i]t was like she
didn’t hear us almost”); id., at 304 (Officer Garcia’s testi­
mony that Hughes acted “almost as if we weren’t there”).
Although the officers were in uniform, they never verbally
identified themselves as law enforcement officers.
   Kisela did not wait for Hughes to register, much less
respond to, the officers’ rushed commands. Instead, Kisela
immediately and unilaterally escalated the situation.
Without giving any advance warning that he would shoot,
and without attempting less dangerous methods to deesca­
late the situation, he dropped to the ground and shot four
times at Hughes (who was stationary) through a chain-
link fence. After being shot, Hughes fell to the ground,
screaming and bleeding from her wounds. She looked at
the officers and asked, “ ‘Why’d you shoot me?’ ” Id., at
308. Hughes was immediately transported to the hospital,
4                     KISELA v. HUGHES

                    SOTOMAYOR, J., dissenting

where she required treatment for her injuries. Kisela
alone resorted to deadly force in this case. Confronted
with the same circumstances as Kisela, neither of his
fellow officers took that drastic measure.
                              II
   Police officers are not entitled to qualified immunity if
“(1) they violated a federal statutory or constitutional
right, and (2) the unlawfulness of their conduct was ‘clearly
established at the time.’ ” District of Columbia v. Wesby,
583 U. S. ___, ___ (2018) (slip op., at 13) (quoting Reichle v.
Howards, 566 U. S. 658, 664 (2012)). Faithfully applying
that well-settled standard, the Ninth Circuit held that a
jury could find that Kisela violated Hughes’ clearly estab­
lished Fourth Amendment rights. That conclusion was
correct.
                               A
   I begin with the first step of the qualified-immunity
inquiry: whether there was a violation of a constitutional
right. Hughes alleges that Kisela violated her Fourth
Amendment rights by deploying excessive force against
her. In assessing such a claim, courts must ask “whether
the officers’ actions are ‘objectively reasonable’ in light of
the facts and circumstances confronting them.” Graham
v. Connor, 490 U. S. 386, 397 (1989). That inquiry “re­
quires careful attention to the facts and circumstances of
each particular case, including the severity of the crime at
issue, whether the suspect poses an immediate threat to
the safety of the officers or others, and whether he is
actively resisting arrest or attempting to evade arrest by
flight.” Id., at 396; see also Tennessee v. Garner, 471 U. S.
1, 11 (1985). All of those factors (and others) support the
Ninth Circuit’s conclusion that a jury could find that
Kisela’s use of deadly force was objectively unreasonable.
862 F. 3d, at 779–782. Indeed, the panel’s resolution of
                 Cite as: 584 U. S. ____ (2018)           5

                   SOTOMAYOR, J., dissenting

this question was so convincing that not a single judge on
the Ninth Circuit, including the seven who dissented from
denial of rehearing en banc, expressly disputed that con­
clusion. See id., at 791–799 (opinion of Ikuta, J.). Neither
does the majority here, which simply assumes without
deciding that “a Fourth Amendment violation occurred.”
Ante, at 4.
   First, Hughes committed no crime and was not suspected
of committing a crime. The officers were responding to a
“check welfare” call, which reported no criminal activity,
and the officers did not observe any illegal activity while
at the scene. The mere fact that Hughes held a kitchen
knife down at her side with the blade pointed away from
Chadwick hardly elevates the situation to one that justi­
fies deadly force.
   Second, a jury could reasonably conclude that Hughes
presented no immediate or objective threat to Chadwick or
the other officers. It is true that Kisela had received a
report that a woman matching Hughes’ description had
been acting erratically. But the police officers themselves
never witnessed any erratic conduct. Instead, when
viewed in the light most favorable to Hughes, the record
evidence of what the police encountered paints a calmer
picture. It shows that Hughes was several feet from
Chadwick and even farther from the officers, she never
made any aggressive or threatening movements, and she
appeared “composed and content” during the brief
encounter.
   Third, Hughes did not resist or evade arrest. Based on
this record, there is significant doubt as to whether she
was aware of the officers’ presence at all, and evidence
suggests that Hughes did not hear the officers’ swift com­
mands to drop the knife.
   Finally, the record suggests that Kisela could have, but
failed to, use less intrusive means before deploying deadly
force. 862 F. 3d, at 781. For instance, Hughes submitted
6                    KISELA v. HUGHES

                   SOTOMAYOR, J., dissenting

expert testimony concluding that Kisela should have used
his Taser and that shooting his gun through the fence was
dangerous because a bullet could have fragmented against
the fence and hit Chadwick or his fellow officers. Ibid.; see
also Bryan v. MacPherson, 630 F. 3d 805, 831 (CA9 2010)
(noting that “police are required to consider what other
tactics if any were available to effect the arrest” and
whether there are “clear, reasonable, and less intrusive
alternatives” (internal quotation marks and alteration
omitted)). Consistent with that assessment, the other two
officers on the scene declined to fire at Hughes, and one of
them explained that he was inclined to use “some of the
lesser means” than shooting, including verbal commands,
because he believed there was time “[t]o try to talk
[Hughes] down.” Record 120–121. That two officers on
the scene, presented with the same circumstances as
Kisela, did not use deadly force reveals just how unneces­
sary and unreasonable it was for Kisela to fire four shots
at Hughes. See Plumhoff v. Rickard, 572 U. S. ___, ___
(2014) (slip op., at 8) (“We analyze [the objective reason-
ableness] question from the perspective of a reasonable
officer on the scene” (internal quotation marks omitted)).
  Taken together, the foregoing facts would permit a jury
to conclude that Kisela acted outside the bounds of the
Fourth Amendment by shooting Hughes four times.
                               B
  Rather than defend the reasonableness of Kisela’s con­
duct, the majority sidesteps the inquiry altogether and
focuses instead on the “clearly established” prong of the
qualified-immunity analysis. Ante, at 4. To be “ ‘clearly
established’ . . . [t]he contours of the right must be suffi­
ciently clear that a reasonable official would understand
that what he is doing violates that right.” Anderson v.
Creighton, 483 U. S. 635, 640 (1987). That standard is not
nearly as onerous as the majority makes it out to be. As
                  Cite as: 584 U. S. ____ (2018)             7

                    SOTOMAYOR, J., dissenting

even the majority must acknowledge, ante, at 4, this Court
has long rejected the notion that “an official action is
protected by qualified immunity unless the very action in
question has previously been held unlawful,” Anderson,
483 U. S., at 640. “[O]fficials can still be on notice that
their conduct violates established law even in novel factual
circumstances.” Hope v. Pelzer, 536 U. S. 730, 741 (2002).
At its core, then, the “clearly established” inquiry boils
down to whether Kisela had “fair notice” that he acted
unconstitutionally. See ibid.; Brosseau v. Haugen, 543
U. S. 194, 198 (2004) (per curiam) (“[T]he focus” of quali­
fied immunity “is on whether the officer had fair notice
that her conduct was unlawful”).
   The answer to that question is yes. This Court’s prece­
dents make clear that a police officer may only deploy
deadly force against an individual if the officer “has prob­
able cause to believe that the [person] poses a threat of
serious physical harm, either to the officer or to others.”
Garner, 471 U. S., at 11; see also Graham, 490 U. S., at
397. It is equally well established that any use of lethal
force must be justified by some legitimate governmental
interest. See Scott v. Harris, 550 U. S. 372, 383 (2007);
Mullenix v. Luna, 577 U. S. ___, ___–___ (2015)
(SOTOMAYOR, J., dissenting) (slip op., at 2–3). Consistent
with those clearly established principles, and contrary to
the majority’s conclusion, Ninth Circuit precedent predat­
ing these events further confirms that Kisela’s conduct
was clearly unreasonable. See Brosseau, 543 U. S., at 199
(“[A] body of relevant case law” may “ ‘clearly establish’ ”
the violation of a constitutional right); Ashcroft v. al-Kidd,
563 U. S. 731, 746 (2011) (KENNEDY, J., concurring)
(“[Q]ualified immunity is lost when plaintiffs point either
to ‘cases of controlling authority in their jurisdiction at the
time of the incident’ or to ‘a consensus of cases of persua­
sive authority such that a reasonable officer could not
have believed that his actions were lawful’ ” (quoting
8                     KISELA v. HUGHES

                    SOTOMAYOR, J., dissenting

Wilson v. Layne, 526 U. S. 603, 617 (1999))). Because
Kisela plainly lacked any legitimate interest justifying the
use of deadly force against a woman who posed no objec­
tive threat of harm to officers or others, had committed no
crime, and appeared calm and collected during the police
encounter, he was not entitled to qualified immunity.
   The Ninth Circuit’s opinion in Deorle v. Rutherford, 272
F. 3d 1272 (2001) proves the point. In that case, the police
encountered a man who had reportedly been acting “errat­
ically.” Id., at 1276. The man was “verbally abusive,”
shouted “ ‘kill me’ ” at the officers, screamed that he would
“ ‘kick [the] ass’ ” of one of the officers, and “brandish[ed] a
hatchet at a police officer,” ultimately throwing it “into a
clump of trees when told to put it down.” Id., at 1276–
1277. The officers also observed the man carrying an
unloaded crossbow in one hand and what appeared to be
“a can or a bottle of lighter fluid in the other.” Id., at
1277. The man discarded the crossbow when instructed to
do so by the police and then steadily walked toward one of
the officers. Ibid. In response, that officer, without giving
a warning, shot the man in the face with beanbag rounds.
Id., at 1278. The man suffered serious injuries, including
multiple fractures to his cranium and the loss of his left
eye. Ibid.
   The Ninth Circuit denied qualified immunity to the
officer, concluding that his use of force was objectively
unreasonable under clearly established law. Id., at 1285–
1286. The court held, “Every police officer should know
that it is objectively unreasonable to shoot . . . an unarmed
man who: has committed no serious offense, is mentally or
emotionally disturbed, has been given no warning of the
imminent use of such a significant degree of force, poses
no risk of flight, and presents no objectively reasonable
threat to the safety of the officer or other individuals.” Id.,
at 1285.
   The same holds true here. Like the man in Deorle,
                 Cite as: 584 U. S. ____ (2018)           9

                   SOTOMAYOR, J., dissenting

Hughes committed no serious crime, had been given no
warning of the imminent use of force, posed no risk of
flight, and presented no objectively reasonable threat to
the safety of officers or others. In fact, Hughes presented
even less of a danger than the man in Deorle, for, unlike
him, she did not threaten to “kick [their] ass,” did not
appear agitated, and did not raise her kitchen knife or
make any aggressive gestures toward the police or Chad­
wick. If the police officers acted unreasonably in shooting
the agitated, screaming man in Deorle with beanbag bul­
lets, a fortiori Kisela acted unreasonably in shooting the
calm-looking, stationary Hughes with real bullets. In my
view, Deorle and the precedent it cites place the unlawful­
ness of Kisela’s conduct “ ‘beyond debate.’ ” Wesby, 583
U. S., at ___ (slip op., at 15).
   The majority strains mightily to distinguish Deorle, to
no avail. It asserts, for instance, that, unlike the man in
Deorle, Hughes was “armed with a large knife.” Ante, at 7.
But that is not a fair characterization of the record, par­
ticularly at this procedural juncture. Hughes was not
“armed” with a knife. She was holding “a kitchen knife—
an everyday household item which can be used as a
weapon but ordinarily is a tool for safe, benign purposes”—
down at her side with the blade pointed away from Chad­
wick. 862 F. 3d, at 788 (Berzon, J., concurring in denial of
rehearing en banc). Hughes also spoke calmly with
Chadwick during the events at issue, did not raise the
knife, and made no other aggressive movements, under­
mining any suggestion that she was a threat to Chadwick
or anyone else. Similarly, the majority asserts that
Hughes was “within striking distance” of Chadwick, ante,
at 7, but that stretches the facts and contravenes this
Court’s repeated admonition that inferences must be
drawn in the exact opposite direction, i.e., in favor of
Hughes. See Tolan, 572 U. S., at ___ (slip op., at 8). The
facts, properly viewed, show that, when she was shot,
10                   KISELA v. HUGHES

                   SOTOMAYOR, J., dissenting

Hughes had stopped and stood still about six feet away
from Chadwick. Whether Hughes could “strik[e]” Chad­
wick from that particular distance, even though the kitchen
knife was held down at her side, is an inference that
should be drawn by the jury, not this Court.
   The majority next posits that Hughes, unlike the man in
Deorle, “ignored the officers’ orders to drop the” kitchen
knife. Ante, at 7. Yet again, the majority here draws
inferences in favor of Kisela, instead of Hughes. The
available evidence would allow a reasonable jury to find
that Hughes did not hear or register the officers’ swift
commands and that Kisela, like his fellow officers on the
scene, should have realized that as well. See supra, at 3–
4. Accordingly, at least at the summary-judgment stage,
the Court is mistaken in distinguishing Deorle based on
Hughes’ ostensible disobedience to the officers’ directives.
   The majority also implies that Deorle is distinguishable
because the police in that case observed the man over a
40-minute period, whereas the situation here unfolded in
less than a minute. Ante, at 7. But that fact favors
Hughes, not Kisela. The only reason this case unfolded in
such an abrupt timeframe is because Kisela, unlike his
fellow officer, showed no interest in trying to talk further
to Hughes or use a “lesser means” of force. See Record
120–121, 304.
   Finally, the majority passingly notes that “this Court
has already instructed the Court of Appeals not to read
[Deorle] too broadly.” Ante, at 7 (citing City and County of
San Francisco v. Sheehan, 575 U. S. ___, ___–___ (2015)
(slip op., at 13–14)). But the Court in Sheehan concluded
that Deorle was plainly distinguishable because, unlike in
Deorle, the officers there confronted a woman who “was
dangerous, recalcitrant, law-breaking, and out of sight.”
575 U. S., at ___ (slip op., at 14). As explained above,
however, Hughes was none of those things: She did not
threaten or endanger the officers or Chadwick, she did not
                      Cite as: 584 U. S. ____ (2018)                    11

                       SOTOMAYOR, J., dissenting

break any laws, and she was visible to the officers on the
scene. See supra, at 2–4. Thus, there simply is no basis
for the Court’s assertion that “ ‘the differences between
[Deorle] and the case before us leap from the page.’ ” Ante,
at 7 (quoting Sheehan, 575 U. S., at ___ (slip op., at 14)).
   Deorle, moreover, is not the only case that provided fair
notice to Kisela that shooting Hughes under these circum­
stances was unreasonable. For instance, the Ninth Circuit
has held that the use of deadly force against an individual
holding a semiautomatic rifle was unconstitutional where
the individual “did not point the gun at the officers and
apparently was not facing them when they shot him the
first time.” Curnow v. Ridgecrest Police, 952 F. 2d 321,
325 (1991). Similarly, in Harris v. Roderick, 126 F. 3d
1189 (1997), the Ninth Circuit held that the officer unrea­
sonably used deadly force against a man who, although
armed, made “no threatening movement” or “aggressive
move of any kind.” Id., at 1203.* Both Curnow and Har-
ris establish that, where, as here, an individual with a
weapon poses no objective and immediate threat to officers
or third parties, law enforcement cannot resort to exces­
sive force. See Harris, 126 F. 3d, at 1201 (“Law enforce­
ment officers may not shoot to kill unless, at a minimum,
the suspect presents an immediate threat to the officers,
or is fleeing and his escape will result in a serious threat
of injury to persons”).
   If all that were not enough, decisions from several other
Circuits illustrate that the Fourth Amendment clearly
——————
  * The majority insists that reliance on Harris fails the “ ‘straight-face
test’ ” because Harris involved an FBI sniper on a hilltop who shot a
man while he was retreating to a cabin during a standoff. Ante, at 8
(quoting 862 F. 3d, at 797 (opinion of Ikuta, J.)). If anything, though,
the context of Harris could be viewed as more dangerous than the
context here because, unlike Hughes, the suspect in Harris had en­
gaged in a firefight with other officers the previous day, during which
an officer was shot. See 126 F. 3d, at 1193–1194.
12                   KISELA v. HUGHES

                   SOTOMAYOR, J., dissenting

forbids the use of deadly force against a person who is
merely holding a knife but not threatening anyone with it.
See, e.g., McKinney v. DeKalb County, 997 F. 2d 1440,
1442 (CA11 1993) (affirming denial of summary judgment
based on qualified immunity to officer who shot a person
holding a butcher knife in one hand and a foot-long stick
in the other, where the person threw the stick and began
to rise from his seated position); Reyes v. Bridgwater, 362
Fed. Appx. 403, 404–405 (CA5 2010) (reversing grant of
summary judgment based on qualified immunity to officer
who shot a person holding a kitchen knife in his apart­
ment entryway, even though he refused to follow the
officer’s multiple commands to drop the knife); Duong v.
Telford Borough, 186 Fed. Appx. 214, 215, 217 (CA3 2006)
(affirming denial of summary judgment based on qualified
immunity to officer who shot a person holding a knife
because a reasonable jury could conclude that the plaintiff
was sitting down and pointing the knife away from the
officer at the time he was shot and had not received any
warnings to drop the knife).
  Against this wall of case law, the majority points to a
single Ninth Circuit decision, Blanford v. Sacramento
County, 406 F. 3d 1110 (2005), as proof that Kisela rea­
sonably could have believed that Hughes posed an imme­
diate danger. But Blanford involved far different circum­
stances. In that case, officers observed a man walking
through a neighborhood brandishing a 2½-foot cavalry
sword; officers commanded the man to drop the sword,
identified themselves as police, and warned “ ‘We’ll shoot.’ ”
Id., at 1112–1113. The man responded with “a loud growl­
ing or roaring sound,” which increased the officers’ concern
that he posed a risk of harm. Id., at 1113. In an effort to
“evade [police] authority,” the man, while still wielding the
sword, tried to enter a home, thus prompting officers to
open fire to protect anyone who might be inside. Id., at
1113, 1118. The Ninth Circuit concluded that use of deadly
                 Cite as: 584 U. S. ____ (2018)           13

                   SOTOMAYOR, J., dissenting

force was reasonable in those circumstances. See id., at
1119.
  This case differs significantly from Blanford in several
key respects. Unlike the man in Blanford, Hughes held a
kitchen knife down by her side, as compared to a 2½-foot
sword; she appeared calm and collected, and did not make
threatening noises or gestures toward the officers on the
scene; she stood still in front of her own home, and was not
wandering about the neighborhood, evading law enforce­
ment, or attempting to enter another house. Moreover,
unlike the officers in Blanford, Kisela never verbally
identified himself as an officer and never warned Hughes
that he was going to shoot before he did so. Given these
significant differences, no reasonable officer would believe
that Blanford justified Kisela’s conduct. The majority’s
conclusion to the contrary is fanciful.
                         *     *     *
   In sum, precedent existing at the time of the shooting
clearly established the unconstitutionality of Kisela’s
conduct. The majority’s decision, no matter how much it
says otherwise, ultimately rests on a faulty premise: that
those cases are not identical to this one. But that is not
the law, for our cases have never required a factually
identical case to satisfy the “clearly established” standard.
Hope, 536 U. S., at 739. It is enough that governing law
places “the constitutionality of the officer’s conduct beyond
debate.” Wesby, 583 U. S., at ___ (slip op., at 13) (internal
quotation marks omitted). Because, taking the facts in the
light most favorable to Hughes, it is “beyond debate” that
Kisela’s use of deadly force was objectively unreasonable,
he was not entitled to summary judgment on the basis of
qualified immunity.
                          III
  For the foregoing reasons, it is clear to me that the
14                   KISELA v. HUGHES

                   SOTOMAYOR, J., dissenting

Court of Appeals got it right. But even if that result were
not so clear, I cannot agree with the majority’s apparent
view that the decision below was so manifestly incorrect as
to warrant “the extraordinary remedy of a summary re­
versal.” Major League Baseball Players Assn. v. Garvey,
532 U. S. 504, 512–513 (2001) (Stevens, J., dissenting). “A
summary reversal is a rare disposition, usually reserved
by this Court for situations in which the law is settled and
stable, the facts are not in dispute, and the decision below
is clearly in error.” Schweiker v. Hansen, 450 U. S. 785,
791 (1981) (Marshall, J., dissenting); Office of Personnel
Management v. Richmond, 496 U. S. 414, 422 (1990)
(“Summary reversals of courts of appeals are unusual
under any circumstances”). This is not such a case. The
relevant facts are hotly disputed, and the qualified-
immunity question here is, at the very best, a close call.
Rather than letting this case go to a jury, the Court de­
cides to intervene prematurely, purporting to correct an
error that is not at all clear.
   This unwarranted summary reversal is symptomatic of
“a disturbing trend regarding the use of this Court’s re­
sources” in qualified-immunity cases. Salazar-Limon v.
Houston, 581 U. S. ___, ___ (2017) (SOTOMAYOR, J., dis­
senting from denial of certiorari) (slip op., at 8). As I have
previously noted, this Court routinely displays an un­
flinching willingness “to summarily reverse courts for
wrongly denying officers the protection of qualified im­
munity” but “rarely intervene[s] where courts wrongly
afford officers the benefit of qualified immunity in these
same cases.” Id., at ___–___ (slip op., at 8–9); see also
Baude, Is Qualified Immunity Unlawful? 106 Cal. L. Rev.
45, 82 (2018) (“[N]early all of the Supreme Court’s quali­
fied immunity cases come out the same way—by finding
immunity for the officials”); Reinhardt, The Demise of
Habeas Corpus and the Rise of Qualified Immunity: The
Court’s Ever Increasing Limitations on the Development
                 Cite as: 584 U. S. ____ (2018)          15

                   SOTOMAYOR, J., dissenting

and Enforcement of Constitutional Rights and Some Par­
ticularly Unfortunate Consequences, 113 Mich. L. Rev.
1219, 1244–1250 (2015). Such a one-sided approach to
qualified immunity transforms the doctrine into an abso­
lute shield for law enforcement officers, gutting the deter­
rent effect of the Fourth Amendment.
   The majority today exacerbates that troubling asym­
metry. Its decision is not just wrong on the law; it also
sends an alarming signal to law enforcement officers and
the public. It tells officers that they can shoot first and
think later, and it tells the public that palpably unreason­
able conduct will go unpunished. Because there is noth-
ing right or just under the law about this, I respectfully
dissent.

```

---

## GROUP: content/cases/Knight v. Jacobson.md  (`case`, 6 assertions)

### content_page

```
---
title: Knight v. Jacobson
type: case
citation: "300 F.3d 1272 (2002)"
parallel_cite: ""
neutral_cite: ""
court: 11th Cir. 2002
court_level: coa
circuit: ca11
year: 2002
date_decided: 2002-09-18
docket: 01-15506
authority_weight: "Binding in-circuit — 11th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/778847/arthur-knight-v-jacobson-officer-badge-3359-individual/"
  cluster_id: 778847
  opinion_id: null
  identity_checked: true
lake:
  record_id: Knight v. Jacobson
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Entry to Arrest]]"
    role: "Key — constructive-entry (11th Cir. narrow side: officer's body, not his voice, stays outside the threshold, 300 F.3d at 1277)"
  - page: "[[Arrest in the Home]]"
    role: "Related — constructive-entry cross-ref"
related:
  - "[[Entry to Arrest]]"
  - "[[Arrest in the Home]]"
  - "[[Payton v. New York]]"
  - "[[United States v. Watson]]"
tags:
  - case
  - fourth-amendment
  - arrest
  - warrantless-arrest
  - payton
  - threshold
  - home
holding: "Payton's warrant requirement for in-home arrests is not violated when an officer standing outside the home orders a suspect to step outside and then arrests him without a warrant — Payton keeps the officer's body, not his voice, outside the threshold."
---

# Knight v. Jacobson

*300 F.3d 1272 (11th Cir. 2002)* (No. 01-15506) · U.S. Court of Appeals for the Eleventh Circuit · **Binding in-circuit — 11th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 778847 → opinion 778847 (300 F.3d 1272, decided 2002-09-18); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Miami Officer Dennis Jacobson, investigating a report from Arthur Knight's ex-girlfriend, went to Knight's home. Knight came to the door in response to a knock; Jacobson, standing outside, told him to step outside. Knight complied, stepped out, and was arrested without a warrant. Knight sued under § 1983, contending the warrantless arrest violated *[[Payton v. New York]]*. The district court denied the officer summary judgment on [[Qualified Immunity|qualified immunity]], and Jacobson appealed.

## Issue
Whether *[[Payton v. New York|Payton]]*'s prohibition on warrantless in-home arrests is violated when an officer outside the home directs a suspect to step outside and then arrests him without a warrant.

## Rule
The Eleventh Circuit reversed, answering "no." *[[Payton v. New York|Payton]]* draws "a firm line at the entrance to the house" that officers may not cross without a warrant absent [[Exigent Circumstances and Hot Pursuit|exigency]] — but the arrest here happened outside that line. "*Payton* keeps the officer's body outside the threshold, not his voice. It does not prevent a law enforcement officer from telling a suspect to step outside his home and then arresting him without a warrant." — 300 F.3d at 1277.

## Application
Because Officer Jacobson never crossed the threshold and Knight was arrested just outside his door after voluntarily stepping out at the officer's request, no in-home arrest occurred. The public-place arrest was governed by the ordinary rule permitting warrantless arrests on probable cause, not by *[[Payton v. New York|Payton]]*'s in-home warrant requirement, so the officer was entitled to [[Qualified Immunity|qualified immunity]].

## Conclusion
The denial of summary judgment was **reversed**; Officer Jacobson was entitled to [[Qualified Immunity|qualified immunity]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Knight v. Jacobson* marks the boundary of the *[[Payton v. New York|Payton]]* rule: the constitutional protection attaches to physical entry across the threshold, so an officer's summons to a suspect to come outside — followed by a warrantless arrest supported by probable cause under *[[United States v. Watson]]* — does not offend the Fourth Amendment.

## Appears on
- [[Entry to Arrest]] — *Key*
- [[Arrest in the Home]] — *Related*

## Sources
- [*Knight v. Jacobson*, 300 F.3d 1272 (11th Cir. 2002)](https://www.courtlistener.com/opinion/778847/arthur-knight-v-jacobson-officer-badge-3359-individual/) — pinpoint: 1277 (Opinion of the Court); Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8556b6b56491be99", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "300 F.3d 1272 (2002)", "court": "11th Cir. 2002", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Knight v. Jacobson", "year": "2002"}}
{"assertion_id": "453767d37f1bd10d", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Payton's warrant requirement for in-home arrests is not violated when an officer standing outside the home orders a suspect to step outside and then arrests him without a warrant — Payton keeps the officer's body, not his voice, outside the threshold.", "title": "Knight v. Jacobson"}}
{"assertion_id": "5721b37e2f7363b6", "dimension": "support", "kind": "home_role", "locator": {"home": "Entry to Arrest"}, "payload": {"home": "Entry to Arrest", "role": "Key — constructive-entry (11th Cir. narrow side: officer's body, not his voice, stays outside the threshold, 300 F.3d at 1277)", "title": "Knight v. Jacobson"}}
{"assertion_id": "9037c171e8e80ec4", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest in the Home"}, "payload": {"home": "Arrest in the Home", "role": "Related — constructive-entry cross-ref", "title": "Knight v. Jacobson"}}
{"assertion_id": "aa8e5751b345dca4", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Knight v. Jacobson", "varies_by_point": "false"}}
{"assertion_id": "f6bd7b111f54fd78", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 11th Cir.", "title": "Knight v. Jacobson"}}
```

### lake record — Knight v. Jacobson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Knight v. Jacobson",
  "status": "under_review",
  "identity": {
    "case_name": "Arthur Knight v. Jacobson, Officer, Badge 3359, Individual",
    "case_name_short": "",
    "case_name_full": "Arthur KNIGHT, Plaintiff-Appellee, v. JACOBSON, Officer, Badge # 3359, Individual, Defendant-Appellant",
    "input_case_name": "Knight v. Jacobson",
    "court": "11th Cir. 2002",
    "court_id": "ca11",
    "court_level": "coa",
    "circuit": "ca11",
    "state": null,
    "date_decided": "2002-09-18",
    "year": 2002,
    "docket": "01-15506",
    "cluster_id": 778847,
    "lead_opinion_id": 778847,
    "sibling_ids": [],
    "absolute_url": "/opinion/778847/arthur-knight-v-jacobson-officer-badge-3359-individual/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "300 F.3d 1272",
      "volume": "300",
      "reporter": "F.3d",
      "page": "1272",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "300 F.3d 1272",
        "volume": "300",
        "reporter": "F.3d",
        "page": "1272",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "300 F.3d 1272",
    "official_selection": {
      "court_class": "state",
      "selected": "300 F.3d 1272",
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
    "date_created": "2026-07-06T05:46:16Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:46:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:46:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:46:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:46:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "knight-v-jacobson--778847",
      "to_record_id": "Knight v. Jacobson",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Knight v. Jacobson

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b1221-25">
  CARNES, Circuit Judge:
 </author>
<p id="b1221-26">
  This appeal by a law enforcement officer from the denial of qualified immunity presents us with these three issues: 1) whether there was an absence of probable cause for the officer’s arrest of the plaintiff; 2) whether non-compliance with state law in making an arrest is itself enough to violate
  <span citation-index="1" class="star-pagination" label="1274"> 
   *1274
   </span>
  the Fourth Amendment; and 3) whether the restrictions that
  <em>
   Payton v. New York,
  </em>
  <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U.S. 573</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">63 L.Ed.2d 639</a></span> (1980), places upon warrantless arrests are violated when an officer arrests a suspect who has stepped outside his home at the officer’s command. We answer each of those questions “no.”
 </p>
<p id="b1222-3">
  Miami Police Officer Dennis Jacobson investigated a report from Arthur Knight’s ex-girlfriend that Knight, who lived next door to her, had called and threatened to kill her. She recounted to Jacobson that Knight had told her that not only was he going to kill her, but that he was going to enjoy killing her and would derive great pleasure from it. Officer Jacobson interviewed the woman; she recounted those facts to him and convinced him that she feared for her life. The woman also told Officer Jacobson about other incidents involving Knight that had caused her to bring criminal charges against him, and she gave Jacobson the case numbers for two of the cases that had resulted from her previous complaints against Knight. She was visibly upset and told Officer Jacobson that she feared for her life. Based on everything he heard and his observations of the woman’s demeanor, Officer Jacobson left her apartment, went next door and knocked on Knight’s door. He told Knight to step outside, and when he did, Jacobson arrested him on the spot without first obtaining a warrant. The arrest took place at 2:00 a.m. on June 25, 1996.
 </p>
<p id="b1222-4">
  Knight’s arrest did not result in prosecution, but it did result in Knight filing a lawsuit against Jacobson under <span class="citation no-link">42 U.S.C. § 1983</span> claiming an unconstitutional arrest.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  Knight contends that Officer Jacobson’s arrest of him violated the Fourth Amendment. The district court initially granted Officer Jacobson summary judgment but later took it back in an order issued under Rule 60(b)(3), the procedural details of which are not relevant to the issues that are now before us. Insofar as Officer Jacobson’s appeal from the denial of qualified immunity on the unconstitutional arrest claim is concerned—the only appeal before us—the dispositive issues are the three we stated in the opening paragraph of this opinion.
 </p>
<p id="b1222-7">
  An officer sued for having made an arrest without probable cause is entitled to qualified immunity if there was arguable probable cause for the arrest, which is a more lenient standard than probable cause.
  <em>
   See Jones v. Cannon,
  </em>
  <span class="citation" data-id="73740"><a href="/opinion/73740/jones-v-cannon/" aria-description="Citation for case: Jones v. Cannon">174 F.3d 1271</a></span>, 1283 n. 3 (11th Cir.1999) (“Arguable probable cause, not the higher standard of actual probable cause, governs the qualified immunity inquiry.”);
  <em>
   Montoute v. Carr,
  </em>
  <span class="citation" data-id="71806"><a href="/opinion/71806/montoute-v-city-of-sebring/#184" aria-description="Citation for case: Montoute v. City of Sebring">114 F.3d 181, 184</a></span> (11th Cir.1997) (“In order to be entitled to qualified immunity from a Fourth Amendment claim, an officer need not have actual probable cause but only ‘arguable probable cause,’ i.e., the facts and circumstances must be such that the officer reasonably could have believed that probable cause existed.”). The difference in the two standards is immaterial in this case because Officer Jacobson had probable cause to arrest Knight.
 </p>
<p id="b1222-8">
  Probable cause is “defined in terms of facts and circumstances sufficient to warrant a prudent man in believing that the suspect had committed or was committing an offense.”
  <em>
   Gerstein v. Pugh,
  </em>
  <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#111" aria-description="Citation for case: Gerstein v. Pugh">420 U.S. 103, 111</a></span>, <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#862" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854, 862</a></span>, <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">43 L.Ed.2d 54</a></span> (1975) (internal quotation marks, citation, and brackets omitted). A prudent
  <span citation-index="1" class="star-pagination" label="1275"> 
   *1275
   </span>
  man in Officer Jacobson’s place would have been warranted in believing that Knight had committed the crime of misdemeanor assault. Florida law defines misdemeanor assault as “an intentional, unlawful threat by word or act to do violence to the person of another, coupled with an apparent ability to do so, and in doing some act which creates a well-founded fear in such other person that such violence is imminent.” <span class="citation no-link">Fla. Stat. Ann. § 784.011</span>.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
</p>
<p id="b1223-5">
  By the time he finished talking with Knight’s ex-girlfriend, Officer Jacobson had heard enough to warrant a prudent person in believing that Knight had intentionally threatened to do violence to her and that Knight, who lived next door to her, had an apparent ability to carry out the threat, and in making it had created a well-founded fear in her that violence was imminent. Knight was never convicted or even prosecuted for that crime or any other stemming from the arrest, but that does not matter.
  <em>
   See Baker v. McCollan,
  </em>
  <span class="citation" data-id="9427663"><a href="/opinion/110132/baker-v-mccollan/#145" aria-description="Citation for case: Baker v. McCollan">443 U.S. 137, 145</a></span>, <span class="citation" data-id="9427663"><a href="/opinion/110132/baker-v-mccollan/#2695" aria-description="Citation for case: Baker v. McCollan">99 S.Ct. 2689, 2695</a></span>, <span class="citation" data-id="9427663"><a href="/opinion/110132/baker-v-mccollan/" aria-description="Citation for case: Baker v. McCollan">61 L.Ed.2d 433</a></span> (1979) (“The Constitution does not guarantee that only the guilty will be arrested. If it did, § 1983 would provide a cause of action for every defendant acquitted—indeed, for every suspect released.”);
  <em>
   Von Stein v. Brescher,
  </em>
  <span class="citation" data-id="542392"><a href="/opinion/542392/charles-h-von-stein-v-george-a-brescher/" aria-description="Citation for case: Charles H. Von Stein v. George A. Brescher">904 F.2d 572</a></span>, 578 n. 9 (11th Cir.1990) (“‘Probable cause’ defines a radically different standard than ‘beyond a reasonable doubt,’ and while an arrest must stand on more than suspicion, the arresting officer need not have in hand evidence sufficient to obtain a conviction.”);
  <em>
   United States v. Pantoja-Soto,
  </em>
  <span class="citation" data-id="9472437"><a href="/opinion/439177/united-states-v-fulgencio-pantoja-soto-raul-pal-sali-nelio-a-nunez-and/" aria-description="Citation for case: United States v. Fulgencio Pantoja-Soto, Raul Pal-Sali,...">739 F.2d 1520</a></span>, 1524 n. 7 (11th Cir.1984) (same). When Knight was arrested in the early morning hours of July 25, 1996, there was probable cause to believe he had committed the crime of misdemean- or assault.
 </p>
<p id="b1223-8">
  Knight’s principal argument to the contrary maintains that under Florida law an assault cannot occur if the threat is made over the telephone. For that proposition he relies on
  <em>
   Trowell v. Meads,
  </em>
  <span class="citation" data-id="1802074"><a href="/opinion/1802074/trowell-v-meads/" aria-description="Citation for case: Trowell v. Meads">618 So.2d 351</a></span> (Fla. 1st DCA 1993), which is readily distinguishable. In
  <em>
   <span class="citation" data-id="1802074"><a href="/opinion/1802074/trowell-v-meads/" aria-description="Citation for case: Trowell v. Meads">Trowell</a></span>
  </em>
  the plaintiff sought a permanent restraining order against her former husband, contending that he had assaulted her by making threats during a telephone conversation while he was involuntarily confined in a Florida state mental hospital.
  <span class="citation" data-id="1802074"><a href="/opinion/1802074/trowell-v-meads/#351" aria-description="Citation for case: Trowell v. Meads"><em>
   Id.
  </em>
  at 351</a></span>. In a two-paragraph opinion, the district court of appeals concluded that under those facts there had been no assault.
  <span class="citation" data-id="1802074"><a href="/opinion/1802074/trowell-v-meads/#351" aria-description="Citation for case: Trowell v. Meads"><em>
   Id.
  </em>
  at 351-52</a></span>. The facts in this case are different. Unlike the former husband in
  <em>
   Tro-well,
  </em>
  Knight was not involuntarily confined and therefore without any apparent ability to inflict violence and create a well-founded fear that the threatened violence was imminent. Instead, Knight was free and unconfined and conveniently located right next door to the target of his threat. Knight’s contention that Officer Jacobson had no probable cause to arrest him is unfounded.
 </p>
<p id="b1223-9">
  Knight also contends that his arrest, even if supported by probable cause, violated the Fourth Amendment because it was not done in accord with state law.
  <span citation-index="1" class="star-pagination" label="1276"> 
   *1276
   </span>
  With an exception or two not relevant here, Florida law authorizes warrantless arrests for misdemeanors only if they are committed in the officer’s presence. <span class="citation no-link">Fla. Stat. Ann. § 901.15</span>(1). The misdemeanor assault in this case was not. From those two premises Knight concludes that his arrest violated the Fourth Amendment. However, there is another premise essential to that conclusion which is not correct, and it is the proposition that an arrest supported by probable cause in circumstances where arrest is not permitted under state law violates the Fourth Amendment.
 </p>
<p id="b1224-4">
  Section 1983 does not create a remedy for every wrong committed under the color of state law, but only for those that deprive a plaintiff of a federal right.
  <em>
   See Paul v. Davis,
  </em>
  <span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/#698" aria-description="Citation for case: Paul v. Davis">424 U.S. 693, 698-99</a></span>, <span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/#1159" aria-description="Citation for case: Paul v. Davis">96 S.Ct. 1155, 1159</a></span>, <span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/" aria-description="Citation for case: Paul v. Davis">47 L.Ed.2d 405</a></span> (1976). There is no federal right not to be arrested in violation of state law.
  <em>
   See Pyles v. Raisor,
  </em>
  <span class="citation" data-id="9488345"><a href="/opinion/700474/teresa-a-pyles-v-robert-s-raisor-ray-l-sabbatine/#1215" aria-description="Citation for case: Teresa A. Pyles v. Robert S. Raisor, Ray L. Sabbatine">60 F.3d 1211, 1215</a></span> (6th Cir.1995) (holding that federal law, not state law, determines the validity of arrests under the Fourth Amendment);
  <em>
   Fields v. City of South Houston,
  </em>
  922 F.2d at 1183, 1189 (5th Cir.1991) (same);
  <em>
   Barry v. Fowler,
  </em>
  902 F.2d at 770, 772 (9th Cir.1990) (same);
  <em>
   McKinney v. George,
  </em>
  <span class="citation" data-id="430916"><a href="/opinion/430916/raymond-lee-mckinney-v-velma-george/#1188" aria-description="Citation for case: Raymond Lee McKinney v. Velma George">726 F.2d 1183, 1188</a></span> (7th Cir.1984) (same);
  <em>
   Street v. Surdyka,
  </em>
  <span class="citation" data-id="317151"><a href="/opinion/317151/george-b-street-v-officer-leo-surdyka-baltimore-city-police-department/#370" aria-description="Citation for case: George B. Street v. Officer Leo Surdyka, Baltimore City...">492 F.2d 368, 370-73</a></span> (4th Cir.1974) (same). While the violation of state law may (or may not) give rise to a state tort claim, it is not enough by itself to support a claim under section 1983.
  <em>
   See Barry,
  </em>
  902 F.2d at 773 (“While Barry may have a remedy under state law [for the warrantless arrest], she has faded to allege a federal constitutional or federal statutory violation”);
  <em>
   Diamond v. Marland,
  </em>
  <span class="citation" data-id="1416667"><a href="/opinion/1416667/diamond-v-marland/#439" aria-description="Citation for case: Diamond v. Marland">395 F.Supp. 432, 439</a></span> (S.D.Ga.1976) (“Even if a police officer violates a state arrest statute, he would not be hable under [§ 1983] unless he also violated federal constitutional law governing warrantless arrests.”);
  <em>
   see also Paul v. Davis,
  </em>
  <span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/#699" aria-description="Citation for case: Paul v. Davis">424 U.S. at 699</a></span>, <span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/#1159" aria-description="Citation for case: Paul v. Davis">96 S.Ct. at 1159</a></span> (rejecting the argument that “every legally cognizable injury which may have been inflicted by a state official acting ‘under color of law’ establishes] a violation of the Fourteenth Amendment”);
  <em>
   Lovins v. Lee,
  </em>
  <span class="citation" data-id="70285"><a href="/opinion/70285/lovins-v-lee/" aria-description="Citation for case: Lovins v. Lee">53 F.3d 1208</a></span>, 1210 — 1211 (11th Cir.1995) (holding that while the plaintiff may have a claim under state law against defendants because they acted contrary to state law in releasing an inmate who harmed her, that violation of state law did not give her a federal constitutional claim).
 </p>
<p id="b1224-7">
  The only authority Knight cites in support of his contention that violation of state law governing arrests automatically contravenes the Fourth Amendment is a Supreme Court case that applied state arrest law to determine the validity of an arrest for a federal offense when there was no federal statute governing the situation.
  <em>
   See Johnson v. United States,
  </em>
  <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U.S. 10</a></span>, 15 n. 5, <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#370" aria-description="Citation for case: Johnson v. United States">68 S.Ct. 367, 370</a></span>, <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">92 L.Ed. 436</a></span> (1948);
  <em>
   see also United States v. Di Re,
  </em>
  <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#589" aria-description="Citation for case: United States v. Di Re">332 U.S. 581, 589</a></span>, <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#226" aria-description="Citation for case: United States v. Di Re">68 S.Ct. 222, 226</a></span>, <span class="citation no-link">92 L.Ed. 210</span> (1948). Borrowing state arrest procedure standards in those circumstances is a different matter from holding that those state law standards define constitutional mínimums. As the Fourth Circuit concluded: “The use of state law in such cases seems clearly to be based on non-constitutional considerations.”
  <em>
   Street,
  </em>
  <span class="citation" data-id="317151"><a href="/opinion/317151/george-b-street-v-officer-leo-surdyka-baltimore-city-police-department/" aria-description="Citation for case: George B. Street v. Officer Leo Surdyka, Baltimore City...">492 F.2d at 372</a></span> n. 7.
  <em>
   See also
  </em>
  3 Wayne R. La Fave, Search and Seizure § 5.1(b), at 22 (3d ed,1996)(same). We reject the notion that the Florida law procedures governing warrantless arrests are written into the federal Constitution.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b1225-3">
<span citation-index="1" class="star-pagination" label="1277"> 
   *1277
   </span>
  Knight’s final contention is that his arrest violated the Fourth Amendment as explicated in
  <em>
   Payton v. New York,
  </em>
  <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#590" aria-description="Citation for case: Payton v. New York">445 U.S. 573, 590</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1382" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371, 1382</a></span> (1980), which held that a warrantless arrest inside the home of a suspect is presumptively unreasonable unless exigent circumstances justify the intrusion. This part of Knight’s case founders on the facts, because Knight was not arrested inside his home, but just outside the door of it after he stepped out as instructed by Officer Jacobson.
 </p>
<p id="b1225-4">
  The rule of
  <em>
   <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
  </em>
  is that there is “a firm line at the entrance to the house,” and absent exigent circumstances “that threshold may not reasonably be crossed without a warrant.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#590" aria-description="Citation for case: Payton v. New York">445 U.S. at 590</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1382" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1382</a></span>. Officer Jacobson never crossed that threshold or went over the line at the entrance to the house. As Knight himself testified in deposition: “There was a knock on my door, I came to the door, and Officer Jacobson said, “What are you doing?’ I said, T am in here, can I help you?’ He told me to step outside; I stepped outside; he walked around me a full circle and he told me to put my hands on the car ... And then he handcuffed me. And then he put me in the car.”
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
</p>
<p id="b1225-7">
<em>
   <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
  </em>
  keeps the officer’s body outside the threshold, not his voice. It does not prevent a law enforcement officer from telling a suspect to step outside his home and then arresting him without a warrant. In that situation, the officer never crosses “the firm line at the entrance to the house” which is where
  <em>
   <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
  </em>
  drew the line.
  <em>
   See United States v. Berkowitz,
  </em>
  <span class="citation" data-id="9481419"><a href="/opinion/557342/united-states-v-marvin-berkowitz/#1386" aria-description="Citation for case: United States v. Marvin Berkowitz">927 F.2d 1376, 1386</a></span> (7th Cir.1991)
  <em>
   (Payton
  </em>
  prohibits only a warrantless
  <em>
   entry
  </em>
  into the
  <em>
   home, “not
  </em>
  a policeman’s use of his voice to convey a message of arrest from outside the home.” (emphasis in original)).
  <em>
   See also United States v. Carrion,
  </em>
  <span class="citation" data-id="482020"><a href="/opinion/482020/united-states-v-anthony-nicholas-carrion-and-fred-solmor/#1128" aria-description="Citation for case: United States v. Anthony Nicholas Carrion and Fred Solmor">809 F.2d 1120, 1128</a></span> (5th Cir.1987) (arrest of suspect in doorway of home is reasonable and not contrary to Payton);
  <em>
   McKinney v. George,
  </em>
  <span class="citation" data-id="430916"><a href="/opinion/430916/raymond-lee-mckinney-v-velma-george/#1188" aria-description="Citation for case: Raymond Lee McKinney v. Velma George">726 F.2d 1183, 1188</a></span> (7th Cir.1984) (arrest of suspect who opened the door in response to officers’ knocks and who was arrested outside his home is reasonable and not contrary to
  <em>
   Payton); United States v. Whitten,
  </em>
  <span class="citation" data-id="418069"><a href="/opinion/418069/united-states-v-kenneth-joe-whitten-john-elmer-gaiefsky-jack-wayne-gish/#1015" aria-description="Citation for case: United States v. Kenneth Joe Whitten, John Elmer...">706 F.2d 1000, 1015</a></span> (9th Cir.1983) (doorway is
  <span citation-index="1" class="star-pagination" label="1278"> 
   *1278
   </span>
  a public place not subject to
  <em>
   <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
  </em>
  restriction);
  <em>
   United States v. Botero,
  </em>
  <span class="citation" data-id="362276"><a href="/opinion/362276/united-states-v-diego-botero-united-states-of-america-v-robert-dennis/#432" aria-description="Citation for case: United States v. Diego Botero, United States of America...">589 F.2d 430, 432</a></span> (9th Cir.1978) (arrest of suspect in doorway after the suspect answers the door is reasonable).
  <em>
   See generally
  </em>
  3 Wayne R. La Fave, Search and Seizure § 6.1(e), at 254-263 (3d ed.1996).
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
</p>
<p id="b1226-4">
  The order of the district court denying .Officer Jacobson’s motion for summary judgment based on qualified immunity is REVERSED, and the case is REMANDED with directions that summary judgment be entered for him on that basis.
 </p>





<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b1222-5">
   . Knight says that the arrest involved in this case is just one of four warrantless arrests that represent a pattern of harassment by the City of Miami, Jacobson, and another defendant in this lawsuit. We are concerned only with the arrest that occurred on June 25, 1996, and with the issues arising from it as they relate to Officer Jacobson, the only defendant before us in this appeal.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b1223-6">
<em>
    .
   </em>
   Knight contends that he was arrested for misdemeanor assault, while Officer Jacobson says the arrest was for the crime of domestic violence. We need not resolve that dispute, because Jacobson prevails even under Knight’s theory, and it is irrelevant which crime he thought he was arresting Knight for at the time.
   <em>
    See Lee v. Ferraro,
   </em>
   <span class="citation" data-id="75789"><a href="/opinion/75789/kim-d-lee-v-luis-ferraro/#1196" aria-description="Citation for case: Kim D. Lee v. Luis Ferraro">284 F.3d 1188, 1196</a></span> (11th Cir.) C'[W]hen an officer makes an arrest, which is properly supported by probable cause to arrest lor a certain offense, neither his subjective reliance on an offense for which no probable cause exists nor his verbal announcement of the wrong offense vitiates the arrest.” (internal marks omitted) (quoting
   <em>
    United States v. Saunders,
   </em>
   <span class="citation" data-id="310037"><a href="/opinion/310037/united-states-v-mansfield-saunders/#7" aria-description="Citation for case: United States v. Mansfield Saunders">476 F.2d 5, 7</a></span> (5th Cir.1973)))
   <em>
    reh’g and reh’g en banc denied,
   </em>
   <span class="citation no-link">37 Fed.Appx. 503</span> (11th Cir. May 13, 2002) (No. 00-16054).
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b1224-5">
   . About warrantless arrests for misdemeanors, we decide only the issue framed by Knight's argument, which is that violation of a state law restriction on such arrests violates the Fourth Amendment because state law has been contravened. Knight has not argued, and so we do not decide, whether an arrest
   <span citation-index="1" class="star-pagination" label="1277"> 
    *1277
    </span>
   for a misdemeanor not committed in the officer’s presence violates the Fourth Amendment itself irrespective of state law. We note in passing, however, that every circuit that has addressed the issue has held that the Fourth Amendment does not include an in-the-presence requirement for warrantless misdemeanor arrests.
   <em>
    See Pyles v. Raisor,
   </em>
   <span class="citation" data-id="9488345"><a href="/opinion/700474/teresa-a-pyles-v-robert-s-raisor-ray-l-sabbatine/#1215" aria-description="Citation for case: Teresa A. Pyles v. Robert S. Raisor, Ray L. Sabbatine">60 F.3d 1211, 1215</a></span> (6th Cir.1995) (“Pyles' rights under Kentucky law, including her right as an alleged misdemeanant to be arrested only when the misdemeanor is committed in the presence of the arresting officer, are not grounded in the federal Constitution and will not support a § 1983 claim.");
   <em>
    Fields v. City of South Houston,
   </em>
   922 F.2d at 1183, 1189 (5th Cir.1991) (“The United States Constitution does not require a warrant for misdemeanors not occurring in the presence of the arresting officer.”);
   <em>
    Barry v. Fowler,
   </em>
   902 F.2d at 770, 772 (9th Cir.1990) ("The requirement that a misdemeanor must have occurred in the officer's presence to justify a warrantless arrest is not grounded in the Fourth Amendment.”);
   <em>
    Street v. Surdyka,
   </em>
   <span class="citation" data-id="317151"><a href="/opinion/317151/george-b-street-v-officer-leo-surdyka-baltimore-city-police-department/#372" aria-description="Citation for case: George B. Street v. Officer Leo Surdyka, Baltimore City...">492 F.2d 368, 372</a></span> (4th Cir.1974) ("We do not think the Fourth Amendment should now be interpreted to prohibit warrantless arrests for misdemeanors committed outside an officer’s presence.”).
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b1225-9">
   . Knight did say that Officer Jacobson eventually went inside the apartment, but he made clear that happened after the arrest had been made and was done for the purpose of retrieving Knight’s identification. Knight testified: "Then Jacobson—the other one, his partner stayed in there [at his ex-girlfriend’s apartment] and then because he was asking me do I have ID and I told him my ID was inside on my dresser. He went in, he got my <span class="citation" data-id="317151"><a href="/opinion/317151/george-b-street-v-officer-leo-surdyka-baltimore-city-police-department/" aria-description="Citation for case: George B. Street v. Officer Leo Surdyka, Baltimore City...">ID.</a></span> Or my driver’s license.” At oral argument, Knight again conceded that no officer stepped inside the home until after he had been arrested. Knight has not argued that Officer Jacobson's entry into the apartment after the arrest had been made and for the purpose of retrieving Knight's identification violated the
   <em>
    <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
   </em>
   rule.
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b1226-13">
   . Some courts have held that when the suspect leaves his home because of coercive tactics by the police, the arrest is illegal.
   <em>
    See, e.g., United States v. Morgan,
   </em>
   <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1166" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d 1158, 1166-67</a></span> (6th Cir.1984) (holding that a war-rantless arrest made after the suspect stepped outside the home was unconstitutional because of the coercive tactics used by the police, which included having nine officers surround the home, flooding the home with spotlights, and summoning the suspect through a bullhorn). There were no such tactics in this case, just a simple direction by one officer that Knight step outside.
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Knowles v. Iowa.md  (`case`, 6 assertions)

### content_page

```
---
title: "Knowles v. Iowa"
type: case
citation: "525 U.S. 113 (1998)"
parallel_cite: "119 S. Ct. 484; 142 L. Ed. 2d 492"
neutral_cite: 1998 U.S. LEXIS 8068
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1998
date_decided: 1998-12-08
docket: 97-7597
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1998-12-08
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Knowles v. Iowa
  varies_by_point: false
  scope_note: "Controlling: there is no 'search incident to citation' — issuing a citation, without a custodial arrest, does not authorize a full search."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118250/knowles-v-iowa/"
  cluster_id: 118250
  opinion_id: 118250
  identity_checked: true
homes:
  - page: "[[SIA Persons]]"
    role: "Limiting"
  - page: "[[Traffic Stops]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Robinson]]", "[[Pennsylvania v. Mimms]]", "[[Maryland v. Wilson]]", "[[Virginia v. Moore]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "traffic-stops", "citation"]
holding: "Issuing a traffic citation, without a custodial arrest, does not authorize a search incident to arrest; neither the officer-safety nor the evidence-preservation rationale supports a full search where the driver is merely cited."
lake:
  record_id: Knowles v. Iowa
  status: verified
  projected_at: 2026-07-09
---

# Knowles v. Iowa

*525 U.S. 113 (1998)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
An Iowa officer stopped Knowles for driving 43 mph in a 25 mph zone and issued him a citation rather than arresting him, although Iowa law authorized either course. Relying on an Iowa statute the state courts read to permit a "search incident to citation," the officer then conducted a full search of the car and found marijuana and a pipe under the driver's seat. Knowles was arrested on drug charges. At the [[Common Legal Terms#suppression-hearing|suppression hearing]] the officer conceded he had neither Knowles' consent nor probable cause to search.

## Issue
Does the Fourth Amendment permit an officer to conduct a full search of a vehicle incident to the issuance of a traffic citation, where the driver has not been placed under custodial arrest?

## Rule
No. The question "is whether such a procedure authorizes the officer, consistently with the Fourth Amendment, to conduct a full search of the car. We answer this question 'no.' " — 525 U.S. at 113. ^pin-113

The two rationales for the search-incident exception — officer safety and the preservation of evidence — do not support the search: "neither of these underlying rationales for the search incident to arrest exception is sufficient to justify the search in the present case." — [*Id.* at 116–17](https://www.courtlistener.com/opinion/118250/knowles-v-iowa/#:~:text=neither%20of%20these%20underlying%20rationales). ^pin-116

A traffic stop's officer-safety concern is lower than a custodial arrest's and is met by lesser measures (ordering occupants out, a *[[Terry v. Ohio|Terry]]* frisk on reasonable suspicion, a *[[Michigan v. Long]]* protective search). And as to evidence, "[o]nce Knowles was stopped for speeding and issued a citation, all the evidence necessary to prosecute that offense had been obtained." — *Id.* at 118. ^pin-118

The Court refused to extend *[[United States v. Robinson|Robinson]]*'s bright-line full-search rule "to a situation where the concern for officer safety is not present to the same extent and the concern for destruction or loss of evidence is not present at all. We decline to do so." — [*Id.* at 118–19](https://www.courtlistener.com/opinion/118250/knowles-v-iowa/#:~:text=to%20a%20situation%20where%20the). ^pin-119

## Application
Knowles was cited, not arrested, and the officer had neither consent nor probable cause. Because a brief traffic stop poses a lesser safety risk — addressable by ordering the driver out, a frisk on reasonable suspicion, or a protective vehicle search — and because issuing the speeding citation had already secured all evidence of that offense, neither search-incident rationale applied. The "search incident to citation" had no constitutional basis.

## Conclusion
The full search of the car was unconstitutional; the judgment of the Iowa Supreme Court was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Knowles* remains controlling: there is no "search incident to citation." It cabins [[United States v. Robinson]]'s [[Common Legal Terms#bright-line-rule|bright-line rule]] to actual custodial arrests and is the contrast point in [[Virginia v. Moore]] (full search permitted because Moore was *arrested*). No negative treatment.

## Appears on
- [[SIA Persons]] — *Limiting*
- [[Traffic Stops]] — *Related (cross-doctrine)*

## Sources
- *Knowles v. Iowa*, 525 U.S. 113 (1998) — https://www.courtlistener.com/opinion/118250/knowles-v-iowa/ — pinpoints: 113, 116–117, 118, 119.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "412159bf6f12c69f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "525 U.S. 113 (1998)", "court": "U.S. Supreme Court", "neutral_cite": "1998 U.S. LEXIS 8068", "official_citation_present": true, "parallel_cite": "119 S. Ct. 484; 142 L. Ed. 2d 492", "title": "Knowles v. Iowa", "year": "1998"}}
{"assertion_id": "13da9a35894ebd89", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Related (cross-doctrine)", "title": "Knowles v. Iowa"}}
{"assertion_id": "3e4c6328e4f9ecb8", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Persons"}, "payload": {"home": "SIA Persons", "role": "Limiting", "title": "Knowles v. Iowa"}}
{"assertion_id": "717934c828fa7ace", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Issuing a traffic citation, without a custodial arrest, does not authorize a search incident to arrest; neither the officer-safety nor the evidence-preservation rationale supports a full search where the driver is merely cited.", "title": "Knowles v. Iowa"}}
{"assertion_id": "21c054c3619b4d87", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1998-12-08", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Knowles v. Iowa", "field_i_validity": "good_law", "scope_note": "Controlling: there is no 'search incident to citation' — issuing a citation, without a custodial arrest, does not authorize a full search.", "title": "Knowles v. Iowa", "varies_by_point": "false"}}
{"assertion_id": "f6948c840c39a85a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Knowles v. Iowa"}}
```

### lake record — Knowles v. Iowa

```json
{
  "schema_version": "s2.v1",
  "record_id": "Knowles v. Iowa",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Knowles v. Iowa",
    "case_name_short": "Knowles",
    "case_name_full": "Knowles v. Iowa",
    "input_case_name": "Knowles v. Iowa",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1998-12-08",
    "year": 1998,
    "docket": "97-7597",
    "cluster_id": 118250,
    "lead_opinion_id": 118250,
    "sibling_ids": [
      118250
    ],
    "absolute_url": "/opinion/118250/knowles-v-iowa/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9179844,
        "score": 20,
        "case_name": "Knowles v. Iowa"
      },
      {
        "cluster_id": 9179843,
        "score": 20,
        "case_name": "Knowles v. Iowa"
      },
      {
        "cluster_id": 9170706,
        "score": 20,
        "case_name": "Knowles v. Iowa"
      },
      {
        "cluster_id": 9168391,
        "score": 20,
        "case_name": "Knowles v. Iowa"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "525 U.S. 113",
      "volume": "525",
      "reporter": "U.S.",
      "page": "113",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "119 S. Ct. 484",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "484",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "142 L. Ed. 2d 492",
        "volume": "142",
        "reporter": "L. Ed. 2d",
        "page": "492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1998 U.S. LEXIS 8068",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "8068",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "525 U.S. 113",
        "volume": "525",
        "reporter": "U.S.",
        "page": "113",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "119 S. Ct. 484",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "484",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "142 L. Ed. 2d 492",
        "volume": "142",
        "reporter": "L. Ed. 2d",
        "page": "492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1998 U.S. LEXIS 8068",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "8068",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "525 U.S. 113",
    "official_selection": {
      "court_class": "scotus",
      "selected": "525 U.S. 113",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-113",
      "page": null,
      "quote": "the officer then conducted a full search of the car and found marijuana and a pipe under the driver's seat. Knowles was arrested on drug charges. At the suppression hearing the officer conceded he had neither Knowles' consent nor probable cause to search. ## Issue Does the Fourth Amendment permit an officer to conduct a full search of a vehicle incident to the issuance of a traffic citation, where the driver has not been placed under custodial arrest? ## Rule No. The question",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-116",
      "page": null,
      "quote": "neither of these underlying rationales for the search incident to arrest exception is sufficient to justify the search in the present case.",
      "star_marker": "117",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 7271,
      "fragment": "#:~:text=neither%20of%20these%20underlying%20rationales",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-118",
      "page": null,
      "quote": "[o]nce Knowles was stopped for speeding and issued a citation, all the evidence necessary to prosecute that offense had been obtained.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-119",
      "page": null,
      "quote": "to a situation where the concern for officer safety is not present to the same extent and the concern for destruction or loss of evidence is not present at all. We decline to do so.",
      "star_marker": "119",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 14092,
      "fragment": "#:~:text=to%20a%20situation%20where%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1998-12-08",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Knowles v. Iowa",
    "varies_by_point": false,
    "scope_note": "Controlling: there is no 'search incident to citation' \u2014 issuing a citation, without a custodial arrest, does not authorize a full search.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Solorio",
          "cluster_id": 10133534,
          "cite": [
            "304 Or. App. 666",
            "468 P.3d 522"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. James Evans",
          "cluster_id": 2802206,
          "cite": [
            "786 F.3d 779",
            "15 Cal. Daily Op. Serv. 4997",
            "2015 U.S. App. LEXIS 8293",
            "2015 WL 2385010"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. William A. Nash, Jr. and David Lewis",
          "cluster_id": 2736697,
          "cite": [
            "100 A.3d 157",
            "2014 D.C. App. LEXIS 393"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Riley v. Cal. United States",
          "cluster_id": 2680439,
          "cite": [
            "189 L. Ed. 2d 430",
            "134 S. Ct. 2473",
            "2014 U.S. LEXIS 4497",
            "82 U.S.L.W. 4558"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Danielle Kelly v. State of Indiana",
          "cluster_id": 2644345,
          "cite": [
            "997 N.E.2d 1045",
            "2013 WL 6122278",
            "2013 Ind. LEXIS 904"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Green",
          "cluster_id": 2487584,
          "cite": [
            "79 So. 3d 1013",
            "2012 La. LEXIS 268",
            "2012 WL 415483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Samuel Cendejas Fernandez v. State",
          "cluster_id": 3130718,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Fernandez v. State",
          "cluster_id": 1748290,
          "cite": [
            "306 S.W.3d 354",
            "2010 Tex. App. LEXIS 1039",
            "2010 WL 520810"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Triston Lee Harris",
          "cluster_id": 1052778,
          "cite": [
            "280 S.W.3d 832",
            "2008 Tenn. Crim. App. LEXIS 112"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Arizona v. Gant",
          "cluster_id": 145887,
          "cite": [
            "173 L. Ed. 2d 485",
            "129 S. Ct. 1710",
            "556 U.S. 332",
            "2009 U.S. LEXIS 3120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
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
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
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
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Johnson",
          "cluster_id": 145912,
          "cite": [
            "172 L. Ed. 2d 694",
            "129 S. Ct. 781",
            "555 U.S. 323",
            "2009 U.S. LEXIS 868"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Birchfield v. N. Dakota. William Robert Bernard",
          "cluster_id": 3216497,
          "cite": [
            "579 U.S. 438",
            "195 L. Ed. 2d 560",
            "2016 U.S. LEXIS 4058",
            "136 S. Ct. 2160"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
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
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
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
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donald Bennett v. City of Eastpointe",
          "cluster_id": 790530,
          "cite": [
            "410 F.3d 810",
            "2005 U.S. App. LEXIS 10587",
            "2005 WL 1384366"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Jay Hill and Malcolm Scott Hill",
          "cluster_id": 766585,
          "cite": [
            "195 F.3d 258",
            "1999 U.S. App. LEXIS 24597",
            "1999 WL 781810"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Menotti v. City of Seattle",
          "cluster_id": 3032002,
          "cite": [
            "409 F.3d 1113",
            "2005 WL 1300994"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Eleuterio Lopez-Moreno, Also Known as Eleuterio Lopez",
          "cluster_id": 791593,
          "cite": [
            "420 F.3d 420",
            "2005 U.S. App. LEXIS 16564",
            "2005 WL 1864257"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dennis Dayton Holt",
          "cluster_id": 774866,
          "cite": [
            "264 F.3d 1215",
            "2001 Colo. J. C.A.R. 4452",
            "2001 U.S. App. LEXIS 19759",
            "2001 WL 1013251"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jones",
          "cluster_id": 2058953,
          "cite": [
            "830 N.E.2d 541",
            "215 Ill. 2d 261",
            "294 Ill. Dec. 129",
            "2005 Ill. LEXIS 632"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "E.W. v. Rosemary Dolgos",
          "cluster_id": 4467174,
          "cite": [
            "884 F.3d 172"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Woods",
          "cluster_id": 5607944,
          "cite": [
            "21 Cal. 4th 668",
            "99 Cal. Daily Op. Serv. 6990",
            "99 Daily Journal DAR 8867",
            "981 P.2d 1019",
            "88 Cal. Rptr. 2d 88",
            "1999 Cal. LEXIS 5534"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jenkins",
          "cluster_id": 1195377,
          "cite": [
            "997 P.2d 13",
            "93 Haw. 87",
            "2000 Haw. LEXIS 97"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
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
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 2087727,
          "cite": [
            "745 A.2d 856",
            "1999 Del. LEXIS 445",
            "1999 WL 1259008"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salazar v. Buono",
          "cluster_id": 145221,
          "cite": [
            "176 L. Ed. 2d 634",
            "130 S. Ct. 1803",
            "559 U.S. 700",
            "2010 U.S. LEXIS 3674"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Floyd v. City of Crystal Springs",
          "cluster_id": 1711298,
          "cite": [
            "749 So. 2d 110",
            "1999 WL 1063627"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramirez v. City of Buena Park",
          "cluster_id": 1227729,
          "cite": [
            "560 F.3d 1012",
            "2009 U.S. App. LEXIS 6394",
            "2009 WL 764568"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Woods",
          "cluster_id": 1160907,
          "cite": [
            "981 P.2d 1019",
            "88 Cal. Rptr. 2d 88",
            "21 Cal. 4th 668"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mitchell v. State",
          "cluster_id": 853407,
          "cite": [
            "745 N.E.2d 775",
            "2001 Ind. LEXIS 300",
            "2001 WL 371941"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118250) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTMyNjE3NjAwMDAwJnM9NzkyNTU2JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118250%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(118250)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjAmcz0yNzc4NzcyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28118250%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118250)",
        "reviewed": 18,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 18,
        "triage_read": 0,
        "triage_snippet_classified": 18
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118250)",
    "indexed_citing_opinions": 490,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118250,
        "count": 490,
        "count_source": "search"
      }
    ],
    "citation_count": 801,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/knowles-v-iowa.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc4NzI1MjImcz03ODU1MzIyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118250%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118250,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 108995,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 118086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 1734862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 1833134,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 1877452,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 2075076,
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
    "date_created": "2026-07-05T10:19:41Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:21:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:21:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:24:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:21:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Knowles v. Iowa

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b298-7">
  CHIEF Justice Rehnquist
 </author>
<p id="A-N9">
  delivered the opinion of the Court.
 </p>
<p id="b298-8">
  An Iowa police officer stopped petitioner Knowles for speeding, but issued him a citation rather than arresting him. The question presented is whether such a procedure authorizes the officer, consistently with the Fourth Amendment, to conduct a foil search of the car. We answer this question "no.”
 </p>
<p id="b298-9">
  Knowles was stopped in Newton, Iowa, after having been clocked driving 43 miles per hour on a road where the speed limit was 25 miles per hour. The police officer issued a citation to Knowles, although under Iowa law he might have arrested him. The officer then conducted a foil search of the car, and under the driver’s seat he found a bag of marijuana and a “pot pipe.” Knowles was then arrested and charged with violation of state laws dealing with controlled substances.
 </p>
<p id="b298-10">
  Before trial, Knowles moved to suppress the evidence so obtained. He argued that the search could not be sustained under the "search incident to arrest” exception recognized in
  <em>
   United States
  </em>
  v.
  <em>
   Robinson,
  </em>
  <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973), because he had not been placed under arrest.. At the hearing on the motion to suppress, the police officer conceded that he had
  <span citation-index="1" class="star-pagination" label="115"> 
   *115
   </span>
  neither Knowles’ consent nor probable cause to conduct the search. He relied on Iowa law dealing with such searches.
 </p>
<p id="b299-5">
  <span class="citation no-link">Iowa Code Ann. § 321.485</span>(l)(a) (West 1997) provides that Iowa peace officers having cause to believe that a person has violated any traffic or motor vehicle equipment law may arrest the person and immediately take the person before a magistrate. Iowa law also authorizes the far more usual practice of issuing a citation in lieu of arrest or in lieu of continued custody after an initial arrest.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  See <span class="citation no-link">Iowa Code Ann. §805.1</span>(1) (West Supp. 1997). Section 805.1(4) provides that the issuance of a citation in lieu of an arrest “does not affect the officer’s authority to conduct an otherwise lawful search.” The Iowa Supreme Court has interpreted this provision as providing authority to officers to conduct a full-blown search of an automobile and driver in those cases where police elect not to make a custodial arrest and instead issue a citation — that is, a search incident to citation. See
  <em>
   State
  </em>
  v.
  <em>
   Meyer,
  </em>
  <span class="citation" data-id="1734862"><a href="/opinion/1734862/state-v-meyer/#879" aria-description="Citation for case: State v. Meyer">543 N. W. 2d 876, 879</a></span> (1996);
  <em>
   State
  </em>
  v.
  <em>
   Becker,
  </em>
  <span class="citation" data-id="2075076"><a href="/opinion/2075076/state-v-becker/#607" aria-description="Citation for case: State v. Becker">458 N. W. 2d 604, 607</a></span> (1990).
 </p>
<p id="b299-6">
  Based on this authority, the trial court denied the motion to suppress and found Knowles guilty. The Supreme Court of Iowa, sitting en bane, affirmed by a divided vote. <span class="citation" data-id="9687529"><a href="/opinion/1833134/state-v-knowles/" aria-description="Citation for case: State v. Knowles">569 N. W. 2d 601</a></span> (1997). Relying on its earlier opinion in
  <em>
   State
  </em>
  v.
  <em>
   Doran,
  </em>
  <span class="citation" data-id="9691123"><a href="/opinion/1877452/state-v-doran/" aria-description="Citation for case: State v. Doran">563 N. W. 2d 620</a></span> (1997), the Iowa Supreme Court upheld the constitutionality of the search under a bright-line “search incident to citation” exception to the Fourth Amendment’s warrant requirement, reasoning that so long as the
  <span citation-index="1" class="star-pagination" label="116"> 
   *116
   </span>
  arresting officer had probable cause to make a custodial arrest, there need not in fact have been a custodial arrest. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./523/1019/">523 U. S. 1019</a></span> (1998), and we now reverse.
 </p>
<p id="b300-5">
  The State contends that Knowles has challenged Iowa Code’s §805.1(4) only “on its face” and not “as applied,” in which case, the argument continues, his challenge would run afoul of
  <em>
   Sibron
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span> (1968). But in his motion to suppress, Knowles argued that “[bjeeause the officer had no probable cause and no search warrant, and the search cannot otherwise be justified under the Fourth Amendment, the search of the car was unconstitutional.” App. 7. Knowles did not argue below, and does not argue here, that the statute could never be lawfully applied. The question we therefore address is whether the search at issue, authorized as it was by state law, nonetheless violates the Fourth Amendment.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
</p>
<p id="b300-6">
  In
  <em>
   <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Robinson, supra,</a></span>
  </em>
  we noted the two historical rationales for the “search incident to arrest” exception: (1) the need to disarm the suspect in order to take him into custody, and (2) the need to preserve evidence for later use at trial. <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#234" aria-description="Citation for case: United States v. Robinson">414 U. S., at 234</a></span>. See also
  <em>
   United States
  </em>
  v.
  <em>
   Edwards,
  </em>
  <span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/#802" aria-description="Citation for case: United States v. Edwards">415 U. S. 800, 802-803</a></span> (1974);
  <em>
   Chimel
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#762" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 762-763</a></span> (1969);
  <em>
   Preston
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964);
  <span citation-index="1" class="star-pagination" label="117"> 
   *117
   </span>
<em>
   Agnello
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span> (1926);
  <em>
   Weeks
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span> (1914). But neither of these underlying rationales for the search incident to arrest exception is sufficient to justify the search in the present case.
 </p>
<p id="b301-5">
  We have recognized that the first rationale — officer safety — is “‘both legitimate and weighty,’”
  <em>
   Maryland
  </em>
  v.
  <em>
   Wilson,
  </em>
  <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#412" aria-description="Citation for case: Maryland v. Wilson">519 U. S. 408, 412</a></span> (1997) (quoting
  <em>
   Pennsylvania
  </em>
  v.
  <em>
   Mimms,
  </em>
  <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#110" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 110</a></span> (1977)
  <em>
   (per curiam)).
  </em>
  The threat to officer safety from issuing a traffic citation, however, is a good deal less than in the ease of a custodial arrest. In
  <em>
   <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Robinson</a></span>,
  </em>
  we stated that a custodial arrest involves “danger to an officer” because of “the extended exposure which follows the taking of a suspect into custody and transporting him to the police station.” <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#234" aria-description="Citation for case: United States v. Robinson">414 U. S., at 234-235</a></span>. We recognized that “[t]he danger to the police officer flows from the faet of the arrest, and its attendant proximity, stress, and uncertainty, and not from the grounds for arrest.”
  <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#234" aria-description="Citation for case: United States v. Robinson"><em>
   Id.,
  </em>
  at 234, n. 5</a></span>. A routine traffic stop, on the other hand,' is a relatively brief encounter and “is more analogous to a so-called
  <em>
   ‘Terry
  </em>
  stop’ . . . than to a formal arrest.”
  <em>
   Berkemer
  </em>
  v.
  <em>
   McCarty,
  </em>
  <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#439" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 439</a></span> (1984). See also
  <em>
   Cupp
  </em>
  v.
  <em>
   Murphy,
  </em>
  <span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/#296" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291, 296</a></span> (1973) (“Where there is no formal arrest... a person might well be less hostile to the police and less likely to take conspicuous, immediate steps to destroy incriminating evidence”).
 </p>
<p id="b301-6">
  This is not to say that the concern for officer safety is absent in the ease of a routine traffic stop. It plainly is not. See
  <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#110" aria-description="Citation for case: Pennsylvania v. Mimms"><em>
   Mimms, supra,
  </em>
  at 110</a></span>;
  <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#413" aria-description="Citation for case: Maryland v. Wilson"><em>
   Wilson, supra,
  </em>
  at 413-414</a></span>. But while the concern for officer safety in this context may justify the “minimal” additional intrusion of ordering a driver and passengers out of the car, it does not by itself justify the often considerably greater intrusion attending a full field-type search. Even without the search authority Iowa urges, officers have other, independent bases to search for weapons and protect themselves from danger. For example, they
  <span citation-index="1" class="star-pagination" label="118"> 
   *118
   </span>
  may order out of a vehicle both the driver,
  <em>
   Mimms, swpra,
  </em>
  at Ill, and any passengers,
  <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#414" aria-description="Citation for case: Maryland v. Wilson"><em>
   Wilson, supra,
  </em>
  at 414</a></span>; perform a “patdown” of a driver and any passengers upon reasonable suspicion that they may be armed and dangerous,
  <em>
   Terry
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968); conduct a
  <em>
   “Terry
  </em>
  patdown” of the passenger compartment of a vehicle upon reasonable suspicion that an occupant is dangerous and may gain immediate control of a weapon,
  <em>
   Michigan
  </em>
  v.
  <em>
   Long,
  </em>
  <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1049" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1049</a></span> (1983); and even conduct a full search of the passenger compartment, including any containers therein, pursuant to a custodial arrest,
  <em>
   New York
  </em>
  v.
  <em>
   Belton,
  </em>
  <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S. 454, 460</a></span> (1981).
 </p>
<p id="b302-5">
  Nor has Iowa shown the second justification for the authority to search incident to arrest — the need to discover and preserve evidence. Once Knowles was stopped for speeding and issued a citation, all the evidence necessary to prosecute that offense had been obtained. No further evidence of excessive speed was going to be found either on the person of the offender or in the passenger compartment of the car.
 </p>
<p id="b302-6">
  Iowa nevertheless argues that a “search incident to citation” is justified because a suspect who is subject to a routine traffic stop may attempt to hide or destroy evidence related to his identity
  <em>
   (e. g.,
  </em>
  a driver’s license or vehicle registration), or destroy evidence of another, as yet undetected crime. As for the destruction of evidence relating to identity, if a police officer is not satisfied with the identification furnished by the driver, this may be a basis for arresting him rather than merely issuing a citation. As for destroying evidence of other crimes, the possibility that an officer would stumble onto evidence wholly unrelated to the speeding offense seems remote.
 </p>
<p id="b302-7">
  In
  <em>
   <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Robinson</a></span>,
  </em>
  we held that the authority to conduct a full field search as incident to an arrest was a “bright-line rule,” which was based on the concern for officer safety and destruction or loss of evidence, but which did not depend in every case upon the existence of either concern. Here we
  <span citation-index="1" class="star-pagination" label="119"> 
   *119
   </span>
  are asked to extend that “bright-line rule” to a situation where the concern for officer safety is not present to the same extent and the concern for destruction or loss of evidence is not present at all. We decline to do so. The judgment of the- Supreme Court of Iowa is reversed, and the cause is remanded for further proceedings not inconsistent with this opinion.
 </p>
<p id="b303-4">
<em>
   It is so ordered.
  </em>
</p>


<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b299-7">
   Iowa law permits the issuance of a citation in lieu of arrest for most offenses for which an accused person would be "eligible for bail.” See <span class="citation no-link">Iowa Code Ann. §805.1</span>(1) (West Supp. 1997). In addition to traffic and motor vehicle equipment violations, this would permit the issuance of a citation in lieu of arrest for such serious felonies as second-degree burglary, §713.5 (West Supp. 1997), and first-degree theft, §714.2(1) (West 1993), both bailable offenses under Iowa law. See §811.1 (West Supp. 1997) (listing all nonbailable offenses). The practice in Iowa of permitting citation in lieu of arrest is consistent with law reform efforts. See 3 W. LaFave, Search and Seizure § 5.2(h), p. 99, and n. 151 (3d ed. 1996).
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b300-7">
   Iowa also contends that Knowles’ challenge is precluded because he failed to seek review of a separate decision of the Iowa Supreme Court, which affirmed his conviction for possession of drug paraphernalia in violation of a city ordinance. That decision, Iowa argues, resulted from the same search at issue here, rejected the same Fourth Amendment challenge Knowles now makes, and, under principles of res judicata, bars his present challenge. Even if Knowles’ failure to seek certiorari review of this decision could preclude his present challenge, Iowa waived this argument by failing to raise it in its brief in opposition to the petition for certiorari. See this Court’s Rule 15.2;
   <em>
    Oklahoma City
   </em>
   v.
   <em>
    Tuttle,
   </em>
   <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#816" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S. 808, 816</a></span> (1985) (“Nonjurisdietional defects of this sort should be brought to our attention
   <em>
    no later
   </em>
   than in respondent’s brief in opposition to the petition for certiorari; if
   <em>
    not,
   </em>
   we consider it within our discretion to deem the defect waived”).
  </p>
</div></div></opinion>
```

---
