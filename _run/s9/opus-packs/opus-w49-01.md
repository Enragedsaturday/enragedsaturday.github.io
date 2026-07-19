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

## GROUP: content/cases/Plumhoff v. Rickard.md  (`case`, 5 assertions)

### content_page

```
---
title: "Plumhoff v. Rickard"
type: case
citation: ""
parallel_cite: "134 S. Ct. 2012; 188 L. Ed. 2d 1056; 82 U.S.L.W. 4394; 572 U.S. 765; 24 Fla. L. Weekly Fed. S 790"
neutral_cite: "2014 U.S. LEXIS 3816; 2014 WL 2178335"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2014
date_decided: 2014-05-27
docket: 12-1117
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2014-05-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Plumhoff v. Rickard
  varies_by_point: false
  scope_note: "Good law: deadly force to end a dangerous high-speed chase is reasonable; officers also had QI. Reasonableness is judged on the totality (consistent with Barnes v. Felix (2025))."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2675750/plumhoff-v-rickard/"
  cluster_id: 2675750
  opinion_id: 2675750
  identity_checked: true
homes:
  - page: "[[Use of Force]]"
    role: "Key — Progeny / Refinement"
related: ["[[Scott v. Harris]]", "[[Graham v. Connor]]", "[[Mullenix v. Luna]]"]
aliases: []
tags: ["case", "use-of-force", "deadly-force", "high-speed-chase", "qualified-immunity", "section-1983"]
holding: "Using deadly force to end a dangerous high-speed chase is reasonable under the Fourth Amendment, and officers need not stop shooting until the threat ends; even if it were unreasonable, the officers would be entitled to qualified immunity."
lake:
  record_id: Plumhoff v. Rickard
  status: verified
  projected_at: 2026-07-09
---

# Plumhoff v. Rickard

*572 U.S. 765 (2014)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A West Memphis officer stopped Donald Rickard's car for a broken headlight. When asked to step out, Rickard sped off and led police on a chase exceeding 100 mph for over five minutes, passing more than two dozen cars. After colliding with cruisers and spinning into a parking lot, Rickard kept maneuvering to escape — bumper flush against a police car, accelerator down, wheels spinning. Officers fired 15 shots, killing Rickard and his passenger, Kelly Allen. Rickard's daughter sued the officers under § 1983 for excessive force.

## Issue
Whether the officers' use of deadly force to end the chase (and the firing of 15 shots) violated the Fourth Amendment, and if so whether the officers were entitled to [[Qualified Immunity|qualified immunity]].

## Rule
The deadly force was reasonable. "it is beyond serious dispute that Rickard's flight posed a grave public safety risk, and here, as in *Scott*, the police acted reasonably in using deadly force to end that risk." — 572 U.S. at 777. ^pin-777

And the number of shots was not excessive: "if police officers are justified in firing at a suspect in order to end a severe threat to public safety, the officers need not stop shooting until the threat has ended." — [*Id.*](https://www.courtlistener.com/opinion/2675750/plumhoff-v-rickard/#:~:text=if%20police%20officers%20are%20justified) ^pin-777b

Alternatively, the officers had [[Qualified Immunity|qualified immunity]]: "We have held that petitioners' conduct did not violate the Fourth Amendment, but even if that were not the case, petitioners would still be entitled to summary judgment based on qualified immunity." — *Id.* at 778. ^pin-778

## Application
Judged from the perspective of a reasonable officer at the moment force was used, Rickard's continued effort to flee — engine revving, wheels spinning against a cruiser — showed he was intent on resuming a chase that had already endangered many motorists, so deadly force to stop him was reasonable as in [[Scott v. Harris]]. Because Rickard never gave up during the roughly ten-second span of fire and in fact drove off afterward, the 15 shots did not make the force excessive. The passenger Kelly Allen's presence did not enhance Rickard's own Fourth Amendment rights. And even assuming a violation, no clearly established law (per *[[Brosseau v. Haugen]]*) precluded the officers' conduct, so [[Qualified Immunity|qualified immunity]] applied.

## Conclusion
Reversed. The use of deadly force to end the chase was reasonable and the 15 shots were not excessive; in any event the officers were entitled to [[Qualified Immunity|qualified immunity]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Plumhoff* applies the dangerous-flight deadly-force rule of [[Scott v. Harris]] and the [[Graham v. Connor]] reasonableness standard, and pairs with the high-specificity qualified-immunity cases like [[Mullenix v. Luna]]. Its totality-based reasonableness analysis is consistent with the later clarification in [[Barnes v. Felix]] (2025) that there is no "moment of the threat" rule cutting off the surrounding circumstances. No negative treatment.

## Appears on
- [[Use of Force]] — *Key — Progeny / Refinement*
- [[Section 1983 Liability and Qualified Immunity]] — *Related (cross-doctrine)*

## Sources
- *Plumhoff v. Rickard*, 572 U.S. 765 (2014) — https://www.courtlistener.com/opinion/2675750/plumhoff-v-rickard/ — pinpoints: 777, 778.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a2b10f8e41042c06", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2014 U.S. LEXIS 3816; 2014 WL 2178335", "official_citation_present": false, "parallel_cite": "134 S. Ct. 2012; 188 L. Ed. 2d 1056; 82 U.S.L.W. 4394; 572 U.S. 765; 24 Fla. L. Weekly Fed. S 790", "title": "Plumhoff v. Rickard", "year": "2014"}}
{"assertion_id": "1e46cd7e468d54d1", "dimension": "support", "kind": "home_role", "locator": {"home": "Use of Force"}, "payload": {"home": "Use of Force", "role": "Key — Progeny / Refinement", "title": "Plumhoff v. Rickard"}}
{"assertion_id": "b0f8b74982726a81", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Using deadly force to end a dangerous high-speed chase is reasonable under the Fourth Amendment, and officers need not stop shooting until the threat ends; even if it were unreasonable, the officers would be entitled to qualified immunity.", "title": "Plumhoff v. Rickard"}}
{"assertion_id": "0706fd7b13c86aa3", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Plumhoff v. Rickard"}}
{"assertion_id": "451c94049c94f64c", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2014-05-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Plumhoff v. Rickard", "field_i_validity": "good_law", "scope_note": "Good law: deadly force to end a dangerous high-speed chase is reasonable; officers also had QI. Reasonableness is judged on the totality (consistent with Barnes v. Felix (2025)).", "title": "Plumhoff v. Rickard", "varies_by_point": "false"}}
```

### lake record — Plumhoff v. Rickard

```json
{
  "schema_version": "s2.v1",
  "record_id": "Plumhoff v. Rickard",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Plumhoff v. Rickard",
    "case_name_short": "Plumhoff",
    "case_name_full": "Officer Vance PLUMHOFF, Et Al., Petitioners v. Whitne RICKARD, a Minor Child, Individually, and as Surviving Daughter of Donald Rickard, Deceased, by and Through Her Mother Samantha Rickard, as Parent and Next Friend.",
    "input_case_name": "Plumhoff v. Rickard",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2014-05-27",
    "year": 2014,
    "docket": "12-1117",
    "cluster_id": 2675750,
    "lead_opinion_id": 2675750,
    "sibling_ids": [
      2675750
    ],
    "absolute_url": "/opinion/2675750/plumhoff-v-rickard/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8415040,
        "score": 20,
        "case_name": "Plumhoff v. Rickard"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "134 S. Ct. 2012",
        "volume": "134",
        "reporter": "S. Ct.",
        "page": "2012",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "188 L. Ed. 2d 1056",
        "volume": "188",
        "reporter": "L. Ed. 2d",
        "page": "1056",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 U.S.L.W. 4394",
        "volume": "82",
        "reporter": "U.S.L.W.",
        "page": "4394",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "572 U.S. 765",
        "volume": "572",
        "reporter": "U.S.",
        "page": "765",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 790",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "790",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2014 U.S. LEXIS 3816",
        "volume": "2014",
        "reporter": "U.S. LEXIS",
        "page": "3816",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 2178335",
        "volume": "2014",
        "reporter": "WL",
        "page": "2178335",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "134 S. Ct. 2012",
        "volume": "134",
        "reporter": "S. Ct.",
        "page": "2012",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "188 L. Ed. 2d 1056",
        "volume": "188",
        "reporter": "L. Ed. 2d",
        "page": "1056",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 U.S. LEXIS 3816",
        "volume": "2014",
        "reporter": "U.S. LEXIS",
        "page": "3816",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 U.S.L.W. 4394",
        "volume": "82",
        "reporter": "U.S.L.W.",
        "page": "4394",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "572 U.S. 765",
        "volume": "572",
        "reporter": "U.S.",
        "page": "765",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 790",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "790",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 2178335",
        "volume": "2014",
        "reporter": "WL",
        "page": "2178335",
        "type": 7,
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
      "id": "pin-777",
      "page": null,
      "quote": "--- # Plumhoff v. Rickard *572 U.S. 765 (2014)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A West Memphis officer stopped Donald Rickard's car for a broken headlight. When asked to step out, Rickard sped off and led police on a chase exceeding 100 mph for over five minutes, passing more than two dozen cars. After colliding with cruisers and spinning into a parking lot, Rickard kept maneuvering to escape \u2014 bumper flush against a police car, accelerator down, wheels spinning. Officers fired 15 shots, killing Rickard and his passenger, Kelly Allen. Rickard's daughter sued the officers under \u00a7 1983 for excessive force. ## Issue Whether the officers' use of deadly force to end the chase (and the firing of 15 shots) violated the Fourth Amendment, and if so whether the officers were entitled to qualified immunity. ## Rule The deadly force was reasonable.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-777b",
      "page": null,
      "quote": "if police officers are justified in firing at a suspect in order to end a severe threat to public safety, the officers need not stop shooting until the threat has ended.",
      "star_marker": "8",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 26739,
      "fragment": "#:~:text=if%20police%20officers%20are%20justified",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-778",
      "page": null,
      "quote": "We have held that petitioners' conduct did not violate the Fourth Amendment, but even if that were not the case, petitioners would still be entitled to summary judgment based on qualified immunity.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2014-05-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Plumhoff v. Rickard",
    "varies_by_point": false,
    "scope_note": "Good law: deadly force to end a dangerous high-speed chase is reasonable; officers also had QI. Reasonableness is judged on the totality (consistent with Barnes v. Felix (2025)).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Christopher J. Weiland v. Palm Beach County Sheriff's Office",
          "cluster_id": 2815299,
          "cite": [
            "792 F.3d 1313",
            "92 Fed. R. Serv. 3d 378",
            "2015 U.S. App. LEXIS 11750",
            "2015 WL 4098270"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Maben v. Troy Thelen",
          "cluster_id": 4483206,
          "cite": [
            "887 F.3d 252"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schuchardt v. President of the United States",
          "cluster_id": 4302531,
          "cite": [
            "839 F.3d 336",
            "2016 U.S. App. LEXIS 18025",
            "2016 WL 5799656"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barna v. Board of School Directors of the Panther Valley School District",
          "cluster_id": 4449477,
          "cite": [
            "877 F.3d 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Raspardo v. Carlone",
          "cluster_id": 8442004,
          "cite": [
            "770 F.3d 97",
            "2014 U.S. App. LEXIS 19010",
            "98 Empl. Prac. Dec. (CCH) 45,175",
            "124 Fair Empl. Prac. Cas. (BNA) 1049",
            "2014 WL 4958157"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "David Gavitt v. Bruce Born",
          "cluster_id": 4253418,
          "cite": [
            "835 F.3d 623",
            "2016 FED App. 0216P",
            "2016 U.S. App. LEXIS 16181"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
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
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Reese, Jr. v. County of Sacramento",
          "cluster_id": 4489118,
          "cite": [
            "888 F.3d 1030"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Katie Joseph v. John Doe",
          "cluster_id": 4821017,
          "cite": [
            "981 F.3d 319"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Phillip Cordell v. Glen McKinney",
          "cluster_id": 2683914,
          "cite": [
            "759 F.3d 573",
            "2014 WL 3455556",
            "2014 U.S. App. LEXIS 13500"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "A.M. Ex Rel. F.M. v. Holmes",
          "cluster_id": 4241340,
          "cite": [
            "830 F.3d 1123"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
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
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paige Ray-Cluney v. Charles Palmer",
          "cluster_id": 4542007,
          "cite": [
            "906 F.3d 540"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Austin Gates v. Hassan Khokar",
          "cluster_id": 4476683,
          "cite": [
            "884 F.3d 1290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
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
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael-Ryan Kruger v. State of Nebraska",
          "cluster_id": 3192229,
          "cite": [
            "820 F.3d 295",
            "2016 U.S. App. LEXIS 6326",
            "2016 WL 1376343"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Angelo DiLuzio v. Village of Yorkville Ohio",
          "cluster_id": 2982966,
          "cite": [
            "796 F.3d 604",
            "2015 FED App. 0179P",
            "2015 U.S. App. LEXIS 13720",
            "2015 WL 4646121"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
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
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leona Mullins v. Oscar Cyranek",
          "cluster_id": 3153107,
          "cite": [
            "805 F.3d 760",
            "2015 FED App. 0273P",
            "2015 U.S. App. LEXIS 19485",
            "2015 WL 6859303"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Randy Cole v. Michael Hunter",
          "cluster_id": 4654098,
          "cite": [
            "935 F.3d 444"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
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
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Debbie Latits v. Lowell Phillips",
          "cluster_id": 4455479,
          "cite": [
            "878 F.3d 541"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
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
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edrei v. Maguire",
          "cluster_id": 8439942,
          "cite": [
            "892 F.3d 525"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kishna Brown v. Bradley Lewis",
          "cluster_id": 2782387,
          "cite": [
            "779 F.3d 401",
            "2004 FED App. 0354P",
            "2015 U.S. App. LEXIS 2917",
            "2015 WL 794705"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Plumhoff v. Rickard:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2675750) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTkyNzg0MDAwMDAwJnM9NDc2MjY5MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%282675750%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 0,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 0,
        "triage_snippet_classified": 200
      },
      "lane2_top_cited": {
        "query": "cites:(2675750)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTkmcz00NzgzNjIwJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%282675750%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2675750)",
        "reviewed": 144,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 144,
        "triage_read": 0,
        "triage_snippet_classified": 144
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2675750)",
    "indexed_citing_opinions": 498,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2675750,
        "count": 498,
        "count_source": "search"
      }
    ],
    "citation_count": 1736,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/plumhoff-v-rickard.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzMzEyODUmcz0xMDQ2MzYxMSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%282675750%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2675750,
        "cited_id": 76270,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 111481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 117950,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 137736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 145705,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 145738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 145875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 145918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 543722,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 772438,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2675750,
        "cited_id": 783116,
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
    "date_created": "2026-07-05T17:12:36Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:12:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:12:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:15:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:12:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Plumhoff v. Rickard

```
(Slip Opinion)              OCTOBER TERM, 2013                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

       PLUMHOFF ET AL. v. RICKARD, A MINOR CHILD,

         INDIVIDUALLY, AND AS SURVIVING DAUGHTER

             OF RICKARD, DECEASED, BY AND

              THROUGH HER MOTHER RICKARD,

                      AS PARENT AND NEXT FRIEND


CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE SIXTH CIRCUIT

      No. 12–1117. Argued March 4, 2014—Decided May 27, 2014
Donald Rickard led police officers on a high-speed car chase that came
 to a temporary halt when Rickard spun out into a parking lot. Rick-
 ard resumed maneuvering his car, and as he continued to use the ac-
 celerator even though his bumper was flush against a patrol car, an
 officer fired three shots into Rickard’s car. Rickard managed to drive
 away, almost hitting an officer in the process. Officers fired 12 more
 shots as Rickard sped away, striking him and his passenger, both of
 whom died from some combination of gunshot wounds and injuries
 suffered when the car eventually crashed.
    Respondent, Rickard’s minor daughter, filed a 42 U. S. C. §1983
 action, alleging that the officers used excessive force in violation of
 the Fourth and Fourteenth Amendments. The District Court denied
 the officers’ motion for summary judgment based on qualified im-
 munity, holding that their conduct violated the Fourth Amendment
 and was contrary to clearly established law at the time in question.
 After finding that it had appellate jurisdiction, the Sixth Circuit held
 that the officers’ conduct violated the Fourth Amendment. It af-
 firmed the District Court’s order, suggesting that it agreed that the
 officers violated clearly established law.
Held:
    1. The Sixth Circuit properly exercised jurisdiction under 28
 U. S. C. §1291, which gives courts of appeals jurisdiction to hear ap-
 peals from “final decisions” of the district courts. The general rule
2                        PLUMHOFF v. RICKARD

                                  Syllabus

    that an order denying a summary judgment motion is not a “final de-
    cision[n],” and thus not immediately appealable, does not apply when
    it is based on a qualified immunity claim. Johnson v. Jones, 515
    U. S. 304, 311. Respondent argues that Johnson forecloses appellate
    jurisdiction here, but the order in Johnson was not immediately ap-
    pealable because it merely decided “a question of ‘evidence sufficien-
    cy,’ ” id., at 313, while here, petitioners’ qualified immunity claims
    raise legal issues quite different from any purely factual issues that
    might be confronted at trial. Deciding such legal issues is a core re-
    sponsibility of appellate courts and does not create an undue burden
    for them. See, e.g., Scott v. Harris, 550 U. S. 372. Pp. 5–7.
       2. The officers’ conduct did not violate the Fourth Amendment.
    Pp. 7–15.
          (a) Addressing this question first will be “beneficial” in “devel-
    op[ing] constitutional precedent” in an area that courts typically con-
    sider in cases in which the defendant asserts a qualified immunity
    defense, Pearson v. Callahan, 555 U. S. 223, 236. Pp. 7–8.
          (b) Respondent’s excessive-force argument requires analyzing the
    totality of the circumstances from the perspective “of a reasonable of-
    ficer on the scene.” Graham v. Connor, 490 U. S. 386, 396. Respond-
    ent contends that the Fourth Amendment did not allow the officers to
    use deadly force to terminate the chase, and that, even if they were
    permitted to fire their weapons, they went too far when they fired as
    many rounds as they did. Pp. 8–12.
            (1) The officers acted reasonably in using deadly force. A “po-
    lice officer’s attempt to terminate a dangerous high-speed car chase
    that threatens the lives of innocent bystanders does not violate the
    Fourth Amendment, even when it places the fleeing motorist at risk
    of serious injury or death.” Scott, supra, at 385. Rickard’s outra-
    geously reckless driving—which lasted more than five minutes, ex-
    ceeded 100 miles per hour, and included the passing of more than two
    dozen other motorists—posed a grave public safety risk, and the rec-
    ord conclusively disproves that the chase was over when Rickard’s
    car came to a temporary standstill and officers began shooting. Un-
    der the circumstances when the shots were fired, all that a reasona-
    ble officer could have concluded from Rickard’s conduct was that he
    was intent on resuming his flight, which would again pose a threat to
    others on the road. Pp. 9–11.
            (2) Petitioners did not fire more shots than necessary to end
    the public safety risk. It makes sense that, if officers are justified in
    firing at a suspect in order to end a severe threat to public safety,
    they need not stop shooting until the threat has ended. Here, during
    the 10-second span when all the shots were fired, Rickard never
    abandoned his attempt to flee and eventually managed to drive away.
                     Cite as: 572 U. S. ____ (2014)                    3

                                Syllabus

  A passenger’s presence does not bear on whether officers violated
  Rickard’s Fourth Amendment rights, which “are personal rights
  [that] may not be vicariously asserted.” Alderman v. United States,
  394 U. S. 165, 174. Pp. 11–12.
     3. Even if the officers’ conduct had violated the Fourth Amend-
  ment, petitioners would still be entitled to summary judgment based
  on qualified immunity. An official sued under §1983 is entitled to
  qualified immunity unless it is shown that the official violated a
  statutory or constitutional right that was “ ‘clearly established’ ” at
  the time of the challenged conduct. Ashcroft v. al-Kidd, 563 U. S. ___,
  ___. Brosseau v. Haugen, 543 U. S. 194, 201, where an officer shot at
  a fleeing vehicle to prevent possible harm, makes plain that no clear-
  ly established law precluded the officer’s conduct there. Thus, to pre-
  vail, respondent must meaningfully distinguish Brosseau or point to
  any “controlling authority” or “robust ‘consensus of cases of persua-
  sive authority,’ ” al-Kidd, supra, at ___, that emerged between the
  events there and those here that would alter the qualified-immunity
  analysis. Respondent has made neither showing. If anything, the
  facts here are more favorable to the officers than the facts in
  Brosseau; and respondent points to no cases that could be said to
  have clearly established the unconstitutionality of using lethal force
  to end a high-speed car chase. Pp. 12–15.
