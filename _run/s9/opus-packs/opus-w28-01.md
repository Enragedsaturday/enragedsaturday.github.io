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

## GROUP: content/cases/Brown v. Texas.md  (`case`, 6 assertions)

### content_page

```
---
title: "Brown v. Texas"
type: case
citation: "443 U.S. 47 (1979)"
parallel_cite: "99 S. Ct. 2637; 61 L. Ed. 2d 357"
neutral_cite: 1979 U.S. LEXIS 136
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-06-25
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1979-06-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Brown v. Texas
  varies_by_point: false
  scope_note: "Good law. Police may not detain a person and demand identification without reasonable suspicion; the case supplies the three-factor balancing test for suspicionless seizures. Hiibel v. Sixth Judicial Dist. Court (2004) later upheld an identify-yourself demand during a lawful Terry stop — the question Brown expressly reserved — and does not disturb Brown."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110128/brown-v-texas/"
  cluster_id: 110128
  opinion_id: 110128
  identity_checked: true
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Anchor"
  - page: "[[Seizure of the Person]]"
    role: "Related (cross-doctrine)"
related: ["[[Terry v. Ohio]]", "[[Delaware v. Prouse]]", "[[Hiibel v. Sixth Judicial Dist. Court]]", "[[Kolender v. Lawson]]"]
aliases: []
tags: ["case", "fourth-amendment", "terry-stop", "reasonable-suspicion", "stop-and-identify", "seizure"]
holding: "Police may not stop a person and demand identification without reasonable suspicion of criminal activity; the constitutionality of suspicionless seizures is judged by balancing public concern, advancement of the public interest, and the severity of the intrusion on liberty."
lake:
  record_id: Brown v. Texas
  status: under_review
  projected_at: 2026-07-06
---

# Brown v. Texas

*443 U.S. 47 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Two El Paso officers, patrolling an area with a high incidence of drug traffic, saw Brown and another man walking in opposite directions away from one another in an alley. They stopped Brown and asked him to identify himself and explain what he was doing. One officer testified the situation "looked suspicious" but could point to no specific facts; he acknowledged the only reason for the stop was to ascertain Brown's identity. Brown refused to identify himself and was arrested and convicted under a Texas statute (§ 38.02) making it a crime to refuse to give one's name to an officer who has lawfully stopped him.

## Issue
Whether officers may detain an individual and require him to identify himself, on penalty of criminal punishment for refusing, when they lack reasonable suspicion that he is engaged in criminal activity.

## Rule
No. The constitutionality of a seizure short of arrest is judged by a balancing test: "Consideration of the constitutionality of such seizures involves a weighing of the gravity of the public concerns served by the seizure, the degree to which the seizure advances the public interest, and the severity of the interference with individual liberty." — 443 U.S. at 51. ^pin-51

And the seizure of a particular person requires individualized, objective justification: "the Fourth Amendment requires that a seizure must be based on specific, objective facts indicating that society's legitimate interests require the seizure of the particular individual, or that the seizure must be carried out pursuant to a plan embodying explicit, neutral limitations on the conduct of individual officers." — *Id.* at 51. ^pin-51b

A brief investigative detention therefore demands "a reasonable suspicion, based on objective facts, that the individual is involved in criminal activity."

## Application
The officers had no such basis. One could say only that the alley "looked suspicious" without identifying any supporting fact; there was no indication it was unusual for people to be there; and "[t]he fact that appellant was in a neighborhood frequented by drug users, standing alone, is not a basis for concluding that appellant himself was engaged in criminal conduct." The only reason for the stop was to learn Brown's identity. Absent reasonable suspicion, the stop tilted the balance toward the individual's liberty, and the Court held: "The application of Tex. Penal Code Ann., Tit. 8, § 38.02 (1974), to detain appellant and require him to identify himself violated the Fourth Amendment because the officers lacked any reasonable suspicion to believe appellant was engaged or had engaged in criminal conduct." — *Id.* at 53. ^pin-53

## Conclusion
Because the stop was not supported by reasonable suspicion, applying the statute to punish Brown for refusing to identify himself violated the Fourth Amendment; the conviction was reversed. An officer may not seize a person to demand identification without reasonable suspicion (or a neutral, plan-based scheme).

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. The *Brown* three-factor balancing test governs suspicionless seizures and is applied in the checkpoint cases ([[Michigan Dept. of State Police v. Sitz]], [[City of Indianapolis v. Edmond]], [[Illinois v. Lidster]]). The Court expressly reserved whether an individual may be required to identify himself during a *lawful* investigatory stop; [[Hiibel v. Sixth Judicial Dist. Court]] (2004) answered yes, upholding a stop-and-identify statute applied during a *[[Terry v. Ohio|Terry]]* stop supported by reasonable suspicion — distinguishing, not overruling, *Brown*.

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Anchor*
- [[Seizure of the Person]] — *Related (cross-doctrine)*

## Sources
- *Brown v. Texas*, 443 U.S. 47 (1979) — https://www.courtlistener.com/opinion/110128/brown-v-texas/ — pinpoints: 51, 52, 53.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "de145b577d89f4bb", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "443 U.S. 47 (1979)", "court": "U.S. Supreme Court", "neutral_cite": "1979 U.S. LEXIS 136", "official_citation_present": true, "parallel_cite": "99 S. Ct. 2637; 61 L. Ed. 2d 357", "title": "Brown v. Texas", "year": "1979"}}
{"assertion_id": "8834e2e4f430e078", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Police may not stop a person and demand identification without reasonable suspicion of criminal activity; the constitutionality of suspicionless seizures is judged by balancing public concern, advancement of the public interest, and the severity of the intrusion on liberty.", "title": "Brown v. Texas"}}
{"assertion_id": "916df69b7d16f0bb", "dimension": "support", "kind": "home_role", "locator": {"home": "Terry Stops and Reasonable Suspicion"}, "payload": {"home": "Terry Stops and Reasonable Suspicion", "role": "Anchor", "title": "Brown v. Texas"}}
{"assertion_id": "e4684d258c4a0408", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Related (cross-doctrine)", "title": "Brown v. Texas"}}
{"assertion_id": "3808752cfbfce768", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1979-06-25", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Brown v. Texas", "field_i_validity": "good_law", "scope_note": "Good law. Police may not detain a person and demand identification without reasonable suspicion; the case supplies the three-factor balancing test for suspicionless seizures. Hiibel v. Sixth Judicial Dist. Court (2004) later upheld an identify-yourself demand during a lawful Terry stop — the question Brown expressly reserved — and does not disturb Brown.", "title": "Brown v. Texas", "varies_by_point": "false"}}
{"assertion_id": "9f36191a4dd24c8a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Brown v. Texas"}}
```

