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

## GROUP: content/cases/United States v. Rideau.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Rideau"
type: case
citation: "969 F.2d 1572 (1992)"
parallel_cite: ""
neutral_cite: "1992 U.S. App. LEXIS 18693; 1992 WL 195842"
court: "U.S. Court of Appeals, 5th Circuit"
court_level: coa
circuit: 5th
year: 1992
date_decided: 1992-08-14
docket: ""
authority_weight: "Binding in-circuit — 5th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 1992-08-14
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Rideau
  varies_by_point: false
  scope_note: "Good law; en banc. Public-welfare/community-caretaking function applied to an impaired person in the roadway."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/587275/united-states-v-izeal-rideau-jr/"
  cluster_id: 587275
  opinion_id: 587275
  identity_checked: false
homes:
  - page: "[[Community Caretaking]]"
    role: "Key — Progeny"
related: ["[[United States v. Garner]]", "[[Cady v. Dombrowski]]", "[[Terry v. Ohio]]", "[[Adams v. Williams]]", "[[Caniglia v. Strom]]"]
aliases: ["United States v. Izeal Rideau, Jr.", "United States v. Rideau (5th Cir. 1992)"]
tags: ["case", "fourth-amendment", "community-caretaking", "public-welfare", "investigative-detention", "persons-in-public", "fifth-circuit"]
holding: "Police serve a public-welfare/community-caretaking function by removing apparently intoxicated people from the public streets, and an officer is warranted in stopping to check on the condition of an impaired person standing in the roadway; on these facts the en banc court held the stop and protective patdown reasonable under the Fourth Amendment."
lake:
  record_id: United States v. Rideau
  status: under_review
  projected_at: 2026-07-09
---

# United States v. Rideau