509 Fed. Appx. 388, reversed and remanded.

  ALITO, J., delivered the opinion of the Court, in which ROBERTS, C. J.,
and SCALIA, KENNEDY, THOMAS, SOTOMAYOR, and KAGAN, JJ., joined, in
which GINSBURG, J., joined as to the judgment and Parts I, II, and III–
C, and in which BREYER, J., joined except as to Part III–B–2.
                        Cite as: 572 U. S. ____ (2014)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash­
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 12–1117
                                   _________________


OFFICER VANCE PLUMHOFF, ET AL., PETITIONERS v.

WHITNE RICKARD, A MINOR CHILD, INDIVIDUALLY, AND

   AS SURVIVING DAUGHTER OF DONALD RICKARD,

      DECEASED, BY AND THROUGH HER MOTHER

        SAMANTHA RICKARD, AS PARENT AND 

                   NEXT FRIEND

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE SIXTH CIRCUIT

                                 [May 27, 2014] 


   JUSTICE ALITO delivered the opinion of the Court.*
   The courts below denied qualified immunity for police
officers who shot the driver of a fleeing vehicle to put an
end to a dangerous car chase. We reverse and hold that
the officers did not violate the Fourth Amendment. In the
alternative, we conclude that the officers were entitled to
qualified immunity because they violated no clearly estab­
lished law.
                             I

                             A

   Because this case arises from the denial of the officers’
motion for summary judgment, we view the facts in the
light most favorable to the nonmoving party, the daughter
——————
  * JUSTICE GINSBURG joins the judgment and Parts I, II, and III–C of
this opinion. JUSTICE BREYER joins this opinion except as to Part III–
B–2.
2                     PLUMHOFF v. RICKARD

                         Opinion of the Court

of the driver who attempted to flee. Wilkie v. Robbins, 551
U. S. 537, 543, n. 2 (2007). Near midnight on July 18,
2004, Lieutenant Joseph Forthman of the West Memphis,
Arkansas, Police Department pulled over a white Honda
Accord because the car had only one operating headlight.
Donald Rickard was the driver of the Accord, and Kelly
Allen was in the passenger seat. Forthman noticed an
indentation, “ ‘roughly the size of a head or a basketball’ ”
in the windshield of the car. Estate of Allen v. West Mem-
phis, 2011 WL 197426, *1 (WD Tenn., Jan. 20, 2011). He
asked Rickard if he had been drinking, and Rickard re­
sponded that he had not. Because Rickard failed to pro­
duce his driver’s license upon request and appeared nerv­
ous, Forthman asked him to step out of the car. Rather
than comply with Forthman’s request, Rickard sped away.
   Forthman gave chase and was soon joined by five other
police cruisers driven by Sergeant Vance Plumhoff and
Officers Jimmy Evans, Lance Ellis, Troy Galtelli, and
John Gardner. The officers pursued Rickard east on In­
terstate 40 toward Memphis, Tennessee. While on I–40,
they attempted to stop Rickard using a “rolling roadblock,”
id., at *2, but they were unsuccessful. The District Court
described the vehicles as “swerving through traffic at high
speeds,” id., at *8, and respondent does not dispute that
the cars attained speeds over 100 miles per hour.1 See
Memorandum of Law in Response to Defendants’ Motion
for Summary Judgment in No. 2:05–cv–2585 (WD Tenn.),
p. 16; see also Tr. of Oral Arg. 54:23–55:6. During the
——————
    1 It
      is also undisputed that Forthman saw glass shavings on the
dashboard of Rickard’s car, a sign that the windshield had been broken
recently; that another officer testified that the windshield indentation
and glass shavings would have justified a suspicion “ ‘that someone had
possibly been struck by that vehicle, like a pedestrian’ ”; and that
Forthman saw beer in Rickard’s car. See App. 424–426 (Response to
Defendant’s Statement of Undisputed Material Facts in No. 2:05–cv–
2585 (WD Tenn.), ¶¶15–19).
                 Cite as: 572 U. S. ____ (2014)            3

                     Opinion of the Court

chase, Rickard and the officers passed more than two
dozen vehicles.
   Rickard eventually exited I–40 in Memphis, and shortly
afterward he made “a quick right turn,” causing “contact
[to] occu[r]” between his car and Evans’ cruiser. 2011 WL
197426, *3. As a result of that contact, Rickard’s car spun
out into a parking lot and collided with Plumhoff ’s cruiser.
Now in danger of being cornered, Rickard put his car into
reverse “in an attempt to escape.” Ibid. As he did so,
Evans and Plumhoff got out of their cruisers and ap­
proached Rickard’s car, and Evans, gun in hand, pounded
on the passenger-side window. At that point, Rickard’s
car “made contact with” yet another police cruiser. Ibid.
Rickard’s tires started spinning, and his car “was rocking
back and forth,” ibid., indicating that Rickard was using
the accelerator even though his bumper was flush against
a police cruiser. At that point, Plumhoff fired three shots
into Rickard’s car. Rickard then “reversed in a 180 degree
arc” and “maneuvered onto” another street, forcing Ellis to
“step to his right to avoid the vehicle.” Ibid. As Rickard
continued “fleeing down” that street, ibid., Gardner and
Galtelli fired 12 shots toward Rickard’s car, bringing the
total number of shots fired during this incident to 15.
Rickard then lost control of the car and crashed into a
building. Ibid. Rickard and Allen both died from some
combination of gunshot wounds and injuries suffered in
the crash that ended the chase. See App. 60, 76.
                              B
  Respondent, Rickard’s surviving daughter, filed this
action under Rev. Stat. §1979, 42 U. S. C. §1983, against
the six individual police officers and the mayor and chief
of police of West Memphis. She alleged that the officers
used excessive force in violation of the Fourth and Four­
teenth Amendments.
  The officers moved for summary judgment based on
4                     PLUMHOFF v. RICKARD

                        Opinion of the Court

qualified immunity, but the District Court denied that
motion, holding that the officers’ conduct violated the
Fourth Amendment and was contrary to law that was
clearly established at the time in question. The officers
appealed, but a Sixth Circuit motions panel initially dis­
missed the appeal for lack of jurisdiction based on this
Court’s decision in Johnson v. Jones, 515 U. S. 304, 309
(1995). Later, however, that panel granted rehearing,
vacated its dismissal order, and left the jurisdictional
issue to be decided by a merits panel.
   The merits panel then affirmed the District Court’s
decision on the merits. Estate of Allen v. West Memphis,
509 Fed. Appx. 388 (CA6 2012). On the issue of appellate
jurisdiction, the merits panel began by stating that a
“motion for qualified immunity denied on the basis of a
district court’s determination that there exists a triable
issue of fact generally cannot be appealed on an interlocu­
tory basis.” Id., at 391. But the panel then noted that the
Sixth Circuit had previously interpreted our decision in
Scott v. Harris, 550 U. S. 372 (2007), as creating an “ex­
ception to this rule” under which an immediate appeal
may be taken to challenge “ ‘blatantly and demonstrably
false’ ” factual determinations. 509 Fed. Appx., at 391
(quoting Moldowan v. Warren, 578 F. 3d 351, 370 (CA6
2009)). Concluding that none of the District Court’s fac-
tual determinations ran afoul of that high standard, and
distinguishing the facts of this case from those in Scott,
the panel held that the officers’ conduct violated the
Fourth Amendment. 509 Fed. Appx., at 392, and n. 3.
The panel said nothing about whether the officers violated
clearly established law, but since the panel affirmed the
order denying the officers’ summary judgment motion,2
——————
  2 After expressing some confusion about whether it should dismiss or

affirm, the panel wrote that “it would seem that what we are doing is
affirming [the District Court’s] judgment.” 509 Fed. Appx., at 393.
                 Cite as: 572 U. S. ____ (2014)           5

                     Opinion of the Court

the panel must have decided that issue in respondent’s
favor.
  We granted certiorari. 571 U. S. ____ (2013).
                              II
   We start with the question whether the Court of Ap­
peals properly exercised jurisdiction under 28 U. S. C.
§1291, which gives the courts of appeals jurisdiction to
hear appeals from “final decisions” of the district courts.
   An order denying a motion for summary judgment is
generally not a final decision within the meaning of §1291
and is thus generally not immediately appealable. John-
son, 515 U. S., at 309. But that general rule does not
apply when the summary judgment motion is based on a
claim of qualified immunity. Id., at 311; Mitchell v. For-
syth, 472 U. S. 511, 528 (1985). “[Q]ualified immunity is
‘an immunity from suit rather than a mere defense to
liability.’ ” Pearson v. Callahan, 555 U. S. 223, 231 (2009)
(quoting Mitchell, supra, at 526). As a result, pretrial
orders denying qualified immunity generally fall within
the collateral order doctrine. See Ashcroft v. Iqbal, 556
U. S. 662, 671–672 (2009). This is so because such orders
conclusively determine whether the defendant is entitled
to immunity from suit; this immunity issue is both im­
portant and completely separate from the merits of the
action, and this question could not be effectively reviewed
on appeal from a final judgment because by that time the
immunity from standing trial will have been irretrievably
lost. See ibid; Johnson, supra, at 311–312 (citing Mitchell,
supra, at 525–527).
   Respondent argues that our decision in Johnson, fore­
closes appellate jurisdiction under the circumstances here,
but the order from which the appeal was taken in Johnson
was quite different from the order in the present case. In
Johnson, the plaintiff brought suit against certain police
officers who, he alleged, had beaten him. 515 U. S., at
6                  PLUMHOFF v. RICKARD

                      Opinion of the Court

307. These officers moved for summary judgment, assert­
ing that they were not present at the time of the alleged
beating and had nothing to do with it. Id., at 307–308.
The District Court determined, however, that the evidence
in the summary judgment record was sufficient to support
a contrary finding, and the court therefore denied the
officers’ motion for summary judgment. Id., at 308. The
officers then appealed, arguing that the District Court had
not correctly analyzed the relevant evidence. Ibid.
   This Court held that the Johnson order was not imme­
diately appealable because it merely decided “a question of
‘evidence sufficiency,’ i.e., which facts a party may, or may
not, be able to prove at trial.” Id., at 313. The Court noted
that an order denying summary judgment based on a
determination of “evidence sufficiency” does not present a
legal question in the sense in which the term was used in
Mitchell, the decision that first held that a pretrial order
rejecting a claim of qualified immunity is immediately
appealable. Johnson, 515 U. S., at 314. In addition, the
Court observed that a determination of evidence sufficiency
is closely related to other determinations that the trial
court may be required to make at later stages of the case.
Id., at 317. The Court also noted that appellate courts
have “no comparative expertise” over trial courts in mak­
ing such determinations and that forcing appellate courts
to entertain appeals from such orders would impose an
undue burden. Id., at 309–310, 316.
   The District Court order in this case is nothing like the
order in Johnson. Petitioners do not claim that other
officers were responsible for shooting Rickard; rather, they
contend that their conduct did not violate the Fourth
Amendment and, in any event, did not violate clearly
established law. Thus, they raise legal issues; these issues
are quite different from any purely factual issues that the
trial court might confront if the case were tried; deciding
legal issues of this sort is a core responsibility of appellate
                 Cite as: 572 U. S. ____ (2014)            7

                     Opinion of the Court

courts, and requiring appellate courts to decide such is­
sues is not an undue burden.
  The District Court order here is not materially distin­
guishable from the District Court order in Scott v. Harris,
and in that case we expressed no doubts about the juris­
diction of the Court of Appeals under §1291. Accordingly,
here, as in Scott, we hold that the Court of Appeals prop-
erly exercised jurisdiction, and we therefore turn to the
merits.
                             III

                              A

   Petitioners contend that the decision of the Court of
Appeals is wrong for two separate reasons. They maintain
that they did not violate Rickard’s Fourth Amendment
rights and that, in any event, their conduct did not violate
any Fourth Amendment rule that was clearly established
at the time of the events in question. When confronted
with such arguments, we held in Saucier v. Katz, 533 U. S.
194, 200 (2001), that “the first inquiry must be whether a
constitutional right would have been violated on the facts
alleged.” Only after deciding that question, we concluded,
may an appellate court turn to the question whether the
right at issue was clearly established at the relevant time.
Ibid.
   We subsequently altered this rigid framework in Pear-
son, declaring that “Saucier’s procedure should not be
regarded as an inflexible requirement.” 555 U. S., at 227.
At the same time, however, we noted that the Saucier
procedure “is often beneficial” because it “promotes the
development of constitutional precedent and is especially
valuable with respect to questions that do not frequently
arise in cases in which a qualified immunity defense is
unavailable.” 555 U. S., at 236. Pearson concluded that
courts “have the discretion to decide whether that [Sau-
cier] procedure is worthwhile in particular cases.” Id., at
8                  PLUMHOFF v. RICKARD

                      Opinion of the Court

242.
  Heeding our guidance in Pearson, we begin in this case
with the question whether the officers’ conduct violated
the Fourth Amendment. This approach, we believe, will
be “beneficial” in “develop[ing] constitutional precedent” in
an area that courts typically consider in cases in which the
defendant asserts a qualified immunity defense. See
Pearson, supra, at 236.
                               B
   A claim that law-enforcement officers used excessive
force to effect a seizure is governed by the Fourth
Amendment’s “reasonableness” standard. See Graham v.
Connor, 490 U. S. 386 (1989); Tennessee v. Garner, 471
U. S. 1 (1985). In Graham, we held that determining the
objective reasonableness of a particular seizure under the
Fourth Amendment “requires a careful balancing of the
nature and quality of the intrusion on the individual’s
Fourth Amendment interests against the countervailing
governmental interests at stake.” 490 U. S., at 396 (inter­
nal quotation marks omitted). The inquiry requires ana­
lyzing the totality of the circumstances. See ibid.
   We analyze this question from the perspective “of a
reasonable officer on the scene, rather than with the 20/20
vision of hindsight.” Ibid. We thus “allo[w] for the fact
that police officers are often forced to make split-second
judgments—in circumstances that are tense, uncertain,
and rapidly evolving—about the amount of force that is
necessary in a particular situation.” Id., at 396–397.
   In this case, respondent advances two main Fourth
Amendment arguments. First, she contends that the
Fourth Amendment did not allow petitioners to use deadly
force to terminate the chase. See Brief for Respondent 24–
35. Second, she argues that the “degree of force was ex­
cessive,” that is, that even if the officers were permitted to
fire their weapons, they went too far when they fired as
                 Cite as: 572 U. S. ____ (2014)            9

                     Opinion of the Court

many rounds as they did. See id., at 36–38. We address
each issue in turn.
                              1
   In Scott, we considered a claim that a police officer
violated the Fourth Amendment when he terminated a
high-speed car chase by using a technique that placed a
“fleeing motorist at risk of serious injury or death.” 550
U. S., at 386. The record in that case contained a vide­
otape of the chase, and we found that the events recorded
on the tape justified the officer’s conduct. We wrote as
follows: “Although there is no obvious way to quantify the
risks on either side, it is clear from the videotape that
respondent posed an actual and imminent threat to the
lives of any pedestrians who might have been present, to
other civilian motorists, and to the officers involved in the
chase.” Id., at 383–384. We also wrote:
    “[R]espondent’s vehicle rac[ed] down narrow, two-lane
    roads in the dead of night at speeds that are shock-
    ingly fast. We see it swerve around more than a dozen
    other cars, cross the double-yellow line, and force cars
    traveling in both directions to their respective shoul­
    ders to avoid being hit. We see it run multiple red
    lights and travel for considerable periods of time in
    the occasional center left-turn-only lane, chased by
    numerous police cars forced to engage in the same
    hazardous maneuvers just to keep up.” Id., at 379–
    380 (footnote omitted).
  In light of those facts, “we [thought] it [was] quite clear
that [the police officer] did not violate the Fourth Amend­
ment.” Id., at 381. We held that a “police officer’s attempt
to terminate a dangerous high-speed car chase that
threatens the lives of innocent bystanders does not violate
the Fourth Amendment, even when it places the fleeing
10                     PLUMHOFF v. RICKARD

                          Opinion of the Court

motorist at risk of serious injury or death.”3 Id., at 386.
  We see no basis for reaching a different conclusion here.
As we have explained supra, at ___, the chase in this case
exceeded 100 miles per hour and lasted over five minutes.
During that chase, Rickard passed more than two dozen
other vehicles, several of which were forced to alter course.
Rickard’s outrageously reckless driving posed a grave
public safety risk. And while it is true that Rickard’s car
eventually collided with a police car and came temporarily
to a near standstill, that did not end the chase. Less than
three seconds later, Rickard resumed maneuvering his
car. Just before the shots were fired, when the front
bumper of his car was flush with that of one of the police
cruisers, Rickard was obviously pushing down on the
accelerator because the car’s wheels were spinning, and
then Rickard threw the car into reverse “in an attempt to
escape.” Thus, the record conclusively disproves respond­
ent’s claim that the chase in the present case was already
over when petitioners began shooting. Under the circum­
stances at the moment when the shots were fired, all that
a reasonable police officer could have concluded was that
Rickard was intent on resuming his flight and that, if he
was allowed to do so, he would once again pose a deadly
threat for others on the road. Rickard’s conduct even after
the shots were fired—as noted, he managed to drive away
despite the efforts of the police to block his path—
——————
  3 In holding that petitioners’ conduct violated the Fourth Amend­
ment, the District Court relied on reasoning that is irreconcilable with
our decision in Scott. The District Court held that the danger presented
by a high-speed chase cannot justify the use of deadly force because
that danger was caused by the officers’ decision to continue the chase.
Estate of Allen v. West Memphis, 2011 WL 197426, *8 (WD Tenn., Jan.
20, 2011). In Scott, however, we declined to “lay down a rule requiring
the police to allow fleeing suspects to get away whenever they drive so
recklessly that they put other people’s lives in danger,” concluding that
the Constitution “assuredly does not impose this invitation to impunity­
earned-by-recklessness.” 550 U. S., at 385–386.
                  Cite as: 572 U. S. ____ (2014)            11

                      Opinion of the Court

underscores the point.
  In light of the circumstances we have discussed, it is
beyond serious dispute that Rickard’s flight posed a grave
public safety risk, and here, as in Scott, the police acted
reasonably in using deadly force to end that risk.
                                 2
   We now consider respondent’s contention that, even if
