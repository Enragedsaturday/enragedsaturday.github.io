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

## GROUP: content/cases/United States v. Edwards.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Edwards"
type: case
citation: "415 U.S. 800 (1974)"
parallel_cite: "94 S. Ct. 1234; 39 L. Ed. 2d 771"
neutral_cite: 1974 U.S. LEXIS 120
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1974
date_decided: 1974-03-26
docket: 73-88
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1974-03-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Edwards
  varies_by_point: false
  scope_note: "Still controlling on the timing of a search incident to arrest: effects subject to search at arrest may be seized at the jail after a reasonable delay."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108995/united-states-v-edwards/"
  cluster_id: 108995
  opinion_id: 108995
  identity_checked: true
homes:
  - page: "[[SIA Persons]]"
    role: "Progeny"
related: ["[[United States v. Robinson]]", "[[Chimel v. California]]", "[[Abel v. United States]]", "[[Illinois v. Lafayette]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "custodial-arrest", "booking"]
holding: "A search incident to arrest may extend in time: clothing and effects in an arrestee's possession that were subject to search at the time of arrest may be seized and examined without a warrant at the jail, even after a substantial, reasonable delay."
lake:
  record_id: United States v. Edwards
  status: verified
  projected_at: 2026-07-06
---

# United States v. Edwards

*415 U.S. 800 (1974)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Edwards was lawfully arrested shortly after 11 p.m. for attempting to break into a post office and was jailed. Investigation at the scene revealed the entry had been pried open, leaving paint chips. The next morning, substitute clothing was purchased for Edwards; his own clothing — worn at and since the arrest, about 10 hours earlier — was then taken and held as evidence. Laboratory examination revealed paint chips matching the window. Edwards objected that the warrantless seizure of his clothing violated the Fourth Amendment.

## Issue
Does the Fourth Amendment bar the warrantless seizure of an arrestee's clothing at the jail roughly 10 hours after his arrest, once the administrative mechanics of arrest are complete and the prisoner is incarcerated?

## Rule
No. Searches and seizures "that could be made on the spot at the time of arrest may legally be conducted later when the accused arrives at the place of detention." — 415 U.S. at 803. ^pin-803

More broadly, "once the accused is lawfully arrested and is in custody, the effects in his possession at the place of detention that were subject to search at the time and place of his arrest may lawfully be searched and seized without a warrant even though a substantial period of time has elapsed between the arrest and subsequent administrative processing . . . and the taking of the property for use as evidence." — *Id.* at 807. ^pin-807

The legal arrest "does — for at least a reasonable time and to a reasonable extent — take [the arrestee's] own privacy out of the realm of protection from police interest in weapons, means of escape, and evidence." — *Id.* at 808–09 (quoting *United States v. DeLeo*). ^pin-808

## Application
Edwards was lawfully arrested, and the police were entitled to seize the clothing in his immediate possession as evidence of the crime; probable cause linked the clothing to the burglary. They could have taken it the night of the arrest, but it was late, no substitute clothing was available, and it would have been unreasonable to strip him and leave him exposed in his cell overnight. Waiting until morning, when substitutes were purchased, was a reasonable delay in effectuating a normal incident of custodial arrest; the lapse of time did not render the warrantless seizure unreasonable.

## Conclusion
The warrantless seizure and examination of Edwards' clothing were valid; the Court of Appeals was reversed. The Court did not hold that the Warrant Clause is never applicable to post-arrest seizures of an arrestee's effects.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Edwards* remains the controlling authority that a [[Search Incident to Arrest|search incident to arrest]] may extend in time — effects subject to search at arrest may be seized and examined at the place of detention after a reasonable delay. It builds on [[United States v. Robinson]] and [[Chimel v. California]] and is paired with station-house cases like [[Illinois v. Lafayette]]. No negative treatment.

## Appears on
- [[SIA Persons]] — *Progeny*

## Sources
- *United States v. Edwards*, 415 U.S. 800 (1974) — https://www.courtlistener.com/opinion/108995/united-states-v-edwards/ — pinpoints: 803, 807, 808–809.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b38a2f1b2bdd4ca0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "415 U.S. 800 (1974)", "court": "U.S. Supreme Court", "neutral_cite": "1974 U.S. LEXIS 120", "official_citation_present": true, "parallel_cite": "94 S. Ct. 1234; 39 L. Ed. 2d 771", "title": "United States v. Edwards", "year": "1974"}}
{"assertion_id": "733944b25a31dbcd", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Persons"}, "payload": {"home": "SIA Persons", "role": "Progeny", "title": "United States v. Edwards"}}
{"assertion_id": "cabd5ab3cdceed97", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A search incident to arrest may extend in time: clothing and effects in an arrestee's possession that were subject to search at the time of arrest may be seized and examined without a warrant at the jail, even after a substantial, reasonable delay.", "title": "United States v. Edwards"}}
{"assertion_id": "87b69847e82142ac", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1974-03-26", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Edwards", "field_i_validity": "good_law", "scope_note": "Still controlling on the timing of a search incident to arrest: effects subject to search at arrest may be seized at the jail after a reasonable delay.", "title": "United States v. Edwards", "varies_by_point": "false"}}
{"assertion_id": "9238c299164286b3", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Edwards"}}
```

### lake record — United States v. Edwards

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Edwards",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Edwards",
    "case_name_short": "Edwards",
    "case_name_full": "UNITED STATES v. EDWARDS Et Al.",
    "input_case_name": "United States v. Edwards",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1974-03-26",
    "year": 1974,
    "docket": "73-88",
    "cluster_id": 108995,
    "lead_opinion_id": 108995,
    "sibling_ids": [
      108995,
      9425658,
      9425659
    ],
    "absolute_url": "/opinion/108995/united-states-v-edwards/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "415 U.S. 800",
      "volume": "415",
      "reporter": "U.S.",
      "page": "800",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "94 S. Ct. 1234",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "1234",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "39 L. Ed. 2d 771",
        "volume": "39",
        "reporter": "L. Ed. 2d",
        "page": "771",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1974 U.S. LEXIS 120",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "120",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "415 U.S. 800",
        "volume": "415",
        "reporter": "U.S.",
        "page": "800",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 S. Ct. 1234",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "1234",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "39 L. Ed. 2d 771",
        "volume": "39",
        "reporter": "L. Ed. 2d",
        "page": "771",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1974 U.S. LEXIS 120",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "120",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "415 U.S. 800",
    "official_selection": {
      "court_class": "scotus",
      "selected": "415 U.S. 800",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-803",
      "page": null,
      "quote": "--- # United States v. Edwards *415 U.S. 800 (1974)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Edwards was lawfully arrested shortly after 11 p.m. for attempting to break into a post office and was jailed. Investigation at the scene revealed the entry had been pried open, leaving paint chips. The next morning, substitute clothing was purchased for Edwards; his own clothing \u2014 worn at and since the arrest, about 10 hours earlier \u2014 was then taken and held as evidence. Laboratory examination revealed paint chips matching the window. Edwards objected that the warrantless seizure of his clothing violated the Fourth Amendment. ## Issue Does the Fourth Amendment bar the warrantless seizure of an arrestee's clothing at the jail roughly 10 hours after his arrest, once the administrative mechanics of arrest are complete and the prisoner is incarcerated? ## Rule No. Searches and seizures",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-807",
      "page": null,
      "quote": "once the accused is lawfully arrested and is in custody, the effects in his possession at the place of detention that were subject to search at the time and place of his arrest may lawfully be searched and seized without a warrant even though a substantial period of time has elapsed between the arrest and subsequent administrative processing . . . and the taking of the property for use as evidence.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-808",
      "page": null,
      "quote": "does \u2014 for at least a reasonable time and to a reasonable extent \u2014 take [the arrestee's] own privacy out of the realm of protection from police interest in weapons, means of escape, and evidence.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1974-03-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Edwards",
    "varies_by_point": false,
    "scope_note": "Still controlling on the timing of a search incident to arrest: effects subject to search at arrest may be seized at the jail after a reasonable delay.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Rosario-Santiago",
          "cluster_id": 4666565,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane1_negative"
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
        "journal_ref": "United States v. Edwards:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Tremblay",
          "cluster_id": 4428704,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Matter of Jamal S.",
          "cluster_id": 2757696,
          "cite": [
            "123 A.D.3d 429",
            "999 N.Y.S.2d 7"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Douglas A. Guilmette v. State of Indiana",
          "cluster_id": 2718767,
          "cite": [
            "14 N.E.3d 38",
            "2014 WL 3953636",
            "2014 Ind. LEXIS 650"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Oles v. State",
          "cluster_id": 1722157,
          "cite": [
            "965 S.W.2d 641",
            "1998 Tex. App. LEXIS 1367",
            "1998 WL 95098"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Contreras v. State",
          "cluster_id": 1747151,
          "cite": [
            "838 S.W.2d 594",
            "1992 WL 142198"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Joyce",
          "cluster_id": 7906322,
          "cite": [
            "30 Conn. App. 164",
            "619 A.2d 872",
            "1993 Conn. App. LEXIS 43"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane1_negative"
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
        "journal_ref": "United States v. Edwards:lane2_top_cited"
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
        "journal_ref": "United States v. Edwards:lane2_top_cited"
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
        "journal_ref": "United States v. Edwards:lane2_top_cited"
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
        "journal_ref": "United States v. Edwards:lane2_top_cited"
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
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Lafayette",
          "cluster_id": 110976,
          "cite": [
            "77 L. Ed. 2d 65",
            "103 S. Ct. 2605",
            "462 U.S. 640",
            "1983 U.S. LEXIS 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Knowles v. Iowa",
          "cluster_id": 118250,
          "cite": [
            "142 L. Ed. 2d 492",
            "119 S. Ct. 484",
            "525 U.S. 113",
            "1998 U.S. LEXIS 8068"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
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
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Bible",
          "cluster_id": 1154894,
          "cite": [
            "858 P.2d 1152",
            "175 Ariz. 549",
            "145 Ariz. Adv. Rep. 3",
            "1993 Ariz. LEXIS 73"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Young v. State",
          "cluster_id": 1860086,
          "cite": [
            "283 S.W.3d 854",
            "2009 Tex. Crim. App. LEXIS 979",
            "2009 WL 1066912"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Johns",
          "cluster_id": 111305,
          "cite": [
            "83 L. Ed. 2d 890",
            "105 S. Ct. 881",
            "469 U.S. 478",
            "1985 U.S. LEXIS 45",
            "53 U.S.L.W. 4126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McGee v. State",
          "cluster_id": 1960022,
          "cite": [
            "105 S.W.3d 609",
            "2003 Tex. Crim. App. LEXIS 75",
            "2003 WL 1918091"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carmine Tramunti",
          "cluster_id": 326798,
          "cite": [
            "513 F.2d 1087"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James N. Gramenos v. Jewel Companies, Inc.",
          "cluster_id": 474259,
          "cite": [
            "797 F.2d 432"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
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
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Caraher",
          "cluster_id": 1188275,
          "cite": [
            "653 P.2d 942",
            "293 Or. 741",
            "1982 Ore. LEXIS 1190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ernest Raymond Basurto",
          "cluster_id": 319510,
          "cite": [
            "497 F.2d 781"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bruce Carneil Webster, A/K/A B-Love",
          "cluster_id": 759707,
          "cite": [
            "162 F.3d 308"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Russell v. State",
          "cluster_id": 1505440,
          "cite": [
            "665 S.W.2d 771",
            "1983 Tex. Crim. App. LEXIS 1111"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marquez v. State",
          "cluster_id": 2391915,
          "cite": [
            "725 S.W.2d 217",
            "1987 Tex. Crim. App. LEXIS 500"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tommie T. Childs",
          "cluster_id": 776249,
          "cite": [
            "277 F.3d 947",
            "2002 U.S. App. LEXIS 760",
            "2002 WL 63798"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hill",
          "cluster_id": 1388061,
          "cite": [
            "528 P.2d 1",
            "12 Cal. 3d 731",
            "117 Cal. Rptr. 393"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Swain v. Spinney",
          "cluster_id": 197434,
          "cite": [
            "117 F.3d 1",
            "1997 WL 339126"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carl Bailey",
          "cluster_id": 410253,
          "cite": [
            "691 F.2d 1009"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Nuccio",
          "cluster_id": 1088486,
          "cite": [
            "454 So. 2d 93"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Edwards:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108995 OR 9425658 OR 9425659) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MDgzMDcyMDAwMDAmcz0xNDQ3MzcyJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108995+OR+9425658+OR+9425659%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108995 OR 9425658 OR 9425659)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzgmcz0xMTg1ODc5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108995+OR+9425658+OR+9425659%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108995 OR 9425658 OR 9425659)",
        "reviewed": 11,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 11,
        "triage_read": 0,
        "triage_snippet_classified": 11
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108995 OR 9425658 OR 9425659)",
    "indexed_citing_opinions": 600,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108995,
        "count": 546,
        "count_source": "search"
      },
      {
        "opinion_id": 9425658,
        "count": 68,
        "count_source": "search"
      },
      {
        "opinion_id": 9425659,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 917,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-edwards.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY0Nzg5Njgmcz00NjY2NTY1JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108995+OR+9425658+OR+9425659%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108995,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 104314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 108288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 237906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 250962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 252159,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 265378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 268259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 271127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 272209,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 272272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 272441,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 272841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 274387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 276677,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 277074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 278241,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 280000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 285514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 285576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 286531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 288700,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 290365,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 301119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108995,
        "cited_id": 308901,
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
    "date_created": "2026-07-05T23:49:51Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:50:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:50:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:53:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:50:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Edwards

```
<div>
<center><b><span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/" aria-description="Citation for case: United States v. Edwards">415 U.S. 800</a></span> (1974)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
EDWARDS ET AL.</h1></center>
<center>No. 73-88.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 15, 1974.</center>
<center>Decided March 26, 1974.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SIXTH CIRCUIT.
<p><span class="star-pagination">*801</span> <i>Edward R. Korman</i> argued the cause for the United States. With him on the brief were <i>Solicitor General Bork, Assistant Attorney General Petersen,</i> and <i>Jerome M. Feit.</i></p>
<p><i>Thomas R. Smith,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1125/">414 U. S. 1125</a></span>, argued the cause and filed a brief for respondents.<sup>[*]</sup></p>
<p>MR. JUSTICE WHITE delivered the opinion of the Court.</p>
<p>The question here is whether the Fourth Amendment should be extended to exclude from evidence certain clothing taken from respondent Edwards while he was in custody at the city jail approximately 10 hours after his arrest.</p>
<p>Shortly after 11 p. m. on May 31, 1970, respondent Edwards was lawfully arrested on the streets of Lebanon, Ohio, and charged with attempting to break into that city's Post Office.<sup>[1]</sup> He was taken to the local jail and placed in a cell. Contemporaneously or shortly thereafter, investigation at the scene revealed that the attempted entry had been made through a wooden window which apparently had been pried up with a pry bar, leaving paint chips on the window sill and wire mesh <span class="star-pagination">*802</span> screen. The next morning, trousers and a T-shirt were purchased for Edwards to substitute for the clothing which he had been wearing at the time of and since his arrest. His clothing was then taken from him and held as evidence. Examination of the clothing revealed paint chips matching the samples that had been taken from the window. This evidence and his clothing were received at trial over Edwards' objection that neither the clothing nor the results of its examination were admissible because the warrantless seizure of his clothing was invalid under the Fourth Amendment.</p>
<p>The Court of Appeals reversed. Expressly disagreeing with two other Courts of Appeals,<sup>[2]</sup> it held that although the arrest was lawful and probable cause existed to believe that paint chips would be discovered on respondent's clothing, the warrantless seizure of the clothing carried out "after the administrative process and the mechanics of the arrest have come to a halt" was nevertheless unconstitutional under the Fourth Amendment. <span class="citation" data-id="308901"><a href="/opinion/308901/united-states-v-eugene-howard-edwards/#1211" aria-description="Citation for case: United States v. Eugene Howard Edwards">474 F. 2d 1206, 1211</a></span> (CA6 1973). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./414/818/">414 U. S. 818</a></span>, and now conclude that the Fourth Amendment should not be extended to invalidate the search and seizure in the circumstances of this case.</p>
<p>The prevailing rule under the Fourth Amendment that searches and seizures may not be made without a warrant is subject to various exceptions. One of them permits warrantless searches incident to custodial arrests, <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973); <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#755" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 755</a></span> (1969); <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span> (1914), and has traditionally been justified by the reasonableness of searching for weapons, instruments of escape, and evidence of crime <span class="star-pagination">*803</span> when a person is taken into official custody and lawfully detained. <i>United States</i> v. <i><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Robinson, supra.</a></span></i><sup></sup>[3]</p>
<p>It is also plain that searches and seizures that could be made on the spot at the time of arrest may legally be conducted later when the accused arrives at the place of detention. If need be, <i>Abel</i> v. <i>United States,</i> <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U. S. 217</a></span> (1960), settled this question. There the defendant was arrested at his hotel, but the belongings taken with him to the place of detention were searched there. In sustaining the search, the Court noted that a valid search of the property could have been made at the place of arrest and perceived little difference</p>
<blockquote>"when the accused decides to take the property with him, for the search of it to occur instead at the first place of detention when the accused arrives there, especially as the search of property carried by an accused to the place of detention has additional justifications, similar to those which justify a search of the person of one who is arrested." <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#239" aria-description="Citation for case: Abel v. United States"><i>Id.,</i> at 239</a></span>.</blockquote>
<p>The courts of appeals have followed this same rule, holding that both the person and the property in his immediate possession may be searched at the station house after the arrest has occurred at another place and if evidence of crime is discovered, it may be seized and admitted in evidence.<sup>[4]</sup> Nor is there any doubt <span class="star-pagination">*804</span> that clothing or other belongings may be seized upon arrival of the accused at the place of detention and later subjected to laboratory analysis or that the test results are admissible at trial.<sup>[5]</sup></p>
<p>Conceding all this, the Court of Appeals in this case nevertheless held that a warrant is required where the search occurs after the administrative mechanics of arrest have been completed and the prisoner is incarcerated. But even on these terms, it seems to us that the normal processes incident to arrest and custody had not been completed when Edwards was placed in his cell on the night of May 31. With or without probable cause, the authorities were entitled at that point not only to search Edwards' clothing but also to take it from him and keep it in official custody. There was testimony that this was the standard practice in this city.<sup>[6]</sup> The police <span class="star-pagination">*805</span> were also entitled to take from Edwards any evidence of the crime in his immediate possession, including his clothing. And the Court of Appeals acknowledged that contemporaneously with or shortly after the time Edwards went to his cell, the police had probable cause to believe that the articles of clothing he wore were themselves material evidence of the crime for which he had been arrested. <span class="citation" data-id="308901"><a href="/opinion/308901/united-states-v-eugene-howard-edwards/#1210" aria-description="Citation for case: United States v. Eugene Howard Edwards">474 F. 2d, at 1210</a></span>. But it was late at night; no substitute clothing was then available for Edwards to wear, and it would certainly have been unreasonable for the police to have stripped respondent of his clothing and left him exposed in his cell throughout the night. Cf. <i>United States</i> v. <i>Caruso,</i> <span class="citation" data-id="271127"><a href="/opinion/271127/united-states-v-ciro-michael-caruso/#185" aria-description="Citation for case: United States v. Ciro Michael Caruso">358 F. 2d 184, 185-186</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./385/862/">385 U. S. 862</a></span> (1966). When the substitutes were purchased the next morning, the clothing he had been wearing at the time of arrest was taken from him and subjected to laboratory analysis. This was no more than taking from respondent the effects in his immediate possession that constituted evidence of crime. This was and is a normal incident of a custodial arrest, and reasonable delay in effectuating it does not change the fact that Edwards was no more imposed upon than he could have been at the time and place of the arrest or immediately upon arrival at the place of detention. The police did no more on June 1 than they were entitled to do incident to the usual custodial arrest and incarceration.</p>
<p><span class="star-pagination">*806</span> Other closely related considerations sustain the examination of the clothing in this case. It must be remembered that on both May 31 and June 1 the police had lawful custody of Edwards and necessarily of the clothing he wore. When it became apparent that the articles of clothing were evidence of the crime for which Edwards was being held, the police were entitled to take, examine, and preserve them for use as evidence, just as they are normally permitted to seize evidence of crime when it is lawfully encountered. <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969); <i>Frazier</i> v. <i>Cupp,</i> <span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731</a></span> (1969); <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967); <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963) (plurality opinion); <i>Zap</i> v. <i>United States,</i> <span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/" aria-description="Citation for case: Zap v. United States">328 U. S. 624</a></span> (1946), vacated on other grounds, <span class="citation multiple-matches"><a href="/c/U.%20S./330/800/">330 U. S. 800</a></span> (1947). Surely, the clothes could have been brushed down and vacuumed while Edwards had them on in the cell, and it was similarly reasonable to take and examine them as the police did, particularly in view of the existence of probable cause linking the clothes to the crime. Indeed, it is difficult to perceive what is unreasonable about the police's examining and holding as evidence those personal effects of the accused that they already have in their lawful custody as the result of a lawful arrest.</p>
<p>In <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span> (1967), an accused had been arrested for a narcotics offense and his automobile impounded preparatory to institution of forfeiture proceedings. The car was searched a week later without a warrant and evidence seized that was later introduced at the defendant's criminal trial. The warrantless search and seizure were sustained because they were "closely related to the reason petitioner was arrested, the reason his car had been impounded, and the reason it was being retained. . . . It would be unreasonable to hold that the police, having to retain the car in their <span class="star-pagination">*807</span> custody for such a length of time, had no right, even for their own protection, to search it." <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California"><i>Id.,</i> at 61-62</a></span>. It was no answer to say that the police could have obtained a search warrant, for the Court held the test to be, not whether it was reasonable to procure a search warrant, but whether the search itself was reasonable, which it was. <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#62" aria-description="Citation for case: Cooper v. California"><i>Id.,</i> at 62</a></span>. <i>United States</i> v. <i><span class="citation" data-id="271127"><a href="/opinion/271127/united-states-v-ciro-michael-caruso/" aria-description="Citation for case: United States v. Ciro Michael Caruso">Caruso, supra</a></span></i><i>,</i> expresses similar views. There, defendant's clothes were not taken until six hours after his arrival at a place of detention. The Court of Appeals properly held that no warrant was required:</p>
<blockquote>"He and his clothes were constantly in custody from the moment of his arrest, and the inspection of his clothes and the holding of them for use in evidence were, under the circumstances, reasonable and proper." <span class="citation" data-id="271127"><a href="/opinion/271127/united-states-v-ciro-michael-caruso/#185" aria-description="Citation for case: United States v. Ciro Michael Caruso">358 F. 2d, at 185</a></span> (citations omitted).</blockquote>
<p><i>Caruso</i> is typical of most cases in the courts of appeals that have long since concluded that once the accused is lawfully arrested and is in custody, the effects in his possession at the place of detention that were subject to search at the time and place of his arrest may lawfully be searched and seized without a warrant even though a substantial period of time has elapsed between the arrest and subsequent administrative processing, on the one hand, and the taking of the property for use as evidence, on the other. This is true where the clothing or effects are immediately seized upon arrival at the jail, held under the defendant's name in the "property room" of the jail, and at a later time searched and taken for use at the subsequent criminal trial.<sup>[7]</sup> The result is the <span class="star-pagination">*808</span> same where the property is not physically taken from the defendant until sometime after his incarceration.<sup>[8]</sup></p>
<p>In upholding this search and seizure, we do not conclude that the Warrant Clause of the Fourth Amendment is never applicable to postarrest seizures of the effects of an arrestee.<sup>[9]</sup> But we do think that the Court of Appeals for the First Circuit captured the essence of situations like this when it said in <i>United States</i> v. <i>DeLeo,</i> <span class="citation" data-id="288700"><a href="/opinion/288700/united-states-v-ralph-f-deleo/#493" aria-description="Citation for case: United States v. Ralph F. Deleo">422 F. 2d 487, 493</a></span> (1970) (footnote omitted):</p>
<blockquote>"While the legal arrest of a person should not destroy the privacy of his premises, it doesfor at <span class="star-pagination">*809</span> least a reasonable time and to a reasonable extent take his own privacy out of the realm of protection from police interest in weapons, means of escape, and evidence."</blockquote>
<p>The judgment of the Court of Appeals is reversed.</p>
<p><i>So ordered.</i></p>
<p>MR. JUSTICE STEWART, with whom MR. JUSTICE DOUGLAS, MR. JUSTICE BRENNAN, and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>The Court says that the question before us "is whether the Fourth Amendment should be extended" to prohibit the warrantless seizure of Edwards' clothing. I think, on the contrary, that the real question in this case is whether the Fourth Amendment is to be ignored. For in my view the judgment of the Court of Appeals can be reversed only by disregarding established Fourth Amendment principles firmly embodied in many previous decisions of this Court.</p>
<p>As the Court has repeatedly emphasized in the past, "the most basic constitutional rule in this area is that `searches conducted outside the judicial process, without prior approval by judge or magistrate, are <i>per se</i> unreasonable under the Fourth Amendmentsubject only to a few specifically established and well-delineated exceptions.' " <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#454" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 454-455</a></span>; <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span>. Since it is conceded here that the seizure of Edwards' clothing was not made pursuant to a warrant, the question becomes whether the Government has met its burden of showing that the circumstances of this seizure brought it within one of the "jealously and carefully drawn"<sup>[1]</sup> exceptions to the warrant requirement.</p>
<p><span class="star-pagination">*810</span> The Court finds a warrant unnecessary in this case because of the custodial arrest of the respondent. It is, of course, well settled that the Fourth Amendment permits a warrantless search or seizure incident to a constitutionally valid custodial arrest. <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span>; <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span>. But the mere fact of an arrest does not allow the police to engage in warrantless searches of unlimited geographic or temporal scope. Rather, the search must be spatially limited to the person of the arrestee and the area within his reach, <i>Chimel</i> v. <i>California, supra</i><i>,</i> and must, as to time, be "substantially contemporaneous with the arrest," <i>Stoner</i> v. <i>California,</i> <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#486" aria-description="Citation for case: Stoner v. California">376 U. S. 483, 486</a></span>; <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367-368</a></span>.</p>
<p>Under the facts of this case, I am unable to agree with the Court's holding that the search was "incident" to Edwards' custodial arrest. The search here occurred fully 10 hours after he was arrested, at a time when the administrative processing and mechanics of arrest had long since come to an end. His clothes were not seized as part of an "inventory" of a prisoner's effects, nor were they taken pursuant to a routine exchange of civilian clothes for jail garb.<sup>[2]</sup> And the considerations that typically justify a warrantless search incident to a lawful arrest were wholly absent here. As Mr. Justice <span class="star-pagination">*811</span> Black stated for a unanimous Court in <i>Preston</i> v. <i>United States, supra,</i> at 367:</p>
<blockquote>"The rule allowing contemporaneous searches is justified, for example, by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the destruction of evidence of the crimethings which might easily happen where the weapon or evidence is on the accused's person or under his immediate control. But these justifications are absent where a search is remote in time or place from the arrest."<sup>[3]</sup></blockquote>
<p>Accordingly, I see no justification for dispensing with the warrant requirement here. The police had ample time to seek a warrant, and no exigent circumstances were present to excuse their failure to do so. Unless the exceptions to the warrant requirement are to be "enthroned into the rule," <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#80" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 80</a></span> (Frankfurter, J., dissenting), this is precisely the sort of situation where the Fourth Amendment requires a magistrate's prior approval for a search.</p>
<p>The Court says that the relevant question is "not whether it was reasonable to procure a search warrant, but whether the search itself was reasonable." <i>Ante,</i> at 807. Precisely such a view, however, was explicitly rejected in <i>Chimel</i> v. <i>California, supra,</i> at 764-765, where the Court characterized the argument as "founded on little more than a subjective view regarding the acceptability of certain sorts of police conduct, and not on considerations relevant to Fourth Amendment interests." As <span class="star-pagination">*812</span> they were in <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>,</i> the words of Mr. Justice Frank-further are again most relevant here:</p>
<blockquote>"To say that the search must be reasonable is to require some criterion of reason. It is no guide at all either for a jury or for district judges or the police to say that an `unreasonable search' is forbidden that the search must be reasonable. What is the test of reason which makes a search reasonable? The test is the reason underlying and expressed by the Fourth Amendment: the history and the experience which it embodies and the safeguards afforded by it against the evils to which it was a response. There must be a warrant to permit search, barring only inherent limitations upon that requirement when there is a good excuse for not getting a search warrant . . . ." <i>United States</i> v. <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#83" aria-description="Citation for case: United States v. Rabinowitz"><i>Rabinowitz, supra,</i> at 83</a></span> (dissenting opinion).</blockquote>
<p>The intrusion here was hardly a shocking one, and it cannot be said that the police acted in bad faith. The Fourth Amendment, however, was not designed to apply only to situations where the intrusion is massive and the violation of privacy shockingly flagrant. Rather, as the Court's classic admonition in <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 635</a></span>, put the matter:</p>
<blockquote>"It may be that it is the obnoxious thing in its mildest and least repulsive form; but illegitimate and unconstitutional practices get their first footing in that way, namely, by silent approaches and slight deviations from legal modes of procedure. This can only be obviated by adhering to the rule that constitutional provisions for the security of person and property should be liberally construed. A close and literal construction deprives them of half their efficacy, and leads to gradual depreciation of the right, <span class="star-pagination">*813</span> as if it consisted more in sound than in substance. It is the duty of courts to be watchful for the constitutional rights of the citizen, and against any stealthy encroachments thereon."</blockquote>
<p>Because I believe that the Court today unjustifiably departs from well-settled constitutional principles, I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]  <i>Frank G. Carrington, Jr., Wayne W. Schmidt, Fred E. Inbau, Glen Murphy, Paul Keller,</i> and <i>Courtney A. Evans</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae</i> urging reversal.</p>
<p>[1]  Edwards (hereafter also referred to as respondent) had an alleged confederate, William T. Livesay, who was corespondent in this case, but died after the petition for certiorari was granted. We therefore vacate the judgment as to him and remand the case to the District Court with directions to dismiss the indictment. <i>Durham</i> v. <i>United States,</i> <span class="citation" data-id="9424482"><a href="/opinion/108288/durham-v-united-states/" aria-description="Citation for case: Durham v. United States">401 U. S. 481</a></span> (1971).</p>
<p>[2]  The Court stated that it could not agree with <i>United States</i> v. <i>Williams,</i> <span class="citation" data-id="286531"><a href="/opinion/286531/united-states-v-leslie-edward-williams-joseph-anthony-butera-and/" aria-description="Citation for case: United States v. Leslie Edward Williams, Joseph Anthony...">416 F. 2d 4</a></span> (CA5 1969), and <i>United States</i> v. <i>Caruso,</i> <span class="citation" data-id="271127"><a href="/opinion/271127/united-states-v-ciro-michael-caruso/" aria-description="Citation for case: United States v. Ciro Michael Caruso">358 F. 2d 184</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./385/862/">385 U. S. 862</a></span> (1966).</p>
<p>[3]  "A custodial arrest of a suspect based on probable cause is a reasonable intrusion under the Fourth Amendment; that intrusion being lawful, a search incident to the arrest requires no additional justification. It is the fact of the lawful arrest which establishes the authority to search, and we hold that in the case of a lawful custodial arrest a full search of the person is not only an exception to the warrant requirement of the Fourth Amendment, but is also a `reasonable' search under that Amendment." <i>United States</i> v. <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#235" aria-description="Citation for case: United States v. Robinson"><i>Robinson, supra,</i> at 235</a></span>.</p>
<p>[4]  <i>United States</i> v. <i>Manar,</i> <span class="citation" data-id="301119"><a href="/opinion/301119/united-states-v-lendon-howard-manar/" aria-description="Citation for case: United States v. Lendon Howard Manar">454 F. 2d 342</a></span> (CA7 1971); <i>United States</i> v. <i>Gonzalez-Perez,</i> <span class="citation" data-id="290365"><a href="/opinion/290365/united-states-v-ricardo-antonio-gonzalez-perez-ana-soria-prieto-antonio/" aria-description="Citation for case: United States v. Ricardo Antonio Gonzalez-Perez, Ana...">426 F. 2d 1283</a></span> (CA5 1970); <i>United States</i> v. <i>DeLeo,</i> <span class="citation" data-id="288700"><a href="/opinion/288700/united-states-v-ralph-f-deleo/" aria-description="Citation for case: United States v. Ralph F. Deleo">422 F. 2d 487</a></span> (CA1 1970); <i>United States</i> v. <i><span class="citation" data-id="286531"><a href="/opinion/286531/united-states-v-leslie-edward-williams-joseph-anthony-butera-and/" aria-description="Citation for case: United States v. Leslie Edward Williams, Joseph Anthony...">Williams, supra</a></span></i><i>; </i><i>United States</i> v. <i>Miles,</i> <span class="citation" data-id="285576"><a href="/opinion/285576/united-states-v-jerry-edgar-miles-wilbert-theodore-vaughn-and-george/" aria-description="Citation for case: United States v. Jerry Edgar Miles, Wilbert Theodore...">413 F. 2d 34</a></span> (CA3 1969); <i>Ray</i> v. <i>United States,</i> <span class="citation" data-id="285514"><a href="/opinion/285514/leroy-herbert-ray-v-united-states/" aria-description="Citation for case: Leroy Herbert Ray v. United States">412 F. 2d 1052</a></span> (CA9 1969); <i>Westover</i> v. <i>United States,</i> <span class="citation" data-id="280000"><a href="/opinion/280000/carl-calvin-westover-v-united-states/" aria-description="Citation for case: Carl Calvin Westover v. United States">394 F. 2d 164</a></span> (CA9 1968); <i>United States</i> v. <i>Frankenberry,</i> <span class="citation" data-id="278241"><a href="/opinion/278241/united-states-v-james-robert-frankenberry-jr/" aria-description="Citation for case: United States v. James Robert Frankenberry, Jr.">387 F. 2d 337</a></span> (CA2 1967); <i>Evalt</i> v. <i>United States,</i> <span class="citation" data-id="277074"><a href="/opinion/277074/anton-vaughn-evalt-v-united-states/" aria-description="Citation for case: Anton Vaughn Evalt v. United States">382 F. 2d 424</a></span> (CA9 1967); <i>Malone</i> v. <i>Crouse,</i> <span class="citation" data-id="276677"><a href="/opinion/276677/dick-malone-v-sherman-h-crouse-warden-kansas-state-penitentiary/" aria-description="Citation for case: Dick Malone v. Sherman H. Crouse, Warden, Kansas State...">380 F. 2d 741</a></span> (CA10 1967); <i>Cotton</i> v. <i>United States,</i> <span class="citation" data-id="274387"><a href="/opinion/274387/gary-leland-cotton-v-united-states/" aria-description="Citation for case: Gary Leland Cotton v. United States">371 F. 2d 385</a></span> (CA9 1967); <i>Miller</i> v. <i>Eklund,</i> <span class="citation" data-id="272841"><a href="/opinion/272841/glenn-roy-miller-v-r-l-eklund-etc/" aria-description="Citation for case: Glenn Roy Miller v. R. L. Eklund, Etc.">364 F. 2d 976</a></span> (CA9 1966); <i>Hancock</i> v. <i>Nelson,</i> <span class="citation" data-id="9451942"><a href="/opinion/272441/parker-l-hancock-warden-v-russell-nelson/" aria-description="Citation for case: Parker L. Hancock, Warden v. Russell Nelson">363 F. 2d 249</a></span> (CA1 1966); <i>Golliher</i> v. <i>United States,</i> <span class="citation" data-id="272272"><a href="/opinion/272272/richard-lee-golliher-v-united-states-of-america-harry-richard-holmes-v/" aria-description="Citation for case: Richard Lee Golliher v. United States of America, Harry...">362 F. 2d 594</a></span> (CA8 1966); <i>Rodgers</i> v. <i>United States,</i> <span class="citation" data-id="272209"><a href="/opinion/272209/john-wesley-rodgers-v-united-states/" aria-description="Citation for case: John Wesley Rodgers v. United States">362 F. 2d 358</a></span> (CA8), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./385/993/">385 U. S. 993</a></span> (1966); <i>United States</i> v. <i><span class="citation" data-id="271127"><a href="/opinion/271127/united-states-v-ciro-michael-caruso/" aria-description="Citation for case: United States v. Ciro Michael Caruso">Caruso, supra</a></span></i><i>; </i><i>Whalem</i> v. <i>United States,</i> 120 U. S. App. D. C. 331, <span class="citation" data-id="9450802"><a href="/opinion/268259/thomas-w-whalem-v-united-states/" aria-description="Citation for case: Thomas W. Whalem v. United States">346 F. 2d 812</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./382/862/">382 U. S. 862</a></span> (1965); <i>Grillo</i> v. <i>United States,</i> <span class="citation" data-id="265378"><a href="/opinion/265378/henry-grillo-v-united-states-of-america-saul-glassman-v-united-states-of/" aria-description="Citation for case: Henry Grillo v. United States of America, Saul Glassman...">336 F. 2d 211</a></span> (CA1 1964), cert. denied <i>sub nom. </i><i>Gorin</i> v. <i>United States,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./379/971/">379 U. S. 971</a></span> (1965); <i>Robinson</i> v. <i>United States,</i> 109 U. S. App. D. C. 22, <span class="citation" data-id="252159"><a href="/opinion/252159/james-w-robinson-v-united-states-of-america-thomas-f-dawson-v-united/" aria-description="Citation for case: James W. Robinson v. United States of America, Thomas F....">283 F. 2d 508</a></span> (1960); <i>Baskerville</i> v. <i>United States,</i> <span class="citation" data-id="237906"><a href="/opinion/237906/drury-reinhardt-baskerville-v-united-states/" aria-description="Citation for case: Drury Reinhardt Baskerville v. United States">227 F. 2d 454</a></span> (CA10 1955).</p>
<p>[5]  See, <i>e. g., </i><i>United States</i> v. <i><span class="citation" data-id="271127"><a href="/opinion/271127/united-states-v-ciro-michael-caruso/" aria-description="Citation for case: United States v. Ciro Michael Caruso">Caruso, supra</a></span></i><i>; </i><i>United States</i> v. <i>Williams, supra</i><i>; </i><i>Golliher</i> v. <i>United States, supra</i><i>; </i><i>Whalem</i> v. <i>United States, supra</i><i>; </i><i>Robinson</i> v. <i>United States, supra</i><i>; </i><i>Evalt</i> v. <i>United States, supra</i><i>; </i><i>Hancock</i> v. <i><span class="citation" data-id="9451942"><a href="/opinion/272441/parker-l-hancock-warden-v-russell-nelson/" aria-description="Citation for case: Parker L. Hancock, Warden v. Russell Nelson">Nelson, supra</a></span></i><i>.</i></p>
<p>[6]  App. 6. Historical evidence points to the established and routine custom of permitting a jailer to search the person who is being processed for confinement under his custody and control. See, <i>e. g.,</i> T. Gardner &amp; V. Manian, Principles and Cases of the Law of Arrest, Search, and Seizure 200 (1974); E. Fisher, Search and Seizure 71 (1970). While "[a] rule of practice must not be allowed . . . to prevail over a constitutional right," <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#313" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 313</a></span> (1921), little doubt has ever been expressed about the validity or reasonableness of such searches incident to incarceration. T. Taylor, Two Studies in Constitutional Interpretation 50 (1969).</p>
<p>[7]  See <i>Evalt</i> v. <i>United States,</i> <span class="citation" data-id="277074"><a href="/opinion/277074/anton-vaughn-evalt-v-united-states/" aria-description="Citation for case: Anton Vaughn Evalt v. United States">382 F. 2d 424</a></span> (CA9 1967); <i>Westover</i> v. <i>United States,</i> <span class="citation" data-id="280000"><a href="/opinion/280000/carl-calvin-westover-v-united-states/" aria-description="Citation for case: Carl Calvin Westover v. United States">394 F. 2d 164</a></span> (CA9 1968); <i>Baskerville</i> v. <i>United States,</i> <span class="citation" data-id="237906"><a href="/opinion/237906/drury-reinhardt-baskerville-v-united-states/" aria-description="Citation for case: Drury Reinhardt Baskerville v. United States">227 F. 2d 454</a></span> (CA10 1955). In <i><span class="citation" data-id="237906"><a href="/opinion/237906/drury-reinhardt-baskerville-v-united-states/" aria-description="Citation for case: Drury Reinhardt Baskerville v. United States">Baskerville</a></span>,</i> the effects were taken for safekeeping on December 23 but re-examined and taken as evidence on January 6. <i>Brett</i> v. <i>United States,</i> <span class="citation" data-id="9454652"><a href="/opinion/285354/robert-brett-v-united-states/" aria-description="Citation for case: Robert Brett v. United States">412 F. 2d 401</a></span> (CA5 1969), is <i>contra.</i> There the defendant's clothes were taken from him shortly after arrival at the jail, as was the custom, and held in the property room of the jail. Three days later the clothing was searched and incriminating evidence found. A divided panel of the Court of Appeals held the evidence inadmissible for want of a warrant authorizing the search.</p>
<p>[8]  <i>Hancock</i> v. <i>Nelson,</i> <span class="citation" data-id="9451942"><a href="/opinion/272441/parker-l-hancock-warden-v-russell-nelson/" aria-description="Citation for case: Parker L. Hancock, Warden v. Russell Nelson">363 F. 2d 249</a></span> (CA1 1966); <i>Malone</i> v. <i>Crouse,</i> <span class="citation" data-id="276677"><a href="/opinion/276677/dick-malone-v-sherman-h-crouse-warden-kansas-state-penitentiary/" aria-description="Citation for case: Dick Malone v. Sherman H. Crouse, Warden, Kansas State...">380 F. 2d 741</a></span> (CA10 1967); <i>United States</i> v. <i>Caruso,</i> <span class="citation" data-id="271127"><a href="/opinion/271127/united-states-v-ciro-michael-caruso/" aria-description="Citation for case: United States v. Ciro Michael Caruso">358 F. 2d 184</a></span> (CA2 1966). In <i><span class="citation" data-id="9451942"><a href="/opinion/272441/parker-l-hancock-warden-v-russell-nelson/" aria-description="Citation for case: Parker L. Hancock, Warden v. Russell Nelson">Hancock</a></span>,</i> the defendant was first taken into custody at 12:51 a. m. His clothes were taken at 2 p. m. on the same day, two hours after probable cause to do so eventuated.</p>
<p>[9]  Holding the Warrant Clause inapplicable in the circumstances present here does not leave law enforcement officials subject to no restraints. This type of police conduct "must [still] be tested by the Fourth Amendment's general proscription against unreasonable searches and seizures." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20</a></span> (1968). But the Court of Appeals here conceded that probable cause existed for the search and seizure of respondent's clothing, and respondent complains only that a warrant should have been secured. We thus have no occasion to express a view concerning those circumstances surrounding custodial searches incident to incarceration which might "violate the dictates of reason either because of their number or their manner of perpetration." <i>Charles</i> v. <i>United States,</i> <span class="citation" data-id="250962"><a href="/opinion/250962/james-d-charles-v-united-states/#389" aria-description="Citation for case: James D. Charles v. United States">278 F. 2d 386, 389</a></span> (CA9), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./364/831/">364 U. S. 831</a></span> (1960). Cf. <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966); <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952).</p>
<p>[1]  <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499</a></span>.</p>
<p>[2]  The Government conceded at oral argument that the seizure of the respondent's clothing was not a matter of routine jail procedure, but was undertaken solely for the purpose of searching for the incriminating paint chips.
</p>
<p>No contention is made that the warrantless seizure of the clothes was necessitated by the exigencies of maintaining discipline or security within the jail system. There is thus no occasion to consider the legitimacy of warrantless searches or seizures in a penal institution based upon that quite different rationale.</p>
<p>[3]  No claim is made that the police feared that Edwards either possessed a weapon or was planning to destroy the paint chips on his clothing. Indeed, the Government has not even suggested that he was aware of the presence of the paint chips on his clothing.</p>