### lake record — Brown v. Texas

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brown v. Texas",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Brown v. Texas",
    "case_name_short": "Brown",
    "case_name_full": "Brown v. Texas",
    "input_case_name": "Brown v. Texas",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-06-25",
    "year": 1979,
    "docket": null,
    "cluster_id": 110128,
    "lead_opinion_id": 110128,
    "sibling_ids": [
      110128
    ],
    "absolute_url": "/opinion/110128/brown-v-texas/",
    "identity_method": "pending",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9021114,
        "score": 10,
        "case_name": "Brown v. Texas"
      },
      {
        "cluster_id": 9020748,
        "score": 10,
        "case_name": "Brown v. Texas"
      }
    ],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "443 U.S. 47",
      "volume": "443",
      "reporter": "U.S.",
      "page": "47",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 2637",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2637",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 357",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "357",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 136",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "136",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "443 U.S. 47",
        "volume": "443",
        "reporter": "U.S.",
        "page": "47",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 2637",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2637",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 357",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "357",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 136",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "136",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "443 U.S. 47",
    "official_selection": {
      "court_class": "scotus",
      "selected": "443 U.S. 47",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-51",
      "page": null,
      "quote": "but could point to no specific facts; he acknowledged the only reason for the stop was to ascertain Brown's identity. Brown refused to identify himself and was arrested and convicted under a Texas statute (\u00a7 38.02) making it a crime to refuse to give one's name to an officer who has lawfully stopped him. ## Issue Whether officers may detain an individual and require him to identify himself, on penalty of criminal punishment for refusing, when they lack reasonable suspicion that he is engaged in criminal activity. ## Rule No. The constitutionality of a seizure short of arrest is judged by a balancing test:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-51b",
      "page": null,
      "quote": "the Fourth Amendment requires that a seizure must be based on specific, objective facts indicating that society's legitimate interests require the seizure of the particular individual, or that the seizure must be carried out pursuant to a plan embodying explicit, neutral limitations on the conduct of individual officers.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-53",
      "page": null,
      "quote": "## Application The officers had no such basis. One could say only that the alley",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1979-06-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Brown v. Texas",
    "varies_by_point": false,
    "scope_note": "Good law. Police may not detain a person and demand identification without reasonable suspicion; the case supplies the three-factor balancing test for suspicionless seizures. Hiibel v. Sixth Judicial Dist. Court (2004) later upheld an identify-yourself demand during a lawful Terry stop \u2014 the question Brown expressly reserved \u2014 and does not disturb Brown.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Arias",
          "cluster_id": 10843215,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
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
        "journal_ref": "Brown v. Texas:lane1_negative"
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
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sievers - supplemental opinion",
          "cluster_id": 4571040,
          "cite": [
            "301 Neb. 806",
            "920 N.W.2d 443"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
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
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Christian",
          "cluster_id": 4477521,
          "cite": [
            "2018 Ohio 957",
            "109 N.E.3d 183"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hairston",
          "cluster_id": 4426228,
          "cite": [
            "2017 Ohio 7612",
            "97 N.E.3d 784"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Elvis Elvis Ramirez-Tamayo v. State",
          "cluster_id": 4311099,
          "cite": [
            "501 S.W.3d 788",
            "2016 Tex. App. LEXIS 10905",
            "2016 WL 5874327"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
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
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Carlos Gonzalez v. Able Huerta",
          "cluster_id": 3216824,
          "cite": [
            "826 F.3d 854",
            "2016 U.S. App. LEXIS 11530",
            "2016 WL 3457258"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Leming v. State",
          "cluster_id": 5447022,
          "cite": [
            "493 S.W.3d 552",
            "2016 WL 1458242",
            "2016 Tex. Crim. App. LEXIS 73"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mocek v. City of Albuquerque",
          "cluster_id": 3164764,
          "cite": [
            "813 F.3d 912",
            "2015 U.S. App. LEXIS 22435",
            "2015 WL 9298662"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Mercedes-De la Cruz",
          "cluster_id": 2803337,
          "cite": [
            "787 F.3d 61",
            "2015 U.S. App. LEXIS 8624",
            "2015 WL 3378255"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cortez",
          "cluster_id": 110377,
          "cite": [
            "66 L. Ed. 2d 621",
            "101 S. Ct. 690",
            "449 U.S. 411",
            "1981 U.S. LEXIS 58",
            "49 U.S.L.W. 4099"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Wardlow",
          "cluster_id": 118326,
          "cite": [
            "145 L. Ed. 2d 570",
            "120 S. Ct. 673",
            "528 U.S. 119",
            "2000 U.S. LEXIS 504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rawlings v. Kentucky",
          "cluster_id": 110326,
          "cite": [
            "65 L. Ed. 2d 633",
            "100 S. Ct. 2556",
            "448 U.S. 98",
            "1980 U.S. LEXIS 142"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ford v. State",
          "cluster_id": 1355298,
          "cite": [
            "158 S.W.3d 488",
            "2005 Tex. Crim. App. LEXIS 399",
            "2005 WL 544796"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Smith",
          "cluster_id": 1828048,
          "cite": [
            "433 So. 2d 688"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wyoming v. Houghton",
          "cluster_id": 118277,
          "cite": [
            "143 L. Ed. 2d 408",
            "119 S. Ct. 1297",
            "526 U.S. 295",
            "1999 U.S. LEXIS 2347"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.",
          "cluster_id": 136990,
          "cite": [
            "159 L. Ed. 2d 292",
            "124 S. Ct. 2451",
            "542 U.S. 177",
            "2004 U.S. LEXIS 4385",
            "17 Fla. L. Weekly Fed. S 406",
            "72 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schall v. Martin",
          "cluster_id": 111198,
          "cite": [
            "81 L. Ed. 2d 207",
            "104 S. Ct. 2403",
            "467 U.S. 253",
            "1984 U.S. LEXIS 96",
            "52 U.S.L.W. 4681"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Yeargan",
          "cluster_id": 1060948,
          "cite": [
            "958 S.W.2d 626",
            "1997 Tenn. LEXIS 574",
            "1997 WL 724993"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Howard",
          "cluster_id": 5684310,
          "cite": [
            "50 N.Y.2d 583",
            "408 N.E.2d 908",
            "430 N.Y.S.2d 578",
            "1980 N.Y. LEXIS 2454"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110128) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzkyNzY4MDAwMDAwJnM9MjY3OTQ2MSZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110128%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110128)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNzEmcz0yOTQ3NzE2JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110128%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110128)",
        "reviewed": 32,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 32,
        "triage_read": 1,
        "triage_snippet_classified": 31
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110128)",
    "indexed_citing_opinions": 1635,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110128,
        "count": 1635,
        "count_source": "search"
      }
    ],
    "citation_count": 2680,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/brown-v-texas.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1MjY3NCZzPTk0Mzg0MTMmdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28110128%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110128,
        "cited_id": 103170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 246074,
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
    "date_created": "2026-07-04T20:53:09Z",
    "date_modified": "2026-07-06T07:26:24Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:53:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:53:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:56:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:53:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Brown v. Texas

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b72-10">
  Mr. Chief Justice Burger
 </author>
<p id="AWL">
  delivered the opinion of the Court.
 </p>
<p id="b72-11">
  This appeal presents the question whether appellant was validly convicted for refusing to comply with a policeman’s demand that he identify himself pursuant to a provision of the Texas Penal Code which makes it a crime to refuse such identification on request.
 </p>
<p id="b72-12">
  I
 </p>
<p id="b72-13">
  At 12:45 in the afternoon of December 9, 1977, Officers Venegas and Sotelo of the El Paso Police Department were cruising in a patrol car. They observed appellant and another man walking in opposite directions away from one another in an alley. Although the two men were a few feet apart when they first were seen, Officer Venegas later testified that both officers believed the two had been together or were about to meet until the patrol car appeared.
 </p>
<p id="b72-14">
  The car entered the alley, and Officer Venegas got out and asked appellant to identify himself and explain what he was
  <span citation-index="1" class="star-pagination" label="49"> 
   *49
   </span>
  doing there. The other man was not questioned or detained. The officer testified that he stopped appellant because the situation “looked suspicious and we had never seen that subject in that area before.” The area of El Paso where appellant was stopped has a high incidence of drug traffic. However, the officers did not claim to suspect appellant of any specific misconduct, nor did they have any reason to believe that he was armed.
 </p>
<p id="b73-5">
  Appellant refused to identify himself and angrily asserted that the officers had no right to stop him. Officer Venegas replied that he was in a “high drug problem area”; Officer Sotelo then “frisked” appellant, but found nothing.
 </p>
<p id="b73-6">
  When appellant continued to refuse to identify himself, he was arrested for violation of Tex. Penal Code Ann., Tit. 8, § 38.02 (a) (1974), which makes it a criminal act for a person to refuse to give his name and address to an officer “who has lawfully stopped him and requested the information.”
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  Following the arrest the officers searched appellant; nothing untoward was found.
 </p>
<p id="b73-7">
  While being taken to the El Paso County Jail appellant identified himself. Nonetheless, he was held in custody and charged with violating § 38.02 (a). When he was booked he was routinely searched a third time. Appellant was convicted in the El Paso Municipal Court and fined $20 plus court costs for violation of § 38.02. He then exercised his right under Texas law to a trial
  <em>
   de novo
  </em>
  in the El Paso County Court. There, he moved to set aside the information on the ground that § 38.02 (a) of the Texas Penal Code violated the First, Fourth, and Fifth Amendments and was unconstitutionally vague in violation of the Fourteenth Amendment. The
  <span citation-index="1" class="star-pagination" label="50"> 
   *50
   </span>
  motion was denied. Appellant waived a jury, and the court convicted him and imposed a fine of $45 plus court costs.
 </p>
<p id="b74-5">
  Under Texas law an appeal from an inferior court to a county court is subject to further review only if a fine exceeding $100 is imposed. Tex. Code Crim. Proc. Ann., Art. 4.03 (Vernon 1977). Accordingly, the County Courtis rejection of appellant's constitutional claims was a decision “by the highest court of a State in which a decision could be had.” <span class="citation no-link">28 U. S. C. § 1257</span> (2). On appeal here we noted probable jurisdiction. <span class="citation multiple-matches"><a href="/c/U.%20S./439/909/">439 U. S. 909</a></span> (1978). We reverse.
 </p>
<p id="b74-6">
  II
 </p>
<p id="b74-7">
  When the officers detained appellant for the purpose of requiring him to identify himself, they performed a seizure of his person subject to the requirements of the Fourth Amendment. In convicting appellant, the County Court necessarily found as a matter of fact that the officers “lawfully stopped” appellant. See Tex. Penal Code Ann., Tit. 8, § 38.02 (1974). The Fourth Amendment, of course, “applies to all seizures of the person, including seizures that involve only a brief detention short of traditional arrest.
  <em>
   Davis
  </em>
  v.
  <em>
   Mississippi,
  </em>
  <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969);
  <em>
   Terry
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 16-19</a></span> (1968). ‘[W] hen ever a police officer accosts an individual and restrains his freedom to walk away, he has “seized” that person,’
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio"><em>
   id.,
  </em>
  at 16</a></span>, and the Fourth Amendment requires that the seizure be ‘reasonable.’ ”
  <em>
   United States
  </em>
  v.
  <em>
   Brignoni-Ponce,
  </em>
  <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975).
 </p>
<p id="b74-8">
  The reasonableness of seizures that are less intrusive than a traditional arrest, see
  <em>
   Dunaway
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#209" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 209-210</a></span> (1979);
  <em>
   Terry
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20</a></span> (1968), depends “on a balance between the public interest and the individual’s right to personal security free from arbitrary interference by law officers.”
  <em>
   Pennsylvania
  </em>
  v.
  <em>
   Mimms,
  </em>
  <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#109" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 109</a></span>
  <em>
   (1977); United States
  </em>
  v.
  <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce"><em>
   Brignoni-Ponce, supra,
  </em>
  at 878</a></span>. Consideration of the constitutionality of such seizures involves a
  <span citation-index="1" class="star-pagination" label="51"> 
   *51
   </span>
  weighing of the gravity of the public concerns served by the seizure, the degree to which the seizure advances the public interest, and the severity of the interference with individual liberty. See,
  <em>
   e. g.,
  </em>
  <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 878-883</a></span>.
 </p>
<p id="b75-5">
  A central concern in balancing these competing considerations in a variety of settings has been to assure that an individual’s reasonable expectation of privacy is not subject to arbitrary invasions solely at the unfettered discretion of officers in the field. See
  <em>
   Delaware
  </em>
  v.
  <em>
   Prouse,
  </em>
  <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654-655</a></span> (1979);
  <em>
   United States
  </em>
  v.
  <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#882" aria-description="Citation for case: United States v. Brignoni-Ponce"><em>
   Brignoni-Ponce, supra,
  </em>
  at 882</a></span>. To this end, the Fourth Amendment requires that a seizure must be based on specific, objective facts indicating that society’s legitimate interests require the seizure of the particular individual, or that the seizure must be carried out pursuant to a plan embodying explicit, neutral limitations on the conduct of individual officers.
  <em>
   Delaware
  </em>
  v.
  <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse"><em>
   Prouse, supra,
  </em>
  at 663</a></span>. See
  <em>
   United States
  </em>
  v.
  <em>
   Martinez-Fuerte,
  </em>
  <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#558" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 558-562</a></span> (1976).
 </p>
<p id="b75-6">
  The State does not contend that appellant was stopped pursuant to a practice embodying neutral criteria, but rather maintains that the officers were justified in stopping appellant because they had a “reasonable, articulable suspicion that a crime had just been, was being, or was about to be committed.” We have recognized that in some circumstances an officer may detain a suspect briefly for questioning although he does not have “probable cause” to believe that the suspect is involved in criminal activity, as is required for a traditional arrest.
  <em>
   United States
  </em>
  v.
  <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#880" aria-description="Citation for case: United States v. Brignoni-Ponce"><em>
   Brignoni-Ponce, supra,
  </em>
  at 880-881</a></span>. See
  <em>
   Terry
  </em>
  v.
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#25" aria-description="Citation for case: Terry v. Ohio"><em>
   Ohio, supra,
  </em>
  at 25-26</a></span>. However, we have required the officers to have a reasonable suspicion, based on objective facts, that the individual is involved in criminal activity.
  <em>
   Delaware
  </em>
  v.
  <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse"><em>
   Prouse, supra,
  </em>
  at 663</a></span>;
  <em>
   United States
  </em>
  v.
  <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#882" aria-description="Citation for case: United States v. Brignoni-Ponce"><em>
   Brignoni-Ponce, supra,
  </em>
  at 882-883</a></span>; see also
  <em>
   Lanzetta
  </em>
  v.
  <em>
   New Jersey,
  </em>
  <span class="citation" data-id="103170"><a href="/opinion/103170/lanzetta-v-new-jersey/" aria-description="Citation for case: Lanzetta v. New Jersey">306 U. S. 451</a></span> (1939),
 </p>
<p id="b75-7">
  The flaw in the State’s case is that none of the circum
  <span citation-index="1" class="star-pagination" label="52"> 
   *52
   </span>
  stances preceding the officers’ detention of appellant justified a reasonable suspicion that he was involved in criminal conduct. Officer Yenegas testified at appellant’s trial that the situation in the alley “looked suspicious,” but he was unable to point to any facts supporting that conclusion.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  There is no indication in the record that it was unusual for people to be in the alley. The fact that appellant was in a neighborhood frequented by drug users, standing alone, is not a basis for concluding that appellant himself was engaged in criminal conduct. In short, the appellant’s activity was no different from the activity of other pedestrians in that neighborhood. When pressed, Officer Venegas acknowledged that the only reason he stopped appellant was to ascertain his identity. The record suggests an understandable desire to assert a police presence; however, that purpose does not negate Fourth Amendment guarantees.
 </p>
<p id="b76-5">
  In the absence of any basis for suspecting appellant of misconduct, the balance between the public interest and appellant’s right to personal security and privacy tilts in favor of freedom from police interference. The Texas statute under which appellant was stopped and required to identify himself is designed to advance a weighty social objective in large metropolitan centers: prevention of crime. But even assuming that purpose is served to some degree by stopping and demanding identification from an individual without any specific basis for believing he is involved in criminal activity, the guarantees of the Fourth Amendment do not allow it. When such a stop is not based on objective criteria, the risk of arbitrary and abusive police practices exceeds tolerable limits. See
  <em>
   Delaware
  </em>
  v.
  <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#661" aria-description="Citation for case: Delaware v. Prouse"><em>
   Prouse, supra,
  </em>
  at 661</a></span>.
 </p>
<p id="b77-4">
<span citation-index="1" class="star-pagination" label="53"> 
   *53
   </span>
  The application of Tex. Penal Code Ann., Tit. 8, § 38.02 (1974), to detain appellant and require him to identify himself violated the Fourth Amendment because the officers lacked any reasonable suspicion to believe appellant was engaged or had engaged in criminal conduct.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  Accordingly, appellant may not be punished for refusing to identify himself, and the conviction is
 </p>
<p id="b77-5">
<em>
   Reversed.
  </em>
</p>
<p id="b77-6">
  APPENDIX TO OPINION OF THE COURT
 </p>
<blockquote id="b77-7">
  “THE COURT: . . . What do you think about if you stop a person lawfully, and then if he doesn’t want to talk to you, you put him in jail for committing a crime.
 </blockquote>
<blockquote id="b77-8">
  “MR. PATTON [Prosecutor]: Well first of all, I would question the Defendant’s statement in his motion that the First Amendment gives an individual the right to silence.
 </blockquote>
<blockquote id="b77-9">
  “THE COURT: . . . I’m asking you why should the State put you in jail because you don’t want to say anything.
 </blockquote>
<blockquote id="b77-10">
  “MR. PATTON: Well, I think there’s certain interests that have to be viewed.
 </blockquote>
<blockquote id="b77-11">
  “THE COURT: Okay, I’d like you to tell me what those are.
 </blockquote>
<blockquote id="b77-12">
  “MR. PATTON: Well, the Governmental interest to maintain the safety and security of the society and the citizens to live in the society, and there are certainly strong Governmental interests in that direction and because of that, these interests outweigh the interests of an individual for a certain amount of intrusion upon his personal liberty. I think these Governmental interests outweigh the individual’s interests in
  <span citation-index="1" class="star-pagination" label="54"> 
   *54
   </span>
  this respect, as far as simply asking an individual for his name and address under the proper circumstances.
 </blockquote>
<blockquote id="b78-5">
  “THE COURT: But why should it be a crime to not answer?
 </blockquote>
<blockquote id="b78-6">
  “MR. PATTON: Again, I can only contend that if an answer is not given, it tends to disrupt.
 </blockquote>
<blockquote id="b78-7">
  “THE COURT: What does it disrupt?
 </blockquote>
<blockquote id="b78-8">
  “MR. PATTON: I think it tends to disrupt the goal of this society to maintain security over its citizens to make sure they are secure in their gains and their homes.
 </blockquote>
<blockquote id="b78-9">
  “THE COURT: How does that secure anybody by forcing them, under penalty of being prosecuted, to giving their name and address, even though they are lawfully stopped?
 </blockquote>
<blockquote id="b78-10">
  “MR. PATTON: Well I, you know, under the circumstances in which some individuals would be lawfully stopped, it’s presumed that perhaps this individual is up to something, and the officer is doing his duty simply to find out the individual’s name and address, and to determine what exactly is going on.
 </blockquote>
<blockquote id="b78-11">
  “THE COURT: I’m not questioning, I’m not asking whether the officer shouldn’t ask questions. I’m sure they should ask everything they possibly could find out.
  <em>
   What I’m asking is what’s the State’s interest in putting a man in jail because he doesn’t want to answer something.
  </em>
  I realize lots of times an officer will give a defendant a Miranda warning which means a defendant doesn’t have to make a statement. Lots of defendants go ahead and confess, which is fine if they want to do that. But if they don’t confess, you can’t put them in jail, can you, for refusing to confess to a crime?” App. 15-17 (emphasis added).
 </blockquote>



<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b73-8">
   The entire section reads as follows:
  </p>
<p id="b73-9">
   “§ 38.02. Failure to Identify as Witness
  </p>
<p id="b73-10">
   “(a) A person commits an offense if he intentionally refuses to report or gives a false report of his name and residence address to a peace officer who has lawfully stopped him and requested the information.”
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b76-6">
   This situation is to be distinguished from the observations of a trained, experienced police officer who is able to perceive and articulate meaning in given conduct which would be wholly innocent to the untrained observer. See
   <em>
    United States
   </em>
   v.
   <em>
    Brignoni-Ponce,
   </em>
   <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#884" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 884-885</a></span> (1975);
   <em>
    Christensen
   </em>
   v.
   <em>
    United States,
   </em>
   104 U. S. App. D. C. 35, 36, 259 E. 2d 192, 193 (1958).
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b77-13">
   We need not decide whether an individual may be punished for refusing to identify himself in the context of a lawful investigatory stop which satisfies Fourth Amendment requirements. See
   <em>
    Dunaway
   </em>
   v.
   <em>
    New York,
   </em>
   <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span>, 210 n. 12 (1979);
   <em>
    Terry
   </em>
   v.
   <em>
    Ohio,
   </em>
   <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#34" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 34</a></span> (1968) (White, J., concurring). The County Court Judge who convicted appellant was troubled by this question, as shown by the colloquy set out in the Appendix to this opinion.
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Buckley v. Fitzsimmons.md  (`case`, 5 assertions)

### content_page

```
---
title: Buckley v. Fitzsimmons
type: case
citation: "509 U.S. 259 (1993)"
parallel_cite: "113 S. Ct. 2606; 125 L. Ed. 2d 209"
neutral_cite: 1993 U.S. LEXIS 4400
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1993
date_decided: 1993-06-24
docket: No. 91-7849
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
  opinion_url: "https://www.courtlistener.com/opinion/112894/buckley-v-fitzsimmons/"
  cluster_id: 112894
  opinion_id: null
  identity_checked: true
lake:
  record_id: Buckley v. Fitzsimmons
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Absolute Immunity]]"
    role: Anchor
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Imbler v. Pachtman]]"
tags:
  - case
  - section-1983
  - prosecutorial-immunity
  - absolute-immunity
  - qualified-immunity
  - fabricated-evidence
holding: "Absolute prosecutorial immunity extends only to the prosecutor's role as advocate in initiating and pursuing a prosecution; a prosecutor who fabricates evidence during the investigative phase, before there is probable cause to arrest, and who makes statements to the press, is protected by only qualified immunity."
aliases:
  - Buckley v. Fitzsimmons
  - "Buckley v. Fitzsimmons (1993)"
---

# Buckley v. Fitzsimmons

*509 U.S. 259 (1993)* (No. 91-7849) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 112894 → combined opinion 112894 (Stevens, J.; 509 U.S. 259, decided June 24, 1993). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*275` follows the quoted sentence, placing it at 274; Kennedy op. cross-references it as "Ante, at 274"). S9 promotes. -->

## Background
Stephen Buckley was charged in connection with the widely publicized rape and murder of Jeanine Nicarico. Buckley alleged that, during the investigation and before any probable cause existed to arrest him, the prosecutors fabricated evidence — shopping among experts until one, over the contrary conclusions of three others, tied a bootprint found at the scene to Buckley's boot — and that the State's Attorney announced the indictment at a press conference. After the charges against him were eventually dropped, Buckley sued the prosecutors under § 1983. The lower courts held the prosecutors absolutely immune.

## Issue
Whether a prosecutor has absolute immunity from a § 1983 claim for (1) fabricating evidence during the preliminary investigation, before there was probable cause to arrest, and (2) making statements to the press.

## Rule
Prosecutorial immunity is functional: absolute immunity attaches to the advocate's tasks in initiating and pursuing a prosecution, but not to investigative or administrative work. Fixing the dividing line at probable cause, the Court held: "A prosecutor neither is, nor should consider himself to be, an advocate before he has probable cause to have anyone arrested." — 509 U.S. at 274. ^pin-274

## Application
When the prosecutors were endeavoring to manufacture the bootprint connection, they had not yet developed probable cause and their mission was "entirely investigative in character" — the work of detectives, not advocates — so absolute immunity did not reach it; only [[Qualified Immunity|qualified immunity]] did. Their statements at a press conference likewise fell outside the advocate's role and drew only [[Qualified Immunity|qualified immunity]]. Absolute immunity remained available for the prosecutors' genuinely advocatory conduct in presenting the State's case.

## Conclusion
The judgment was **reversed** in relevant part and the case [[Reading and Citing Cases#on-remand|remanded]]. Stevens, J., delivered the opinion of the Court; Scalia, J., concurred; Kennedy, J. (joined by Rehnquist, C.J., and White and Souter, JJ.), concurred in part and dissented in part.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Buckley* sharpens *[[Imbler v. Pachtman|Imbler]]*'s judicial-phase immunity test into a functional line: **advocacy** (initiating and presenting the case) is absolutely immune, while **investigation, administration, and press statements** get only [[Qualified Immunity|qualified immunity]]. Teach it alongside *[[Imbler v. Pachtman|Imbler]]* as the two poles of the prosecutorial-immunity spectrum.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Anchor*

## Sources
- [*Buckley v. Fitzsimmons*, 509 U.S. 259 (1993)](https://www.courtlistener.com/opinion/112894/buckley-v-fitzsimmons/) — pinpoint: 274 (Stevens, J., for the Court; the CL opinion text places the reporter star `*275` immediately after the quoted sentence, and the separate Kennedy opinion cross-references it as "Ante, at 274"). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "451ccd8e8a0d15db", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "509 U.S. 259 (1993)", "court": "U.S. Supreme Court", "neutral_cite": "1993 U.S. LEXIS 4400", "official_citation_present": true, "parallel_cite": "113 S. Ct. 2606; 125 L. Ed. 2d 209", "title": "Buckley v. Fitzsimmons", "year": "1993"}}
{"assertion_id": "58004fb5a47e7248", "dimension": "support", "kind": "home_role", "locator": {"home": "Absolute Immunity"}, "payload": {"home": "Absolute Immunity", "role": "Anchor", "title": "Buckley v. Fitzsimmons"}}
{"assertion_id": "e918ece32bc0bbae", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Absolute prosecutorial immunity extends only to the prosecutor's role as advocate in initiating and pursuing a prosecution; a prosecutor who fabricates evidence during the investigative phase, before there is probable cause to arrest, and who makes statements to the press, is protected by only qualified immunity.", "title": "Buckley v. Fitzsimmons"}}
{"assertion_id": "3e3fe9a7b8e27918", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Buckley v. Fitzsimmons"}}
{"assertion_id": "88f11861354c631b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Buckley v. Fitzsimmons", "varies_by_point": "false"}}
```

### lake record — Buckley v. Fitzsimmons

```json
{
  "schema_version": "s2.v1",
  "record_id": "Buckley v. Fitzsimmons",
  "status": "under_review",
  "identity": {
    "case_name": "Buckley v. Fitzsimmons",
    "case_name_short": "Buckley",
    "case_name_full": "BUCKLEY v. FITZSIMMONS Et Al.",
    "input_case_name": "Buckley v. Fitzsimmons",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1993-06-24",
    "year": 1993,
    "docket": "No. 91-7849",
    "cluster_id": 112894,
    "lead_opinion_id": 9432862,
    "sibling_ids": [],
    "absolute_url": "/opinion/112894/buckley-v-fitzsimmons/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "509 U.S. 259",
      "volume": "509",
      "reporter": "U.S.",
      "page": "259",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "113 S. Ct. 2606",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "2606",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "125 L. Ed. 2d 209",
        "volume": "125",
        "reporter": "L. Ed. 2d",
        "page": "209",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1993 U.S. LEXIS 4400",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "4400",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "509 U.S. 259",
        "volume": "509",
        "reporter": "U.S.",
        "page": "259",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 S. Ct. 2606",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "2606",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "125 L. Ed. 2d 209",
        "volume": "125",
        "reporter": "L. Ed. 2d",
        "page": "209",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 U.S. LEXIS 4400",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "4400",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "509 U.S. 259",
    "official_selection": {
      "court_class": "scotus",
      "selected": "509 U.S. 259",
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
    "date_created": "2026-07-06T13:53:46Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:53:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:53:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:53:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:53:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "buckley-v-fitzsimmons--112894",
      "to_record_id": "Buckley v. Fitzsimmons",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Buckley v. Fitzsimmons

```
<opinion type="majority">
<author id="b303-5">Justice Stevens</author>
<p id="As9">delivered the opinion of the Court.</p>
<p id="b303-6">In an action brought under <span class="citation no-link">42 U. S. C. § 1983</span>, petitioner seeks damages from respondent prosecutors for allegedly fabricating evidence diming the preliminary investigation of a crime and making false statements at a press conference announcing the return of an indictment. The questions presented are whether respondents are absolutely immune from liability on either or both of these claims.</p>
<p id="b303-7">As the case comes to us, we have no occasion to consider whether some or all of respondents’ conduct may be protected by qualified immunity. Moreover, we make two important assumptions about the case: first, that petitioner’s allegations are entirely true; and, second, that they allege constitutional violations for which § 1983 provides a remedy. Our statement of facts is therefore derived entirely from petitioner’s complaint and is limited to matters relevant to respondents’ claim to absolute immunity.</p>
<p id="b303-8">I</p>
<p id="b303-9">Petitioner commenced this action on March 4,1988, following his release from jail in Du Page County, Illinois. He had been incarcerated there for three years on charges growing out of the highly publicized murder of Jeanine Nicarico, an 11-year-old child, on February 25, 1983. The complaint, named 17 defendants, including Du Page County, its sheriff and seven of his assistants, two expert witnesses and the estate of a third, and the five respondents.</p>
<p id="b303-10">Respondent Fitzsimmons was the duly elected Du Page County State’s Attorney from the time of the Nicarico <page-number citation-index="1" label="262">*262</page-number>murder through December 1984, when he was succeeded by respondent Ryan, who had defeated him in a Republican primary election on March 21, 1984. Respondent Knight was an assistant state’s attorney under Fitzsimmons and served as a special prosecutor in the Nicarico case under Ryan. Respondents Kilander (who came into office with Ryan) and King were assistant prosecutors, also assigned to the case.</p>
<p id="b304-5">The theory of petitioner’s case is that in order to obtain an indictment in a case that had engendered “extensive publicity” and “intense emotions in the community,” the prosecutors fabricated false evidence, and that in order to gain votes, Fitzsimmons made false statements about petitioner in a press conference announcing his arrest and indictment 12 days before the primary election. Petitioner claims that respondents’ misconduct created a “highly prejudicial and inflamed atmosphere” that seriously impaired the fairness of the judicial proceedings against an innocent man and caused him to suffer a serious loss of freedom, mental anguish, and humiliation.</p>
<p id="b304-6">The fabricated evidence related to a bootprint on the door of the Nicarico home apparently left by the killer when he kicked in the door. After three separate studies by experts from the Du Page County Crime Lab, the Illinois Department of Law Enforcement, and the Kansas Bureau of Identification, all of whom were unable to make a reliable connection between the print and a pair of boots that petitioner had voluntarily supplied, respondents obtained a “positive identification” from one Louise Robbins, an anthropologist in North Carolina who was allegedly well known for her willingness to fabricate unreliable expert testimony. Her opinion was obtained during the early stages of the investigation, which was being conducted under the joint supervision and direction of the sheriff and respondent Fitzsimmons, whose <page-number citation-index="1" label="263">*263</page-number>police officers and assistant prosecutors were performing essentially the same investigatory functions.<footnotemark>1</footnotemark></p>
<p id="b305-5">Thereafter, having failed to obtain sufficient evidence to support petitioner’s (or anyone else’s) arrest, respondents convened a special grand jury for the sole purpose of investi<page-number citation-index="1" label="264">*264</page-number>gating the Nicarico case. After an 8-month investigation, during which the grand jury heard the testimony of over 100 witnesses, including the bootprint experts, it was still unable to return an indictment. On January 27, 1984, respondent Fitzsimmons admitted in a public statement that there was insufficient evidence to indict anyone for the rape and murder of Jeanine Nicarico. Although no additional evidence was obtained in the interim, the indictment was returned in March, when Fitzsimmons held the defamatory press conference so shortly before the primary election. Petitioner was then arrested, and because he was unable to meet the bond (set at $3 million), he was held in jail.</p>
<p id="b306-5">Petitioner’s trial began 10 months later, in January 1985. The principal evidence against him was provided by Robbins, the North Carolina anthropologist. Because the jury was unable to reach a verdict on the charges against petitioner, the trial judge declared a mistrial. Petitioner remained in prison for two more years, during which a third party confessed to the crime and the prosecutors prepared for petitioner’s retrial. After Robbins died, however, all charges against him were dropped. He was released, and filed this action.</p>
<p id="b306-6">II</p>
<p id="b306-7">We are not concerned with petitioner’s actions against the police officers (who have asserted the defense of qualified immunity), against the expert witnesses (whose trial testimony was granted absolute immunity by the District Court, App. 53-57), and against Du Page County (whose motion to dismiss on other grounds was granted in part, <em>id., </em>at 57-61). At issue here is only the action against the prosecutors, who moved to dismiss based on their claim to absolute immunity. The District Court held that respondents were entitled to absolute immunity for all claims except the claim against Fitzsimmons based on his press conference. <em>Id., </em>at 53. With respect to the claim based on the alleged fabrication of evidence, the District Court framed the question as whether <page-number citation-index="1" label="265">*265</page-number>the effort “to obtain definitive boot evidence linking [petitioner to the crime] was in the nature of acquisition of evidence or in the nature of evaluation of evidence for the purpose of initiating the criminal process.” <em>Id., </em>at 45. The Court concluded that it “appears” that it was more evaluative than acquisitive.</p>
<p id="b307-5">Both petitioner and Fitzsimmons appealed, and a divided panel of the Court of Appeals for the Seventh Circuit ruled that the prosecutors had absolute immunity on both claims. <em>Buckley </em>v. <em>Fitzsimmons, </em><span class="citation" data-id="9481079"><a href="/opinion/552217/stephen-buckley-plaintiff-appellee-cross-appellant-v-j-michael/" aria-description="Citation for case: Stephen Buckley, Plaintiff-Appellee-Cross-Appellant v. J....">919 F. 2d 1230</a></span> (1990). In the Court of Appeals’ view, “damages remedies are unnecessary,” <span class="citation" data-id="9481079"><a href="/opinion/552217/stephen-buckley-plaintiff-appellee-cross-appellant-v-j-michael/#1240" aria-description="Citation for case: Stephen Buckley, Plaintiff-Appellee-Cross-Appellant v. J...."><em>id., </em>at 1240</a></span>, when “[c]ourts can curtail the costs of prosecutorial blunders ... by cutting short the prosecution or mitigating its effects,” <span class="citation" data-id="9481079"><a href="/opinion/552217/stephen-buckley-plaintiff-appellee-cross-appellant-v-j-michael/#1241" aria-description="Citation for case: Stephen Buckley, Plaintiff-Appellee-Cross-Appellant v. J...."><em>id., </em>at 1241</a></span>. Thus, when “out-of-court acts cause injury only to the extent a case proceeds” in court, <span class="citation" data-id="9481079"><a href="/opinion/552217/stephen-buckley-plaintiff-appellee-cross-appellant-v-j-michael/#1242" aria-description="Citation for case: Stephen Buckley, Plaintiff-Appellee-Cross-Appellant v. J...."><em>id., </em>at 1242</a></span>, the prosecutor is entitled to absolute immunity and “the defendant must look to the court in which the case pends to protect his interests,” <span class="citation" data-id="9481079"><a href="/opinion/552217/stephen-buckley-plaintiff-appellee-cross-appellant-v-j-michael/#1241" aria-description="Citation for case: Stephen Buckley, Plaintiff-Appellee-Cross-Appellant v. J...."><em>id., </em>at 1241</a></span>. By contrast, if “a constitutional wrong is complete before the case begins,” the prosecutor is entitled only to qualified immunity. <span class="citation" data-id="9481079"><a href="/opinion/552217/stephen-buckley-plaintiff-appellee-cross-appellant-v-j-michael/#1241" aria-description="Citation for case: Stephen Buckley, Plaintiff-Appellee-Cross-Appellant v. J...."><em>Id., </em>at 1241-1242</a></span>. Applying this unprecedented theory to petitioner’s allegations, the Court of Appeals concluded that neither the press conference nor the fabricated evidence caused any constitutional injury independent of the indictment and trial. <span class="citation" data-id="9481079"><a href="/opinion/552217/stephen-buckley-plaintiff-appellee-cross-appellant-v-j-michael/#1243" aria-description="Citation for case: Stephen Buckley, Plaintiff-Appellee-Cross-Appellant v. J...."><em>Id., </em>at 1243, 1244</a></span>.<footnotemark>2</footnotemark></p>
<p id="b308-3"><page-number citation-index="1" label="266">*266</page-number>Judge Fairchild dissented in part. He agreed with the District Court that Fitzsimmons was entitled only to qualified immunity for his press statements. He noted that the majority had failed to examine the particular function that Fitzsimmons was performing, and concluded that conducting a press conference was not among “the functions that entitle judges and prosecutors in the judicial branch to absolute immunity.” <span class="citation" data-id="9481079"><a href="/opinion/552217/stephen-buckley-plaintiff-appellee-cross-appellant-v-j-michael/#1246" aria-description="Citation for case: Stephen Buckley, Plaintiff-Appellee-Cross-Appellant v. J...."><em>Id., </em>at 1246</a></span> (opinion dissenting in part and concurring in part). Responding directly to the majority’s reasoning, he wrote:</p>
<blockquote id="b308-4">“It is true that procedures afforded in our system of justice give a defendant a good chance to avoid such results of prejudicial publicity as excessive bail, difficulty or inability of selecting an impartial jury, and the like. These procedures reduce the cost of impropriety by a prosecutor, but I do not find that the courts have recognized their availability as a sufficient reason for conferring immunity.” <em><span class="citation" data-id="9481079"><a href="/opinion/552217/stephen-buckley-plaintiff-appellee-cross-appellant-v-j-michael/" aria-description="Citation for case: Stephen Buckley, Plaintiff-Appellee-Cross-Appellant v. J....">Ibid.</a></span></em></blockquote>
<p id="b308-5">We granted Buckley’s petition for certiorari, vacated the judgment, and remanded the case for further proceedings in light of our intervening decision in <em>Burns </em>v. <em>Reed, </em><span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/" aria-description="Citation for case: Burns v. Reed">500 U. S. 478</a></span> (1991). <span class="citation multiple-matches"><a href="/c/U.%20S./502/801/">502 U. S. 801</a></span> (1991). On remand, the same panel, again divided, reaffirmed its initial decision, with one modification not relevant here. <span class="citation" data-id="9482435"><a href="/opinion/574937/stephen-buckley-plaintiff-appellee-cross-appellant-v-j-michael/" aria-description="Citation for case: Stephen Buckley, Plaintiff-Appellee--Cross-Appellant v....">952 F. 2d 965</a></span> (CA7 1992) <em>(per curiam). </em>The Court of Appeals held that “[njothing in <em>Burns </em>undermine[d]” its initial holding that prosecutors are absolutely immune for “normal preparatory steps”; unlike the activities at issue in <em>Burns, </em>“[tjalking with (willing) experts is trial preparation.” <span class="citation" data-id="9482435"><a href="/opinion/574937/stephen-buckley-plaintiff-appellee-cross-appellant-v-j-michael/#966" aria-description="Citation for case: Stephen Buckley, Plaintiff-Appellee--Cross-Appellant v....">952 F. 2d, at 966-967</a></span>. In similar fashion, the court adhered to its conclusion that Fitzsimmons was entitled to absolute immunity for conducting the press conference. The court recognized that the press conference bore some similarities to the conduct in <em>Burns </em>(advising the police as to the propriety of an arrest). It did not take place in court, and it was not part of the prosecutor’s <page-number citation-index="1" label="267">*267</page-number>trial preparation. <span class="citation" data-id="9482435"><a href="/opinion/574937/stephen-buckley-plaintiff-appellee-cross-appellant-v-j-michael/#967" aria-description="Citation for case: Stephen Buckley, Plaintiff-Appellee--Cross-Appellant v....">952 F. 2d, at 967</a></span>. The difference, according to the court, is that “[a]n arrest causes injury whether or not a prosecution ensues,” whereas the only constitutional injury caused by the press conference depends on judicial action. <em><span class="citation" data-id="9482435"><a href="/opinion/574937/stephen-buckley-plaintiff-appellee-cross-appellant-v-j-michael/" aria-description="Citation for case: Stephen Buckley, Plaintiff-Appellee--Cross-Appellant v....">Ibid.</a></span></em></p>
<p id="b309-5">Judge Fairchild again dissented. He adhered to his earlier conclusion that Fitzsimmons was entitled to only qualified immunity for the press conference, but he was also persuaded that <em>Burns </em>had drawn a line between “ ‘conduct closely related to the judicial process’ ” and conduct in the role of “ ‘administrator or investigative officer.’ ” He agreed that trial preparation falls on the absolute immunity side of that line, but felt otherwise about the search for favorable evidence that might link the bootprint to petitioner during “a year long pre-arrest and pre-indictment investigation” aggressively supervised by Fitzsimmons. <span class="citation" data-id="9482435"><a href="/opinion/574937/stephen-buckley-plaintiff-appellee-cross-appellant-v-j-michael/#969" aria-description="Citation for case: Stephen Buckley, Plaintiff-Appellee--Cross-Appellant v....">952 F. 2d, at 969</a></span> (opinion dissenting in part).</p>
<p id="b309-6">We granted certiorari for a second time, limited to issues relating to prosecutorial immunity. <span class="citation multiple-matches"><a href="/c/U.%20S./506/814/">506 U. S. 814</a></span> (1992).<footnotemark>3</footnotemark> We now reverse.</p>
<p id="b309-7">Ill</p>
<p id="b309-8">The principles applied to determine the scope of immunity for state officials sued under Rev. Stat. § 1979, as amended, <page-number citation-index="1" label="268">*268</page-number><span class="citation no-link">42 U. S. C. § 1983</span>, are by now familiar. Section 1983 on its face admits of no defense of official immunity. It subjects to liability “[ejvery person” who, acting under color of state law, commits the prohibited acts. In <em>Tenney </em>v. <em>Brandhove, </em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/#376" aria-description="Citation for case: Tenney v. Brandhove">341 U. S. 367, 376</a></span> (1951), however, we held that Congress did not intend § 1983 to abrogate immunities “well grounded in history and reason.” Certain immunities were so well established in 1871, when §1983 was enacted, that “we presume that Congress would have specifically so provided had it wished to abolish” them. <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#554" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547, 554-555</a></span> (1967). See also <em>Newport </em>v. <em>Fact Concerts, Inc., </em><span class="citation" data-id="9428471"><a href="/opinion/110553/city-of-newport-v-fact-concerts-inc/#258" aria-description="Citation for case: City of Newport v. Fact Concerts, Inc.">453 U. S. 247, 258</a></span> (1981). Although we have found immunities in § 1983 that do not appear on the face of the statute, “[w]e do not have a license to establish immunities from §1983 actions in the interests of what we judge to be sound public policy.” <em>Tower </em>v. <em>Glover, </em><span class="citation" data-id="9842065"><a href="/opinion/111224/tower-v-glover/#922" aria-description="Citation for case: Tower v. Glover">467 U. S. 914, 922-923</a></span> (1984). “[Q]ur role is to interpret the intent of Congress in enacting § 1983, not to make a freewheeling policy choice.” <em>Malley </em>v. <em>Briggs, </em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#342" aria-description="Citation for case: Malley v. Briggs">475 U. S. 335, 342</a></span> (1986).</p>
<p id="b310-5">Since <em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/" aria-description="Citation for case: Tenney v. Brandhove">Tenney</a></span>, </em>we have recognized'two kinds of immunities under § 1983. Most public officials are entitled only to qualified immunity. <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#807" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 807</a></span> (1982); <em>Butz </em>v. <em>Economou, </em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#508" aria-description="Citation for case: Butz v. Economou">438 U. S. 478, 508</a></span> (1978). Under this form of immunity, government officials are not subject to damages liability for the performance of their discretionary functions when “their conduct does not violate clearly established statutory or constitutional rights of which a reasonable person would have known.” <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 818</a></span>. In most cases, qualified immunity is sufficient to “protect officials who are required to exercise their discretion and the related public interest in encouraging the vigorous exercise of official authority.” <em>Butz </em>v. <em>Economou, </em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#506" aria-description="Citation for case: Butz v. Economou">438 U. S., at 506</a></span>.</p>
<p id="b310-6">We have recognized, however, that some officials perform “special functions” which, because of their similarity to func<page-number citation-index="1" label="269">*269</page-number>tions that would have been immune when Congress enacted §1983, deserve absolute protection from damages liability. <em>Id., </em>at 508. “[T]he official seeking absolute immunity bears the burden of showing that such immunity is justified for the function in question.” <em>Burns </em>v. <em>Reed, </em><span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/#486" aria-description="Citation for case: Burns v. Reed">500 U. S., at 486</a></span>; <em>Antoine </em>v. <em>Byers &amp; Anderson, Inc., </em><span class="citation" data-id="112876"><a href="/opinion/112876/antoine-v-byers-anderson-inc/#432" aria-description="Citation for case: Antoine v. Byers &amp; Anderson, Inc.">508 U. S. 429, 432</a></span>, and n. 4 (1993). Even when we can identify a common-law tradition of absolute immunity for a given function, we have considered “whether §1983’s history or purposes nonetheless counsel against recognizing the same immunity in §1983 actions.” <em>Tower </em>v. <em>Glover, </em><span class="citation" data-id="9842065"><a href="/opinion/111224/tower-v-glover/#920" aria-description="Citation for case: Tower v. Glover">467 U. S., at 920</a></span>. Not surprisingly, we have been “quite sparing” in recognizing absolute immunity for state actors in this context. <em>Forrester </em>v. <em>White, </em><span class="citation" data-id="111977"><a href="/opinion/111977/forrester-v-white/#224" aria-description="Citation for case: Forrester v. White">484 U. S. 219, 224</a></span> (1988).</p>
<p id="b311-5">In determining whether particular actions of government officials fit within a common-law tradition of absolute immunity, or only the more general standard of qualified immunity, we have applied a “functional approach,” see, <em>e. g., Burns, </em><span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/#486" aria-description="Citation for case: Burns v. Reed">500 U. S., at 486</a></span>, which looks to “the nature of the function performed, not the identity of the actor who performed it,” <em>Forrester </em>v. <em>White, </em><span class="citation" data-id="111977"><a href="/opinion/111977/forrester-v-white/#229" aria-description="Citation for case: Forrester v. White">484 U. S., at 229</a></span>. We have twice applied this approach in determining whether the functions of contemporary prosecutors are entitled to absolute immunity.</p>
<p id="b311-6">In <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409</a></span> (1976), we held that a state prosecutor had absolute immunity for the initiation and pursuit of a criminal prosecution, including presentation of the State’s case at trial. Noting that our earlier cases had been “predicated upon a considered inquiry into the immunity historically accorded the relevant official at common law and the interests behind it,” <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#421" aria-description="Citation for case: Imbler v. Pachtman"><em>id., </em>at 421</a></span>, we focused on the functions of the prosecutor that had most often invited common-law tort actions. We concluded that the common-law rule of immunity for prosecutors was “well settled” and that “the same considerations of public policy that underlie the common-law rule likewise countenance absolute immu<page-number citation-index="1" label="270">*270</page-number>nity under § 1983.” <em>Id., </em>at 424. Those considerations<footnotemark>4</footnotemark> supported a rule of absolute immunity for conduct of prosecutors that was “intimately associated with the judicial phase of the criminal process.” <em>Id., </em>at 430. In concluding that “in initiating a prosecution and in presenting the State’s ease, the prosecutor is immune from a civil suit for damages under § 1983,” we did not attempt to describe the line between a prosecutor’s acts in preparing for those functions, some of which would be absolutely immune, and his acts of investigation or “administration,” which would not. <em>Id., </em>at 431, and n. 33.</p>
<p id="b312-5">We applied the <em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">Imbler</a></span> </em>analysis two Terms ago in <em>Burns </em>v. <span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/" aria-description="Citation for case: Burns v. Reed"><em>Reed, 500 </em>U. S. 478</a></span> (1991). There the § 1983 suit challenged two acts by a prosecutor: (1) giving legal advice to the police on the propriety of hypnotizing a suspect and on whether probable cause existed to arrest that suspect, and (2) participating in a probable-cause hearing. We held that only the latter was entitled to absolute immunity. Immunity for that action under § 1983 accorded with the common-law absolute immunity of prosecutors and other attorneys for eliciting false or defamatory testimony from witnesses or for making false or defamatory statements during, and related to, judicial proceedings. <em>Id., </em>at 489-490; <em>id., </em>at 501 (Scalia, J., concurring in judgment in part and dissenting in <page-number citation-index="1" label="271">*271</page-number>part). Under that analysis, appearing before a judge and presenting evidence in support of a motion for a search warrant involved the prosecutor’s “‘role as advocate for the State.’ ” <em>Id., </em>at 491, quoting <em>Imbler, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#431" aria-description="Citation for case: Imbler v. Pachtman">424 U. S., at 431, n. 33</a></span>. Because issuance of a search warrant is a judicial act, appearance at the probable-cause hearing was “ ‘intimately associated with the judicial phase of the criminal process,’ ” <em>Burns, </em><span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/#492" aria-description="Citation for case: Burns v. Reed">500 U. S., at 492</a></span>, quoting <em>Imbler, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#430" aria-description="Citation for case: Imbler v. Pachtman">424 U. S., at 430</a></span>.</p>
<p id="b313-5">We further decided, however, that prosecutors are not entitled to absolute immunity for their actions in giving legal advice to the police. We were unable to identify any historical or common-law support for absolute immunity in the performance of this function. <span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/#492" aria-description="Citation for case: Burns v. Reed">500 U. S., at 492-493</a></span>. We also noted that any threat to the judicial process from “the harassment and intimidation associated with litigation” based on advice to the police was insufficient to overcome the “[a]bsen[ce] [of] a tradition of immunity comparable to the common-law immunity from malicious prosecution, which formed the basis for the decision in <span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/#493" aria-description="Citation for case: Burns v. Reed"><em>Imbler.” Id., </em>at 493, 494</a></span>. And though we noted that several checks other than civil litigation prevent prosecutorial abuses in advising the police, “one of the most important checks, the judicial process,” will not be effective in all cases, especially when in the end the suspect is not prosecuted. <span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/#496" aria-description="Citation for case: Burns v. Reed"><em>Id., </em>at 496</a></span>. In sum, we held that providing legal advice to the police was not a function “closely associated with the judicial process.” <span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/#495" aria-description="Citation for case: Burns v. Reed"><em>Id., </em>at 495</a></span>.</p>
<p id="b313-6">IV</p>
<p id="b313-7">In this case the Court of Appeals held that respondents are entitled to absolute immunity because the injuries suffered by petitioner occurred during criminal proceedings. That holding is contrary to the approach we have consistently followed since <em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">Imbler</a></span>. </em>As we have noted, the <em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">Imbler</a></span> </em>approach focuses on the conduct for which immunity is claimed, not on the harm that the conduct may have caused or the question whether it was lawful. The location of the <page-number citation-index="1" label="272">*272</page-number>injury may be relevant to the question whether a complaint has adequately alleged a cause of action for damages (a question that this case does not present, see <em>supra, </em>at 261). It is irrelevant, however, to the question whether the conduct of a prosecutor is protected by absolute immunity. Accordingly, although the Court of Appeals’ reasoning may be relevant to the proper resolution of issues that are not before us, it does not provide an acceptable basis for concluding that either the preindictment fabrication of evidence or the post-indictment press conference was a function protected by absolute immunity. We therefore turn to consider each of respondents’ claims of absolute immunity.</p>
<p id="b314-5">A</p>
<p id="b314-6">We first address petitioner’s argument that the prosecutors are not entitled to absolute immunity for the claim that they conspired to manufacture false evidence that would link his boot with the bootprint the murderer left on the front door. To obtain this false evidence, petitioner submits, the prosecutors shopped for experts until they found one who would provide the opinion they sought. App. 7-9. At the time of this witness shopping the assistant prosecutors were working hand in hand with the sheriff’s detectives under the joint supervision of the sheriff and State’s attorney Fitzsimmons.</p>
<p id="b314-7">Petitioner argues that Imbler]s protection for a prosecutor’s conduct “in initiating a prosecution and in presenting the State’s case,” <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#431" aria-description="Citation for case: Imbler v. Pachtman">424 U. S., at 431</a></span>, extends only to the act of initiation itself and to conduct occurring in the courtroom. This extreme position is plainly foreclosed by our opinion in <em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">Imbler</a></span> </em>itself. We expressly stated that “the duties of the prosecutor in his role as advocate for the State involve actions preliminary to the initiation of a prosecution and actions apart from the courtroom,” and are nonetheless entitled to absolute immunity. <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#431" aria-description="Citation for case: Imbler v. Pachtman"><em>Id., </em>at 431, n. 33</a></span>. We noted in particular that an out-of-court “effort to control the presen<page-number citation-index="1" label="273">*273</page-number>tation of [a] witness’ testimony” was entitled to absolute immunity because it was “fairly within [the prosecutor’s] function as an advocate.” <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#430" aria-description="Citation for case: Imbler v. Pachtman"><em>Id., </em>at 430, n. 32</a></span>. To be sure, <em>Burns </em>made explicit the point we had reserved in <em>Imbler, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#430" aria-description="Citation for case: Imbler v. Pachtman">424 U. S., at 430-431</a></span>, and n. 33: A prosecutor’s administrative duties and those investigatory functions that do not relate to an advocate’s preparation for the initiation of a prosecution or for judicial proceedings are not entitled to absolute immunity. See <em>Burns, </em><span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/#494" aria-description="Citation for case: Burns v. Reed">500 U. S., at 494-496</a></span>. We have not retreated, however, from the principle that acts undertaken by a prosecutor in preparing for the initiation of judicial proceedings or for trial, and which occur in the course of his role as an advocate for the State, are entitled to the protections of absolute immunity. Those acts must include the professional evaluation of the evidence assembled by the police and appropriate preparation for its presentation at trial or before a grand jury after a decision to seek an indictment has been made.</p>
<p id="b315-5">On the other hand, as the function test of <em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">Imbler</a></span> </em>recognizes, the actions of a prosecutor are not absolutely immune merely because they are performed by a prosecutor. Qualified immunity “ ‘represents the norm’ ” for executive officers, <em>Malley </em>v. <em>Briggs, </em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#340" aria-description="Citation for case: Malley v. Briggs">475 U. S., at 340</a></span>, quoting <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#807" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 807</a></span>, so when a prosecutor “functions as an administrator rather than as an officer of the court” he is entitled only to qualified immunity. <em>Imbler, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#431" aria-description="Citation for case: Imbler v. Pachtman">424 U. S., at 431, n. 33</a></span>. There is a difference between the advocate’s role in evaluating evidence and interviewing witnesses as he prepares for trial, on the one hand, and the detective’s role in searching for the clues and corroboration that might give him probable cause to recommend that a suspect be arrested, on the other hand. When a prosecutor performs the investigative functions normally performed by a detective or police officer, it is “neither appropriate nor justifiable that, for the same act, immunity should protect the one and not the other.” <em>Hampton </em>v. <em>Chicago, </em><span class="citation multiple-matches"><a href="/c/F.%202d/484/602/">484 F. 2d 602</a></span>, 608 (CA7 1973) <page-number citation-index="1" label="274">*274</page-number>(internal quotation marks omitted), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./415/917/">415 U. S. 917</a></span> (1974). Thus, if a prosecutor plans and executes a raid on a suspected weapons cache, he “has no greater claim to complete immunity than activities of police officers allegedly acting under his direction.” 484 F. 2d, at 608-609.</p>
<p id="b316-5">The question, then, is whether the prosecutors have carried their burden of establishing that they were functioning as “advocates” when they were endeavoring to determine whether the bootprint at the scene of the crime had been made by petitioner’s foot. A careful examination of the allegations concerning the conduct of the prosecutors during the period before they convened a special grand jury to investigate the crime provides the answer. See <em>supra, </em>at 263, n. 1. The prosecutors do not contend that they had probable cause to arrest petitioner or to initiate judicial proceedings during that period. Their mission at that time was entirely investigative in character. A prosecutor neither is, nor should consider himself to be, an advocate before he has probable cause to have anyone arrested.<footnotemark>5</footnotemark></p>
<p id="b317-4"><page-number citation-index="1" label="275">*275</page-number>11 was well after the alleged fabrication of false evidence concerning the bootprint that a special grand jury was empaneled. And when it finally was convened, its immediate purpose was to conduct a more thorough investigation of the crime — not to return an indictment against a suspect whom there was already probable cause to arrest. Buckley was not arrested, in fact, until 10 months after the grand jury had been convened and had finally indicted him. Under these circumstances, the prosecutors’ conduct occurred well before they could properly claim to be acting as advocates. Respondents have not cited any authority that supports an argument that a prosecutor’s fabrication of false evidence during the preliminary investigation of an unsolved crime was immune from liability at common law, either in 1871 or at any date before the enactment of §1983. It therefore remains protected only by qualified immunity.</p>
<p id="b317-5">After <em>Burns, </em>it would be anomalous, to say the least, to grant prosecutors only qualified immunity when offering legal advice to police about an unarrested suspect, but then to endow them with absolute immunity when conducting investigative work themselves in order to decide whether a suspect may be arrested.<footnotemark>6</footnotemark> That the prosecutors later called <page-number citation-index="1" label="276">*276</page-number>a grand jury to consider the evidence this work produced does not retroactively transform that work from the administrative into the prosecutorial.<footnotemark>7</footnotemark> A prosecutor may not shield his investigative work with the aegis of absolute immunity merely because, after a suspect is eventually arrested, indicted, and tried, that work may be retrospectively described as “preparation” for a possible trial; every prosecutor might then shield himself from liability for any constitutional wrong against innocent citizens by ensuring that they go to trial. When the functions of prosecutors and detectives are the same, as they were here, the immunity that protects them is also the same.</p>
<p id="b318-5">B</p>
<p id="b318-6">We next consider petitioner’s claims regarding Fitzsimmons’ statements to the press. Petitioner alleged that, during the prosecutor’s public announcement of the indictment, Fitzsimmons made false assertions that numerous pieces of evidence, including the bootprint evidence, tied Buckley to a burglary ring that committed the Nicarico murder. App. 12. Petitioner also alleged that Fitzsimmons released mug shots of him to the media, “which were prominently and repeatedly displayed on television and in the newspapers.” <em>Ibid. </em>Peti<page-number citation-index="1" label="277">*277</page-number>tioner’s legal theory is that “[t]hese false and prejudicial statements inflamed the populace of DuPage County against” him, <em>ibid.; </em>see also <em>id., </em>at 14, thereby defaming him, resulting in deprivation of his right to a fair trial, and causing the jury to deadlock rather than acquit, <em>id., </em>at 19.</p>
<p id="b319-4">Fitzsimmons’ statements to the media are not entitled to absolute immunity. Fitzsimmons does not suggest that in 1871 there existed a common-law immunity for a prosecutor’s, or attorney’s, out-of-court statement to the press. The Court of Appeals agreed that no such historical precedent exists. <span class="citation" data-id="9482435"><a href="/opinion/574937/stephen-buckley-plaintiff-appellee-cross-appellant-v-j-michael/#967" aria-description="Citation for case: Stephen Buckley, Plaintiff-Appellee--Cross-Appellant v....">952 F. 2d, at 967</a></span>. Indeed, while prosecutors, like all attorneys, were entitled to absolute immunity from defamation liability for statements made during the course of judicial proceedings and relevant to them, see <em>Burns, </em><span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/#489" aria-description="Citation for case: Burns v. Reed">500 U. S., at 489-490</a></span>; <em>Irnbler, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#426" aria-description="Citation for case: Imbler v. Pachtman">424 U. S., at 426, n. 23</a></span>; <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#439" aria-description="Citation for case: Imbler v. Pachtman"><em>id., </em>at 439</a></span> (White, J., concurring in judgment), most statements made out of court received only good-faith immunity. The common-law rule was that “[t]he speech of a counsel is privileged by the occasion on which it is spoken . . . .” <em>Flint </em>v. <em>Pike, </em>4 Barn. &amp; Cress. 473, 478, 107 Eng. Rep. 1136, 1138 (K. B. 1825) (Bayley, J.).<footnotemark>8</footnotemark></p>
<p id="b319-5">The functional approach of <em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">Imbler</a></span>, </em>which conforms to the common-law theory, leads us to the same conclusion. Comments to the media have no functional tie to the judicial process just because they are made by a prosecutor. At the <page-number citation-index="1" label="278">*278</page-number>press conference, Fitzsimmons did not act in “‘his role as advocate for the State,’ ” <em>Burns </em>v. <em>Reed, </em><span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/#491" aria-description="Citation for case: Burns v. Reed">500 U. S., at 491</a></span>, quoting <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#431" aria-description="Citation for case: Imbler v. Pachtman">424 U. S., at 431, n. 33</a></span>. The conduct of a press conference does not involve the initiation of a prosecution, the presentation of the State’s case in court, or actions preparatory for these functions. Statements to the press may be an integral part of a prosecutor’s job, see National District Attorneys Assn., National Prosecution Standards 107, 110 (2d ed. 1991), and they may serve a vital public function. But in these respects a prosecutor is in no different position than other executive officials who deal with the press, and, as noted, <em>supra, </em>at 268, 277, qualified immunity is the norm for them.</p>
<p id="b320-5">Fitzsimmons argues nonetheless that policy considerations support extending absolute immunity to press statements. Brief for Respondents 30-33. There are two responses to his submissions. First, “[w]e do not have a license to establish immunities from § 1983 actions in the interests of what we judge to be sound public policy.” <em>Tower </em>v. <em>Glover, </em><span class="citation" data-id="9842065"><a href="/opinion/111224/tower-v-glover/#922" aria-description="Citation for case: Tower v. Glover">467 U. S., at 922-923</a></span>. When, as here, the prosecutorial function is not within the advocate’s role and there is no historical tradition of immunity on which we can draw, our inquiry is at an end. Second, “[t]he presumption is that qualified rather than absolute immunity is sufficient to protect government officials in the exercise of their duties.” <em>Burns </em>v. <em>Reed, </em><span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/#486" aria-description="Citation for case: Burns v. Reed">500 U. S., at 486-487</a></span>. Even if policy considerations allowed us to carve out new absolute immunities to liability for constitutional wrongs under § 1983, we see little reason to suppose that qualified immunity would provide adequate protection to prosecutors in their provision of legal advice to the police, see <em>id., </em>at 494-496, yet would fail to provide sufficient protection in the present context.<footnotemark>9</footnotemark></p>
<p id="A2G"><page-number citation-index="1" label="279">*279</page-number>V</p>
<p id="b321-4">In his complaint, petitioner also charged that the prosecutors violated his rights under the Due Process Clause through extraction of statements implicating him by coercing two witnesses and paying them money. App. 9-11, 19. The precise contours of these claims are unclear, and they were not addressed below; we leave them to be passed on in the first instance by the Court of Appeals on remand.</p>
<p id="b321-5">As we have stated, <em>supra, </em>at 261, 264, 265, n. 2, petitioner does not challenge many aspects of the Court of Appeals’ decision, and we have not reviewed them; they remain undisturbed by this opinion. As to the two challenged rulings on absolute immunity, however, the judgment of the United States Court of Appeals for the Seventh Circuit is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b321-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b305-6"> The relevant period and prosecutorial functions are described in petitioner’s first amended complaint:</p>
<blockquote id="b305-7">“28) Defendant Knight, and various others [sic] Defendants, including Doria, Fitzsimmons, and Burandt, apparently not satisfied with Defendant German’s conclusions, contacted anthropologist Louise Robbins and Defendant Olsen of the Kansas Bureau of Indentification [sic] Crime Lab in search of a positive boot identification.</blockquote>
<blockquote id="b305-8">“31) Confronted with three different expert reports which failed to match Plaintiff’s boot with the footprint on the door, the Defendants, including Knight, Burandt, and German, procured their ‘positive identification’ from Louise Robbins, whose theories and reputation in the forensic community were generally discredited and viewed with great skepticism, a fact these Defendants knew or should have known.</blockquote>
<blockquote id="b305-9">“32) Defendants Knight and King were involved with the Sheriff’s police in all the early stages of their investigation, including the interrogation of witnesses and potential suspects. Specifically, Sheriff’s detectives, including defendants Wilkosz and Kurzawa, at the direction and under the supervision, and sometimes in the presence and with the assistance of Defendants Knight, King, Soucek and Lepic, repeatedly interrogated alleged suspects, including Plaintiff Buckley and Alex Hernandez, who were not represented by counsel. Despite intense pressure and intimidation, Plaintiff Buckley steadfastly maintained his innocence and demonstrated no knowledge of the crime, while Hernandez told such wild and palpably false stories that his mental instability was obvious to the Defendants.</blockquote>
<blockquote id="b305-10">“33) As a result of these interrogations, at least one experienced Sheriff’s detective who participated^] concluded that Buckley and Hernandez were not involved in the Nicarico crime. This conclusion was buttressed by his general knowledge of the bootprint ‘evidence.’</blockquote>
<blockquote id="b305-11">“34) He repeatedly communicated his conclusion, and its basis, to the Defendants named herein, including Defendants Doria, Knight, King, Soucek, Lepic, and Wilkosz.</blockquote>
<blockquote id="b305-12">“36) Unable to solve the case, Defendants Doria, Fitzsimmons, Knight and King convened a special Du Page County ‘investigativé’ grand jury, devoted solely to investigating the Nicarico case.” App. 8-10.</blockquote>
</footnote>
<footnote label="2">
<p id="b307-6"> With respect to an issue not before us, petitioner’s claims that he was subject to coercive interrogations by some of the respondent prosecutors, the court found that the extent of immunity depended on the nature of those claims. The court reasoned that, because claims based on <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), and the Self-Incrimination Clause of the Fifth Amendment depend on what happens at trial, prosecutors are entitled to absolute immunity for those claims; by contrast, only qualified immunity is available against petitioner’s claims as to “coercive tactics that are independently wrongful.” <span class="citation" data-id="9481079"><a href="/opinion/552217/stephen-buckley-plaintiff-appellee-cross-appellant-v-j-michael/#1244" aria-description="Citation for case: Stephen Buckley, Plaintiff-Appellee-Cross-Appellant v. J....">919 F. 2d, at 1244</a></span>. Because it could not characterize the nature of those claims, the court remanded for further proceedings concerning Fitzsimmons, King, and Knight on this issue. <span class="citation" data-id="9481079"><a href="/opinion/552217/stephen-buckley-plaintiff-appellee-cross-appellant-v-j-michael/#1245" aria-description="Citation for case: Stephen Buckley, Plaintiff-Appellee-Cross-Appellant v. J...."><em>Id., </em>at 1245</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b309-9"> Although petitioner also alleged that respondents violated his constitutional rights in presenting the fabricated evidence to the grand jury and his trial jury, see App. 10-11,14-15, we are not presented with any question regarding those claims. The Court of Appeals agreed with the District Court, see <em>id., </em>at 45-47, and held that those actions were protected by absolute immunity. <em>Buckley </em>v. <em>Fitzsimmons, </em><span class="citation" data-id="9481079"><a href="/opinion/552217/stephen-buckley-plaintiff-appellee-cross-appellant-v-j-michael/#1243" aria-description="Citation for case: Stephen Buckley, Plaintiff-Appellee-Cross-Appellant v. J....">919 F. 2d 1230, 1243</a></span> (CA7 1990) (“The selection of evidence to present to the grand jurors, and the manner of questioning witnesses, can no more be the basis of liability than may the equivalent activities before the petit jury”). That decision was made according to traditional principles of absolute immunity under § 1983, however, and did not depend on the original, injury-focused theory of absolute prosecutorial immunity with which we are concerned here; nor was it included within the questions presented in petitioner’s petition for certiorari.</p>
</footnote>
<footnote label="4">
<p id="b312-6"> In particular, we expressed concern that fear of potential liability would undermine a prosecutor’s performance of his duties by forcing him to consider his own potential liability when making prosecutorial decisions and by diverting his “energy and attention . . . from the pressing duty of enforcing the criminal law.” <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#424" aria-description="Citation for case: Imbler v. Pachtman">424 U. S., at 424-425</a></span>. Suits against prosecutors would devolve into “a virtual retrial of the criminal offense of a new forum,” <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#425" aria-description="Citation for case: Imbler v. Pachtman"><em>id., </em>at 425</a></span>, and would undermine the vigorous enforcement of the law by providing a prosecutor an incentive not “to go forward with a close case where an acquittal likely would trigger a suit against him for damages,” <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#426" aria-description="Citation for case: Imbler v. Pachtman"><em>id., </em>at 426</a></span>, and n. 24. We also expressed concern that the availability of a damages action might cause judges to be reluctant to award relief to convicted defendants in post-trial motions. <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#427" aria-description="Citation for case: Imbler v. Pachtman"><em>Id., </em>at 427</a></span>. <page-number citation-index="1" label="275">*275</page-number>might be subject to liability for one but not the other, the dissent allows its particular policy concerns to erase the function test it purports to respect.</p>
<p id="b317-8">In general, the dissent’s distress over the denial of absolute immunity for prosecutors who fabricate evidence regarding unsolved crimes, <em>post, </em>at 283-285, like the holding of the Court of Appeals, seems to conflate the question whether a § 1983 plaintiff has stated a cause of action with the question whether the defendant is entitled to absolute immunity for his actions.</p>
</footnote>
<footnote label="5">
<p id="b316-6"> Of course, a determination of probable cause does not guarantee a prosecutor absolute immunity from liability for all actions taken after-wards. Even after that determination, as the opinion dissenting in part points out, <em>post, </em>at 290, a prosecutor may engage in “police investigative work” that is entitled to only qualified immunity.</p>
<p id="b316-7">Furthermore, there is no “true anomaly,” <em>post, </em>at 286, in denying absolute immunity for a state actor’s investigative acts made before there is probable cause to have a suspect arrested just because a prosecutor would be entitled to absolute immunity for the malicious prosecution of someone whom he lacked probable cause to indict. That criticism ignores the essence of the function test. The reason that lack of probable cause allows us to deny absolute immunity to a state actor for the former function (fabrication of evidence) is that there is no common-law tradition of immunity for it, whether performed by a police officer or prosecutor. The reason that we grant it for the latter function (malicious prosecution) is that we have found a common-law tradition of immunity for a prosecutor’s decision to bring an indictment, whether he has probable cause or not. By insisting on an equation of the two functions merely because a prosecutor</p>
</footnote>
<footnote label="6">
<p id="b317-11"> Cf. <em>Burns </em>v. <em>Reed, </em><span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/#495" aria-description="Citation for case: Burns v. Reed">500 U. S. 478, 495</a></span> (1991): “Indeed, it is incongruous to allow prosecutors to be absolutely immune from liability for giving advice to the police, but to allow police officers only qualified immunity for following the advice... . Almost any action by a prosecutor, including his or her direct participation in purely investigative activity, could be said to be in some way related to the ultimate decision whether to prosecute, but we have never indicated that absolute immunity is that expansive.” If the police, under the guidance of the prosecutors, had solicited the alleg<page-number citation-index="1" label="276">*276</page-number>edly “fabricated” testimony, of course, they would not be entitled to anything more than qualified immunity.</p>
</footnote>
<footnote label="7">
<p id="b318-9"> See <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#431" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409, 431, n. 33</a></span> (1976): “Preparation, both for the initiation of the criminal process and for a trial, may require the obtaining, reviewing, and evaluating of evidence. At some point, and with respect to some decisions, the prosecutor no doubt functions as an administrator rather than as an officer of the court. Drawing a proper line between these functions may present difficult questions, but this case does not require us to anticipate them.” Although the respondents rely on the first sentence of this passage to suggest that a prosecutor’s actions in “obtaining, reviewing, and evaluating” evidence are always protected by absolute immunity, the sentence that follows qualifies that suggestion. It confirms that some of these actions may fall on the administrative, rather than the judicial, end of the prosecutor’s activities, and therefore be entitled only to qualified immunity.</p>
</footnote>
<footnote label="8">
<p id="b319-6"> “[Absolute immunity] does not apply to or include any publication of defamatory matter before the commencement, or after the termination of the judicial proceeding (unless such publication is an act incidental to the proper initiation thereof, or giving legal effect thereto); nor does it apply to or include any publication of defamatory matter to any person other than those to whom, or in any place other than that in which, such publication is required or authorized by law to be made for the proper conduct of the judicial proceedings.” Veeder, Absolute Immunity in Defamation: Judicial Proceedings, <span class="citation no-link">9 Colum. L. Rev. 463</span>, 489 (1909) (footnotes omitted). See, <em>e. g., Viosca </em>v. <em>Landfried, </em><span class="citation no-link">140 La. 610</span>, 615, <span class="citation" data-id="7170264"><a href="/opinion/7256474/viosca-v-landfried/#700" aria-description="Citation for case: Viosca v. Landfried">73 So. 698, 700</a></span> (1916); <em>Youmans </em>v. <em>Smith, </em><span class="citation" data-id="3579619"><a href="/opinion/3598358/youmans-v-smith/#220" aria-description="Citation for case: Youmans v. . Smith">153 N. Y. 214, 220-223</a></span>, <span class="citation" data-id="3579619"><a href="/opinion/3598358/youmans-v-smith/#267" aria-description="Citation for case: Youmans v. . Smith">47 N. E. 265, 267-268</a></span> (1897). See also G. Bower, Law of Actionable Defamation 103, n. <em>h, </em>104-105 (1908).</p>
</footnote>
<footnote label="9">
<p id="b320-6"> The Circuits other than the Seventh Circuit that have addressed this issue have applied only qualified immunity to press statements, see, <em>e. g., Powers </em>v. <em>Coe, </em><span class="citation" data-id="431713"><a href="/opinion/431713/arthur-b-powers-v-glenn-e-coe-and-austin-j-mcguigan/#103" aria-description="Citation for case: Arthur B. Powers v. Glenn E. Coe and Austin J. McGuigan">728 F. 2d 97, 103</a></span> (CA2 1984); <em>Marrero </em>v. <em>Hialeah, </em><span class="citation" data-id="380133"><a href="/opinion/380133/juan-a-marrero-and-maria-marrero-v-city-of-hialeah-etc/#506" aria-description="Citation for case: Juan A. Marrero and Maria Marrero v. City of Hialeah, Etc.">625 F. 2d 499, 506-507</a></span> (CA5 1980), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./450/913/">450 U. S. 913</a></span> (1981); <em>Gobel </em>v. <em>Mari</em><page-number citation-index="1" label="279">*279</page-number><em>copa County, </em><span class="citation" data-id="518482"><a href="/opinion/518482/earl-edwin-gobel-and-michael-j-defranco-v-maricopa-county-thomas-e/#1205" aria-description="Citation for case: Earl Edwin Gobel and Michael J. Defranco v. Maricopa...">867 F. 2d 1201, 1205</a></span> (CA9 1989); <em>England </em>v. <em>Hendricks, </em><span class="citation" data-id="8972057"><a href="/opinion/8980223/england-v-hendricks/#285" aria-description="Citation for case: England v. Hendricks">880 F. 2d 281, 285</a></span> (CA10 1989), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./493/1078/">493 U. S. 1078</a></span> (1990); <em>Marx </em>v. <em>Gumbinner, </em><span class="citation" data-id="9478087"><a href="/opinion/510760/richard-marx-individually-and-kristina-marx-a-minor-v-glenn-h/#791" aria-description="Citation for case: Richard Marx, Individually and Kristina Marx, a Minor v....">855 F. 2d 783, 791</a></span> (CA11 1988); cf. <em>Rose </em>v. <em>Bartle, </em><span class="citation" data-id="8968355"><a href="/opinion/8976609/rose-v-bartle/#346" aria-description="Citation for case: Rose v. Bartle">871 F. 2d 331, 346-346</a></span> (CA3 1989), yet Fitzsimmons has not suggested that prosecutors in those Circuits have been unduly constrained in keeping the public informed of pending criminal prosecutions. We also do not perceive why anything except a firm common-law rule should entitle a prosecutor to absolute immunity for his statements to the press when nortprosecutors who make similar statements, for instance, an attorney general’s press spokesperson or a police officer announcing the return of an indictment, receive only qualified immunity.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Bumper v. North Carolina.md  (`case`, 5 assertions)

### content_page

```
---
title: "Bumper v. North Carolina"
type: case
citation: "391 U.S. 543 (1968)"
parallel_cite: "88 S. Ct. 1788; 20 L. Ed. 2d 797; 46 Ohio Op. 2d 382"
neutral_cite: 1968 U.S. LEXIS 1470
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1968
date_decided: 1968-06-03
docket: 1016
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1968-06-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Bumper v. North Carolina
  varies_by_point: false
  scope_note: "Foundational consent-voluntariness rule; good law and incorporated into the Schneckloth totality-of-circumstances framework."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107716/bumper-v-north-carolina/"
  cluster_id: 107716
  opinion_id: 107716
  identity_checked: true
homes:
  - page: "[[Consent Searches]]"
    role: "Limiting (voluntariness)"
related: ["[[Schneckloth v. Bustamonte]]"]
aliases: []
tags: ["case", "fourth-amendment", "consent", "voluntariness", "claim-of-authority", "warrant"]
holding: "Consent to search is involuntary, and cannot justify a search, when it is given only in acquiescence to an officer's claim of lawful authority — including a false or unsubstantiated assertion that the officer holds a warrant; the State bears the burden of proving voluntary consent."
lake:
  record_id: Bumper v. North Carolina
  status: verified
  projected_at: 2026-07-06
---

# Bumper v. North Carolina

*391 U.S. 543 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers investigating a rape went to the home where the suspect, Bumper, lived with his grandmother, Mrs. Leath. They told her they had a search warrant, and she replied "Go ahead" and let them in. They found a rifle later admitted at trial to convict Bumper. At the [[Common Legal Terms#suppression-hearing|suppression hearing]] the prosecution did not rely on — or even produce — any warrant; it sought to justify the search solely as consensual.

## Issue
Whether a homeowner's permission to search, given after officers assert that they have a search warrant, constitutes valid voluntary consent under the Fourth Amendment when the warrant's validity is not established.

## Rule
No. "When a prosecutor seeks to rely upon consent to justify the lawfulness of a search, he has the burden of proving that the consent was, in fact, freely and voluntarily given. This burden cannot be discharged by showing no more than acquiescence to a claim of lawful authority." — 391 U.S. at 548–549. ^pin-548

A claimed-warrant entry is inherently coercive: "When a law enforcement officer claims authority to search a home under a warrant, he announces in effect that the occupant has no right to resist the search. The situation is instinct with coercion — albeit colorably lawful coercion. Where there is coercion there cannot be consent." — *Id.* at 550. ^pin-550

## Application
Mrs. Leath let the officers in only because they announced they had a warrant — a claim the State never substantiated and did not rely on at the hearing. Her "Go ahead" was therefore mere acquiescence to a claim of lawful authority, not free and voluntary consent. The State could not discharge its burden of proving voluntariness, so the search could not be justified as consensual and the rifle should have been suppressed.

## Conclusion
There was no valid consent; admitting the rifle was constitutional error. The judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Bumper* states the enduring rule that consent is involuntary when it is mere acquiescence to a claimed authority (especially a false claim of warrant), and that the government bears the burden of proving voluntariness — principles carried forward in the totality-of-circumstances test of [[Schneckloth v. Bustamonte]].

## Appears on
- [[Consent Searches]] — *Limiting (voluntariness)*

## Sources
- *Bumper v. North Carolina*, 391 U.S. 543 (1968) — https://www.courtlistener.com/opinion/107716/bumper-v-north-carolina/ — pinpoints: 548–549, 550.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "bf9a70088e135c0e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "391 U.S. 543 (1968)", "court": "U.S. Supreme Court", "neutral_cite": "1968 U.S. LEXIS 1470", "official_citation_present": true, "parallel_cite": "88 S. Ct. 1788; 20 L. Ed. 2d 797; 46 Ohio Op. 2d 382", "title": "Bumper v. North Carolina", "year": "1968"}}
{"assertion_id": "6c8e4754630e2de9", "dimension": "support", "kind": "home_role", "locator": {"home": "Consent Searches"}, "payload": {"home": "Consent Searches", "role": "Limiting (voluntariness)", "title": "Bumper v. North Carolina"}}
{"assertion_id": "b06b39ee7714bb7f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Consent to search is involuntary, and cannot justify a search, when it is given only in acquiescence to an officer's claim of lawful authority — including a false or unsubstantiated assertion that the officer holds a warrant; the State bears the burden of proving voluntary consent.", "title": "Bumper v. North Carolina"}}
{"assertion_id": "1c8b4bf8ca6aa95b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1968-06-03", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Bumper v. North Carolina", "field_i_validity": "good_law", "scope_note": "Foundational consent-voluntariness rule; good law and incorporated into the Schneckloth totality-of-circumstances framework.", "title": "Bumper v. North Carolina", "varies_by_point": "false"}}
{"assertion_id": "9e23304386eb2cca", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Bumper v. North Carolina"}}
```

### lake record — Bumper v. North Carolina

```json
{
  "schema_version": "s2.v1",
  "record_id": "Bumper v. North Carolina",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Bumper v. North Carolina",
    "case_name_short": "Bumper",
    "case_name_full": "Bumper v. North Carolina",
    "input_case_name": "Bumper v. North Carolina",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-06-03",
    "year": 1968,
    "docket": "1016",
    "cluster_id": 107716,
    "lead_opinion_id": 107716,
    "sibling_ids": [
      107716,
      9423732,
      9423733,
      9423734,
      9423735
    ],
    "absolute_url": "/opinion/107716/bumper-v-north-carolina/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8969853,
        "score": 10,
        "case_name": "Bumper v. North Carolina"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "391 U.S. 543",
      "volume": "391",
      "reporter": "U.S.",
      "page": "543",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "88 S. Ct. 1788",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1788",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 797",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "797",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "46 Ohio Op. 2d 382",
        "volume": "46",
        "reporter": "Ohio Op. 2d",
        "page": "382",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1968 U.S. LEXIS 1470",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1470",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "391 U.S. 543",
        "volume": "391",
        "reporter": "U.S.",
        "page": "543",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 1788",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1788",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 797",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "797",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1968 U.S. LEXIS 1470",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1470",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "46 Ohio Op. 2d 382",
        "volume": "46",
        "reporter": "Ohio Op. 2d",
        "page": "382",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "391 U.S. 543",
    "official_selection": {
      "court_class": "scotus",
      "selected": "391 U.S. 543",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-548",
      "page": null,
      "quote": "and let them in. They found a rifle later admitted at trial to convict Bumper. At the suppression hearing the prosecution did not rely on \u2014 or even produce \u2014 any warrant; it sought to justify the search solely as consensual. ## Issue Whether a homeowner's permission to search, given after officers assert that they have a search warrant, constitutes valid voluntary consent under the Fourth Amendment when the warrant's validity is not established. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-550",
      "page": null,
      "quote": "When a law enforcement officer claims authority to search a home under a warrant, he announces in effect that the occupant has no right to resist the search. The situation is instinct with coercion \u2014 albeit colorably lawful coercion. Where there is coercion there cannot be consent.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1968-06-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Bumper v. North Carolina",
    "varies_by_point": false,
    "scope_note": "Foundational consent-voluntariness rule; good law and incorporated into the Schneckloth totality-of-circumstances framework.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "People v. Gutierrez",
          "cluster_id": 6240355,
          "cite": [
            "245 Cal. Rptr. 3d 143",
            "33 Cal. App. Supp. 5th 11"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Banks",
          "cluster_id": 6658146,
          "cite": [
            "434 P.3d 361",
            "364 Or. 332"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Buckley",
          "cluster_id": 4468007,
          "cite": [
            "90 N.E.3d 767",
            "478 Mass. 861"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane1_negative"
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
        "journal_ref": "Bumper v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Rush",
          "cluster_id": 3164356,
          "cite": [
            "808 F.3d 1007",
            "2015 U.S. App. LEXIS 22212",
            "2015 WL 9269763"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Casellas-Toro",
          "cluster_id": 3160467,
          "cite": [
            "807 F.3d 380",
            "2015 U.S. App. LEXIS 21199",
            "2015 WL 8044991"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Moises Donjuan v. State",
          "cluster_id": 2980860,
          "cite": [
            "461 S.W.3d 611",
            "2015 Tex. App. LEXIS 1618",
            "2015 WL 732640"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Camp",
          "cluster_id": 2774669,
          "cite": [
            "2015 Ohio 329"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane1_negative"
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
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
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
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
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
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
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
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
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
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carmouche v. State",
          "cluster_id": 1463452,
          "cite": [
            "10 S.W.3d 323",
            "2000 Tex. Crim. App. LEXIS 8",
            "2000 WL 60020"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lockhart v. McCree",
          "cluster_id": 111665,
          "cite": [
            "90 L. Ed. 2d 137",
            "106 S. Ct. 1758",
            "476 U.S. 162",
            "1986 U.S. LEXIS 153",
            "54 U.S.L.W. 4449"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Murphy",
          "cluster_id": 111105,
          "cite": [
            "79 L. Ed. 2d 409",
            "104 S. Ct. 1136",
            "465 U.S. 420",
            "1984 U.S. LEXIS 33",
            "52 U.S.L.W. 4246"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
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
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Kelly",
          "cluster_id": 1397401,
          "cite": [
            "204 S.W.3d 808",
            "2006 Tex. Crim. App. LEXIS 2060",
            "2006 WL 3019246"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. Mississippi",
          "cluster_id": 107912,
          "cite": [
            "22 L. Ed. 2d 676",
            "89 S. Ct. 1394",
            "394 U.S. 721",
            "1969 U.S. LEXIS 1869"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Andresen v. Maryland",
          "cluster_id": 109522,
          "cite": [
            "49 L. Ed. 2d 627",
            "96 S. Ct. 2737",
            "427 U.S. 463",
            "1976 U.S. LEXIS 78"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ledesma",
          "cluster_id": 1228080,
          "cite": [
            "729 P.2d 839",
            "43 Cal. 3d 171",
            "233 Cal. Rptr. 404",
            "1987 Cal. LEXIS 278"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
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
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Carter",
          "cluster_id": 118249,
          "cite": [
            "142 L. Ed. 2d 373",
            "119 S. Ct. 469",
            "525 U.S. 83",
            "1998 U.S. LEXIS 7844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
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
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. State",
          "cluster_id": 1577216,
          "cite": [
            "790 S.W.2d 568",
            "1989 Tex. Crim. App. LEXIS 151",
            "1989 WL 69709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Biswell",
          "cluster_id": 108533,
          "cite": [
            "32 L. Ed. 2d 87",
            "92 S. Ct. 1593",
            "406 U.S. 311",
            "1972 U.S. LEXIS 60"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Guloy",
          "cluster_id": 1116120,
          "cite": [
            "705 P.2d 1182",
            "104 Wash. 2d 412"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Phillips",
          "cluster_id": 8924874,
          "cite": [
            "664 F.2d 971",
            "9 Fed. R. Serv. 970"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dorsey v. State",
          "cluster_id": 2347482,
          "cite": [
            "350 A.2d 665",
            "276 Md. 638",
            "1976 Md. LEXIS 1109"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lo-Ji Sales, Inc. v. New York",
          "cluster_id": 110100,
          "cite": [
            "60 L. Ed. 2d 920",
            "99 S. Ct. 2319",
            "442 U.S. 319",
            "1979 U.S. LEXIS 107",
            "5 Media L. Rep. (BNA) 1177"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 1718150,
          "cite": [
            "803 S.W.2d 272",
            "1990 WL 180807"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Weaver",
          "cluster_id": 2633370,
          "cite": [
            "29 P.3d 103",
            "111 Cal. Rptr. 2d 2",
            "26 Cal. 4th 876",
            "2001 D.A.R. 8853",
            "2001 Daily Journal DAR 8853",
            "2001 Cal. Daily Op. Serv. 7228",
            "2001 Cal. LEXIS 5263"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mark Steven Phillips and Richard Elliott Grant, Jr., United States of America v. Robert Jay Meinster, A/K/A \"Robby\", Eugene Arter Myers, A/K/A \"Big Gene\", Richard Elliott Grant, Jr., Randall Gene Fisher, Modesto Echezarreta-Cruz, Robert Elliot Platshorn, A/K/A \"Roger Culpepper\"",
          "cluster_id": 397156,
          "cite": [
            "664 F.2d 971",
            "9 Fed. R. Serv. 970",
            "1981 U.S. App. LEXIS 14875"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bumper v. North Carolina:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107716 OR 9423732 OR 9423733 OR 9423734 OR 9423735) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDE0NTQwODAwMDAwJnM9MzEzMzMxNyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107716+OR+9423732+OR+9423733+OR+9423734+OR+9423735%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107716 OR 9423732 OR 9423733 OR 9423734 OR 9423735)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMDUmcz0zMTI3NzImdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107716+OR+9423732+OR+9423733+OR+9423734+OR+9423735%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107716 OR 9423732 OR 9423733 OR 9423734 OR 9423735)",
        "reviewed": 32,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 32,
        "triage_read": 0,
        "triage_snippet_classified": 32
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107716 OR 9423732 OR 9423733 OR 9423734 OR 9423735)",
    "indexed_citing_opinions": 2086,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107716,
        "count": 1901,
        "count_source": "search"
      },
      {
        "opinion_id": 9423732,
        "count": 259,
        "count_source": "search"
      },
      {
        "opinion_id": 9423733,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423734,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423735,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3107,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/bumper-v-north-carolina.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3NjE1ODgmcz05NDk1NjY2JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107716+OR+9423732+OR+9423733+OR+9423734+OR+9423735%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107716,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 105691,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 106259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 106963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 227607,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 233239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 268815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 269625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 1149975,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 1271914,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 1383993,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 1405835,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 1507641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 1543976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 1565757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 1723755,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 1868038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 1963425,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 3423906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107716,
        "cited_id": 3831607,
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
    "date_created": "2026-07-04T20:56:59Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:57:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:57:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T21:01:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:57:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Bumper v. North Carolina

```
<div>
<center><b><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">391 U.S. 543</a></span> (1968)</b></center>
<center><h1>BUMPER<br>
v.<br>
NORTH CAROLINA.</h1></center>
<center>No. 1016.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued April 24-25, 1968.</center>
<center>Decided June 3, 1968.</center>
CERTIORARI TO THE SUPREME COURT OF NORTH CAROLINA.
<p><i>Norman B. Smith</i> argued the cause and filed briefs for petitioner, <i>pro hac vice.</i></p>
<p><i>Harry W. McGalliard,</i> Deputy Attorney General of North Carolina, argued the cause for respondent. With him on the brief was <i>T. W. Bruton,</i> Attorney General.</p>
<p><span class="star-pagination">*544</span> Briefs of <i>amici curiae</i> were filed by <i>Jack Greenberg, James M. Nabrit III, Michael Meltsner, Leroy D. Clark, Norman C. Amaker,</i> and <i>Charles S. Ralston</i> for the NAACP Legal Defense and Educational Fund, Inc., et al., and by <i>F. Lee Bailey, pro se.</i></p>
<p>MR. JUSTICE STEWART delivered the opinion of the Court.</p>
<p>The petitioner was brought to trial in a North Carolina court upon a charge of rape, an offense punishable in that State by death unless the jury recommends life imprisonment.<sup>[1]</sup> Among the items of evidence introduced by the prosecution at the trial was a .22-caliber rifle allegedly used in the commission of the crime. The jury found the petitioner guilty, but recommended a sentence of life imprisonment.<sup>[2]</sup> The trial court imposed that sentence, and the Supreme Court of North Carolina affirmed the judgment.<sup>[3]</sup> We granted certiorari<sup>[4]</sup> to consider two separate constitutional claims pressed unsuccessfully by the petitioner throughout the litigation in the North Carolina courts. First, the petitioner argues that his constitutional right to an impartial jury was violated in this capital case when the prosecution was permitted to challenge for cause all prospective jurors who stated that they were opposed to capital punishment or had conscientious <span class="star-pagination">*545</span> scruples against imposing the death penalty. Secondly, the petitioner contends that the .22-caliber rifle introduced in evidence against him was obtained by the State in a search and seizure violative of the Fourth and Fourteenth Amendments.</p>
<p></p>
<h2>I.</h2>
<p>In <i>Witherspoon</i> v. <i>Illinois, ante,</i> p. 510, we have held that a death sentence cannot constitutionally be executed if imposed by a jury from which have been excluded for cause those who, without more, are opposed to capital punishment or have conscientious scruples against imposing the death penalty. Our decision in <i>Witherspoon</i> does not govern the present case, because here the jury recommended a sentence of life imprisonment. The petitioner argues, however, that a jury qualified under such standards must necessarily be biased as well with respect to a defendant's guilt, and that his conviction must accordingly be reversed because of the denial of his right under the Sixth and Fourteenth Amendments to trial by an impartial jury. <i>Duncan</i> v. <i>Louisiana, ante,</i> p. 145; <i>Turner</i> v. <i>Louisiana,</i> <span class="citation" data-id="9422932"><a href="/opinion/106963/turner-v-louisiana/#471" aria-description="Citation for case: Turner v. Louisiana">379 U. S. 466, 471-473</a></span>; <i>Irvin</i> v. <i>Dowd,</i> <span class="citation" data-id="9422231"><a href="/opinion/106259/irvin-v-dowd/#722" aria-description="Citation for case: Irvin v. Dowd">366 U. S. 717, 722-723</a></span>. We cannot accept that contention in the present case. The petitioner adduced no evidence to support the claim that a jury selected as this one was is necessarily "prosecution prone,"<sup>[5]</sup> and the materials referred to in his brief are no more substantial than those brought to our attention in <i>Witherspoon.</i><sup>[6]</sup> Accordingly, we decline to reverse the judgment of conviction upon this basis.</p>
<p></p>
<h2>
<span class="star-pagination">*546</span> II.</h2>
<p>The petitioner lived with his grandmother, Mrs. Hattie Leath, a 66-year-old Negro widow, in a house located in a rural area at the end of an isolated mile-long dirt road. Two days after the alleged offense but prior to the petitioner's arrest, four white law enforcement officers the county sheriff, two of his deputies, and a state investigatorwent to this house and found Mrs. Leath there with some young children. She met the officers at the front door. One of them announced, "I have a search warrant to search your house." Mrs. Leath responded, "Go ahead," and opened the door. In the kitchen the officers found the rifle that was later introduced in evidence at the petitioner's trial after a motion to suppress had been denied.</p>
<p>At the hearing on this motion, the prosecutor informed the court that he did not rely upon a warrant to justify the search, but upon the consent of Mrs. Leath.<sup>[7]</sup> She testified at the hearing, stating, among other things:</p>
<blockquote>"Four of them came. I was busy about my work, and they walked into the house and one of them walked up and said, `I have a search warrant to search your house,' and I walked out and told them to come on in. . . . He just come on in and said he had a warrant to search the house, and he didn't <span class="star-pagination">*547</span> read it to me or nothing. So, I just told him to come on in and go ahead and search, and I went on about my work. I wasn't concerned what he was about. I was just satisfied. He just told me he had a search warrant, but he didn't read it to me. He did tell me he had a search warrant.</blockquote>
<blockquote>.....</blockquote>
<blockquote>". . . He said he was the law and had a search warrant to search the house, why I thought he could go ahead. I believed he had a search warrant. I took him at his word. . . . I just seen them out there in the yard. They got through the door when I opened it. At that time, I did not know my grandson had been charged with crime. Nobody told me anything. They didn't tell me anything, just picked it up like that. They didn't tell me nothing about my grandson."<sup>[8]</sup></blockquote>
<p>Upon the basis of Mrs. Leath's testimony, the trial court found that she had given her consent to the search, and <span class="star-pagination">*548</span> denied the motion to suppress.<sup>[9]</sup> The Supreme Court of North Carolina approved the admission of the evidence on the same basis.<sup>[10]</sup></p>
<p>The issue thus presented is whether a search can be justified as lawful on the basis of consent when that "consent" has been given only after the official conducting the search has asserted that he possesses a warrant.<sup>[11]</sup> We hold that there can be no consent under such circumstances.</p>
<p>When a prosecutor seeks to rely upon consent to justify the lawfulness of a search, he has the burden of proving that the consent was, in fact, freely and voluntarily given.<sup>[12]</sup> This burden cannot be discharged by <span class="star-pagination">*549</span> showing no more than acquiescence to a claim of lawful authority.<sup>[13]</sup> A search conducted in reliance upon a warrant cannot later be justified on the basis of consent if it turns out that the warrant was invalid.<sup>[14]</sup> The result can be no different when it turns out that the State does not even attempt to rely upon the validity of the warrant, <span class="star-pagination">*550</span> or fails to show that there was, in fact, any warrant at all.<sup>[15]</sup></p>
<p>When a law enforcement officer claims authority to search a home under a warrant, he announces in effect that the occupant has no right to resist the search. The situation is instinct with coercionalbeit colorably lawful coercion. Where there is coercion there cannot be consent.</p>
<p>We hold that Mrs. Leath did not consent to the search, and that it was constitutional error to admit the rifle in evidence against the petitioner. <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>. Because the rifle was plainly damaging evidence against the petitioner with respect to all three of the charges against him, its admission at the trial was not harmless error. <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span>.<sup>[16]</sup></p>
<p><span class="star-pagination">*551</span> The judgment of the Supreme Court of North Carolina is, accordingly, reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE DOUGLAS joins Part II of the opinion of the Court. Since, however, the record shows that 16 of 53 prospective jurors were excused for cause because of their opposition to capital punishment, he would also reverse on the ground that petitioner was denied the right to trial on the issue of guilt by a jury representing a fair cross-section of the community. <i>Witherspoon</i> v. <i>Illinois, ante,</i> at 523 (separate opinion). Under North Carolina law, rape is punishable by death unless the jury recommends life imprisonment. N. C. Gen. Stat. § 14-21 (1953). But an indictment for rape includes the lesser offense of an assault with intent to commit rape, and the court has the duty to submit to the jury the lesser degrees of the offense of rape which are supported by the evidence. <i>State</i> v. <i>Green,</i> <span class="citation" data-id="1271914"><a href="/opinion/1271914/state-v-green/" aria-description="Citation for case: State v. Green">246 N. C. 717</a></span>, <span class="citation" data-id="1271914"><a href="/opinion/1271914/state-v-green/" aria-description="Citation for case: State v. Green">100 S. E. 2d 52</a></span> (1957). See N. C. Gen. Stat. §§ 15-169, 15-170 (1953). These include assault with intent to commit rape, for which the range of punishment is one to 15 years' imprisonment (N. C. Gen. Stat. § 14-22), and assault (N. C. Gen. Stat. § 14-33). In the instant case, the trial judge did in fact charge the jury with respect to these lesser offenses.</p>
<p>MR. JUSTICE HARLAN, concurring.</p>
<p>While I join in the judgment of the Court and in Part II of its opinion, I am prompted to add a brief note.</p>
<p><span class="star-pagination">*552</span> I share, as I am sure every member of the majority does, MR. JUSTICE BLACK'S abhorrence of the brutal crime of which petitioner stands convicted. To avoid any misapprehension, I wish to make it perfectly clear that reversal of this conviction is not a "penalty" imposed on the State for infringement of federal constitutional rights. Reversal by this Court results, as always, only from a decision that petitioner was not constitutionally proved guilty and hence there is no legally valid basis for imposition of a penalty upon him.</p>
<p>In determining whether a criminal defendant was convicted "according to law," the test is not and cannot be simply whether this Court finds credible the evidence against him. Crediting or discrediting evidence is the function of the trier of fact, in this case a jury. The jury's verdict is a lawful verdict, however, only if it is based upon evidence constitutionally admissible. When it is not, as it is not here, reversal rests on the oldest and most fundamental principle of our criminal jurisprudence that a defendant is entitled to put the prosecution to its lawful proof.</p>
<p>The evidence against petitioner consisted in part of a gun that he alleged was unlawfully taken from the home of Mrs. Leath, where petitioner was living. The State contended that Mrs. Leath had consented to the search of her home. However, this "consent" was obtained immediately after a sheriff told Mrs. Leath that he had a search warrant, that is, that he had a lawful right to enter her home with or without consent. Nothing Mrs. Leath said in response to that announcement can be taken to mean that she considered the officers welcome in her home with or without a warrant. What she would have done if the sheriff had not said he had a warrant is, on this record, a hypothetical question about an imaginary situation that Mrs. Leath never faced.</p>
<p><span class="star-pagination">*553</span> Of course, if the officers had a valid search warrant, no consent was required to make the search lawful. There was a search warrant in this case, and it remains possible that this warrant was issued under circumstances meeting all the requirements of the Federal Constitution. Consequently, if this were a situation where a state court had simply chosen the wrong line of constitutional analysis of this search, I would vote to remand the case to give the prosecution an opportunity to justify the search on proper grounds. However, as noted by the Court, the prosecution here explicitly and repeatedly renounced any reliance on the warrant. Like all other parties to lawsuits, a prosecutor has an obligation to the courts (including this Court) and to other parties to present its claims at the earliest appropriate time, and to create an adequate record. Cf. <i>Ciucci</i> v. <i>Illinois,</i> <span class="citation" data-id="9421619"><a href="/opinion/105691/ciucci-v-illinois/#573" aria-description="Citation for case: Ciucci v. Illinois">356 U. S. 571, 573</a></span> (separate note of Mr. Justice Frankfurter and MR. JUSTICE HARLAN).</p>
<p>Finally, if I were persuaded that the admission of the gun was "harmless error," I would vote to affirm, and if I were persuaded that it was arguably harmless error, I would vote to remand the case for state consideration of the point. But the question cannot be whether, in the view of this Court, the defendant actually committed the crimes charged, so that the error was "harmless" in the sense that petitioner got what he deserved. The question is whether the error was such that it cannot be said that petitioner's guilt was adjudicated on the basis of constitutionally admissible evidence, which means, in this case, whether the properly admissible evidence was such that the improper admission of the gun could not have affected the result.</p>
<p>I do not think this can be said here. The critical question was the identity of the perpetrator of these crimes. The State introduced eyewitness identification of petitioner by his two victims, and a gun with which there <span class="star-pagination">*554</span> was evidence these victims were shot, together with testimony that it had been found in petitioner's place of abode. The jury could, of course, have found the testimony of the victims credible beyond a reasonable doubt, and convicted petitioner on this basis alone. But it might well not have. The addition of a tangible cross-check linking petitioner with the crime can hardly be said, from the judicial vantage point, to have been harmless surplusage.</p>
<p>MR. JUSTICE BLACK, dissenting.</p>
<p></p>
<h2>I.</h2>
<p>This case, like <i>Witherspoon</i> v. <i>Illinois, ante,</i> p. 510, decided today, was brought to this Court primarily to decide the question whether the constitutional rights of a criminal defendant are violated when prospective jurors who state they are opposed to capital punishment or who have conscientious scruples against imposing the death penalty are excluded for cause. As the Court in <i>Witherspoon</i> limited its holding to the question of punishment and not of guilt,<sup>[1]</sup> the jury issue became moot in this case since petitioner had been sentenced to life imprisonment. Ironically, however, this case now becomes about as good an example as can be found of the fallacious assumption of the holding in <i>Witherspoon.</i> For the <i>Witherspoon</i> decision rests on the premise that a jury "[c]ulled of all who harbor doubts about the wisdom of capital punishment" is somehow prosecution-prone, callous or even lacking in "charity."<sup>[2]</sup> Yet the jury in this case, from which had been excluded all persons who stated they were opposed to the death penalty, unanimously recommended life imprisonment in a case where, but for their recommendation, the death sentence would <span class="star-pagination">*555</span> have been automatic.<sup>[3]</sup> And this is a case where the evidence conclusively showed that the accused twice raped a young woman at gunpoint, shot both the woman and her companion while they were tied helplessly to trees with the announced intention of killing them, and left them for dead. Even with these horrible facts before it, this so-called "prosecution-prone," "callous," and "uncharitable" jury refused to allow imposition of the death penalty and recommended life imprisonment instead. In these circumstances, where the real reason for granting certiorari in the case has disappeared, it seems to me that the Court should dismiss the petition as improvidently granted. This is especially true here, where, as I point out at the end of this opinion, there is an open-and-shut case of guilt, and the petitioner received the lightest sentence available under state law.</p>
<p></p>
<h2>II.</h2>
<p>Passing over the jury issue, the Court still reverses the conviction in this case and sends it back for a new trial on the ground that the rifle, which the record shows was used to shoot the victims, and which is held by the majority to have been obtained through an unconstitutional search and seizure, was admitted into evidence at petitioner's trial. One of the reasons that I cannot agree with the Court's reversal is because I believe the searching officers had valid permission to conduct their search. The facts surrounding the search are these: Petitioner had been raised by his grandmother, Mrs. Hattie Leath, with whom he was living at the time the rape and assaults were committed. Shortly after the victims were able to recount to the police what had happened to them, the county sheriff, with two of his deputies and a state police officer, went to Mrs. Leath's <span class="star-pagination">*556</span> house. One of the deputies went up on the porch of the house and stated to Mrs. Leath, who was standing inside the screen door, that he had a warrant to search her house. He did not appear to have any paper in his hand, and he did not read anything to her. Mrs. Leath's <i>immediate</i> response, without mentioning anything about a warrant or asking to see it or read it or have it read to her, was to tell the deputy "to come on in." At the trial Mrs. Leath described her reaction to the visit of the law officers as follows:</p>
<blockquote>"He did tell me he had a search warrant. I don't know if Sheriff Stockard was with him. I was not paying much attention. I told Mr. Stockard [after he had come up on the porch] to go ahead and look all over the house. I had no objection to them making a search of my house. I was willing to let them look in any room or drawer in my house they wanted to. Nobody threatened me with anything. Nobody told me they were going to hurt me if I didn't let them search my house. Nobody told me they would give me any money if I would let them search. I let them search, and <i>it was all my own free will.</i> Nobody forced me at all." (Emphasis added.)</blockquote>
<p>My study of the record in this case convinces me that Mrs. Leath voluntarily consented to this search,<sup>[4]</sup> and in fact that she actually wanted the officers to search her houseto prove to them that she had nothing to hide. Mrs. Leath's readiness to permit the search was the action of a person so conscious of her innocence, so proud of her own home,<sup>[5]</sup> that she was not going to require <span class="star-pagination">*557</span> a search warrant, thus indicating a doubt about the rectitude of her household. There are such people in this world of ours,<sup>[6]</sup> and the evidence in this case causes me to believe Mrs. Leath is one of them. As she herself testified, "I just give them a free will to look because I felt like the boy wasn't guilty."</p>
<p>Despite the statements of Mrs. Leath cited above, and despite the clear finding of consent by the trial judge, who personally saw and heard Mrs. Leath testify,<sup>[7]</sup> this Court, refusing to accept Mrs. Leath's sworn testimony that she did freely consent and overruling the trial judge's findings, concludes on its own that she did not consent. I do not believe the Court should substitute what it believes Mrs. Leath should have said for what she actually said"it was all my own free will." I cannot accept what I believe to be an unwarranted conclusion by the Court.</p>
<p></p>
<h2>III.</h2>
<p>Even assuming for the purposes of argument that there was no consent to search and that the rifle which was <span class="star-pagination">*558</span> seized from Mrs. Leath's house should not have been admitted into evidence, I still believe the conviction should stand. For the overwhelming evidence in this case, even when the rifle and related testimony are excluded, amply demonstrates petitioner's guilt. Unfortunately, to show this, it is necessary to go into the sordid facts of the case. The victims were a young man and his girl friend. At trial both testified in detail to the following: They were parked shortly after dusk on a country road not far from where the petitioner Bumper lived. Bumper approached the car, stuck a rifle barrel up to the window and ordered the girl to get out of the car, indicating that if she refused he would shoot her. Both got out of the car and Bumper ordered the girl to undress, stating that "I want a white girl's p______." When the girl adamantly refused, Bumper pointed the rifle at the young man, and the girl, understanding that she must submit or her boy friend would be killed, followed Bumper's orders. Bumper then forced the young man into the rear seat of the car, requiring him to stay down on the floor, while Bumper raped the girl on the back of the car. A short time after this, Bumper forced the couple to drive to another spot. Here he made them get out of the car and walk down a dirt road into some bushes. At this time Bumper told the couple he was going to kill them, and when they pleaded with him to let them go, he replied, "I can't do it; you will go to the cops." The couple then suggested that if Bumper would tie them up and blindfold them that he could get away with no problem. This Bumper did, tying each to a separate tree. But he did not leave. Instead he raped the girl again while she was tied to the tree. After this, Bumper went over to the young man and felt his chest, asking him where his heart was and if he was scared. He then cooly proceeded to shoot the young man where he thought his heart was. The girl, tied to the tree and <span class="star-pagination">*559</span> blindfolded, heard the shot, and a moment later herself was shot through the left breast close to her heart. Bumper then took the car and drove away, obviously believing he had killed the young couple. They were able to free themselves, however, and with much difficulty made their way to a nearby house where the owner got them to a hospital.<sup>[8]</sup> The time during which the couple was held captive was approximately an hour and a half. During that time they clearly got to know who their assailant was. Both got a plain view of Bumper right at the beginning of their ordeal when they opened the car doors and saw his face in the light coming from the inside of the car. Moreover, the undisputed evidence in the record shows that the night of the attack was a bright moonlit night. Both testified positively at trial that it was Bumper.<sup>[9]</sup> Also there was substantial corroborating evidence outside of that relating to the rifle. Here we have the clear and convincing testimony of the two victims, whose characters were in no way impeached or challenged. The only witnesses at the trial were state <span class="star-pagination">*560</span> witnesses (the two victims plus medical and police testimony), and none of their testimony was refuted or denied in any way. Thus, this is a case where every word of evidence introduced at trial pointed to guilt, and there was no challenge to the truthfulness of the State's evidence, nor to the character of any of its witnesses. Yet even with all this, the Court persists in reversing the case, thus requiring the State to hold a new trial if it wishes to punish Bumper for his crimes.</p>
<p>When it is clear beyond all shadow of a doubt, as here, that a defendant committed the crimes charged, I do not believe that this Court should enforce on the States a <i>"per se"</i> rule automatically requiring a new trial in every case where this Court concludes that some part of the evidence was obtained by an unreasonable search and seizure. The primary reason the "exclusionary rule" was adopted by this Court was to deter unreasonable searches and seizures in violation of the Fourth Amendment. <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>. But see my concurring opinion at 661-666. I believe that the deterrence desired by some can be served adequately without blind adherence to a mechanical formula that requires automatic reversal in every case where the exclusionary rule is violated. While little is known about the effect the exclusionary rule really has on actual police practices, I think it is a fair assumption that refusal to reverse a conviction of a defendant, because of the admission of illegally seized evidence, where other evidence conclusively demonstrates his guilt, is not going to lessen police sensitivity to the exclusionary rule, thereby reducing its deterrent effect. Obviously at the time a search is carried out the police are not going to know whether the evidence they hope to obtain is going to be necessary for the prosecution's case, and, of course, if they know it will not be necessary, no search is needed. Thus the only effect of not automatically reversing all cases in which there <span class="star-pagination">*561</span> has been a violation of the exclusionary rule will be to allow state convictions of obviously guilty defendants to stand. And they should stand.</p>
<p></p>
<h2>IV.</h2>
<p>In this case, as I have shown, the evidence of the two victims points positively to guilt without any doubt. When there is added to this the fact that the rifle, from which came the bullets which went into the bodies of the two victims, was found where Bumper lived, which was not far from the scene of the assault, this makes, as the North Carolina Supreme Court pointed out, assurance doubly sure. Whether one views the evidence of guilt with or without the rifle, the conclusion is inescapable that this defendant committed the crimes for which the jury convicted him. In these circumstances no State should be forced to give a new trial; justice does not require it.<sup>[10]</sup></p>
<p>MR. JUSTICE WHITE, dissenting.</p>
<p>When "consent" to a search is given after the occupant has been told by police officers that they have a warrant for the search, it seems reasonable to me for Fourth Amendment purposes to view the consent as conditioned on there being a valid warrant, absent clear proof that the consent was actually unconditional. The evidence in this record does not show unconditional consent with sufficient clarity, and perhaps this would be the result in most cases. But this does not mean that <span class="star-pagination">*562</span> every search following conditional consent is invalid. If upon a motion to suppress or upon an objection to evidence offered at the trial, the State produces a valid warrant for the search, there is no good reason to exclude the evidence simply because police at the time of the search relied on the consent and neither served nor returned the warrant. In the case before us the State represented in this Court that there was a warrant for the challenged search. Unlike the Court and MR. JUSTICE HARLAN, I would not brush this matter aside. Since the existence and validity of the warrant have not been determined in the state courts, the case is not ripe for reversal or affirmance. I would therefore not reverse, but vacate, this conviction, returning the case to the state courts for a determination of the validity of the warrant. If because of the absence of probable cause, or for some other reason, the warrant would not have been a proper predicate for the search, <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), would require reversal of the conviction unless it is saved under the harmless-error rule of <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967).<sup>[*]</sup></p>
<h2>NOTES</h2>
<p>[1]  "Every person who is convicted of ravishing and carnally knowing any female of the age of twelve years or more by force and against her will, or who is convicted of unlawfully and carnally knowing and abusing any female child under the age of twelve years, shall suffer death: Provided, if the jury shall so recommend at the time of rendering its verdict in open court, the punishment shall be imprisonment for life in the State's prison, and the court shall so instruct the jury." N. C. Gen. Stat. § 14-21 (1953).</p>
<p>[2]  The petitioner was also convicted upon two charges of felonious assault and sentenced to consecutive 10-year prison terms.</p>
<p>[3]  <span class="citation" data-id="1383993"><a href="/opinion/1383993/state-v-bumpers/" aria-description="Citation for case: State v. Bumpers">270 N. C. 521</a></span>, <span class="citation" data-id="1383993"><a href="/opinion/1383993/state-v-bumpers/" aria-description="Citation for case: State v. Bumpers">155 S. E. 2d 173</a></span>.</p>
<p>[4]  <span class="citation multiple-matches"><a href="/c/U.%20S./389/1034/">389 U. S. 1034</a></span>.</p>
<p>[5]  He did submit affidavits to the North Carolina Supreme Court referring to studies by W. C. Wilson and F. J. Goldberg, see <i>Witherspoon</i> v. <i>Illinois, ante,</i> at 517, n. 10. The court made no findings with respect to those studies and did not mention them in its opinion.</p>
<p>[6]  In addition to the materials mentioned in <i>Witherspoon, ante,</i> at 517, n. 10, the petitioner's brief in this Court cites an unpublished dissertation by R. Crosson, An Investigation Into Certain Personality Variables Among Capital Trial Jurors (Western Reserve University, January 1966), involving a sample of 72 jurors in Ohio.</p>
<p>[7]  "THE COURT: There is a motion here that says the property [was] seized against the will of Mrs. Hattie Leath and without a search warrant. Now, the question is, are we going into the search warrant?
</p>
<p>"MR. COOPER: The State is not relying on the search warrant.</p>
<p>"THE COURT: Are you stating so for the record?</p>
<p>"MR. COOPER: Yes, sir."</p>
<p>[8]  She also testified, at another point:
</p>
<p>"I had no objection to them making a search of my house. I was willing to let them look in any room or drawer in my house they wanted to. Nobody threatened me with anything. Nobody told me they were going to hurt me if I didn't let them search my house. Nobody told me they would give me any money if I would let them search. I let them search, and it was all my own free will. Nobody forced me at all.</p>
<p>.....</p>
<p>"I just give them a free will to look because I felt like the boy wasn't guilty."</p>
<p>The transcript of the suppression hearing comes to us from North Carolina in the form of a narrative; <i>i. e.,</i> the actual questions and answers have been rewritten in the form of continuous first person testimony. The effect is to put into the mouth of the witness some of the words of the attorneys. In the case of an obviously compliant witness like Mrs. Leath, the result is a narrative that has the tone of decisiveness but is shot through with contradictions.</p>
<p>[9]  "The Court finds that from the evidence of Mrs. Hattie Leath that it is of a clear and convincing nature that she, the said Mrs. Hattie Leath, voluntarily consented to the search of her premises, as is more particularly set forth in her evidence, and that that consent was specifically given and is not the result of coercion from the officers."</p>
<p>[10]  That court also stated: "The fact that [the search] did reveal the presence of the guilty weapon . . . justifies the search. . . . [The petitioner's] rights have not been violated. Rather, his wrongs have been detected." <span class="citation" data-id="1383993"><a href="/opinion/1383993/state-v-bumpers/#530" aria-description="Citation for case: State v. Bumpers">270 N. C., at 530-531</a></span>, <span class="citation" data-id="1383993"><a href="/opinion/1383993/state-v-bumpers/#180" aria-description="Citation for case: State v. Bumpers">155 S. E. 2d, at 180</a></span>.
</p>
<p>Any idea that a search can be justified by what it turns up was long ago rejected in our constitutional jurisprudence. "A search prosecuted in violation of the Constitution is not made lawful by what it brings to light . . . ." <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#29" aria-description="Citation for case: Byars v. United States">273 U. S. 28, 29</a></span>. See also <i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#595" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 595</a></span>; <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#103" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 103</a></span>.</p>
<p>[11]  Mrs. Leath owned both the house and the rifle. The petitioner concedes that her voluntary consent to the search would have been binding upon him. Conversely, there can be no question of the petitioner's standing to challenge the lawfulness of the search. He was the "one against whom the search was directed," <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#261" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 261</a></span>, and the house searched was his home. The rifle was used by all members of the household and was found in the common part of the house.</p>
<p>[12]  <i>Wren</i> v. <i>United States,</i> <span class="citation" data-id="269625"><a href="/opinion/269625/james-wren-v-united-states/" aria-description="Citation for case: James Wren v. United States">352 F. 2d 617</a></span>; <i>Simmons</i> v. <i>Bomar,</i> <span class="citation" data-id="268815"><a href="/opinion/268815/kenneth-b-simmons-v-lynn-bomar-warden-tennessee-state-penitentiary/" aria-description="Citation for case: Kenneth B. Simmons v. Lynn Bomar, Warden, Tennessee State...">349 F. 2d 365</a></span>; <i>Judd</i> v. <i>United States,</i> 89 U. S. App. D. C. 64, <span class="citation" data-id="227607"><a href="/opinion/227607/judd-v-united-states/" aria-description="Citation for case: Judd v. United States">190 F. 2d 649</a></span>; <i>Kovach</i> v. <i>United States,</i> <span class="citation" data-id="1543976"><a href="/opinion/1543976/kovach-v-united-states/" aria-description="Citation for case: Kovach v. United States">53 F. 2d 639</a></span>.</p>
<p>[13]  See, <i>e. g., </i><i>Amos</i> v. <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/#317" aria-description="Citation for case: Amos v. United States">255 U. S. 313, 317</a></span>; <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13</a></span>; <i>Higgins</i> v. <i>United States,</i> 93 U. S. App. D. C. 340, <span class="citation" data-id="233239"><a href="/opinion/233239/higgins-v-united-states/" aria-description="Citation for case: Higgins v. United States">209 F. 2d 819</a></span>; <i>United States</i> v. <i>Marra,</i> <span class="citation" data-id="1565757"><a href="/opinion/1565757/united-states-v-marra/" aria-description="Citation for case: United States v. Marra">40 F. 2d 271</a></span>; <i>MacKenzie</i> v. <i>Robbins,</i> <span class="citation" data-id="1405835"><a href="/opinion/1405835/mackenzie-v-robbins/" aria-description="Citation for case: MacKenzie v. Robbins">248 F. Supp. 496</a></span>.</p>
<p>[14]  "Orderly submission to law-enforcement officers who, in effect, represented to the defendant that they had the authority to enter and search the house, against his will if necessary, was not such consent as constituted an understanding, intentional and voluntary waiver by the defendant of his fundamental rights under the Fourth Amendment to the Constitution." <i>United States</i> v. <i>Elliott,</i> <span class="citation" data-id="1963425"><a href="/opinion/1963425/united-states-v-elliott/#360" aria-description="Citation for case: United States v. Elliott">210 F. Supp. 357, 360</a></span>.
</p>
<p>"One is not held to have consented to the search of his premises where it is accomplished pursuant to an apparently valid search warrant. On the contrary, the legal effect is that consent is on the basis of such a warrant and his permission is construed as an intention to abide by the law and not resist the search under the warrant, rather than an invitation to search." <i>Bull</i> v. <i>Armstrong,</i> <span class="citation" data-id="1149975"><a href="/opinion/1149975/bull-v-armstrong/#394" aria-description="Citation for case: Bull v. Armstrong">254 Ala. 390, 394</a></span>, <span class="citation" data-id="1149975"><a href="/opinion/1149975/bull-v-armstrong/#470" aria-description="Citation for case: Bull v. Armstrong">48 So. 2d 467, 470</a></span>.</p>
<p>"One who, upon the command of an officer authorized to enter and search and seize by search warrant, opens the door to the officer and acquiesces in obedience to such a request, no matter by what language used in such acquiescence, is but showing a regard for the supremacy of the law. . . . The presentation of a search warrant to those in charge at the place to be searched, by one authorized to serve it, is tinged with coercion, and submission thereto cannot be considered an invitation that would waive the constitutional right against unreasonable searches and seizures, but rather is to be considered a submission to the law." <i>Meno</i> v. <i>State,</i> <span class="citation" data-id="3423906"><a href="/opinion/3426817/meno-v-state/#24" aria-description="Citation for case: Meno v. State">197 Ind. 16, 24</a></span>, <span class="citation" data-id="3423906"><a href="/opinion/3426817/meno-v-state/#96" aria-description="Citation for case: Meno v. State">164 N. E. 93, 96</a></span>.</p>
<p>See also <i>Salata</i> v. <i>United States,</i> <span class="citation" data-id="8828815"><a href="/opinion/8843598/salata-v-united-states/" aria-description="Citation for case: Salata v. United States">286 F. 125</a></span>; <i>Brown</i> v. <i>State,</i> <span class="citation" data-id="1723755"><a href="/opinion/1723755/brown-v-state/" aria-description="Citation for case: Brown v. State">42 Ala. App. 429</a></span>, <span class="citation" data-id="1723755"><a href="/opinion/1723755/brown-v-state/" aria-description="Citation for case: Brown v. State">167 So. 2d 281</a></span>; <i>Mattingly</i> v. <i>Commonwealth,</i> <span class="citation" data-id="7148029"><a href="/opinion/7235610/mattingly-v-commonwealth/" aria-description="Citation for case: Mattingly v. Commonwealth">199 Ky. 30</a></span>, <span class="citation" data-id="7148029"><a href="/opinion/7235610/mattingly-v-commonwealth/" aria-description="Citation for case: Mattingly v. Commonwealth">250 S. W. 105</a></span>. Cf. <i>Gibson</i> v. <i>United States,</i> 80 U. S. App. D. C. 81, <span class="citation" data-id="1507641"><a href="/opinion/1507641/gibson-v-united-states/" aria-description="Citation for case: Gibson v. United States">149 F. 2d 381</a></span>; <i>Naples</i> v. <i>Maxwell,</i> <span class="citation" data-id="1868038"><a href="/opinion/1868038/naples-v-maxwell/" aria-description="Citation for case: Naples v. Maxwell">271 F. Supp. 850</a></span>; <i>Atwood</i> v. <i>State,</i> <span class="citation" data-id="3831607"><a href="/opinion/4073599/atwood-v-state/" aria-description="Citation for case: Atwood v. State">44 Okla. Cr. 206</a></span>, <span class="citation" data-id="3831607"><a href="/opinion/4073599/atwood-v-state/" aria-description="Citation for case: Atwood v. State">280 P. 319</a></span>; <i>State</i> v. <i>Watson,</i> <span class="citation" data-id="7994759"><a href="/opinion/8038360/state-v-watson/" aria-description="Citation for case: State v. Watson">133 Miss. 796</a></span>, <span class="citation" data-id="7994759"><a href="/opinion/8038360/state-v-watson/" aria-description="Citation for case: State v. Watson">98 So. 241</a></span>.</p>
<p>[15]  During the course of the argument in this case we were advised that the searching officers did, in fact, have a warrant. But no warrant was ever returned, and there is no way of knowing the conditions under which it was issued, or determining whether it was based upon probable cause.</p>
<p>[16]  It is suggested in dissent that "[e]ven assuming . . . that there was no consent to search and that the rifle . . . should not have been admitted into evidence, . . . the conviction should stand." This suggestion seems to rest on the "horrible" facts of the case, and the assumption that the petitioner was guilty. But it is not the function of this Court to determine innocence or guilt, much less to apply our own subjective notions of justice. Our duty is to uphold the Constitution of the United States.
</p>
<p>In view of the discursive factual recital contained in the dissenting opinion, however, an additional word may be in order. There can be no doubt that the crimes were grave and shocking. There <i>can</i> be doubt that the petitioner was their perpetrator. The crimes were committed at night. When, at first, the victims separately viewed a lineup that included the petitioner, each of the victims identified the same man as their assailant. That man was <i>not</i> the petitioner. Later, the victims together viewed another lineup, and every man in the lineup was made to speak <i>his name</i> for "voice identification." This time the victims identified the petitioner as their assailant. At the time of the lineups a local newspaper had reported that a man named Wayne Bumper was being held by the sheriff as the "prime suspect" in the case, and at least one of the victims knew of that fact. Earlier both victims had been shown a collection of photographs. One victim identified a picture of the petitioner; the petitioner's name was written on the back of the photograph.</p>
<p>[1]  See <i>ante,</i> at 522, n. 21.</p>
<p>[2]  See <i>ante,</i> at 520, n. 17.</p>
<p>[3]  See N. C. Gen. Stat. § 14-21. The Court imposed additional sentences of 10 years' imprisonment, to run consecutively, on the two felonious assault charges.</p>
<p>[4]  Mrs. Leath's voluntary consent was sufficient to validate the search since she owned the house which was searched and the rifle that was taken. It should also be noted that the rifle was not found in petitioner's private room, nor in any part of the house assigned to him, but in the kitchen behind the door.</p>
<p>[5]  Mrs. Leath owned the house in which she was living and throughout her questioning repeatedly referred to "my house."</p>
<p>[6]  See <i>Commonwealth</i> v. <i>Tucker,</i> <span class="citation" data-id="6429130"><a href="/opinion/6555383/commonwealth-v-tucker/#469" aria-description="Citation for case: Commonwealth v. Tucker">189 Mass. 457, 469</a></span>, <span class="citation" data-id="6429130"><a href="/opinion/6555383/commonwealth-v-tucker/#131" aria-description="Citation for case: Commonwealth v. Tucker">76 N. E. 127, 131</a></span>. In this case a mother consented for officers who were looking for broken pieces of a knife used in a murder to search her home. The Court found that officers went "to the door of the house where Tucker resided, and stated to his mother, at the outside door of the house, that they had this search warrant to search for the article named therein . . . that she . . . invited the officers to make all the search they desired, saying that she knew her son to be innocent; and thereupon the officers made search, not upon the warrant, but in consequence of her invitation . . . ." The knife blade was admitted against the contention that it was barred by the Fourth and Fourteenth Amendments.</p>
<p>[7]  The finding of the court was as follows: "The Court finds that from the evidence of Mrs. Hattie Leath that it is of a clear and convincing nature that she, the said Mrs. Hattie Leath, voluntarily consented to the search of her premises, as is more particularly set forth in her evidence, and that that consent was specifically given and is not the result of coercion form the officers."</p>
<p>[8]  It was on these facts and this testimony, it must be remembered, that this jury, selected in the way <i>Witherspoon</i> holds is designed to produce a "hanging" jury, recommended a life sentence for petitioner.</p>
<p>[9]  The Court's opinion attempts to convey the impression that the victims were not sure of their assailant's identification because of an alleged mistake during a police lineup. See majority opinion, n. 16. This completely overlooks the fact, however, that before Bumper was arrested, and before the victims had any idea of their attacker's name or where he was from, the girl, while still in the hospital, identified Bumper's picture from a number of others. The young man also had identified Bumper's picture days before the lineup was held. After the girl went through the lineup the first time she confessed that she was too scared to look at the men and that she had made no real attempt at identification. And it should not be forgotten that she testified positively under oath at trial that "In my own mind I am certain [that Bumper was my assailant], and nothing could really dissuade me from it. I haven't made up my mind; I know."</p>
<p>[10]  <span class="citation no-link">28 U. S. C. § 2106</span> provides: "The Supreme Court or any other court of appellate jurisdiction may affirm, modify, vacate, set aside or reverse any judgment, decree, or order of a court lawfully brought before it for review, and may remand the cause and direct the entry of such appropriate judgment, decree, or order, or require such further proceedings to be had <i>as may be just under the circumstances.</i>" (Emphasis added.)</p>
<p>[*]  Of course, if it was determined that the grandmother's consent was not good against petitioner, who had standing to raise the validity of the search, it would be unnecessary to deal with the issues which have been argued and determined in this case.</p>

</div>
```

---

## GROUP: content/cases/Burdeau v. McDowell.md  (`case`, 5 assertions)

### content_page

```
---
title: Burdeau v. McDowell
type: case
citation: "256 U.S. 465 (1921)"
parallel_cite: "41 S. Ct. 574; 65 L. Ed. 1048; 13 A.L.R. 1159"
neutral_cite: 1921 U.S. LEXIS 1576
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1921
date_decided: 1921-06-01
docket: ""
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
  opinion_url: "https://www.courtlistener.com/opinion/99820/burdeau-v-mcdowell/"
  cluster_id: 99820
  opinion_id: null
  identity_checked: true
lake:
  record_id: Burdeau v. McDowell
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Private and Foreign Searches]]"
    role: Anchor
related:
  - "[[Private and Foreign Searches]]"
  - "[[United States v. Jacobsen]]"
tags:
  - case
  - fourth-amendment
  - private-search-doctrine
  - state-action
  - governmental-action
holding: "The Fourth Amendment restrains only governmental action; where private parties, without any participation by the government, wrongfully seize a person's private papers and later turn them over to federal prosecutors, there is no Fourth Amendment violation and the government may retain and use the papers."
aliases:
  - Burdeau v. McDowell
  - "Burdeau v. McDowell (1921)"
---

# Burdeau v. McDowell

*256 U.S. 465 (1921)* · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 99820 → majority opinion 99820 (Day, J.; 256 U.S. 465, decided 1921). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*475`); the quote begins at "Its origin and history…" to avoid an OCR typo ("giyes") in the preceding clause of the CL text. S9 promotes. -->

## Background
Officers of a company that had discharged J.C. McDowell for fraud broke into his office, drilled open his private safes, and took his personal books and papers. Some months later — after communicating with the Department of Justice — the company turned certain of those papers over to a federal official, who intended to present them to a grand jury investigating McDowell for mail fraud. No federal agent took part in, or knew of, the seizure until well after it occurred. McDowell petitioned for the return of the papers, invoking the Fourth and Fifth Amendments. The District Court ordered them returned; the government appealed.

## Issue
Whether the Fourth Amendment bars the government from retaining and using a person's private papers that were wrongfully taken by private parties, without any governmental involvement, and later delivered to prosecutors.

## Rule
The Fourth Amendment's protection runs against the sovereign, not against private wrongdoing. As the Court explained: "Its origin and history clearly show that it was intended as a restraint upon the activities of sovereign authority, and was not intended to be a limitation upon other than governmental agencies". — 256 U.S. at 475. ^pin-475

## Application
The record showed that no official of the federal government had anything to do with the theft of McDowell's papers, or any knowledge of it, until months afterward, when the property was already in the company's hands. Because the wrong "was the act of individuals," there was no governmental search or seizure to which the Fourth Amendment could attach; the Amendment simply did not reach the private taking. The government was therefore free to retain the papers and use them before the grand jury, leaving McDowell to whatever civil remedies he had against those who took them.

## Conclusion
The order requiring return of the papers was **reversed**. Day, J., delivered the opinion of the Court; Brandeis, J. (joined by Holmes, J.), dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Burdeau* is the foundational statement of the **private-search doctrine**: the Fourth Amendment reaches only state action, so evidence produced by a genuinely private search is admissible. Modern doctrine builds on it — most importantly *[[United States v. Jacobsen]]* (a later government inspection is measured against, and limited to, the scope of the antecedent private search). The rule turns on the *absence* of government participation or instigation; when officials direct or join the search, the Amendment applies.

## Appears on
- [[Private and Foreign Searches]] — *Anchor*

## Sources
- [*Burdeau v. McDowell*, 256 U.S. 465 (1921)](https://www.courtlistener.com/opinion/99820/burdeau-v-mcdowell/) — pinpoint: 475 (Day, J., for the Court; the CL opinion text carries the reporter star `*475` immediately before the quoted paragraph). Rule quote string-matched to the CL opinion text 2026-07-07 (quote taken from "Its origin and history…" to avoid an OCR artifact — "giyes" for "gives" — in the sentence's opening clause).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c4ff20c3e1d35bc2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "256 U.S. 465 (1921)", "court": "U.S. Supreme Court", "neutral_cite": "1921 U.S. LEXIS 1576", "official_citation_present": true, "parallel_cite": "41 S. Ct. 574; 65 L. Ed. 1048; 13 A.L.R. 1159", "title": "Burdeau v. McDowell", "year": "1921"}}
{"assertion_id": "73f3f1c155ffd255", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Fourth Amendment restrains only governmental action; where private parties, without any participation by the government, wrongfully seize a person's private papers and later turn them over to federal prosecutors, there is no Fourth Amendment violation and the government may retain and use the papers.", "title": "Burdeau v. McDowell"}}
{"assertion_id": "8f6d7bfa6afd0b3b", "dimension": "support", "kind": "home_role", "locator": {"home": "Private and Foreign Searches"}, "payload": {"home": "Private and Foreign Searches", "role": "Anchor", "title": "Burdeau v. McDowell"}}
{"assertion_id": "83407c978168462d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Burdeau v. McDowell"}}
{"assertion_id": "fff972670ad40441", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Burdeau v. McDowell", "varies_by_point": "false"}}
```

### lake record — Burdeau v. McDowell

```json
{
  "schema_version": "s2.v1",
  "record_id": "Burdeau v. McDowell",
  "status": "under_review",
  "identity": {
    "case_name": "Burdeau v. McDowell",
    "case_name_short": "Burdeau",
    "case_name_full": "BURDEAU v. McDOWELL",
    "input_case_name": "Burdeau v. McDowell",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1921-06-01",
    "year": 1921,
    "docket": null,
    "cluster_id": 99820,
    "lead_opinion_id": 99820,
    "sibling_ids": [],
    "absolute_url": "/opinion/99820/burdeau-v-mcdowell/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "256 U.S. 465",
      "volume": "256",
      "reporter": "U.S.",
      "page": "465",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "41 S. Ct. 574",
        "volume": "41",
        "reporter": "S. Ct.",
        "page": "574",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 1048",
        "volume": "65",
        "reporter": "L. Ed.",
        "page": "1048",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "13 A.L.R. 1159",
        "volume": "13",
        "reporter": "A.L.R.",
        "page": "1159",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1921 U.S. LEXIS 1576",
        "volume": "1921",
        "reporter": "U.S. LEXIS",
        "page": "1576",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "256 U.S. 465",
        "volume": "256",
        "reporter": "U.S.",
        "page": "465",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "41 S. Ct. 574",
        "volume": "41",
        "reporter": "S. Ct.",
        "page": "574",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 1048",
        "volume": "65",
        "reporter": "L. Ed.",
        "page": "1048",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1921 U.S. LEXIS 1576",
        "volume": "1921",
        "reporter": "U.S. LEXIS",
        "page": "1576",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "13 A.L.R. 1159",
        "volume": "13",
        "reporter": "A.L.R.",
        "page": "1159",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "256 U.S. 465",
    "official_selection": {
      "court_class": "scotus",
      "selected": "256 U.S. 465",
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
    "date_created": "2026-07-06T13:10:19Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:10:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:10:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:10:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:10:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "burdeau-v-mcdowell--99820",
      "to_record_id": "Burdeau v. McDowell",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Burdeau v. McDowell

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b518-5">
  Mr. Justice Day
 </author>
<p id="ADX">
  delivered the opinion of the court.
 </p>
<p id="b518-6">
  J. C. McDowell, hereinafter called the petitioner, filed a petition in the United States District Court for the Western District of Pennsylvania asking for an order for ohe return to him of certain books', papers, memoranda, correspondence and other data in the possession of Joseph A. Burdeau, appellant herein, Special Assistant to the Attorney General of the United States.
 </p>
<p id="b518-7">
  In the petition it is stated that Burdeau and his associates intended to present to the grand jury in and for the Western District of Pennsylvania a charge against petitioner of an alleged violation of § 215 of the Criminal Code of the United States in the fraudulent use of the mails; that it was the intention of Burdeau and his associates, including certain post-office inspectors cooperating with him, to present to the grand jury certain private books, papers, memoranda, etc., which were the private property of the petitioner; that the papers had been in the possession and exclusive control of the petitioner in the Farmers Bank Building in Pittsburgh. It is alleged that during the spring and summer of 1920 these papers were unlawfully seized and stolen from petitioner by certain persons participating in and furthering the proposed investigation so to be made by the grand jury, under the direction and control of Burdeau as special assistant to the Attorney General, and that such books, papers, memoranda, etc., were being held in the possession and control of Burdeau and his assistants; that in the taking of the personal private books and papers the person who purloined and stole the same drilled the petitioner’s private safes, broke the locks upon his private
  <span citation-index="1" class="star-pagination" label="471"> 
   *471
   </span>
  desk, and broke into and abstracted from the files in his offices his private papers; that the possession of the books, papers, etc., by Burdeau and his assistants was unlawful and in violation of the legal and constitutional rights of the petitioner. It is charged that the presentation to the grand jury of the same, or any secondary or other evidence secured through or by them, would work a deprivation of petitioner’s constitutional rights secured to him by the Fourth and Fifth Amendments to the Constitution of the United States.
 </p>
<p id="b519-4">
  An answer was filed claiming the right to hold and use the papers. A hearing was had before the District Judge, who made an order requiring the delivery of the papers to the clerk of the court, together with all copies memoranda and data taken therefrom, which the court found had been stolen from the offices of the petitioner at rooms numbered 1320 and 1321 in the Farmers Bank Building in the . City of Pittsburgh. The order further provided that upon delivery of the books, papers, etc., to the clerk of the court the same should be sealed and impounded for the period of ten days, at the end of which period they should be delivered to the petitioner or his attorney unless an appeal were taken from the order of the court, in which event, the books, papers, etc., should be impounded until the determination of the appeal. An order was made restraining Burdeau, Special Assistant Attorney General, the Department of Justice, its officers and agents, and the United States Attorney from presenting to the United States Commissioner, the grand jury or any judicial tribunal, any of the books, papers, memoranda, letters, copies of letters, correspondence, etc., or any evidence of any nature whatsoever secured by or coming into their possession as a result of tíie knowledge obtained, from the inspection of such books, papers, memoranda, etc.
 </p>
<p id="b519-5">
  In his opinion the District Judge stated that it was the
  <span citation-index="1" class="star-pagination" label="472"> 
   *472
   </span>
  intention of the Department of Justice, through Burdeau and his assistants, to present the books, papers, etc., to the grand-jury with a view to having the petitioner indicted for the alleged violation of § 215 of the Criminal Code of the United .States, and the court held that the evidence offered by the petitioner showed that the papers had been stolen from him, and that he was entitled to the return of the same. In this connection the District Judge stated that it did not appear that Burdeau, or any official or agent of the United States, or any of the'Departments, had anything to do with the search of the petitioner’s safe, files and desk, or the abstraction therefrom of any of the writings referred to in the petition, and added that “the order made in this case is not made because of any unlawful act on the part of anybody representing the United States or any of its Departments but solely upon the ground that the Government should not use stolen property for any purpose after demand made for its return.” Expressing his views,,at the close of the testimony, the Judge said that' there • had been a gross violation of the Fourth and Fifth Amendments to the Federal Constitution; that the Government had not been a party to any illegal seizure; that those Amendments, in the understanding of the court, were passed for the benefit of the States against action, by the United States, forbidden by those Amendments, and that the court was satisfied that the papers were illegally and wrongfully taken from the possession of the petitioner, and were then in the hands of the Government.
 </p>
<p id="b520-5">
  So far as is necessary for our .consideration certain facts from the record may be stated. Henry L. Doherty. &amp; Company of New York were operating managers of the Cities Service Company, which company is a holding company, having control of various oil and gas companies.. Petitioner was a director in the Cities Service Company
  <span citation-index="1" class="star-pagination" label="473"> 
   *473
   </span>
  and. a director in the Quapaw Gas Company, a subsidiary company, and occupied an office room in the building owned by the Farmers Bank of Pittsburgh. The rooms were leased by the Quapaw Gas Company. McDowell occupied one room for his private office. He was employed by Doherty &amp; Company as the head of the natural gas division of the 'Cities Service Company. Doherty &amp; Company discharged McDowell for alleged unlawful and. fraudulent conduct in the course of the business. An officer of Doherty &amp; Company and the Cities Service Company went to-Pittsburgh in March, 1920, with authority .of the president of the Quapaw Gas Company to take possession of the company’s office. He took possession of room 1320; that room and the adjoining ’ room had McDowell’s name on the door. At various times papers were taken from the safe and desk in the rooms, and the rooms were placed in charge of detectives. 'A large quantity of papers were taken and shipped to the auditor of the Cities Service Company at 60 Wall Street, New York, which was the office of that company,. Doherty &amp; Company and the Quapaw Gas Company. The secretary of McDowell testified that room 1320 was his private office; that practically all the furniture in both rooms belonged to him; that there was a large safe belonging to the Farmers Bank and a small safe belonging to McDowell; that on March 23, 1920, a representative of the company and a detective came to the offices; that the detective was placed in charge of room 1320; that the large safe was opened with a view to selecting papers belonging to the company, and that the representative- of the/éompany took private papers of McDowell’s also! While the rooms were in charge of detectives both safes were blown open. - In the small safe nothing of consequence was found, but in the large safe papers belonging to McDowell were found. The desk was forced open, and all'the papers taken from.it.
  <span citation-index="1" class="star-pagination" label="474"> 
   *474
   </span>
  The papers were placed in cases, and shipped to Doherty &amp; Company, 60 Wall Street, New York.
 </p>
<p id="b522-5">
  In June, 1920, followiiig, Doherty &amp; Company, after communication with, the Department of Justice, turned over a letter, found in "McDowell’s desk,
  <em>
   tg
  </em>
  the Department’s representative. Burdeau admitted at the hearing that as the representative of the United States in the Department of Justice he had papers which he assumed were taken from the office of McDowell., The communication to the Attorney General stated that McDowell had violated the laws of the United States in the use of the mail in the transmission of various letters to partieswho owned the properties which were sold by or offered to the Cities Service Company; that some of such letters, or copies of them taken from McDowell’s file, were in the possession , of the Cities Service Company, that the Company also had in its possession portions of a diary of McDowell in which he had jotted down the commissions which he had received from a number of the transactions, and other data which, it is stated, would be useful in the investigation of the matter before the grand jury and subsequent prosecution should an indictment be returned.
 </p>
<p id="b522-6">
  We do not question the authority of the court to control the disposition of tlje papers, and come directly to the contention that the constitutional rights , of the petitioner were violated by their seizure, and that having subsequently come into the possession of the prosecuting officers of. the. Government, he was entitled to their return. The Amendments involved are the Fourth and Fifth, protecting a citizen against unreasonable searches and seizures, and compulsory testimony against himself. An extended consideration of the origin and purposes of these Amendments would be superfluous in view of the fact that this court has had occasion to deal with those subjects in. a series of cases.
  <em>
   Boyd
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>;
  <em>
   Adams v.
  </em>
  New York, <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U. S. 585</a></span>;
  <em>
   Weeks
  </em>
  v.
  <span citation-index="1" class="star-pagination" label="475"> 
   *475
   </span>
<em>
   United States,
  </em>
  <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>;
  <em>
   Johnson
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="97862"><a href="/opinion/97862/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">228 U. S. 457</a></span>;
  <em>
   Perlman
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99162"><a href="/opinion/99162/perlman-v-united-states/" aria-description="Citation for case: Perlman v. United States">247 U. S. 7</a></span>;
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>; and
  <em>
   Gouled
  </em>
  v.
  <em>
   United States, 255
  </em>
  U. S. 298.
 </p>
<p id="b523-5">
  The Fourth Amendment giyes protection against unlawful searches and seizures, and as shown in the previous cases, its protection applies to governmental action. Its origin and history clearly show that it was intended as a restraint upon the activities of sovereign authority, and was not intended to be a limitation upon other than governmental agencies; as against such authority it was the purpose of the Fourth Amendment to secure the citizen in the right of unmolested occupation of his dwelling and the possession of his property, subject to the right of seizure by process duly issued.
 </p>
<p id="b523-6">
  In the present case the record clearly shows' that no official of the Federal Government had anything to do with the wrongful seizure of the petitioner’s property, or any knowledge thereof until several months after the property had been taken from him and was in the possession of the Cities Service Company. It is manifest that there was no invasion of the security afforded by the Fourth Amendment against unreasonable search and seizure, as whatever wrong was done was the act of individuals in taking the property of another. A portion of the property so taken and held was tinned over to the prosecuting officers of the Federal Government. We assume that petitioner has an unquestionable right of redress against those'who illegally and wrongfully took his private property' under the circumstances herein disclosed, but with such remedies we are not now concerned.
 </p>
<p id="b523-7">
  The Fifth Amendment, as its terms import is intended to secure the citizen from compulsory testimony against himself. If protects from extorted confessions, or examinations in court proceedings by compulsory methods.
 </p>
<p id="b523-8">
  The exact question to be decided here is: May the
  <span citation-index="1" class="star-pagination" label="476"> 
   *476
   </span>
  Government retain incriminating papers, coming to it in the manner described; with a view to their use in a subsequent investigation by a grand jury where such papers will be part of the evidence, against the accused, and may be used against him upon trial should an indictment' be returned?
 </p>
<p id="b524-5">
  We know of no constitutional principle which requires the Government to surrender the papers under such circumstances. Had it learned that such incriminatory .papers,- tending to show a violation of federal law, were in the hands of a person other than the accused, it having had no part in wrongfully obtaining them, we know of no reason why a subpoena might not issue for the. production of the papers as evidence. Such production wduld require no- unreasonable search or seizure,' nor would, it amount to compelling the accused to testify against himself.
 </p>
<p id="b524-6">
  The papers having come into the possession of the Government without a violation of petitioner’s rights by governmental , authority, we see no reason why the fact that, individuals., unconnected with the Government,, may have wrongfully taken them,^should prevent them from being held .for use in prosecuting an offense where the documents aré of an incriminatory character.
 </p>
<p id="b524-7">
  It follows that the District Court erred in making the order appealed from, and the same is
 </p>
<p id="b524-8">
<em>
   Reversed.
  </em>
</p>
<judges id="b524-9">
  Mr. Justice Brandéis dissenting, with whom Mr. Justice Holmes concurs.
 </judges>
<p id="b524-10">
  Plaintiff’s private papers were stolen. The thief, to further his own ends, delivered them to the law officer of the United States. He, knowing them to have been stolen, retains, them for use against the plaintiff. Should the court permit him to do so?
 </p>
<p id="AdNu">
<span citation-index="1" class="star-pagination" label="477"> 
   *477
   </span>
  That the court would restore the papers to plaintiff if they were still in the thief’s possession is not questioned. That it has power to control the disposition óf these stolen papers, although they have passed into the possession of the law officer, is also not questioned. But it is said that no provision of the Constitution requires their surrender and that the papers could have been subpoenaed. This may be true.. Still I cannot' believe that action of a publie official is necessarily lawful, because it does not violate constitutional prohibitions and because the same result might have been attained by other and proper means. At the foundation of our civil liberty lies the principle which denies to government officials an exceptional position before the law and which subjects them to the same rules of conduct that are commands to the citizen. And in the development of our liberty insistence upon procedural regularity has been a large factor. Respect for law. will not be advanced by resort, in its enforcement, to means which shock the common man’s sense of decency and fair play.
 </p>
</opinion>
```

---
