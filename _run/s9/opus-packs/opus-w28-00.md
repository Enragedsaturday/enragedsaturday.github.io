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

## GROUP: content/cases/Brosseau v. Haugen.md  (`case`, 6 assertions)

### content_page

```
---
title: "Brosseau v. Haugen"
type: case
citation: "543 U.S. 194 (2004)"
parallel_cite: "125 S. Ct. 596; 160 L. Ed. 2d 583"
neutral_cite: 2004 U.S. LEXIS 8275
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-12-13
docket: 03-1261
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2004-12-13
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Brosseau v. Haugen
  varies_by_point: false
  scope_note: "Good law (per curiam). The leading specificity case for qualified immunity in the use-of-force setting: Graham and Garner are 'cast at a high level of generality' and rarely clearly establish the answer in a particular shooting; repeatedly reaffirmed (e.g. Mullenix v. Luna, Kisela v. Hughes)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/137736/brosseau-v-haugen/"
  cluster_id: 137736
  opinion_id: 137736
  identity_checked: true
homes:
  - page: "[[Use of Force]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Qualified Immunity]]"
    role: "Related (cross-doctrine)"
related: ["[[Tennessee v. Garner]]", "[[Graham v. Connor]]", "[[Mullenix v. Luna]]", "[[Kisela v. Hughes]]", "[[Plumhoff v. Rickard]]"]
aliases: []
tags: ["case", "use-of-force", "deadly-force", "qualified-immunity", "section-1983", "clearly-established-law", "fleeing-suspect"]
holding: "Officer Brosseau was entitled to qualified immunity for shooting a fleeing suspect in a vehicle: Garner and Graham are cast at too high a level of generality to clearly establish that the shooting was unlawful, and the handful of relevant fact-specific cases placed her conduct in the 'hazy border between excessive and acceptable force.'"
lake:
  record_id: Brosseau v. Haugen
  status: verified
  projected_at: 2026-07-06
---

# Brosseau v. Haugen

*543 U.S. 194 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officer Rochelle Brosseau of the Puyallup, Washington, police responded to a report of a fight at Kenneth Haugen's mother's house; Haugen had a felony no-bail warrant. After a foot search, Haugen jumped into his Jeep, locked the door, and ignored Brosseau's commands to get out. Brosseau broke the driver's window with her handgun and struck him, but Haugen started the Jeep. As it began to move — with another officer on foot, occupied vehicles nearby, and a girlfriend and child in a car in the driveway — Brosseau fired one shot through the rear window, hitting Haugen in the back. He survived, pleaded guilty to felony "eluding," and sued under § 1983 for excessive force.

## Issue
Whether Officer Brosseau was entitled to [[Qualified Immunity|qualified immunity]] on the excessive-force claim — i.e., whether it was clearly established that shooting a fleeing suspect in these circumstances violated the Fourth Amendment.

## Rule
[[Qualified Immunity|Qualified immunity]] protects an officer who reasonably misjudges an unsettled legal question. "Qualified immunity shields an officer from suit when she makes a decision that, even if constitutionally deficient, reasonably misapprehends the law governing the circumstances she confronted." — 543 U.S. at 198. ^pin-198

The clearly-established inquiry must be particularized, not abstract. "*Graham* and *Garner*, following the lead of the Fourth Amendment's text, are cast at a high level of generality." — 543 U.S. at 199. ^pin-199

Those general standards "clearly establish" the answer only "in an obvious case … even without a body of relevant case law." — *Id.*

The fact-specific precedent did not place the question beyond debate. The relevant cases "taken together undoubtedly show that this area is one in which the result depends very much on the facts of each case. None of them squarely governs the case here; they do suggest that Brosseau's actions fell in the '"hazy border between excessive and acceptable force."'" — 543 U.S. at 201. ^pin-201

Accordingly, "[t]he cases by no means 'clearly establish' that Brosseau's conduct violated the Fourth Amendment." — *Id.* ^pin-201b

## Application
The Court took the facts in the light most favorable to Haugen and expressed no view on whether the shooting actually violated the Fourth Amendment; it resolved the case on the second, qualified-immunity step alone. Measured at the proper level of specificity — whether to shoot "a disturbed felon, set on avoiding capture through vehicular flight, when persons in the immediate area are at risk from that flight" — only a "handful" of lower-court decisions spoke to the situation, and they pointed in different directions (*Cole v. Bone* and *Smith v. Freland* finding no violation; *Estate of Starks v. Enyart* finding a jury question). Because that body of law did not give Brosseau fair notice that her single shot was unlawful, her conduct fell in the hazy border the doctrine protects, and she was entitled to [[Qualified Immunity|qualified immunity]].

## Conclusion
Reversed. The Ninth Circuit erred on [[Qualified Immunity|qualified immunity]]; Brosseau was entitled to it because the law did not clearly establish that her shooting of the fleeing Haugen violated the Fourth Amendment.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- *Brosseau* is the foundational reminder that excessive-force [[Qualified Immunity|qualified immunity]] is judged at a high level of specificity: the general reasonableness tests of [[Graham v. Connor]] and [[Tennessee v. Garner]] rarely "clearly establish" the answer in a particular shooting. The Court has reaffirmed and applied it repeatedly — [[Mullenix v. Luna]] and [[Kisela v. Hughes]] both rely on *Brosseau*, and [[Plumhoff v. Rickard]] cited it for the proposition that no clearly established law forbade the officers' conduct. No negative treatment.

## Appears on
- [[Use of Force]] — *Key — Progeny / Refinement*
- [[Section 1983 Liability and Qualified Immunity]] — *Related (cross-doctrine)*

## Sources
- *Brosseau v. Haugen*, 543 U.S. 194 (2004) (per curiam) — https://www.courtlistener.com/opinion/137736/brosseau-v-haugen/ — pinpoints: 198, 199, 201.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "04a5eff5ffe34f72", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "543 U.S. 194 (2004)", "court": "U.S. Supreme Court", "neutral_cite": "2004 U.S. LEXIS 8275", "official_citation_present": true, "parallel_cite": "125 S. Ct. 596; 160 L. Ed. 2d 583", "title": "Brosseau v. Haugen", "year": "2004"}}
{"assertion_id": "0eb7c057ff305d2f", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Related (cross-doctrine)", "title": "Brosseau v. Haugen"}}
{"assertion_id": "9acb1813ca50be73", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Officer Brosseau was entitled to qualified immunity for shooting a fleeing suspect in a vehicle: Garner and Graham are cast at too high a level of generality to clearly establish that the shooting was unlawful, and the handful of relevant fact-specific cases placed her conduct in the 'hazy border between excessive and acceptable force.'", "title": "Brosseau v. Haugen"}}
{"assertion_id": "ffedffb7173b429e", "dimension": "support", "kind": "home_role", "locator": {"home": "Use of Force"}, "payload": {"home": "Use of Force", "role": "Key — Progeny / Refinement", "title": "Brosseau v. Haugen"}}
{"assertion_id": "442e6213111971f6", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Brosseau v. Haugen"}}
{"assertion_id": "bc28fa6452994330", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2004-12-13", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Brosseau v. Haugen", "field_i_validity": "good_law", "scope_note": "Good law (per curiam). The leading specificity case for qualified immunity in the use-of-force setting: Graham and Garner are 'cast at a high level of generality' and rarely clearly establish the answer in a particular shooting; repeatedly reaffirmed (e.g. Mullenix v. Luna, Kisela v. Hughes).", "title": "Brosseau v. Haugen", "varies_by_point": "false"}}
```

