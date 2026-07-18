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

## GROUP: content/cases/United States v. Watson.md  (`case`, 6 assertions)

### content_page

```
---
title: "United States v. Watson"
type: case
citation: "423 U.S. 411 (1976)"
parallel_cite: "96 S. Ct. 820; 46 L. Ed. 2d 598"
neutral_cite: 1976 U.S. LEXIS 121
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-01-26
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-01-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Watson
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109352/united-states-v-watson/"
  cluster_id: 109352
  opinion_id: 109352
  identity_checked: true
homes:
  - page: "[[Arrest and Arrest Warrants]]"
    role: "Key — Anchor (warrantless public arrest on probable cause)"
  - page: "[[Consent Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Schneckloth v. Bustamonte]]", "[[United States v. Drayton]]", "[[United States v. Mendenhall]]", "[[United States v. Santana]]"]
aliases: []
tags: ["case", "fourth-amendment", "consent-search", "voluntariness", "custody", "warrantless-arrest"]
holding: "Custody alone does not render consent involuntary. The fact of being under arrest / in custody is ONE factor in the…"
lake:
  record_id: United States v. Watson
  status: verified
  projected_at: 2026-07-10
---

# United States v. Watson

*423 U.S. 411 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Acting on a reliable informant's tip — corroborated when the informant showed the inspector stolen credit cards Watson had supplied — a postal inspector arrested Watson without a warrant in a restaurant. After the arrest and *[[Miranda v. Arizona|Miranda]]* warnings, the inspector asked to search Watson's nearby car; Watson said "Go ahead," and stolen credit cards were found inside. Watson moved to suppress. The Ninth Circuit held the warrantless arrest invalid and the consent therefore tainted.

## Issue
Whether Watson's consent to search, given after a custodial arrest, was voluntary — and whether the fact of being in custody renders consent involuntary.

## Rule
First, the warrantless arrest was lawful — a warrantless felony arrest in public on probable cause does not violate the Fourth Amendment — so the consent was not the product of an illegal arrest. Second, consent given in custody is judged by the *[[Schneckloth v. Bustamonte|Schneckloth]]* [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], and custody alone does not make it involuntary: "He had been arrested and was in custody, but his consent was given while on a public street, not in the confines of the police station. Moreover, the fact of custody alone has never been enough in itself to demonstrate a coerced confession or consent to search." — 423 U.S. at 424. ^pin-424

Nor is the suspect's ignorance of the right to refuse controlling — the absence of such proof "may be a factor in the overall judgment," but "is not to be given controlling significance." — [*Id.*](https://www.courtlistener.com/opinion/109352/united-states-v-watson/#:~:text=may%20be%20a%20factor%20in) ^pin-424a

## Application
Because Watson's arrest was valid, his consent was not tainted by any illegality. There was no overt act or threat of force, no promises, and no subtle coercion; Watson consented on a public street rather than at the station house. That he was under arrest, and any lack of proof that he knew he could refuse, did not by themselves overbear his will. Under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] his consent was his own free choice, and the stolen credit cards found in the car were admissible.

## Conclusion
The warrantless public arrest was lawful and Watson's consent to the search was voluntary; the Supreme Court reversed the Court of Appeals.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Watson* applies the [[Schneckloth v. Bustamonte]] totality-of-the-circumstances voluntariness test to a custodial setting: being under arrest is one factor, not a disqualifier, and the suspect need not be told he may refuse. *Watson*'s separate holding — that a warrantless felony arrest in public on probable cause is reasonable — also remains good law and informs [[United States v. Santana]].

## Appears on
- [[Arrest and Arrest Warrants]] — *Key — Anchor*
- [[Consent Searches]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Watson*, 423 U.S. 411 (1976) — https://www.courtlistener.com/opinion/109352/united-states-v-watson/ — pinpoint: 424 (parallel 96 S. Ct. 820).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "907e7dd077b47313", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "423 U.S. 411 (1976)", "court": "U.S. Supreme Court", "neutral_cite": "1976 U.S. LEXIS 121", "official_citation_present": true, "parallel_cite": "96 S. Ct. 820; 46 L. Ed. 2d 598", "title": "United States v. Watson", "year": "1976"}}
{"assertion_id": "02f20c7ccdb3759d", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Custody alone does not render consent involuntary. The fact of being under arrest / in custody is ONE factor in the…", "title": "United States v. Watson"}}
{"assertion_id": "914a5f4344b74902", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest and Arrest Warrants"}, "payload": {"home": "Arrest and Arrest Warrants", "role": "Key — Anchor (warrantless public arrest on probable cause)", "title": "United States v. Watson"}}
{"assertion_id": "de36ea0463485cc2", "dimension": "support", "kind": "home_role", "locator": {"home": "Consent Searches"}, "payload": {"home": "Consent Searches", "role": "Key — Progeny / Refinement", "title": "United States v. Watson"}}
{"assertion_id": "7deef6a183ab92e5", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Watson"}}
{"assertion_id": "a393a9c21c894ccd", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1976-01-26", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Watson", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Watson", "varies_by_point": "false"}}
```