</div>
```

---

## GROUP: content/cases/United States v. Evans.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Evans"
type: case
citation: "937 F.2d 1534 (1991)"
parallel_cite: ""
neutral_cite: "1991 U.S. App. LEXIS 14383; 1991 WL 118519"
court: "U.S. Court of Appeals, Tenth Circuit"
court_level: coa
circuit: 10th
year: 1991
date_decided: 1991-07-08
docket: 90-6234
authority_weight: "Binding in-circuit — 10th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 1991-07-08
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Evans
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/564407/united-states-v-daryl-lee-evans/"
  cluster_id: 564407
  opinion_id: 564407
  identity_checked: true
homes:
  - page: "[[Inventory Searches]]"
    role: "Recent development (role-based)"
related: ["[[Florida v. Wells]]", "[[Colorado v. Bertine]]", "[[Illinois v. Lafayette]]", "[[South Dakota v. Opperman]]", "[[Nix v. Williams]]"]
aliases: ["United States v. Evans (10th Cir. 1991)", "United States v. Daryl Lee Evans"]
tags: ["case", "fourth-amendment", "inventory-search", "search-incident-to-arrest", "standardized-criteria", "tenth-circuit"]
holding: "UPHELD an inventory search of a carry-on bag (cocaine found in a container) conducted at a bus station: the officer followed the…"
lake:
  record_id: United States v. Evans
  status: verified
  projected_at: 2026-07-06
---

# United States v. Evans

*937 F.2d 1534 (10th Cir. 1991)* · U.S. Court of Appeals, Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Oklahoma City detectives working a drug-interdiction detail at the Union Bus Station approached Daryl Lee Evans after he disembarked from a Los Angeles bus acting nervously. After consent issues with his carry-on bag and a consented pat-down that produced a lump Evans called "weed," he was arrested. Pursuant to department policy, Sergeant Ring pried open the bag's zipper to inventory it before booking and found a taped bundle packaged like the cocaine kilos he had seized before. The search stopped when Evans asked them to get a warrant; warrants were obtained and the bundles tested positive for cocaine.

## Issue
Whether the warrantless opening of an arrestee's locked carry-on bag at the arrest scene, conducted under a written department inventory policy, was a lawful inventory search rather than a ruse for investigatory rummaging.

## Rule
An inventory search conducted pursuant to standardized department procedures, and not as a ruse for general investigatory rummaging, is a lawful exception to the warrant requirement. The Tenth Circuit held: "we hold the search conducted at the bus station of the carry-on bag was a lawful inventory search, and the evidence discovered subsequently (pursuant to valid search warrants) was not the fruit of an illegality, but was lawfully obtained." — 937 F.2d at 1539. ^pin-1539

The validity turns on adherence to a governing policy rather than the officer's location: "Section 239.29 of the Oklahoma City Police Department policy does not require officers to conduct their inventory at a particular place." — *Id.* The court read [[Florida v. Wells]] as cautioning only "against inventory searches being used as a ruse for investigatory purposes," and distinguished it because *[[Florida v. Wells|Wells]]* "dealt with the specific problem of the absence of a department policy or standardized criteria governing such searches." — *Id.* ^pin-1539a

## Application
On these facts the search satisfied the inventory exception. A written policy (Section 239.29) directed that locked containers "must be opened and the contents inventoried before booking," and the court found no probable cause to believe contraband was inside when Sergeant Ring first opened the bag, so the policy's competing "obtain a warrant" directive was not triggered. Conducting the inventory at the bus station rather than the station house did not invalidate it, because the policy did not fix a location; and the officer's failure to take notes and his cessation of the search after the first bundle did not show a ruse, given that he was "at the very outset of the inventory" and stopped out of caution when Evans demanded a warrant. Because Sergeant Ring adhered to the standardized procedure and there was no evidence he intended any purpose other than inventory, the search was lawful and the later warranted openings were not fruit of an illegality.

## Conclusion
The bus-station opening of the carry-on bag was a valid inventory search; the denial of the motion to suppress was affirmed. The court did not reach the district court's alternative inevitable-discovery ground.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 10th Cir.**
- No negative subsequent treatment identified. The decision applies the SCOTUS inventory-search line — [[South Dakota v. Opperman]], [[Illinois v. Lafayette]], [[Colorado v. Bertine]], and [[Florida v. Wells]] — to a locked carry-on bag opened under standardized policy.

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Evans*, 937 F.2d 1534 (10th Cir. 1991) — https://www.courtlistener.com/opinion/564407/united-states-v-daryl-lee-evans/ — pinpoint: 1539.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "35ec817790ad6875", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "937 F.2d 1534 (1991)", "court": "U.S. Court of Appeals, Tenth Circuit", "neutral_cite": "1991 U.S. App. LEXIS 14383; 1991 WL 118519", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Evans", "year": "1991"}}
{"assertion_id": "76de6fcee1e5f2e9", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "UPHELD an inventory search of a carry-on bag (cocaine found in a container) conducted at a bus station: the officer followed the…", "title": "United States v. Evans"}}
{"assertion_id": "ebf34716152f87fe", "dimension": "support", "kind": "home_role", "locator": {"home": "Inventory Searches"}, "payload": {"home": "Inventory Searches", "role": "Recent development (role-based)", "title": "United States v. Evans"}}
{"assertion_id": "12320b4ecd204cbc", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1991-07-08", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Evans", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Evans", "varies_by_point": "false"}}
{"assertion_id": "b37bbf9ab36be2ed", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 10th Cir.", "title": "United States v. Evans"}}
```