the use of deadly force was permissible, petitioners acted
unreasonably in firing a total of 15 shots. We reject that
argument. It stands to reason that, if police officers are
justified in firing at a suspect in order to end a severe
threat to public safety, the officers need not stop shooting
until the threat has ended. As petitioners noted below, “if
lethal force is justified, officers are taught to keep shooting
until the threat is over.” 509 Fed. Appx., at 392.
   Here, during the 10-second span when all the shots were
fired, Rickard never abandoned his attempt to flee. In­
deed, even after all the shots had been fired, he managed
to drive away and to continue driving until he crashed.
This would be a different case if petitioners had initiated a
second round of shots after an initial round had clearly
incapacitated Rickard and had ended any threat of con­
tinued flight, or if Rickard had clearly given himself up.
But that is not what happened.
   In arguing that too many shots were fired, respondent
relies in part on the presence of Kelly Allen in the front
seat of the car, but we do not think that this factor
changes the calculus. Our cases make it clear that “Fourth
Amendment rights are personal rights which . . . may not
be vicariously asserted.” Alderman v. United States, 394
U. S. 165, 174 (1969); see also Rakas v. Illinois, 439 U. S.
128, 138–143 (1978). Thus, the question before us is
whether petitioners violated Rickard’s Fourth Amendment
rights, not Allen’s. If a suit were brought on behalf of
Allen under either §1983 or state tort law, the risk to
12                    PLUMHOFF v. RICKARD

                         Opinion of the Court

Allen would be of central concern.4 But Allen’s presence in
the car cannot enhance Rickard’s Fourth Amendment
rights. After all, it was Rickard who put Allen in danger
by fleeing and refusing to end the chase, and it would be
perverse if his disregard for Allen’s safety worked to his
benefit.
                               C
   We have held that petitioners’ conduct did not violate
the Fourth Amendment, but even if that were not the case,
petitioners would still be entitled to summary judgment
based on qualified immunity.
   An official sued under §1983 is entitled to qualified
immunity unless it is shown that the official violated a
statutory or constitutional right that was “ ‘clearly estab­
lished’ ” at the time of the challenged conduct. Ashcroft v.
al-Kidd, 563 U. S. ___, ___ (2011) (slip op., at 3). And a
defendant cannot be said to have violated a clearly estab­
lished right unless the right’s contours were sufficiently
definite that any reasonable official in the defendant’s
shoes would have understood that he was violating it. Id.,
at ___ (slip op., at 9). In other words, “existing precedent
must have placed the statutory or constitutional question”
confronted by the official “beyond debate.” Ibid. In addi­
tion, “[w]e have repeatedly told courts . . . not to define
clearly established law at a high level of generality,” id., at
——————
  4 There seems to be some disagreement among lower courts as to
whether a passenger in Allen’s situation can recover under a Fourth
Amendment theory. Compare Vaughan v. Cox, 343 F. 3d 1323 (CA11
2003) (suggesting yes), and Fisher v. Memphis, 234 F. 3d 312 (CA6
2000) (same), with Milstead v. Kibler, 243 F. 3d 157 (CA4 2001) (sug­
gesting no), and Landol-Rivera v. Cruz Cosme, 906 F. 2d 791 (CA1
1990) (same). We express no view on this question. We also note that
in County of Sacramento v. Lewis, 523 U. S. 833, 836 (1998), the Court
held that a passenger killed as a result of a police chase could recover
under a substantive due process theory only if the officer had “a pur­
pose to cause harm unrelated to the legitimate object of arrest.”
                  Cite as: 572 U. S. ____ (2014)            13

                      Opinion of the Court

___ (slip op., at 10), since doing so avoids the crucial ques­
tion whether the official acted reasonably in the particular
circumstances that he or she faced. We think our deci­
sion in Brosseau v. Haugen, 543 U. S. 194 (2004) (per
curiam) squarely demonstrates that no clearly established
law precluded petitioners’ conduct at the time in question.
In Brosseau, we held that a police officer did not violate
clearly established law when she fired at a fleeing vehicle
to prevent possible harm to “other officers on foot who
[she] believed were in the immediate area, . . . occupied
vehicles in [the driver’s] path[,] and . . . any other citizens
who might be in the area.” Id., at 197 (quoting 339 F. 3d
857, 865 (CA9 2003); internal quotation marks omitted).
After surveying lower court decisions regarding the rea­
sonableness of lethal force as a response to vehicular
flight, we observed that this is an area “in which the result
depends very much on the facts of each case” and that the
cases “by no means ‘clearly establish[ed]’ that [the of­
ficer’s] conduct violated the Fourth Amendment.” 543
U. S., at 201. In reaching that conclusion, we held that
Garner and Graham, which are “cast at a high level of
generality,” did not clearly establish that the officer’s
decision was unreasonable. 543 U. S., at 199.
   Brosseau makes plain that as of February 21, 1999—the
date of the events at issue in that case—it was not clearly
established that it was unconstitutional to shoot a fleeing
driver to protect those whom his flight might endanger.
We did not consider later decided cases because they
“could not have given fair notice to [the officer].” Id., at
200, n. 4. To defeat immunity here, then, respondent
must show at a minimum either (1) that the officers’ con­
duct in this case was materially different from the conduct
in Brosseau or (2) that between February 21, 1999, and
July 18, 2004, there emerged either “ ‘controlling authority’ ”
or a “robust ‘consensus of cases of persuasive authority,’ ”
al-Kidd, supra, at ___ (slip op., at 10) (quoting Wilson
14                 PLUMHOFF v. RICKARD

                     Opinion of the Court

v. Layne, 526 U. S. 603, 617 (1999); some internal quota­
tion marks omitted), that would alter our analysis of the
qualified immunity question. Respondent has made nei­
ther showing.
   To begin, certain facts here are more favorable to the
officers. In Brosseau, an officer on foot fired at a driver
who had just begun to flee and who had not yet driven his
car in a dangerous manner. In contrast, the officers here
shot at Rickard to put an end to what had already been a
lengthy, high-speed pursuit that indisputably posed a
danger both to the officers involved and to any civilians
who happened to be nearby. Indeed, the lone dissenting
Justice in Brosseau emphasized that in that case, “there
was no ongoing or prior high-speed car chase to inform the
[constitutional] analysis.” 543 U. S., at 206, n. 4 (opinion
of Stevens, J.). Attempting to distinguish Brosseau, re­
spondent focuses on the fact that the officer there fired
only 1 shot, whereas here three officers collectively fired
15 shots. But it was certainly not clearly established at
the time of the shooting in this case that the number of
shots fired, under the circumstances present here, ren­
dered the use of force excessive.
   Since respondent cannot meaningfully distinguish
Brosseau, her only option is to show that its analysis was
out of date by 2004. Yet respondent has not pointed us to
any case—let alone a controlling case or a robust consen­
sus of cases—decided between 1999 and 2004 that could
be said to have clearly established the unconstitutionality
of using lethal force to end a high-speed car chase. And
respondent receives no help on this front from the opinions
below. The District Court cited only a single case decided
between 1999 and 2004 that identified a possible constitu­
tional violation by an officer who shot a fleeing driver, and
the facts of that case—where a reasonable jury could have
concluded that the suspect merely “accelerated to eighty to
eighty-five miles per hour in a seventy-miles-per-hour
                 Cite as: 572 U. S. ____ (2014)           15

                     Opinion of the Court

zone” and did not “engag[e] in any evasive maneuvers,”
Vaughan v. Cox, 343 F. 3d 1323, 1330–1331 (CA11
2003)—bear little resemblance to those here.
                        *     *    *
  Under the circumstances present in this case, we hold
that the Fourth Amendment did not prohibit petitioners
from using the deadly force that they employed to termi­
nate the dangerous car chase that Rickard precipitated.
In the alternative, we note that petitioners are entitled to
qualified immunity for the conduct at issue because they
violated no clearly established law.
  The judgment of the Court of Appeals is reversed, and
the case is remanded for further proceedings consistent
with this opinion.
                                            It is so ordered.

```

---

## GROUP: content/cases/Preston v. United States.md  (`case`, 6 assertions)

### content_page

```
---
title: "Preston v. United States"
type: case
citation: "376 U.S. 364 (1964)"
parallel_cite: "84 S. Ct. 881; 11 L. Ed. 2d 777"
neutral_cite: 1964 U.S. LEXIS 1578
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1964
date_decided: 1964-03-23
docket: 163
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1964-03-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Preston v. United States
  varies_by_point: false
  scope_note: "The search-incident-to-arrest remoteness holding remains controlling. Preston is a SITA case; the later automobile-exception line ([[Chambers v. Maroney]], [[Michigan v. Thomas]]) independently permits warrantless delayed vehicle searches on probable cause, distinguishing — not overruling — Preston, so it no longer implies every station-house car search is unreasonable."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106771/preston-v-united-states/"
  cluster_id: 106771
  opinion_id: 106771
  identity_checked: true
homes:
  - page: "[[SIA Persons]]"
    role: "Historical"
  - page: "[[Automobile Exception]]"
    role: "Related (cross-doctrine)"