### lake record — Brosseau v. Haugen

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brosseau v. Haugen",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Brosseau v. Haugen",
    "case_name_short": "Brosseau",
    "case_name_full": "Brosseau v. Haugen",
    "input_case_name": "Brosseau v. Haugen",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-12-13",
    "year": 2004,
    "docket": "03-1261",
    "cluster_id": 137736,
    "lead_opinion_id": 137736,
    "sibling_ids": [
      137736,
      9434715,
      9434716,
      9434717
    ],
    "absolute_url": "/opinion/137736/brosseau-v-haugen/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "543 U.S. 194",
      "volume": "543",
      "reporter": "U.S.",
      "page": "194",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "125 S. Ct. 596",
        "volume": "125",
        "reporter": "S. Ct.",
        "page": "596",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "160 L. Ed. 2d 583",
        "volume": "160",
        "reporter": "L. Ed. 2d",
        "page": "583",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 8275",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "8275",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "543 U.S. 194",
        "volume": "543",
        "reporter": "U.S.",
        "page": "194",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "125 S. Ct. 596",
        "volume": "125",
        "reporter": "S. Ct.",
        "page": "596",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "160 L. Ed. 2d 583",
        "volume": "160",
        "reporter": "L. Ed. 2d",
        "page": "583",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 8275",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "8275",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "543 U.S. 194",
    "official_selection": {
      "court_class": "scotus",
      "selected": "543 U.S. 194",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-198",
      "page": null,
      "quote": "and sued under \u00a7 1983 for excessive force. ## Issue Whether Officer Brosseau was entitled to qualified immunity on the excessive-force claim \u2014 i.e., whether it was clearly established that shooting a fleeing suspect in these circumstances violated the Fourth Amendment. ## Rule Qualified immunity protects an officer who reasonably misjudges an unsettled legal question.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-199",
      "page": null,
      "quote": "*Graham* and *Garner*, following the lead of the Fourth Amendment's text, are cast at a high level of generality.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-201",
      "page": null,
      "quote": "\u2014 *Id.* The fact-specific precedent did not place the question beyond debate. The relevant cases",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-201b",
      "page": null,
      "quote": "[t]he cases by no means 'clearly establish' that Brosseau's conduct violated the Fourth Amendment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2004-12-13",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Brosseau v. Haugen",
    "varies_by_point": false,
    "scope_note": "Good law (per curiam). The leading specificity case for qualified immunity in the use-of-force setting: Graham and Garner are 'cast at a high level of generality' and rarely clearly establish the answer in a particular shooting; repeatedly reaffirmed (e.g. Mullenix v. Luna, Kisela v. Hughes).",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
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
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tolan v. Cotton",
          "cluster_id": 2672535,
          "cite": [
            "188 L. Ed. 2d 895",
            "134 S. Ct. 1861",
            "2014 U.S. LEXIS 3112",
            "82 U.S.L.W. 4358",
            "572 U.S. 650",
            "88 Fed. R. Serv. 3d 765",
            "24 Fla. L. Weekly Fed. S 731",
            "2014 WL 1757856"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
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
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reichle v. Howards",
          "cluster_id": 801500,
          "cite": [
            "182 L. Ed. 2d 985",
            "132 S. Ct. 2088",
            "566 U.S. 658",
            "2012 U.S. LEXIS 4132"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
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
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "White v. Pauly",
          "cluster_id": 4374579,
          "cite": [
            "580 U.S. 73",
            "196 L. Ed. 2d 463",
            "2017 U.S. LEXIS 5",
            "137 S. Ct. 548",
            "26 Fla. L. Weekly Fed. S 409",
            "85 U.S.L.W. 4027",
            "2017 WL 69170"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460854,
          "cite": [
            "583 U.S. 48",
            "138 S. Ct. 577",
            "199 L. Ed. 2d 453",
            "2018 U.S. LEXIS 760"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kisela v. Hughes",
          "cluster_id": 4482892,
          "cite": [
            "584 U.S. 100",
            "138 S. Ct. 1148",
            "200 L. Ed. 2d 449",
            "2018 U.S. LEXIS 2066"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Plumhoff v. Rickard",
          "cluster_id": 2675750,
          "cite": [
            "188 L. Ed. 2d 1056",
            "134 S. Ct. 2012",
            "2014 U.S. LEXIS 3816",
            "82 U.S.L.W. 4394",
            "572 U.S. 765",
            "24 Fla. L. Weekly Fed. S 790",
            "2014 WL 2178335"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crawford v. Metropolitan Government of Nashville and Davidson Cty.",
          "cluster_id": 145915,
          "cite": [
            "172 L. Ed. 2d 650",
            "129 S. Ct. 846",
            "555 U.S. 271",
            "2009 U.S. LEXIS 870",
            "21 Fla. L. Weekly Fed. S 609",
            "77 U.S.L.W. 4093",
            "91 Empl. Prac. Dec. (CCH) 43,434",
            "105 Fair Empl. Prac. Cas. (BNA) 353"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Goebert v. Lee County",
          "cluster_id": 77881,
          "cite": [
            "510 F.3d 1312",
            "2007 U.S. App. LEXIS 29513",
            "2007 WL 4458122"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Laura Skop v. City of Atlanta, Georgia",
          "cluster_id": 77695,
          "cite": [
            "485 F.3d 1130",
            "2007 U.S. App. LEXIS 10341",
            "2007 WL 1288012"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilkie v. Robbins",
          "cluster_id": 145705,
          "cite": [
            "168 L. Ed. 2d 389",
            "127 S. Ct. 2588",
            "551 U.S. 537",
            "2007 U.S. LEXIS 8513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460811,
          "cite": [
            "583 U.S. 48"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patrick Booker v. South Carolina Department of Corrections",
          "cluster_id": 4387227,
          "cite": [
            "855 F.3d 533",
            "2017 WL 1531576",
            "2017 U.S. App. LEXIS 7563"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Deville v. Marcantel",
          "cluster_id": 65780,
          "cite": [
            "567 F.3d 156",
            "2009 U.S. App. LEXIS 9403",
            "2009 WL 1162586"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morgan v. Swanson",
          "cluster_id": 8441074,
          "cite": [
            "659 F.3d 359",
            "2011 U.S. App. LEXIS 19656",
            "2011 WL 4470233"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Iqbal v. Hasty",
          "cluster_id": 2716,
          "cite": [
            "490 F.3d 143"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cindy Abbott v. Sangamon County",
          "cluster_id": 816250,
          "cite": [
            "705 F.3d 706",
            "2013 WL 322920",
            "2013 U.S. App. LEXIS 1963"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ellen Keates v. Michael Koile",
          "cluster_id": 4474827,
          "cite": [
            "883 F.3d 1228"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roe v. Elyea",
          "cluster_id": 183790,
          "cite": [
            "631 F.3d 843",
            "78 Fed. R. Serv. 3d 874",
            "2011 U.S. App. LEXIS 1781",
            "2011 WL 256978"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maldonado v. Fontanes",
          "cluster_id": 203857,
          "cite": [
            "568 F.3d 263",
            "2009 U.S. App. LEXIS 12716",
            "2009 WL 1547737"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Victoria Zetwick v. County of Yolo",
          "cluster_id": 4370725,
          "cite": [
            "850 F.3d 436",
            "2017 WL 710476",
            "2017 U.S. App. LEXIS 3260",
            "101 Empl. Prac. Dec. (CCH) 45,744",
            "129 Fair Empl. Prac. Cas. (BNA) 1657"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
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
        "journal_ref": "Brosseau v. Haugen:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(137736 OR 9434715 OR 9434716 OR 9434717) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTk3MzYzMjAwMDAwJnM9NDc3NTMxOCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28137736+OR+9434715+OR+9434716+OR+9434717%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(137736 OR 9434715 OR 9434716 OR 9434717)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNjUmcz0yMDkyJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28137736+OR+9434715+OR+9434716+OR+9434717%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(137736 OR 9434715 OR 9434716 OR 9434717)",
        "reviewed": 105,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 105,
        "triage_read": 0,
        "triage_snippet_classified": 105
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(137736 OR 9434715 OR 9434716 OR 9434717)",
    "indexed_citing_opinions": 1039,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 137736,
        "count": 743,
        "count_source": "search"
      },
      {
        "opinion_id": 9434715,
        "count": 312,
        "count_source": "search"
      },
      {
        "opinion_id": 9434716,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434717,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2766,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/brosseau-v-haugen.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyOTAwNjYmcz0xMDM3MzA2NCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28137736+OR+9434715+OR+9434716+OR+9434717%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 137736,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 112594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 112671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 118098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 121169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 136067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 541812,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 576267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 607163,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 652953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 765106,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 765160,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 767897,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 776968,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 783116,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137736,
        "cited_id": 784483,
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
    "date_created": "2026-07-04T20:37:54Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:38:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:38:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:41:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:38:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Brosseau v. Haugen

```
<div>
<center><b><span class="citation" data-id="9434715"><a href="/opinion/137736/brosseau-v-haugen/" aria-description="Citation for case: Brosseau v. Haugen">543 U.S. 194</a></span> (2004)</b></center>
<center><h1>BROSSEAU<br>
v.<br>
HAUGEN</h1></center>
<center>No. 03-1261.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Decided December 13, 2004.</center>
ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p>PER CURIAM.</p>
<p>Officer Rochelle Brosseau, a member of the Puyallup, Washington, Police Department, shot Kenneth Haugen in the back as he attempted to flee from law enforcement authorities in his vehicle. Haugen subsequently filed this action in the United States District Court for the Western District of <span class="star-pagination">*195</span> Washington pursuant to Rev. Stat. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>. He alleged that the shot fired by Brosseau constituted excessive force and violated his federal constitutional rights.<sup>[1]</sup> The District Court granted summary judgment to Brosseau after finding she was entitled to qualified immunity. The Court of Appeals for the Ninth Circuit reversed. <span class="citation" data-id="9496321"><a href="/opinion/783116/kenneth-j-haugen-v-rochelle-brosseau-puyallup-police-department-the-city/" aria-description="Citation for case: Kenneth J. Haugen v. Rochelle Brosseau, Puyallup Police...">339 F. 3d 857</a></span> (2003). Following the two-step process set out in <i>Saucier</i> v. <i>Katz,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./533/194/">533 U. S. 194</a></span> (2001), the Court of Appeals found, first, that Brosseau had violated Haugen's Fourth Amendment right to be free from excessive force and, second, that the right violated was clearly established and thus Brosseau was not entitled to qualified immunity. Brosseau then petitioned for writ of certiorari, requesting that we review both of the Court of Appeals' determinations. We grant the petition on the second, qualified immunity question and reverse.</p>
<p>The material facts, construed in a light most favorable to Haugen, are as follows.<sup>[2]</sup> On the day before the fracas, Glen Tamburello went to the police station and reported to Brosseau that Haugen, a former crime partner of his, had stolen tools from his shop. Brosseau later learned that there was a felony no-bail warrant out for Haugen's arrest on drug and other offenses. The next morning, Haugen was spray painting his Jeep Cherokee in his mother's driveway. Tamburello learned of Haugen's whereabouts, and he and cohort Matt Atwood drove a pickup truck to Haugen's mother's house to pay Haugen a visit. A fight ensued, which was witnessed by a neighbor who called 911.</p>
<p>Brosseau heard a report that the men were fighting in Haugen's mother's yard and responded. When she arrived, Tamburello and Atwood were attempting to get Haugen into <span class="star-pagination">*196</span> Tamburello's pickup. Brosseau's arrival created a distraction, which provided Haugen the opportunity to get away. Haugen ran through his mother's yard and hid in the neighborhood. Brosseau requested assistance, and, shortly thereafter, two officers arrived with a K-9 to help track Haugen down. During the search, which lasted about 30 to 45 minutes, officers instructed Tamburello and Atwood to remain in Tamburello's pickup. They instructed Deanna Nocera, Haugen's girlfriend who was also present with her 3-year-old daughter, to remain in her small car with her daughter. Tamburello's pickup was parked in the street in front of the driveway; Nocera's small car was parked in the driveway in front of and facing the Jeep; and the Jeep was in the driveway facing Nocera's car and angled somewhat to the left. The Jeep was parked about 4 feet away from Nocera's car and 20 to 30 feet away from Tamburello's pickup.</p>
<p>An officer radioed from down the street that a neighbor had seen a man in her backyard. Brosseau ran in that direction, and Haugen appeared. He ran past the front of his mother's house and then turned and ran into the driveway. With Brosseau still in pursuit, he jumped into the driver's side of the Jeep and closed and locked the door. Brosseau believed that he was running to the Jeep to retrieve a weapon.</p>
<p>Brosseau arrived at the Jeep, pointed her gun at Haugen, and ordered him to get out of the vehicle. Haugen ignored her command and continued to look for the keys so he could get the Jeep started. Brosseau repeated her commands and hit the driver's side window several times with her handgun, which failed to deter Haugen. On the third or fourth try, the window shattered. Brosseau unsuccessfully attempted to grab the keys and struck Haugen on the head with the barrel and butt of her gun. Haugen, still undeterred, succeeded in starting the Jeep. As the Jeep started or shortly after it began to move, Brosseau jumped back and to the left. She fired one shot through the rear driver's side window <span class="star-pagination">*197</span> at a forward angle, hitting Haugen in the back. She later explained that she shot Haugen because she was "`fearful for the other officers on foot who [she] believed were in the immediate area, [and] for the occupied vehicles in [Haugen's] path and for any other citizens who might be in the area.'" <span class="citation" data-id="9496321"><a href="/opinion/783116/kenneth-j-haugen-v-rochelle-brosseau-puyallup-police-department-the-city/#865" aria-description="Citation for case: Kenneth J. Haugen v. Rochelle Brosseau, Puyallup Police...">339 F. 3d, at 865</a></span>.</p>
<p>Despite being hit, Haugen, in his words, "`st[ood] on the gas'"; navigated the "`small, tight space'" to avoid the other vehicles; swerved across the neighbor's lawn; and continued down the street. <span class="citation" data-id="9496321"><a href="/opinion/783116/kenneth-j-haugen-v-rochelle-brosseau-puyallup-police-department-the-city/#882" aria-description="Citation for case: Kenneth J. Haugen v. Rochelle Brosseau, Puyallup Police..."><i>Id.,</i> at 882</a></span>. After about a half block, Haugen realized that he had been shot and brought the Jeep to a halt. He suffered a collapsed lung and was airlifted to a hospital. He survived the shooting and subsequently pleaded guilty to the felony of "eluding." <span class="citation no-link">Wash. Rev. Code § 46.61.024</span> (1994). By so pleading, he admitted that he drove his Jeep in a manner indicating "a wanton or wilful disregard for the lives . . . of others." <i><span class="citation no-link">Ibid.</span></i> He subsequently brought this § 1983 action against Brosseau.</p>
<p></p>
<h2>*  *  *</h2>
<p>When confronted with a claim of qualified immunity, a court must ask first the following question: "Taken in the light most favorable to the party asserting the injury, do the facts alleged show the officer's conduct violated a constitutional right?" <i>Saucier</i> v. <i>Katz,</i> 533 U. S., at 201. As the Court of Appeals recognized, the constitutional question in this case is governed by the principles enunciated in <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985), and <i>Graham</i> v. <i>Connor,</i> <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U. S. 386</a></span> (1989). These cases establish that claims of excessive force are to be judged under the Fourth Amendment's "`objective reasonableness'" standard. <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#388" aria-description="Citation for case: Graham v. Connor"><i>Id.,</i> at 388</a></span>. Specifically with regard to deadly force, we explained in <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span></i> that it is unreasonable for an officer to "seize an unarmed, nondangerous suspect by shooting him dead." <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#11" aria-description="Citation for case: Tennessee v. Garner">471 U. S., at 11</a></span>. But "[w]here the officer has probable cause to believe that the suspect poses a threat of serious physical <span class="star-pagination">*198</span> harm, either to the officer or to others, it is not constitutionally unreasonable to prevent escape by using deadly force." <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Ibid.</a></span></i></p>
<p>We express no view as to the correctness of the Court of Appeals' decision on the constitutional question itself. We believe that, however that question is decided, the Court of Appeals was wrong on the issue of qualified immunity.<sup>[3]</sup></p>
<p>Qualified immunity shields an officer from suit when she makes a decision that, even if constitutionally deficient, reasonably misapprehends the law governing the circumstances she confronted. <i>Saucier</i> v. <i>Katz,</i> 533 U.S., at 206 (qualified immunity operates "to protect officers from the sometimes `hazy border between excessive and acceptable force'"). Because the focus is on whether the officer had fair notice that her conduct was unlawful, reasonableness is judged against the backdrop of the law at the time of the conduct. If the law at that time did not clearly establish that the officer's conduct would violate the Constitution, the officer should not be subject to liability or, indeed, even the burdens of litigation.</p>
<p>It is important to emphasize that this inquiry "must be undertaken in light of the specific context of the case, not as a broad general proposition." <i>Id.,</i> at 201. As we previously said in this very context:</p>
<blockquote>"[T]here is no doubt that <i>Graham</i> v. <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Connor, supra</a></span></i><i>,</i> clearly establishes the general proposition that use of force is contrary to the Fourth Amendment if it is excessive under objective standards of reasonableness. Yet that is not enough. Rather, we emphasized in <i>Anderson</i> [v. <i>Creighton</i>] `that the right the official is alleged to have violated must have been "clearly established" in <span class="star-pagination">*199</span> a more particularized, and hence more relevant, sense: The contours of the right must be sufficiently clear that a reasonable official would understand that what he is doing violates that right.' 483 U.S. [635,] 640 [(1987)]. The relevant, dispositive inquiry in determining whether a right is clearly established is whether it would be clear to a reasonable officer that his conduct was unlawful in the situation he confronted." <i>Id.,</i> at 201-202.</blockquote>
<p>The Court of Appeals acknowledged this statement of law, but then proceeded to find fair warning in the general tests set out in <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i> and <i>Garner.</i> <span class="citation" data-id="9496321"><a href="/opinion/783116/kenneth-j-haugen-v-rochelle-brosseau-puyallup-police-department-the-city/#873" aria-description="Citation for case: Kenneth J. Haugen v. Rochelle Brosseau, Puyallup Police...">339 F.3d, at 873-874</a></span>. In so doing, it was mistaken. <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i> and <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span>,</i> following the lead of the Fourth Amendment's text, are cast at a high level of generality. See <i>Graham</i> v. <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor"><i>Connor, supra,</i> at 396</a></span> ("`[T]he test of reasonableness under the Fourth Amendment is not capable of precise definition or mechanical application'"). Of course, in an obvious case, these standards can "clearly establish" the answer, even without a body of relevant case law. See <i>Hope</i> v. <i>Pelzer,</i> <span class="citation" data-id="9434318"><a href="/opinion/121169/hope-v-pelzer/#738" aria-description="Citation for case: Hope v. Pelzer">536 U.S. 730, 738</a></span> (2002) (noting in a case where the Eighth Amendment violation was "obvious" that there need not be a materially similar case for the right to be clearly established). See also <i>Pace</i> v. <i>Capobianco,</i> <span class="citation" data-id="7009807"><a href="/opinion/7103965/pace-v-capobianco/#1283" aria-description="Citation for case: Pace v. Capobianco">283 F.3d 1275, 1283</a></span> (CA11 2002) (explaining in a Fourth Amendment case involving an officer shooting a fleeing suspect in a vehicle that, "when we look at decisions such as <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span></i> and <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span>,</i> we see some tests to guide us in determining the law in many different kinds of circumstances; but we do not see the kind of clear law (clear answers) that would apply" to the situation at hand). The present case is far from the obvious one where <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i> and <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span></i> alone offer a basis for decision.</p>
<p>We therefore turn to ask whether, at the time of Brosseau's actions, it was "`"clearly established"'" in this more "`particularized'" sense that she was violating Haugen's Fourth Amendment right. <i>Saucier</i> v. <i>Katz,</i> 533 U.S., at <span class="star-pagination">*200</span> 202. The parties point us to only a handful of cases relevant to the "situation [Brosseau] confronted": whether to shoot a disturbed felon, set on avoiding capture through vehicular flight, when persons in the immediate area are at risk from that flight.<sup>[4]</sup><i>Ibid.</i> Specifically, Brosseau points us to <i>Cole</i> v. <i>Bone,</i> <span class="citation" data-id="9010890"><a href="/opinion/9017761/cole-v-bone/" aria-description="Citation for case: Cole v. Bone">993 F. 2d 1328</a></span> (CA8 1993), and <i>Smith</i> v. <i>Freland,</i> <span class="citation" data-id="576267"><a href="/opinion/576267/patricia-smith-individually-and-as-administratrix-of-the-estate-of-brent/" aria-description="Citation for case: Patricia Smith, Individually and as Administratrix of the...">954 F. 2d 343</a></span> (CA6 1992).</p>
<p>In these cases, the courts found no Fourth Amendment violation when an officer shot a fleeing suspect who presented a risk to others. <i>Cole</i> v. <span class="citation" data-id="9010890"><a href="/opinion/9017761/cole-v-bone/#1333" aria-description="Citation for case: Cole v. Bone"><i>Bone, supra,</i> at 1333</a></span> (holding the officer "had probable cause to believe that the truck posed an imminent threat of serious physical harm to innocent motorists as well as to the officers themselves"); <i>Smith</i> v. <i>Freland,</i> <span class="citation" data-id="576267"><a href="/opinion/576267/patricia-smith-individually-and-as-administratrix-of-the-estate-of-brent/#347" aria-description="Citation for case: Patricia Smith, Individually and as Administratrix of the...">954 F. 2d, at 347</a></span> (noting "a car can be a deadly weapon" and holding the officer's decision to stop the car from possibly injuring others was reasonable). <i><span class="citation" data-id="576267"><a href="/opinion/576267/patricia-smith-individually-and-as-administratrix-of-the-estate-of-brent/" aria-description="Citation for case: Patricia Smith, Individually and as Administratrix of the...">Smith</a></span></i> is closer to this case. There, the officer and suspect engaged in a car chase, which appeared to be at an end when the officer cornered the suspect at the back of a dead-end residential street. The suspect, however, freed his car and began speeding down the street. At this point, the officer fired a shot, which killed the suspect. The court held the officer's decision was reasonable and thus did not violate the Fourth Amendment. It noted that the suspect, like Haugen here, "had proven he would do almost anything to avoid capture" and that he posed a major threat to, among others, the officers at the end of the street. <i><span class="citation" data-id="576267"><a href="/opinion/576267/patricia-smith-individually-and-as-administratrix-of-the-estate-of-brent/" aria-description="Citation for case: Patricia Smith, Individually and as Administratrix of the...">Ibid.</a></span></i></p>
<p><span class="star-pagination">*201</span> Haugen points us to <i>Estate of Starks</i> v. <i>Enyart,</i> <span class="citation" data-id="6928206"><a href="/opinion/7026598/estate-of-starks-v-enyart/" aria-description="Citation for case: Estate of Starks v. Enyart">5 F. 3d 230</a></span> (CA7 1993), where the court found summary judgment inappropriate on a Fourth Amendment claim involving a fleeing suspect. There, the court concluded that the threat created by the fleeing suspect's failure to brake when an officer suddenly stepped in front of his just-started car was not a sufficiently grave threat to justify the use of deadly force. <span class="citation" data-id="6928206"><a href="/opinion/7026598/estate-of-starks-v-enyart/#234" aria-description="Citation for case: Estate of Starks v. Enyart"><i>Id.,</i> at 234</a></span>.</p>
<p>These three cases taken together undoubtedly show that this area is one in which the result depends very much on the facts of each case. None of them squarely governs the case here; they do suggest that Brosseau's actions fell in the "`hazy border between excessive and acceptable force.'" <i>Saucier</i> v. <i>Katz, supra,</i> at 206. The cases by no means "clearly establish" that Brosseau's conduct violated the Fourth Amendment.</p>
<p>The judgment of the United States Court of Appeals for the Ninth Circuit is therefore reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE BREYER, with whom JUSTICE SCALIA and JUSTICE GINSBURG join, concurring.</p>
<p>I join the Court's opinion but write separately to express my concern about the matter to which the Court refers in footnote 3, namely, the way in which lower courts are required to evaluate claims of qualified immunity under the Court's decision in <i>Saucier</i> v. <i>Katz,</i> <span class="citation multiple-matches"><a href="/c/U.S./533/194/">533 U.S. 194</a></span>, 201 (2001). As the Court notes, <i>ante,</i> at 198, n. 3, <i>Saucier</i> requires lower courts to decide (1) the constitutional question prior to deciding (2) the qualified immunity question. I am concerned that the current rule rigidly requires courts unnecessarily to decide difficult constitutional questions when there is available an easier basis for the decision (<i>e. g.,</i> qualified immunity) that will satisfactorily resolve the case before the court. Indeed when courts' dockets are crowded, a rigid "order of <span class="star-pagination">*202</span> battle" makes little administrative sense and can sometimes lead to a constitutional decision that is effectively insulated from review, see <i>Bunting</i> v. <i>Mellen,</i> <span class="citation" data-id="9434630"><a href="/opinion/136067/bunting-v-mellen/#1025" aria-description="Citation for case: Bunting v. Mellen">541 U. S. 1019, 1025</a></span> (2004) (SCALIA, J., dissenting from denial of certiorari). For these reasons, I think we should reconsider this issue.</p>
<p>JUSTICE STEVENS, dissenting.</p>
<p>In my judgment, the answer to the constitutional question presented by this case is clear: Under the Fourth Amendment, it was objectively unreasonable for Officer Brosseau to use deadly force against Kenneth Haugen in an attempt to prevent his escape. What is not clear is whether Brosseau is nonetheless entitled to qualified immunity because it might not have been apparent to a reasonably well-trained officer in Brosseau's shoes that killing Haugen to prevent his escape was unconstitutional. In my opinion that question should be answered by a jury.</p>
<p></p>
<h2>I</h2>
<p>Law enforcement officers should never be subject to damages liability for failing to anticipate novel developments in constitutional law. Accordingly, whenever a suit against an officer is based on the alleged violation of a constitutional right that has not been clearly established, the qualified immunity defense is available. <i>Harlow</i> v. <i>Fitzgerald,</i> <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 818</a></span> (1982). Prompt dismissal of such actions protects officers from unnecessary litigation and accords with this Court's wise "policy of avoiding the unnecessary adjudication of constitutional questions." <i>County of Sacramento</i> v. <i>Lewis,</i> <span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/#859" aria-description="Citation for case: County of Sacramento v. Lewis">523 U.S. 833, 859</a></span> (1998) (STEVENS, J., concurring in judgment). When, however, the applicable constitutional rule is well settled, "we should address the constitutional question at the outset." <i>Ibid.;</i> see also <i>Siegert</i> v. <i>Gilley,</i> <span class="citation" data-id="9432276"><a href="/opinion/112594/siegert-v-gilley/" aria-description="Citation for case: Siegert v. Gilley">500 U. S. 226</a></span> (1991). The constitutional limits on the use of deadly force have been clearly established for almost two decades.</p>
<p><span class="star-pagination">*203</span> In 1985, we held that the killing of an unarmed burglar to prevent his escape was an unconstitutional seizure. <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span>. We considered, and rejected, the State's contention that the Fourth Amendment's prohibition against unreasonable seizures should be construed in light of the common-law rule, which allowed the use of whatever force was necessary to effectuate the arrest of a fleeing felon. <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#12" aria-description="Citation for case: Tennessee v. Garner"><i>Id.,</i> at 12-13</a></span>. We recognized that the common-law rule had been fashioned "when virtually all felonies were punishable by death" and long before guns were available to the police, and noted that modern police departments in a majority of large cities allowed the firing of a weapon only when a felon presented a threat of death or serious bodily harm. <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#13" aria-description="Citation for case: Tennessee v. Garner"><i>Id.,</i> at 13-19</a></span>. We concluded that "changes in the legal and technological context" had made the old rule obsolete. <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#15" aria-description="Citation for case: Tennessee v. Garner"><i>Id.,</i> at 15</a></span>.</p>
<p>Unlike most "excessive force" cases in which the degree of permissible force varies widely from case to case, the only issue in a "deadly force" case is whether the facts apparent to the officer justify a decision to kill a suspect in order to prevent his escape.</p>
<p>In <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span></i> we stated the governing rule:</p>
<blockquote>"The use of deadly force to prevent the escape of all felony suspects, whatever the circumstances, is constitutionally unreasonable. It is not better that all felony suspects die than that they escape. Where the suspect poses no immediate threat to the officer and no threat to others, the harm resulting from failing to apprehend him does not justify the use of deadly force to do so.... A police officer may not seize an unarmed, nondangerous suspect by shooting him dead....</blockquote>
<blockquote>"Where the officer has probable cause to believe that the suspect poses a threat of serious physical harm, either to the officer or to others, it is not constitutionally unreasonable to prevent escape by using deadly force. Thus, if the suspect threatens the officer with a weapon or <span class="star-pagination">*204</span> there is probable cause to believe that he has committed a crime involving the infliction or threatened infliction of serious physical harm, deadly force may be used if necessary to prevent escape, and if, where feasible, some warning has been given." <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#11" aria-description="Citation for case: Tennessee v. Garner"><i>Id.,</i> at 11-12</a></span>.</blockquote>
<p>The most common justifications for the use of deadly force are plainly inapplicable to this case. Respondent Haugen had not threatened anyone with a weapon, and petitioner Brosseau did not shoot in order to defend herself.<sup>[1]</sup> Haugen was not a person who had committed a violent crime; nor was there any reason to believe he would do so if permitted to escape. Indeed, there is nothing in the record to suggest he intended to harm anyone.<sup>[2]</sup> The "threat of serious physical harm, either to the officer or to others," <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#11" aria-description="Citation for case: Tennessee v. Garner"><i>id.,</i> at 11</a></span>, that provides the sole justification for Brosseau's use of deadly force was the risk that while fleeing in his vehicle Haugen would accidentally collide with a pedestrian or another vehicle. Whether Brosseau's shot enhanced or minimized that risk is debatable, but the risk of such an accident surely did <span class="star-pagination">*205</span> not justify an attempt to kill the fugitive.<sup>[3]</sup> Thus, I have no difficulty in endorsing the Court's assumption that Brosseau's conduct violated the Constitution.</p>
<p></p>
<h2>II</h2>
<p>An officer is entitled to qualified immunity, despite having engaged in constitutionally deficient conduct, if, in doing so, she did not violate "clearly established statutory or constitutional rights of which a reasonable person would have known." <i>Harlow,</i> <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 818</a></span>. The requirement that the law be clearly established is designed to ensure that officers have fair notice of what conduct is proscribed. See <i>Hope</i> v. <i>Pelzer,</i> <span class="citation" data-id="9434318"><a href="/opinion/121169/hope-v-pelzer/#739" aria-description="Citation for case: Hope v. Pelzer">536 U. S. 730, 739</a></span> (2002). Accordingly, we have recognized that "general statements of the law are not inherently incapable of giving fair and clear warning," <i>United States</i> v. <i>Lanier,</i> <span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/#271" aria-description="Citation for case: United States v. Lanier">520 U. S. 259, 271</a></span> (1997), and have firmly rejected the notion that "an official action is protected by qualified immunity unless the very action in question has previously been held unlawful," <i>Anderson</i> v. <i>Creighton,</i> <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#640" aria-description="Citation for case: Anderson v. Creighton">483 U. S. 635, 640</a></span> (1987).</p>
<p>Thus, the Court's search for relevant case law applying the <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span></i> standard to materially similar facts is both unnecessary and ill advised. See <i>Hope,</i> <span class="citation" data-id="9434318"><a href="/opinion/121169/hope-v-pelzer/#741" aria-description="Citation for case: Hope v. Pelzer">536 U. S., at 741</a></span> ("Although earlier cases involving `fundamentally similar' facts can provide especially strong support for a conclusion that the law is clearly established, they are not necessary to such a finding"); see also <i>Lanier,</i> <span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/#269" aria-description="Citation for case: United States v. Lanier">520 U. S., at 269</a></span>. Indeed, the cases the majority relies on are inapposite and, in fact, only serve <span class="star-pagination">*206</span> to illuminate the patent unreasonableness of Brosseau's actions.<sup>[4]</sup></p>
<p>Rather than uncertainty about the law, it is uncertainty about the likely consequences of Haugen's flight  or, more precisely, uncertainty about how a reasonable officer making the split-second decision to use deadly force would have assessed the foreseeability of a serious accident  that prevents me from answering the question of qualified immunity that this case presents. This is a quintessentially "fact-specific" question, not a question that judges should try to answer "as a matter of law." Cf. <i>Anderson,</i> <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#641" aria-description="Citation for case: Anderson v. Creighton">483 U.S., at 641</a></span>. Although it is preferable to resolve the qualified immunity question at the earliest possible stage of litigation, this preference does not give judges license to take inherently factual questions away from the jury. See <i>Hunter</i> v. <i>Bryant,</i> <span class="citation" data-id="9432435"><a href="/opinion/112671/hunter-v-bryant/#229" aria-description="Citation for case: Hunter v. Bryant">502 U. S. 224, 229</a></span> (1991) <i>(per curiam)</i> (SCALIA, J., concurring in judgment); <span class="citation" data-id="9432435"><a href="/opinion/112671/hunter-v-bryant/#233" aria-description="Citation for case: Hunter v. Bryant"><i>id.,</i> at 233</a></span> (STEVENS, J., dissenting) ("`Whether <span class="star-pagination">*207</span> a reasonable officer could have believed he had probable cause is a question for the trier of fact, and summary judgment or a directed verdict in a § 1983 action based on [the] lack of probable cause is proper only if there is only one reasonable conclusion a jury could reach'" (quoting <i>Bryant</i> v. <i>U. S. Treasury Dept., Secret Service,</i> <span class="citation" data-id="9480344"><a href="/opinion/541812/james-v-bryant-jr-v-united-states-treasury-department-secret-service/#721" aria-description="Citation for case: James v. Bryant, Jr. v. United States Treasury...">903 F. 2d 717, 721</a></span> (CA9 1990))). The bizarre scenario described in the record of this case convinces me that reasonable jurors could well disagree about the answer to the qualified immunity issue. My conclusion is strongly reinforced by the differing opinions expressed by the Circuit Judges who have reviewed the record.</p>
<p></p>
<h2>III</h2>
<p>The Court's attempt to justify its decision to reverse the Court of Appeals without giving the parties an opportunity to provide full briefing and oral argument is woefully unpersuasive. If Brosseau had deliberately shot Haugen in the head and killed him, the legal issues would have been the same as those resulting from the nonfatal wound. I seriously doubt that my colleagues would be so confident about the result as to decide the case without the benefit of briefs or argument on such facts.<sup>[5]</sup> At a minimum, the Ninth Circuit's decision was not clearly erroneous, and the extraordinary remedy of summary reversal is not warranted on these facts. See R. Stern, E. Gressman, &amp; S. Shapiro, Supreme Court Practice 281 (6th ed. 1986).</p>
<p>In sum, the constitutional limits on an officer's use of deadly force have been well settled in this Court's jurisprudence for nearly two decades, and, in this case, Officer Brosseau acted outside of those clearly delineated bounds. <span class="star-pagination">*208</span> Nonetheless, in my judgment, there is a genuine factual question as to whether a reasonably well-trained officer standing in Brosseau's shoes could have concluded otherwise, and that question plainly falls with the purview of the jury.</p>
<p>For these reasons, I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[1]  Haugen also asserted pendent state-law claims and claims against the city and police department. These claims are not presently before us.</p>
<p>[2]  Because this case arises in the posture of a motion for summary judgment, we are required to view all facts and draw all reasonable inferences in favor of the nonmoving party, Haugen. See <i>Saucier</i> v. <i>Katz,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./533/194/">533 U. S. 194</a></span>, 201 (2001).</p>
<p>[3]  We have no occasion in this case to reconsider our instruction in <i>Saucier</i> v. <i>Katz, supra</i><i>,</i> that lower courts decide the constitutional question prior to deciding the qualified immunity question. We exercise our summary reversal procedure here simply to correct a clear misapprehension of the qualified immunity standard.</p>
<p>[4]  The parties point us to a number of other cases in this vein that postdate the conduct in question, <i>i. e.,</i> Brosseau's February 21, 1999, shooting of Haugen. See <i>Cowan ex rel. Estate of Cooper</i> v. <i>Breen,</i> <span class="citation" data-id="784483"><a href="/opinion/784483/margaret-cowan-administratrix-of-the-estate-of-victoria-cooper-v-michael/#763" aria-description="Citation for case: Margaret Cowan, Administratrix of the Estate of Victoria...">352 F. 3d 756, 763</a></span> (CA2 2003); <i>Pace</i> v. <i>Capobianco,</i> <span class="citation" data-id="7009807"><a href="/opinion/7103965/pace-v-capobianco/#1281" aria-description="Citation for case: Pace v. Capobianco">283 F. 3d 1275, 1281-1282</a></span> (CA11 2002); <i>Scott</i> v. <i>Clay County,</i> <span class="citation" data-id="9492855"><a href="/opinion/767897/patricia-scott-v-clay-county-tennessee-chinn-anderson-billy-pierce/#877" aria-description="Citation for case: Patricia Scott v. Clay County, Tennessee Chinn Anderson...">205 F. 3d 867, 877</a></span> (CA6 2000); <i>McCaslin</i> v. <i>Wilkins,</i> <span class="citation multiple-matches"><a href="/c/F.%203d/183/775/">183 F. 3d 775</a></span>, 778-779 (CA8 1999); <i>Abraham</i> v. <i>Raso,</i> <span class="citation" data-id="765106"><a href="/opinion/765106/vanessa-abraham-in-her-own-right-and-as-administratrix-of-the-estate-of/#288" aria-description="Citation for case: Vanessa Abraham, in Her Own Right and as Administratrix...">183 F. 3d 279, 288-296</a></span> (CA3 1999). These decisions, of course, could not have given fair notice to Brosseau and are of no use in the clearly established inquiry.</p>
<p>[1]  Although Brosseau attested that she believed Haugen may have been attempting to retrieve a weapon from the floorboard of his vehicle sometime during the struggle, a fact which Haugen hotly contests, there is no evidence in the record to suggest that, at the time the shot was fired, Brosseau believed, or any reasonable officer would have thought, that Haugen had access to a weapon at that moment.</p>
<p>[2]  At the time of the shooting, Brosseau had the following facts at her disposal. Haugen had a felony no-bail warrant for a nonviolent drug offense, was suspected in a nonviolent burglary, and had been fleeing from law enforcement on foot for approximately 30 to 45 minutes without incident. At the behest of Brosseau, the private individuals on the scene were inside their respective vehicles. Haugen's girlfriend and her daughter were in a small car approximately four feet in front and slightly to the right of Haugen's Jeep; Glen Tamburello and Matt Atwood were inside a pickup truck on the street blocking the driveway, approximately 20 to 30 feet from Haugen's Jeep. The only two police officers on foot at the scene were last seen in a neighbor's backyard, two houses down and to the right of the driveway.</p>
<p>[3]  The evidence supporting Haugen's allegation that Brosseau did "willfully fire her weapon with the intent to murder me," 1 Record, Doc. No. 1, includes a statement by a defense expert that Brosseau had "clearly articulated her intention to use deadly force," <i><span class="citation" data-id="765106"><a href="/opinion/765106/vanessa-abraham-in-her-own-right-and-as-administratrix-of-the-estate-of/" aria-description="Citation for case: Vanessa Abraham, in Her Own Right and as Administratrix...">id.,</a></span></i> Doc. No. 24. Moreover, the report of the Puyallup, Washington, Police Department Firearms Review Board stated that Brosseau "chose to use deadly force to stop Haugen." 2 <i><span class="citation" data-id="765106"><a href="/opinion/765106/vanessa-abraham-in-her-own-right-and-as-administratrix-of-the-estate-of/" aria-description="Citation for case: Vanessa Abraham, in Her Own Right and as Administratrix...">id.,</a></span></i> Doc. No. 27, Exh. H.</p>
<p>[4]  In <i>Cole</i> v. <i>Bone,</i> <span class="citation" data-id="9010890"><a href="/opinion/9017761/cole-v-bone/" aria-description="Citation for case: Cole v. Bone">993 F. 2d 1328</a></span> (CA8 1993), an 18-wheel tractor-trailer sped through a tollbooth and engaged the police in a high-speed pursuit in excess of 90 miles per hour on a high-traffic interstate during the holiday season. During the course of the pursuit, the driver passed traffic on both shoulders of the interstate, repeatedly attempted to ram several police cars, drove more than 100 passenger vehicles off the road, ran through several roadblocks, and continued driving after the officer shot out the wheels of the fugitive's truck. <span class="citation" data-id="9010890"><a href="/opinion/9017761/cole-v-bone/#1330" aria-description="Citation for case: Cole v. Bone"><i>Id.,</i> at 1330-1331</a></span>. Only then did the officer finally resort to deadly force to disable the driver. Similarly, in <i>Smith</i> v. <i>Freland,</i> <span class="citation" data-id="576267"><a href="/opinion/576267/patricia-smith-individually-and-as-administratrix-of-the-estate-of-brent/" aria-description="Citation for case: Patricia Smith, Individually and as Administratrix of the...">954 F. 2d 343</a></span> (CA6 1992), the suspect led a police officer on a high-speed chase, reaching speeds in excess of 90 miles per hour. When the officer initially cornered the suspect in a field, the driver repeatedly swerved directly toward the police car, forcing the officer to move out of the way and allowing the suspect to continue the chase. <span class="citation" data-id="576267"><a href="/opinion/576267/patricia-smith-individually-and-as-administratrix-of-the-estate-of-brent/#344" aria-description="Citation for case: Patricia Smith, Individually and as Administratrix of the..."><i>Id.,</i> at 344</a></span>. Only after additional officers cornered the suspect for a second time, and after the suspect smashed directly into an unoccupied police car and began to flee again, did the officer finally shoot the driver. <i><span class="citation" data-id="576267"><a href="/opinion/576267/patricia-smith-individually-and-as-administratrix-of-the-estate-of-brent/" aria-description="Citation for case: Patricia Smith, Individually and as Administratrix of the...">Ibid.</a></span></i>
</p>
<p>In stark contrast, at the time Brosseau shot Haugen, the Jeep was immobile, or at best, had just started moving. Haugen had not driven at excess speeds; nor had he rammed, or attempted to ram, nearby police cars or passenger vehicles. In sum, there was no ongoing or prior high-speed car chase to inform the probable-cause analysis.</p>
<p>[5]  The Court's recitation of the facts that led up to the shooting obscures the undisputed point that no one contends Haugen was the kind of dangerous person  perhaps a terrorist or an escaped convict on a crime spree  who would have been a danger to the community if he had been allowed to escape. The factual issues relate only to the danger that he posed while in the act of escaping.</p>

</div>
```

---

## GROUP: content/cases/Brower v. County of Inyo.md  (`case`, 6 assertions)

### content_page

```
---
title: "Brower v. County of Inyo"
type: case
citation: "489 U.S. 593 (1989)"
parallel_cite: "109 S. Ct. 1378; 103 L. Ed. 2d 628; 57 U.S.L.W. 4321"
neutral_cite: 1989 U.S. LEXIS 1569
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1989
date_decided: 1989-03-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1989-03-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Brower v. County of Inyo
  varies_by_point: false
  scope_note: "Good law. A Fourth Amendment seizure occurs only when the government terminates a person's freedom of movement through means intentionally applied; a stop produced by the very instrumentality the police put in place is a seizure. Canonical caption is Brower v. County of Inyo; the ingest queue refers to it as Brower v. Inyo County (aliased)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/"
  cluster_id: 112218
  opinion_id: 112218
  identity_checked: true
homes:
  - page: "[[Seizure of the Person]]"
    role: "Anchor"
  - page: "[[Use of Force]]"
    role: "Related (cross-doctrine)"
related: ["[[California v. Hodari D.]]", "[[Torres v. Madrid]]", "[[Scott v. Harris]]", "[[Tennessee v. Garner]]"]
aliases: ["Brower v. Inyo County"]
tags: ["case", "fourth-amendment", "seizure", "roadblock", "use-of-force", "section-1983"]
holding: "A Fourth Amendment seizure occurs only when the government terminates a person's freedom of movement through means intentionally applied; stopping a fleeing driver with a roadblock he crashes into is a seizure because he is stopped by the very instrumentality put in place to stop him."
lake:
  record_id: Brower v. County of Inyo
  status: verified
  projected_at: 2026-07-09
---

# Brower v. County of Inyo

*489 U.S. 593 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After Brower stole a car and led police on a roughly 20-mile chase, officers set up a roadblock to stop him: they placed an 18-wheel tractor-trailer across both lanes of the highway, behind a curve, with a police car's headlights aimed to blind Brower as he approached. Brower crashed into the trailer and was killed. His heirs sued under 42 U.S.C. § 1983, alleging an unreasonable Fourth Amendment seizure. The District Court dismissed for failure to state a claim, reasoning no "seizure" had occurred, and the Ninth Circuit affirmed.

## Issue
Whether a Fourth Amendment "seizure" occurs when police stop a fleeing motorist by means of a roadblock into which he crashes — i.e., what governmental conduct counts as a seizure of the person.

## Rule
A seizure requires that the government stop the person by the means it intended. "[A] Fourth Amendment seizure does not occur whenever there is a governmentally caused termination of an individual's freedom of movement (the innocent passerby), nor even whenever there is a governmentally caused and governmentally *desired* termination of an individual's freedom of movement (the fleeing felon), but only when there is a governmental termination of freedom of movement *through means intentionally applied*." — 489 U.S. at 596–597. ^pin-596

The Amendment "addresses 'misuse of power,' . . . not the accidental effects of otherwise lawful government conduct." — *Id.* at 596. ^pin-596b

It is therefore "enough for a seizure that a person be stopped by the very instrumentality set in motion or put in place in order to achieve that result." — [*Id.* at 599](https://www.courtlistener.com/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/#:~:text=enough%20for%20a%20seizure%20that). ^pin-599

## Application
Unlike a pursuing police car with flashing lights — which stops the suspect, if at all, only by his own loss of control — a roadblock "is designed to produce a stop by physical impact if voluntary compliance does not occur." Brower was stopped by the very obstacle the officers erected to stop him: "Brower was meant to be stopped by the physical obstacle of the roadblock — and that he was so stopped." The Court declined to parse the officers' subjective hope that he would halt short of the barrier, or to distinguish a roadblock placed for a voluntary stop from one placed around a bend to force a collision. Because the complaint alleged a stop by the intended means, it stated a Fourth Amendment seizure; the Court reversed the dismissal and [[Reading and Citing Cases#on-remand|remanded]] for the separate question whether that seizure was unreasonable.

## Conclusion
A seizure of the person occurs when the government terminates freedom of movement through means intentionally applied, which the alleged roadblock did; the dismissal was reversed and the case [[Reading and Citing Cases#on-remand|remanded]] to decide reasonableness. *Brower* supplies the controlling definition of when a seizure of the person occurs.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Brower*'s "means intentionally applied" definition governs seizure-of-the-person analysis and is applied in [[California v. Hodari D.]] (show of authority requires submission), [[Scott v. Harris]] (deadly-force pursuit seizure), and [[Torres v. Madrid]] (application of physical force with intent to restrain is a seizure even if the suspect escapes).

## Appears on
- [[Seizure of the Person]] — *Anchor*
- [[Use of Force]] — *Related (cross-doctrine)*

## Sources
- *Brower v. County of Inyo*, 489 U.S. 593 (1989) — https://www.courtlistener.com/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/ — pinpoints: 596–597, 599.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6e5f568db2dc4597", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "489 U.S. 593 (1989)", "court": "U.S. Supreme Court", "neutral_cite": "1989 U.S. LEXIS 1569", "official_citation_present": true, "parallel_cite": "109 S. Ct. 1378; 103 L. Ed. 2d 628; 57 U.S.L.W. 4321", "title": "Brower v. County of Inyo", "year": "1989"}}
{"assertion_id": "7d86e48e7284ba13", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A Fourth Amendment seizure occurs only when the government terminates a person's freedom of movement through means intentionally applied; stopping a fleeing driver with a roadblock he crashes into is a seizure because he is stopped by the very instrumentality put in place to stop him.", "title": "Brower v. County of Inyo"}}
{"assertion_id": "a1bacb6178df3f16", "dimension": "support", "kind": "home_role", "locator": {"home": "Use of Force"}, "payload": {"home": "Use of Force", "role": "Related (cross-doctrine)", "title": "Brower v. County of Inyo"}}
{"assertion_id": "bbc9b2b96d46bfff", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Anchor", "title": "Brower v. County of Inyo"}}
{"assertion_id": "29d51014a7bd278b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1989-03-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Brower v. County of Inyo", "field_i_validity": "good_law", "scope_note": "Good law. A Fourth Amendment seizure occurs only when the government terminates a person's freedom of movement through means intentionally applied; a stop produced by the very instrumentality the police put in place is a seizure. Canonical caption is Brower v. County of Inyo; the ingest queue refers to it as Brower v. Inyo County (aliased).", "title": "Brower v. County of Inyo", "varies_by_point": "false"}}
{"assertion_id": "e7091615a913f975", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Brower v. County of Inyo"}}
```

### lake record — Brower v. County of Inyo

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brower v. County of Inyo",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Brower Ex Rel. Estate of Caldwell v. County of Inyo",
    "case_name_short": "Brower",
    "case_name_full": "BROWER, Individually and as Administrator of the ESTATE OF CALDWELL (BROWER), Et Al. v. COUNTY OF INYO Et Al.",
    "input_case_name": "Brower v. County of Inyo",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1989-03-21",
    "year": 1989,
    "docket": null,
    "cluster_id": 112218,
    "lead_opinion_id": 112218,
    "sibling_ids": [
      112218,
      9431604,
      9431605
    ],
    "absolute_url": "/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "489 U.S. 593",
      "volume": "489",
      "reporter": "U.S.",
      "page": "593",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 1378",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1378",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 L. Ed. 2d 628",
        "volume": "103",
        "reporter": "L. Ed. 2d",
        "page": "628",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4321",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4321",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1989 U.S. LEXIS 1569",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "1569",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "489 U.S. 593",
        "volume": "489",
        "reporter": "U.S.",
        "page": "593",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 1378",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1378",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 L. Ed. 2d 628",
        "volume": "103",
        "reporter": "L. Ed. 2d",
        "page": "628",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 U.S. LEXIS 1569",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "1569",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4321",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4321",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "489 U.S. 593",
    "official_selection": {
      "court_class": "scotus",
      "selected": "489 U.S. 593",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-596",
      "page": null,
      "quote": "occurs when police stop a fleeing motorist by means of a roadblock into which he crashes \u2014 i.e., what governmental conduct counts as a seizure of the person. ## Rule A seizure requires that the government stop the person by the means it intended.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-596b",
      "page": null,
      "quote": "addresses 'misuse of power,' . . . not the accidental effects of otherwise lawful government conduct.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-599",
      "page": null,
      "quote": "enough for a seizure that a person be stopped by the very instrumentality set in motion or put in place in order to achieve that result.",
      "star_marker": "599",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15618,
      "fragment": "#:~:text=enough%20for%20a%20seizure%20that",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1989-03-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Brower v. County of Inyo",
    "varies_by_point": false,
    "scope_note": "Good law. A Fourth Amendment seizure occurs only when the government terminates a person's freedom of movement through means intentionally applied; a stop produced by the very instrumentality the police put in place is a seizure. Canonical caption is Brower v. County of Inyo; the ingest queue refers to it as Brower v. Inyo County (aliased).",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Brower v. County of Inyo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tanguay",
          "cluster_id": 4598184,
          "cite": [
            "918 F.3d 1"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Claudia Harbourt v. PPE Casino Resorts Maryland",
          "cluster_id": 3197571,
          "cite": [
            "820 F.3d 655",
            "26 Wage & Hour Cas.2d (BNA) 625",
            "2016 U.S. App. LEXIS 7415",
            "2016 WL 1621908"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 2546477,
          "cite": [
            "359 S.W.3d 725",
            "2011 WL 6176184"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hernandez v. City of Pomona",
          "cluster_id": 1801687,
          "cite": [
            "46 Cal. 4th 501",
            "207 P.3d 506",
            "94 Cal. Rptr. 3d 1",
            "2009 Cal. LEXIS 4630"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bell Atlantic Corp. v. Twombly",
          "cluster_id": 145730,
          "cite": [
            "167 L. Ed. 2d 929",
            "127 S. Ct. 1955",
            "550 U.S. 544",
            "2007 U.S. LEXIS 5901",
            "41 Communications Reg. (P&F) 567",
            "20 Fla. L. Weekly Fed. S 267",
            "68 Fed. R. Serv. 3d 661",
            "75 U.S.L.W. 4337"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
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
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
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
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
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
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albright v. Oliver",
          "cluster_id": 112924,
          "cite": [
            "127 L. Ed. 2d 114",
            "114 S. Ct. 807",
            "510 U.S. 266",
            "1994 U.S. LEXIS 1319"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "County of Sacramento v. Lewis",
          "cluster_id": 118214,
          "cite": [
            "140 L. Ed. 2d 1043",
            "118 S. Ct. 1708",
            "523 U.S. 833",
            "1998 U.S. LEXIS 3404"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
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
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
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
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
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
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 622304,
          "cite": [
            "181 L. Ed. 2d 911",
            "132 S. Ct. 945",
            "565 U.S. 400",
            "2012 U.S. LEXIS 1063"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shirley Presley v. City of Charlottesville Rivanna Trails Foundation",
          "cluster_id": 795822,
          "cite": [
            "464 F.3d 480",
            "2006 U.S. App. LEXIS 24048",
            "2006 WL 2709208"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael Hayes v. Idaho Correctional Center",
          "cluster_id": 4372888,
          "cite": [
            "849 F.3d 1204",
            "2017 WL 836072",
            "2017 U.S. App. LEXIS 3851"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Garcia-Cantu",
          "cluster_id": 1769810,
          "cite": [
            "253 S.W.3d 236",
            "2008 Tex. Crim. App. LEXIS 581",
            "2008 WL 1958956"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
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
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cindy Abbott v. Sangamon County",
          "cluster_id": 816250,
          "cite": [
            "705 F.3d 706",
            "2013 WL 322920",
            "2013 U.S. App. LEXIS 1963"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lamont v. New Jersey",
          "cluster_id": 205997,
          "cite": [
            "637 F.3d 177",
            "2011 U.S. App. LEXIS 4104",
            "2011 WL 753856"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 1676406,
          "cite": [
            "912 S.W.2d 227",
            "1995 Tex. Crim. App. LEXIS 115",
            "1995 WL 675559"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Outdoor Media Dimensions Inc. v. State",
          "cluster_id": 836243,
          "cite": [
            "20 P.3d 180",
            "331 Or. 634",
            "2001 Ore. LEXIS 135"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henry Szabla v. City Of Brooklyn Park",
          "cluster_id": 797743,
          "cite": [
            "486 F.3d 385",
            "2007 U.S. App. LEXIS 11602"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murphy v. Lynn",
          "cluster_id": 7048090,
          "cite": [
            "118 F.3d 938",
            "1997 WL 371091"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyle Ciminillo v. Thomas Streicher Daniel Hills Richard Janke, Gerald Knight City of Cincinnati",
          "cluster_id": 792929,
          "cite": [
            "434 F.3d 461",
            "2006 U.S. App. LEXIS 1020",
            "2006 WL 89157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Emil Ewolski v. City of Brunswick",
          "cluster_id": 777338,
          "cite": [
            "287 F.3d 492",
            "2002 U.S. App. LEXIS 7129",
            "2002 WL 571329"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. Madrid",
          "cluster_id": 4867542,
          "cite": [
            "592 U.S. 306",
            "141 S. Ct. 989",
            "209 L. Ed. 2d 190"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark Atkinson v. City of Mountain View",
          "cluster_id": 819982,
          "cite": [
            "709 F.3d 1201",
            "2013 WL 462381",
            "2013 U.S. App. LEXIS 2703"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Flores v. City of Palacios",
          "cluster_id": 36003,
          "cite": [
            "381 F.3d 391",
            "2004 U.S. App. LEXIS 16477",
            "2004 WL 1775948"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112218 OR 9431604 OR 9431605) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTc3ODkxMjAwMDAwJnM9MTQ1NzM4JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112218+OR+9431604+OR+9431605%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112218 OR 9431604 OR 9431605)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNTkmcz0xNTI2NTImdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112218+OR+9431604+OR+9431605%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112218 OR 9431604 OR 9431605)",
        "reviewed": 26,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 26,
        "triage_read": 0,
        "triage_snippet_classified": 26
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112218 OR 9431604 OR 9431605)",
    "indexed_citing_opinions": 705,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112218,
        "count": 604,
        "count_source": "search"
      },
      {
        "opinion_id": 9431604,
        "count": 112,
        "count_source": "search"
      },
      {
        "opinion_id": 9431605,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1485,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/brower-v-county-of-inyo.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgxMDUxNzImcz05MzY5NTk3JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112218+OR+9431604+OR+9431605%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112218,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 105573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 108305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 109009,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 110169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 111831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 458562,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 461210,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 476350,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 484686,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 487470,
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
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:12:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:12:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:16:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:12:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Brower v. County of Inyo

```
<div>
<center><b><span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo">489 U.S. 593</a></span> (1989)</b></center>
<center><h1>BROWER, INDIVIDUALLY AND AS ADMINISTRATOR OF THE ESTATE OF CALDWELL (BROWER), ET AL.<br>
v.<br>
COUNTY OF INYO ET AL.</h1></center>
<center>No. 87-248.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 11, 1989</center>
<center>Decided March 21, 1989</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT
<p><span class="star-pagination">*594</span> <i>Robert G. Gilmore</i> argued the cause for petitioners. With him on the briefs was <i>Craig A. Diamond.</i></p>
<p><i>Philip W. McDowell</i> argued the cause for respondents. With him on the brief was <i>Gregory L. James.</i></p>
<p>JUSTICE SCALIA delivered the opinion of the Court.</p>
<p>On the night of October 23, 1984, William James Caldwell (Brower) was killed when the stolen car that he had been driving at high speeds for approximately 20 miles in an effort to elude pursuing police crashed into a police roadblock. His heirs, petitioners here, brought this action in Federal District Court under <span class="citation no-link">42 U. S. C. § 1983</span>, claiming, <i>inter alia,</i> that respondents used "brutal, excessive, unreasonable and unnecessary physical force" in establishing the roadblock, and thus effected an unreasonable seizure of Brower, in violation of the Fourth Amendment. Petitioners alleged that "under color of statutes, regulations, customs and usages," respondents (1) caused an 18-wheel tractor-trailer to be placed across both lanes of a two-lane highway in the path of Brower's flight, (2) "effectively concealed" this roadblock by placing it behind a curve and leaving it unilluminated, and (3) positioned a police car, with its headlights on, between Brower's oncoming vehicle and the truck, so that Brower would be "blinded" on his approach. App. 8-9. Petitioners further alleged that Brower's fatal collision with the truck was "a proximate result" of this official conduct. <span class="citation no-link"><i>Id.,</i> at 9</span>. The District Court granted respondents' motion to dismiss the complaint for failure to state a claim on the ground (insofar as the Fourth Amendment claim was concerned) that "establishing a roadblock [was] not unreasonable under the circumstances." App. to Pet. for Cert. A-21. A divided panel of the Court of Appeals for the Ninth Circuit affirmed the dismissal of the Fourth Amendment claim on the basis that no "seizure" had occurred. <span class="citation multiple-matches"><a href="/c/F.%202d/817/540/">817 F. 2d 540</a></span>, 545-546 (1987). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./487/1217/">487 U. S. 1217</a></span> (1988), to resolve a conflict between that decision and the contrary holding <span class="star-pagination">*595</span> of the Court of Appeals for the Fifth Circuit in <i>Jamieson</i> v. <i>Shaw,</i> <span class="citation" data-id="8934389"><a href="/opinion/8943843/jamieson-v-shaw/" aria-description="Citation for case: Jamieson v. Shaw">772 F. 2d 1205</a></span> (1985).</p>
<p>The Fourth Amendment to the Constitution provides:</p>
<blockquote>"The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the person or things to be seized."</blockquote>
<p>In <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985), all Members of the Court agreed that a police officer's fatal shooting of a fleeing suspect constituted a Fourth Amendment "seizure." See <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#7" aria-description="Citation for case: Tennessee v. Garner"><i>id.,</i> at 7</a></span>; <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#25" aria-description="Citation for case: Tennessee v. Garner"><i>id.,</i> at 25</a></span> (O'CONNOR, J., dissenting). We reasoned that "[w]henever an officer restrains the freedom of a person to walk away, he has seized that person." <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#7" aria-description="Citation for case: Tennessee v. Garner"><i>Id.,</i> at 7</a></span>. While acknowledging <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span>,</i> the Court of Appeals here concluded that no "seizure" occurred when Brower collided with the police roadblock because "[p]rior to his failure to stop voluntarily, his freedom of movement was never arrested or restrained" and because "[h]e had a number of opportunities to stop his automobile prior to the impact." 817 F. 2d, at 546. Essentially the same thing, however, could have been said in <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span>.</i> Brower's independent decision to continue the chase can no more eliminate respondents' responsibility for the termination of his movement effected by the roadblock than Garner's independent decision to flee eliminated the Memphis police officer's responsibility for the termination of his movement effected by the bullet.</p>
<p>The Court of Appeals was impelled to its result by consideration of what it described as the "analogous situation" of a police chase in which the suspect unexpectedly loses control of his car and crashes. See <i>Galas</i> v. <i>McKee,</i> <span class="citation" data-id="476350"><a href="/opinion/476350/galas-v-mckee/#202" aria-description="Citation for case: Galas v. Mckee">801 F. 2d 200, 202-203</a></span> (CA6 1986) (no seizure in such circumstances). We agree that no unconstitutional seizure occurs there, but not for a reason that has any application to the present case. <span class="star-pagination">*596</span> Violation of the Fourth Amendment requires an intentional acquisition of physical control. A seizure occurs even when an unintended person or thing is the object of the detention or taking, see <i>Hill</i> v. <i>California,</i> <span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/#802" aria-description="Citation for case: Hill v. California">401 U. S. 797, 802-805</a></span> (1971); cf. <i>Maryland</i> v. <i>Garrison,</i> <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#85" aria-description="Citation for case: Maryland v. Garrison">480 U. S. 79, 85-89</a></span> (1987), but the detention or taking itself must be willful. This is implicit in the word "seizure," which can hardly be applied to an unknowing act. The writs of assistance that were the principal grievance against which the Fourth Amendment was directed, see <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 624-625</a></span> (1886); T. Cooley, Constitutional Limitations *301-*302, did not involve unintended consequences of government action. Nor did the general warrants issued by Lord Halifax in the 1760's, which produced "the first and only major litigation in the English courts in the field of search and seizure," T. Taylor, Two Studies in Constitutional Interpretation 26 (1969), including the case we have described as a "monument of English freedom" "undoubtedly familiar" to "every American statesman" at the time the Constitution was adopted, and considered to be "the true and ultimate expression of constitutional law," <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#626" aria-description="Citation for case: Boyd v. United States"><i>Boyd, supra,</i> at 626</a></span> (discussing <i>Entick</i> v. <i>Carrington,</i> 19 How. St. Tr. 1029, 95 Eng. Rep. 807 (K. B. 1765)). In sum, the Fourth Amendment addresses "misuse of power," <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#33" aria-description="Citation for case: Byars v. United States">273 U. S. 28, 33</a></span> (1927), not the accidental effects of otherwise lawful government conduct.</p>
<p>Thus, if a parked and unoccupied police car slips its brake and pins a passerby against a wall, it is likely that a tort has occurred, but not a violation of the Fourth Amendment. And the situation would not change if the passerby happened, by lucky chance, to be a serial murderer for whom there was an outstanding arrest warrant  even if, at the time he was thus pinned, he was in the process of running away from two pursuing constables. It is clear, in other words, that a Fourth Amendment seizure does not occur whenever there is a governmentally caused termination of an <span class="star-pagination">*597</span> individual's freedom of movement (the innocent passerby), nor even whenever there is a governmentally caused and governmentally <i>desired</i> termination of an individual's freedom of movement (the fleeing felon), but only when there is a governmental termination of freedom of movement <i>through means intentionally applied.</i> That is the reason there was no seizure in the hypothetical situation that concerned the Court of Appeals. The pursuing police car sought to stop the suspect only by the show of authority represented by flashing lights and continuing pursuit; and though he was in fact stopped, he was stopped by a different means  his loss of control of his vehicle and the subsequent crash. If, instead of that, the police cruiser had pulled alongside the fleeing car and sideswiped it, producing the crash, then the termination of the suspect's freedom of movement would have been a seizure.</p>
<p>This analysis is reflected by our decision in <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924), where an armed revenue agent had pursued the defendant and his accomplice after seeing them obtain containers thought to be filled with "moonshine whisky." During their flight they dropped the containers, which the agent recovered. The defendant sought to suppress testimony concerning the containers' contents as the product of an unlawful seizure. Justice Holmes, speaking for a unanimous Court, concluded: "The defendant's own acts, and those of his associates, disclosed the jug, the jar and the bottle  and there was no seizure in the sense of the law when the officers examined the contents of each after they had been abandoned." <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#58" aria-description="Citation for case: Hester v. United States"><i>Id.,</i> at 58</a></span>. Thus, even though the incriminating containers were unquestionably taken into possession as a result (in the broad sense) of action by the police, the Court held that no seizure had taken place. It would have been quite different, of course, if the revenue agent had shouted, "Stop and give us those bottles, in the name of the law!" and the defendant and his accomplice had complied. Then the taking of possession would have been <span class="star-pagination">*598</span> not merely the result of government action but the result of the very means (the show of authority) that the government selected, and a Fourth Amendment seizure would have occurred.</p>
<p>In applying these principles to the dismissal of petitioners' Fourth Amendment complaint for failure to state a claim, we can sustain the District Court's action only if, taking the allegations of the complaint in the light most favorable to petitioners, see <i>Scheuer</i> v. <i>Rhodes,</i> <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#236" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232, 236</a></span> (1974), we nonetheless conclude that they could prove no set of facts entitling them to relief for a "seizure." See <i>Conley</i> v. <i>Gibson,</i> <span class="citation" data-id="105573"><a href="/opinion/105573/conley-v-gibson/#45" aria-description="Citation for case: Conley v. Gibson">355 U. S. 41, 45-46</a></span> (1957). Petitioners have alleged the establishment of a roadblock crossing both lanes of the highway. In marked contrast to a police car pursuing with flashing lights, or to a policeman in the road signaling an oncoming car to halt, see <i>Kibbe</i> v. <i>Springfield,</i> <span class="citation" data-id="461210"><a href="/opinion/461210/lois-thurston-kibbe-administrator-of-the-estate-of-clinton-thurston-v/#802" aria-description="Citation for case: Lois Thurston Kibbe, Administrator of the Estate of...">777 F. 2d 801, 802-803</a></span> (CA1 1985), cert. dism'd, <span class="citation" data-id="9430858"><a href="/opinion/111831/city-of-springfield-v-kibbe/" aria-description="Citation for case: City of Springfield v. Kibbe">480 U. S. 257</a></span> (1987), a roadblock is not just a significant show of authority to induce a voluntary stop, but is designed to produce a stop by physical impact if voluntary compliance does not occur. It may well be that respondents here preferred, and indeed earnestly hoped, that Brower would stop on his own, without striking the barrier, but we do not think it practicable to conduct such an inquiry into subjective intent. See <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#922" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 922, n. 23</a></span> (1984); see also <i>Anderson</i> v. <i>Creighton,</i> <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#641" aria-description="Citation for case: Anderson v. Creighton">483 U. S. 635, 641</a></span> (1987); <i>Harlow</i> v. <i>Fitzgerald,</i> <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#815" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 815-819</a></span> (1982). Nor do we think it possible, in determining whether there has been a seizure in a case such as this, to distinguish between a roadblock that is designed to give the oncoming driver the option of a voluntary stop (<i>e. g.,</i> one at the end of a long straightaway), and a roadblock that is designed precisely to produce a collision (<i>e. g.,</i> one located just around a bend). In determining whether the means that terminates the freedom of movement is the very means that the government intended we cannot draw too fine a line, or we will be driven to saying that one is not seized who has been <span class="star-pagination">*599</span> stopped by the accidental discharge of a gun with which he was meant only to be bludgeoned, or by a bullet in the heart that was meant only for the leg. We think it enough for a seizure that a person be stopped by the very instrumentality set in motion or put in place in order to achieve that result. It was enough here, therefore, that, according to the allegations of the complaint, Brower was meant to be stopped by the physical obstacle of the roadblock  and that he was so stopped.</p>
<p>This is not to say that the precise character of the roadblock is irrelevant to further issues in this case. "Seizure" alone is not enough for § 1983 liability; the seizure must be "unreasonable." Petitioners can claim the right to recover for Brower's death only because the unreasonableness they allege consists precisely of setting up the roadblock in such manner as to be likely to kill him. This should be contrasted with the situation that would obtain if the sole claim of unreasonableness were that there was no probable cause for the stop. In that case, if Brower had had the opportunity to stop voluntarily at the roadblock, but had negligently or intentionally driven into it, then, because of lack of proximate causality, respondents, though responsible for depriving him of his freedom of movement, would not be liable for his death. See <i>Martinez</i> v. <i>California,</i> <span class="citation" data-id="110169"><a href="/opinion/110169/martinez-v-california/#285" aria-description="Citation for case: Martinez v. California">444 U. S. 277, 285</a></span> (1980); <i>Cameron</i> v. <i>Pontiac,</i> <span class="citation" data-id="484686"><a href="/opinion/484686/betty-cameron-personal-representative-of-the-estate-of-christopher-cameron/#786" aria-description="Citation for case: Betty Cameron, Personal Representative of the Estate of...">813 F. 2d 782, 786</a></span> (CA6 1987). Thus, the circumstances of this roadblock, including the allegation that headlights were used to blind the oncoming driver, may yet determine the outcome of this case.</p>
<p>The complaint here sufficiently alleges that respondents, under color of law, sought to stop Brower by means of a roadblock and succeeded in doing so. That is enough to constitute a "seizure" within the meaning of the Fourth Amendment. Accordingly, we reverse the judgment of the Court of Appeals and remand for consideration of whether the District Court properly dismissed the Fourth Amendment claim <span class="star-pagination">*600</span> on the basis that the alleged roadblock did not effect a seizure that was "unreasonable."</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE STEVENS, with whom JUSTICE BRENNAN, JUSTICE MARSHALL, and JUSTICE BLACKMUN join, concurring in the judgment.</p>
<p>The Court is unquestionably correct in concluding that respondents' use of a roadblock to stop Brower's car constituted a seizure within the meaning of the Fourth Amendment. I therefore concur in its judgment. I do not, however, join its opinion because its dicta seem designed to decide a number of cases not before the Court and to establish the proposition that "[v]iolation of the Fourth Amendment requires an intentional acquisition of physical control." <i>Ante,</i> at 596.</p>
<p>The intentional acquisition of physical control of something is no doubt a characteristic of the typical seizure, but I am not entirely sure that it is an essential element of every seizure or that this formulation is particularly helpful in deciding close cases. The Court suggests that the test it articulates does not turn on the subjective intent of the officer. <i>Ante,</i> at 598. This, of course, not only comports with the recent trend in our cases, see, <i>e. g., </i><i>Harlow</i> v. <i>Fitzgerald,</i> <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#815" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 815-819</a></span> (1982); <i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 554, n. 6</a></span> (1980) (opinion of Stewart, J.), but also makes perfect sense. No one would suggest that the Fourth Amendment provides no protection against a police officer who is too drunk to act intentionally, yet who appears in uniform brandishing a weapon in a threatening manner. Alternatively, however, the concept of objective intent, at least in the vast majority of cases, adds little to the well-established rule that "a person has been `seized' within the meaning of the Fourth Amendment only if, in view of all of the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave." <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Id.,</a></span></i> at 554 <span class="star-pagination">*601</span> (opinion of Stewart, J.); see also <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#215" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 215</a></span> (1984).</p>
<p>There may be a case that someday comes before this Court in which the concept of intent is useful in applying the Fourth Amendment. What is extraordinary about the Court's discussion of the intent requirement in this case is that there is no dispute that the roadblock was intended to stop the decedent. Decision in the case before us is thus not advanced by pursuing a hypothetical inquiry concerning whether an unintentional act might also violate the Fourth Amendment. Rather, as explained in Judge Pregerson's dissent in the Court of Appeals, this case is plainly controlled by our decision in <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985). <span class="citation multiple-matches"><a href="/c/F.%202d/817/540/">817 F. 2d 540</a></span>, 548 (CA9 1987) (opinion concurring in part and dissenting in part). In that case, we held that "there can be no question that apprehension by the use of deadly force is a seizure subject to the reasonableness requirement of the Fourth Amendment." <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#7" aria-description="Citation for case: Tennessee v. Garner">471 U. S., at 7</a></span>. Because it was undisputed that the police officer acted intentionally, we did not discuss the hypothetical case of an unintentional seizure. I would exercise the same restraint here.</p>
<p>I am in full accord with Judge Pregerson's dissenting opinion, and, for the reasons stated in his opinion, I join the Court's judgment.</p>
</div>
```

---

## GROUP: content/cases/Brown v. Illinois.md  (`case`, 5 assertions)

### content_page

```
---
title: "Brown v. Illinois"
type: case
citation: "422 U.S. 590 (1975)"
parallel_cite: "95 S. Ct. 2254; 45 L. Ed. 2d 416"
neutral_cite: 1975 U.S. LEXIS 82
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1975
date_decided: 1975-06-26
docket: 73-6650
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1975-06-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Brown v. Illinois
  varies_by_point: false
  scope_note: "Attenuation factors remain the governing test; applied in Utah v. Strieff."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109304/brown-v-illinois/"
  cluster_id: 109304
  opinion_id: 109304
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Wong Sun v. United States]]", "[[Utah v. Strieff]]", "[[Dunaway v. New York]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "attenuation", "fruit-of-the-poisonous-tree"]
holding: "Sets out the attenuation factors: temporal proximity, intervening circumstances, and the purpose and flagrancy of the official…"
lake:
  record_id: Brown v. Illinois
  status: verified
  projected_at: 2026-07-06
---

# Brown v. Illinois

*422 U.S. 590 (1975)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers arrested Brown without probable cause or a warrant, broke into and waited in his apartment, then took him to the station, gave [[Miranda and Custodial Interrogation|Miranda warnings]], and obtained two inculpatory statements within about two hours. The Illinois courts treated the [[Miranda and Custodial Interrogation|Miranda warnings]] as automatically dissipating the taint of the unlawful arrest.

## Issue
Whether [[Miranda and Custodial Interrogation|Miranda warnings]], by themselves, break the causal chain between an illegal arrest and a subsequent confession so as to make the confession admissible under the Fourth Amendment.

## Rule
[[Miranda and Custodial Interrogation|Miranda warnings]] do not automatically purge the taint: "The Miranda warnings are an important factor, to be sure, in determining whether the confession is obtained by exploitation of an illegal arrest. But they are not the only factor to be considered." — 422 U.S. at 603. ^pin-603

Voluntariness aside, [[Fruits and Attenuation|attenuation]] turns on a multi-factor inquiry: "The temporal proximity of the arrest and the confession, the presence of intervening circumstances, . . . and, particularly, the purpose and flagrancy of the official misconduct . . . are all relevant." — *Id.* at 603-604. ^pin-604

## Application
Brown's first statement came less than two hours after the illegal arrest, with no significant intervening event, and the arrest had a purposeful, investigatory quality. Weighing those factors, the State failed to show the statements were sufficiently attenuated from the unlawful arrest, so the [[Miranda and Custodial Interrogation|Miranda warnings]] alone did not make them admissible.

## Conclusion
[[Miranda and Custodial Interrogation|Miranda warnings]] do not [[Common Legal Terms#per-se|per se]] purge the taint of an illegal arrest; the statements should have been suppressed, and the judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. The *Brown* [[Fruits and Attenuation|attenuation]] factors remain the governing framework and were applied in [[Utah v. Strieff]].

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *Brown v. Illinois*, 422 U.S. 590 (1975) — https://www.courtlistener.com/opinion/109304/brown-v-illinois/ — pinpoints: 603, 604.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e3cdcca61b5aa549", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "422 U.S. 590 (1975)", "court": "U.S. Supreme Court", "neutral_cite": "1975 U.S. LEXIS 82", "official_citation_present": true, "parallel_cite": "95 S. Ct. 2254; 45 L. Ed. 2d 416", "title": "Brown v. Illinois", "year": "1975"}}
{"assertion_id": "00f47683cd516eb6", "dimension": "support", "kind": "home_role", "locator": {"home": "Fruits & Attenuation"}, "payload": {"home": "Fruits & Attenuation", "role": "Key — Progeny / Refinement", "title": "Brown v. Illinois"}}
{"assertion_id": "eeb39671a8ddfd66", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Sets out the attenuation factors: temporal proximity, intervening circumstances, and the purpose and flagrancy of the official…", "title": "Brown v. Illinois"}}
{"assertion_id": "56b2f472a101d48f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1975-06-26", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Brown v. Illinois", "field_i_validity": "good_law", "scope_note": "Attenuation factors remain the governing test; applied in Utah v. Strieff.", "title": "Brown v. Illinois", "varies_by_point": "false"}}
{"assertion_id": "93d6097b78b04f55", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Brown v. Illinois"}}
```

### lake record — Brown v. Illinois

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brown v. Illinois",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Brown v. Illinois",
    "case_name_short": "Brown",
    "case_name_full": "Brown v. Illinois",
    "input_case_name": "Brown v. Illinois",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1975-06-26",
    "year": 1975,
    "docket": "73-6650",
    "cluster_id": 109304,
    "lead_opinion_id": 109304,
    "sibling_ids": [
      109304,
      9426178,
      9426179,
      9426180
    ],
    "absolute_url": "/opinion/109304/brown-v-illinois/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "422 U.S. 590",
      "volume": "422",
      "reporter": "U.S.",
      "page": "590",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "95 S. Ct. 2254",
        "volume": "95",
        "reporter": "S. Ct.",
        "page": "2254",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "45 L. Ed. 2d 416",
        "volume": "45",
        "reporter": "L. Ed. 2d",
        "page": "416",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1975 U.S. LEXIS 82",
        "volume": "1975",
        "reporter": "U.S. LEXIS",
        "page": "82",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "422 U.S. 590",
        "volume": "422",
        "reporter": "U.S.",
        "page": "590",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "95 S. Ct. 2254",
        "volume": "95",
        "reporter": "S. Ct.",
        "page": "2254",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "45 L. Ed. 2d 416",
        "volume": "45",
        "reporter": "L. Ed. 2d",
        "page": "416",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1975 U.S. LEXIS 82",
        "volume": "1975",
        "reporter": "U.S. LEXIS",
        "page": "82",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "422 U.S. 590",
    "official_selection": {
      "court_class": "scotus",
      "selected": "422 U.S. 590",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-603",
      "page": null,
      "quote": "--- # Brown v. Illinois *422 U.S. 590 (1975)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers arrested Brown without probable cause or a warrant, broke into and waited in his apartment, then took him to the station, gave Miranda warnings, and obtained two inculpatory statements within about two hours. The Illinois courts treated the Miranda warnings as automatically dissipating the taint of the unlawful arrest. ## Issue Whether Miranda warnings, by themselves, break the causal chain between an illegal arrest and a subsequent confession so as to make the confession admissible under the Fourth Amendment. ## Rule Miranda warnings do not automatically purge the taint:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-604",
      "page": null,
      "quote": "The temporal proximity of the arrest and the confession, the presence of intervening circumstances, . . . and, particularly, the purpose and flagrancy of the official misconduct . . . are all relevant.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1975-06-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Brown v. Illinois",
    "varies_by_point": false,
    "scope_note": "Attenuation factors remain the governing test; applied in Utah v. Strieff.",
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
        "journal_ref": "Brown v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Privette",
          "cluster_id": 9387170,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Christian",
          "cluster_id": 4643309,
          "cite": [
            "445 P.3d 183"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Fredericq",
          "cluster_id": 4613398,
          "cite": [
            "121 N.E.3d 166",
            "482 Mass. 70"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Serrano-Acevedo",
          "cluster_id": 4506969,
          "cite": [
            "892 F.3d 454"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Muldrow",
          "cluster_id": 4448772,
          "cite": [
            "2017 Ohio 8839",
            "100 N.E.3d 1093"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Turpin",
          "cluster_id": 4423584,
          "cite": [
            "2017 Ohio 7435",
            "96 N.E.3d 1171"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Matthew Elliot Cohagan",
          "cluster_id": 4421478,
          "cite": [
            "162 Idaho 717",
            "404 P.3d 659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane1_negative"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wallace v. Kato",
          "cluster_id": 145756,
          "cite": [
            "127 S. Ct. 1091",
            "549 U.S. 384"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Browder v. Director, Dept. of Corrections of Ill.",
          "cluster_id": 109761,
          "cite": [
            "54 L. Ed. 2d 521",
            "98 S. Ct. 556",
            "434 U.S. 257",
            "1978 U.S. LEXIS 53"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Watson",
          "cluster_id": 109352,
          "cite": [
            "46 L. Ed. 2d 598",
            "96 S. Ct. 820",
            "423 U.S. 411",
            "1976 U.S. LEXIS 121"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Crews",
          "cluster_id": 110230,
          "cite": [
            "63 L. Ed. 2d 537",
            "100 S. Ct. 1244",
            "445 U.S. 463",
            "1980 U.S. LEXIS 1293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Spring",
          "cluster_id": 111798,
          "cite": [
            "93 L. Ed. 2d 954",
            "107 S. Ct. 851",
            "479 U.S. 564",
            "1987 U.S. LEXIS 418",
            "55 U.S.L.W. 4162"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Johnson",
          "cluster_id": 110754,
          "cite": [
            "73 L. Ed. 2d 202",
            "102 S. Ct. 2579",
            "457 U.S. 537",
            "1982 U.S. LEXIS 134",
            "50 U.S.L.W. 4742"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Henry",
          "cluster_id": 110300,
          "cite": [
            "65 L. Ed. 2d 115",
            "100 S. Ct. 2183",
            "447 U.S. 264",
            "1980 U.S. LEXIS 111"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Payner",
          "cluster_id": 110317,
          "cite": [
            "65 L. Ed. 2d 468",
            "100 S. Ct. 2439",
            "447 U.S. 727",
            "1980 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109304 OR 9426178 OR 9426179 OR 9426180) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDk1NjcwNDAwMDAwJnM9NDM5NTYxMSZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109304+OR+9426178+OR+9426179+OR+9426180%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 8,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(109304 OR 9426178 OR 9426179 OR 9426180)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00ODAmcz02MDY2ODkmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109304+OR+9426178+OR+9426179+OR+9426180%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109304 OR 9426178 OR 9426179 OR 9426180)",
        "reviewed": 52,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 52,
        "triage_read": 1,
        "triage_snippet_classified": 51
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109304 OR 9426178 OR 9426179 OR 9426180)",
    "indexed_citing_opinions": 3078,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109304,
        "count": 2757,
        "count_source": "search"
      },
      {
        "opinion_id": 9426178,
        "count": 410,
        "count_source": "search"
      },
      {
        "opinion_id": 9426179,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426180,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4589,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/brown-v-illinois.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxMDM1MzImcz0xMDI4NjMwNiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109304+OR+9426178+OR+9426179+OR+9426180%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109304,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 106699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 108139,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 108538,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 108794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 268537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 268701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 292479,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 297732,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 302281,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 313628,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 317292,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 2060189,
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
    "date_created": "2026-07-04T20:42:31Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:42:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:42:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:48:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:42:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Brown v. Illinois

```
<div>
<center><b><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U.S. 590</a></span> (1975)</b></center>
<center><h1>BROWN<br>
v.<br>
ILLINOIS.</h1></center>
<center>No. 73-6650.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 18, 1975.</center>
<center>Decided June 26, 1975.</center>
CERTIORARI TO THE SUPREME COURT OF ILLINOIS.
<p><span class="star-pagination">*591</span> <i>Robert P. Isaacson</i> argued the cause for petitioner <i>pro hac vice.</i> With him on the brief were <i>James J. Doherty</i> and <i>John T. Moran.</i></p>
<p><i>Jayne A. Carr,</i> Assistant Attorney General of Illinois, argued the cause for respondent. With her on the brief were <i>William J. Scott,</i> Attorney General, and <i>James B. Zagel,</i> Assistant Attorney General.<sup>[*]</sup></p>
<p>MR. JUSTICE BLACKMUN delivered the opinion of the Court.</p>
<p>This case lies at the crossroads of the Fourth and the Fifth Amendments. Petitioner was arrested without probable cause and without a warrant. He was given, in full, the warnings prescribed by <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Thereafter, while in custody, he made two inculpatory statements. The issue is whether evidence of those statements was properly admitted, or should have been excluded, in petitioner's subsequent trial for murder in state court. Expressed another way, the issue is whether the statements were to be excluded <span class="star-pagination">*592</span> as the fruit of the illegal arrest, or were admissible because the giving of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings sufficiently attenuated the taint of the arrest. See <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963). The Fourth Amendment, of course, has been held to be applicable to the States through the Fourteenth Amendment. <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961).</p>
<p></p>
<h2>I</h2>
<p>As petitioner Richard Brown was climbing the last of the stairs leading to the rear entrance of his Chicago apartment in the early evening of May 13, 1968, he happened to glance at the window near the door. He saw, pointed at him through the window, a revolver held by a stranger who was inside the apartment. The man said: "Don't move, you are under arrest." App. 42. Another man, also with a gun, came up behind Brown and repeated the statement that he was under arrest. It was about 7:45 p. m. The two men turned out to be Detectives William Nolan and William Lenz of the Chicago police force. It is not clear from the record exactly when they advised Brown of their identity, but it is not disputed that they broke into his apartment, searched it, and then arrested Brown, all without probable cause and without any warrant, when he arrived. They later testified that they made the arrest for the purpose of questioning Brown as part of their investigation of the murder of a man named Roger Corpus.</p>
<p>Corpus was murdered one week earlier, on May 6, with a .38-caliber revolver in his Chicago West Side second-floor apartment. Shortly thereafter, Detective Lenz obtained petitioner's name, among others, from Corpus' brother. Petitioner and the others were identified as acquaintances of the victim, not as suspects.<sup>[1]</sup></p>
<p><span class="star-pagination">*593</span> On the day of petitioner's arrest. Detectives Lenz and Nolan, armed with a photograph of Brown, and another officer arrived at petitioner's apartment about 5 p. m. App. 77, 78. While the third officer covered the front entrance downstairs, the two detectives broke into Brown's apartment and searched it. <i>Id.,</i> at 86. Lenz then positioned himself near the rear door and watched through the adjacent window which opened onto the back porch. Nolan sat near the front door. He described the situation at the later suppression hearing:</p>
<blockquote>"After we were there for a while, Detective Lenz told me that somebody was coming up the back stairs. I walked out the front door through the hall and around the corner, and I stayed there behind a door leading on to the back porch. At this time I heard Detective Lenz say, `Don't move, you are under arrest.' I looked out. I saw Mr. Brown backing away from the window. I walked up behind him, I told him he is under arrest, come back inside the apartment with us." <i>Id.,</i> at 42.</blockquote>
<p>As both officers held him at gunpoint, the three entered the apartment. Brown was ordered to stand against the wall and was searched. No weapon was found. <i>Id.,</i> at 93. He was asked his name. When he denied being Richard Brown, Detective Lenz showed him the photograph, informed him that he was under arrest for the murder of Roger Corpus, <i>id.,</i> at 16, handcuffed him, <i>id.,</i> at 93, and escorted him to the squad car.</p>
<p>The two detectives took petitioner to the Maxwell Street police station. During the 20-minute drive Nolan again asked Brown, who then was sitting with him in the back seat of the car, whether his name was Richard Brown and whether he owned a 1966 Oldsmobile. Brown <span class="star-pagination">*594</span> alternately evaded these questions or answered them falsely. Tr. 74. Upon arrival at the station house Brown was placed in the second-floor central interrogation room. The room was bare, except for a table and four chairs. He was left alone, apparently without handcuffs, for some minutes while the officers obtained the file on the Corpus homicide. They returned with the file, sat down at the table, one across from Brown and the other to his left, and spread the file on the table in front of him. App. 19.</p>
<p>The officers warned Brown of his rights under <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i><sup>[2]</sup><i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i> They then informed him that they knew of an incident that had occurred in a poolroom on May 5, when Brown, angry at having been cheated at dice, fired a shot from a revolver into the ceiling. Brown answered: "Oh, you know about that." <i>Id.,</i> at 20. Lenz informed him that a bullet had been obtained from the ceiling of the poolroom and had been taken to the crime laboratory to be compared with bullets taken from Corpus' body.<sup>[3]</sup><i>Ibid.</i> Brown responded: "Oh, you know that, too." <i>Id.,</i> at 20-21. At this pointit was about 8:45 p. m.Lenz asked Brown whether he wanted to talk about the Corpus homicide. Petitioner answered that he did. For the next 20 to 25 minutes Brown answered questions put to him by Nolan, as Lenz typed. <i>Id.,</i> at 21-23.</p>
<p>This questioning produced a two-page statement in which Brown acknowledged that he and a man named <span class="star-pagination">*595</span> Jimmy Claggett visited Corpus on the evening of May 5; that the three for some time sat drinking and smoking marihuana; that Claggett ordered him at gunpoint to bind Corpus' hands and feet with cord from the headphone of a stereo set; and that Claggett, using a .38-caliber revolver sold to him by Brown, shot Corpus three times through a pillow. The statement was signed by Brown. <i>Id.,</i> at 9, 38.</p>
<p>About 9:30 p. m. the two detectives and Brown left the station house to look for Claggett in an area of Chicago Brown knew him to frequent. They made a tour of that area but did not locate their quarry. They then went to police headquarters where they endeavored, without success, to obtain a photograph of Claggett. They resumed their searchit was now about 11 p. m.and they finally observed Claggett crossing at an intersection. Lenz and Nolan arrested him. All four, the two detectives and the two arrested men, returned to the Maxwell Street station about 12:15 a. m. <i>Id.,</i> at 39.</p>
<p>Brown was again placed in the interrogation room. He was given coffee and was left alone, for the most part, until 2 a. m. when Assistant State's Attorney Crilly arrived.</p>
<p>Crilly, too, informed Brown of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. After a half hour's conversation, a court reporter appeared. Once again the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings were given: "I read him the card." <i>Id.,</i> at 30. Crilly told him that he "was sure he would be charged with murder." <i>Id.,</i> at 32. Brown gave a second statement, providing a factual account of the murder substantially in accord with his first statement, but containing factual inaccuracies with respect to his personal background.<sup>[4]</sup> When the statement <span class="star-pagination">*596</span> was completed, at about 3 a. m., Brown refused to sign it. <i>Id.,</i> at 57. An hour later he made a phone call to his mother. At 9:30 that morning, about 14 hours after his arrest, he was taken before a magistrate.</p>
<p>On June 20 Brown and Claggett were jointly indicted by a Cook County grand jury for Corpus' murder. Prior to trial, petitioner moved to suppress the two statements he had made. He alleged that his arrest and detention had been illegal and that the statements were taken from him in violation of his constitutional rights. After a hearing, the motion was denied. R. 46.</p>
<p>The case proceeded to trial. The State introduced evidence of both statements. Detective Nolan testified as to the contents of the first, App. 89-92, but the writing itself was not placed in evidence. The second statement was introduced and was read to the jury in full. Tr. 509-528. Brown was 23 at the time of the trial. <i>Id.,</i> at 543.</p>
<p>The jury found petitioner guilty of murder. R. 80., He was sentenced to imprisonment for not less than 15 years nor more than 30 years. <i>Id.,</i> at 83.</p>
<p>On appeal, the Supreme Court of Illinois affirmed the judgment of conviction. <span class="citation" data-id="2060189"><a href="/opinion/2060189/people-v-brown/" aria-description="Citation for case: People v. Brown">56 Ill. 2d 312</a></span>, <span class="citation" data-id="2060189"><a href="/opinion/2060189/people-v-brown/" aria-description="Citation for case: People v. Brown">307 N. E. 2d 356</a></span> (1974). The court refused to accept the State's argument that Brown's arrest was lawful. "Upon review of the record, we conclude that the testimony fails to show that at the time of his apprehension there was probable cause for defendant's arrest, [and] that his arrest was, therefore, unlawful." <span class="citation" data-id="2060189"><a href="/opinion/2060189/people-v-brown/#315" aria-description="Citation for case: People v. Brown"><i>Id.,</i> at 315</a></span>, 307 N. E. <span class="star-pagination">*597</span> 2d, at 357. But it went on to hold in two significant and unembellished sentences:</p>
<blockquote>"[W]e conclude that the giving of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, in the first instance by the police officer and in the second by the assistant State's Attorney, served to break the causal connection between the illegal arrest and the giving of the statements, and that defendant's act in making the statements was `sufficiently an act of free will to purge the primary taint of the unlawful invasion.' (<i>Wong Sun v. United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, at 486</a></span>.) We hold, therefore, that the circuit court did not err in admitting the statements into evidence." <i>Id.,</i> at 317, <span class="citation" data-id="2060189"><a href="/opinion/2060189/people-v-brown/#358" aria-description="Citation for case: People v. Brown">307 N. E. 2d, at 358</a></span>.</blockquote>
<p>Aside from its reliance upon the presence of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, no specific aspect of the record or of the circumstances was cited by the court in support of its conclusion. The court, in other words, appears to have held that the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings in and of themselves broke the causal chain so that any subsequent statement, even one induced by the continuing effects of unconstitutional custody, was admissible so long as, in the traditional sense, it was voluntary and not coerced in violation of the Fifth and Fourteenth Amendments.</p>
<p>Because of our concern about the implication of our holding in <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), to the facts of Brown's case, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./419/894/">419 U. S. 894</a></span> (1974).</p>
<p></p>
<h2>II</h2>
<p>In <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>,</i> the Court pronounced the principles to be applied where the issue is whether statements and other evidence obtained after an illegal arrest or search should be excluded. In that case, federal agents elicited an oral statement from defendant Toy after forcing entry <span class="star-pagination">*598</span> at 6 a. m. into his laundry, at the back of which he had his living quarters. The agents had followed Toy down the hall to the bedroom and there had placed him under arrest. The Court of Appeals found that there was no probable cause for the arrest. This Court concluded that finding was "amply justified by the facts clearly shown on this record." <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#479" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 479</a></span>. Toy's statement, which bore upon his participation in the sale of narcotics, led the agents to question another person, Johnny Yee, who actually possessed narcotics. Yee stated that heroin had been brought to him earlier by Toy and another Chinese known to him only as "Sea Dog." Under questioning, Toy said that "Sea Dog" was Wong Sun. Toy led agents to a multifamily dwelling where, he said, Wong Sun lived. Gaining admittance to the building through a bell and buzzer, the agents climbed the stairs and entered the apartment. One went into the back room and brought Wong Sun out in hand-cuffs. After arraignment, Wong Sun was released on his own recognizance. Several days later, he returned voluntarily to give an unsigned confession.</p>
<p>This Court ruled that Toy's declarations and the contraband taken from Yee were the fruits of the agents' illegal action and should not have been admitted as evidence against Toy. <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#484" aria-description="Citation for case: Wong Sun v. United States"><i>Id.,</i> at 484-488</a></span>. It held that the statement did not result from " `an intervening independent act of a free will,' " and that it was not "sufficiently an act of free will to purge the primary taint of the unlawful invasion." <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States"><i>Id.,</i> at 486</a></span>. With respect to Wong Sun's confession, however, the Court held that in the light of his lawful arraignment and release on his own recognizance, and of his return voluntarily several days later to make the statement, the connection between his unlawful arrest and the statement "had `become so attenuated as to dissipate the taint.' <i>Nardone</i> v. <i>United</i> <span class="star-pagination">*599</span> <i>States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span>." <i>Id.,</i> at 491. The Court said:</p>
<blockquote>"We need not hold that all evidence is `fruit of the poisonous tree' simply because it would not have come to light but for the illegal actions of the police. Rather, the more apt question in such a case is `whether, granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint'. Maguire, Evidence of Guilt, 221 (1959)." <i>Id.,</i> at 487-488.</blockquote>
<p>The exclusionary rule thus was applied in <i>Wong Sun primarily</i> to protect Fourth Amendment rights. Protection of the Fifth Amendment right against self-incrimination was not the Court's paramount concern there. To the extent that the question whether Toy's statement was voluntary was considered, it was only to judge whether it "was <i>sufficiently</i> an act of free will to purge the primary taint of the unlawful invasion." <i>Id.,</i> at 486 (emphasis added).</p>
<p>The Court in <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>,</i> as is customary, emphasized that application of the exclusionary rule on Toy's behalf protected Fourth Amendment guarantees in two respects: "in terms of deterring lawless conduct by federal officers," and by "closing the doors of the federal courts to any use of evidence unconstitutionally obtained." <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Ibid.</a></span></i> These considerations of deterrence and of judicial integrity, by now, have become rather commonplace in the Court's cases. See <i>e. g., United States</i> v. <i>Peltier, ante,</i> at 535-538; <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#347" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 347</a></span> (1974); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#12" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 12-13, 28-29</a></span> (1968). "The rule is calculated to prevent, not to repair. Its purpose is to deterto compel respect for the <span class="star-pagination">*600</span> constitutional guaranty in the only effectively available wayby removing the incentive to disregard it." <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#217" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 217</a></span> (1960). But "[d]espite its broad deterrent purpose, the exclusionary rule has never been interpreted to proscribe the use of illegally seized evidence in all proceedings or against all persons." <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S., at 348</a></span>. See also <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#446" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 446-447</a></span> (1974).<sup>[5]</sup></p>
<p></p>
<h2>III</h2>
<p>The Illinois courts refrained from resolving the question, as apt here as it was in <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>,</i> whether Brown's statements were obtained by exploitation of the illegality of his arrest. They assumed that the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, by themselves, assured that the statements (verbal acts, as contrasted with physical evidence) were of sufficient free will as to purge the primary taint of the unlawful arrest. <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>,</i> of course, preceded <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i></p>
<p>This Court has described the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings as a "prophylactic rule", <i>Michigan</i> v. <i>Payne,</i> <span class="citation" data-id="8985601"><a href="/opinion/8993355/michigan-v-payne/#53" aria-description="Citation for case: Michigan v. Payne">412 U. S. 47, 53</a></span> (1973), and as a "procedural safeguard," <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#457" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 457, 478</a></span>, employed to protect Fifth Amendment rights against "the compulsion inherent in custodial surroundings." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#458" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 458</a></span>. The function of the warnings relates to the Fifth Amendment's guarantee against coerced self-incrimination, and the exclusion <span class="star-pagination">*601</span> of a statement made in the absence of the warnings, it is said, serves to deter the taking of an incriminating statement without first informing the individual of his Fifth Amendment rights.</p>
<p>Although, almost 90 years ago, the Court observed that the Fifth Amendment is in "intimate relation" with the Fourth, <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#633" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 633</a></span> (1886), the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings thus far have not been regarded as a means either of remedying or deterring violations of Fourth Amendment rights. Frequently, as here, rights under the two Amendments may appear to coalesce since "the `unreasonable searches and seizures' condemned in the Fourth Amendment are almost always made for the purpose of compelling a man to give evidence against himself, which in criminal cases is condemned in the Fifth Amendment." <i>Ibid.;</i> see <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 646</a></span> n. 5. The exclusionary rule, however, when utilized to effectuate the Fourth Amendment, serves interests and policies that are distinct from those it serves under the Fifth. It is directed at all unlawful searches and seizures, and not merely those that happen to produce incriminating material or testimony as fruits. In short, exclusion of a confession made without <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings might be regarded as necessary to effectuate the Fifth Amendment, but it would not be sufficient fully to protect the Fourth. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, and the exclusion of a confession made without them, do not alone sufficiently deter a Fourth Amendment violation.<sup>[6]</sup></p>
<p>Thus, even if the statements in this case were found to be voluntary under the Fifth Amendment, the Fourth <span class="star-pagination">*602</span> Amendment issue remains. In order for the causal chain, between the illegal arrest and the statements made subsequent thereto, to be broken, <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> requires not merely that the statement meet the Fifth Amendment standard of voluntariness but that it be "sufficiently an act of free will to purge the primary taint." <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 486</a></span>. <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> thus mandates consideration of a statement's admissibility in light of the distinct policies and interests of the Fourth Amendment.</p>
<p>If <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, by themselves, were held to attenuate the taint of an unconstitutional arrest, regardless of how wanton and purposeful the Fourth Amendment violation, the effect of the exclusionary rule would be substantially diluted. See <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#726" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 726-727</a></span> (1969). Arrests made without warrant or without probable cause, for questioning or "investigation," would be encouraged by the knowledge that evidence derived therefrom could well be made admissible at trial by the simple expedient of giving <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings.<sup>[7]</sup> Any incentive to avoid Fourth Amendment violations would be eviscerated by making the warnings, in effect, a "cure-all," and the constitutional guarantee against unlawful searches and seizures could <span class="star-pagination">*603</span> be said to be reduced to "a form of words". See <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#648" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 648</a></span>.</p>
<p>It is entirely possible, of course, as the State here argues, that persons arrested illegally frequently may decide to confess as an act of free will unaffected by the initial illegality. But the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, <i>alone</i> and <i>per se,</i> cannot always make the act sufficiently a product of free will to break, for Fourth Amendment purposes, the causal connection between the illegality and the confession. They cannot assure in every case that the Fourth Amendment violation has not been unduly exploited. See <i>Westover</i> v. <i>United States,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#496" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 496-497</a></span> (1966).</p>
<p>While we therefore reject the <i>per se</i> rule which the Illinois courts appear to have accepted, we also decline to adopt any alternative <i>per se</i> or "but for" rule. The petitioner himself professes not to demand so much. Tr. of Oral Arg. 12, 45, 47. The question whether a confession is the product of a free will under <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> must be answered on the facts of each case. No single fact is dispositive. The workings of the human mind are too complex, and the possibilities of misconduct too diverse, to permit protection of the Fourth Amendment to turn on such a talismanic test. The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings are an important factor, to be sure, in determining whether the confession is obtained by exploitation of an illegal arrest. But they are not the only factor to be considered. The temporal proximity of the arrest and the confession,<sup>[8]</sup> the presence of intervening circumstances, <span class="star-pagination">*604</span> see <i>Johnson</i> v. <i>Louisiana,</i> <span class="citation" data-id="9424879"><a href="/opinion/108538/johnson-v-louisiana/#365" aria-description="Citation for case: Johnson v. Louisiana">406 U. S. 356, 365</a></span> (1972), and, particularly, the purpose and flagrancy of the official misconduct<sup>[9]</sup> are all relevant. See <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#491" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 491</a></span>. The voluntariness of the statement is a threshold requirement. Cf. <span class="citation no-link">18 U. S. C. § 3501</span>. And the burden of showing admissibility rests, of course, on the prosecution.<sup>[10]</sup></p>
<p></p>
<h2>IV</h2>
<p>Although the Illinois courts failed to undertake the inquiry mandated by <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> to evaluate the circumstances of this case in the light of the policy served by the exclusionary rule, the trial resulted in a record of amply sufficient detail and depth from which the determination may be made. We therefore decline the suggestion of the United States, as <i>amicus curiae,</i> see <i>Morales</i> v. <i>New York,</i> <span class="citation" data-id="108004"><a href="/opinion/108004/morales-v-new-york/" aria-description="Citation for case: Morales v. New York">396 U. S. 102</a></span> (1969), to remand the case for further factual findings. We conclude that the State failed to sustain the burden of showing that the evidence in question was admissible under <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>.</i></p>
<p>Brown's first statement was separated from his illegal arrest by less than two hours, and there was no intervening event of significance whatsoever. In its essentials, his situation is remarkably like that of James Wah Toy in <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>.</i><sup>[11]</sup> We could hold Brown's first statement <span class="star-pagination">*605</span> admissible only if we overrule <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>.</i> We decline to do so. And the second statement was clearly the result and the fruit of the first.<sup>[12]</sup></p>
<p>The illegality here, moreover, had a quality of purposefulness. The impropriety of the arrest was obvious; awareness of that fact was virtually conceded by the two detectives when they repeatedly acknowledged, in their testimony, that the purpose of their action was "for investigation" or for "questioning."<sup>[13]</sup> App. 35, 43, 78, 81, 83, 88, 89, 94. The arrest, both in design and in execution, was investigatory. The detectives embarked upon this expedition for evidence in the hope that something might turn up. The manner in which Brown's arrest was effected gives the appearance of having been calculated to cause surprise, fright, and confusion.</p>
<p>We emphasize that our holding is a limited one. We decide only that the Illinois courts were in error in assuming that the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, by themselves, under <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> always purge the taint of an illegal arrest.</p>
<p>The judgment of the Supreme Court of Illinois is reversed and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p><span class="star-pagination">*606</span> MR. JUSTICE WHITE, concurring in the judgment.</p>
<p>Insofar as the Court holds (1) that despite <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings the Fourth and Fourteenth Amendments require the exclusion from evidence of statements obtained as the fruit of an arrest which the arresting officers knew or should have known was without probable cause and unconstitutional, and (2) that the statements obtained in this case were in this category, I am in agreement and therefore concur in the judgment.</p>
<p>MR. JUSTICE POWELL, with whom MR. JUSTICE REHNQUIST joins, concurring in part.</p>
<p>I join the Court insofar as it holds that the <i>per se</i> rule adopted by the Illinois Supreme Court for determining the admissibility of petitioner's two statements inadequately accommodates the diverse interests underlying the Fourth Amendment exclusionary rule. I would, however, remand the case for reconsideration under the general standards articulated in the Court's opinion and elaborated herein.</p>
<p></p>
<h2>A</h2>
<p>The issue presented in this case turns on proper application of the policies underlying the Fourth Amendment exclusionary rule, not on the Fifth Amendment or the prophylaxis added to that guarantee by <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966).<sup>[1]</sup> The Court recognized in <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), that the Fourth Amendment exclusionary rule applies to statements obtained following an illegal arrest just as it does to tangible evidence seized in a similar manner <span class="star-pagination">*607</span> or obtained pursuant to an otherwise illegal search and seizure. <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> squarely rejected, however, the suggestion that the admissibility of statements so obtained should be governed by a simple "but for" test that would render inadmissible all statements given subsequent to an illegal arrest. <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#487" aria-description="Citation for case: Wong Sun v. United States"><i>Id.,</i> at 487-488</a></span>. In a similar manner, the Court today refrains from according dispositive weight to the single factor of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. I agree with each holding. Neither of the rejected extremes adequately recognizes the competing considerations involved in a determination to exclude evidence after finding that official possession of that evidence was to some degree caused by a violation of the Fourth Amendment.</p>
<p>On this record, I cannot conclude as readily as the Court that admission of the statements here at issue would constitute an effective overruling of <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>.</i> See <i>ante,</i> at 604-605. Although <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> establishes the boundaries within which this case must be decided, the incompleteness of the record leaves me uncertain that it compels the exclusion of petitioner's statements. The statements at issue in <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> were on the temporal extremes in relation to the illegal arrest. Cf. <i>Collins</i> v. <i>Beto,</i> <span class="citation" data-id="9450950"><a href="/opinion/268701/clarence-collins-v-george-j-beto-director-texas-department-of/#832" aria-description="Citation for case: Clarence Collins v. George J. Beto, Director, Texas...">348 F. 2d 823, 832, 834-836</a></span> (CA5 1965) (Friendly, J., concurring). Toy's statement was obtained immediately after his pursuit and arrest by six agents. It appears to have been a spontaneous response to a question put to him in the frenzy of that event, and there is no indication that the agents made any attempt to inform him of his right to remain silent. Wong Sun's statement, by contrast, was not given until after he was arraigned and released on his own recognizance. Wong Sun voluntarily returned to the station a few days after the arrest for questioning. His statement was preceded by an official warning of his right <span class="star-pagination">*608</span> to remain silent and to have counsel if he desired.<sup>[2]</sup> The Court rejected the Government's assertion that Toy's statement resulted from an independent act of free will sufficient to purge the consequences of the illegal arrest. Wong Sun's statement, however, was deemed admissible. Given the circumstances in which Wong Sun's statement was obtained, the Court concluded that "the connection between the arrest and the statement had `become so attenuated as to dissipate the taint.' " <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#491" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 491</a></span>.</p>
<p>Like most cases in which the admissibility of statements obtained subsequent to an illegal arrest is contested, this case concerns statements more removed than that of Toy from the time and circumstances of the illegal arrest. Petitioner made his first statement some two hours following his arrest, after he had been given <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. The Court is correct in noting that no other significant intervening event altered the relationship established between petitioner and the officers by the illegal arrest. But the Court's conclusion that admission of this statement could be allowed only by overruling <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> rests either on an overly restrictive interpretation of the attenuation doctrine, to which I cannot subscribe, or on its view that the arrest was made for investigatory purposes, a factual determination that I think more appropriately should have been left for decision in the first instance by the state courts.</p>
<p></p>
<h2>B</h2>
<p>The Court's rejection in <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> of a "but for" test, reaffirmed today, <i>ante,</i> at 603-604, recognizes that in some <span class="star-pagination">*609</span> circumstances strict adherence to the Fourth Amendment exclusionary rule imposes greater cost on the legitimate demands of law enforcement than can be justified by the rule's deterrent purposes. The notion of the "dissipation of the taint" attempts to mark the point at which the detrimental consequences of illegal police action become so attenuated that the deterrent effect of the exclusionary rule no longer justifies its cost. Application of the <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> doctrine will generate fact-specific cases bearing distinct differences as well as similarities, and the question of attenuation inevitably is largely a matter of degree. The Court today identifies the general factors that the trial court must consider in making this determination. I think it appropriate, however, to attempt to articulate the possible relationships of those factors in particular, broad categories of cases.</p>
<p>All Fourth Amendment violations are, by constitutional definition, "unreasonable." There are, however, significant practical differences that distinguish among violations, differences that measurably assist in identifying the kinds of cases in which disqualifying the evidence is likely to serve the deterrent purposes of the exclusionary rule. Cf. <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#347" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 347-348</a></span> (1974); <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#250" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 250</a></span> (1973) (POWELL, J., concurring). In my view, the point at which the taint can be said to have dissipated should be related, in the absence of other controlling circumstances, to the nature of that taint.</p>
<p>That police have not succeeded in coercing the accused's confession through willful or negligent misuse of the power of arrest does not remove the fact that they may have tried. The impermissibility of the attempt, and the extent to which such attempts can be deterred by the use of the exclusionary rule, are of primary relevance in determining whether exclusion is an appropriate remedy. <span class="star-pagination">*610</span> The basic purpose of the rule, briefly stated, is to remove possible motivations for illegal arrests. Given this purpose the notion of voluntariness has practical value in deciding whether the rule should apply to statements removed from the immediate circumstances of the illegal arrest. If an illegal arrest merely provides the occasion of initial contact between the police and the accused, and because of time or other intervening factors the accused's eventual statement is the product of his own reflection and free will, application of the exclusionary rule can serve little purpose: the police normally will not make an illegal arrest in the hope of eventually obtaining such a truly volunteered statement. In a similar manner, the role of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings in the <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> inquiry is indirect. To the extent that they dissipate the psychological pressures of custodial interrogation, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings serve to assure that the accused's decision to make a statement has been relatively unaffected by the preceding illegal arrest. Correspondingly, to the extent that the police perceive <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings to have this equalizing potential, their motivation to abuse the power of arrest is diminished. Bearing these considerations in mind, and recognizing that the deterrent value of the Fourth Amendment exclusionary rule is limited to certain kinds of police conduct, the following general categories can be identified.</p>
<p>Those most readily identifiable are on the extremes: the flagrantly abusive violation of Fourth Amendment rights, on the one hand, and "technical" Fourth Amendment violations, on the other. In my view, these extremes call for significantly different judicial responses.</p>
<p>I would require the clearest indication of attenuation in cases in which official conduct was flagrantly abusive of Fourth Amendment rights. If, for example, the factors <span class="star-pagination">*611</span> relied on by the police in determining to make the arrest were so lacking in indicia of probable cause as to render official belief in its existence entirely unreasonable, or if the evidence clearly suggested that the arrest was effectuated as a pretext for collateral objectives, cf. <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#237" aria-description="Citation for case: United States v. Robinson">414 U. S. 218, 237</a></span>, 238 n. 2 (1973) (POWELL, J., concurring), or the physical circumstances of the arrest unnecessarily intrusive on personal privacy, I would consider the equalizing potential of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings rarely sufficient to dissipate the taint. In such cases the deterrent value of the exclusionary rule is most likely to be effective, and the corresponding mandate to preserve judicial integrity, see <i>United States</i> v. <i>Peltier, ante,</i> p. 531; <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433</a></span>, 450 n. 25 (1974), most clearly demands that the fruits of official misconduct be denied. I thus would require some demonstrably effective break in the chain of events leading from the illegal arrest to the statement, such as actual consultation with counsel or the accused's presentation before a magistrate for a determination of probable cause, before the taint can be deemed removed, see <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span> (1975); cf. <i>Johnson</i> v. <i>Louisiana,</i> <span class="citation" data-id="9424879"><a href="/opinion/108538/johnson-v-louisiana/#365" aria-description="Citation for case: Johnson v. Louisiana">406 U. S. 356, 365</a></span> (1972); <i>Parker</i> v. <i>North Carolina,</i> <span class="citation" data-id="9424258"><a href="/opinion/108139/parker-v-north-carolina/#796" aria-description="Citation for case: Parker v. North Carolina">397 U. S. 790, 796</a></span> (1970).</p>
<p>At the opposite end of the spectrum lie "technical" violations of Fourth Amendment rights where, for example, officers in good faith arrest an individual in reliance on a warrant later invalidated<sup>[3]</sup> or pursuant to a statute that subsequently is declared unconstitutional, see <i>United States</i> v. <i>Kilgen,</i> <span class="citation" data-id="297732"><a href="/opinion/297732/united-states-v-robert-h-kilgen-jr/" aria-description="Citation for case: United States v. Robert H. Kilgen, Jr.">445 F. 2d 287</a></span> (CA5 <span class="star-pagination">*612</span> 1971). As we noted in <i>Michigan</i> v. <i><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker, supra,</a></span></i> at 447: "The deterrent purpose of the exclusionary rule necessarily assumes that the police have engaged in willful, or at the very least negligent, conduct which has deprived the defendant of some right." In cases in which this underlying premise is lacking, the deterrence rationale of the exclusionary rule does not obtain, and I can see no legitimate justification for depriving the prosecution of reliable and probative evidence. Thus, with the exception of statements given in the immediate circumstances of the illegal arresta constraint I think is imposed by existing exclusionary-rule lawI would not require more than proof that effective <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings were given and that the ensuing statement was voluntary in the Fifth Amendment sense. Absent aggravating circumstances, I would consider a statement given at the station house after one has been advised of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights to be sufficiently removed from the immediate circumstances of the illegal arrest to justify its admission at trial.</p>
<p>Between these extremes lies a wide range of situations that defy ready categorization, and I will not attempt to embellish on the factors set forth in the Court's opinion other than to emphasize that the <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> inquiry always should be conducted with the deterrent purpose of the Fourth Amendment exclusionary rule sharply in focus. See ALI Model Code of Pre-Arraignment Procedure, Art. 150, p. 54 <i>et seq.</i> and Commentary thereon, p. 375 <i>et seq.</i> (Prop. Off. Draft 1975). And, in view of the inevitably fact-specific nature of the inquiry, we must place primary reliance on the "learning, good sense, fairness and courage" of judges who must make the determination in the first instance. <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#342" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 342</a></span> (1939). See <i>ante,</i> at 604 n. 10.</p>
<p></p>
<h2>
<span class="star-pagination">*613</span> C</h2>
<p>On the facts of record as I view them, it is possible that the police may have believed reasonably that there was probable cause for petitioner's arrest. Although the trial court conducted hearings on petitioner's motion to suppress and received his testimony and that of the arresting officers, its inquiry focused on determining whether petitioner's statements were preceded by adequate <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and were made voluntarily. The court did not inquire into the possible justification, actual or perceived, for the arrest. Indeed, numerous questions addressed to the circumstances of the arrest elicited the State's objection, which was sustained. App. 14-15. The Illinois Supreme Court's consideration of the factual basis for its ruling similarly failed to focus on these relevant issues or to rest in any meaningful sense on the factors set forth in the Court's opinion today. After determining that the officers lacked probable cause for petitioner's arrest, the Illinois court concluded simply that examination of the record persuaded it that "the giving of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings . . . served to break the causal connection between the illegal arrest and the giving of the statements." <span class="citation" data-id="2060189"><a href="/opinion/2060189/people-v-brown/#317" aria-description="Citation for case: People v. Brown">56 Ill. 2d 312, 317</a></span>, <span class="citation" data-id="2060189"><a href="/opinion/2060189/people-v-brown/#358" aria-description="Citation for case: People v. Brown">307 N. E. 2d 356, 358</a></span> (1974).</p>
<p>I am not able to conclude on this record that the officers arrested petitioner solely for the purpose of questioning, <i>ante,</i> at 605; see also <i>ante,</i> at 606 (WHITE, J., concurring in judgment). To be sure, there is evidence suggesting, as the Court notes, an investigatory arrest. The strongest evidence on that point is the inconclusive testimony by the arresting officers themselves. But the evidence is conflicting. Responding to questions as to what they told petitioner upon his arrest, the officers testified he was advised that the arrest was for investigation of murder. Responding to more pointed questions, <span class="star-pagination">*614</span> however, one of the arresting officers stated that he informed petitioner that he was being arrested for murder. See App. 16.<sup>[4]</sup></p>
<p>Moreover, other evidence of record indicates that the police may well have believed that probable cause existed to think that petitioner committed the crime of which he ultimately was convicted. As the opinion of the Illinois Supreme Court reveals, petitioner had been identified as an acquaintance of the deceased, and the police had been told that petitioner was seen in the building where the deceased lived on the day of the murder. <span class="citation" data-id="2060189"><a href="/opinion/2060189/people-v-brown/#315" aria-description="Citation for case: People v. Brown">56 Ill. 2d, at 315</a></span>, <span class="citation" data-id="2060189"><a href="/opinion/2060189/people-v-brown/#357" aria-description="Citation for case: People v. Brown">307 N. E. 2d, at 357</a></span>. It is also plain that the investigation had begun to focus on petitioner. For example, the police had gone to the trouble of obtaining a bullet that petitioner had fired in an unrelated incident for the purpose of comparing it with the bullets that killed the victim. App. 20. The officers also obtained petitioner's photograph prior to seeking him out, and the circumstances of petitioner's arrest indicate that their suspicions of him were quite pronounced.</p>
<p>The trial court made no determination as to whether probable cause existed for petitioner's arrest.<sup>[5]</sup> The Illinois <span class="star-pagination">*615</span> Supreme Court resolved that issue, but did not consider whether the officers might reasonably, albeit erroneously, have thought that probable cause existed. Rather than decide those matters for the first time at this level, I think it preferable to allow the state courts to reconsider the case under the general guidelines expressed in today's opinions.<sup>[6]</sup> I therefore would remand for reconsideration<sup>[7]</sup> with directions to conduct such further factual <span class="star-pagination">*616</span> inquiries as may be necessary to resolve the admissibility issue.</p>
<h2>NOTES</h2>
<p>[*]  <i>Solicitor General Bork</i> and <i>Acting Assistant Attorney General Keeney</i> filed a memorandum for the United States as <i>amicus curiae.</i></p>
<p>[1]  The brother, however, when asked at the trial whether any of the victim's family suggested to the police that petitioner was possibly responsible for the victim's death, answered: "Nobody asked." App. 74.</p>
<p>[2]  There is no assertion here that he did not understand those rights.</p>
<p>[3]  It was stipulated at the trial that if expert testimony were taken, it would be to the effect that the bullet eventually was ascertained to be a "wiped bullet," that is, that its sides were "clean and therefore it was not ballistically comparable to any other bullets, specifically the bullets taken from the body of the deceased, Roger Corpus." Tr. 543.</p>
<p>[4]  In response to questions from Mr. Crilly, Brown stated that he was employed at E. I. Guffman Company in Niles, Ill., and that he was a punch press operator, App. 97, whereas he later conceded that he worked at Arnold Schwinn Bicycle Company and had never worked at any other place. <i>Id.,</i> at 63. He also remarked in the Crilly statement that he had completed three years of high school, <i>id.,</i> at 96, whereas later he conceded that he "never went to high school." <i>Id.,</i> at 58.</p>
<p>[5]  Members of the Court on occasion have indicated disenchantment with the rule. See, <i>e. g., </i><i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#490" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 490</a></span> (1971) (Harlan, J., concurring); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#492" aria-description="Citation for case: Coolidge v. New Hampshire"><i>id.,</i> at 492</a></span> (BURGER, C. J., dissenting in part and concurring in part); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#493" aria-description="Citation for case: Coolidge v. New Hampshire"><i>id.,</i> at 493</a></span> (Black, J., concurring and dissenting); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#510" aria-description="Citation for case: Coolidge v. New Hampshire"><i>id.,</i> at 510</a></span> (WHITE, J., concurring and dissenting); <i>Bivens</i> v. <i>Six Unknown Federal Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#411" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388, 411</a></span> (1971) (BURGER, C. J., dissenting). Its efficacy has been subject to some dispute. <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">414 U. S. 338</a></span>, 348 n. 5 (1974). See <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#218" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 218</a></span> (1960).</p>
<p>[6]  The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings in no way inform a person of his Fourth Amendment rights, including his right to be released from unlawful custody following an arrest made without a warrant or without probable cause.</p>
<p>[7]  A great majority of the commentators have taken the same position. See, <i>e. g.,</i> Pitler, "The Fruit of the Poisonous Tree" Revisited and Shepardized, <span class="citation no-link">56 Calif. L. Rev. 579</span>, 603-604 (1968); Ruffin, Out on a Limb of the Poisonous Tree: The Tainted Witness, 15 U. C. L. A. L. Rev. 32, 70 (1967); Comment, 1 Fla. St. L. Rev. 533, 539-540 (1973); Note, Admissibility of Confessions Made Subsequent to an Illegal Arrest: Wong Sun v. United States Revisited, 61 J. Crim. L. 207, 212 n. 58 (1970); Comment, Scope of Taint Under the Exclusionary Rule of the Fifth Amendment Privilege Against Self-Incrimination, <span class="citation no-link">114 U. Pa. L. Rev. 570</span>, 574 (1966). But see Comment, Voluntary Incriminating Statements Made Subsequent to an Illegal ArrestA Proposed Modification of the Exclusionary Rule, <span class="citation no-link">71 Dick. L. Rev. 573</span>, 582-583 (1967).</p>
<p>[8]  See <i>United States</i> v. <i>Owen,</i> <span class="citation" data-id="317292"><a href="/opinion/317292/united-states-v-william-e-owen-jr-frederick-morse-allen-joseph-g/#1107" aria-description="Citation for case: United States v. William E. Owen, Jr., Frederick Morse...">492 F. 2d 1100, 1107</a></span> (CA5), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./419/965/">419 U. S. 965</a></span> (1974); <i>Hale</i> v. <i>Henderson,</i> <span class="citation" data-id="9459888"><a href="/opinion/313628/albert-william-hale-v-c-murray-henderson-warden-tennessee-state/#267" aria-description="Citation for case: Albert William Hale v. C. Murray Henderson, Warden...">485 F. 2d 266, 267-269</a></span> (CA6 1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./415/930/">415 U. S. 930</a></span> (1974); <i>United States</i> v. <i>Fallon,</i> <span class="citation" data-id="302281"><a href="/opinion/302281/united-states-v-john-kearn-fallon/#19" aria-description="Citation for case: United States v. John Kearn Fallon">457 F. 2d 15, 19-20</a></span> (CA10 1972); <i>Leonard</i> v. <i>United States,</i> <span class="citation" data-id="279328"><a href="/opinion/279328/andrew-j-leonard-v-united-states/#538" aria-description="Citation for case: Andrew J. Leonard v. United States">391 F 2d 537, 538</a></span> (CA9 1968); <i>Pennsylvania ex rel. Craig</i> v. <i>Maroney,</i> <span class="citation" data-id="268537"><a href="/opinion/268537/commonwealth-of-pennsylvania-ex-rel-george-w-craig-v-james-f-maroney/#29" aria-description="Citation for case: Commonwealth of Pennsylvania Ex Rel. George W. Craig v....">348 F. 2d 22, 29</a></span> (CA3 1965).</p>
<p>[9]  See <i>United States</i> v. <i>Edmons,</i> <span class="citation" data-id="8883830"><a href="/opinion/8897209/united-states-v-edmons/" aria-description="Citation for case: United States v. Edmons">432 F. 2d 577</a></span> (CA2 1970). See also <i>United States ex rel. Gockley</i> v. <i>Myers,</i> <span class="citation" data-id="9457491"><a href="/opinion/299686/united-states-of-america-ex-rel-edwin-gockley-v-david-n-myers/#236" aria-description="Citation for case: United States of America Ex Rel. Edwin Gockley v. David...">450 F. 2d 232, 236</a></span> (CA3 1971), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./404/1063/">404 U. S. 1063</a></span> (1972); <i>United States</i> v. <i>Kilgen,</i> <span class="citation" data-id="297732"><a href="/opinion/297732/united-states-v-robert-h-kilgen-jr/#289" aria-description="Citation for case: United States v. Robert H. Kilgen, Jr.">445 F. 2d 287, 289</a></span> (CA5 1971).</p>
<p>[10]  Our approach relies heavily, but not excessively, on the "learning, good sense, fairness and courage of federal trial judges." <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#342" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 342</a></span> (1939).</p>
<p>[11]  The situation here is thus in dramatic contrast to that of Wong Sun himself. Wong Sun's confession, which the Court held admissible, came several days after the illegality, and was preceded by a lawful arraignment and a release from custody on his own recognizance. <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#491" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 491</a></span>.</p>
<p>[12]  The fact that Brown had made one statement, believed by him to be admissible, and his cooperation with the arresting and interrogating officers in the search for Claggett, with his anticipation of leniency, bolstered the pressures for him to give the second, or at least vitiated any incentive on his part to avoid self-incrimination. Cf. <i>Fahy</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422676"><a href="/opinion/106699/fahy-v-connecticut/" aria-description="Citation for case: Fahy v. Connecticut">375 U. S. 85</a></span> (1963).</p>
<p>[13]  Detective Lenz had been a member of the Chicago police force for 14 years and a detective for 12 years. App. 6. Detective Nolan had been a detective on the force for 5 1/2 years. <span class="citation" data-id="9422676"><a href="/opinion/106699/fahy-v-connecticut/#87" aria-description="Citation for case: Fahy v. Connecticut"><i>Id.,</i> at 87</a></span>.</p>
<p>[1]  Each of these guarantees provides an independent ground for suppression of statements and thus may make it unnecessary in many cases to conduct the inquiry mandated by <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963).</p>
<p>[2]  Toy gave a second statement under circumstances similar to those in Wong Sun's case. The Court did not, however, rule as to the admissibility of this statement, finding instead that it lacked corroboration and was therefore insufficient to support Toy's conviction. <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 488-491</a></span>.</p>
<p>[3]  I note that this resolution might have the added benefit of encouraging the police to seek a warrant whenever possible. Cf. <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#113" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 113</a></span> (1975), and sources cited therein.</p>
<p>[4]  The majority of the statements cited by the Court are the officers' responses to questions inquiring as to what the officers <i>told</i> petitioner upon arresting him and thus are only indirectly relevant to the issue whether the officers might reasonably have thought they then had sufficient evidence to support a probable-cause determination. Moreover, as noted above, that evidence is contradictory. In only two instances during the trial did the inquiry relate more directly to whether the officers arrested petitioner for questioning. App. 83, 94. The officers' responses to those questions tend to support the Court's conclusion. In view of the weight of the contrary evidence, however, I think that the matter should be considered in the first instance by the state courts.</p>
<p>[5]  Petitioner's motion to suppress alleged that the police lacked reasonable grounds for believing that he committed a crime. But the testimony at the hearing focused primarily on the issue of the adequacy of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and the voluntariness of petitioner's statements. At the close of the hearing the trial court ruled, without elaboration or findings of fact, that the statements were admissible. <i>Id.,</i> at 65. Conceivably the trial court thought that probable cause existed to support the arrest. The State argued this point unsuccessfully on appeal. Equally possible, the trial court might have determined that the probable-cause issue was a close one and that, viewing the totality of the circumstances with that fact in mind, the statement should be admitted.</p>
<p>[6]  The Solicitor General has filed a memorandum as <i>amicus curiae</i> in which he urges the Court to remand the case for further factual hearings, cf. <i>Morales</i> v. <i>New York,</i> <span class="citation" data-id="108004"><a href="/opinion/108004/morales-v-new-york/" aria-description="Citation for case: Morales v. New York">396 U. S. 102</a></span> (1969). I concur in the Court's rejection of this suggestion, agreeing that the record is adequate to allow us to rule on the major issuewhether advice of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights constitutes a <i>per se</i> attenuation of the taint of an illegal arrest in all cases. I do not agree, however, that the record is adequate for the Court to rule, in addition, that there was insufficient attenuation of taint in this case.</p>
<p>[7]  Petitioner's second statement, corroborative of the first, was given more than six hours after his arrest and some five hours after the initial statement. During this time petitionercooperating with the policehad made two trips away from the police headquarters in search of Claggett, whom he had identified as his confederate in the murder. This second statement was given to an assistant state's attorney who again had informed petitioner of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. The Court deems this statement to be the fruit of the first one and thus excludable along with it.
</p>
<p>I also would leave the question of admissibility of this statement to the lower Illinois courts. Of course, if the first statement were ruled admissible under the general guidelines articulated in today's opinion, it would follow that the second statement also would be admissible. In any event, the question whether there was sufficient attenuation between the first and second statements to render the second admissible in spite of the inadmissibility of the first presents a factual issue which, like the factual issue underlying the possible admissibility of the first statement, has not been passed on by the state courts.</p>

</div>
```

---

## GROUP: content/cases/Brown v. Mississippi.md  (`case`, 5 assertions)

### content_page

```
---
title: "Brown v. Mississippi"
type: case
citation: "297 U.S. 278 (1936)"
parallel_cite: "56 S. Ct. 461; 80 L. Ed. 682"
neutral_cite: 1936 U.S. LEXIS 527
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1936
date_decided: 1936-02-17
docket: 301
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1936-02-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Brown v. Mississippi
  varies_by_point: false
  scope_note: "Foundational due-process voluntariness case; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/102604/brown-v-mississippi/"
  cluster_id: 102604
  opinion_id: 102604
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Anchor"
related: ["[[Chambers v. Florida]]", "[[Ashcraft v. Tennessee]]", "[[Colorado v. Connelly]]"]
aliases: []
tags: ["case", "due-process", "confessions", "voluntariness", "coercion"]
holding: "A confession extracted by physical torture is involuntary and its use to convict violates Fourteenth Amendment due process."
lake:
  record_id: Brown v. Mississippi
  status: under_review
  projected_at: 2026-07-09
---

# Brown v. Mississippi

*297 U.S. 278 (1936)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Three Black tenant farmers were convicted of murder in Mississippi on the strength of confessions extracted by brutal physical torture — repeated whippings and a mock hanging — administered by a deputy and others. The torture was openly described at trial, yet the confessions were admitted and were the only real evidence of guilt.

## Issue
Whether a state criminal conviction resting solely on confessions extracted by physical torture violates the Due Process Clause of the Fourteenth Amendment.

## Rule
"And the trial equally is a mere pretense where the state authorities have contrived a conviction resting solely upon confessions obtained by violence." — 297 U.S. at 286. ^pin-286

"It would be difficult to conceive of methods more revolting to the sense of justice than those taken to procure the confessions of these petitioners, and the use of the confessions thus obtained as the basis for conviction and sentence was a clear denial of due process." — [*Id.*](https://www.courtlistener.com/opinion/102604/brown-v-mississippi/#:~:text=It%20would%20be%20difficult%20to) ^pin-286b

## Application
The confessions here were wrung from the defendants by physical brutality, and the convictions rested on nothing else. Using such coerced confessions as the basis for conviction and sentence was a clear denial of due process of law.

## Conclusion
The convictions violated Fourteenth Amendment due process and were reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Brown* is the foundational due-process voluntariness case; the doctrine was developed in [[Chambers v. Florida]] and [[Ashcraft v. Tennessee]] and later cabined to coercive *police* conduct in [[Colorado v. Connelly]].

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Anchor*

## Sources
- *Brown v. Mississippi*, 297 U.S. 278 (1936) — https://www.courtlistener.com/opinion/102604/brown-v-mississippi/ — pinpoint: 286.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e682104fc03a0ccf", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "297 U.S. 278 (1936)", "court": "U.S. Supreme Court", "neutral_cite": "1936 U.S. LEXIS 527", "official_citation_present": true, "parallel_cite": "56 S. Ct. 461; 80 L. Ed. 682", "title": "Brown v. Mississippi", "year": "1936"}}
{"assertion_id": "55587eb6f2848f57", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A confession extracted by physical torture is involuntary and its use to convict violates Fourteenth Amendment due process.", "title": "Brown v. Mississippi"}}
{"assertion_id": "d321c7ed599c4e81", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Key — Anchor", "title": "Brown v. Mississippi"}}
{"assertion_id": "311c955c0681ae01", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1936-02-17", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Brown v. Mississippi", "field_i_validity": "good_law", "scope_note": "Foundational due-process voluntariness case; good law.", "title": "Brown v. Mississippi", "varies_by_point": "false"}}
{"assertion_id": "e5e60df5c80c5cff", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Brown v. Mississippi"}}
```

### lake record — Brown v. Mississippi

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brown v. Mississippi",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Brown v. Mississippi",
    "case_name_short": "Brown",
    "case_name_full": "BROWN Et Al. v. MISSISSIPPI",
    "input_case_name": "Brown v. Mississippi",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1936-02-17",
    "year": 1936,
    "docket": "301",
    "cluster_id": 102604,
    "lead_opinion_id": 102604,
    "sibling_ids": [
      102604
    ],
    "absolute_url": "/opinion/102604/brown-v-mississippi/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "297 U.S. 278",
      "volume": "297",
      "reporter": "U.S.",
      "page": "278",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "56 S. Ct. 461",
        "volume": "56",
        "reporter": "S. Ct.",
        "page": "461",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 L. Ed. 682",
        "volume": "80",
        "reporter": "L. Ed.",
        "page": "682",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1936 U.S. LEXIS 527",
        "volume": "1936",
        "reporter": "U.S. LEXIS",
        "page": "527",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "297 U.S. 278",
        "volume": "297",
        "reporter": "U.S.",
        "page": "278",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 S. Ct. 461",
        "volume": "56",
        "reporter": "S. Ct.",
        "page": "461",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 L. Ed. 682",
        "volume": "80",
        "reporter": "L. Ed.",
        "page": "682",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1936 U.S. LEXIS 527",
        "volume": "1936",
        "reporter": "U.S. LEXIS",
        "page": "527",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "297 U.S. 278",
    "official_selection": {
      "court_class": "scotus",
      "selected": "297 U.S. 278",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-286",
      "page": null,
      "quote": "--- # Brown v. Mississippi *297 U.S. 278 (1936)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Three Black tenant farmers were convicted of murder in Mississippi on the strength of confessions extracted by brutal physical torture \u2014 repeated whippings and a mock hanging \u2014 administered by a deputy and others. The torture was openly described at trial, yet the confessions were admitted and were the only real evidence of guilt. ## Issue Whether a state criminal conviction resting solely on confessions extracted by physical torture violates the Due Process Clause of the Fourteenth Amendment. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-286b",
      "page": null,
      "quote": "It would be difficult to conceive of methods more revolting to the sense of justice than those taken to procure the confessions of these petitioners, and the use of the confessions thus obtained as the basis for conviction and sentence was a clear denial of due process.",
      "star_marker": "286",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 17614,
      "fragment": "#:~:text=It%20would%20be%20difficult%20to",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1936-02-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Brown v. Mississippi",
    "varies_by_point": false,
    "scope_note": "Foundational due-process voluntariness case; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Long",
          "cluster_id": 4786330,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
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
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Richard Ellis Hill",
          "cluster_id": 3161206,
          "cite": [
            "871 N.W.2d 900",
            "2015 Minn. LEXIS 743",
            "2015 WL 8343418"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Courtney Bishop",
          "cluster_id": 2655823,
          "cite": [
            "431 S.W.3d 22",
            "2014 WL 888198",
            "2014 Tenn. LEXIS 189"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brandon Dale Woodruff v. State",
          "cluster_id": 3094579,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Limone v. Condon",
          "cluster_id": 201063,
          "cite": [
            "372 F.3d 39",
            "2004 WL 1299980"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dickerson",
          "cluster_id": 2967209,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Peevy",
          "cluster_id": 1378981,
          "cite": [
            "17 Cal. 4th 1184",
            "953 P.2d 1212",
            "98 Daily Journal DAR 4763",
            "98 Cal. Daily Op. Serv. 3444",
            "73 Cal. Rptr. 2d 865",
            "1998 Cal. LEXIS 2623"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. D.F.",
          "cluster_id": 741773,
          "cite": [
            "115 F.3d 413",
            "1997 U.S. App. LEXIS 11994",
            "1997 WL 254194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Norman v. Gloria Farms, Inc.",
          "cluster_id": 1703009,
          "cite": [
            "668 So. 2d 1016",
            "1996 WL 46883"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Zuliani v. State",
          "cluster_id": 2372052,
          "cite": [
            "903 S.W.2d 812",
            "1995 WL 410841"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cathy Burns v. Rick Reed",
          "cluster_id": 686495,
          "cite": [
            "44 F.3d 524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Cahill",
          "cluster_id": 1244769,
          "cite": [
            "853 P.2d 1037",
            "5 Cal. 4th 478",
            "20 Cal. Rptr. 2d 582",
            "93 Daily Journal DAR 8304",
            "93 Cal. Daily Op. Serv. 4902",
            "1993 Cal. LEXIS 3087"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Luther Wilkins, Jr. v. James A. May",
          "cluster_id": 521076,
          "cite": [
            "872 F.2d 190"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Griffin v. State",
          "cluster_id": 1779038,
          "cite": [
            "765 S.W.2d 422",
            "1989 Tex. Crim. App. LEXIS 29",
            "1989 WL 8702"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ex Parte McCary",
          "cluster_id": 1793877,
          "cite": [
            "528 So. 2d 1133",
            "1988 WL 10157"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Miranda v. Arizona",
          "cluster_id": 107252,
          "cite": [
            "16 L. Ed. 2d 694",
            "86 S. Ct. 1602",
            "384 U.S. 436",
            "1966 U.S. LEXIS 2817",
            "10 Ohio Misc. 9",
            "36 Ohio Op. 2d 237",
            "10 A.L.R. 3d 974"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Denno",
          "cluster_id": 106881,
          "cite": [
            "12 L. Ed. 2d 908",
            "84 S. Ct. 1774",
            "378 U.S. 368",
            "1964 U.S. LEXIS 826",
            "1 A.L.R. 3d 1205",
            "28 Ohio Op. 2d 177"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rose v. Lundy",
          "cluster_id": 110662,
          "cite": [
            "71 L. Ed. 2d 379",
            "102 S. Ct. 1198",
            "455 U.S. 509",
            "1982 U.S. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re GAULT",
          "cluster_id": 107439,
          "cite": [
            "18 L. Ed. 2d 527",
            "87 S. Ct. 1428",
            "387 U.S. 1",
            "1967 U.S. LEXIS 1478",
            "40 Ohio Op. 2d 378"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fay v. Noia",
          "cluster_id": 106548,
          "cite": [
            "9 L. Ed. 2d 837",
            "83 S. Ct. 822",
            "372 U.S. 391",
            "1963 U.S. LEXIS 1945",
            "24 Ohio Op. 2d 12"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moran v. Burbine",
          "cluster_id": 111614,
          "cite": [
            "89 L. Ed. 2d 410",
            "106 S. Ct. 1135",
            "475 U.S. 412",
            "1986 U.S. LEXIS 32",
            "54 U.S.L.W. 4265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rochin v. California",
          "cluster_id": 104943,
          "cite": [
            "96 L. Ed. 2d 183",
            "72 S. Ct. 205",
            "342 U.S. 165",
            "1952 U.S. LEXIS 2576",
            "25 A.L.R. 2d 1396",
            "96 L. Ed. 183"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Allen",
          "cluster_id": 105074,
          "cite": [
            "97 L. Ed. 2d 469",
            "73 S. Ct. 397",
            "344 U.S. 443",
            "1953 U.S. LEXIS 2391",
            "97 L. Ed. 469"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Palko v. Connecticut",
          "cluster_id": 102879,
          "cite": [
            "302 U.S. 319",
            "58 S. Ct. 149",
            "82 L. Ed. 288",
            "1937 U.S. LEXIS 549"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McNabb v. United States",
          "cluster_id": 103791,
          "cite": [
            "318 U.S. 332",
            "63 S. Ct. 608",
            "87 L. Ed. 819",
            "1943 U.S. LEXIS 1280"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Screws v. United States",
          "cluster_id": 104135,
          "cite": [
            "325 U.S. 91",
            "65 S. Ct. 1031",
            "89 L. Ed. 1495",
            "1945 U.S. LEXIS 2096",
            "162 A.L.R. 1330"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dickerson v. United States",
          "cluster_id": 118380,
          "cite": [
            "147 L. Ed. 2d 405",
            "120 S. Ct. 2326",
            "530 U.S. 428",
            "2000 U.S. LEXIS 4305"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lego v. Twomey",
          "cluster_id": 108429,
          "cite": [
            "30 L. Ed. 2d 618",
            "92 S. Ct. 619",
            "404 U.S. 477",
            "1972 U.S. LEXIS 100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shelley v. Kraemer",
          "cluster_id": 104545,
          "cite": [
            "92 L. Ed. 2d 1161",
            "68 S. Ct. 836",
            "334 U.S. 1",
            "1948 U.S. LEXIS 2764",
            "3 A.L.R. 2d 441",
            "92 L. Ed. 1161"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miller v. Fenton",
          "cluster_id": 111542,
          "cite": [
            "88 L. Ed. 2d 405",
            "106 S. Ct. 445",
            "474 U.S. 104",
            "1985 U.S. LEXIS 144",
            "54 U.S.L.W. 4022"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estes v. Texas",
          "cluster_id": 107083,
          "cite": [
            "14 L. Ed. 2d 543",
            "85 S. Ct. 1628",
            "381 U.S. 532",
            "1965 U.S. LEXIS 2339",
            "1 Media L. Rep. (BNA) 1187",
            "6 Rad. Reg. 2d (P & F) 2104"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Culombe v. Connecticut",
          "cluster_id": 106284,
          "cite": [
            "6 L. Ed. 2d 1037",
            "81 S. Ct. 1860",
            "367 U.S. 568",
            "1961 U.S. LEXIS 811"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wolf v. Colorado",
          "cluster_id": 104709,
          "cite": [
            "93 L. Ed. 2d 1782",
            "69 S. Ct. 1359",
            "338 U.S. 25",
            "1949 U.S. LEXIS 2079",
            "93 L. Ed. 1782"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hansberry v. Lee",
          "cluster_id": 103379,
          "cite": [
            "311 U.S. 32",
            "61 S. Ct. 115",
            "85 L. Ed. 22",
            "1940 U.S. LEXIS 108",
            "132 A.L.R. 741"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(102604) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01Mzg3OTA0MDAwMDAmcz0xMTQ4MDg1JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28102604%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 16,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 16,
        "triage_snippet_classified": 184
      },
      "lane2_top_cited": {
        "query": "cites:(102604)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05MDgmcz0xMTI0NTImdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28102604%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(102604)",
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
    "complete_query": "cites:(102604)",
    "indexed_citing_opinions": 618,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 102604,
        "count": 618,
        "count_source": "search"
      }
    ],
    "citation_count": 961,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/brown-v-mississippi.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU2NTc4Nzcmcz00NDQ5OTI0JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28102604%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 102604,
        "cited_id": 89245,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 91054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 96356,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 96885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 100122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 100929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 102189,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 3517982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 3518564,
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
    "date_created": "2026-07-04T20:48:14Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:48:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:48:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:53:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:48:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Brown v. Mississippi

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b325-8">
  Mr. Chief Justice Hughes
 </author>
<p id="AqF">
  delivered the opinion of the Court.
 </p>
<p id="b325-9">
  The question in this case is whether convictions, which rest solely upon confessions shown to have been extorted by officers of the.State by brutality and violence, are consistent with the due process of law required by the Fourteenth Amendment of the Constitution of the United States.
 </p>
<p id="b325-10">
  Petitioners were indicted for the murder of one Raymond Stewart, whose death occurred on March 30, 1934. They, were indicted on April 4, 1934, and were then arraigned and. pleaded not guilty. Counsel were appointed by the court to defend them. Trial was begun the next morning and was concluded on the following day, when they were found guilty and sentenced to death.
 </p>
<p id="b325-11">
  Aside from the confessions, there Was no evidence sufficient, to warrant the submission of the case to the jury. After a preliminary inquiry, testimony as to the confessions was received over the objection of defendants’ counsel. Defendants then testified that the confessions were false and had been procured-by physical torture. The case went to the 'jury with instructions, upon the request of defendants’ counsel, that if the jury had reasonable doubt as to the. confessions having resulted, from coercion, and that they were not true, they were not to be considered as evidence. On their appeal to the Su
  <span citation-index="1" class="star-pagination" label="280"> 
   *280
   </span>
  preme Court of the State, defendants assigned as error the inadmissibility of the confessions. The judgment was affirmed. <span class="citation" data-id="3520101"><a href="/opinion/3547181/brown-v-state/" aria-description="Citation for case: Brown v. State">158 So. 339</a></span>.
 </p>
<p id="b326-6">
  Defendants then moved in the Supreme Court of the State to arrest the judgment and for a new trial' on the ground, that all the evidence against them was obtained by coercion and brutality known to the court and to-the district attorney, and that defendants had been denied the benefit of counsel or opportunity to confer with counsel in, a reasonable manner. The motion was supported by affidavits. At about the same time, defendants filed in the Supreme Court a “suggestion of error” explicitly challenging the proceedings of the trial, in the use of- the confessions and with respect to the alleged denial of representation by counsel, as violating the due process clause of the Fourteenth Amendment of the Constitution of the United States. The state court entertained the suggestion of error, considered the federal question, and decided it against defendants’ contentions. <span class="citation multiple-matches"><a href="/c/So./161/465/">161 So. 465</a></span>. Two judges dissented..
  <em>
   Id.,
  </em>
  p. 470. We granted a writ of certiorari.
 </p>
<p id="b326-7">
  The grounds of the decision were (1) that immunity from self-incrimination is not essential to due process of law, and (2) that the failure of the trial court to exclude the confessions after the introduction of evidence showing their incompetency, in the absence-of a request for such exclusion, did not deprive the defendants of life or liberty without due process of law; and that even if the trial court had erroneously overruled a motion to exclude the confessions^ the ruling would have been, mere error reversible on appeal, but not a violation of constitutional right.
  <em>
   Id.,
  </em>
  p. 468.
 </p>
<p id="b326-8">
  The opinion of the state court did not set forth the evidence as to the circumstances in which the confessions were procured. That the evidence established that they were procured by coercion was not questioned. The state
  <span citation-index="1" class="star-pagination" label="281"> 
   *281
   </span>
  court said: “After the state closed its case on the merits, the appellants, for the first time, introduced evidence from which it appears that the confessions were not madé voluntarily but were coerced.”
  <em>
   Id.,
  </em>
  p. 466. There is no dispute as to the facts upon this point- and as they are clearly and adequately stated in the dissenting opinion of •Judge Griffith (with whom Judge Anderson concurred)-^-1 showing both the extreme brutality of the measures to extort the confessions and the participation of the state auth orities — we quote this part of his opinion in full, as follows
  <em>
   (Id.,
  </em>
  pp. 470, 471):'
 </p>
<blockquote id="b327-6">
  “The crime with which these defendants, all ignorant negroes, are charged, was discovered about one o’clock p. m. on ¡Friday, March 30,1934. On that night one Dial, a deputy sheriff, accompanied by others, came to the home of Ellington,- one of the defendants, and requested him to accompany them to the house of the deceased, and there, a number of white men were gathered, who began to accuse the defendant of the crime. Upon his denial they seized him, and with the participation of the deputy they . hanged him by a rope to the limb of a tree, and having let him down, they hung him again, and when he was.let down the second time, and he still' protested his innocence, he was tied to a tree and whipped, and still declining to accede to the demands that he confess, he was finally released and he returned with some difficulty to his home, suffering intense pain and agony. The record of the' testimony shows that the signs of the rope on his neck were plainly visible during the so-called trial: A da, or two thereafter the said deputy; accompanied by another, returned to the home of the said defendant and arrested him, and departed’with the prisoner towards the jail in an adjoining county, but., went by a route which led into the State of Alabama; and while on the way, in that State, the deputy stopped and again severely whipped the defendant, declaring that he would continue the whipping
  <span citation-index="1" class="star-pagination" label="282"> 
   *282
   </span>
  until he confessed, and the defendant then agreed to confess to such a statement as the deputy would dictate, and he did so, after which he was delivered to jail.
 </blockquote>
<blockquote id="b328-5">
  “The other two defendants, Ed Brown and Henry Shields, were also arrested and taken to the same jail. On Sunday night, April 1, 1934, the same deputy, accompanied by a number of white men, one of whom was also an officer, and by the jailer, came to the jail, and the two last named defendants were made to strip and they were laid over chairs and their backs were cut to pieces with a leather strap with buckles on it, and they were likewise made by the said deputy definitely to understand that the whipping would be continued unless and until they confessed, and not only confessed,' but confessed in every matter of detail as demanded by those present; and in this manner the defendants confessed the crime, and as the whippings progressed and were repeated, they changed or adjusted their confession in all particulars of detail so as to conform to the demands of their torturers. When the confessions had been obtained in the exact form and contents as desired by the mob, they left with the parting admonition and warning that, if the defendants changed their story at any time in any respect from that last statéd, the perpetrators of the outrage would administer the same or equally effective treatment.
 </blockquote>
<blockquote id="b328-6">
  “Further details of the brutal treatment to which these helpless prisoners were subjected need not be pursued. It is sufficient to say that in pertinent respects the transcript reads more like pages tom from some medieval account, than a record made within the confines of a modern civilization which aspires to an enlightened constitutional government.
 </blockquote>
<blockquote id="b328-7">
  “All this having been accomplished, on. the next day, that is, on Monday, April 2, when the defendants had been given time to recuperate somewhat from the tortures to which they had been subjected, the two sheriffs, one
  <span citation-index="1" class="star-pagination" label="283"> 
   *283
   </span>
  of the county where the crime was committed,. and the other of the county of the jail in which the prisoners were confined, came to the jail, accompanied by eight other persons, some of them deputies, there to hear the free and yoluntary confession of these miserable and abject defendants. The sheriff of the county of the crime admitted that he had heard of the whipping, but averred that he had no personal knowledge of it. He admitted that one of the defendants, when brought before him to confess, was limping and did not sit down, and that this particular defendant then and there stated that he had been strapped so severely that he could not sit down, and as already stated, the signs of the rope on the neck of another of the defendants were plainly visible to all. Nevertheless the. solemn farce of hearing the free and voluntary confessions was gone through with, and these two sheriffs and one other person then present were the three witnesses used in court to establish the so-called confessions, which were received by the court and admitted in evidence over the objections of the defendants duly entered of record as each of the said three witnesses delivered their alleged testimony. There was thus enough before the court when these confessions were first offered to make known to the court, that they were not, beyond all reasonable doubt, free and voluntary; and the failure of the court then to exclude the confessions is sufficient to reverse the judgment, under every rule of procedure that has heretofore been prescribed, and hence it was not necessary subsequently to renew the objections by motion or otherwise. *
 </blockquote>
<blockquote id="b329-6">
  “The spurious confessions having been obtained — and the farce last mentioned having been gone through with on Monday, April 2d — the court, thén in session, on the' following day, Tuesday, April 3, 1934, ordered the grand jury to reassemble on the succeeding day, April 4, 1934, at nine o’clock, and on the morning of the day last men
  <span citation-index="1" class="star-pagination" label="284"> 
   *284
   </span>
  tionecl the grand jury returned an indictment against the defendants- for murder. Late that afternoon the defendants were brought from the jail in the adjoining county and arraigned, when one or more of them offered to plead guilty, which the • court declined to accept, and, upon inquiry whether they had or desired counsel, they stated that they had none, and did not suppose that counsel could be of any assistance to them. The court thereupon appointed counsel, and set the case for trial for the following morning at nine o’clock, and the defendants were returned to the jail in the adjoining county about thirty mile's away.
 </blockquote>
<blockquote id="AIdQ">
  “The defendants were brought to the courthouse of the county on the following morning, April 5th, and the so-' called trial was opened, and was concluded on the next day, April 6, 1934, and resulted in a pretended conviction with' death sentences. The evidence upon which the conviction was obtained was the so-called confessions. Without this evidence a peremptory instruction to find for the defendants'would have been inescapable. The defendants were put on the stand, and by their testimony the facts and the details thereof as to the manner by which the confessions were extorted from them were fully developed, and it is. further disclosed by the record that the same deputy, Dial, .under whose guiding hand and active participation the tortures to coerce the confessions were administered, was actively in the performance of the supposed duties of a court deputy in the courthouse and in the presence of the prisoners during what is denominated, in complimentaiy terms, the trial of these defendants. This deputy was put on the stand by the1 state in rebuttal, and admitted the whippings. It is interesting to note that in his testimony with reference to the whipping of the defendant Ellington, and in response to the inquiry as to how severely.he was whipped, the deputy stated, ‘Not, too much for a negro; .not as much as I would have done if it were left to me.’ Two others who had participated
  <span citation-index="1" class="star-pagination" label="285"> 
   *285
   </span>
  in these whippings were introduced and admitted it — not a single witness was introduced who denied it. The facts are not only undisputed, they are admitted, and admitted to have been done by officers of the state, in conjunction with other participants, and all this was definitely well known to everybody connected with the trial, and during the trial, including the state’s prosecuting attorney and the trial judge presiding.”
 </blockquote>
<p id="A4jD">
  1. The State stresses the statement in
  <em>
   Twining
  </em>
  v.
  <em>
   New Jersey,
  </em>
  <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/#114" aria-description="Citation for case: Twining v. New Jersey">211 U. S. 78, 114</a></span>, that “exemption from compulsory self-incrimination in the courts of the States is not secured by any part of the Federal Constitution,” and the statement in
  <em>
   Snyder
  </em>
  v.
  <em>
   Massachusetts,
  </em>
  <span class="citation" data-id="9418797"><a href="/opinion/102189/snyder-v-massachusetts/#105" aria-description="Citation for case: Snyder v. Massachusetts">291 U. S. 97, 105</a></span>, that “the privilege against self-incrimination may be withdrawn .and the accused put upon the stand as a witness for the State.” But the question of the right of the State to withdraw the privilege against self-incrimination is not here involved. The compulsion to which .the quoted statements refer is that of -the processes' of justice by which the accused may be called as a witness and required to testify. Compulsion by torture to extort a confession is a different matter.
 </p>
<p id="b331-7">
  The State is free to regulate the procedure of its courts in accordance with its own conceptions of policy, unless in so doing it “offends some principle of justice so rooted in the traditions and conscience of our people as to be ranked as fundamental.”
  <em>
   Snyder
  </em>
  v.
  <em>
   <span class="citation" data-id="9418797"><a href="/opinion/102189/snyder-v-massachusetts/" aria-description="Citation for case: Snyder v. Massachusetts">Massachusetts, supra;</a></span> Rogers
  </em>
  v.
  <em>
   Peck,
  </em>
  <span class="citation" data-id="96356"><a href="/opinion/96356/rogers-v-peck/#434" aria-description="Citation for case: Rogers v. Peck">199 U. S. 425, 434</a></span>. The State may abolish trial'by jury. It may dispense with indictment by a grand jury and substitute complaint or information.
  <em>
   Walker
  </em>
  v.
  <em>
   Sauvinet,
  </em>
  <span class="citation" data-id="89245"><a href="/opinion/89245/walker-v-sauvinet/" aria-description="Citation for case: Walker v. Sauvinet">92 U. S. 90</a></span>;
  <em>
   Hurtado
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9417375"><a href="/opinion/91054/hurtado-v-california/" aria-description="Citation for case: Hurtado v. California">110 U. S. 516</a></span>;
  <em>
   Snyder
  </em>
  v.
  <em>
   <span class="citation" data-id="9418797"><a href="/opinion/102189/snyder-v-massachusetts/" aria-description="Citation for case: Snyder v. Massachusetts">Massachusetts, supra.</a></span>
  </em>
  But the freedom of the State in establishing its policy is the freedom of constitutional government and is limited by the requirement of due process of law. Because a State may dispense with a jury trial, it does not follow that it may substitute trial by ordeal. The rack and tor
  <span citation-index="1" class="star-pagination" label="286"> 
   *286
   </span>
  ture chamber may not be substituted for the witness stand. The ■ State may not permit, an accused to be hurried to conviction under mob domination — where the whole pro- ■ ceeding is but a mask — without supplying corrective process.
  <em>
   Moore
  </em>
  v.
  <em>
   Dempsey,
  </em>
  <span class="citation" data-id="9418497"><a href="/opinion/100122/moore-v-dempsey/#91" aria-description="Citation for case: Moore v. Dempsey">261 U. S. 86, 91</a></span>. The State may not deny to the accused the aid of counsel.
  <em>
   Powell
  </em>
  v.
  <em>
   Alabama,
  </em>
  <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span>. Nor may a State, through the action of its officers, contrive a conviction through the pretense of a trial which in truth is “but used as a means of depriving a defendant of liberty through a deliberate deception of court and jury, by the presentation of testimony known to be perjured.”
  <em>
   Mooney
  </em>
  v.
  <em>
   Holohan,
  </em>
  <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#112" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103, 112</a></span>. And the trial equally is a mere pretense where the state authorities have contrived a conviction resting solely upon confessions obtained by violence. The due process clause requires “that state action, whether through one agency or another, shall be consistent with the fundamental principles of liberty and justice which lie at the base of all oúr civil ,and political institutions.”
  <em>
   Hebert
  </em>
  v.
  <em>
   Louisiana,
  </em>
  <span class="citation" data-id="100929"><a href="/opinion/100929/hebert-v-louisiana/#316" aria-description="Citation for case: Hebert v. Louisiana">272 U. S. 312, 316</a></span>. It would be difficult to conceive of methods more revolting to the sense of justice than those taken to procure the confessions of these petitioners, and the use of the confessions thus obtained as the basis for conviction and sentence was a clear denial of due process.
 </p>
<p id="b332-5">
  2. It is in this view that the further contention of the State must be considered. That contention rests upon the failure of counsel .for the accused, who had objected to the admissibility of the confessions, to move for1 their exclusion after they had been introduced and the fact of coercion had been proved. It is a contention which proceeds upon a misconception of the nature of petitioners’ complaint. That complaint is not of the commission of mere error, but of a wrong so fundamental that it made the whole proceeding a. mere pretense of a trial and rendered-the conviction and sentence wholly void.
  <em>
   Moore
  </em>
  v.
  <em>
   <span class="citation" data-id="9418497"><a href="/opinion/100122/moore-v-dempsey/" aria-description="Citation for case: Moore v. Dempsey">Dempsey, supra.</a></span>
  </em>
  We are not concerned with a mere
  <span citation-index="1" class="star-pagination" label="287"> 
   *287
   </span>
  question of state practice, or whether counsel assigned to petitioners were competent ór mistakenly assumed that their first objections were sufficient. In an earlier case the Supreme Court of the State had recognized the duty of the court to supply corrective process where due process of law had been denied. In
  <em>
   Fisher
  </em>
  v.
  <em>
   State,
  </em>
  <span class="citation" data-id="3518564"><a href="/opinion/3545864/fisher-v-state/#134" aria-description="Citation for case: Fisher v. State">145 Miss. 116, 134</a></span>; <span class="citation" data-id="3518564"><a href="/opinion/3545864/fisher-v-state/#365" aria-description="Citation for case: Fisher v. State">110 So. 361, 365</a></span>, the court said: “Coercing the supposed state’s criminals into confessions and using such confessions so coerced from them against them in trials has been the curse of all countries. It was the chief inequity, the crowning infamy of the Star Chamber, and the Inquisition, and other similar institutions. The constitution recognized the evils that lay behind these practices and prohibited them in this country. . . . The duty of maintaining constitutional rights of a person on trial for his life rises above mere rules of procedure and wherever the court is clearly satisfied that such violations exist, it will refuse to sanction such violations and will apply the corrective.”
 </p>
<p id="b333-6">
  In the instant case, the trial court was fully advised by the undisputed evidence of the way in which the confessions had been procured-. The trial court knew that there was no other evidence upon which conviction and sentence could be based. Yet it proceeded to permit conviction and to pronounce sentence. The conviction and sentence were void for want of the essential elements of due process, and the proceeding thus vitiated could be challenged in any appropriate manner.
  <em>
   Mooney
  </em>
  v.
  <em>
   <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">Holohan, supra.</a></span>
  </em>
  It was challenged before the Supreme Court of the State by the express invocation of the Fourteenth Amendment. That court entertained the challenge, considered the federal question thus presented, but declined to enforce petitioners’ constitutional right. The court thus denied a federal right fully established and specially set up and claimed and the jüdgment must be
 </p>
<p id="b333-7">
<em>
   Reversed.
  </em>
</p>
</opinion>
```

---