### lake record — United States v. Evans

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Evans",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Daryl Lee Evans",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Daryl Lee EVANS, Defendant-Appellant",
    "input_case_name": "United States v. Evans",
    "court": "U.S. Court of Appeals, Tenth Circuit",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "10th",
    "state": null,
    "date_decided": "1991-07-08",
    "year": 1991,
    "docket": "90-6234",
    "cluster_id": 564407,
    "lead_opinion_id": 564407,
    "sibling_ids": [
      564407
    ],
    "absolute_url": "/opinion/564407/united-states-v-daryl-lee-evans/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "937 F.2d 1534",
      "volume": "937",
      "reporter": "F.2d",
      "page": "1534",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "1991 U.S. App. LEXIS 14383",
        "volume": "1991",
        "reporter": "U.S. App. LEXIS",
        "page": "14383",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 WL 118519",
        "volume": "1991",
        "reporter": "WL",
        "page": "118519",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "937 F.2d 1534",
        "volume": "937",
        "reporter": "F.2d",
        "page": "1534",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 U.S. App. LEXIS 14383",
        "volume": "1991",
        "reporter": "U.S. App. LEXIS",
        "page": "14383",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 WL 118519",
        "volume": "1991",
        "reporter": "WL",
        "page": "118519",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "937 F.2d 1534",
    "official_selection": {
      "court_class": "coa",
      "selected": "937 F.2d 1534",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1539",
      "page": null,
      "quote": "he was arrested. Pursuant to department policy, Sergeant Ring pried open the bag's zipper to inventory it before booking and found a taped bundle packaged like the cocaine kilos he had seized before. The search stopped when Evans asked them to get a warrant; warrants were obtained and the bundles tested positive for cocaine. ## Issue Whether the warrantless opening of an arrestee's locked carry-on bag at the arrest scene, conducted under a written department inventory policy, was a lawful inventory search rather than a ruse for investigatory rummaging. ## Rule An inventory search conducted pursuant to standardized department procedures, and not as a ruse for general investigatory rummaging, is a lawful exception to the warrant requirement. The Tenth Circuit held:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1539a",
      "page": null,
      "quote": "Section 239.29 of the Oklahoma City Police Department policy does not require officers to conduct their inventory at a particular place.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1991-07-08",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Evans",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Hansen",
          "cluster_id": 2630631,
          "cite": [
            "2002 UT 125",
            "63 P.3d 650",
            "463 Utah Adv. Rep. 5",
            "2002 Utah LEXIS 215",
            "2002 WL 31845283"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Steven Curtis Waupekenay",
          "cluster_id": 590024,
          "cite": [
            "973 F.2d 1533",
            "1992 U.S. App. LEXIS 20488",
            "1992 WL 207624"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKinstrey",
          "cluster_id": 1372825,
          "cite": [
            "852 P.2d 467",
            "17 Brief Times Rptr. 893",
            "1993 Colo. LEXIS 470",
            "1993 WL 189812"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re JM",
          "cluster_id": 2264984,
          "cite": [
            "619 A.2d 497",
            "1992 D.C. App. LEXIS 348",
            "1992 WL 387505"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Oscar Arzaga",
          "cluster_id": 656678,
          "cite": [
            "9 F.3d 91",
            "1993 U.S. App. LEXIS 29057",
            "1993 WL 461577"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Morales",
          "cluster_id": 2604608,
          "cite": [
            "935 P.2d 936",
            "1997 Colo. LEXIS 166",
            "1997 WL 86035"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Welch",
          "cluster_id": 1209950,
          "cite": [
            "873 P.2d 601",
            "1994 Wyo. LEXIS 56",
            "1994 WL 147907"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. T.H.",
          "cluster_id": 1163445,
          "cite": [
            "892 P.2d 301",
            "19 Brief Times Rptr. 452",
            "1995 Colo. LEXIS 51",
            "1995 WL 117069"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilcher v. City of Wilmington",
          "cluster_id": 1471789,
          "cite": [
            "924 F. Supp. 613",
            "1996 U.S. Dist. LEXIS 5970",
            "1996 WL 224204"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jim",
          "cluster_id": 10702082,
          "cite": [
            "508 P.3d 937"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Little",
          "cluster_id": 2081478,
          "cite": [
            "862 F. Supp. 334",
            "1994 U.S. Dist. LEXIS 12833",
            "1994 WL 487950"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Woodard",
          "cluster_id": 1466244,
          "cite": [
            "873 F. Supp. 535",
            "1994 U.S. Dist. LEXIS 18705",
            "1994 WL 723964"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Manuel",
          "cluster_id": 1503195,
          "cite": [
            "791 F. Supp. 265",
            "1992 U.S. Dist. LEXIS 6844",
            "1992 WL 94094"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Armijo",
          "cluster_id": 1411372,
          "cite": [
            "781 F. Supp. 1551",
            "1991 U.S. Dist. LEXIS 19017",
            "1991 WL 285732"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hanks",
          "cluster_id": 1510418,
          "cite": [
            "821 F. Supp. 1425",
            "1993 U.S. Dist. LEXIS 7541",
            "1993 WL 185573"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Baker",
          "cluster_id": 4398905,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cruz-Mendez",
          "cluster_id": 168346,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Evans:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(564407) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca10)",
        "reviewed": 1,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 1,
        "triage_read": 0,
        "triage_snippet_classified": 1
      },
      "lane2_top_cited": {
        "query": "cites:(564407)",
        "reviewed": 18,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 17,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(564407)",
        "reviewed": 0,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 0,
        "triage_read": 0,
        "triage_snippet_classified": 0
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(564407)",
    "indexed_citing_opinions": 18,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 564407,
        "count": 18,
        "count_source": "search"
      }
    ],
    "citation_count": 50,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-evans.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 18,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 564407,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 564407,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 564407,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 564407,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 564407,
        "cited_id": 112412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 564407,
        "cited_id": 112631,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "RU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T23:53:39Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:53:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:53:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:56:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:53:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Evans

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b1635-26">
  BRORBY, Circuit Judge.
 </author>
<p id="b1635-27">
  This appeal arises from the district court’s denial of Defendant Daryl Lee Evans’s, motion to suppress evidence. Defendant states the issues presented for review as follows: “Whether the district court erred in denying appellant’s motion to suppress evidence seized pursuant to an un
  <span citation-index="1" class="star-pagination" label="1536"> 
   *1536
   </span>
  lawful employment of a drug courier profile and unlawful
  <em>
   Terry
  </em>
  investigation;” and “[w]hether the district court erred when it denied appellant’s motion to suppress evidence seized pursuant to an unlawful search of the carry-on luggage without a search warrant.” We affirm.
 </p>
<p id="b1636-4">
  I.
 </p>
<p id="b1636-5">
  On April 25, 1990, Detective Sergeants Gary Eastridge and Glenn Ring of the Oklahoma City Police Department were working at the Union Bus Station in Oklahoma City as part of an interdiction program to detect and deter the arrival of drugs into the area. At approximately 2:00 p.m. that day, the officers observed a bus, which had originated in Los Angeles, arrive at the station and its passengers disembark. Among the passengers observed by the officers was Daryl Lee Evans. Mr. Evans was carrying a gray, soft sided bag. As Mr. Evans proceeded through the terminal, the officers noticed him scanning the area and acting in a very nervous manner. Mr. Evans then placed the gray bag he was carrying between his feet as he watched the luggage being unloaded from the bus.
 </p>
<p id="b1636-6">
  Based on these observations and Sergeant Ring’s experience and training in detecting drug couriers, the officers approached Mr. Evans, identifying themselves as narcotics officers, asked Mr. Evans for identification, and explained their reason for speaking with him.
 </p>
<p id="b1636-7">
  Mr. Evans produced his identification while the conversation ensued but became increasingly nervous. Sergeant Ring then asked if Mr. Evans would allow the officers to search his carry-on bag. Mr. Evans told the officers he did not have the keys to the bag but subsequently produced two claim tags for other luggage that he claimed contained the keys. Mr. Evans gave the tags to Sergeant Eastridge, who attempted, but was unable, to locate the other luggage. The officers continued their conversation with Mr. Evans. Sergeant Ring stated he thought it was unusual that Mr. Evans did not have the keys to the bag on his person, whereupon Sergeant Ring asked Mr. Evans if he could pat him down to try and find the keys, and Mr. Evans consented. Both officers then proceeded to pat down Mr. Evans, and Sergeant Eas-tridge discovered a lump near the calf of Mr. Evans’s leg. When Sergeant Eas-tridge inquired about the lump, Mr. Evans responded that it was “weed.”
 </p>
<p id="b1636-9">
  Following this, Mr. Evans was advised he was under arrest and was taken to an interior office at the bus station. Sergeant Ring then informed Mr. Evans that due to his arrest his carry-on bag would be inventoried before submitting it to the Oklahoma City property room according to department policy. Sergeant Ring then pried open a zipper on the bag and removed from the compartment a taped plastic bundle. Sergeant Ring noticed the bundle was sealed and packaged like kilograms of cocaine he had seized in the past. Sergeant Ring then asked Mr. Evans if there were any additional narcotics, and Mr. Evans said there were two other packages similar to the one already discovered. Sergeant Ring then asked Mr. Evans if he would consent to the officers opening the taped bundle. At this point, Mr. Evans advised that he wanted the search to cease until the officers obtained a search warrant, and the search ceased.
 </p>
<p id="b1636-10">
  Mr. Evans was then transported to the police station, and Sergeant Ring and Sergeant Eastridge sought and secured two search warrants — one for the taped bundle, and one for the other compartment of the bag. After obtaining these warrants, all three bundles were opened. The contents tested positive for the substance cocaine hydrochloride.
 </p>
<p id="b1636-11">
  II.
 </p>
<p id="b1636-12">
  In reviewing the denial of a defendant’s motion to suppress evidence, we accept the trial court’s findings of fact, unless clearly erroneous, and consider all the evidence in a light most favorable to the Government.
  <em>
   United States v. McAlpine,
  </em>
  <span class="citation" data-id="552251"><a href="/opinion/552251/united-states-v-william-james-mcalpine/#1463" aria-description="Citation for case: United States v. William James McAlpine">919 F.2d 1461, 1463</a></span> (10th Cir.1990). However, ultimate determinations of reasonableness under the Fourth Amendment, and other questions of law, are reviewed de
  <span citation-index="1" class="star-pagination" label="1537"> 
   *1537
   </span>
  novo.
  <em>
   United States v. Butler,
  </em>
  <span class="citation" data-id="9480414"><a href="/opinion/542920/united-states-v-ricky-e-butler/#1484" aria-description="Citation for case: United States v. Ricky E. Butler">904 F.2d 1482, 1484</a></span> (10th Cir.1990).
 </p>
<p id="b1637-4">
  Mr. Evans first contends his Fourth Amendment rights were violated when the officers at the Union Bus Station approached him based on a drug courier profile. Before addressing the lawfulness of using a drug courier profile, we must determine whether any Fourth Amendment protection is due Mr. Evans under these circumstances. This court has previously identified three categories of encounters between police and citizens, each representing different levels of Fourth Amendment entitlement. We described these categories as follows:
 </p>
<blockquote id="b1637-5">
  The first is referred to as a police-citizen encounter and is characterized by the voluntary cooperation of a citizen in response to non-coercive questioning. This has been held to raise no constitutional issues because this type of contract [sic] is not a seizure within the meaning of the Fourth Amendment....
 </blockquote>
<blockquote id="b1637-6">
  The second type of encounter is the Terry-type of stop. The standards here are set forth in
  <em>
   Terry v. Ohio,
  </em>
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span> (1968). Most courts characterize this as a “brief, non-intrusive detention during a frisk for weapons or preliminary questioning * * This is considered a.seizure of the person within the meaning of the Fourth Amendment, but need not be supported by probable cause. In order to justify an investigatory stop, the officer need have only “specific and articulable facts sufficient to give rise to reasonable suspicion that a person has committed or is committing a crime.”
 </blockquote>
<blockquote id="b1637-7">
  The final category is an arrest which is characterized by highly intrusive or lengthy search or detention. An arrest is justified only when there is probable cause to believe that a person has committed or is committing a crime.
 </blockquote>
<p id="b1637-8">
<em>
   United States v. Cooper,
  </em>
  <span class="citation" data-id="9472135"><a href="/opinion/435289/united-states-v-vanessa-elaine-cooper-and-darryl-keith-threat/#1363" aria-description="Citation for case: United States v. Vanessa Elaine Cooper, and Darryl Keith...">733 F.2d 1360, 1363</a></span> (10th Cir.) (citations omitted),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./467/1255/">467 U.S. 1255</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./104/3543/">104 S.Ct. 3543</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/82/847/">82 L.Ed.2d 847</a></span> (1984).
 </p>
<p id="b1637-11">
  In the present case, the district court found the initial questioning of Mr. Evans prior to the pat down fell within the first category of police/citizen encounters, rendering any Fourth Amendment claims unwarranted.
  <em>
   See id.
  </em>
  Merely approaching an individual in a public place and asking questions of the individual, including asking to examine the person’s identification or requesting the person’s consent to search his or her luggage is not a seizure implicating the Fourth Amendment.
  <em>
   Florida v. Bostick,
  </em>
  — U.S. --, -, <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#2386" aria-description="Citation for case: Florida v. Bostick">111 S.Ct. 2382, 2386</a></span>, <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">115 L.Ed.2d 389</a></span> (1991). As long as the police have not, by means of physical force or show of authority, in some way restrained the liberty of the citizen, such a consensual encounter will not constitute a seizure for purposes of the Fourth Amendment.
  <em>
   <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Id.</a></span>
  </em>
  at- — -, <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#2386" aria-description="Citation for case: Florida v. Bostick">111 S.Ct. at 2386</a></span>. The district court found, inter alia: “the encounter was a cooperative one”; “[t]he defendant was engaged in conversations ... [and] was approached in a friendly conversational manner”; and “[t]here were no threats made to the defendant ... [nor] promises ... given.” Our review of the record reveals these findings are fully supported and not clearly erroneous. Therefore, no Fourth Amendment concerns were implicated during this initial non-coercive questioning.
 </p>
<p id="b1637-15">
  The pat down of Mr. Evans, as it involved more than mere cooperative questioning, is entitled to Fourth Amendment scrutiny. In regard to the pat down, the district court made the following findings: “that this pat down was consented to by the defendant”; “that the consent was not limited to Detective Ring”; “that it was not limited to the pockets only”; and that “defendant was well aware of these two officers” and “[t]he fact that the defendant was looking at Officer Ring when this consent was made does not serve to limit the consent.”
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  Consent to search is valid if given voluntarily.
  <em>
   Schneckloth v. Busta
  </em>
<span citation-index="1" class="star-pagination" label="1538"> 
   *1538
   </span>
<em>
   monte,
  </em>
  <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#222" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218, 222-23</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#2045" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041, 2045-46</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">36 L.Ed.2d 854</a></span> (1973). The volun-tariness of consent is a question of fact to be determined from the totality of all the circumstances.
  <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#227" aria-description="Citation for case: Schneckloth v. Bustamonte"><em>
   Id.
  </em>
  at 227</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#2047" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. at 2047</a></span>. We have previously set forth the following three-tiered analysis to be used in determining whether consent was voluntary:
 </p>
<blockquote id="Ajsn">
  First, there must be clear and positive testimony that the consent was unequivocal and specific, and freely and intelligently given. Second, the Government must establish that consent was given without duress or coercion. Finally, we evaluate the first two standards with the traditional indulgence of the courts against a presumption of waiver of constitutional rights.
 </blockquote>
<p id="b1638-4">
<em>
   United States v. Corral,
  </em>
  <span class="citation" data-id="538919"><a href="/opinion/538919/united-states-v-silverio-corral-united-states-of-america-v-jesus-valdez/#994" aria-description="Citation for case: United States v. Silverio Corral, United States of...">899 F.2d 991, 994</a></span> (10th Cir.1990) (quoting
  <em>
   United States v. Recalde,
  </em>
  <span class="citation" data-id="451967"><a href="/opinion/451967/united-states-v-miguel-angel-recalde/#1453" aria-description="Citation for case: United States v. Miguel Angel Recalde">761 F.2d 1448, 1453</a></span> (10th Cir.1985) (citations omitted)).
 </p>
<p id="b1638-5">
  The record herein clearly indicates Mr. Evans gave a voluntary and unequivocal consent to the pat down. There is no evidence the officers used any threats or other forms of coercive conduct in obtaining this consent. Moreover, after the pat down by both officers had commenced, Mr. Evans did not request the officers to cease the pat down, nor did he manifest any conduct indicating he wanted the pat down to be ceased. Therefore, we find the district court’s findings on this issue were supported by the record and not clearly erroneous. Based on the totality of the circumstances and giving the appropriate indulgence to the presumption against waiver, we nevertheless conclude the consent given by Mr. Evans was voluntary and not restricted to a search by Sergeant Ring only.
 </p>
<p id="b1638-6">
  Mr. Evans next argues the district court erred in not suppressing the evidence because it was “fruit of the poisonous tree” of the unlawful search of the carry-on bag, and cites
  <em>
   Wong Sun v. United States,
  </em>
  <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U.S. 471</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407</a></span>, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">9 L.Ed.2d 441</a></span> (1963). The search complained of was upheld by the district court pursuant to the inventory search exception to the warrant requirement, and alternatively, under the inevitable discovery doctrine. Mr. Evans contests both rulings.
 </p>
<p id="b1638-8">
  First, in regard to its ruling that the initial search of the carry-on bag was conducted as a legitimate inventory search, the district court made the following findings: “Section 239.29 is the policy provision that governed or should have governed Officer Ring’s conduct in this case”; “pursuant to this policy, the case in which the cocaine was found was directed to have been opened by Officer Ring and inventoried before booking”; and “there was not probable cause at that time to believe that contraband or evidence was within and, as a result, there was no requirement for the officer at that stage to follow the second directive with respect to Section 239.29.”
 </p>
<p id="b1638-9">
  Oklahoma City Police Department Policy, Section 239.29, states in pertinent part:
 </p>
<blockquote id="b1638-10">
  [1] Locked containers such as suitcases or briefcases must be opened and the contents inventoried before booking. [2] If probable cause exists to believe that contraband or evidence is within, care should be taken to obtain legal authority before opening to ensure the admissibility of that evidence in court.
 </blockquote>
<p id="b1638-11">
  The first directive indicated above clearly advises the officer to open and inventory the contents of locked containers, unless the second directive is activated by the existence of probable cause. We are convinced, based on the record before us, that probable cause to believe further contraband would be found in the bag did
  <em>
   not
  </em>
  exist at the time Sergeant Ring first opened the bag at the bus station. Therefore, his search was in accordance with departmental policy directing him to open locked containers
  <em>
   before booking.
  </em>
  While Defendant argues the location of the search (at the bus station rather than the police station) mandates a finding that its purpose was merely a “ruse for a general rummaging,”
  <em>
   see Florida v. Wells,
  </em>
  — U.S. -, —, <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/#1635" aria-description="Citation for case: Florida v. Wells">110 S.Ct. 1632, 1635</a></span>, <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/" aria-description="Citation for case: Florida v. Wells">109 L.Ed.2d 1</a></span> (1990), we find this argument without merit. Section 239.29 of the Oklahoma City Police Department policy does not require officers to conduct their inventory at a particular place, but “specifically
  <span citation-index="1" class="star-pagination" label="1539"> 
   *1539
   </span>
  envisions otherwise.” Nor is there any directive in the law imposing such a requirement. We find the officers’ explanation for conducting the search at the bus station reasonable, and conclude the search was not invalidated because it was not done at the police station.
 </p>
<p id="b1639-4">
  Defendant also claims the absence of note-taking by the officers and the cessation of the “inventory” search after finding the first suspicious package further indicates the search was a ruse. The district court acknowledged these concerns but was persuaded that Sergeant Ring’s failure to take notes was not improper, since he was at the very outset of the inventory when he encountered the suspicious, taped bundle. The court also declined to fault the officers for acting out of an abundance of caution in heeding Defendant’s request that a search warrant be obtained.
 </p>
<p id="b1639-5">
  In
  <em>
   <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/" aria-description="Citation for case: Florida v. Wells">Wells</a></span>,
  </em>
  the case relied on by Mr. Evans, the Supreme Court cautioned against inventory searches being used as a ruse for investigatory purposes. — U.S. at-, <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/#1635" aria-description="Citation for case: Florida v. Wells">110 S.Ct. at 1635</a></span>. Our review of the record leads us to conclude that the district court’s findings on this matter are not clearly erroneous, and the initial search into Mr. Evans’s carry-on bag was not a mere ruse for investigation.
  <em>
   <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/" aria-description="Citation for case: Florida v. Wells">Wells</a></span>
  </em>
  dealt with the specific problem of the absence of a department policy or standardized criteria governing such searches.
  <em>
   <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/" aria-description="Citation for case: Florida v. Wells">Id.</a></span>
  </em>
  We do not have such a void in this case. Section 239.29 of the Oklahoma City Police Department Policy clearly provides procedures to be followed. Sergeant Ring adhered to these procedures, and there is no evidence in the record that he anticipated or intended the search to serve any purpose other than that of an inventory of the contents of the bag. Accordingly, we hold the search conducted at the bus station of the carry-on bag was a lawful inventory search, and the evidence discovered subsequently (pursuant to valid search warrants) was not the fruit of an illegality, but was lawfully obtained.
 </p>
<p id="b1639-8">
  Having decided the search of the carry-on bag was a lawful inventory search, we uphold the district court’s decision to deny Mr. Evans’s motion to suppress on this basis. Therefore, we need not address the district court’s alternate holding that the search was justified and lawful under the inevitable discovery doctrine.
  <em>
   See Nix v. Williams,
  </em>
  <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">467 U.S. 431</a></span>, <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">104 S.Ct. 2501</a></span>, <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">81 L.Ed.2d 377</a></span> (1984).
 </p>
<p id="b1639-10">
  III.
 </p>
<p id="b1639-11">
  For the aforementioned reasons, we AFFIRM the district court’s decision to deny Mr. Evans’s motion to suppress evidence.
 </p>

<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b1637-9">
   . The district court also found on this point that two statements made in the Defendant’s affidavit relating to an alleged restriction of his consent, were unsupported in the record and otherwise not credible. We agree with these findings.
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/United States v. Flores-Montano.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Flores-Montano"
type: case
citation: ""
parallel_cite: "541 U.S. 149; 124 S. Ct. 1582; 158 L. Ed. 2d 311; 72 U.S.L.W. 4263; 17 Fla. L. Weekly Fed. S 207"
neutral_cite: 2004 U.S. LEXIS 2548
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-03-30
docket: 02-1794
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2004-03-30
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Flores-Montano
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/134729/united-states-v-flores-montano/"
  cluster_id: 134729
  opinion_id: 134729
  identity_checked: true
homes:
  - page: "[[Border Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Montoya de Hernandez]]", "[[United States v. Martinez-Fuerte]]", "[[Carroll v. United States]]", "[[Almeida-Sanchez v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "border-searches", "vehicle-search", "gas-tank", "suspicionless-search"]
holding: "The government's authority to conduct suspicionless searches of vehicles at the border includes disassembling and reassembling a gas…"
lake:
  record_id: United States v. Flores-Montano
  status: verified
  projected_at: 2026-07-09
---

# United States v. Flores-Montano

*541 U.S. 149 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
At the Otay Mesa Port of Entry, customs inspectors sent Manuel Flores-Montano's station wagon to secondary inspection. A second inspector tapped the gas tank, found it sounded solid, and had a contract mechanic remove the tank; the inspector then hammered off bondo, opened an access plate, and found 37 kilograms of marijuana. The Government did not rely on reasonable suspicion; the Ninth Circuit (following its *Molina-Tarazon* decision) had held the fuel-tank disassembly required reasonable suspicion.

## Issue
Whether the Fourth Amendment requires reasonable suspicion before customs officers may remove, disassemble, and reassemble a vehicle's fuel tank in a search at the international border.

## Rule
No. A suspicionless border search of a vehicle, including disassembly of its fuel tank, is reasonable. The Court held at the outset: "We hold that the search in question did not require reasonable suspicion." — 541 U.S. at 150. ^pin-150

The border is a special context: "The Government's interest in preventing the entry of unwanted persons and effects is at its zenith at the international border," and searches there "are reasonable simply by virtue of the fact that they occur at the border." — *Id.* at 152–53. ^pin-152

The intrusiveness analysis that may attend highly invasive *person* searches does not transfer to vehicles: "Complex balancing tests to determine what is a 'routine' search of a vehicle, as opposed to a more 'intrusive' search of a person, have no place in border searches of vehicles." — *Id.* at 152. ^pin-152a

## Application
On these facts the disassembly was reasonable without any suspicion. The Court rejected Flores-Montano's privacy argument because the expectation of privacy is diminished at the border and "the search of a gas tank, which should be solely a repository for fuel," is no greater an invasion than a search of the passenger compartment. It rejected his property argument because the removal, disassembly, and reassembly is "a brief procedure that can be reversed without damaging the safety or operation of the vehicle," with no record evidence of serious damage; any interference was "justified by the Government's paramount interest in protecting the border." The Court therefore "conclude[d] that the Government's authority to conduct suspicionless inspections at the border includes the authority to remove, disassemble, and reassemble a vehicle's fuel tank." — [*Id.* at 155](https://www.courtlistener.com/opinion/134729/united-states-v-flores-montano/#:~:text=the%20search%20of%20a%20gas). ^pin-155

## Conclusion
No reasonable suspicion was required; the Ninth Circuit's judgment suppressing the marijuana was reversed. The Court reserved that "some searches of property [may be] so destructive as to require a different result," but this was not one.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment. *Flores-Montano* confines the "routine vs. non-routine" distinction drawn for *person* searches in [[United States v. Montoya de Hernandez]] and instead applies the plenary suspicionless-search rule to vehicles; it expressly leaves open only searches so destructive as to require a different result.

## Appears on
- [[Border Searches]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Flores-Montano*, 541 U.S. 149 (2004) — https://www.courtlistener.com/opinion/134729/united-states-v-flores-montano/ — pinpoints: 150, 152–53, 155.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c100df29bc756d10", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2004 U.S. LEXIS 2548", "official_citation_present": false, "parallel_cite": "541 U.S. 149; 124 S. Ct. 1582; 158 L. Ed. 2d 311; 72 U.S.L.W. 4263; 17 Fla. L. Weekly Fed. S 207", "title": "United States v. Flores-Montano", "year": "2004"}}
{"assertion_id": "7ab8bd6c0a5155c2", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The government's authority to conduct suspicionless searches of vehicles at the border includes disassembling and reassembling a gas…", "title": "United States v. Flores-Montano"}}
{"assertion_id": "ccf0150ed52ad022", "dimension": "support", "kind": "home_role", "locator": {"home": "Border Searches"}, "payload": {"home": "Border Searches", "role": "Key — Progeny / Refinement", "title": "United States v. Flores-Montano"}}
{"assertion_id": "0a99e4b492cb5da4", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2004-03-30", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Flores-Montano", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Flores-Montano", "varies_by_point": "false"}}
{"assertion_id": "741908299a89b953", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Flores-Montano"}}
```

### lake record — United States v. Flores-Montano

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Flores-Montano",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Flores-Montano",
    "case_name_short": "Flores-Montano",
    "case_name_full": "United States v. Flores-Montano",
    "input_case_name": "United States v. Flores-Montano",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-03-30",
    "year": 2004,
    "docket": "02-1794",
    "cluster_id": 134729,
    "lead_opinion_id": 134729,
    "sibling_ids": [
      134729,
      9434573,
      9434574
    ],
    "absolute_url": "/opinion/134729/united-states-v-flores-montano/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "541 U.S. 149",
        "volume": "541",
        "reporter": "U.S.",
        "page": "149",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 1582",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "1582",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "158 L. Ed. 2d 311",
        "volume": "158",
        "reporter": "L. Ed. 2d",
        "page": "311",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 U.S.L.W. 4263",
        "volume": "72",
        "reporter": "U.S.L.W.",
        "page": "4263",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 Fla. L. Weekly Fed. S 207",
        "volume": "17",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "207",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 2548",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "2548",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "541 U.S. 149",
        "volume": "541",
        "reporter": "U.S.",
        "page": "149",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 1582",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "1582",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "158 L. Ed. 2d 311",
        "volume": "158",
        "reporter": "L. Ed. 2d",
        "page": "311",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 2548",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "2548",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 U.S.L.W. 4263",
        "volume": "72",
        "reporter": "U.S.L.W.",
        "page": "4263",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 Fla. L. Weekly Fed. S 207",
        "volume": "17",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "207",
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
      "id": "pin-150",
      "page": null,
      "quote": "--- # United States v. Flores-Montano *541 U.S. 149 (2004)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background At the Otay Mesa Port of Entry, customs inspectors sent Manuel Flores-Montano's station wagon to secondary inspection. A second inspector tapped the gas tank, found it sounded solid, and had a contract mechanic remove the tank; the inspector then hammered off bondo, opened an access plate, and found 37 kilograms of marijuana. The Government did not rely on reasonable suspicion; the Ninth Circuit (following its *Molina-Tarazon* decision) had held the fuel-tank disassembly required reasonable suspicion. ## Issue Whether the Fourth Amendment requires reasonable suspicion before customs officers may remove, disassemble, and reassemble a vehicle's fuel tank in a search at the international border. ## Rule No. A suspicionless border search of a vehicle, including disassembly of its fuel tank, is reasonable. The Court held at the outset:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-152",
      "page": null,
      "quote": "The Government's interest in preventing the entry of unwanted persons and effects is at its zenith at the international border,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-152a",
      "page": null,
      "quote": "Complex balancing tests to determine what is a 'routine' search of a vehicle, as opposed to a more 'intrusive' search of a person, have no place in border searches of vehicles.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-155",
      "page": null,
      "quote": "the search of a gas tank, which should be solely a repository for fuel,",
      "star_marker": "154",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 13434,
      "fragment": "#:~:text=the%20search%20of%20a%20gas",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2004-03-30",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Flores-Montano",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Caballero",
          "cluster_id": 7319742,
          "cite": [
            "178 F. Supp. 3d 1008",
            "2016 U.S. Dist. LEXIS 51132",
            "2016 WL 1546731"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Levy",
          "cluster_id": 8442407,
          "cite": [
            "803 F.3d 120",
            "2015 U.S. App. LEXIS 17154",
            "2015 WL 5692332"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cotterman",
          "cluster_id": 213651,
          "cite": [
            "637 F.3d 1068",
            "2011 U.S. App. LEXIS 6483",
            "2011 WL 1137302"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Perez-Diaz",
          "cluster_id": 8473264,
          "cite": [
            "172 F. App'x 717"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane1_negative"
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
        "journal_ref": "United States v. Flores-Montano:lane1_negative"
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
        "journal_ref": "United States v. Flores-Montano:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Delores Henry v. Melody Hulett",
          "cluster_id": 4774392,
          "cite": [
            "969 F.3d 769"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
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
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stuart Romm",
          "cluster_id": 795139,
          "cite": [
            "455 F.3d 990",
            "2006 U.S. App. LEXIS 18474",
            "2006 WL 2042827"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
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
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Al Otro Lado v. Chad Wolf",
          "cluster_id": 4732848,
          "cite": [
            "952 F.3d 999"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alfaro-Moncada",
          "cluster_id": 147332,
          "cite": [
            "607 F.3d 720",
            "2010 A.M.C. 1680",
            "2010 U.S. App. LEXIS 10841",
            "2010 WL 2103442"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ray Askins v. Usdhs",
          "cluster_id": 4526305,
          "cite": [
            "899 F.3d 1035"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Howard Cotterman",
          "cluster_id": 854692,
          "cite": [
            "709 F.3d 952",
            "2013 WL 856292",
            "2013 U.S. App. LEXIS 4731"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "International Refugee Assistance Project v. Trump",
          "cluster_id": 4394639,
          "cite": [
            "857 F.3d 554",
            "2017 U.S. App. LEXIS 9109",
            "2017 WL 2273306"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Guzman-Padilla",
          "cluster_id": 1448445,
          "cite": [
            "573 F.3d 865",
            "2009 U.S. App. LEXIS 16298",
            "2009 WL 2182818"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vincent Franklin Bennett",
          "cluster_id": 785723,
          "cite": [
            "363 F.3d 947",
            "64 Fed. R. Serv. 467",
            "2004 U.S. App. LEXIS 6935"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carlyle Bryan v. United States",
          "cluster_id": 4582985,
          "cite": [
            "913 F.3d 356"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Abbouchi",
          "cluster_id": 1235958,
          "cite": [
            "502 F.3d 850",
            "2007 U.S. App. LEXIS 21280",
            "2007 WL 2493507"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Theodore Stewart",
          "cluster_id": 1039561,
          "cite": [
            "729 F.3d 517",
            "2013 WL 4711054",
            "2013 U.S. App. LEXIS 18224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Troy",
          "cluster_id": 204022,
          "cite": [
            "583 F.3d 20",
            "2009 U.S. App. LEXIS 21186",
            "2009 WL 3050901"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Denson v. United States",
          "cluster_id": 78422,
          "cite": [
            "574 F.3d 1318",
            "2009 U.S. App. LEXIS 15634",
            "2009 WL 2031036"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anas Elhady v. Unidentified CBP Agents",
          "cluster_id": 5299118,
          "cite": [
            "18 F.4th 880"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Miguel Cano",
          "cluster_id": 4649091,
          "cite": [
            "934 F.3d 1002"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Manuel Flores-Montano",
          "cluster_id": 792061,
          "cite": [
            "424 F.3d 1044",
            "2005 U.S. App. LEXIS 19768",
            "2005 WL 2218952"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tabbaa v. Chertoff",
          "cluster_id": 2661,
          "cite": [
            "509 F.3d 89",
            "2007 U.S. App. LEXIS 27258",
            "2007 WL 4150299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karl Touset",
          "cluster_id": 4500452,
          "cite": [
            "890 F.3d 1227"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anas Elhady v. Charles Kable, IV",
          "cluster_id": 4869134,
          "cite": [
            "993 F.3d 208"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hamza Kolsuz",
          "cluster_id": 4496513,
          "cite": [
            "890 F.3d 133"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Molina-Gomez",
          "cluster_id": 2788117,
          "cite": [
            "781 F.3d 13",
            "2015 WL 1283956"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Flores-Montano:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(134729 OR 9434573 OR 9434574) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 105,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 6,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 105,
        "triage_read": 8,
        "triage_snippet_classified": 97
      },
      "lane2_top_cited": {
        "query": "cites:(134729 OR 9434573 OR 9434574)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNSZzPTc4NjMwMyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28134729+OR+9434573+OR+9434574%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(134729 OR 9434573 OR 9434574)",
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
    "complete_query": "cites:(134729 OR 9434573 OR 9434574)",
    "indexed_citing_opinions": 145,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 134729,
        "count": 109,
        "count_source": "search"
      },
      {
        "opinion_id": 9434573,
        "count": 39,
        "count_source": "search"
      },
      {
        "opinion_id": 9434574,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 217,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-flores-montano.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcxOTE4NjEmcz00ODY5MTM0JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28134729+OR+9434573+OR+9434574%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 134729,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134729,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134729,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134729,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134729,
        "cited_id": 112795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134729,
        "cited_id": 521938,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134729,
        "cited_id": 686763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134729,
        "cited_id": 776460,
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
    "date_created": "2026-07-05T23:56:13Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:56:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:56:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:00:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:56:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Flores-Montano

```
<div>
<center><b><span class="citation" data-id="9434573"><a href="/opinion/134729/united-states-v-flores-montano/" aria-description="Citation for case: United States v. Flores-Montano">541 U.S. 149</a></span> (2004)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
FLORES-MONTANO</h1></center>
<center>No. 02-1794.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 25, 2004.</center>
<center>Decided March 30, 2004.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><span class="star-pagination">*150</span> REHNQUIST, C. J., delivered the opinion for a unanimous Court. BREYER, J., filed a concurring opinion, <i>post,</i> p. 156.</p>
<p><i>Lisa S. Blatt</i> argued the cause for the United States. With her on the briefs were <i>Solicitor General Olson, Assistant Attorney General Wray, Deputy Solicitor General Dreeben, Daniel S. Goodman,</i> and <i>Alfonso Robles.</i></p>
<p><i>Steven F. Hubachek,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./540/1043/">540 U. S. 1043</a></span>, argued the cause for respondent. With him on the brief were <i>Vincent J. Brunkow</i> and <i>John C. Lemon.</i><sup>[*]</sup></p>
<p>CHIEF JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>Customs officials seized 37 kilograms  a little more than 81 pounds  of marijuana from respondent Manuel Flores-Montano's gas tank at the international border. The Court of Appeals for the Ninth Circuit, relying on an earlier decision by a divided panel of that court, <i>United States</i> v. <i>Molina-Tarazon,</i> <span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/" aria-description="Citation for case: United States v. Jose Molina-Tarazon">279 F. 3d 709</a></span> (2002), held that the Fourth Amendment forbade the fuel tank search absent reasonable suspicion. No. 02-50306, <span class="citation no-link">2003 WL 22410705</span> (Mar. 14, 2003). We hold that the search in question did not require reasonable suspicion.</p>
<p>Respondent, driving a 1987 Ford Taurus station wagon, attempted to enter the United States at the Otay Mesa Port of Entry in southern California. A customs inspector conducted an inspection of the station wagon, and requested respondent to leave the vehicle. The vehicle was then taken to a secondary inspection station.</p>
<p><span class="star-pagination">*151</span> At the secondary station, a second customs inspector inspected the gas tank by tapping it, and noted that the tank sounded solid. Subsequently, the inspector requested a mechanic under contract with Customs to come to the border station to remove the tank. Within 20 to 30 minutes, the mechanic arrived. He raised the car on a hydraulic lift, loosened the straps and unscrewed the bolts holding the gas tank to the undercarriage of the vehicle, and then disconnected some hoses and electrical connections. After the gas tank was removed, the inspector hammered off bondo (a putty-like hardening substance that is used to seal openings) from the top of the gas tank. The inspector opened an access plate underneath the bondo and found 37 kilograms of marijuana bricks. The process took 15 to 25 minutes.</p>
<p>A grand jury for the Southern District of California indicted respondent on one count of unlawfully importing marijuana, in violation of <span class="citation no-link">21 U. S. C. § 952</span>, and one count of possession of marijuana with intent to distribute, in violation of § 841(a)(1). Relying on <i><span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/" aria-description="Citation for case: United States v. Jose Molina-Tarazon">Molina-Tarazon</a></span>,</i> respondent filed a motion to suppress the marijuana recovered from the gas tank. In <i><span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/" aria-description="Citation for case: United States v. Jose Molina-Tarazon">Molina-Tarazon</a></span>,</i> a divided panel of the Court of Appeals held, <i>inter alia,</i> that removal of a gas tank requires reasonable suspicion in order to be consistent with the Fourth Amendment. <span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/#717" aria-description="Citation for case: United States v. Jose Molina-Tarazon">279 F. 3d, at 717</a></span>.</p>
<p>The Government advised the District Court that it was not relying on reasonable suspicion as a basis for denying respondent's suppression motion, but that it believed <i><span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/" aria-description="Citation for case: United States v. Jose Molina-Tarazon">Molina-Tarazon</a></span></i> was wrongly decided. The District Court, relying on <i><span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/" aria-description="Citation for case: United States v. Jose Molina-Tarazon">Molina-Tarazon</a></span>,</i> held that reasonable suspicion was required to justify the search and, accordingly, granted respondent's motion to suppress. The Court of Appeals, citing <i><span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/" aria-description="Citation for case: United States v. Jose Molina-Tarazon">Molina-Tarazon</a></span>,</i> summarily affirmed the District Court's judgment. No. 02-50306, <span class="citation no-link">2003 WL 22410705</span> (CA9, Mar. 14, 2003). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./540/945/">540 U. S. 945</a></span> (2003), and now reverse.</p>
<p><span class="star-pagination">*152</span> In <i><span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/" aria-description="Citation for case: United States v. Jose Molina-Tarazon">Molina-Tarazon</a></span>,</i> the Court of Appeals decided a case presenting similar facts to the one at bar. It asked "whether [the removal and dismantling of the defendant's fuel tank] is a `routine' border search for which no suspicion whatsoever is required." <span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/#711" aria-description="Citation for case: United States v. Jose Molina-Tarazon">279 F. 3d, at 711</a></span>. The Court of Appeals stated that "[i]n order to conduct a search that goes beyond the routine, an inspector must have reasonable suspicion," and the "critical factor" in determining whether a search is "routine" is the "degree of intrusiveness." <span class="citation" data-id="9494749"><a href="/opinion/776460/united-states-v-jose-molina-tarazon/#712" aria-description="Citation for case: United States v. Jose Molina-Tarazon"><i>Id.,</i> at 712-713</a></span>.</p>
<p>The Court of Appeals seized on language from our opinion in <i>United States</i> v. <i>Montoya de Hernandez,</i> <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U. S. 531</a></span> (1985), in which we used the word "routine" as a descriptive term in discussing border searches. <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#538" aria-description="Citation for case: United States v. Montoya De Hernandez"><i>Id.,</i> at 538</a></span> ("Routine searches of the persons and effects of entrants are not subject to any requirement of reasonable suspicion, probable cause, or warrant"); <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#541" aria-description="Citation for case: United States v. Montoya De Hernandez"><i>id.,</i> at 541, n. 4</a></span> ("Because the issues are not presented today we suggest no view on what level of suspicion, if any, is required for nonroutine border searches such as strip, body-cavity, or involuntary x-ray searches"). The Court of Appeals took the term "routine," fashioned a new balancing test, and extended it to searches of vehicles. But the reasons that might support a requirement of some level of suspicion in the case of highly intrusive searches of the person  dignity and privacy interests of the person being searched  simply do not carry over to vehicles. Complex balancing tests to determine what is a "routine" search of a vehicle, as opposed to a more "intrusive" search of a person, have no place in border searches of vehicles.</p>
<p>The Government's interest in preventing the entry of unwanted persons and effects is at its zenith at the international border. Time and again, we have stated that "searches made at the border, pursuant to the longstanding right of the sovereign to protect itself by stopping and examining persons and property crossing into this country, are reasonable simply by virtue of the fact that they occur at the <span class="star-pagination">*153</span> border." <i>United States</i> v. <i>Ramsey,</i> <span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#616" aria-description="Citation for case: United States v. Ramsey">431 U. S. 606, 616</a></span> (1977). Congress, since the beginning of our Government, "has granted the Executive plenary authority to conduct routine searches and seizures at the border, without probable cause or a warrant, in order to regulate the collection of duties and to prevent the introduction of contraband into this country." <i>Montoya de <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/" aria-description="Citation for case: United States v. Montoya De Hernandez">Hernandez, supra,</a></span></i> at 537 (citing <i><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/" aria-description="Citation for case: United States v. Ramsey">Ramsey, supra,</a></span></i> at 616-617 (citing Act of July 31, 1789, ch. 5, <span class="citation no-link">1 Stat. 29</span>)). The modern statute that authorized the search in this case, <span class="citation no-link">46 Stat. 747</span>, <span class="citation no-link">19 U. S. C. § 1581</span>(a),<sup>[1]</sup> derived from a statute passed by the First Congress, the Act of Aug. 4, 1790, ch. 35, § 31, <span class="citation no-link">1 Stat. 164</span>, see <i>United States</i> v. <i>Villamonte-Marquez,</i> <span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/#584" aria-description="Citation for case: United States v. Villamonte-Marquez">462 U. S. 579, 584</a></span> (1983), and reflects the "impressive historical pedigree" of the Government's power and interest, <span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/#585" aria-description="Citation for case: United States v. Villamonte-Marquez"><i>id.,</i> at 585</a></span>. It is axiomatic that the United States, as sovereign, has the inherent authority to protect, and a paramount interest in protecting, its territorial integrity.</p>
<p>That interest in protecting the borders is illustrated in this case by the evidence that smugglers frequently attempt to penetrate our borders with contraband secreted in their automobiles' fuel tank. Over the past 5½ fiscal years, there have been 18,788 vehicle drug seizures at the southern California ports of entry. App. to Pet. for Cert. 12a. Of those 18,788, gas tank drug seizures have accounted for 4,619 of the vehicle drug seizures, or approximately 25%. <i><span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/" aria-description="Citation for case: United States v. Villamonte-Marquez">Ibid.</a></span></i> In addition, instances of persons smuggled in and around gas tank compartments are discovered at the ports of entry of <span class="star-pagination">*154</span> San Ysidro and Otay Mesa at a rate averaging 1 approximately every 10 days. <i><span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/" aria-description="Citation for case: United States v. Villamonte-Marquez">Id.,</a></span></i> at 16a.</p>
<p>Respondent asserts two main arguments with respect to his Fourth Amendment interests. First, he urges that he has a privacy interest in his fuel tank, and that the suspicionless disassembly of his tank is an invasion of his privacy. But on many occasions, we have noted that the expectation of privacy is less at the border than it is in the interior. <i>Montoya de Hernandez, supra,</i> at 538. We have long recognized that automobiles seeking entry into this country may be searched. See <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#154" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 154</a></span> (1925) ("Travellers may be so stopped in crossing an international boundary because of national self protection reasonably requiring one entering the country to identify himself as entitled to come in, and his belongings as effects which may be lawfully brought in"). It is difficult to imagine how the search of a gas tank, which should be solely a repository for fuel, could be more of an invasion of privacy than the search of the automobile's passenger compartment.</p>
<p>Second, respondent argues that the Fourth Amendment "protects property as well as privacy," <i>Soldal</i> v. <i>Cook County,</i> <span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/#62" aria-description="Citation for case: Soldal v. Cook County">506 U. S. 56, 62</a></span> (1992), and that the disassembly and reassembly of his gas tank is a significant deprivation of his property interest because it may damage the vehicle. He does not, and on the record cannot, truly contend that the procedure of removal, disassembly, and reassembly of the fuel tank in this case or any other has resulted in serious damage to, or destruction of, the property.<sup>[2]</sup> According to <span class="star-pagination">*155</span> the Government, for example, in fiscal year 2003, 348 gas tank searches conducted along the southern border were negative (<i>i. e.,</i> no contraband was found), the gas tanks were reassembled, and the vehicles continued their entry into the United States without incident. Brief for United States 31.</p>
<p>Respondent cites not a single accident involving the vehicle or motorist in the many thousands of gas tank disassemblies that have occurred at the border. A gas tank search involves a brief procedure that can be reversed without damaging the safety or operation of the vehicle. If damage to a vehicle were to occur, the motorist might be entitled to recovery. See, <i>e. g.,</i> <span class="citation no-link">31 U. S. C. § 3723</span>; <span class="citation no-link">19 U. S. C. § 1630</span>. While the interference with a motorist's possessory interest is not insignificant when the Government removes, disassembles, and reassembles his gas tank, it nevertheless is justified by the Government's paramount interest in protecting the border.<sup>[3]</sup></p>
<p>For the reasons stated, we conclude that the Government's authority to conduct suspicionless inspections at the border includes the authority to remove, disassemble, and reassemble a vehicle's fuel tank. While it may be true that some <span class="star-pagination">*156</span> searches of property are so destructive as to require a different result, this was not one of them. The judgment of the United States Court of Appeals for the Ninth Circuit is therefore reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE BREYER, concurring.</p>
<p>I join the Court's opinion in full. I also note that Customs keeps track of the border searches its agents conduct, including the reasons for the searches. Tr. of Oral Arg. 53-54. This administrative process should help minimize concerns that gas tank searches might be undertaken in an abusive manner.</p>
<h2>NOTES</h2>
<p>[*]   <i>Daniel J. Popeo</i> and <i>Richard A. Samp</i> filed a brief for the Washington Legal Foundation et al. as <i>amici curiae</i> urging reversal.
</p>
<p><i>John Wesley Hall, Jr., David M. Siegel,</i> and <i>Lisa B. Kemler</i> filed a brief for the National Association of Criminal Defense Lawyers as <i>amicus curiae</i> urging affirmance.</p>
<p>[1]  Section 1581(a) provides:
</p>
<p>"Any officer of the customs may at any time go on board of any vessel or vehicle at any place in the United States or within the customs waters or, as he may be authorized, within a customs-enforcement area established under the Anti-Smuggling Act, or at any other authorized place, without as well as within his district, and examine the manifest and other documents and papers and examine, inspect, and search the vessel or vehicle and every part thereof and any person, trunk, package, or cargo on board, and to this end may hail and stop such vessel or vehicle, and use all necessary force to compel compliance."</p>
<p>[2]  Respondent's reliance on cases involving exploratory drilling searches is misplaced. See <i>United States</i> v. <i>Rivas,</i> <span class="citation" data-id="6976386"><a href="/opinion/7071868/united-states-v-rivas/" aria-description="Citation for case: United States v. Rivas">157 F. 3d 364</a></span> (CA5 1998) (drilling into body of trailer required reasonable suspicion); <i>United States</i> v. <i>Robles,</i> <span class="citation" data-id="686763"><a href="/opinion/686763/united-states-v-jose-robles/" aria-description="Citation for case: United States v. Jose Robles">45 F. 3d 1</a></span> (CA1 1995) (drilling into machine part required reasonable suspicion); <i>United States</i> v. <i>Carreon,</i> <span class="citation" data-id="521938"><a href="/opinion/521938/united-states-v-enrique-carreon/" aria-description="Citation for case: United States v. Enrique Carreon">872 F. 2d 1436</a></span> (CA10 1989) (drilling into camper required reasonable suspicion). We have no reason at this time to pass on the reasonableness of drilling, but simply note the obvious factual difference that this case involves the procedure of removal, disassembly, and reassembly of a fuel tank, rather than potentially destructive drilling. We again leave open the question "whether, and under what circumstances, a border search might be deemed `unreasonable' because of the particularly offensive manner in which it is carried out." <i>United States</i> v. <i>Ramsey,</i> <span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#618" aria-description="Citation for case: United States v. Ramsey">431 U. S. 606, 618, n. 13</a></span> (1977).</p>
<p>[3]  Respondent also argued that he has some sort of Fourth Amendment right not to be subject to delay at the international border and that the need for the use of specialized labor, as well as the hour actual delay here and the potential for even greater delay for reassembly are an invasion of that right. Respondent points to no cases indicating the Fourth Amendment shields entrants from inconvenience or delay at the international border.
</p>
<p>The procedure in this case took about an hour (including the wait for the mechanic). At oral argument, the Government advised us that, depending on the type of car, a search involving the disassembly and reassembly of a gas tank may take one to two hours. Tr. of Oral Arg. 10. We think it clear that delays of one to two hours at international borders are to be expected.</p>

</div>
```

---

## GROUP: content/cases/United States v. Ganias.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Ganias
type: case
citation: "824 F.3d 199 (2016)"
parallel_cite: "117 A.F.T.R.2d (RIA) 1841"
neutral_cite: "2016 U.S. App. LEXIS 9706; 2016 WL 3031285"
court: 2d Cir. en banc
court_level: coa
circuit: ca2
year: 2016
date_decided: 2016-05-27
docket: 12-240-cr
authority_weight: "Binding in-circuit — 2d Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/3207604/united-states-v-ganias/"
  cluster_id: 3207604
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Ganias
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Plain View Doctrine]]"
    role: Key
related:
  - "[[Plain View Doctrine]]"
  - "[[United States v. Leon]]"
  - "[[Riley v. California]]"
  - "[[The Exclusionary Rule]]"
tags:
  - case
  - fourth-amendment
  - search
  - digital-privacy
  - computer-search
  - over-retention
  - particularity
  - good-faith-exception
  - second-circuit
holding: "Sitting en banc, the Second Circuit affirmed Ganias's tax-evasion conviction on good-faith grounds — the agents' reliance on the 2006 warrant to search forensic mirror images retained from a 2003 search was objectively reasonable under Leon — and therefore expressly declined to decide whether the Government's years-long retention of non-responsive mirrored computer data beyond the 2003 warrant's scope violated the Fourth Amendment, displacing the panel's contrary holding."
---

# United States v. Ganias

*824 F.3d 199 (2d Cir. 2016) (en banc)* (No. 12-240-cr) · U.S. Court of Appeals for the Second Circuit · **Binding in-circuit — 2d Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 3207604 → en banc majority opinion 3207498 (824 F.3d 199, decided 2016-05-27); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
In 2003, Army criminal investigators obtained a warrant to search the office of accountant Stavros Ganias for records of two companies (IPM and American Boiler) suspected of defrauding the Army. Rather than sift the computers on site, agents made complete forensic **mirror images** of three hard drives for off-site review. Those mirrors contained both data responsive to the 2003 warrant and a great deal of **non-responsive** data — including Ganias's own personal and client files. The Government retained the full mirrors as its investigation continued. In 2006, after suspicion turned to Ganias himself, agents obtained a **second warrant** and searched the retained non-responsive data, finding evidence that convicted Ganias of two counts of tax evasion. Ganias argued that once the responsive data had been segregated (by early 2005), continued retention of the non-responsive mirror data violated the Fourth Amendment and tainted the 2006 search.

## Issue
Whether the Government's retention of forensically mirrored computer data that was non-responsive to the 2003 warrant, and its later search of that data under a 2006 warrant, required suppression — or whether the agents' reliance on the 2006 warrant was protected by the [[The Good-Faith Exception|good-faith exception]], making it unnecessary to decide the Fourth Amendment retention question.

## Rule
The [[Reading and Citing Cases#en-banc|en banc]] court resolved the case on the [[The Good-Faith Exception|good-faith exception]] without reaching the constitutional retention question. Because the agents obtained and relied on a 2006 warrant, and that reliance was objectively reasonable, the *[[United States v. Leon|Leon]]* [[The Good-Faith Exception|good-faith exception]] foreclosed suppression regardless of whether the underlying retention was lawful: "We conclude that the Government relied in good faith on the 2006 warrant, and that this reliance was objectively reasonable. Accordingly, we need not decide whether retention of the forensic mirrors violated the Fourth Amendment, and we AFFIRM the judgment of the district court." — 824 F.3d 199, slip op. at 3. ^pin-op3

## Application
The court assumed without deciding that the prolonged retention of non-responsive mirror data might raise a serious Fourth Amendment concern, but held that even if it did, the deterrence rationale of the exclusionary rule had no purchase here: the agents did not act deliberately, recklessly, or with gross negligence. They preserved the mirrors in the good-faith belief that doing so was lawful, sought a fresh judicial warrant in 2006 before searching the retained data, and reasonably relied on that warrant. On that record, suppression was unwarranted under *[[United States v. Leon|Leon]]*, and the constitutional question about digital over-seizure and over-retention could be left for another day.

## Conclusion
**Affirmed.** Judges Livingston and Lynch wrote for the [[Reading and Citing Cases#en-banc|en banc]] majority; Judge Lohier (joined by Judge Pooler) concurred, and Judge Chin dissented. The [[Reading and Citing Cases#en-banc|en banc]] court's good-faith disposition displaced the 2014 panel decision, which had held that the retention of the non-responsive mirror data violated the Fourth Amendment.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Ganias* is the Second Circuit's marquee statement on the **digital over-seizure / over-retention** problem, but it decides the issue only through the *[[United States v. Leon|Leon]]* good-faith exit — the [[Reading and Citing Cases#en-banc|en banc]] court expressly declined to hold whether keeping non-responsive computer-mirror data beyond a warrant's scope is itself a Fourth Amendment violation, leaving the [[Particularity|particularity]]/retention question open in the circuit. Frame it as an unresolved-scope authority, paired with the plain-view anti-exploratory-search principle.

## Appears on
- [[Plain View Doctrine]] — *Key*

## Sources
- [*United States v. Ganias*, 824 F.3d 199 (2d Cir. 2016) (en banc)](https://www.courtlistener.com/opinion/3207604/united-states-v-ganias/) — pinpoint: slip op. at 3 (good-faith holding + express reservation of the retention question; the CL opinion text is slip-paginated, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d33ffbec1d9885d4", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "824 F.3d 199 (2016)", "court": "2d Cir. en banc", "neutral_cite": "2016 U.S. App. LEXIS 9706; 2016 WL 3031285", "official_citation_present": true, "parallel_cite": "117 A.F.T.R.2d (RIA) 1841", "title": "United States v. Ganias", "year": "2016"}}
{"assertion_id": "658fc5613e2e4d34", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Sitting en banc, the Second Circuit affirmed Ganias's tax-evasion conviction on good-faith grounds — the agents' reliance on the 2006 warrant to search forensic mirror images retained from a 2003 search was objectively reasonable under Leon — and therefore expressly declined to decide whether the Government's years-long retention of non-responsive mirrored computer data beyond the 2003 warrant's scope violated the Fourth Amendment, displacing the panel's contrary holding.", "title": "United States v. Ganias"}}
{"assertion_id": "b7211d23ef7e822d", "dimension": "support", "kind": "home_role", "locator": {"home": "Plain View Doctrine"}, "payload": {"home": "Plain View Doctrine", "role": "Key", "title": "United States v. Ganias"}}
{"assertion_id": "9f64e17b3a53379e", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Ganias", "varies_by_point": "false"}}
{"assertion_id": "ea0281eb0024c54f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 2d Cir.", "title": "United States v. Ganias"}}
```

### lake record — United States v. Ganias

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Ganias",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Ganias",
    "case_name_short": "Ganias",
    "case_name_full": "UNITED STATES of America, Appellee, v. Stavros M. GANIAS, Defendant-Appellant",
    "input_case_name": "United States v. Ganias",
    "court": "2d Cir. en banc",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca2",
    "state": null,
    "date_decided": "2016-05-27",
    "year": 2016,
    "docket": "12-240-cr",
    "cluster_id": 3207604,
    "lead_opinion_id": 9823643,
    "sibling_ids": [],
    "absolute_url": "/opinion/3207604/united-states-v-ganias/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "824 F.3d 199",
      "volume": "824",
      "reporter": "F.3d",
      "page": "199",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "117 A.F.T.R.2d (RIA) 1841",
        "volume": "117",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1841",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2016 U.S. App. LEXIS 9706",
        "volume": "2016",
        "reporter": "U.S. App. LEXIS",
        "page": "9706",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 WL 3031285",
        "volume": "2016",
        "reporter": "WL",
        "page": "3031285",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "824 F.3d 199",
        "volume": "824",
        "reporter": "F.3d",
        "page": "199",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "117 A.F.T.R.2d (RIA) 1841",
        "volume": "117",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1841",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 U.S. App. LEXIS 9706",
        "volume": "2016",
        "reporter": "U.S. App. LEXIS",
        "page": "9706",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 WL 3031285",
        "volume": "2016",
        "reporter": "WL",
        "page": "3031285",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "824 F.3d 199",
    "official_selection": {
      "court_class": "coa",
      "selected": "824 F.3d 199",
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
    "date_created": "2026-07-07T01:39:29Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:39:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:39:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:39:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:39:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-ganias--3207604",
      "to_record_id": "United States v. Ganias",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Ganias (truncated)

```
<opinion type="majority">
<p id="b224-10">LIVINGSTON and LYNCH, JJ., filed the majority opinion in which KATZMANN, C.J., JACOBS, CABRANES, RAGGI, WESLEY, HALL, CARNEY, and DRONEY, JJ., joined in full, and POOLER and LOHIER, JJ., joined in full as to Parts I and III and in part as to Part II.</p>
<judges id="b224-12">LOHIER, J., filed a concurring opinion in which POOLER, J., joined.</judges>
<judges id="b224-13">CHIN, J., filed a dissenting opinion.</judges>
<author id="b224-14">DEBRA ANN LIVINGSTON and GERARD E. LYNCH, Circuit Judges:</author>
<p id="b224-15">Defendant-Appellant Stavros Ganias appeals from a judgment of the United States District Court for the District of Connecticut (Thompson, <em>J.) </em>convicting him, after a jury trial, of two counts of tax evasion in violation of <span class="citation no-link">26 U.S.C. § 7201</span>. He challenges his conviction on the ground that the Government violated his Fourth Amendment rights when, after lawfully copying three of his hard drives for off-site review pursuant to a 2003 search warrant, it retained these full forensic copies (or “mirrors”), which included data both responsive and non-responsive to the 2003 warrant, while its investigation continued, and ultimately searched the non-responsive data pursuant to a second warrant in 2006. Ganias contends that the Government had successfully sorted the data on the mirrors responsive to the 2003 warrant from the non-responsive data by January 2005, and that the retention of the mirrors thereafter (and, by extension, the 2006 search, which would not have been possible but for that retention) violated the Fourth Amendment. He argues that evidence obtained in executing the 2006 search warrant should therefore have been suppressed.</p>
<p id="b224-16">We conclude that the Government relied in good faith on the 2006 warrant, and that this reliance was objectively reasonable. Accordingly, we need not decide whether retention of the forensic mirrors violated the Fourth Amendment, and we AFFIRM the judgment of the district court.</p>
<p id="b224-17">I</p>
<p id="b224-18">A. Background<footnotemark>1</footnotemark></p>
<p id="b224-19">In August 2003, agents of the U.S. Army Criminal Investigation Division (“Army <page-number citation-index="1" label="201">*201</page-number>CID”) received an anonymous tip that Industrial Property Management (“IPM”), a company providing security for and otherwise maintaining a government-owned property in Stratford, Connecticut, pursuant to an Army contract, had engaged in misconduct in connection with that work. In particular, the informant alleged that IPM, owned by James McCarthy, had billed the Army for work that IPM employees had done for one of McCarthy’s other businesses, American Boiler, Inc. (“AB”), and for construction work performed for IPM’s operations manager at his home residence. The informant told the agents, including Special Agent Michael Conner, that IPM and AB’s financial books were maintained by Stavros Ganias, a former Internal Revenue Service (“IRS”) agent, who conducted business as Taxes International. On the basis of the informant’s information, as well as extensive additional corroboration, Agent Conner prepared an affidavit seeking three warrants to search the offices of IPM, AB, and Taxes International for evidence of criminal activity.<footnotemark>2</footnotemark> Nothing in the record suggests that Ganias himself was suspected of any crimes at that time.</p>
<p id="b225-11">In a warrant dated November 17, 2003, U.S. Magistrate Judge William I. Garfink-el authorized the search of Taxes International. The warrant authorized agents to seize, <em>inter alia, </em>“[a]ll books, records, documents, materials, computer hardware and software and computer associated data relating to the business, financial and accounting operations of [IPM] and [AB].” J.A. 438. It further authorized seizure of “[a]ny of the items described [in the warrant] ... which are stored in the form of magnetic or electronic coding on computer media or on media capable of being read by a computer with the aid of computer-related equipment, including ... fixed hard disks, or removable hard disk cartridges, software or memory in any form.” <em><span class="citation no-link">Id.</span> </em>The warrant also specifically authorized a number of digital search protocols, though it did not state that <em>only </em>these protocols were permitted.<footnotemark>3</footnotemark> The warrant authorized seizure of all hardware relevant to the alleged crimes.<footnotemark>4</footnotemark></p>
<p id="b226-3"><page-number citation-index="1" label="202">*202</page-number>On November 19, 2003, Army CID agents executed the search warrants. Because the warrants authorized the seizure of computer hardware and software, in addition to paper documents, Agent Conner sought the help, in executing the warrants, of agents from the Army CID’s Computer Crimes Investigation Unit (“CCIU”), a unit with specialized expertise in digital forensics and imaging. At Gani-as’s office, the CCIU agents — and in particular Special Agent David Shaver — located three computers. Rather than take the physical hard drives, which would have significantly impaired Ganias’s ability to conduct his business, Agent Shaver created mirror images: exact copies of all of the data stored thereon, down to the bit.<footnotemark>5</footnotemark> Ga-nias was present at his office during the creation of the mirrors, spoke with the agents, and was aware that mirrored copies of his three hard drives had been created and taken off-site.<footnotemark>6</footnotemark> There is no dispute that the forensic mirrors taken from Gani-as’s office contained all of the computerized data maintained by Ganias’s business, including not only material related to IPM or AB, but also Ganias’s own personal <page-number citation-index="1" label="203">*203</page-number>financial records, and the records of “many other” accounting clients of Ganias: businesses of various sorts having no connection to the Government’s criminal investigation.<footnotemark>7</footnotemark> J.A. 464, ¶ 14.</p>
<p id="b227-5">The next day, Agent Shaver consolidated the eleven mirrored hard drives from all three searches (including the three from Ganias’s office) onto a single external hard drive which he provided to Agent Conner. Agent Conner, in turn, provided this hard drive to the evidence custodian of the Army CID, who stored it at Fort Devens, Massachusetts. There the consolidated drive remained, unaltered and untouched, throughout the events relevant to this case. Around the same time, Agent Shaver created two additional copies of the mirrored drives on two sets of nineteen DVDs. After providing these DVD sets to Agent Conner, Agent Shaver then purged the external hard drives onto which he had originally written the mirrors. At this point, a week after the search, three complete copies of the mirrors of Ganias’s hard drives existed: an untouched copy stowe.d away in an evidence locker and two copies available for forensic analysis.<footnotemark>8</footnotemark></p>
<p id="b227-6">Though internal protocols required that specialized digital forensic analysts search the mirrored hard drives, the paper files were not subject to such limitations. Thus, shortly after the November 19 seizure, the Army CID agents began to analyze the non-digital files seized pursuant to' the warrant. These files suggested that IPM had made payments to a third company whose owner, according to the Connecticut Department of Labor, was a full-time employee of an insurance company who received no wages from any source other than that insurance company. This and other red flags spurred Agent Conner to contact the Criminal Investigation Division of the IRS, which subsequently joined the investigation.</p>
<p id="b227-9">In early February 2004, as he and his fellow agents continued to follow leads from the paper files, Agent Conner sent one of the two DVD sets containing the forensic mirrors to the Army Criminal Investigation Laboratory (“ACIL”) in Forest Park, Georgia, accompanied by a copy of one of the three search warrants..In early June, the ACIL assigned Gregory Norman, a digital evidence examiner, to perform a forensic analysis. Around the same time, Special Agent Michelle Chowaniec, who replaced Agent Conner as the primary case agent for the Army CID in late March, provided the second set of DVDs to the IRS agent assigned to the case, Special Agent Paul Holowczyk. Agent Ho-Iowczyk in turn, passed it on, by way of intermediaries, to Special Agent Vita Paukstelis, a computer investigative spe<page-number citation-index="1" label="204">*204</page-number>cialist. By the end of June 2004, computer experts for the Army CID and the IRS— Norman and Agent Paukstelis, respectively — had received copies of the digital evidence (which, as the district court found, were “encoded so that only agents with forensic software not directly available to the case agents could view [them],” <em>Gañí-as, </em><span class="citation no-link">2011 WL 2532396</span>, at *7), and forensic examination began.</p>
<p id="b228-4">Norman commenced his analysis in late June by loading the eleven mirrored drives into EnCase — the same software with which Agent Shaver initially created the mirrors — so that he could search the data thereon. After looking at the search warrants, he created a number of keywords, with which he searched for potentially relevant data. Initially, the search returned far too many results for practicable review (more than 17,000 hits); thus, Norman requested new keywords from Agent Cho-waniec. On the basis of these new keywords, he was able to narrow his search and ultimately identify several files he thought might be of interest to the investigation, all of which he put on a single CD.<footnotemark>9</footnotemark> Some of these files he was able personally to examine, to determine whether they were responsive to the warrant; a few (including the QuickBooks file labeled “Steve_ga.qbw,” which was ultimately searched pursuant to the 2006 warrant, J.A. 467) Norman could not open without a specific software edition of QuickBooks to which he did not have immediate access. However, as these files (like the others) contained keywords that were taken from the narrower list and generated on the basis of the warrant, Norman included the QuickBooks files in the CD he ultimately sent to Agent Chowaniec along with a report.<footnotemark>10</footnotemark> On July 23, 2004, Chowaniec received this CD. Norman, in turn, returned the nineteen DVDs to Army CID’s evidence custodian in Boston for safekeeping.</p>
<p id="b228-7">Norman’s counterpart in the IRS, Agent Paukstelis — who, in addition to receiving the search warrant with her set of DVDs, also received a list of companies, addresses, and key individuals relating to the investigation, along with “a handwritten notation next to the name ‘Taxes International’ that stated ‘(return preparer) do not search,’ ” <em>Ganias, </em><span class="citation no-link">2011 WL 2532396</span>, at *3 — conducted her analysis over a period of about four months. Because she worked for the IRS, she limited her search to the three mirrored drives from Taxes International. Though Agent Paukstelis used ILook, a different software program, to review the mirrored hard drives, she too could not open Quick-Books files without the relevant proprietary software. Still, though she could not open these files, she believed, based on the information to which she had access, that they were within the scope of the warrant; thus, in October 2004, she copied this data, in concert with other responsive data, onto a CD, three copies of which she sent to Agent Holowczyk and Special Agent Amy Hosney, also with the IRS. In light of the note she had received with her DVD set as well as the list of relevant entities, Agent Paukstelis avoided, to the degree she could, searching any files of Taxes International that did not appear to be directly relevant to that list. On November 30, 2004, Paukstelis also provided a “restoration” of the mirrors of the Taxes International hard drives to Special Agent <page-number citation-index="1" label="205">*205</page-number>George Francischelli, an IRS computer specialist assigned to the case.<footnotemark>11</footnotemark></p>
<p id="b229-5">Agents Chowaniec and Conner, after receiving Norman’s CD and report in late July, conducted initial reviews of the data. Like Norman and Agent Paukstelis, however, they could not open the QuickBooks files. At the same time, the agents were busy, in the words of Agent Chowaniec, “tracking down other leads[,] ... [issuing] grand jury subpoenas, ... doing interviews of subcontractors and identifying subcontractors from the papers that [the agents had] received from the search warrants.” J.A. 294-95. In October, Agents Hosney and Chowaniec attempted, together, to review the QuickBooks files, but again lacked the relevant software to do so. Finally, in November 2004, Agent Cho-waniec, having acquired the appropriate software, opened two IPM QuickBooks files on her office computer, and then in December, Agents Hosney and Chowaniec, using the restoration provided by Agent Paukstelis, looked at additional IPM QuickBooks files. Though they had the entirety of the mirrored data before them (the only time throughout the investigation that the case agents had direct access to a software interface permitting them to view essentially all of the data stored on the mirrors), they carefully limited their search: Agent Hosney testified that they “only looked at the QuickBooks files for Industrial Property Management and American Boiler ... [b]eeause those were the only two companies named in the search warrant attachment.” J.A. 340. They did, however, observe that other files existed — both on the CD Norman had provided and on the restoration — in particular, the files Agent Hosney ultimately searched in 2006.</p>
<p id="b229-9">Ganias contends that there is no dispute that by this point, the agents had finished “identifying and segregating the files within the November 2003 warrant’s scope.” Appellant Reply Br. at 5. In actuality, the record is unclear as to whether the forensic examination of the mirrored computers pursuant to the initial search warrant had indeed concluded as a forward-looking matter, rather than from the perspective of hindsight.<footnotemark>12</footnotemark> The district court did not find any facts decisive to this question. It is, further, undisputed that the investigation into McCarthy, IPM, and AB was ongoing at this time, and that this investigation would culminate in an indictment of McCarthy in 2008 secured in large part <page-number citation-index="1" label="206">*206</page-number>through reliance on evidence responsive to the 2003 warrant and located on the mirrored copies of Ganias’s hard drives. <em>See </em>Indictment, <em>United States v. McCarthy, </em>No. 3:08cr224 (EBB) (D. Conn. Oct. 31, 2008), EOF No. 1. When asked why, at this time or any time later, Agent Conner did not return or destroy the data stored on the mirrors that did not appear directly to relate to the crimes alleged in the warrant, Agent Conner explained that “[the] investigation was still ... open” and that, generally, items would be “released back to the owner” once an investigation was closed. J.A. 123. He further noted that the Army CID “would not routinely go into DVDs to delete data, as we’re altering the original data that was seized.” J.A. 122.<footnotemark>13</footnotemark></p>
<p id="b230-7">Over the next year, the agents continued to investigate IPM and AB. Analysis of the paper files taken pursuant to the November 2003 search warrant revealed potential errors in AB’s tax returns that seemed to omit income reflected in checks deposited into IPM’s account. Aware that Ganias had prepared these tax returns and deposited the majority of these checks, Agent Hos-ney came to suspect that Ganias was engaged in tax-related crimes.<footnotemark>14</footnotemark> She did not, however, return to the restoration or otherwise open any of Ganias’s digital financial documents or files associated with <page-number citation-index="1" label="207">*207</page-number>Taxes International.<footnotemark>15</footnotemark> Instead, Agent Hos-ney subpoenaed Ganias’s bank records from 1999 to 2003 and accessed his income tax returns for the same period. On July 28, 2005, the IRS — believing Ganias to be involved both personally and as an accomplice or co-conspirator in tax evasion— officially expanded the investigation to include him.</p>
<p id="b231-5">On February 14, 2006, Ganias, accompanied by his lawyer, met in a proffer session with Agent Hosney and others involved in the investigation.<footnotemark>16</footnotemark> That' day or shortly thereafter, Agent Hosney asked Ganias for consent to access his personal QuickBooks files and those of his business, Taxes International — data Agent Hosney knew to be present on the forensic mirrors but which she had not accessed. When, by April 24, 2006 (two and a half months later), Ganias had failed to respond (either by consenting, objecting, or filing a motion under Federal Rule of Criminal Procedure 41(g) for return of seized property), Agent Hosney sought a search warrant to search the mirrored drives again.<footnotemark>17</footnotemark> In her search warrant affidavit, Agent Hosney pointed to bank records, income tax forms, and additional evidence to demonstrate that she had probable cause to believe that Ganias had violated <span class="citation no-link">26 U.S.C. § 7201</span> (by committing tax evasion) and § 7206(1) (by making false declarations).<footnotemark>18</footnotemark> She further noted that the items to be searched were “mirror images of computers seized on November 19, 2003 from the offices of Taxes International,” J.A. 461, ¶ 7; that information material to the initial investigation had been located on these mirrors and that, “[djuring th[at] investigation,” such information had been “analyzed in detail,” J.A. 464, ¶ 15; that Ganias was not, at the time of the initial seizure, under investigation, J.A. 461, ¶ 3 (“On July 28, 2005, the Government’s investigation was expanded to include an examination of whether Ganias, McCarthy’s accountant and former IRS Revenue ‘Agent, violated the federal tax laws.”); and thus that, though Agent Hos-ney believed that the second mirrored drive, called Taxlnt_2, was “the primary computer for Taxes International,” J.A. 463, ¶ 13, she could not search Ganias’s personal or business files as “[p]ursuant to the 2003 search warrant, only files for [AB] and IPM could be viewed,” J.A. 464, ¶ 14. The magistrate judge issued the warrant, Agent Hosney searched the referenced data, and ultimately the Government indicted Ganias for tax evasion.</p>
<p id="b231-9">B. Procedural History</p>
<p id="b231-10">In February 2010, Ganias moved to suppress the evidence Agent Hosney acquired pursuant to the 2006 warrant. After a two-<page-number citation-index="1" label="208">*208</page-number>day hearing, the district court denied the motion on April 14, 2010, and issued a written decision on June 24, 2011. In that decision, the district court found, <em>inter alia, </em>that the forensic examination of the mirrored drives “was conducted within the limitations imposed by the [2003] warrant” and that “[a] copy of the evidence was preserved in the form in which it was taken.” <em>Ganias, </em><span class="citation no-link">2011 WL 2532396</span>, at *8. Judge Thompson observed that Ganias “never moved for destruction or return of the data, which could have led to the seized pertinent data being preserved by other means.” <em><span class="citation no-link">Id.</span> </em>The district court concluded that the Government’s retention of the mirrored drives' — and thus its subsequent search of those drives pursuant to a warrant — did not violate the Fourth Amendment. Having found no Fourth Amendment violation, the district court did not reach the question of good faith. <span class="citation no-link"><em>Id. </em>at *9</span>.</p>
<p id="b232-4">At trial, the Government introduced information in Ganias’s QuickBooks files as evidence against him, in particular highlighting the fact that payments made to him by clients such as IPM were characterized as “owner’s contributions,” which prevented QuickBooks from recognizing them as income.<footnotemark>19</footnotemark> On the basis of this and other evidence, the jury convicted Ganias of two counts of tax evasion, and the district court sentenced him to two terms of 24 months’ incarceration, to be served concurrently.</p>
<p id="b232-8">Ganias appealed. On review of his conviction, a panel of this Court concluded, unanimously, that the Government had violated the Fourth Amendment; in a divided decision, the panel then ordered suppression of the evidence obtained in executing the 2006 warrant and vacated the jury verdict. We subsequently ordered this rehearing <em>en banc </em>in regards to, first, the existence of a Fourth Amendment violation and, second, the appropriateness of suppression.<footnotemark>20</footnotemark></p>
<p id="b232-9">II</p>
<p id="b232-10">“On appeal from a district court’s ruling on a motion to suppress evidence, ‘we review legal conclusions de novo and findings of fact for clear error.’ ” <em>United States v. Bershchansky, </em><span class="citation" data-id="8413470"><a href="/opinion/8442239/united-states-v-bershchansky/#108" aria-description="Citation for case: United States v. Bershchansky">788 F.3d 102, 108</a></span> (2d Cir. 2015) (quoting <em>United States v. Freeman, 735 </em>F.3d 92, 95 (2d Cir. 2013)). We may uphold the validity of a judgment “on any ground that finds support in the record.” <em>Headley v. Tilghman, </em><span class="citation" data-id="695149"><a href="/opinion/695149/andrew-headley-v-lawrence-tilghman-warden-connecticut-correction/#476" aria-description="Citation for case: Andrew Headley v. Lawrence Tilghman, Warden, Connecticut...">53 F.3d 472, 476</a></span> (2d Cir. 1995).</p>
<p id="b232-11">The district court concluded that the conduct of the agents in this case comported fully with the Fourth Amendment, and <page-number citation-index="1" label="209">*209</page-number>thus did not reach the question whether they also acted in good faith. Because we conclude that the agents acted in good faith, we need not decide whether a Fourth Amendment violation occurred. We thus affirm the district court on an alternate ground. Nevertheless, though we offer no opinion on the existence of a Fourth Amendment violation in this case, we make some observations bearing on the reasonableness of the agents’ actions, both to illustrate the complexity of the questions in this significant Fourth Amendment context and to highlight the importance of careful consideration of the technological contours of digital search and seizure for future cases.</p>
<p id="b233-6">“The touchstone of the Fourth Amendment is reasonableness.... ” <em>United States v. Miller, </em><span class="citation" data-id="792539"><a href="/opinion/792539/united-states-v-alfred-g-miller/#97" aria-description="Citation for case: United States v. Alfred G. Miller">430 F.3d 93, 97</a></span> (2d Cir. 2005) (alteration omitted) (quoting <em>United States v. Knights, </em><span class="citation" data-id="9434170"><a href="/opinion/118468/united-states-v-knights/#118" aria-description="Citation for case: United States v. Knights">534 U.S. 112, 118</a></span>, <span class="citation" data-id="9434170"><a href="/opinion/118468/united-states-v-knights/" aria-description="Citation for case: United States v. Knights">122 S.Ct. 587</a></span>, <span class="citation" data-id="9434170"><a href="/opinion/118468/united-states-v-knights/" aria-description="Citation for case: United States v. Knights">151 L.Ed.2d 497</a></span> (2001)). As relevant here, “searches pursuant to a warrant will rarely require any deep inquiry into reasonableness.” <em>United States v. Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#922" aria-description="Citation for case: United States v. Leon">468 U.S. 897, 922</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">82 L.Ed.2d 677</a></span> (1984) (alteration omitted) (quoting <em>Illinois v. Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#267" aria-description="Citation for case: Illinois v. Gates">462 U.S. 213, 267</a></span>, <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">103 S.Ct. 2317</a></span>, <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">76 L.Ed.2d 527</a></span> (1983) (White, J., concurring in judgment)). Nevertheless, both the scope of a seizure permitted by a warrant,<footnotemark>21</footnotemark> and the reasonableness of government conduct in executing a valid warrant,<footnotemark>22</footnotemark> can present Fourth <page-number citation-index="1" label="210">*210</page-number>Amendment issues. Ganias thus argues that the Government violated the Fourth Amendment in this case, notwithstanding the two warrants that issued, by retaining complete forensic copies of his three hard drives during the pendency of its investigation.</p>
<p id="b234-4">According to Ganias, when law enforcement officers execute a warrant for a hard drive or forensic mirror that contains data that, as here, cannot feasibly be sorted into responsive and non-responsive categories on-site, “the Fourth Amendment demands, at the very least, that the officers expeditiously complete their off-site search and then promptly return (or destroy) files outside the warrant’s scope.”<footnotemark>23</footnotemark> Appellant Br. at 18. Arguing that a culling process took place here and that it had concluded by, at the latest, January 2005, Ganias faults the Government for retaining the mirrored drives — including storing one forensic copy in an evidence locker for safekeeping.<footnotemark>24</footnotemark> It was this retention, he argues, that constituted the Fourth Amendment violation — a violation that, in turn, made the 2006 search of the data itself unconstitutional as, but for this retention, the search could never have occurred.</p>
<p id="b234-10">To support this argument, Ganias relies principally on <em>United States v. Tamura, </em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">694 F.2d 591</a></span> (9th Cir. 1982), a Ninth Circuit case involving the search and seizure of physical records. In <em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">Tamura</a></span> </em>(unlike the present case, in which a warrant specifically authorized the agents to seize hard drives and to search them off-site) officers armed only with a warrant authorizing them to seize specific “records” instead seized numerous boxes of printouts, file <page-number citation-index="1" label="211">*211</page-number>drawers, and cancelled checks for off-site search and sorting. <span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/#594" aria-description="Citation for case: United States v. Leigh Raymond Tamura"><em>Id. </em>at 594-95</a></span>. After the officers had clearly sorted the responsive paper documents from the non-responsive ones, they refused — despite request — to return the non-responsive paper files. <span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/#596" aria-description="Citation for case: United States v. Leigh Raymond Tamura"><em>Id. </em>at 596-97</a></span>. The Ninth Circuit concluded that both the unauthorized seizure of voluminous material not specified in the warrant and the retention of the seized documents violated the Fourth Amendment.<footnotemark>25</footnotemark> <span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/#595" aria-description="Citation for case: United States v. Leigh Raymond Tamura"><em>Id. </em>at 595, 597</a></span>; <em>see also Andresen v. Maryland, </em><span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">427 U.S. 463</a></span>, 482 n. 11, <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">96 S.Ct. 2737</a></span>, <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">49 L.Ed.2d 627</a></span> (1976) (“[W]e observe that to the extent [seized] papers were not within the scope of the warrants or were otherwise improperly seized, the State was correct in returning them voluntarily and the trial judge was correct in suppressing others.... In searches for papers, it is certain that some innocuous documents will be examined, at least cursorily, in order to determine whether they are, in fact, among those papers authorized to be seized.... [Responsible officials [conducting such searches], including judicial officials, must take care to assure that they are conducted in a manner that minimizes unwarranted intrusions upon privacy.”); <em>cf. United States v. Matias, </em><span class="citation" data-id="499737"><a href="/opinion/499737/united-states-v-miguel-matias-sr-jose-caraballo-miguel-matias-jr/#747" aria-description="Citation for case: United States v. Miguel Matias, Sr., Jose Caraballo,...">836 F.2d 744, 747</a></span> (2d Cir. 1988) (“[W]hen items outside the scope of a valid warrant are seized, the normal remedy is suppression and return of those items.... ”).</p>
<p id="b235-5">Because we resolve this case on good faith grounds, we need not decide the relevance, if any, of <em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">Tamura</a></span> </em>(or, more broadly, the validity of Ganias’s Fourth Amendment claim). We note, however, that there are reasons to doubt whether <em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">Tamura</a></span> </em>(to the extent we would indeed follow it) answers the questions before us. First, on its facts, <em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">Tamura</a></span> </em>is distinguishable from this case, insofar as the officers there seized for off-site review records that the warrant did not authorize them to seize,<footnotemark>26</footnotemark> and retained those records even after their return was requested. Here, in contrast, the warrant authorized the seizure of the hard drives, not merely particular records, and Ganias did not request return or destruction of the mirrors (even after he was indisputably alerted to the Government’s continued retention of them) by, for instance, filing a motion for such return pursuant to Federal Rule of Criminal Procedure 41(g). Second, and more broadly, even if the facts of <em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">Tamura</a></span> </em>were otherwise on point, Ganias’s invocation of <em>Ta-mura’s </em>reasoning rests on an analogy between paper files intermingled in a file cabinet and digital data on a hard drive. Though we do not take any position on the ultimate disposition of the constitutional questions herein, we nevertheless pause to address the appropriateness of this analogy, which is often invoked '(including by the dissent) and bears examination.</p>
<p id="b235-9">The central premise of Ganias’s reliance on <em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">Tamura</a></span> </em>is that the search of a digital storage medium is analogous to the search of a file cabinet. The analogy has some force, particularly as seen from the perspective of the affected computer user. Computer users — or at least, average users (in contrast to, say, digital forensics experts) — typically experience computers as filing cabinets, as that is precisely how <page-number citation-index="1" label="212">*212</page-number>user interfaces are designed to be perceived by such users.<footnotemark>27</footnotemark> Given that the file cabinet analogy (at least largely) thus captures an average person’s subjective experience with a computer interface, the analogy may shed light on a user’s subjective expectations of privacy regarding data maintained on a digital storage device. Because we experience' digital files as discrete items, and because we navigate through a computer as through a virtual storage space, we may expect the law similarly to treat data on a storage device as comprised of distinct, severable files, even if, in fact, “[sjtorage media do not naturally divide into parts.” Josh Goldfoot, <em>The Physical Computer and the Fourth Amendment, </em>16 Berkeley J. Crim. L. 112, 131 (2011). In this case, for example, a person in Ganias’s situation could well understand the “files” on his hard drives containing information relating to IPM and AB as separate from the “files” containing his personal financial information and that of other clients. Indeed, the very fact that the Government sought additional search authorization via the 2006 warrant when it established probable cause to search Gani-as’s personal files indicates that the Government too understood — and credited— this distinction.</p>
<p id="b236-7">That said, though it may have some relevance to our inquiry, the file cabinet analogy is only that — an analogy, and an imperfect one. <em>Cf. </em>James Boyle, <em>The Public Domain </em>107 (2008) (“Analogies are only bad when they ignore the key difference between the two things being analyzed.”). Though to a user a hard drive may seem like a file cabinet, a digital forensics expert reasonably perceives the hard drive simply as a coherent physical storage medium for digital data^ — data that is interspersed <em>throughout </em>the medium, which itself must be maintained and accessed with care, lest this data be altered or destroyed.<footnotemark>28</footnotemark> <em>See </em><page-number citation-index="1" label="213">*213</page-number>Goldfoot, <em>supra, </em>at 114 (arguing digital storage media are physical objects like “drugs, blood, or clothing”); Wayne Jekot, <em>Computer Forensics, Search Strategies, and the Particularity Requirement, </em>7 U. Pitt. J. Tech. L. &amp; Pol'y, art. 5, at 1, 30 (2007) (“[A] computer does not simply hold data, it is <em>composed </em>of data.”). Even the most conventional “files” — word documents and spreadsheets such as those the Government searched in this case — are not maintained, like files in a file cabinet, in discrete physical locations separate and distinct from other files. They are in fact “fragmented” on a storage device, potentially across physical locations. Jekot, <em>supra, </em>at 13. “Because of the manner in which data is written to the hard drive, rarely will one file be stored intact in one place on a hard drive,” <em>id.; </em>so-called “files” are stored in multiple locations and in multiple forms, <em>see </em>Goldfoot, <em>supra, </em>at 127-28.<footnotemark>29</footnotemark> And as a corollary to this fragmentation, the computer stores unseen information about any given “file”' — not only meta-data about when the file was created or who created it, <em>see </em>Michael W. Graves, <em>Digital Archaeology: The Art and Science of Digital Forensics </em>94-95 (2014), but also prior versions or edits that may still exist “in the document or associated temporary files on [the] disk” — further interspersing the data corresponding to that “file” across the physical storage medium, Eoghan Casey, <em>Digital Evidence and Computer Crime </em>507 (3d ed. 2011).</p>
<p id="b237-7">“Files,” in short, are not as discrete as they may appear to a user. Their interspersion throughout a digital storage medium, moreover, may affect the degree to which it is feasible, in a case involving search pursuant to a warrant, to fully extract and segregate responsive data from non-responsive data. To be clear, we do not suggest that it is impossible to do so in any particular or in every case; we emphasize only that in assessing the reasonableness, for Fourth Amendment purposes, of the search and seizure of digital evidence, we must be. attuned to the technological features unique to digital media as a whole and to those relevant in a particular case— features that simply do not exist in the context of paper files.</p>
<p id="b237-8">These features include an additional complication affecting the validity of the file cabinet analogy: namely, that a good deal of the information that a forensic examiner may seek on a digital storage device (again, because it is a coherent and complex forensic object and not a file cabinet) does not even remotely fit into the typical user’s conception of a “file.” <em>See </em>Daniel B. Garrie <em>&amp; </em>Francis M. Allegra, Fed. Judicial Ctr., <em>Understanding Software, the Internet, Mobile Computing, and the Cloud: A Guide for Judges </em>39 (2015) (“Forensic software gives a forensic examiner access to electronically stored information (ESI) that is otherwise unavailable to a typical computer user.”). Forensic investigators may, <em>inter alia, </em>search for and discover evidence that a file was <page-number citation-index="1" label="214">*214</page-number>deleted as well as evidence sufficient to reconstruct a deleted file — evidence that can exist in so-called “unallocated” space on a hard drive. <em>See </em>Casey, <em>supra, </em>at 496; Orin S. Kerr, <em>Searches and Seizures in a Digital World, </em><span class="citation no-link">119 Harv. L. Rev. 531</span>, 542, 545 (2005); Fed. Judicial Ctr., <em>supra, </em>at 40 (“A host of information can lie in the interstices between the allocated spaces.”). They may seek responsive metadata about a user’s activities, or the manner in which information has been stored, to show such things as knowledge or intent, or to create timelines as to when information was created or accessed.<footnotemark>30</footnotemark> Forensic examiners will sometimes seek evidence on a storage medium that something <em>did not happen: </em>“If a defendant claims he is innocent because a computer virus committed the crime, the absence of a virus on his hard drive is ‘dog that did not bark’ negative evidence that disproves his story.... To prove something is not on a hard drive, it is necessary to look at every place on the drive where it might be found and confirm it is not there.”<footnotemark>31</footnotemark> Goldfoot, <em>supra, </em>at 141; <em>see also United States v. O’Keefe, </em><span class="citation" data-id="77425"><a href="/opinion/77425/united-states-v-michael-aaron-okeefe/#1341" aria-description="Citation for case: United States v. Michael Aaron O&#x27;Keefe">461 F.3d 1338, 1341</a></span> (11th Cir. 2006) (“[The government’s expert] testified that the two viruses he found on [the defendant’s] computer were not capable of ‘downloading and uploading child pornography and sending out advertisements.’ ”).<footnotemark>32</footnotemark></p>
<p id="b239-4"><page-number citation-index="1" label="215">*215</page-number>Finally, because of the complexity of the data thereon and the manner in which it is stored, the nature of digital storage presents potential challenges to parties seeking to preserve digital evidence, authenticate it at trial, and establish its integrity for a fact-finder — challenges that materially differ from those in the paper file context. First, the extraction of specific data files to some other medium can alter, omit, or even destroy portions of the information contained in the original storage medium. Preservation of the original medium or a complete mirror may therefore be necessary in order to safeguard the integrity of evidence that has been lawfully obtained or to authenticate it at trial. Graves, <em>supra, </em>at 95-96 (“[The investigator] must be able to prove that the information presented came from where he or she claims and was not altered in any way during examination, and that there was no opportunity for it to have been replaced or altered in the interim.”); <em>see also </em>Casey, <em>supra, </em>at 480 (“Even after copying data from a computer or piece of storage media, digital investigators generally retain the original evidential item in a secure location for future reference.”).<footnotemark>33</footnotemark> The preservation of data, moreover, is not simply a concern for law enforcement. Retention of the original storage medium or its mirror may also be necessary to afford criminal defendants access to that medium or its forensic copy so that, relying on forensic experts of their own, they may challenge the authenticity or reliability of evidence allegedly retrieved. <em>See, e.g., United States v. Kimoto, </em><span class="citation" data-id="1311543"><a href="/opinion/1311543/united-states-v-kimoto/#480" aria-description="Citation for case: United States v. Kimoto">588 F.3d 464, 480</a></span> (7th Cir. 2009) (quoting the defendant’s motion as stating: “Upon beginning their work, [digital analysis experts] advised [the defendant’s] Counsel that the discovery provided to the defense did not appear to be a complete forensic copy, and that such was necessary to verify the data as accurate and unaltered.”).<footnotemark>34</footnotemark> Defendants may also require access to a forensic copy to conduct an independent analysis of precisely what the government’s forensic expert did — potentially altering evidence in a manner material to the case — or to locate exculpatory evidence that the government missed.<footnotemark>35</footnotemark></p>
<p id="b240-3"><page-number citation-index="1" label="216">*216</page-number>Notwithstanding any other distinctions between this ease and <em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">Tamura</a></span>, </em>then, the Government plausibly argues that, because digital storage media constitute coherent forensic objects with contours more complex than — and materially distinct from— file cabinets containing interspersed paper documents, a digital storage medium or its forensic copy may need to be retained, during the course of an investigation and prosecution, to permit the accurate extraction of the primary evidentiary material sought pursuant to the warrant; to secure metadata and other probative evidence stored in the interstices of the storage medium; and to preserve, authenticate, and effectively present at trial the evidence thus lawfully obtained. To be clear, we do not decide the ultimate merit of this argument as applied to the circumstances of this case.<footnotemark>36</footnotemark> Nor do we gainsay the <page-number citation-index="1" label="217">*217</page-number>privacy concerns implicated when the government retains a hard drive or forensic mirror containing personal information irrelevant to the ongoing investigation, even if such information is never viewed. We discuss the aptness and limitations of Gani-as’s analogy and the Government’s response simply to highlight the complexity of the relevant questions for future cases and to underscore the importance, in answering such questions, of engaging with the technological specifics.<footnotemark>37</footnotemark></p>
<p id="b241-5">In emphasizing such specifics, we reiterate that we do not mean to thereby minimize or ignore the privacy concerns implicated when a hard drive or forensic mirror is retained, even pursuant to a warrant. The seizure of a computer hard drive, and its subsequent retention by the government, can give the government possession of a vast trove of personal information about the person to whom the drive belongs, much of which may be entirely irrelevant to the criminal investigation that led to the seizure. Indeed, another weakness of the file cabinet analogy is that no file cabinet has the capacity to contain as much information as the typical computer hard drive. In 2005, Professor Orin Kerr noted that the typical personal computer hard drive had a storage capacity of about eighty gigabytes, which he estimated could hold text files equivalent to the “information contained in the books on one floor of a typical academic library.” Kerr, <em>Searches and Seizures in a Digital World, supra, </em>at <page-number citation-index="1" label="218">*218</page-number>542. By 2011, computers were being sold with one terabyte of capacity — about twelve times the size of Professor Kerr’s library floor. Paul Ohm, Response, <em>Massive Hard Drives, General Warrants, and the Power of Magistrate Judges, </em>97 Va. L. Rev. In Brief 1, 6 (2011). The <em>New York Times </em>recently reported that commercially available storage devices can hold “16 pe-tabytes of data, roughly equal to 16 billion thick’books.” Quentin Hardy, As <em>a Data Deluge Grows, Companies Rethink Storage, </em>N.Y. Times, Mar. 15, 2016, at B3.</p>
<p id="b242-4">Moreover, quantitative measures fail to capture the significance of the data kept by many individuals on their computers. Tax records, diaries, personal photographs, electronic books, electronic media, medical data, records of internet searches, banking and shopping information — all may be kept in the same device, interspersed among the evidentiary material that justifies the seizure or search. <em>Cf. Riley v. California, </em>— U.S. -, <span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/#2489" aria-description="Citation for case: Riley v. Cal. United States">134 S.Ct. 2473, 2489-90</a></span>, <span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">189 L.Ed.2d 430</a></span> (2014) (explaining that even microcomputers, such as cellphones, have “immense storage capacity” that may contain “every piece of mail [people] have received for the past several months, every picture they have taken, or every book or article they have read,” which can allow the “sum of an individual’s private life [to] be reconstructed”); <em>United States v. Galpin, </em><span class="citation" data-id="931473"><a href="/opinion/931473/united-states-v-galpin/#446" aria-description="Citation for case: United States v. Galpin">720 F.3d 436, 446</a></span> (2d Cir. 2013) (“[Advances in technology and the centrality of computers in the lives of average people have rendered the computer hard drive akin to a residence in terms of the scope and quantity of private information it may contain.”). While physical searches for paper records or other evidence may require agents to rummage at least cursorily through much private material, the reasonableness of seizure and subsequent retention by the government of such vast quantities of irrelevant private material was rarely if ever presented in cases prior to the age of digital storage, and has never before been considered justified, or even practicable, in such cases. Even as we recognize that search and seizure of digital media is, in some ways, distinct from what has come before, we must remain mindful of the privacy interests that necessarily inform our analysis.<footnotemark>38</footnotemark></p>
<p id="b242-9">We note, however, that parties with an interest in retained storage media are not without recourse. As noted above, Ganias never sought the return of any seized material, either by negotiating 'with the Government or by motion to the court. Though negotiated stipulations regarding the admissibility or integrity of evidence may not always suffice to satisfy reasonable interests of the government in retention during the pendency of an investigation,<footnotemark>39</footnotemark> such <page-number citation-index="1" label="219">*219</page-number>stipulations may make return feasible in a proper case, and can be explored.</p>
<p id="b243-5">A person from whom property is seized by law enforcement may move for its return under Federal Rule of Criminal Procedure 41(g).<footnotemark>40</footnotemark> Rule 41(g) permits a defendant or any “person aggrieved” by either an unlawful or <em>lawful </em>deprivation of property, <em>see United States v. Comprehensive Drug Testing, Inc., </em><span class="citation" data-id="9438359"><a href="/opinion/175207/united-states-v-comprehensive-drug-testing-inc/#1173" aria-description="Citation for case: United States v. Comprehensive Drug Testing, Inc.">621 F.3d 1162, 1173</a></span> (9th Cir. 2010) (en banc) (per curiam), to move for its return, Fed. R. Crim. P. 41(g). Evaluating such a motion, a district court “must receive evidence on any factual issue necessary to decide the motion,” and, in the event that the motion is granted, may “impose reasonable conditions to protect access to the property and its use in later proceedings.” <em><span class="citation" data-id="9438359"><a href="/opinion/175207/united-states-v-comprehensive-drug-testing-inc/" aria-description="Citation for case: United States v. Comprehensive Drug Testing, Inc.">Id.</a></span> </em>Since we resolve this case on other grounds, we need not address whether Ganias’s failure to make such a motion forfeited any Fourth Amendment objection he might otherwise have had to the Government’s retention of the mirrors. But we agree with the district court that, as a pragmatic matter, such a motion “would have given a court the opportunity to consider ‘whether the government’s interest could be served by an alternative to retaining the property,’ and perhaps to order the [mirrors] returned to Ganias, all while enabling the court to ‘impose reasonable conditions to protect access to the property and its use in later proceedings.’ ” <em>Ganias, </em><span class="citation no-link">2011 WL 2532396</span>, at *8 (citation omitted) (first quoting <em>In re Smith, 888 </em>F.2d 167, 168 (D.C. Cir. 1989) (per curiam); then quoting Fed. R. Crim. P. 41(g)).</p>
<p id="b243-11">Rule 41(g) thus provides a potential mechanism, in at least some contexts, for dealing with the question of retention at a time when the government may be expected to have greater information about the data it seeks and the best process through which to search and present that data in court. It is worth observing, then, that Rule 41(g) constitutes a statutory solution (as opposed to a purely judicially constructed one) to at least one facet of the retention problem.<footnotemark>41</footnotemark> Statutory approaches, of course, do not relieve courts from their obligation to interpret the Constitution; nevertheless, such approaches have, historically, provided one mechanism for safeguarding privacy interests while, at the same time, addressing the needs of law enforcement in the face of technological change. Indeed, when Congress addressed wiretapping in the Omnibus Crime Control <page-number citation-index="1" label="220">*220</page-number>and Safe Streets Act of 1968, the Senate Judiciary Committee issued a report reflecting precisely this ambition — to provide a framework through which law enforcement might comport with the demands of the Constitution and meet important law enforcement interests. <em>See </em>S. Rep. No. 90-1097, at 66-76 (1968) (describing the construction of the then-Omnibus Crime Control and Safe Streets of Act of 1967, which laid out comprehensive rules for when and how law enforcement could intercept wire and oral communications through electronic surveillance, as a Congressional attempt to respond to and synthesize, first, technological change, <em>id. </em>at 67, second, ineffective or unclear state statutory regimes, <em>id. </em>at 69, third, evolving Supreme Court precedent, <em>id. </em>at 74-75, and fourth, law enforcement concerns, <em>id. </em>at 70); <em>see also id. </em>at 66 (“Title III has as its dual purpose (1) protecting the privacy of wire and oral communications, and (2) delineating on a uniform basis the circumstances and conditions under which the interception of wire and oral communications may be author-izecl.”). The Act did not seek to supplant the role of the courts, nor could it have done so, but it did demonstrate the intuitive proposition that Congress can and should be a partner in the process of fleshing out the contours of law-enforcement policy in a shifting technological landscape. In acknowledging the role of Rule 41(g), then, we seek also to suggest that search and seizure of electronic media may, no less than wiretapping, merit not only judicial review but also legislative analysis; courts need not act alone.</p>
<p id="b244-6">As we have said, we need not resolve the ultimate question whether the Government’s retention of forensic copies of Gani-as’s hard drives during the pendency of its investigation violated the Fourth Amendment. We conclude, moreover, that we should not decide this question on the present record, which does not permit a full assessment of the complex and rapidly evolving technological issues, and the significant privacy concerns, relevant to its consideration.<footnotemark>42</footnotemark> Having noted Ganias’s ar<page-number citation-index="1" label="221">*221</page-number>gument, we do not decide its merits. We instead turn to the question of good faith.</p>
<p id="b245-4">Ill</p>
<p id="b245-5">The Government argues that, because it acted in good faith throughout the pen-dency of this case, any potential violation of the Fourth Amendment does not justify the extraordinary remedy of suppression. <em>See Davis v. United States, </em><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/#237" aria-description="Citation for case: Davis v. United States">564 U.S. 229, 237</a></span>, <span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">131 S.Ct. 2419</a></span>, <span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">180 L.Ed.2d 285</a></span> (2011) (noting the “heavy toll” exacted by suppression, which “requires courts to ignore reliable, trustworthy evidence,” and characterizing suppression as a “bitter pill,” to be taken “only as a ‘last resort’ ” (quoting <em>Hudson v. Michigan, </em><span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/#591" aria-description="Citation for case: Hudson v. Michigan">547 U.S. 586, 591</a></span>, <span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/" aria-description="Citation for case: Hudson v. Michigan">126 S.Ct. 2159</a></span>, <span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/" aria-description="Citation for case: Hudson v. Michigan">165 L.Ed.2d 56</a></span> (2006))); <em>accord United States v. Clark, </em><span class="citation" data-id="206195"><a href="/opinion/206195/united-states-v-clark/#99" aria-description="Citation for case: United States v. Clark">638 F.3d 89, 99</a></span> (2d Cir. 2011). In particular, the Government urges that its “reliance on the 2006 warrant,” which it obtained after disclosing to the magistrate judge all relevant facts regarding its retention of the mirrored files, “fits squarely within the traditional <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>exception for conduct taken in reliance on a search warrant issued by a neutral and detached magistrate judge.”<footnotemark>43</footnotemark> Government Br. at 59; <em>see Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#922" aria-description="Citation for case: United States v. Leon">468 U.S. at 922</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span>. For the following reasons, we agree.</p>
<p id="b245-8">In <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>, </em>the Supreme Court determined that the exclusion of evidence is inappropriate when the government acts “in objectively reasonable reliance” on a search warrant, even when the warrant is subsequently invalidated. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#922" aria-description="Citation for case: United States v. Leon">468 U.S. at 922</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span>; <em>see also Clark, </em><span class="citation" data-id="206195"><a href="/opinion/206195/united-states-v-clark/#100" aria-description="Citation for case: United States v. Clark">638 F.3d at 100</a></span> (“[I]n <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>, </em>the Supreme Court strongly signaled that most searches conducted pursuant to a warrant would likely fall within its protection.”). Such reliance, however, must be <em>objectively reasonable. See Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#922" aria-description="Citation for case: United States v. Leon">468 U.S. at 922-23</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span> (“[I]t is clear that in some circumstances the officer will have no reasonable grounds for believing that the warrant was properly issued.” (footnote omitted)). Thus, to assert good faith reliance successfully, officers must, <em>inter alia, </em>disclose all potentially adverse information to the issuing judge. <em>See United States v. Reilly, </em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/#1280" aria-description="Citation for case: United States v. Kevin C. Reilly">76 F.3d 1271, 1280</a></span> (2d Cir.) (“The good faith exception to the exclusionary rule does not protect searches by officers who fail to provide all potentially adverse information to the issuing judge.... ”), <em>aff'd and amended, </em><span class="citation multiple-matches"><a href="/c/F.3d/91/331/">91 F.3d 331</a></span> (2d Cir. 1996) (per curiam); <em>see also United States v. Thomas, </em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/#1368" aria-description="Citation for case: United States v. Thomas">757 F.2d 1359, 1368</a></span> (2d Cir. 1985) (finding good faith reliance on a warrant, under <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>, </em>where officers, first, committed a constitutional violation they did not <page-number citation-index="1" label="222">*222</page-number>reasonably know, at the time, was unconstitutional — a warrantless canine sniff— and second, in relying on evidence from this sniff in a warrant application, fully revealed the fact of the canine sniff to a magistrate judge), <em>cert. denied by Fisher v. United States, </em><span class="citation" data-id="9049107"><a href="/opinion/9055582/fisher-v-united-states/" aria-description="Citation for case: Fisher v. United States">474 U.S. 819</a></span>, <span class="citation" data-id="9049105"><a href="/opinion/9055580/coronel-quintana-v-united-states/" aria-description="Citation for case: Coronel-Quintana v. United States">106 S.Ct. 66</a></span>, <span class="citation" data-id="9049110"><a href="/opinion/9055585/mcmahon-v-green/" aria-description="Citation for case: McMahon v. Green">88 L.Ed.2d 54</a></span> (1985) <em>and Rice v. United States, </em><span class="citation" data-id="9057476"><a href="/opinion/9063854/rice-v-united-states/" aria-description="Citation for case: Rice v. United States">479 U.S. 818</a></span>, <span class="citation" data-id="9057476"><a href="/opinion/9063854/rice-v-united-states/" aria-description="Citation for case: Rice v. United States">107 S.Ct. 78</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/93/34/">93 L.Ed.2d 34</a></span> (1986).</p>
<p id="b246-4">Ganias argues that reliance on the 2006 warrant is misplaced for two reasons. First, he urges that the alleged constitutional violation here (unlawful retention of the mirrored drives) had “long since” ripened into a violation by April 2006, when the second warrant was obtained, Appellant Br. at 55-56, and attests that “[n]oth-ing [in Leon] suggests that the police, <em>after </em>they engage in misconduct, can then ‘launder their prior unconstitutional behavior by presenting the fruits of it to a magistrate,’ ” <em>id. </em>at 56 (quoting <em>State v. Hicks, </em><span class="citation" data-id="1268637"><a href="/opinion/1268637/state-v-hicks/" aria-description="Citation for case: State v. Hicks">146 Ariz. 533</a></span>, <span class="citation" data-id="1268637"><a href="/opinion/1268637/state-v-hicks/#333" aria-description="Citation for case: State v. Hicks">707 P.2d 331, 333</a></span> (Ariz. Ct. App. 1985)). Second, Ganias argues that, even if “a subsequent warrant can ever appropriately purge the taint of an earlier violation, the agent must, at the very least, ‘provide all potentially adverse information’ regarding the earlier illegality ‘to the issuing [magistrate] judge,’” a requirement that he argues was not satisfied here. <em><span class="citation" data-id="1268637"><a href="/opinion/1268637/state-v-hicks/" aria-description="Citation for case: State v. Hicks">Id.</a></span> </em>at 58 (quoting <em>Reilly, </em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/#1280" aria-description="Citation for case: United States v. Kevin C. Reilly">76 F.3d at 1280</a></span>). Ganias’s arguments are unavailing.</p>
<p id="b246-5">First, Ganias relies on this Court’s decision in <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span> </em>to argue categorically that agents who have engaged in a predicate Fourth Amendment violation may not rely on a subsequently issued warrant to establish good faith. <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span>, </em>however, stands for no such thing. In <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span>, </em>officers unlawfully intruded on the defendant’s curtilage, discovering about twenty marijuana plants, before they departed and obtained a search warrant based on a “bare-bones” description of their intrusion and resulting observations which this Court found “almost calculated to mislead.” <em>Reilly, </em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/#1280" aria-description="Citation for case: United States v. Kevin C. Reilly">76 F.3d at 1280</a></span>; <em>see also <span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">id.</a></span> </em>(“[The affidavit] simply ... stated that [the officers] walked along Reilly’s property until they found an area where marijuana plants were grown. It did not describe this area to the Judge[,] ... [and it] gave no description of the cottage, pond, gazebo, or other characteristics of the area.... [The omitted information] was crucial. Without it, the issuing judge could not possibly make a valid assessment of the legality of the warrant that he was asked to issue.”). We rejected the government’s argument that the officers were entitled to rely on the warrant, noting that the officers had “undert[aken] a search that caused them to invade what they could not fail to have known was potentially ... curtilage,” and that they thereafter “failed to provide [the magistrate issuing the warrant] with an account of what they did,” so that the magistrate was unable to ascertain whether the evidence on which the officers relied in seeking the warrant was “itself obtained illegally and in bad faith.” <span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/#1281" aria-description="Citation for case: United States v. Kevin C. Reilly"><em>Id. </em>at 1281</a></span>. In such circumstances, <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>did not — and does not — permit good faith reliance on a warrant. <em>See Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#923" aria-description="Citation for case: United States v. Leon">468 U.S. at 923</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span> (observing that an officer’s reliance on a warrant is not <em>objectively reasonable </em>if he “misled [the magistrate with] information in an affidavit that [he] knew was false or would have known was false except for his reckless disregard of the truth”).</p>
<p id="b246-8">The present case, however, is akin not to <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span>, </em>but to this Court’s decision in <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span>, </em>which the <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span> </em>panel carefully distinguished, while reaffirming. <em>See Reilly, </em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/#1281" aria-description="Citation for case: United States v. Kevin C. Reilly">76 F.3d at 1281-82</a></span>. In <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span>, </em>an agent, acting without a warrant, used a dog trained to detect narcotics to conduct a “canine sniff’ at a dwelling. <span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/#1367" aria-description="Citation for case: United States v. Thomas">757 F.2d at 1367</a></span>. The agent presented evidence acquired as a result of the sniff to a “neutral <page-number citation-index="1" label="223">*223</page-number>and detached magistrate” who, on the basis of this and other evidence, determined that the officer had probable cause to conduct a subsequent search of the dwelling in question. <span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/#1368" aria-description="Citation for case: United States v. Thomas"><em>Id. </em>at 1368</a></span>. The defendant moved to suppress the evidence found in executing the search warrant, arguing that the antecedent canine sniff constituted a war-rantless, unconstitutional search and that the evidence acquired from that sniff was dispositive to the magistrate judge’s finding of probable cause. <span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/#1366" aria-description="Citation for case: United States v. Thomas"><em>See id. </em>at 1366</a></span>. This Court agreed on both counts: first deciding, as a matter of first impression in our Circuit, that the canine sniff at issue constituted a search, <span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/#1367" aria-description="Citation for case: United States v. Thomas"><em>id. </em>at 1367</a></span>, and second determining that, absent the evidence acquired from this search, the warrant was not supported by probable cause, <span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/#1368" aria-description="Citation for case: United States v. Thomas"><em>id. </em>at 1368</a></span>. The <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span> </em>panel nevertheless concluded that suppression was inappropriate because the agent’s reliance on the warrant was objectively reasonable: “The ... agent brought his evidence, including [a factual description of the canine sniff], to a neutral and detached magistrate. That magistrate determined that probable cause to search existed, and issued a search warrant. There is nothing more the officer could have or should have done under these circumstances to be sure his search would be legal.” <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Id.</a></span></em></p>
<p id="b247-4"><em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span> </em>carefully distinguished <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span>, </em>and in a manner that makes apparent that it is <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span> </em>that is dispositive here. First, the <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span> </em>panel noted that <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span> </em>was unlike <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span>, </em>in that the agent in <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span> </em>disclosed all crucial facts for the legal determination in question to the magistrate judge. <em>Reilly, </em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/#1281" aria-description="Citation for case: United States v. Kevin C. Reilly">76 F.3d at 1281</a></span>. Then, the <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span> </em>panel articulated another difference: while in <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span>, </em>“the officers undertook a search that caused them to invade what they could not fail to have known was potentially Reilly’s curtilage,” in <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span>, </em>the agent “did not have any significant reason to believe that what he had done [conducting the canine sniff] was unconstitutional.” <em>Id:, see also <span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">id.</a></span> </em>(“[U]ntil <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span> </em>was decided, no court in this Circuit had held that canine sniffs violated the Fourth Amendment.”). Thus, the predicate act in <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span> </em>tainted the subsequent search warrant, whereas the predicate act in <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span> </em>did not. The distinction did not turn on whether the violation found was <em>predicate, </em>or prior to, the subsequent search warrant on which the officers eventually relied, but on whether the officers’ reliance on the warrant was reasonable.</p>
<p id="b247-8">Contrary to Ganias’s argument, then, it is not the case that good faith reliance on a warrant is never possible in circumstances in which a predicate constitutional violation has occurred. The agents in <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span> </em>committed such a violation, but they had no “significant reason to believe” that their predicate act was indeed unconstitutional, <em>Reilly, </em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/#1281" aria-description="Citation for case: United States v. Kevin C. Reilly">76 F.3d at 1281</a></span>, and the issuing magistrate was apprised of the relevant conduct, so that the magistrate was able to determine whether any predicate illegality precluded issuance of the warrant. In such circumstances, invoking the good faith doctrine does not “launder [the agents’] prior unconstitutional behavior by presenting the fruits of it to a magistrate,” as Ganias suggests. Appellant Br. at 56 (quoting <em>Hicks, </em><span class="citation" data-id="1268637"><a href="/opinion/1268637/state-v-hicks/#333" aria-description="Citation for case: State v. Hicks">707 P.2d at 333</a></span>). In such cases, the good faith doctrine simply reaffirms <em>Leon's, </em>basic lesson: that suppression is inappropriate where reliance on a warrant was “objectively reasonable.” <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#922" aria-description="Citation for case: United States v. Leon">468 U.S. at 922</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span>.<footnotemark>44</footnotemark></p>
<p id="b248-3"><page-number citation-index="1" label="224">*224</page-number>Such is the case here. First, Agent Hosney provided sufficient information in her affidavit to apprise the magistrate judge of the pertinent facts regarding the retention of the mirrored copies of Gani-as’s hard drives — the alleged constitutional violation on which he relies. Agent Hosney explained that the mirror images in question had been “seized on November 19, 2003 from the offices of Taxes International,” J.A. 461, ¶ 7; that information material to the initial investigation of a third party had been located on the mirrors and “analyzed in detail,” J.A. 464, ¶ 15; that Ganias was not, at the time of the original seizure, under investigation, J.A. 461, ¶ 3; that, “[pjursuant to [that initial warrant],” Agent Hosney could not search Ganias’s personal or business files as the warrant authorized search only of “files for [AB] and IPM,” J.A. 464, ¶ 14; and that Gani-as’s personal data — which Agent Hosney was not authorized to search — was <em>on those mirrored drives, </em>J.A. 467, ¶ 27, and thus, <em>a fortiori, </em>had been there for the past two and a half years. The magistrate judge was thus informed of the fact that mirrors containing data non-responsive to the 2003 warrant had been retained for several years past the initial execution of that warrant and, to the degree it was necessary, that data responsive to the 2003 warrant had been analyzed in detail. The magistrate therefore had sufficient information on which to determine whether such retention precluded issuance of the 2006 warrant. <em>Cf. Thomas, </em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/#1368" aria-description="Citation for case: United States v. Thomas">757 F.2d at 1368</a></span> (“The magistrate, whose duty it is to interpret the law, determined that the canine sniff could form the basis for probable cause.... ”).</p>
<p id="b248-6">Ganias disagrees, arguing, in particular, that, though Agent Hosney alerted the magistrate that the mirrors had been retained for several years; that data responsive to the original warrant had been both located and extensively analyzed; and that those of Ganias’s QuickBooks files that Agent Hosney wanted to search were non-responsive to the original warrant, the Hosney affidavit did not go far enough in. that it failed to disclose that the agents “had been retaining the non-responsive records for a full 16 months <em>after </em>the files within the November 2003 warrant’s scope had been identified.” Appellant Br. at 60. As an initial matter, the Government <em>did </em>alert the magistrate that it had located responsive data on the mirrors <em>and </em>conducted extensive analysis of that responsive material, and it is not clear what else the Government should have said: the district court did not determine — nor does the record show — that by January 2005, as Ganias contends, the Government had determined, as a forward-looking matter, that it had performed all forensic searches of data responsive to the 2003 warrant that might prove necessary over the course of its investigation. <em>Compare </em>J.A. 322 (Q: “So it’s fair to say that as of mid-December [2004], your forensic analysis was completed at that time?” Agent Chowaniec: “That’s correct, of the computers.”), <em>with </em>J.A. 324 (Q: “Did you know you wouldn’t require further analysis by Greg Norman or any other examiner at the Army lab in Georgia after December of 2004?” Agent <page-number citation-index="1" label="225">*225</page-number>Chowaniec: “No.”); see <em>supra </em>note 12. Nor would it be reasonable to expect additional detail in the affidavit on this point, even assuming Ganias’s contention to be correct that the Government had both finished its segregation <em>and </em>provided insufficient facts to alert the magistrate judge to that reality, given the dearth of precedent suggesting its relevance. <em>Cf. Clark, </em><span class="citation" data-id="206195"><a href="/opinion/206195/united-states-v-clark/#105" aria-description="Citation for case: United States v. Clark">638 F.3d at 105</a></span> (“[Wjhere the need for specificity in a warrant or warrant affidavit on a particular point was not yet settled or was otherwise ambiguous, we have declined to find that a well-trained officer could not reasonably rely on a warrant issued in the absence of such specificity.”); <em>cf. Reilly, </em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/#1280" aria-description="Citation for case: United States v. Kevin C. Reilly">76 F.3d at 1280</a></span> (noting that the affidavit in that case, in clear contrast to the affidavit in this one, was “almost calculated to mislead”).</p>
<p id="b249-5">Second, here, as in <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span>, </em>it is also clear that the agents, as the panel put it in <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span>, </em>“did not have any significant reason to believe that what [they] had done was unconstitutional,” <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span>, </em>76 F.3d at 1281— that their retention of the mirrored hard drives, while the investigation was ongoing, was anything but routine. At the time of the retention, no court in this Circuit had held that retention of a mirrored hard drive during the pendency of an investigation could violate the Fourth Amendment, much less that such retention would do so in the circumstances presented here. <em>See <span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">id.</a></span> </em>(noting that suppression was inappropriate in <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span> </em>in part because no relevant precedent established that canine sniffs of a dwelling “violated the Fourth Amendment”).<footnotemark>45</footnotemark> Moreover, as noted above, the 2003 warrant authorized the lawful seizure not merely of particular records or data, but of the hard drives themselves, or in the alternative the creation of mirror images of the drives to be removed from the premises for later forensic evaluation, . and set no greater limit on the Government’s retention of those materials than on any other evidence whose seizure it authorized.</p>
<p id="b249-9">Finally, the record here is clear that the agents acted reasonably throughout the investigation. They sought authorization in 2003 to seize the hard drives and search them off-site; they minimized the disruption to Ganias’s business by taking full forensic mirrors; they searched the mirrors only to the extent authorized by, first, the 2003 warrant, and then the warrant issued in 2006; they were never alerted that Ganias sought the return of the mirrors; and they alerted the magistrate judge to these pertinent facts in applying for the second warrant. In short, the agents acted reasonably in relying on the 2006 warrant to search for evidence of Ganias’s tax evasion. This case fits squarely within <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>so that, assuming, <em>arguen-do, </em>that a Fourth Amendment violation occurred, suppression was not warranted.</p>
<p id="b249-10">We conclude that the Government relied in good faith on the 2006 search warrant and thus AFFIRM the judgment of the <page-number citation-index="1" label="226">*226</page-number>district court. Given this determination, we do not reach the specific Fourth Amendment question posed to us today.</p>
<footnote label="1">
<p id="b225-5">. These facts are drawn from the district court decision denying Ganias s motion to suppress and from testimony at the suppression hearing and at Ganias’s jury trial. With few exceptions noted herein, the facts in this case are not in dispute.</p>
</footnote>
<footnote label="2">
<p id="b225-6">. Specifically, Agent Conner sought evidence relating to violations of <span class="citation no-link">18 U.S.C. § 287</span> (making false claims) and § 641 (stealing government property).</p>
</footnote>
<footnote label="3">
<p id="b225-7">. The warrant specified as follows:</p>
<blockquote id="b225-8">The search procedure of the electronic data contained in computer operating software or memory devices may include the following techniques:</blockquote>
<blockquote id="b225-9">(a)surveying various file ''directories” and the individual files they contain (analogous to looking at the outside of a file cabinet for the markings it contains and opening a drawer believed to contain pertinent files);</blockquote>
<blockquote id="b225-13">(b) "opening” or cursorily reading the first few "pages” of such files in order to determine their precise contents;</blockquote>
<blockquote id="b225-14">(c) "scanning” storage areas to discover and possibly recover recently deleted files;</blockquote>
<blockquote id="b225-15">(d) "scanning” storage areas for deliberately hidden files; or</blockquote>
<blockquote id="b225-16">(e) performing key word searches through all electronic storage areas to determine whether occurrences of language contained in such storage areas exist that are intimately related to the subject matter of the investigation.</blockquote>
<p id="b225-17">J.A. 433-34.</p>
</footnote>
<footnote label="4">
<p id="b225-18">.In his attached affidavit, Agent Conner offered three reasons why it was necessary for the agents to take entire hard drives off-site for subsequent search rather than search the <page-number citation-index="1" label="202">*202</page-number>hard drives on-site: First, he stated that computer searches had to be conducted by computer forensics experts, who "us[ed] ... investigative techniques” to both “protect the integrity of the evidence ... [and] detect hidden, disguised, erased, compressed, password protected, or encrypted files.” J.A. 448-49. Because of "[t]he vast array” of software and hardware available, it would not always be possible "to know before a search which expert is qualified to analyze the [particular] system and its data.” J.A. 450. Thus, the appropriate experts could not be expected, in all cases, to accompany agents to the relevant site to be searched. Second, Agent Conner affirmed that such searches often must occur in "a laboratory or other controlled environment” given the sensitivity of the digital storage media. J.A. 449-50. And third, he stated that "[t]he search process can take weeks or months, depending on the particulars of the hard drive to be searched.” J.A. 449. The district court found, in denying Ganias's motion to suppress, that, as a result of technological limitations in 2003 and the complexities of searching digital data,. "[a] full [on-site] search would have taken months to complete.” <em>United States </em>v. <em>Ganias, </em>No. 3:08CR00224, <span class="citation no-link">2011 WL 2532396</span>, at *2 D. Conn. June 24, 2011.</p>
</footnote>
<footnote label="5">
<p id="b226-5">. Hard drives are storage media comprising numerous bits — units of data that may be expressed as ones or zeros. Mirroring involves using a commercially available digital software (in the present case, though not always, EnCase) to obtain a perfect, forensic replica of the sequence of ones and zeros written onto the original hard drive. During the mirroring, EnCase acquires metadata about the mirroring process, writing an unalterable record of who creates the copy and when the copy is created. It also assigns the mirror a "hash value” — a unique code that can be used to verify whether, upon subsequent examination of the mirror at any later date, even a single one or zero has been altered from the original reproduction.</p>
</footnote>
<footnote label="6">
<p id="b226-8">. Testifying at the suppression hearing, Agent Conner explained that the decision to take mirrors, rather than the hard drives themselves, reflected a desire to mitigate the burden on Ganias and his business. <em>See </em>J.A. 140-41. The district court credited this testimony, concluding that the agents "used a means less intrusive to the individual whose possessions were seized than other means they were authorized to use.” <em>Ganias, </em><span class="citation no-link">2011 WL 2532396</span>, at *8. The district court, further, explicitly found that the 2003 warrant authorized the Government to take these mirrors, <span class="citation no-link"><em>id. </em>at *10</span>, a position Ganias has not challenged on appeal, and that runs directly counter to the dissent's seeming suggestions that the Government somehow acted improperly when it mirrored Ganias's hard drives or that this initial seizure went beyond the scope of the 2003 warrant, <em>see, e.g., </em>Dissent at 227 (noting that “although the Government had a warrant for documents relating to only two of defendant-appellant Stavros Ganias's accounting clients, it seized <em>all </em>the data from three of his computers”); <em>id. </em>at <em>111 </em>(stating that "the Government ... entered Ganias’s premises with a warrant to seize certain papers and indiscriminately seized — and <em>retained </em>— all papers instead”).</p>
</footnote>
<footnote label="7">
<p id="b227-7">. Ganias claimed before the district court that when he expressed some concern about the scope of the data being seized, an agent assured him that the agents were only looking for files related to AB and IPM, and that irrelevant files "would be purged once they completed their search” for such files. J.A. 428. The district court made no finding to this effect, however. It is undisputed, moreover, that Ganias became aware in February 2006 that the Government retained the mirrors and sought to search them in connection with Ganias’s own tax reporting. At no time thereafter did Ganias seek return of the mirrors pursuant to Federal Rule of Criminal Procedure 41(g) or otherwise contact a case agent to seek their return or destruction.</p>
</footnote>
<footnote label="8">
<p id="b227-11">. These copies were identical digital replicas of Ganias's hard drives as mirrored on November 19, 2003. Notably, the original hard drives in Ganias’s computers had, already been significantly altered since the Government mirrored them. Ganias explains in his brief before this Court that ”[t]wo days after the execution of the November 2003 warrant, [he] reviewed his personal QuickBooks file and.... <em>corrected over 90 errors in earlier journal entries.” </em>Appellant Br. at 15 n.7 (emphasis added).</p>
</footnote>
<footnote label="9">
<p id="b228-5">. The rest of the data remained on the DVDs, where agents would not be able to access it without specific forensic software. <em>See Ganias, </em><span class="citation no-link">2011 WL 2532396</span>, at *7.</p>
</footnote>
<footnote label="10">
<p id="b228-8">. Norman describes the storage device he sent to Chowaniec as a "DVD,” J.A. 218; the district court described it as a "CD,” <em>Ganias, </em><span class="citation no-link">2011 WL 2532396</span>, at *4. The distinction is immaterial.</p>
</footnote>
<footnote label="11">
<p id="b229-6">. A “restoration” is a software interface that enables a user (potentially a jury) to view data on a mirror as such data would have appeared to a person accessing the data on the original storage device at the time the mirror was created. <em>Ganias, </em><span class="citation no-link">2011 WL 2532396</span>, at *4.</p>
</footnote>
<footnote label="12">
<p id="b229-7">. At the suppression hearing, Agent Chowan-iec testified, in response to the question whether "as of mid-December, [her] forensic analysis was completed": "That's correct, of the computers.” J.A. 322. But when asked later, "[D]id you know [in December 2004] you wouldn't need to look at any information that had been provided by Greg Norman on that CD anymore in the course of this investigation,” Agent Chowaniec responded, "No,” and when further asked, "Did you know you wouldn’t require further analysis by Greg Norman or any other examiner at the Army lab in Georgia after December of 2004," Agent Chowaniec again responded, "No.” J.A. 324. Agent Conner similarly answered with uncertainty when asked a related question. <em>See </em>J.A. 145 (“I didn’t know the entire universe of information that was contained within the DVDs that were sent to [Norman] for analysis. I knew only what he sent back to me saying this is what I found off your keyword search.”). The dissent disputes our conclusion that the record was unclear on this point, arguing, through citation to Agent Chowan-iec’s testimony, that "the record ... shows otherwise.” Dissent at 233. The district court found no facts on this issue, and the record, as demonstrated above, is indeed unclear.</p>
</footnote>
<footnote label="13">
<p id="b230-4">. Agent Conner’s explanation for why the Government did not, as a matter of policy in this or other cases, delete mirrored drives or otherwise require segregation or deletion of non-responsive data, is not a model of clarity: in addition to citing concerns of evidentiary integrity and suggesting a policy of non-deletion or return prior to the end of an investigation, he noted that "you never know what data you may need in the future," J.A. 122, and at one point referred to the DVDs as "the government’s property, not Mr. Ganias'[s] property," J.A. 146. The dissent seizes on this single sentence during Agent Conner's cross-examination as the smoking gun of the Government’s bad faith, citing it on no fewer than four occasions. <em>See </em>Dissent at 227, 229, 238, 240. The district court, however, did not find facts explicating Agent Conner’s testimony or placing it within the context of the explanations that he and other agents offered for retention of the mirrors. The court did note in its legal analysis that "[a] copy of the evidence was preserved in the form in which it was taken.” <em>Ganias, </em><span class="citation no-link">2011 WL 2532396</span>, at *8. Further, the Government on appeal provides numerous rationales — many echoing those articulated by Agent Conner <em>throughout </em>his testimony — for why retention of a forensic mirror may be necessary during the pendency of an investigation, none of which amounts to the argument that the mirror is simply "government[] property."</p>
</footnote>
<footnote label="14">
<p id="b230-5">. The dissent suggests that "[w]hat began nearly thirteen years ago as an investigation by the Army into two of Ganias’s business clients <em>somehow </em>evolved into an unrelated investigation by the IRS into Ganias’s personal affairs, largely because” the Government retained the mirrored copies of Ganias's hard drives. Dissent at 241 (emphasis added). In fact, Agent Hosney's affidavit in support of the 2006 warrant explains that the Government suspected Ganias of underreporting his income because of evidence that Ganias had assisted McCarthy in underreporting income from <em>McCarthy’s </em>companies — evidence which led to an indictment of <em>both </em>McCarthy and Ganias for conspiracy to commit tax fraud. Further, when Agent Hosney developed this suspicion — which was hardly "unrelated” to the initial investigation — she did not turn to the mirrors, but instead engaged in old-fashioned investigatory work, "examining Gani-as’s tax returns] more closely to determine if his own income was underreported.” J.A. 465, ¶ 18. She then reviewed deposits in his bank account, cross-referenced bank records and tax returns, and finally presented this evidence in a proffer session to Ganias — all without once looking at any non-responsive information on the mirrors. Only after she had acquired independent probable cause— and only after extensive evidence suggested Ganias may have committed a crime — did Agent Hosney seek a second warrant to search the mirrors. It is, in short, no mystery how the investigation of McCarthy, IPM, and AB came to include Ganias, and, further, an inaccurate statement of the record to suggest that this "evolution” had anything to do with the retention of the mirrors.</p>
</footnote>
<footnote label="15">
<p id="b231-6">. Agent Hosney explained in her testimony: "[W]e couldn't look at that file because it wasn’t — Steve Ganias and Taxes International were not listed on the original Attachment B, items to be seized.” J.A. 348.</p>
</footnote>
<footnote label="16">
<p id="b231-7">. According to Agent Hosney, in that proffer session Ganias claimed "that he failed to record income from his own business [to his QuickBook files] as a result of a computer flaw in the QuickBooks software ... [but that,] ... although he attempted to duplicate the software error, he was unable to do so.” J.A. 467, ¶ 28. Agent Hosney contacted Intuit, Inc., which released QuickBooks, to determine whether such an error might have affected, generally, the pertinent version of the software, and was told that the company was aware of no such "widespread malfunction.” J.A. 469, ¶ 35.</p>
</footnote>
<footnote label="17">
<p id="b231-12">. U.S. Magistrate Judge William I. Garfink-el, who had authorized the 2003 warrant, authorized this 2006 warrant as well. J.A. 430, 454.</p>
</footnote>
<footnote label="18">
<p id="b231-13">. Ganias did not contest before the district court, and does not contest on appeal, that this evidence — none of which was acquired through search of non-responsive data on the mirrors — created sufficient probable cause for the 2006 warrant.</p>
</footnote>
<footnote label="19">
<p id="b232-5">. Many of these entries existed <em>only </em>on the QuickBooks files that the Government had accessed on the mirrors, as a result of Gani-as’s amendments to the entries on his hard drives days after the execution of the 2003 warrant. At trial, Ganias testified that his characterization of the payments as "owner's contributions" was simply a good faith mistake, and not evidence of intent to commit tax evasion, a claim that the Government labeled implausible in light of Ganias’s extensive experience as an IRS agent and accountant.</p>
</footnote>
<footnote label="20">
<p id="b232-6">. Specifically, we asked the parties to brief the following two issues:</p>
<blockquote id="b232-12">(1) Whether the Fourth Amendment was violated when, pursuant to a warrant, the government seized and cloned three computer hard drives containing both responsive and non-responsive files, retained the cloned hard drives for some two-and-a-half years, and then searched the nonresponsive files pursuant to a subsequently issued warrant; and</blockquote>
<blockquote id="b232-13">(2) Considering all relevant factors, whether the government agents in this case acted reasonably and in good faith such that the files obtained from the cloned hard drives should not be suppressed.</blockquote>
<p id="b232-14"><em>United States v. Ganias, 791 </em>F.3d 290 (2d Cir. 2015) (mem.).</p>
</footnote>
<footnote label="21">
<p id="b233-4">. Specifically, courts have long recognized that a prohibition on "general warrants”— warrants completely lacking in particularity— was a central impetus for the ratification of the Fourth Amendment. <em>See, e.g., Riley v. California, - </em>U.S. -, <span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/#2494" aria-description="Citation for case: Riley v. Cal. United States">134 S.Ct. 2473, 2494</a></span>, <span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">189 L.Ed.2d 430</a></span> (2014) (noting, in the context of evaluating the reasonableness of a warrant-less search of a cell phone, that "[o]ur cases have recognized that the Fourth Amendment was the founding generation's response to the reviled ‘general warrants’ and ‘writs of assistance’ of the colonial era, which allowed British officers to rummage through homes in an unrestrained search for evidence of criminal activity” and that "opposition to such searches was in fact one of the driving forces behind the Revolution itself”); <em>Marshall v. Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#311" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U.S. 307, 311</a></span>, <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">98 S.Ct. 1816</a></span>, <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">56 L.Ed.2d 305</a></span> (1978) (noting, in the context of evaluating the reasonableness of warrantless inspections of business premises, that “[t]he particular offensiveness” of general warrants "was acutely felt by the merchants and businessmen whose premises and products were inspected” under them); <em>Stanford v. Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#486" aria-description="Citation for case: Stanford v. Texas">379 U.S. 476, 486</a></span>, <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">85 S.Ct. 506</a></span>, <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">13 L.Ed.2d 431</a></span> (1965) (”[T]he Fourth ... Amendment ] guarantee^] ... that no official ... shall ransack [a person’s] home and seize his books and papers under the unbridled authority of a general warrant....”); <em>United States v. Galpin, </em><span class="citation" data-id="931473"><a href="/opinion/931473/united-states-v-galpin/#445" aria-description="Citation for case: United States v. Galpin">720 F.3d 436, 445</a></span> (2d Cir. 2013) ("The chief evil that prompted the framing and adoption of the Fourth Amendment was the 'indiscriminate searches and seizures’ conducted by the British ‘under the authority of "general warrants.” ’ ” (quoting <em>Payton v. New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York">445 U.S. 573, 583</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">63 L.Ed.2d 639</a></span> (1980))).</p>
<p id="b233-8">We agree with the dissent that "the precedents are absolutely clear that general warrants are unconstitutional.” Dissent at 237. To the degree that the dissent would go further, however, and find it "absolutely clear” to a reasonable- government agent in 2005 that the retention of a lawfully acquired mirror during the pendency of an investigation and the subsequent search of data on that mirror pursuant to a second warrant would implicate the ban on general warrants, we respectfully disagree.</p>
</footnote>
<footnote label="22">
<p id="b233-9">. <em>See, e.g., L.A. Cty. v. Rettele, </em><span class="citation" data-id="9435063"><a href="/opinion/145728/los-angeles-county-california-v-rettele/#614" aria-description="Citation for case: Los Angeles County, California v. Rettele">550 U.S. 609, 614-16</a></span>, <span class="citation" data-id="9435063"><a href="/opinion/145728/los-angeles-county-california-v-rettele/" aria-description="Citation for case: Los Angeles County, California v. Rettele">127 S.Ct. 1989</a></span>, <span class="citation" data-id="9435063"><a href="/opinion/145728/los-angeles-county-california-v-rettele/" aria-description="Citation for case: Los Angeles County, California v. Rettele">167 L.Ed.2d 974</a></span> (2007) (applying the reasonableness standard to evaluate whether police officers' manner of executing a valid warrant violated the Fourth Amendment); <em>Wilson v. Layne, </em><span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/#611" aria-description="Citation for case: Wilson v. Layne">526 U.S. 603, 611</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">119 S.Ct. 1692</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">143 L.Ed.2d 818</a></span> (1999) ("[T]he Fourth Amendment does require that police actions in execution of a warrant be related to the objectives of the authorized intrusion....”); <em>Dalia </em>v. <em>United States, </em><span class="citation" data-id="9427537"><a href="/opinion/110061/dalia-v-united-states/#258" aria-description="Citation for case: Dalia v. United States">441 U.S. 238, 258</a></span>, <span class="citation" data-id="9427537"><a href="/opinion/110061/dalia-v-united-states/" aria-description="Citation for case: Dalia v. United States">99 S.Ct. 1682</a></span>, <span class="citation" data-id="9427537"><a href="/opinion/110061/dalia-v-united-states/" aria-description="Citation for case: Dalia v. United States">60 L.Ed.2d 177</a></span> (1979) ("[T]he manner in which a warrant is executed is subject to later judicial review as to its reasonableness.”); <em>Terebesi v. Torreso, </em><span class="citation" data-id="8413121"><a href="/opinion/8441937/terebesi-v-torreso/#235" aria-description="Citation for case: Terebesi v. Torreso">764 F.3d 217, 235</a></span> (2d Cir. 2014) ("[T]he method used to execute a search warrant ... <page-number citation-index="1" label="210">*210</page-number>[is] as a matter of clearly established constitutional law,.subject to Fourth Amendment protections. ..c<em>ert. denied sub nom. Torresso v. </em>Terebesi, - U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./135/1842/">135 S.Ct. 1842</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/191/723/">191 L.Ed.2d 723</a></span> (2015) (mem.); <em>Lauro v. Charles, </em><span class="citation" data-id="769506"><a href="/opinion/769506/john-lauro-jr-v-michael-charles-the-city-of-new-york-and-the-police/#209" aria-description="Citation for case: John Lauro, Jr. v. Michael Charles, the City of New York...">219 F.3d 202, 209</a></span> (2d Cir. 2000) ("[T]he Fourth Amendment’s proscription of unreasonable searches and seizures 'not only ... prevents] searches and seizures that would be unreasonable if conducted at all, but also ... ensure[s] reasonableness in the manner and scope of searches and seizures that are carried out.' ” (all but first alteration in original) (quoting <em>Ayeni v. Mottola, </em><span class="citation" data-id="678500"><a href="/opinion/678500/tawa-ayeni-v-james-mottola/#684" aria-description="Citation for case: Tawa Ayeni v. James Mottola">35 F.3d 680, 684</a></span> (2d Cir. 1994))).</p>
</footnote>
<footnote label="23">
<p id="b234-8">. On appeal, Ganias does not question the scope or validity of the 2003 warrant. The district court found that the 2003 warrant authorized the Government to mirror Gani-as's hard drives for off-site review, <em>Ganias, </em><span class="citation no-link">2011 WL 2532396</span>, at *10; that the warrant, though authorizing such seizure, was sufficiently particularized and not a "general warrant," <em>id.; </em>that, absent mirroring for off-site review, on-site review would have taken months, <span class="citation no-link"><em>id. </em>at *2</span>; and that mirroring thus minimized any intrusion on Ganias's business, <span class="citation no-link"><em>id. </em>at *8</span>; <em>cf. </em>Fed. R. Crim. P. 41(e)(2)(B) (which, as amended in 2009, permits a warrant to "authorize the seizure of electronic storage media or the seizure or copying of electronically stored information,” and notes that "[ujnless otherwise specified, the warrant authorizes a later review of the media or information consistent with the warrant”); Fed. R. Crim. P. 41(e)(2)(B) advisory committee's note to 2009 amendments (explaining that, because "[c]omputers and other electronic storage media commonly contain such large amounts of information that it is often impractical for law enforcement to review all of the information during execution of the warrant at the search location[, t]his rule acknowledges the need for a two-step process: officers may seize or copy the entire storage medium and review it later to determine what electronically stored information falls within the scope of the warrant”). Ganias does not contest these conclusions on appeal but contends, instead, that considerations <em>underlying </em>the prohibition on general warrants may require that, if the government lawfully mirrors an entire hard drive containing non-responsive as well as responsive information for off-site review, it may not then retain the mirror throughout the pendency of its investigation.</p>
</footnote>
<footnote label="24">
<p id="b234-12">. As already noted, the district court made no finding as to when or whether forensic examination of the mirrors pursuant to the 2003 warrant was completed.</p>
</footnote>
<footnote label="25">
<p id="b235-6">. The Ninth Circuit declined to reverse the defendant’s conviction, as no improperly seized document was admitted at trial, and as blanket suppression was not warranted. <em>See Tamura, </em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/#597" aria-description="Citation for case: United States v. Leigh Raymond Tamura">694 F.2d at 597</a></span>.</p>
</footnote>
<footnote label="26">
<p id="b235-7">. The fact that the officers in <em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">Tamura</a></span> </em>lacked a warrant for the initial seizure was not incidental to the decision: the <em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">Tamura</a></span> </em>court explicitly found that it was the lack of a warrant that made the initial seizure — even if otherwise understandable in light of the voluminous material to be reviewed — a violation of the Fourth Amendment. <em>See </em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/#596" aria-description="Citation for case: United States v. Leigh Raymond Tamura">694 F.2d at 596</a></span>.</p>
</footnote>
<footnote label="27">
<p id="b236-4">. <em>See </em>Daniel B. Garrie &amp; Francis M. Allegra, Fed. Judicial Ctr., <em>Understanding Software, the Internet, Mobile Computing, and the Cloud: A Guide forjudges </em>8-14 (2015) (contrasting "operating systems ... [which] hide the hardware resources behind abstractions to provide an environment that is more user-friendly,” <em>id. </em>at 13, with machine language, assembly language, high-level languages, data structures, and algorithms); Josh Goldfoot, <em>The Physical Computer and the Fourth Amendment, </em>16 Berkeley J. Crim. L. 112, 117 (2011) (contrasting two perspectives on digital storage media — the "internal perspective,” or how “the user experiences [such media,] as parcels of information, grouped into files, or even into smaller units such as spreadsheet rows” and the "external perspective,” or how the actual computer functions, in which "files are not ... ‘things’ at all,” but "groupings of data ... inseparably tied to the storage medium,” created by the computer by manipulating "chunks of physical matter [such as regions on a hard drive] whose state is altered to record information”).</p>
</footnote>
<footnote label="28">
<p id="b236-5">. <em>See </em>Eoghan Casey, <em>Digital Evidence and Computer Crime </em>472, 474-96 (3d ed. 2011) (highlighting the fact that forensic examination of storage media can create tiny alterations, which necessitates care on the part of examiners in acquiring, searching, and preserving that data); <em>id. </em>at 477-78 (describing the importance of protecting digital storage media from "dirt, fluids, humidity, impact, excessive heat and cold, strong magnetic fields, and static electricity”); Michael W. Graves, <em>Digital Archaeology: The Art and Science of Digital Forensics </em>95 (2014) ("Computer data is extremely volatile and easily deleted, and can be destroyed, either intentionally or accidentally, with a few mouse clicks.”); Bill Nelson et al., <em>Guide to Computer Forensics and Investigations </em>160 (5th ed. 2015) (emphasizing the importance of “maintaining] the integrity of digital evidence in the lab” by creating a read-only copy prior to analysis); Jonathan L. Moore, <em>Time for an Upgrade: Amending the Federal Rules of Evidence to Address the Challenges of Electronically Stored Information in Civil Litigation, </em><span class="citation no-link">50 Jurimetrics J. 147</span>, 153 (2010) ("[All electronically stored information is] prone to manipulation[;] ... [such] alteration can occur intentionally or inadvertently.”); Int’l Org. for Standardization &amp; Int’l Electrotechnical Comm’n, <em>Guidelines for Identification, Collec</em><page-number citation-index="1" label="213">*213</page-number><em>tion, Acquisition, and Preservation of Digital Evidence </em>17 (2012) [hereinafter ISO/IEC, Guidelines] (emphasizing the importance of careful storage and transport techniques and noting that "[s]poliation can result from magnetic degradation, electrical degradation, heat, high or low humidity exposure, as well as shock and vibration”).</p>
</footnote>
<footnote label="29">
<p id="b237-6">. <em>See </em>Goldfoot, <em>supra </em>("Storage media do not naturally divide into parts,” <em>id. </em>at 131; "it is difficult to agree ... on where the subcon-tamers begin and end,” <em>id. </em>at 113.); Orin S. Kerr, <em>Searches and Seizures in a Digital World, </em><span class="citation no-link">119 Harv. L. Rev. 531</span>, 557 (2005) ("[V]irtual files are not robust concepts. Files are contingent creations assembled by operating systems and software.”); <em>see also </em>Orin S. Kerr, <em>Executing Warrants for Digital Evidence: The Case for Use Restrictions on Nonresponsive Data, </em><span class="citation no-link">48 Tex. Tech L. Rev. 1</span>, 32 (2015) ("What does it mean to 'delete' data?”).</p>
</footnote>
<footnote label="30">
<p id="b238-4">. <em>See Fharmacy Records v. Nassar, </em><span class="citation" data-id="2979016"><a href="/opinion/2979016/fharmacy-records-v-salaam-nassar/#525" aria-description="Citation for case: Fharmacy Records v. Salaam Nassar">379 Fed. Appx. 522, 525</a></span> (6th Cir. 2010) (describing testimony of a digital forensics expert in a copyright case that the number and physical location of a file on an Apple Macintosh— which saves files sequentially on its storage medium — demonstrated that the file had been back-dated).</p>
</footnote>
<footnote label="31">
<p id="b238-5">. Indeed, in this very case, as already noted, <em>see supra </em>note 16, Ganias at one point claimed that a “software error” or “computer flaw” prevented him from recording certain income in his QuickBooks files. J.A. 467, ¶ 28. Data confirming the existence, or non-existence, of an error affecting the particular installation of a program on a given digital storage device could be, in a hypothetical case, relevant to the probity of information otherwise located thereupon.</p>
</footnote>
<footnote label="32">
<p id="b238-6">. We note that some of these inferences may be limited to — or at least of more relevance to — traditional magnetic disk drives, which have long been the primary digital storage technology. "Generally when data is deleted from a [traditional hard disk drive], the data is retained until new data is written onto the same location. If no new data is written over the deleted data, then the forensic investigator can recover the deleted data, albeit in fragments.” Alastair Nisbet et al., <em>A Forensic Analysis and Comparison of Solid State Drive Data Retention with TRIM Enabled File Systems, </em>Proceedings of the 11th Australian Digital Forensics Conference 103 (2013). In contrast, the technology used in solid state drives “requires a cell to be completely erased or zeroed-out before a further write can be committed,” <em>id. </em>at 104, and in part because such erasure can be time consuming, solid state drives incorporate protocols which “zero-delete data locations ... as a matter of course,” thereby "reducing] the data that can be retrieved from the drive by [a] forensic investigator,” <em>id. </em>at 103. <em>See also </em>Graeme B. Bell &amp; Richard Boddington, <em>Solid State Drives: The Beginning of the End for Current Practice in Digital Forensic Recovery?, </em>5 J. Digital Forensics, Sec. &amp; L., no. 3, 2010, at 1, 12 (staling that, in connection with such storage devices, "evidence indicating 'no data’ does not authoritatively prove that data did not exist at the time of capture”). That is not to say that studies indicate that deleted information is <em>never </em>recoverable from any model of solid state drive. <em>See, e.g., </em>Christopher King &amp; Timothy Vidas, <em>Empirical Analysis of Solid State Disk Data Retention When Used with Contemporary Operating Systems, </em>8 Digital Investigation 111, 113 (2011) (citing a study suggesting that data deleted from a particular solid state drive was recoverable in certain contexts); Gabriele Bonetti et al., <em>A Comprehensive Black-Box Methodolo

[...TRUNCATED 21519 of 141519 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