### lake record — United States v. Watson

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Watson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Watson",
    "case_name_short": "Watson",
    "case_name_full": "United States v. Watson",
    "input_case_name": "United States v. Watson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-01-26",
    "year": 1976,
    "docket": null,
    "cluster_id": 109352,
    "lead_opinion_id": 109352,
    "sibling_ids": [
      109352,
      9426247,
      9426248,
      9426249,
      9426250
    ],
    "absolute_url": "/opinion/109352/united-states-v-watson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "423 U.S. 411",
      "volume": "423",
      "reporter": "U.S.",
      "page": "411",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 820",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "820",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "46 L. Ed. 2d 598",
        "volume": "46",
        "reporter": "L. Ed. 2d",
        "page": "598",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 121",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "121",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "423 U.S. 411",
        "volume": "423",
        "reporter": "U.S.",
        "page": "411",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 820",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "820",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "46 L. Ed. 2d 598",
        "volume": "46",
        "reporter": "L. Ed. 2d",
        "page": "598",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 121",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "121",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "423 U.S. 411",
    "official_selection": {
      "court_class": "scotus",
      "selected": "423 U.S. 411",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-424",
      "page": null,
      "quote": "and stolen credit cards were found inside. Watson moved to suppress. The Ninth Circuit held the warrantless arrest invalid and the consent therefore tainted. ## Issue Whether Watson's consent to search, given after a custodial arrest, was voluntary \u2014 and whether the fact of being in custody renders consent involuntary. ## Rule First, the warrantless arrest was lawful \u2014 a warrantless felony arrest in public on probable cause does not violate the Fourth Amendment \u2014 so the consent was not the product of an illegal arrest. Second, consent given in custody is judged by the *Schneckloth* totality of the circumstances, and custody alone does not make it involuntary:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-424a",
      "page": null,
      "quote": "may be a factor in the overall judgment,",
      "star_marker": "424",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 23606,
      "fragment": "#:~:text=may%20be%20a%20factor%20in",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-01-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Watson",
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
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jenkins",
          "cluster_id": 2444991,
          "cite": [
            "3 A.3d 806",
            "298 Conn. 209",
            "2010 Conn. LEXIS 304"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bartlett v. State",
          "cluster_id": 1449101,
          "cite": [
            "249 S.W.3d 658",
            "2008 WL 480174"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Bickel, 2006-Coa-034 (7-10-2007)",
          "cluster_id": 3949285,
          "cite": [
            "2007 Ohio 3517"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Winston",
          "cluster_id": 202176,
          "cite": [
            "444 F.3d 115",
            "2006 U.S. App. LEXIS 10038",
            "2006 WL 1044180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Keith Forbes",
          "cluster_id": 764880,
          "cite": [
            "181 F.3d 1",
            "1999 WL 315796"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Sandoval v. State",
          "cluster_id": 1575995,
          "cite": [
            "35 S.W.3d 763",
            "2000 WL 1863674"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Atwater v. City of Lago Vista",
          "cluster_id": 7076046,
          "cite": [
            "165 F.3d 380",
            "1999 U.S. App. LEXIS 1639",
            "1999 WL 13050"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. La Fontaine",
          "cluster_id": 6144105,
          "cite": [
            "235 A.D.2d 93",
            "664 N.Y.S.2d 587",
            "1997 N.Y. App. Div. LEXIS 11046"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Glia",
          "cluster_id": 6134935,
          "cite": [
            "226 A.D.2d 66",
            "651 N.Y.S.2d 967",
            "1996 N.Y. App. Div. LEXIS 12576"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Mourning",
          "cluster_id": 8913620,
          "cite": [
            "716 F. Supp. 279",
            "1989 U.S. Dist. LEXIS 7281",
            "1989 WL 71233"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Leal v. State",
          "cluster_id": 5244283,
          "cite": [
            "736 S.W.2d 903"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane1_negative"
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
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. United States",
          "cluster_id": 1732,
          "cite": [
            "176 L. Ed. 2d 1",
            "130 S. Ct. 1265",
            "559 U.S. 133",
            "2010 U.S. LEXIS 2201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
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
        "journal_ref": "United States v. Watson:lane2_top_cited"
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
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ramey",
          "cluster_id": 1185860,
          "cite": [
            "545 P.2d 1333",
            "16 Cal. 3d 263",
            "127 Cal. Rptr. 629",
            "1976 Cal. LEXIS 220"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gonzalez",
          "cluster_id": 5681980,
          "cite": [
            "39 N.Y.2d 122",
            "347 N.E.2d 575",
            "383 N.Y.S.2d 215",
            "1976 N.Y. LEXIS 2389"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patrick Bell, Sr., Etc. v. City of Milwaukee, Howard Johnson and Edwin Shaffer, Patrick Bell, Sr., Etc. v. Thomas Grady, Jr., Patrick Bell, Sr., Etc. v. City of Milwaukee",
          "cluster_id": 443256,
          "cite": [
            "746 F.2d 1205",
            "16 Fed. R. Serv. 279",
            "1984 U.S. App. LEXIS 18950"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. James",
          "cluster_id": 1433510,
          "cite": [
            "561 P.2d 1135",
            "19 Cal. 3d 99",
            "137 Cal. Rptr. 447"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ervine",
          "cluster_id": 2527109,
          "cite": [
            "47 Cal. 4th 745",
            "220 P.3d 820",
            "102 Cal. Rptr. 3d 786",
            "2009 Cal. LEXIS 12406"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
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
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hulit v. State",
          "cluster_id": 2452885,
          "cite": [
            "982 S.W.2d 431",
            "1998 Tex. Crim. App. LEXIS 174",
            "1998 WL 870923"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jackie David Miller",
          "cluster_id": 362441,
          "cite": [
            "589 F.2d 1117",
            "3 Fed. R. Serv. 1418",
            "1978 U.S. App. LEXIS 7704"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Saundra Prescott",
          "cluster_id": 358848,
          "cite": [
            "581 F.2d 1343",
            "1978 U.S. App. LEXIS 9041"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Monterroso",
          "cluster_id": 2507854,
          "cite": [
            "101 P.3d 956",
            "22 Cal. Rptr. 3d 1",
            "34 Cal. 4th 743",
            "2004 Daily Journal DAR 14707",
            "2004 Cal. Daily Op. Serv. 10899",
            "2004 Cal. LEXIS 11763"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Orlando Vasquez, Carlos Sanchez, Fernando Eugenio Medina, Amparo Valencia Medina, Clara Inez Mesa and Hernando Mesa",
          "cluster_id": 386016,
          "cite": [
            "638 F.2d 507",
            "1980 U.S. App. LEXIS 11022"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Walker",
          "cluster_id": 2005731,
          "cite": [
            "350 N.E.2d 678",
            "370 Mass. 548",
            "1976 Mass. LEXIS 1011"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Juarez v. State",
          "cluster_id": 1562920,
          "cite": [
            "758 S.W.2d 772",
            "1988 Tex. Crim. App. LEXIS 172",
            "1988 WL 98938"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nancy Reed and Morris Goldsmith, A/K/A \"Marlowe,\"",
          "cluster_id": 354014,
          "cite": [
            "572 F.2d 412",
            "3 Fed. R. Serv. 155",
            "1978 U.S. App. LEXIS 11727"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arcila v. State",
          "cluster_id": 1495036,
          "cite": [
            "834 S.W.2d 357",
            "1992 Tex. Crim. App. LEXIS 160",
            "1992 WL 139308"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bacigalupo",
          "cluster_id": 1386250,
          "cite": [
            "820 P.2d 559",
            "1 Cal. 4th 103",
            "2 Cal. Rptr. 2d 335",
            "91 Daily Journal DAR 15109",
            "1991 Cal. LEXIS 5500"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Reginald Glover",
          "cluster_id": 578612,
          "cite": [
            "957 F.2d 1004",
            "1992 U.S. App. LEXIS 2799",
            "1992 WL 29046"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Deunte L. Humphries",
          "cluster_id": 786633,
          "cite": [
            "372 F.3d 653",
            "2004 U.S. App. LEXIS 11898",
            "2004 WL 1351562"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dyar v. State",
          "cluster_id": 1384792,
          "cite": [
            "125 S.W.3d 460",
            "2003 Tex. Crim. App. LEXIS 74",
            "2003 WL 1917729"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Richard Wiener",
          "cluster_id": 334863,
          "cite": [
            "534 F.2d 15",
            "1976 U.S. App. LEXIS 12212"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Avalos",
          "cluster_id": 2269454,
          "cite": [
            "47 Cal. App. 4th 1569",
            "55 Cal. Rptr. 2d 450",
            "96 Cal. Daily Op. Serv. 5718",
            "96 Daily Journal DAR 9266",
            "1996 Cal. App. LEXIS 740"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Watson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109352 OR 9426247 OR 9426248 OR 9426249 OR 9426250) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NTcxMDcyMDAwMDAmcz0xNjIxMTI5JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109352+OR+9426247+OR+9426248+OR+9426249+OR+9426250%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 12,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 12,
        "triage_snippet_classified": 188
      },
      "lane2_top_cited": {
        "query": "cites:(109352 OR 9426247 OR 9426248 OR 9426249 OR 9426250)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDYmcz0zODkyNTAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109352+OR+9426247+OR+9426248+OR+9426249+OR+9426250%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109352 OR 9426247 OR 9426248 OR 9426249 OR 9426250)",
        "reviewed": 30,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 30,
        "triage_read": 0,
        "triage_snippet_classified": 30
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109352 OR 9426247 OR 9426248 OR 9426249 OR 9426250)",
    "indexed_citing_opinions": 508,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109352,
        "count": 191,
        "count_source": "search"
      },
      {
        "opinion_id": 9426247,
        "count": 329,
        "count_source": "search"
      },
      {
        "opinion_id": 9426248,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426249,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426250,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2263,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-watson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwMDg3NyZzPTEwMTI3OTAzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109352+OR+9426247+OR+9426248+OR+9426249+OR+9426250%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109352,
        "cited_id": 84759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 84827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 91385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 91470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 95265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 101970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 106850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 108135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 108605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 108713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 108714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 226125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 227607,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 227881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 241496,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 260271,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 262538,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 267195,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 267556,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 269642,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 271327,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 273438,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 275790,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 277223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 278957,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 286516,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 291586,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 293653,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 299839,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 305071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 305803,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 305873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 306113,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 322384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 1606693,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 1939307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 1978640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 2114928,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 2292926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 2304502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 2614205,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 3238539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 5513252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109352,
        "cited_id": 5554010,
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
    "date_created": "2026-07-06T03:32:02Z",
    "date_modified": "2026-07-10T00:12:42Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:32:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:32:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:39:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:32:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Watson (truncated)

```
<div>
<center><b><span class="citation no-link">423 U.S. 411</span> (1976)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
WATSON.</h1></center>
<center>No. 74-538.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 8, 1975.</center>
<center>Decided January 26, 1976.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><span class="star-pagination">*412</span> <i>Deputy Solicitor General Frey</i> argued the cause for the United States. With him on the briefs were <i>Solicitor General Bork, Acting Assistant Attorney General Keeney,</i> and <i>Peter M. Shannon, Jr.</i></p>
<p><i>Michael D. Nasatir,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./421/997/">421 U. S. 997</a></span>. argued the cause for respondent. With him on the brief was <i>Donald M. Re.</i></p>
<p>MR. JUSTICE WHITE delivered the opinion of the Court.</p>
<p>This case presents questions under the Fourth Amendment as to the legality of a warrantless arrest and of an ensuing search of the arrestee's automobile carried out with his purported consent.</p>
<p></p>
<h2>I</h2>
<p>The relevant events began on August 17, 1972, when an informant, one Khoury, telephoned a postal inspector informing him that respondent Watson was in possession of a stolen credit card and had asked Khoury to cooperate in using the card to their mutual advantage. On five to 10 previous occasions Khoury had provided the inspector with reliable information on postal inspection matters, some involving Watson. Later that day <span class="star-pagination">*413</span> Khoury delivered the card to the inspector. On learning that Watson had agreed to furnish additional cards, the inspector asked Khoury to arrange to meet with Watson. Khoury did so, a meeting being scheduled for August 22.<sup>[1]</sup> Watson canceled that engagement, but at noon on August 23, Khoury met with Watson at a restaurant designated by the latter. Khoury had been instructed that if Watson had additional stolen credit cards, Khoury was to give a designated signal. The signal was given, the officers closed in, and Watson was forthwith arrested. He was removed from the restaurant to the street where he was given the warnings required by <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). A search having revealed that Watson had no credit cards on his person, the inspector asked if he could look inside Watson's car, which was standing within view. Watson said, "Go ahead," and repeated these words when the inspector cautioned that "[i]f I find anything, it is going to go against you." Using keys furnished by Watson, the inspector entered the car and found under the floor mat an envelope containing two credit cards in the names of other persons. These cards were the basis for two counts of a four-count indictment charging Watson with possessing stolen mail in violation of <span class="citation no-link">18 U. S. C. § 1708</span>.<sup>[2]</sup></p>
<p>Prior to trial, Watson moved to suppress the cards, claiming that his arrest was illegal for want of probable cause and an arrest warrant and that his consent to search the car was involuntary and ineffective because he had not been told that he could withhold consent. <span class="star-pagination">*414</span> The motion was denied, and Watson was convicted of illegally possessing the two cards seized from his car.<sup>[3]</sup></p>
<p>A divided panel of the Court of Appeals for the Ninth Circuit reversed, <span class="citation" data-id="9461128"><a href="/opinion/322384/united-states-v-henry-ogle-watson/" aria-description="Citation for case: United States v. Henry Ogle Watson">504 F. 2d 849</a></span> (1974), ruling that the admission in evidence of the two credit cards found in the car was prohibited by the Fourth Amendment. In reaching this judgment, the court decided two issues in Watson's favor. First, notwithstanding its agreement with the District Court that Khoury was reliable and that there was probable cause for arresting Watson, the court held the arrest unconstitutional because the postal inspector had failed to secure an arrest warrant although he concededly had time to do so. Second, based on the totality of the circumstances, one of which was the illegality of the arrest, the court held Watson's consent to search had been coerced and hence was not a valid ground for the warrantless search of the automobile. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./420/924/">420 U. S. 924</a></span> (1975).</p>
<p></p>
<h2>II</h2>
<p>A major part of the Court of Appeals' opinion was its holding that Watson's warrantless arrest violated the Fourth Amendment. Although it did not expressly do so, it may have intended to overturn the conviction on the independent ground that the two credit cards were the inadmissible fruits of an unconstitutional arrest. Cf. <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975). However that may be, the Court of Appeals treated the illegality of Watson's arrest as an important factor in determining the voluntariness of his consent to search his car. We therefore deal first with the arrest issue.</p>
<p>Contrary to the Court of Appeals' view, Watson's arrest was not invalid because executed without a warrant. <span class="star-pagination">*415</span> Title <span class="citation no-link">18 U. S. C. § 3061</span> (a) (3) expressly empowers the Board of Governors of the Postal Service to authorize Postal Service officers and employees "performing duties related to the inspection of postal matters" to</p>
<blockquote>"make arrests without warrant for felonies cognizable under the laws of the United States if they have reasonable grounds to believe that the person to be arrested has committed or is committing such a felony."</blockquote>
<p>By regulation, <span class="citation no-link">39 CFR § 232.5</span> (a) (3) (1975), and in identical language, the Board of Governors has exercised that power and authorized warrantless arrests. Because there was probable cause in this case to believe that Watson had violated § 1708, the inspector and his subordinates, in arresting Watson, were acting strictly in accordance with the governing statute and regulations. The effect of the judgment of the Court of Appeals was to invalidate the statute as applied in this case and as applied to all the situations where a court fails to find exigent circumstances justifying a warrantless arrest. We reverse that judgment.</p>
<p>Under the Fourth Amendment, the people are to be "secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, . . . and no Warrants shall issue, but upon probable cause . . . ." Section 3061 represents a judgment by Congress that it is not unreasonable under the Fourth Amendment for postal inspectors to arrest without a warrant provided they have probable cause to do so.<sup>[4]</sup> This was not an <span class="star-pagination">*416</span> isolated or quixotic judgment of the legislative branch. Other federal law enforcement officers have been expressly authorized by statute for many years to make felony arrests on probable cause but without a warrant. This is true of United States marshals, <span class="citation no-link">18 U. S. C. § 3053</span>, and of agents of the Federal Bureau of Investigation, <span class="citation no-link">18 U. S. C. § 3052</span>; the Drug Enforcement Administration, <span class="citation no-link">84 Stat. 1273</span>, <span class="citation no-link">21 U. S. C. § 878</span>; the Secret Service, <span class="citation no-link">18 U. S. C. § 3056</span> (a); and the Customs Service, <span class="citation no-link">26 U. S. C. § 7607</span>.<sup>[5]</sup></p>
<p>Because there is a "strong presumption of constitutionality due to an Act of Congress, especially when it turns on what is `reasonable,' " "[o]bviously the Court should be reluctant to decide that a search thus authorized by Congress was unreasonable and that the Act was therefore unconstitutional." <i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#585" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 585</a></span> (1948). Moreover, there is nothing in the Court's prior cases indicating that under the <span class="star-pagination">*417</span> Fourth Amendment a warrant is required to make a valid arrest for a felony. Indeed, the relevant prior decisions are uniformly to the contrary.</p>
<p>"The usual rule is that a police officer may arrest without warrant one believed by the officer upon reasonable cause to have been guilty of a felony . . . ." <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 156</a></span> (1925). In <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span> (1959), the Court dealt with an FBI agent's warrantless arrest under <span class="citation no-link">18 U. S. C. § 3052</span>, which authorizes a warrantless arrest where there are reasonable grounds to believe that the person to be arrested has committed a felony. The Court declared that "[t]he statute states the constitutional standard. . . ." <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#100" aria-description="Citation for case: Henry v. United States">361 U. S., at 100</a></span>. The necessary inquiry, therefore, was not whether there was a warrant or whether there was time to get one, but whether there was probable cause for the arrest. In <i>Abel</i> v. <i>United States,</i> <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#232" aria-description="Citation for case: Abel v. United States">362 U. S. 217, 232</a></span> (1960), the Court sustained an administrative arrest made without "a judicial warrant within the scope of the Fourth Amendment." The crucial question in <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959), was whether there was probable cause for the warrantless arrest. If there was, the Court said, "the arrest, though without a warrant, was lawful . . . ." <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#310" aria-description="Citation for case: Draper v. United States"><i>Id.,</i> at 310</a></span>. <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#34" aria-description="Citation for case: Ker v. California">374 U. S. 23, 34-35</a></span> (1963) (opinion of Clark, J.), reiterated the rule that "[t]he lawfulness of the arrest without warrant, in turn, must be based upon probable cause . . ." and went on to sustain the warrantless arrest over other claims going to the mode of entry. Just last Term, while recognizing that maximum protection of individual rights could be assured by requiring a magistrate's review of the factual justification prior to any arrest, we stated that "such a requirement would constitute an intolerable handicap for legitimate law enforcement" and noted that the Court "has never invalidated an arrest supported by probable cause solely <span class="star-pagination">*418</span> because the officers failed to secure a warrant." <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#113" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 113</a></span> (1975).<sup>[6]</sup></p>
<p>The cases construing the Fourth Amendment thus reflect the ancient common-law rule that a peace officer was permitted to arrest without a warrant for a misdemeanor or felony committed in his presence as well as for a felony not committed in his presence if there was reasonable ground for making the arrest. 10 Halsbury's Laws of England 344-345 (3d ed. 1955); 4 W. Blackstone, Commentaries *292; 1 J. Stephen, A History of the Criminal Law of England 193 (1883); 2 M. Hale, Pleas of the Crown *72-74; Wilgus, Arrest Without a Warrant <span class="citation no-link">22 Mich. L. Rev. 541</span>, 547-550, 686-688 (1924); <span class="star-pagination">*419</span> <i>Samuel</i> v. <i>Payne,</i> <span class="citation" data-id="6629715"><a href="/opinion/6747612/green-v-graves/" aria-description="Citation for case: Green v. Graves">1 Doug. 359</a></span>, 99 Eng. Rep. 230 (K. B. 1780); <i>Beckwith</i> v. <i>Philby,</i> 6 Barn. &amp; Cress. 635, 108 Eng. Rep. 585 (K. B. 1827). This has also been the prevailing rule under state constitutions and statutes. "The rule of the common law, that a peace officer or a private citizen may arrest a felon without a warrant, has been generally held by the courts of the several States to be in force in cases of felony punishable by the civil tribunals." <i>Kurtz</i> v. <i>Moffitt,</i> <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/#504" aria-description="Citation for case: Kurtz v. Moffitt">115 U. S. 487, 504</a></span> (1885).</p>
<p>In <i>Rohan</i> v. <i>Sawin,</i> <span class="citation no-link">59 Mass. 281</span> (1850), a false-arrest case, the Supreme Judicial Court of Massachusetts held that the common-law rule obtained in that State. Given probable cause to arrest, "[t]he authority of a constable, to arrest without warrant, in cases of felony, is most fully established by the elementary books, and adjudicated cases." <i>Id.,</i> at 284. In reaching this judgment the court observed:</p>
<blockquote>"It has been sometimes contended, that an arrest of this character, without a warrant, was a violation of the great fundamental principles of our national and state constitutions, forbidding unreasonable searches and arrests, except by warrant founded upon a complaint made under oath. Those provisions doubtless had another and different purpose, being in restraint of general warrants to make searches, and requiring warrants to issue only upon a complaint made under oath. They do not conflict with the authority of constables or other peace-officers, or private persons under proper limitations, to arrest without warrant those who have committed felonies. The public safety, and the due apprehension of criminals, charged with heinous offences, imperiously require that such arrests should be made without warrant by officers of the law." <i>Id.,</i> at 284-285.</blockquote>
<p><span class="star-pagination">*420</span> Also rejected, <i>id.,</i> at 285-286, was the trial court's view that to justify a warrantless arrest, the State must show "an immediate necessity therefor, arising from the danger, that the plaintiff would otherwise escape, or secrete the stolen property, before a warrant could be procured against him." The Supreme Judicial Court ruled that there was no "authority for thus restricting a constable in the exercise of his authority to arrest for a felony without a warrant." <i>Id.,</i> at 286. Other early cases to similar effect were <i>Wakely</i> v. <i>Hart,</i> <span class="citation" data-id="6313783"><a href="/opinion/6441697/wakely-v-hart/" aria-description="Citation for case: Wakely v. Hart">6 Binn. 316</a></span> (Pa. 1814); <i>Tolley</i> v. <i>Mix,</i> <span class="citation" data-id="5513252"><a href="/opinion/5666272/holley-v-mix/" aria-description="Citation for case: Holley v. Mix">3 Wend. 350</a></span> (N. Y. Sup. Ct. 1829); <i>State</i> v. <i>Brown,</i> <span class="citation multiple-matches"><a href="/c/Del./5/505/">5 Del. 505</a></span> (Ct. Gen. Sess. 1853); <i>Johnson</i> v. <i>State,</i> <span class="citation" data-id="5554010"><a href="/opinion/5704309/johnson-v-state/" aria-description="Citation for case: Johnson v. State">30 Ga. 426</a></span> (1860); <i>Wade</i> v. <i>Chaffee,</i> 8 R. I. 224 (1865). See <i>Reuck</i> v. <i>McGregor,</i> 32 N. J. L. 70, 74 (Sup. Ct. 1866); <i>Baltimore &amp; O. R. Co.</i> v. <i>Cain,</i> <span class="citation" data-id="7899354"><a href="/opinion/7948364/baltimore-ohio-railroad-v-cain/#100" aria-description="Citation for case: Baltimore &amp; Ohio Railroad v. Cain">81 Md. 87, 100, 102</a></span>, <span class="citation" data-id="7899354"><a href="/opinion/7948364/baltimore-ohio-railroad-v-cain/#803" aria-description="Citation for case: Baltimore &amp; Ohio Railroad v. Cain">31 A. 801, 803, 804</a></span> (1895).<sup>[7]</sup></p>
<p>Because the common-law rule authorizing arrests without a warrant generally prevailed in the States, it is important for present purposes to note that in 1792 Congress invested United States marshals and their deputies with "the same powers in executing the laws of the United States, as sheriffs and their deputies in the several states have by law, in executing the laws of their respective states." Act of May 2, 1792, c. 28, § 9, <span class="citation no-link">1 Stat. 265</span>. The Second Congress thus saw no inconsistency between the Fourth Amendment and legislation giving United States marshals the same power as local peace officers to arrest for a felony without a warrant.<sup>[8]</sup> This provision equating the power of federal marshals <span class="star-pagination">*421</span> with those of local sheriffs was several times reenacted<sup>[9]</sup> and is today § 570 of Title 28 of the United States Code. That provision, however, was supplemented in 1935 by § 504a of the Judicial Code,<sup>[10]</sup> which in its essential elements is now <span class="citation no-link">18 U. S. C. § 3053</span> and which expressly empowered marshals to make felony arrests without warrant and on probable cause. It was enacted to furnish a federal standard independent of the vagaries of state laws, the Committee Report remarking that under existing law a "marshal or deputy marshal may make an arrest without a warrant within his district in all cases where the sheriff might do so under the State statutes." H. R. Rep. No. 283, 74th Cong., 1st Sess., 1 (1935). See <i>United States</i> v. <i>Riggs,</i> <span class="citation" data-id="308790"><a href="/opinion/308790/united-states-v-fairh-riggs/#702" aria-description="Citation for case: United States v. Fairh Riggs">474 F. 2d 699, 702-703, n. 2</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/820/">414 U. S. 820</a></span> (1973).</p>
<p>The balance struck by the common law in generally authorizing felony arrests on probable cause, but without a warrant, has survived substantially intact. It appears <span class="star-pagination">*422</span> in almost all of the States in the form of express statutory authorization. In 1963, the American Law Institute undertook the task of formulating a model statute governing police powers and practice in criminal law enforcement and related aspects of pretrial procedure. In 1975, after years of discussion, A Model Code of Pre-arraignment Procedure was proposed. Among its provisions was § 120.1 which authorizes an officer to take a person into custody if the officer has reasonable cause to believe that the person to be arrested has committed a felony, or has committed a misdemeanor or petty misdemeanor in his presence.<sup>[11]</sup> The commentary to this section said: "The Code thus adopts the traditional and almost universal standard for arrest without a warrant."<sup>[12]</sup></p>
<p><span class="star-pagination">*423</span> This is the rule Congress has long directed its principal law enforcement officers to follow. Congress has plainly decided against conditioning warrantless arrest power on proof of exigent circumstances.<sup>[13]</sup> Law enforcement officers may find it wise to seek arrest warrants where practicable to do so, and their judgments about probable cause may be more readily accepted where backed by a warrant issued by a magistrate. See <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#106" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 106</a></span> (1965); <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#111" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108, 111</a></span> (1964); <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#479" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 479-480</a></span> (1963). But we decline to transform this judicial preference into a constitutional rule when the judgment of the Nation and Congress has for so long been to authorize warrantless public arrests on probable cause rather than to encumber criminal prosecutions with endless litigation with respect to the existence of exigent circumstances, whether it was practicable <span class="star-pagination">*424</span> to get a warrant, whether the suspect was about to flee, and the like.</p>
<p>Watson's arrest did not violate the Fourth Amendment, and the Court of Appeals erred in holding to the contrary.</p>
<p></p>
<h2>III</h2>
<p>Because our judgment is that Watson's arrest comported with the Fourth Amendment, Watson's consent to the search of his car was not the product of an illegal arrest. To the extent that the issue of the voluntariness of Watson's consent was resolved on the premise that his arrest was illegal, the Court of Appeals was also in error.</p>
<p>We are satisfied in addition that the remaining factors relied upon by the Court of Appeals to invalidate Watson's consent are inadequate to demonstrate that, in the totality of the circumstances, Watson's consent was not his own "essentially free and unconstrained choice" because his "will ha[d] been overborne and his capacity for self-determination critically impaired." <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#225" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 225</a></span> (1973). There was no overt act or threat of force against Watson proved or claimed. There were no promises made to him and no indication of more subtle forms of coercion that might flaw his judgment. He had been arrested and was in custody, but his consent was given while on a public street, not in the confines of the police station. Moreover, the fact of custody alone has never been enough in itself to demonstrate a coerced confession or consent to search. Similarly, under <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span>,</i> the absence of proof that Watson knew he could withhold his consent, though it may be a factor in the overall judgment, is not to be given controlling significance. There is no indication in this record that Watson was a newcomer <span class="star-pagination">*425</span> to the law,<sup>[14]</sup> mentally deficient, or unable in the face of a custodial arrest to exercise a free choice. He was given <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and was further cautioned that the results of the search of his car could be used against him. He persisted in his consent.</p>
<p>In these circumstances, to hold that illegal coercion is made out from the fact of arrest and the failure to inform the arrestee that he could withhold consent would not be consistent with <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span></i> and would distort the voluntariness standard that we reaffirmed in that case.</p>
<p>In consequence, we reverse the judgment of the Court of Appeals.</p>
<p><i>So ordered.</i></p>
<p>MR. JUSTICE STEVENS took no part in the consideration or decision of this case.</p>
<p>MR. JUSTICE POWELL, concurring.</p>
<p>Although I concur in the opinion of the Court, I write to express additional views. I note at the outset that the case could be disposed of on the ground that respondent's consent to the search was plainly voluntary. <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973). Indeed, the evidence that his consent was the product of free will is so overwhelming that I would have held the consent voluntary even on the assumption that the preceding warrantless arrest was unconstitutional, and that the doctrine of <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), therefore was applicable. See <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975). The Court's different route to <span class="star-pagination">*426</span> the same result requires, however, an inquiry into the validity of the arrest itself.</p>
<p></p>
<h2>I</h2>
<p>Respondent was arrested without a warrant in a public restaurant six days after postal inspectors learned from a reliable source that he possessed stolen credit cards in violation of <span class="citation no-link">18 U. S. C. § 1708</span>. The Government made no effort to show that circumstances precluded the obtaining of a warrant, relying instead for the validity of the arrest solely upon the showing of probable cause to believe that respondent had committed a felony. Respondent contends, and the Court of Appeals held, that the absence of any exigency justifying the failure to procure a warrant renders this arrest violative of the Fourth Amendment.</p>
<p>In reversing the Court of Appeals, the Court concludes that nothing in our previous cases involving warrantless arrests supports the position of respondent and the Court of Appeals. See, <i>e. g., </i><i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#113" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 113</a></span> (1975). But it is fair to say, I think, that the prior decisions of the Court have assumed the validity of such arrests without addressing in a reasoned way the analysis advanced by respondent.<sup>[1]</sup> Today's decision is <span class="star-pagination">*427</span> the first square holding that the Fourth Amendment permits a duly authorized law enforcement officer to make a warrantless arrest in a public place even though he had adequate opportunity to procure a warrant after developing probable cause for arrest.</p>
<p>On its face, our decision today creates a certain anomaly. There is no more basic constitutional rule in the Fourth Amendment area than that which makes a warrantless search unreasonable except in a few "jealously and carefully drawn" exceptional circumstances. <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499</a></span> (1958); see <i>Almeida-Sanchez</i> v. <i>United States</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#279" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 279-280</a></span> (1973) (POWELL, J., concurring); <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#314" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 314-321</a></span> (1972); <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#454" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 454-455</a></span> (1971). On more than one occasion this Court has rejected an argument that a law enforcement officer's own probable cause to search a private place for contraband or evidence of crime should excuse his otherwise unexplained failure to procure a warrant beforehand. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#450" aria-description="Citation for case: Coolidge v. New Hampshire"><i>Id.,</i> at 450</a></span>; <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span>, 356-358 <span class="star-pagination">*428</span> (1967). In short, the course of judicial development of the Fourth Amendment with respect to searches has remained true to the principles so well expressed by Mr. Justice Jackson:</p>
<blockquote>"Any assumption that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers. . . . When the right of privacy must reasonably yield to the right of search is, as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948).</blockquote>
<p>Since the Fourth Amendment speaks equally to both searches and seizures, and since an arrest, the taking hold of one's person, is quintessentially a seizure, it would seem that the constitutional provision should impose the same limitations upon arrests that it does upon searches. Indeed, as an abstract matter an argument can be made that the restrictions upon arrest perhaps should be greater. A search may cause only annoyance and temporary inconvenience to the law-abiding citizen, assuming more serious dimension only when it turns up evidence of criminality. An arrest, however, is a serious personal intrusion regardless of whether the person seized is guilty or innocent. Although an arrestee cannot be held for a significant period without some neutral determination that there are grounds to do so, see <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein, supra,</a></span></i> no decision that he should go free can come quickly enough to erase the invasion of his privacy that already will have occurred. See <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#776" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 776</a></span> (1969) (WHITE, J., dissenting); cf. <i>United States</i> v. <span class="star-pagination">*429</span> <i>Robinson,</i> 414 U. S. 218, 237-238 (1973) (POWELL, J., concurring). Logic therefore would seem to dictate that arrests be subject to the warrant requirement at least to the same extent as searches.</p>
<p>But logic sometimes must defer to history and experience. The Court's opinion emphasizes the historical sanction accorded warrantless felony arrests. In the early days of the common law most felony arrests were made upon personal knowledge and without warrants. So established were such arrests as the usual practice that Lord Coke seriously questioned whether a justice of the peace, receiving his information secondhand instead of from personal knowledge, even could authorize an arrest by warrant. 4 E. Coke, Institutes 177 (6th ed. 1681). By the late 18th century it had been firmly established by Blackstone, with an intervening assist from Sir Matthew Hale, that magistrates could issue arrest warrants upon information supplied by others. 4 W. Blackstone, Commentaries *290; see 2 M. Hale, Pleas of the Crown *108-110. But recognition of the warrant power cast no doubt upon the validity of warrantless felony arrests, which continued to be practiced and upheld as before. 4 W. Blackstone, <i>supra,</i> at *282; 1 J. Chitty, Criminal Law *14-15. There is no historical evidence that the Framers or proponents of the Fourth Amendment, outspokenly opposed to the infamous general warrants and writs of assistance, were at all concerned about warrantless arrests by local constables and other peace officers. See N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 79-105 (1937); cf. <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#114" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 114-116</a></span>. As the Court today notes, the Second Congress' passage of an Act authorizing such arrests<sup>[2]</sup> so soon after the adoption of the Fourth Amendment <span class="star-pagination">*430</span> itself underscores the probability that the constitutional provision was intended to restrict entirely different practices.</p>
<p>The historical momentum for acceptance of warrantless arrests, already strong at the adoption of the Fourth Amendment, has gained strength during the ensuing two centuries. Both the judiciary and the legislative bodies of this Nation repeatedly have placed their imprimaturs upon the practice and, as the Government emphasizes, law enforcement agencies have developed their investigative and arrest procedures upon an assumption that warrantless arrests were valid so long as based upon probable cause. The decision of the Court of Appeals in this case was virtually unprecedented.<sup>[3]</sup> Of course, no practice that is inconsistent with constitutional protections can be saved merely by appeal to previous uncritical acceptance. But the warrantless felony arrest, long preferred at common law and unimpeached at the passage of the Fourth Amendment, is not such a practice. Given the revolutionary implications of such a holding, a declaration at this late date that warrantless felony arrests are constitutionally infirm would have to rest upon reasons more substantial than a desire to harmonize the rules for arrest with those governing searches. Cf. <i>United States</i> v. <i>Robinson, supra,</i> at 230.</p>
<p><span class="star-pagination">*431</span> Moreover, a constitutional rule permitting felony arrests only with a warrant or in exigent circumstances could severely hamper effective law enforcement. Good police practice often requires postponing an arrest, even after probable cause has been established, in order to place the suspect under surveillance or otherwise develop further evidence necessary to prove guilt to a jury.<sup>[4]</sup> Under the holding of the Court of Appeals such additional investigative work could imperil the entire prosecution. Should the officers fail to obtain a warrant initially, and later be required by unforeseen circumstances to arrest immediately with no chance to procure a lastminute warrant, they would risk a court decision that the subsequent exigency did not excuse their failure to get a warrant in the interim since they first developed probable cause. If the officers attempted to meet such a contingency <span class="star-pagination">*432</span> by procuring a warrant as soon as they had probable cause and then merely held it during their subsequent investigation, they would risk a court decision that the warrant had grown stale by the time it was used.<sup>[5]</sup> Law enforcement personnel caught in this squeeze could ensure validity of their arrests only by obtaining a warrant and arresting as soon as probable cause existed, thereby foreclosing the possibility of gathering vital additional evidence from the suspect's continued actions.</p>
<p>In sum, the historical and policy reasons sketched above fully justify the Court's sustaining of a warrantless arrest upon probable cause, despite the resulting divergence between the constitutional rule governing searches and that now held applicable to seizures of the person.<sup>[6]</sup></p>
<p></p>
<h2>II</h2>
<p>Finally, I share the view expressed in the opinion of MR. JUSTICE STEWART. It makes clear that we do not today consider or decide whether or under what circumstances <span class="star-pagination">*433</span> an officer lawfully may make a warrantless arrest in a private home or other place where the person has a reasonable expectation of privacy.<sup>[7]</sup></p>
<p>MR. JUSTICE STEWART, concurring in the result.</p>
<p>The arrest in this case was made upon probable cause in a public place in broad daylight. The Court holds that this arrest did not violate the Fourth Amendment, and I agree. The Court does <i>not</i> decide, nor could it decide in this case, whether or under what circumstances an officer must obtain a warrant before he may lawfully enter a private place to effect an arrest. See <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span>, 113 n. 13; <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#474" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 474-481</a></span>; <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#728" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 728</a></span>; <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499-500</a></span>.</p>
<p>MR. JUSTICE MARSHALL, with whom MR. JUSTICE BRENNAN joins, dissenting.</p>
<p>By granting police broad powers to make warrantless arrests, the Court today sharply reverses the course of our modern decisions construing the Warrant Clause of the Fourth Amendment. The Court turns next to the consent-to-search question last dealt with in <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span></i> <span class="star-pagination">*434</span> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973). Without acknowledgment or analysis, the Court extends the scope of that decision to the situation expressly reserved in <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span>,</i> and creates a rule inconsistent with <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span></i>'s own analysis. The Court takes both steps with a remarkable lack of consideration of either the facts of this case or the constitutional questions it is deciding. That is unfortunate not only because, in my view, the Court decides the constitutional questions wrongly, but also because consideration would have shown that the first question decided today is not raised by the facts before us, and that the second question should not be resolved here, given the present posture of this case. I respectfully dissent.</p>
<p></p>
<h2>I</h2>
<p>Before addressing what the Court does today, I note what it does not do. It does not decide this case on the narrow question that is presented. That is unfortunate for this is, fundamentally, a simple case.</p>
<p>On the afternoon of August 23, 1972, Awad Khoury, an informant of proved reliability, met with respondent Watson at a public restaurant under the surveillance of two postal inspectors. Khoury was under instructions to light a cigarette as a signal to the watching agents if Watson was in possession of stolen credit cards. Khoury lit a cigarette, and the postal inspectors moved in, made the arrest, and, ultimately, discovered under the floor mat of Watson's automobile the stolen credit cards that formed the basis of Watson's conviction and this appeal.</p>
<p>The signal of the reliable informant that Watson was in possession of stolen credit cards gave the postal inspectors probable cause to make the arrest. This probable cause was separate and distinct from the probable cause relating to the offense six days earlier, and provided an <span class="star-pagination">*435</span> adequate independent basis for the arrest. Whether or not a warrant ordinarily is required prior to making an arrest, no warrant is required when exigent circumstances are present. When law enforcement officers have probable cause to believe that an offense is taking place in their presence and that the suspect is at that moment in possession of the evidence, exigent circumstances exist. Delay could cause the escape of the suspect or the destruction of the evidence. Accordingly, Watson's warrantless arrest was valid under the recognized exigent-circumstances exception to the warrant requirement, and the Court has no occasion to consider whether a warrant would otherwise be necessary.<sup>[1]</sup></p>
<p>This conclusion should properly dispose of the case before us. As the Court observes, <i>ante,</i> at 414, the Court of Appeals relied heavily on the supposed illegality of Watson's arrest in ruling that his consent to the search of his car was coerced. Neither the opinion of the Court of Appeals nor the briefs of the parties here address the remaining issue of the circumstances under which consent to search given by a suspect <i>lawfully</i> in custody may be deemed coerced. Since that issue is both complex and <span class="star-pagination">*436</span> expressly reserved in <i>Schneckloth</i> v. <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Bustamonte, supra</a></span></i><i>,</i> I think it inappropriate for resolution without the benefit of the views of the parties and the Court of Appeals. Accordingly, I would reverse the Court of Appeals on the legality of the arrest, vacate its judgment, and remand the case to that court for further proceedings.</p>
<p></p>
<h2>II</h2>
<p>Since, for reasons it leaves unexpressed, the Court does not take this traditional course, I am constrained to express my views on the issues it unnecessarily decides. The Court reaches its conclusion that a warrant is not necessary for a police officer to make an arrest in a public place, so long as he has probable cause to believe a felony has been committed, on the basis of its views of precedent and history. As my Brother POWELL correctly observes, <i>ante,</i> at 426-427, n. 1 (concurring), the precedent is spurious. None of the cases cited by the Court squarely confronted the issue decided today. Moreover, an examination of the history relied on by the Court shows that it does not support the conclusion laid upon it. After showing why, in my view, the Court's rationale does not support today's result, I shall examine the relevant decisions and suggest what I believe to be the proper rule for arrests.</p>
<p>The Fourth Amendment provides:</p>
<blockquote>"The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</blockquote>
<p>There is no doubt that by the reference to the seizure of persons, the Fourth Amendment was intended to <span class="star-pagination">*437</span> apply to arrests. <i>Ex parte Burford,</i> <span class="citation" data-id="84827"><a href="/opinion/84827/ex-parte-burford/" aria-description="Citation for case: Ex Parte Burford">3 Cranch 448</a></span> (1806). See generally N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 79-82 (1937). Indeed, we have often considered whether arrests were made in conformity with the Fourth Amendment. <i>E. g., </i><i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89</a></span> (1964); <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963); <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959); <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span> (1958). Admittedly, as the Court observes, some of our decisions make passing reference to the common-law rule on arrests. <i>E. g., </i><i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 156</a></span> (1925); <i>Bad Elk</i> v. <i>United States,</i> <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/#534" aria-description="Citation for case: Bad Elk v. United States">177 U. S. 529, 534</a></span> (1900); <i>Kurtz</i> v. <i>Moffitt,</i> <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/#498" aria-description="Citation for case: Kurtz v. Moffitt">115 U. S. 487, 498-499</a></span> (1885). However, none of the cases cited by the Court, nor any other warrantless arrest case in this Court, mandates the decision announced today. Frequently exigent circumstances were present, so that the warrantless arrest was proper even if a warrant ordinarily may be required. <i>Ker</i> v. <i>California, supra</i><i>; </i><i>Draper</i> v. <i>United States, supra</i><i>; </i><i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/" aria-description="Citation for case: United States v. Di Re">332 U. S. 581</a></span> (1948). Many cases have invalidated arrests as not based on probable cause, thereby bypassing the need to reach the warrant question. <i>E. g., </i><i>Beck</i> v. <i>Ohio, supra</i><i>; </i><i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span> (1959). Elsewhere the Court has simply assumed the propriety of the arrest and resolved the case before it on other grounds. <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969). Cf. <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#476" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 476</a></span> (1971). And in other cases, the Court noted, but did not reach, the warrantless-arrest issue, <i>E. g., </i><i>Giordenello</i> v. <i>United States, supra</i><i>.</i> In sum, as the case-by-case analysis undertaken by my Brother POWELL demonstrates, the dicta relied upon by the Court in support of its decision today are just thatdicta. See <i>ante,</i> at 426-427, n. 1 (concurring). They are no substitute <span class="star-pagination">*438</span> for reasoned analysis of the relationship between the warrant requirement and the law of arrest.</p>
<p>The Court next turns to history. It relies on the English common-law rule of arrest and the many state and federal statutes following it. There are two serious flaws in this approach. First, as a matter of factual analysis, the substance of the ancient common-law rule provides no support for the far-reaching modern rule that the Court fashions on its model. Second, as a matter of doctrine, the longstanding existence of a Government practice does not immunize the practice from scrutiny under the mandate of our Constitution.</p>
<p>The common-law rule was indeed as the Court states it:</p>
<blockquote>"[A] peace officer was permitted to arrest without a warrant for a misdemeanor or felony committed in his presence as well as for a felony not committed in his presence if there was reasonable ground for making the arrest." <i>Ante,</i> at 418, and sources cited.</blockquote>
<p>See also <i>Kurtz</i> v. <i><span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/" aria-description="Citation for case: Kurtz v. Moffitt">Moffitt, supra</a></span></i><i>; </i><i>Bad Elk</i> v. <i>United States, supra</i><i>.</i> To apply the rule blindly today, however, makes as much sense as attempting to interpret Hamlet's admonition to Ophelia, "Get thee to a nunnery, go,"<sup>[2]</sup> without understanding the meaning of Hamlet's words in the context of their age.<sup>[3]</sup> For the fact is that a felony at common law and a felony today bear only slight resemblance, with the result that the relevance of the common-law rule of arrest to the modern interpretation of our Constitution is minimal.</p>
<p>Both at common law and today, felonies find definition in the penal consequences of crime rather than the <span class="star-pagination">*439</span> nature of the crime itself. At common law, as this Court has several times recognized,</p>
<blockquote>"No crime was considered a felony which did not occasion a total forfeiture of the offender's lands, or goods, or both." <i>Kurtz</i> v. <i>Moffitt,</i> <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/#499" aria-description="Citation for case: Kurtz v. Moffitt">115 U. S., at 499</a></span>.</blockquote>
<p>See also <i>Ex parte Wilson,</i> <span class="citation" data-id="91385"><a href="/opinion/91385/ex-parte-wilson/#423" aria-description="Citation for case: Ex Parte Wilson">114 U. S. 417, 423</a></span> (1885); 4 W. Blackstone, Commentaries *95.<sup>[4]</sup> At present, on the other hand,</p>
<blockquote>"Any offense punishable by death or imprisonment for a term exceeding one year is a felony." <span class="citation no-link">18 U. S. C. § 1</span> (1).<sup>[5]</sup></blockquote>
<p>This difference reflects more than changing notions of penology. It reflects a substantive change in the kinds of crimes called felonies. <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S., at 158</a></span>.<sup>[6]</sup> Only the most serious crimes were felonies at common law, and many crimes now classified <span class="star-pagination">*440</span> as felonies under federal or state law were treated as misdemeanors. Professor Wilgus has summarized and documented the cases:</p>
<blockquote>"At common law an assault was a misdemeanor and it was still only such even if made with the intent to rob, murder, or rape. Affrays, abortion, barratry, bribing voters, challenging to fight, compounding felonies, cheating by false weights or measures, escaping from lawful arrest, eavesdropping, forgery, false imprisonment, forcible and violent entry, forestalling, kidnapping, libel, mayhem, maliciously killing valuable animals, obstructing justice, public nuisance, perjury, riots and routs, etc. were misdemeanors. . . ." Wilgus, Arrest Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 541</span>, 572-573 (1924) (footnotes omitted).</blockquote>
<p>See also 9 Halsbury's Laws of England 450-793 (1909).<sup>[7]</sup> To make an arrest for any of these crimes at common law, the police officer was required to obtain a warrant, unless the crime was committed in his presence.<sup>[8]</sup> Since many of these same crimes are commonly classified as felonies today,<sup>[9]</sup> however, under the Court's holding a <span class="star-pagination">*441</span> warrant is no longer needed to make such arrests, a result in contravention of the common law.</p>
<p>Thus the lesson of the common law, and those courts in this country that have accepted its rule, is an ambiguous one. Applied in its original context, the common-law rule would allow the warrantless arrest of some, but not all, of those we call felons today. Accordingly, the Court is simply historically wrong when it tells us that "[t]he balance struck by the common law in generally authorizing felony arrests on probable cause, but without a warrant, has survived substantially intact." <i>Ante,</i> at 421. As a matter of substance, the balance struck by the <span class="star-pagination">*442</span> common law in accommodating the public need for the most certain and immediate arrest of criminal suspects with the requirement of magisterial oversight to protect against mistaken insults to privacy decreed that only in the most serious of cases could the warrant be dispensed with. This balance is not recognized when the common-law rule is unthinkingly transposed to our present classifications of criminal offenses. Indeed, the only clear lesson of history is contrary to the one the Court draws: the common law considered the arrest warrant far more important than today's decision leaves it.</p>
<p>I do not mean by this that a modern warrant requirement should apply only to arrests precisely analogous to common-law misdemeanors, and be inapplicable to analogous of common-law felonies. Rather, the point is simply that the Court's unblinking literalism cannot replace analysis of the constitutional interests involved. While we can learn from the common law, the ancient rule does not provide a simple answer directly transferable to our system. Thus, in considering the applicability of the common-law rule to our present constitutional scheme, we must consider <i>both</i> of the rule's two opposing constructs: the presumption favoring warrants, as well as the exception allowing immediate arrests of the most dangerous criminals. The Court's failure to do so, indeed its failure to recognize any tension in the common-law rule at all, drains all validity from its historical analysis.</p>
<p>Lastly, the Court relies on the numerous state and federal statutes codifying the common-law rule. But this, too, is no substitute for reasoned analysis. True enough, the national and state legislatures have steadily ratified the drift of the balance struck by the common-law rule past the bounds of its original intent. And it is true as well, as the Court observes, that a presumption of constitutionality attaches to every Act of Congress. But neither observation is determinative of the constitutional issue, <span class="star-pagination">*443</span> and the doctrine of deference that the Court invokes is contrary to the principles of constitutional analysis practiced since <i>Marbury</i> v. <i>Madison,</i> <span class="citation" data-id="84759"><a href="/opinion/84759/marbury-v-madison/" aria-description="Citation for case: Marbury v. Madison">1 Cranch 137</a></span> (1803). The Court's error on this score is far more dangerous than its misreading of history, for it is well settled that the mere existence of statutes or practice, even of long standing, is no defense to an unconstitutional practice. "[N]o one acquires a vested or protected right in violation of the Constitution by long use, even when that span of time covers our entire national existence and indeed predates it." <i>Walz</i> v. <i>Tax Comm'n,</i> <span class="citation" data-id="9841980"><a href="/opinion/108135/walz-v-tax-commn-of-city-of-new-york/#678" aria-description="Citation for case: Walz v. Tax Comm&#x27;n of City of New York">397 U. S. 664, 678</a></span> (1970). See also <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973); <i>Roe</i> v. <i>Wade,</i> <span class="citation" data-id="9425157"><a href="/opinion/108713/roe-v-wade/" aria-description="Citation for case: Roe v. Wade">410 U. S. 113</a></span> (1973); <i>Furman</i> v. <i>Georgia,</i> <span class="citation" data-id="9424993"><a href="/opinion/108605/furman-v-georgia/" aria-description="Citation for case: Furman v. Georgia">408 U. S. 238</a></span> (1972); <i>Reynolds</i> v. <i>Sims,</i> <span class="citation" data-id="9422829"><a href="/opinion/106850/reynolds-v-sims/" aria-description="Citation for case: Reynolds v. Sims">377 U. S. 533</a></span> (1964).<sup>[10]</sup> Our function in constitutional cases is weightier than the Court today suggests: where reasoned analysis shows a practice to be constitutionally deficient, our obligation is to the Constitution, not the Congress.</p>
<p>In sum, the Court's opinion is without foundation. It relies on precedents that are not precedents. It relies on history that offers no clear rule to impose, but only conflicting interests to balance. It relies on statutes that constitute, at best, no more than an aid to construction. The Court never grapples with the warrant requirement of the Fourth Amendment and the cases construing it. It simply announces, by <i>ipse dixit,</i> a rule squarely rejecting the warrant requirement we have favored for so long.</p>
<p></p>
<h2>III</h2>
<p>My Brother POWELL concludes: "Logic . . . would seem to dictate that arrests be subject to the warrant <span class="star-pagination">*444</span> requirement at least to the same extent as searches." <i>Ante,</i> at 429 (concurring). I agree.</p>
<p>One of the few absolutes of our law is the requirement that, absent the presence of one of a few "jealously and carefully drawn" exceptions, <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499</a></span> (1958), a warrant be obtained prior to any search.<sup>[11]</sup> "[E]xcept in certain carefully defined classes of cases, a search of private property without proper consent is `unreasonable' [within the meaning of the Fourth Amendment] unless it has been authorized by a valid search warrant." <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528-529</a></span> (1967). See <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#439" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 439</a></span> (1973); <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#315" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 315-316, 318</a></span> (1972); <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#454" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 454-455</a></span>; <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#762" aria-description="Citation for case: Chimel v. California">395 U. S., at 762</a></span>; <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968); <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> (1967).</p>
<p>The rule the Court announces today for arrests is the reverse of this approach. It is, in essence, the <i>Rabinowitz</i> rule: "The relevant test is not whether it is reasonable to procure [an arrest] warrant, but whether the [arrest] was reasonable." <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#66" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 66</a></span> (1950). In the search context, <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> has been overruled, <i>Chimel</i> v. <i>California, supra,</i> at 764-768, and thoroughly discredited, see, <i>e. g., </i><i>United States</i> v. <i>United States District Court, supra,</i> at 315, and n. 16. The <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> approach simply does not provide adequate protection for the important personal privacy interests codified in the <span class="star-pagination">*445</span> Fourth Amendment. Given "[t]he history of the use, and not infrequent abuse, of the power to arrest," <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#479" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 479</a></span> (1963), and the fact that arrests are, in terms, as fully governed by the Fourth Amendment as searches, the logical presumption is that arrests and searches should be treated equally under the Fourth Amendment. Analysis of the interests involved confirms this supposition.</p>
<p>The Court has typically engaged in a two-part analysis in deciding whether the presumption favoring a warrant should be given effect in situations where a warrant has not previously been clearly required. Utilizing that approach we must now consider (1) whether the privacy of our citizens will be better protected by ordinarily requiring a warrant to be issued before they may be arrested; and (2) whether a warrant requirement would unduly burden legitimate governmental interests. <i>United States</i> v. <i>United States District Court, supra,</i> at 315; <i>Camara</i> v. <i>Municipal Court, supra,</i> at 533.</p>
<p>The first question is easily answered. Of course, the privacy of our citizens will be better protected by a warrant requirement. We have recognized that "the Fourth Amendment protects people, not places." <i>Katz</i> v. <i>United States, supra,</i> at 351. Indeed, the privacy guaranteed by the Fourth Amendment is quintessentially personal. Cf. <i>Roe</i> v. <i><span class="citation" data-id="9425157"><a href="/opinion/108713/roe-v-wade/" aria-description="Citation for case: Roe v. Wade">Wade, supra</a></span></i><i>; </i><i>Doe</i> v. <i>Bolton,</i> <span class="citation" data-id="9425160"><a href="/opinion/108714/doe-v-bolton/" aria-description="Citation for case: Doe v. Bolton">410 U. S. 179</a></span> (1973); <i>Griswold</i> v. <i>Connecticut,</i> <span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/" aria-description="Citation for case: Griswold v. Connecticut">381 U. S. 479</a></span> (1965). Thus a warrant is required in search situations not because of some high regard for property, but because of our regard for the individual, and <i>his</i> interest in his possessions and person.</p>
<blockquote>"It is not the breaking of his doors, and the rummaging of his drawers, that constitutes the essence of the offense; but it is the invasion of his indefeasible right of personal security, personal liberty and <span class="star-pagination">*446</span> private property, where that right has never been forfeited by his conviction of some public offense, it is the invasion of this sacred right which underlies and constitutes the essence of Lord Camden's judgment [in the classic English warrant case of <i>Entick</i> v. <i>Carrington,</i> 19 How. St. Tr. 1029, 95 Eng. Rep. 807 (1765)]." <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span> (1886).</blockquote>
<p>Not only is the Fourth Amendment directly addressed to the privacy of our citizens, but it speaks in indistinguishable terms about the freedom of both persons and property from unreasonable seizures. A warrant is required in the search situation to protect the privacy of the individual, but there can be no less invasion of privacy when the individual himself, rather than his property, is searched and seized. Indeed, an unjustified arrest that forces the individual temporarily to forfeit his right to control his person and movements and interrupts the course of his daily business may be more intrusive than an unjustified search.</p>
<blockquote>"Being arrested and held by the police, even if for a few hours, is, for most persons, awesome and frightening. Unlike other occasions on which one may be authoritatively required to be somewhere or do something, an arrest abruptly subjects a person to constraint, and removes him to unfamiliar and threatening surroundings. Moreover, this exercise of control over the person depends not just on his willingness to comply with an impersonal directive, such as a summons or subpoena, but on an order which a policeman issues on the spot and stands ready then and there to back up with force. The security of the individual requires that so abrupt and intrusive an authority be granted to public officials only on a guarded basis." ALI, Model Code <span class="star-pagination">*447</span> of Pre-arraignment Procedure, Commentary 290-291 (1975).</blockquote>
<p>A warrant requirement for arrests would, of course, minimize the possibility that such an intrusion into the individual's sacred sphere of personal privacy would occur on less than probable cause. Primarily for this reason, a warrant is required for searches. Surely there is no reason to place greater trust in the partisan assessment of a police officer that there is probable cause for an arrest than in his determination that probable cause exists for a search.<sup>[12]</sup> Last Term the Court unanimously recognized <span class="star-pagination">*448</span> that detention of a person cannot be prolonged without judicial oversight of the probable-cause determination. <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span> (1975). But while <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> may provide the best protection possible against less-than-probable-cause warrantless arrests based on exigent circumstances, it does not fully protect the Fourth Amendment rights at stake here. A less-than-probable-cause arrest followed by a <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> release is as offensive to the Fourth Amendment as a less-than-probable-cause search that fails to uncover the evidence sought, and the requirement of a warrant is as instrumental in protecting against the one as the other. Indeed, the Court's opinion in <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> expressly recognizes that maximum protection of individual rights can only be realized "by requiring a magistrate's review of the factual justification prior to any arrest . . . ." <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#113" aria-description="Citation for case: Gerstein v. Pugh"><i>Id.,</i> at 113</a></span>.</p>
<p>We come then to the second part of the warrant test: whether a warrant requirement would unduly burden legitimate law enforcement interests. Dicta in <i><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></i> answer this question in the affirmative, and these concerns are somewhat amplified in the concurrence of my Brother POWELL. <i>Ante,</i> at 431-432. I believe, however, that the suggested concerns are wholly illusory. Indeed, the argument that a warrant requirement for arrests would be an onerous chore for the police seems somewhat anomalous in light of the Government's concession that "it is the standard practice of the Federal Bureau of Investigation [FBI] to present its evidence to the United States Attorney, and to obtain a warrant, before making an arrest." Brief for United States 26 n. 15. In the past, the practice and experience of the FBI have been taken as a substantial indication that no intolerable burden would be presented by a proposed rule of procedure. <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#483" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 483-486</a></span> (1966). <span class="star-pagination">*449</span> There is no reason to accord less deference to the FBI practice here.<sup>[13]</sup></p>
<p>The Government's assertion that a warrant requirement would impose an intolerable burden stems, in large part, from the specious supposition that procurement of an arrest warrant would be necessary as soon as probable cause ripens. Brief for United States 22-24. There is no requirement that a search warrant be obtained the moment police have probable cause to search. The rule is only that present probable cause be shown and a warrant obtained before a search is undertaken.<sup>[14]</sup> Fed. Rule Crim. Proc. 41. Cf. <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#59" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 59</a></span> (1967). The same rule should obtain for arrest warrants, where it may even make more sense. Certainly, there is less need for prompt procurement of a warrant in the arrest situation. Unlike probable cause to search, probable cause to arrest, once formed, will continue to exist for the indefinite future, at least if no intervening exculpatory facts come to light. See <i>Wilson</i> v. <i>United States,</i> 117 U. S. App. D. C. 28, <span class="citation" data-id="262538"><a href="/opinion/262538/percy-e-wilson-v-united-states/" aria-description="Citation for case: Percy E. Wilson v. United States">325 F. 2d 224</a></span> (1963), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./377/1005/">377 U. S. 1005</a></span> (1964), and <span class="star-pagination">*450</span> <i>United States</i> v. <i>Wilson,</i> <span class="citation" data-id="267195"><a href="/opinion/267195/united-states-v-percy-wilson/" aria-description="Citation for case: United States v. Percy Wilson">342 F. 2d 782</a></span> (CA2 1965) (both upholding delay of 16 months between formation of probable cause and issuance of arrest warrant). Cf. <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#310" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 310</a></span> (1966).</p>
<p>This sensible approach obviates most of the difficulties that have been suggested with an arrest warrant rule. Police would not have to cut their investigation short the moment they obtain probable cause to arrest, nor would undercover agents be forced suddenly to terminate their work and forfeit their covers. <i>Godfrey</i> v. <i>United States,</i> 123 U. S. App. D. C. 219, <span class="citation" data-id="271327"><a href="/opinion/271327/larry-c-godfrey-v-united-states/" aria-description="Citation for case: Larry C. Godfrey v. United States">358 F. 2d 850</a></span> (1966). Moreover, if in the course of the continued police investigation exigent circumstances develop that demand an immediate arrest, the arrest may be made without fear of unconstitutionality, so long as the exigency was unanticipated and not used to avoid the arrest warrant requirement. Cf. <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#469" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 469-471</a></span> (evidence may be seized if in plain view only if its discovery is inadvertent). Likewise, if in the course of the continued investigation police uncover evidence tying the suspect to another crime, they may immediately arrest him for that crime if exigency demands it, and still be in full conformity with the warrant rule. This is why the arrest in this case was not improper.<sup>[15]</sup> Other than where police attempt to evade the warrant requirement, the rule would invalidate an arrest only in the obvious situation: where police, with probable cause but without exigent circumstances, set out to arrest a suspect. Such an arrest must be void, even if exigency develops in the course of the arrest that <span class="star-pagination">*451</span> would ordinarily validate it; otherwise the warrant requirement would be reduced to a toothless prescription.</p>
<p>In sum, the requirement that officers about to arrest a suspect ordinarily obtain a warrant before they do so does not seem unduly burdensome, at least no more burdensome than any other requirement that law enforcement officials undertake a new procedure in order to comply with the dictates of the Constitution. Cf. <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span> (1975); <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967); <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967); <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona, supra</a></span></i><i>; </i><i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span> (1963).</p>
<p>It is suggested, however, that even if application of this rule does not require police to secure a warrant as soon as they obtain probable cause, the confused officer would nonetheless be prone to do so. If so, police "would risk a court decision that the warrant had grown stale by the time it was used." <i>Ante,</i> at 432 (POWELL, J., concurring) (footnote omitted). This fear is groundless. First, as suggested above, the requirement that police procure a warrant before an arrest is made is rather simple of application. Thus, there is no need for the police to find themselves in this "squeeze." Second, the "squeeze" is nonexistent. Just as it is virtually impossible for probable cause for an arrest to grow stale between the time of formation and the time a warrant is procured, it is virtually impossible for probable cause to become stale between procurement and arrest.<sup>[16]</sup> Delay by law enforcement officers in executing an arrest warrant does not ordinarily affect the legality of the arrest.<sup>[17]</sup><span class="star-pagination">*452</span> <i>United States</i> v. <i>Wilson, supra</i><i>; </i><i>Wilson</i> v. <i>United States, supra</i><i>; </i><i>Carlo</i> v. <i>United States,</i> <span class="citation" data-id="9447739"><a href="/opinion/253075/john-carlo-v-united-states/#846" aria-description="Citation for case: John Carlo v. United States">286 F. 2d 841, 846</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./366/944/">366 U. S. 944</a></span> (1961); <i>United States</i> v. <i>Joines,</i> <span class="citation" data-id="245925"><a href="/opinion/245925/united-states-v-j-paul-joines-and-john-robert-joines-appeal-of-john/" aria-description="Citation for case: United States v. J. Paul Joines and John Robert Joines....">258 F. 2d 471</a></span> (CA3), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./358/880/">358 U. S. 880</a></span> (1958); <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9445492"><a href="/opinion/241496/veto-giordenello-v-united-states/" aria-description="Citation for case: Veto Giordenello v. United States">241 F. 2d 575</a></span> (CA5 1957), rev'd on other grounds, <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span> (1958). In short, staleness should be the least of an arresting officer's worries.<sup>[18]</sup></p>
<p>Thus, the practical reasons marshaled against an arrest warrant requirement are unimpressive.<sup>[19]</sup> If anything, the virtual nonexistence of a staleness problem suggests that such a requirement would be less burdensome for police than the search warrant rule. And given the significant protection our citizens will gain from a warrant requirement, accepted Fourth Amendment <span class="star-pagination">*453</span> analysis dictates that a warrant rule be imposed. This conclusion, then, answers the questions posed by analysis of the common-law rule on arrest. In choosing between the common law's prescription that a warrant ordinarily be obtained for the arrest of persons suspected of committing less serious crimes, and the common-law exception allowing warrantless arrests of suspects in more serious offenses, the intervention of our Fourth Amendment and the cases developing its application necessarily favor the former approach. Thus, I believe the proper result is application of the warrant requirement, as it has developed in the search context, to all arrests.</p>
<p></p>
<h2>IV</h2>
<p>Accordingly, I dissent from the Court's contrary holding. It is always disheartening when the Court ignores a relevant body of precedent and eschews any considered analysis. It is more so when the result of such an approach is a rule that "leave[s] law-abiding citizens at the mercy of the officers' whim or caprice," <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span> (1949), and renders the constitutional protection of our "persons" a nullity. The consequences of the Court's casually adopted rationale are clear.</p>
<p>First, the opinion all but answers the question raised in <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#480" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 480-481</a></span>, namely, "whether and under what circumstances an officer may enter a suspect's home to make a warrantless arrest." <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 113</a></span> n. 13.<sup>[20]</sup><span class="star-pagination">*454</span> Admittedly, my Brothers STEWART and POWELL do not read the opinion to resolve that issue and, indeed, the Court purports to leave it open. <i>Ante,</i> at 418 n. 6. But the mode of analysis utilized herereliance on the common law and federal and state statutesprovides a ready answer, as indeed the Court hints by its extended discussion of § 120.6 of the ALI Model Code of Prearraignment Procedure and its relevant commentary. <i>Ante,</i> at 418 n. 6. See also Wilgus, 22 Mich. L. Rev., at 800 ("For a felony . . . one may break into the dwelling house to take the felon . . ."); <i>id.,</i> at 558, 803; 9 Halsbury's Laws of England 307 (1909); 1 J. Chitty, Criminal Law *23; 4 W. Blackstone, Commentaries *292. Unless the approach of this opinion is to be fundamentally rejected, it will be difficult, if not impossible, to follow these sources to any but one conclusionthat entry to effect a warrantless arrest is permissible.</p>
<p>Second, by paying no attention whatever to the substance of the offense, and considering only whether it is labeled "felony," the Court, in the guise of "constitutionalizing" the common-law rule, actually does away with it altogether, replacing it with the rule that the police may, consistent with the Constitution, arrest on probable cause anyone who they believe has committed any sort of crime at all. Certainly this rule would follow <span class="star-pagination">*455</span> if the legislatures redenominated all crimes as "felonies." As a matter of substance, it would seem to follow in any event from the holding of this case, for the Court surely does not intend to accord constitutional status to a distinction that can be readily changed by legislative fiat.<sup>[21]</sup></p>
<p>Lastly, the Court surrenders the opportunity to put teeth in our oft-expressed preference for the use of arrest warrants. <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S., at 96</a></span>; <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#479" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 479-482</a></span>. While some incentives for police to obtain arrest warrants remain,<sup>[22]</sup><span class="star-pagination">*456</span> they are only indirect and have proved ineffective in the past in assuring routine application for arrest warrants when the circumstances permit it. By our holding today, the preference for an arrest warrant, which the Court has conceded is the optimal method to protect our citizens from the affront of an unlawful arrest, will remain only an ideal, one that the Court will espouse but not enforce.</p>
<p></p>
<h2>V</h2>
<p>Having disposed of the suggestion that the Fourth Amendment requires a warrant of arrest before the police may seize our persons, the Court turns its attention, briefly, to whether Watson voluntarily consented to the search of his automobile. I have suggested above that because this issue is of some complexity and has not been thoroughly briefed for us I would remand this case for initial consideration of the question by the Court of Appeals. The Court, however, finds the question simplicity itself. It applies the "totality of the circumstances" test established in <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973), and treats the question as merely requiring the application of settled law to the facts before us.</p>
<p>That is not the case. Watson was in custody when his consent was obtained. The lack of custody was of decisional importance in <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span>,</i> which repeatedly distinguished the case before it from one involving a suspect in custody. <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#232" aria-description="Citation for case: Schneckloth v. Bustamonte"><i>Id.,</i> at 232, 240-241</a></span>, and n. 29, 246-248, and n. 36. The Court held:</p>
<blockquote>"Our decision today is a narrow one. We hold only that <i>when the subject of a search is not in custody</i> and the State attempts to justify a search on the basis of his consent, the Fourth and Fourteenth <span class="star-pagination">*457</span> Amendments require that it demonstrate that the consent was in fact voluntarily given, and not the result of duress or coercion, express or implied." <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#248" aria-description="Citation for case: Schneckloth v. Bustamonte"><i>Id.,</i> at 248</a></span> (emphasis added).</blockquote>
<p>Not once, but twice, the question the Court today treats as settled was expressly reserved:</p>
<blockquote>"[T]he present case does not require a determination of the proper standard to be applied in assessing the validity of a search authorized solely by an alleged consent that is obtained from a person after he has been placed in custody." <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Id.,</a></span></i> at 241 n. 29.</blockquote>
<p>See also <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">id.,</a></span></i> at 247 n. 36.</p>
<p>I adhere to the views expressed in my dissent in <i>Schneckloth, id.,</i> at 277, and therefore believe that the Government must always show that a person who consented to a search did so knowing he had the right to refuse. But even short of this position, there are valid reasons for application of such a rule to consents procured from suspects held in custody. It was, apparently, the force of those reasons that prompted the Court in <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span></i> to reserve the question. Most significantly, we have previously accorded constitutional recognition to the distinction between custodial and noncustodial police contacts. <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#477" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 477-478</a></span>. Indeed, <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span></i> directly relied on <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s articulation of that distinction to reach its conclusion. <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#232" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S., at 232</a></span>. Thus, while custodial interrogation is inherently coercive, and any consent thereby obtained necessarily suspect, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> (and <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span></i>) expressly reject the notion that there is anything inherently coercive about general noncustodial interrogation. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#477" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 477-478</a></span>; <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#247" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S., at 247</a></span>. For this reason it is entirely appropriate to place a substantially greater burden on the Government <span class="star-pagination">*458</span> to validate a consent obtained from a suspect following custodial interrogation, however brief. Indeed, it is difficult, if not impossible, to square a contrary conclusion with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> A substantially greater burden on the Government means, quite obviously, that the fact of custody is not merely another factor to be considered in the "totality of the circumstances."<sup>[23]</sup> And, in my view, it means that the Government must show that the suspect knew he was not obligated to consent to the search.</p>
<p>Whether after due consideration the Court would accept this view or not, it is a surrender of our judicial task altogether to ignore the question. And, equally disturbing, it is a distortion of our precedent to pretend that what seemed a difficult and complex problem three years ago is no problem at all today.</p>
<p>I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[1]  In the meantime the inspector had verified that the card was stolen.</p>
<p>[2]  Title <span class="citation no-link">18 U. S. C. § 1708</span> punishes the theft of mail as well as the possession of stolen mail. The punishment is a fine of not more than $2,000 or imprisonment for not more than five years, or both.</p>
<p>[3]  Watson was acquitted on the second count. The fourth was dismissed prior to trial.</p>
<p>[4]  At least since approval of the Act of June 10, 1955, c. 137, § 203, <span class="citation no-link">69 Stat. 106</span>, <span class="citation no-link">39 U. S. C. § 3523</span> (a) (2) (K) (1964 ed.), postal inspectors' duties have been thought to permit arrest without a warrant upon probable cause. Compare <i>United States</i> v. <i>Helbock,</i> <span class="citation" data-id="2304502"><a href="/opinion/2304502/united-states-v-helbock/" aria-description="Citation for case: United States v. Helbock">76 F. Supp. 985</a></span> (Ore. 1948), with <i>United States</i> v. <i>Alexander,</i> <span class="citation" data-id="286516"><a href="/opinion/286516/united-states-v-orlando-c-alexander/" aria-description="Citation for case: United States v. Orlando C. Alexander">415 F. 2d 1352</a></span> (CA7 1969), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./397/1014/">397 U. S. 1014</a></span> (1970); <i>Kelley</i> v. <i>Dunne,</i> <span class="citation" data-id="9450633"><a href="/opinion/267556/john-j-kelley-v-raymond-j-dunne-two-cases-elizabeth-ann-kelley-v/" aria-description="Citation for case: John J. Kelley v. Raymond J. Dunne, (Two Cases)....">344 F. 2d 129</a></span> (CA1 1965); and <i>United States</i> v. <i>Bell,</i> <span class="citation" data-id="8769475"><a href="/opinion/8785630/united-states-v-bell/" aria-description="Citation for case: United States v. Bell">294 F. Supp. 1314</a></span> (ND Ill. 1968). The Court of Appeals for the Ninth Circuit held, however, that § 3523 (a) (2) (K) did not give the necessary express power to arrest, but that a warrantless arrest by a postal inspector could be upheld by resort to a citizen's power to arrest. <i>United States</i> v. <i>DeCatur,</i> <span class="citation" data-id="291586"><a href="/opinion/291586/united-states-v-arthur-ronald-decatur/" aria-description="Citation for case: United States v. Arthur Ronald Decatur">430 F. 2d 365</a></span> (1970); <i>Neggo</i> v. <i>United States,</i> <span class="citation" data-id="279069"><a href="/opinion/279069/rein-neggo-jr-v-united-states/" aria-description="Citation for case: Rein Neggo, Jr. v. United States">390 F. 2d 609</a></span> (1968); <i>Ward</i> v. <i>United States,</i> <span class="citation" data-id="260271"><a href="/opinion/260271/james-vernon-ward-v-united-states/" aria-description="Citation for case: James Vernon Ward v. United States">316 F. 2d 113</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./375/862/">375 U. S. 862</a></span> (1963).
</p>
<p>In 1968 in the face of confusion generated by these decisions and two others striking down warrantless arrests by postal inspectors as not authorized by federal statute or by state law, <i>Alexander</i> v. <i>United States,</i> <span class="citation" data-id="278957"><a href="/opinion/278957/rodney-leon-alexander-v-united-states/" aria-description="Citation for case: Rodney Leon Alexander v. United States">390 F. 2d 101</a></span> (CA5 1968); <i>United States</i> v. <i>Moderacki,</i> <span class="citation" data-id="1607433"><a href="/opinion/1607433/united-states-v-moderacki/" aria-description="Citation for case: United States v. Moderacki">280 F. Supp. 633</a></span> (Del. 1968), the Congress enacted <span class="citation no-link">18 U. S. C. § 3061</span> to make clear that postal inspectors are empowered to arrest without warrant upon probable cause. <span class="citation no-link">Pub. L. 90-560, § 5</span> (a), <span class="citation no-link">82 Stat. 998</span>; H. R. Conf. Rep. No. 1918, 90th Cong., 2d Sess., 6 (1968); H. R. Rep. No. 1725, 90th Cong., 2d Sess. (1968); 114 Cong. Rec. 20914-20915, 26928, 28864-28865 (1968).</p>
<p>[5]  There are other federal officers subject to a more restrictive statutory standard. See, <i>e. g.,</i> <span class="citation no-link">18 U. S. C. § 3050</span>, with respect to employees of the Bureau of Prisons.</p>
<p>[6]  In the case before us the Court of Appeals relied heavily, but mistakenly, on <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#480" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 480-481</a></span> (1971), for as we noted in <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 113</a></span> n. 13, the still unsettled question posed in that part of the <i><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span></i> opinion was "whether and under what circumstances an officer may enter a suspect's home to make a warrantless arrest." Watson's midday public arrest does not present that question.
</p>
<p>In its proposed Model Code of Pre-arraignment Procedure, the American Law Institute has addressed the question and recommends that an officer who is empowered to make an arrest and has probable cause to believe the person to be arrested is on private premises be authorized to demand entry to such premises and thereupon to enter to make an arrest. ALI, Model Code of Pre-arraignment Procedure § 120.6 (1) (1975). In certain cases of necessity, however, notification and demand are not required. § 120.6 (2). Authority to make nighttime arrests on private premises is restricted to arrests with warrants authorizing nighttime execution and to certain cases of necessity. § 120.6 (3). The commentary states that 24 States (and the District of Columbia) authorize forcible entry whenever there is authority to arrest, six whenever the arrest is under a warrant or for a felony, six whenever the arrest is under a warrant, and two whenever the arrest is for a felony. <i>Id.,</i> at 310, 696-697. Of these jurisdictions all but three have prior-notice requirements for entries to make an arrest similar to those <span class="citation no-link">18 U. S. C. § 3109</span> imposes on entries to execute a search warrant. ALI Model Code, <i>supra,</i> at 310-313.</p>
<p>[7]  As Professor Wilgus observed in his article Arrest Without A Warrant, <span class="citation no-link">22 Mich. L. Rev. 541</span>, 549-550 (1924) (footnote omitted), "[i]t was early argued that similar provisions [to the Fourth Amendment of the Constitution] in state constitutions forbade arrests without a warrant; it was ruled otherwise as to arrests by officers and private persons according to the common law."</p>
<p>[8]  Of equal import is the rule recognized by this Court that even in the absence of a federal statute granting or restricting the authority of federal law enforcement officers, "the law of the state where an arrest without warrant takes place determines its validity." <i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#589" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 589</a></span> (1948). Accord, <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#305" aria-description="Citation for case: Miller v. United States">357 U. S. 301, 305</a></span> (1958); <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, 15 n. 5 (1948); <i>Bad Elk</i> v. <i>United States,</i> <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/#535" aria-description="Citation for case: Bad Elk v. United States">177 U. S. 529, 535</a></span> (1900). This rule is consistent with the express statutory authority of United States marshals discussed in the text, as well as with the Act of Sept. 24, 1789, c. 20, § 33, <span class="citation no-link">1 Stat. 91</span>, providing that for any offense against the United States the offender may be arrested by any judge or justice of the United States "agreeably to the usual mode of process against offenders in such state" as he might be found. See <i>United States</i> v. <i>Di Re, supra,</i> at 589 n. 8.</p>
<p>[9]  Act of Feb. 28, 1795, c. 36, § 9, <span class="citation no-link">1 Stat. 425</span>; Act of July 29, 1861, c. 25, § 7, <span class="citation no-link">12 Stat. 282</span>; Rev. Stat. § 788 (1874); Judicial Code of 1948, § 549, <span class="citation no-link">62 Stat. 912</span>.</p>
<p>[10]  Act of June 15, 1935, c. 259, § 2, <span class="citation no-link">49 Stat. 378</span>.</p>
<p>[11]  Section 120.1 of the Model Code provides, in pertinent part:
</p>
<p>"(1) <i>Authority to Arrest Without a Warrant.</i> A law enforcement officer may arrest a person without a warrant if the officer has reasonable cause to believe that such person has committed</p>
<p>"(a) a felony;</p>
<p>"(b) a misdemeanor, and the officer has reasonable cause to believe that such person</p>
<p>"(i) will not be apprehended unless immediately arrested; or</p>
<p>"(ii) may cause injury to himself or others or damage to property unless immediately arrested; or</p>
<p>"(c) a misdemeanor or petty misdemeanor in the officer's presence."</p>
<p>[12]  <i>Id.,</i> at 289 (footnote omitted). The commentary goes on to say with respect to § 120.1:
</p>
<p>"This Section does not require an officer to arrest under a warrant even if a reasonable opportunity to obtain a warrant exists. As to arrests on the street such a requirement would be entirely novel. Moreover the need for it is not urgent, and the subsequent inquiry such a requirement would authorize would be indeterminate and difficult." <i>Id.,</i> at 303 (footnotes omitted).</p>
<p>As the commentary notes, <i>id.,</i> at 289 n. 1, a statute in the State of Georgia is more restrictive of the arrest power than the general standard. <span class="citation no-link">Ga. Code Ann. § 27-207</span> (a) (Supp. 1975). See also <span class="citation no-link">Colo. Rev. Stat. Ann. § 16-3-102</span> (1973), which provides that an arrest warrant should be obtained "when practicable," and Mont. Rev. Codes Ann. § 95-608 (d) (1969) which authorizes a warrantless arrest if "existing circumstances require" it. A North Carolina statute, N. C. Gen. Stat. § 15-41 (1965), similar to the Georgia statute, was replaced in 1975 by a provision permitting warrantless felony arrests on probable cause. N. C. Gen. Stat. § 15A-401 (b) (2) (1975).</p>
<p>[13]  Until 1951, <span class="citation no-link">18 U. S. C. § 3052</span> conditioned the warrantless arrest powers of the agents of the Federal Bureau of Investigation on there being reasonable grounds to believe that the person would escape before a warrant could be obtained. The Act of Jan. 10, 1951, c. 1221, § 1, <span class="citation no-link">64 Stat. 1239</span>, eliminated this condition. The House Report explained the purpose of the amendment, H. R. Rep. No. 3228, 81st Cong., 2d Sess., 1-2 (1950), and the amendment was given effect by the courts in accordance with its terms. Compare <i>United States</i> v. <i>Coplon,</i> <span class="citation" data-id="226125"><a href="/opinion/226125/united-states-v-coplon/#633" aria-description="Citation for case: United States v. Coplon">185 F. 2d 629, 633-636</a></span> (CA2 1950), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./342/920/">342 U. S. 920</a></span> (1952), with <i>Coplon</i> v. <i>United States,</i> 89 U. S. App. D. C. 103, 108-109, <span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/#753" aria-description="Citation for case: Coplon v. United States (Two Cases)">191 F. 2d 749, 753-754</a></span> (1951), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./342/926/">342 U. S. 926</a></span> (1952).</p>
<p>[14]  On the contrary, the inspector making the arrest in this case had arrested Watson in 1971 for mail theft. Those charges were dropped when Watson cooperated with the prosecution. During the ensuing two years he also furnished information to the authorities.</p>
<p>[1]  None of the decisions cited by the Court today squarely faced the issue. In <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span> (1959), for example, the Court declared that <span class="citation no-link">18 U. S. C. § 3052</span>, which authorizes an FBI agent to make a warrantless arrest when he has reasonable grounds to believe that a person has committed a felony, "states the constitutional standard." <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#100" aria-description="Citation for case: Henry v. United States">361 U. S., at 100</a></span>. But that declaration was made without discussion, and the issue actually presented to and addressed by the Court was whether there was in fact probable cause for the arrest in that case. Similarly, <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959), stands only for the validity of a warrantless arrest made with probable cause to believe that the arrestee had committed an offense in the arresting officer's presence. See <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#313" aria-description="Citation for case: Draper v. United States"><i>id.,</i> at 313</a></span>. As this Court had noted in an earlier case, such an arrest presents no danger that an innocent person might be ensnared, since the officer observes both the crime and the culprit with his own eyes; there thus would be no reason to require a warrant in that particular situation even if there might be in others. <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/#705" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699, 705</a></span> (1948). Another case cited by the Court, <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), involved no challenge to an arrest. Nor did <i>Abel</i> v. <i>United States,</i> <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U. S. 217</a></span> (1960), in which the Court refused to consider petitioner's challenge to his arrest under less than a judicial warrant because of his failure to raise the issue in the lower courts. See <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#230" aria-description="Citation for case: Abel v. United States"><i>id.,</i> at 230-232</a></span>. Finally, in <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963), the Court addressed only the questions of whether there was probable cause for arrest and whether the method of entry for the purpose of arrest was reasonable; no issue arose as to whether a warrant was necessary for either the arrest or the entry.</p>
<p>[2]  Act of May 2, 1792, c. 18, § 9, <span class="citation no-link">1 Stat. 265</span>; see <span class="citation no-link">28 U. S. C. § 570</span>.</p>
<p>[3]  Respondent has cited no other decision, state or federal, in support of the Court of Appeals' result in this case. The Government stated in its petition that the decision below was the first of which it was aware that required a warrant for an arrest in a public place. The Court of Appeals relied upon part of this Court's discussion in <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#480" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 480-481</a></span> (1971), but as other courts have recognized that discussion had nothing to do with warrantless arrests in public places. See, <i>e. g., </i><i>United States</i> v. <i>Miles,</i> <span class="citation" data-id="306113"><a href="/opinion/306113/united-states-v-jerry-edgar-miles-appeal-of-george-kirby/#486" aria-description="Citation for case: United States v. Jerry Edgar Miles Appeal of George Kirby">468 F. 2d 482, 486-487</a></span>, and n. 6 (CA3 1972); <i>United States</i> v. <i>Bazinet,</i> <span class="citation" data-id="304301"><a href="/opinion/304301/the-united-states-v-michael-bazinet-the-united-states-v-george-knox/#987" aria-description="Citation for case: The United States v. Michael Bazinet, the United States...">462 F. 2d 982, 987</a></span> (CA8), cert. denied <i>sub nom. Knox</i> v. <i>United States,</i> <span class="citation" data-id="8982985"><a href="/opinion/8990812/knox-v-united-states/" aria-description="Citation for case: Knox v. United States">409 U. S. 1010</a></span> (1972).</p>
<p>[4]  This Court has not attempted a more precise definition of probable cause than the one in <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#161" aria-description="Citation for case: Carroll v. United States">267 U. S., at 161</a></span>, where the standard was affirmed as "facts and circumstances. . . such as to warrant a man of [reasonable] prudence and caution in believing that the offense has been committed" and, of course, that the person to be arrested was the offender. See generally <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#100" aria-description="Citation for case: Henry v. United States">361 U. S., at 100-102</a></span>. Whatever evidence may be necessary to establish probable cause in a given case, however, it is clear that it never need rise to the level required to prove guilt beyond a reasonable doubt. <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#102" aria-description="Citation for case: Henry v. United States"><i>Id.,</i> at 102</a></span>; <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#311" aria-description="Citation for case: Draper v. United States">358 U. S., at 311-312</a></span>, and n. 4. The different standards for arrest and conviction reflect a recognition of society's valid interest in the earliest detention of suspected criminals that is consistent with the individual's interest in freedom from arbitrary interference with his liberty. See <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span> (1949). But society's equally valid interest in ultimate conviction of the guilty requires the police sometimes to continue their investigation after establishing probable cause to arrest, even if doing so means they have to leave a suspect at large pending such investigation. See generally ALI, A Model Code of Pre-arraignment Procedure § 120.1, Commentary, pp. 289, 292-296 (1975).</p>
<p>[5]  The probable cause to support issuance of an arrest warrant normally would not grow stale as easily as that which supports a warrant to search a particular place for particular objects. This is true because once there is probable cause to believe that someone is a felon the passage of time often will bring new supporting evidence. But in some cases the original grounds supporting the warrant could be disproved by subsequent investigation that at the same time turns up wholly new evidence supporting probable cause on a different theory. In those cases the warrant could be stale because based upon discredited information.</p>
<p>[6]  I do not understand today's decision to suggest any retreat from our longstanding position that such an arrest should receive careful judicial scrutiny if challenged. "An arrest without a warrant bypasses the safeguards provided by an objective determination of probable cause, and substitutes instead the far less reliable procedure of an after-the-event justification for the arrest . . . , too likely to be subtly influenced by the familiar shortcomings of hindsight judgment." <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 96</a></span> (1964).</p>
<p>[7]  Compare <i>Dorman</i> v. <i>United States,</i> 140 U. S. App. D. C. 313, 318-319, <span class="citation" data-id="9456306"><a href="/opinion/293653/harold-b-dorman-v-united-states/#390" aria-description="Citation for case: Harold B. Dorman v. United States">435 F. 2d 385, 390-391</a></span> (1970) (en banc) (warrant required, absent exigent circumstances, for entry into a suspect's home for purpose of arrest), with <i>People</i> v. <i>Eddington,</i> <span class="citation" data-id="1939307"><a href="/opinion/1939307/people-v-eddington/" aria-description="Citation for case: People v. Eddington">23 Mich. App. 210</a></span>, <span class="citation" data-id="1939307"><a href="/opinion/1939307/people-v-eddington/" aria-description="Citation for case: People v. Eddington">178 N. W. 2d 686</a></span> (1970), aff'd, <span class="citation" data-id="9704090"><a href="/opinion/1978640/people-v-eddington/" aria-description="Citation for case: People v. Eddington">387 Mich. 551</a></span>, <span class="citation" data-id="9704090"><a href="/opinion/1978640/people-v-eddington/" aria-description="Citation for case: People v. Eddington">198 N. W. 2d 297</a></span> (1972) (only probable cause to arrest needed to enter suspect's home if there is a reasonable belief that he is there). Compare <i>England</i> v. <i>State,</i> <span class="citation" data-id="2614205"><a href="/opinion/2614205/england-v-state/" aria-description="Citation for case: England v. State">488 P. 2d 1347</a></span> (Okla. Crim. 1971) (search warrant needed to enter residence of third party to arrest suspect), with <i>United States</i> v. <i>Brown,</i> 151 U. S. App. D. C. 365, 369, <span class="citation" data-id="305803"><a href="/opinion/305803/united-states-v-roland-w-brown/#423" aria-description="Citation for case: United States v. Roland W. Brown">467 F. 2d 419, 423</a></span> (1972) (only an arrest warrant, plus reasonable belief that the suspect is present, necessary to support entry onto third party's premises).</p>
<p>[1]  The Court of Appeals did not recognize this independent probable cause to arrest petitioner, perhaps because one of the arresting officers testified that the arrest was made for the earlier, rather than the contemporaneous, offense. App. 23-24. That testimony should not limit the inquiry into contemporaneous probable cause. Where the good faith of the arresting officers is not at issue, and where the crime for which a suspect is arrested and that for which the officers have probable cause are closely related, courts typically use an objective rather than subjective measure of probable cause. <i>Ramirez</i> v. <i>Rodriguez,</i> <span class="citation" data-id="305873"><a href="/opinion/305873/henry-ramirez-v-felix-rodriguez-warden/" aria-description="Citation for case: Henry Ramirez v. Felix Rodriguez, Warden">467 F. 2d 822</a></span> (CA10 1972); <i>United States</i> v. <i>Martinez,</i> <span class="citation" data-id="305071"><a href="/opinion/305071/united-states-v-nestor-martinez/" aria-description="Citation for case: United States v. Nestor Martinez">465 F. 2d 79</a></span> (CA2 1972); <i>United States</i> v. <i>Atkinson,</i> <span class="citation" data-id="9457517"><a href="/opinion/299839/united-states-v-james-william-atkinson-aka-walter-j-atkinson/#838" aria-description="Citation for case: United States v. James William Atkinson, A/K/A Walter J....">450 F. 2d 835, 838</a></span> (CA5 1971). Since the objective facts demonstrably show probable cause as to the contemporaneous offense as well as the earlier offense, Watson's arrest is properly justified by reference to those facts.</p>
<p>[2]  W. Shakespeare, Hamlet, act iii, sc. 1, line 142.</p>
<p>[3]  Nunnery was Elizabethan slang for house of prostitution. 7 Oxford English Dictionary 264 (1933).</p>
<p>[4]  Professor Wilgus has defined felonies at common law as
</p>
<p>"those bootless crimes, prosecuted by an appeal with an offer of trial by battle, the felon's lands to go to his lord or the king, his chattels confiscated, and life and members forfeited, if guilty, and if he fled he became an outlaw . . . ." Wilgus, Arrest Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 541</span>, 569 (1924).</p>
<p>[5]  In the States the most common rule is that any crime punishable by death or imprisonment in the state prison is a felony. See <i>id.,</i> at 571. See also, <i>e. g.,</i> Ark. Stat. Ann. § 41-103 (1964); 22 <span class="citation no-link">Fla. Stat. Ann. § 775.08</span> (Supp. 1975); Ill. Ann. Stat. § 2-7 (Supp. 1975); <span class="citation no-link">Ky. Rev. Stat. Ann. § 431.060</span> (1970); Mass. Gen. Laws Ann., c. 274, § 1 (1970); Okla. Stat. Ann., Tit. 21, § 5 (1958); <span class="citation no-link">Wash. Rev. Code § 9.01.020</span> (1974).</p>
<p>[6]  "In England at the common law the difference in punishment between felonies and misdemeanors was very great. Under our present federal statutes, it is much less important and Congress may exercise a relatively wide discretion in classing particular offenses as felonies or misdemeanors." <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S., at 158</a></span>.</p>
<p>[7]  Indeed, by statute, it was no more than a high misdemeanor wilfully to discharge or attempt to discharge a pistol at or near the King of England. 9 Halsbury's Laws of <span class="citation" data-id="2614205"><a href="/opinion/2614205/england-v-state/#459" aria-description="Citation for case: England v. State">England 459</a></span> (1909). Cf. <span class="citation no-link">18 U. S. C. § 871</span> (felony to make threats against President of United States); § 1751 (felony to assault President of United States).</p>
<p>[8]  This exception was essentially a narrowly drawn exigent-circumstances exception. See <i>Carroll</i> v. <i>United States, supra,</i> at 157.</p>
<p>[9]  For example, under federal law these are some of the commonlaw misdemeanors, or their modern equivalents, now considered felonies: assault, <span class="citation no-link">18 U. S. C. §§ 111-112</span>; assault with intent to commit murder, rape or any other felony, § 113; forging securities of the United States, § 471; bribing voters, § 597; escape, § 751; kidnaping, § 1201; obstruction 

[...TRUNCATED 16711 of 136711 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/Vernonia School District 47J v. Acton.md  (`case`, 5 assertions)

### content_page

```
---
title: "Vernonia School District 47J v. Acton"
type: case
citation: "515 U.S. 646 (1995)"
parallel_cite: "115 S. Ct. 2386; 132 L. Ed. 2d 564"
neutral_cite: 1995 U.S. LEXIS 4275
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1995
date_decided: 1995-06-26
docket: 94-590
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1995-06-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Vernonia School District 47J v. Acton
  varies_by_point: false
  scope_note: "Extended to non-athlete competitive extracurriculars by Board of Education v. Earls (2002); good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/117964/vernonia-school-district-47j-v-acton/"
  cluster_id: 117964
  opinion_id: 9433198
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Anchor"
related: ["[[Board of Education v. Earls]]", "[[New Jersey v. T.L.O.]]", "[[Skinner v. Railway Labor Executives' Ass'n]]", "[[National Treasury Employees Union v. Von Raab]]"]
aliases: ["Vernonia v. Acton", "Acton"]
tags: ["case", "fourth-amendment", "special-needs", "drug-testing", "schools", "student-athletes"]
holding: "Suspicionless random drug testing of public-school student athletes is reasonable under the special-needs doctrine, given athletes'…"
lake:
  record_id: Vernonia School District 47J v. Acton
  status: verified
  projected_at: 2026-07-09
---

# Vernonia School District 47J v. Acton

*515 U.S. 646 (1995)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Faced with a sharp rise in student drug use led by the school's athletes, the Vernonia, Oregon school district adopted a Student Athlete Drug Policy conditioning participation in interscholastic sports on consent to suspicionless urinalysis — a test at the start of each season plus random weekly testing during the season. Seventh grader James Acton was denied a spot on the football team after he and his parents refused to sign the consent forms. The Actons sued, claiming the policy violated the Fourth Amendment.

## Issue
Whether a public school district's policy of random, suspicionless urinalysis drug testing of student athletes is a reasonable search under the Fourth Amendment.

## Rule
State-compelled urinalysis is a search, and "the ultimate measure of the constitutionality of a governmental search is 'reasonableness'" — judged, where there was no clear founding-era practice, by "balancing its intrusion on the individual's Fourth Amendment interests against its promotion of legitimate governmental interests." — 515 U.S. at 652–653. ^pin-652

A school search may proceed without individualized suspicion under the "special needs" doctrine, and the relevant privacy expectation is reduced in the school setting and reduced further for athletes: "Legitimate privacy expectations are even less with regard to student athletes." — [*Id.* at 657](https://www.courtlistener.com/opinion/117964/vernonia-school-district-47j-v-acton/#:~:text=%E2%80%9Cwhen-,special%20needs). ^pin-657

Weighing "the decreased expectation of privacy, the relative unobtrusiveness of the search, and the severity of the need met by the search," the Court held: "we conclude Vernonia's Policy is reasonable and hence constitutional." — *Id.* at 664–665. ^pin-665

## Application
On these facts the three factors favored the District. Student athletes have a decreased expectation of privacy: schoolchildren are already subject to physical exams and vaccinations, athletes dress and shower communally, and by "going out for the team" they voluntarily accept added regulation. The character of the intrusion was negligible — male students produced samples at a urinal observed only from behind, female students in an enclosed stall with a monitor listening for tampering, and results were screened only for drugs and disclosed to a limited set of school personnel, not law enforcement. And the governmental concern was immediate and important: deterring drug use among the very students leading a drug epidemic, with athletes at heightened physical risk. Balancing those factors, the random-testing policy was reasonable.

## Conclusion
The Policy was a reasonable search; the judgment of the Ninth Circuit invalidating it was reversed. The Court cautioned that its holding did not mean suspicionless testing would "readily pass constitutional muster in other contexts."

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Vernonia* was **extended** by [[Board of Education v. Earls]] (2002), which upheld suspicionless testing of students in all competitive extracurricular activities, not just athletics. It builds on the school-search framework of [[New Jersey v. T.L.O.]] and the drug-testing balancing of [[Skinner v. Railway Labor Executives' Ass'n]] and [[National Treasury Employees Union v. Von Raab]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Anchor*

## Sources
- *Vernonia School District 47J v. Acton*, 515 U.S. 646 (1995) — https://www.courtlistener.com/opinion/117964/vernonia-school-district-47j-v-acton/ — pinpoints: 652–653, 657, 664–665.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "bf77a65e022570ef", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "515 U.S. 646 (1995)", "court": "U.S. Supreme Court", "neutral_cite": "1995 U.S. LEXIS 4275", "official_citation_present": true, "parallel_cite": "115 S. Ct. 2386; 132 L. Ed. 2d 564", "title": "Vernonia School District 47J v. Acton", "year": "1995"}}
{"assertion_id": "40c7563c884ef5da", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Suspicionless random drug testing of public-school student athletes is reasonable under the special-needs doctrine, given athletes'…", "title": "Vernonia School District 47J v. Acton"}}
{"assertion_id": "47e3145d9669f63f", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Key — Anchor", "title": "Vernonia School District 47J v. Acton"}}
{"assertion_id": "749d58331f8df6da", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1995-06-26", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Vernonia School District 47J v. Acton", "field_i_validity": "good_law", "scope_note": "Extended to non-athlete competitive extracurriculars by Board of Education v. Earls (2002); good law.", "title": "Vernonia School District 47J v. Acton", "varies_by_point": "false"}}
{"assertion_id": "dd36d629b0002f40", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Vernonia School District 47J v. Acton"}}
```

### lake record — Vernonia School District 47J v. Acton

```json
{
  "schema_version": "s2.v1",
  "record_id": "Vernonia School District 47J v. Acton",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Vernonia School District 47J v. Acton",
    "case_name_short": "Acton",
    "case_name_full": "VERNONIA SCHOOL DISTRICT 47J v. ACTON Et Ux., Guardians Ad Litem for ACTON",
    "input_case_name": "Vernonia School District 47J v. Acton",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1995-06-26",
    "year": 1995,
    "docket": "94-590",
    "cluster_id": 117964,
    "lead_opinion_id": 9433198,
    "sibling_ids": [
      117964,
      9433198,
      9433199,
      9433200
    ],
    "absolute_url": "/opinion/117964/vernonia-school-district-47j-v-acton/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "515 U.S. 646",
      "volume": "515",
      "reporter": "U.S.",
      "page": "646",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "115 S. Ct. 2386",
        "volume": "115",
        "reporter": "S. Ct.",
        "page": "2386",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "132 L. Ed. 2d 564",
        "volume": "132",
        "reporter": "L. Ed. 2d",
        "page": "564",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1995 U.S. LEXIS 4275",
        "volume": "1995",
        "reporter": "U.S. LEXIS",
        "page": "4275",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "515 U.S. 646",
        "volume": "515",
        "reporter": "U.S.",
        "page": "646",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "115 S. Ct. 2386",
        "volume": "115",
        "reporter": "S. Ct.",
        "page": "2386",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "132 L. Ed. 2d 564",
        "volume": "132",
        "reporter": "L. Ed. 2d",
        "page": "564",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1995 U.S. LEXIS 4275",
        "volume": "1995",
        "reporter": "U.S. LEXIS",
        "page": "4275",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "515 U.S. 646",
    "official_selection": {
      "court_class": "scotus",
      "selected": "515 U.S. 646",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-652",
      "page": null,
      "quote": "--- # Vernonia School District 47J v. Acton *515 U.S. 646 (1995)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Faced with a sharp rise in student drug use led by the school's athletes, the Vernonia, Oregon school district adopted a Student Athlete Drug Policy conditioning participation in interscholastic sports on consent to suspicionless urinalysis \u2014 a test at the start of each season plus random weekly testing during the season. Seventh grader James Acton was denied a spot on the football team after he and his parents refused to sign the consent forms. The Actons sued, claiming the policy violated the Fourth Amendment. ## Issue Whether a public school district's policy of random, suspicionless urinalysis drug testing of student athletes is a reasonable search under the Fourth Amendment. ## Rule State-compelled urinalysis is a search, and",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-657",
      "page": null,
      "quote": "special needs",
      "star_marker": "653",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 12646,
      "fragment": "#:~:text=%E2%80%9Cwhen-,special%20needs",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-665",
      "page": null,
      "quote": "the decreased expectation of privacy, the relative unobtrusiveness of the search, and the severity of the need met by the search,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1995-06-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Vernonia School District 47J v. Acton",
    "varies_by_point": false,
    "scope_note": "Extended to non-athlete competitive extracurriculars by Board of Education v. Earls (2002); good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Moore v. Portland Public Schools",
          "cluster_id": 10143838,
          "cite": [
            "328 Or. App. 391"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Strudwick",
          "cluster_id": 10018712,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Strudwick",
          "cluster_id": 5293509,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hilton",
          "cluster_id": 10018723,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hilton",
          "cluster_id": 5144554,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Ryan Mark Thompson",
          "cluster_id": 4311783,
          "cite": [
            "886 N.W.2d 224",
            "2016 Minn. LEXIS 656"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sarah Beth Keller",
          "cluster_id": 4247956,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Blue",
          "cluster_id": 3185413,
          "cite": [
            "783 S.E.2d 524",
            "246 N.C. App. 259",
            "2016 N.C. App. LEXIS 293"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Morris",
          "cluster_id": 3185407,
          "cite": [
            "783 S.E.2d 528",
            "246 N.C. App. 349",
            "2016 N.C. App. LEXIS 291"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis Ex Rel. LaShonda D. v. Monroe County Board of Education",
          "cluster_id": 118290,
          "cite": [
            "143 L. Ed. 2d 839",
            "119 S. Ct. 1661",
            "526 U.S. 629",
            "1999 U.S. LEXIS 3452",
            "12 Fla. L. Weekly Fed. S 280",
            "67 U.S.L.W. 4329",
            "1999 Colo. J. C.A.R. 2948",
            "99 Cal. Daily Op. Serv. 3861",
            "99 Daily Journal DAR 4931"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. King",
          "cluster_id": 873669,
          "cite": [
            "186 L. Ed. 2d 1",
            "133 S. Ct. 1958",
            "2013 U.S. LEXIS 4165",
            "569 U.S. 435",
            "24 Fla. L. Weekly Fed. S 234",
            "81 U.S.L.W. 4343",
            "2013 WL 2371466"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brittany Morrow v. Barry Balaski",
          "cluster_id": 891221,
          "cite": [
            "719 F.3d 160",
            "98 A.L.R. 6th 777",
            "2013 WL 2466892",
            "2013 U.S. App. LEXIS 11246"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hedges v. Musco",
          "cluster_id": 767706,
          "cite": [
            "204 F.3d 109",
            "2000 U.S. App. LEXIS 2671"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe Ex Rel. Magee v. Covington County School District",
          "cluster_id": 626050,
          "cite": [
            "675 F.3d 849",
            "2012 U.S. App. LEXIS 6080",
            "2012 WL 976349"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chandler v. Miller",
          "cluster_id": 118100,
          "cite": [
            "137 L. Ed. 2d 513",
            "117 S. Ct. 1295",
            "520 U.S. 305",
            "1997 U.S. LEXIS 2505"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ferguson v. City of Charleston",
          "cluster_id": 118414,
          "cite": [
            "149 L. Ed. 2d 205",
            "121 S. Ct. 1281",
            "532 U.S. 67",
            "2001 U.S. LEXIS 2460",
            "2001 Daily Journal DAR 2839",
            "2001 Colo. J. C.A.R. 1427",
            "14 Fla. L. Weekly Fed. S 152",
            "69 U.S.L.W. 4184"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of Education of Independent School District No. 92 of Pottawatomie County v. Earls",
          "cluster_id": 121171,
          "cite": [
            "153 L. Ed. 2d 735",
            "122 S. Ct. 2559",
            "536 U.S. 822",
            "2002 U.S. LEXIS 4882",
            "2002 Cal. Daily Op. Serv. 5761",
            "2002 Daily Journal DAR 7275",
            "70 U.S.L.W. 4737",
            "15 Fla. L. Weekly Fed. S 483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tenenbaum v. Williams",
          "cluster_id": 7079141,
          "cite": [
            "193 F.3d 581",
            "1999 WL 822538"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gates v. Texas Deparment of Protective & Regulatory Services",
          "cluster_id": 62905,
          "cite": [
            "537 F.3d 404",
            "2008 WL 2875378"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gonzalez v. City of Schenectady",
          "cluster_id": 1038554,
          "cite": [
            "728 F.3d 149",
            "2013 U.S. App. LEXIS 17943",
            "2013 WL 4528864"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Snider",
          "cluster_id": 1746280,
          "cite": [
            "608 N.W.2d 502",
            "239 Mich. App. 393"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(117964 OR 9433198 OR 9433199 OR 9433200) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzkyOTQwODAwMDAwJnM9MjY1NDAxOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28117964+OR+9433198+OR+9433199+OR+9433200%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 12,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 12,
        "triage_snippet_classified": 188
      },
      "lane2_top_cited": {
        "query": "cites:(117964 OR 9433198 OR 9433199 OR 9433200)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjYmcz03MDY5NTAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28117964+OR+9433198+OR+9433199+OR+9433200%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(117964 OR 9433198 OR 9433199 OR 9433200)",
        "reviewed": 34,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 34,
        "triage_read": 1,
        "triage_snippet_classified": 33
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(117964 OR 9433198 OR 9433199 OR 9433200)",
    "indexed_citing_opinions": 895,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 117964,
        "count": 778,
        "count_source": "search"
      },
      {
        "opinion_id": 9433198,
        "count": 129,
        "count_source": "search"
      },
      {
        "opinion_id": 9433199,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433200,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1472,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/vernonia-school-district-47j-v-acton.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4MTA0Mzkmcz05NTA1OTgzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28117964+OR+9433198+OR+9433199+OR+9433200%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 117964,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 107841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 109136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 109635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 111754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 111834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 111835,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 111927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 111979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 112202,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 112220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 112459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 319945,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 669794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 1559138,
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
    "date_created": "2026-07-06T03:50:22Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:50:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:50:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:53:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:50:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Vernonia School District 47J v. Acton

```
<opinion type="majority">
<author id="b694-9">Justice Scalia</author>
<p id="AIZ">delivered the opinion of the Court.</p>
<p id="b694-10">The Student Athlete Drug Policy adopted by School District 47J in the town of Vernonia, Oregon, authorizes random urinalysis drug testing of students who participate in the District’s school athletics programs. We granted certiorari to decide whether this violates the Fourth and Fourteenth Amendments to the United States Constitution.</p>
<p id="AR7">I</p>
<p id="b694-3">A</p>
<p id="b694-4">Petitioner Vernonia School District 47J (District) operates one high school and three grade schools in the logging community of Vernonia, Oregon. As elsewhere in small-town America, school sports play a prominent role in the town’s life, and student athletes are admired in their schools and in the community.</p>
<p id="b694-5">Drugs had not been a major problem in Vernonia schools. In the mid-to-late 1980’s, however, teachers and administrators observed a sharp increase in drug use. Students began to speak out about their attraction to the drug culture, and to boast that there was nothing the school could do about it. Along with more drugs came more disciplinary problems. <page-number citation-index="1" label="649">*649</page-number>Between 1988 and 1989 the number of disciplinary referrals in Vernonia schools rose to more than twice the number reported in the early 1980’s, and several students were suspended. Students became increasingly rude during class; outbursts of profane language became common.</p>
<p id="b695-5">Not only were student athletes included among the drug users but, as the District Court found, athletes were the leaders of the drug culture. <span class="citation" data-id="1559138"><a href="/opinion/1559138/acton-v-vernonia-school-district-47j/#1357" aria-description="Citation for case: Acton v. Vernonia School District 47J">796 F. Supp. 1354, 1357</a></span> (Ore. 1992). This caused the District’s administrators particular concern, since drug use increases the risk of sports-related injury. Expert testimony at the trial confirmed the deleterious effects of drugs on motivation, memory, judgment, reaction, coordination, and performance. The high school football and wrestling coach witnessed a severe sternum injury suffered by a wrestler, and various omissions of safety procedures and misexecutions by football players, all attributable in his belief to the effects of drug use.</p>
<p id="b695-6">Initially, the District responded to the drug problem by offering special classes, speakers, and presentations designed to deter drug use. It even brought in a specially trained dog to detect drugs, but the drug problem persisted. According to the District Court:</p>
<blockquote id="AR5">“[T]he administration was at its wits end and ... a large segment of the student body, particularly those involved in interscholastic athletics, was in a state of rebellion. Disciplinary actions had reached ‘epidemic proportions.’ The coincidence of an almost three-fold increase in classroom disruptions and disciplinary reports along with the staff’s direct observations of students using drugs or glamorizing drug and alcohol use led the administration to the inescapable conclusion that the rebellion was being fueled by alcohol and drug abuse as well as the student’s misperceptions about the drug culture.” <em><span class="citation" data-id="1559138"><a href="/opinion/1559138/acton-v-vernonia-school-district-47j/" aria-description="Citation for case: Acton v. Vernonia School District 47J">Ibid.</a></span></em></blockquote>
<p id="b695-8">At that point, District officials began considering a drug-testing program. They held a parent “input night” to dis<page-number citation-index="1" label="650">*650</page-number>cuss the proposed Student Athlete Drug Policy (Policy), and the parents in attendance gave their unanimous approval. The school board approved the Policy for implementation in the fall of 1989. Its expressed purpose is to prevent student athletes from using drugs, to protect their health and safety, and to provide drug users with assistance programs.</p>
<p id="b696-4">B</p>
<p id="b696-5">The Policy applies to all students participating in interscholastic athletics. Students wishing to play sports must sign a form consenting to the testing and must obtain the written consent of their parents. Athletes are tested at the beginning of the season for their sport. In addition, once each week of the season the names of the athletes are placed in a “pool” from which a student, with the supervision of two adults, blindly draws the names of 10% of the athletes for random testing. Those selected are notified and tested that same day, if possible.</p>
<p id="b696-6">The student to be tested completes a specimen control form which bears an assigned number. Prescription medications that the student is taking must be identified by providing a copy of the prescription or a doctor’s authorization. The student then enters an empty locker room accompanied by an adult monitor of the same sex. Each boy selected produces a sample at a urinal, remaining fully clothed with his back to the monitor, who stands approximately 12 to 15 feet behind the student. Monitors may (though do not always) watch the student while he produces the sample, and they listen for normal sounds of urination. Girls produce samples in an enclosed bathroom stall, so that they can be heard but not observed. After the sample is produced, it is given to the monitor, who checks it for temperature and tampering and then transfers it to a vial.</p>
<p id="b696-7">The samples are sent to an independent laboratory, which routinely tests them for amphetamines, cocaine, and marijuana. Other drugs, such as LSD, may be screened at the <page-number citation-index="1" label="651">*651</page-number>request of the District, but the identity of a particular student does not determine which drugs will be tested. The laboratory’s procedures are 99.94% accurate. The District follows strict procedures regarding the chain of custody and access to test results. The laboratory does not know the identity of the students whose samples it tests. It is authorized to mail written test reports only to the superintendent and to provide test results to District personnel by telephone only after the requesting official recites a code confirming his authority. Only the superintendent, principals, vice-principals, and athletic directors have access to test results, and the results are not kept for more than one year.</p>
<p id="b697-5">If a sample tests positive, a second test is administered as soon as possible to confirm the result. If the second test is negative, no further action is taken. If the second test is positive, the athlete’s parents are notified, and the school principal convenes a meeting with the student and his parents, at which the student is given the option of (1) participating for six weeks in an assistance program that includes weekly urinalysis, or (2) suffering suspension from athletics for the remainder of the current season and the next athletic season. The student is then retested prior to the start of the next athletic season for which he or she is eligible. The Policy states that a second offense results in automatic imposition of option (2); a third offense in suspension for the remainder of the current season and the next two athletic seasons.</p>
<p id="b697-6">C</p>
<p id="b697-7">In the fall of 1991, respondent James Acton, then a seventh grader, signed up to play football at one of the District’s grade schools. He was denied participation, however, because he and his parents refused to sign the testing consent forms. The Actons filed suit, seeking declaratory and in-junctive relief from enforcement of the Policy on the grounds that it violated the Fourth and Fourteenth Amendments to the United States Constitution and Article I, § 9, of the Ore<page-number citation-index="1" label="652">*652</page-number>gon Constitution. After a bench trial, the District Court entered an order denying the claims on the merits and dismissing the action. <span class="citation" data-id="1559138"><a href="/opinion/1559138/acton-v-vernonia-school-district-47j/#1355" aria-description="Citation for case: Acton v. Vernonia School District 47J">796 F. Supp., at 1355</a></span>. The United States Court of Appeals for the Ninth Circuit reversed, holding that the Policy violated both the Fourth and Fourteenth Amendments and Article I, § 9, of the Oregon Constitution. <span class="citation" data-id="9486735"><a href="/opinion/669794/wayne-acton-and-judy-acton-guardians-ad-litem-for-james-acton-v-vernonia/" aria-description="Citation for case: Wayne Acton and Judy Acton, Guardians Ad Litem for James...">23 F. 3d 1514</a></span> (1994). We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./513/1013/">513 U. S. 1013</a></span> (1994).</p>
<p id="b698-5">II</p>
<p id="b698-6">The Fourth Amendment to the United States Constitution provides that the Federal Government shall not violate “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures . . . .” We have held that the Fourteenth Amendment extends this constitutional guarantee to searches and seizures by state officers, <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#213" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 213</a></span> (1960), including public school officials, <em>New Jersey </em>v. <em>T L. </em>O., <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#336" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 336-337</a></span> (1985). In <em>Skinner </em>v. <em>Railway Labor Executives’ Assn., </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#617" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602, 617</a></span> (1989), we held that state-compelled collection and testing of urine, such as that required by the Policy, constitutes a “search” subject to the demands of the Fourth Amendment. See also <em>Treasury Employees </em>v. <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#665" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656, 665</a></span> (1989).</p>
<p id="b698-7">As the text of the Fourth Amendment indicates, the ultimate measure of the constitutionality of a governmental search is “reasonableness.” At least in a case such as this, where there was no clear practice, either approving or disapproving the type of search at issue, at the time the constitutional provision was enacted,<footnotemark>1</footnotemark> whether a particular search meets the reasonableness standard “ ‘is judged by balancing <page-number citation-index="1" label="653">*653</page-number>its intrusion on the individual’s Fourth Amendment interests against its promotion of legitimate governmental interests.’” <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner, supra,</a></span> </em>at 619 (quoting <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654</a></span> (1979)). Where a search is undertaken by law enforcement officials to discover evidence of criminal wrongdoing, this Court has said that reasonableness generally requires the obtaining of a judicial warrant, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#619" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><em>Skinner, supra, </em>at 619</a></span>. Warrants cannot be issued, of course, without the showing of probable cause required by the Warrant Clause. But a warrant is not required to establish the reasonableness of <em>all </em>government searches; and when a warrant is not required (and the Warrant Clause therefore not applicable), probable cause is not invariably required either. A search unsupported by probable cause can be constitutional, we have said, “when special needs, beyond the normal need for law enforcement, make the warrant and probable-cause requirement impracticable.” <em>Griffin </em>v. <em>Wisconsin, </em><span class="citation multiple-matches"><a href="/c/U.%20S./488/868/">488 U. S. 868</a></span>, 873 (1987) (internal quotation marks omitted).</p>
<p id="b699-5">We have found such “special needs” to exist in the public school context. There, the warrant requirement “would unduly interfere with the maintenance of the swift and informal disciplinary procedures [that are] needed,” and “strict adherence to the requirement that searches be based on probable cause” would undercut “the substantial need of teachers and administrators for freedom to maintain order in the schools.” <em>T L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#340" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 340, 341</a></span>. The school search we approved in <em>T L. 0., </em>while not based on probable cause, <em>was </em>based on individualized <em>suspicion </em>of wrongdoing. As we explicitly acknowledged, however, “‘the Fourth Amendment imposes no irreducible requirement of such suspicion,’ ” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#342" aria-description="Citation for case: New Jersey v. T. L. O."><em>id., </em>at 342</a></span>, n. 8 (quoting <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#560" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 560-561</a></span> (1976)). We have upheld sus-picionless searches and seizures to conduct drug testing of railroad personnel involved in train accidents, see <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner, supra;</a></span> </em>to conduct random drug testing of federal customs officers who carry arms or are involved in drug interdiction, <page-number citation-index="1" label="654">*654</page-number>see <em>Von <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Raab, supra;</a></span> </em>and to maintain automobile checkpoints looking for illegal immigrants and contraband, <em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte, supra,</a></span> </em>and drunk drivers, <em>Michigan Dept. of State Police </em>v. <em>Sitz, </em><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S. 444</a></span> (1990).</p>
<p id="b700-7">1 — 1 1 — 1</p>
<p id="b700-3">The first factor to be considered is the nature of the privacy interest upon which the search here at issue intrudes. The Fourth Amendment does not protect all subjective expectations of privacy, but only those that society recognizes as “legitimate.” <em>T L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#338" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 338</a></span>. What expectations are legitimate varies, of course, with context, <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#337" aria-description="Citation for case: New Jersey v. T. L. O."><em>id., </em>at 337</a></span>, depending, for example, upon whether the individual asserting the privacy interest is at home, at work, in a car, or in a public park. In addition, the legitimacy of certain privacy expectations vis-a-vis the State may depend upon the individual’s legal relationship with the State. For example, in <em>Griffin, supra, </em>we held that, although a “probationer’s home, like anyone else’s, is protected by the Fourth Amendment,” the supervisory relationship between probationer and State justifies “a degree of impingement upon [a probationer’s] privacy that would not be constitutional if applied to the public at large.” 483 U. S., at 873, 875. Central, in our view, to the present case is the fact that the subjects of the Policy are (1) children, who (2) have been committed to the temporary custody of the State as schoolmaster.</p>
<p id="b700-4">Traditionally at common law, and still today, unemanci-pated minors lack some of the most fundamental rights of self-determination — including even the right of liberty in its narrow sense, <em>i. e., </em>the right to come and go at will. They are subject, even as to their physical freedom, to the control of their parents or guardians. See 59 Am. Jur. 2d, Parent and Child §10 (1987). When parents place minor children in private schools for their education, the teachers and administrators of those schools stand <em>in loco parentis </em>over the children entrusted to them. In fact, the tutor or schoolmas<page-number citation-index="1" label="655">*655</page-number>ter is the very prototype of that status. As Blackstone describes it, a parent “may . . . delegate part of his parental authority, during his life, to the tutor or schoolmaster of his child; who is then <em>in loco parentis, </em>and has such a portion of the power of the parent committed to his charge, viz. that of restraint and correction, as may be necessary to answer the purposes for which he is employed.” 1 W. Blackstone, Commentaries on the Laws of England 441 (1769).</p>
<p id="b701-5">In <em>I L. O. </em>we rejected the notion that public schools, like private schools, exercise only parental power over their students, which of course is not subject to constitutional constraints. <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#336" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 336</a></span>. Such a view of things, we said, “is not entirely ‘consonant with compulsory education laws/ ” <em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/" aria-description="Citation for case: New Jersey v. T. L. O.">ibid.</a></span> </em>(quoting <em>Ingraham </em>v. <em>Wright, </em><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#662" aria-description="Citation for case: Ingraham v. Wright">430 U. S. 651, 662</a></span> (1977)), and is inconsistent with our prior decisions treating school officials as state actors for purposes of the Due Process and Free Speech Clauses, <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#336" aria-description="Citation for case: New Jersey v. T. L. O."><em>T L. O., supra, </em>at 336</a></span>. But while denying that the State’s power over schoolchildren is formally no more than the delegated power of their parents, <em>T. L. O. </em>did not deny, but indeed emphasized, that the nature of that power is custodial and tutelary, permitting a degree of supervision and control that could not be exercised over free adults. “[A] proper educational environment requires close supervision of schoolchildren, as well as the enforcement of rules against conduct that would be perfectly permissible if undertaken by an adult.” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#339" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 339</a></span>. While we do not, of course, suggest that public schools as a general matter have such a degree of control over children as to give rise to a constitutional “duty to protect,” see <em>DeShaney </em>v. <em>Winnebago County Dept. of Social Servs., </em><span class="citation" data-id="9431570"><a href="/opinion/112202/deshaney-v-winnebago-county-department-of-social-services/#200" aria-description="Citation for case: DeShaney v. Winnebago County Department of Social Services">489 U. S. 189, 200</a></span> (1989), we have acknowledged that for many purposes “school authorities ac[t] <em>in loco parentis,” Bethel School Dist. No. 403 </em>v. <em>Fraser, </em><span class="citation" data-id="9430701"><a href="/opinion/111754/bethel-school-district-no-403-v-fraser/#684" aria-description="Citation for case: Bethel School District No. 403 v. Fraser">478 U. S. 675, 684</a></span> (1986), with the power and indeed the duty to “inculcate the habits and manners of civility,” <span class="citation" data-id="9430701"><a href="/opinion/111754/bethel-school-district-no-403-v-fraser/#681" aria-description="Citation for case: Bethel School District No. 403 v. Fraser"><em>id., </em>at 681</a></span> (internal quotation marks omitted). Thus, while children assuredly do not “shed their constitutional <page-number citation-index="1" label="656">*656</page-number>rights ... at the schoolhouse gate,” <em>Tinker </em>v. <em>Des Moines Independent Community School Dist., </em><span class="citation" data-id="9423907"><a href="/opinion/107841/tinker-v-des-moines-independent-community-school-district/#506" aria-description="Citation for case: Tinker v. Des Moines Independent Community School District">393 U. S. 503, 506</a></span> (1969), the nature of those rights is what is appropriate for children in school. See, <em>e. g., Goss </em>v. <em>Lopez, </em><span class="citation" data-id="9425909"><a href="/opinion/109136/goss-v-lopez/#581" aria-description="Citation for case: Goss v. Lopez">419 U. S. 565, 581-582</a></span> (1975) (due process for a student challenging disciplinary suspension requires only that the teacher “informally discuss the alleged misconduct with the student minutes after it has occurred”); <span class="citation" data-id="9430701"><a href="/opinion/111754/bethel-school-district-no-403-v-fraser/#683" aria-description="Citation for case: Bethel School District No. 403 v. Fraser"><em>Fraser, supra, </em>at 683</a></span> (“[I]t is a highly appropriate function of public school education to prohibit the use of vulgar and offensive terms in public discourse”); <em>Hazelwood School Dist. </em>v. <em>Kuhlmeier, </em><span class="citation" data-id="9431159"><a href="/opinion/111979/hazelwood-school-district-v-kuhlmeier/#273" aria-description="Citation for case: Hazelwood School District v. Kuhlmeier">484 U. S. 260, 273</a></span> (1988) (public school authorities may censor school-sponsored publications, so long as the censorship is “reasonably related to legitimate pedagogical concerns”); <span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#682" aria-description="Citation for case: Ingraham v. Wright"><em>Ingraham, supra, </em>at 682</a></span> (“Imposing additional administrative safeguards [upon corporal punishment]... would ... entail a significant intrusion into an area of primary educational responsibility”).</p>
<p id="b702-5">Fourth Amendment rights, no less than First and Fourteenth Amendment rights, are different in public schools than elsewhere; the “reasonableness” inquiry cannot disregard the schools’ custodial and tutelary responsibility for children. For their own good and that of their classmates, public school children are routinely required to submit to various physical examinations, and to be vaccinated against various diseases. According to the American Academy of Pediatrics, most public schools “provide vision and hearing screening and dental and dermatological checks. . . . Others also mandate scoliosis screening at appropriate grade levels.” Committee on School Health, American Academy of Pediatrics, School Health: A Guide for Health Professionals 2 (1987). In the 1991-1992 school year, all 50 States required public school students to be vaccinated against diphtheria, measles, rubella, and polio. U. S. Dept, of Health &amp; Human Services, Public Health Service, Centers for Disease Control, State Immunization Requirements 1991-1992, p. 1. Particularly with regard to medical examinations and proce<page-number citation-index="1" label="657">*657</page-number>dures, therefore, “students within the school environment have a lesser expectation of privacy than members of the population generally.” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#348" aria-description="Citation for case: New Jersey v. T. L. O."><em>I L. O., supra, </em>at 348</a></span> (Powell, J., concurring).</p>
<p id="b703-5">Legitimate privacy expectations are even less with regard to student athletes. School sports are not for the bashful. They require “suiting up” before each practice or event, and showering and changing afterwards. Public school locker rooms, the usual sites for these activities, are not notable for the privacy they afford. The locker rooms in Vernonia are typical: No individual dressing rooms are provided; shower heads are lined up along a wall, unseparated by any sort of partition or curtain; not even all the toilet stalls have doors. As the United States Court of Appeals for the Seventh Circuit has noted, there is “an element of ‘communal undress’ inherent in athletic participation,” <em>Schaill by Kross </em>v. <em>Tippecanoe County School Corp., </em><span class="citation" data-id="8966879"><a href="/opinion/8975213/schaill-ex-rel-kross-v-tippecanoe-county-school-corp/#1318" aria-description="Citation for case: Schaill ex rel. Kross v. Tippecanoe County School Corp.">864 F. 2d 1309, 1318</a></span> (1988).</p>
<p id="b703-6">There is an additional respect in which school athletes have a reduced expectation of privacy. By choosing to “go out for the team,” they voluntarily subject themselves to a degree of regulation even higher than that imposed on students generally. In Vernonia’s public schools, they must submit to a preseason physical exam (James testified that his included the giving of a urine sample, App. 17), they must acquire adequate insurance coverage or sign an insurance waiver, maintain a minimum grade point average, and comply with any “rules of conduct, dress, training hours and related matters as may be established for each sport by the head coach and athletic director with the principal’s approval.” Record, Exh. 2, p. 30, ¶ 8. Somewhat like adults who choose to participate in a “closely regulated industry,” students who voluntarily participate in school athletics have reason to expect intrusions upon normal rights and privileges, including privacy. See <em>Skinner, </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#627" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 627</a></span>; <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S. 311, 316</a></span> (1972).</p>
<p id="b704-7">
<page-number citation-index="1" label="658">*658</page-number>
<em>&gt;</em>
</p>
<p id="b704-3">Having considered the scope of the legitimate expectation of privacy at issue here, we turn next to the character of the intrusion that is complained of. We recognized in <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span> </em>that collecting the samples for urinalysis intrudes upon “an excretory function traditionally shielded by great privacy.” 489 U. S., at 626. We noted, however, that the degree of intrusion depends upon the manner in which production of the urine sample is monitored. <em>Ibid. </em>Under the District’s Policy, male students produce samples at a urinal along a wall. They remain fully clothed and are only observed from behind, if at all. Female students produce samples in an enclosed stall, with a female monitor standing outside listening only for sounds of tampering. These conditions are nearly identical to those typically encountered in public restrooms, which men, women, and especially schoolchildren use daily. Under such conditions, the privacy interests compromised by the process of obtaining the urine sample are in our view negligible.</p>
<p id="b704-4">The other privacy-invasive aspect of urinalysis is, of course, the information it discloses concerning the state of the subject’s body, and the materials he has ingested. In this regard it is significant that the tests at issue here look only for drugs, and not for whether the student is, for example, epileptic, pregnant, or diabetic. See <em>id., </em>at 617. Moreover, the drugs for which the samples are screened are standard, and do not vary according to the identity of the student. And finally, the results of the tests are disclosed only to a limited class of school personnel who have a need to know; and they are not turned over to law enforcement authorities or used for any internal disciplinary function. <span class="citation" data-id="1559138"><a href="/opinion/1559138/acton-v-vernonia-school-district-47j/#1364" aria-description="Citation for case: Acton v. Vernonia School District 47J">796 F. Supp., at 1364</a></span>; see also <span class="citation" data-id="9486735"><a href="/opinion/669794/wayne-acton-and-judy-acton-guardians-ad-litem-for-james-acton-v-vernonia/#1521" aria-description="Citation for case: Wayne Acton and Judy Acton, Guardians Ad Litem for James...">23 F. 3d, at 1521</a></span>.<footnotemark>2</footnotemark></p>
<p id="b705-3"><page-number citation-index="1" label="659">*659</page-number>Respondents argue, however, that the District’s Policy is in fact more intrusive than this suggests, because it requires the students, if they are to avoid sanctions for a falsely positive test, to identify <em>in advance </em>prescription medications they are taking. We agree that this raises some cause for concern. In <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span>, </em>we flagged as one of the salutary features of the Customs Service drug-testing program the fact that employees were not required to disclose medical information unless they tested positive, and, even then, the information was supplied to a licensed physician rather than to the Government employer. See <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#672" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 672-673, n. 2</a></span>. On the other hand, we have never indicated that requiring advance disclosure of medications is <em>per se </em>unreasonable. Indeed, in <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span> </em>we held that it was not <em>“a </em>significant invasion of privacy.” 489 U. S., at 626, n. 7. It can be argued that, in <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span>, </em>the disclosure went only to the medical personnel taking the sample, and the Government personnel analyzing it, see <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#609" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><em>id., </em>at 609</a></span>, but see <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#610" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><em>id., </em>at 610</a></span> (railroad personnel responsible for forwarding the sample, and presumably accompanying information, to the Government’s testing lab); and that disclosure to teachers and coaches — to persons who personally <em>know </em>the student — is a greater invasion of privacy. Assuming for the sake of argu<page-number citation-index="1" label="660">*660</page-number>ment that both those propositions are true, we do not believe they establish a difference that respondents are entitled to rely on here.</p>
<p id="b706-5">The General Authorization Form that respondents refused to sign, which refusal was the basis for James’s exclusion from the sports program, said only (in relevant part): “I . . . authorize the Vernonia School District to conduct a test on a urine specimen which I provide to test for drugs and/or alcohol use. I also authorize the release of information concerning the results of such a test to the Vernonia School District and to the parents and/or guardians of the student.” App. 10-11. While the practice of the District seems to have been to have a school official take medication information from the student at the time of the test, see <em>id., </em>at 29, 42, that practice is not set forth in, or required by, the Policy, which says simply: “Student athletes who . . . are or have been taking prescription medication must provide verification (either by a copy of the prescription or by doctor’s authorization) prior to being tested.” <em>Id., </em>at 8. It may well be that, if and when James was selected for random testing at a time that he was taking medication, the School District would have permitted him to provide the requested information in a confidential manner — for example, in a sealed envelope delivered to the testing lab. Nothing in the Policy contradicts that, and when respondents choose, in effect, to challenge the Policy on its face, we will not assume the worst. Accordingly, we reach the same conclusion as in <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span>: </em>that the invasion of privacy was not significant.</p>
<p id="b706-6">V</p>
<p id="b706-7">Finally, we turn to consider the nature and immediacy of the governmental concern at issue here, and the efficacy of this means for meeting it. In both <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span> </em>and <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span>, </em>we characterized the government interest motivating the search as “compelling.” <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#628" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><em>Skinner, supra, </em>at 628</a></span> (interest in preventing railway accidents); <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#670" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><em>Von Raab, supra, </em>at 670</a></span> (in<page-number citation-index="1" label="661">*661</page-number>terest in ensuring fitness of customs officials to interdict drugs and handle firearms). Relying on these cases, the District Court held that because the District’s program also called for drug testing in the absence of individualized suspicion, the District “must demonstrate a ‘compelling need’ for the program.” <span class="citation" data-id="1559138"><a href="/opinion/1559138/acton-v-vernonia-school-district-47j/#1368" aria-description="Citation for case: Acton v. Vernonia School District 47J">796 F. Supp., at 1368</a></span>. The Court of Appeals appears to have agreed with this view. See <span class="citation" data-id="9486735"><a href="/opinion/669794/wayne-acton-and-judy-acton-guardians-ad-litem-for-james-acton-v-vernonia/#1526" aria-description="Citation for case: Wayne Acton and Judy Acton, Guardians Ad Litem for James...">23 F. 3d, at 1526</a></span>. It is a mistake, however, to think that the phrase “compelling state interest,” in the Fourth Amendment context, describes a fixed, minimum quantum of governmental concern, so that one can dispose of a case by answering in isolation the question: Is there a compelling state interest here? Rather, the phrase describes an interest that appears <em>important enough </em>to justify the particular search at hand, in light of other factors that show the search to be relatively intrusive upon a genuine expectation of privacy. Whether that relatively high degree of government concern is necessary in this case or not, we think it is met.</p>
<p id="b707-5">That the nature of the concern is important — indeed, perhaps compelling — can hardly be doubted. Deterring drug use by our Nation’s schoolchildren is at least as important as enhancing efficient enforcement of the Nation’s laws against the importation of drugs, which was the governmental concern in <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#668" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><em>Von Raab, supra, </em>at 668</a></span>, or deterring drug use by engineers and trainmen, which was the governmental concern in <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#628" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><em>Skinner, supra, </em>at 628</a></span>. School years are the time when the physical, psychological, and addictive effects of drugs are most severe. “Maturing nervous systems are more critically impaired by intoxicants than mature ones are; childhood losses in learning are lifelong and profound”; “children grow chemically dependent more quickly than adults, and their record of recovery is depressingly poor.” Hawley, The Bumpy Road to Drug-Free Schools, 72 Phi Delta Kap-pan 310, 314 (1990). See also Estroff, Schwartz, &amp; Hoff-mann, Adolescent Cocaine Abuse: Addictive Potential, Behavioral and Psychiatric Effects, 28 Clinical Pediatrics 550 <page-number citation-index="1" label="662">*662</page-number>(Dec. 1989); Kandel, Davies, Karus, &amp; Yamaguchi, The Consequences in Young Adulthood of Adolescent Drug Involvement, 43 Arch. Gen. Psychiatry 746 (Aug. 1986). And of course the effects of a drug-infested school are visited not just upon the users, but upon the entire student body and faculty, as the educational process is disrupted. In the present case, moreover, the necessity for the State to act is magnified by the fact that this evil is being visited not just upon individuals at large, but upon children for whom it has undertaken a special responsibility of care and direction. Finally, it must not be lost sight of that this program is directed more narrowly to drug use by school athletes, where the risk of immediate physical harm to the drug user or those with whom he is playing his sport is particularly high. Apart from psychological effects, which include impairment of judgment, slow reaction time, and a lessening of the perception of pain, the particular drugs screened by the District’s Policy have been demonstrated to pose substantial physical risks to athletes. Amphetamines produce an “artificially induced heart rate increase, [peripheral vasoconstriction, [b]lood pressure increase, and [mjasking of the normal fatigue response,” making them a “very dangerous drug when used during exercise of any type.” Hawkins, Drugs and Other Ingesta: Effects on Athletic Performance, in H. Appenzeller, Managing Sports and Risk Management Strategies 90, 90-91 (1993). Marijuana causes “[ijrregular blood pressure responses during changes in body position,” “[Reduction in the oxygen-carrying capacity of the blood,” and “[ijnhibition of the normal sweating responses resulting in increased body temperature.” <em>Id., </em>at 94. Cocaine produces “[vjasocon-striction[,] [e]levated blood pressure,” and “[possible coronary artery spasms and myocardial infarction.” <em>Ibid.</em></p>
<p id="b708-5">As for the immediacy of the District’s concerns: We are not inclined to question — indeed, we could not possibly find clearly erroneous — the District Court’s conclusion that “a large segment of the student body, particularly those in<page-number citation-index="1" label="663">*663</page-number>volved in interscholastic athletics, was in a state of rebellion,” that “[disciplinary actions had reached ‘epidemic proportions/” and that “the rebellion was being fueled by alcohol and drug abuse as well as by the student’s mispercep-tions about the drug culture.” <span class="citation" data-id="1559138"><a href="/opinion/1559138/acton-v-vernonia-school-district-47j/#1357" aria-description="Citation for case: Acton v. Vernonia School District 47J">796 F. Supp., at 1357</a></span>. That is an immediate crisis of greater proportions than existed in <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span>, </em>where we upheld the Government’s drug-testing program based on findings of drug use by railroad employees nationwide, without proof that a problem existed on the particular railroads whose employees were subject to the test. See <em>Skinner, </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#607" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 607</a></span>. And of much greater proportions than existed in <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span>, </em>where there was no documented history of drug use by any customs officials. See <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#673" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 673</a></span>; <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#683" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><em>id., </em>at 683</a></span> (Scalia, J., dissenting).</p>
<p id="b709-5">As to the efficacy of this means for addressing the problem: It seems to us self-evident that a drug problem largely fueled by the “role model” effect of athletes’ drug use, and of particular danger to athletes, is effectively addressed by making sure that athletes do not use drugs. Respondents argue that a “less intrusive means to the same end” was available, namely, “drug testing on suspicion of drug use.” Brief for Respondents 45-46. We have repeatedly refused to declare that only the “least intrusive” search practicable can be reasonable under the Fourth Amendment. <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#629" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><em>Skinner, supra, </em>at 629, n. 9</a></span> (collecting cases). Respondents’ alternative entails substantial difficulties — if it is indeed practicable at all. It may be impracticable, for one thing, simply because the parents who are willing to accept random drug testing for athletes are not willing to accept accusatory drug testing for all students, which transforms the process into a badge of shame. Respondents’ proposal brings the risk that teachers will impose testing arbitrarily upon troublesome but not drug-likely students. It generates the expense of defending lawsuits that charge such arbitrary imposition, or that simply demand greater process before accusatory drug</p>
<p id="b710-6"><page-number citation-index="1" label="664">*664</page-number>testing is imposed. And not least of all, it adds to the ever-expanding diversionary duties of schoolteachers the new function of spotting and bringing to account drug abuse, a task for which they are ill prepared, and which is not readily compatible with their vocation. Cf. <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner, supra,</a></span> </em>at 628 (quoting <span class="citation no-link">50 Fed. Reg. 31526</span> (1985)) (a drug impaired individual “will seldom display any outward ‘signs detectable by the lay person or, in many cases, even the physician’”); <em>Goss, </em><span class="citation" data-id="9425909"><a href="/opinion/109136/goss-v-lopez/#594" aria-description="Citation for case: Goss v. Lopez">419 U. S., at 594</a></span> (Powell, J., dissenting) (“There is an ongoing relationship, one in which the teacher must occupy many roles — educator, adviser, friend, and, at times, parent-substitute. It is rarely adversary in nature . . .”) (footnote omitted). In many respects, we think, testing based on “suspicion” of drug use would not be better, but worse.<footnotemark>3</footnotemark></p>
<p id="b710-7">
<em>&gt;</em>
</p>
<p id="b710-3">Taking into account all the factors we have considered above — the decreased expectation of privacy, the relative unobtrusiveness of the search, and the severity of the need met <page-number citation-index="1" label="665">*665</page-number>by the search — we conclude Vernonia’s Policy is reasonable and hence constitutional.</p>
<p id="b711-5">We caution against the assumption that suspicionless drug testing will readily pass constitutional muster in other contexts. The most significant element in this case is the first we discussed: that the Policy was undertaken in furtherance of the government’s responsibilities, under a public school system, as guardian and tutor of children entrusted to its care.<footnotemark>4</footnotemark> Just as when the government conducts a search in its capacity as employer (a warrantless search of an absent employee’s desk to obtain an urgently needed file, for example), the relevant question is whether that intrusion upon privacy is one that a reasonable employer might engage in, see <em>O’Connor </em>v. <em>Ortega, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709</a></span> (1987); so also when the government acts as guardian and tutor the relevant question is whether the search is one that a reasonable guardian and tutor might undertake. Given the findings of need made by the District Court, we conclude that in the present case it is.</p>
<p id="b711-6">We may note that the primary guardians of Vernonia’s schoolchildren appear to agree. The record shows no objection to this districtwide program by any parents other than the couple before us here — even though, as we have described, a public meeting was held to obtain parents’ views. We find insufficient basis to contradict the judgment of Ver-nonia’s parents, its school board, and the District Court, as to what was reasonably in the interest of these children under the circumstances.</p>
<p id="ATj"><page-number citation-index="1" label="666">*666</page-number>* * *</p>
<p id="b712-4">The Ninth Circuit held that Vernonia’s Policy not only violated the Fourth Amendment, but also, by reason of that violation, contravened Article I, § 9, of the Oregon Constitution. Our conclusion that the former holding was in error means that the latter holding rested on a flawed premise. We therefore vacate the judgment, and remand the case to the Court of Appeals for further proceedings consistent with this opinion.</p>
<p id="b712-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b698-8"> Not until 1852 did Massachusetts, the pioneer in the “common school” movement, enact a compulsory school-attendance law, and as late as the 1870’s only 14 States had such laws. R. Butts, Public Education in the United States From Revolution to Reform 102-103 (1978); 1 Children and Youth in America 467-468 (R. Bremner ed. 1970). The drug problem, and the technology of drug testing, are of course even more recent.</p>
</footnote>
<footnote label="2">
<p id="b704-5"> Despite the fact that, like routine school physicals and vaccinations— which the dissent apparently finds unobjectionable even though they “are both blanket searches of a sort,” <em>post, </em>at 682 — the search here is undertaken for prophylactic and distinctly wowpunitive purposes (protecting <page-number citation-index="1" label="659">*659</page-number>student athletes from injury, and deterring drug use in the student population), see <span class="citation" data-id="1559138"><a href="/opinion/1559138/acton-v-vernonia-school-district-47j/#1363" aria-description="Citation for case: Acton v. Vernonia School District 47J">796 F. Supp., at 1363</a></span>, the dissent would nonetheless lump this search together with “evidentiary” searches, which generally require probable cause, see <em>supra, </em>at 653, because, from the student’s perspective, the test may be “regarded” or “understood” as punishment, <em>post, </em>at 683-684. In light of the District Court’s findings regarding the purposes and consequences of the testing, any such perception is by definition an irrational one, which is protected nowhere else in the law. In any event, our point is not, as the dissent apparently believes, <em>post, </em>at 682-683, that <em>since </em>student vaccinations and physical exams are constitutionally reasonable, student drug testing must be so as well; but rather that, by reason of those prevalent practices, public school children in general, and student athletes in particular, have a diminished expectation of privacy. See <em>supra, </em>at 656-657.</p>
</footnote>
<footnote label="3">
<p id="b710-4"> There is no basis for the dissent’s insinuation that in upholding the District’s Policy we are equating the Fourth Amendment status of schoolchildren and prisoners, who, the dissent asserts, may have what it calls the “categorical protection” of a “strong preference for an individualized suspicion requirement,” <em>post, </em>at 681. The case on which it relies for that proposition, <em>Bell </em>v. <em>Wolfish, </em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">441 U. S. 520</a></span> (1979), displays no stronger a preference for individualized suspicion than we do today. It reiterates the proposition on which we rely, that “‘elaborate less-restrictive-alternative arguments could raise insuperable barriers to the exercise of virtually all search-and-seizure powers.’” <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#559" aria-description="Citation for case: Bell v. Wolfish"><em>Id., </em>at 559</a></span>, n. 40 (quoting <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 556-557, n. 12</a></span> (1976)). Even Wolfish’s <em>arguendo </em>“assum[ption] that the existence of less intrusive alternatives is relevant to the determination of the reasonableness of the particular search method at issue,” <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#559" aria-description="Citation for case: Bell v. Wolfish">441 U. S., at 559, n. 40</a></span>, does not support the dissent, for the opinion ultimately rejected the hypothesized alternative (as we do) on the ground that it would impair other policies important to the institution. See <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#560" aria-description="Citation for case: Bell v. Wolfish"><em>id., </em>at 560, n. 40</a></span> (monitoring of visits instead of conducting body searches would destroy “the confidentiality and intimacy that these visits are intended to afford”).</p>
</footnote>
<footnote label="4">
<p id="b711-7"> The dissent devotes a few meager paragraphs of its 21 pages to this central aspect of the testing program, see <em>post, </em>at 680-682, in the course of which it shows none of the interest in the original meaning of the Fourth Amendment displayed elsewhere in the opinion, see <em>post, </em>at 669-671. Of course at the time of the framing, as well as at the time of the adoption of the Fourteenth Amendment, children had substantially fewer “rights” than legislatures and courts confer upon them today. See 1 D. Kramer, Legal Rights of Children § 1.02, p. 9 (2d ed. 1994); Wald, Children’s Rights: A Framework for Analysis, 12 U. C. D. L. Rev. 255, 256 (1979).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Walder v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Walder v. United States"
type: case
citation: "347 U.S. 62 (1954)"
parallel_cite: "74 S. Ct. 354; 98 L. Ed. 2d 503; 98 L. Ed. 503"
neutral_cite: 1954 U.S. LEXIS 2453
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1954
date_decided: 1954-02-01
docket: 121
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1954-02-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Walder v. United States
  varies_by_point: false
  scope_note: "Origin of the impeachment exception; remains good law and was extended (Harris v. New York, Havens) and cabined (James v. Illinois)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/105188/walder-v-united-states/"
  cluster_id: 105188
  opinion_id: 105188
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Anchor (impeachment exception)"
related: ["[[Weeks v. United States]]", "[[Agnello v. United States]]", "[[United States v. Havens]]", "[[James v. Illinois]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "impeachment-exception", "credibility"]
holding: "Illegally seized evidence, though inadmissible in the prosecution's case in chief, may be used to impeach a defendant who, on his own direct examination, makes a sweeping affirmative assertion beyond a denial of the charged offense; the exclusionary rule is a shield, not a license to commit perjury."
lake:
  record_id: Walder v. United States
  status: verified
  projected_at: 2026-07-09
---

# Walder v. United States

*347 U.S. 62 (1954)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
In 1950 Walder was indicted for narcotics possession; a heroin capsule was suppressed as the product of an unlawful search, and that case was dismissed. In 1952 he was indicted for four other narcotics transactions. Testifying in his own defense, he volunteered on direct examination that he had never sold or possessed any narcotics in his life. On cross-examination the Government, over objection, asked about the 1950 capsule and then introduced the previously suppressed evidence — but solely to impeach his credibility, under a limiting instruction. He was convicted.

## Issue
Whether evidence obtained by an unlawful search and seizure, inadmissible in the prosecution's case in chief, may be used to impeach a defendant who, on his own direct examination, makes a sweeping claim that he never possessed narcotics.

## Rule
Yes. "It is one thing to say that the Government cannot make an affirmative use of evidence unlawfully obtained. It is quite another to say that the defendant can turn the illegal method by which evidence in the Government's possession was obtained to his own advantage, and provide himself with a shield against contradiction of his untruths. Such an extension of the *Weeks* doctrine would be a perversion of the Fourth Amendment." — 347 U.S. at 65. ^pin-65

A defendant "must be free to deny all the elements of the case against him without thereby giving leave to the Government to introduce by way of rebuttal evidence illegally secured by it"; but "there is hardly justification for letting the defendant affirmatively resort to perjurious testimony in reliance on the Government's disability to challenge his credibility." — [*Id.*](https://www.courtlistener.com/opinion/105188/walder-v-united-states/#:~:text=must%20be%20free%20to%20deny) ^pin-65b

## Application
Walder "went beyond a mere denial of complicity in the crimes of which he was charged and made the sweeping claim that he had never dealt in or possessed any narcotics." That volunteered, perjurious assertion on his own direct examination opened the door, so the Government could use the unlawfully seized heroin to impeach his credibility — but only for impeachment, not as substantive proof of the charged offenses (hence the limiting instruction). The Court "sharply contrasted" this with *[[Agnello v. United States]]*, where the Government, after the defendant said nothing about the evidence on direct, tried to smuggle suppressed evidence in through its own cross-examination — which is impermissible.

## Conclusion
Because Walder himself opened the door with a sweeping false claim, the impeachment use of the suppressed evidence was proper; the conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Walder* is the origin of the **impeachment exception** to the exclusionary rule, built on [[Weeks v. United States]] and distinguishing [[Agnello v. United States]]. It was later extended to statements taken in violation of *[[Miranda v. Arizona|Miranda]]* ([[Harris v. New York]]) and to cross-examination reasonably suggested by direct in [[United States v. Havens]], and cabined to the defendant himself (no other defense witnesses) in [[James v. Illinois]].

## Appears on
- [[The Exclusionary Rule]] — *Key — Anchor (impeachment exception)*

## Sources
- *Walder v. United States*, 347 U.S. 62 (1954) — https://www.courtlistener.com/opinion/105188/walder-v-united-states/ — pinpoints: 65, 66.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "21392c60975d7379", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "347 U.S. 62 (1954)", "court": "U.S. Supreme Court", "neutral_cite": "1954 U.S. LEXIS 2453", "official_citation_present": true, "parallel_cite": "74 S. Ct. 354; 98 L. Ed. 2d 503; 98 L. Ed. 503", "title": "Walder v. United States", "year": "1954"}}
{"assertion_id": "4670f640a1c89336", "dimension": "support", "kind": "home_role", "locator": {"home": "Fruits & Attenuation"}, "payload": {"home": "Fruits & Attenuation", "role": "Key — Anchor (impeachment exception)", "title": "Walder v. United States"}}
{"assertion_id": "4b4d6f82271e0406", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Illegally seized evidence, though inadmissible in the prosecution's case in chief, may be used to impeach a defendant who, on his own direct examination, makes a sweeping affirmative assertion beyond a denial of the charged offense; the exclusionary rule is a shield, not a license to commit perjury.", "title": "Walder v. United States"}}
{"assertion_id": "47910fda341a9928", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Walder v. United States"}}
{"assertion_id": "f84ef2b001b044ca", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1954-02-01", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Walder v. United States", "field_i_validity": "good_law", "scope_note": "Origin of the impeachment exception; remains good law and was extended (Harris v. New York, Havens) and cabined (James v. Illinois).", "title": "Walder v. United States", "varies_by_point": "false"}}
```

### lake record — Walder v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Walder v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Walder v. United States",
    "case_name_short": "Walder",
    "case_name_full": "Walder v. United States",
    "input_case_name": "Walder v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1954-02-01",
    "year": 1954,
    "docket": "121",
    "cluster_id": 105188,
    "lead_opinion_id": 105188,
    "sibling_ids": [
      105188
    ],
    "absolute_url": "/opinion/105188/walder-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "347 U.S. 62",
      "volume": "347",
      "reporter": "U.S.",
      "page": "62",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "74 S. Ct. 354",
        "volume": "74",
        "reporter": "S. Ct.",
        "page": "354",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 L. Ed. 2d 503",
        "volume": "98",
        "reporter": "L. Ed. 2d",
        "page": "503",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 L. Ed. 503",
        "volume": "98",
        "reporter": "L. Ed.",
        "page": "503",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1954 U.S. LEXIS 2453",
        "volume": "1954",
        "reporter": "U.S. LEXIS",
        "page": "2453",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "347 U.S. 62",
        "volume": "347",
        "reporter": "U.S.",
        "page": "62",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "74 S. Ct. 354",
        "volume": "74",
        "reporter": "S. Ct.",
        "page": "354",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 L. Ed. 2d 503",
        "volume": "98",
        "reporter": "L. Ed. 2d",
        "page": "503",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1954 U.S. LEXIS 2453",
        "volume": "1954",
        "reporter": "U.S. LEXIS",
        "page": "2453",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 L. Ed. 503",
        "volume": "98",
        "reporter": "L. Ed.",
        "page": "503",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "347 U.S. 62",
    "official_selection": {
      "court_class": "scotus",
      "selected": "347 U.S. 62",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-65",
      "page": null,
      "quote": "--- # Walder v. United States *347 U.S. 62 (1954)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In 1950 Walder was indicted for narcotics possession; a heroin capsule was suppressed as the product of an unlawful search, and that case was dismissed. In 1952 he was indicted for four other narcotics transactions. Testifying in his own defense, he volunteered on direct examination that he had never sold or possessed any narcotics in his life. On cross-examination the Government, over objection, asked about the 1950 capsule and then introduced the previously suppressed evidence \u2014 but solely to impeach his credibility, under a limiting instruction. He was convicted. ## Issue Whether evidence obtained by an unlawful search and seizure, inadmissible in the prosecution's case in chief, may be used to impeach a defendant who, on his own direct examination, makes a sweeping claim that he never possessed narcotics. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-65b",
      "page": null,
      "quote": "must be free to deny all the elements of the case against him without thereby giving leave to the Government to introduce by way of rebuttal evidence illegally secured by it",
      "star_marker": "65",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 6673,
      "fragment": "#:~:text=must%20be%20free%20to%20deny",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1954-02-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Walder v. United States",
    "varies_by_point": false,
    "scope_note": "Origin of the impeachment exception; remains good law and was extended (Harris v. New York, Havens) and cabined (James v. Illinois).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "People v. Hopson",
          "cluster_id": 4405826,
          "cite": [
            "219 Cal. Rptr. 3d 717",
            "396 P.3d 1054",
            "3 Cal. 5th 424",
            "2017 WL 2837126",
            "2017 Cal. LEXIS 4894"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Yoirlan Rojas",
          "cluster_id": 3217322,
          "cite": [
            "826 F.3d 1126",
            "100 Fed. R. Serv. 871",
            "2016 U.S. App. LEXIS 11688",
            "2016 WL 3513902"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kansas v. Ventris",
          "cluster_id": 145880,
          "cite": [
            "173 L. Ed. 2d 801",
            "129 S. Ct. 1841",
            "556 U.S. 586",
            "2009 U.S. LEXIS 3299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Richard Leroy Parker",
          "cluster_id": 4472828,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Agim Baftiri",
          "cluster_id": 774763,
          "cite": [
            "263 F.3d 856",
            "2001 U.S. App. LEXIS 19334",
            "2001 WL 987524"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Paul A. Bilzerian",
          "cluster_id": 556608,
          "cite": [
            "926 F.2d 1285",
            "31 Fed. R. Serv. 1185",
            "1991 U.S. App. LEXIS 66",
            "1991 WL 430"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Jacobs",
          "cluster_id": 6049311,
          "cite": [
            "149 A.D.2d 112",
            "544 N.Y.S.2d 1011",
            "1989 N.Y. App. Div. LEXIS 10994"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. David Alexander, United States of America v. Everton Knight",
          "cluster_id": 518838,
          "cite": [
            "868 F.2d 492",
            "1989 U.S. App. LEXIS 1989",
            "1989 WL 13234"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. May",
          "cluster_id": 1454345,
          "cite": [
            "748 P.2d 307",
            "44 Cal. 3d 309",
            "243 Cal. Rptr. 369",
            "1988 Cal. LEXIS 20"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane1_negative"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Franks v. Delaware",
          "cluster_id": 109925,
          "cite": [
            "57 L. Ed. 2d 667",
            "98 S. Ct. 2674",
            "438 U.S. 154",
            "1978 U.S. LEXIS 127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mateo",
          "cluster_id": 2006639,
          "cite": [
            "811 N.E.2d 1053",
            "2 N.Y.3d 383",
            "779 N.Y.S.2d 399",
            "2 N.Y. 383",
            "2004 N.Y. LEXIS 263"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doyle v. Ohio",
          "cluster_id": 109491,
          "cite": [
            "49 L. Ed. 2d 91",
            "96 S. Ct. 2240",
            "426 U.S. 610",
            "1976 U.S. LEXIS 66"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. New York",
          "cluster_id": 108272,
          "cite": [
            "28 L. Ed. 2d 1",
            "91 S. Ct. 643",
            "401 U.S. 222",
            "1971 U.S. LEXIS 75"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richardson v. Marsh",
          "cluster_id": 111865,
          "cite": [
            "95 L. Ed. 2d 176",
            "107 S. Ct. 1702",
            "481 U.S. 200",
            "1987 U.S. LEXIS 1812",
            "55 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brewer v. Williams",
          "cluster_id": 109624,
          "cite": [
            "51 L. Ed. 2d 424",
            "97 S. Ct. 1232",
            "430 U.S. 387",
            "1977 U.S. LEXIS 64"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Hass",
          "cluster_id": 109221,
          "cite": [
            "43 L. Ed. 2d 570",
            "95 S. Ct. 1215",
            "420 U.S. 714",
            "1975 U.S. LEXIS 5"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jenkins v. Anderson",
          "cluster_id": 110298,
          "cite": [
            "65 L. Ed. 2d 86",
            "100 S. Ct. 2124",
            "447 U.S. 231",
            "1980 U.S. LEXIS 131"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nix v. Whiteside",
          "cluster_id": 111603,
          "cite": [
            "89 L. Ed. 2d 123",
            "106 S. Ct. 988",
            "475 U.S. 157",
            "1986 U.S. LEXIS 8",
            "54 U.S.L.W. 4194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. United States",
          "cluster_id": 105661,
          "cite": [
            "2 L. Ed. 2d 589",
            "78 S. Ct. 622",
            "356 U.S. 148",
            "1958 U.S. LEXIS 1286"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ceccolini",
          "cluster_id": 109816,
          "cite": [
            "55 L. Ed. 2d 268",
            "98 S. Ct. 1054",
            "435 U.S. 268",
            "1978 U.S. LEXIS 70"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Harvey",
          "cluster_id": 112385,
          "cite": [
            "108 L. Ed. 2d 293",
            "110 S. Ct. 1176",
            "494 U.S. 344",
            "1990 U.S. LEXIS 1229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Havens",
          "cluster_id": 110267,
          "cite": [
            "64 L. Ed. 2d 559",
            "100 S. Ct. 1912",
            "446 U.S. 620",
            "1980 U.S. LEXIS 103"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morris W. Gordon v. United States",
          "cluster_id": 277392,
          "cite": [
            "383 F.2d 936"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(105188) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MjY3Mjk2MDAwMDAmcz0xNzMzMTc5JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28105188%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 10,
        "triage_snippet_classified": 190
      },
      "lane2_top_cited": {
        "query": "cites:(105188)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNTcmcz01NjMyMDEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28105188%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(105188)",
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
    "complete_query": "cites:(105188)",
    "indexed_citing_opinions": 638,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 105188,
        "count": 638,
        "count_source": "search"
      }
    ],
    "citation_count": 1024,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/walder-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY2MTM2NjImcz00Njk2MTE1JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28105188%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 105188,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105188,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105188,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105188,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105188,
        "cited_id": 104607,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105188,
        "cited_id": 230984,
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
    "date_created": "2026-07-06T03:56:50Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:57:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:57:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:59:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:57:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Walder v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b136-12">
  Mr. Justice Frankfurter
 </author>
<p id="A0M">
  delivered the opinion of the Court.
 </p>
<p id="b136-13">
  In May 1950, petitioner was indicted in the United States District Court for the Western District of Missouri for purchasing and possessing one grain of heroin. Claiming that the heroin capsule had been obtained through an unlawful search and seizure, petitioner moved
  <span citation-index="1" class="star-pagination" label="63"> 
   *63
   </span>
  to suppress it. The motion was granted, and shortly thereafter, on the Government’s motion, the case against petitioner was dismissed.
 </p>
<p id="b137-5">
  In January of 1952, petitioner was again indicted, this time for four other illicit transactions in narcotics. The Government’s case consisted principally of the testimony of two drug addicts who claimed to have procured the illicit stuff from petitioner under the direction of federal agents. The only witness for the defense was the defendant himself, petitioner here. He denied any narcotics dealings with the two Government informers and attributed the testimony against him to personal hostility.
 </p>
<p id="b137-6">
  Early on his direct examination petitioner testified as follows:
 </p>
<blockquote id="b137-7">
  “Q. Now, first, Mr. Walder, before we go further in your testimony, I want to you [sic] tell the Court and jury whether, not referring to these informers in this case, but whether you have ever sold any narcotics to anyone.
 </blockquote>
<blockquote id="b137-8">
  “A. I have never sold any narcotics to anyone in my life.
 </blockquote>
<blockquote id="b137-9">
  “Q. Have you ever had any narcotics in your possession, other than what may have been given to you by a physician for an ailment?
 </blockquote>
<blockquote id="b137-10">
  “A. No.
 </blockquote>
<blockquote id="b137-11">
  “Q. Now, I will ask you one more thing. Have you ever handed or given any narcotics to anyone as a gift or in any other manner without the receipt of any money or any other compensation?
 </blockquote>
<blockquote id="b137-12">
  “A. I have not.
 </blockquote>
<blockquote id="b137-13">
  “Q. Have you ever even acted as, say, have you acted as a conduit for the purpose of handling what you knew to be a narcotic from one person to another?
 </blockquote>
<blockquote id="b137-14">
  “A. No, sir.”
 </blockquote>
<p id="b138-4">
<span citation-index="1" class="star-pagination" label="64"> 
   *64
   </span>
  On cross-examination, in response to a question by Government counsel making reference to this direct testimony, petitioner reiterated his assertion that he had never purchased, sold or possessed any narcotics. Over the defendant’s objection, the Government then questioned him about the heroin capsule unlawfully seized from his home in his presence back in February 1950. The defendant stoutly denied that any narcotics were taken from him at that time.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  The Government then put on the stand one of the officers who had participated in the unlawful search and seizure and also the chemist who had analyzed the heroin capsule there seized. The trial judge admitted this evidence, but carefully charged the jury that it was not to be used to determine whether the defendant had committed the crimes here charged, but solely for the purpose of impeaching the defendant’s credibility. The defendant was convicted, and the Court of Appeals for the Eighth Circuit affirmed, one judge dissenting. <span class="citation" data-id="9443562"><a href="/opinion/230984/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">201 F. 2d 715</a></span>. The question which divided that court, and the sole issue here, is whether the defendant’s assertion on direct examination that he had never possessed any narcotics opened the door, solely for the purpose of attacking the defendant’s credibility, to evidence of the heroin unlawfully seized in connection with the earlier proceeding. Because this question presents a novel aspect of the scope of the doctrine of
  <em>
   Weeks
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./345/992/">345 U. S. 992</a></span>.
 </p>
<p id="b138-5">
  The Government cannot violate the Fourth Amendment
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  — in the only way in which the Government can do anything, namely through its agents — and use the fruits
  <span citation-index="1" class="star-pagination" label="65"> 
   *65
   </span>
  of such unlawful conduct to secure a conviction.
  <em>
   Weeks
  </em>
  v.
  <em>
   United States, supra.
  </em>
  Nor can the Government make indirect use of such evidence for its case,
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>, or support a conviction on evidence obtained through leads from the unlawfully obtained evidence, cf.
  <em>
   Nardone
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">308 U. S. 338</a></span>. All these methods are outlawed, and convictions obtained by means of them are invalidated, because they encourage the kind of society that is obnoxious to free men.
 </p>
<p id="b139-5">
  It is one thing to say that the Government cannot make an affirmative use of evidence unlawfully obtained. It is quite another to say that the defendant can turn the illegal method by which evidence in the' Government’s possession was obtained to his own advantage, and provide himself with a shield against contradiction of his untruths. Such an extension of the
  <em>
   <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>
  </em>
  doctrine would be a perversion of the Fourth Amendment.
 </p>
<p id="b139-6">
  Take the present situation. Of his own accord, the defendant went beyond a mere denial of complicity in the crimes of which he was charged and made the sweeping claim that he had never dealt in or possessed any narcotics. Of course, the Constitution guarantees a defendant the fullest opportunity to meet the accusation against him. He must be free to deny all the elements of the case against him without thereby giving leave to the Government to introduce by way of rebuttal evidence illegally secured by it, and therefore not available for its case in chief. Beyond that, however, there is hardly justification for letting the defendant affirmatively resort to perjurious testimony in reliance on the Government’s disability to challenge his credibility.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="Azo">
<span citation-index="1" class="star-pagination" label="66"> 
   *66
   </span>
  The situation here involved is to be sharply contrasted with that presented by
  <em>
   Agnello
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span>. There the Government, after having failed in its efforts to introduce the tainted evidence in its case in chief, tried to smuggle it in on cross-examination by asking the accused the broad question “Did you ever see narcotics before?”
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  After eliciting the expected denial, it sought to introduce evidence of narcotics located in the defendant’s home by means of an unlawful search and seizure, in order to discredit the defendant. In holding that the Government could no more work in this evidence on cross-examination than it could in its case in chief, the Court foreshadowed, perhaps unwittingly, the result we reach today:
 </p>
<blockquote id="b140-4">
  “And the contention that the evidence of the search and seizure was admissible in rebuttal is without merit. In his direct examination, Agnello was not asked and did not testify concerning the can of cocaine. In cross-examination, in answer to a question permitted over his objection, he said he had never seen it. He did nothing to waive his constitutional protection or to justify cross-examination in respect of the evidence claimed to have been obtained by the search. . . .” <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#35" aria-description="Citation for case: Agnello v. United States">269 U. S., at 35</a></span>.
 </blockquote>
<p id="b140-5">
  The judgment is
 </p>
<p id="b140-6">
<em>
   Affirmed.
  </em>
</p>
<judges id="b140-7">
  Mr. Justice Black and Mr. Justice Douglas dissent.
 </judges>




<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b138-6">
   This denial squarely contradicted the affidavit filed by the defendant in the earlier proceeding, in connection with his motion under Rule 41 (e) to suppress the evidence unlawfully seized.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b138-7">
   “The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated . . . .”
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b139-7">
   Cf.
   <em>
    Michelson
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9420246"><a href="/opinion/104607/michelson-v-united-states/" aria-description="Citation for case: Michelson v. United States">335 U. S. 469</a></span>, 479: “The price a defendant must pay for attempting to prove his good name is to throw open the entire subject which the law has kept closed for his
   <span citation-index="1" class="star-pagination" label="66"> 
    *66
    </span>
   benefit and to make himself vulnerable where the law otherwise shields him.”
  </p>
<p id="b140-9">
   The underlying rationale of the
   <em>
    <span class="citation" data-id="9420246"><a href="/opinion/104607/michelson-v-united-states/" aria-description="Citation for case: Michelson v. United States">Michelson</a></span>
   </em>
   case also disposes of the evidentiary question raised by petitioner, to wit, “whether defendant’s actual guilt under a former indictment which was dismissed may be proved by extrinsic evidence introduced to impeach him in a prosecution for a subsequent offense.”
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b140-10">
<em>
</em>
   Transcript of Record, p. 476,
   <em>
    Agnello
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span>.
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Warden v. Hayden.md  (`case`, 5 assertions)

### content_page

```
---
title: "Warden v. Hayden"
type: case
citation: "387 U.S. 294 (1967)"
parallel_cite: "87 S. Ct. 1642; 18 L. Ed. 2d 782"
neutral_cite: 1967 U.S. LEXIS 2753
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1967
date_decided: 1967-05-29
docket: 480
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1967-05-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Warden v. Hayden
  varies_by_point: false
  scope_note: "Foundational hot-pursuit case; also abolished the 'mere evidence' rule of Gouled v. United States. Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107465/warden-maryland-penitentiary-v-hayden/"
  cluster_id: 107465
  opinion_id: 9423434
  identity_checked: true
homes:
  - page: "[[Exigent Circumstances and Hot Pursuit]]"
    role: "Key — Anchor"
related: ["[[United States v. Santana]]", "[[Kentucky v. King]]", "[[Welsh v. Wisconsin]]"]
aliases: ["Warden, Maryland Penitentiary v. Hayden", "Hayden"]
tags: ["case", "fourth-amendment", "exigent-circumstances", "hot-pursuit", "warrantless-entry"]
holding: "Hot pursuit of a fleeing armed robber into a house is a valid warrantless entry and search where \"the exigencies of the situation made…"
lake:
  record_id: Warden v. Hayden
  status: verified
  projected_at: 2026-07-06
---

# Warden v. Hayden

*387 U.S. 294 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
An armed robber held up a taxi company and fled. Two cab drivers followed him and radioed his description and the address of the house he entered. Police arrived within minutes, were told an armed suspect had just gone in, and entered without a warrant. Searching the house for the robber and his weapons, they found Hayden feigning sleep in an upstairs bedroom, a shotgun and pistol in a flush tank, ammunition, and clothing matching the robber's description in a washing machine. All were used to convict him.

## Issue
Whether the warrantless entry into and search of a house, in immediate pursuit of an armed robber reported to have entered moments earlier, was reasonable under the Fourth Amendment.

## Rule
[[Exigent Circumstances and Hot Pursuit|Hot pursuit]] of a fleeing armed suspect into a dwelling is a valid warrantless entry and search where the [[Exigent Circumstances and Hot Pursuit|exigencies]] make it imperative: "neither the entry without warrant to search for the robber, nor the search for him without warrant was invalid. Under the circumstances of this case, 'the exigencies of the situation made that course imperative.'" — 387 U.S. at 298. ^pin-298

The scope follows the emergency: "The Fourth Amendment does not require police officers to delay in the course of an investigation if to do so would gravely endanger their lives or the lives of others." — *Id.* at 298–299. ^pin-299

## Application
On these facts the police acted within minutes of an armed robbery on information that the armed suspect had just entered the house. Speed was essential: only a prompt, thorough search for persons and weapons could ensure that Hayden was the only man present and that officers controlled any weapons that could be used against them or to effect an escape. The warrantless entry and the search for the robber and his weapons were therefore reasonable, and the items found in the course of that search were admissible.

## Conclusion
The warrantless entry and search in [[Exigent Circumstances and Hot Pursuit|hot pursuit]] were reasonable; the seizure of the weapons and clothing was valid. The Court also rejected the "mere evidence" limitation, holding that evidentiary items (not just contraband, fruits, or instrumentalities) may be seized.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Hayden* anchors the hot-pursuit branch of the [[Exigent Circumstances and Hot Pursuit|exigency]] doctrine, applied to a suspect fleeing into her own home in [[United States v. Santana]] and framed within the [[Exigent Circumstances and Hot Pursuit|exigency]] framework reaffirmed in [[Kentucky v. King]]; the gravity-of-offense limit on home-entry [[Exigent Circumstances and Hot Pursuit|exigencies]] is drawn in [[Welsh v. Wisconsin]]. Its separate holding abolishing the "mere evidence" rule remains good law.

## Appears on
- [[Exigent Circumstances and Hot Pursuit]] — *Key — Anchor*

## Sources
- *Warden v. Hayden*, 387 U.S. 294 (1967) — https://www.courtlistener.com/opinion/107465/warden-maryland-penitentiary-v-hayden/ — pinpoints: 298, 298–299.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1cefe7f72089e3f3", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "387 U.S. 294 (1967)", "court": "U.S. Supreme Court", "neutral_cite": "1967 U.S. LEXIS 2753", "official_citation_present": true, "parallel_cite": "87 S. Ct. 1642; 18 L. Ed. 2d 782", "title": "Warden v. Hayden", "year": "1967"}}
{"assertion_id": "1fdf9030500c29e2", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Hot pursuit of a fleeing armed robber into a house is a valid warrantless entry and search where \\\"the exigencies of the situation made…", "title": "Warden v. Hayden"}}
{"assertion_id": "69f9e593f4ff71ca", "dimension": "support", "kind": "home_role", "locator": {"home": "Exigent Circumstances and Hot Pursuit"}, "payload": {"home": "Exigent Circumstances and Hot Pursuit", "role": "Key — Anchor", "title": "Warden v. Hayden"}}
{"assertion_id": "4d08dcf7c37ac102", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1967-05-29", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Warden v. Hayden", "field_i_validity": "good_law", "scope_note": "Foundational hot-pursuit case; also abolished the 'mere evidence' rule of Gouled v. United States. Good law.", "title": "Warden v. Hayden", "varies_by_point": "false"}}
{"assertion_id": "f835d10557aa8de3", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Warden v. Hayden"}}
```

### lake record — Warden v. Hayden

```json
{
  "schema_version": "s2.v1",
  "record_id": "Warden v. Hayden",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Warden, Maryland Penitentiary v. Hayden",
    "case_name_short": "Hayden",
    "case_name_full": "Warden, Maryland Penitentiary v. Hayden",
    "input_case_name": "Warden v. Hayden",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-05-29",
    "year": 1967,
    "docket": "480",
    "cluster_id": 107465,
    "lead_opinion_id": 9423434,
    "sibling_ids": [
      107465,
      9423434,
      9423435,
      9423436
    ],
    "absolute_url": "/opinion/107465/warden-maryland-penitentiary-v-hayden/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "387 U.S. 294",
      "volume": "387",
      "reporter": "U.S.",
      "page": "294",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 1642",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1642",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 782",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "782",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 2753",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "2753",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "387 U.S. 294",
        "volume": "387",
        "reporter": "U.S.",
        "page": "294",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 1642",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1642",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 782",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "782",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 2753",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "2753",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "387 U.S. 294",
    "official_selection": {
      "court_class": "scotus",
      "selected": "387 U.S. 294",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-298",
      "page": null,
      "quote": "--- # Warden v. Hayden *387 U.S. 294 (1967)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An armed robber held up a taxi company and fled. Two cab drivers followed him and radioed his description and the address of the house he entered. Police arrived within minutes, were told an armed suspect had just gone in, and entered without a warrant. Searching the house for the robber and his weapons, they found Hayden feigning sleep in an upstairs bedroom, a shotgun and pistol in a flush tank, ammunition, and clothing matching the robber's description in a washing machine. All were used to convict him. ## Issue Whether the warrantless entry into and search of a house, in immediate pursuit of an armed robber reported to have entered moments earlier, was reasonable under the Fourth Amendment. ## Rule Hot pursuit of a fleeing armed suspect into a dwelling is a valid warrantless entry and search where the exigencies make it imperative:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-299",
      "page": null,
      "quote": "The Fourth Amendment does not require police officers to delay in the course of an investigation if to do so would gravely endanger their lives or the lives of others.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1967-05-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Warden v. Hayden",
    "varies_by_point": false,
    "scope_note": "Foundational hot-pursuit case; also abolished the 'mere evidence' rule of Gouled v. United States. Good law.",
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
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. McCarthy",
          "cluster_id": 4746120,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Perkins",
          "cluster_id": 4433002,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Louisiana v. Joseph Michael Moultrie",
          "cluster_id": 4405157,
          "cite": [
            "224 So. 3d 349",
            "2017 La. LEXIS 1382",
            "2017 WL 2836066"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Amended July 5, 2017 State of Iowa v. Maurice D. Angel and Kemia B. McDowell",
          "cluster_id": 4471947,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Maurice D. Angel and Kemia B. McDowell",
          "cluster_id": 4384931,
          "cite": [
            "893 N.W.2d 904",
            "2017 WL 1422692",
            "2017 Iowa Sup. LEXIS 41"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ricky Johnson v. State of Indiana",
          "cluster_id": 4371565,
          "cite": [
            "70 N.E.3d 890",
            "2017 WL 765897",
            "2017 Ind. App. LEXIS 88"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
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
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Shamel L. Alexander",
          "cluster_id": 3177044,
          "cite": [
            "2016 VT 19",
            "201 Vt. 329",
            "139 A.3d 574",
            "2016 Vt. LEXIS 19",
            "2016 WL 555794"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Yee",
          "cluster_id": 3062319,
          "cite": [
            "177 So. 3d 72",
            "2015 Fla. App. LEXIS 15198",
            "2015 WL 5965213"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
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
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chad Camou",
          "cluster_id": 2759861,
          "cite": [
            "773 F.3d 932",
            "2014 U.S. App. LEXIS 23347",
            "2014 WL 6980135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
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
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Leotis B. Branigh, III",
          "cluster_id": 1034108,
          "cite": [
            "155 Idaho 404",
            "313 P.3d 732",
            "2013 WL 3718751",
            "2013 Ida. App. LEXIS 63"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Katz v. United States",
          "cluster_id": 107564,
          "cite": [
            "19 L. Ed. 2d 576",
            "88 S. Ct. 507",
            "389 U.S. 347",
            "1967 U.S. LEXIS 2"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Simmons v. United States",
          "cluster_id": 107636,
          "cite": [
            "19 L. Ed. 2d 1247",
            "88 S. Ct. 967",
            "390 U.S. 377",
            "1968 U.S. LEXIS 2167"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spinelli v. United States",
          "cluster_id": 107831,
          "cite": [
            "21 L. Ed. 2d 637",
            "89 S. Ct. 584",
            "393 U.S. 410",
            "1969 U.S. LEXIS 2701"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. Sykes",
          "cluster_id": 109717,
          "cite": [
            "53 L. Ed. 2d 594",
            "97 S. Ct. 2497",
            "433 U.S. 72",
            "1977 U.S. LEXIS 135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chambers v. Maroney",
          "cluster_id": 108184,
          "cite": [
            "26 L. Ed. 2d 419",
            "90 S. Ct. 1975",
            "399 U.S. 42",
            "1970 U.S. LEXIS 19"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gilbert v. California",
          "cluster_id": 107487,
          "cite": [
            "18 L. Ed. 2d 1178",
            "87 S. Ct. 1951",
            "388 U.S. 263",
            "1967 U.S. LEXIS 1086"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107465 OR 9423434 OR 9423435 OR 9423436) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjQwMzU4NDAwMDAwJnM9Mjg4MDMwOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107465+OR+9423434+OR+9423435+OR+9423436%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 14,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 14,
        "triage_snippet_classified": 186
      },
      "lane2_top_cited": {
        "query": "cites:(107465 OR 9423434 OR 9423435 OR 9423436)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzg0JnM9MTA5NTA0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107465+OR+9423434+OR+9423435+OR+9423436%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107465 OR 9423434 OR 9423435 OR 9423436)",
        "reviewed": 16,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 16,
        "triage_read": 0,
        "triage_snippet_classified": 16
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107465 OR 9423434 OR 9423435 OR 9423436)",
    "indexed_citing_opinions": 2140,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107465,
        "count": 1965,
        "count_source": "search"
      },
      {
        "opinion_id": 9423434,
        "count": 239,
        "count_source": "search"
      },
      {
        "opinion_id": 9423435,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423436,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3217,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/warden-v-hayden.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgxNjA2NTkmcz05MzgwNzA2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107465+OR+9423434+OR+9423435+OR+9423436%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107465,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 104407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 105532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 105746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106142,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106240,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 107102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 268073,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 1421285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 1476321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 1481331,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 1990408,
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
    "date_created": "2026-07-06T04:05:02Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:05:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:05:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:08:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:05:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Warden v. Hayden

```
<opinion type="majority">
<author id="b339-13">Mr. Justice Brennan</author>
<p id="AdV">delivered the opinion of the Court.</p>
<p id="b339-14">We review in this case the validity of the proposition that there is under the Fourth Amendment a “distinction <page-number citation-index="1" label="296">*296</page-number>between merely evidentiary materials, on the one hand, which may not be seized either under the authority of a search warrant or during the course of a search incident to arrest, and on the other hand, those objects which may validly be seized including the instrumentalities and means by which a crime is committed, the fruits of crime such as stolen property, weapons by which escape of the person arrested might be effected, and property the possession of which is a crime.” <footnotemark>1</footnotemark></p>
<p id="b340-6">A Maryland court sitting without a jury convicted respondent of armed robbery. Items of his clothing, a cap, jacket,- and trousers, among other things, were seized during a search of his home, and were admitted in evidence without objection. After unsuccessful state court proceedings, he sought and was denied federal habeas corpus relief in the District Court for Maryland.<footnotemark>2</footnotemark> A divided panel of the Court of Appeals for the Fourth Circuit reversed. <span class="citation" data-id="9451981"><a href="/opinion/272530/bennie-joe-hayden-v-warden-maryland-penitentiary/" aria-description="Citation for case: Bennie Joe Hayden v. Warden, Maryland Penitentiary">363 F. 2d 647</a></span>. The Court of Appeals believed that <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#154" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 154</a></span>, sustained the validity of the search, but held that respondent was correct in his contention that the clothing seized was improperly admitted in evidence because the items had “evidential value only” and therefore were not <page-number citation-index="1" label="297">*297</page-number>lawfully subject to seizure. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./385/926/">385 U. S. 926</a></span>. We reverse.<footnotemark>3</footnotemark></p>
<p id="b341-5">I.</p>
<p id="b341-6">About 8 a. m. on March 17, 1962, an armed robber entered the business premises of the Diamond Cab Company in Baltimore, Maryland. He took some $363 and ran. Two cab drivers in the vicinity, attracted by shouts of “Holdup,” followed the man to 2111 Cocoa Lane. One driver notified the company dispatcher by radio that the man was a Negro about 5'8" tall, wearing a light cap and dark jacket, and that he had entered the house on Cocoa Lane. The dispatcher relayed the information to police who were proceeding to the scene of the robbery. Within minutes, police arrived at the house in a number of patrol cars. An officer knocked and announced their presence. Mrs. Hayden answered, and the officers told her they believed that a robber had entered the house, and asked to search the house. She offered no objection.<footnotemark>4</footnotemark></p>
<p id="b342-5"><page-number citation-index="1" label="298">*298</page-number>The officers spread out through the first and second floors and the cellar in search of the robber. Hayden was found in an upstairs bedroom feigning sleep. He was arrested when the officers on the first floor and in the cellar reported that no other man was in the house. Meanwhile an officer was attracted to an adjoining bathroom by the noise of running water, and discovered a shotgun and a pistol in a flush tank; another officer who, according to the District Court, “was searching the cellar for a man or the money” found in a washing machine a jacket and trousers of the type the fleeing man was said to have worn. A clip of ammunition for the pistol and a cap were found under the mattress of Hayden’s bed, and ammunition for the shotgun was found in a bureau drawer in Hayden’s room. All these items of evidence were introduced against respondent at his trial.</p>
<p id="b342-6">II.</p>
<p id="b342-7">We agree with the Court of Appeals that neither the entry without warrant to search for the robber, nor the search for him without warrant was invalid. Under the circumstances of this case, “the exigencies of the situation made that course imperative.” <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#456" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 456</a></span>. The police were informed that an armed robbery had taken place, and that the suspect had entered 2111 Cocoa Lane less than five minutes before they reached it. They acted reasonably when they entered the house and began to search for a man of the description they had been given and for weapons which he had used in the robbery or might use against them. The Fourth Amendment does not require police officers to delay in the course of an investigation <page-number citation-index="1" label="299">*299</page-number>if to do so would gravely endanger their lives or the lives of others. Speed here was essential, and only a thorough search of the house for persons and weapons could have insured that Hayden was the only man present and that the police had control of all weapons which could be used against them or to effect an escape.</p>
<p id="b343-5">We do not rely upon <em>Harris </em>v. <em>United States, supra, </em>in sustaining the validity of the search. The principal issue in <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>was whether the search there could properly be regarded as incident to the lawful arrest, since Harris was in custody before the search was made and the evidence seized. Here, the seizures occurred prior to or immediately contemporaneous with Hayden’s arrest, as part of an effort to find a suspected felon, armed, within the house into which he had run only minutes before the police arrived. The permissible scope of search must, therefore, at the least, be as broad as may reasonably be necessary to prevent the dangers that the suspect at large in the house may resist or escape.</p>
<p id="b343-6">It is argued that, while the weapons, ammunition, and cap may have been seized in the course of a search for weapons, the officer who seized the clothing was searching neither for the suspect nor for weapons when he looked into the washing machine in which he found the clothing. But even if we assume, although we do not decide, that the exigent circumstances in this case made lawful a search without warrant only for the suspect or his weapons, it cannot be said on this record that the officer who found the clothes in the washing machine was not searching for weapons. He testified that he was searching for the man or the money, but his failure to state explicitly that he was searching for weapons, in the absence of a specific question to that effect, can hardly be accorded controlling weight. He knew that the robber was armed and he did not know that some <page-number citation-index="1" label="300">*300</page-number>weapons had been found at the time he opened the machine.<footnotemark>5</footnotemark> In these circumstances the inference that he was in fact also looking for weapons is fully justified.</p>
<p id="b344-6">III.</p>
<p id="b344-7">We come, then, to the question whether, even though the search was lawful, the Court of Appeals was correct in holding that the seizure and introduction of the items of clothing violated the Fourth Amendment because they are “mere evidence.” The distinction made by some of our cases between seizure of items of evidential value only and seizure of instrumentalities, fruits, or contraband has been criticized by courts<footnotemark>6</footnotemark> and commentators.<footnotemark>7</footnotemark> The Court of Appeals, however, felt “obligated to adhere to it.” <span class="citation" data-id="9451981"><a href="/opinion/272530/bennie-joe-hayden-v-warden-maryland-penitentiary/#655" aria-description="Citation for case: Bennie Joe Hayden v. Warden, Maryland Penitentiary">363 F. 2d, at 655</a></span>. We today reject the distinction as based on premises no longer <page-number citation-index="1" label="301">*301</page-number>accepted as rules governing the application of the Fourth Amendment.<footnotemark>8</footnotemark></p>
<p id="b345-5">We have examined on many occasions the history and purposes of the Amendment.<footnotemark>9</footnotemark> It was a reaction to the evils of the use of the general warrant in England and the writs of assistance in the Colonies, and was intended to protect against invasions of “the sanctity of a man’s home and the privacies of life,” <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span>, from searches under indiscriminate, general authority. Protection of these interests was assured by prohibiting all “unreasonable” searches and seizures, and by requiring the use of warrants, which particularly describe “the place to be searched, and the persons or things to be seized,” thereby interposing “a magistrate between the citizen and the police,” <em>McDonald </em>v. <em>United States, supra, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 U. S., at 455</a></span>.</p>
<p id="b345-6">Nothing in the language of the Fourth Amendment supports the distinction between “mere evidence” and instrumentalities, fruits of crime, or contraband. On its face, the provision assures the “right of the people to be secure in their persons, houses, papers, and effects . . . ,” without regard to the use to which any of these things are applied. This “right of the people” is certainly unrelated to the “mere evidence” limitation. Privacy is disturbed no more by a search directed to a purely evidentiary object than it is by a search directed to an instrumen<page-number citation-index="1" label="302">*302</page-number>tality, fruit, or contraband. A magistrate can intervene in both situations, and the requirements of probable cause and specificity can be preserved intact. Moreover, nothing in the nature of property seized as evidence renders it more private than property seized, for example, as an instrumentality; quite the opposite may be true. Indeed, the distinction is wholly irrational, since, depending on the circumstances, the same “papers and effects” may be “mere evidence” in one case and “instrumentality” in another. See Comment, <span class="citation no-link">20 U. Chi. L. Rev. 319</span>, 320-322 (1953).</p>
<p id="b346-4">In <em>Gouled </em>v. <em>United States, </em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#309" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 309</a></span>, the Court said that search warrants “may not be used as a means of gaining access to a man’s house or office and papers solely for the purpose of making search to secure evidence to be used against him in a criminal or penal proceeding . . . .” The Court derived from <em>Boyd </em>v. <em>United States, supra, </em>the proposition that warrants “may be resorted to only when a primary right to such search and seizure may be found in the interest which the public or the complainant may have in the property to be seized, or in the right to the possession of it, or when a valid exercise of the police power renders possession of the property by the accused unlawful and provides that it may be taken,” <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#309" aria-description="Citation for case: Gouled v. United States">255 U. S., at 309</a></span>; that is, when the property is an instrumentality or fruit of crime, or contraband. Since it was “impossible to say, on the record . . . that the Government had any interest” in the papers involved “other than as evidence against the accused . . . ,” “to permit them to be used in evidence would be, in effect, as ruled in the <em>Boyd Case, </em>to compel the defendant to become a witness against himself.” <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#311" aria-description="Citation for case: Gouled v. United States"><em>Id., at </em>311</a></span>.</p>
<p id="b346-5">The items of clothing involved in this case are not “testimonial” or “communicative” in nature, and their introduction therefore did not compel respondent to be<page-number citation-index="1" label="303">*303</page-number>come a witness against himself in violation of the Fifth Amendment. <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span>. This case thus does not require that we consider whether there are items of evidential value whose very nature precludes them from being the object of a reasonable search and seizure.</p>
<p id="b347-5">The Fourth Amendment ruling in <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>was based upon the dual, related premises that historically the right to search for and seize property depended upon the assertion by the Government of a valid claim of superior interest, and that it was not enough that the purpose of the search and seizure was to obtain evidence to use in apprehending and convicting criminals. The common law of search and seizure after <em>Entick </em>v. <em>Carrington, </em>19 How. St. Tr. 1029, reflected Lord Camden’s view, derived no doubt from the political thought of his time, that the “great end, for which men entered into society, was to secure their property.” <em>Id., </em>at 1066. Warrants were “allowed only where the primary right to such a search and seizure is in the interest which the public or complainant may have in the property seized.” Lasson, The History and Development of the Fourth Amendment to the United States Constitution 133-134. Thus stolen property — the fruits of crime — was always subject to seizure. And the power to search for stolen property was gradually extended to cover “any property which the private citizen was not permitted to possess,” which included instrumentalities of crime (because of the early notion that items used in crime were forfeited to the State) and contraband. Kaplan, Search and Seizure: A No-Man’s Land in the Criminal Law, <span class="citation no-link">49 Calif. L. Rev. 474</span>, 475. No separate governmental interest in seizing evidence to apprehend and convict criminals was recognized; it was required that some property interest be asserted. The remedial structure also reflected these dual premises. Trespass, replevin, and the other means of <page-number citation-index="1" label="304">*304</page-number>redress for persons aggrieved by searches and seizures, depended upon proof of a superior property interest. And since a lawful seizure presupposed a superior claim, it was inconceivable that a person could recover property lawfully seized. As Lord Camden pointed out in <em>Entick </em>v. <em>Carrington, supra, </em>at 1066, a general warrant enabled “the party’s own property [to be] seized before and without conviction, and he has no power to reclaim his goods, even after his innocence is cleared by acquittal.”</p>
<p id="b348-6">The premise that property interests control the right of the Government to search and seize has been discredited. Searches and seizures may be “unreasonable” within the Fourth Amendment even though the Government asserts a superior property interest at common law. We have recognized that the principal object of the Fourth Amendment is the protection of privacy rather than property, and have increasingly discarded fictional and procedural barriers rested on property concepts. See <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#266" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 266</a></span>; <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 511</a></span>. This shift in emphasis from property to privacy has come about through a subtle interplay of substantive and procedural reform. The remedial structure at the time even of <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, was arguably explainable in property terms. The Court held in <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>that a defendant could petition <em>before </em>trial for the return of his illegally seized property, a proposition not necessarily inconsistent with <em>Adams </em>v. <em>New York, </em><span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U. S. 585</a></span>, which held in effect that the property issues involved in search and seizure are collateral to a criminal proceeding.<footnotemark>10</footnotemark> The remedial structure finally escaped the bounds of common law property limitations in <em>Silverthorne </em><page-number citation-index="1" label="305">*305</page-number><em>Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>, and <em>Gouled </em>v. <em>United States, supra, </em>when it became established that suppression might be sought during a criminal trial, and under circumstances which would not sustain an action in trespass or replevin. Recognition that the role of the Fourth Amendment was to protect against invasions of privacy demanded a remedy to condemn the seizure in <em>Silverthorne, </em>although no possible common law claim existed for the return of the copies made by the Government of the papers it had seized. The remedy of suppression, necessarily involving only the limited, functional consequence of excluding the evidence from trial, satisfied that demand.</p>
<p id="b349-5">The development of search and seizure law since <em>Silver-thorne </em>and <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>is replete with examples of the transformation in substantive law brought about through the interaction of the felt need to protect privacy from unreasonable invasions and the flexibility in rulemaking made possible by the remedy of exclusion. We have held, for example, that intangible as well as tangible evidence may be suppressed, <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#485" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 485-486</a></span>, and that an actual trespass under local property law is unnecessary to support a remediable violation of the Fourth Amendment, <em>Silverman </em>v. <em>United States, supra. </em>In determining whether someone is a “person aggrieved by an unlawful search and seizure” we have refused “to import into the law . . . subtle distinctions, developed and refined by the common law in evolving the body of private property law which, more than almost any other branch of law, has been shaped by distinctions whose validity is largely historical.” <em>Jones </em>v. <em>United States, supra, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#266" aria-description="Citation for case: Jones v. United States">362 U. S., at 266</a></span>. And with particular relevance here, we have given recognition to the interest in privacy despite the complete absence of a property claim by suppressing the very items which at <page-number citation-index="1" label="306">*306</page-number>common law could be seized with impunity: stolen goods, <em>Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span>; instrumentalities, <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89</a></span>; <em>McDonald </em>v. <em>United States, supra; </em>and contraband, <em>Trupiano </em>v. <em>United States, </em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span>; <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span>.</p>
<p id="b350-6">The premise in <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>that government may not seize evidence simply for the purpose of proving crime has likewise been discredited. The requirement that the Government assert in addition some property interest in material it seizes has long been a fiction,<footnotemark>11</footnotemark> obscuring the reality that government has an interest in solving crime. <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>settled the proposition that it is reasonable, within the terms of the Fourth Amendment, to conduct otherwise permissible searches for the purpose of obtaining evidence which would aid in apprehending and convicting criminals. The requirements of the Fourth Amendment can secure the same protection of privacy <page-number citation-index="1" label="307">*307</page-number>whether the search is for “mere evidence” or for fruits, instrumentalities or contraband. There must, of course, be a nexus — automatically provided in the case of fruits, instrumentalities or contraband — between the item to be seized and criminal behavior. Thus in the case of “mere evidence,” probable cause must be examined in terms of cause to believe that the evidence sought will aid in a particular apprehension or conviction. In so doing, consideration of police purposes will be required. Cf. <em>Kremen </em>v. <em>United States, </em><span class="citation" data-id="8931353"><a href="/opinion/8940894/kremen-v-united-states/" aria-description="Citation for case: Kremen v. United States">353 U. S. 346</a></span>. But no such problem is presented in this case. The clothes found in the washing machine matched the description of those worn by the robber and the police therefore could reasonably believe that the items would aid in the identification of the culprit.</p>
<p id="b351-5">The remedy of suppression, moreover, which made possible protection of privacy from unreasonable searches without regard to proof of a superior property interest, likewise provides the procedural device necessary for allowing otherwise permissible searches and seizures conducted solely to obtain evidence of crime. For just as the suppression of evidence does not entail a declaration of superior property interest in the person aggrieved, thereby enabling him to suppress evidence unlawfully seized despite his inability to demonstrate such an interest (as with fruits, instrumentalities, contraband), the refusal to suppress evidence carries no declaration of superior property interest in the State, and should thereby enable the State to introduce evidence lawfully seized despite its inability to demonstrate such an interest. And, unlike the situation at common law, the owner of property would not be rendered remediless if “mere evidence” could lawfully be seized to prove crime. For just as the suppression of evidence does not in itself necessarily entitle the aggrieved person to its return (as, for example, contraband), the introduction of “mere evidence” does not in <page-number citation-index="1" label="308">*308</page-number>itself entitle the State to its retention. Where public officials “unlawfully seize <em>or hold </em>a citizen’s realty or chattels, recoverable by appropriate action at law or in equity . . . ,” the true owner may “bring his possessory action to reclaim that which is wrongfully withheld.” <em>Land </em>v. <em>Dollar, </em><span class="citation" data-id="9419978"><a href="/opinion/104407/land-v-dollar/#738" aria-description="Citation for case: Land v. Dollar">330 U. S. 731, 738</a></span>. (Emphasis added.) See <em>Burdeau </em>v. <em>McDowell, </em><span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/#474" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465, 474</a></span>.</p>
<p id="b352-6">The survival of the <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>distinction is attributable more to chance than considered judgment. Legislation has helped perpetuate it. Thus, Congress has never authorized the issuance of search warrants for the seizure of mere evidence of crime. See <em>Davis </em>v. <em>United States, </em><span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/#606" aria-description="Citation for case: Davis v. United States">328 U. S. 582, 606</a></span> (dissenting opinion of Mr. Justice Frankfurter). Even in the Espionage Act of 1917, where Congress for the first time granted general authority for the issuance of search warrants, the authority was limited to fruits of crime, instrumentalities, and certain contraband. <span class="citation no-link">40 Stat. 228</span>. <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>concluded, needlessly it appears, that the Constitution virtually limited searches and seizures to these categories.<footnotemark>12</footnotemark> After <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span>, </em>pressure <page-number citation-index="1" label="309">*309</page-number>to test this conclusion was slow to mount. Rule 41 (b) of the Federal Rules of Criminal Procedure incorporated the <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>categories as limitations on federal authorities to issue warrants, and <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, only recently made the “mere evidence” rule a problem in the state courts. Pressure against the rule in the federal courts has taken the form rather of broadening the categories of evidence subject to seizure, thereby creating considerable confusion in the law. See, <em>e. g., </em>Note, 54 Geo. L. J. 593, 607-621 (1966).</p>
<p id="b353-5">The rationale most frequently suggested for the rule preventing the seizure of evidence is that “limitations upon the fruit to be gathered tend to limit the quest itself.” <em>United States </em>v. <em>Poller, </em><span class="citation" data-id="1476321"><a href="/opinion/1476321/united-states-v-poller/#914" aria-description="Citation for case: United States v. Poller">43 F. 2d 911, 914</a></span> (C. A. 2d Cir. 1930). But privacy “would be just as well served by a restriction on search to the even-numbered days of the month. . . . And it would have the extra advantage of avoiding hair-splitting questions . . . .” Kaplan, <em>op. cit. supra, </em>at 479. The “mere evidence” limitation has spawned exceptions so numerous and confusion so great, in fact, that it is questionable whether it affords meaningful protection. But if its rejection does enlarge the area of permissible searches, the intrusions are nevertheless made after fulfilling the probable cause and particularity requirements of the Fourth Amendment and after the intervention of “a neutral and detached magis<page-number citation-index="1" label="310">*310</page-number>trate . . . .” <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span>. The Fourth Amendment allows intrusions upon privacy-under these circumstances, and there is no viable reason to distinguish intrusions to secure “mere evidence” from intrusions to secure fruits, instrumentalities, or contraband.</p>
<p id="b354-4">The judgment of the Court of Appeals is</p>
<p id="b354-5">
<em>Reversed.</em>
</p>
<judges id="b354-6">Mr. Justice Black concurs in the result.</judges>
<footnote label="1">
<p id="b340-7"> <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#154" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 154</a></span>; see also <em>Gouled </em>v. <em>United States, </em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span>; <em>United States </em>v. <em>Lefkowitz, </em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#465" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 465-466</a></span>; <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#64" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 64, n. 6</a></span>; <em>Abel </em>v. <em>United States, </em><span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#234" aria-description="Citation for case: Abel v. United States">362 U. S. 217, 234-235</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b340-8"> Hayden did not appeal from his conviction. He first sought relief by an application under the Maryland Post Conviction Procedure Act which was denied without hearing. The Maryland Court of Appeals reversed and remanded for a hearing. <span class="citation" data-id="1990408"><a href="/opinion/1990408/hayden-v-warden-of-the-maryland-penitentiary/" aria-description="Citation for case: Hayden v. Warden of the Maryland Penitentiary">233 Md. 613</a></span>, <span class="citation" data-id="1990408"><a href="/opinion/1990408/hayden-v-warden-of-the-maryland-penitentiary/" aria-description="Citation for case: Hayden v. Warden of the Maryland Penitentiary">195 A. 2d 692</a></span>. The trial court denied relief after hearing, concluding “that the search of his home and the seizure of the articles in question were proper.” His application for federal habeas corpus relief resulted, after hearing in the District Court, in the same conclusion.</p>
</footnote>
<footnote label="3">
<p id="b341-7"> The State claims that, since Hayden failed to raise the search and seizure question at trial, he deliberately bypassed state remedies and should be denied an opportunity to assert his claim in federal court. See <em>Henry </em>v. Mississippi, <span class="citation" data-id="9422929"><a href="/opinion/106962/henry-v-mississippi/" aria-description="Citation for case: Henry v. Mississippi">379 U. S. 443</a></span>; <em>Fay </em>v. <em>Noia, </em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/" aria-description="Citation for case: Fay v. Noia">372 U. S. 391</a></span>. Whether or not the Maryland Court of Appeals actually intended, when it reversed the state trial court’s denial of post-conviction relief, that Hayden be afforded a hearing on the merits of his claim, it is clear that the trial court so understood the order of the Court of Appeals. A hearing was held in the state courts, and the claim denied on the merits. In this circumstance, the Fourth Circuit was correct in rejecting the State’s deliberate-bypassing claim. The deliberate-bypass rule is applicable only “to an applicant who has deliberately by-passed the orderly procedure of the state courts <em>and in so doing has forfeited his state court remedies.” Fay </em>v. <em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/" aria-description="Citation for case: Fay v. Noia">Noia, supra,</a></span> </em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#438" aria-description="Citation for case: Fay v. Noia">372 U. S., at 438</a></span>. (Emphasis added.) But see <em>Nelson </em>v. <em>California, </em><span class="citation" data-id="268073"><a href="/opinion/268073/chester-nelson-v-people-of-the-state-of-california-robert-a-heinze/#82" aria-description="Citation for case: Chester Nelson v. People of the State of California,...">346 F. 2d 73, 82</a></span> (C. A. 9th Cir. 1965).</p>
</footnote>
<footnote label="4">
<p id="b341-8"> The state postconviction court found that Mrs. Hayden “gave the policeman permission to enter the home.” The federal habeas corpus court stated it “would be justified in accepting the findings <page-number citation-index="1" label="298">*298</page-number>of historical fact made by Judge Sodaro on that issue but concluded that resolution of the issue would be unnecessary, because the officers were “justified in entering and searching the house for the felon, for his weapons and for the fruits of the robbery.”</p>
</footnote>
<footnote label="5">
<p id="b344-8"> The officer was asked in the District Court whether he found the money. He answered that he did not, and stated: “By the time I had gotten down into the basement I heard someone say upstairs, 'There’s a man up here.’ ” He was asked: “What did you do then?” and answered: “By this time I had already discovered some clothing which fit the description of the clothing worn by the subject that we were looking for . . . .” It is clear from the record and from the findings that the weapons were found after or at the same time the police found Hayden.</p>
</footnote>
<footnote label="6">
<p id="b344-9"> <em>People </em>v. <em>Thayer, </em><span class="citation" data-id="1421285"><a href="/opinion/1421285/people-v-thayer/" aria-description="Citation for case: People v. Thayer">63 Cal. 2d 635</a></span>, <span class="citation" data-id="1421285"><a href="/opinion/1421285/people-v-thayer/" aria-description="Citation for case: People v. Thayer">408 P. 2d 108</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./384/908/">384 U. S. 908</a></span>; <em>State </em>v. <em>Bisaccia, </em>45 N. J. 504, <span class="citation" data-id="1923442"><a href="/opinion/1923442/state-v-bisaccia/" aria-description="Citation for case: State v. Bisaccia">213 A. 2d 185</a></span>. Compare <em>United States </em>v. <em>Poller, </em><span class="citation" data-id="1476321"><a href="/opinion/1476321/united-states-v-poller/#914" aria-description="Citation for case: United States v. Poller">43 F. 2d 911, 914</a></span> (C. A. 2d Cir. 1930).</p>
</footnote>
<footnote label="7">
<p id="b344-10"> <em>E. g., </em>Chafee, The Progress of the Law, 1919-1922, <span class="citation no-link">35 Harv. L. Rev. 673</span> (1922); Kamisar, The Wiretapping-Eavesdropping Problem: A Professor’s View, <span class="citation no-link">44 Minn. L. Rev. 891</span>, 914-918 (1960); Kaplan, Search and Seizure: A No-Man’s Land in the Criminal Law, <span class="citation no-link">49 Calif. L. Rev. 474</span>, 478 (1961); Comment, 45 N. C. L. Rev. 512 (1967); Comment, 66 Col. L. Rev. 355 (1966); Comment, <span class="citation no-link">20 U. Chi. L. Rev. 319</span> (1953); Comment, 31 Yale L. J. 518 (1922). Compare, <em>e. g., </em>Fraenkel, Concerning Searches and Seizures, <span class="citation no-link">34 Harv. L. Rev. 361</span> (1921); Note, 54 Geo. L. J. 593 (1966).</p>
</footnote>
<footnote label="8">
<p id="b345-7"> This Court has approved the seizure and introduction of items having only evidential value without, however, considering the validity of the distinction rejected today. See <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span>; <em>Cooper </em>v. <em>California, </em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span>.</p>
</footnote>
<footnote label="9">
<p id="b345-10"> <em>E. g., Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 481-485</a></span>; <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#724" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717, 724-729</a></span>; <em>Frank </em>v. <em>Maryland, </em><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#363" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360, 363-365</a></span>. See generally Lasson, The History and Development of the Fourth Amendment to the United States Constitution (1937); Landynski, Search and Seizure and the Supreme Court (1966).</p>
</footnote>
<footnote label="10">
<p id="b348-7"> Both <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>and <em><span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">Adams</a></span> </em>were written by Justice Day, and joined by several of the same Justices, including Justice Holmes.</p>
</footnote>
<footnote label="11">
<p id="b350-7"> At common law the Government did assert a superior property interest when it searched lawfully for stolen property, since the procedure then followed made it necessary that the true owner swear that his goods had been taken. But no such procedure need be followed today; the Government may demonstrate probable cause and lawfully search for stolen property even though the true owner is unknown or unavailable to request and authorize the Government to assert his interest. As to instrumentalities, the Court in <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>allowed their seizure, not because the Government had some property interest in them (under the ancient, fictitious forfeiture theory), but because they could be used to perpetrate further crime. <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#309" aria-description="Citation for case: Gouled v. United States">255 U. S., at 309</a></span>. The same holds true, of course, for “mere evidence”; the prevention of crime is served at least as much by allowing the Government to identify and capture the criminal, as it is by allowing the seizure of his instrumentalities. Finally, contraband is indeed property in which the Government holds a superior interest, but only because the Government decides to vest such an interest in itself. And while there may be limits to what may be declared contraband, the concept is hardly more than a form through which the Government seeks to prevent and deter crime.</p>
</footnote>
<footnote label="12">
<p id="b352-7"> <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>was decided on certified questions. The only question which referred to the Espionage Act of 1917 stated: “Are papers of . . . evidential value . . . , when taken under search warrants issued pursuant to Act of June 15, 1917, from the house or office of the person so suspected, — seized and taken in violation of the 4th amendment?” <em>Gouled </em>v. <em>United States, </em>No. 250, Oct. Term, 1920, Certificate, p. 4. Thus the form in which the case was certified made it difficult if not impossible “to limit the decision to the sensible proposition of statutory construction, that Congress had not as yet authorized the seizure of purely evidentiary material.” Chafee, <em>op. cit. supra, </em>at 699. The Government assumed the validity of petitioner’s argument that <em>Entick </em>v. <em>Carrington, Boyd </em>v. <em>United States, </em>and other authorities established the constitutional illegality of seizures of private papers for use as evidence. <em>Gouled </em>v. <em>United States, supra, </em>Brief for the United States, p. 50. It argued, complaining of the absence of a record, that the papers introduced in evidence were instrumentalities of crime. The Court ruled that the <page-number citation-index="1" label="309">*309</page-number>record before it revealed no government interest in the papers other than as evidence against the accused. <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#311" aria-description="Citation for case: Gouled v. United States">255 U. S., at 311</a></span>.</p>
<p id="b353-7">Significantly, <em>Entick </em>v. <em>Carrington </em>itself has not been read by the English courts as making unlawful the seizure of all papers for use as evidence. See <em>Dillon </em>v. <em>O’Brien, </em>20 L. R. Ir. 300; <em>Elias </em>v. <em>Pasmore, </em>[1934] 2 K. B. 164. Although <em>Dillon, </em>decided in 1887, involved instrumentalities, the court did not rely on this fact, but rather on “the interest which the State has in a person guilty (or reasonably believed to be guilty) of a crime being brought to justice . . . .” 20 L. R. Ir., at 317.</p>
</footnote>
</opinion>
```

---