*969 F.2d 1572 (5th Cir. 1992) (en banc)* · U.S. Court of Appeals, 5th Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Around 10:30 p.m. in a high-crime area of Beaumont, Texas, Officer Ellison saw a man wearing dark clothing standing in the road. Ellison flashed his bright lights to encourage the man to leave the street; the man turned, stepped toward the shoulder, and stumbled, leading Ellison to suspect he was drunk. Ellison pulled over and approached to investigate and check on him. When Ellison asked the man's name, he appeared nervous, did not answer, and began to back away; Ellison closed the gap and patted the man's outer pants pocket, where he felt a firearm. The man — Izeal Rideau, a convicted felon — was arrested and charged with being a felon in possession (18 U.S.C. § 922(g)(1)). A panel had reversed his conviction, and the Fifth Circuit reheard the case [[Reading and Citing Cases#en-banc|en banc]].

## Issue
Whether an officer acted reasonably under the Fourth Amendment in stopping an apparently intoxicated man standing in a roadway at night to check on his condition, and then conducting a limited protective patdown when the man backed away.

## Rule
Police actions in caring for an impaired person on the public streets serve a recognized public-welfare/community-caretaking function. "Police have long served the public welfare by removing intoxicated people from the public streets, where they pose a hazard to themselves and others." — 969 F.2d at 1574 (citing *Powell v. Texas* and *Cady v. Dombrowski*'s "community caretaking functions"). ^pin-1574

Accordingly, "Officer Ellison was warranted in stopping to investigate the situation and check on the man's condition." — [*Id.*](https://www.courtlistener.com/opinion/587275/united-states-v-izeal-rideau-jr/#:~:text=Officer%20Ellison%20was%20warranted%20in) ^pin-1574a

A lawful detention is not a license to frisk, but the protective patdown here was supported by specific and articulable facts: "A reasonably prudent man in Ellison's situation could have believed that his safety and that of his partner was in danger." — [*Id.*](https://www.courtlistener.com/opinion/587275/united-states-v-izeal-rideau-jr/#:~:text=A%20reasonably%20prudent%20man%20in%20Ellison%27s) ^pin-1574b

The court added that "police officers must have specific and articulable facts indicating that their safety is in danger to justify a patdown." — 969 F.2d at 1576. ^pin-1576

## Application
Ellison was justified in stopping because Rideau, apparently intoxicated and standing in the roadway at night, presented both a possible public-intoxication offense and a public-welfare concern that warranted checking on his condition. The subsequent patdown was supported by specific and articulable facts: after the lawful detention, in a high-crime area where weapons were common, Rideau backed away when asked his name — conduct a reasonably prudent officer could read as gaining room to draw a weapon. The single, spontaneous touch of the front pants pocket was a limited and tailored response to that safety concern.

## Conclusion
The [[Reading and Citing Cases#en-banc|en banc]] court held the officer's actions reasonable under the Fourth Amendment and affirmed the denial of suppression and the conviction, reversing the panel.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 5th Cir.** (en banc).
- *Rideau* is a leading progeny illustration of the public-welfare/community-caretaking function applied to a **person** (not a vehicle): it grounds the caretaking stop in [[Cady v. Dombrowski]] and is cited by [[United States v. Garner]] (10th Cir.) for extending a caretaking detention based on an apparently impaired person's behavior.
- [[Caniglia v. Strom]] (2021) barred a *freestanding* community-caretaking entry into the **home**; that home-limited holding does not disturb *Rideau*'s rule for an impaired person in public.

## Appears on
- [[Community Caretaking]] — *Key — Progeny*

## Sources
- *United States v. Rideau*, 969 F.2d 1572 (5th Cir. 1992) (en banc) — https://www.courtlistener.com/opinion/587275/united-states-v-izeal-rideau-jr/ — pinpoints: 1574, 1576.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0c7487f3c3f20214", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "969 F.2d 1572 (1992)", "court": "U.S. Court of Appeals, 5th Circuit", "neutral_cite": "1992 U.S. App. LEXIS 18693; 1992 WL 195842", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Rideau", "year": "1992"}}
{"assertion_id": "330d7c7931af43f1", "dimension": "support", "kind": "home_role", "locator": {"home": "Community Caretaking"}, "payload": {"home": "Community Caretaking", "role": "Key — Progeny", "title": "United States v. Rideau"}}
{"assertion_id": "c0e4a12671176c10", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Police serve a public-welfare/community-caretaking function by removing apparently intoxicated people from the public streets, and an officer is warranted in stopping to check on the condition of an impaired person standing in the roadway; on these facts the en banc court held the stop and protective patdown reasonable under the Fourth Amendment.", "title": "United States v. Rideau"}}
{"assertion_id": "ef3f058efdf663f8", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 5th Cir.", "title": "United States v. Rideau"}}
{"assertion_id": "f61daaf18ea376bc", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1992-08-14", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Rideau", "field_i_validity": "good_law", "scope_note": "Good law; en banc. Public-welfare/community-caretaking function applied to an impaired person in the roadway.", "title": "United States v. Rideau", "varies_by_point": "false"}}
```

### lake record — United States v. Rideau

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Rideau",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Izeal Rideau, Jr.",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Izeal RIDEAU, Jr., Defendant-Appellant",
    "input_case_name": "United States v. Rideau",
    "court": "U.S. Court of Appeals, 5th Circuit",
    "court_id": "ca5",
    "court_level": "coa",
    "circuit": "5th",
    "state": null,
    "date_decided": "1992-08-14",
    "year": 1992,
    "docket": null,
    "cluster_id": 587275,
    "lead_opinion_id": 587275,
    "sibling_ids": [
      587275,
      9483168,
      9483169
    ],
    "absolute_url": "/opinion/587275/united-states-v-izeal-rideau-jr/",
    "identity_method": "pending",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 572438,
        "score": 20,
        "case_name": "United States v. Izeal Rideau, Jr."
      }
    ],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "969 F.2d 1572",
      "volume": "969",
      "reporter": "F.2d",
      "page": "1572",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "1992 U.S. App. LEXIS 18693",
        "volume": "1992",
        "reporter": "U.S. App. LEXIS",
        "page": "18693",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1992 WL 195842",
        "volume": "1992",
        "reporter": "WL",
        "page": "195842",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "969 F.2d 1572",
        "volume": "969",
        "reporter": "F.2d",
        "page": "1572",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1992 U.S. App. LEXIS 18693",
        "volume": "1992",
        "reporter": "U.S. App. LEXIS",
        "page": "18693",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1992 WL 195842",
        "volume": "1992",
        "reporter": "WL",
        "page": "195842",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "969 F.2d 1572",
    "official_selection": {
      "court_class": "coa",
      "selected": "969 F.2d 1572",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1574",
      "page": null,
      "quote": "--- # United States v. Rideau *969 F.2d 1572 (5th Cir. 1992) (en banc)* \u00b7 U.S. Court of Appeals, 5th Circuit \u00b7 **Binding in-circuit \u2014 5th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Around 10:30 p.m. in a high-crime area of Beaumont, Texas, Officer Ellison saw a man wearing dark clothing standing in the road. Ellison flashed his bright lights to encourage the man to leave the street; the man turned, stepped toward the shoulder, and stumbled, leading Ellison to suspect he was drunk. Ellison pulled over and approached to investigate and check on him. When Ellison asked the man's name, he appeared nervous, did not answer, and began to back away; Ellison closed the gap and patted the man's outer pants pocket, where he felt a firearm. The man \u2014 Izeal Rideau, a convicted felon \u2014 was arrested and charged with being a felon in possession (18 U.S.C. \u00a7 922(g)(1)). A panel had reversed his conviction, and the Fifth Circuit reheard the case en banc. ## Issue Whether an officer acted reasonably under the Fourth Amendment in stopping an apparently intoxicated man standing in a roadway at night to check on his condition, and then conducting a limited protective patdown when the man backed away. ## Rule Police actions in caring for an impaired person on the public streets serve a recognized public-welfare/community-caretaking function.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1574a",
      "page": null,
      "quote": "Officer Ellison was warranted in stopping to investigate the situation and check on the man's condition.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 13804,
      "fragment": "#:~:text=Officer%20Ellison%20was%20warranted%20in",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-1574b",
      "page": null,
      "quote": "A reasonably prudent man in Ellison's situation could have believed that his safety and that of his partner was in danger.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 14107,
      "fragment": "#:~:text=A%20reasonably%20prudent%20man%20in%20Ellison%27s",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-1576",
      "page": null,
      "quote": "police officers must have specific and articulable facts indicating that their safety is in danger to justify a patdown.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 23241
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1992-08-14",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Rideau",
    "varies_by_point": false,
    "scope_note": "Good law; en banc. Public-welfare/community-caretaking function applied to an impaired person in the roadway.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Lionel Alexander v. City of Round Rock",
          "cluster_id": 4384027,
          "cite": [
            "854 F.3d 298",
            "2017 U.S. App. LEXIS 6692",
            "2017 WL 1393702"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tosh Toussaint",
          "cluster_id": 4259133,
          "cite": [
            "838 F.3d 503",
            "2016 U.S. App. LEXIS 17357",
            "2016 WL 5314862"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Marcus Wadley",
          "cluster_id": 717593,
          "cite": [
            "83 F.3d 108",
            "1996 WL 226785"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Rene Ponce",
          "cluster_id": 656578,
          "cite": [
            "8 F.3d 989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Robert Earl Sanders",
          "cluster_id": 607884,
          "cite": [
            "994 F.2d 200",
            "1993 U.S. App. LEXIS 14818",
            "1993 WL 211684"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Peterson v. City of Fort Worth, Tex.",
          "cluster_id": 69197,
          "cite": [
            "588 F.3d 838",
            "2009 U.S. App. LEXIS 25183",
            "2009 WL 3818826"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wright v. State",
          "cluster_id": 1870455,
          "cite": [
            "7 S.W.3d 148",
            "1999 Tex. Crim. App. LEXIS 146",
            "1999 WL 1178566"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
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
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michelletti",
          "cluster_id": 6205,
          "cite": [
            "13 F.3d 838",
            "1994 U.S. App. LEXIS 1229",
            "1994 WL 19106"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Shiffermiller",
          "cluster_id": 4592777,
          "cite": [
            "302 Neb. 245",
            "922 N.W.2d 763"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bradley Lee Winters v. Robert Adams and Craig Prahm",
          "cluster_id": 773752,
          "cite": [
            "254 F.3d 758",
            "2001 U.S. App. LEXIS 14157",
            "2001 WL 704426"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lizette Vargas v. City of Philadelphia",
          "cluster_id": 2794598,
          "cite": [
            "783 F.3d 962",
            "2015 U.S. App. LEXIS 6331",
            "2015 WL 1741504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Macias v. Raul A. (Unknown), Badge No. 153",
          "cluster_id": 6480,
          "cite": [
            "23 F.3d 94",
            "1994 U.S. App. LEXIS 14792",
            "1994 WL 232885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Klare v. State",
          "cluster_id": 2335254,
          "cite": [
            "76 S.W.3d 68",
            "2002 WL 369940"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Roch",
          "cluster_id": 5959,
          "cite": [
            "5 F.3d 894",
            "1993 U.S. App. LEXIS 27282",
            "1993 WL 413854"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Guy",
          "cluster_id": 1251064,
          "cite": [
            "492 N.W.2d 311",
            "172 Wis. 2d 86",
            "1992 Wisc. LEXIS 763"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Jeffrey Dana Kurth",
          "cluster_id": 4472335,
          "cite": [
            "813 N.W.2d 270",
            "2012 WL 1648253",
            "2012 Iowa Sup. LEXIS 47"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Regon Hill",
          "cluster_id": 2676368,
          "cite": [
            "752 F.3d 1029",
            "2014 WL 2219064",
            "2014 U.S. App. LEXIS 9960"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Terry Lee Coffman",
          "cluster_id": 4509998,
          "cite": [
            "914 N.W.2d 240"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth D. Evans",
          "cluster_id": 607901,
          "cite": [
            "994 F.2d 317",
            "1993 WL 143866"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fontenot v. Cormier",
          "cluster_id": 7279,
          "cite": [
            "56 F.3d 669",
            "1995 U.S. App. LEXIS 15158",
            "1995 WL 366232"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Eleanor Keller v. Attala County",
          "cluster_id": 4728903,
          "cite": [
            "952 F.3d 216"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alvarez",
          "cluster_id": 6043,
          "cite": [
            "6 F.3d 287",
            "1993 WL 426048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. State",
          "cluster_id": 1448073,
          "cite": [
            "854 P.2d 688",
            "1993 Wyo. LEXIS 105",
            "1993 WL 195796"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alvarez",
          "cluster_id": 6623468,
          "cite": [
            "40 F.4th 339"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salazar v. State",
          "cluster_id": 1528589,
          "cite": [
            "893 S.W.2d 138",
            "1995 Tex. App. LEXIS 65",
            "1995 WL 19359"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas",
          "cluster_id": 4883758,
          "cite": [
            "997 F.3d 603"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Rideau:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(587275 OR 9483168 OR 9483169) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca5)",
        "reviewed": 21,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 5,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 21,
        "triage_read": 5,
        "triage_snippet_classified": 16
      },
      "lane2_top_cited": {
        "query": "cites:(587275 OR 9483168 OR 9483169)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00JnM9NDYxNjUxNyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28587275+OR+9483168+OR+9483169%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(587275 OR 9483168 OR 9483169)",
        "reviewed": 2,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 2,
        "triage_read": 0,
        "triage_snippet_classified": 2
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(587275 OR 9483168 OR 9483169)",
    "indexed_citing_opinions": 69,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 587275,
        "count": 47,
        "count_source": "search"
      },
      {
        "opinion_id": 9483168,
        "count": 26,
        "count_source": "search"
      },
      {
        "opinion_id": 9483169,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 157,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-rideau.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU4OTQ3Nzkmcz00NTA5OTk4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28587275+OR+9483168+OR+9483169%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 587275,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 107750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 111477,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 112239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 112384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 1122661,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 587275,
        "cited_id": 1187451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 532013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 545167,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 1141153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 2290134,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 8994043,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 9090740,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 9423233,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 9423752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 9424935,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 9427853,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 9431933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 9475728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 9531694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483169,
        "cited_id": 9552492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 532013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 551302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 557811,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 572438,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9423752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9424935,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9425411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9427002,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9427183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9430099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9431641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9431933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9475728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9842054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9483168,
        "cited_id": 9883102,
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
    "date_created": "2026-07-06T02:28:43Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:29:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:29:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:32:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:29:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Rideau

```
<p class="case_cite"><span class="citation" data-id="9483168"><a href="/opinion/587275/united-states-v-izeal-rideau-jr/" aria-description="Citation for case: United States v. Izeal Rideau, Jr.">969 F.2d 1572</a></span></p>
    <p class="parties">UNITED STATES of America, Plaintiff-Appellee,<br>v.<br>Izeal RIDEAU, Jr., Defendant-Appellant.</p>
    <p class="docket">No. 91-4172.</p>
    <p class="court">United States Court of Appeals,<br>Fifth Circuit.</p>
    <p class="date">Aug. 14, 1992.</p>
    <div class="prelims">
      <p class="indent">Donald E. Sample, Beaumont, Tex.  (Court-appointed), for defendant-appellant.</p>
      <p class="indent">Paul Naman, Kerry M. Klintworth, Asst. U.S. Attys., Bob Wortham, U.S. Atty., Beaumont, Tex., for plaintiff-appellee.</p>
      <p class="indent">Appeal from the United States District Court for the Eastern District of Texas.</p>
      <p class="indent">Before POLITZ, Chief Judge, GOLDBERG, KING, GARWOOD, JOLLY, HIGGINBOTHAM, DAVIS, JONES, SMITH, DUHE, WIENER, BARKSDALE, EMILIO M. GARZA, DeMOSS, Circuit Judges.</p>
      <p class="indent">PATRICK E. HIGGINBOTHAM, Circuit Judge:</p>
    </div>
    <div class="num" id="p1">
      <span class="num">1</span>
      <p class="indent">This case requires us to consider the reasonableness of a police officer's actions in an encounter with a person he suspected was intoxicated, standing in the road, at night, in a high crime area.   A panel of this court held that the officer violated the Fourth Amendment when he reached out and touched the pants pocket of the individual and discovered a gun.   We granted rehearing en banc, and now hold that the officer's actions were reasonable under the Fourth Amendment.</p>
    </div>
    <p>I.</p>
    <div class="num" id="p2">
      <span class="num">2</span>
      <p class="indent">At about 10:30 one night in July of 1989,<a class="footnote" href="#fn1" id="fn1_ref">1</a> police officer Jimmy Ellison and his partner were driving toward the intersection of Bonham Street and Martin Luther King Boulevard, a high crime area in Beaumont, Texas, where people often carried weapons and transacted drug deals on the street, and where public drunkenness was a recurrent problem.   As he drove up Bonham Street, officer Ellison saw a man wearing dark clothing standing in the road.   Ellison flashed his bright lights to see the man better and to encourage him to get out of the street.   The man turned to step out of the roadway and stumbled as he moved toward the shoulder.   Ellison suspected that he was drunk.   He pulled over, got out of his car, and approached the man to investigate.   Ellison asked the man his name.   He seemed nervous.   When the man did not answer but instead began to back away, Ellison immediately closed the gap and reached out to pat the man's outer clothing.   Ellison's quick move was to see if he had any weapons that could harm him or his partner.   The first place he touched was the man's right front pants pocket, where he felt a firearm.   He shouted "gun" to his partner and grabbed the man's arm.   Ellison and his partner then put the man up against the patrol car, removed the gun from his pocket, handcuffed him and placed him under arrest.</p>
    </div>
    <div class="num" id="p3">
      <span class="num">3</span>
      <p class="indent">The man was later identified as Izeal Rideau, previously convicted of robbery and burglary in Texas state court.   Rideau was charged with possession of a firearm by a convicted felon, in violation of <span class="citation no-link">18 U.S.C. &#167; 922</span>(g)(1).   Before his trial, he moved to suppress the gun, arguing that Ellison violated his Fourth Amendment rights when he stopped him and patted his pants pocket.   The district court denied the motion to suppress, and a jury convicted Rideau.   A panel of this court reversed Rideau's conviction on appeal, however, finding that although the officers were justified in detaining Rideau, they had failed to provide specific and articulable facts to justify a patdown, and thereby violated the Fourth Amendment's prohibition on unreasonable searches and seizures, <span class="citation" data-id="572438"><a href="/opinion/572438/united-states-v-izeal-rideau-jr/" aria-description="Citation for case: United States v. Izeal Rideau, Jr.">949 F.2d 718</a></span>.   We granted rehearing en banc to consider the issue further.</p>
    </div>
    <p>II.</p>
    <div class="num" id="p4">
      <span class="num">4</span>
      <p class="indent">In Terry v. Ohio, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span> (1968), the Supreme Court explained the limits that the Fourth Amendment imposes on the conduct of police officers on the beat.   First, it recognized that effective crime prevention and detection requires that officers be allowed to detain individuals briefly on the street even though there is no probable cause to arrest them.   To justify such brief detentions, the officers must have a reasonable suspicion that criminal activity is afoot.   The showing required to demonstrate "reasonable suspicion" is considerably less than that which is necessary to prove probable cause.   In this context, the Fourth Amendment requires only some minimal level of objective justification for the officer's actions, measured in light of the totality of the circumstances.   See United States v. Sokolow, <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#6" aria-description="Citation for case: United States v. Sokolow">490 U.S. 1, 6-8</a></span>, <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#1585" aria-description="Citation for case: United States v. Sokolow">109 S.Ct. 1581, 1585</a></span>, <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">104 L.Ed.2d 1</a></span> (1989).</p>
    </div>
    <div class="num" id="p5">
      <span class="num">5</span>
      <p class="indent">Second, the Court recognized that law enforcement officers need to protect themselves and the public at large from violence that may ensue in the course of such encounters.   It therefore held that if police officers are justified in believing that the individuals whose suspicious behavior they are investigating at close range are armed and presently dangerous to the officers or to others, they may conduct a limited protective search for concealed weapons.  Terry, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 24</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#1881" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. at 1881</a></span>;  Adams v. Williams, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U.S. 143, 146</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#1923" aria-description="Citation for case: Adams v. Williams">92 S.Ct. 1921, 1923</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">32 L.Ed.2d 612</a></span> (1972).   An officer need not be certain that an individual is armed;  the issue is whether a reasonably prudent man could believe, based on "specific and articulable facts," that his safety or that of others is in danger.  <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">Id.</a></span> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 27</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#1883" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. at 1883</a></span>;  Maryland v. Buie, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#332" aria-description="Citation for case: Maryland v. Buie">494 U.S. 325, 332</a></span>, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#1097" aria-description="Citation for case: Maryland v. Buie">110 S.Ct. 1093, 1097</a></span>, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">108 L.Ed.2d 276</a></span> (1990).</p>
    </div>
    <div class="num" id="p6">
      <span class="num">6</span>
      <p class="indent">In assessing the reasonableness of an officer's actions, "it is imperative that the facts be judged against an objective standard:  would the facts available to the officer at the moment of the seizure or the search 'warrant a man of reasonable caution in the belief' that the action taken was appropriate?".  Terry, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 22</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#1880" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. at 1880</a></span> (citations omitted).   The officer's state of mind, or his stated justification for his actions, is not the focus of our inquiry.   See Maryland v. Macon, <span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/#470" aria-description="Citation for case: Maryland v. MacOn">472 U.S. 463, 470-71</a></span>, <span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/#2782" aria-description="Citation for case: Maryland v. MacOn">105 S.Ct. 2778, 2782-83</a></span>, <span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/" aria-description="Citation for case: Maryland v. MacOn">86 L.Ed.2d 370</a></span> (1985);  Scott v. United States, <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#138" aria-description="Citation for case: Scott v. United States">436 U.S. 128, 138-39</a></span>, <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#1723" aria-description="Citation for case: Scott v. United States">98 S.Ct. 1717, 1723-24</a></span>, <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/" aria-description="Citation for case: Scott v. United States">56 L.Ed.2d 168</a></span> (1978);  United States v. Colin, <span class="citation" data-id="557811"><a href="/opinion/557811/united-states-v-antonio-h-colin/#678" aria-description="Citation for case: United States v. Antonio H. Colin">928 F.2d 676, 678</a></span> (5th Cir.1991).   As long as all the facts and circumstances, viewed objectively, support the officer's decisions, the Fourth Amendment is satisfied.   We must attempt to put ourselves in the shoes of a reasonable police officer as he or she approaches a given situation and assesses the likelihood of danger in a particular context.</p>
    </div>
    <div class="num" id="p7">
      <span class="num">7</span>
      <p class="indent">There is no serious question that Ellison had reasonable suspicion to detain Rideau.   Rideau had been standing in the roadway at night in a high crime area, where public drunkenness was common, and stumbled out of the road only when Ellison flashed his lights at him.   Ellison had reason to believe that Rideau was drunk.   Since public intoxication is a criminal offense under Texas law, see Tex.  Penal Code &#167; 42.08 (Vernon's 1991), the officers had adequate grounds for a stop.   In any event, Terry recognizes that "[e]ncounters are initiated by the police for a wide variety of purposes, some of which are wholly unrelated to a desire to prosecute for crime."  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#13" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 13</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#1876" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. at 1876</a></span>.   Police have long served the public welfare by removing intoxicated people from the public streets, where they pose a hazard to themselves and others.   See Powell v. Texas, <span class="citation" data-id="9883102"><a href="/opinion/107750/powell-v-texas/" aria-description="Citation for case: Powell v. Texas">392 U.S. 514</a></span>, <span class="citation" data-id="9883102"><a href="/opinion/107750/powell-v-texas/" aria-description="Citation for case: Powell v. Texas">88 S.Ct. 2145</a></span>, <span class="citation" data-id="9883102"><a href="/opinion/107750/powell-v-texas/" aria-description="Citation for case: Powell v. Texas">20 L.Ed.2d 1254</a></span> (1968);  see also Cady v. Dombrowski, <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski">413 U.S. 433, 441</a></span>, <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#2528" aria-description="Citation for case: Cady v. Dombrowski">93 S.Ct. 2523, 2528</a></span>, <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">37 L.Ed.2d 706</a></span> (1973) (describing "community caretaking functions" that police officers serve).   Officer Ellison was warranted in stopping to investigate the situation and check on the man's condition.</p>
    </div>
    <div class="num" id="p8">
      <span class="num">8</span>
      <p class="indent">We also find that Ellison's decision to reach out and pat Rideau's pocket rested on specific and articulable facts.   A reasonably prudent man in Ellison's situation could have believed that his safety and that of his partner was in danger.   Ellison already had some reason to believe that Rideau might be intoxicated or perhaps injured.   When approached and asked his name, Rideau did not respond but appeared nervous and, critically, backed away.   It was not unreasonable under the circumstances for Ellison to have feared that Rideau was moving back to give himself time and space to draw a weapon.   It was not then unreasonable for Ellison simply to touch Rideau's front pants pocket to determine whether he had a gun.</p>
    </div>
    <div class="num" id="p9">
      <span class="num">9</span>
      <p class="indent">Rideau's specific moves took place after a detention, at night, in a high crime area where the carrying of weapons is common.   These are articulable facts upon which a police officer may legitimately rely in justifying his actions.   See Adams v. Williams, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U.S. 143</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">92 S.Ct. 1921</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">32 L.Ed.2d 612</a></span> (1972);  United States v. Laing, <span class="citation" data-id="532013"><a href="/opinion/532013/united-states-v-kenroy-laing-aka-junior-roy-laing-united-states-of/#286" aria-description="Citation for case: United States v. Kenroy Laing, A/K/A Junior Roy Laing,...">889 F.2d 281, 286</a></span> (D.C.Cir.1989);  United States v. Trullo, <span class="citation" data-id="9475728"><a href="/opinion/481633/united-states-v-john-f-trullo/#111" aria-description="Citation for case: United States v. John F. Trullo">809 F.2d 108, 111</a></span> (1st Cir.1987).   Stripped from their context, the backward steps offer no threat, but to a police officer in Ellison's situation, they become very significant in the matrix of the general facts.   Stated abstractly, specific actions may be construed as more or less hostile depending on the setting in which they occur.   Of course, that an individual is in a high crime neighborhood at night is not in and of itself enough to support an officer's decision to stop or frisk him.  Brown v. Texas, <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#52" aria-description="Citation for case: Brown v. Texas">443 U.S. 47, 52</a></span>, <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#2641" aria-description="Citation for case: Brown v. Texas">99 S.Ct. 2637, 2641</a></span>, <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">61 L.Ed.2d 357</a></span> (1979).   But when someone engages in suspicious activity in a high crime area, where weapons and violence abound, police officers must be particularly cautious in approaching and questioning him.   Trained, experienced officers like Ellison may perceive danger where an untrained observer would not.  <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Id.</a></span> at 52 n. 2, <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">99 S.Ct. at 2641</a></span> n. 2.   We are unwilling to tie the hands of police officers operating in potentially dangerous situations by precluding them from taking reasonable steps to ensure their safety when they have legitimately detained an individual.</p>
    </div>
    <div class="num" id="p10">
      <span class="num">10</span>
      <p class="indent">We do not suggest that the police have a right to frisk anyone on the street at night in a high crime neighborhood.   There was no such rousting here.   First, as we have observed, the detention was proper, beyond cavil.   That is, only persons meeting the requirements of a Terry stop can be detained, and this detention did not rest solely on Rideau's presence in a bad part of town.   Second, after Rideau was lawfully detained, he responded to the request of the officer by backing away--a move which in this specific context was reasonably seen as threatening.   Ellison could reasonably believe that Rideau was gaining room to use a weapon.   Rideau had no legitimate right to be free of the minor invasion of his liberty that came in response to this behavior.   On these facts, there is no basis for concluding that the officer's concerns for his safety were unreasonable.   We reject the suggestion that Rideau's movement could not reasonably be seen as threatening because it at best presented a risk of flight.   The suggestion ironically discloses the emptiness of Rideau's asserted liberty interest.   The officer could have grabbed Rideau to keep him from fleeing.   It is perverse to suggest that he could not touch him to protect himself against the drawing of a weapon.</p>
    </div>
    <div class="num" id="p11">
      <span class="num">11</span>
      <p class="indent">The scope of Ellison's "frisk" of Rideau is a relevant factor for us to consider.  "The touchstone of our analysis under the Fourth Amendment is always 'the reasonableness in all the circumstances of the particular governmental invasion of a citizen's personal security.' "  Pennsylvania v. Mimms, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#109" aria-description="Citation for case: Pennsylvania v. Mimms">434 U.S. 106, 109</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#332" aria-description="Citation for case: Pennsylvania v. Mimms">98 S.Ct. 330, 332</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">54 L.Ed.2d 331</a></span> (1977) (quoting Terry );  see also Michigan v. Long, <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1045" aria-description="Citation for case: Michigan v. Long">463 U.S. 1032, 1045-46</a></span>, <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#3479" aria-description="Citation for case: Michigan v. Long">103 S.Ct. 3469, 3479</a></span>, <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">77 L.Ed.2d 1201</a></span> (1983).   Reaching out to touch Rideau's pocket was a limited and tailored response to Ellison's fears for his safety, and served to validate his concerns.   Its very spontaneity equally validates the objective reasonableness of the practical balance of safety and liberty.   This was not the intrusive exploration of a detainee's body that the Court envisioned in Terry.<a class="footnote" href="#fn2" id="fn2_ref">2</a> Rideau was not put up against a wall or across a car and subjected to a shake down.   As we have observed, Ellison could have grabbed Rideau in a more invasive manner to prevent him from fleeing.   Thus the minimal intrusion involved in this encounter is another factor supporting officer Ellison's decision.</p>
    </div>
    <div class="num" id="p12">
      <span class="num">12</span>
      <p class="indent">The dissent accuses us of taking "significant liberties with both the facts and the law."   It is settled that in reviewing this denial of a motion to suppress, we view the evidence taken both at the suppression hearing and at trial in the light most favorable to the ruling.  United States v. Simmons, <span class="citation" data-id="551302"><a href="/opinion/551302/united-states-v-robert-simmons/#479" aria-description="Citation for case: United States v. Robert Simmons">918 F.2d 476, 479</a></span> (5th Cir.1990).   The dissent turns the standard upside down, searching for any inference contrary to the district court's ruling, proceeding as if this ruling, by a veteran of thirty-six years on the trial bench, did not exist.   At trial, Rideau told a very different story about the street encounter, and the district judge simply did not believe him.   He denied walking away from the police officers, denied tripping or stumbling, and even denied that the gun was found in the frisk.   His story was that the police officers found a cocaine pipe in his sock and while on the "... way from putting me in the back of the vehicle ... that's when I throwed the gun on the ground."   The dissent refers to our statement that Rideau "began to back away" as "at best misleading."   The arresting officer used these exact words in his testimony, and we are required to give credence to them.   Curiously, Judge Smith, in writing the panel opinion described the facts as follows:  "Ellison got out of the car and asked Rideau to identify himself.   Rideau began to back away."</p>
    </div>
    <div class="num" id="p13">
      <span class="num">13</span>
      <p class="indent">We do not depart from the rule that police officers must have specific and articulable facts indicating that their safety is in danger to justify a patdown.   Nor do we assert that a lawful detention is a license to frisk.   We simply look to the reality that the setting in which the police officer acts may reasonably and significantly affect his decisional calculus.   A reasonably prudent man in officer Ellison's position could believe that he was in danger as he approached Rideau.   The minimally intrusive action that he took to ensure his safety and that of his partner was not a violation of Rideau's constitutional rights.   The Fourth Amendment does not require police to allow a suspect to draw first.   This is East Texas, but it is 1992.</p>
    </div>
    <div class="num" id="p14">
      <span class="num">14</span>
      <p class="indent">AFFIRMED.</p>
    </div>
    <div class="num" id="p15">
      <span class="num">15</span>
      <p class="indent">JERRY E. SMITH, Circuit Judge, with whom POLITZ, Chief Judge, GOLDBERG, DUHE and WIENER, Circuit Judges, join, dissenting:</p>
    </div>
    <div class="num" id="p16">
      <span class="num">16</span>
      <p class="indent">The en banc majority takes limited but significant liberties with both the facts and the law.   More importantly, the court today comes dangerously close to declaring that persons in "bad parts of town" enjoy second-class status in regard to the Fourth Amendment.   Accordingly, I respectfully dissent from its well-intentioned view.</p>
    </div>
    <p>I.</p>
    <div class="num" id="p17">
      <span class="num">17</span>
      <p class="indent">In some important particulars, the facts in the record bear only a superficial resemblance to those set forth in the opinion for the en banc court.   The pertinent portions of the record are brief and are reprinted in the two footnotes that follow.   The first is from the transcript of the suppression hearing,<a class="footnote" href="#fn1-1" id="fn1-1_ref">1</a> and the second recounts the relevant portions of the trial before the jury.<a class="footnote" href="#fn2-1" id="fn2-1_ref">2</a></p>
    </div>
    <div class="num" id="p18">
      <span class="num">18</span>
      <p class="indent">As the transcript reveals, there is more to the facts than the majority has disclosed. Importantly, the majority opinion, as well as the government's oral argument, emphasizes Officer Ellison's suspicion that the defendant, Izeal Rideau, was drunk.   In fact, at the suppression hearing (at the close of which the district court denied the motion to suppress the fruits of the search), absolutely no mention was made of intoxication.   Instead, at that hearing Ellison, when asked at what point he decided to detain Rideau and talk to him, said, "After observing him stumble, as he moved out of the street."</p>
    </div>
    <div class="num" id="p19">
      <span class="num">19</span>
      <p class="indent">Even if the mention of stumbling<a class="footnote" href="#fn3-1" id="fn3-1_ref">3</a> could be understood as a proxy for intoxication,<a class="footnote" href="#fn4" id="fn4_ref">4</a> Ellison used it as justification only for the stop, not for the frisk.   But at issue here is the patdown, for, as the majority says and the panel held, there is no dispute that the officers had justification to detain Rideau, at least briefly, under Terry v. Ohio, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span> (1968).</p>
    </div>
    <div class="num" id="p20">
      <span class="num">20</span>
      <p class="indent">Intoxication was never mentioned until the trial on the merits, when Ellison finally said that he at first thought Rideau might be drunk.<a class="footnote" href="#fn5" id="fn5_ref">5</a>  He acknowledged that the only reason he stopped Rideau was that he saw him trip, "[c]ompounded with standing in the roadway."</p>
    </div>
    <div class="num" id="p21">
      <span class="num">21</span>
      <p class="indent">There is no suggestion that, once Rideau had stepped the six or seven feet to the edge of the road, he was a threat to himself or others.   He did exactly what Ellison wanted him to do--leave the roadway.   At that point his actions were those of a reasonable person and could be viewed, if anything, as cooperative.   Without more, there were no articulable facts to justify a search.</p>
    </div>
    <div class="num" id="p22">
      <span class="num">22</span>
      <p class="indent">The only justification offered by the majority is that Rideau "began to back away" as Ellison got out of his patrol car and walked toward him.   This is, at best, misleading.   Ellison's plain testimony is that Rideau only took "a couple of steps backwards"--hardly the makings of a hasty retreat to gain room to draw a weapon.</p>
    </div>
    <div class="num" id="p23">
      <span class="num">23</span>
      <p class="indent">In fact, the theory that Rideau intended, or appeared, to move back to give himself room to draw a gun is wholly the invention of the majority.<a class="footnote" href="#fn6" id="fn6_ref">6</a>  Officer Ellison's explanation is critically different.   At the suppression hearing, without mentioning any fear that Rideau was retreating in order to produce a gun, Ellison simply states, in conclusionary terms, that "concerned for my safety, due to the area, time of night and his apparent nervousness, I reached out to pat his outer clothing for officer safety."</p>
    </div>
    <div class="num" id="p24">
      <span class="num">24</span>
      <p class="indent">At the jury trial, Ellison's testimony was even more telling.   It is obvious that his suspicion of Rideau was a product of Rideau's condition and circumstance, not--as the majority opines--a result of any action taken by the defendant.   The search of Rideau, importantly, was conducted because of the general conditions in the neighborhood and not because of any articulable suspicion regarding Rideau.</p>
    </div>
    <div class="num" id="p25">
      <span class="num">25</span>
      <p class="indent">Thus, asked "what's the purpose of you patting somebody down in that area?", Ellison's explanation was as follows:</p>
    </div>
    <div class="num" id="p26">
      <span class="num">26</span>
      <p>The purpose of that is, a lot of times you have an area such as this, it is a high crime area, the officer is always concerned for his safety and any other citizens that could be nearby.   You pat down a person's outer clothing to determine if he's got any kind of weapons or knives, guns, et cetera, that could be quickly accessible to him before you could have a chance to get control of him, if he did try to go for them.  [Emphasis added.]</p>
    </div>
    <div class="num" id="p27">
      <span class="num">27</span>
      <p class="indent">Remarkably, what Ellison unwittingly describes is akin to a general warrant<a class="footnote" href="#fn7" id="fn7_ref">7</a> or to an indiscriminate dragnet-like procedure whereby all persons detained in a "bad part of town" are subject to search, not for anything they have done, but for the general purpose of ensuring the officer's safety or finding evidence of criminal activity.   In other words, Ellison frisked Rideau not because Rideau did anything (i.e., stepped backward) to arouse individualized suspicion but because he was there, in a bad part of town, and, like anyone else in that area that night, might have had a weapon.</p>
    </div>
    <div class="num" id="p28">
      <span class="num">28</span>
      <p class="indent">Thus, the search of Rideau was conducted not because he had started to draw a weapon--or because a reasonable officer in Ellison's situation objectively might have believed as much.   Instead, the patdown was effected to make sure that the officers would not be harmed if Rideau should decide to go for a gun--a gun the officers had no reason to believe he even had.   Unfortunately, however, for those who accept the dangers inherent in law enforcement work, the Fourth Amendment does not provide officers with that hefty an insurance policy.</p>
    </div>
    <div class="num" id="p29">
      <span class="num">29</span>
      <p class="indent">I must take issue, therefore, with the majority's assertion that "[i]t was not unreasonable under the circumstances for Ellison to have feared that Rideau was moving back to give himself time and space to draw a weapon."   Maj. op. at 1575.   Nothing that Rideau did showed that he--any more than anyone else in that area that night--was likely to endanger the police or the public.   Again, the Constitution requires specific and articulable facts.   An amorphous fear for one's safety, and the desire to take extra steps to guarantee that safety, are not enough.</p>
    </div>
    <div class="num" id="p30">
      <span class="num">30</span>
      <p class="indent">In this regard, one must examine in some depth the details of Rideau's movements at the instant in question.   It is undisputed that he took only "a couple of steps backwards," a critical detail the majority fails to note.   First, a movement of two steps, without more,<a class="footnote" href="#fn8" id="fn8_ref">8</a> is not enough to indicate that a suspect is trying to buy space in which to pull a gun, and no reasonable person could think as much.   Second, there is no reasonable ground for concluding that that specific action was more threatening than any other action Rideau could have taken.</p>
    </div>
    <div class="num" id="p31">
      <span class="num">31</span>
      <p class="indent">By the government's own acknowledgement, and the majority's rationale, Rideau is caught in a classic "Catch 22."   That is, once the officers exited their vehicle and began walking toward him, there is nothing he could have done to save himself from a frisk.   The action he took--stepping back a couple of paces--has been fantasized by the majority into a hastily conceived plot to draw a gun and fire on the officers.   But, as the government seemed to admit in oral argument, any other action, by that point, also would have been viewed as "suspicious."</p>
    </div>
    <div class="num" id="p32">
      <span class="num">32</span>
      <p class="indent">For example, if Rideau had stepped forward, Ellison most certainly would have viewed it as threatening.   Had the defendant stepped to the right or left, it would have been interpreted as nervousness or an attempt to flee.   If Rideau had remained stiffly frozen in place, it would have been viewed, presumably, as a show of guilt or of abnormal behavior caused by drugs or alcohol.</p>
    </div>
    <div class="num" id="p33">
      <span class="num">33</span>
      <p class="indent">Perhaps if Rideau had graduated from charm school and had been taught how to look "cool and collected" in the face of approaching uniformed officers, he could have managed to avoid the patdown.   Otherwise, he was doomed to the intrusion that in fact occurred.   Government counsel candidly admitted as much, at oral argument, by stating that Rideau was subject to search as soon as he was seen standing in the street, then tripping;  in other words, Ellison did not even have to rely upon fear of his safety as an excuse for the frisk.</p>
    </div>
    <div class="num" id="p34">
      <span class="num">34</span>
      <p class="indent">The Fourth Amendment proscribes only those searches that are unreasonable.   But it defies reason to base a justification for a search upon actions that any similarly-situated person would have taken.   The meat of the Terry analysis is that a search is unreasonable if it is based not upon the individualized and unusual actions taken by the suspect but upon actions any reasonable person would or might have taken under the circumstances.</p>
    </div>
    <div class="num" id="p35">
      <span class="num">35</span>
      <p class="indent">Indeed, one can surmise that many totally innocent citizens, upon seeing the approach of two uniformed officers, would take "a couple of steps" backward and would be surprised to learn that that normal reaction could subject them to a search of their person and the consequent invasion of privacy.   This underscores the fact that Rideau was searched not because of anything he did but because of his status--a person in a "bad part of town" where, presumably, people do not belong late at night, on the street, unless they are "up to no good."   By that measure, almost any person in the vicinity of Martin Luther King Boulevard and Bonham Street that night could have been stopped and frisked.</p>
    </div>
    <div class="num" id="p36">
      <span class="num">36</span>
      <p class="indent">The only "fact" that distinguishes Rideau from other such persons is that he was seen to stumble in the street while avoiding an oncoming car.   But, as the panel held, that action alone reasonably subjected him only to a stop--a brief inquiry by the officers to check on his condition--and not to a search<a class="footnote" href="#fn9" id="fn9_ref">9</a> of his person.   This is why what was done to Rideau is tantamount to a general warrant, a dragnet, and why what happened to Rideau is precisely what the Constitution forbids.</p>
    </div>
    <p>II.</p>
    <div class="num" id="p37">
      <span class="num">37</span>
      <p class="indent">The majority mentions only in passing, and fails to discuss, the most significant Supreme Court authority regarding this case.   In Maryland v. Buie, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">494 U.S. 325</a></span>, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">110 S.Ct. 1093</a></span>, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">108 L.Ed.2d 276</a></span> (1990), the Court summarizes the law as it has developed since the seminal case of Terry v. Ohio, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span> (1968).   The Court reminds us that Terry authorizes only "a limited patdown for weapons where a reasonably prudent officer would be warranted in the belief, based on 'specific and articulable facts,' ... and not on a mere 'inchoate and unparticularized suspicion or "hunch," ... that he is dealing with an armed and dangerous individual.' "  Buie, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#332" aria-description="Citation for case: Maryland v. Buie">494 U.S. at 332</a></span>, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#1097" aria-description="Citation for case: Maryland v. Buie">110 S.Ct. at 1097</a></span> (emphasis added) (quoting Terry, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 21, 27</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#1880" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. at 1880, 1883</a></span>).</p>
    </div>
    <div class="num" id="p38">
      <span class="num">38</span>
      <p class="indent">The majority concludes that "[a] reasonably prudent man in Ellison's situation could have believed that his safety and that of his partner was [sic] in danger."   Maj. op. at 1574.   But the Court in Buie--a recent restatement of Terry--words it in a way that requires much more:  The officer must reasonably believe "that he is dealing with an armed and dangerous individual."  Buie, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#332" aria-description="Citation for case: Maryland v. Buie">494 U.S. at 332</a></span>, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">110 S.Ct. at 1097</a></span> (quoting Terry, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 27</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#1883" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. at 1883</a></span>).   Significantly, this is phrased in the conjunctive:  The suspect must be both armed and dangerous.</p>
    </div>
    <div class="num" id="p39">
      <span class="num">39</span>
      <p class="indent">It is true that Rideau proved to be armed, but hindsight will not justify a search.   As I have stated, the fact of tripping slightly in the street, coupled with his taking two steps backward, gave the officers no reasonable belief that he was armed.   Moreover, absolutely nothing in this record supports a reasonable conclusion that, at the moment he was searched, Rideau was also "dangerous," to either the officers or others.</p>
    </div>
    <div class="num" id="p40">
      <span class="num">40</span>
      <p class="indent">The majority also misreads the law regarding "specific and articulable facts."   Emphatically, the Supreme Court in Buie has reiterated its warning in Terry that the officer's belief<a class="footnote" href="#fn10" id="fn10_ref">10</a> that the suspect is "armed and dangerous" may not be based upon only "a mere inchoate and unparticularized suspicion or 'hunch.' "  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Id.</a></span> (first internal quotation marks omitted).<a class="footnote" href="#fn11" id="fn11_ref">11</a></p>
    </div>
    <div class="num" id="p41">
      <span class="num">41</span>
      <p class="indent">Yet, such an impermissible "hunch" is the very most that Ellison seems to be describing when he states, "The purpose of [the patdown] is, a lot of times you have an area such as this, it is a high crime area, the officer is always concerned for his safety...."  In fact, this statement seems not even to describe a hunch but rather a general practice of searching all suspects in high-crime areas, even without individualized suspicion.   The only other factor that Ellison relied upon was Rideau's "apparent nervousness," but there is nothing about such a trait that would indicate to a reasonable officer that a person is armed and dangerous.<a class="footnote" href="#fn12" id="fn12_ref">12</a></p>
    </div>
    <div class="num" id="p42">
      <span class="num">42</span>
      <p class="indent">This is the heart of the instant case.   The essential question for the en banc court today is whether an officer may use the general conditions in a particular part of town as justification for a search, where the suspect is guilty of no culpable conduct but merely reacts as any reasonable person would under the circumstances.<a class="footnote" href="#fn13" id="fn13_ref">13</a></p>
    </div>
    <div class="num" id="p43">
      <span class="num">43</span>
      <p class="indent">In Buie, the Court addresses this question specifically:</p>
    </div>
    <div class="num" id="p44">
      <span class="num">44</span>
      <p>[D]espite the danger that inheres in on-the-street encounters and the need for police to act quickly for their own safety, ... [e]ven in high crime areas, where the possibility that any given individual is armed is significant, Terry requires reasonable, individualized suspicion before a frisk of weapons can be conducted.</p>
    </div>
    <div class="num" id="p45">
      <span class="num">45</span>
      <p class="indent"><span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">Id.</a></span> <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">494 U.S. at 334</a></span> n. 2, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">110 S.Ct. at 1098</a></span> n. 2.</p>
    </div>
    <div class="num" id="p46">
      <span class="num">46</span>
      <p class="indent">The majority does not attend to this important passage from Buie.   It sets forth, as the only articulable facts upon which it relies, that the officers had reason to believe Rideau was intoxicated or injured;  that when approached, Rideau "did not respond but appeared nervous and, critically, backed away";  and that "Rideau's specific moves took place after a detention, at night, in a high crime area where the carrying of weapons is common."   Maj. op. at 1574-1575.<a class="footnote" href="#fn14" id="fn14_ref">14</a></p>
    </div>
    <div class="num" id="p47">
      <span class="num">47</span>
      <p class="indent">The majority takes pains to state that "[o]f course, that an individual is in a high crime neighborhood at night is not in and of itself enough to support an officer's decision to stop or frisk him."   Id. at 1575.<a class="footnote" href="#fn15" id="fn15_ref">15</a>  So, it is only what the majority terms Rideau's "suspicious activity," id., that the majority adds to the equation to tip the scales in favor of the frisk.   But it is a challenge to the imagination to say that Rideau's actions were "suspicious," and certainly there was nothing about them that gave rise to a reasonable suspicion that he was armed and dangerous.</p>
    </div>
    <div class="num" id="p48">
      <span class="num">48</span>
      <p class="indent">Thus, the majority in this case has installed the very rule it attempts to deny:  that, practically speaking, any person in a high-crime area (or "bad part of town") late at night is subject to a frisk.   Such a maxim could make the directive to "round up the usual suspects" the order of the day.</p>
    </div>
    <p>III.</p>
    <div class="num" id="p49">
      <span class="num">49</span>
      <p class="indent">The majority expresses a concern that I share regarding officer safety--a problem important enough to warrant separate discussion.   In Buie, Terry, and elsewhere, the Supreme Court has provided that a search can be reasonable under some circumstances when effected to ensure safety in the field, when spur-of-the-moment encounters reasonably raise the specter of danger to an officer or to others.   It is also plain, however, that such concerns do not automatically trump the Fourth Amendment.</p>
    </div>
    <div class="num" id="p50">
      <span class="num">50</span>
      <p class="indent">The safety of police officers undoubtedly would be enhanced if, when entering a high-crime area for a legitimate purpose, they could briefly and effectively search all persons in the area for weapons.   The salutary interest of law enforcement would be served by such a rule, but it would come at the unacceptable expense of intrusions upon innocent members of the public as to whom there is no reasonable suspicion of wrongdoing.   Our Bill of Rights does not permit such intrusions.</p>
    </div>
    <div class="num" id="p51">
      <span class="num">51</span>
      <p class="indent">The majority, Maj. op. at 1576, reminds us that this is 1992, presumably referring to the growing problem of drugs and crime in our inner cities and to the consequent dangers that confront well-meaning law enforcement personnel who enter there to do their jobs.   But only two years ago, in 1990, the Supreme Court reminded us that the proscription of unreasonable searches is alive and well despite the obvious peril to officers that can be presented by limiting their ability to conduct street searches.   The Court's words are poignant, so I quote them again:</p>
    </div>
    <div class="num" id="p52">
      <span class="num">52</span>
      <p>[D]espite the danger that inheres in on-the-street encounters and the need for police to act quickly for their own safety, the Court in Terry did not adopt a bright-line rule authorizing frisks for weapons in all confrontational encounters.   Even in high crime areas, where the possibility that any given individual is armed is significant, Terry requires reasonable, individualized suspicion before a frisk for weapons can be conducted.</p>
    </div>
    <div class="num" id="p53">
      <span class="num">53</span>
      <p class="indent">Buie, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">494 U.S. at 334</a></span> n. 2, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">110 S.Ct. at 1098</a></span> n. 2 (emphasis added).</p>
    </div>
    <div class="num" id="p54">
      <span class="num">54</span>
      <p class="indent">We must remember, too, that this is not an all-or-nothing matter.   By imposing limits on searches, the Constitution and the Supreme Court have not left the police unprotected.   The requirement of individualized suspicion merely ensures that officers receive greater protection in those instances in which they are most likely to be in danger.   That is the essence of the requirement that searches be "reasonable."</p>
    </div>
    <div class="num" id="p55">
      <span class="num">55</span>
      <p class="indent">Like the rule of Miranda v. Arizona, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U.S. 436</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S.Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L.Ed.2d 694</a></span> (1966), the lesson of Buie and Terry makes law enforcement more difficult.   Much as police officers must learn to administer the warnings required by the Court in Miranda, they likewise must be aware of the constraints upon searches in the street and must accept their jobs with that understanding.<a class="footnote" href="#fn16" id="fn16_ref">16</a></p>
    </div>
    <div class="num" id="p56">
      <span class="num">56</span>
      <p class="indent">This is no criticism of Officer Ellison.   He is accused of no wrongdoing or malice, and his actions are subject to reasonably differing legal interpretations that today divide our en banc court.   The search he conducted on defendant Rideau was in accordance with proper procedure as he understood it and was in the interest of law enforcement.   The majority has put its stamp of approval on his conduct;  concluding that he crossed the constitutional line, I disagree.</p>
    </div>
    <p>IV.</p>
    <div class="num" id="p57">
      <span class="num">57</span>
      <p class="indent">Finally, I wish to comment upon the status of this case as an en banc rehearing.   Interestingly, the government never requested either en banc or panel rehearing in this matter.   Nor, as often is its practice, did it even seek an extension of time in which to suggest rehearing en banc, in order to seek permission from the Solicitor General.</p>
    </div>
    <div class="num" id="p58">
      <span class="num">58</span>
      <p class="indent">Presumably, this is because the Department of Justice and the interests it represents perceived no jurisprudential danger from the panel's conclusion that the fruits of the instant search should be suppressed.   This case was routine, made no new law, and should not have been reviewed en banc.   The panel opinion posed no threat to officer safety, and the government's reaction to it showed as much.<a class="footnote" href="#fn17" id="fn17_ref">17</a></p>
    </div>
    <div class="num" id="p59">
      <span class="num">59</span>
      <p class="indent">By taking the case en banc and fashioning today's ruling, the court has run afoul of the Constitution and Supreme Court precedent and has rendered the Fourth Amendment essentially meaningless in an entire category of ordinary street encounters.   Despite the good intention of the majority to protect our officers on the street, I respectfully dissent.</p>
    </div>
    <div class="footnotes">
      <div class="footnote" id="fn1">
        <a class="footnote" href="#fn1_ref">1</a>
        <p> Defendant testified that the encounter occurred between 3:30 and 4:30 a.m.   The arresting officer placed the time at 10:30 p.m</p>
      </div>
      <div class="footnote" id="fn2">
        <a class="footnote" href="#fn2_ref">2</a>
        <p> The Court described a frisk in Terry as follows:  " 'The officer must feel with sensitive fingers every portion of the prisoner's body.   A thorough search must be made of the prisoner's arms and armpits, waistline and back, the groin and area about the testicles, and entire surface of the legs down to the feet.' "  392 U.S. at 17 n. 13, 88 S.Ct. at 1877 n. 13 (citation omitted)</p>
      </div>
      <div class="footnote" id="fn1-1">
        <a class="footnote" href="#fn1-1_ref">1</a>
        <p> The pertinent portion of the transcript of the suppression hearing is as follows:</p>
        <p>Direct examination of defendant Rideau (by his attorney):</p>
        <p>Q. At the time of the arrest where were you standing?</p>
        <p>A. On the street corner.</p>
        <p>Q. You were at the corner of Martin Luther King Boulevard and Bonham Street?</p>
        <p>A. Yes.</p>
        <p>Q. Was there anyone with you?</p>
        <p>A. No, sir.</p>
        <p>Q. Were you just standing on the street corner at that time?</p>
        <p>A. Standing on the street corner, on the side of the street.</p>
        <p>Q. Did the officers approach you in a marked vehicle?</p>
        <p>A. They came in a white--black-and-white car with the siren on top.</p>
        <p>Q. And did you walk away from them at all?</p>
        <p>A. No.</p>
        <p>Q. Did you remain standing at that position?</p>
        <p>A. Yes.</p>
        <p>Q. Had you been in the street at any time where you had tripped or stumbled?</p>
        <p>A. No.</p>
        <p>Q. After the officers approached you, did they place their hands on you?</p>
        <p>A. Yes.</p>
        <p>Cross-examination of defendant Rideau (by government counsel):</p>
        <p>Q. What time of day was this, Mr. Rideau?</p>
        <p>A. I guess it was 3:30, 4:30 in the morning.</p>
        <p>Q. Would you agree with me that at least back on July of '89 that was a[ ] high crime area?</p>
        <p>A. Not really.</p>
        <p>Q. You thought that was a very safe place to go?</p>
        <p>A. People live up there.</p>
        <p>Q. I realize that.   But there are lots of drug dealings going down in that area;  is that correct?</p>
        <p>A. Not at that time.</p>
        <p>Q. I don't mean right at that minute;  I mean that time in 1989 in July?</p>
        <p>A. Yes.</p>
        <p>Q. It has improved now.   But at that point, it was not a place that you want your children to be walking around late at night?</p>
        <p>A. No.</p>
        <p>Q. You do not live in that area;  is that correct?</p>
        <p>A. Yes.</p>
        <p>Q. You were, in fact, living in Liberty?</p>
        <p>A. Yes.</p>
        <p>Q. Isn't it a fact, that you were wearing warm up pants, dark warm up pants?</p>
        <p>A. Yes.</p>
        <p>Q. And what kind of a shirt were you wearing?   Do you remember?</p>
        <p>A. No.</p>
        <p>Q. Dark in color, however?</p>
        <p>A. I think so.</p>
        <p>Q. Isn't it a fact, that when the officers were driving along the street, that you were in fact in the street area?</p>
        <p>A. No.</p>
        <p>Q. Isn't it a fact, that they flashed their headlights to get you to move out of the street?</p>
        <p>A. No.</p>
        <p>Q. They didn't do that at all?</p>
        <p>A. No.</p>
        <p>Q. Isn't it a fact, Mr. Rideau, that the officers pulled over and, without too much discussion, they patted the outside of your clothing?</p>
        <p>A. Yes.</p>
        <p>Direct examination of Officer Ellison (by government counsel):</p>
        <p>Q. Were you in the area of Bonham and Martin Luther King at about 10:30 p.m. on that day?</p>
        <p>A. Yes, ma'am.</p>
        <p>Q. Did you happen to observe someone standing in the roadway of that area wearing dark clothing?</p>
        <p>A. I did.</p>
        <p>Q. What type of area is that, high crime, high crime area, that sort of thing?</p>
        <p>A. Yes, ma'am, it is.   There's a high crime area, drug trafficking, street deals, that type of thing.</p>
        <p>Q. In your experience have you found people in that area also carry weapons?</p>
        <p>A. Yes, ma'am.</p>
        <p>Q. When you observed this person in the roadway with the dark clothing on, what action did you take?</p>
        <p>A. When I saw the person standing there in dark clothing, I flashed my bright lights to see him better and make sure it was a person and if it was, hopefully, he would step out of the roadway.</p>
        <p>Q. And did this person, in fact, step out of the roadway?</p>
        <p>A. Yes, ma'am.</p>
        <p>Q. Did you observe him make that move?</p>
        <p>A. Yes, ma'am.   As he stepped out of the roadway towards the shoulder, he began to stumble somewhat.</p>
        <p>Q. So did you stop to check on his condition?</p>
        <p>A. Yes, ma'am, I did.</p>
        <p>Q. And when got out [sic] of your patrol car, which I assume you did, what action did you take?</p>
        <p>A. I stepped out of the patrol car and approached him and asked him his name.   And as I approached him, he began to back up from me, back away.</p>
        <p>Q. So what did you do then?</p>
        <p>A. At that time, concerned for my safety due to the area, time of night and his apparent nervousness, I reached out to pat his outer clothing for officer safety.</p>
        <p>Q. Did you actual [sic] reach into a pocket or reach into his clothing?</p>
        <p>A. No, ma'am, I did not.</p>
        <p>Q. Specifically, what did you do?</p>
        <p>A. I patted down his outer clothing, his outer pockets, normally [sic] pat down the outer pockets of any jacket or shirt, and his pants.</p>
        <p>Q. And in this particular case, exactly what did you pat?</p>
        <p>A. The first thing that I reached out [sic] was his right front pant's [sic] pocket.</p>
        <p>Q. And what, if anything, did you notice when you touched that outer pocket?</p>
        <p>A. When I touched that outer pocket, I felt what appeared to be a small firearm in the pocket?  [sic]</p>
        <p>Q. And what you did [sic] do then?</p>
        <p>A. At that time I secured him and called out "gun" to my partner.   And then my partner secured the other arm and I reached in and found it to be a small firearm and pulled it out of the pocket.</p>
        <p>Cross-examination of Officer Ellison (by Rideau's counsel):</p>
        <p>Q. And is there a street light at the corner of Martin Luther King and Bonham?</p>
        <p>A. There's a street light near that corner.</p>
        <p>Q. And how is the road surfaced?</p>
        <p>A. It's asphalt.</p>
        <p>Q. Does it have a curb and gutter or does it just have a shoulder?</p>
        <p>A. Just a shoulder, no curb and gutter.</p>
        <p>Q. At the time that you exited your vehicle, where was the Defendant?</p>
        <p>A. He was standing on the shoulder of the roadway.   I don't recall that there's a street light on that corner.</p>
        <p>Q. Now, at the time that you saw him move from the street, had you already flashed your lights?</p>
        <p>A. I flashed the bright lights at him as we were approaching in traffic.</p>
        <p>Q. And was he looking at you when you flashed the bright lights?</p>
        <p>A. Yes, sir.</p>
        <p>Q. Then after that you saw him removed from the street?</p>
        <p>A. Right.</p>
        <p>Q. Now, you're not pretending that it's a crime for a person to stumble are you?</p>
        <p>A. No, sir.</p>
        <p>Q. ... [A]t what point in time did you determine that you were going to stop the Defendant and talk to him?</p>
        <p>A. After observing him stumble, as he moved out of the street.</p>
        <p>Q. Is there any other thing that made you determine that you were going to stop and talk to him?</p>
        <p>A. No, sir.</p>
      </div>
      <div class="footnote" id="fn2-1">
        <a class="footnote" href="#fn2-1_ref">2</a>
        <p> The significant testimony from the trial regarding the search is as follows:</p>
        <p>Direct testimony of Officer Ellison (by government counsel):</p>
        <p>Q. And how long have you been a police officer?</p>
        <p>A. Approximately six and a half years.</p>
        <p>Q. Tell us about that area.   What's in that vicinity, is it a residential, stores, factories, what?</p>
        <p>A. There is a small residential area that is similar to a project type area, there's a night club located about a block away from there.   Other than that, it's mainly commercial.</p>
        <p>Q. And back on July the 6th 1989, what type of a crime area was it?</p>
        <p>A. At that time, this area was an area with numerous drug type offenses:  street buys of cocaine, lots of drunkenness, weapons, drugs and so forth.</p>
        <p>Q. You've experienced all or any of those in your experience as a patrol officer there?</p>
        <p>A. Yes, ma'am.</p>
        <p>Q. You would claim it to be a high crime area?</p>
        <p>A. Yes, ma'am.</p>
        <p>Q. What, if anything, did you observe?</p>
        <p>A. We observed a black male standing in the intersection of Bonham and M.L.K.</p>
        <p>Q. What type of clothing did he have on, do you recall?</p>
        <p>A. He had on dark clothing, is all we could tell from the distance.</p>
        <p>Q. I take it [sic] was hard to see him then?</p>
        <p>A. Yes, ma'am.</p>
        <p>Q. What, if anything, did you do when you observed this man in the street there ...?</p>
        <p>A. I just flicked the bright lights to see if it was someone standing in the road, and then turned them off.</p>
        <p>Q. What action, if anything, did the man take then?</p>
        <p>A. When he saw the bright lights, he had turned towards us, and began to step out of the roadway towards the shoulder.   He was near the corner.   And when he did, he stumbled or tripped or something.</p>
        <p>Q. You don't know if he tripped over anything, but you obviously noticed the stumbling and staggering?</p>
        <p>A. Right.</p>
        <p>Q. At the point that you observed him to stumble or stagger, was he still facing your patrol unit?</p>
        <p>A. He had turned to step out of the roadway, as he--he saw us and then turned to step out of the roadway, and that was the time that he stumbled.</p>
        <p>Q. What did you think when you saw this stumbling?</p>
        <p>A. I thought that he may be intoxicated.</p>
        <p>Q. So what did you do?</p>
        <p>A. We passed through the intersection and stopped right there at the corner where he was standing.</p>
        <p>Q. He didn't try to run away or anything?</p>
        <p>A. No, ma'am.</p>
        <p>Q. Did he, in fact, get out of the roadway?</p>
        <p>A. Yes, ma'am.   He had already stepped out of the roadway and was standing on the shoulder at the corner.</p>
        <p>Q. And after pulling up to the vehicle, did you turn your siren on or anything like that?</p>
        <p>A. No, ma'am.   We just simply pulled over to the shoulder.</p>
        <p>Q. And did you get out of the vehicle then?</p>
        <p>A. Yes, ma'am.</p>
        <p>Q. Did your partner also get out?</p>
        <p>A. Yes, ma'am.</p>
        <p>Q. What did you do when you got out of your vehicle yourself?</p>
        <p>A. I was on the driver's side and my side of the vehicle was closest to him, I stepped out of the vehicle into the roadway and asked him who he was as I walked up to him.</p>
        <p>Q. I take it this is a very--this is happening very quickly then?</p>
        <p>A. Yes, ma'am.   Just enough time to exit the vehicle and step a few feet towards him.</p>
        <p>Q. Okay.   What, if anything, did you observe as you were approaching him?</p>
        <p>A. He began to back up as I spoke to him and approached him a little bit, he took a couple of steps backwards.</p>
        <p>Q. And so what did you do?</p>
        <p>A. At that time I reached out to pat down his outer clothing for any weapons or anything that could harm me or my partner.</p>
        <p>Q. Explain that a little better for us.   What was the purpose of reaching out and patting somebody when you haven't even struck up a conversation yet?</p>
        <p>A. Well, due to the high crime area, the time of the night--</p>
        <p>Q. Once again, what's the purpose of you [sic] patting somebody down in that area?</p>
        <p>A. The purpose of that is, a lot of times you have an area such as this, it is a high crime area, the officer is always concerned for his safety and any other citizens that could be nearby.   You pat down a person's outer clothing to determine if he's got any kind of weapons or knives, guns, et cetera, that could be quickly accessible to him before you could have a chance to get control of him, if he did try to go for them.</p>
        <p>Q. You don't put them up against the wall, across your car?</p>
        <p>A. No, ma'am.   It's simple just to reach and pat of [sic] his outer pockets.   There's no body search or anything like that.   It's simply a pat down....  The first place that I patted him was his right front pant's [sic] pocket....  I felt an object in there that was consistent with a firearm....  At that time I squeezed the--I still didn't reach into the pocket, I just grabbed it as to get control of it, and grabbed his arm and called out "gun" to my partner, who then grabbed his other arm and we placed him up against the patrol car....</p>
        <p>Q. What was the offense that you did, in fact, arrest him for?</p>
        <p>A. Unlawfully carrying a weapon.</p>
        <p>Cross-examination of Officer Ellison (by Rideau's counsel):</p>
        <p>Q. Mr. Ellison, how far from the side of the roadway did you observe the Defendant?</p>
        <p>A. Probably six to seven feet, approximately.</p>
        <p>Q. Was he standing or moving towards the side of the roadway?</p>
        <p>A. He was just standing.</p>
        <p>Q. At the time that you flashed your bright lights, was he facing the vehicle?</p>
        <p>A. I don't recall if he was facing the vehicle at the time that I turned the brights on.   He had turned after I had the brights on;  I could see him then, I could see his face.</p>
        <p>Q. Did he fall all the way to the ground?</p>
        <p>A. No, sir.</p>
        <p>Q. More like a trip as he was walking to the side of the street?</p>
        <p>A. Yes, sir.</p>
        <p>Q. Now, as you were on patrol, did you stop everyone that night that you saw who tripped?</p>
        <p>A. I don't recall doing that, no.</p>
        <p>Q. Is it correct that the only reason that you stopped this man was because you saw him trip?</p>
        <p>A. Saw him trip, thinking that he may be intoxicated, yes.</p>
        <p>Q. But the trip is the only thing that you had suspicion about?</p>
        <p>A. Compounded with standing in the roadway.</p>
        <p>Q. By the time you got up to him, where was he?</p>
        <p>A. He was standing on the shoulder in the southwest corner of those two streets.</p>
      </div>
      <div class="footnote" id="fn3-1">
        <a class="footnote" href="#fn3-1_ref">3</a>
        <p> The term "stumble" must be viewed in light of the entire record, for at another point Ellison answered "Yes" to the question whether Rideau's miscue was "[m]ore like a trip as he was walking to the side of the street."</p>
      </div>
      <div class="footnote" id="fn4">
        <a class="footnote" href="#fn4_ref">4</a>
        <p> The stumbling cannot fairly be read as a surrogate for inebriation, for although, as the majority opinion states, public intoxication is a crime, Ellison answered "No" to the question, "Now, you're not pretending that it's a crime for a person to stumble are you?"</p>
      </div>
      <div class="footnote" id="fn5">
        <a class="footnote" href="#fn5_ref">5</a>
        <p> In fact, Rideau was arrested not for public intoxication but for unlawful possession of a weapon</p>
      </div>
      <div class="footnote" id="fn6">
        <a class="footnote" href="#fn6_ref">6</a>
        <p> Thus, the majority opines that "Ellison's quick move was to see if [Rideau] had any weapons that could harm him or his partner."   Op. at 1573.   Nothing supports this claim except the majority's ipse dixit</p>
      </div>
      <div class="footnote" id="fn7">
        <a class="footnote" href="#fn7_ref">7</a>
        <p> "[I]ndiscriminate searches and seizures conducted under the authority of 'general warrants' were the immediate evils that motivated the framing and adoption of the Fourth Amendment."  Payton v. New York, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York">445 U.S. 573, 583</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1378" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371, 1378</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">63 L.Ed.2d 639</a></span> (1980) (footnote omitted).   See generally JACOB W. LANDYNSKI, SEARCH AND SEIZURE AND THE SUPREME COURT 19-42 (1966)</p>
      </div>
      <div class="footnote" id="fn8">
        <a class="footnote" href="#fn8_ref">8</a>
        <p> "More" might include, for example, "furtive hand movements," a fact relied upon in a case cited by the majority, United States v. Laing, <span class="citation" data-id="532013"><a href="/opinion/532013/united-states-v-kenroy-laing-aka-junior-roy-laing-united-states-of/#286" aria-description="Citation for case: United States v. Kenroy Laing, A/K/A Junior Roy Laing,...">889 F.2d 281, 286</a></span> (D.C.Cir.1989), cert. denied, <span class="citation multiple-matches"><a href="/c/U.S./494/1008/">494 U.S. 1008</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./110/1306/">110 S.Ct. 1306</a></span>, <span class="citation no-link">108 L.Ed.2d 482</span>, and cert. denied, <span class="citation multiple-matches"><a href="/c/U.S./494/1069/">494 U.S. 1069</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./110/1790/">110 S.Ct. 1790</a></span>, <span class="citation" data-id="9090740"><a href="/opinion/9096492/thai-do-hoang-v-kansas/" aria-description="Citation for case: Thai Do Hoang v. Kansas">108 L.Ed.2d 792</a></span> (1990), or a bulge in the suspect's pocket, as in  United States v. Trullo, <span class="citation" data-id="9475728"><a href="/opinion/481633/united-states-v-john-f-trullo/#113" aria-description="Citation for case: United States v. John F. Trullo">809 F.2d 108, 113</a></span> (1st Cir.), cert. denied, <span class="citation multiple-matches"><a href="/c/U.S./482/916/">482 U.S. 916</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./107/3191/">107 S.Ct. 3191</a></span>, <span class="citation no-link">96 L.Ed.2d 679</span> (1987), another case the majority cites</p>
      </div>
      <div class="footnote" id="fn9">
        <a class="footnote" href="#fn9_ref">9</a>
        <p> The majority describes the search euphemistically.   Thus, in its introduction, the majority states that Ellison "reached out and touched the pants pocket of the individual and discovered a gun."   Maj. op. at 1573.   Similarly, the majority refers to "Ellison's decision to reach out and pat Rideau's pocket," <span class="citation no-link">id. at 1574</span>, and says that the officer "simply [touched] Rideau's front pants pocket," <span class="citation no-link">id. at 1575</span>, and "[r]each[ed] out to touch Rideau's pocket," <span class="citation no-link">id. at 1575</span>.   The phrase "reach out and touch" should be left to long-distance telephone commercials:  The frank truth is that Rideau was searched</p>
        <p>The fact that the frisk in this case did not involve the anatomical exploration that the majority finds it necessary to describe graphically in quoting from Terry v. Ohio, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span>, 17 n. 13, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, 1877 n. 13, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span> (1968), see Maj. op. at 1575 n. 2, makes it no less an intrusion governed by the Fourth Amendment.   What the majority terms "a limited and tailored response," id. at 1575, is the same "frisk for weapons" that the Supreme Court recently has reminded us " 'constitutes a severe, though brief, intrusion upon cherished personal security.' "  Maryland v. Buie, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#332" aria-description="Citation for case: Maryland v. Buie">494 U.S. 325, 332</a></span>, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#1097" aria-description="Citation for case: Maryland v. Buie">110 S.Ct. 1093, 1097</a></span>, <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">108 L.Ed.2d 276</a></span> (1990) (quoting Terry, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 24-25</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#1882" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. at 1882</a></span>).</p>
      </div>
      <div class="footnote" id="fn10">
        <a class="footnote" href="#fn10_ref">10</a>
        <p> The majority properly notes that we judge an officer's actions against an objective standard;  Ellison's state of mind is not directly at issue, though his factual observations are</p>
      </div>
      <div class="footnote" id="fn11">
        <a class="footnote" href="#fn11_ref">11</a>
        <p> The majority does not mention this critical passage</p>
      </div>
      <div class="footnote" id="fn12">
        <a class="footnote" href="#fn12_ref">12</a>
        <p> In Brown v. Texas, <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#52" aria-description="Citation for case: Brown v. Texas">443 U.S. 47, 52</a></span>, <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#2641" aria-description="Citation for case: Brown v. Texas">99 S.Ct. 2637, 2641</a></span>, <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">61 L.Ed.2d 357</a></span> (1979), the Court said the fact that the defendant "looked suspicious" was not enough:</p>
        <p>Officer Venegas testified ... that the situation in the alley "looked suspicious," but he was unable to point to any facts supporting that conclusion....  The fact that appellant was in a neighborhood frequented by drug users, standing alone, is not a basis for concluding that appellant himself was engaged in criminal conduct.   In short, the appellant's activity was no different from the activity of other pedestrians in that neighborhood.</p>
        <p>(Footnote omitted.)</p>
        <p>Similarly,</p>
        <p>it has properly been held that the "hesitancy of a car to pass a police cruiser and a glance at the police officer by a passenger," a "startled look at the sight of a police officer," appearing nervous when a police car passed, looking away from police activity in the vicinity, pointing toward police, or quickening one's pace upon seeing the police are not, standing alone, sufficient basis for an investigative stop.</p>
      </div>
      <div class="footnote">
        <a class="footnote">3</a>
        <p> WAYNE R. LAFAVE, SEARCH AND SEIZURE &#167; 9.3(c), at 450-51 (2d ed. 1987) (footnotes omitted).   Accord United States v. Carter, <span class="citation" data-id="2290134"><a href="/opinion/2290134/united-states-v-carter/#27" aria-description="Citation for case: United States v. Carter">369 F.Supp. 26, 27-30</a></span> (E.D.Mo.1974) (no justification for stop where occupants of car "appeared [to officer] to be nervous" and "appeared surprised and disturbed at the presence of the police officer")</p>
        <p>"Nervousness in the presence of a police officer does not furnish a reasonable basis for a detention...."  People v. Loewen, <span class="citation" data-id="9531694"><a href="/opinion/1122661/people-v-loewen/" aria-description="Citation for case: People v. Loewen">35 Cal.3d 117</a></span>, <span class="citation" data-id="9531694"><a href="/opinion/1122661/people-v-loewen/#851" aria-description="Citation for case: People v. Loewen">196 Cal.Rptr. 846, 851</a></span>, <span class="citation" data-id="9531694"><a href="/opinion/1122661/people-v-loewen/#441" aria-description="Citation for case: People v. Loewen">672 P.2d 436, 441</a></span> (1983).  "Nervousness on the part of a black laborer when confronted by an armed uniformed officer does not seem so unusual as to indicate guilt or criminal proclivity."  State v. Scott, <span class="citation" data-id="1141153"><a href="/opinion/1141153/state-v-scott/#989" aria-description="Citation for case: State v. Scott">412 So.2d 988, 989</a></span> (La.1982).</p>
      </div>
      <div class="footnote" id="fn13">
        <a class="footnote" href="#fn13_ref">13</a>
        <p> "The 'high crime area' factor is not an 'activity' of an individual.   Many citizens ... are forced to live in areas that have 'high crime' rates or they come to these areas to shop, work, play, transact business, or visit relatives or friends.   The spectrum of legitimate human behavior occurs every day in so-called high crime areas."  People v. Bower, <span class="citation" data-id="9552492"><a href="/opinion/1187451/people-v-bower/" aria-description="Citation for case: People v. Bower">24 Cal.3d 638</a></span>, <span class="citation" data-id="9552492"><a href="/opinion/1187451/people-v-bower/#860" aria-description="Citation for case: People v. Bower">156 Cal.Rptr. 856, 860</a></span>, <span class="citation" data-id="9552492"><a href="/opinion/1187451/people-v-bower/#119" aria-description="Citation for case: People v. Bower">597 P.2d 115, 119</a></span> (1979)</p>
      </div>
      <div class="footnote" id="fn14">
        <a class="footnote" href="#fn14_ref">14</a>
        <p> The majority avers that "[t]hese [i.e., Rideau's specific moves taking place after a detention, at night, in a high crime area where weapons were common] are articulable facts upon which a police officer may legitimately rely in justifying his actions."   Maj. op. at 1575.   While these are permissible factors, the majority mentions only one Supreme Court case--Adams v. Williams, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U.S. 143</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">92 S.Ct. 1921</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">32 L.Ed.2d 612</a></span> (1972)--in support</p>
        <p>Williams is inapposite, though, as a review of the instant record shows how vapid the present facts are in comparison to those in Williams.   There, an officer was on patrol in a high-crime area when a known informant told him that the defendant was nearby in a car, carrying narcotics and a gun.   The officer proceeded to reach into the defendant's vehicle and remove the weapon from his waistband.   The Court concluded that "[w]hile properly investigating the activity of a person who was reported to be carrying narcotics and a concealed weapon and who was sitting alone in a car in a high-crime area at 2:15 in the morning, [the officer] had ample reason to fear for his safety."  <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#147" aria-description="Citation for case: Adams v. Williams">Id. at 147-48</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#1924" aria-description="Citation for case: Adams v. Williams">92 S.Ct. at 1924</a></span> (footnote omitted).   The Court even emphasized that its case was "stronger ... than obtains in the case of an anonymous telephone tip," <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">id. at 146</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#1923" aria-description="Citation for case: Adams v. Williams">92 S.Ct. at 1923</a></span>, thus suggesting that an anonymous tip might not have been enough to justify the search, even in a high-crime area.</p>
        <p>The Court reiterated the Terry rule as follows:  "[T]he policeman making a reasonable investigatory stop should not be denied the opportunity to protect himself from attack by a hostile suspect.  'When an officer is justified in believing that the individual whose suspicious behavior he is investigating at close range is armed and presently dangerous ...,' he may conduct a limited protective search for concealed weapons."  <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">Id.</a></span> (emphasis added) (quoting Terry, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 24</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#1881" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. at 1881</a></span>).   Rideau was not "hostile," and his actions were not "suspicious."</p>
      </div>
      <div class="footnote" id="fn15">
        <a class="footnote" href="#fn15_ref">15</a>
        <p> "The [majority] doth protest too much, methinks."   WILLIAM SHAKESPEARE, HAMLET act III, sc. ii, ln. 242.   The majority belabors its disclaimer, as though repetition can make it so.   E.g., "Of course, that an individual is in a high crime neighborhood at night is not in and of itself enough to support an officer's decision to stop or frisk him," Maj. op. at 1575;  "[w]e do not suggest that the police have a right to frisk anyone on the street at night in a high crime neighborhood," id. at 1575;  "[w]e do not depart from the rule that police officers must have specific and articulable facts indicating that their safety is in danger to justify a patdown.   Nor do we assert that a lawful detention is a license to frisk," id. at 1576.   The unfortunate fact is that by allowing an innocent action, such as taking two steps backward, to turn a situation in which no search is permitted into one in which a search is justified, the majority in effect has adopted the rule it purports to eschew:  that being in the wrong part of town at the wrong time of day deprives one of significant Fourth Amendment protections</p>
      </div>
      <div class="footnote" id="fn16">
        <a class="footnote" href="#fn16_ref">16</a>
        <p> Today's holding enhances an officer's opportunity to use general terms such as "nervousness" and "suspicious behavior" as pretexts to conduct searches of persons who the officer has no reason to believe has done anything wrong.   The requirement of "specific and articulable facts" should encompass more than the routine use of such generalities</p>
      </div>
      <div class="footnote" id="fn17">
        <a class="footnote" href="#fn17_ref">17</a>
        <p> I do not mean to posit that this court should never consider cases en banc when no party has suggested it.   In fact, we have done so twice recently in cases implicating the Fourth Amendment.   I.e., United States v. Pierre, <span class="citation" data-id="8994043"><a href="/opinion/9001504/united-states-v-pierre/" aria-description="Citation for case: United States v. Pierre">943 F.2d 6</a></span> (5th Cir.1991) (sua sponte granting rehearing en banc);  United States v. DeLeon-Reyna, <span class="citation" data-id="545167"><a href="/opinion/545167/united-states-v-mario-de-leon-reyna/" aria-description="Citation for case: United States v. Mario De Leon-Reyna">908 F.2d 1229</a></span> (5th Cir.1990) (same).   But we should take an extra look when the agency charged with enforcing the laws of the United States, and not known for its timidity in Fourth Amendment cases, decides that a case it has lost is not worthy of en banc review</p>
      </div>
    </div>
    
```

---

## GROUP: content/cases/United States v. Robinson (4th Cir. en banc).md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Robinson (4th Cir. en banc)"
type: case
citation: "846 F.3d 694 (2017)"
parallel_cite: ""
neutral_cite: "2017 WL 280727; 2017 U.S. App. LEXIS 1134"
court: "U.S. Court of Appeals, 4th Cir. (en banc)"
court_level: coa
circuit: ca4
year: 2017
date_decided: ""
docket: No. 14-4902
authority_weight: "Binding in-circuit — 4th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4340460/united-states-v-shaquille-robinson/"
  cluster_id: 4340460
  opinion_id: null
  identity_checked: true
lake:
  record_id: "United States v. Robinson (4th Cir. en banc)"
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: Illustrates a circuit split
related:
  - "[[Terry Stops and Reasonable Suspicion]]"
  - "[[Terry v. Ohio]]"
  - "[[Northrup v. City of Toledo Police Dept]]"
  - "[[United States v. Black]]"
  - "[[Adams v. Williams]]"
tags:
  - case
  - fourth-amendment
  - terry-stop
  - frisk
  - reasonable-suspicion
  - armed-and-dangerous
  - circuit-split
holding: "An officer who makes a lawful traffic stop and who reasonably suspects that one of the vehicle's occupants is armed may frisk that person for weapons without separately establishing that the person is dangerous, even where state law would allow the person to carry a concealed firearm; the danger justifying a protective frisk arises from the combination of a forced police encounter and the presence of a weapon, not from any illegality in the weapon's possession."
aliases:
  - "United States v. Robinson (4th Cir. en banc)"
  - "United States v. Robinson (4th Cir. 2017)"
  - United States v. Shaquille Robinson
---

# United States v. Robinson (4th Cir. en banc)

*846 F.3d 694 (4th Cir. 2017)* · U.S. Court of Appeals for the Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4340460 → en banc majority opinion 9871494 (Niemeyer, Circuit Judge, for the en banc court; 846 F.3d 694, decided Jan. 23, 2017). Caption disambiguated (worklist): the 4th Cir. en banc United States v. Shaquille Robinson, distinct from the SCOTUS search-incident United States v. Robinson (1973). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*696`). Frontier-split row (role: Illustrates a circuit split): in-circuit binding, persuasive elsewhere; the split posture is named in Treatment (LINT-21). S9 promotes. -->

## Background
Acting on an anonymous tip that a man in a Toyota Camry had loaded a firearm and concealed it in his pocket in a high-crime 7-Eleven parking lot in Ranson, West Virginia, police stopped the car for a seatbelt violation. Reasonably believing the passenger, Shaquille Robinson, was armed, an officer frisked him and found the gun; because Robinson was a felon, he was arrested for illegal possession of a firearm. Robinson moved to suppress, arguing the officers had no articulable basis to think he was *dangerous* — since West Virginia allows people to obtain permits to carry concealed firearms, being armed did not make him a threat. The district court denied suppression; Robinson pleaded guilty conditionally, a panel reversed, and the Fourth Circuit reheard the case [[Reading and Citing Cases#en-banc|en banc]].

## Issue
Whether an officer who lawfully stops a person and reasonably believes that person is armed may conduct a protective frisk, or whether — in a jurisdiction that permits carrying a concealed firearm — the officer must additionally have reasonable suspicion that the person is dangerous.

## Rule
The [[Reading and Citing Cases#en-banc|en banc]] court held that reasonable suspicion the stopped person is armed is enough; lawful eligibility to carry the weapon does not dissolve the risk. It held: "We reject Robinson's argument and affirm, concluding that an officer who makes a lawful traffic stop and who has a reasonable suspicion that one of the automobile's occupants is armed may frisk that individual for the officer's protection and the safety of everyone on the scene." — 846 F.3d at 696. ^pin-696

## Application
Reasoning from *[[Terry v. Ohio|Terry]]*, *[[Pennsylvania v. Mimms]]*, and *[[Adams v. Williams]]*, the court explained that the danger justifying a frisk arises from the combination of a forced police encounter and the presence of a weapon — not from any illegality in possessing it. It was therefore inconsequential that Robinson was a passenger, or that he might have been entitled to a concealed-carry permit: an officer forced into close quarters with an armed person need not "take unnecessary risks" by assuming the weapon poses no threat. The frisk was reasonable, and suppression was properly denied.

## Conclusion
The denial of Robinson's suppression motion was **affirmed**. Niemeyer, Circuit Judge, wrote for the [[Reading and Citing Cases#en-banc|en banc]] majority (ten judges joining). Wynn, J., concurred in the judgment; Harris, J., dissented, joined by Gregory, C.J., and Motz and Davis, JJ.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion.

**Illustrates a circuit split (in-circuit rule).** *Robinson* is the Fourth Circuit's [[Reading and Citing Cases#en-banc|en banc]] answer — binding there, persuasive only elsewhere — that a lawfully stopped person reasonably believed to be *armed* may be frisked without a separate showing of *dangerousness*, even in a right-to-carry jurisdiction. That reading divides the courts: the [[Common Legal Terms#dissenting-opinion|dissent]] and other authorities treat *[[Terry v. Ohio|Terry]]*'s "armed *and* dangerous" formula as requiring an independent basis to believe the person is dangerous, so that lawful gun possession alone cannot justify a frisk. It sits on the opposite side of the split from *[[Northrup v. City of Toledo Police Dept]]* (6th Cir.) and the reasoning of *[[United States v. Black]]*, which hold that lawful firearm possession, standing alone, does not supply the suspicion of dangerousness the Fourth Amendment requires. Teach *Robinson* as one pole of that split, not a nationally settled rule.

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Illustrates a circuit split*

## Sources
- [*United States v. Robinson*, 846 F.3d 694 (4th Cir. 2017) (en banc)](https://www.courtlistener.com/opinion/4340460/united-states-v-shaquille-robinson/) — pinpoint: 696 (Niemeyer, J., for the en banc court; the CL opinion text carries the reporter star `*696` immediately before the paragraph containing the quoted holding). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "aa50b84c5058000f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "846 F.3d 694 (2017)", "court": "U.S. Court of Appeals, 4th Cir. (en banc)", "neutral_cite": "2017 WL 280727; 2017 U.S. App. LEXIS 1134", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Robinson (4th Cir. en banc)", "year": "2017"}}
{"assertion_id": "7410e9f7e97765d1", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An officer who makes a lawful traffic stop and who reasonably suspects that one of the vehicle's occupants is armed may frisk that person for weapons without separately establishing that the person is dangerous, even where state law would allow the person to carry a concealed firearm; the danger justifying a protective frisk arises from the combination of a forced police encounter and the presence of a weapon, not from any illegality in the weapon's possession.", "title": "United States v. Robinson (4th Cir. en banc)"}}
{"assertion_id": "e0d0d8d764e3009f", "dimension": "support", "kind": "home_role", "locator": {"home": "Terry Stops and Reasonable Suspicion"}, "payload": {"home": "Terry Stops and Reasonable Suspicion", "role": "Illustrates a circuit split", "title": "United States v. Robinson (4th Cir. en banc)"}}
{"assertion_id": "0e18db7a5717fcad", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Robinson (4th Cir. en banc)", "varies_by_point": "false"}}
{"assertion_id": "8a8a9e964e7a00b6", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 4th Cir.", "title": "United States v. Robinson (4th Cir. en banc)"}}
```

### lake record — United States v. Robinson (4th Cir. en banc)

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Robinson (4th Cir. en banc)",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Shaquille Robinson",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Shaquille Montel ROBINSON, Defendant-Appellant",
    "input_case_name": "United States v. Robinson (4th Cir. en banc)",
    "court": "U.S. Court of Appeals, 4th Cir. (en banc)",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca4",
    "state": null,
    "date_decided": null,
    "year": 2017,
    "docket": "No. 14-4902",
    "cluster_id": 4340460,
    "lead_opinion_id": 9871494,
    "sibling_ids": [],
    "absolute_url": "/opinion/4340460/united-states-v-shaquille-robinson/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": false,
    "alternates": [],
    "reason_code": "caption_mismatch_accepted_by_case_name"
  },
  "citations": {
    "official": {
      "cite": "846 F.3d 694",
      "volume": "846",
      "reporter": "F.3d",
      "page": "694",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2017 WL 280727",
        "volume": "2017",
        "reporter": "WL",
        "page": "280727",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 U.S. App. LEXIS 1134",
        "volume": "2017",
        "reporter": "U.S. App. LEXIS",
        "page": "1134",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "846 F.3d 694",
        "volume": "846",
        "reporter": "F.3d",
        "page": "694",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 WL 280727",
        "volume": "2017",
        "reporter": "WL",
        "page": "280727",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 U.S. App. LEXIS 1134",
        "volume": "2017",
        "reporter": "U.S. App. LEXIS",
        "page": "1134",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "846 F.3d 694",
    "official_selection": {
      "court_class": "coa",
      "selected": "846 F.3d 694",
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
    "date_created": "2026-07-06T13:41:21Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [
      "input caption does not match CL canonical caption",
      "frontier identity accepted by case_name rung despite caption mismatch"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:41:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:41:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:41:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:41:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-robinson-4th-cir-en-banc--4340460",
      "to_record_id": "United States v. Robinson (4th Cir. en banc)",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Robinson (4th Cir. en banc)

```
<opinion type="majority">
<p id="b717-10">Affirmed by published opinion. Judge NIEMEYER wrote the majority opinion, in which Judge WILKINSON, Judge TRAXLER, Judge KING, Judge SHEDD, Judge DUNCAN, Judge AGEE, Judge KEENAN, Judge DIAZ, Judge FLOYD, and Judge THACKER joined. Judge WYNN wrote a separate opinion concurring in the judgment. Judge HARRIS wrote a dissenting opinion, in which Chief Judge GREGORY, Judge MOTZ, and Senior Judge DAVTS joined.</p>
<p id="b717-12">ON REHEARING EN BANC</p>
<author id="b717-13">NIEMEYER, Circuit Judge:</author>
<p id="b717-14">This appeal presents the question of whether a law enforcement officer is justified, in frisking a person whom the officer has lawfully stopped and whom the officer reasonably believes to be armed, regardless of whether the person may legally be entitled to carry the firearm. Stated otherwise, the question is whether the risk of danger to a law enforcement officer created by the forced stop of a person who is armed is eliminated by the fact that state law authorizes persons to obtain a permit to carry a concealed firearm.</p>
<p id="b717-15">After receiving a tip that a man in a parking lot well known for drug-trafficking activity had just loaded a firearm and then concealed it in his pocket before getting into a car as a passenger, Ranson, West Virginia police stopped the ear after observing that its occupants were not wearing seatbelts. Reasonably believing that the car’s passenger, • Shaquille Robinson, was armed, the police frisked him and uncovered the firearm, leading to his arrest for the possession of a firearm by a felon. .</p>
<p id="b717-16">During his prosecution, Robinson filed a motion to suppress the evidence recovered as a result of the frisk, contending that the frisk violated . his Fourth Amendment rights. The' officers, he argued, had no articulable facts demonstrating that he was dangerous since, as far as the officers knew, the State could have issued him a permit to earry a concealed firearm. After the district court denied the motion to suppress, Robinson pleaded guilty to the illegal possession of a firearm, reserving <page-number citation-index="1" label="696">*696</page-number>the right to appeal the denial of his motion to suppress.</p>
<p id="b718-4">On appeal, Robinson contends again that the information that police received from the tip described seemingly innocent conduct and that his conduct at the time of the traffic stop also provided no basis for officers to reach the conclusion that he was dangerous. He argues, “Under the logic of the district court, in any state where carrying a firearm is a perfectly legal activity, every citizen could be dangerous, and subject to a <em>Terry </em>frisk and pat down.”</p>
<p id="b718-5">We reject Robinson’s argument and affirm, concluding that an officer who makes a lawful traffic stop and who has a reasonable suspicion that one of the automobile’s occupants is armed may frisk that individual for the officer’s protection and the safety of everyone on the scene. <em>See Pennsylvania v. Mimms, </em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#112" aria-description="Citation for case: Pennsylvania v. Mimms">434 U.S. 106, 112</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">98 S.Ct. 330</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">54 L.Ed.2d 331</a></span> (1977) (per curiam). The Fourth Amendment does not “require ... police officers [to] take unnecessary risks in the performance of their duties.” <em>Terry v. Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#23" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1, 23</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span> (1968). And it is inconsequential that the person thought to be armed was a passenger. <em>See Maryland v. Wilson, </em><span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#414" aria-description="Citation for case: Maryland v. Wilson">519 U.S. 408, 414</a></span>, <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">117 S.Ct. 882</a></span>, <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">137 L.Ed.2d 41</a></span> (1997). It is also inconsequential that the passenger may have had a permit to carry the concealed firearm. The danger justifying a protective frisk arises from the combination of a forced police encounter and the presence of a weapon, not from any illegality of the weapon’s possession. <em>See Adams v. Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U.S. 143, 146</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">92 S.Ct. 1921</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">32 L.Ed.2d 612</a></span> (1972); <em>Michigan v. Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U.S. 1032</a></span>, 1052 n.16, <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">103 S.Ct. 3469</a></span>, <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">77 L.Ed.2d 1201</a></span> (1983).</p>
<p id="b718-6">I</p>
<p id="b718-7">The material facts in this case are not disputed. At about 3:55 p.m. on March 24, 2014, an unidentified man called the Ran-son, West Virginia Police Department and told Officer Crystal Tharp that he had just “witnessed a black male in a bluish greenish Toyota Camry load a firearm [and] conceal it in his pocket” while in the parking lot of the 7-Eleven on North Mildred Street. The caller advised Officer Tharp that the Camry was being driven by a white woman and had “just left” the parking lot, traveling south on North Mildred Street.</p>
<p id="b718-9">The 7-Eleven on North Mildred Street is adjacent to the Apple Tree Garden Apartments, and the area constitutes the highest crime area in Ranson. One officer who testified said that in his short one and a half years as a state trooper, he had experience with at least 20 incidents of drug trafficking in the 7-Eleven parking lot. Another officer testified that “when [she] was doing drug work[,] ... [she] dropped an informant off to buy drugs” at the 7-Eleven parking lot and observed “three other people waiting for drugs in that parking lot.” She added that she had personally received “numerous complaints” of people running between the parking lot and the apartment complex, making drug transactions. Another officer testified that “[a]nytime you hear Apple Tree or 7-Elev-en, your radar goes up a notch.” Accordingly, when the Ranson Police Department received the tip about someone loading a gun in the 7-Eleven parking lot, its officers’ “radar [went] up a notch,” and the officers went “on heightened alert.”</p>
<p id="b718-10">While still on the telephone with the caller, Officer Tharp relayed the information to Officer Kendall Hudson and Captain Robbie Roberts. Hudson immediately left the station to respond to the call, and Roberts left soon thereafter to provide backup.</p>
<p id="b719-4"><page-number citation-index="1" label="697">*697</page-number>When Officer Hudson turned onto North Mildred Street a short time later, he observed a blue-green Toyota Camry being driven by a white woman with a black male passenger. Noticing that they were not wearing seatbelts, Hudson effected a traffic stop approximately seven blocks, or three-quarters of a mile, south of the 7-Eleven. He estimated that the traffic stop took place two to three minutes after the call had been received at the station.</p>
<p id="b719-5">After calling in the stop, Officer Hudson approached the driver’s side of the vehicle with his weapon drawn but carried below his waist and asked the driver for her license, registration, and proof of insurance. He also asked the male passenger, the defendant Robinson, for his identification but quickly realized that doing so was “probably not a good idea” because “[t]his guy might have a gun[,] [and] I’m asking him to get into his pocket to get his I.D.” Instead, Officer Hudson asked Robinson to step out of the vehicle.</p>
<p id="b719-6">At this point, Captain Roberts arrived and opened the front passenger door. As Robinson was exiting the vehicle, Captain Roberts asked him if he had any weapons on him. Instead of responding verbally, Robinson “gave [Roberts] a weird look” or, more specifically, an “‘oh, crap’ look[].” Roberts took the look to mean, “I don’t want to lie to you, but I’m not going to tell you anything [either].” At this point, Captain Roberts directed Robinson to put his hands on top of the car and performed a frisk for weapons, recovering a loaded gun from the front pocket of Robinson’s pants. After conducting the frisk, Roberts recognized Robinson, recalled that he had previously been convicted of a felony, and arrested him.</p>
<p id="b719-7">After Robinson was charged with the illegal possession of a firearm by a felon, in violation of <span class="citation no-link">18 U.S.C. § 922</span>(g)(1), he filed a motion to suppress the evidence of the firearm and ammunition seized during the frisk, arguing that the frisk violated his Fourth Amendment rights.</p>
<p id="b719-9">The district court denied the motion, concluding that the officers possessed reasonable suspicion to believe that Robinson was armed and dangerous. Relying on <em>Navarette v. California, </em>— U.S. —, <span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/" aria-description="Citation for case: Prado Navarette v. California">134 S.Ct. 1683</a></span>, <span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/" aria-description="Citation for case: Prado Navarette v. California">188 L.Ed.2d 680</a></span> (2014), the court concluded that the anonymous caller’s eyewitness knowledge and the contemporaneous nature of the report indicated that the tip was sufficiently reliable to contribute to the officers’ reasonable suspicion. The court explained that the “anonymous tip that [Robinson] [had] recently loaded a firearm and concealed it on his person in a public parking lot in a high-crime area,” as well as Robinson’s “weird look and failure to verbally respond to the inquiry whether he was armed,” gave rise to a reasonable suspicion that Robinson was armed and dangerous.</p>
<p id="b719-11">Robinson thereafter pleaded guilty to the firearm possession charge, reserving his right to appeal the district court’s denial of his suppression motion, and the district court sentenced him to 37 months’ imprisonment. Robinson appealed the denial of his motion to suppress, and a panel of this court reversed the district court’s decision denying Robinson’s motion to suppress and vacated his conviction and sentence. <em>United States v. Robinson, </em><span class="citation" data-id="9821731"><a href="/opinion/3179638/united-states-v-shaquille-robinson/#213" aria-description="Citation for case: United States v. Shaquille Robinson">814 F.3d 201, 213</a></span> (4th Cir. 2016). By order dated April 25, 2016, we granted the government’s petition for rehearing <em>en banc, </em>which vacated the panel’s judgment and opinion. <em>See </em>4th Cir. Local R. 35(c).</p>
<p id="b719-12">II</p>
<p id="b719-13">Robinson’s appeal is defined as much by what he concedes as by what he challenges. Robinson rightfully acknowledges that the Ranson police had the right to <page-number citation-index="1" label="698">*698</page-number>stop the vehicle in which he was a passenger after observing a traffic violation, <em>see Whren v. United States, </em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#819" aria-description="Citation for case: Whren v. United States">517 U.S. 806, 819</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S.Ct. 1769</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L.Ed.2d 89</a></span> (1996), and also that they had the authority to direct him to exit the vehicle during the valid traffic stop, <em>see Wilson, </em><span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#415" aria-description="Citation for case: Maryland v. Wilson">519 U.S. at 415</a></span>, <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">117 S.Ct. 882</a></span>. He also correctly concedes that the anonymous tip received by the Ranson Police Department was sufficiently reliable to justify the officers’ reliance on it. <em>See Navarette, </em><span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/#1688" aria-description="Citation for case: Prado Navarette v. California">134 S.Ct. at 1688-89</a></span> (concluding that an anonymous 911 call “bore adequate indicia of reliability for the officer to credit the caller’s account” in large part because, like here, the caller “claimed eyewitness knowledge of the alleged [conduct]” and the call was a “contemporaneous report” that was “made under the stress of excitement caused by a startling event”). Finally, and most importantly, Robinson does not contest the district court’s conclusion that the police had reasonable suspicion to believe that he was armed.</p>
<p id="b720-6">Robinson’s argument focuses on whether the officers could reasonably have suspected that he was dangerous. He argues that while the officers may well have had good reason to suspect that he was carrying a loaded concealed firearm, they lacked objective facts indicating <em>that he was also dangerous, </em>so as to justify a frisk for weapons, since an officer must reasonably suspect that the person being frisked is both armed <em>and </em>dangerous. <em>See Terry, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 27</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>. Robinson notes that at the time of the frisk, West Virginia residents could lawfully carry a concealed firearm if they had received a license from the State. <em>See </em><span class="citation no-link">W. Va. Code § 61-7-3</span> to -4 (2014). And, because the police did not know whether or not he possessed such a license, the tip that a suspect matching his description was carrying a loaded firearm concealed in his pocket was, he argues, a report of <em>innocent behavior </em>that was not sufficient to indicate that he posed a danger to others. Moreover, he argues, his behavior during the stop did not create suspicion—“he was compliant, cooperative, [and] not displaying signs of nervousness.” In these circumstances, he concludes, the officer’s frisk was not justified by any reasonable suspicion that he was <em>dangerous.</em></p>
<p id="AlV">Robinson’s argument presumes that the legal possession of a firearm cannot pose a danger to police officers during a forced stop, and it collapses the requirements for making a stop with the requirements for conducting a frisk. It thus fails at several levels when considered under the Supreme Court’s “stop-and-frisk” jurisprudence. First, Robinson confuses the standard for making stops—which requires a reasonable suspicion <em>that a crime or other infraction has been or is being </em>committed—with the standard for conducting a frisk—which requires both a lawful investigatory stop and a reasonable suspicion <em>that the person stopped is armed and dangerous. See Arizona v. Johnson, </em><span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/#326" aria-description="Citation for case: Arizona v. Johnson">555 U.S. 323, 326-27</a></span>, <span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">129 S.Ct. 781</a></span>, <span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">172 L.Ed.2d 694</a></span> (2009). Second, he fails to recognize that traffic stops alone are inherently dangerous for police officers. Third, he also fails to recognize that traffic stops of persons who are armed, whether legally or illegally, pose yet a greater safety risk to police officers. And fourth, he argues illogically that when a person forcefully stopped may be <em>legally </em>permitted to possess a firearm, any risk of danger to police officers posed by the firearm is eliminated.</p>
<p id="b720-9">We begin by noting that the Supreme Court has repeatedly recognized that whenever police officers use their authority to effect a stop, they subject themselves to a risk of harm. This holds true whether the temporary detention is a traditional, <page-number citation-index="1" label="699">*699</page-number>“on-the-street” <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop to investigate an officer’s reasonable suspicion “that the person apprehended is committing or has committed a criminal offense,” <em>Johnson, </em><span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/#326" aria-description="Citation for case: Arizona v. Johnson">555 U.S. at 326</a></span>, <span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">129 S.Ct. 781</a></span>, or a stop of a motor vehicle and all of its occupants to enforce a jurisdiction’s traffic laws, <span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/#327" aria-description="Citation for case: Arizona v. Johnson"><em>id. </em>at 327</a></span>,<span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">129 S.Ct. 781</a></span>. The. Supreme Court has explained that “the risk of a violent encounter in a traffic-stop setting ‘stems not from the ordinary reaction of a motorist stopped for a speeding violation, but from the fact that evidence of a more serious crime might be uncovered during the stop.’” <span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/#331" aria-description="Citation for case: Arizona v. Johnson"><em>Id. </em>at 331</a></span>, <span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">129 S.Ct. 781</a></span> (quoting <em>Wilson, </em><span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#414" aria-description="Citation for case: Maryland v. Wilson">519 U.S. at 414</a></span>, <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">117 S.Ct. 882</a></span>); <em>see also Mimms, </em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#110" aria-description="Citation for case: Pennsylvania v. Mimms">434 U.S. at 110</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">98 S.Ct. 330</a></span> (rejecting “the argument that traffic violations necessarily involve less danger to officers than other types of confrontations”). Indeed, the Court has concluded that traffic stops are “especially fraught with danger to police officers.” <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1047" aria-description="Citation for case: Michigan v. Long">463 U.S. at 1047</a></span>, <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">103 S.Ct. 3469</a></span>. And the Court has also observed that when the stop involves one or more passengers, that fact “increases the possible sources of harm to the officer,” <em>Wilson, </em><span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#413" aria-description="Citation for case: Maryland v. Wilson">519 U.S. at 413</a></span>, <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">117 S.Ct. 882</a></span>, as “the motivation of a passenger to employ violence ... is every bit as great as that of the driver,” <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#414" aria-description="Citation for case: Maryland v. Wilson"><em>id. </em>at 414</a></span>,<span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">117 S.Ct. 882</a></span>.</p>
<p id="b721-4">In <em><span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">Wilson</a></span>, </em>the Court observed that “[i]n 1994 alone, there were 5,762 officer assaults and 11 officers killed during traffic pursuits and stops,” <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#413" aria-description="Citation for case: Maryland v. Wilson">519 U.S. at 413</a></span>, <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">117 S.Ct. 882</a></span>, prompting the Court to conclude that the public interest in police officer safety during traffic stops is “both legitimate and weighty,” <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#412" aria-description="Citation for case: Maryland v. Wilson"><em>id. </em>at 412</a></span>, <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">117 S.Ct. 882</a></span> (quoting <em>Mimms, </em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#110" aria-description="Citation for case: Pennsylvania v. Mimms">434 U.S. at 110</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">98 S.Ct. 330</a></span>). And more recent statistics, unfortunately, remain as grim. Of the 51 law enforcement officers feloniously killed in the line of duty in 2014, 9 officers (or 18%) were fatally injured during traffic pursuits or stops. FBI, <em>Officers Feloniously Killed, in </em>Uniform Crime Reports: Law Enforcement Officers Killed and Assaulted, 2014.</p>
<p id="b721-7">To be clear, the general risk that is inherent during a traffic stop does not, without more, justify a frisk of the automobile’s occupants. But the risk inherent in all .traffic stops is heightened exponentially when.the person who has been stopped—a person whose propensities are unknown— is “armed with - a weapon that could unexpectedly and fatally be used against” the officer in a matter of seconds. <em>Terry, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#23" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 23</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>. As such, when the officer reasonably suspects that the person he has stopped is armed, the officer is “warranted in the belief that his safety ... [is] in danger,” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><em>id. </em>at 27</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, thus justifying a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>frisk.</p>
<p id="b721-8">In <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>Officer McFadden “seized” Terry on the street and subjected him to a “search” without probable cause to believe that he had committed or was committing a crime or that he was armed, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 19</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>. The Court was thus confronted with two distinct constitutional issues: <em>first, </em>whether a person could be stopped (seized) on suspicion of criminal conduct that fell short of probable cause; and <em>second, </em>whether the officer could conduct a protective frisk or “pat down” for weapons (search) during the stop. The Court .readily concluded that Terry’s seizure was “reasonable” under the Fourth Amendment because the officer reasonably believed that criminal conduct was afoot. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio"><em>Id. </em>at 22-23</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>. The Court then turned its attention to the legality of the frisk, stating, “We are now concerned with more than the governmental interest in investigating crime; in addition, there is the more immediate interest of the police officer in taking steps to assure himself that the person with whom he is dealing is not armed with a weapon that could-unexpectedly and fatally be used against him.” <page-number citation-index="1" label="700">*700</page-number><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#23" aria-description="Citation for case: Terry v. Ohio"><em>Id. </em>at 23</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>. The <em>concern—i.e., </em>the danger—was thus found in <em>the presence of a weapon during a forced police encounter. </em>Indeed, the Court said as much, noting in approving Officer McFadden’s frisk of Terry that “a reasonably prudent man would have been warranted in believing petitioner was armed <em>and thus presented a threat to the officer’s safety.” Id. </em>at 28, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span> (emphasis added). In this manner, the Court adopted the now well-known standard that an officer can frisk a validly stopped person if the officer reasonably believes that the person is “armed and dangerous.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><em>Id. </em>at 27</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>; <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#32" aria-description="Citation for case: Terry v. Ohio"><em>see also id. </em>at 32</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span> (Harlan, J., concurring) (explaining that because a “frisk is justified in order to protect the officer during an encounter with a citizen, the officer must first have constitutional grounds to insist on an encounter, to make a forcible stop”).</p>
<p id="b722-4">The Supreme Court applied <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>to circumstances analogous to those before us in <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span>, </em>where an officer, after making a routine traffic stop, “noticed a large bulge” under the defendant’s jacket and therefore conducted a frisk. <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#107" aria-description="Citation for case: Pennsylvania v. Mimms">434 U.S. at 107</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">98 S.Ct. 330</a></span>. Holding that the frisk was clearly justified, the <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span> </em>Court explained that “[t]he bulge in the jacket permitted the officer to conclude that Mimms was armed <em>and thus posed a serious and present danger to the safety of the officer,” </em>adding that “[i]n these circumstances, any man of ‘reasonable caution’ would likely have conducted the ‘pat down.’ ” <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#112" aria-description="Citation for case: Pennsylvania v. Mimms"><em>Id. </em>at 112</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">98 S.Ct. 330</a></span> (emphasis added). The only evidence of Mimms’ dangerousness was the bulge indicating that he was armed. <em>See <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">id.</a></span> </em>It was thus Mimms’ status of being armed during a forced police encounter (the traffic stop) that posed the danger justifying the frisk, and we have previously relied on <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span> </em>for that precise principle. <em>See United States v. Baker, </em><span class="citation" data-id="714150"><a href="/opinion/714150/united-states-v-anthony-marcellus-baker/#137" aria-description="Citation for case: United States v. Anthony Marcellus Baker">78 F.3d 135, 137</a></span> (4th Cir. 1996) (citing <em>Mimms, </em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#112" aria-description="Citation for case: Pennsylvania v. Mimms">434 U.S. at 112</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">98 S.Ct. 330</a></span>) (“Based on the inordinate risk of danger to law enforcement officers during traffic stops, observing a bulge that could be made by a weapon in a suspect’s clothing reasonably warrants a belief that the suspect is potentially dangerous, even if the suspect was stopped only for a minor violation”).</p>
<p id="b722-6">In short, established Supreme Court law imposes two requirements for conducting a frisk, but no more than two: <em>first, </em>that the officer have conducted a lawful stop, which includes both a traditional <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop as well as a traffic stop; and <em>second, </em>that during the valid but forced encounter, the officer reasonably suspect that the person is <em>armed and therefore dangerous. </em>In both Terry. and <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span>, </em>the Court deliberately linked “armed” and “dangerous,” recognizing that the frisks in those cases were lawful because the stops were valid and the officer reasonably believed that the person stopped “was armed <em>and thus” </em>dangerous. <em>Terry, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#28" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 28</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span> (emphasis added); <em>Mimms, </em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#112" aria-description="Citation for case: Pennsylvania v. Mimms">434 U.S. at 112</a></span>, <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">98 S.Ct. 330</a></span> (emphasis added). The use of “and thus” recognizes that the risk of danger is created simply because the person, who was forcibly stopped, is armed.</p>
<p id="b722-7">In this case, both requirements—a lawful stop and a reasonable suspicion that Robinson was armed—were satisfied, thus justifying Captain Roberts’ frisk under the Fourth Amendment as a matter of law.</p>
<p id="b722-8">Robinson argues that <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span> </em>is distinguishable because the frisk there took place in a jurisdiction that made it a crime to carry a concealed deadly weapon. West Virginia, on the other hand, generally permits its citizens to carry firearms. From this distinction, Robinson argues that when the person forcibly stopped may be <em>legally </em>permitted to possess a firearm, the <page-number citation-index="1" label="701">*701</page-number>risk of danger posed by the firearm is eliminated. This argument, however, fails under the Supreme Court’s express recognition that the legality of the frisk does not depend on the illegality of the firearm’s possession. Indeed, the Court has twice explained that “[t]he purpose of this limited search <em>[ie., </em>the frisk] is not to discover evidence of crime, but to allow the officer to pursue his investigation without fear of violence, and thus the frisk for weapons might be equally necessary and reasonable, <em>whether or not carrying a concealed weapon violated any applicable state law” Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U.S. at 146</a></span>, <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">92 S.Ct. 1921</a></span> (emphasis added); <em>see also Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U.S. at 1052</a></span> n.16, <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">103 S.Ct. 3469</a></span> (“[W]e have expressly rejected the view that the validity of a <em>Temj </em>search <em>[ie., </em>a frisk] depends on whether the weapon is possessed in accordance with state law”). Robinson’s position directly conflicts with these observations.</p>
<p id="b723-5">Notwithstandipg the Supreme Court’s statements, Robinson’s position also fails as a matter of logic to recognize that the risk inherent in a forced stop of a person who is armed exists even when the firearm is legally possessed. The presumptive lawfulness of an individual’s gun possession in a particular State does next to nothing to negate the reasonable concern an officer has for his own safety when forcing an encounter with an individual who is armed with a gun and whose propensities are unknown. <em>See United States v. Rodriguez, </em><span class="citation" data-id="2647900"><a href="/opinion/2647900/united-states-v-rodriguez/#491" aria-description="Citation for case: United States v. Rodriguez">739 F.3d 481, 491</a></span> (10th Cir. 2013) (concluding that “an officer making a lawful investigatory stop [must have] the ability to protect himself from an armed suspect whose propensities are unknown” and therefore rejecting the defendant’s argument that the officer “had no reason to believe he was dangerous” even though the officer had seen a handgun tucked into the waistband of his pants).</p>
<p id="A_1">Accordingly, we conclude that given Robinson’s concession that he was lawfully stopped and that the police officers had reasonable suspicion to believe that he was armed, the officers were, as a matter of law, justified in frisking him and, in doing so, did not violate Robinson’s Fourth Amendment rights.</p>
<p id="b723-7">Ill</p>
<p id="b723-8">While the lawful traffic stop of Robinson and the reasonable suspicion that he was armed justified the frisk in this case, the officers had knowledge of additional facts that increased the level of their suspicion that Robinson was dangerous.</p>
<p id="b723-9">First, the reliable tip in this case was not just that an individual matching Robinson’s description possessed a firearm. Rather, the caller reported that he had observed an individual “load a firearm [and] conceal it in his pocket” while in the parking lot of the 7-Eleven on North Mildred Street, a location that the officers knew to be a popular spot for drug-trafficking activity. Four officers testified about the high level of drug-trafficking and other criminal activity in that particular parking lot, prompting one to explain, “[a]nytime you hear ... 7-Eleven, your radar goes up a notch.” Knowing that the 7-Eleven parking lot was frequently used as a site for drug trafficking, a reasonable officer could legitimately suspect that an individual who was seen both loading and concealing a firearm in that very parking lot may well have been doing so in connection with drug-trafficking activity, making his possession of a firearm even more dangerous. <em>See United States v. Lomax, </em><span class="citation" data-id="778011"><a href="/opinion/778011/united-states-v-clarence-j-lomax/#705" aria-description="Citation for case: United States v. Clarence J. Lomax">293 F.3d 701, 705</a></span> (4th Cir. 2002) (recognizing the “numerous ways in which a firearm might further or advance drug trafficking”).</p>
<p id="b723-10">Second, when Captain Roberts asked Robinson, as he was getting out of the car, <page-number citation-index="1" label="702">*702</page-number>whether he was carrying any firearms, Robinson failed to respond verbally and instead gave the officer an ‘“oh, crap’ look[],” which Roberts took to mean, “I don’t want to lie to you, but I’m not going to tell you anything [either].” Surely, Robinson’s evasive response further heightened Captain Roberts’ legitimate concern as to the dangerousness of the situation.</p>
<p id="b724-4">While not necessary to the conclusion in this case, these facts can only confirm Captain Roberts’ reasonable suspicion that Robinson was dangerous and therefore should be frisked for the protection of the officer and all others present. Indeed, in light of all of the circumstances known to Captain Roberts, he would unquestionably have been criticized for not conducting a frisk if, after having failed to do so, something untoward had happened.</p>
<p id="pAjI">[[Image here]]</p>
<p id="b724-5">The judgment of the district court is accordingly</p>
<p id="AJ3b">
<em>AFFIRMED.</em>
</p>
</opinion>
```

---

## GROUP: content/cases/United States v. Ruckman.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Ruckman
type: case
citation: "806 F.2d 1471 (1986)"
parallel_cite: 55 U.S.L.W. 2398
neutral_cite: 1986 U.S. App. LEXIS 34802
court: 10th Cir.
court_level: coa
circuit: ca10
year: 1986
date_decided: 1986-12-18
docket: 85-2801
authority_weight: "Binding in-circuit — 10th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/480405/united-states-v-frank-william-ruckman/"
  cluster_id: 480405
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Ruckman
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Tents]]"
    role: Key
related:
  - "[[Tents]]"
  - "[[Katz v. United States]]"
  - "[[Oliver v. United States]]"
tags:
  - case
  - fourth-amendment
  - reasonable-expectation-of-privacy
  - public-land
  - dwelling
  - open-fields
  - tenth-circuit
holding: "A person who lives without authorization in a natural cave on federal public land has no objectively reasonable expectation of privacy in it, because he can be ousted by the managing authorities at any time; the cave is not a Fourth Amendment 'house,' so the warrantless search that produced the charged contraband did not fall within the Fourth Amendment's protection, and the denial of suppression was affirmed."
aliases:
  - United States v. Ruckman
  - "United States v. Ruckman (10th Cir. 1986)"
---

# United States v. Ruckman

*806 F.2d 1471 (10th Cir. 1986)* (No. 85-2731) · U.S. Court of Appeals for the Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 480405 → lead opinion 480405 (McWilliams, J.; 806 F.2d 1471, decided 1986-12-18). Header docket 85-2731 is the opinion caption; the lake/projected docket (85-2801) is stale — S2 data note. Rule quote string-matched to the CL opinion text 2026-07-07; paragraph-style pin (CL text is paragraph-numbered with no reporter star-pagination or cross-reference — per orchestrator adjudication). S9 promotes. -->

## Background
Frank William Ruckman was convicted by a jury of the unlawful possession of thirteen unregistered anti-personnel booby traps — destructive devices under 26 U.S.C. § 5861(d) — and received a suspended sentence and three years' probation. Before trial he moved to suppress the physical evidence seized in a warrantless search of what he called his "home." On the agreed facts, that "home" was a natural cave in a remote area about twenty-four miles northeast of St. George, Utah, on land owned by the United States and administered by the Bureau of Land Management. Ruckman had lived in and around the cave for roughly eight months and had fashioned a crude entrance wall and door. After he failed to appear on a state misdemeanor charge, a state arrest warrant issued, and state and federal authorities went to the cave to arrest him; he was not there, and they searched the cave.

## Issue
Whether a person who occupies a cave on federal public land without authorization has a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in it that brings a warrantless search within the protection of the Fourth Amendment.

## Rule
The Fourth Amendment protects people, not places, but whether protection attaches still turns on the place — and a squatter on public land he may be ousted from at any time holds no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] there, nor is such a cave a constitutionally protected "house." As the court held: "Without belaboring the matter, we decline to hold that the instant case comes within the ambit of the Fourth Amendment. The fact that Ruckman may have subjectively deemed the cave to be his 'castle' is not decisive of the present problem." — 806 F.2d 1471 (10th Cir. 1986) (majority op. ¶ 9). ^pin-9

## Application
Whatever subjective expectation of privacy Ruckman held in the cave, the court found it unreasonable: he occupied federal land he had no right to occupy, and the BLM could have ousted him at any time, so his tenure carried no legitimate privacy interest that society would recognize. His own counsel had characterized the stay as extended camping rather than a permanent residence, and the makeshift wall and door did not transform an unauthorized cave on the public domain into a Fourth Amendment "house." Drawing on the open-fields line and cases denying privacy to those occupying public or unlawfully held land, the court declined to extend Fourth Amendment protection to the search, and the suppression motion was properly denied.

## Conclusion
**Affirmed.** Judge McWilliams wrote for the panel (McKay, Tacha, and McWilliams, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Ruckman* is a frequently taught illustration on the outer edge of the "home": an **unauthorized dwelling on public land** — a cave the occupant can be evicted from at will — carries no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] and is not a Fourth Amendment "house." Read it against *[[Katz v. United States|Katz]]* (privacy, not places) and the *[[Oliver v. United States|Oliver]]* open-fields line, and note that the result turns on the unauthorized, oustable character of the occupancy rather than on the crudeness of the shelter.

## Appears on
- [[Tents]] — *Key*

## Sources
- [*United States v. Ruckman*, 806 F.2d 1471 (10th Cir. 1986)](https://www.courtlistener.com/opinion/480405/united-states-v-frank-william-ruckman/) — pinpoint: majority op. ¶ 9 (no reasonable expectation of privacy in a cave occupied without authorization on federal public land; the CL opinion text is paragraph-numbered with no reporter star-pagination, so the pin is paragraph-style per the orchestrator's adjudication). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a8f187f7b52334a6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "806 F.2d 1471 (1986)", "court": "10th Cir.", "neutral_cite": "1986 U.S. App. LEXIS 34802", "official_citation_present": true, "parallel_cite": "55 U.S.L.W. 2398", "title": "United States v. Ruckman", "year": "1986"}}
{"assertion_id": "1a4820158fa5babc", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A person who lives without authorization in a natural cave on federal public land has no objectively reasonable expectation of privacy in it, because he can be ousted by the managing authorities at any time; the cave is not a Fourth Amendment 'house,' so the warrantless search that produced the charged contraband did not fall within the Fourth Amendment's protection, and the denial of suppression was affirmed.", "title": "United States v. Ruckman"}}
{"assertion_id": "e8def61deb40601a", "dimension": "support", "kind": "home_role", "locator": {"home": "Tents"}, "payload": {"home": "Tents", "role": "Key", "title": "United States v. Ruckman"}}
{"assertion_id": "3344e740d29798ba", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Ruckman", "varies_by_point": "false"}}
{"assertion_id": "40f91805746fb39b", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 10th Cir.", "title": "United States v. Ruckman"}}
```

### lake record — United States v. Ruckman

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Ruckman",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Frank William Ruckman",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Frank William RUCKMAN, Defendant-Appellant",
    "input_case_name": "United States v. Ruckman",
    "court": "10th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca10",
    "state": null,
    "date_decided": "1986-12-18",
    "year": 1986,
    "docket": "85-2801",
    "cluster_id": 480405,
    "lead_opinion_id": 9475634,
    "sibling_ids": [],
    "absolute_url": "/opinion/480405/united-states-v-frank-william-ruckman/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "806 F.2d 1471",
      "volume": "806",
      "reporter": "F.2d",
      "page": "1471",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "55 U.S.L.W. 2398",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "2398",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. App. LEXIS 34802",
        "volume": "1986",
        "reporter": "U.S. App. LEXIS",
        "page": "34802",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "806 F.2d 1471",
        "volume": "806",
        "reporter": "F.2d",
        "page": "1471",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. App. LEXIS 34802",
        "volume": "1986",
        "reporter": "U.S. App. LEXIS",
        "page": "34802",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 2398",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "2398",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "806 F.2d 1471",
    "official_selection": {
      "court_class": "coa",
      "selected": "806 F.2d 1471",
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
    "date_created": "2026-07-07T18:19:00Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:19:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:19:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:19:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:19:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-ruckman--480405",
      "to_record_id": "United States v. Ruckman",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Ruckman

```
<opinion data-order="7" data-type="opinion" id="x999-1" type="majority">
<author id="b1555-21">MCWILLIAMS, Circuit Judge.</author>
<p id="b1555-22">After examining the briefs and the appellate record, this three-judge panel has determined unanimously that oral argument would not be of material assistance in the determination of this appeal. <em>See </em>Fed.R.App.P. 34(a); Tenth Cir.R. 10(e). The cause is therefore ordered submitted without oral argument.</p>
<p id="b1555-23">Frank William Ruckman was convicted August 7, 1985, by a jury for the unlawful possession of destructive devices within the meaning of <span class="citation no-link">26 U.S.C. § 5845</span>(f)(3), namely, the possession of 13 anti-personnel booby traps which were not registered to Ruck-man in the National Firearms Registration and Transfer Record as required by <span class="citation no-link">26 U.S.C. § 5841</span>, all in violation of <span class="citation no-link">26 U.S.C. § 5861</span>(d). Ruckman was given a suspended sentence and placed on probation for three years. Ruckman now appeals. We affirm.</p>
<p id="b1555-24">Prior to trial, Ruckman moved to suppress the use at trial of any and all physical evidence seized in a warrantless search <page-number citation-index="1" label="1472">*1472</page-number>of his “home.” This search resulted in the seizure, <em>inter alia, </em>of the items which formed the basis for the charge above referred to. No testimony was offered at the hearing on the motion to suppress, counsel for Ruckman and the United States being in apparent agreement as to the critical facts. After argument of counsel, which included considerable colloquy between counsel and the court, the court, by minute order, denied the motion without any comment. Accordingly, we do not have benefit of the trial court’s thinking on the issue raised.</p>
<p id="b1556-4">From the record, it is agreed that the “home” which was searched by the authorities was a “cave” located in a remote area some 24 miles northeast of St. George, Utah, on land owned by the United States and controlled by the Bureau of Land Management (BLM). It is referred to as being a “natural cave,” as opposed, apparently, to a “man-made cave.” Ruckman had lived in and around the cave some eight months prior to the events which formed the basis for the present proceeding. Ruckman had attempted to “enclose” the cave by fashioning a crude entrance wall from boards and other materials which surrounded a so-called “door.”</p>
<p id="b1556-5">The fact that Ruckman was living in the cave area apparently became known to the local authorities. A state warrant calling for Ruckman’s arrest issued when Ruck-man failed to appear in state court to answer a misdemeanor charge. State and federal authorities later went to the cave area to arrest Ruckman on the state warrant. When the authorities arrived at the scene, Ruckman was nowhere to be found. In this setting, the authorities searched the cave. Certain firearms were found and seized. About this time, Ruckman appeared on the scene, and he was arrested and given his <em>Miranda </em>warning. Asked if there were any other weapons in the cave, Ruckman stated that there was a “shotgun in the comer.” The shotgun was located and seized. Ruckman was then taken to the local jail.</p>
<p id="b1556-6">Eight days later, the BLM agents and local authorities returned to the cave to “clean it out” and remove Ruckman’s belongings. In cleaning out, the authorities found, and seized, the anti-personnel booby traps which formed the basis for the present prosecution.</p>
<p id="b1556-7">Counsel agree that the ultimate issue is whether Ruckman had a right under the Fourth Amendment to be free from search, without a warrant, of his “home,” in this case a natural cave, and counsel further agree that the more immediate issue is whether Ruckman had a subjective expectation of privacy in the cave, and, if so, whether his expectation is one which society is prepared to recognize as being reasonable under the circumstances. <em>Katz v. United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U.S. 347, 361</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#516" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507, 516</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L.Ed.2d 576</a></span> (1967). <em>See also Rakas v. Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#151" aria-description="Citation for case: Rakas v. Illinois">439 U.S. 128, 151</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#434" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. 421, 434</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">58 L.Ed.2d 387</a></span> (1978).</p>
<p id="b1556-8">We shall assume that Ruckman entertained a subjective expectation of privacy, i.e., absent a search warrant or probable cause or exigent circumstances, none of which is contended for by the government, his cave could not be searched by any law enforcement officers without violating Fourth Amendment rights. However, the record, as we read it, contains no statement by Ruckman that he had any subjective expectation of privacy. Perhaps the filing of the motion to suppress presupposes such subjective expectation. In any event, we assume such subjective expectation. No doubt Ruckman would so testify. The real issue is whether such subjective expectation is reasonable under the circumstances of the case. Stated differently, the issue is whether the cave comes within the ambit of the Fourth Amendment’s prohibition of unreasonable searches of “houses.” Under the circumstances, we conclude that Ruck-man’s cave is not subject to the protection of the Fourth Amendment.</p>
<p id="b1556-9">Ruckman was admittedly a trespasser on federal lands and subject to immediate ejectment. With respect to its own lands, the government has the rights of an ordinary proprietor, i.e., to maintain its posses<page-number citation-index="1" label="1473">*1473</page-number>sion and to prosecute trespassers. <em>United States v. Osterlund, </em><span class="citation" data-id="1950798"><a href="/opinion/1950798/united-states-v-osterlund/#167" aria-description="Citation for case: United States v. Osterlund">505 F.Supp. 165, 167</a></span> (D.Colo.1981), <em>aff’d, </em><span class="citation" data-id="399952"><a href="/opinion/399952/united-states-v-jon-w-osterlund/" aria-description="Citation for case: United States v. Jon W. Osterlund">671 F.2d 1267</a></span> (10th Cir.1982). While he had been living off the land for several months, the cave could hardly be considered a permanent residence. Counsel himself describes Ruck-man as “just camping out there for an extended period of time.” Ruckman’s subjective expectation of privacy is not reasonable in light of the fact that he could be ousted by BLM authorities from the place he was occupying at any time. While it has been often stated, the Fourth Amendment protects people, and not places <em>(Katz, supra, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States">389 U.S. at 353</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#512" aria-description="Citation for case: Katz v. United States">88 S.Ct. at 512</a></span>), any determination of just what protection is to be given requires, in a given case, some reference to a place. And the place in this instance was on federal (BLM) land. The government’s authority over federal lands has been clearly stated by the Supreme Court. “[T]he power over the public land thus entrusted to Congress is without limitations.” <em>United States v. San Francisco, </em><span class="citation" data-id="103341"><a href="/opinion/103341/united-states-v-city-county-of-san-francisco/#29" aria-description="Citation for case: United States v. City &amp; County of San Francisco">310 U.S. 16, 29</a></span>, <span class="citation" data-id="103341"><a href="/opinion/103341/united-states-v-city-county-of-san-francisco/#756" aria-description="Citation for case: United States v. City &amp; County of San Francisco">60 S.Ct. 749, 756</a></span>, <span class="citation" data-id="103341"><a href="/opinion/103341/united-states-v-city-county-of-san-francisco/" aria-description="Citation for case: United States v. City &amp; County of San Francisco">84 L.Ed. 1050</a></span> (1940), <em>reh’g denied, </em><span class="citation multiple-matches"><a href="/c/U.S./310/657/">310 U.S. 657</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./60/1071/">60 S.Ct. 1071</a></span>, <span class="citation no-link">84 L.Ed. 1420</span> (1940). This power derives from the Constitution. “[A]rticle IV, § 3, cl. 2 of the Constitution provides that ‘the Congress shall have Power to dispose of and make all needful Rules and Regulations respecting the Territory and other Property belonging to the United States.’ ” <em>Id. </em>A necessary ancillary to this regulatory power over lands within the public domain is the power to control their occupancy and use, to protect them from trespass and injury and to prescribe the conditions upon which others may obtain rights....” <em>Utah Power &amp; Light Co. v. United States, </em><span class="citation" data-id="98904"><a href="/opinion/98904/utah-power-light-co-v-united-states/#405" aria-description="Citation for case: Utah Power &amp; Light Co. v. United States">243 U.S. 389, 405</a></span>, <span class="citation" data-id="98904"><a href="/opinion/98904/utah-power-light-co-v-united-states/#389" aria-description="Citation for case: Utah Power &amp; Light Co. v. United States">37 S.Ct. 387, 389</a></span>, <span class="citation" data-id="98904"><a href="/opinion/98904/utah-power-light-co-v-united-states/" aria-description="Citation for case: Utah Power &amp; Light Co. v. United States">61 L.Ed. 791</a></span> (1917). The Fourth Amendment itself proscribes, <em>inter alia, </em>an unreasonable search of “houses.” Without belaboring the matter, we decline to hold that the instant case comes within the ambit of the Fourth Amendment. The fact that Ruckman may have subjectively deemed the cave to be his “castle” is not decisive of the present problem. As a Ninth Circuit case involving invalid mining claims on public lands pointed out, “[A] person, under the guise of repeatedly locating invalid mining claims, may not use public lands primarily for residential purposes.” <em>United States v. Allen, </em><span class="citation" data-id="357143"><a href="/opinion/357143/united-states-v-lincoln-albert-allen-aka-bud-allen-helen-carter-allen/#237" aria-description="Citation for case: United States v. Lincoln Albert Allen, AKA Bud Allen,...">578 F.2d 236, 237-38</a></span> (9th Cir.1978).</p>
<p id="b1557-9">We do not regard the circumstances underlying the “public telephone booth” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States"><em>(Katz, </em>supra)</a></span> or “public restroom” <em>(People v. Triggs, </em><span class="citation" data-id="1362811"><a href="/opinion/1362811/sheriff-clark-cty-v-levinson/" aria-description="Citation for case: SHERIFF, CLARK CTY. v. Levinson">95 Nev. 436</a></span>, <span class="citation" data-id="1354211"><a href="/opinion/1354211/people-v-triggs/" aria-description="Citation for case: People v. Triggs">506 P.2d 232</a></span> (1973)) cases to be of particular relevance. The “open field” cases perhaps have more relevance. In explaining the distinction between “open fields” and the “certain enclaves” which should be free from arbitrary government interference, the Supreme Court has noted that, as a practical matter, “open fields” usually are accessible to the public and the police in ways that a home, an office or commercial structure would not be. <em>Oliver v. United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#179" aria-description="Citation for case: Oliver v. United States">466 U.S. 170, 179</a></span>, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#1741" aria-description="Citation for case: Oliver v. United States">104 S.Ct. 1735, 1741</a></span>, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">80 L.Ed.2d 214</a></span> (1984). This Court has found that a person has no legitimate expectation of privacy even in his own private property where that property is surrounded by barbed wire fences, even if there are “No Trespassing” signs posted. <em>United States v. Rucinski, </em><span class="citation" data-id="393926"><a href="/opinion/393926/united-states-v-bill-rucinski-and-alfred-medina/#743" aria-description="Citation for case: United States v. Bill Rucinski, and Alfred Medina">658 F.2d 741, 743-46</a></span> (10th Cir.1981), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./455/939/">455 U.S. 939</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./102/1430/">102 S.Ct. 1430</a></span>, <span class="citation" data-id="9030626"><a href="/opinion/9037308/gerard-v-louisiana/" aria-description="Citation for case: Gerard v. Louisiana">71 L.Ed.2d 649</a></span> (1982). Other cases with some degree of relevancy include <em>People v. Sumlin, </em><span class="citation" data-id="6200887"><a href="/opinion/6332327/people-v-sumlin/" aria-description="Citation for case: People v. Sumlin">105 Misc.2d 134</a></span>, <span class="citation" data-id="6200887"><a href="/opinion/6332327/people-v-sumlin/" aria-description="Citation for case: People v. Sumlin">431 N.Y.S.2d 967</a></span> (1980), in which the New York County Supreme Court held that a casual guest of the employee of a squatter in a city-owned abandoned building did not have any expectation of privacy and that defendant, as a trespasser who was wrongly on premises, could not claim Fourth Amendment violation of rights. <em>Id., </em>at 969-70. In <em>People v. Smith, </em><span class="citation" data-id="6202334"><a href="/opinion/6333767/people-v-smith/" aria-description="Citation for case: People v. Smith">113 Misc.2d 176</a></span>, <span class="citation" data-id="6202334"><a href="/opinion/6333767/people-v-smith/" aria-description="Citation for case: People v. Smith">448 N.Y.S.2d 404</a></span> (1982), the court held that even if defendant was a subtenant, he could not derive any rights from one who has none, i.e., a squatter. <em>Id., </em>406.</p>
<p id="b1557-10">A case having perhaps greater relevance than those above cited is <em>Amezquita v. Hernandez-Colon, </em><span class="citation" data-id="328469"><a href="/opinion/328469/pedro-amezquita-v-rafael-hernandez-colon/" aria-description="Citation for case: Pedro Amezquita v. Rafael Hernandez Colon">518 F.2d 8</a></span> (1st Cir.1975), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./424/916/">424 U.S. 916</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./96/1117/">96 S.Ct. 1117</a></span>, <span class="citation" data-id="8999448"><a href="/opinion/9006709/alexander-v-buckley/" aria-description="Citation for case: Alexander v. Buckley">47 L.Ed.2d 321</a></span> (1976). There “squat<page-number citation-index="1" label="1474">*1474</page-number>ters” moved onto land owned by the Commonwealth of Puerto Rico and built structures thereon. When the government threatened to oust them, the squatters brought a civil rights action seeking injunctive relief and damages. The district court ruled for the squatters. On appeal, the First Circuit reversed. In holding that the squatters had no reasonable or legitimate expectation of privacy, the First Circuit opined that, under the circumstances of that case, a claim that the squatters had a reasonable expectation of privacy was “ludicrous.” <span class="citation" data-id="328469"><a href="/opinion/328469/pedro-amezquita-v-rafael-hernandez-colon/#11" aria-description="Citation for case: Pedro Amezquita v. Rafael Hernandez Colon"><em>Amezquita, supra, </em>at 11</a></span>. (Legitimacy of a privacy claim is determined by the totality of the circumstances. <em>Ra-leas, supra, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#152" aria-description="Citation for case: Rakas v. Illinois">439 U.S. at 152</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#435" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. at 435</a></span>. The test of legitimacy is not whether the individual chooses to conceal assertedly “private” activity but whether the government’s intrusion infringes upon the personal and societal values protected by the Fourth Amendment. <em>Oliver, supra, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#182" aria-description="Citation for case: Oliver v. United States">466 U.S. at 182-83</a></span>, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#1743" aria-description="Citation for case: Oliver v. United States">104 S.Ct. at 1743</a></span>.) Further, considering what constitutes a “home” for Fourth Amendment purposes, the First Circuit commented as follows:</p>
<blockquote id="b1558-4">But whether a place constitutes a person’s “home” for this purpose cannot be decided without any attention to its location or the means by which it was acquired; that is, whether the occupancy and construction were in bad faith is highly relevant. Where the plaintiffs had no legal right to occupy the land and build structures on it, those <em>faits accom-plis </em>could give rise to no reasonable expectation of privacy even if the plaintiffs did own the resulting structures.</blockquote>
<p id="ARUD"><span class="citation" data-id="328469"><a href="/opinion/328469/pedro-amezquita-v-rafael-hernandez-colon/#12" aria-description="Citation for case: Pedro Amezquita v. Rafael Hernandez Colon"><em>Amezquita, supra, </em>at 12</a></span>.</p>
<p id="b1558-5">Judgment affirmed.</p>
</opinion>
```

---

## GROUP: content/cases/United States v. Ruiz.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Ruiz
type: case
citation: "536 U.S. 622 (2002)"
parallel_cite: "122 S. Ct. 2450; 153 L. Ed. 2d 586"
neutral_cite: 2002 U.S. LEXIS 4650
court: U.S.
court_level: scotus
circuit: ""
year: 2002
date_decided: 2002-06-24
docket: 01-595
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
  opinion_url: "https://www.courtlistener.com/opinion/121166/united-states-v-ruiz/"
  cluster_id: 121166
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Ruiz
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Brady and Giglio]]"
    role: Key
related:
  - "[[Brady and Giglio]]"
  - "[[Brady v. Maryland]]"
  - "[[Giglio v. United States]]"
tags:
  - case
  - fifth-amendment
  - sixth-amendment
  - due-process
  - brady
  - giglio
  - impeachment-evidence
  - guilty-plea
  - plea-bargaining
holding: "The Constitution does not require federal prosecutors to disclose material impeachment information — or information supporting an affirmative defense — to a defendant before the defendant enters a binding guilty plea, because such information bears on the fairness of a trial the defendant is giving up rather than on whether the guilty plea itself is knowing and voluntary."
aliases:
  - United States v. Ruiz
  - "United States v. Ruiz (2002)"
---

# United States v. Ruiz

*536 U.S. 622 (2002)* (No. 01-595) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 121166 → lead opinion 121166 (Breyer, J., for the Court; 536 U.S. 622, decided 2002-06-24); Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star-pagination *625). S9 promotes. -->

## Background
Immigration agents found approximately 30 kilograms of marijuana in Angela Ruiz's luggage. Federal prosecutors in the Southern District of California offered her a "fast track" plea bargain under which the Government would recommend a reduced sentence in exchange for her guilty plea. The proposed agreement stated that the Government had turned over any known information establishing the defendant's factual innocence and acknowledged a continuing duty to do so, but it required Ruiz to waive the right to receive impeachment information relating to informants or other witnesses, along with information supporting any [[Common Legal Terms#affirmative-defense|affirmative defense]]. Ruiz refused to waive those rights, the Government withdrew the offer, and she was indicted and ultimately pleaded guilty without an agreement. She nonetheless sought the sentence reduction; the district court declined, and the Ninth Circuit [[Reading and Citing Cases#vacated|vacated]] the sentence, reasoning that the Constitution entitles a defendant to impeachment information before pleading guilty.

## Issue
Whether the Fifth and Sixth Amendments require federal prosecutors, before entering into a binding plea agreement, to disclose material impeachment information relating to informants or other witnesses.

## Rule
A guilty plea is valid only if knowing, intelligent, and voluntary, but impeachment information bears on the fairness of a trial rather than on the voluntariness of a plea that gives the trial up. Because a defendant who pleads guilty forgoes the trial at which such impeachment would matter, the Court held that the Constitution imposes no duty to disclose it beforehand: "We hold that the Constitution does not require that disclosure." — 536 U.S. at 625. ^pin-625

## Application
The Court reasoned that the value of impeachment evidence to a defendant deciding whether to plead is both limited and highly contingent — it depends on the defendant's own knowledge of the Government's case and on the random chance that a particular impeachment happens to help — while a pre-plea disclosure obligation would burden the plea-bargaining system, risking premature exposure of witnesses and disruption of ongoing investigations. It emphasized that a defendant may waive even the right to trial itself without knowing every detail a trial would reveal, and that the proposed agreement already preserved the Government's duty to disclose information establishing factual innocence and to honor the other guilty-plea safeguards of Rule 11. Weighing the modest incremental value against those systemic costs, the Court concluded that due process does not demand pre-plea disclosure of impeachment or affirmative-defense information.

## Conclusion
The judgment of the Court of Appeals for the Ninth Circuit was **reversed**. Breyer, J., delivered the opinion of the Court; Thomas, J., filed an opinion concurring in the judgment.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Ruiz* is the controlling limit on the *[[Brady and Giglio|Brady]]/[[Giglio v. United States|Giglio]]* disclosure duty at the plea stage: the right to impeachment and affirmative-defense information is a trial right, so it does not attach before a guilty plea. It leaves open — and lower courts continue to divide over — whether the distinct duty to disclose material **[[Brady and Giglio|exculpatory]]** (as opposed to impeachment) information applies before a plea. Teach it as the boundary between the trial-fairness rationale of *Brady/Giglio* and the knowing-and-voluntary standard that governs guilty pleas.

## Appears on
- [[Brady and Giglio]] — *Key*

## Sources
- [*United States v. Ruiz*, 536 U.S. 622 (2002)](https://www.courtlistener.com/opinion/121166/united-states-v-ruiz/) — pinpoint: 625 (opinion of the Court, holding that pre-plea disclosure of impeachment information is not constitutionally required; Breyer, J.); the CL opinion text star-paginates the U.S. Reports. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0f7228f909c8d45e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "536 U.S. 622 (2002)", "court": "U.S.", "neutral_cite": "2002 U.S. LEXIS 4650", "official_citation_present": true, "parallel_cite": "122 S. Ct. 2450; 153 L. Ed. 2d 586", "title": "United States v. Ruiz", "year": "2002"}}
{"assertion_id": "0c62280e07c0531a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Constitution does not require federal prosecutors to disclose material impeachment information — or information supporting an affirmative defense — to a defendant before the defendant enters a binding guilty plea, because such information bears on the fairness of a trial the defendant is giving up rather than on whether the guilty plea itself is knowing and voluntary.", "title": "United States v. Ruiz"}}
{"assertion_id": "0db4d663ca76aaf3", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Key", "title": "United States v. Ruiz"}}
{"assertion_id": "3c7d88c995f0680d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Ruiz", "varies_by_point": "false"}}
{"assertion_id": "9ba483952057d13f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Ruiz"}}
```

### lake record — United States v. Ruiz

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Ruiz",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Ruiz",
    "case_name_short": "Ruiz",
    "case_name_full": "United States v. Ruiz",
    "input_case_name": "United States v. Ruiz",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2002-06-24",
    "year": 2002,
    "docket": "01-595",
    "cluster_id": 121166,
    "lead_opinion_id": 9434310,
    "sibling_ids": [],
    "absolute_url": "/opinion/121166/united-states-v-ruiz/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "536 U.S. 622",
      "volume": "536",
      "reporter": "U.S.",
      "page": "622",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "122 S. Ct. 2450",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "2450",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "153 L. Ed. 2d 586",
        "volume": "153",
        "reporter": "L. Ed. 2d",
        "page": "586",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2002 U.S. LEXIS 4650",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "4650",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "536 U.S. 622",
        "volume": "536",
        "reporter": "U.S.",
        "page": "622",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "122 S. Ct. 2450",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "2450",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "153 L. Ed. 2d 586",
        "volume": "153",
        "reporter": "L. Ed. 2d",
        "page": "586",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 U.S. LEXIS 4650",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "4650",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "536 U.S. 622",
    "official_selection": {
      "court_class": "scotus",
      "selected": "536 U.S. 622",
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
    "date_created": "2026-07-07T18:19:36Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:19:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:19:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:19:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:19:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-ruiz--121166",
      "to_record_id": "United States v. Ruiz",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Ruiz

```
<opinion type="majority">
<author id="b675-4"><page-number citation-index="1" label="625">*625</page-number>Justice Breyer</author>
<p id="A0R">delivered the opinion of the Court.</p>
<p id="b675-5">In this case we primarily consider whether the Fifth and Sixth Amendments require federal prosecutors, before entering into a binding plea agreement with a criminal defendant, to disclose “impeachment information relating to any informants or other witnesses.” App. to Pet. for Cert. 46a. We hold that the Constitution does not require that disclosure.</p>
<p id="b675-6">I</p>
<p id="b675-7">After immigration agents found 30 kilograms of marijuana in Angela Ruiz’s luggage, federal prosecutors offered her what is known in the Southern District of California as a “fast track” plea bargain. That bargain — standard in that district — asks a defendant to waive indictment, trial, and an appeal. In return, the Government agrees to recommend to the sentencing judge a two-level departure downward from the otherwise applicable United States Sentencing Guidelines sentence. In Ruiz’s case, a two-level departure downward would have shortened the ordinary Guidelines-specified 18-to-24-month sentencing range by 6 months, to 12-to-18 months. <span class="citation" data-id="9493832"><a href="/opinion/772301/united-states-v-angela-ruiz/#1161" aria-description="Citation for case: United States v. Angela Ruiz">241 F. 3d 1157, 1161</a></span> (2001).</p>
<p id="b675-8">The prosecutors’ proposed plea agreement contains a set of detailed terms. Among other things, it specifies that “any [known] information establishing the factual innocence of the defendant” “has been, turned over to the defendant,” and it acknowledges the Government’s “continuing duty to provide such information.” App. to Pet. for Cert. 45a-46a. At the same time it requires that the defendant “waiv[e] the right” to receive “impeachment information relating to any informants or other witnesses” as well as the right to receive information supporting any affirmative defense the defendant raises if the case goes to trial. <em><span class="citation" data-id="9493832"><a href="/opinion/772301/united-states-v-angela-ruiz/" aria-description="Citation for case: United States v. Angela Ruiz">Id.,</a></span> </em>at 46a. Because Ruiz would not agree to this last-mentioned waiver, the prosecutors withdrew their bargaining offer. The Government then indicted Ruiz for unlawful drug possession. And despite <page-number citation-index="1" label="626">*626</page-number>the absence of any agreement, Ruiz ultimately pleaded guilty.</p>
<p id="b676-5">At sentencing, Ruiz asked the judge to grant her the same two-level downward departure that the Government would have recommended had she accepted the “fast track” agreement. The Government opposed her request, and the District Court denied it, imposing a standard Guideline sentence instead. <span class="citation" data-id="9493832"><a href="/opinion/772301/united-states-v-angela-ruiz/#1161" aria-description="Citation for case: United States v. Angela Ruiz">241 F. 3d, at 1161</a></span>.</p>
<p id="b676-6">Relying on <span class="citation no-link">18 U. S. C. § 3742</span>, see <em>infra, </em>at 627, 628-629, Ruiz appealed her sentence to the United States Court of Appeals for the Ninth Circuit. The Ninth Circuit vacated the District Court’s sentencing determination. The Ninth Circuit pointed out that the Constitution requires prosecutors to make certain impeachment information available to a defendant before trial. <span class="citation" data-id="9493832"><a href="/opinion/772301/united-states-v-angela-ruiz/#1166" aria-description="Citation for case: United States v. Angela Ruiz">241 F. 3d, at 1166</a></span>. It decided that this obligation entitles defendants to receive that same information before they enter into a plea agreement. <span class="citation" data-id="9493832"><a href="/opinion/772301/united-states-v-angela-ruiz/#1164" aria-description="Citation for case: United States v. Angela Ruiz"><em>Id., </em>at 1164</a></span>. The Ninth Circuit also decided that the Constitution prohibits defendants from waiving their right to that information. <span class="citation" data-id="9493832"><a href="/opinion/772301/united-states-v-angela-ruiz/#1165" aria-description="Citation for case: United States v. Angela Ruiz"><em>Id., </em>at 1165-1166</a></span>. And it held that the prosecutors’ standard “fast track” plea agreement was unlawful because it insisted upon that waiver. <span class="citation" data-id="9493832"><a href="/opinion/772301/united-states-v-angela-ruiz/#1167" aria-description="Citation for case: United States v. Angela Ruiz"><em>Id., </em>at 1167</a></span>. The Ninth Circuit remanded the case so that the District Court could decide any related factual disputes and determine an appropriate remedy. <span class="citation" data-id="9493832"><a href="/opinion/772301/united-states-v-angela-ruiz/#1169" aria-description="Citation for case: United States v. Angela Ruiz"><em>Id., </em>at 1169</a></span>.</p>
<p id="b676-7">The Government sought certiorari. It stressed what it considered serious adverse practical implications of the Ninth Circuit’s constitutional holding. And it added that the holding is unique among courts of appeals. Pet. for Cert. 8. We granted the Government’s petition. <span class="citation multiple-matches"><a href="/c/U.%20S./534/1074/">534 U. S. 1074</a></span> (2002).</p>
<p id="b676-8">II</p>
<p id="b676-9">At the outset, we note that a question of statutory jurisdiction potentially blocks our consideration of the Ninth Circuit’s constitutional holding. The relevant statute says that a</p>
<blockquote id="b677-4"><page-number citation-index="1" label="627">*627</page-number>“defendant may file a notice of appeal... for review ... if the sentence</blockquote>
<blockquote id="b677-5">“(1) was imposed in violation of law;</blockquote>
<blockquote id="b677-6">“(2) was imposed as a result of an incorrect application of the sentencing guidelines; or</blockquote>
<blockquote id="b677-7">“(3) is greater than [the Guideline] specified [sentence] .. .; or</blockquote>
<blockquote id="b677-8">“(4) was imposed for an offense for which there is no sentencing guideline and is plainly unreasonable.” <span class="citation no-link">18 U. S. C. § 3742</span>(a).</blockquote>
<p id="b677-9">Every Circuit has held that this statute does <em>not </em>authorize a defendant to appeal a sentence where the ground for appeal consists of a claim that the district court abused its discretion in refusing to depart. See, <em>e. g., United States </em>v. <em>Conway, </em><span class="citation" data-id="9439917"><a href="/opinion/196702/united-states-v-conway/#16" aria-description="Citation for case: United States v. Conway">81 F. 3d 15, 16</a></span> (CA1 1996); <em>United States </em>v. <em>Lawal, </em><span class="citation" data-id="664052"><a href="/opinion/664052/united-states-v-genevieve-lawal-francis-wiredu-augustina-erskine-hannah/#562" aria-description="Citation for case: United States v. Genevieve Lawal, Francis Wiredu,...">17 F. 3d 560, 562</a></span> (CA2 1994); <em>United States </em>v. <em>Powell, </em><span class="citation" data-id="775322"><a href="/opinion/775322/united-states-v-allen-powell-aka-keith-bates/#179" aria-description="Citation for case: United States v. Allen Powell, A/K/A Keith Bates">269 F. 3d 175, 179</a></span> (CA3 2001); <em>United States </em>v. <em>Ivester, </em><span class="citation" data-id="9488872"><a href="/opinion/712094/united-states-v-sidney-wayne-ivester/#183" aria-description="Citation for case: United States v. Sidney Wayne Ivester">75 F. 3d 182, 183</a></span> (CA4 1996); <em>United States </em>v. <em>Cooper, </em><span class="citation" data-id="25905"><a href="/opinion/25905/united-states-v-cooper/#248" aria-description="Citation for case: United States v. Cooper">274 F. 3d 230, 248</a></span> (CA5 2001); <em>United States </em>v. <em>Scott, </em><span class="citation" data-id="711073"><a href="/opinion/711073/united-states-v-thomas-c-scott/#112" aria-description="Citation for case: United States v. Thomas C. Scott">74 F. 3d 107, 112</a></span> (CA6 1996); <em>United States </em>v. <em>Byrd, </em><span class="citation" data-id="774740"><a href="/opinion/774740/united-states-v-cornell-r-byrd/#707" aria-description="Citation for case: United States v. Cornell R. Byrd">263 F. 3d 705, 707</a></span> (CA7 2001); <em>United States </em>v. <em>Mora-Higuera, </em><span class="citation multiple-matches"><a href="/c/F.%203d/269/905/">269 F. 3d 905</a></span>, 913 (CA8 2001); <em>United States </em>v. <em>Garcia-Garcia, </em><span class="citation" data-id="556736"><a href="/opinion/556736/united-states-v-jose-fernando-garcia-garcia/#490" aria-description="Citation for case: United States v. Jose Fernando Garcia-Garcia">927 F. 2d 489, 490</a></span> (CA9 1991); <em>United States </em>v. <em>Coddington, </em><span class="citation" data-id="155034"><a href="/opinion/155034/united-states-v-coddington/#1441" aria-description="Citation for case: United States v. Coddington">118 F. 3d 1439, 1441</a></span> (CA10 1997); <em>United States </em>v. <em>Calderon, </em><span class="citation" data-id="747578"><a href="/opinion/747578/united-states-v-alberto-calderon/#1342" aria-description="Citation for case: United States v. Alberto Calderon">127 F. 3d 1314, 1342</a></span> (CA11 1997); <em>In re Sealed Case No. 98-3116, </em><span class="citation" data-id="9439185"><a href="/opinion/185016/in-re-sealed-case-no-98-3116/#491" aria-description="Citation for case: In Re Sealed Case No. 98-3116">199 F. 3d 488, 491-492</a></span> (CADC 1999).</p>
<p id="b677-10">The statute does, however, authorize an appeal from a sentence that “was imposed in violation of law.” Two quite different theories might support appellate jurisdiction pursuant to that provision. First, as the Court of Appeals recognized, if the District Court’s sentencing decision rested on a mistaken belief that it lacked the legal power to grant a departure, the quoted provision would apply. <span class="citation" data-id="9493832"><a href="/opinion/772301/united-states-v-angela-ruiz/#1162" aria-description="Citation for case: United States v. Angela Ruiz">241 F. 3d, at 1162, n. 2</a></span>. Our reading of the record, however, convinces us that the District Judge correctly understood that he had such discretion but decided not to exercise it. We therefore reject <page-number citation-index="1" label="628">*628</page-number>that basis for finding appellate jurisdiction. Second, if respondent’s constitutional claim, discussed in Part III, <em>infra, </em>were sound, her sentence would have been “imposed in violation of law.” Thus, if she had prevailed on the merits, her victory would also have confirmed the jurisdiction of the Court of Appeals.</p>
<p id="AcE">Although we ultimately conclude that respondent’s sentence was not “imposed in violation of law” and therefore that § 3742(a)(1) does not authorize an appeal in a case of this kind, it is familiar law that a federal court always has jurisdiction to determine its own jurisdiction. See <em>United States </em>v. <em>Mine Workers, </em><span class="citation" data-id="9419944"><a href="/opinion/104385/united-states-v-united-mine-workers-of-america/#291" aria-description="Citation for case: United States v. United Mine Workers of America">330 U. S. 258, 291</a></span> (1947). In order to make that determination, it was necessary for the Ninth Circuit to address the merits. We therefore hold that appellate jurisdiction was proper.</p>
<p id="Afk">III</p>
<p id="Aoi">The constitutional question concerns a federal criminal defendant’s waiver of the right to receive from prosecutors exculpatory impeachment material — a right that the Constitution provides as part of its basic “fair trial” guarantee. See U. S. Const., Arndts. 5, 6. See also <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83, 87</a></span> (1963) (Due process requires prosecutors to “avoi[d] ... an unfair trial” by making available “upon request” evidence “favorable to an accused . . . where the evidence is material either to guilt or to punishment”); <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#112" aria-description="Citation for case: United States v. Agurs">427 U. S. 97, 112-113</a></span> (1976) (defense request unnecessary); <em>Kyles </em>v. <em>Whitley, </em><span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#435" aria-description="Citation for case: Kyles v. Whitley">514 U. S. 419, 435</a></span> (1995) (exculpatory evidence is evidence the suppression of which would “undermine confidence in the verdict”); <em>Giglio </em>v. <em>United States, </em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 154</a></span> (1972) (exculpatory evidence includes “evidence affecting” witness “credibility,” where the witness’ “reliability” is likely “determinative of guilt or innocence”).</p>
<p id="A5m">When a defendant pleads guilty he or she, of course, forgoes not only a fair trial, but also other accompanying consti<page-number citation-index="1" label="629">*629</page-number>tutional guarantees. <em>Boykin </em>v. <em>Alabama, </em><span class="citation" data-id="9424054"><a href="/opinion/107951/boykin-v-alabama/#243" aria-description="Citation for case: Boykin v. Alabama">395 U. S. 238, 243</a></span> (1969) (pleading guilty implicates the Fifth Amendment privilege against self-incrimination, the Sixth Amendment right to confront one’s accusers, and the Sixth Amendment right to trial by jury). Given the seriousness of the matter, the Constitution insists, among other things, that the defendant enter a guilty plea that is “voluntary” and that the defendant must make related waivers “knowing[ly], intelligently], [and] with sufficient awareness of the relevant circumstances and likely consequences.” <em>Brady </em>v. <em>United States, </em><span class="citation" data-id="108137"><a href="/opinion/108137/brady-v-united-states/#748" aria-description="Citation for case: Brady v. United States">397 U. S. 742, 748</a></span> (1970); see also <span class="citation" data-id="9424054"><a href="/opinion/107951/boykin-v-alabama/#242" aria-description="Citation for case: Boykin v. Alabama"><em>Boykin, supra, </em>at 242</a></span>.</p>
<p id="b679-5">In this case, the Ninth Circuit in effect held that a guilty plea is not “voluntary” (and that the defendant could not, by pleading guilty, waive her right to a fair trial) unless the prosecutors first made the same disclosure of material impeachment information that the prosecutors would have had to make had the defendant insisted upon a trial. We must decide whether the Constitution requires that preguilty plea disclosure of impeachment information. We conclude that it does not.</p>
<p id="b679-6">First, impeachment information is special in relation to the <em>fairness of a trial, </em>not in respect to whether a plea is <em>voluntary </em>(“knowing,” “intelligent,” and “sufficient[ly] aware”). Of course, the more information the defendant has, the more aware he is of the likely consequences of a plea, waiver, or decision, and the wiser that decision will likely be. But the Constitution does not require the prosecutor to share all useful information with the defendant. <em>Weatherford </em>v. <em>Bursey, </em><span class="citation" data-id="9426656"><a href="/opinion/109590/weatherford-v-bursey/#559" aria-description="Citation for case: Weatherford v. Bursey">429 U. S. 545, 559</a></span> (1977) (“There is no general constitutional right to discovery in a criminal case”). And the law ordinarily considers a waiver knowing, intelligent, and sufficiently aware if the defendant fully understands the nature of the right and how it would likely apply <em>in general </em>in the circumstances — even though the defendant may not know the <em>specific detailed </em>consequences of invoking it. A defendant, for example, may waive his right to remain silent, his <page-number citation-index="1" label="630">*630</page-number>right to a jury trial, or his right to counsel even if the defendant does not know the specific questions the authorities intend to ask, who will likely serve on the jury, or the particular lawyer the State might otherwise provide. Cf. <em>Colorado </em>v. <em>Spring, </em><span class="citation" data-id="9430793"><a href="/opinion/111798/colorado-v-spring/#573" aria-description="Citation for case: Colorado v. Spring">479 U. S. 564, 573-575</a></span> (1987) (Fifth Amendment privilege against self-incrimination waived when defendant received standard <em>Miranda </em>warnings regarding the nature of the right but not told the specific interrogation questions to be asked).</p>
<p id="b680-5">It is particularly difficult to characterize impeachment information as critical information of which the defendant must always be aware prior to pleading guilty given the random way in which such information may, or may not, help a particular defendant. The degree of help that impeachment information can provide will depend upon the defendant’s own independent knowledge of the prosecution’s potential case — a matter that the Constitution does not require prosecutors to disclose.</p>
<p id="b680-6">Second, we have found no legal authority embodied either in this Court’s past cases or in cases from other circuits that provides significant support for the Ninth Circuit’s decision. To the contrary, this Court has found that the Constitution, in respect to a defendant’s awareness of relevant circumstances, does not require complete knowledge of the relevant circumstances, but permits a court to accept a guilty plea, with its accompanying waiver of various constitutional rights, despite various forms of misapprehension under which a defendant might labor. See <em>Brady </em>v. <em>United States, </em><span class="citation" data-id="108137"><a href="/opinion/108137/brady-v-united-states/#757" aria-description="Citation for case: Brady v. United States">397 U. S., at 757</a></span> (defendant “misapprehended the quality of the State’s case”); <em>ibid, </em>(defendant misapprehended “the likely penalties”); <em>ibid, </em>(defendant failed to “anticipate” a change in the law regarding relevant “punishments”); <em>McMann </em>v. <em>Richardson, </em><span class="citation" data-id="9424256"><a href="/opinion/108138/mcmann-v-richardson/#770" aria-description="Citation for case: McMann v. Richardson">397 U. S. 759, 770</a></span> (1970) (counsel “misjudged the admissibility” of a “confession”); <em>United States </em>v. <em>Broce, </em><span class="citation" data-id="9431528"><a href="/opinion/112177/united-states-v-broce/#573" aria-description="Citation for case: United States v. Broce">488 U. S. 563, 573</a></span> (1989) (counsel failed to point out a potential defense); <em>Tollett </em>v. <em>Henderson, </em><span class="citation" data-id="9425244"><a href="/opinion/108762/tollett-v-henderson/#267" aria-description="Citation for case: Tollett v. Henderson">411 U. S. 258, 267</a></span> <page-number citation-index="1" label="631">*631</page-number>(1973) (counsel failed to find a potential constitutional infirmity in grand jury proceedings). It is difficult to distinguish, in terms of importance, (1) a defendant’s ignorance of grounds for impeachment of potential witnesses at a possible future trial from (2) the varying forms of ignorance at issue in these cases.</p>
<p id="b681-5">Third, due process considerations, the very considerations that led this Court to find trial-related rights to exculpatory and impeachment information in <em>Brady </em>and Giglio, argue against the existence of the “right” that the Ninth Circuit found here. This Court has said that due process considerations include not only (1) the nature of the private interest at stake, but also (2) the value of the additional safeguard, and (8) the adverse impact of the requirement upon the Government’s interests. <em>Ake </em>v. <em>Oklahoma, </em><span class="citation" data-id="9429915"><a href="/opinion/111356/ake-v-oklahoma/#77" aria-description="Citation for case: Ake v. Oklahoma">470 U. S. 68, 77</a></span> (1985). Here, as we have just pointed out, the added value of the Ninth Circuit’s “right” to a defendant is often limited, for it depends upon the defendant’s independent awareness of the details of the Government’s case. And in any case, as the proposed plea agreement at issue here specifies, the Government will provide “any information establishing the factual innocence of the defendant” regardless. That fact, along with other guilty-plea safeguards, see Fed. Rule Crim. Proc. 11, diminishes the force of Ruiz’s concern that, in the absence of impeachment information, innocent individuals, accused of crimes, will plead guilty. Cf. <em>McCarthy </em>v. <em>United States, </em><span class="citation" data-id="9423979"><a href="/opinion/107892/mccarthy-v-united-states/#465" aria-description="Citation for case: McCarthy v. United States">394 U. S. 459, 465-467</a></span> (1969) (discussing Rule ll’s role in protecting a defendant’s constitutional rights).</p>
<p id="b681-6">At the same time, a constitutional obligation to provide impeachment information during plea bargaining, prior to entry of a guilty plea, could seriously interfere with the Government’s interest in securing those guilty pleas that are factually justified, desired by defendants, and help to secure the efficient administration of justice. The Ninth Circuit’s rule risks premature disclosure of Government witness information, which, the Government tells us, could “disrupt ongoing <page-number citation-index="1" label="632">*632</page-number>investigations” and expose prospective witnesses to serious harm. Brief for United States 25. Cf. Amendments to Federal Rules of Criminal Procedure: Hearings before the Subcommittee on Criminal Justice of the House Committee on the Judiciary, 94th Cong., 1st Sess., 92 (1975) (statement of John C. Keeney, Acting Assistant Attorney General, Criminal Div., Dept, of Justice) (opposing mandated witness disclosure three days before trial because of documented instances of witness intimidation). And the careful tailoring that characterizes most legal Government witness disclosure requirements suggests recognition by both Congress and the Federal Rules Committees that such concerns are valid. See, <em>e. g., </em><span class="citation no-link">18 U. S. C. § 3432</span> (witness list disclosure required in capital cases three days before trial with exceptions); § 3500 (Government witness statements ordinarily subject to discovery only after testimony given); Fed. Rule Crim. Proe. 16(a)(2) (embodies limitations of <span class="citation no-link">18 U. S. C. §3500</span>). Compare 156 F. R. D. 460, 461-462 (1994) (congressional proposal to significantly broaden §3500) with 167 F. R. D. 221, 223, n. (judicial conference opposing congressional proposal).</p>
<p id="b682-5">Consequently, the Ninth Circuit’s requirement could force the Government to abandon its “general practice” of not “disclosing] to a defendant pleading guilty information that would reveal the identities of cooperating informants, undercover investigators, or other prospective witnesses.” Brief for United States 25. It could require the Government to devote substantially more resources to trial preparation prior to plea bargaining, thereby depriving the plea-bargaining process of its main resource-saving advantages. Or it could lead the Government instead to abandon its heavy reliance upon plea bargaining in a vast number — 90% or more — of federal criminal cases. We cannot say that the Constitution’s due process requirement demands so radical a change in the criminal justice process in order to achieve so comparatively small a constitutional benefit.</p>
<p id="b683-4"><page-number citation-index="1" label="633">*633</page-number>These considerations, taken together, lead us to conclude that the Constitution does not require the Government to disclose material impeachment evidence prior to entering a plea agreement with a criminal defendant.</p>
<p id="b683-5">In addition, we note that the “fast track” plea agreement requires a defendant to waive her right to receive information the Government has regarding any “affirmative defense” she raises at trial. App. to Pet. for Cert. 46a. We do not believe the Constitution here requires provision of this information to the defendant prior to plea bargaining — for most (though not all) of the reasons previously stated. That is to say, in the context of this agreement, the need for this information is more closely related to the <em>fairness </em>of a trial than to the <em>voluntariness </em>of the plea; the value in terms of the defendant’s added awareness of relevant circumstances is ordinarily limited; yet the added burden imposed upon the Government by requiring its provision well in advance of trial (often before trial preparation begins) can be serious, thereby significantly interfering with the administration of the plea-bargaining process.</p>
<p id="b683-6">For these reasons the judgment of the Court of Appeals for the Ninth Circuit is</p>
<p id="b683-7">
<em>Reversed.</em>
</p>
</opinion>
```

---