related: ["[[Chambers v. Maroney]]", "[[Chimel v. California]]", "[[Agnello v. United States]]", "[[United States v. Chadwick]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "automobile", "vehicle-search", "warrant-requirement"]
holding: "A warrantless search of a vehicle is not a valid search incident to arrest once the arrestee is in custody and the car has been removed; a search remote in time or place from the arrest cannot be justified as incident to it."
lake:
  record_id: Preston v. United States
  status: verified
  projected_at: 2026-07-09
---

# Preston v. United States

*376 U.S. 364 (1964)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police received a 3 a.m. complaint about three suspicious men who had been sitting in a parked car for hours in a business district. Officers questioned the men, found their answers evasive, learned all three were unemployed with 25 cents among them, and arrested them for vagrancy. The men were searched for weapons and taken to the station; the car, unsearched at the scene, was driven to the station and then towed to a garage. After the men were booked, officers searched the car at the garage, finding loaded revolvers in the glove compartment and — after forcing into the trunk — robbery paraphernalia (a stocking mask, rope, a fake license plate). The items were used to convict petitioner of conspiracy to rob a bank.

## Issue
May a warrantless search of a car at a garage — conducted after the arrestees were in custody at the station and the car had been towed — be justified as a search incident to the arrest?

## Rule
No. A [[Search Incident to Arrest|search incident to arrest]] must be contemporaneous, and "[o]nce an accused is under arrest and in custody, then a search made at another place, without a warrant, is simply not incident to the arrest." — 376 U.S. at 367. ^pin-367

The officer-safety and evidence-preservation "justifications are absent where a search is remote in time or place from the arrest." — [*Id.*](https://www.courtlistener.com/opinion/106771/preston-v-united-states/#:~:text=justifications%20are%20absent%20where%20a) ^pin-367b

On these facts, "the search was too remote in time or place to have been made as incidental to the arrest . . . , [so] the search of the car without a warrant failed to meet the test of reasonableness under the Fourth Amendment, rendering the evidence obtained . . . inadmissible." — *Id.* at 368. ^pin-368

## Application
The car was not searched until the men had been arrested, booked, and taken into custody at the station, and the car had been towed to a garage. At that point none of the arrestees could have reached a weapon in the car or destroyed evidence, and there was no danger the car would be moved out of the locality. The search was therefore too remote in time and place from the arrest to qualify as incident to it, and no warrant had been obtained.

## Conclusion
The warrantless garage search of the car was unreasonable and its fruits inadmissible. The judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Preston* remains a controlling statement of the temporal/spatial limit on [[Search Incident to Arrest|searches incident to arrest]], regularly cited (e.g., in [[United States v. Chadwick]]). It was decided solely on search-incident grounds; the later automobile-exception line ([[Chambers v. Maroney]], [[Michigan v. Thomas]]) **distinguished** *Preston* and now independently permits a warrantless delayed vehicle search on probable cause — so *Preston* does not bar every station-house car search, but its search-incident holding is intact and not overruled.

## Appears on
- [[SIA Persons]] — *Historical*
- [[Automobile Exception]] — *Related (cross-doctrine)*

## Sources
- *Preston v. United States*, 376 U.S. 364 (1964) — https://www.courtlistener.com/opinion/106771/preston-v-united-states/ — pinpoints: 367, 368.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "43798a84eb8f5ac3", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "376 U.S. 364 (1964)", "court": "U.S. Supreme Court", "neutral_cite": "1964 U.S. LEXIS 1578", "official_citation_present": true, "parallel_cite": "84 S. Ct. 881; 11 L. Ed. 2d 777", "title": "Preston v. United States", "year": "1964"}}
{"assertion_id": "22b4f941814cc9e7", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Persons"}, "payload": {"home": "SIA Persons", "role": "Historical", "title": "Preston v. United States"}}
{"assertion_id": "65934ec265dce68d", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Related (cross-doctrine)", "title": "Preston v. United States"}}
{"assertion_id": "b270afb643baf46c", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A warrantless search of a vehicle is not a valid search incident to arrest once the arrestee is in custody and the car has been removed; a search remote in time or place from the arrest cannot be justified as incident to it.", "title": "Preston v. United States"}}
{"assertion_id": "2d847ec9868c0c59", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Preston v. United States"}}
{"assertion_id": "6dbfaaf59bbdf694", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1964-03-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Preston v. United States", "field_i_validity": "good_law", "scope_note": "The search-incident-to-arrest remoteness holding remains controlling. Preston is a SITA case; the later automobile-exception line ([[Chambers v. Maroney]], [[Michigan v. Thomas]]) independently permits warrantless delayed vehicle searches on probable cause, distinguishing — not overruling — Preston, so it no longer implies every station-house car search is unreasonable.", "title": "Preston v. United States", "varies_by_point": "false"}}
```

### lake record — Preston v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Preston v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Preston v. United States",
    "case_name_short": "Preston",
    "case_name_full": "Preston v. United States",
    "input_case_name": "Preston v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1964-03-23",
    "year": 1964,
    "docket": "163",
    "cluster_id": 106771,
    "lead_opinion_id": 106771,
    "sibling_ids": [
      106771
    ],
    "absolute_url": "/opinion/106771/preston-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "376 U.S. 364",
      "volume": "376",
      "reporter": "U.S.",
      "page": "364",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "84 S. Ct. 881",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "881",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "11 L. Ed. 2d 777",
        "volume": "11",
        "reporter": "L. Ed. 2d",
        "page": "777",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1964 U.S. LEXIS 1578",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "1578",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "376 U.S. 364",
        "volume": "376",
        "reporter": "U.S.",
        "page": "364",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 S. Ct. 881",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "881",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "11 L. Ed. 2d 777",
        "volume": "11",
        "reporter": "L. Ed. 2d",
        "page": "777",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1964 U.S. LEXIS 1578",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "1578",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "376 U.S. 364",
    "official_selection": {
      "court_class": "scotus",
      "selected": "376 U.S. 364",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-367",
      "page": null,
      "quote": "--- # Preston v. United States *376 U.S. 364 (1964)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police received a 3 a.m. complaint about three suspicious men who had been sitting in a parked car for hours in a business district. Officers questioned the men, found their answers evasive, learned all three were unemployed with 25 cents among them, and arrested them for vagrancy. The men were searched for weapons and taken to the station; the car, unsearched at the scene, was driven to the station and then towed to a garage. After the men were booked, officers searched the car at the garage, finding loaded revolvers in the glove compartment and \u2014 after forcing into the trunk \u2014 robbery paraphernalia (a stocking mask, rope, a fake license plate). The items were used to convict petitioner of conspiracy to rob a bank. ## Issue May a warrantless search of a car at a garage \u2014 conducted after the arrestees were in custody at the station and the car had been towed \u2014 be justified as a search incident to the arrest? ## Rule No. A search incident to arrest must be contemporaneous, and",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-367b",
      "page": null,
      "quote": "justifications are absent where a search is remote in time or place from the arrest.",
      "star_marker": "367",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 8643,
      "fragment": "#:~:text=justifications%20are%20absent%20where%20a",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-368",
      "page": null,
      "quote": "the search was too remote in time or place to have been made as incidental to the arrest . . . , [so] the search of the car without a warrant failed to meet the test of reasonableness under the Fourth Amendment, rendering the evidence obtained . . . inadmissible.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1964-03-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Preston v. United States",
    "varies_by_point": false,
    "scope_note": "The search-incident-to-arrest remoteness holding remains controlling. Preston is a SITA case; the later automobile-exception line ([[Chambers v. Maroney]], [[Michigan v. Thomas]]) independently permits warrantless delayed vehicle searches on probable cause, distinguishing \u2014 not overruling \u2014 Preston, so it no longer implies every station-house car search is unreasonable.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Dennis",
          "cluster_id": 4679939,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
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
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kenneth Lee Douds v. State",
          "cluster_id": 2983810,
          "cite": [
            "434 S.W.3d 842",
            "2014 WL 2619863",
            "2014 Tex. App. LEXIS 6152"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hughes v. State",
          "cluster_id": 2284872,
          "cite": [
            "334 S.W.3d 379",
            "2011 WL 561497"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Sawyer",
          "cluster_id": 167203,
          "cite": [
            "441 F.3d 890",
            "2006 U.S. App. LEXIS 6838",
            "2006 WL 689451"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Opinion No.",
          "cluster_id": 3256671,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Garner",
          "cluster_id": 8742797,
          "cite": [
            "945 F. Supp. 990",
            "1996 U.S. Dist. LEXIS 16709",
            "1996 WL 655571"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Mark A. McKinnell",
          "cluster_id": 531282,
          "cite": [
            "888 F.2d 669",
            "28 Fed. R. Serv. 1309",
            "1989 U.S. App. LEXIS 16209",
            "1989 WL 127016"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Belton",
          "cluster_id": 5685394,
          "cite": [
            "55 N.Y.2d 49",
            "432 N.E.2d 745",
            "447 N.Y.S.2d 873",
            "1982 N.Y. LEXIS 3067"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Riegler",
          "cluster_id": 2135147,
          "cite": [
            "127 Cal. App. 3d 317",
            "179 Cal. Rptr. 530",
            "1981 Cal. App. LEXIS 2530"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gill v. State",
          "cluster_id": 1770662,
          "cite": [
            "625 S.W.2d 307",
            "1981 Tex. Crim. App. LEXIS 1283"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jozsef Tibor Wiga, United States of America v. Jozsef Tibor Wiga",
          "cluster_id": 396356,
          "cite": [
            "662 F.2d 1325",
            "1981 U.S. App. LEXIS 15460"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rafaela Monclavo-Cruz",
          "cluster_id": 396352,
          "cite": [
            "662 F.2d 1285"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Taylor v. State",
          "cluster_id": 1596133,
          "cite": [
            "399 So. 2d 881"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schmerber v. California",
          "cluster_id": 107262,
          "cite": [
            "16 L. Ed. 2d 908",
            "86 S. Ct. 1826",
            "384 U.S. 757",
            "1966 U.S. LEXIS 1129"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beck v. Ohio",
          "cluster_id": 106936,
          "cite": [
            "13 L. Ed. 2d 142",
            "85 S. Ct. 223",
            "379 U.S. 89",
            "1964 U.S. LEXIS 151",
            "3 Ohio Misc. 71",
            "31 Ohio Op. 2d 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sibron v. New York",
          "cluster_id": 107730,
          "cite": [
            "20 L. Ed. 2d 917",
            "88 S. Ct. 1889",
            "392 U.S. 40",
            "1968 U.S. LEXIS 1346",
            "44 Ohio Op. 2d 402"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ventresca",
          "cluster_id": 106990,
          "cite": [
            "13 L. Ed. 2d 684",
            "85 S. Ct. 741",
            "380 U.S. 102",
            "1965 U.S. LEXIS 2438",
            "16 A.F.T.R.2d (RIA) 5787"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warden, Maryland Penitentiary v. Hayden",
          "cluster_id": 107465,
          "cite": [
            "18 L. Ed. 2d 782",
            "87 S. Ct. 1642",
            "387 U.S. 294",
            "1967 U.S. LEXIS 2753"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cady v. Dombrowski",
          "cluster_id": 108850,
          "cite": [
            "37 L. Ed. 2d 706",
            "93 S. Ct. 2523",
            "413 U.S. 433",
            "1973 U.S. LEXIS 48"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Winston Bryant McConney",
          "cluster_id": 431931,
          "cite": [
            "728 F.2d 1195",
            "1984 U.S. App. LEXIS 25576"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. United States",
          "cluster_id": 107625,
          "cite": [
            "19 L. Ed. 2d 1067",
            "88 S. Ct. 992",
            "390 U.S. 234",
            "1968 U.S. LEXIS 2283"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cooper v. California",
          "cluster_id": 107360,
          "cite": [
            "17 L. Ed. 2d 730",
            "87 S. Ct. 788",
            "386 U.S. 58",
            "1967 U.S. LEXIS 2199"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. McNeely",
          "cluster_id": 858288,
          "cite": [
            "185 L. Ed. 2d 696",
            "133 S. Ct. 1552",
            "569 U.S. 141",
            "2013 U.S. LEXIS 3160",
            "81 U.S.L.W. 4250",
            "24 Fla. L. Weekly Fed. S 150",
            "2013 WL 1628934"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vale v. Louisiana",
          "cluster_id": 108183,
          "cite": [
            "26 L. Ed. 2d 409",
            "90 S. Ct. 1969",
            "399 U.S. 30",
            "1970 U.S. LEXIS 18"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cardwell v. Lewis",
          "cluster_id": 109069,
          "cite": [
            "41 L. Ed. 2d 325",
            "94 S. Ct. 2464",
            "417 U.S. 583",
            "1974 U.S. LEXIS 75",
            "69 Ohio Op. 2d 69"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Edwards",
          "cluster_id": 108995,
          "cite": [
            "39 L. Ed. 2d 771",
            "94 S. Ct. 1234",
            "415 U.S. 800",
            "1974 U.S. LEXIS 120"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106771) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNTIwODAwMDAwMDAmcz0xNTk2MTMzJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106771%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 14,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 16,
        "triage_snippet_classified": 184
      },
      "lane2_top_cited": {
        "query": "cites:(106771)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMzAmcz0xMzg4MDYxJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106771%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106771)",
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
    "complete_query": "cites:(106771)",
    "indexed_citing_opinions": 1251,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106771,
        "count": 1251,
        "count_source": "search"
      }
    ],
    "citation_count": 1906,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/preston-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU5NTI0OSZzPTQ1MjQ4MjImdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28106771%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106771,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106771,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106771,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106771,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106771,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106771,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106771,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106771,
        "cited_id": 106107,
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
    "date_created": "2026-07-05T17:15:33Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:15:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:15:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:19:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:15:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Preston v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b426-12">
  Mr. Justice Black
 </author>
<p id="A69">
  delivered the opinion of the Court.
 </p>
<p id="b426-13">
  Petitioner and three others were convicted in the United States District Court for the Eastern District of Kentucky on a charge of conspiracy to rob a federally insured bank in violation of <span class="citation no-link">18 U. S. C. § 2113</span>, the conviction having been based largely on evidence obtained by the search of a motorcar. The Court of Appeals for the Sixth Circuit affirmed, rejecting the contentions, timely made in the trial and appellate courts, that
  <span citation-index="1" class="star-pagination" label="365"> 
   *365
   </span>
  both the original arrest, on a charge of vagrancy, and the subsequent search and seizure had violated the Fourth Amendment. <span class="citation" data-id="9448645"><a href="/opinion/257690/united-states-v-john-richard-sykes-john-brenton-preston-and-kenneth-ray/" aria-description="Citation for case: United States v. John Richard Sykes, John Brenton...">305 F. 2d 172</a></span>. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./373/931/">373 U. S. 931</a></span>. In the view we take of the case, we heed not decide whether the arrest was valid, since we hold that the search and seizure was not-.
 </p>
<p id="b427-5">
  The police of Newport, Kentucky, received a telephone complaint at 3 o’clock one morning that “three suspicious men acting suspiciously”- had been seated in a motorcar parked in a business district since 10 o’clock the evening before. Four policemen straightaway went to the place where the car was parked and found petitioner and two companions. The officers asked the three men why they were parked there, but the men gave answers which the officers testified were unsatisfactory and evasive. All three men admitted that they were unemployed; all of them together had only 25 cents. One of the men said that he had bought the car the day before (which later turned out to be true), but he could not produce any title. They said that their reason for being there was to meet a truck driver who would pass through Newport that night, but they could not identify the company he worked for, could not say what his truck looked like, and did not know what time he would arrive. The officers arrested the three men for vagrancy, searched them for weapons, and took them to police headquarters. The car, which had not been searched at the time of the arrest, was driven by an officer to the station, from which it was towed to a garage. Soon after the men had been booked at the station, some of the police officers went to the garage to search the car and found two loaded revolvers in the glove compartment. They were unable to open the trunk and returned to the station, where a detective told one of the officers to go back and try to get into the trunk. The officer did so, was able to enter the trunk through the back seat of the car, and in
  <span citation-index="1" class="star-pagination" label="366"> 
   *366
   </span>
  the trunk found caps, women’s stockings (one with mouth and eye holes), rope, pillow slips, an illegally manufactured license plate equipped to be snapped over another plate, and other items. After the search, one of petitioner’s companions confessed that he and two others— he did not name petitioner — intended to rob a bank in Berry, Kentucky, a town about 51 miles from Newport. At this, the police called the Federal Bureau of Investigation into the case and turned over to the Bureau the articles found in the car. It was the use of these articles, over timely objections, which raised the Fourth Amendment question we here consider.
 </p>
<p id="b428-5">
  The Amendment provides:
 </p>
<blockquote id="b428-6">
  “The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.”
 </blockquote>
<p id="b428-7">
  The question whether evidence obtained by state officers and used against a defendant in a federal trial was obtained by unreasonable search and seizure is to be judged as if the search and seizure had been made by federal officers.
  <em>
   Elkins
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">364 U. S. 206</a></span> (1960). Our cases make it clear that searches of motorcars must meet the test of reasonableness under the Fourth Amendment before evidence obtained as a result of such searches is admissible.
  <em>
   E. g., Carroll
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925);
  <em>
   Brinegar
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949). Common sense dictates, of course, that questions involving searches of motorcars or other things readily moved cannot be treated as identical to questions arising out of searches of fixed structures like houses. For this reason, what may be an unreasonable search of
  <span citation-index="1" class="star-pagination" label="367"> 
   *367
   </span>
  a house may be reasonable in the case of a motorcar. See
  <em>
   Carroll
  </em>
  v.
  <em>
   United States, supra,
  </em>
  <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S., at 153</a></span>. But even in the case of motorcars, the test still is, was the search unreasonable. Therefore we must inquire whether the facts of this case are such as to fall within any of the exceptions to the constitutional rule that a search warrant must be had before a search may be made.
 </p>
<p id="b429-5">
  It is argued that the search and seizure was justified as incidental to a lawful arrest. Unquestionably, when a person is lawfully arrested, the police have the right, without a search warrant, to make a contemporaneous search of the person of the accused for weapons or for the fruits of or implements used to commit the crime.
  <em>
   Weeks
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span> (1914);
  <em>
   Agnello
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span> (1925). This right to search and seize without a search warrant extends to things under the accused’s immediate control,
  <em>
   Carroll
  </em>
  v.
  <em>
   United States, supra,
  </em>
  <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S., at 158</a></span>, and, to an extent depending on the circumstances of the case, to the place where he is arrested,
  <em>
   Agnello
  </em>
  v.
  <em>
   United States, supra,
  </em>
  <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S., at 30</a></span>;
  <em>
   Marron
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#199" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 199</a></span> (1927);
  <em>
   United States
  </em>
  v.
  <em>
   Rabinowitz,
  </em>
  <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#61" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 61-62</a></span> (1950). The rule allowing contemporaneous searches is justified, for example, by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the destruction of evidence of the crime — things which might easily happen where the weapon or evidence is on the accused’s person or under his immediate control. But these justifications are absent where a search is remote in time or place from the arrest. Once an accused is under arrest and in custody, then a search made at another place, without a warrant, is simply not incident to the arrest.
  <em>
   Agnello
  </em>
  v.
  <em>
   United States, supra,
  </em>
  <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#31" aria-description="Citation for case: Agnello v. United States">269 U. S., at 31</a></span>. Here, we may assume, as the Government urges, that, either because the arrests were valid or because the police had
  <span citation-index="1" class="star-pagination" label="368"> 
   *368
   </span>
  probable cause to think the car stolen, the police had the right to search the car when they first came on the scene. But this does not decide the question of the reasonableness of a search at a later time and at another place. See
  <em>
   Stoner
  </em>
  v.
  <em>
   California, post,
  </em>
  p. 483. The search of the car was not undertaken until petitioner and his companions had been arrested and taken in custody to the police station and the car had been towed to the garage. At this point there was no danger that any of the men arrested could have used any weapons in the car or could have destroyed any evidence of a crime — assuming that there are articles which can be the “fruits” or “implements” of the crime of vagrancy. Cf.
  <em>
   United States
  </em>
  v.
  <em>
   Jeffers,
  </em>
  <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51-52</a></span> (1951). Nor, since the men were under arrest at the police station and the car was in police custody at a garage, was there any danger that the car would be moved out of the locality or jurisdiction. See
  <em>
   Carroll
  </em>
  v.
  <em>
   United States, supra,
  </em>
  <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S., at 153</a></span>. We think that the search was too remote in time or place to have been made as incidental to the arrest and conclude, therefore, that the search of the car without a warrant failed to meet the test of reasonableness under the Fourth Amendment, rendering the evidence obtained as a result of the search inadmissible.
 </p>
<p id="b430-5">
<em>
   Reversed and remanded.
  </em>
</p>
</opinion>
```

---

## GROUP: content/cases/Rawlings v. Kentucky.md  (`case`, 5 assertions)

### content_page

```
---
title: "Rawlings v. Kentucky"
type: case
citation: "448 U.S. 98 (1980)"
parallel_cite: "100 S. Ct. 2556; 65 L. Ed. 2d 633"
neutral_cite: 1980 U.S. LEXIS 142
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1980
date_decided: 1980-06-25
docket: 79-5146
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1980-06-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Rawlings v. Kentucky
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110326/rawlings-v-kentucky/"
  cluster_id: 110326
  opinion_id: 110326
  identity_checked: true
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: "Key — Progeny / Refinement"
related: ["[[Rakas v. Illinois]]", "[[Katz v. United States]]", "[[United States v. Salvucci]]", "[[Byrd v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "standing", "expectation-of-privacy", "ownership", "consent"]
holding: "Owning the items seized is not enough to challenge a search; a defendant must have a legitimate expectation of privacy in the PLACE…"
lake:
  record_id: Rawlings v. Kentucky
  status: verified
  projected_at: 2026-07-06
---

# Rawlings v. Kentucky

*448 U.S. 98 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
While police detained the occupants of a house and waited for a search warrant, Rawlings dumped a quantity of drugs into the purse of a companion, Vanessa Cox, whom he had known only a few days. When the warrant arrived and an officer searched Cox's purse, the drugs were found; Rawlings immediately admitted they were his. He moved to suppress, claiming his ownership of the drugs gave him a privacy interest in the purse.

## Issue
Whether a defendant who owns the items seized, but lacks a legitimate expectation of privacy in the place searched, may challenge the search — and whether ownership of the items alone suffices.

## Rule
Ownership of the seized items does not, by itself, confer a legitimate expectation of privacy in the place searched. After [[Rakas v. Illinois]], "the two inquiries merge into one: whether governmental officials violated any legitimate expectation of privacy held by petitioner." — 448 U.S. at 106. ^pin-106

Although the defendant's ownership of the property "is undoubtedly one fact to be considered," *[[Rakas v. Illinois|Rakas]]* "emphatically rejected the notion that 'arcane' concepts of property law ought to control the ability to claim the protections of the Fourth Amendment." — 448 U.S. at 105. ^pin-105

## Application
Rawlings had known Cox only a few days, had never before sought or obtained access to her purse, had no right to exclude others from it (another acquaintance had free access), and admitted he held no expectation that the purse would remain free from governmental intrusion; the precipitous "bailment" of the drugs showed no effort to maintain privacy. He therefore had no legitimate expectation of privacy in Cox's purse, and his ownership of the drugs did not supply one. He could not challenge the search.

## Conclusion
Owning the seized drugs did not give Rawlings a privacy interest in Cox's purse; he could not contest the search, and the conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Rawlings* applies [[Rakas v. Illinois]]: privacy in the *[[United States v. Place|place]]* searched, not ownership of the items, governs the ability to challenge a search.

## Appears on
- [[Standing to Challenge a Search]] — *Key — Progeny / Refinement*

## Sources
- *Rawlings v. Kentucky*, 448 U.S. 98 (1980) — https://www.courtlistener.com/opinion/110326/rawlings-v-kentucky/ — pinpoints: 105, 106.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1bd9c63e12e67b68", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "448 U.S. 98 (1980)", "court": "U.S. Supreme Court", "neutral_cite": "1980 U.S. LEXIS 142", "official_citation_present": true, "parallel_cite": "100 S. Ct. 2556; 65 L. Ed. 2d 633", "title": "Rawlings v. Kentucky", "year": "1980"}}
{"assertion_id": "16c94a65c034a45e", "dimension": "support", "kind": "home_role", "locator": {"home": "Standing to Challenge a Search"}, "payload": {"home": "Standing to Challenge a Search", "role": "Key — Progeny / Refinement", "title": "Rawlings v. Kentucky"}}
{"assertion_id": "3b8757cb648b2e2f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Owning the items seized is not enough to challenge a search; a defendant must have a legitimate expectation of privacy in the PLACE…", "title": "Rawlings v. Kentucky"}}
{"assertion_id": "8aaab5f48b9477b2", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1980-06-25", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Rawlings v. Kentucky", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Rawlings v. Kentucky", "varies_by_point": "false"}}
{"assertion_id": "9426b6da9f8b8788", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Rawlings v. Kentucky"}}
```

### lake record — Rawlings v. Kentucky

```json
{
  "schema_version": "s2.v1",
  "record_id": "Rawlings v. Kentucky",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Rawlings v. Kentucky",
    "case_name_short": "Rawlings",
    "case_name_full": "Rawlings v. Kentucky",
    "input_case_name": "Rawlings v. Kentucky",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-06-25",
    "year": 1980,
    "docket": "79-5146",
    "cluster_id": 110326,
    "lead_opinion_id": 110326,
    "sibling_ids": [
      110326,
      9428038,
      9428039,
      9428040,
      9428041
    ],
    "absolute_url": "/opinion/110326/rawlings-v-kentucky/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "448 U.S. 98",
      "volume": "448",
      "reporter": "U.S.",
      "page": "98",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 2556",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "2556",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 2d 633",
        "volume": "65",
        "reporter": "L. Ed. 2d",
        "page": "633",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 142",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "142",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "448 U.S. 98",
        "volume": "448",
        "reporter": "U.S.",
        "page": "98",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 2556",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "2556",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 2d 633",
        "volume": "65",
        "reporter": "L. Ed. 2d",
        "page": "633",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 142",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "142",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "448 U.S. 98",
    "official_selection": {
      "court_class": "scotus",
      "selected": "448 U.S. 98",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-106",
      "page": null,
      "quote": "--- # Rawlings v. Kentucky *448 U.S. 98 (1980)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background While police detained the occupants of a house and waited for a search warrant, Rawlings dumped a quantity of drugs into the purse of a companion, Vanessa Cox, whom he had known only a few days. When the warrant arrived and an officer searched Cox's purse, the drugs were found; Rawlings immediately admitted they were his. He moved to suppress, claiming his ownership of the drugs gave him a privacy interest in the purse. ## Issue Whether a defendant who owns the items seized, but lacks a legitimate expectation of privacy in the place searched, may challenge the search \u2014 and whether ownership of the items alone suffices. ## Rule Ownership of the seized items does not, by itself, confer a legitimate expectation of privacy in the place searched. After [[Rakas v. Illinois]],",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-105",
      "page": null,
      "quote": "is undoubtedly one fact to be considered,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1980-06-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Rawlings v. Kentucky",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Garrett",
          "cluster_id": 4552162,
          "cite": [
            "2018 Ohio 4530",
            "123 N.E.3d 327"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532256,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532251,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Pirk",
          "cluster_id": 7327733,
          "cite": [
            "282 F. Supp. 3d 585"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane1_negative"
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
        "journal_ref": "Rawlings v. Kentucky:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Smith",
          "cluster_id": 2713876,
          "cite": [
            "2014 SD 50",
            "851 N.W.2d 719",
            "2014 S.D. LEXIS 65",
            "2014 WL 3558758"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane1_negative"
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
        "journal_ref": "Rawlings v. Kentucky:lane1_negative"
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
        "journal_ref": "Rawlings v. Kentucky:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Joshua Daniel Fleming",
          "cluster_id": 4472496,
          "cite": [
            "790 N.W.2d 560",
            "2010 Iowa Sup. LEXIS 110"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane1_negative"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Matthews",
          "cluster_id": 2362733,
          "cite": [
            "805 S.W.2d 776",
            "1990 Tenn. Crim. App. LEXIS 597"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Ciraolo",
          "cluster_id": 111666,
          "cite": [
            "90 L. Ed. 2d 210",
            "106 S. Ct. 1809",
            "476 U.S. 207",
            "1986 U.S. LEXIS 154"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ballard",
          "cluster_id": 1533349,
          "cite": [
            "987 S.W.2d 889",
            "1999 Tex. Crim. App. LEXIS 14",
            "1999 WL 89535"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Knotts",
          "cluster_id": 110882,
          "cite": [
            "75 L. Ed. 2d 55",
            "103 S. Ct. 1081",
            "460 U.S. 276",
            "1983 U.S. LEXIS 135",
            "51 U.S.L.W. 4232"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Lee Rusher, United States of America v. Sarah Jean Shoemaker Rusher, A/K/A Sarah Anne Rusher, United States of America v. James Joseph Flannery, A/K/A James Joseph Fleming, A/K/A Richard J. Mutschler",
          "cluster_id": 584528,
          "cite": [
            "966 F.2d 868",
            "1992 U.S. App. LEXIS 12338"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sepulveda",
          "cluster_id": 195094,
          "cite": [
            "15 F.3d 1161"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Campbell",
          "cluster_id": 4463634,
          "cite": [
            "2018 COA 5",
            "425 P.3d 1163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Letner and Tobin",
          "cluster_id": 2630926,
          "cite": [
            "235 P.3d 62",
            "50 Cal. 4th 99",
            "112 Cal. Rptr. 3d 746",
            "2010 Cal. LEXIS 7290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Oody",
          "cluster_id": 1740610,
          "cite": [
            "823 S.W.2d 554",
            "1991 Tenn. Crim. App. LEXIS 405"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Carter",
          "cluster_id": 2629957,
          "cite": [
            "117 P.3d 476",
            "32 Cal. Rptr. 3d 759",
            "36 Cal. 4th 1114",
            "2005 Cal. Daily Op. Serv. 7196",
            "2005 Daily Journal DAR 9801",
            "2005 Cal. LEXIS 8908"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ramirez-Portoreal",
          "cluster_id": 2033638,
          "cite": [
            "666 N.E.2d 207",
            "88 N.Y.2d 99",
            "643 N.Y.S.2d 502"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110326 OR 9428038 OR 9428039 OR 9428040 OR 9428041) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjgwMzYxNjAwMDAwJnM9MjYzMDkyNiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110326+OR+9428038+OR+9428039+OR+9428040+OR+9428041%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110326 OR 9428038 OR 9428039 OR 9428040 OR 9428041)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNDImcz00NzU4NDAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110326+OR+9428038+OR+9428039+OR+9428040+OR+9428041%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110326 OR 9428038 OR 9428039 OR 9428040 OR 9428041)",
        "reviewed": 34,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 34,
        "triage_read": 0,
        "triage_snippet_classified": 34
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110326 OR 9428038 OR 9428039 OR 9428040 OR 9428041)",
    "indexed_citing_opinions": 1565,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110326,
        "count": 1385,
        "count_source": "search"
      },
      {
        "opinion_id": 9428038,
        "count": 212,
        "count_source": "search"
      },
      {
        "opinion_id": 9428039,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428040,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428041,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2426,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/rawlings-v-kentucky.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MTQ1MzQmcz0xMDAyMDg3NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110326+OR+9428038+OR+9428039+OR+9428040+OR+9428041%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110326,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 108760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 110161,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 270326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 304598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 2463407,
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
    "date_created": "2026-07-05T17:23:01Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:23:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:23:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:26:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:23:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Rawlings v. Kentucky

```
<div>
<center><b><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">448 U.S. 98</a></span> (1980)</b></center>
<center><h1>RAWLINGS<br>
v.<br>
KENTUCKY.</h1></center>
<center>No. 79-5146.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 26, 1980.</center>
<center>Decided June 25, 1980.</center>
CERTIORARI TO THE SUPREME COURT OF KENTUCKY.
<p><span class="star-pagination">*99</span> <i>J. Vincent Aprile II</i> argued the cause and filed briefs for petitioner.</p>
<p><i>Victor Fox,</i> Assistant Attorney General of Kentucky, argued the cause for respondent. With him on the brief were <i>Steven L. Beshear,</i> Attorney General, and <i>Gerald Henry</i> and <i>Patrick B. Kimberlin III,</i> Assistant Attorneys General.</p>
<p><span class="star-pagination">*100</span> MR. JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>Petitioner David Rawlings was convicted by the Commonwealth of Kentucky on charges of trafficking in, and possession of, various controlled substances. Throughout the proceedings below, Rawlings challenged the admissibility of certain evidence and statements on the ground that they were the fruits of an illegal detention and illegal searches. The trial court, the Kentucky Court of Appeals, and the Supreme Court of Kentucky all rejected Rawlings' challenges. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./444/989/">444 U. S. 989</a></span>, and now affirm.</p>
<p></p>
<h2>I</h2>
<p>In the middle of the afternoon on October 18, 1976, six police officers armed with a warrant for the arrest of one Lawrence Marquess on charges of drug distribution arrived at Marquess' house in Bowling Green, Ky. In the house at the time the police arrived were one of Marquess' housemates, Dennis Saddler, and four visitors, Keith Northern, Linda Braden, Vanessa Cox, and petitioner David Rawlings. While searching unsuccessfully in the house for Marquess, several police officers smelled marihuana smoke and saw marihuana seeds on the mantel in one of the bedrooms. After conferring briefly, Officers Eddie Railey and John Bruce left to obtain a search warrant. While Railey and Bruce were gone, the other four officers detained the occupants of the house in the living room, allowing them to leave only if they consented to a body search. Northern and Braden did consent to such a search and were permitted to depart. Saddler, Cox, and petitioner remained seated in the living room.</p>
<p>Approximately 45 minutes later, Railey and Bruce returned with a warrant authorizing them to search the house. Railey read the warrant to Saddler, Cox, and petitioner, and also read <i>"Miranda"</i> warnings from a card he carried in his pocket. At that time, Cox was seated on a couch with petitioner seated to her left. In the space between them was Cox's handbag.</p>
<p>After Railey finished his recitation, he approached petitioner <span class="star-pagination">*101</span> and told him to stand. Officer Don Bivens simultaneously approached Cox and ordered her to empty the contents of her purse onto a coffee table in front of the couch. Among those contents were a jar containing 1,800 tablets of LSD and a number of smaller vials containing benzphetamine, methamphetamine, methyprylan, and pentobarbital, all of which are controlled substances under Kentucky law.</p>
<p>Upon pouring these objects out onto the coffee table, Cox turned to petitioner and told him "to take what was his." App. 62. Petitioner, who was standing in response to Officer Railey's command, immediately claimed ownership of the controlled substances. At that time, Railey searched petitioner's person and found $4,500 in cash in petitioner's shirt pocket and a knife in a sheath at petitioner's side. Railey then placed petitioner under formal arrest.</p>
<p>Petitioner was indicted for possession with intent to sell the various controlled substances recovered from Cox's purse. At the suppression hearing, he testified that he had flown into Bowling Green about a week before his arrest to look for a job and perhaps to attend the local university. He brought with him at that time the drugs later found in Cox's purse. Initially, petitioner stayed in the house where the arrest took place as the guest of Michael Swank, who shared the house with Marquess and Saddler. While at a party at that house, he met Cox and spent at least two nights of the next week on a couch at Cox's house.</p>
<p>On the morning of petitioner's arrest, Cox had dropped him off at Swank's house where he waited for her to return from class. At that time, he was carrying the drugs in a green bank bag. When Cox returned to the house to meet him, petitioner dumped the contents of the bank bag into Cox's purse. Although there is dispute over the discussion that took place, petitioner testified that he "asked her if she would carry this for me, and she said, `yes'. . . ." App. 42.<sup>[1]</sup> Petitioner <span class="star-pagination">*102</span> then left the room to use the bathroom and, by the time he returned, discovered that the police had arrived to arrest Marquess.</p>
<p>The trial court denied petitioner's motion to suppress the drugs and the money and to exclude the statements made by petitioner when the police discovered the drugs. According to the trial court, the warrant obtained by the police authorized them to search Cox's purse. Moreover, even if the search of the purse was illegal, the trial court believed that petitioner lacked "standing" to contest that search. Finally, the trial court believed that the search that revealed the money and the knife was permissible "under the exigencies of the situation." <i>Id.,</i> at 21. After a bench trial, petitioner was found guilty of possession with intent to sell LSD and of possession of benzphetamine, methamphetamine, methyprylan, and pentobarbital.</p>
<p><span class="star-pagination">*103</span> The Kentucky Court of Appeals affirmed. Disagreeing with the trial court, the appellate court held that petitioner did have "standing" to dispute the legality of the search of Cox's purse but that the detention of the five persons present in the house and the subsequent searches were legitimate because the police had probable cause to arrest all five people in the house when they smelled the marihuana smoke and saw the marihuana seeds.</p>
<p>The Supreme Court of Kentucky in turn affirmed, but again on a somewhat different rationale. See <span class="citation" data-id="9778383"><a href="/opinion/2463407/rawlings-v-commonwealth/" aria-description="Citation for case: Rawlings v. Commonwealth">581 S. W. 2d 348</a></span> (1979). According to the Supreme Court, petitioner had no "standing" because he had no "legitimate or reasonable expectation of freedom from governmental intrusion" into Cox's purse. <span class="citation" data-id="9778383"><a href="/opinion/2463407/rawlings-v-commonwealth/#350" aria-description="Citation for case: Rawlings v. Commonwealth"><i>Id.,</i> at 350</a></span>, citing <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978). Moreover, according to the Supreme Court, the search uncovering the money in petitioner's pocket, which search followed petitioner's admission that he owned the drugs in Cox's purse, was justifiable as incident to a lawful arrest based on probable cause.</p>
<p></p>
<h2>II</h2>
<p>In this Court, petitioner challenges three aspects of the judgment below. First, he claims that he did have a reasonable expectation of privacy in Cox's purse so as to allow him to challenge the legality of the search of that purse.<sup>[2]</sup> Second, petitioner argues that his admission of ownership was the fruit of an illegal detention that began when the police refused to let the occupants of the house leave unless they consented to a search. Third, petitioner contends that the search uncovering the money and the knife was itself illegal.</p>
<p></p>
<h2>
<span class="star-pagination">*104</span> A</h2>
<p>In holding that petitioner could not challenge the legality of the search of Cox's purse, the Supreme Court of Kentucky looked primarily to our then recent decision in <i>Rakas</i> v. <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Illinois, supra</a></span></i><i>,</i> where we abandoned a separate inquiry into a defendant's "standing" to contest an allegedly illegal search in favor of an inquiry that focused directly on the substance of the defendant's claim that he or she possessed a "legitimate expectation of privacy" in the area searched. See <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967). In the present case, the Supreme Court of Kentucky looked to the "totality of the circumstances," including petitioner's own admission at the suppression hearing that he did not believe that Cox's purse would be free from governmental intrusion,<sup>[3]</sup> and held that petitioner "[had] not made a sufficient showing that his legitimate or reasonable expectations of privacy were violated" by the search of the purse. <span class="citation" data-id="9778383"><a href="/opinion/2463407/rawlings-v-commonwealth/#350" aria-description="Citation for case: Rawlings v. Commonwealth">581 S. W. 2d, at 350</a></span>.</p>
<p>We believe that the record in this case supports that conclusion. Petitioner, of course, bears the burden of proving not only that the search of Cox's purse was illegal, but also that he had a legitimate expectation of privacy in that purse. See <span class="star-pagination">*105</span> <i>Rakas</i> v. <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#131" aria-description="Citation for case: Rakas v. Illinois"><i>Illinois, supra,</i> at 131, n. 1</a></span>; <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#389" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 389-390</a></span> (1968). At the time petitioner dumped thousands of dollars worth of illegal drugs into Cox's purse, he had known her for only a few days. According to Cox's uncontested testimony, petitioner had never sought or received access to her purse prior to that sudden bailment. Contrast <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#259" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 259</a></span> (1960). Nor did petitioner have any right to exclude other persons from access to Cox's purse. See <i>Rakas</i> v. <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#149" aria-description="Citation for case: Rakas v. Illinois"><i>Illinois, supra,</i> at 149</a></span>. In fact, Cox testified that Bob Stallons, a longtime acquaintance and frequent companion of Cox's, had free access to her purse and on the very morning of the arrest had rummaged through its contents in search of a hairbrush. Moreover, even assuming that petitioner's version of the bailment is correct and that Cox did consent to the transfer of possession,<sup>[4]</sup> the precipitous nature of the transaction hardly supports a reasonable inference that petitioner took normal precautions to maintain his privacy. Contrast <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#11" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 11</a></span> (1977); <i>Katz</i> v. <i>United States, supra,</i> at 352. In addition to all the foregoing facts, the record also contains a frank admission by petitioner that he had no subjective expectation that Cox's purse would remain free from governmental intrusion, an admission credited by both the trial court and the Supreme Court of Kentucky. See n. 3, <i>supra,</i> and accompanying text.</p>
<p>Petitioner contends nevertheless that, because he claimed ownership of the drugs in Cox's purse, he should be entitled to challenge the search regardless of his expectation of privacy. We disagree. While petitioner's ownership of the drugs is undoubtedly one fact to be considered in this case, <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span></i> emphatically rejected the notion that "arcane" concepts of property law ought to control the ability to claim the protections of the Fourth Amendment. See <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#149" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 149-150, n. 17</a></span>. See also <i>United States</i> v. <i>Salvucci, ante,</i> at 91-92. <span class="star-pagination">*106</span> Had petitioner placed his drugs in plain view, he would still have owned them, but he could not claim any legitimate expectation of privacy. Prior to <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span>,</i> petitioner might have been given "standing" in such a case to challenge a "search" that netted those drugs but probably would have lost his claim on the merits. After <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span>,</i> the two inquiries merge into one: whether governmental officials violated any legitimate expectation of privacy held by petitioner.</p>
<p>In sum, we find no reason to overturn the lower court's conclusion that petitioner had no legitimate expectation of privacy in Cox's purse at the time of the search.</p>
<p></p>
<h2>B</h2>
<p>We turn, then, to petitioner's contention that the occupants of the house were illegally detained by the police and that his admission to ownership of the drugs was a fruit of that illegal detention. Somewhat surprisingly, none of the courts below confronted this issue squarely, even though it would seem to be presented under any analysis of this case except that adopted by the Kentucky Court of Appeals, which concluded that the police officers were entitled to arrest the five occupants of the house as soon as they smelled marihuana smoke and saw the marihuana seeds.</p>
<p>We can assume both that this issue was properly presented in the Kentucky courts and that the police violated the Fourth and Fourteenth Amendments by detaining petitioner and his companions in the house while they obtained a search warrant for the premises. Even given such a constitutional violation, however, exclusion of petitioner's admissions would not be necessary unless his statements were the result of his illegal detention. As we noted in <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590, 603</a></span> (1975), where we rejected a "but for" approach to the admissibility of such statements, "persons arrested illegally frequently may decide to confess, as an act of free will unaffected by the initial illegality." In <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> we also set forth <span class="star-pagination">*107</span> the standard for determining whether such statements were tainted by antecedent illegality:</p>
<blockquote>"The question whether a confession is the product of a free will . . . must be answered on the facts of each case. No single fact is dispositive. . . . The <i>Miranda</i> warnings are an important factor, to be sure, in determining whether the confession is obtained by exploitation of an illegal arrest. But they are not the only factor to be considered. The temporal proximity of the arrest and the confession, the presence of intervening circumstances, and, particularly, the purpose and flagrancy of the official misconduct are all relevant. The voluntariness of the statement is a threshold requirement. And the burden of showing admissibility rests, of course, on the prosecution." <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois"><i>Id.,</i> at 603-604</a></span> (footnotes and citations omitted).</blockquote>
<p>See also <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#218" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 218</a></span> (1979). As already noted, the lower courts did not undertake the inquiry suggested by <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>.</i> Nevertheless, as in <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> itself, we believe that "the trial resulted in a record of amply sufficient detail and depth from which the determination may be made." <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 604</a></span>.</p>
<p>First, we observe that petitioner received <i>Miranda</i> warnings only moments before he made his incriminating statements, a consideration <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> treated as important, although not dispositive, in determining whether the statements at issue were obtained by exploitation of an illegal detention.</p>
<p>Second, <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> calls our attention to the "temporal proximity of the arrest and the confession. . . ." <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois"><i>Id.,</i> at 603</a></span>. In this case, petitioner and his companions were detained for a period of approximately 45 minutes. Although under the strictest of custodial conditions such a short lapse of time might not suffice to purge the initial taint, we believe it necessary to examine the precise conditions under which the occupants of this house were detained. By all accounts, the three people who chose not to consent to a body search in order to leave sat <span class="star-pagination">*108</span> quietly in the living room or, at least initially, moved freely about the first floor of the house. Upon being informed that he would be detained until Officers Railey and Bruce returned with a search warrant, Dennis Saddler "just went on in and got a cup of coffee and sat down and started waiting" for the officers to return. Tr. 109. When asked by petitioner's counsel whether there was "any show of force or violence by you or Dave or anybody else," Saddler explained:</p>
<blockquote>"A Oh, no. One person tried to sick my four and a half month old dog on one of the officers. (laughing)</blockquote>
<blockquote>"Q48 You're saying that in a joking manner?</blockquote>
<blockquote>"A Yeah. He just wagged his tail.</blockquote>
<blockquote>"Q49 And other than that, that's the most violent thing you proposed toward these police officers; is that correct?</blockquote>
<blockquote>"A Yes sir. I wouldthey were more or less courteous to us and were trying to bewe offered them coffee or a drink of water or whatever they wanted." <i>Id.,</i> at 113.</blockquote>
<p>According to Saddler, petitioner's first reaction when the officers told him that he would be detained pending issuance of a search warrant was to "[get] up and put an album on. . . ." <i>Id.,</i> at 110. As even the dissenting judge in the Court of Appeals noted: "[A]ll witnesses for both sides of this litigation agreed to the congenial atmosphere existing during the forty-five minute interval. . . ." App. 73 (Lester, J., dissenting). We think that these circumstances outweigh the relatively short period of time that elapsed between the initiation of the detention and petitioner's admissions.</p>
<p>Third, <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> suggests that we inquire whether any circumstances intervened between the initial detention and the challenged statements. Here, where petitioner's admissions were apparently spontaneous reactions to the discovery of his drugs in Cox's purse, we have little doubt that this factor weighs heavily in favor of a finding that petitioner acted "of free will unaffected by the initial illegality." 422 U. S., at <span class="star-pagination">*109</span> 603. Nor need we speculate as to petitioner's motivations in admitting ownership of the drugs, since he explained them later to Lawrence Marquess and Dennis Saddler. Under examination by petitioner's counsel, Marquess testified as follows:</p>
<blockquote>"Q1 Mr. Marquess, when you were talking to David Rawlings in the jail, and he told you that the things were dumped out on the table and that he admitted they were his, did he tell you why he did that?</blockquote>
<blockquote>"A Well, he said Vanessa [Cox] was freaking out, you know, or something.</blockquote>
<blockquote>"Q2 Did he tell you that he did that to protect her or words to that effect?</blockquote>
<blockquote>"A Well, now, I mean he said he was going to take what was his, I mean, he wasn't going to try to pin that on her." Tr. 130.</blockquote>
<p>Saddler offered additional insight into petitioner's motivations:</p>
<blockquote>"Q114 Did Dave Rawlings make any statements to you in jail about any of these substances?</blockquote>
<blockquote>"A Yes sir.</blockquote>
<blockquote>"Q115 And would you tell the Court what statements he made?</blockquote>
<blockquote>"A well, his main concern was whether or not Vanessa Cox was going to say anything, and he just kept talking and harping on that, and I don't know how many times he mentioned it, you know, `I hope she doesn't break,' or hope she doesn't talk. And I saw her walking on the sidewalk through the windows and got a little upset about that because we all thought she turned State's evidence." <i>Id.,</i> at 103.</blockquote>
<p>Fourth, <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> mandates consideration of "the purpose and flagrancy of the official misconduct. . . ." <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 604</a></span>. The officers who detained petitioner and his companions uniformly testified that they took those measures to avoid the <span class="star-pagination">*110</span> asportation or destruction of the marihuana they thought was present in the house and that they believed that a warrant authorizing them to search the house would also authorize them to search the five occupants of the house. While the legality of temporarily detaining a person at the scene of suspected drug activity to secure a search warrant may be an open question,<sup>[5]</sup> and while the officer's belief about the scope of the warrant they obtained may well have been erroneous under our recent decision in <i>Ybarra</i> v. <i>Illinois,</i> <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85</a></span> (1979), the conduct of the police here does not rise to the level of conscious or flagrant misconduct requiring prophylactic exclusion of petitioner's statements. Contrast <i>Brown</i> v. <i>Illinois, supra,</i> at 605.</p>
<p>Finally, while <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> requires that the voluntariness of the statement be established as a threshold requirement, petitioner has not argued here or in any other court that his admission to ownership of the drugs was anything other than voluntary. Thus, examining the totality of circumstances present in this case, we believe that the Commonwealth of Kentucky has carried its burden of showing that petitioner's statements were acts of free will unaffected by any illegality in the initial detention.</p>
<p></p>
<h2>C</h2>
<p>Petitioner also contends that the search of his person that uncovered the money and the knife was illegal. Like the <span class="star-pagination">*111</span> Supreme Court of Kentucky, we have no difficulty upholding this search as incident to petitioner's formal arrest. Once petitioner admitted ownership of the sizable quantity of drugs found in Cox's purse, the police clearly had probable cause to place petitioner under arrest. Where the formal arrest followed quickly on the heels of the challenged search of petitioner's person, we do not believe it particularly important that the search preceded the arrest rather than vice versa. See <i>Bailey</i> v. <i>United States,</i> 128 U. S. App. D. C. 354, 357, <span class="citation multiple-matches"><a href="/c/F.%202d/389/305/">389 F. 2d 305</a></span>, 308 (1967); <i>United States</i> v. <i>Brown,</i> 150 U. S. App. D. C. 113, 114, <span class="citation" data-id="304598"><a href="/opinion/304598/united-states-v-reginald-t-brown/#950" aria-description="Citation for case: United States v. Reginald T. Brown">463 F. 2d 949, 950</a></span> (1972). See also <i>Cupp</i> v. <i>Murphy,</i> <span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291</a></span> (1973); <i>United States</i> v. <i>Gorman,</i> <span class="citation" data-id="270326"><a href="/opinion/270326/united-states-v-robert-william-gorman-and-edward-terrence-roche/#160" aria-description="Citation for case: United States v. Robert William Gorman and Edward...">355 F. 2d 151, 160</a></span> (CA2 1965) (dictum), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./384/1024/">384 U. S. 1024</a></span> (1966).<sup>[6]</sup></p>
<p></p>
<h2>III</h2>
<p>Having found no error in the lower courts' refusal to suppress the evidence challenged by petitioner, we believe that the judgment of the Supreme Court of Kentucky should be, and the same hereby is,</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE BLACKMUN, concurring.</p>
<p>I join the Court's opinion, but I write separately to explain my somewhat different approach to the issues addressed in Part II-A thereof.</p>
<p>In my view, <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978), recognized two analytically distinct but "invariably intertwined" issues of substantive Fourth Amendment jurisprudence. <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#139" aria-description="Citation for case: Rakas v. Illinois"><i>Id.,</i> at 139</a></span>. The first is "whether [a] disputed search or seizure has infringed an interest of the defendant which the Fourth Amendment was designed to protect," <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#140" aria-description="Citation for case: Rakas v. Illinois"><i>id.,</i> at 140</a></span>; the second <span class="star-pagination">*112</span> is whether "the challenged search or seizure violated [that] Fourth Amendment righ[t]," <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">ibid.</a></span></i> The first of these questions is answered by determining whether the defendant has a "legitimate expectation of privacy" that has been invaded by a governmental search or seizure. The second is answered by determining whether applicable cause and warrant requirements have been properly observed.</p>
<p>I agree with the Court that these two inquiries "merge into one," <i>ante,</i> at 106, in the sense that both are to be addressed under the principles of Fourth Amendment analysis developed in <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), and its progeny. But I do not read today's decision, or <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span>,</i> as holding that it is improper for lower courts to treat these inquiries as distinct components of a Fourth Amendment claim. Indeed, I am convinced that it would invite confusion to hold otherwise. It remains possible for a defendant to prove that his legitimate interest of privacy was invaded, and yet fail to prove that the police acted illegally in doing so. And it is equally possible for a defendant to prove that the police acted illegally, and yet fail to prove that his own privacy interest was affected.</p>
<p>Nor do I read this Court's decisions to hold that property interests cannot be, in some circumstances at least, weighty factors in establishing the existence of Fourth Amendment rights. Not every concept of ownership or possession is "arcane." Not every interest in property exists only in the desiccated atmosphere of ancient maxims and dusty books. Earlier this Term the Court recognized that "the right to exclude" is an essential element of modern property rights. <i>Kaiser Aetna</i> v. <i>United States,</i> <span class="citation" data-id="9427728"><a href="/opinion/110161/kaiser-aetna-v-united-states/#179" aria-description="Citation for case: Kaiser Aetna v. United States">444 U. S. 164, 179-180</a></span> (1979). In my view, that "right to exclude" often may be a principal determinant in the establishment of a legitimate Fourth Amendment interest. Accordingly, I would confine analysis to the facts of this case. On those facts, however, I agree that petitioner's possessory interest in the vials of controlled <span class="star-pagination">*113</span> substances is not sufficient to create a privacy interest in Vanessa Cox's purse, and that such an interest was not otherwise conferred by any agreement between petitioner and Cox.</p>
<p>MR. JUSTICE WHITE, with whom MR. JUSTICE STEWART joins, concurring in part.</p>
<p>Although I join Parts I and II-A of the Court's opinion, I do not join Parts II-B, II-C, and III because I believe that the fruits inquiry undertaken in Part II-B should not be done in the first instance in this Court. As the Court recognizes, the Supreme Court of Kentucky did not address the question whether petitioner's admission to ownership of the drugs was the fruit of an illegal detention, even though the question was presented there. The state-court majority did state that in concluding that the search of petitioner's person was incident to a valid arrest it "disregard[ed] as irrelevant the detention during the period in which the officers were procuring a search warrant." The court also observed that "[t]his search was not explored in detail at the suppression hearing" and that "the sequence of the search of the purse and Rawlings' admission of ownership of the drugs is not clearly established in the record." The court then concluded that "[c]learly, after Rawlings admitted ownership of the drugs, the officers were entitled to arrest and search the person, or search and then arrest." <span class="citation" data-id="9778383"><a href="/opinion/2463407/rawlings-v-commonwealth/#350" aria-description="Citation for case: Rawlings v. Commonwealth">581 S. W. 2d 348, 350</a></span> (1979).</p>
<p>In proceeding in this manner, the Supreme Court of Kentucky plainly failed properly to dispose of a federal question, as the Court implicitly recognizes. Because the fruits question was never addressed below and was barely mentioned in the briefs before this Court, I would vacate the judgment below and remand to permit the state court to address the question under the correct legal standard. This Court should not attempt to decide a factual issue on a record that the <span class="star-pagination">*114</span> state court itself apparently thought inadequate for that purpose.</p>
<p>MR. JUSTICE MARSHALL, with whom MR. JUSTICE BRENNAN joins, dissenting.</p>
<p>The vials of pills found in Vanessa Cox's purse and petitioner's admission that they belonged to him established his guilt conclusively. The State concedes, as it must, that the search of the purse was unreasonable and in violation of the Fourth Amendment, see <i>Ybarra</i> v. <i>Illinois,</i> <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85</a></span> (1979), and the Court assumes that the detention which led to the search, the seizure, and the admissions also violated the Fourth Amendment, <i>ante,</i> at 106. Nevertheless, the Court upholds the conviction. I dissent.</p>
<p></p>
<h2>I</h2>
<p>The Court holds first that petitioner may not object to the introduction of the pills into evidence because the unconstitutional actions of the police officers did not violate his personal Fourth Amendment rights. To reach this result, the Court holds that the Constitution protects an individual against unreasonable searches and seizures only if he has "a `legitimate expectation of privacy' in the area searched." <i>Ante,</i> at 104. This holding cavalierly rejects the fundamental principle, unquestioned until today, that an interest in either the place searched or the property seized is sufficient to invoke the Constitution's protections against unreasonable searches and seizures.</p>
<p>The Court's examination of previous Fourth Amendment cases begins and endsas it must if it is to reach its desired conclusionwith <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978). Contrary to the Court's assertion, however, <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span></i> did not establish that the Fourth Amendment protects individuals against unreasonable searches and seizures only if they have a privacy interest in the place searched. The question before the Court in <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span></i> was whether the defendants could establish <span class="star-pagination">*115</span> their right to Fourth Amendment protection simply by showing that they were "legitimately on [the] premises" searched, see <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 267</a></span> (1960). Overruling that portion of <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> the Court held that when a Fourth Amendment objection is based on an interest in the place searched, the defendant must show an actual invasion of his personal privacy interest. The petitioners in <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span></i> did not claim that they had standing either under the <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> automatic standing rule for persons charged with possessory offenses, which the Court overrules today, see <i>United States</i> v. <i>Salvucci, ante,</i> p. 83, or because their possessory interest in the items seized gave them "actual standing." No Fourth Amendment claim based on an interest in the property seized was before the Court, and, consequently, the Court did not and could not have decided whether such a claim could be maintained. In fact, the Court expressly disavowed any intention to foreclose such a claim ("This is not to say that such [casual] visitors could not contest the lawfulness of the seizure of evidence or the search if their own property were seized during the search," <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#142" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 142, n. 11</a></span>), and suggested its continuing validity ("[P]etitioners' claims must fail. They asserted neither a property nor a possessory interest in the automobile, <i>nor an interest in the property seized,</i>" <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#148" aria-description="Citation for case: Rakas v. Illinois"><i>id.,</i> at 148</a></span> (emphasis supplied)).</p>
<p>The decision today, then, is not supported by the only case directly cited in its favor.<sup>[*]</sup> Further, the Court has ignored <span class="star-pagination">*116</span> a long tradition embodying the opposite view. <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span> (1951), for example, involved a seizure of contraband alleged to belong to the defendant from a hotel room occupied by his two aunts. The Court rejected the Government's argument that because the search of the room did not invade Jeffers' privacy he lacked standing to suppress the evidence. It held that standing to object to the seizure could not be separated from standing to object to the search, for "[t]he search and seizure are . . . incapable of being untied." <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#52" aria-description="Citation for case: United States v. Jeffers"><i>Id.,</i> at 52</a></span>. The Court then concluded that Jeffers "unquestionably had standing . . . unless the contraband nature of the narcotics seized precluded his assertion, for purposes of the exclusionary rule, of <i>a property interest therein." <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">Ibid.</a></span></i> (emphasis supplied).</p>
<p>Similarly, <i>Jones</i> v. <i>United States, supra</i><i>,</i> is quite plainly premised on the understanding that an interest in the seized property is sufficient to establish that the defendant "himself was the victim of an invasion of privacy." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#261" aria-description="Citation for case: Jones v. United States">362 U. S., at 261</a></span>. The Court observed that the "conventional standing requirement," <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#262" aria-description="Citation for case: Jones v. United States"><i>id.,</i> at 262</a></span>, required the defendant to "claim either to have <i>owned or possessed the seized property</i> or to have had a substantial possessory interest in the premises searched," <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#261" aria-description="Citation for case: Jones v. United States"><i>id.,</i> at 261</a></span> (emphasis supplied). The Court relaxed that rule for defendants charged with possessory offenses because "[t]he same element . . . which has caused a dilemma, <i>i. e.,</i> that <i>possession both convicts and confers standing,</i> eliminates any necessity for a preliminary showing of an interest in the premises searched <i>or the property seized,</i> which ordinarily is <span class="star-pagination">*117</span> required when standing is challenged." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#263" aria-description="Citation for case: Jones v. United States"><i>Id.,</i> at 263</a></span> (emphasis supplied). Instead, "[t]he possession on the basis of which petitioner is to be and was convicted suffices to give him standing," <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#264" aria-description="Citation for case: Jones v. United States"><i>id.,</i> at 264</a></span>.</p>
<p><i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U. S. 377</a></span> (1968), proceeded upon a like understanding. The Court there reiterated that prior to <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> "a defendant who wished to assert a Fourth Amendment objection was required to show that he was the owner or possessor <i>of the seized property</i> or that he had a possessory interest in the searched premises." <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#389" aria-description="Citation for case: Simmons v. United States">390 U. S., at 389-390</a></span> (emphasis supplied). <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> had changed that rule only with respect to defendants charged with possessory offenses, so the defendant Garrett, who was charged with armed robbery, had to establish standing. Because he was not "legitimately on [the] premises" at the time of the search, see <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States"><i>Jones, supra,</i> at 267</a></span>, "[t]he only, or at least the most natural, way in which he could found standing to object to the admission of the suitcase was to testify that he was its owner." <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#391" aria-description="Citation for case: Simmons v. United States">390 U. S., at 391</a></span> (footnote omitted). See also <i>Brown</i> v. <i>United States,</i> <span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/#228" aria-description="Citation for case: Brown v. United States">411 U. S. 223, 228</a></span> (1973); <i>Mancusi</i> v. <i>DeForte,</i> <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#367" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364, 367</a></span> (1968).</p>
<p>The Court's decision today is not wrong, however, simply because it is contrary to our previous cases. It is wrong because it is contrary to the Fourth Amendment, which guarantees that "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated." The Court's reading of the Amendment is far too narrow. The Court misreads the guarantee of security <i>"in</i> their persons, houses, papers, and effects, <i>against</i> unreasonable searches and seizures" to afford protection only against unreasonable searches and seizures <i>of</i> persons and places.</p>
<p>The Fourth Amendment, it seems to me, provides in plain language that if one's security in one's "effects" is disturbed by an unreasonable search and seizure, one has been the victim of a constitutional violation; and so it has always been <span class="star-pagination">*118</span> understood. Therefore the Court's insistence that in order to challenge the legality of the search one must also assert a protected interest in the premises is misplaced. The interest in the item seized is quite enough to establish that the defendant's personal Fourth Amendment rights have been invaded by the government's conduct.</p>
<p>The idea that a person cannot object to a search unless he can show an interest in the premises, even though he is the owner of the seized property, was squarely rejected almost 30 years ago in <i>United States</i> v. <i><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">Jeffers, supra</a></span></i><i>.</i> There the Court stated:</p>
<blockquote>"The Government argues . . . that the search did not invade respondent's privacy and that he, therefore, lacked the necessary standing to suppress the evidence seized. The significant act, it says, is the seizure of the goods of the respondent without a warrant. We do not believe the events are so easily isolable. Rather they are bound together by one sole purposeto locate and seize the narcotics of respondent. The search and seizure are, therefore, incapable of being untied. To hold that this search and seizure were lawful as to the respondent would permit a quibbling distinction to overturn a principle which was designed to protect a fundamental right." <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#52" aria-description="Citation for case: United States v. Jeffers"><i>Id.,</i> at 52</a></span>.</blockquote>
<p>When the government seizes a person's property, it interferes with his constitutionally protected right to be secure in his effects. That interference gives him the right to challenge the reasonableness of the government's conduct, including the seizure. If the defendant's property was seized as the result of an unreasonable search, the seizure cannot be other than unreasonable.</p>
<p>In holding that the Fourth Amendment protects only those with a privacy interest in the place searched, and not those with an ownership or possessory interest in the things seized, the Court has turned the development of the law of search <span class="star-pagination">*119</span> and seizure on its head. The history of the Fourth Amendment shows that it was designed to protect property interests as well as privacy interests; in fact, until <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> the question whether a person's Fourth Amendment rights had been violated turned on whether he had a property interest in the place searched or the items seized. <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> and <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), expanded our view of the protections afforded by the Fourth Amendment by recognizing that privacy interests are protected even if they do not arise from property rights. But that recognition was never intended to exclude interests that had historically been sheltered by the Fourth Amendment from its protection. Neither <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> nor <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> purported to provide an exclusive definition of the interests protected by the Fourth Amendment. Indeed, as <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> recognized: "That Amendment protects individual privacy against certain kinds of governmental intrusion, but its protections go further, and often have nothing to do with privacy at all." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#350" aria-description="Citation for case: Katz v. United States">389 U. S., at 350</a></span>. Those decisions freed Fourth Amendment jurisprudence from the constraints of "subtle distinctions, developed and refined by the common law in evolving the body of private property law which, more than almost any other branch of law, has been shaped by distinctions whose validity is largely historical." <i>Jones,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#266" aria-description="Citation for case: Jones v. United States">362 U. S., at 266</a></span>. Rejection of those finely drawn distinctions as irrelevant to the concerns of the Fourth Amendment did not render property rights wholly outside its protection, however. Not every concept involving property rights, we should remember, is "arcane." Cf. <i>ante,</i> at 105.</p>
<p>In fact, the Court rather inconsistently denies that property rights may, by themselves, entitle one to the protection of the Fourth Amendment, but simultaneously suggests that a person may claim such protection only if his expectation of privacy in the premises searched is so strong that he may exclude all others from that place. See <i>ante,</i> at 105-106; <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#149" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 149</a></span>. Such a harsh threshold requirement <span class="star-pagination">*120</span> was not imposed even in the heyday of a property rights oriented Fourth Amendment.</p>
<p></p>
<h2>II</h2>
<p>Petitioner also contends that his admission of ownership of the drugs should have been suppressed as the fruit of an unlawful detention. The state courts did not pass on that claim, and no factual record was developed which would shed light on the proper disposition of the claim. In such circumstances, it would be appropriate for us to defer to the state court and permit it to make the initial determination. Nevertheless, the majority proceeds to dispose of petitioner's claim by concluding that, even if the detention was illegal, "petitioner's statements were acts of free will unaffected by any illegality in the initial detention." <i>Ante,</i> at 110. I disagree.</p>
<p>Petitioner's admissions, far from being "spontaneous," <i>ante,</i> at 108, were made in response to Vanessa Cox's demand that petitioner "take what was his." In turn, it is plain that her statement was the direct product of the illegal search of her purse. And that search was made possible only because the police refused to let anyone in the house depart unless they "consented" to a body search; that detention the Court has assumed was illegal. Under these circumstances petitioner's admissions were obviously the fruit of the illegal detention and should have been suppressed.</p>
<p></p>
<h2>III</h2>
<p>In the words of Mr. Justice Frankfurter: "A decision [of a Fourth Amendment claim] may turn on whether one gives that Amendment a place second to none in the Bill of Rights, or considers it on the whole a kind of nuisance, a serious impediment in the war against crime." <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#157" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 157</a></span> (1947) (dissenting opinion). Today a majority of the Court has substantially cut back the protection afforded by the Fourth Amendment and the ability of the <span class="star-pagination">*121</span> people to claim that protection, apparently out of concern lest the government's ability to obtain criminal convictions be impeded. A slow and steady erosion of the ability of victims of unconstitutional searches and seizures to obtain a remedy for the invasion of their rights saps the constitutional guarantee of its life just as surely as would a substantive limitation. Because we are called on to decide whether evidence should be excluded only when a search has been "successful," it is easy to forget that the standards we announce determine what government conduct is reasonable in searches and seizures directed at persons who turn out to be innocent as well as those who are guilty. I continue to believe that ungrudging application of the Fourth Amendment is indispensable to preserving the liberties of a democratic society. Accordingly, I dissent.</p>
<h2>NOTES</h2>
<p>[1]  At petitioner's trial, Vanessa Cox described the transfer of possession quite differently. She testified that, as she and petitioner were getting ready to leave the house, petitioner asked "would you please carry this for me" and simultaneously dumped the drugs into her purse. According to Cox, she looked into her purse, saw the drugs, and said "would you please take this, I do not want this in my purse." Petitioner allegedly replied "okay, just a minute, I will," and then went out of the room. At that point the police entered the house. Tr. 12-14. David Saddler, who was in the next room at the time of the transfer, corroborated Cox's version of the events, testifying that he heard Cox say "I do not want this in my purse" and that he heard petitioner reply "don't worry" or something to that effect. <i>Id.,</i> at 100.
</p>
<p>Although none of the lower courts specifically found that Cox did not consent to the bailment, the trial court clearly was skeptical about petitioner's version of events:</p>
<p>"The Court finds it unbelievable that just of his own volition, David Rawlings put the contraband in the purse of Mrs. Cox just a minute before the officers knocked on the door. He had been carrying these things around Bowling Green in a bank deposit sack for days, either on his person or in his pocket, and it is unworthy of belief that just immediately before the officers knocked on the door that he put them in the purse of Vanessa Cox. It is far more plausible to believe that he saw the officers pull up out front and then elected to `push them off' on Vanessa Cox, believing that search was probable, possible, and emminent [<i>sic</i>]." App. 21.</p>
<p>[2]  Petitioner also claims that he is entitled to "automatic standing" to contest the legality of the search that uncovered the drugs. See <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960). Our decision today in <i>United States</i> v. <i>Salvucci, ante,</i> p. 83, disposes of this contention adversely to him.</p>
<p>[3]  Under questioning by his own counsel, petitioner testified as follows:
</p>
<p>"Q72 Did you feel that Vannessa [<i>sic</i>] Cox's purse would be free from the intrusion of the officers as you sat there? When you put the pills in her purse, did you feel that they would be free from governmental intrusion?</p>
<p>"A No sir." App. 48.</p>
<p>The trial court also credited this statement, noting immediately:</p>
<p>"You know what, I believe this boy tells the truth. You all wanted to bring him in here before the Court, and he said, `no, I want a jury.' He said `no, I don't understand that.' And I don't blame him for not understanding that. That's the first time I've ever seen such a thing brought on before this Court, and I've been here for quite a few years as an attorney, of course.</p>
<p>"Now, no question but what the boy fully understood what was meant by that. None at all in the Court's mind. If you want to go ahead, you can do so." <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Ibid.</a></span></i></p>
<p>[4]  But see n. 1, <i>supra.</i></p>
<p>[5]  "The reasonableness of seizures that are less intrusive than a traditional arrest, see <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#209" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 209-210</a></span> (1979); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20</a></span> (1968), depends `on a balance between the public interest and the individual's right to personal security free from arbitrary interference by law officers.' <i>Pennsylvania</i> v. <i>Mimms,</i> <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#109" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 109</a></span> (1977); <i>United States</i> v. <i>Brignoni-Ponce,</i> [<span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975)]. Consideration of the constitutionality of such seizures involves a weighing of the gravity of the public concerns served by the seizure, the degree to which the seizure advances the public interest, and the severity of the interference with individual liberty." <i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#50" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 50-51</a></span> (1979).</p>
<p>[6]  The fruits of the search of petitioner's person were, of course, not necessary to support probable cause to arrest petitioner.</p>
<p>[*]  The Court invites the reader to "contrast" <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960), which it expressly overrules, and to "see" <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#389" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 389-390</a></span> (1968). <i>Ante,</i> at 105, 104. The passage cited in <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> contains the following language: "At one time, a defendant who wished to assert a Fourth Amendment objection was required to show that he was the owner or possessor <i>of the seized property</i> or that he had a possessory interest in the searched premises." <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#389" aria-description="Citation for case: Simmons v. United States">390 U. S., at 389-390</a></span> (emphasis supplied). The Court in <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> then observed that <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> had "relaxed" those standing requirements by holding that in a case charging a possessory offense "the Government is precluded from denying that the defendant has the requisite possessory interest to challenge the admission of the evidence. . . ." <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#390" aria-description="Citation for case: Simmons v. United States">390 U. S., at 390</a></span>. The Court also "contrasts" two other cases in connection with its subsidiary point that a "bailment" that is "precipitous" may not be enough to show that a person "took normal precautions to maintain his privacy." <i>Ante,</i> at 105. The Court also cites <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), as the source of the phrase "legitimate expectation of privacy." But <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> did not purport to restrict the interest protected by the Fourth Amendment, see <i>infra,</i> at 119-120.</p>

</div>
```

---

## GROUP: content/cases/Richards v. Wisconsin.md  (`case`, 5 assertions)

### content_page

```
---
title: "Richards v. Wisconsin"
type: case
citation: "520 U.S. 385 (1997)"
parallel_cite: "117 S. Ct. 1416; 137 L. Ed. 2d 615"
neutral_cite: 1997 U.S. LEXIS 2794
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1997
date_decided: 1997-04-28
docket: 96-5955
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1997-04-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Richards v. Wisconsin
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118103/richards-v-wisconsin/"
  cluster_id: 118103
  opinion_id: 118103
  identity_checked: true
homes:
  - page: "[[Knock-and-Announce]]"
    role: "Key — Progeny / Refinement"
related: ["[[Wilson v. Arkansas]]", "[[Hudson v. Michigan]]", "[[Maryland v. Buie]]"]
aliases: []
tags: ["case", "fourth-amendment", "knock-and-announce", "no-knock", "reasonable-suspicion", "warrant-execution"]
holding: "There is **no blanket exception** to knock-and-announce for entire categories of crime (e.g., felony drug cases); the no-knock decision…"
lake:
  record_id: Richards v. Wisconsin
  status: verified
  projected_at: 2026-07-06
---

# Richards v. Wisconsin

*520 U.S. 385 (1997)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers had a warrant to search Richards's motel room for drugs (the magistrate had deleted no-knock authorization). An officer posing as a maintenance man knocked; Richards opened the door, saw a uniformed officer, and quickly closed it. The officers then forced entry without further announcement and found drugs and cash. The Wisconsin Supreme Court upheld the entry under a blanket rule that police need never knock and announce when executing a warrant in a felony drug investigation.

## Issue
Whether the Fourth Amendment permits a blanket exception to the [[Knock-and-Announce|knock-and-announce]] requirement for an entire category of crime — all felony drug investigations.

## Rule
No blanket exception. "[T]he fact that felony drug investigations may frequently present circumstances warranting a no-knock entry cannot remove from the neutral scrutiny of a reviewing court the reasonableness of the police decision not to knock and announce in a particular case." — 520 U.S. at 394. ^pin-394

"In order to justify a 'no-knock' entry, the police must have a reasonable suspicion that knocking and announcing their presence, under the particular circumstances, would be dangerous or futile, or that it would inhibit the effective investigation of the crime by, for example, allowing the destruction of evidence." — 520 U.S. at 394. ^pin-394a

## Application
Rejecting Wisconsin's blanket rule, the Court nonetheless held the no-knock entry into Richards's room was reasonable on these facts: once Richards opened the door, recognized the police, and slammed it, the officers had reasonable suspicion that he would destroy the easily disposable drugs if they paused to announce. The magistrate's deletion of no-knock authority did not control, because reasonableness is judged as of the moment of entry.

## Conclusion
There is no blanket [[Knock-and-Announce|knock-and-announce]] exception for drug cases; case-specific reasonable suspicion is required, and it was present here, so the entry was upheld and the judgment affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Richards* refines the [[Knock-and-Announce|knock-and-announce]] rule of [[Wilson v. Arkansas]]; suppression for a [[Knock-and-Announce|knock-and-announce]] violation was later denied in [[Hudson v. Michigan]].

## Appears on
- [[Knock-and-Announce]] — *Key — Progeny / Refinement*

## Sources
- *Richards v. Wisconsin*, 520 U.S. 385 (1997) — https://www.courtlistener.com/opinion/118103/richards-v-wisconsin/ — pinpoint: 394.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "58e31ef339b6ad30", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "520 U.S. 385 (1997)", "court": "U.S. Supreme Court", "neutral_cite": "1997 U.S. LEXIS 2794", "official_citation_present": true, "parallel_cite": "117 S. Ct. 1416; 137 L. Ed. 2d 615", "title": "Richards v. Wisconsin", "year": "1997"}}
{"assertion_id": "043aa1a4a8430336", "dimension": "support", "kind": "home_role", "locator": {"home": "Knock-and-Announce"}, "payload": {"home": "Knock-and-Announce", "role": "Key — Progeny / Refinement", "title": "Richards v. Wisconsin"}}
{"assertion_id": "f65cca3b75579469", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "There is **no blanket exception** to knock-and-announce for entire categories of crime (e.g., felony drug cases); the no-knock decision…", "title": "Richards v. Wisconsin"}}
{"assertion_id": "30a6b9fc61c99cb1", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Richards v. Wisconsin"}}
{"assertion_id": "33f9f414e9d28c10", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1997-04-28", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Richards v. Wisconsin", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Richards v. Wisconsin", "varies_by_point": "false"}}
```

### lake record — Richards v. Wisconsin

```json
{
  "schema_version": "s2.v1",
  "record_id": "Richards v. Wisconsin",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Richards v. Wisconsin",
    "case_name_short": "Richards",
    "case_name_full": "Richards v. Wisconsin",
    "input_case_name": "Richards v. Wisconsin",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1997-04-28",
    "year": 1997,
    "docket": "96-5955",
    "cluster_id": 118103,
    "lead_opinion_id": 118103,
    "sibling_ids": [
      118103
    ],
    "absolute_url": "/opinion/118103/richards-v-wisconsin/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9163841,
        "score": 20,
        "case_name": "Richards v. Wisconsin"
      },
      {
        "cluster_id": 9163840,
        "score": 20,
        "case_name": "Richards v. Wisconsin"
      },
      {
        "cluster_id": 9162684,
        "score": 20,
        "case_name": "Richards v. Wisconsin"
      },
      {
        "cluster_id": 9162683,
        "score": 20,
        "case_name": "Richards v. Wisconsin"
      },
      {
        "cluster_id": 9284920,
        "score": 20,
        "case_name": "Richards v. Wisconsin"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "520 U.S. 385",
      "volume": "520",
      "reporter": "U.S.",
      "page": "385",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "117 S. Ct. 1416",
        "volume": "117",
        "reporter": "S. Ct.",
        "page": "1416",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 L. Ed. 2d 615",
        "volume": "137",
        "reporter": "L. Ed. 2d",
        "page": "615",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1997 U.S. LEXIS 2794",
        "volume": "1997",
        "reporter": "U.S. LEXIS",
        "page": "2794",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "520 U.S. 385",
        "volume": "520",
        "reporter": "U.S.",
        "page": "385",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "117 S. Ct. 1416",
        "volume": "117",
        "reporter": "S. Ct.",
        "page": "1416",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 L. Ed. 2d 615",
        "volume": "137",
        "reporter": "L. Ed. 2d",
        "page": "615",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1997 U.S. LEXIS 2794",
        "volume": "1997",
        "reporter": "U.S. LEXIS",
        "page": "2794",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "520 U.S. 385",
    "official_selection": {
      "court_class": "scotus",
      "selected": "520 U.S. 385",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-394",
      "page": null,
      "quote": "--- # Richards v. Wisconsin *520 U.S. 385 (1997)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers had a warrant to search Richards's motel room for drugs (the magistrate had deleted no-knock authorization). An officer posing as a maintenance man knocked; Richards opened the door, saw a uniformed officer, and quickly closed it. The officers then forced entry without further announcement and found drugs and cash. The Wisconsin Supreme Court upheld the entry under a blanket rule that police need never knock and announce when executing a warrant in a felony drug investigation. ## Issue Whether the Fourth Amendment permits a blanket exception to the knock-and-announce requirement for an entire category of crime \u2014 all felony drug investigations. ## Rule No blanket exception.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-394a",
      "page": null,
      "quote": "In order to justify a 'no-knock' entry, the police must have a reasonable suspicion that knocking and announcing their presence, under the particular circumstances, would be dangerous or futile, or that it would inhibit the effective investigation of the crime by, for example, allowing the destruction of evidence.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1997-04-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Richards v. Wisconsin",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. McCarthy",
          "cluster_id": 10160868,
          "cite": [
            "369 Or. 129",
            "501 P.3d 478"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Harte v. Board Comm'rs Cnty of Johnson",
          "cluster_id": 4411980,
          "cite": [
            "864 F.3d 1154",
            "2017 WL 3138494"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "James Sunny Burton v. State",
          "cluster_id": 3092638,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Foster",
          "cluster_id": 835141,
          "cite": [
            "217 P.3d 168",
            "347 Or. 1",
            "2009 Ore. LEXIS 223"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gilbert, 06ca3055 (5-30-2007)",
          "cluster_id": 4021002,
          "cite": [
            "2007 Ohio 2717"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dennis Russell Callaghan",
          "cluster_id": 2933574,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
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
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Singleton",
          "cluster_id": 793669,
          "cite": [
            "441 F.3d 290",
            "2006 U.S. App. LEXIS 7201",
            "2006 WL 724800"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Richard J. Rizzi",
          "cluster_id": 792946,
          "cite": [
            "434 F.3d 669",
            "2006 U.S. App. LEXIS 450",
            "2006 WL 39266"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Flores v. State",
          "cluster_id": 1790339,
          "cite": [
            "177 S.W.3d 8"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Missouri v. McNeely",
          "cluster_id": 858288,
          "cite": [
            "185 L. Ed. 2d 696",
            "133 S. Ct. 1552",
            "569 U.S. 141",
            "2013 U.S. LEXIS 3160",
            "81 U.S.L.W. 4250",
            "24 Fla. L. Weekly Fed. S 150",
            "2013 WL 1628934"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. JL",
          "cluster_id": 118352,
          "cite": [
            "146 L. Ed. 2d 254",
            "120 S. Ct. 1375",
            "529 U.S. 266",
            "2000 U.S. LEXIS 2345",
            "13 Fla. L. Weekly Fed. S 216",
            "68 U.S.L.W. 4236",
            "2000 Cal. Daily Op. Serv. 2409",
            "2000 Colo. J. C.A.R. 1642",
            "2000 Daily Journal DAR 3226"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Henning",
          "cluster_id": 1060855,
          "cite": [
            "975 S.W.2d 290",
            "1998 Tenn. LEXIS 370",
            "1998 WL 324318"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ramirez",
          "cluster_id": 118180,
          "cite": [
            "140 L. Ed. 2d 191",
            "118 S. Ct. 992",
            "523 U.S. 65",
            "1998 U.S. LEXIS 1600"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Fields Christopher Crawley",
          "cluster_id": 740479,
          "cite": [
            "113 F.3d 313",
            "1997 U.S. App. LEXIS 10728"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Zhahir",
          "cluster_id": 2196510,
          "cite": [
            "751 A.2d 1153",
            "561 Pa. 545",
            "2000 Pa. LEXIS 1245"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bravo v. City of Santa Maria",
          "cluster_id": 618647,
          "cite": [
            "665 F.3d 1076",
            "101 A.L.R. 6th 615",
            "2011 U.S. App. LEXIS 24383",
            "2011 WL 6117918"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Quinn v. Jesus Guerrero",
          "cluster_id": 4407590,
          "cite": [
            "863 F.3d 353",
            "2017 WL 2951586",
            "2017 U.S. App. LEXIS 12290"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Willie Jacobs and Linda Siller v. City of Chicago , a Municipal Corporation the Estate of Sergeant Michael Garner Officers Quintero, Buckner, McLean Keith, and Garrido and Metropolitan Enforcement Group Officers Huff, Martin, Sowinski, and McIntyre",
          "cluster_id": 769087,
          "cite": [
            "215 F.3d 758",
            "46 Fed. R. Serv. 3d 832",
            "2000 U.S. App. LEXIS 12013"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kelly Donald Gould",
          "cluster_id": 785789,
          "cite": [
            "364 F.3d 578",
            "2004 U.S. App. LEXIS 5505",
            "2004 WL 576173"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adcock v. Commonwealth",
          "cluster_id": 2433405,
          "cite": [
            "967 S.W.2d 6",
            "1998 Ky. LEXIS 59",
            "1998 WL 178596"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Nordstrom",
          "cluster_id": 2587271,
          "cite": [
            "25 P.3d 717",
            "200 Ariz. 229",
            "350 Ariz. Adv. Rep. 16",
            "2001 Ariz. LEXIS 89"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118103) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTA4MzM5MjAwMDAwJnM9MTU0NzY1NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118103%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118103)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NSZzPTIwMzYwMzgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118103%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118103)",
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
    "complete_query": "cites:(118103)",
    "indexed_citing_opinions": 584,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118103,
        "count": 584,
        "count_source": "search"
      }
    ],
    "citation_count": 959,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/richards-v-wisconsin.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY3NDA1MDgmcz00NzQ3Mzk3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118103%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118103,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 112384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 112873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 1124319,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 1504743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 1632862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 1677415,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 2032318,
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
    "date_created": "2026-07-05T17:29:24Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:30:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:30:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:33:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:30:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Richards v. Wisconsin

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b479-5">
  Justice Stevens
 </author>
<p id="AAd">
  delivered the opinion of the Court.
 </p>
<p id="b479-6">
  In
  <em>
   Wilson
  </em>
  v.
  <em>
   Arkansas,
  </em>
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927</a></span> (1995), we held that the Fourth Amendment incorporates the common-law requirement that police officers entering a dwelling must knock on the door and announce their identity and purpose before attempting forcible entry. At the same time, we recognized that the “flexible requirement of reasonableness should not be read to mandate a rigid rule of announcement that ignores countervailing law enforcement interests,”
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#934" aria-description="Citation for case: Wilson v. Arkansas"><em>
   id.,
  </em>
  at 934</a></span>, and left “to the lower courts the task of determining the circumstances under which an unannounced entry is reasonable under the Fourth Amendment,”
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#936" aria-description="Citation for case: Wilson v. Arkansas"><em>
   id.,
  </em>
  at 936</a></span>.
 </p>
<p id="b479-7">
  In this case, the Wisconsin Supreme Court concluded that police officers are
  <em>
   never
  </em>
  required to knock and announce their presence when executing a search warrant in a felony
  <span citation-index="1" class="star-pagination" label="388"> 
   *388
   </span>
  drug investigation. In so doing, it reaffirmed a
  <em>
   pre-Wilson
  </em>
  holding and concluded that
  <em>
   <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>
  </em>
  did not preclude this
  <em>
   per se
  </em>
  rule. We disagree with the court’s conclusion that the Fourth Amendment permits a blanket exception to the knock-and-announce requirement for this entire category of criminal activity. But because the evidence presented to support the officers’ actions in this case establishes that the decision not to knock and announce was a reasonable one under the circumstances, we affirm the judgment of the Wisconsin court.
 </p>
<p id="b480-5">
  I
 </p>
<p id="b480-6">
  On December 31, 1991, police officers in Madison, Wisconsin, obtained a warrant to search Steiney Richards’ motel room for drugs and related paraphernalia. The search warrant was the culmination of an investigation that had uncovered substantial evidence that Richards was one of several individuals dealing drugs out of hotel rooms in Madison. The police requested a warrant that would have given advance authorization for a “no-knock” entry into the motel room, but the Magistrate explicitly deleted those portions of the warrant. App. 7, 9.
 </p>
<p id="b480-7">
  The officers arrived at the motel room at 3:40 a.m. Officer Pharo, dressed as a maintenance man, led the team. With him were several plainclothes officers and at least one man in uniform. Officer Pharo knocked on Richards’ door and, responding to the query from inside the room, stated that he was a maintenance man. With the chain still on the door, Richards cracked it open. Although there is some dispute as to what occurred next, Richards acknowledges that when he opened the door he saw the man in uniform standing behind Officer Pharo. Brief for Petitioner 6. He quickly slammed the door closed and, after waiting two or three seconds, the officers began kicking and ramming the door to gain entry to the locked room. At trial, the officers testified that they identified themselves as police while they were kicking the door in. App. 40. When they finally did break
  <span citation-index="1" class="star-pagination" label="389"> 
   *389
   </span>
  into the room, the officers caught Richards trying to escape through the window. They also found cash and cocaine hidden in plastic bags above the bathroom ceiling tiles.
 </p>
<p id="b481-5">
  Richards sought to have the evidence from his motel room suppressed on the ground that the officers had failed to knock and announce their presence prior to forcing entry into the room. The trial court denied the motion, concluding that the officers could gather from Richards’ strange behavior when they first sought entry that he knew they were police officers and that he might try to destroy evidence or to escape.
  <em>
   Id.,
  </em>
  at 54. The judge emphasized that the easily disposable nature of the drugs the police were searching for further justified their decision to identify themselves as they crossed the threshold instead of announcing their presence before seeking entry.
  <em>
   Id.,
  </em>
  at 55. Richards appealed the decision to the Wisconsin Supreme Court and that court affirmed. <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/" aria-description="Citation for case: State v. Richards">201 Wis. 2d 845</a></span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/" aria-description="Citation for case: State v. Richards">549 N. W. 2d 218</a></span> (1996).
 </p>
<p id="b481-6">
  The Wisconsin Supreme Court did not delve into the events underlying Richards’ arrest in any detail, but accepted the following facts: “[0]n December 31, 1991, police executed a search warrant for the motel room of the defendant seeking evidence of the felonious crime of Possession with Intent to Deliver a Controlled Substance in violation of <span class="citation no-link">Wis. Stat. § 161.41</span>(lm) (1991-92). They did not knock and announce prior to their entry. Drugs were seized.”
  <span class="citation no-link"><em>
   Id.,
  </em>
  at 849</span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#220" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 220</a></span>.
 </p>
<p id="b481-7">
  Assuming these facts, the court proceeded to consider whether our decision in
  <em>
   <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>
  </em>
  required the court to abandon its decision in
  <em>
   State
  </em>
  v.
  <em>
   Stevens,
  </em>
  <span class="citation" data-id="9668150"><a href="/opinion/1677415/state-v-stevens/" aria-description="Citation for case: State v. Stevens">181 Wis. 2d 410</a></span>, <span class="citation" data-id="9668150"><a href="/opinion/1677415/state-v-stevens/" aria-description="Citation for case: State v. Stevens">511 N. W. 2d 591</a></span> (1994), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./515/1102/">515 U. S. 1102</a></span> (1995), which held that “when the police have a search warrant, supported by probable cause, to search a residence for evidence of delivery of drugs or evidence of possession with intent to deliver drugs, they necessarily have reasonable cause to believe exigent circumstances exist” to justify a no-knock entry. <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#852" aria-description="Citation for case: State v. Richards">201 Wis. 2d, at 852</a></span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#221" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 221</a></span>. The court concluded
  <span citation-index="1" class="star-pagination" label="390"> 
   *390
   </span>
  that nothing in
  <em>
   Wilson’s
  </em>
  acknowledgment that the knock- and-announce rule was an element of the Fourth Amendment “reasonableness” requirement would prohibit application of a
  <em>
   per se
  </em>
  exception to that rule in a category of cases. <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#854" aria-description="Citation for case: State v. Richards">201 Wis. 2d, at 854-855</a></span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#220" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 220</a></span>.
 </p>
<p id="b482-5">
  In reaching this conclusion, the Wisconsin court found it reasonable — after considering criminal conduct surveys, newspaper articles, and other judicial opinions — to assume that all felony drug crimes will involve “an extremely high risk of serious if not deadly injury to the police as well as the potential for the disposal of drugs by the occupants prior to entry by the police.”
  <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#847" aria-description="Citation for case: State v. Richards"><em>
   Id.,
  </em>
  at 847-848</a></span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#219" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 219</a></span>. Notwithstanding its acknowledgment that in “some cases, police officers will undoubtedly decide that their safety, the safety of others, and the effective execution of the warrant dictate that they knock and announce,”
  <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#863" aria-description="Citation for case: State v. Richards"><em>
   id.,
  </em>
  at 863</a></span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#225" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 225</a></span>, the court concluded that exigent circumstances justifying a no-knock entry are always present in felony drug cases. Further, the court reasoned that the violation of privacy that occurs when officers who have a search warrant forcibly enter a residence without first announcing their presence is minimal, given that the residents would ultimately be without authority to refuse the police entry. The principal intrusion on individual privacy interests in such a situation, the court concluded, comes from the issuance of the search warrant, not the manner in which it is executed.
  <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#864" aria-description="Citation for case: State v. Richards"><em>
   Id.,
  </em>
  at 864-865</a></span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#226" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 226</a></span>. Accordingly, the court determined that police in Wisconsin do not need specific information about dangerousness, or the possible destruction of drugs in a particular case, in order to dispense with the knock-and-announce requirement in felony drug cases.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
</p>
<p id="b483-7">
<span citation-index="1" class="star-pagination" label="391"> 
   *391
   </span>
  Justice Abrahamson concurred in the judgment because, in her view, the facts found by the trial judge justified a no-knock entry.
  <em>
   Id,.,
  </em>
  at 866-868, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#227" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 227</a></span>. Specifically, she noted that Richards’ actions in slamming the door when he saw the uniformed man standing behind Officer Pharo indicated that he already knew that the people knocking on his door were police officers. Under these circumstances, any further announcement of their presence would have been a useless gesture.
  <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#868" aria-description="Citation for case: State v. Richards"><em>
   Id.,
  </em>
  at 868-869, n. 3</a></span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#228" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 228, n. 3</a></span>. While agreeing with the outcome, Justice Abrahamson took issue with her colleagues’ affirmation of the blanket exception to the knock-and-announce requirement in drug felony cases. She observed that the constitutional reasonableness of a search has generally been a matter left to the court, rather than to the officers who conducted the search, and she objected to the creation of a blanket rule that insulated searches in a particular category of crime from the neutral oversight of a reviewing judge.
  <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#868" aria-description="Citation for case: State v. Richards"><em>
   Id.,
  </em>
  at 868-875</a></span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#228" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 228-230</a></span>.
 </p>
<p id="AxNk">
  II
 </p>
<p id="Ahtv">
  We recognized in
  <em>
   <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>
  </em>
  that the knock-and-announce requirement could give way “under circumstances presenting a threat of physical violence,” or “where police officers have reason to believe that evidence would likely be destroyed if advance notice were given.” <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#936" aria-description="Citation for case: Wilson v. Arkansas">514 U. S., at 936</a></span>. It is indisputable that felony drug investigations may frequently involve both of these circumstances.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  The question we must
  <span citation-index="1" class="star-pagination" label="392"> 
   *392
   </span>
  resolve is whether this fact justifies dispensing with case-by-case evaluation of the manner in which a search was executed.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b484-5">
  The Wisconsin court explained its blanket exception as necessitated by the special circumstances of today’s drug culture, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#863" aria-description="Citation for case: State v. Richards">201 Wis. 2d, at 863-866</a></span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#226" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 226-227</a></span>, and the State asserted at oral argument that the blanket exception was reasonable in “felony drug cases because of the convergence in a violent and dangerous form of commerce of weapons and the destruction of drugs.” Tr. of Oral Arg. 26. But creating exceptions to the knock-and-announce rule based on the “culture” surrounding a general category of criminal behavior presents at least two serious concerns.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
</p>
<p id="b485-4">
<span citation-index="1" class="star-pagination" label="393"> 
   *393
   </span>
  First, the exception contains considerable overgeneralization. For example, while drug investigation frequently does pose special risks to officer safety and the preservation of evidence, not every drug investigation will pose these risks to a substantial degree. For example, a search could be conducted at a time when the only individuals present in a residence have no connection with the drug activity and thus will be unlikely to threaten officers or destroy evidence. Or the police could know that the drugs being searched for were of a type or in a location that made them impossible to destroy quickly. In those situations, the asserted governmental interests in preserving evidence and maintaining safety may not outweigh the individual privacy interests intruded upon by a no-knock entry.
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  Wisconsin’s blanket rule imper-missibly insulates these cases from judicial review.
 </p>
<p id="b485-5">
  A second difficulty with permitting a criminal-category exception to the knock-and-announce requirement is that the
  <span citation-index="1" class="star-pagination" label="394"> 
   *394
   </span>
  reasons for creating an exception in one category can, relatively easily, be applied to others. Armed bank robbers, for example, are, by definition, likely to have weapons, and the fruits of their crime may be destroyed without too much difficulty. If a
  <em>
   per se
  </em>
  exception were allowed for each category of criminal investigation that included a considerable — albeit hypothetical — risk of danger to officers or destruction of evidence, the knock-and-announce element of the Fourth Amendment’s reasonableness requirement would be meaningless.
 </p>
<p id="b486-4">
  Thus, the fact that felony drug investigations may frequently present circumstances warranting a no-knock entry cannot remove from the neutral scrutiny of a reviewing court the reasonableness of the police decision not to knock and announce in a particular case. Instead, in each case, it is the duty of a court confronted with the question to determine whether the facts and circumstances of the particular entry justified dispensing with the knock-and-announce requirement.
 </p>
<p id="b486-5">
  In order to justify a “no-knock” entry, the police must have a reasonable suspicion that knocking and announcing their presence, under the particular circumstances, would be dangerous or futile, or that it would inhibit the effective investigation of the crime by, for example, allowing the destruction of evidence. This standard — as opposed to a probable-cause requirement — strikes the appropriate balance between the legitimate law enforcement concerns at issue in the execution of search warrants and the individual privacy interests affected by no-knock entries. Cf.
  <em>
   Maryland
  </em>
  v.
  <em>
   Buie,
  </em>
  <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#337" aria-description="Citation for case: Maryland v. Buie">494 U. S. 325, 337</a></span> (1990) (allowing a protective sweep of a house during an arrest where the officers have “a reasonable belief based on specific and articulable facts that the area to be swept harbors an individual posing a danger to those on the arrest scene”);
  <em>
   Terry
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 30</a></span> (1968) (requiring a reasonable and articulable suspicion of danger to justify a patdown search). This showing is not high, but the police
  <span citation-index="1" class="star-pagination" label="395"> 
   *395
   </span>
  should be required to make it whenever the reasonableness of a no-knock entry is challenged.
 </p>
<p id="b487-5">
  III
 </p>
<p id="b487-6">
  Although we reject the Wisconsin court’s blanket exception to the knock-and-announce requirement, we conclude that the officers’ no-knock entry into Richards’ motel room did not violate the Fourth Amendment. We agree with the trial court, and with Justice Abrahamson, that the circumstances in this case show that the officers had a reasonable suspicion that Richards might destroy evidence if given further opportunity to do so.
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
</p>
<p id="b487-7">
  The judge who heard testimony at Richards’ suppression hearing concluded that it was reasonable for the officers executing the warrant to believe that Richards knew, after opening the door to his motel room the first time, that the men seeking entry to his room were the police. App. 54. Once the officers reasonably believed that Richards knew who they were, the court concluded, it was reasonable for them to force entry immediately given the disposable nature of the drugs.
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#55" aria-description="Citation for case: Terry v. Ohio"><em>
   Id.,
  </em>
  at 55</a></span>.
 </p>
<p id="b487-8">
  In arguing that the officers’ entry was unreasonable, Richards places great emphasis on the fact that the Magistrate who signed the search warrant for his motel room deleted the portions of the proposed warrant that would have given the officers permission to execute a no-knock entry. But this fact does not alter the reasonableness of the officers’ decision, which must be evaluated as of the time they entered the motel room. At the time the officers obtained the warrant, they did not have evidence sufficient, in the judgment of the Magistrate, to justify a no-knock warrant. Of course,
  <span citation-index="1" class="star-pagination" label="396"> 
   *396
   </span>
  the Magistrate could not have anticipated in every particular the circumstances that would confront the officers when they arrived at Richards’ motel room.
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  These actual circumstances — petitioner’s apparent recognition of the officers combined with the easily disposable nature of the drugs— justified the officers’ ultimate decision to enter without first announcing their presence and authority.
 </p>
<p id="b488-5">
  Accordingly, although we reject the blanket exception to the knock-and-announce requirement for felony drug investigations, the judgment of the Wisconsin Supreme Court is affirmed.
 </p>
<p id="b488-6">
<em>
   It is so ordered.
  </em>
</p>







<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b482-6">
   Several other state courts — in eases that predate our decision in
   <em>
    <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>
   </em>
   — have adopted similar rules, concluding that simple probable cause to search a home for narcotics always allows the police to forgo the knock- and-announce requirement. See, e.
   <em>
    g., People
   </em>
   v.
   <em>
    Lujan,
   </em>
   <span class="citation" data-id="1185551"><a href="/opinion/1185551/people-v-lujan/#1241" aria-description="Citation for case: People v. Lujan">484 P. 2d 1238, 1241</a></span> (Colo. 1971) (en banc);
   <em>
    Henson
   </em>
   v.
   <em>
    State,
   </em>
   <span class="citation no-link">236 Md. 519</span>, 523-524, 204 A.
   <span citation-index="1" class="star-pagination" label="391"> 
    *391
    </span>
   2d 516, 519-520 (1964);
   <em>
    State
   </em>
   v.
   <em>
    Loucks,
   </em>
   <span class="citation" data-id="1632862"><a href="/opinion/1632862/state-v-loucks/#777" aria-description="Citation for case: State v. Loucks">209 N. W. 2d 772, 777-778</a></span> (N. D. 1973). Cf.
   <em>
    People
   </em>
   v.
   <em>
    De Lago,
   </em>
   16 N. Y. 2d 289, 292, <span class="citation" data-id="5522059"><a href="/opinion/5674482/people-v-de-lago/#661" aria-description="Citation for case: People v. De Lago">213 N. E. 2d 659, 661</a></span> (1965) (similar rule for searches related to gambling operations), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./383/963/">383 U. S. 963</a></span> (1966).
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b483-5">
   This Court has encountered before the links between drugs and violence, see,
   <em>
    e. g., Michigan
   </em>
   v.
   <em>
    Summers,
   </em>
   <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 702</a></span> (1981), and the likelihood that drug dealers will attempt to dispose of drugs before police seize them, see,
   <em>
    e. g., Ker
   </em>
   v.
   <em>
    California,
   </em>
   <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#28" aria-description="Citation for case: Ker v. California">374 U. S. 23, 28, n. 3</a></span> (1963).
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b484-6">
   Although our decision in
   <em>
    <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>
   </em>
   did not address this issue directly, it is instructive that in that case — which involved a felony drug investigation — we remanded to the state court for further factual development to determine whether the no-knock entry was reasonable under the circumstances of the case. Two
   <em>
    amicus
   </em>
   briefs in
   <em>
    <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>
   </em>
   suggested that we adopt just the sort of
   <em>
    per se
   </em>
   rule the Wisconsin court propounded here. Brief for Americans for Effective Law Enforcement, Inc., et al. as
   <em>
    Amici Curiae
   </em>
   10-11, Brief for Wayne County, Michigan, as
   <em>
    Amicus Curiae
   </em>
   39-46, in
   <em>
    Wilson
   </em>
   v.
   <em>
    Arkansas, O.
   </em>
   T. 1994, No. 5707. Although the respondent did not argue for a categorical rule, the petitioner, in her reply brief, did address the arguments put forward by the
   <em>
    dmicus
   </em>
   briefs, Reply Brief for Petitioner in
   <em>
    Wilson
   </em>
   v.
   <em>
    <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Arkansas</a></span>,
   </em>
   O. T. 1994, No. 5707, p. 11, and
   <em>
    amici
   </em>
   supporting the petitioner also presented arguments against a categorical rule. Brief for American Civil Liberties Union et al. as
   <em>
    Amici Curiae
   </em>
   in
   <em>
    Wilson
   </em>
   v.
   <em>
    <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Arkansas</a></span>,
   </em>
   O. T. 1994, No. 5707, p. 29, n. 44. Thus, while the prospect of a categorical rule was one to which we were alerted in
   <em>
    <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>,
   </em>
   we did not choose to adopt such a rule at that time.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b484-9">
   It is always somewhat dangerous to ground exceptions to constitutional protections in the social norms of a given historical moment. The purpose of the Fourth Amendment’s requirement of reasonableness “is to preserve that degree of respect for the privacy of persons and the inviolability of their property that existed when the provision was adopted — even if a later, less virtuous age should become accustomed to considering all sorts of intrusion ‘reasonable.’”
   <em>
    Minnesota
   </em>
   v.
   <em>
    Dickerson,
   </em>
   <span class="citation" data-id="9432823"><a href="/opinion/112873/minnesota-v-dickerson/#380" aria-description="Citation for case: Minnesota v. Dickerson">508 U. S. 366, 380</a></span> (1993) (Scalia, J,, concurring).
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b485-6">
   The State asserts that the intrusion on individual interests effectuated by a no-knock entry is minimal because the execution of the warrant itself constitutes the primary intrusion on individual privacy and that the individual privacy interest cannot outweigh the generalized governmental interest in effective and safe law enforcement. Brief for Respondent 21-24. See also Brief for United States as
   <em>
    Amicus Curiae
   </em>
   16 (“occupants’ privacy interest is necessarily limited to the brief interval between the officers’ announcement and their entry”). While it is true that a no-knoek entry is less intrusive than, for example, a warrantless search, the individual interests implicated by an unannounced, forcible entry should not be unduly minimized. As we observed in
   <em>
    Wilson
   </em>
   v.
   <em>
    Arkansas,
   </em>
   <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#930" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927, 930-932</a></span> (1995), the common law recognized that individuals should be provided the opportunity to comply with the law and to avoid the destruction of property occasioned by a forcible entry. These interests are not inconsequential.
  </p>
<p id="b485-7">
   Additionally, when police enter a residence without announcing their presence, the residents are not given any opportunity to prepare themselves for such an entry. The State pointed out at oral argument that, in Wisconsin, most search warrants are executed during the late night and early morning hours. Tr. of Oral Arg. 24. The brief interlude between announcement and entry with a warrant may be the opportunity that an individual has to pull on clothes or get out of bed.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b487-9">
   We note that the attorneys general of 26 States, the Commonwealth of Puerto Rico, and the Territory of Guam filed an
   <em>
    amicus
   </em>
   brief taking the position that the officers’ decision was reasonable under the specific facts of this ease, but rejecting Wisconsin’s
   <em>
    per se
   </em>
   rule. See Brief for Ohio et al. as
   <em>
    Amici Curiae.
   </em>
</p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b488-7">
   A number of States give magistrate judges the authority to issue “no-knoek” warrants if the officers demonstrate ahead of time a reasonable suspicion that entry without prior announcement will be appropriate in a particular context. See,
   <em>
    e. g.,
   </em>
   725 Ill. Comp. Stat., eh. 725, § 5/108-8 (1992); <span class="citation no-link">Neb. Rev. Stat. §29-411</span> (1995); Okla. Stat., Tit. 22, §1228 (Supp. 1997); S. D. Codified Laws §23A-35-9 (1988); <span class="citation no-link">Utah Code Ann. § 77-23-210</span> (1995). But see
   <em>
    State
   </em>
   v.
   <em>
    Arce,
   </em>
   <span class="citation" data-id="9529581"><a href="/opinion/1118987/state-v-arce/" aria-description="Citation for case: State v. Arce">83 Ore. App. 185</a></span>, <span class="citation" data-id="9529581"><a href="/opinion/1118987/state-v-arce/" aria-description="Citation for case: State v. Arce">730 P. 2d 1260</a></span> (1986) (magistrate has no authority to abrogate knock-and-announce requirement);
   <em>
    State
   </em>
   v.
   <em>
    Bamber,
   </em>
   <span class="citation" data-id="1124319"><a href="/opinion/1124319/state-v-bamber/" aria-description="Citation for case: State v. Bamber">630 So. 2d 1048</a></span> (Fla. 1994) (same).
  </p>
<p id="b488-8">
   The practice of allowing magistrates to issue no-knock warrants seems entirely reasonable when sufficient cause to do so can be demonstrated ahead of time. But, as the facts of this case demonstrate, a magistrate’s decision not to authorize a no-knoek entry should not be interpreted to remove the officers’ authority to exercise independent judgment concerning the wisdom of a no-knock entry at the time the warrant is being executed.
  </p>
</div></div></opinion>
```

---
