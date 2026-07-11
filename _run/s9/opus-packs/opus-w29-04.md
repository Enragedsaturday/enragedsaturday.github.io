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

## GROUP: content/cases/City of Canton v. Harris.md  (`case`, 5 assertions)

### content_page

```
---
title: "City of Canton v. Harris"
type: case
citation: "489 U.S. 378 (1989)"
parallel_cite: "109 S. Ct. 1197; 103 L. Ed. 2d 412; 57 U.S.L.W. 4270"
neutral_cite: 1989 U.S. LEXIS 1200
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1989
date_decided: 1989-02-28
docket: 86-1088
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1989-02-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: City of Canton v. Harris
  varies_by_point: false
  scope_note: "Good law: the 'deliberate indifference' standard for municipal failure-to-train liability."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112209/city-of-canton-v-harris/"
  cluster_id: 112209
  opinion_id: 112209
  identity_checked: true
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Monell v. Department of Social Services]]", "[[Pembaur v. City of Cincinnati]]", "[[Connick v. Thompson]]"]
aliases: ["Canton v. Harris", "City of Canton, Ohio v. Harris"]
tags: ["case", "section-1983", "municipal-liability", "failure-to-train", "deliberate-indifference", "monell"]
holding: "A municipality is liable under § 1983 for inadequate police training only where the failure to train amounts to deliberate indifference to the rights of persons with whom the police come into contact."
lake:
  record_id: City of Canton v. Harris
  status: verified
  projected_at: 2026-07-09
---

# City of Canton v. Harris

*489 U.S. 378 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Geraldine Harris was arrested and brought to the Canton, Ohio police station, where she slumped to the floor several times and behaved incoherently. Officers summoned no medical care; she was later diagnosed with emotional ailments requiring treatment. She sued the city under § 1983, claiming it had failed to train its officers on when to provide medical care to detainees in custody.

## Issue
Whether, and on what fault standard, a municipality can be held liable under § 1983 for a constitutional injury caused by its failure to adequately train its police officers.

## Rule
Failure-to-train liability requires [[Section 1983 Liability and Qualified Immunity|deliberate indifference]]. "We hold today that the inadequacy of police training may serve as the basis for § 1983 liability only where the failure to train amounts to deliberate indifference to the rights of persons with whom the police come into contact." — 489 U.S. at 388. ^pin-388

That high standard is met where "the need for more or different training is so obvious, and the inadequacy so likely to result in the violation of constitutional rights, that the policymakers of the city can reasonably be said to have been deliberately indifferent to the need." — [*Id.* at 390](https://www.courtlistener.com/opinion/112209/city-of-canton-v-harris/#:~:text=employees-,the%20need%20for%20more%20or%20different%20training%20is%20so%20obvious%2C%20and%20the%20inadequacy%20so%20likely%20to%20result%20in%20the%20violation%20of%20constitutional%20rights%2C%20that%20the%20policymakers%20of%20the%20city%20can%20reasonably%20be%20said%20to%20have%20been%20deliberately%20indifferent%20to%20the%20need.). ^pin-390

Only then does the training failure represent a municipal "policy" for which the city is responsible under *[[Monell v. Department of Social Services|Monell]]*.

## Application
Because the trial court's instructions had permitted liability on a theory closer to [[Common Legal Terms#respondeat-superior|respondeat superior]] than [[Section 1983 Liability and Qualified Immunity|deliberate indifference]], the Court could not sustain the verdict and [[Reading and Citing Cases#on-remand|remanded]]. The plaintiff would have to show that the city's failure to train reflected a deliberate or conscious choice — a policy of inaction in the face of an obvious need — and that the identified training deficiency actually caused her injury, not merely that an officer was unsatisfactorily trained or that better training could have avoided the harm.

## Conclusion
[[Reading and Citing Cases#vacated|Vacated]] and [[Reading and Citing Cases#on-remand|remanded]]. Inadequate training supports municipal § 1983 liability only on a showing of [[Section 1983 Liability and Qualified Immunity|deliberate indifference]], applied to the specific training deficiency that caused the constitutional injury.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Canton* builds on [[Monell v. Department of Social Services]] (policy-or-custom) and [[Pembaur v. City of Cincinnati]] (policymaker decisions) by defining the fault standard for inaction. Its "deliberate indifference" rule and the difficulty of proving it without a pattern were later underscored in [[Connick v. Thompson]]. No negative treatment.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *City of Canton v. Harris*, 489 U.S. 378 (1989) — https://www.courtlistener.com/opinion/112209/city-of-canton-v-harris/ — pinpoints: 388, 390.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a040e15d45559791", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "489 U.S. 378 (1989)", "court": "U.S. Supreme Court", "neutral_cite": "1989 U.S. LEXIS 1200", "official_citation_present": true, "parallel_cite": "109 S. Ct. 1197; 103 L. Ed. 2d 412; 57 U.S.L.W. 4270", "title": "City of Canton v. Harris", "year": "1989"}}
{"assertion_id": "4c9a1a7ca60c6f9b", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Key — Progeny / Refinement", "title": "City of Canton v. Harris"}}
{"assertion_id": "5c423eb55ea36cae", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A municipality is liable under § 1983 for inadequate police training only where the failure to train amounts to deliberate indifference to the rights of persons with whom the police come into contact.", "title": "City of Canton v. Harris"}}
{"assertion_id": "c6ab200bb80f5de3", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1989-02-28", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "City of Canton v. Harris", "field_i_validity": "good_law", "scope_note": "Good law: the 'deliberate indifference' standard for municipal failure-to-train liability.", "title": "City of Canton v. Harris", "varies_by_point": "false"}}
{"assertion_id": "e4c0d93181bb4d0c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "City of Canton v. Harris"}}
```

### lake record — City of Canton v. Harris

```json
{
  "schema_version": "s2.v1",
  "record_id": "City of Canton v. Harris",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "City of Canton v. Harris",
    "case_name_short": "Canton",
    "case_name_full": "CITY OF CANTON, OHIO v. HARRIS Et Al.",
    "input_case_name": "City of Canton v. Harris",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1989-02-28",
    "year": 1989,
    "docket": "86-1088",
    "cluster_id": 112209,
    "lead_opinion_id": 112209,
    "sibling_ids": [
      112209,
      9431589,
      9431590,
      9431591
    ],
    "absolute_url": "/opinion/112209/city-of-canton-v-harris/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "489 U.S. 378",
      "volume": "489",
      "reporter": "U.S.",
      "page": "378",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 1197",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1197",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 L. Ed. 2d 412",
        "volume": "103",
        "reporter": "L. Ed. 2d",
        "page": "412",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4270",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4270",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1989 U.S. LEXIS 1200",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "1200",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "489 U.S. 378",
        "volume": "489",
        "reporter": "U.S.",
        "page": "378",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 1197",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1197",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 L. Ed. 2d 412",
        "volume": "103",
        "reporter": "L. Ed. 2d",
        "page": "412",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 U.S. LEXIS 1200",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "1200",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4270",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4270",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "489 U.S. 378",
    "official_selection": {
      "court_class": "scotus",
      "selected": "489 U.S. 378",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-388",
      "page": null,
      "quote": "--- # City of Canton v. Harris *489 U.S. 378 (1989)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Geraldine Harris was arrested and brought to the Canton, Ohio police station, where she slumped to the floor several times and behaved incoherently. Officers summoned no medical care; she was later diagnosed with emotional ailments requiring treatment. She sued the city under \u00a7 1983, claiming it had failed to train its officers on when to provide medical care to detainees in custody. ## Issue Whether, and on what fault standard, a municipality can be held liable under \u00a7 1983 for a constitutional injury caused by its failure to adequately train its police officers. ## Rule Failure-to-train liability requires deliberate indifference.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-390",
      "page": null,
      "quote": "the need for more or different training is so obvious, and the inadequacy so likely to result in the violation of constitutional rights, that the policymakers of the city can reasonably be said to have been deliberately indifferent to the need.",
      "star_marker": "390",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 19335,
      "fragment": "#:~:text=employees-,the%20need%20for%20more%20or%20different%20training%20is%20so%20obvious%2C%20and%20the%20inadequacy%20so%20likely%20to%20result%20in%20the%20violation%20of%20constitutional%20rights%2C%20that%20the%20policymakers%20of%20the%20city%20can%20reasonably%20be%20said%20to%20have%20been%20deliberately%20indifferent%20to%20the%20need.",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1989-02-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "City of Canton v. Harris",
    "varies_by_point": false,
    "scope_note": "Good law: the 'deliberate indifference' standard for municipal failure-to-train liability.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Alanda Forrest v. Kevin Parry",
          "cluster_id": 4638072,
          "cite": [
            "930 F.3d 93"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gregory Baldwin v. City of Estherville, Iowa",
          "cluster_id": 4629600,
          "cite": [
            "929 N.W.2d 691"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Keyon Harrison v. Curt Vanderkooi",
          "cluster_id": 4522518,
          "cite": [
            "918 N.W.2d 785",
            "502 Mich. 751"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane1_negative"
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
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of the County Commissioners of Bryan County v. Brown",
          "cluster_id": 118104,
          "cite": [
            "137 L. Ed. 2d 626",
            "117 S. Ct. 1382",
            "520 U.S. 397",
            "1997 U.S. LEXIS 2793",
            "65 U.S.L.W. 4286",
            "10 Fla. L. Weekly Fed. S 405",
            "12 I.E.R. Cas. (BNA) 1217",
            "97 Cal. Daily Op. Serv. 3033",
            "97 Daily Journal DAR 5311"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Seiter",
          "cluster_id": 112626,
          "cite": [
            "115 L. Ed. 2d 271",
            "111 S. Ct. 2321",
            "501 U.S. 294",
            "1991 U.S. LEXIS 3490"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
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
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. City of Harker Heights",
          "cluster_id": 112699,
          "cite": [
            "117 L. Ed. 2d 261",
            "112 S. Ct. 1061",
            "503 U.S. 115",
            "1992 U.S. LEXIS 1376"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leatherman v. Tarrant County Narcotics Intelligence and Coordination Unit",
          "cluster_id": 112825,
          "cite": [
            "122 L. Ed. 2d 517",
            "113 S. Ct. 1160",
            "507 U.S. 163",
            "1993 U.S. LEXIS 1941",
            "61 U.S.L.W. 4205",
            "25 Fed. R. Serv. 3d 1",
            "93 Cal. Daily Op. Serv. 1493",
            "8 I.E.R. Cas. (BNA) 428",
            "7 Fla. L. Weekly Fed. S 40",
            "93 Daily Journal DAR 2747"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lee v. City of Los Angeles",
          "cluster_id": 7092482,
          "cite": [
            "250 F.3d 668",
            "2001 WL 468408"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lee v. City Of Los Angeles",
          "cluster_id": 773312,
          "cite": [
            "250 F.3d 668",
            "2001 Cal. Daily Op. Serv. 3507",
            "2001 Daily Journal DAR 4351",
            "56 Fed. R. Serv. 698",
            "2001 U.S. App. LEXIS 8150"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
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
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jonathon Castro v. County of Los Angeles",
          "cluster_id": 4247081,
          "cite": [
            "833 F.3d 1060",
            "2016 U.S. App. LEXIS 14950",
            "2016 WL 4268955"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
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
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John C. McGuckin v. Dr. Smith John C. Medlen, Dr.",
          "cluster_id": 590324,
          "cite": [
            "974 F.2d 1050",
            "92 Cal. Daily Op. Serv. 7224",
            "23 Fed. R. Serv. 3d 922",
            "92 Daily Journal DAR 11690",
            "1992 U.S. App. LEXIS 19402",
            "1992 WL 201087"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
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
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James C. Dunkel",
          "cluster_id": 557241,
          "cite": [
            "927 F.2d 955",
            "67 A.F.T.R.2d (RIA) 637",
            "1991 U.S. App. LEXIS 3599",
            "1991 WL 28790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alfredo Miranda v. County of Lake",
          "cluster_id": 4525558,
          "cite": [
            "900 F.3d 335"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gebser v. Lago Vista Independent School District",
          "cluster_id": 118232,
          "cite": [
            "141 L. Ed. 2d 277",
            "118 S. Ct. 1989",
            "524 U.S. 274",
            "1998 U.S. LEXIS 4173"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Piotrowski v. City of Houston",
          "cluster_id": 22972,
          "cite": [
            "237 F.3d 567",
            "2001 U.S. App. LEXIS 603",
            "2001 WL 6712"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tjymas Blackmore v. Kalamazoo County",
          "cluster_id": 788501,
          "cite": [
            "390 F.3d 890",
            "2004 U.S. App. LEXIS 25057",
            "2004 WL 2792016"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Philomene Long, Surviving Spouse and Heir-At-Law of John Thomas Idlet, Deceased v. County of Los Angeles",
          "cluster_id": 793848,
          "cite": [
            "442 F.3d 1178",
            "2006 U.S. App. LEXIS 7552",
            "2006 WL 770615"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kneipp v. Tedder",
          "cluster_id": 726573,
          "cite": [
            "95 F.3d 1199",
            "159 A.L.R. Fed. 619",
            "1996 U.S. App. LEXIS 24401"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Grieveson v. Anderson",
          "cluster_id": 1443143,
          "cite": [
            "538 F.3d 763",
            "2008 WL 3823872"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
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
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Howlett Ex Rel. Howlett v. Rose",
          "cluster_id": 112456,
          "cite": [
            "110 L. Ed. 2d 332",
            "110 S. Ct. 2430",
            "496 U.S. 356",
            "1990 U.S. LEXIS 3077"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott L. Matthews v. Leon E. Jones, Sr., Jefferson County Police Department, and Unknown Police Officer, Jefferson County Police Department",
          "cluster_id": 678528,
          "cite": [
            "35 F.3d 1046",
            "1994 U.S. App. LEXIS 25924",
            "1994 WL 509049"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Everson v. Leis",
          "cluster_id": 1464717,
          "cite": [
            "556 F.3d 484",
            "2009 U.S. App. LEXIS 3288",
            "2009 WL 414625"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Canton v. Harris:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112209 OR 9431589 OR 9431590 OR 9431591) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTE0NDE5MjAwMDAwJnM9NzMyODI4MiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112209+OR+9431589+OR+9431590+OR+9431591%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112209 OR 9431589 OR 9431590 OR 9431591)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04MTImcz0xNTYyOTMmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112209+OR+9431589+OR+9431590+OR+9431591%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112209 OR 9431589 OR 9431590 OR 9431591)",
        "reviewed": 85,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 85,
        "triage_read": 0,
        "triage_snippet_classified": 85
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112209 OR 9431589 OR 9431590 OR 9431591)",
    "indexed_citing_opinions": 3328,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112209,
        "count": 2907,
        "count_source": "search"
      },
      {
        "opinion_id": 9431589,
        "count": 451,
        "count_source": "search"
      },
      {
        "opinion_id": 9431590,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431591,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 10152,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/city-of-canton-v-harris.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0MTI0OCZzPTEwNjE1NDQyJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112209+OR+9431589+OR+9431590+OR+9431591%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112209,
        "cited_id": 108153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 109349,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 110076,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 110589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 110998,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 111441,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 111615,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 111630,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 111831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 112017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 366970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 392242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 398831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 414191,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 424798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 424905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 447620,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 453103,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 459876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 460084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 462512,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 464799,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 469366,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 480385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 487192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 489887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 492036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112209,
        "cited_id": 501192,
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
    "date_created": "2026-07-05T00:11:30Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:11:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:11:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:17:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:11:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — City of Canton v. Harris

```
<div>
<center><b><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">489 U.S. 378</a></span> (1989)</b></center>
<center><h1>CITY OF CANTON, OHIO<br>
v.<br>
HARRIS ET AL.</h1></center>
<center>No. 86-1088.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 8, 1988</center>
<center>Decided February 28, 1989</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SIXTH CIRCUIT
<p><span class="star-pagination">*380</span> <i>Carter G. Phillips</i> argued the cause for petitioner. With him on the briefs were <i>Mark D. Hopson, W. Scott Gwin, William J. Hamann,</i> and <i>John S. Coury.</i></p>
<p><i>David Rudovsky</i> argued the cause for respondent. With him on the brief were <i>Emanuella Harris Groves</i> and <i>Dexter W. Clark.</i><sup>[*]</sup></p>
<p><i>John A. Powell, Steven R. Shapiro, Howard A. Friedman,</i> and <i>Michael Aaron Avery</i> filed a brief for the American Civil Liberties Union et al. as <i>amici curiae</i> urging affirmance.</p>
<p>JUSTICE WHITE delivered the opinion of the Court.</p>
<p>In this case, we are asked to determine if a municipality can ever be liable under <span class="citation no-link">42 U. S. C. § 1983</span><sup>[1]</sup> for constitutional violations resulting from its failure to train municipal employees. We hold that, under certain circumstances, such liability is permitted by the statute.</p>
<p></p>
<h2>
<span class="star-pagination">*381</span> I</h2>
<p>In April 1978, respondent Geraldine Harris was arrested by officers of the Canton Police Department. Mrs. Harris was brought to the police station in a patrol wagon.</p>
<p>When she arrived at the station, Mrs. Harris was found sitting on the floor of the wagon. She was asked if she needed medical attention, and responded with an incoherent remark. After she was brought inside the station for processing, Mrs. Harris slumped to the floor on two occasions. Eventually, the police officers left Mrs. Harris lying on the floor to prevent her from falling again. No medical attention was ever summoned for Mrs. Harris. After about an hour, Mrs. Harris was released from custody, and taken by an ambulance (provided by her family) to a nearby hospital. There, Mrs. Harris was diagnosed as suffering from several emotional ailments; she was hospitalized for one week and received subsequent outpatient treatment for an additional year.</p>
<p>Some time later, Mrs. Harris commenced this action alleging many state-law and constitutional claims against the city of Canton and its officials. Among these claims was one seeking to hold the city liable under <span class="citation no-link">42 U. S. C. § 1983</span> for its violation of Mrs. Harris' right, under the Due Process Clause of the Fourteenth Amendment, to receive necessary medical attention while in police custody.</p>
<p>A jury trial was held on Mrs. Harris' claims. Evidence was presented that indicated that, pursuant to a municipal regulation,<sup>[2]</sup> shift commanders were authorized to determine, in their sole discretion, whether a detainee required medical <span class="star-pagination">*382</span> care. Tr. X-XXX-X-XXX. In addition, testimony also suggested that Canton shift commanders were not provided with any special training (beyond first-aid training) to make a determination as to when to summon medical care for an injured detainee. <i>Ibid.;</i> App. to Pet. for Cert. 4a.</p>
<p>At the close of the evidence, the District Court submitted the case to the jury, which rejected all of Mrs. Harris' claims except one: her § 1983 claim against the city resulting from its failure to provide her with medical treatment while in custody. In rejecting the city's subsequent motion for judgment notwithstanding the verdict, the District Court explained the theory of liability as follows:</p>
<blockquote>"The evidence construed in a manner most favorable to Mrs. Harris could be found by a jury to demonstrate that the City of Canton had a custom or policy of vesting complete authority with the police supervisor of when medical treatment would be administered to prisoners. Further, the jury could find from the evidence that the vesting of such <i>carte blanche</i> authority with the police supervisor without adequate training to recognize when medical treatment is needed was grossly negligent or so reckless that future police misconduct was almost inevitable or substantially certain to result." <i>Id.,</i> at 16a.</blockquote>
<p>On appeal, the Sixth Circuit affirmed this aspect of the District Court's analysis, holding that "a municipality is liable for failure to train its police force, [where] the plaintiff . . . prove[s] that the municipality acted recklessly, intentionally, or with gross negligence." <i>Id.,</i> at 5a.<sup>[3]</sup> The Court of Appeals also stated that an additional prerequisite of this theory <span class="star-pagination">*383</span> of liability was that the plaintiff must prove "that the lack of training was so reckless or grossly negligent that deprivations of persons' constitutional rights were substantially certain to result." <i>Ibid.</i> Thus, the Court of Appeals found that there had been no error in submitting Mrs. Harris' "failure to train" claim to the jury. However, the Court of Appeals reversed the judgment for respondent, and remanded this case for a new trial, because it found that certain aspects of the District Court's jury instructions might have led the jury to believe that it could find against the city on a mere <i>respondeat superior</i> theory. Because the jury's verdict did not state the basis on which it had ruled for Mrs. Harris on her § 1983 claim, a new trial was ordered.</p>
<p>The city petitioned for certiorari, arguing that the Sixth Circuit's holding represented an impermissible broadening of municipal liability under § 1983. We granted the petition. <span class="citation multiple-matches"><a href="/c/U.%20S./485/933/">485 U. S. 933</a></span> (1988).</p>
<p></p>
<h2>II</h2>
<p>We first address respondent's contention that the writ of certiorari should be dismissed as improvidently granted, because "petitioner failed to preserve for review the principal issues it now argues in this Court." Brief for Respondent 5.</p>
<p>We think it clear enough that petitioner's three "Questions Presented" in its petition for certiorari encompass the critical question before us in this case: Under what circumstances can inadequate training be found to be a "policy" that is actionable under § 1983? See Pet. for Cert. i. The petition itself addressed this issue directly, attacking the Sixth Circuit's "failure to train" theory as inconsistent with this Court's precedents. See <i>id.,</i> at 8-12. It is also clear  as respondent conceded at argument, Tr. of Oral Arg. 34, 54  that her brief in opposition to our granting of certiorari did not raise the objection that petitioner had failed to press its claims on the courts below.</p>
<p>As to respondent's contention that the claims made by petitioner here were not made in the same fashion below, that <span class="star-pagination">*384</span> failure, if it occurred, does not affect our jurisdiction; and because respondent did not oppose our grant of review at that time based on her contention that these claims were not pressed below, we will not dismiss the writ as improvidently granted. "[T]he `decision to grant certiorari represents a commitment of scarce judicial resources with a view to deciding the merits . . . of the questions presented in the petition.' " <i>St. Louis</i> v. <i>Praprotnik,</i> <span class="citation" data-id="9431224"><a href="/opinion/112017/city-of-st-louis-v-praprotnik/#120" aria-description="Citation for case: City of St. Louis v. Praprotnik">485 U. S. 112, 120</a></span> (1988) (quoting <i>Oklahoma City</i> v. <i>Tuttle,</i> <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#816" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S. 808, 816</a></span> (1985)). As we have expressly admonished litigants in respondent's position: "Nonjurisdictional defects of this sort should be brought to our attention <i>no later</i> than in respondent's brief in opposition to the petition for certiorari; if not, we consider it within our discretion to deem the defect waived." <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#816" aria-description="Citation for case: City of Oklahoma v. Tuttle"><i>Tuttle, supra,</i> at 816</a></span>.</p>
<p>It is true that petitioner's litigation posture with respect to the questions presented here has not been consistent; most importantly, petitioner conceded below that " `inadequate training' [is] a means of establishing municipal liability under Section 1983." Reply Brief for Petitioner 4, n. 3; see also Petition for Rehearing in No. 85-3314 (CA6), p. 1. However, at each stage in the proceedings below, petitioner contested any finding of liability on this ground, with objections of varying specificity. It opposed the District Court's jury instructions on this issue, Tr. 4-369; claimed in its judgment notwithstanding verdict motion that there was "no evidence of a . . . policy or practice on the part of the City . . . [of] den[ying] medical treatment to prisoners," Motion for Judgment Notwithstanding Verdict in No. C80-18-A (ND Ohio), p. 1; and argued to the Court of Appeals that there was no basis for finding a policy of denying medical treatment to prisoners in this case. See Brief for Appellant in No. 85-3314 (CA6), pp. 26-29. Indeed, petitioner specifically contended that the Sixth Circuit precedents that permitted inadequate training to be a basis for municipal liability on facts similar to these, see n. 3, <i>supra,</i> were in conflict with <span class="star-pagination">*385</span> our decision in <i><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">Tuttle</a></span>.</i> Brief for Appellant in No. 85-3314 (CA6), p. 29. These various presentations of the issues below might have been so inexact that we would have denied certiorari had this matter been brought to our attention at the appropriate stage in the proceedings. But they were at least adequate to yield a decision by the Sixth Circuit on the questions presented for our review now.</p>
<p>Here the Sixth Circuit held that where a plaintiff proves that a municipality, acting recklessly, intentionally, or with gross negligence, has failed to train its police force  resulting in a deprivation of constitutional rights that was "substantially certain to result"  § 1983 permits that municipality to be held liable for its actions. Petitioner's petition for certiorari challenged the soundness of that conclusion, and respondent did not inform us prior to the time that review was granted that petitioner had arguably conceded this point below. Consequently, we will not abstain from addressing the question before us.</p>
<p></p>
<h2>III</h2>
<p>In <i>Monell</i> v. <i>New York City Dept. of Social Services,</i> <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658</a></span> (1978), we decided that a municipality can be found liable under § 1983 only where the municipality <i>itself</i> causes the constitutional violation at issue. <i>Respondeat superior</i> or vicarious liability will not attach under § 1983. <i>Id.,</i> at 694-695. "It is only when the `execution of the government's policy or custom . . . inflicts the injury' that the municipality may be held liable under § 1983." <i>Springfield</i> v. <i>Kibbe,</i> <span class="citation" data-id="9430858"><a href="/opinion/111831/city-of-springfield-v-kibbe/#267" aria-description="Citation for case: City of Springfield v. Kibbe">480 U. S. 257, 267</a></span> (1987) (O'CONNOR, J., dissenting) (quoting <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs."><i>Monell, supra,</i> at 694</a></span>).</p>
<p>Thus, our first inquiry in any case alleging municipal liability under § 1983 is the question whether there is a direct causal link between a municipal policy or custom and the alleged constitutional deprivation. The inquiry is a difficult one; one that has left this Court deeply divided in a series of <span class="star-pagination">*386</span> cases that have followed <i><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span>;</i><sup>[4]</sup> one that is the principal focus of our decision again today.</p>
<p></p>
<h2>A</h2>
<p>Based on the difficulty that this Court has had defining the contours of municipal liability in these circumstances, petitioner urges us to adopt the rule that a municipality can be found liable under § 1983 only where "the policy in question [is] itself unconstitutional." Brief for Petitioner 15. Whether such a rule is a valid construction of § 1983 is a question the Court has left unresolved. See, <i>e. g., </i><i>St. Louis</i> v. <span class="citation" data-id="9431224"><a href="/opinion/112017/city-of-st-louis-v-praprotnik/#147" aria-description="Citation for case: City of St. Louis v. Praprotnik"><i>Praprotnik, supra,</i> at 147</a></span> (BRENNAN, J., concurring in judgment); <i>Oklahoma City</i> v. <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#824" aria-description="Citation for case: City of Oklahoma v. Tuttle"><i>Tuttle, supra,</i> at 824, n. 7</a></span>. Under such an approach, the outcome here would be rather clear: we would have to reverse and remand the case with instructions that judgment be entered for petitioner.<sup>[5]</sup> There can be little doubt that on its face the city's policy regarding medical treatment for detainees is constitutional. The policy states that the city jailer "shall . . . have [a person needing medical care] taken to a hospital for medical treatment, with <span class="star-pagination">*387</span> permission of his supervisor . . . ." App. 33. It is difficult to see what constitutional guarantees are violated by such a policy.</p>
<p>Nor, without more, would a city automatically be liable under § 1983 if one of its employees happened to apply the policy in an unconstitutional manner, for liability would then rest on <i>respondeat superior.</i> The claim in this case, however, is that if a concededly valid policy is unconstitutionally applied by a municipal employee, the city is liable if the employee has not been adequately trained and the constitutional wrong has been caused by that failure to train. For reasons explained below, we conclude, as have all the Courts of Appeals that have addressed this issue,<sup>[6]</sup> that there are limited circumstances in which an allegation of a "failure to train" can be the basis for liability under § 1983. Thus, we reject petitioner's contention that only unconstitutional policies are actionable under the statute.</p>
<p></p>
<h2>
<span class="star-pagination">*388</span> B</h2>
<p>Though we agree with the court below that a city can be liable under § 1983 for inadequate training of its employees, we cannot agree that the District Court's jury instructions on this issue were proper, for we conclude that the Court of Appeals provided an overly broad rule for when a municipality can be held liable under the "failure to train" theory. Unlike the question whether a municipality's failure to train employees can ever be a basis for § 1983 liability  on which the Courts of Appeals have all agreed, see n. 6, <i>supra,</i>  there is substantial division among the lower courts as to what <i>degree of fault</i> must be evidenced by the municipality's inaction before liability will be permitted.<sup>[7]</sup> We hold today that the inadequacy of police training may serve as the basis for § 1983 liability only where the failure to train amounts to deliberate indifference to the rights of persons with whom the police come into contact.<sup>[8]</sup> This rule is most consistent with our admonition <span class="star-pagination">*389</span> in <i>Monell,</i> <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 694</a></span>, and <i>Polk County</i> v. <i>Dodson,</i> <span class="citation" data-id="9428551"><a href="/opinion/110589/polk-county-v-dodson/#326" aria-description="Citation for case: Polk County v. Dodson">454 U. S. 312, 326</a></span> (1981), that a municipality can be liable under § 1983 only where its policies are the "moving force [behind] the constitutional violation." Only where a municipality's failure to train its employees in a relevant respect evidences a "deliberate indifference" to the rights of its inhabitants can such a shortcoming be properly thought of as a city "policy or custom" that is actionable under § 1983. As JUSTICE BRENNAN's opinion in <i>Pembaur</i> v. <i>Cincinnati,</i> <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#483" aria-description="Citation for case: Pembaur v. City of Cincinnati">475 U. S. 469, 483-484</a></span> (1986) (plurality) put it: "[M]unicipal liability under § 1983 attaches where  and only where  a deliberate choice to follow a course of action is made from among various alternatives" by city policymakers. See also <i>Oklahoma City</i> v. <i>Tuttle,</i> <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#823" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S., at 823</a></span> (opinion of REHNQUIST, J.). Only where a failure to train reflects a "deliberate" or "conscious" choice by a municipality  a "policy" as defined by our prior cases  can a city be liable for such a failure under § 1983.</p>
<p><i>Monell's</i> rule that a city is not liable under § 1983 unless a municipal policy causes a constitutional deprivation will not be satisfied by merely alleging that the existing training program for a class of employees, such as police officers, represents a policy for which the city is responsible.<sup>[9]</sup> That much <span class="star-pagination">*390</span> may be true. The issue in a case like this one, however, is whether that training program is adequate; and if it is not, the question becomes whether such inadequate training can justifiably be said to represent "city policy." It may seem contrary to common sense to assert that a municipality will actually have a policy of not taking reasonable steps to train its employees. But it may happen that in light of the duties assigned to specific officers or employees the need for more or different training is so obvious, and the inadequacy so likely to result in the violation of constitutional rights, that the policymakers of the city can reasonably be said to have been deliberately indifferent to the need.<sup>[10]</sup> In that event, the failure to provide proper training may fairly be said to represent a policy for which the city is responsible, and for which the city may be held liable if it actually causes injury.<sup>[11]</sup></p>
<p>In resolving the issue of a city's liability, the focus must be on adequacy of the training program in relation to the tasks the particular officers must perform. That a particular officer may be unsatisfactorily trained will not alone suffice to fasten liability on the city, for the officer's shortcomings may <span class="star-pagination">*391</span> have resulted from factors other than a faulty training program. See <i>Springfield</i> v. <i>Kibbe,</i> <span class="citation" data-id="9430858"><a href="/opinion/111831/city-of-springfield-v-kibbe/#268" aria-description="Citation for case: City of Springfield v. Kibbe">480 U. S., at 268</a></span> (O'CONNOR, J., dissenting); <i>Oklahoma City</i> v. <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#821" aria-description="Citation for case: City of Oklahoma v. Tuttle"><i>Tuttle, supra,</i> at 821</a></span> (opinion of REHNQUIST, J.). It may be, for example, that an otherwise sound program has occasionally been negligently administered. Neither will it suffice to prove that an injury or accident could have been avoided if an officer had had better or more training, sufficient to equip him to avoid the particular injury-causing conduct. Such a claim could be made about almost any encounter resulting in injury, yet not condemn the adequacy of the program to enable officers to respond properly to the usual and recurring situations with which they must deal. And plainly, adequately trained officers occasionally make mistakes; the fact that they do says little about the training program or the legal basis for holding the city liable.</p>
<p>Moreover, for liability to attach in this circumstance the identified deficiency in a city's training program must be closely related to the ultimate injury. Thus in the case at hand, respondent must still prove that the deficiency in training actually caused the police officers' indifference to her medical needs.<sup>[12]</sup> Would the injury have been avoided had the employee been trained under a program that was not deficient in the identified respect? Predicting how a hypothetically well-trained officer would have acted under the circumstances may not be an easy task for the factfinder, particularly since matters of judgment may be involved, and since officers who are well trained are not free from error and perhaps might react very much like the untrained officer in similar circumstances. But judge and jury, doing their respective jobs, will be adequate to the task.</p>
<p>To adopt lesser standards of fault and causation would open municipalities to unprecedented liability under § 1983. <span class="star-pagination">*392</span> In virtually every instance where a person has had his or her constitutional rights violated by a city employee, a § 1983 plaintiff will be able to point to something the city "could have done" to prevent the unfortunate incident. See <i>Oklahoma City</i> v. <i>Tuttle,</i> <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#823" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S., at 823</a></span> (opinion of REHNQUIST, J.). Thus, permitting cases against cities for their "failure to train" employees to go forward under § 1983 on a lesser standard of fault would result in <i>de facto respondeat superior</i> liability on municipalities  a result we rejected in <i>Monell,</i> <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#693" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 693-694</a></span>. It would also engage the federal courts in an endless exercise of second-guessing municipal employee-training programs. This is an exercise we believe the federal courts are ill suited to undertake, as well as one that would implicate serious questions of federalism. Cf. <i>Rizzo</i> v. <i>Goode,</i> <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/#378" aria-description="Citation for case: Rizzo v. Goode">423 U. S. 362, 378-380</a></span> (1976).</p>
<p>Consequently, while claims such as respondent's  alleging that the city's failure to provide training to municipal employees resulted in the constitutional deprivation she suffered  are cognizable under § 1983, they can only yield liability against a municipality where that city's failure to train reflects deliberate indifference to the constitutional rights of its inhabitants.</p>
<p></p>
<h2>IV</h2>
<p>The final question here is whether this case should be remanded for a new trial, or whether, as petitioner suggests, we should conclude that there are no possible grounds on which respondent can prevail. See Tr. of Oral Arg. 57-58. It is true that the evidence in the record now does not meet the standard of § 1983 liability we have set forth above. But, the standard of proof the District Court ultimately imposed on respondent (which was consistent with Sixth Circuit precedent) was a lesser one than the one we adopt today, see Tr. X-XXX-X-XXX. Whether respondent should have an opportunity to prove her case under the "deliberate indifference" rule we have adopted is a matter for the Court of Appeals to deal with on remand.</p>
<p></p>
<h2>
<span class="star-pagination">*393</span> V</h2>
<p>Consequently, for the reasons given above, we vacate the judgment of the Court of Appeals and remand this case for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE BRENNAN, concurring.</p>
<p>The Court's opinion, which I join, makes clear that the Court of Appeals is free to remand this case for a new trial.</p>
<p>JUSTICE O'CONNOR, with whom JUSTICE SCALIA and JUSTICE KENNEDY join, concurring in part and dissenting in part.</p>
<p>I join Parts I and II and all of Part III of the Court's opinion except footnote 11, see <i>ante,</i> at 390, n. 11. I thus agree that where municipal policymakers are confronted with an obvious need to train city personnel to avoid the violation of constitutional rights and they are deliberately indifferent to that need, the lack of necessary training may be appropriately considered a city "policy" subjecting the city itself to liability under our decision in <i>Monell</i> v. <i>New York City Dept. of Social Services,</i> <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658</a></span> (1978). As the Court observes, "[o]nly where a failure to train reflects a `deliberate' or `conscious' choice by a municipality  a `policy' as defined by our prior cases  can a city be liable for such a failure under [42 U. S. C.] § 1983." <i>Ante,</i> at 389. I further agree that a § 1983 plaintiff pressing a "failure to train" claim must prove that the lack of training was the "cause" of the constitutional injury at issue and that this entails more than simply showing "but for" causation. <i>Ante,</i> at 392. Lesser requirements of fault and causation in this context would "open municipalities to unprecedented liability under § 1983," <i>ante,</i> at 391, and would pose serious federalism concerns. <i>Ante,</i> at 392.</p>
<p>My single point of disagreement with the majority is thus a small one. Because I believe, as the majority strongly hints, <span class="star-pagination">*394</span> see <i>ibid.,</i> that respondent has not and could not satisfy the fault and causation requirements we adopt today, I think it unnecessary to remand this case to the Court of Appeals for further proceedings. This case comes to us after a full trial during which respondent vigorously pursued numerous theories of municipal liability including an allegation that the city had a "custom" of not providing medical care to detainees suffering from emotional illnesses. Respondent thus had every opportunity and incentive to adduce the type of proof necessary to satisfy the deliberate indifference standard we adopt today. Rather than remand in this context, I would apply the deliberate indifference standard to the facts of this case. After undertaking that analysis below, I conclude that there is no evidence in the record indicating that the city of Canton has been deliberately indifferent to the constitutional rights of pretrial detainees.</p>
<p></p>
<h2>I</h2>
<p>In <i><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span>,</i> the Court held that municipal liability can be imposed under § 1983 only where the municipality, as an entity, can be said to be "responsible" for a constitutional violation committed by one of its employees. "[T]he touchstone of the § 1983 action against a government body is an allegation that official policy is responsible for a deprivation of rights protected by the Constitution." <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#690" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 690</a></span>. The Court found that the language of § 1983, and rejection of the "Sherman Amendment" by the 42d Congress, were both strong indicators that the framers of the Civil Rights Act of 1871 did not intend that municipal governments be held vicariously liable for the constitutional torts of their employees. Thus a § 1983 plaintiff seeking to attach liability to the city for the acts of one of its employees may not rest on the employment relationship alone; both fault and causation <i>as to the acts or omissions of the city itself</i> must be proved. The Court reaffirms these requirements today.</p>
<p>Where, as here, a claim of municipal liability is predicated upon a failure to act, the requisite degree of fault must be <span class="star-pagination">*395</span> shown by proof of a background of events and circumstances which establish that the "policy of inaction" is the functional equivalent of a decision by the city itself to violate the Constitution. Without some form of notice to the city, and the opportunity to conform to constitutional dictates both what it does and what it chooses not to do, the failure to train theory of liability could completely engulf <i><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span>,</i> imposing liability without regard to fault. Moreover, absent a requirement that the lack of training at issue bear a very close causal connection to the violation of constitutional rights, the failure to train theory of municipal liability could impose "prophylactic" duties on municipal governments only remotely connected to underlying constitutional requirements themselves.</p>
<p>Such results would be directly contrary to the intent of the drafters of § 1983. The central vice of the Sherman Amendment, as noted by the Court's opinion in <i><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span>,</i> was that it "impose[d] a species of vicarious liability on municipalities since it could be construed to impose liability even if the municipality <i>did not know</i> of an impending or ensuing riot or did not have the wherewithal to do anything about it." <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#692" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 692, n. 57</a></span> (emphasis added). Moreover, as noted in <i><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span>,</i> the authors of § 1 of the Ku Klux Act did not intend to create any new rights or duties beyond those contained in the Constitution. <i>Id.,</i> at 684-685. Thus, § 1 was referred to as "reenacting the Constitution." Cong. Globe, 42d Cong., 1st Sess., 569 (1871) (Rep. Edmunds). Representative Bingham, the author of § 1 of the Fourteenth Amendment, saw the purpose of § 1983 as "the enforcement . . . of the Constitution on behalf of every individual citizen of the Republic . . . to the extent of the rights guaranteed to him by the Constitution." <i>Id.,</i> at App. 81. See also <i>Chapman</i> v. <i>Houston Welfare Rights Organization,</i> <span class="citation" data-id="9427567"><a href="/opinion/110076/chapman-v-houston-welfare-rights-organization/#617" aria-description="Citation for case: Chapman v. Houston Welfare Rights Organization">441 U. S. 600, 617</a></span> (1979) ("[Section] 1 of the Civil Rights Act of 1871 did not provide for any substantive rights  equal or otherwise. As introduced and enacted, it served only to insure that an individual had a cause of action for violations of the Constitution"). <span class="star-pagination">*396</span> Thus § 1983 is not a "federal good government act" for municipalities. Rather it creates a federal cause of action against persons, including municipalities, who deprive citizens of the United States of their constitutional rights.</p>
<p>Sensitive to these concerns, the Court's opinion correctly requires a high degree of fault on the part of city officials before an omission that is not in itself unconstitutional can support liability as a municipal policy under <i><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span>.</i> As the Court indicates, "it may happen that . . . the need for more or different training is so obvious, and the inadequacy so likely to result in the violation of constitutional rights, that the policymakers of the city can reasonably be said to have been deliberately indifferent to the need." <i>Ante,</i> at 390. Where a § 1983 plaintiff can establish that the facts available to city policymakers put them on actual or constructive notice that the particular omission is substantially certain to result in the violation of the constitutional rights of their citizens, the dictates of <i><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span></i> are satisfied. Only then can it be said that the municipality has made " `a deliberate choice to follow a course of action . . . from among various alternatives.' " <i>Ante,</i> at 389, quoting <i>Pembaur</i> v. <i>Cincinnati,</i> <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#483" aria-description="Citation for case: Pembaur v. City of Cincinnati">475 U. S. 469, 483-484</a></span> (1986).</p>
<p>In my view, it could be shown that the need for training was obvious in one of two ways. First, a municipality could fail to train its employees concerning a clear constitutional duty implicated in recurrent situations that a particular employee is certain to face. As the majority notes, see <i>ante,</i> at 390, n. 10, the constitutional limitations established by this Court on the use of deadly force by police officers present one such situation. The constitutional duty of the individual officer is clear, and it is equally clear that failure to inform city personnel of that duty will create an extremely high risk that constitutional violations will ensue.</p>
<p>The claim in this case  that police officers were inadequately trained in diagnosing the symptoms of emotional illness  falls far short of the kind of "obvious" need for training <span class="star-pagination">*397</span> that would support a finding of deliberate indifference to constitutional rights on the part of the city. As the Court's opinion observes, <i>ante,</i> at 388-389, n. 8, this Court has not yet addressed the precise nature of the obligations that the Due Process Clause places upon the police to seek medical care for pretrial detainees who have been <i>physically</i> injured while being apprehended by the police. See <i>Revere</i> v. <i>Massachusetts General Hospital,</i> <span class="citation" data-id="9429305"><a href="/opinion/110998/city-of-revere-v-massachusetts-general-hospital/#246" aria-description="Citation for case: City of Revere v. Massachusetts General Hospital">463 U. S. 239, 246</a></span> (1983) (REHNQUIST, J., concurring). There are thus no clear constitutional guideposts for municipalities in this area, and the diagnosis of mental illness is not one of the "usual and recurring situations with which [the police] must deal." <i>Ante,</i> at 391. The lack of training at issue here is not the kind of omission that can be characterized, in and of itself, as a "deliberate indifference" to constitutional rights.</p>
<p>Second, I think municipal liability for failure to train may be proper where it can be shown that policymakers were aware of, and acquiesced in, a pattern of constitutional violations involving the exercise of police discretion. In such cases, the need for training may not be obvious from the outset, but a pattern of constitutional violations could put the municipality on notice that its officers confront the particular situation on a regular basis, and that they often react in a manner contrary to constitutional requirements. The lower courts that have applied the "deliberate indifference" standard we adopt today have required a showing of a pattern of violations from which a kind of "tacit authorization" by city policymakers can be inferred. See, <i>e. g., </i><i>Fiacco</i> v. <i>Rensselaer,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/783/319/">783 F. 2d 319</a></span>, 327 (CA2 1986) (multiple incidents required for finding of deliberate indifference); <i>Patzner</i> v. <i>Burkett,</i> <span class="citation" data-id="462512"><a href="/opinion/462512/leland-patzner-v-joyce-burkett-aka-joyce-mclaughlin-deborah-myerchin-and/#1367" aria-description="Citation for case: Leland Patzner v. Joyce Burkett A/K/A Joyce McLaughlin...">779 F. 2d 1363, 1367</a></span> (CA8 1985) ("[A] municipality may be liable if it had notice of prior misbehavior by its officers and failed to take remedial steps amounting to deliberate indifference to the offensive acts"); <i>Languirand</i> v. <i>Hayden,</i> <span class="citation" data-id="9471173"><a href="/opinion/424798/john-languirand-cross-appellant-v-john-hayden-an-individual-city-of/#227" aria-description="Citation for case: John Languirand, Cross-Appellant v. John Hayden, an...">717 F. 2d 220, 227-228</a></span> (CA5 1983) (municipal liability for failure to train requires "evidence at least of a pattern of similar <span class="star-pagination">*398</span> incidents in which citizens were injured or endangered"); <i>Wellington</i> v. <i>Daniels,</i> <span class="citation" data-id="424905"><a href="/opinion/424905/cynthia-wellington-guardian-of-the-estate-of-robert-d-gravelle-v-brian/#936" aria-description="Citation for case: Cynthia Wellington, Guardian of the Estate of Robert D....">717 F. 2d 932, 936</a></span> (CA4 1983) ("[A] failure to supervise gives rise to § 1983 liability, however, only in those situations where there is a history of widespread abuse. Only then may knowledge be imputed to the supervisory personnel").</p>
<p>The Court's opinion recognizes this requirement, see <i>ante,</i> at 390, and n. 10, but declines to evaluate the evidence presented in this case in light of the new legal standard. <i>Ante,</i> at 392. From the outset of this litigation, respondent has pressed a claim that the city of Canton had a custom of denying medical care to pretrial detainees with emotional disorders. See Amended Complaint ¶ 28, App. 27. Indeed, up to and including oral argument before this Court, counsel for respondent continued to assert that respondent was attempting to hinge municipal liability upon "both a custom of denying medical care to a certain class of prisoners, and a failure to train police that led to this particular violation." Tr. of Oral Arg. 37-38. At the time respondent filed her complaint in 1980, it was clear that proof of the existence of a custom entailed a showing of "practices . . . so permanent and well settled as to constitute a `custom or usage' with the force of law." <i>Adickes</i> v. <i>S. H. Kress &amp; Co.,</i> <span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/#168" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">398 U. S. 144, 168</a></span> (1970); see also <i>Garner</i> v. <i>Memphis Police Department,</i> <span class="citation" data-id="366970"><a href="/opinion/366970/garner-v-memphis-police-department/#54" aria-description="Citation for case: Garner v. Memphis Police Department">600 F. 2d 52, 54-55</a></span>, and n. 4 (CA6 1979) (discussing proof of custom in light of <i>Monell</i>).</p>
<p>Whatever the prevailing standard at the time concerning liability for failure to train, respondent thus had every incentive to adduce proof at trial of a pattern of violations to support her claim that the city had an unwritten custom of denying medical care to emotionally ill detainees. In fact, respondent presented no testimony from any witness indicating that there had been past incidents of "deliberate indifference" to the medical needs of emotionally disturbed detainees or that any other circumstance had put the city on actual or constructive notice of a need for additional training in this <span class="star-pagination">*399</span> regard. At trial, David Maser, who was Chief of Police of the city of Canton from 1971 to 1980, testified without contradiction that during his tenure he received no complaints that detainees in the Canton jails were not being accorded proper medical treatment. Tr. 4-347  4-348. Former Officer Cherry, who had served as a jailer for the Canton Police Department, indicated that he had never had to seek medical treatment for persons who were emotionally upset at the prospect of arrest, because they usually calmed down when a member of the department spoke with them or one of their family members arrived. <i><span class="citation" data-id="366970"><a href="/opinion/366970/garner-v-memphis-police-department/" aria-description="Citation for case: Garner v. Memphis Police Department">Id.,</a></span></i> at 4-83  4-84. There is quite simply nothing in this record to indicate that the city of Canton had any reason to suspect that failing to provide this kind of training would lead to injuries of any kind, let alone violations of the Due Process Clause. None of the Courts of Appeals that already apply the standard we adopt today would allow respondent to take her claim to a jury based on the facts she adduced at trial. See <i>Patzner</i> v. <span class="citation" data-id="462512"><a href="/opinion/462512/leland-patzner-v-joyce-burkett-aka-joyce-mclaughlin-deborah-myerchin-and/#1367" aria-description="Citation for case: Leland Patzner v. Joyce Burkett A/K/A Joyce McLaughlin..."><i>Burkett, supra,</i> at 1367</a></span> (summary judgment proper under "deliberate indifference" standard where evidence of only single incident adduced); <i>Languirand</i> v. <span class="citation" data-id="9471173"><a href="/opinion/424798/john-languirand-cross-appellant-v-john-hayden-an-individual-city-of/#229" aria-description="Citation for case: John Languirand, Cross-Appellant v. John Hayden, an..."><i>Hayden, supra,</i> at 229</a></span> (reversing jury verdict rendered under failure to train theory where there was no evidence of prior incidents to support a finding that municipal policymakers were "consciously indifferent" to constitutional rights); <i>Wellington</i> v. <span class="citation" data-id="424905"><a href="/opinion/424905/cynthia-wellington-guardian-of-the-estate-of-robert-d-gravelle-v-brian/#937" aria-description="Citation for case: Cynthia Wellington, Guardian of the Estate of Robert D...."><i>Daniels, supra,</i> at 937</a></span> (affirming judgment notwithstanding verdict for municipality under "deliberate indifference" standard where evidence of only a single incident was presented at trial); cf. <i>Fiacco</i> v. <i>Rensselaer, supra,</i> at 328-332 (finding evidence of "deliberate indifference" sufficient to support jury verdict where a pattern of similar violations was shown at trial).</p>
<p>Allowing an inadequate training claim such as this one to go to the jury based upon a single incident would only invite jury nullification of <i><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span>.</i> "To infer the existence of a city policy from the isolated misconduct of a single, low-level officer, and then to hold the city liable on the basis of that policy, <span class="star-pagination">*400</span> would amount to permitting precisely the theory of strict <i>respondeat superior</i> liability rejected in <i>Monell." Oklahoma City</i> v. <i>Tuttle,</i> <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#831" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S. 808, 831</a></span> (1985) (BRENNAN, J., concurring in part and concurring in judgment). As the authors of the Ku Klux Act themselves realized, the resources of local government are not inexhaustible. The grave step of shifting those resources to particular areas where constitutional violations are likely to result through the deterrent power of § 1983 should certainly not be taken on the basis of an isolated incident. If § 1983 and the Constitution require the city of Canton to provide detailed medical and psychological training to its police officers, or to station paramedics at its jails, other city services will necessarily suffer, including those with far more direct implications for the protection of constitutional rights. Because respondent's evidence falls far short of establishing the high degree of fault on the part of the city required by our decision today, and because there is no indication that respondent could produce any new proof in this regard, I would reverse the judgment of the Court of Appeals and order entry of judgment for the city.</p>
<h2>NOTES</h2>
<p>[*]  <i>Benna Ruth Solomon, Beate Bloch,</i> and <i>Richard K. Willard</i> filed a brief for the International City Management Association et al. as <i>amici curiae</i> urging reversal.</p>
<p>[1]  Title <span class="citation no-link">42 U. S. C. § 1983</span> provides, in relevant part, that:
</p>
<p>"Every person who, under color of any statute, ordinance, regulation, custom, or usage . . . subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress. . . ."</p>
<p>[2]  The city regulation in question provides that a police officer assigned to act as "jailer" at the city police station
</p>
<p>"shall, when a prisoner is found to be unconscious or semi-unconscious, or when he or she is unable to explain his or her condition, or who complains of being ill, have such person taken to a hospital for medical treatment, with permission of his supervisor before admitting the person to City Jail." App. 33.</p>
<p>[3]  In upholding Mrs. Harris' "failure to train" claim, the Sixth Circuit relied on two of its previous decisions which had approved such a theory of municipal liability under § 1983. See <i>Rymer</i> v. <i>Davis,</i> <span class="citation" data-id="447620"><a href="/opinion/447620/paul-d-rymer-v-trooper-ha-davis-city-of-shepherdsville-kentucky-and/" aria-description="Citation for case: Paul D. Rymer v. Trooper H.A. Davis, City of...">754 F. 2d 198</a></span>, vacated and remanded <i>sub nom. </i><i>Shepherdsville</i> v. <i>Rhymer,</i> <span class="citation" data-id="9048113"><a href="/opinion/9054597/city-of-shepherdsville-v-rymer/" aria-description="Citation for case: City of Shepherdsville v. Rymer">473 U. S. 901</a></span>, reinstated, <span class="citation" data-id="460084"><a href="/opinion/460084/paul-d-rymer-v-trooper-ha-davis-city-of-shepherdsville-kentucky-and/#757" aria-description="Citation for case: Paul D. Rymer v. Trooper H.A. Davis, City of...">775 F. 2d 756, 757</a></span> (1985); <i>Hays</i> v. <i>Jefferson County,</i> <span class="citation" data-id="9468792"><a href="/opinion/398831/donald-l-hays-jr-and-michael-c-potter-cross-appellants-v-jefferson/#874" aria-description="Citation for case: Donald L. Hays, Jr., and Michael C. Potter,...">668 F. 2d 869, 874</a></span> (1982).</p>
<p>[4]  See, <i>e. g., </i><i>St. Louis</i> v. <i>Praprotnik,</i> <span class="citation" data-id="9431224"><a href="/opinion/112017/city-of-st-louis-v-praprotnik/" aria-description="Citation for case: City of St. Louis v. Praprotnik">485 U. S. 112</a></span> (1988); <i>Springfield</i> v. <i>Kibbe,</i> <span class="citation" data-id="9430858"><a href="/opinion/111831/city-of-springfield-v-kibbe/" aria-description="Citation for case: City of Springfield v. Kibbe">480 U. S. 257</a></span> (1987); <i>Los Angeles</i> v. <i>Heller,</i> <span class="citation" data-id="9430425"><a href="/opinion/111630/city-of-los-angeles-v-heller/" aria-description="Citation for case: City of Los Angeles v. Heller">475 U. S. 796</a></span> (1986); <i>Oklahoma City</i> v. <i>Tuttle,</i> <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S. 808</a></span> (1985).</p>
<p>[5]  In this Court, in addition to suggesting that the city's failure to train its officers amounted to a "policy" that resulted in the denial of medical care to detainees, respondent also contended the city had a "custom" of denying medical care to those detainees suffering from emotional or mental ailments. See Brief for Respondent 31-32; Tr. of Oral Arg. 38-39. As respondent described it in her brief, and at argument, this claim of an unconstitutional "custom" appears to be little more than a restatement of her "failure-to-train as policy" claim. See <i><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">ibid.</a></span></i>
</p>
<p>However, to the extent that this claim poses a distinct basis for the city's liability under § 1983, we decline to determine whether respondent's contention that such a "custom" existed is an alternative ground for affirmance. The "custom" claim was not passed on by the Court of Appeals  nor does it appear to have been presented to that court as a distinct ground for its decision. See Brief of Appellee in No. 85-3314 (CA6), pp. 4-9, 11. Thus, we will not consider it here.</p>
<p>[6]  In addition to the Sixth Circuit decisions discussed in n. 3, <i>supra,</i> most of the other Courts of Appeals have held that a failure to train can create liability under § 1983. See, <i>e. g., </i><i>Spell</i> v. <i>McDaniel,</i> <span class="citation" data-id="8952845"><a href="/opinion/8961657/spell-v-mcdaniel/#1389" aria-description="Citation for case: Spell v. McDaniel">824 F. 2d 1380, 1389-1391</a></span> (CA4 1987); <i>Haynesworth</i> v. <i>Miller,</i> 261 U. S. App. D. C. 66, 80-83, <span class="citation" data-id="9476300"><a href="/opinion/489887/josiah-haynesworth-and-fred-hancock-v-frank-p-miller-chief-law/#1259" aria-description="Citation for case: Josiah Haynesworth and Fred Hancock v. Frank P. Miller,...">820 F. 2d 1245, 1259-1262</a></span> (1987); <i>Warren</i> v. <i>Lincoln,</i> <span class="citation" data-id="487192"><a href="/opinion/487192/jackson-warren-v-city-of-lincoln-nebraska-james-breen-sandra-l-myers-and/#1262" aria-description="Citation for case: Jackson Warren v. City of Lincoln, Nebraska James Breen...">816 F. 2d 1254, 1262-1263</a></span> (CA8 1987); <i>Bergquist</i> v. <i>County of Cochise,</i> <span class="citation" data-id="8946582"><a href="/opinion/8955600/bergquist-v-county-of-cochise/#1369" aria-description="Citation for case: Bergquist v. County of Cochise">806 F. 2d 1364, 1369-1370</a></span> (CA9 1986); <i>Wierstak</i> v. <i>Heffernan,</i> <span class="citation" data-id="469366"><a href="/opinion/469366/philip-f-wierstak-v-james-w-heffernan-philip-f-wierstak-v-james-w/#974" aria-description="Citation for case: Philip F. Wierstak v. James W. Heffernan, Philip F....">789 F. 2d 968, 974</a></span> (CA1 1986); <i>Fiacco</i> v. <i>Rensselaer,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/783/319/">783 F. 2d 319</a></span>, 326-327 (CA2 1986); <i>Gilmere</i> v. <i>Atlanta,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/774/1495/">774 F. 2d 1495</a></span>, 1503-1504 (CA11 1985) (en banc); <i>Rock</i> v. <i>McCoy,</i> <span class="citation" data-id="453103"><a href="/opinion/453103/charlie-rock-jr-v-roy-mccoy-and-the-city-of-checotah-oklahoma-a/#397" aria-description="Citation for case: Charlie Rock, Jr. v. Roy McCoy and the City of Checotah,...">763 F. 2d 394, 397-398</a></span> (CA10 1985); <i>Languirand</i> v. <i>Hayden,</i> <span class="citation" data-id="9471173"><a href="/opinion/424798/john-languirand-cross-appellant-v-john-hayden-an-individual-city-of/#227" aria-description="Citation for case: John Languirand, Cross-Appellant v. John Hayden, an...">717 F. 2d 220, 227-228</a></span> (CA5 1983). Two other Courts of Appeals have stopped short of expressly embracing this rule, and have instead only implicitly endorsed it. See, <i>e. g., </i><i>Colburn</i> v. <i>Upper Darby Township,</i> <span class="citation" data-id="8957077"><a href="/opinion/8965741/colburn-v-upper-darby-township/#672" aria-description="Citation for case: Colburn v. Upper Darby Township">838 F. 2d 663, 672-673</a></span> (CA3 1988); <i>Lenard</i> v. <i>Argento,</i> <span class="citation" data-id="414191"><a href="/opinion/414191/bennie-lenard-cross-appellant-v-robert-argento-joseph-sansone-v/#885" aria-description="Citation for case: Bennie Lenard, Cross-Appellant v. Robert Argento &amp; Joseph...">699 F. 2d 874, 885-887</a></span> (CA7 1983).
</p>
<p>In addition, six current Members of this Court have joined opinions in the past that have (at least implicitly) endorsed this theory of liability under § 1983. See <i>Oklahoma City</i> v. <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#829" aria-description="Citation for case: City of Oklahoma v. Tuttle"><i>Tuttle, supra,</i> at 829-831</a></span> (BRENNAN, J., joined by MARSHALL and BLACKMUN, JJ., concurring in part and concurring in judgment); <i>Springfield</i> v. <span class="citation" data-id="9430858"><a href="/opinion/111831/city-of-springfield-v-kibbe/#268" aria-description="Citation for case: City of Springfield v. Kibbe"><i>Kibbe, supra,</i> at 268-270</a></span> (O'CONNOR, J., joined by REHNQUIST, C. J., and Powell and WHITE, JJ., dissenting).</p>
<p>[7]  Some courts have held that a showing of "gross negligence" in a city's failure to train its employees is adequate to make out a claim under § 1983. See, <i>e. g., </i><i>Bergquist</i> v. <span class="citation" data-id="8946582"><a href="/opinion/8955600/bergquist-v-county-of-cochise/#1370" aria-description="Citation for case: Bergquist v. County of Cochise"><i>County of Cochise, supra,</i> at 1370</a></span>; <i>Herrera</i> v. <i>Valentine,</i> <span class="citation" data-id="392242"><a href="/opinion/392242/herrera-v-valentine/#1224" aria-description="Citation for case: Herrera v. Valentine">653 F. 2d 1220, 1224</a></span> (CA8 1981). But the more common rule is that a city must exhibit "deliberate indifference" towards the constitutional rights of persons in its domain before a § 1983 action for "failure to train" is permissible. See, <i>e. g., </i><i>Fiacco</i> v. <i>Rensselaer, supra,</i> at 326; <i>Patzner</i> v. <i>Burkett,</i> <span class="citation" data-id="462512"><a href="/opinion/462512/leland-patzner-v-joyce-burkett-aka-joyce-mclaughlin-deborah-myerchin-and/#1367" aria-description="Citation for case: Leland Patzner v. Joyce Burkett A/K/A Joyce McLaughlin...">779 F. 2d 1363, 1367</a></span> (CA8 1985); <i>Wellington</i> v. <i>Daniels,</i> <span class="citation" data-id="424905"><a href="/opinion/424905/cynthia-wellington-guardian-of-the-estate-of-robert-d-gravelle-v-brian/#936" aria-description="Citation for case: Cynthia Wellington, Guardian of the Estate of Robert D....">717 F. 2d 932, 936</a></span> (CA4 1983); <i>Languirand</i> v. <span class="citation" data-id="9471173"><a href="/opinion/424798/john-languirand-cross-appellant-v-john-hayden-an-individual-city-of/#227" aria-description="Citation for case: John Languirand, Cross-Appellant v. John Hayden, an..."><i>Hayden, supra,</i> at 227</a></span>.</p>
<p>[8]  The "deliberate indifference" standard we adopt for § 1983 "failure to train" claims does not turn upon the degree of fault (if any) that a plaintiff must show to make out an underlying claim of a constitutional violation. For example, this Court has never determined what degree of culpability must be shown before the particular constitutional deprivation asserted in this case  a denial of the due process right to medical care while in detention  is established. Indeed, in <i>Revere</i> v. <i>Massachusetts General Hospital,</i> <span class="citation" data-id="9429305"><a href="/opinion/110998/city-of-revere-v-massachusetts-general-hospital/#243" aria-description="Citation for case: City of Revere v. Massachusetts General Hospital">463 U. S. 239, 243-245</a></span> (1983), we reserved decision on the question whether something less than the Eighth Amendment's "deliberate indifference" test may be applicable in claims by detainees asserting violations of their due process right to medical care while in custody.
</p>
<p>We need not resolve here the question left open in <i><span class="citation" data-id="9429305"><a href="/opinion/110998/city-of-revere-v-massachusetts-general-hospital/" aria-description="Citation for case: City of Revere v. Massachusetts General Hospital">Revere</a></span></i> for two reasons. First, petitioner has conceded that, as the case comes to us, we must assume that respondent's constitutional right to receive medical care was denied by city employees  whatever the nature of that right might be. See Tr. of Oral Arg. 8-9. Second, the proper standard for determining when a municipality will be liable under § 1983 for constitutional wrongs does not turn on any underlying culpability test that determines when such wrongs have occurred. Cf. Brief for Respondent 27.</p>
<p>[9]  The plurality opinion in <i><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/" aria-description="Citation for case: City of Oklahoma v. Tuttle">Tuttle</a></span></i> explained why this must be so:
</p>
<p>"Obviously, if one retreats far enough from a constitutional violation some municipal `policy' can be identified behind almost any . . . harm inflicted by a municipal official; for example, [a police officer] would never have killed Tuttle if Oklahoma City did not have a `policy' of establishing a police force. But <i><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span></i> must be taken to require proof of a city policy different in kind from this latter example before a claim can be sent to a jury on the theory that a particular violation was `caused' by the municipal `policy.' " <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#823" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S., at 823</a></span>. Cf. also <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#833" aria-description="Citation for case: City of Oklahoma v. Tuttle"><i>id.,</i> at 833, n. 9</a></span> (opinion of BRENNAN, J.).</p>
<p>[10]  For example, city policymakers know to a moral certainty that their police officers will be required to arrest fleeing felons. The city has armed its officers with firearms, in part to allow them to accomplish this task. Thus, the need to train officers in the constitutional limitations on the use of deadly force, see <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985), can be said to be "so obvious," that failure to do so could properly be characterized as "deliberate indifference" to constitutional rights.
</p>
<p>It could also be that the police, in exercising their discretion, so often violate constitutional rights that the need for further training must have been plainly obvious to the city policymakers, who, nevertheless, are "deliberately indifferent" to the need.</p>
<p>[11]  The record indicates that city did train its officers and that its training included first-aid instruction. See App. to Pet. for Cert. 4a. Petitioner argues that it could not have been obvious to the city that such training was insufficient to administer the written policy, which was itself constitutional. This is a question to be resolved on remand. See Part IV, <i>infra.</i></p>
<p>[12]  Respondent conceded as much at argument. See Tr. of Oral Arg. 50-51; cf. also <i>Oklahoma City</i> v. <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#831" aria-description="Citation for case: City of Oklahoma v. Tuttle"><i>Tuttle, supra,</i> at 831</a></span> (opinion of BRENNAN, J.).</p>

</div>
```

---

## GROUP: content/cases/City of Indianapolis v. Edmond.md  (`case`, 7 assertions)

### content_page

```
---
title: "City of Indianapolis v. Edmond"
type: case
citation: ""
parallel_cite: "531 U.S. 32; 121 S. Ct. 447; 148 L. Ed. 2d 333; 69 U.S.L.W. 4009; 14 Fla. L. Weekly Fed. S 9; 2000 Colo. J. C.A.R. 6401"
neutral_cite: "2000 U.S. LEXIS 8084; 2000 Cal. Daily Op. Serv. 9549"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2000
date_decided: 2000-11-28
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2000-11-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: City of Indianapolis v. Edmond
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118391/city-of-indianapolis-v-edmond/"
  cluster_id: 118391
  opinion_id: 118391
  identity_checked: true
homes:
  - page: "[[Checkpoints and Roadblocks]]"
    role: "Key — Anchor"
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Related (cross-doctrine)"
  - page: "[[Border Searches]]"
    role: "Related (cross-doctrine)"
related: ["[[Illinois v. Lidster]]", "[[Delaware v. Prouse]]", "[[Ferguson v. City of Charleston]]"]
aliases: ["Indianapolis v. Edmond"]
tags: ["case", "fourth-amendment", "checkpoint", "roadblock", "special-needs", "programmatic-purpose"]
holding: "A checkpoint program whose primary purpose is to detect ordinary criminal wrongdoing / general crime control (here, drug interdiction)…"
lake:
  record_id: City of Indianapolis v. Edmond
  status: verified
  projected_at: 2026-07-06
---

# City of Indianapolis v. Edmond

*531 U.S. 32 (2000)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Indianapolis operated vehicle checkpoints at which officers stopped a set number of cars, checked the driver's license and registration, looked for signs of impairment, and walked a drug-detection dog around each vehicle. The city conceded the program's purpose was to interdict narcotics. Motorists stopped at the checkpoints sued, challenging the program under the Fourth Amendment.

## Issue
Whether a vehicle checkpoint program whose primary purpose is the general interest in crime control (narcotics interdiction) is consistent with the Fourth Amendment.

## Rule
No. Suspicionless checkpoint seizures are measured by their programmatic purpose, and ordinary crime control will not justify them: "We have never approved a checkpoint program whose primary purpose was to detect evidence of ordinary criminal wrongdoing." — 531 U.S. 32, 41. ^pin-41

"Because the primary purpose of the Indianapolis narcotics checkpoint program is to uncover evidence of ordinary criminal wrongdoing, the program contravenes the Fourth Amendment." — *Id.* at 42. ^pin-42

## Application
Indianapolis's checkpoints were aimed primarily at detecting and interdicting unlawful drugs — a general crime-control end, not the border-policing or roadway-safety interests that had justified prior checkpoints. Because that primary purpose was indistinguishable from the general interest in crime control, the suspicionless stops were unreasonable on these facts.

## Conclusion
The narcotics checkpoint program violated the Fourth Amendment; the injunction against it was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Edmond*'s primary-purpose test was distinguished in [[Illinois v. Lidster]] (information-seeking checkpoint about a crime committed by someone else) and applied to invalidate law-enforcement-purpose programs in [[Ferguson v. City of Charleston]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *City of Indianapolis v. Edmond*, 531 U.S. 32 (2000) — https://www.courtlistener.com/opinion/118391/city-of-indianapolis-v-edmond/ — pinpoints: 41, 42.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2f5226f181827020", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2000 U.S. LEXIS 8084; 2000 Cal. Daily Op. Serv. 9549", "official_citation_present": false, "parallel_cite": "531 U.S. 32; 121 S. Ct. 447; 148 L. Ed. 2d 333; 69 U.S.L.W. 4009; 14 Fla. L. Weekly Fed. S 9; 2000 Colo. J. C.A.R. 6401", "title": "City of Indianapolis v. Edmond", "year": "2000"}}
{"assertion_id": "365c1baddfd4e80a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A checkpoint program whose primary purpose is to detect ordinary criminal wrongdoing / general crime control (here, drug interdiction)…", "title": "City of Indianapolis v. Edmond"}}
{"assertion_id": "a22c5a8bf7b13b6d", "dimension": "support", "kind": "home_role", "locator": {"home": "Checkpoints and Roadblocks"}, "payload": {"home": "Checkpoints and Roadblocks", "role": "Key — Anchor", "title": "City of Indianapolis v. Edmond"}}
{"assertion_id": "ccf36202a753bbff", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Related (cross-doctrine)", "title": "City of Indianapolis v. Edmond"}}
{"assertion_id": "cf56193b9958f51b", "dimension": "support", "kind": "home_role", "locator": {"home": "Border Searches"}, "payload": {"home": "Border Searches", "role": "Related (cross-doctrine)", "title": "City of Indianapolis v. Edmond"}}
{"assertion_id": "176a248a8f110dff", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2000-11-28", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "City of Indianapolis v. Edmond", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "City of Indianapolis v. Edmond", "varies_by_point": "false"}}
{"assertion_id": "56d38c3d61b8b50b", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "City of Indianapolis v. Edmond"}}
```

### lake record — City of Indianapolis v. Edmond

```json
{
  "schema_version": "s2.v1",
  "record_id": "City of Indianapolis v. Edmond",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "City of Indianapolis v. Edmond",
    "case_name_short": "Edmond",
    "case_name_full": "CITY OF INDIANAPOLIS Et Al. v. EDMOND Et Al.",
    "input_case_name": "City of Indianapolis v. Edmond",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2000-11-28",
    "year": 2000,
    "docket": null,
    "cluster_id": 118391,
    "lead_opinion_id": 118391,
    "sibling_ids": [
      118391,
      9434014,
      9434015,
      9434016
    ],
    "absolute_url": "/opinion/118391/city-of-indianapolis-v-edmond/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9194630,
        "score": 20,
        "case_name": "City of Indianapolis v. Edmond"
      },
      {
        "cluster_id": 9194629,
        "score": 20,
        "case_name": "City of Indianapolis v. Edmond"
      },
      {
        "cluster_id": 9266095,
        "score": 20,
        "case_name": "City of Indianapolis v. Edmond"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "531 U.S. 32",
        "volume": "531",
        "reporter": "U.S.",
        "page": "32",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 S. Ct. 447",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "447",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "148 L. Ed. 2d 333",
        "volume": "148",
        "reporter": "L. Ed. 2d",
        "page": "333",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 U.S.L.W. 4009",
        "volume": "69",
        "reporter": "U.S.L.W.",
        "page": "4009",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "14 Fla. L. Weekly Fed. S 9",
        "volume": "14",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "9",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 Colo. J. C.A.R. 6401",
        "volume": "2000",
        "reporter": "Colo. J. C.A.R.",
        "page": "6401",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2000 U.S. LEXIS 8084",
        "volume": "2000",
        "reporter": "U.S. LEXIS",
        "page": "8084",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 Cal. Daily Op. Serv. 9549",
        "volume": "2000",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "9549",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "531 U.S. 32",
        "volume": "531",
        "reporter": "U.S.",
        "page": "32",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 S. Ct. 447",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "447",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "148 L. Ed. 2d 333",
        "volume": "148",
        "reporter": "L. Ed. 2d",
        "page": "333",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 U.S. LEXIS 8084",
        "volume": "2000",
        "reporter": "U.S. LEXIS",
        "page": "8084",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 U.S.L.W. 4009",
        "volume": "69",
        "reporter": "U.S.L.W.",
        "page": "4009",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "14 Fla. L. Weekly Fed. S 9",
        "volume": "14",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "9",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 Colo. J. C.A.R. 6401",
        "volume": "2000",
        "reporter": "Colo. J. C.A.R.",
        "page": "6401",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 Cal. Daily Op. Serv. 9549",
        "volume": "2000",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "9549",
        "type": 6,
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
      "id": "pin-41",
      "page": null,
      "quote": "--- # City of Indianapolis v. Edmond *531 U.S. 32 (2000)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Indianapolis operated vehicle checkpoints at which officers stopped a set number of cars, checked the driver's license and registration, looked for signs of impairment, and walked a drug-detection dog around each vehicle. The city conceded the program's purpose was to interdict narcotics. Motorists stopped at the checkpoints sued, challenging the program under the Fourth Amendment. ## Issue Whether a vehicle checkpoint program whose primary purpose is the general interest in crime control (narcotics interdiction) is consistent with the Fourth Amendment. ## Rule No. Suspicionless checkpoint seizures are measured by their programmatic purpose, and ordinary crime control will not justify them:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-42",
      "page": null,
      "quote": "Because the primary purpose of the Indianapolis narcotics checkpoint program is to uncover evidence of ordinary criminal wrongdoing, the program contravenes the Fourth Amendment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2000-11-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "City of Indianapolis v. Edmond",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Nicholson",
          "cluster_id": 4505529,
          "cite": [
            "813 S.E.2d 840",
            "371 N.C. 284"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gigliotti",
          "cluster_id": 7316853,
          "cite": [
            "145 F. Supp. 3d 203",
            "2015 WL 6830675"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jonathan Thomas",
          "cluster_id": 1036878,
          "cite": [
            "726 F.3d 1086",
            "2013 U.S. App. LEXIS 16413",
            "2013 WL 4017239"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. King",
          "cluster_id": 8441539,
          "cite": [
            "736 F.3d 805",
            "2013 WL 4516751"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Marcel King",
          "cluster_id": 854814,
          "cite": [
            "711 F.3d 986",
            "2013 WL 886161",
            "2013 U.S. App. LEXIS 4730"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Daniel Bohman",
          "cluster_id": 803265,
          "cite": [
            "683 F.3d 861",
            "2012 WL 2432595",
            "2012 U.S. App. LEXIS 13195"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane1_negative"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brigham City v. Stuart",
          "cluster_id": 145654,
          "cite": [
            "164 L. Ed. 2d 650",
            "126 S. Ct. 1943",
            "547 U.S. 398",
            "2006 U.S. LEXIS 4155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Knights",
          "cluster_id": 118468,
          "cite": [
            "151 L. Ed. 2d 497",
            "122 S. Ct. 587",
            "534 U.S. 112",
            "2001 U.S. LEXIS 10950"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Samson v. California",
          "cluster_id": 145640,
          "cite": [
            "165 L. Ed. 2d 250",
            "126 S. Ct. 2193",
            "547 U.S. 843",
            "2006 U.S. LEXIS 4885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Lidster",
          "cluster_id": 131154,
          "cite": [
            "157 L. Ed. 2d 843",
            "124 S. Ct. 885",
            "540 U.S. 419",
            "2004 U.S. LEXIS 656"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Club Retro, L.L.C. v. Hilton",
          "cluster_id": 1459439,
          "cite": [
            "568 F.3d 181",
            "2009 U.S. App. LEXIS 9864",
            "2006 WL 6245546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Utah v. Strieff",
          "cluster_id": 3214882,
          "cite": [
            "579 U.S. 232",
            "195 L. Ed. 2d 400",
            "2016 U.S. LEXIS 3926"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carmichael v. Village of Palatine, Ill.",
          "cluster_id": 146911,
          "cite": [
            "605 F.3d 451",
            "2010 U.S. App. LEXIS 10378",
            "2010 WL 2011509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McIntosh",
          "cluster_id": 2058958,
          "cite": [
            "755 N.E.2d 329",
            "96 N.Y.2d 521",
            "730 N.Y.S.2d 265",
            "2001 N.Y. LEXIS 1978"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dickerson Ex Rel. Davison v. Napolitano",
          "cluster_id": 146453,
          "cite": [
            "604 F.3d 732",
            "2010 U.S. App. LEXIS 9887",
            "2010 WL 1931683"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heller v. District of Columbia",
          "cluster_id": 614652,
          "cite": [
            "670 F.3d 1244",
            "399 U.S. App. D.C. 314",
            "2011 U.S. App. LEXIS 20130",
            "2011 WL 4551558"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Caballes",
          "cluster_id": 2192166,
          "cite": [
            "851 N.E.2d 26",
            "221 Ill. 2d 282",
            "303 Ill. Dec. 128",
            "2006 Ill. LEXIS 625"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crowe v. County of San Diego",
          "cluster_id": 148932,
          "cite": [
            "608 F.3d 406",
            "2010 U.S. App. LEXIS 12917",
            "2010 WL 2431842"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kimler",
          "cluster_id": 163635,
          "cite": [
            "335 F.3d 1132",
            "2003 WL 21519916"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hicks",
          "cluster_id": 1060443,
          "cite": [
            "55 S.W.3d 515",
            "2001 Tenn. LEXIS 658",
            "2001 WL 1035172"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of L. A. v. Patel",
          "cluster_id": 2811846,
          "cite": [
            "576 U.S. 409",
            "135 S. Ct. 2443",
            "192 L. Ed. 2d 435",
            "2015 U.S. LEXIS 4065",
            "83 U.S.L.W. 4520",
            "25 Fla. L. Weekly Fed. S 412"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
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
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jacoby, T., Aplt.",
          "cluster_id": 4429713,
          "cite": [
            "170 A.3d 1065"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Indianapolis v. Edmond:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118391 OR 9434014 OR 9434015 OR 9434016) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzEyNDE2MDAwMDAwJnM9Mjk5MTY0NCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118391+OR+9434014+OR+9434015+OR+9434016%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 14,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 15,
        "triage_snippet_classified": 185
      },
      "lane2_top_cited": {
        "query": "cites:(118391 OR 9434014 OR 9434015 OR 9434016)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTImcz0yNjEmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118391+OR+9434014+OR+9434015+OR+9434016%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118391 OR 9434014 OR 9434015 OR 9434016)",
        "reviewed": 28,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 28,
        "triage_read": 0,
        "triage_snippet_classified": 28
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118391 OR 9434014 OR 9434015 OR 9434016)",
    "indexed_citing_opinions": 745,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118391,
        "count": 644,
        "count_source": "search"
      },
      {
        "opinion_id": 9434014,
        "count": 125,
        "count_source": "search"
      },
      {
        "opinion_id": 9434015,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434016,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1207,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/city-of-indianapolis-v-edmond.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MTAwNTkmcz0xMDAxNTMwMSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118391+OR+9434014+OR+9434015+OR+9434016%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118391,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 111600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 111788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 111927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 112220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 112412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 112459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 118100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 118354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 156261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 517399,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 552811,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 765145,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118391,
        "cited_id": 2311329,
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
    "date_created": "2026-07-05T00:17:27Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:17:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:17:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:21:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:17:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — City of Indianapolis v. Edmond

```
<div>
<center><b><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U.S. 32</a></span> (2000)</b></center>
<center><h1>CITY OF INDIANAPOLIS et al.<br>
v.<br>
EDMOND et al.</h1></center>
<center>No. 99-1030.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued October 3, 2000.</center>
<center>Decided November 28, 2000.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SEVENTH CIRCUIT
<p><span class="star-pagination">*33</span> O'Connor, J., delivered the opinion of the Court, in which Stevens, Kennedy, Souter, Ginsburg, and Breyer, JJ., joined. Rehnquist, C. J., filed a dissenting opinion, in which Thomas, J., joined, and in which Scalia, J., joined as to Part I, <i>post,</i> p. 48. Thomas, J., filed a dissenting opinion, <i>post,</i> p. 56.</p>
<p><i>A. Scott Chinn</i> argued the cause for petitioners. With him on the briefs were <i>Anthony W. Overholt, Matthew R. Gutwein,</i> and <i>Thomas M. Fisher.</i> </p>
<p><i>Patricia A. Millett</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With her on the brief were <i>Solicitor General Waxman, Assistant Attorney General Robinson,</i> and <i>Deputy Solicitor General Dreeben.</i> </p>
<p><span class="star-pagination">*34</span> <i>Kenneth J. Falk</i> argued the cause for respondents. With him on the brief were <i>Jacquelyn E. Bowie, Sean C. Lemieux,</i>  and <i>Steven R. Shapiro.</i><sup>[*]</sup></p>
<p>Justice O'Connor, delivered the opinion of the Court.</p>
<p>In <i>Michigan Dept. of State Police</i> v. <i>Sitz,</i> <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S. 444</a></span> (1990), and <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976), we held that brief, suspicionless seizures at highway checkpoints for the purposes of combating drunk driving and intercepting illegal immigrants were constitutional. We now consider the constitutionality of a highway checkpoint program whose primary purpose is the discovery and interdiction of illegal narcotics.</p>
<p></p>
<h2>I</h2>
<p>In August 1998, the city of Indianapolis began to operate vehicle checkpoints on Indianapolis roads in an effort to interdict unlawful drugs. The city conducted six such roadblocks between August and November that year, stopping <span class="star-pagination">*35</span> 1,161 vehicles and arresting 104 motorists. Fifty-five arrests were for drug-related crimes, while 49 were for offenses unrelated to drugs. <i>Edmond</i> v. <i>Goldsmith,</i> <span class="citation" data-id="6983057"><a href="/opinion/7078145/edmond-v-goldsmith/#661" aria-description="Citation for case: Edmond v. Goldsmith">183 F. 3d 659, 661</a></span> (CA7 1999). The overall "hit rate" of the program was thus approximately nine percent.</p>
<p>The parties stipulated to the facts concerning the operation of the checkpoints by the Indianapolis Police Department (IPD) for purposes of the preliminary injunction proceedings instituted below. At each checkpoint location, the police stop a predetermined number of vehicles. Approximately 30 officers are stationed at the checkpoint. Pursuant to written directives issued by the chief of police, at least one officer approaches the vehicle, advises the driver that he or she is being stopped briefly at a drug checkpoint, and asks the driver to produce a license and registration. The officer also looks for signs of impairment and conducts an open-view examination of the vehicle from the outside. A narcoticsdetection dog walks around the outside of each stopped vehicle.</p>
<p>The directives instruct the officers that they may conduct a search only by consent or based on the appropriate quantum of particularized suspicion. The officers must conduct each stop in the same manner until particularized suspicion develops, and the officers have no discretion to stop any vehicle out of sequence. The city agreed in the stipulation to operate the checkpoints in such a way as to ensure that the total duration of each stop, absent reasonable suspicion or probable cause, would be five minutes or less.</p>
<p>The affidavit of Indianapolis Police Sergeant Marshall DePew, although it is technically outside the parties' stipulation, provides further insight concerning the operation of the checkpoints. According to Sergeant DePew, checkpoint locations are selected weeks in advance based on such considerations as area crime statistics and traffic flow. The checkpoints are generally operated during daylight hours and are identified with lighted signs reading, "`NARCOTICS <span class="star-pagination">*36</span> CHECKPOINT MILE AHEAD, NARCOTICS K-9 IN USE, BE PREPARED TO STOP.'" App. to Pet. for Cert. 57a. Once a group of cars has been stopped, other traffic proceeds without interruption until all the stopped cars have been processed or diverted for further processing. Sergeant DePew also stated that the average stop for a vehicle not subject to further processing lasts two to three minutes or less.</p>
<p>Respondents James Edmond and Joell Palmer were each stopped at a narcotics checkpoint in late September 1998. Respondents then filed a lawsuit on behalf of themselves and the class of all motorists who had been stopped or were subject to being stopped in the future at the Indianapolis drug checkpoints. Respondents claimed that the roadblocks violated the Fourth Amendment of the United States Constitution and the search and seizure provision of the Indiana Constitution. Respondents requested declaratory and injunctive relief for the class, as well as damages and attorney's fees for themselves.</p>
<p>Respondents then moved for a preliminary injunction. Although respondents alleged that the officers who stopped them did not follow the written directives, they agreed to the stipulation concerning the operation of the checkpoints for purposes of the preliminary injunction proceedings. The parties also stipulated to certification of the plaintiff class. The United States District Court for the Southern District of Indiana agreed to class certification and denied the motion for a preliminary injunction, holding that the checkpoint program did not violate the Fourth Amendment. <i>Edmond</i>  v. <i>Goldsmith,</i> <span class="citation" data-id="2311329"><a href="/opinion/2311329/edmond-v-goldsmith/" aria-description="Citation for case: Edmond v. Goldsmith">38 F. Supp. 2d 1016</a></span> (1998). A divided panel of the United States Court of Appeals for the Seventh Circuit reversed, holding that the checkpoints contravened the Fourth Amendment. <span class="citation multiple-matches"><a href="/c/F.%203d/183/659/">183 F. 3d 659</a></span> (1999). The panel denied rehearing. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./528/1153/">528 U. S. 1153</a></span> (2000), and now affirm.</p>
<p></p>
<h2>
<span class="star-pagination">*37</span> II</h2>
<p>The Fourth Amendment requires that searches and seizures be reasonable. A search or seizure is ordinarily unreasonable in the absence of individualized suspicion of wrongdoing. <i>Chandler</i> v. <i>Miller,</i> <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#308" aria-description="Citation for case: Chandler v. Miller">520 U. S. 305, 308</a></span> (1997). While such suspicion is not an "irreducible" component of reasonableness, <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#561" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 561</a></span>, we have recognized only limited circumstances in which the usual rule does not apply. For example, we have upheld certain regimes of suspicion less searches where the program was designed to serve "special needs, beyond the normal need for law enforcement." See, <i>e. g., </i><i>Vernonia School Dist. 47J</i> v. <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646</a></span> (1995) (random drug testing of studentathletes); <i>Treasury Employees</i> v. <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656</a></span> (1989) (drug tests for United States Customs Service employees seeking transfer or promotion to certain positions); <i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602</a></span> (1989) (drug and alcohol tests for railway employees involved in train accidents or found to be in violation of particular safety regulations). We have also allowed searches for certain administrative purposes without particularized suspicion of misconduct, provided that those searches are appropriately limited. See, <i>e. g., </i><i>New York</i> v. <i>Burger,</i> <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#702" aria-description="Citation for case: New York v. Burger">482 U. S. 691, 702-704</a></span> (1987) (warrantless administrative inspection of premises of "closely regulated" business); <i>Michigan</i> v. <i>Tyler,</i>  <span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#507" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499, 507-509, 511-512</a></span> (1978) (administrative inspection of fire-damaged premises to determine cause of blaze); <i>Camara</i> v. <i>Municipal Court of City and County of San Francisco,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 534-539</a></span> (1967) (administrative inspection to ensure compliance with city housing code).</p>
<p>We have also upheld brief, suspicion less seizures of motorists at a fixed Border Patrol checkpoint designed to intercept illegal aliens, <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte, supra,</a></span></i> and at a sobriety checkpoint aimed at removing drunk drivers from the road, <i>Michigan Dept. of State Police</i> v. <i>Sitz,</i> <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S. 444</a></span> (1990). In addition, in <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 663</a></span> (1979), <span class="star-pagination">*38</span> we suggested that a similar type of roadblock with the purpose of verifying drivers' licenses and vehicle registrations would be permissible. In none of these cases, however, did we indicate approval of a checkpoint program whose primary purpose was to detect evidence of ordinary criminal wrongdoing.</p>
<p>In <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>,</i> we entertained Fourth Amendment challenges to stops at two permanent immigration checkpoints located on major United States highways less than 100 miles from the Mexican border. We noted at the outset the particular context in which the constitutional question arose, describing in some detail the "formidable law enforcement problems" posed by the northbound tide of illegal entrants into the United States. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#551" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 551-554</a></span>. These problems had also been the focus of several earlier cases addressing the constitutionality of other Border Patrol traffic-checking operations. See <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891</a></span> (1975); <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975); <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973). In <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>,</i> we found that the balance tipped in favor of the Government's interests in policing the Nation's borders. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#561" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 561-564</a></span>. In so finding, we emphasized the difficulty of effectively containing illegal immigration at the border itself. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Id.,</i> at 556</a></span>. We also stressed the impracticality of the particularized study of a given car to discern whether it was transporting illegal aliens, as well as the relatively modest degree of intrusion entailed by the stops. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Id.,</i> at 556-564</a></span>.</p>
<p>Our subsequent cases have confirmed that considerations specifically related to the need to police the border were a significant factor in our <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> decision. For example, in <i>United States</i> v. <i>Montoya de Hernandez,</i> <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#538" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U. S. 531, 538</a></span> (1985), we counted <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> as one of a number of Fourth Amendment cases that "reflect longstanding concern for the protection of the integrity of the border." Although the stops in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> did not occur at the <span class="star-pagination">*39</span> border itself, the checkpoints were located near the border and served a border control function made necessary by the difficulty of guarding the border's entire length. See <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Martinez-Fuerte, supra,</i> at 556</a></span>.</p>
<p>In <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span>,</i> we evaluated the constitutionality of a Michigan highway sobriety checkpoint program. The <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> checkpoint involved brief, suspicion less stops of motorists so that police officers could detect signs of intoxication and remove impaired drivers from the road. <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#447" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S., at 447-448</a></span>. Motorists who exhibited signs of intoxication were diverted for a license and registration check and, if warranted, further sobriety tests. <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#447" aria-description="Citation for case: Michigan Department of State Police v. Sitz"><i>Id.,</i> at 447</a></span>. This checkpoint program was clearly aimed at reducing the immediate hazard posed by the presence of drunk drivers on the highways, and there was an obvious connection between the imperative of highway safety and the law enforcement practice at issue. The gravity of the drunk driving problem and the magnitude of the State's interest in getting drunk drivers off the road weighed heavily in our determination that the program was constitutional. See <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#451" aria-description="Citation for case: Michigan Department of State Police v. Sitz"><i>id.,</i> at 451</a></span>.</p>
<p>In <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span>,</i> we invalidated a discretionary, suspicion less stop for a spot check of a motorist's driver's license and vehicle registration. The officer's conduct in that case was unconstitutional primarily on account of his exercise of "standardless and unconstrained discretion." <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#661" aria-description="Citation for case: Delaware v. Prouse">440 U. S., at 661</a></span>. We nonetheless acknowledged the States' "vital interest in ensuring that only those qualified to do so are permitted to operate motor vehicles, that these vehicles are fit for safe operation, and hence that licensing, registration, and vehicle inspection requirements are being observed." <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#658" aria-description="Citation for case: Delaware v. Prouse"><i>Id.,</i> at 658</a></span>. Accordingly, we suggested that "[q]uestioning of all oncoming traffic at roadblock-type stops" would be a lawful means of serving this interest in highway safety. <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse"><i>Id.,</i> at 663</a></span>.</p>
<p>We further indicated in <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span></i> that we considered the purposes of such a hypothetical roadblock to be distinct from a general purpose of investigating crime. The State proffered <span class="star-pagination">*40</span> the additional interests of "the apprehension of stolen motor vehicles and of drivers under the influence of alcohol or narcotics" in its effort to justify the discretionary spot check. <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#659" aria-description="Citation for case: Delaware v. Prouse"><i>Id.,</i> at 659, n. 18</a></span>. We attributed the entirety of the latter interest to the State's interest in roadway safety. <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Ibid.</a></span></i> We also noted that the interest in apprehending stolen vehicles may be partly subsumed by the interest in roadway safety. <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Ibid.</a></span></i> We observed, however, that "[t]he remaining governmental interest in controlling automobile thefts is not distinguishable from the general interest in crime control." <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Ibid.</a></span></i> Not only does the common thread of highway safety thus run through <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> and <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span>,</i> but <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span></i> itself reveals a difference in the Fourth Amendment significance of highway safety interests and the general interest in crime control.</p>
<p></p>
<h2>III</h2>
<p>It is well established that a vehicle stop at a highway checkpoint effectuates a seizure within the meaning of the Fourth Amendment. See, <i>e. g., </i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#450" aria-description="Citation for case: Michigan Department of State Police v. Sitz"><i>Sitz, supra,</i> at 450</a></span>. The fact that officers walk a narcotics-detection dog around the exterior of each car at the Indianapolis checkpoints does not transform the seizure into a search. See <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place">462 U. S. 696, 707</a></span> (1983). Just as in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> an exterior sniff of an automobile does not require entry into the car and is not designed to disclose any information other than the presence or absence of narcotics. See <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">ibid.</a></span></i> Like the dog sniff in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> a sniff by a dog that simply walks around a car is "much less intrusive than a typical search." <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Ibid.</a></span></i>  Cf. <i>United States</i> v. <i>Turpin,</i> <span class="citation" data-id="552811"><a href="/opinion/552811/united-states-v-maggie-louise-turpin-united-states-of-america-v-darryl/#1385" aria-description="Citation for case: United States v. Maggie Louise Turpin, United States of...">920 F. 2d 1377, 1385</a></span> (CA8 1990). Rather, what principally distinguishes these checkpoints from those we have previously approved is their primary purpose.</p>
<p>As petitioners concede, the Indianapolis checkpoint program unquestionably has the primary purpose of interdicting illegal narcotics. In their stipulation of facts, the parties repeatedly refer to the checkpoints as "drug checkpoints" and <span class="star-pagination">*41</span> describe them as "being operated by the City of Indianapolis in an effort to interdict unlawful drugs in Indianapolis." App. to Pet. for Cert. 51a52a. In addition, the first document attached to the parties' stipulation is entitled "DRUG CHECKPOINT CONTACT OFFICER DIRECTIVES BY ORDER OF THE CHIEF OF POLICE." <i><span class="citation" data-id="552811"><a href="/opinion/552811/united-states-v-maggie-louise-turpin-united-states-of-america-v-darryl/" aria-description="Citation for case: United States v. Maggie Louise Turpin, United States of...">Id.,</a></span></i> at 53a. These directives instruct officers to "[a]dvise the citizen that they are being stopped briefly at a drug checkpoint." <i><span class="citation" data-id="552811"><a href="/opinion/552811/united-states-v-maggie-louise-turpin-united-states-of-america-v-darryl/" aria-description="Citation for case: United States v. Maggie Louise Turpin, United States of...">Ibid.</a></span></i>  The second document attached to the stipulation is entitled "1998 Drug Road Blocks" and contains a statistical breakdown of information relating to the checkpoints conducted. <i><span class="citation" data-id="552811"><a href="/opinion/552811/united-states-v-maggie-louise-turpin-united-states-of-america-v-darryl/" aria-description="Citation for case: United States v. Maggie Louise Turpin, United States of...">Id.,</a></span></i> at 55a. Further, according to Sergeant DePew, the checkpoints are identified with lighted signs reading, "`NARCOTICS CHECKPOINT MILE AHEAD, NARCOTICS K-9 IN USE, BE PREPARED TO STOP.' " <i><span class="citation" data-id="552811"><a href="/opinion/552811/united-states-v-maggie-louise-turpin-united-states-of-america-v-darryl/" aria-description="Citation for case: United States v. Maggie Louise Turpin, United States of...">Id.,</a></span></i> at 57a. Finally, both the District Court and the Court of Appeals recognized that the primary purpose of the roadblocks is the interdiction of narcotics. <span class="citation" data-id="2311329"><a href="/opinion/2311329/edmond-v-goldsmith/#1026" aria-description="Citation for case: Edmond v. Goldsmith">38 F. Supp. 2d, at 1026</a></span> (noting that both parties "stress the primary purpose of the roadblocks as the interdiction of narcotics" and that "[t]he IPD has made it clear that the purpose for its checkpoints is to interdict narcotics traffic"); <span class="citation" data-id="6983057"><a href="/opinion/7078145/edmond-v-goldsmith/#665" aria-description="Citation for case: Edmond v. Goldsmith">183 F. 3d, at 665</a></span> (observing that "the City concedes that its proximate goal is to catch drug offenders").</p>
<p>We have never approved a checkpoint program whose primary purpose was to detect evidence of ordinary criminal wrongdoing. Rather, our checkpoint cases have recognized only limited exceptions to the general rule that a seizure must be accompanied by some measure of individualized suspicion. We suggested in <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span></i> that we would not credit the "general interest in crime control" as justification for a regime of suspicionless stops. <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#659" aria-description="Citation for case: Delaware v. Prouse">440 U. S., at 659, n. 18</a></span>. Consistent with this suggestion, each of the checkpoint programs that we have approved was designed primarily to serve purposes closely related to the problems of policing the border or the necessity of ensuring roadway safety. Because the <span class="star-pagination">*42</span> primary purpose of the Indianapolis narcotics checkpoint program is to uncover evidence of ordinary criminal wrongdoing, the program contravenes the Fourth Amendment.</p>
<p>Petitioners propose several ways in which the narcoticsdetection purpose of the instant checkpoint program may instead resemble the primary purposes of the checkpoints in <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> and <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>.</i> Petitioners state that the checkpoints in those cases had the same ultimate purpose of arresting those suspected of committing crimes. Brief for Petitioners 22. Securing the border and apprehending drunk drivers are, of course, law enforcement activities, and law enforcement officers employ arrests and criminal prosecutions in pursuit of these goals. See <i>Sitz,</i> <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#447" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S., at 447, 450</a></span>; <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#545" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 545-550</a></span>. If we were to rest the case at this high level of generality, there would be little check on the ability of the authorities to construct roadblocks for almost any conceivable law enforcement purpose. Without drawing the line at roadblocks designed primarily to serve the general interest in crime control, the Fourth Amendment would do little to prevent such intrusions from becoming a routine part of American life.</p>
<p>Petitioners also emphasize the severe and intractable nature of the drug problem as justification for the checkpoint program. Brief for Petitioners 14-17, 31. There is no doubt that traffic in illegal narcotics creates social harms of the first magnitude. Cf. <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#668" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 668</a></span>. The law enforcement problems that the drug trade creates likewise remain daunting and complex, particularly in light of the myriad forms of spin-off crime that it spawns. Cf. <i>Montoya de Hernandez,</i> <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#538" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U. S., at 538</a></span>. The same can be said of various other illegal activities, if only to a lesser degree. But the gravity of the threat alone cannot be dispositive of questions concerning what means law enforcement officers may employ to pursue a given purpose. Rather, in determining whether individualized suspicion is required, we must consider the nature of the interests threatened and their connection <span class="star-pagination">*43</span> to the particular law enforcement practices at issue. We are particularly reluctant to recognize exceptions to the general rule of individualized suspicion where governmental authorities primarily pursue their general crime control ends.</p>
<p>Nor can the narcotics-interdiction purpose of the checkpoints be rationalized in terms of a highway safety concern similar to that present in <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span>.</i> The detection and punishment of almost any criminal offense serves broadly the safety of the community, and our streets would no doubt be safer but for the scourge of illegal drugs. Only with respect to a smaller class of offenses, however, is society confronted with the type of immediate, vehicle-bound threat to life and limb that the sobriety checkpoint in <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> was designed to eliminate.</p>
<p>Petitioners also liken the anticontraband agenda of the Indianapolis checkpoints to the antismuggling purpose of the checkpoints in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>.</i> Brief for Petitioners 15 16. Petitioners cite this Court's conclusion in <i>MartinezFuerte</i> that the flow of traffic was too heavy to permit "particularized study of a given car that would enable it to be identified as a possible carrier of illegal aliens," <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#557" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 557</a></span>, and claim that this logic has even more force here. The problem with this argument is that the same logic prevails any time a vehicle is employed to conceal contraband or other evidence of a crime. This type of connection to the roadway is very different from the close connection to roadway safety that was present in <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> and <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span>.</i> Further, the Indianapolis checkpoints are far removed from the border context that was crucial in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>.</i> While the difficulty of examining each passing car was an important factor in validating the law enforcement technique employed in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>,</i> this factor alone cannot justify a regime of suspicionless searches or seizures. Rather, we must look more closely at the nature of the public interests that such a regime is designed principally to serve.</p>
<p><span class="star-pagination">*44</span> The primary purpose of the Indianapolis narcotics checkpoints is in the end to advance "the general interest in crime control," <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#659" aria-description="Citation for case: Delaware v. Prouse">440 U. S., at 659, n. 18</a></span>. We decline to suspend the usual requirement of individualized suspicion where the police seek to employ a checkpoint primarily for the ordinary enterprise of investigating crimes. We cannot sanction stops justified only by the generalized and everpresent possibility that interrogation and inspection may reveal that any given motorist has committed some crime.</p>
<p>Of course, there are circumstances that may justify a law enforcement checkpoint where the primary purpose would otherwise, but for some emergency, relate to ordinary crime control. For example, as the Court of Appeals noted, the Fourth Amendment would almost certainly permit an appropriately tailored roadblock set up to thwart an imminent terrorist attack or to catch a dangerous criminal who is likely to flee by way of a particular route. See 183 F. 3d, at 662 663. The exigencies created by these scenarios are far removed from the circumstances under which authorities might simply stop cars as a matter of course to see if there just happens to be a felon leaving the jurisdiction. While we do not limit the purposes that may justify a checkpoint program to any rigid set of categories, we decline to approve a program whose primary purpose is ultimately indistinguishable from the general interest in crime control.<sup>[1]</sup></p>
<p><span class="star-pagination">*45</span> Petitioners argue that our prior cases preclude an inquiry into the purposes of the checkpoint program. For example, they cite <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U. S. 806</a></span> (1996), and <i>Bond</i> v. <i>United States,</i> <span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">529 U. S. 334</a></span> (2000), to support the proposition that "where the government articulates and pursues a legitimate interest for a suspicionless stop, courts should not look behind that interest to determine whether the government's `primary purpose' is valid." Brief for Petitioners 34; see also <i>id.,</i> at 9. These cases, however, do not control the instant situation.</p>
<p>In <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span>,</i> we held that an individual officer's subjective intentions are irrelevant to the Fourth Amendment validity of a traffic stop that is justified objectively by probable cause to believe that a traffic violation has occurred. <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#810" aria-description="Citation for case: Whren v. United States">517 U. S., at 810-813</a></span>. We observed that our prior cases "foreclose any argument that the constitutional reasonableness of traffic stops depends on the actual motivations of the individual officers involved." <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#813" aria-description="Citation for case: Whren v. United States"><i>Id.,</i> at 813</a></span>. In so holding, we expressly distinguished cases where we had addressed the validity of searches conducted in the absence of probable cause. See <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#811" aria-description="Citation for case: Whren v. United States"><i>id.,</i> at 811-812</a></span> (distinguishing <i>Florida</i> v. <i>Wells,</i> <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/#4" aria-description="Citation for case: Florida v. Wells">495 U. S. 1, 4</a></span> (1990) (stating that "an inventory search must not be a ruse for a general rummaging in order to discover incriminating evidence"), <i>Colorado</i> v. <i>Bertine,</i> <span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/#372" aria-description="Citation for case: Colorado v. Bertine">479 U. S. 367, 372</a></span> (1987) (suggesting that the absence of bad faith and the lack of a purely investigative purpose were relevant to the validity of an inventory search), and <i>Burger,</i> <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#716" aria-description="Citation for case: New York v. Burger">482 U. S., at 716-717, n. 27</a></span> (observing that a valid administrative inspection conducted with neither a warrant nor probable cause did not appear to be a pretext for gathering evidence of violations of the penal laws)).</p>
<p><i>Whren</i> therefore reinforces the principle that, while "[s]ubjective intentions play no role in ordinary, probablecause Fourth Amendment analysis," <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#813" aria-description="Citation for case: Whren v. United States">517 U. S., at 813</a></span>, programmatic purposes may be relevant to the validity of Fourth Amendment intrusions undertaken pursuant to a <span class="star-pagination">*46</span> general scheme without individualized suspicion. Accordingly, <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span></i> does not preclude an inquiry into programmatic purpose in such contexts. Cf. <i>Chandler</i> v. <i>Miller,</i> <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/" aria-description="Citation for case: Chandler v. Miller">520 U. S. 305</a></span> (1997); <i>Treasury Employees</i> v. <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656</a></span> (1989); <i><span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/" aria-description="Citation for case: New York v. Burger">Burger, supra;</a></span> </i><i>Michigan</i> v. <i>Tyler,</i> <span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499</a></span> (1978); <i>Camara</i> v. <i>Municipal Court of City and County of San Francisco,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967). It likewise does not preclude an inquiry into programmatic purpose here.</p>
<p>Last Term in <i><span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">Bond</a></span>,</i> we addressed the question whether a law enforcement officer violated a reasonable expectation of privacy in conducting a tactile examination of carry-on luggage in the overhead compartment of a bus. In doing so, we simply noted that the principle of <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span></i> rendered the subjective intent of an officer irrelevant to this analysis. <span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/#338" aria-description="Citation for case: Bond v. United States">529 U. S., at 338, n. 2</a></span>. While, as petitioners correctly observe, the analytical rubric of <i><span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">Bond</a></span></i> was not "ordinary, probable-cause Fourth Amendment analysis," <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#813" aria-description="Citation for case: Whren v. United States"><i>Whren, supra,</i>  at 813</a></span>, nothing in <i><span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">Bond</a></span></i> suggests that we would extend the principle of <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span></i> to all situations where individualized suspicion was lacking. Rather, subjective intent was irrelevant in <i><span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">Bond</a></span></i> because the inquiry that our precedents required focused on the objective effects of the actions of an individual officer. By contrast, our cases dealing with intrusions that occur pursuant to a general scheme absent individualized suspicion have often required an inquiry into purpose at the programmatic level.</p>
<p>Petitioners argue that the Indianapolis checkpoint program is justified by its lawful secondary purposes of keeping impaired motorists off the road and verifying licenses and registrations. Brief for Petitioners 31-34. If this were the case, however, law enforcement authorities would be able to establish checkpoints for virtually any purpose so long as they also included a license or sobriety check. For this reason, we examine the available evidence to determine the primary purpose of the checkpoint program. While we recognize the challenges inherent in a purpose inquiry, courts <span class="star-pagination">*47</span> routinely engage in this enterprise in many areas of constitutional jurisprudence as a means of sifting abusive governmental conduct from that which is lawful. Cf. <span class="citation" data-id="6983057"><a href="/opinion/7078145/edmond-v-goldsmith/#665" aria-description="Citation for case: Edmond v. Goldsmith">183 F. 3d, at 665</a></span>. As a result, a program driven by an impermissible purpose may be proscribed while a program impelled by licit purposes is permitted, even though the challenged conduct may be outwardly similar. While reasonableness under the Fourth Amendment is predominantly an objective inquiry, our special needs and administrative search cases demonstrate that purpose is often relevant when suspicionless intrusions pursuant to a general scheme are at issue.<sup>[2]</sup></p>
<p>It goes without saying that our holding today does nothing to alter the constitutional status of the sobriety and border checkpoints that we approved in <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> and <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>,</i>  or of the type of traffic checkpoint that we suggested would be lawful in <i><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span>.</i> The constitutionality of such checkpoint programs still depends on a balancing of the competing interests at stake and the effectiveness of the program. See <i>Sitz,</i> <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#450" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S., at 450-455</a></span>; <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 556-564</a></span>. When law enforcement authorities pursue primarily general crime control purposes at checkpoints such as here, however, stops can only be justified by some quantum of individualized suspicion.</p>
<p>Our holding also does not affect the validity of border searches or searches at places like airports and government <span class="star-pagination">*48</span> buildings, where the need for such measures to ensure public safety can be particularly acute. Nor does our opinion speak to other intrusions aimed primarily at purposes beyond the general interest in crime control. Our holding also does not impair the ability of police officers to act appropriately upon information that they properly learn during a checkpoint stop justified by a lawful primary purpose, even where such action may result in the arrest of a motorist for an offense unrelated to that purpose. Finally, we caution that the purpose inquiry in this context is to be conducted only at the programmatic level and is not an invitation to probe the minds of individual officers acting at the scene. Cf. <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren, supra</a></span></i><i>.</i> </p>
<p>Because the primary purpose of the Indianapolis checkpoint program is ultimately indistinguishable from the general interest in crime control, the checkpoints violate the Fourth Amendment. The judgment of the Court of Appeals is, accordingly, affirmed.</p>
<p><i>It is so ordered.</i> </p>
<p>Chief Justice Rehnquist, with whom Justice Thomas joins, and with whom Justice Scalia joins as to Part I, dissenting.</p>
<p>The State's use of a drug-sniffing dog, according to the Court's holding, annuls what is otherwise plainly constitutional under our Fourth Amendment jurisprudence: brief, standardized, discretionless, roadblock seizures of automobiles, seizures which effectively serve a weighty state interest with only minimal intrusion on the privacy of their occupants. Because these seizures serve the State's accepted and significant interests of preventing drunken driving and checking for driver's licenses and vehicle registrations, and because there is nothing in the record to indicate that the addition of the dog sniff lengthens these otherwise legitimate seizures, I dissent.</p>
<p></p>
<h2>
<span class="star-pagination">*49</span> I</h2>
<p>As it is nowhere to be found in the Court's opinion, I begin with blackletter roadblock seizure law. "The principal protection of Fourth Amendment rights at checkpoints lies in appropriate limitations on the scope of the stop." <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#566" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 566-567</a></span> (1976). Roadblock seizures are consistent with the Fourth Amendment if they are "carried out pursuant to a plan embodying explicit, neutral limitations on the conduct of individual officers." <i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#51" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 51</a></span> (1979). Specifically, the constitutionality of a seizure turns upon "a weighing of the gravity of the public concerns served by the seizure, the degree to which the seizure advances the public interest, and the severity of the interference with individual liberty." <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#50" aria-description="Citation for case: Brown v. Texas"><i>Id.,</i> at 50-51</a></span>.</p>
<p>We first applied these principles in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte, supra,</a></span></i> which approved highway checkpoints for detecting illegal aliens. In <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>,</i> we balanced the United States' formidable interest in checking the flow of illegal immigrants against the limited "objective" and "subjective" intrusion on the motorists. The objective intrusionthe stop itself,<sup>[1]</sup> the brief questioning of the occupants, and the visual inspection of the carwas considered "limited" because "[n]either the vehicle nor its occupants [were] searched." <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#558" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Id.,</i> at 558</a></span>. Likewise, the subjective intrusion, or the fear and surprise engendered in law-abiding motorists by the nature of the stop, was found to be minimal because the "regularized manner in which [the] established checkpoints [were] operated [was] visible evidence, reassuring to law-abiding motorists, that the stops [were] duly authorized and believed to serve the public interest." <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#559" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Id.,</i> at 559</a></span>. Indeed, the standardized operation of the roadblocks was viewed as <span class="star-pagination">*50</span> markedly different from roving patrols, where the unbridled discretion of officers in the field could result in unlimited interference with motorists' use of the highways. Cf. <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975). And although the decision in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> did not turn on the checkpoints' effectiveness, the record in one of the consolidated cases demonstrated that illegal aliens were found in 0.12 percent of the stopped vehicles. See <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#554" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 554</a></span>.</p>
<p>In <i>Michigan Dept. of State Police</i> v. <i>Sitz,</i> <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S. 444</a></span> (1990), we upheld the State's use of a highway sobriety checkpoint after applying the framework set out in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte, supra,</a></span></i> and <i>Brown</i> v. <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Texas, supra</a></span></i><i>.</i> There, we recognized the gravity of the State's interest in curbing drunken driving and found the objective intrusion of the approximately 25-second seizure to be "slight." <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#451" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S., at 451</a></span>. Turning to the subjective intrusion, we noted that the checkpoint was selected pursuant to guidelines and was operated by uniformed officers. See <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#453" aria-description="Citation for case: Michigan Department of State Police v. Sitz"><i>id.,</i> at 453</a></span>. Finally, we concluded that the program effectively furthered the State's interest because the checkpoint resulted in the arrest of two drunk drivers, or 1.6 percent of the 126 drivers stopped. See <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#455" aria-description="Citation for case: Michigan Department of State Police v. Sitz"><i>id.,</i> at 455-456</a></span>.</p>
<p>This case follows naturally from <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> and <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span>.</i>  Petitioners acknowledge that the "primary purpose" of these roadblocks is to interdict illegal drugs, but this fact should not be controlling. Even accepting the Court's conclusion that the checkpoints at issue in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> and <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i>  were not primarily related to criminal law enforcement,<sup>[2]</sup> the <span class="star-pagination">*51</span> question whether a law enforcement purpose could support a roadblock seizure is not presented in this case. The District Court found that another "purpose of the checkpoints is to check driver's licenses and vehicle registrations," App. to Pet. for Cert. 44a, and the written directives state that the police officers are to "[l]ook for signs of impairment," <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">id.,</a></span></i> at 53a. The use of roadblocks to look for signs of impairment was validated by <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span>,</i> and the use of roadblocks to check for driver's licenses and vehicle registrations was expressly recognized in <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 663</a></span> (1979).<sup>[3]</sup> That the roadblocks serve these legitimate state interests cannot be seriously disputed, as the 49 people arrested for offenses unrelated to drugs can attest. <i>Edmond</i> v. <i>Goldsmith,</i> <span class="citation" data-id="6983057"><a href="/opinion/7078145/edmond-v-goldsmith/#661" aria-description="Citation for case: Edmond v. Goldsmith">183 F. 3d 659, 661</a></span> (CA7 1999). And it would be speculative to concludegiven the District Court's findings, the written directives, and the actual arreststhat petitioners would not have operated these roadblocks but for the State's interest in interdicting drugs.</p>
<p>Because of the valid reasons for conducting these roadblock seizures, it is constitutionally irrelevant that petitioners also hoped to interdict drugs. In <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U. S. 806</a></span> (1996), we held that an officer's subjective intent would not invalidate an otherwise objectively justifiable stop of an automobile. The reasonableness of an officer's discretionary decision to stop an automobile, at issue in <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span>,</i> turns on whether there is probable cause to believe that a traffic violation has occurred. The reasonableness of highway checkpoints, at issue here, turns on whether they effectively serve a significant state interest with minimal intrusion on motorists. The stop in <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span></i> was objectively reasonable because the police officers had witnessed traffic violations; so too the roadblocks here are objectively <span class="star-pagination">*52</span> reasonable because they serve the substantial interests of preventing drunken driving and checking for driver's licenses and vehicle registrations with minimal intrusion on motorists.</p>
<p>Once the constitutional requirements for a particular seizure are satisfied, the subjective expectations of those responsible for it, be it police officers or members of a city council, are irrelevant. Cf. <i>Scott</i> v. <i>United States,</i> <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#136" aria-description="Citation for case: Scott v. United States">436 U. S. 128, 136</a></span> (1978) ("Subjective intent alone . . . does not make otherwise lawful conduct illegal or unconstitutional"). It is the objective effect of the State's actions on the privacy of the individual that animates the Fourth Amendment. See <i>Bond</i> v. <i>United States,</i> <span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/#338" aria-description="Citation for case: Bond v. United States">529 U. S. 334, 338, n. 2</a></span> (2000) (applying <i>Whren</i> to determine if an officer's conduct amounted to a "search" under the Fourth Amendment because "the issue is not his state of mind, but the objective effect of his actions"). Because the objective intrusion of a valid seizure does not turn upon anyone's subjective thoughts, neither should our constitutional analysis.<sup>[4]</sup></p>
<p>With these checkpoints serving two important state interests, the remaining prongs of the <i>Brown</i> v. <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Texas</a></span></i> balancing test are easily met. The seizure is objectively reasonable as it lasts, on average, two to three minutes and does not involve a search. App. to Pet. for Cert. 57a. The subjective intrusion is likewise limited as the checkpoints are clearly marked and operated by uniformed officers who are directed to stop every vehicle in the same manner. <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Ibid.</a></span></i> The only difference between this case and <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> is the presence of the dog. We have already held, however, that a "sniff test" by a trained narcotics dog is not a "search" within the meaning of the Fourth Amendment because it does not require physical intrusion of the object being sniffed and it does not expose <span class="star-pagination">*53</span> anything other than the contraband items. <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#706" aria-description="Citation for case: United States v. Place">462 U. S. 696, 706-707</a></span> (1983). And there is nothing in the record to indicate that the dog sniff lengthens the stop. Finally, the checkpoints' success rate49 arrests for offenses unrelated to drugsonly confirms the State's legitimate interests in preventing drunken driving and ensuring the proper licensing of drivers and registration of their vehicles. <span class="citation" data-id="6983057"><a href="/opinion/7078145/edmond-v-goldsmith/#661" aria-description="Citation for case: Edmond v. Goldsmith">183 F. 3d, at 661</a></span>.<sup>[5]</sup></p>
<p>These stops effectively serve the State's legitimate interests; they are executed in a regularized and neutral manner; and they only minimally intrude upon the privacy of the motorists. They should therefore be constitutional.</p>
<p></p>
<h2>II</h2>
<p>The Court, unwilling to adopt the straightforward analysis that these precedents dictate, adds a new non-lawenforcement primary purpose test lifted from a distinct area of Fourth Amendment jurisprudence relating to the <i>searches</i>  of homes and businesses. As discussed above, the question that the Court answers is not even posed in this case given the accepted reasons for the seizures. But more fundamentally, whatever sense a non-law-enforcement primary purpose test may make in the search setting, it is ill suited to brief roadblock seizures, where we have consistently looked at "the scope of the stop" in assessing a program's constitutionality. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#567" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 567</a></span>.</p>
<p>We have already rejected an invitation to apply the nonlaw-enforcement primary purpose test that the Court now finds so indispensable. The respondents in <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> argued that the <i>Brown</i> v. <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Texas</a></span></i> balancing test was not the "proper method of analysis" with regards to roadblock seizures:</p>
<blockquote>"Respondents argue that there must be a showing of some special governmental need `beyond the normal <span class="star-pagination">*54</span> need' for criminal law enforcement before a balancing analysis is appropriate, and that [the State] ha[s] demonstrated no such special need.</blockquote>
<blockquote>"But it is perfectly plain from a reading of [<i>Treasury</i>  <i>Employees</i> v.] <i>Von Raab</i> [, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656</a></span> (1989)], which cited and discussed with approval our earlier decision in <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976), that it was in no way designed to repudiate our prior cases dealing with police stops of motorists on public highways. <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte, supra,</a></span></i> which utilized a balancing analysis in approving highway checkpoints for detecting illegal aliens, and <i>Brown</i> v. <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Texas, supra</a></span></i><i>,</i> are the relevant authorities here." <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#449" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S., at 449, 450</a></span>.</blockquote>
<p>Considerations of <i>stare decisis</i> aside, the "perfectly plain" reason for not incorporating the "special needs" test in our roadblock seizure cases is that seizures of automobiles "deal neither with searches nor with the sanctity of private dwellings, ordinarily afforded the most stringent Fourth Amendment protection." <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#561" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Martinez-Fuerte, supra,</i> at 561</a></span>.</p>
<p>The "special needs" doctrine, which has been used to uphold certain suspicionless searches performed for reasons unrelated to law enforcement, is an exception to the general rule that a search must be based on individualized suspicion of wrongdoing. See, <i>e. g., </i><i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602</a></span> (1989) (drug test search); <i>Camara</i>  v. <i>Municipal Court of City and County of San Francisco,</i>  <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967) (home administrative search). The doctrine permits intrusions into a person's body and home, areas afforded the greatest Fourth Amendment protection. But there were no such intrusions here.</p>
<p>"[O]ne's expectation of privacy in an automobile and of freedom in its operation are significantly different from the traditional expectation of privacy and freedom in one's residence." <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#561" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Martinez-Fuerte, supra,</i> at 561</a></span>. This is because "[a]utomobiles, unlike homes, are subjected to pervasive and continuing governmental regulation and controls." <i>South</i>  <span class="star-pagination">*55</span> <i>Dakota</i> v. <i>Opperman,</i> <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#368" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 368</a></span> (1976); see also <i>New York</i> v. <i>Class,</i> <span class="citation" data-id="9430353"><a href="/opinion/111600/new-york-v-class/#113" aria-description="Citation for case: New York v. Class">475 U. S. 106, 113</a></span> (1986) ("[A]utomobiles are justifiably the subject of pervasive regulation by the State"); <i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590</a></span> (1974) ("One has a lesser expectation of privacy in a motor vehicle because its function is transportation and it seldom serves as one's residence or as the repository of personal effects"). The lowered expectation of privacy in one's automobile is coupled with the limited nature of the intrusion: a brief, standardized, nonintrusive seizure.<sup>[6]</sup> The brief seizure of an automobile can hardly be compared to the intrusive search of the body or the home. Thus, just as the "special needs" inquiry serves to both define and limit the permissible scope of those searches, the <i>Brown</i> v. <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Texas</a></span></i> balancing test serves to define and limit the permissible scope of automobile seizures.</p>
<p>Because of these extrinsic limitations upon roadblock seizures, the Court's newfound non-law-enforcement primary purpose test is both unnecessary to secure Fourth Amendment rights and bound to produce wide-ranging litigation over the "purpose" of any given seizure. Police designing highway roadblocks can never be sure of their validity, since a jury might later determine that a forbidden purpose exists. Roadblock stops identical to the one that we upheld in <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i>  10 years ago, or to the one that we upheld 24 years ago in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>,</i> may now be challenged on the grounds that they have some concealed forbidden purpose.</p>
<p>Efforts to enforce the law on public highways used by millions of motorists are obviously necessary to our society. The Court's opinion today casts a shadow over what had been assumed, on the basis of <i>stare decisis,</i> to be a perfectly lawful activity. Conversely, if the Indianapolis police had assigned a different purpose to their activity here, but in no way changed what was done on the ground to individual <span class="star-pagination">*56</span> motorists, it might well be valid. See <i>ante,</i> at 47, n. 2. The Court's non-law-enforcement primary purpose test simply does not serve as a proxy for anything that the Fourth Amendment is, or should be, concerned about in the automobile seizure context.</p>
<p>Petitioners' program complies with our decisions regarding roadblock seizures of automobiles, and the addition of a dog sniff does not add to the length or the intrusion of the stop. Because such stops are consistent with the Fourth Amendment, I would reverse the decision of the Court of Appeals.</p>
<p>Justice Thomas, dissenting.</p>
<p>Taken together, our decisions in <i>Michigan Dept. of State Police</i> v. <i>Sitz,</i> <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S. 444</a></span> (1990), and <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976), stand for the proposition that suspicionless roadblock seizures are constitutionally permissible if conducted according to a plan that limits the discretion of the officers conducting the stops. I am not convinced that <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> and <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> were correctly decided. Indeed, I rather doubt that the Framers of the Fourth Amendment would have considered "reasonable" a program of indiscriminate stops of individuals not suspected of wrongdoing.</p>
<p>Respondents did not, however, advocate the overruling of <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> and <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>,</i> and I am reluctant to consider such a step without the benefit of briefing and argument. For the reasons given by The Chief Justice, I believe that those cases compel upholding the program at issue here. I, therefore, join his opinion.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for the State of Kansas et al. by <i>Carla J. Stovall,</i> Attorney General of Kansas, <i>Stephen R. McAllister,</i> State Solicitor, <i>Jared S. Maag,</i> Assistant Attorney General, and <i>John M. Bailey,</i> Chief State's Attorney of Connecticut, and by the Attorneys General for their respective States as follows: <i>Bill Pryor</i> of Alabama, <i>Janet Napolitano</i> of Arizona, <i>Mark Pryor</i> of Arkansas, <i>Bill Lockyer</i> of California, <i>Robert A. Butterworth</i> of Florida, <i>James E. Ryan</i>  of Illinois, <i>Karen M. Freeman-Wilson</i> of Indiana, <i>Thomas J. Miller</i> of Iowa, <i>Michael C. Moore</i> of Mississippi, <i>Don Stenberg</i> of Nebraska, <i>W. A. Drew Edmondson</i> of Oklahoma, <i>Jan Graham</i> of Utah, and <i>Mark L. Earley</i>  of Virginia; for the National League of Cities et al. by <i>Richard Ruda</i> and <i>James I. Crowley;</i> and for the Washington Legal Foundation et al. by <i>Daniel J. Popeo.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the National Association of Criminal Defense Lawyers et al. by <i>Wesley MacNeil Oliver</i>  and <i>Barbara Bergman;</i> and for the Rutherford Institute by <i>John W. Whitehead</i> and <i>Steven H. Aden.</i> </p>
<p><i>Wayne W. Schmidt, James P. Manak, Richard Weintraub,</i> and <i>Bernard J. Farber</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae.</i> </p>
<p>[1]  The Chief Justice's dissent erroneously characterizes our opinion as resting on the application of a "non-law-enforcement primary purpose test." <i>Post,</i> at 53. Our opinion nowhere describes the purposes of the <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> and <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> checkpoints as being "not primarily related to criminal law enforcement." <i>Post,</i> at 50. Rather, our judgment turns on the fact that the primary purpose of the Indianapolis checkpoints is to advance the general interest in crime control.
</p>
<p>The Chief Justice's dissent also erroneously characterizes our opinion as holding that the "use of a drug-sniffing dog . . . annuls what is otherwise plainly constitutional under our Fourth Amendment jurisprudence." <i>Post,</i> at 48. Again, the constitutional defect of the program is that its primary purpose is to advance the general interest in crime control.</p>
<p>[2]  Because petitioners concede that the primary purpose of the Indianapolis checkpoints is narcotics detection, we need not decide whether the State may establish a checkpoint program with the primary purpose of checking licenses or driver sobriety and a secondary purpose of interdicting narcotics. Specifically, we express no view on the question whether police may expand the scope of a license or sobriety checkpoint seizure in order to detect the presence of drugs in a stopped car. Cf. <i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#341" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 341</a></span> (1985) (search must be "`reasonably related in scope to the circumstances which justified the interference in the first place' " (quoting <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20</a></span> (1968))); <i>Michigan</i> v. <i>Clifford,</i> <span class="citation" data-id="9429413"><a href="/opinion/111057/michigan-v-clifford/#294" aria-description="Citation for case: Michigan v. Clifford">464 U. S. 287, 294-295</a></span> (1984) (plurality opinion).</p>
<p>[1]  The record from one of the consolidated cases indicated that the stops lasted between three and five minutes. See <i>United States</i> v. <i>MartinezFuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#546" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 546-547</a></span> (1976).</p>
<p>[2]  This gloss, see <i>ante,</i> at 38-40, 41-43, is not at all obvious. The respondents in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> were criminally prosecuted for illegally transporting aliens, and the Court expressly noted that "[i]nterdicting the flow of illegal entrants from Mexico poses formidable law enforcement problems." 428 U. S., at 552. And the <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span></i> Court recognized that if an "officer's observations suggest that the driver was intoxicated, an arrest would be made." <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#447" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S., at 447</a></span>. But however persuasive the distinction, the Court's opinion does not impugn the continuing validity of <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span></i> and <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span>.</i> See <i>ante,</i> at 47.</p>
<p>[3]  Several Courts of Appeals have upheld roadblocks that check for driver's licenses and vehicle registrations. See, <i>e. g., </i><i>United States</i>  v. <i>Galindo-Gonzales,</i> <span class="citation" data-id="156261"><a href="/opinion/156261/united-states-v-galindo-gonzales/" aria-description="Citation for case: United States v. Galindo-Gonzales">142 F. 3d 1217</a></span> (CA10 1998); <i>United States</i> v. <i>McFayden,</i> <span class="citation" data-id="517399"><a href="/opinion/517399/united-states-v-gregory-mcfayden/" aria-description="Citation for case: United States v. Gregory McFayden">865 F. 2d 1306</a></span> (CADC 1989).</p>
<p>[4]  Of course we have looked to the purpose of the program in analyzing the constitutionality of certain suspicionless searches. As discussed in Part II, <i>infra,</i> that doctrine has never been applied to seizures of automobiles.</p>
<p>[5]  Put in statistical terms, 4.2 percent of the 1,161 motorists stopped were arrested for offenses unrelated to drugs.</p>
<p>[6]  This fact distinguishes the roadblock seizure of an automobile from an inventory search of an automobile. Cf. <i>Colorado</i> v. <i>Bertine,</i> <span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">479 U. S. 367</a></span> (1987) (automobile inventory search).</p>

</div>
```

---

## GROUP: content/cases/City of Los Angeles v. Patel.md  (`case`, 5 assertions)

### content_page

```
---
title: "City of Los Angeles v. Patel"
type: case
citation: ""
parallel_cite: "576 U.S. 409; 135 S. Ct. 2443; 192 L. Ed. 2d 435; 83 U.S.L.W. 4520; 25 Fla. L. Weekly Fed. S 412"
neutral_cite: 2015 U.S. LEXIS 4065
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2015
date_decided: 2015-06-22
docket: 13-1175
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2015-06-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: City of Los Angeles v. Patel
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2811846/city-of-l-a-v-patel/"
  cluster_id: 2811846
  opinion_id: 2811846
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Camara v. Municipal Court]]", "[[City of Indianapolis v. Edmond]]"]
aliases: ["Los Angeles v. Patel"]
tags: ["case", "fourth-amendment", "administrative-search", "special-needs", "precompliance-review", "facial-challenge"]
holding: "A hotel guest-registry inspection ordinance is facially unconstitutional because it gives operators no opportunity for pre-compliance…"
lake:
  record_id: City of Los Angeles v. Patel
  status: verified
  projected_at: 2026-07-06
---

# City of Los Angeles v. Patel

*576 U.S. 409 (2015)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Los Angeles ordinance required hotel operators to keep specified guest-registry information and to make it available to police on demand, making refusal a misdemeanor punishable by arrest. A group of motel operators brought a facial Fourth Amendment challenge to the on-demand inspection provision.

## Issue
Whether an ordinance compelling hotel operators to turn over their guest registries to police on demand, with no opportunity for pre-compliance review and arrest for refusal, is facially unconstitutional.

## Rule
Yes. An administrative search regime must afford the subject a chance to contest the demand before a neutral official: "absent consent, exigent circumstances, or the like, in order for an administrative search to be constitutional, the subject of the search must be afforded an opportunity to obtain precompliance review before a neutral decisionmaker." — *Los Angeles v. Patel*, 576 U.S. 409 (2015) (slip op., at 10). ^pin-op10

"[W]e hold only that a hotel owner must be afforded an opportunity to have a neutral decisionmaker review an officer's demand to search the registry before he or she faces penalties for failing to comply." — *Id.* (slip op., at 11). ^pin-op11

## Application
The ordinance let an officer demand a hotel's registry on the spot and arrest the operator for any refusal, with no mechanism — administrative subpoena or otherwise — to obtain review before penalties attached. Because it provided no opportunity whatsoever for pre-compliance review, the inspection provision was facially invalid on these terms.

## Conclusion
The registry-inspection provision was facially unconstitutional; the judgment striking it down was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Patel* applies the administrative-search precompliance-review principle of [[Camara v. Municipal Court]] and complements the special-needs purpose analysis of [[City of Indianapolis v. Edmond]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *City of Los Angeles v. Patel*, 576 U.S. 409 (2015) — https://www.courtlistener.com/opinion/2810524/los-angeles-v-patel/ — pinpoints: slip op., at 10, 11 (CL carries the slip opinion under the cluster name "Los Angeles v. Patel").

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ec94f1037ab3e2db", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2015 U.S. LEXIS 4065", "official_citation_present": false, "parallel_cite": "576 U.S. 409; 135 S. Ct. 2443; 192 L. Ed. 2d 435; 83 U.S.L.W. 4520; 25 Fla. L. Weekly Fed. S 412", "title": "City of Los Angeles v. Patel", "year": "2015"}}
{"assertion_id": "cd6ed468703dbc15", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Key — Progeny / Refinement", "title": "City of Los Angeles v. Patel"}}
{"assertion_id": "da7ba18efaefec12", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A hotel guest-registry inspection ordinance is facially unconstitutional because it gives operators no opportunity for pre-compliance…", "title": "City of Los Angeles v. Patel"}}
{"assertion_id": "1ee1b1163494971d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "City of Los Angeles v. Patel"}}
{"assertion_id": "7a196e3419ac48a9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2015-06-22", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "City of Los Angeles v. Patel", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "City of Los Angeles v. Patel", "varies_by_point": "false"}}
```

### lake record — City of Los Angeles v. Patel

```json
{
  "schema_version": "s2.v1",
  "record_id": "City of Los Angeles v. Patel",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "City of L. A. v. Patel",
    "case_name_short": "Patel",
    "case_name_full": "CITY OF LOS ANGELES, CALIFORNIA, for Petitioner v. Naranjibhai PATEL, Et Al.",
    "input_case_name": "City of Los Angeles v. Patel",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2015-06-22",
    "year": 2015,
    "docket": "13-1175",
    "cluster_id": 2811846,
    "lead_opinion_id": 2811846,
    "sibling_ids": [
      2811846
    ],
    "absolute_url": "/opinion/2811846/city-of-l-a-v-patel/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 2810524,
        "score": 120,
        "case_name": "Los Angeles v. Patel"
      },
      {
        "cluster_id": 8172542,
        "score": 20,
        "case_name": "City of L. A. v. Patel"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "576 U.S. 409",
        "volume": "576",
        "reporter": "U.S.",
        "page": "409",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 S. Ct. 2443",
        "volume": "135",
        "reporter": "S. Ct.",
        "page": "2443",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "192 L. Ed. 2d 435",
        "volume": "192",
        "reporter": "L. Ed. 2d",
        "page": "435",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 U.S.L.W. 4520",
        "volume": "83",
        "reporter": "U.S.L.W.",
        "page": "4520",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 412",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "412",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2015 U.S. LEXIS 4065",
        "volume": "2015",
        "reporter": "U.S. LEXIS",
        "page": "4065",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "576 U.S. 409",
        "volume": "576",
        "reporter": "U.S.",
        "page": "409",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 S. Ct. 2443",
        "volume": "135",
        "reporter": "S. Ct.",
        "page": "2443",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "192 L. Ed. 2d 435",
        "volume": "192",
        "reporter": "L. Ed. 2d",
        "page": "435",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2015 U.S. LEXIS 4065",
        "volume": "2015",
        "reporter": "U.S. LEXIS",
        "page": "4065",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 U.S.L.W. 4520",
        "volume": "83",
        "reporter": "U.S.L.W.",
        "page": "4520",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 412",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "412",
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
      "id": "pin-op10",
      "page": null,
      "quote": "--- # City of Los Angeles v. Patel *576 U.S. 409 (2015)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Los Angeles ordinance required hotel operators to keep specified guest-registry information and to make it available to police on demand, making refusal a misdemeanor punishable by arrest. A group of motel operators brought a facial Fourth Amendment challenge to the on-demand inspection provision. ## Issue Whether an ordinance compelling hotel operators to turn over their guest registries to police on demand, with no opportunity for pre-compliance review and arrest for refusal, is facially unconstitutional. ## Rule Yes. An administrative search regime must afford the subject a chance to contest the demand before a neutral official:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op11",
      "page": null,
      "quote": "[W]e hold only that a hotel owner must be afforded an opportunity to have a neutral decisionmaker review an officer's demand to search the registry before he or she faces penalties for failing to comply.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2015-06-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "City of Los Angeles v. Patel",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
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
        "journal_ref": "City of Los Angeles v. Patel:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cosino v. State",
          "cluster_id": 5447462,
          "cite": [
            "503 S.W.3d 592",
            "2016 Tex. App. LEXIS 11431",
            "2016 WL 6134461"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane1_negative"
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
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Perry, Ex Parte James Richard \"Rick\"",
          "cluster_id": 3180638,
          "cite": [
            "483 S.W.3d 884",
            "2016 Tex. Crim. App. LEXIS 43",
            "2016 WL 738237"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salinas, Orlando",
          "cluster_id": 4374733,
          "cite": [
            "523 S.W.3d 103",
            "2017 WL 915525",
            "2017 Tex. Crim. App. LEXIS 284"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Eubanks",
          "cluster_id": 4684248,
          "cite": [
            "2019 IL 123525"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Burns",
          "cluster_id": 3171866,
          "cite": [
            "2015 IL 117387"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of El Cenizo, Texas v. State of Texas",
          "cluster_id": 4496244,
          "cite": [
            "890 F.3d 164"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Plains All American Pipeline L v. Thomas Cook",
          "cluster_id": 4417283,
          "cite": [
            "866 F.3d 534",
            "2017 WL 3403129",
            "2017 U.S. App. LEXIS 14661"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joseph Zadeh v. Mari Robinson",
          "cluster_id": 4636058,
          "cite": [
            "928 F.3d 457"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Free Speech Coalition, Inc. v. Attorney General United States",
          "cluster_id": 3210858,
          "cite": [
            "825 F.3d 149",
            "44 Media L. Rep. (BNA) 2157",
            "2016 U.S. App. LEXIS 10356",
            "2016 WL 3191474"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Porter v. City of Philadelphia",
          "cluster_id": 4786569,
          "cite": [
            "975 F.3d 374"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Toledo v. State",
          "cluster_id": 5448352,
          "cite": [
            "519 S.W.3d 273",
            "2017 WL 1281437",
            "2017 Tex. App. LEXIS 3023"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Durham",
          "cluster_id": 4531050,
          "cite": [
            "902 F.3d 1180"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Shaquille Robinson",
          "cluster_id": 4340460,
          "cite": [
            "846 F.3d 694",
            "2017 WL 280727",
            "2017 U.S. App. LEXIS 1134"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William Gardner v. Jason Evans",
          "cluster_id": 4607076,
          "cite": [
            "920 F.3d 1038"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Winston v. City of Syracuse",
          "cluster_id": 8439878,
          "cite": [
            "887 F.3d 553"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Liberty Coins v. David Goodman",
          "cluster_id": 4460823,
          "cite": [
            "880 F.3d 274"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Curtis Morrison v. Mark Peterson",
          "cluster_id": 3162649,
          "cite": [
            "809 F.3d 1059",
            "2015 U.S. App. LEXIS 21669",
            "2015 WL 8756229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nadine Pellegrino v. TSA",
          "cluster_id": 4657793,
          "cite": [
            "937 F.3d 164"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas Association of Business National Federation of Independent Business, American Staffing Association LeadingEdge Personnel, Ltd. Staff Force, Inc. HT Staffing Ltd. D/B/A the HT Group The Burnett Companies Consolidated, Inc., D/B/A Burnett Specialists Society for Human Resource Management Texas State Council of the Society for Human Resource Management Austin Human Resource Management Association Strickland School, LLC And the State of Texas v. City of Austin, Texas, and Spencer Cronk, City Manager of the City of Austin",
          "cluster_id": 4565114,
          "cite": [
            "565 S.W.3d 425"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Allmond v. Department of Health & Mental Hygiene",
          "cluster_id": 4237242,
          "cite": [
            "141 A.3d 57",
            "448 Md. 592",
            "2016 Md. LEXIS 436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mohamed Mohamud",
          "cluster_id": 4327222,
          "cite": [
            "843 F.3d 420",
            "2016 U.S. App. LEXIS 21622",
            "2016 WL 7046751"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Expressions Hair Design v. Schneiderman",
          "cluster_id": 8442471,
          "cite": [
            "808 F.3d 118",
            "2015 U.S. App. LEXIS 21521",
            "2015 WL 8537667"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Los Angeles v. Patel:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2811846) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 127,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 127,
        "triage_read": 2,
        "triage_snippet_classified": 125
      },
      "lane2_top_cited": {
        "query": "cites:(2811846)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05JnM9NDU0MjIyMSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%282811846%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2811846)",
        "reviewed": 8,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 8,
        "triage_read": 0,
        "triage_snippet_classified": 8
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2811846)",
    "indexed_citing_opinions": 140,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2811846,
        "count": 140,
        "count_source": "search"
      }
    ],
    "citation_count": 241,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/city-of-los-angeles-v-patel.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc3NDAwOTgmcz02NDY3MDQ5JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%282811846%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2811846,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 109005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 110530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 111061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 111835,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 111891,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 111927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 112765,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 112786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 118100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 118299,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 118391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 118405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 118414,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 145777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 145824,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 145887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 202028,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 357364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 385866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 449079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 677802,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 1254195,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 1489882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 2142195,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811846,
        "cited_id": 2620876,
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
    "date_created": "2026-07-05T00:21:22Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:22:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:22:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:26:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:22:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — City of Los Angeles v. Patel

```
(Slip Opinion)              OCTOBER TERM, 2014                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

CITY OF LOS ANGELES, CALIFORNIA v. PATEL ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE NINTH CIRCUIT

      No. 13–1175. Argued March 3, 2015—Decided June 22, 2015
Petitioner, the city of Los Angeles (City), requires hotel operators to
  record and keep specific information about their guests on the prem-
  ises for a 90-day period. Los Angeles Municipal Code §41.49. These
  records “shall be made available to any officer of the Los Angeles Po-
  lice Department for inspection . . . at a time and in a manner that
  minimizes any interference with the operation of the business,”
  §41.49(3)(a), and a hotel operator’s failure to make the records avail-
  able is a criminal misdemeanor, §11.00(m). Respondents, a group of
  motel operators and a lodging association, brought a facial challenge
  to §41.49(3)(a) on Fourth Amendment grounds. The District Court
  entered judgment for the City, finding that respondents lacked a rea-
  sonable expectation of privacy in their records. The Ninth Circuit
  subsequently reversed, determining that inspections under
  §41.49(3)(a) are Fourth Amendment searches and that such searches
  are unreasonable under the Fourth Amendment because hotel own-
  ers are subjected to punishment for failure to turn over their records
  without first being afforded the opportunity for precompliance re-
  view.
Held:
    1. Facial challenges under the Fourth Amendment are not categor-
 ically barred or especially disfavored. Pp. 4–8.
       (a) Facial challenges to statutes—as opposed to challenges to
 particular applications of statutes—have been permitted to proceed
 under a diverse array of constitutional provisions. See, e.g., Sorrell v.
 IMS Health Inc., 564 U. S. ___ (First Amendment); District of Colum-
 bia v. Heller, 554 U. S. 570 (Second Amendment). The Fourth
 Amendment is no exception. Sibron v. New York, 392 U. S. 40, dis-
 tinguished. This Court has entertained facial challenges to statutes
2                        LOS ANGELES v. PATEL

                                   Syllabus

    authorizing warrantless searches, declaring them, on several occa-
    sions, facially invalid, see, e.g., Chandler v. Miller, 520 U. S. 305,
    308–309. Pp. 4–7.
          (b) Petitioner contends that facial challenges to statutes author-
    izing warrantless searches must fail because they will never be un-
    constitutional in all applications, but this Court’s precedents demon-
    strate that such challenges can be brought, and can succeed. Under
    the proper facial-challenge analysis, only applications of a statute in
    which the statute actually authorizes or prohibits conduct are consid-
    ered. See, e.g., Planned Parenthood of Southeastern Pa. v. Casey, 505
    U. S. 833. When addressing a facial challenge to a statute authoriz-
    ing warrantless searches, the proper focus is on searches that the law
    actually authorizes and not those that could proceed irrespective of
    whether they are authorized by the statute, e.g., where exigent cir-
    cumstances, a warrant, or consent to search exists. Pp. 7–8.
       2. Section 41.49(3)(a) is facially unconstitutional because it fails to
    provide hotel operators with an opportunity for precompliance re-
    view. Pp. 9–17.
          (a) “ ‘[S]earches conducted outside the judicial process . . . are
    per se unreasonable under the Fourth Amendment—subject only to a
    few . . . exceptions.’ ” Arizona v. Gant, 556 U. S. 332, 338. One ex-
    ception is for administrative searches. See Camara v. Municipal
    Court of City and County of San Francisco, 387 U. S. 523, 534. To be
    constitutional, the subject of an administrative search must, among
    other things, be afforded an opportunity to obtain precompliance re-
    view before a neutral decisionmaker. See See v. Seattle, 387 U. S.
    541, 545. Assuming the administrative search exception otherwise
    applies here, §41.49 is facially invalid because it fails to afford hotel
    operators any opportunity for precompliance review. To be clear, a
    hotel owner must only be afforded an opportunity for precompliance
    review; actual review need occur only when a hotel operator objects to
    turning over the records. This opportunity can be provided without
    imposing onerous burdens on law enforcement. For instance, officers
    in the field can issue administrative subpoenas without probable
    cause that a regulation is being infringed. This narrow holding does
    not call into question those parts of §41.49 requiring hotel operators
    to keep records nor does it prevent police from obtaining access to
    those records where a hotel operator consents to the search, where
    the officer has a proper administrative warrant, or where some other
    exception to the warrant requirement applies. Pp. 9–13.
          (b) Petitioner’s argument that the ordinance is facially valid un-
    der the more relaxed standard for closely regulated industries is re-
    jected. See Marshall v. Barlow’s, Inc., 436 U. S. 307, 313. This Court
    has only recognized four such industries, and nothing inherent in the
                     Cite as: 576 U. S. ____ (2015)                     3

                                Syllabus

  operation of hotels poses a comparable clear and significant risk to
  the public welfare. Additionally, because the majority of regulations
  applicable to hotels apply to many businesses, to classify hotels as
  closely regulated would permit what has always been a narrow ex-
  ception to swallow the rule. But even if hotels were closely regulated,
  §41.49 would still contravene the Fourth Amendment as it fails to
  satisfy the additional criteria that must be met for searches of closely
  regulated industries to be reasonable. See New York v. Burger, 482
  U. S. 691, 702–703. Pp. 13–17.
738 F. 3d 1058, affirmed.

  SOTOMAYOR, J., delivered the opinion of the Court, in which KENNE-
DY, GINSBURG, BREYER, and KAGAN, JJ., joined. SCALIA, J., filed a dis-
senting opinion, in which ROBERTS, C. J., and THOMAS, J., joined.
ALITO, J., filed a dissenting opinion, in which THOMAS, J., joined.
                        Cite as: 576 U. S. ____ (2015)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 13–1175
                                   _________________


 CITY OF LOS ANGELES, CALIFORNIA, PETITIONER
          v. NARANJIBHAI PATEL, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE NINTH CIRCUIT

                                 [June 22, 2015] 


  JUSTICE SOTOMAYOR delivered the opinion of the Court.
  Respondents brought a Fourth Amendment challenge to
a provision of the Los Angeles Municipal Code that com-
pels “[e]very operator of a hotel to keep a record” contain-
ing specified information concerning guests and to make
this record “available to any officer of the Los Angeles
Police Department for inspection” on demand. Los Ange-
les Municipal Code §§41.49(2), (3)(a), (4) (2015). The
questions presented are whether facial challenges to stat-
utes can be brought under the Fourth Amendment and, if
so, whether this provision of the Los Angeles Municipal
Code is facially invalid. We hold facial challenges can be
brought under the Fourth Amendment. We further hold
that the provision of the Los Angeles Municipal Code that
requires hotel operators to make their registries available
to the police on demand is facially unconstitutional be-
cause it penalizes them for declining to turn over their
records without affording them any opportunity for pre-
compliance review.
2                  LOS ANGELES v. PATEL

                     Opinion of the Court

                              I

                              A

   Los Angeles Municipal Code (LAMC) §41.49 requires
hotel operators to record information about their guests,
including: the guest’s name and address; the number of
people in each guest’s party; the make, model, and license
plate number of any guest’s vehicle parked on hotel prop-
erty; the guest’s date and time of arrival and scheduled
departure date; the room number assigned to the guest;
the rate charged and amount collected for the room; and
the method of payment. §41.49(2). Guests without reser-
vations, those who pay for their rooms with cash, and any
guests who rent a room for less than 12 hours must pre-
sent photographic identification at the time of check-in,
and hotel operators are required to record the number and
expiration date of that document. §41.49(4). For those
guests who check in using an electronic kiosk, the hotel’s
records must also contain the guest’s credit card infor-
mation. §41.49(2)(b). This information can be maintained
in either electronic or paper form, but it must be “kept on
the hotel premises in the guest reception or guest check-in
area or in an office adjacent” thereto for a period of 90
days. §41.49(3)(a).
   Section 41.49(3)(a)—the only provision at issue here—
states, in pertinent part, that hotel guest records “shall be
made available to any officer of the Los Angeles Police
Department for inspection,” provided that “[w]henever
possible, the inspection shall be conducted at a time and in
a manner that minimizes any interference with the opera-
tion of the business.” A hotel operator’s failure to make
his or her guest records available for police inspection is a
misdemeanor punishable by up to six months in jail and a
$1,000 fine. §11.00(m) (general provision applicable to
entire LAMC).
                 Cite as: 576 U. S. ____ (2015)            3

                     Opinion of the Court 


                              B

   In 2003, respondents, a group of motel operators along
with a lodging association, sued the city of Los Angeles
(City or petitioner) in three consolidated cases challenging
the constitutionality of §41.49(3)(a). They sought declara-
tory and injunctive relief. The parties “agree[d] that the
sole issue in the . . . action [would be] a facial constitu-
tional challenge” to §41.49(3)(a) under the Fourth Amend-
ment. App. 195. They further stipulated that respondents
have been subjected to mandatory record inspections
under the ordinance without consent or a warrant. Id., at
194–195.
   Following a bench trial, the District Court entered
judgment in favor of the City, holding that respondents’
facial challenge failed because they lacked a reasonable
expectation of privacy in the records subject to inspection.
A divided panel of the Ninth Circuit affirmed on the same
grounds. 686 F. 3d 1085 (2012). On rehearing en banc,
however, the Court of Appeals reversed. 738 F. 3d 1058,
1065 (2013).
   The en banc court first determined that a police officer’s
nonconsensual inspection of hotel records under §41.49 is
a Fourth Amendment “search” because “[t]he business
records covered by §41.49 are the hotel’s private property”
and the hotel therefore “has the right to exclude others
from prying into the[ir] contents.” Id., at 1061. Next, the
court assessed “whether the searches authorized by §41.49
are reasonable.” Id., at 1063. Relying on Donovan v. Lone
Steer, Inc., 464 U. S. 408 (1984), and See v. Seattle, 387
U. S. 541 (1967), the court held that §41.49 is facially
unconstitutional “as it authorizes inspections” of hotel
records “without affording an opportunity to ‘obtain judi-
cial review of the reasonableness of the demand prior to
suffering penalties for refusing to comply.’ ” 738 F. 3d, at
1065 (quoting See, 387 U. S., at 545).
   Two dissenting opinions were filed. The first dissent
4                  LOS ANGELES v. PATEL

                     Opinion of the Court

argued that facial relief should rarely be available for
Fourth Amendment challenges, and was inappropriate
here because the ordinance would be constitutional in
those circumstances where police officers demand access
to hotel records with a warrant in hand or exigent circum-
stances justify the search. 738 F. 3d, at 1065–1070 (opin-
ion of Tallman, J.). The second dissent conceded that
inspections under §41.49 constitute Fourth Amendment
searches, but faulted the majority for assessing the rea-
sonableness of these searches without accounting for the
weakness of the hotel operators’ privacy interest in the
content of their guest registries. Id., at 1070–1074 (opin-
ion of Clifton, J.).
  We granted certiorari, 574 U. S. ___ (2014), and now
affirm.
                             II
  We first clarify that facial challenges under the Fourth
Amendment are not categorically barred or especially
disfavored.
                               A
   A facial challenge is an attack on a statute itself as
opposed to a particular application. While such challenges
are “the most difficult . . . to mount successfully,” United
States v. Salerno, 481 U. S. 739, 745 (1987), the Court
has never held that these claims cannot be brought
under any otherwise enforceable provision of the Constitu-
tion. Cf. Fallon, Fact and Fiction About Facial Chal-
lenges, 99 Cal. L. Rev. 915, 918 (2011) (pointing to several
Terms in which “the Court adjudicated more facial chal-
lenges on the merits than it did as-applied challenges”).
Instead, the Court has allowed such challenges to proceed
under a diverse array of constitutional provisions. See,
e.g., Sorrell v. IMS Health Inc., 564 U. S. ___ (2011) (First
Amendment); District of Columbia v. Heller, 554 U. S. 570
                  Cite as: 576 U. S. ____ (2015)             5

                      Opinion of the Court

(2008) (Second Amendment); Chicago v. Morales, 527 U. S.
41 (1999) (Due Process Clause of the Fourteenth Amend-
ment); Kraft Gen. Foods, Inc. v. Iowa Dept. of Revenue and
Finance, 505 U. S. 71 (1992) (Foreign Commerce Clause).
   Fourth Amendment challenges to statutes authorizing
warrantless searches are no exception. Any claim to the
contrary reflects a misunderstanding of our decision in
Sibron v. New York, 392 U. S. 40 (1968). In Sibron, two
criminal defendants challenged the constitutionality of a
statute authorizing police to, among other things, “ ‘stop
any person abroad in a public place whom [they] reason-
ably suspec[t] is committing, has committed or is about to
commit a felony.” Id., at 43 (quoting then N. Y. Code
Crim. Proc. §180–a). The Court held that the search of
one of the defendants under the statute violated the
Fourth Amendment, 392 U. S., at 59, 62, but refused to
opine more broadly on the statute’s validity, stating that
“[t]he constitutional validity of a warrantless search is
pre-eminently the sort of question which can only be de-
cided in the concrete factual context of the individual
case.” Id., at 59.
   This statement from Sibron—which on its face might
suggest an intent to foreclose all facial challenges to stat-
utes authorizing warrantless searches—must be under-
stood in the broader context of that case. In the same
section of the opinion, the Court emphasized that the
“operative categories” of the New York law at issue were
“susceptible of a wide variety of interpretations,” id., at 60,
and that “[the law] was passed too recently for the State’s
highest court to have ruled upon many of the questions
involving potential intersections with federal constitutional
guarantees,” id., at 60, n. 20. Sibron thus stands for the
simple proposition that claims for facial relief under the
Fourth Amendment are unlikely to succeed when there is
substantial ambiguity as to what conduct a statute au-
thorizes: Where a statute consists of “extraordinarily
6                  LOS ANGELES v. PATEL

                      Opinion of the Court

elastic categories,” it may be “impossible to tell” whether
and to what extent it deviates from the requirements of
the Fourth Amendment. Id., at 59, 61, n. 20.
   This reading of Sibron is confirmed by subsequent prec-
edents. Since Sibron, the Court has entertained facial
challenges under the Fourth Amendment to statutes
authorizing warrantless searches. See, e.g., Vernonia
School District 47J v. Acton, 515 U. S. 646, 648 (1995)
(“We granted certiorari to decide whether” petitioner’s
student athlete drug testing policy “violates the Fourth
and Fourteenth Amendments to the United States Consti-
tution”); Skinner v. Railway Labor Executives’ Assn., 489
U. S. 602, 633, n. 10 (1989) (“[R]espondents have chal-
lenged the administrative scheme on its face. We deal
therefore with whether the [drug] tests contemplated by
the regulation can ever be conducted”); cf. Illinois v. Krull,
480 U. S. 340, 354 (1987) (“[A] person subject to a statute
authorizing searches without a warrant or probable cause
may bring an action seeking a declaration that the statute
is unconstitutional and an injunction barring its imple-
mentation”). Perhaps more importantly, the Court has on
numerous occasions declared statutes facially invalid
under the Fourth Amendment. For instance, in Chandler
v. Miller, 520 U. S. 305, 308–309 (1997), the Court struck
down a Georgia statute requiring candidates for certain
state offices to take and pass a drug test, concluding that
this “requirement . . . [did] not fit within the closely
guarded category of constitutionally permissible suspicion-
less searches.” Similar examples abound. See, e.g., Fer-
guson v. Charleston, 532 U. S. 67, 86 (2001) (holding that
a hospital policy authorizing “nonconsensual, warrantless,
and suspicionless searches” contravened the Fourth
Amendment); Payton v. New York, 445 U. S. 573, 574, 576
(1980) (holding that a New York statute “authoriz[ing]
police officers to enter a private residence without a war-
rant and with force, if necessary, to make a routine felony
                 Cite as: 576 U. S. ____ (2015)           7

                     Opinion of the Court

arrest” was “not consistent with the Fourth Amendment”);
Torres v. Puerto Rico, 442 U. S. 465, 466, 471 (1979) (hold-
ing that a Puerto Rico statute authorizing “police to search
the luggage of any person arriving in Puerto Rico from the
United States” was unconstitutional because it failed to
require either probable cause or a warrant).

                              B
   Petitioner principally contends that facial challenges to
statutes authorizing warrantless searches must fail be-
cause such searches will never be unconstitutional in all
applications. Cf. Salerno, 481 U. S., at 745 (to obtain
facial relief the party seeking it “must establish that no
set of circumstances exists under which the [statute]
would be valid”). In particular, the City points to situa-
tions where police are responding to an emergency, where
the subject of the search consents to the intrusion, and
where police are acting under a court-ordered warrant.
See Brief for Petitioner 19–20. While petitioner frames
this argument as an objection to respondents’ challenge in
this case, its logic would preclude facial relief in every
Fourth Amendment challenge to a statute authorizing
warrantless searches. For this reason alone, the City’s
argument must fail: The Court’s precedents demonstrate
not only that facial challenges to statutes authorizing
warrantless searches can be brought, but also that they
can succeed. See Part II–A, supra.
   Moreover, the City’s argument misunderstands how
courts analyze facial challenges. Under the most exacting
standard the Court has prescribed for facial challenges, a
plaintiff must establish that a “law is unconstitutional in
all of its applications.” Washington State Grange v. Wash-
ington State Republican Party, 552 U. S. 442, 449 (2008).
But when assessing whether a statute meets this stand-
ard, the Court has considered only applications of the
8                      LOS ANGELES v. PATEL

                          Opinion of the Court

statute in which it actually authorizes or prohibits con-
duct. For instance, in Planned Parenthood of Southeast-
ern Pa. v. Casey, 505 U. S. 833 (1992), the Court struck
down a provision of Pennsylvania’s abortion law that
required a woman to notify her husband before obtaining
an abortion. Those defending the statute argued that
facial relief was inappropriate because most women volun-
tarily notify their husbands about a planned abortion and
for them the law would not impose an undue burden. The
Court rejected this argument, explaining: The
“[l]egislation is measured for consistency with the Consti-
tution by its impact on those whose conduct it affects. . . .
The proper focus of the constitutional inquiry is the group
for whom the law is a restriction, not the group for whom
the law is irrelevant.” Id., at 894.
   Similarly, when addressing a facial challenge to a stat-
ute authorizing warrantless searches, the proper focus of
the constitutional inquiry is searches that the law actually
authorizes, not those for which it is irrelevant. If exigency
or a warrant justifies an officer’s search, the subject of the
search must permit it to proceed irrespective of whether it
is authorized by statute. Statutes authorizing warrantless
searches also do no work where the subject of a search has
consented. Accordingly, the constitutional “applications”
that petitioner claims prevent facial relief here are irrele-
vant to our analysis because they do not involve actual
applications of the statute.1
——————
  1 Relatedly, the United States claims that a statute authorizing war-

rantless searches may still have independent force if it imposes a
penalty for failing to cooperate in a search conducted under a warrant
or in an exigency. See Brief for United States as Amicus Curiae 19.
This argument gets things backwards. An otherwise facially unconsti-
tutional statute cannot be saved from invalidation based solely on the
existence of a penalty provision that applies when searches are not
actually authorized by the statute. This argument is especially uncon-
vincing where, as here, an independent obstruction of justice statute
imposes a penalty for “willfully, resist[ing], delay[ing], or obstruct[ing]
                     Cite as: 576 U. S. ____ (2015)                      9

                          Opinion of the Court

                             III
  Turning to the merits of the particular claim before us,
we hold that §41.49(3)(a) is facially unconstitutional be-
cause it fails to provide hotel operators with an opportu-
nity for precompliance review.
                             A
  The Fourth Amendment protects “[t]he right of the
people to be secure in their persons, houses, papers, and
effects, against unreasonable searches and seizures.” It
further provides that “no Warrants shall issue, but upon
probable cause.” Based on this constitutional text, the
Court has repeatedly held that “ ‘searches conducted out-
side the judicial process, without prior approval by [a]
judge or [a] magistrate [judge], are per se unreasonable . . .
subject only to a few specifically established and well-
delineated exceptions.’ ” Arizona v. Gant, 556 U. S. 332,
338 (2009) (quoting Katz v. United States, 389 U. S. 347,
357 (1967)). This rule “applies to commercial premises as
well as to homes.” Marshall v. Barlow’s, Inc., 436 U. S.
307, 312 (1978).
  Search regimes where no warrant is ever required may
be reasonable where “ ‘special needs . . . make the warrant
and probable-cause requirement impracticable,’ ” Skinner,
489 U. S., at 619 (quoting Griffin v. Wisconsin, 483 U. S.
868, 873 (1987) (some internal quotation marks omitted)),
and where the “primary purpose” of the searches is
“[d]istinguishable from the general interest in crime con-
trol,” Indianapolis v. Edmond, 531 U. S. 32, 44 (2000).
Here, we assume that the searches authorized by §41.49
serve a “special need” other than conducting criminal
investigations: They ensure compliance with the record-

—————— 

any public officer . . . in the discharge or attempt to discharge any duty

of his or her office of employment.” Cal. Penal Code Ann. §148(a)(1)

(West 2014).

10                    LOS ANGELES v. PATEL

                         Opinion of the Court

keeping requirement, which in turn deters criminals from
operating on the hotels’ premises.2 The Court has referred
to this kind of search as an “administrative searc[h].”
Camara v. Municipal Court of City and County of San
Francisco, 387 U. S. 523, 534 (1967). Thus, we consider
whether §41.49 falls within the administrative search
exception to the warrant requirement.
   The Court has held that absent consent, exigent circum-
stances, or the like, in order for an administrative search
to be constitutional, the subject of the search must be
afforded an opportunity to obtain precompliance review
before a neutral decisionmaker. See See, 387 U. S., at 545;
Lone Steer, 464 U. S., at 415 (noting that an administra-
tive search may proceed with only a subpoena where the
subpoenaed party is sufficiently protected by the oppor-
tunity to “question the reasonableness of the subpoena,
before suffering any penalties for refusing to comply with
it, by raising objections in an action in district court”).
And, we see no reason why this minimal requirement is
inapplicable here. While the Court has never attempted to
prescribe the exact form an opportunity for precompliance
review must take, the City does not even attempt to argue
that §41.49(3)(a) affords hotel operators any opportunity
whatsoever. Section 41.49(3)(a) is, therefore, facially
invalid.
   A hotel owner who refuses to give an officer access to his
or her registry can be arrested on the spot. The Court has
held that business owners cannot reasonably be put to this
kind of choice. Camara, 387 U. S., at 533 (holding that
“broad statutory safeguards are no substitute for individ-
ualized review, particularly when those safeguards may
——————
  2 Respondents contend that §41.49’s principal purpose instead is to

facilitate criminal investigation. Brief for Respondents 44–47. Because
we find that the searches authorized by §41.49 are unconstitutional
even if they serve the City’s asserted purpose, we decline to address
this argument.
                 Cite as: 576 U. S. ____ (2015)          11

                     Opinion of the Court

only be invoked at the risk of a criminal penalty”). Absent
an opportunity for precompliance review, the ordinance
creates an intolerable risk that searches authorized by it
will exceed statutory limits, or be used as a pretext to
harass hotel operators and their guests. Even if a hotel
has been searched 10 times a day, every day, for three
months, without any violation being found, the operator
can only refuse to comply with an officer’s demand to turn
over the registry at his or her own peril.
  To be clear, we hold only that a hotel owner must be
afforded an opportunity to have a neutral decisionmaker
review an officer’s demand to search the registry before he
or she faces penalties for failing to comply. Actual review
need only occur in those rare instances where a hotel
operator objects to turning over the registry. Moreover,
this opportunity can be provided without imposing oner-
ous burdens on those charged with an administrative
scheme’s enforcement. For instance, respondents accept
that the searches authorized by §41.49(3)(a) would be
constitutional if they were performed pursuant to an
administrative subpoena. Tr. of Oral Arg. 36–37. These
subpoenas, which are typically a simple form, can be
issued by the individual seeking the record—here, officers
in the field—without probable cause that a regulation is
being infringed. See See, 387 U. S., at 544 (“[T]he demand
to inspect may be issued by the agency”). Issuing a sub-
poena will usually be the full extent of an officer’s burden
because “the great majority of businessmen can be ex-
pected in normal course to consent to inspection without
warrant.” Barlow’s, Inc., 436 U. S., at 316. Indeed, the
City has cited no evidence suggesting that without an
ordinance authorizing on-demand searches, hotel opera-
tors would regularly refuse to cooperate with the police.
  In those instances, however, where a subpoenaed hotel
operator believes that an attempted search is motivated
by illicit purposes, respondents suggest it would be suffi-
12                    LOS ANGELES v. PATEL

                         Opinion of the Court

cient if he or she could move to quash the subpoena before
any search takes place. Tr. of Oral Arg. 38–39. A neutral
decisionmaker, including an administrative law judge,
would then review the subpoenaed party’s objections
before deciding whether the subpoena is enforceable.
Given the limited grounds on which a motion to quash can
be granted, such challenges will likely be rare. And, in the
even rarer event that an officer reasonably suspects that a
hotel operator may tamper with the registry while the
motion to quash is pending, he or she can guard the regis-
try until the required hearing can occur, which ought not
take long. Riley v. California, 573 U. S. ___ (2014) (slip
op., at 12) (police may seize and hold a cell phone “to
prevent destruction of evidence while seeking a warrant”);
Illinois v. McArthur, 531 U. S. 326, 334 (2001) (citing
cases upholding the constitutionality of “temporary re-
straints where [they are] needed to preserve evidence until
police could obtain a warrant”). Cf. Missouri v. McNeely,
569 U. S. ___ (2013) (slip op., at 12) (noting that many
States have procedures in place for considering warrant
applications telephonically).3
   Procedures along these lines are ubiquitous. A 2002
report by the Department of Justice “identified
approximately 335 existing administrative subpoena
authorities held by various [federal] executive branch
entities.” Office of Legal Policy, Report to Congress
on the Use of Administrative Subpoena Authorities by
Executive Branch Agencies and Entities 3, online
at http://www.justice.gov/archive/olp/rpt_to_congress.htm
(All Internet materials as visited June 19, 2015, and
available in Clerk of Court’s case file). Their prevalence
——————
  3 JUSTICE SCALIA professes to be baffled at the idea that we could

suggest that in certain circumstances, police officers may seize some-
thing that they cannot immediately search. Post, at 10–11 (dissenting
opinion). But that is what this Court’s cases have explicitly endorsed,
including Riley just last Term.
                    Cite as: 576 U. S. ____ (2015)                13

                        Opinion of the Court

confirms what common sense alone would otherwise lead
us to conclude: In most contexts, business owners can be
afforded at least an opportunity to contest an administra-
tive search’s propriety without unduly compromising the
government’s ability to achieve its regulatory aims.
   Of course administrative subpoenas are only one way in
which an opportunity for precompliance review can be
made available. But whatever the precise form, the avail-
ability of precompliance review alters the dynamic be-
tween the officer and the hotel to be searched, and reduces
the risk that officers will use these administrative searches
as a pretext to harass business owners.
   Finally, we underscore the narrow nature of our hold-
ing. Respondents have not challenged and nothing in our
opinion calls into question those parts of §41.49 that re-
quire hotel operators to maintain guest registries contain-
ing certain information. And, even absent legislative
action to create a procedure along the lines discussed
above, see supra, at 11, police will not be prevented from
obtaining access to these documents. As they often do,
hotel operators remain free to consent to searches of their
registries and police can compel them to turn them over
if they have a proper administrative warrant—including
one that was issued ex parte—or if some other exception
to the warrant requirement applies, including exigent
circumstances.4
                          B
  Rather than arguing that §41.49(3)(a) is constitutional

——————
  4 In suggesting that our holding today will somehow impede law en-

forcement from achieving its important aims, JUSTICE SCALIA relies on
instances where hotels were used as “prisons for migrants smuggled
across the border and held for ransom” or as “rendezvous sites where
child sex workers meet their clients on threat of violence from their
procurers.” See post, at 2. It is hard to imagine circumstances more
exigent than these.
14                     LOS ANGELES v. PATEL

                          Opinion of the Court

under the general administrative search doctrine, the City
and JUSTICE SCALIA contend that hotels are “closely regu-
lated,” and that the ordinance is facially valid under the
more relaxed standard that applies to searches of this
category of businesses. Brief for Petitioner 28–47; post, at
5. They are wrong on both counts.
  Over the past 45 years, the Court has identified only
four industries that “have such a history of government
oversight that no reasonable expectation of privacy . . .
could exist for a proprietor over the stock of such an en-
terprise,” Barlow’s, Inc., 436 U. S., 313. Simply listing
these industries refutes petitioner’s argument that hotels
should be counted among them. Unlike liquor sales, Col-
onnade Catering Corp. v. United States, 397 U. S. 72
(1970), firearms dealing, United States v. Biswell, 406
U. S. 311, 311–312 (1972), mining, Donovan v. Dewey, 452
U. S. 594 (1981), or running an automobile junkyard, New
York v. Burger, 482 U. S. 691 (1987), nothing inherent in
the operation of hotels poses a clear and significant risk to
the public welfare. See, e.g., id., at 709 (“Automobile
junkyards and vehicle dismantlers provide the major
market for stolen vehicles and vehicle parts”); Dewey, 452
U. S., at 602 (describing the mining industry as “among
the most hazardous in the country”).5
  Moreover, “[t]he clear import of our cases is that the
closely regulated industry . . . is the exception.” Barlow’s,
Inc., 436 U. S., at 313. To classify hotels as pervasively
regulated would permit what has always been a narrow
exception to swallow the rule. The City wisely refrains
from arguing that §41.49 itself renders hotels closely
regulated. Nor do any of the other regulations on which
——————
  5 JUSTICE SCALIA’s effort to depict hotels as raising a comparable de-

gree of risk rings hollow. See post, at 1, 14. Hotels—like practically all
commercial premises or services—can be put to use for nefarious ends.
But unlike the industries that the Court has found to be closely regu-
lated, hotels are not intrinsically dangerous.
                 Cite as: 576 U. S. ____ (2015)          15

                     Opinion of the Court

petitioner and JUSTICE SCALIA rely—regulations requiring
hotels to, inter alia, maintain a license, collect taxes,
conspicuously post their rates, and meet certain sanitary
standards—establish a comprehensive scheme of regula-
tion that distinguishes hotels from numerous other busi-
nesses. See Brief for Petitioner 33–34 (citing regulations);
post, at 7 (same). All businesses in Los Angeles need a
license to operate. LAMC §§21.03(a), 21.09(a). While
some regulations apply to a smaller set of businesses, see
e.g. Cal. Code Regs., tit. 25, §40 (2015) (requiring linens
to be changed between rental guests), online at
http://www.oal.ca.gov/ccr.htm, these can hardly be said to
have created a “ ‘comprehensive’ ” scheme that puts hotel
owners on notice that their “ ‘property will be subject to
periodic inspections undertaken for specific purposes,’ ”
Burger, 482 U. S., at 705, n. 16 (quoting Dewey, 452 U. S.,
at 600). Instead, they are more akin to the widely appli-
cable minimum wage and maximum hour rules that the
Court rejected as a basis for deeming “the entirety of
American interstate commerce” to be closely regulated in
Barlow’s, Inc. 436 U. S., at 314. If such general regula-
tions were sufficient to invoke the closely regulated indus-
try exception, it would be hard to imagine a type of busi-
ness that would not qualify. See Brief for Google Inc. as
Amicus Curiae 16–17; Brief for the Chamber of Commerce
of United States of America as Amicus Curiae 12–13.
   Petitioner attempts to recast this hodgepodge of reg-
ulations as a comprehensive scheme by referring to a
“centuries-old tradition” of warrantless searches of hotels.
Brief for Petitioner 34–36. History is relevant when deter-
mining whether an industry is closely regulated. See,
e.g., Burger, 482 U. S., at 707. The historical record here,
however, is not as clear as petitioner suggests. The City
and JUSTICE SCALIA principally point to evidence that
hotels were treated as public accommodations. Brief for
Petitioner 34–36; post, at 5–6, and n. 1. For instance, the
16                 LOS ANGELES v. PATEL

                     Opinion of the Court

Commonwealth of Massachusetts required innkeepers to
“ ‘furnish[ ] . . . suitable provisions and lodging, for the
refreshment and entertainment of strangers and travel-
lers, pasturing and stable room, hay and provender . . . for
their horses and cattle.’ ” Brief for Petitioner 35 (quoting
An Act For The Due Regulation Of Licensed Houses
(1786), reprinted in Acts and Laws of the Commonwealth
of Massachusetts 209 (1893)). But laws obligating inns to
provide suitable lodging to all paying guests are not the
same as laws subjecting inns to warrantless searches.
Petitioner also asserts that “[f]or a long time, [hotel] own-
ers left their registers open to widespread inspection.”
Brief for Petitioner 51. Setting aside that modern hotel
registries contain sensitive information, such as driver’s
licenses and credit card numbers for which there is no
historic analog, the fact that some hotels chose to make
registries accessible to the public has little bearing on
whether government authorities could have viewed these
documents on demand without a hotel’s consent.
    Even if we were to find that hotels are pervasively
regulated, §41.49 would need to satisfy three additional
criteria to be reasonable under the Fourth Amendment:
(1) “[T]here must be a ‘substantial’ government interest
that informs the regulatory scheme pursuant to which the
inspection is made”; (2) “the warrantless inspections must
be ‘necessary’ to further [the] regulatory scheme”; and (3)
“the statute’s inspection program, in terms of the certainty
and regularity of its application, [must] provid[e] a consti-
tutionally adequate substitute for a warrant.” Burger, 482
U. S., at 702–703 (internal quotation marks omitted). We
assume petitioner’s interest in ensuring that hotels main-
tain accurate and complete registries might fulfill the first
of these requirements, but conclude that §41.49 fails the
second and third prongs of this test.
    The City claims that affording hotel operators any op-
portunity for precompliance review would fatally under-
                 Cite as: 576 U. S. ____ (2015)           17

                     Opinion of the Court

mine the scheme’s efficacy by giving operators a chance to
falsify their records. Brief for Petitioner 41–42. The
Court has previously rejected this exact argument, which
could be made regarding any recordkeeping requirement.
See Barlow’s, Inc., 436 U. S., at 320 (“[It is not] apparent
why the advantages of surprise would be lost if, after
being refused entry, procedures were available for the
[Labor] Secretary to seek an ex parte warrant to reappear
at the premises without further notice to the establish-
ment being inspected”); cf. Lone Steer, 464 U. S., at 411,
415 (affirming use of administrative subpoena which
provided an opportunity for precompliance review as a
means for obtaining “payroll and sales records”). We see
no reason to accept it here.
  As explained above, nothing in our decision today pre-
cludes an officer from conducting a surprise inspection by
obtaining an ex parte warrant or, where an officer reason-
ably suspects the registry would be altered, from guarding
the registry pending a hearing on a motion to quash. See
Barlow’s, Inc., 436 U. S., at 319–321; Riley, 573 U. S., at
___ (slip op., at 12). JUSTICE SCALIA’s claim that these
procedures will prove unworkable given the large number
of hotels in Los Angeles is a red herring. See post, at 11.
While there are approximately 2,000 hotels in Los Ange-
les, ibid., there is no basis to believe that resort to such
measures will be needed to conduct spot checks in the vast
majority of them. See supra, at 11.
  Section 41.49 is also constitutionally deficient under the
“certainty and regularity” prong of the closely regulated
industries test because it fails sufficiently to constrain
police officers’ discretion as to which hotels to search and
under what circumstances. While the Court has upheld
inspection schemes of closely regulated industries that
called for searches at least four times a year, Dewey, 452
U. S., at 604, or on a “regular basis,” Burger, 482 U. S., at
711, §41.49 imposes no comparable standard.
18                 LOS ANGELES v. PATEL

                      Opinion of the Court

                       *     *     *
   For the foregoing reasons, we agree with the Ninth
Circuit that §41.49(3)(a) is facially invalid insofar as it
fails to provide any opportunity for precompliance review
before a hotel must give its guest registry to the police for
inspection. Accordingly, the judgment of the Ninth Circuit
is affirmed.
                                             It is so ordered.
                 Cite as: 576 U. S. ____ (2015)            1

                     SCALIA, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 13–1175
                         _________________


 CITY OF LOS ANGELES, CALIFORNIA, PETITIONER
          v. NARANJIBHAI PATEL, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE NINTH CIRCUIT

                        [June 22, 2015] 


   JUSTICE SCALIA, with whom THE CHIEF JUSTICE and
JUSTICE THOMAS join, dissenting.
   The city of Los Angeles, like many jurisdictions across
the country, has a law that requires motels, hotels, and
other places of overnight accommodation (hereinafter
motels) to keep a register containing specified information
about their guests. Los Angeles Municipal Code (LAMC)
§41.49(2) (2015). The purpose of this recordkeeping re-
quirement is to deter criminal conduct, on the theory that
criminals will be unwilling to carry on illicit activities in
motel rooms if they must provide identifying information
at check-in. Because this deterrent effect will only be
accomplished if motels actually do require guests to pro-
vide the required information, the ordinance also author-
izes police to conduct random spot checks of motels’ guest
registers to ensure that they are properly maintained.
§41.49(3). The ordinance limits these spot checks to the
four corners of the register, and does not authorize police
to enter any nonpublic area of the motel. To the extent
possible, police must conduct these spot checks at times
that will minimize any disruption to a motel’s business.
   The parties do not dispute the governmental interests at
stake. Motels not only provide housing to vulnerable
transient populations, they are also a particularly attrac-
tive site for criminal activity ranging from drug dealing
2                  LOS ANGELES v. PATEL

                     SCALIA, J., dissenting

and prostitution to human trafficking. Offering privacy
and anonymity on the cheap, they have been employed
as prisons for migrants smuggled across the border and
held for ransom, see Sanchez, Immigrant Smugglers Be-
come More Ruthless, Washington Post, June 28, 2004,
p. A3; Wagner, Human Smuggling, Arizona Republic,
July 23, 2006, p. A1, and rendezvous sites where child sex
workers meet their clients on threat of violence from their
procurers.
   Nevertheless, the Court today concludes that Los Ange-
les’s ordinance is “unreasonable” inasmuch as it permits
police to flip through a guest register to ensure it is being
filled out without first providing an opportunity for the
motel operator to seek judicial review. Because I believe
that such a limited inspection of a guest register is emi-
nently reasonable under the circumstances presented, I
dissent.
                               I
   I assume that respondents may bring a facial challenge
to the City’s ordinance under the Fourth Amendment.
Even so, their claim must fail because, as discussed infra,
the law is constitutional in most, if not all, of its applica-
tions. See United States v. Salerno, 481 U. S. 739, 751
(1987). But because the Court discusses the propriety of a
facial challenge at some length, I offer a few thoughts.
   Article III limits our jurisdiction to “Cases” and “Con-
troversies.” Accordingly, “[f]ederal courts may not ‘decide
questions that cannot affect the rights of litigants in the
case before them’ or give ‘opinion[s] advising what the law
would be upon a hypothetical state of facts.’ ” Chafin v.
Chafin, 568 U. S. ___, ___ (2013) (slip op., at 5). To be
sure, the reasoning of a decision may suggest that there is
no permissible application of a particular statute, Chicago
v. Morales, 527 U. S. 41, 77 (1999) (SCALIA, J., dissenting),
and under the doctrine of stare decisis, this reasoning—to
                  Cite as: 576 U. S. ____ (2015)            3

                      SCALIA, J., dissenting

the extent that it is necessary to the holding—will be
binding in all future cases. But in this sense, the facial
invalidation of a statute is a logical consequence of the
Court’s opinion, not the immediate effect of its judgment.
Although we have at times described our holdings as
invalidating a law, it is always the application of a law,
rather than the law itself, that is before us.
  The upshot is that the effect of a given case is a function
not of the plaintiff ’s characterization of his challenge, but
the narrowness or breadth of the ground that the Court
relies upon in disposing of it. If a plaintiff elects not to
present any case-specific facts in support of a claim that a
law is unconstitutional—as is the case here—he will limit
the grounds on which a Court may find for him to highly
abstract rules that would have broad application in future
cases. The decision to do this might be a poor strategic
move, especially in a Fourth Amendment case, where the
reasonableness of a search is a highly factbound question
and general, abstract rules are hard to come by. Cf.
Sibron v. New York, 392 U. S. 40, 59 (1968). But even had
the plaintiffs in this case presented voluminous facts in a
self-styled as-applied challenge, nothing would force this
Court to rely upon those facts rather than the broader
principle that the Court has chosen to rely upon. I see no
reason why a plaintiff ’s self-description of his challenge as
facial would provide an independent reason to reject it
unless we were to delegate to litigants our duty to say
what the law is.
                             II
   The Fourth Amendment provides, in relevant part, that
“[t]he right of the people to be secure in their persons,
houses, papers, and effects, against unreasonable searches
and seizures, shall not be violated, and no Warrants shall
issue, but upon probable cause.” Grammatically, the two
clauses of the Amendment seem to be independent—and
4                  LOS ANGELES v. PATEL

                     SCALIA, J., dissenting

directed at entirely different actors. The former tells the
executive what it must do when it conducts a search, and
the latter tells the judiciary what it must do when it issues
a search warrant. But in an effort to guide courts in ap-
plying the Search-and-Seizure Clause’s indeterminate
reasonableness standard, and to maintain coherence in
our case law, we have used the Warrant Clause as a
guidepost for assessing the reasonableness of a search,
and have erected a framework of presumptions applicable
to broad categories of searches conducted by executive
officials. Our case law has repeatedly recognized, how-
ever, that these are mere presumptions, and the only consti-
tutional requirement is that a search be reasonable.
  When, for example, a search is conducted to enforce an
administrative regime rather than to investigate criminal
wrongdoing, we have been willing to modify the probable-
cause standard so that a warrant may issue absent indi-
vidualized suspicion of wrongdoing. Thus, our cases say a
warrant may issue to inspect a structure for fire-code
violations on the basis of such factors as the passage of
time, the nature of the building, and the condition of the
neighborhood. Camara v. Municipal Court of City and
County of San Francisco, 387 U. S. 523, 538–539 (1967).
As we recognized in that case, “reasonableness is still the
ultimate standard. If a valid public interest justifies the
intrusion contemplated, then there is probable cause to
issue a suitably restricted search warrant.” Id., at 539.
And precisely “because the ultimate touchstone of the
Fourth Amendment is ‘reasonableness,’ ” even the pre-
sumption that the search of a home without a warrant is
unreasonable “is subject to certain exceptions.” Brigham
City v. Stuart, 547 U. S. 398, 403 (2006).
  One exception to normal warrant requirements applies
to searches of closely regulated businesses. “[W]hen an
entrepreneur embarks upon such a business, he has vol-
untarily chosen to subject himself to a full arsenal of
                 Cite as: 576 U. S. ____ (2015)           5

                     SCALIA, J., dissenting

governmental regulation,” and so a warrantless search to
enforce those regulations is not unreasonable. Marshall v.
Barlow’s, Inc., 436 U. S. 307, 313 (1978). Recognizing that
warrantless searches of closely regulated businesses may
nevertheless become unreasonable if arbitrarily conducted,
we have required laws authorizing such searches to satisfy
three criteria: (1) There must be a “ ‘substantial’ govern-
ment interest that informs the regulatory scheme pursu-
ant to which the inspection is made”; (2) “the warrantless
inspections must be ‘necessary to further [the] regulatory
scheme’ ”; and (3) “ ‘the statute’s inspection program, in
terms of the certainty and regularity of its application,
[must] provid[e] a constitutionally adequate substitute for
a warrant.’ ” New York v. Burger, 482 U. S. 691, 702–703
(1987).
  Los Angeles’s ordinance easily meets these standards.
                              A
   In determining whether a business is closely regulated,
this Court has looked to factors including the duration of
the regulatory tradition, id., at 705–707, Colonnade Cater-
ing Corp. v. United States, 397 U. S. 72, 75–77 (1970),
Donovan v. Dewey, 452 U. S. 594, 606 (1981); the compre-
hensiveness of the regulatory regime, Burger, supra, at
704–705, Dewey, supra, at 606; and the imposition of
similar regulations by other jurisdictions, Burger, supra,
at 705. These factors are not talismans, but shed light on
the expectation of privacy the owner of a business may
reasonably have, which in turn affects the reasonableness
of a warrantless search. See Barlow’s, supra, at 313.
   Reflecting the unique public role of motels and their
commercial forebears, governments have long subjected
these businesses to unique public duties, and have estab-
lished inspection regimes to ensure compliance. As Black-
stone observed, “Inns, in particular, being intended for the
lodging and receipt of travellers, may be indicted, sup-
6                      LOS ANGELES v. PATEL

                          SCALIA, J., dissenting

pressed, and the inn-keepers fined, if they refuse to enter-
tain a traveller without a very sufficient cause: for thus to
frustrate the end of their institution is held to be disorderly
behavior.” 4 W. Blackstone, Commentaries on the Laws
of England 168 (1765). Justice Story similarly recognized
“[t]he soundness of the public policy of subjecting particu-
lar classes of persons to extraordinary responsibility, in
cases where an extraordinary confidence is necessarily
reposed in them, and there is an extraordinary temptation
to fraud, or danger of plunder.” J. Story, Commentaries
on the Law of Bailments §464, pp. 487–488 (5th ed. 1851).
Accordingly, in addition to the obligation to receive any
paying guest, “innkeepers are bound to take, not merely
ordinary care, but uncommon care, of the goods, money,
and baggage of their guests,” id., §470, at 495, as travel-
lers “are obliged to rely almost implicitly on the good faith
of innholders, whose education and morals are none of the
best, and who might have frequent opportunities of asso-
ciating with ruffians and pilferers,” id., §471, at 498.
   These obligations were not merely aspirational. At the
time of the founding, searches—indeed, warrantless
searches—of inns and similar places of public accommoda-
tion were commonplace. For example, although Massa-
chusetts was perhaps the State most protective against
government searches, “the state code of 1788 still allowed
tithingmen to search public houses of entertainment on
every Sabbath without any sort of warrant.” W. Cuddihy,
Fourth Amendment: Origins and Original Meaning 602–
1791, 743 (2009).1
   As this evidence demonstrates, the regulatory tradition
governing motels is not only longstanding, but comprehen-
——————
  1 As Beale helpfully confirms, “[f ]rom the earliest times the funda-

mental characteristic of an inn has been its public nature. It is a public
house, a house of public entertainment, or, as it is legally phrased, a
common inn.” J. Beale, The Law of Innkeepers and Hotels §11, p. 10
(1906).
                  Cite as: 576 U. S. ____ (2015)             7

                      SCALIA, J., dissenting

sive. And the tradition continues in Los Angeles. The
City imposes an occupancy tax upon transients who stay
in motels, LAMC §21.7.3, and makes the motel owner
responsible for collecting it, §21.7.5. It authorizes city
officials “to enter [a motel], free of charge, during business
hours” in order to “inspect and examine” them to deter-
mine whether these tax provisions have been complied
with. §§21.7.9, 21.15. It requires all motels to obtain a
“Transient Occupancy Registration Certificate,” which
must be displayed on the premises. §21.7.6. State law
requires motels to “post in a conspicuous place . . . a
statement of rate or range of rates by the day for lodging,”
and forbids any charges in excess of those posted rates.
Cal. Civ. Code Ann. §1863 (West 2010). Hotels must
change bed linens between guests, Cal. Code Regs., tit. 25,
§40 (2015), and they must offer guests the option not to
have towels and linens laundered daily, LAMC §121.08.
“Multiuse drinking utensils” may be placed in guest rooms
only if they are “thoroughly washed and sanitized after
each use” and “placed in protective bags.” Cal. Code Regs.,
tit. 17, §30852. And state authorities, like their municipal
counterparts, “may at reasonable times enter and inspect
any hotels, motels, or other public places” to ensure com-
pliance. §30858.
   The regulatory regime at issue here is thus substan-
tially more comprehensive than the regulations governing
junkyards in Burger, where licensing, inventory-recording,
and permit-posting requirements were found sufficient to
qualify the industry as closely regulated. 482 U. S., at
704–705. The Court’s suggestion that these regulations
are not sufficiently targeted to motels, and are “akin to . . .
minimum wage and maximum hour rules,” ante, at 15, is
simply false. The regulations we have described above
reach into the “minutest detail[s]” of motel operations,
Barlow’s, supra, at 314, and those who enter that business
today (like those who have entered it over the centuries)
8                 LOS ANGELES v. PATEL

                     SCALIA, J., dissenting

do so with an expectation that they will be subjected to
especially vigilant governmental oversight.
   Finally, this ordinance is not an outlier. The City has
pointed us to more than 100 similar register-inspection
laws in cities and counties across the country, Brief for
Petitioner 36, and n. 3, and that is far from exhaustive. In
all, municipalities in at least 41 States have laws similar
to Los Angeles’s, Brief for National League of Cities et al.
as Amici Curiae 16–17, and at least 8 States have their
own laws authorizing register inspections, Brief for Cali-
fornia et al. as Amici Curiae 12–13.
   This copious evidence is surely enough to establish that
“[w]hen a [motel operator] chooses to engage in this perva-
sively regulated business . . . he does so with the
knowledge that his business records . . . will be subject to
effective inspection.” United States v. Biswell, 406 U. S.
311, 316 (1972). And that is the relevant constitutional
test—not whether this regulatory superstructure is “the
same as laws subjecting inns to warrantless searches,” or
whether, as an historical matter, government authorities
not only required these documents to be kept but permit-
ted them to be viewed on demand without a motel’s con-
sent. Ante, at 16.
   The Court’s observation that “[o]ver the past 45 years,
the Court has identified only four industries” as closely
regulated, ante, at 14, is neither here nor there. Since we
first concluded in Colonnade Catering that warrantless
searches of closely regulated businesses are reasonable,
we have only identified one industry as not closely regu-
lated, see Barlow’s, 436 U. S., at 313–314. The Court’s
statistic thus tells us more about how this Court exercises
its discretionary review than it does about the number of
industries that qualify as closely regulated. At the same
time, lower courts, which do not have the luxury of picking
the cases they hear, have identified many more businesses
as closely regulated under the test we have announced:
                 Cite as: 576 U. S. ____ (2015)            9

                     SCALIA, J., dissenting

pharmacies, United States v. Gonsalves, 435 F. 3d 64, 67
(CA1 2006); massage parlors, Pollard v. Cockrell, 578
F. 2d 1002, 1014 (CA5 1978); commercial-fishing opera-
tions, United States v. Raub, 637 F. 2d 1205, 1208–1209
(CA9 1980); day-care facilities, Rush v. Obledo, 756 F. 2d
713, 720–721 (CA9 1985); nursing homes, People v. First-
enberg, 92 Cal. App. 3d 570, 578–580, 155 Cal. Rptr. 80,
84–86 (1979); jewelers, People v. Pashigian, 150 Mich.
App. 97, 100–101, 388 N. W. 2d 259, 261–262 (1986) (per
curiam); barbershops, Stogner v. Kentucky, 638 F. Supp. 1,
3 (WD Ky. 1985); and yes, even rabbit dealers, Lesser v.
Espy, 34 F. 3d 1301, 1306–1307 (CA7 1994). Like auto-
mobile junkyards and catering companies that serve alco-
hol, many of these businesses are far from “intrinsically
dangerous,” cf. ante, at 14, n. 5. This should come as no
surprise. The reason closely regulated industries may be
searched without a warrant has nothing to do with the
risk of harm they pose; rather, it has to do with the expec-
tations of those who enter such a line of work. See Bar-
low’s, supra, at 313.
                              B
   The City’s ordinance easily satisfies the remaining
Burger requirements: It furthers a substantial govern-
mental interest, it is necessary to achieving that interest,
and it provides an adequate substitute for a search
warrant.
   Neither respondents nor the Court question the sub-
stantial interest of the City in deterring criminal activity.
See Brief for Respondents 34–41; ante, at 15. The private
pain and public costs imposed by drug dealing, prostitu-
tion, and human trafficking are beyond contention, and
motels provide an obvious haven for those who trade in
human misery.
   Warrantless inspections are also necessary to advance
this interest. Although the Court acknowledges that law
10                LOS ANGELES v. PATEL

                     SCALIA, J., dissenting

enforcement can enter a motel room without a warrant
when exigent circumstances exist, see ante, at 13, n. 4, the
whole reason criminals use motel rooms in the first place
is that they offer privacy and secrecy, so that police will
never come to discover these exigencies. The recordkeep-
ing requirement, which all parties admit is permissible,
therefore operates by deterring crime. Criminals, who
depend on the anonymity that motels offer, will balk when
confronted with a motel’s demand that they produce iden-
tification. And a motel’s evasion of the recordkeeping
requirement fosters crime. In San Diego, for example,
motel owners were indicted for collaborating with mem-
bers of the Crips street gang in the prostitution of under-
age girls; the motel owners “set aside rooms apart from
the rest of their legitimate customers where girls and
women were housed, charged the gang members/pimps a
higher rate for the rooms where ‘dates’ or ‘tricks’ took
place, and warned the gang members of inquiries by law
enforcement.” Office of the Attorney General, Cal. Dept. of
Justice, The State of Human Trafficking in California 25
(2012). The warrantless inspection requirement provides
a necessary incentive for motels to maintain their regis-
ters thoroughly and accurately: They never know when
law enforcement might drop by to inspect.
   Respondents and the Court acknowledge that inspec-
tions are necessary to achieve the purposes of the record-
keeping regime, but insist that warrantless inspections are
not. They have to acknowledge, however, that the motel
operators who conspire with drug dealers and procurers
may demand precompliance judicial review simply as a
pretext to buy time for making fraudulent entries in their
guest registers. The Court therefore must resort to argu-
ing that warrantless inspections are not “necessary” be-
cause other alternatives exist.
   The Court suggests that police could obtain an adminis-
trative subpoena to search a guest register and, if a motel
                     Cite as: 576 U. S. ____ (2015)                   11

                         SCALIA, J., dissenting

moves to quash, the police could “guar[d] the registry
pending a hearing” on the motion. Ante, at 17. This pro-
posal is equal parts 1984 and Alice in Wonderland. It
protects motels from government inspection of their regis-
ters by authorizing government agents to seize the regis-
ters2 (if “guarding” entails forbidding the register to be
moved) or to upset guests by a prolonged police presence
at the motel. The Court also notes that police can obtain
an ex parte warrant before conducting a register inspec-
tion. Ante, at 17. Presumably such warrants could issue
without probable cause of wrongdoing by a particular
motel, see Camara, 387 U. S., at 535–536; otherwise, this
would be no alternative at all. Even so, under this regime
police would have to obtain an ex parte warrant before
every inspection. That is because law enforcement would
have no way of knowing ahead of time which motels would
refuse consent to a search upon request; and if they wait
to obtain a warrant until consent is refused, motels will
have the opportunity to falsify their guest registers while
the police jump through the procedural hoops required to
obtain a warrant. It is quite plausible that the costs of
this always-get-a-warrant “alternative” would be prohibi-
tive for a police force in one of America’s largest cities,
juggling numerous law-enforcement priorities, and con-
fronting more than 2,000 motels within its jurisdiction.
E. Wallace, K. Pollock, B. Horth, S. Carty, & N. El-
yas, Los Angeles Tourism: A Domestic and Interna-
tional Analysis 7 (May 2014 online at http:
//www.lachamber.com/clientuploads/Global_Programs/
WTW/2014/LATourism_LMU_May2014.pdf            (as    visited
June 19, 2015, and available in Clerk of Court’s

——————
  2 We are not at all “baffled at the idea that . . . police officers may
seize something that they cannot immediately search.” Ante, at 12,
n. 3. We are baffled at the idea that anyone would think a seizure of
required records less intrusive than a visual inspection.
12                 LOS ANGELES v. PATEL

                     SCALIA, J., dissenting

 case file). To be sure, the fact that obtaining a warrant
might be costly will not by itself render a warrantless
search reasonable under the Fourth Amendment; but it
can render a warrantless search necessary in the context
of an administrative-search regime governing closely
regulated businesses.
  But all that discussion is in any case irrelevant. The
administrative search need only be reasonable. It is not
the burden of Los Angeles to show that there are no less
restrictive means of achieving the City’s purposes. Se-
questration or ex parte warrants were possible alternatives
to the warrantless search regimes approved by this Court
in Colonnade Catering, Biswell, Dewey, and Burger. By
importing a least-restrictive-means test into Burger’s
Fourth Amendment framework, today’s opinion implicitly
overrules that entire line of cases.
  Finally, the City’s ordinance provides an adequate
substitute for a warrant. Warrants “advise the owner of
the scope and objects of the search, beyond which limits
the inspector is not expected to proceed.” Barlow’s, 436
U. S., at 323. Ultimately, they aim to protect against
“devolv[ing] almost unbridled discretion upon executive
and administrative officers, particularly those in the field,
as to when to search and whom to search.” Ibid.
  Los Angeles’s ordinance provides that the guest register
must be kept in the guest reception or guest check-in area,
or in an adjacent office, and that it “be made available to
any officer of the Los Angeles Police Department for in-
spection. Whenever possible, the inspection shall be con-
ducted at a time and in a manner that minimizes any
interference with the operation of the business.” LAMC
§41.49(3). Nothing in the ordinance authorizes law en-
forcement to enter a nonpublic part of the motel. Compare
this to the statute upheld in Colonnade Catering, which
provided that “ ‘[t]he Secretary or his delegate may enter,
in the daytime, any building or place where any articles or
                 Cite as: 576 U. S. ____ (2015)           13

                     SCALIA, J., dissenting

objects subject to tax are made, produced, or kept, so far as
it may be necessary for the purpose of examining said
articles or objects,’ ” 397 U. S., at 73, n. 2 (quoting 26
U. S. C. §7606(a) (1964 ed.)); or the one in Biswell, which
stated that “ ‘[t]he Secretary may enter during business
hours the premises (including places of storage) of any
firearms or ammunition importer . . . for the purpose of
inspecting or examining (1) any records or documents
required to be kept . . . , and (2) any firearms or ammuni-
tion kept or stored,’ ” 406 U. S., at 312, n. 1 (quoting 18
U. S. C. §923(g) (1970 ed.)); or the one in Dewey, which
granted federal mine inspectors “ ‘a right of entry to, upon,
or through any coal or other mine,’ ” 452 U. S., at 596
(quoting 30 U. S. C. §813(a) (1976 ed., Supp. III)); or the
one in Burger, which compelled junkyard operators to
“ ‘produce such records and permit said agent or police
officer to examine them and any vehicles or parts of vehi-
cles which are subject to the record keeping requirements
of this section and which are on the premises,’ ” 482 U. S.,
at 694, n. 1 (quoting N. Y. Veh. & Traf. Law §415–a5
(McKinney 1986)). The Los Angeles ordinance—which
limits warrantless police searches to the pages of a guest
register in a public part of a motel—circumscribes police
discretion in much more exacting terms than the laws we
have approved in our earlier cases.
   The Court claims that Los Angeles’s ordinance confers
too much discretion because it does not adequately limit
the frequency of searches. Without a trace of irony, the
Court tries to distinguish Los Angeles’s law from the laws
upheld in Dewey and Burger by pointing out that the
latter regimes required inspections at least four times a
year and on a “ ‘regular basis,’ ” respectively. Ante, at 17.
But the warrantless police searches of a business “10
times a day, every day, for three months” that the Court
envisions under Los Angeles’s regime, ante, at 11, are
entirely consistent with the regimes in Dewey and Burger;
14                 LOS ANGELES v. PATEL

                     SCALIA, J., dissenting

10 times a day, every day, is “at least four times a year,”
and on a (much too) “ ‘regular basis.’ ” Ante, at 17.
  That is not to say that the Court’s hypothetical searches
are necessarily constitutional. It is only to say that Los
Angeles’s ordinance presents no greater risk that such a
hypothetical will materialize than the laws we have al-
ready upheld. As in our earlier cases, we should leave it to
lower courts to consider on a case-by-case basis whether
warrantless searches have been conducted in an unrea-
sonably intrusive or harassing manner.
                             III
   The Court reaches its wrongheaded conclusion not
simply by misapplying our precedent, but by mistaking
our precedent for the Fourth Amendment itself. Rather
than bother with the text of that Amendment, the Court
relies exclusively on our administrative-search cases,
Camara, See v. Seattle, 387 U. S. 541 (1967), and Barlow’s.
But the Constitution predates 1967, and it remains the
supreme law of the land today. Although the categorical
framework our jurisprudence has erected in this area may
provide us guidance, it is guidance to answer the constitu-
tional question at issue: whether the challenged search is
reasonable.
   An administrative, warrantless-search ordinance that
narrowly limits the scope of searches to a single business
record, that does not authorize entry upon premises not
open to the public, and that is supported by the need to
prevent fabrication of guest registers, is, to say the least,
far afield from the laws at issue in the cases the Court
relies upon. The Court concludes that such minor intru-
sions, permissible when the police are trying to tamp down
the market in stolen auto parts, are “unreasonable” when
police are instead attempting to stamp out the market in
child sex slaves.
   Because I believe that the limited warrantless searches
               Cite as: 576 U. S. ____ (2015)     15

                   SCALIA, J., dissenting

authorized by Los Angeles’s ordinance are reasonable
under the circumstances, I respectfully dissent.
                 Cite as: 576 U. S. ____ (2015)            1

                     ALITO, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 13–1175
                         _________________


 CITY OF LOS ANGELES, CALIFORNIA, PETITIONER
          v. NARANJIBHAI PATEL, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE NINTH CIRCUIT

                        [June 22, 2015] 


   JUSTICE ALITO, with whom JUSTICE THOMAS joins,
dissenting.
   After today, the city of Los Angeles can never, under any
circumstances, enforce its 116-year-old requirement that
hotels make their registers available to police officers.
That is because the Court holds that §41.49(3)(a) of the
Los Angeles Municipal Code (2015) is facially unconstitu-
tional. Before entering a judgment with such serious
safety and federalism implications, the Court must con-
clude that every application of this law is unconstitu-
tional—i.e., that “ ‘no set of circumstances exists under
which the [law] would be valid.’ ” Ante, at 7 (quoting United
States v. Salerno, 481 U. S. 739, 745 (1987)). I have
doubts about the Court’s approach to administrative
searches and closely regulated industries. Ante, at 9–17.
But even if the Court were 100% correct, it still should
uphold §41.49(3)(a) because many other applications of
this law are constitutional. Here are five examples.
   Example One. The police have probable cause to believe
that a register contains evidence of a crime. They go to a
judge and get a search warrant. The hotel operator, how-
ever, refuses to surrender the register, but instead stashes
it away. Officers could tear the hotel apart looking for it.
Or they could simply order the operator to produce it. The
Fourth Amendment does not create a right to defy a war-
2                   LOS ANGELES v. PATEL

                       ALITO, J., dissenting

rant. Hence §41.49(3)(a) could be constitutionally applied
in this scenario. Indeed, the Court concedes that it is
proper to apply a California obstruction of justice law in
such a case. See ante, at 8–9, n. 1; Brief for Respondents
49. How could applying a city law with a similar effect be
different? No one thinks that overlapping laws are uncon-
stitutional. See, e.g., Yates v. United States, 574 U. S. ___,
___ (2015) (KAGAN, J. dissenting) (slip op., at 10–11)
(“Overlap—even significant overlap—abounds in criminal
law”) (collecting citations). And a specific law gives more
notice than a general law.
  In any event, the Los Angeles ordinance is arguably
broader in at least one important respect than the Califor-
nia obstruction of justice statute on which the Court relies.
Ante, at 8–9, n. 1. The state law applies when a person
“willfully resists, delays, or obstructs any public officer . . .
in the discharge or attempt to discharge any duty of his or
her office.” Cal. Penal Code Ann. §148(a)(1) (West 2014).
In the example set out above, suppose that the hotel oper-
ator, instead of hiding the register, simply refused to tell
the police where it is located. The Court cites no Califor-
nia case holding that such a refusal would be unlawful,
and the city of Los Angeles submits that under California
law, “[o]bstruction statutes prohibit a hotel owner from
obstructing a search, but they do not require affirmative
assistance.” Reply Brief 5. The Los Angeles ordinance, by
contrast, unequivocally requires a hotel operator to make
the register available on request.
  Example Two. A murderer has kidnapped a woman
with the intent to rape and kill her and there is reason to
believe he is holed up in a certain motel. The Fourth
Amendment’s reasonableness standard accounts for exi-
gent circumstances. See, e.g., Brigham City v. Stuart, 547
U. S. 398, 403 (2006). When the police arrive, the motel
operator folds her arms and says the register is locked in a
safe. Invoking §41.49(3)(a), the police order the operator
                 Cite as: 576 U. S. ____ (2015)            3

                     ALITO, J., dissenting

to turn over the register. She refuses. The Fourth
Amendment does not protect her from arrest.
   Example Three. A neighborhood of “pay by the hour”
motels is a notorious gathering spot for child-sex traffick-
ers. Police officers drive through the neighborhood late
one night and see unusual amounts of activity at a partic-
ular motel. The officers stop and ask the motel operator
for the names of those who paid with cash to rent rooms
for less than three hours. The operator refuses to provide
the information. Requesting to see the register—and
arresting the operator for failing to provide it—would be
reasonable under the “totality of the circumstances.” Ohio
v. Robinette, 519 U. S. 33, 39 (1996). In fact, the Court has
upheld a similar reporting duty against a Fourth Amend-
ment challenge where the scope of information required
was also targeted and the public’s interest in crime pre-
vention was no less serious. See California Bankers Assn.
v. Shultz, 416 U. S. 21, 39, n. 15, 66–67 (1974) (having “no
difficulty” upholding a requirement that banks must
provide reports about transactions involving more than
$10,000, including the name, address, occupation, and
social security number of the customer involved, along
with a summary of the transaction, the amount of money
at issue, and the type of identification presented).
   Example Four. A motel is operated by a dishonest
employee. He has been charging more for rooms than he
records, all the while pocketing the difference. The owner
finds out and eagerly consents to a police inspection of the
register. But when officers arrive and ask to see the regis-
ter, the operator hides it. The Fourth Amendment does
not allow the operator’s refusal to defeat the owner’s
consent. See, e.g., Mancusi v. DeForte, 392 U. S. 364, 369–
370 (1968). Accordingly, it would not violate the Fourth
Amendment to arrest the operator for failing to make the
register “available to any officer of the Los Angeles Police
Department for inspection.” §41.49(3)(a).
4                  LOS ANGELES v. PATEL

                     ALITO, J., dissenting

   Example Five. A “mom and pop” motel always keeps its
old-fashioned guest register open on the front desk. Any-
one who wants to can walk up and leaf through it. (Such
motels are not as common as they used to be, but Los
Angeles is a big place.) The motel has no reasonable
expectation of privacy in the register, and no one doubts
that police officers—like anyone else—can enter into the
lobby. See, e.g., Florida v. Jardines, 569 U. S. 1, ___
(2013) (slip op., at 6); Donovan v. Lone Steer, Inc., 464
U. S. 408, 413 (1984). But when an officer starts looking
at the register, as others do, the motel operator at the desk
snatches it away and will not give it back. Arresting that
person would not violate the Fourth Amendment.
   These are just five examples. There are many more.
The Court rushes past examples like these by suggesting
that §41.49(3)(a) does no “work” in such scenarios. Ante,
at 8. That is not true. Under threat of legal sanction, this
law orders hotel operators to do things they do not want to
do. To be sure, there may be circumstances in which
§41.49(3)(a)’s command conflicts with the Fourth Amend-
ment, and in those circumstances the Fourth Amendment
is supreme. See U. S. Const., Art VI, cl. 2. But no differ-
ent from any other local law, the remedy for such circum-
stances should be an as-applied injunction limited to the
conflict with the Fourth Amendment. Such an injunction
would protect a hotel from being “searched 10 times a day,
every day, for three months, without any violation being
found.” Ante, at 11. But unlike facial invalidation, an as-
applied injunction does not produce collateral damage.
Section 41.49(3)(a) should be enforceable in those many
cases in which the Fourth Amendment is not violated.
   There are serious arguments that the Fourth Amend-
ment’s application to warrantless searches and seizures is
inherently inconsistent with facial challenges. See Sibron
v. New York, 392 U. S. 40, 59, 62 (1968) (explaining that
because of the Fourth Amendment’s reasonableness re-
                 Cite as: 576 U. S. ____ (2015)           5

                     ALITO, J., dissenting

quirement, “[t]he constitutional validity of a warrantless
search is pre-eminently the sort of question which can only
be decided in the concrete factual context of the individual
case”); Brief for Manhattan Institute for Policy Research
as Amicus Curiae 33 (“A constitutional claim under the
first clause of the Fourth Amendment is never a ‘facial’
challenge, because it is always and inherently a challenge
to executive action”). But assuming such facial challenges
ever make sense conceptually, this particular one fails
under basic principles of facial invalidation. The Court’s
contrary holding is befuddling. I respectfully dissent.

```

---

## GROUP: content/cases/City of Ontario v. Quon.md  (`case`, 5 assertions)

### content_page

```
---
title: "City of Ontario v. Quon"
type: case
citation: ""
parallel_cite: "177 L. Ed. 2d 216; 130 S. Ct. 2619; 560 U.S. 746; 30 I.E.R. Cas. (BNA) 1345; 78 U.S.L.W. 4591; 22 Fla. L. Weekly Fed. S 470; 93 Empl. Prac. Dec. (CCH) 43,907"
neutral_cite: 2010 U.S. LEXIS 4972
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2010
date_decided: 2010-06-17
docket: 08-1332
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2010-06-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: City of Ontario v. Quon
  varies_by_point: false
  scope_note: "Good law; applies O'Connor v. Ortega to electronic communications. The Court deliberately declined to set broad rules about digital privacy expectations — a caution later echoed in Riley v. California and Carpenter."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/6796843/city-of-ontario-v-quon/"
  cluster_id: 6796843
  opinion_id: 6681698
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Progeny (digital workplace REP)"
related: ["[[O'Connor v. Ortega]]"]
aliases: ["Ontario v. Quon", "City of Ontario, California v. Quon"]
tags: ["case", "fourth-amendment", "special-needs", "workplace", "public-employee", "electronic-communications", "text-messages"]
holding: "A government employer's review of an employee's text messages on an employer-issued pager is a reasonable search where it is motivated by a legitimate work-related purpose and not excessive in scope; the Court assumed a privacy expectation without deciding it, declining to set broad rules for emerging communications technology."
lake:
  record_id: City of Ontario v. Quon
  status: verified
  projected_at: 2026-07-06
---

# City of Ontario v. Quon

*560 U.S. 746 (2010)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Jeff Quon, a police sergeant on the Ontario, California, SWAT team, was issued a city pager with a monthly character allotment. After he repeatedly exceeded the limit and reimbursed the overage fees, the police chief ordered an audit of the message transcripts (obtained from the wireless carrier) to decide whether the character limit was too low for legitimate work use or whether officers were effectively subsidizing personal texting. The audit revealed many personal and sexually explicit messages. Quon sued, claiming the review of his texts violated the Fourth Amendment.

## Issue
Whether a public employer's warrantless review of the contents of an employee's text messages sent on an employer-provided pager was an unreasonable search under the Fourth Amendment.

## Rule
The search is judged by reasonableness under *[[O'Connor v. Ortega]]*. Assuming arguendo that Quon had a privacy expectation and that the review was a search, the audit was reasonable: "Because the search was motivated by a legitimate work-related purpose, and because it was not excessive in scope, the search was reasonable under the approach of the *O'Connor* plurality." — 560 U.S. at 761. ^pin-761

The Court declined to announce broad rules about digital privacy: "The Court must proceed with care when considering the whole concept of privacy expectations in communications made on electronic equipment owned by a government employer. The judiciary risks error by elaborating too fully on the Fourth Amendment implications of emerging technology before its role in society has become clear." — *Id.* at 759. ^pin-759

## Application
The chief ordered the audit for a legitimate, noninvestigatory purpose — to assess whether the City's wireless plan met the SWAT team's work needs — not to expose Quon's private life, so it was justified at its inception. In scope, the review was limited to transcripts of on-duty months and redacted off-duty messages, so it was not excessively intrusive given its purpose. Whether or not Quon had a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the texts (a question the Court left open in light of fast-changing technology), the search was reasonable.

## Conclusion
The review of Quon's pager messages was a reasonable, constitutional search; the Ninth Circuit's contrary judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Quon* extends the [[O'Connor v. Ortega]] reasonableness framework to electronic workplace communications while expressly declining to fix broad digital-privacy rules — the same caution about emerging technology the Court later voiced in *[[Riley v. California]]* and *[[Carpenter v. United States]]*.

## Appears on
- [[Special Needs and Administrative Searches]] — *Progeny (digital workplace REP)*

## Sources
- *City of Ontario v. Quon*, 560 U.S. 746 (2010) — https://www.courtlistener.com/opinion/148797/city-of-ontario-v-quon/ — pinpoints: 759, 761.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "07d22c12c4cf2ca6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2010 U.S. LEXIS 4972", "official_citation_present": false, "parallel_cite": "177 L. Ed. 2d 216; 130 S. Ct. 2619; 560 U.S. 746; 30 I.E.R. Cas. (BNA) 1345; 78 U.S.L.W. 4591; 22 Fla. L. Weekly Fed. S 470; 93 Empl. Prac. Dec. (CCH) 43,907", "title": "City of Ontario v. Quon", "year": "2010"}}
{"assertion_id": "1e1d9ab5a0fa9e50", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Progeny (digital workplace REP)", "title": "City of Ontario v. Quon"}}
{"assertion_id": "21558aad7183d4f4", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A government employer's review of an employee's text messages on an employer-issued pager is a reasonable search where it is motivated by a legitimate work-related purpose and not excessive in scope; the Court assumed a privacy expectation without deciding it, declining to set broad rules for emerging communications technology.", "title": "City of Ontario v. Quon"}}
{"assertion_id": "9a174a6581f2739d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2010-06-17", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "City of Ontario v. Quon", "field_i_validity": "good_law", "scope_note": "Good law; applies O'Connor v. Ortega to electronic communications. The Court deliberately declined to set broad rules about digital privacy expectations — a caution later echoed in Riley v. California and Carpenter.", "title": "City of Ontario v. Quon", "varies_by_point": "false"}}
{"assertion_id": "d6f06a2f2351c4e7", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "City of Ontario v. Quon"}}
```

### lake record — City of Ontario v. Quon

```json
{
  "schema_version": "s2.v1",
  "record_id": "City of Ontario v. Quon",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "City of Ontario v. Quon",
    "case_name_short": "Quon",
    "case_name_full": "CITY OF ONTARIO, CALIFORNIA v. JEFF QUON",
    "input_case_name": "City of Ontario v. Quon",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2010-06-17",
    "year": 2010,
    "docket": "08-1332",
    "cluster_id": 6796843,
    "lead_opinion_id": 6681698,
    "sibling_ids": [
      6681698,
      6681699,
      6681700
    ],
    "absolute_url": "/opinion/6796843/city-of-ontario-v-quon/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 148797,
        "score": 120,
        "case_name": "City of Ontario v. Quon"
      },
      {
        "cluster_id": 6794962,
        "score": 20,
        "case_name": "City of Ontario v. Quon"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "177 L. Ed. 2d 216",
        "volume": "177",
        "reporter": "L. Ed. 2d",
        "page": "216",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "130 S. Ct. 2619",
        "volume": "130",
        "reporter": "S. Ct.",
        "page": "2619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "560 U.S. 746",
        "volume": "560",
        "reporter": "U.S.",
        "page": "746",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "30 I.E.R. Cas. (BNA) 1345",
        "volume": "30",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "1345",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "78 U.S.L.W. 4591",
        "volume": "78",
        "reporter": "U.S.L.W.",
        "page": "4591",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 Fla. L. Weekly Fed. S 470",
        "volume": "22",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "470",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Empl. Prac. Dec. (CCH) 43,907",
        "volume": "93",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "43,907",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2010 U.S. LEXIS 4972",
        "volume": "2010",
        "reporter": "U.S. LEXIS",
        "page": "4972",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "177 L. Ed. 2d 216",
        "volume": "177",
        "reporter": "L. Ed. 2d",
        "page": "216",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 U.S. LEXIS 4972",
        "volume": "2010",
        "reporter": "U.S. LEXIS",
        "page": "4972",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "130 S. Ct. 2619",
        "volume": "130",
        "reporter": "S. Ct.",
        "page": "2619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "560 U.S. 746",
        "volume": "560",
        "reporter": "U.S.",
        "page": "746",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "30 I.E.R. Cas. (BNA) 1345",
        "volume": "30",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "1345",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "78 U.S.L.W. 4591",
        "volume": "78",
        "reporter": "U.S.L.W.",
        "page": "4591",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 Fla. L. Weekly Fed. S 470",
        "volume": "22",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "470",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Empl. Prac. Dec. (CCH) 43,907",
        "volume": "93",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "43,907",
        "type": 4,
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
      "id": "pin-761",
      "page": null,
      "quote": "--- # City of Ontario v. Quon *560 U.S. 746 (2010)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Jeff Quon, a police sergeant on the Ontario, California, SWAT team, was issued a city pager with a monthly character allotment. After he repeatedly exceeded the limit and reimbursed the overage fees, the police chief ordered an audit of the message transcripts (obtained from the wireless carrier) to decide whether the character limit was too low for legitimate work use or whether officers were effectively subsidizing personal texting. The audit revealed many personal and sexually explicit messages. Quon sued, claiming the review of his texts violated the Fourth Amendment. ## Issue Whether a public employer's warrantless review of the contents of an employee's text messages sent on an employer-provided pager was an unreasonable search under the Fourth Amendment. ## Rule The search is judged by reasonableness under *O'Connor v. Ortega*. Assuming arguendo that Quon had a privacy expectation and that the review was a search, the audit was reasonable:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-759",
      "page": null,
      "quote": "The Court must proceed with care when considering the whole concept of privacy expectations in communications made on electronic equipment owned by a government employer. The judiciary risks error by elaborating too fully on the Fourth Amendment implications of emerging technology before its role in society has become clear.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2010-06-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "City of Ontario v. Quon",
    "varies_by_point": false,
    "scope_note": "Good law; applies O'Connor v. Ortega to electronic communications. The Court deliberately declined to set broad rules about digital privacy expectations \u2014 a caution later echoed in Riley v. California and Carpenter.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "In re the United States",
          "cluster_id": 8441402,
          "cite": [
            "724 F.3d 600",
            "58 Communications Reg. (P&F) 1292",
            "2013 WL 3914484",
            "2013 U.S. App. LEXIS 15510"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Zailey Hess v. Jamie Garcia",
          "cluster_id": 9415232,
          "cite": [
            "72 F.4th 753"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Love v. State",
          "cluster_id": 6241312,
          "cite": [
            "543 S.W.3d 835"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Simon v. City and County of San Francisco",
          "cluster_id": 10382775,
          "cite": [
            "135 F.4th 784"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ruskai v. Pistole",
          "cluster_id": 2764193,
          "cite": [
            "775 F.3d 61",
            "2014 U.S. App. LEXIS 24350",
            "2014 WL 7272770"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crenshaw-Logal v. City of Abilene",
          "cluster_id": 8468431,
          "cite": [
            "436 F. App'x 306"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Weaver",
          "cluster_id": 4957807,
          "cite": [
            "9 F.4th 129"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Caraballo",
          "cluster_id": 8727352,
          "cite": [
            "963 F. Supp. 2d 341",
            "2013 WL 4039028",
            "2013 U.S. Dist. LEXIS 112739"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. Town of Duxbury",
          "cluster_id": 4643762,
          "cite": [
            "931 F.3d 102"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adkisson v. Paxton",
          "cluster_id": 5445438,
          "cite": [
            "459 S.W.3d 761",
            "43 Media L. Rep. (BNA) 1560",
            "2015 Tex. App. LEXIS 2167",
            "2015 WL 1030295"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Moises Zelaya-Veliz",
          "cluster_id": 9476330,
          "cite": [
            "94 F.4th 321"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Osborne v. Harris County",
          "cluster_id": 7312912,
          "cite": [
            "97 F. Supp. 3d 911",
            "2015 U.S. Dist. LEXIS 42534"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rickey Beene",
          "cluster_id": 3183556,
          "cite": [
            "818 F.3d 157",
            "2016 U.S. App. LEXIS 4331",
            "2016 WL 890127"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In re the United States for an Order Pursuant to Title 18",
          "cluster_id": 8713843,
          "cite": [
            "849 F. Supp. 2d 177",
            "2012 WL 989638",
            "2012 U.S. Dist. LEXIS 42779"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barrett v. Town of Plainville",
          "cluster_id": 7327099,
          "cite": [
            "272 F. Supp. 3d 235"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clarissa Gilmore v. Georgia Department of Corrections",
          "cluster_id": 10631717,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Apache Stronghold v. USA",
          "cluster_id": 9501928,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gilberto Morales",
          "cluster_id": 9476335,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jonathan Zelaya-Veliz",
          "cluster_id": 9476334,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Molina-Veliz",
          "cluster_id": 9476333,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Luis Gonzales",
          "cluster_id": 9476332,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Santos Castro",
          "cluster_id": 9476324,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zailey Hess v. Jamie Garcia",
          "cluster_id": 9415233,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "ANDRE VERDUN V. CITY OF SAN DIEGO",
          "cluster_id": 9367683,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jordan",
          "cluster_id": 8358611,
          "cite": [
            "33 Mass. L. Rptr. 180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "City of Ontario v. Quon:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(6681698 OR 6681699 OR 6681700) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 21,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 21,
        "triage_read": 1,
        "triage_snippet_classified": 20
      },
      "lane2_top_cited": {
        "query": "cites:(6681698 OR 6681699 OR 6681700)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0wJnM9OTQ3NjMzMyZ0PW8mZD0yMDI2LTA3LTA2JnA9Mg%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%286681698+OR+6681699+OR+6681700%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(6681698 OR 6681699 OR 6681700)",
        "reviewed": 9,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 9,
        "triage_read": 0,
        "triage_snippet_classified": 9
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(6681698 OR 6681699 OR 6681700)",
    "indexed_citing_opinions": 29,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 6681698,
        "count": 29,
        "count_source": "search"
      },
      {
        "opinion_id": 6681699,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 6681700,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 234,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/city-of-ontario-v-quon.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjQ5MDgzNjkmcz0zMTgzNTU2JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%286681698+OR+6681699+OR+6681700%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T00:26:01Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:26:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:26:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:29:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:26:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — City of Ontario v. Quon

```
<opinion type="majority">
<p id="b267-8">OPINION OF THE COURT</p>
<p id="b267-9">[<span class="citation no-link">560 U.S. 750</span>]</p>
<author id="b267-10">Justice Kennedy</author>
<p id="AMr">delivered the opinion of the Court.</p>
<p id="b267-11">This case involves the assertion by a government employer of the right, in circumstances to be described, to read text messages sent and received on a pager the employer owned and issued to an employee. The employee contends that the privacy of the messages is protected by the ban on “unreasonable searches and seizures” found in the Fourth Amendment to the United States Constitution, made applicable to the States by the Due Process Clause of the Fourteenth Amendment. <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U.S. 643</a></span>, <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">81 S. Ct. 1684</a></span>, <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">6 L. Ed. 2d 1081</a></span> (1961). Though the case touches issues of far-reaching significance, the Court concludes it can be resolved by settled principles determining when a search is reasonable.</p>
<p id="b267-12">I</p>
<p id="b267-13">A</p>
<p id="b267-14">The city of Ontario (City) is a political subdivision of the State of California. The case arose out of incidents in 2001 and 2002 when respondent Jeff Quon was employed by the Ontario Police Department (OPD). He was a police sergeant and member of OPD’s Special Weapons and Tactics (SWAT) Team. The City, OPD, and OPD’s Chief, Lloyd Scharf, are petitioners here. As will be discussed, two respondents share the last name Quon. In this opinion “Quon” refers to Jeff Quon, for the relevant events mostly revolve around him.</p>
<p id="b267-15">In October 2001, the City acquired 20 alphanumeric pagers capable of sending and receiving text messages. Arch Wireless Operating Company <page-number citation-index="1" label="222">*222</page-number>provided wireless service for the pagers. Under the City’s service contract with Arch Wireless, each pager was allotted a limited number of characters</p>
<p id="b268-4">[<span class="citation no-link">560 U.S. 751</span>]</p>
<p id="b268-5">sent or received each month. Usage in excess of that amount would result in an additional fee. The City issued pagers to Quon and other SWAT Team members in order to help the SWAT Team mobilize and respond to emergency situations.</p>
<p id="b268-6">Before acquiring the pagers, the City announced a “Computer Usage, Internet and E-Mail Policy” (Computer Policy) that applied to all employees. Among other provisions, it specified that the City “reserves the right to monitor and log all network activity including e-mail and Internet use, with or without notice. Users should have no expectation of privacy or confidentiality when using these resources.” App. to Pet. for Cert. 151, 152. In March 2000, Quon signed a statement acknowledging that he had read and understood the Computer Policy.</p>
<p id="b268-7">The Computer Policy did not apply, on its face, to text messaging. Text messages share similarities with e-mails, but the two differ in an important way. In this case, for instance, an e-mail sent on a City computer was transmitted through the City’s own data servers, but a text message sent on one of the City’s pagers was transmitted using wireless radio frequencies from an individual pager to a receiving station owned by Arch Wireless. It was routed through Arch Wireless’ computer network, where it remained until the recipient’s pager or cellular telephone was ready to receive the message, at which point Arch Wireless transmitted the message from the transmitting station nearest to the recipient. After delivery, Arch Wireless retained a copy on its computer servers. The message did not pass through computers owned by the City.</p>
<p id="b268-9">Although the Computer Policy did not cover text messages by its explicit terms, the City made clear to employees, including Quon, that the City would treat text messages the same way as it treated e-mails. At an April 18, 2002, staff meeting at which Quon was present, Lieutenant Steven Duke, the OPD officer responsible for the City’s contract</p>
<p id="b268-10">[<span class="citation no-link">560 U.S. 752</span>]</p>
<p id="b268-11">with Arch Wireless, told officers that messages sent on the pagers “are considered e-mail messages. This means that [text] messages would fall under the City’s policy as public information and [would be] eligible for auditing.” App. 30. Duke’s comments were put in writing in a memorandum sent on April 29, 2002, by Chief Scharf to Quon and other City personnel.</p>
<p id="b268-12">Within the first or second billing cycle after the pagers were distributed, Quon exceeded his monthly text message character allotment. Duke told Quon about the overage, and reminded him that messages sent on the pagers were “considered e-mail and could be audited.” <em>Id., </em>at 40. Duke said, however, that “it was not his intent to audit [an] employee’s text messages to see if the overage [was] due to work related transmissions.” <em>Ibid. </em>Duke suggested that Quon could reimburse the City for the overage fee rather than have Duke audit the messages. Quon wrote a check to the City for the overage. Duke offered the same arrangement to other employees who incurred overage fees.</p>
<p id="b268-13">Over the next few months, Quon exceeded his character limit three or four times. Each time he reimbursed the City. Quon and another officer again incurred overage fees for their <page-number citation-index="1" label="223">*223</page-number>pager usage in August 2002. At a meeting in October, Duke told Scharf that he had become “ ‘tired of being a bill collector.’ ” <em>Id., </em>at 91. Scharf decided to determine whether the existing character limit was too low—that is, whether officers such as Quon were having to pay fees for sending work-related messages—or if the overages were for personal messages. Scharf told Duke to request transcripts of text messages sent in August and September by Quon and the other employee who had exceeded the character allowance.</p>
<p id="b269-4">At Duke’s request, an administrative assistant employed by OPD contacted Arch Wireless. After verifying that the City was the subscriber on the accounts, Arch Wireless provided the desired transcripts. Duke reviewed the transcripts</p>
<p id="b269-5">[<span class="citation no-link">560 U.S. 753</span>]</p>
<p id="b269-6">and discovered that many of the messages sent and received on Quon’s pager were not work related, and some were sexually explicit. Duke reported his findings to Scharf, who, along with Quon’s immediate supervisor, reviewed the transcripts himself. After his review, Scharf referred the matter to OPD’s internal affairs division for an investigation into whether Quon was violating OPD rules by pursuing personal matters while on duty.</p>
<p id="b269-7">The officer in charge of the internal affairs review was Sergeant Patrick McMahon. Before conducting a review, McMahon used Quon’s work schedule to redact the transcripts in order to eliminate any messages Quon sent while off duty. He then reviewed the content of the messages Quon sent during work hours. McMahon’s report noted that Quon sent or received 456 messages during work hours in the month of August 2002, of which no more than 57 were work related; he sent as many as 80 messages during a single day at work; and on an average workday, Quon sent or received 28 messages, of which only 3 were related to police business. The report concluded that Quon had violated OPD rules. Quon was allegedly disciplined.</p>
<p id="b269-9">B</p>
<p id="b269-10">Raising claims under Rev. Stat. § 1979, <span class="citation no-link">42 U.S.C. § 1983</span>; <span class="citation no-link">18 U.S.C. § 2701</span> <em>et seq., </em>popularly known as the Stored Communications Act (SCA); and California law, Quon filed suit against petitioners in the United States District Court for the Central District of California. Arch Wireless and an individual not relevant here were also named as defendants. Quon was joined in his suit by another plaintiff who is not a party before this Court and by the other respondents, each of whom exchanged text messages with Quon during August and September 2002: Jerilyn Quon, Jeff Quon’s then-wife, from whom he was separated; April Florio, an OPD employee with whom Jeff Quon was romantically involved; and Steve Trujillo, another member of the OPD SWAT Team.</p>
<p id="b269-11">[<span class="citation no-link">560 U.S. 754</span>]</p>
<p id="b269-12">Among the allegations in the complaint was that petitioners violated respondents’ Fourth Amendment rights and the SCA by obtaining and reviewing the transcript of Jeff Quon’s pager messages and that Arch Wireless had violated the SCA by turning over the transcript to the City.</p>
<p id="b269-13">The parties filed cross-motions for summary judgment. The District Court granted Arch Wireless’ motion for summary judgment on the SCA claim but denied petitioners’ motion for summary judgment on the Fourth Amendment claims. <em>Quon </em>v. <em>Arch Wireless Operating Co., </em><span class="citation" data-id="2499887"><a href="/opinion/2499887/quon-v-arch-wireless-operating-co-inc/" aria-description="Citation for case: Quon v. Arch Wireless Operating Co., Inc.">445 F. Supp. 2d 1116</a></span> (CD Cal. 2006). Relying on <page-number citation-index="1" label="224">*224</page-number>the plurality opinion in <em>O’Connor </em>v. <em>Ortega, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#711" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U.S. 709, 711</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (1987), the District Court determined that Quon had a reasonable expectation of privacy in the content of his text messages. Whether the audit of the text messages was nonetheless reasonable, the District Court concluded, turned on Chief Scharf's intent: “[I]f the purpose for the audit was to determine if Quon was using his pager to ‘play games’ and ‘waste time,’ then the audit was not constitutionally reasonable”; but if the audit’s purpose “was to determine the efficacy of the existing character limits to ensure that officers were not paying hidden work-related costs, ... no constitutional violation occurred.” <span class="citation" data-id="2499887"><a href="/opinion/2499887/quon-v-arch-wireless-operating-co-inc/#1146" aria-description="Citation for case: Quon v. Arch Wireless Operating Co., Inc.">445 F. Supp. 2d, at 1146</a></span>.</p>
<p id="b270-4">The District Court held a jury trial to determine the purpose of the audit. The jury concluded that Scharf ordered the audit to determine the efficacy of the character limits. The District Court accordingly held that petitioners did not violate the Fourth Amendment. It entered judgment in their favor.</p>
<p id="b270-5">The United States Court of Appeals for the Ninth Circuit reversed in part. <em>Quon </em>v. <em>Arch Wireless Operating Co., </em><span class="citation" data-id="1455295"><a href="/opinion/1455295/quon-v-arch-wireless-operating-co-inc/" aria-description="Citation for case: Quon v. Arch Wireless Operating Co., Inc.">529 F.3d 892</a></span> (2008). The panel agreed with the District Court that Jeff Quon had a reasonable expectation of privacy in his text messages but disagreed with the District Court about whether the search was reasonable. Even though the search was conducted for “a legitimate work-related rationale,”</p>
<p id="b270-6">[<span class="citation no-link">560 U.S. 755</span>]</p>
<p id="b270-7">the Court of Appeals concluded, it “was not reasonable in scope.” <em>Id., </em>at 908. The panel disagreed with the District Court’s observation that “there were no less-intrusive means” that Chief Scharf could have used “to verify the efficacy of the 25,000 character limit . . . without intruding on [respondents’] Fourth Amendment rights.” <em>Id., </em>at 908-909. The opinion pointed to a “host of simple ways” that the chief could have used instead of the audit, such as warning Quon at the beginning of the month that his future messages would be audited, or asking Quon himself to redact the transcript of his messages. <em>Id., </em>at 909. The Court of Appeals further concluded that Arch Wireless had violated the SCA by turning over the transcript to the City.</p>
<p id="b270-9">The Ninth Circuit denied a petition for rehearing en banc. <em>Quon </em>v. <em>Arch Wireless Operating Co., </em><span class="citation" data-id="9849623"><a href="/opinion/1276870/quon-v-arch-wireless-operating-co-inc/" aria-description="Citation for case: Quon v. Arch Wireless Operating Co., Inc.">554 F.3d 769</a></span> (2009). Judge Ikuta, joined by six other Circuit Judges, dissented. <span class="citation" data-id="9849623"><a href="/opinion/1276870/quon-v-arch-wireless-operating-co-inc/#774" aria-description="Citation for case: Quon v. Arch Wireless Operating Co., Inc."><em>Id., </em>at 774-779</a></span>. Judge Wardlaw concurred in the denial of rehearing, defending the panel’s opinion against the dissent. <span class="citation" data-id="9849623"><a href="/opinion/1276870/quon-v-arch-wireless-operating-co-inc/#769" aria-description="Citation for case: Quon v. Arch Wireless Operating Co., Inc."><em>Id., </em>at 769-774</a></span>.</p>
<p id="b270-10">This Court granted the petition for certiorari filed by the City, OPD, and Chief Scharf challenging the Court of Appeals’ holding that they violated the Fourth Amendment. <span class="citation no-link">558 U.S. 1090</span>, <span class="citation no-link">130 S. Ct. 1011</span>, <span class="citation no-link">175 L. Ed. 2d 617</span> (2009). The petition for certiorari filed by Arch Wireless challenging the Ninth Circuit’s ruling that Arch Wireless violated the SCA was denied. <em>USA Mobility Wireless, Inc. </em>v. <em>Quon, </em><span class="citation no-link">558 U.S. 1091</span>, <span class="citation no-link">130 S. Ct. 1011</span>, <span class="citation no-link">175 L. Ed. 2d 618</span> (2009).</p>
<p id="b270-11">II</p>
<p id="b270-12">The Fourth Amendment states: “The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated . . . .” It is well settled that the Fourth Amendment’s protection extends beyond the sphere of criminal investigations. <em>Camara </em>v. <em>Municipal Court of City and County of San Francisco, </em><page-number citation-index="1" label="225">*225</page-number><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#530" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U.S. 523, 530</a></span>, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">87 S. Ct. 1727</a></span>, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">18 L. Ed. 2d 930</a></span> (1967). “The Amendment guarantees the privacy, dignity, and security of</p>
<p id="b271-4">[<span class="citation no-link">560 U.S. 756</span>]</p>
<p id="b271-5">persons against certain arbitrary and invasive acts by officers of the Government,” without regard to whether the government actor is investigating crime or performing another function. <em>Skinner </em>v. <em>Railway Labor Executives’ Assn., </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#613" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U.S. 602, 613-614</a></span>, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">109 S. Ct. 1402</a></span>, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">103 L. Ed. 2d 639</a></span> (1989). The Fourth Amendment applies as well when the Government acts in its capacity as an employer. <em>Treasury Employees </em>v. <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#665" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U.S. 656, 665</a></span>, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">109 S. Ct. 1384</a></span>, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">103 L. Ed. 2d 685</a></span> (1989).</p>
<p id="b271-6">The Court discussed this principle in <em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O’Connor</a></span>. </em>There a physician employed by a state hospital alleged that hospital officials investigating workplace misconduct had violated his Fourth Amendment rights by searching his office and seizing personal items from his desk and filing cabinet. All Members of the Court agreed with the general principle that  “[individuals do not lose Fourth Amendment rights merely because they work for the government instead of a private employer.” <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#717" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U.S., at 717</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (plurality opinion); see also <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#731" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>id., </em>at 731</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (Scalia, J., concurring in judgment); <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#737" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>id., </em>at 737</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (Blackmun, J., dissenting). A majority of the Court further agreed that “ ‘special needs, beyond the normal need for law enforcement,’ ” make the warrant and probable-cause requirement impracticable for government employers. <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#725" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>Id., </em>at 725</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (plurality opinion) (quoting <em>New Jersey </em>v. <em>T. L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#351" aria-description="Citation for case: New Jersey v. T. L. O.">469 U.S. 325, 351</a></span>, <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/" aria-description="Citation for case: New Jersey v. T. L. O.">105 S. Ct. 733</a></span>, <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/" aria-description="Citation for case: New Jersey v. T. L. O.">83 L. Ed. 2d 720</a></span> (1985) (Blackmun, J., concurring in judgment)); <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#732" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U.S., at 732</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (opinion of Scalia, J.) (quoting same).</p>
<p id="b271-8">The <em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O’Connor</a></span> </em>Court did disagree on the proper analytical framework for Fourth Amendment claims against government employers. A four-Justice plurality concluded that the correct analysis has two steps. First, because “some government offices may be so open to fellow employees or the public that no expectation of privacy is reasonable,” id<em>., </em>at 718, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>, a court must consider “ [t]he operational realities of the workplace” in order to determine whether an employee’s Fourth Amendment rights are implicated, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#717" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>id., </em>at 717</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>. On this view, “the question whether an employee has a reasonable</p>
<p id="b271-9">[<span class="citation no-link">560 U.S. 757</span>]</p>
<p id="b271-10">expectation of privacy must be addressed on a case-by-case basis.” <em>Id., </em>at 718, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>. Next, where an employee has a legitimate privacy expectation, an employer’s intrusion on that expectation “for noninvestiga-tory, work-related purposes, as well as for investigations of work-related misconduct, should be judged by the standard of reasonableness under all the circumstances.” <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#725" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>Id., </em>at 725-726</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>.</p>
<p id="b271-11">Justice Scalia, concurring in the judgment, outlined a different approach. His opinion would have dispensed with an inquiry into “operational realities” and would conclude “that the offices of government employees . . . are covered by Fourth Amendment protections as a general matter.” <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#731" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>Id., </em>at 731</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>. But he would also have held “that government searches to retrieve work-related materials or to investigate violations of workplace rules—searches of the sort that are regarded as reasonable and normal in <page-number citation-index="1" label="226">*226</page-number>the private-employer context—do not violate the Fourth Amendment.” <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#732" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>Id., </em>at 732</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>.</p>
<p id="b272-4">Later, in the <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span> </em>decision, the Court explained that “operational realities” could diminish an employee’s privacy expectations, and that this diminution could be taken into consideration when assessing the reasonableness of a workplace search. 489 U.S., at 671, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">109 S. Ct. 1402</a></span>, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">103 L. Ed. 2d 639</a></span>. In the two decades since <em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O’Connor</a></span>, </em>however, the threshold test for determining the scope of an employee’s Fourth Amendment rights has not been clarified further. Here, though they disagree on whether Quon had a reasonable expectation of privacy, both petitioners and respondents start from the premise that the <em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O’Connor</a></span> </em>plurality controls. See Brief for Petitioners 22-28; Brief for Respondents 25-32. It is not necessary to resolve whether that premise is correct. The case can be decided by determining that the search was reasonable even assuming Quon had a reasonable expectation of privacy. The two <em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O’Connor</a></span> </em>approaches—the plurality’s and Justice Scalia’s—there-fore lead to the same result here.</p>
<p id="b272-5">[<span class="citation no-link">560 U.S. 758</span>]</p>
<p id="b272-6">III</p>
<p id="b272-7">A</p>
<p id="b272-8">Before turning to the reasonableness of the search, it is instructive to note the parties’ disagreement over whether Quon had a reasonable expectation of privacy. The record does establish that OPD, at the outset, made it clear that pager messages were not considered private. The City’s Computer Policy stated that “[u]sers should have no expectation of privacy or confidentiality when using” City computers. App. to Pet. for Cert. 152. Chief Scharf’s memo and Duke’s statements made clear that this official policy extended to text messaging. The disagreement, at least as respondents see the case, is over whether Duke’s later statements overrode the official policy. Respondents contend that because Duke told Quon that an audit would be unnecessary if Quon paid for the overage, Quon reasonably could expect that the contents of his messages would remain private.</p>
<p id="b272-10">At this point, were we to assume that inquiry into “operational realities” were called for, compare <em>O’Connor, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#717" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U.S., at 717</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (plurality opinion), with <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#730" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>id., </em>at 730-731</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (opinion of Scalia, J.); see also <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#737" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>id., </em>at 737-738</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (Blackmun, J., dissenting), it would be necessary to ask whether Duke’s statements could be taken as announcing a change in OPD policy, and if so, whether he had, in fact or appearance, the authority to make such a change and to guarantee the privacy of text messaging. It would also be necessary to consider whether a review of messages sent on police pagers, particularly those sent while officers are on duty, might be justified for other reasons, including performance evaluations, litigation concerning the lawfulness of police actions, and perhaps compliance with state open records laws. See Brief for Petitioners 35-40 (citing Cal. Public Records Act, Cal. Govt. Code Ann. § 6250 <em>et seq. </em>(West 2008)). These matters would all bear on the legitimacy of an employee’s privacy expectation.</p>
<p id="b272-11">[<span class="citation no-link">560 U.S. 759</span>]</p>
<p id="b272-12">The Court must proceed with care when considering the whole concept of privacy expectations in communi<page-number citation-index="1" label="227">*227</page-number>cations made on electronic equipment owned by a government employer. The judiciary risks error by elaborating too fully on the Fourth Amendment implications of emerging technology before its role in society has become clear. See, <em>e.g., Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U.S. 438</a></span>, <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">48 S. Ct. 564</a></span>, <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">72 L. Ed. 944</a></span> (1928), overruled by <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States">389 U.S. 347, 353</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S. Ct. 507</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L. Ed. 2d 576</a></span> (1967). In <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>the Court relied on its own knowledge and experience to conclude that there is a reasonable expectation of privacy in a telephone booth. See <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States"><em>id., </em>at 360-361</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S. Ct. 507</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L. Ed. 2d 576</a></span> (Harlan, J., concurring). It is not so clear that courts at present are on so sure a ground. Prudence counsels caution before the facts in the instant case are used to establish far-reaching premises that define the existence, and extent, of privacy expectations enjoyed by employees when using employer-provided communication devices.</p>
<p id="b273-4">Rapid changes in the dynamics of communication and information transmission are evident not just in the technology itself but in what society accepts as proper behavior. As one <em>amici </em>brief notes, many employers expect or at least tolerate personal use of such equipment by employees because it often increases worker efficiency. See Brief for Electronic Frontier Foundation et al. 16-20. Another <em>amicus </em>points out that the law is beginning to respond to these developments, as some States have recently passed statutes requiring employers to notify employees when monitoring their electronic communications. See Brief for New York Intellectual Property Law Association 22 (citing Del. Code Ann., Tit. 19, § 705 (2005); <span class="citation no-link">Conn. Gen. Stat. Ann. § 31</span>-48d (West 2003)). At present, it is uncertain how workplace norms, and the law’s treatment of them, will evolve.</p>
<p id="b273-6">Even if the Court were certain that the <em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O’Connor</a></span> </em>plurality’s approach were the right one, the Court would have difficulty predicting how employees’ privacy expectations will be shaped by those changes or the degree to which society</p>
<p id="b273-7">[<span class="citation no-link">560 U.S. 760</span>]</p>
<p id="b273-8">will be prepared to recognize those expectations as reasonable. See <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#715" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U.S., at 715</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>. Cell phone and text message communications are so pervasive that some persons may consider them to be essential means or necessary instruments for self-expression, even self-identification. That might strengthen the case for an expectation of privacy. On the other hand, the ubiquity of those devices has made them generally affordable, so one could counter that employees who need cell phones or similar devices for personal matters can purchase and pay for their own. And employer policies concerning communications will of course shape the reasonable expectations of their employees, especially to the extent that such policies are clearly communicated.</p>
<p id="b273-9">Abroad holding concerning employees’ privacy expectations vis-a-vis employer-provided technological equipment might have implications for future cases that cannot be predicted. It is preferable to dispose of this case on narrower grounds. For present purposes we assume several propositions, <em>arguendo: </em>First, Quon had a reasonable expectation of privacy in the text messages sent on the pager provided to him by the City; second, petitioners’ review of the transcript constituted a search within the meaning of the Fourth Amendment; and third, the principles applicable to a government employer’s search of an employ<page-number citation-index="1" label="228">*228</page-number>ee’s physical office apply with at least the same force when the employer intrudes on the employee’s privacy in the electronic sphere.</p>
<p id="b274-4">B</p>
<p id="b274-5">Even if Quon had a reasonable expectation of privacy in his text messages, petitioners did not necessarily violate the Fourth Amendment by obtaining and reviewing the transcripts.  Although as a general matter, warrantless searches “are <em>per se </em>unreasonable under the Fourth Amendment,” there are “a few specifically established and well-delineated exceptions” to that general rule. <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States"><em>Katz, supra, </em>at 357</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S. Ct. 507</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L. Ed. 2d 576</a></span>. The Court has held that the “ ‘special needs’ ” of the workplace</p>
<p id="AMa">[<span class="citation no-link">560 U.S. 761</span>]</p>
<p id="b274-6">justify one such exception. <em>O’Connor, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#725" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U.S., at 725</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (plurality opinion); <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#732" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>id., </em>at 732</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (Scalia, J., concurring in judgment); <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#666" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U.S., at 666-667</a></span>, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">109 S. Ct. 1384</a></span>, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">103 L. Ed. 2d 685</a></span>.</p>
<p id="b274-7">Under the approach of the <em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O’Connor</a></span> </em>plurality,  when conducted for a “noninvestigatory, work-related purpos[e]” or for the “investi-gatio[n] of work-related misconduct,” a government employer’s warrantless search is reasonable if it is “ ‘justified at its inception’ ” and if “ ‘the measures adopted are reasonably related to the objectives of the search and not excessively intrusive in light of’ ” the circumstances giving rise to the search. <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#725" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U.S., at 725-726</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>. The search here satisfied the standard of the <em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O’Connor</a></span> </em>plurality and was reasonable under that approach.</p>
<p id="b274-8">The search was justified at its inception because there were “reasonable grounds for suspecting that the search [was] necessary for a noninvestigatory work-related purpose.” <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#726" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>Id., </em>at 726</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>. As a jury found, Chief Scharf ordered the search in order to determine whether the character limit on the City’s contract with Arch Wireless was sufficient to meet the City’s needs. This was, as the Ninth Circuit noted, a “legitimate work-related rationale.” <span class="citation" data-id="1455295"><a href="/opinion/1455295/quon-v-arch-wireless-operating-co-inc/#908" aria-description="Citation for case: Quon v. Arch Wireless Operating Co., Inc.">529 F.3d, at 908</a></span>. The City and OPD had a legitimate interest in ensuring that employees were not being forced to pay out of their own pockets for work-related expenses, or on the other hand that the City was not paying for extensive personal communications.</p>
<p id="b274-10">As for the scope of the search, reviewing the transcripts was reasonable because it was an efficient and expedient way to determine whether Quon’s overages were the result of work-related messaging or personal use. The review was also not “ ‘excessively intrusive.’ ” <em>O’Connor, supra, </em>at 726, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span> (plurality opinion). Although Quon had gone over his monthly allotment a number of times, OPD requested transcripts for only the months of August and September 2002. While it may have been reasonable as well for OPD to review transcripts of all the months in which Quon exceeded his</p>
<p id="Amep">[<span class="citation no-link">560 U.S. 762</span>]</p>
<p id="b274-11">allowance, it was certainly reasonable for OPD to review messages for just two months in order to obtain a large enough sample to decide whether the character limits were efficacious. And it is worth noting that during his internal affairs investigation, McMahon redacted all messages Quon sent while off duty, a measure which reduced the intrusiveness of any further review of the transcripts.</p>
<p id="b275-3"><page-number citation-index="1" label="229">*229</page-number>Furthermore, and again on the assumption that Quon had a reasonable expectation of privacy in the contents of his messages,  the extent of an expectation is relevant to assessing whether the search was too intrusive. See <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#671" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><em>Von Raab, supra, </em>at 671</a></span>, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">109 S. Ct. 1384</a></span>, <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">103 L. Ed. 2d 685</a></span>; cf. <em>Vernonia School Dist. 47J </em>v. <em>Acton, </em><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#654" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U.S. 646, 654-657</a></span>, <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">115 S. Ct. 2386</a></span>, <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">132 L. Ed. 2d 564</a></span> (1995). Even if he could assume some level of privacy would inhere in his messages, it would not have been reasonable for Quon to conclude that his messages were in all circumstances immune from scrutiny. Quon was told that his messages were subject to auditing. As a law enforcement officer, he would or should have known that his actions were likely to come under legal scrutiny, and that this might entail an analysis of his on-the-job communications. Under the circumstances, a reasonable employee would be aware that sound management principles might require the audit of messages to determine whether the pager was being appropriately used. Given that the City issued the pagers to Quon and other SWAT Team members in order to help them more quickly respond to crises— and given that Quon had received no assurances of privacy—Quon could have anticipated that it might be necessary for the City to audit pager messages to assess the SWAT Team’s performance in particular emergency situations.</p>
<p id="b275-4">From OPD’s perspective, the fact that Quon likely had only a limited privacy expectation, with boundaries that we need not here explore, lessened the risk that the review would intrude on highly private details of Quon’s life. OPD’s audit of messages on Quon’s employer-provided pager was not nearly as intrusive as a search of his personal e-mail account</p>
<p id="b275-5">[<span class="citation no-link">560 U.S. 763</span>]</p>
<p id="b275-6">or pager, or a wiretap on his home phone line, would have been. That the search did reveal intimate details of Quon’s life does not make it unreasonable, for under the circumstances a reasonable employer would not expect that such a review would intrude on such matters. The search was permissible in its scope.</p>
<p id="b275-7">The Court of Appeals erred in finding the search unreasonable. It pointed to a “host of simple ways to verify the efficacy of the 25,000 character limit . . . without intruding on [respondents’] Fourth Amendment rights.” <span class="citation" data-id="1455295"><a href="/opinion/1455295/quon-v-arch-wireless-operating-co-inc/#909" aria-description="Citation for case: Quon v. Arch Wireless Operating Co., Inc.">529 F.3d, at 909</a></span>. The panel suggested that Scharf “could have warned Quon that for the month of September he was forbidden from using his pager for personal communications, and that the contents of all of his messages would be reviewed to ensure the pager was used only for work-related purposes during that timeframe. Alternatively, if [OPD] wanted to review past usage, it could have asked Quon to count the characters himself, or asked him to redact personal messages and grant permission to [OPD] to review the redacted transcript.” <em><span class="citation" data-id="1455295"><a href="/opinion/1455295/quon-v-arch-wireless-operating-co-inc/" aria-description="Citation for case: Quon v. Arch Wireless Operating Co., Inc.">Ibid.</a></span></em></p>
<p id="b275-8">This approach was inconsistent with controlling precedents.  This Court has “repeatedly refused to declare that only the ‘least intrusive’ search practicable can be reasonable under the Fourth Amendment.” <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#663" aria-description="Citation for case: Vernonia School District 47J v. Acton"><em>Vernonia, supra, </em>at 663</a></span>, <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">115 S. Ct. 2386</a></span>, <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">132 L. Ed. 2d 564</a></span>; see also, <em>e.g., Board of Ed. of Independent School Dist. No. 92 of Pottawatomie Cty. </em>v. <em>Earls, </em><span class="citation" data-id="9434325"><a href="/opinion/121171/board-of-education-of-independent-school-district-no-92-of-pottawatomie/#837" aria-description="Citation for case: Board of Education of Independent School District No. 92...">536 U.S. 822, 837</a></span>, <span class="citation" data-id="9434325"><a href="/opinion/121171/board-of-education-of-independent-school-district-no-92-of-pottawatomie/" aria-description="Citation for case: Board of Education of Independent School District No. 92...">122 S. Ct. 2559</a></span>, <span class="citation" data-id="9434325"><a href="/opinion/121171/board-of-education-of-independent-school-district-no-92-of-pottawatomie/" aria-description="Citation for case: Board of Education of Independent School District No. 92...">153 L. Ed. 2d 735</a></span> (2002); <em>Illinois </em>v. <em>Lafayette, </em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/#647" aria-description="Citation for case: Illinois v. Lafayette">462 U.S. 640, 647</a></span>, <span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">103 S. Ct. 2605</a></span>, <span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">77 L. Ed. 2d 65</a></span> (1983). That rationale “could raise insuperable barriers to the exercise of virtually all search- <page-number citation-index="1" label="230">*230</page-number>and-seizure powers,” <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#557" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U.S. 543, 557, n. 12</a></span>, <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">96 S. Ct. 3074</a></span>, <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">49 L. Ed. 2d 1116</a></span> (1976), because “judges engaged in <em>post hoc </em>evaluations of government conduct can almost always imagine some alternative means by which the objectives of the government might have been accomplished,” <em>Skinner, </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#629" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U.S., at 629, n. 9</a></span>, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">109 S. Ct. 1402</a></span>, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">103 L. Ed. 2d 639</a></span> (internal quotation marks and brackets omitted). The analytic errors of the Court of Appeals in this case illustrate the necessity of</p>
<p id="ACI">[<span class="citation no-link">560 U.S. 764</span>]</p>
<p id="b276-4">this principle. Even assuming there were ways that OPD could have performed the search that would have been less intrusive, it does not follow that the search as conducted was unreasonable.</p>
<p id="b276-5">Respondents argue that the search was <em>per se </em>unreasonable in light of the Court of Appeals’ conclusion that Arch Wireless violated the SCA by giving the City the transcripts of Quon’s text messages. The merits of the SCA claim are not before us. But even if the Court of Appeals was correct to conclude that the SCA forbade Arch Wireless from turning over the transcripts, it does not follow that petitioners’ actions were unreasonable. Respondents point to no authority for the proposition that the existence of statutory protection renders a search <em>per se </em>unreasonable under the Fourth Amendment. And the precedents counsel otherwise. See <em>Virginia </em>v. <em>Moore, </em><span class="citation" data-id="9435233"><a href="/opinion/145814/virginia-v-moore/#168" aria-description="Citation for case: Virginia v. Moore">553 U.S. 164, 168</a></span>, <span class="citation" data-id="9435233"><a href="/opinion/145814/virginia-v-moore/" aria-description="Citation for case: Virginia v. Moore">128 S. Ct. 1598</a></span>, <span class="citation" data-id="9435233"><a href="/opinion/145814/virginia-v-moore/" aria-description="Citation for case: Virginia v. Moore">170 L. Ed. 2d 559</a></span> (2008) (search incident to an arrest that was illegal under state law was reasonable); <em>California </em>v. <em>Greenwood, </em><span class="citation" data-id="9431296"><a href="/opinion/112067/california-v-greenwood/#43" aria-description="Citation for case: California v. Greenwood">486 U.S. 35, 43</a></span>, <span class="citation" data-id="9431296"><a href="/opinion/112067/california-v-greenwood/" aria-description="Citation for case: California v. Greenwood">108 S. Ct. 1625</a></span>, <span class="citation" data-id="9431296"><a href="/opinion/112067/california-v-greenwood/" aria-description="Citation for case: California v. Greenwood">100 L. Ed. 2d 30</a></span> (1988) (rejecting argument that if state law forbade police search of individual’s garbage the search would violate the Fourth Amendment). Furthermore, respondents do not maintain that any OPD employee either violated the law him-self or herself or knew or should have known that Arch Wireless, by turning over the transcript, would have violated the law. The otherwise reasonable search by OPD is not rendered unreasonable by the assumption that Arch Wireless violated the SCA by turning over the transcripts.</p>
<p id="b276-7">Because the search was motivated by a legitimate work-related purpose, and because it was not excessive in scope, the search was reasonable under the approach of the <em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O’Connor</a></span> </em>plurality. <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#726" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U.S., at 726</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>. For these same reasons—that the employer had a legitimate reason for the search, and that the search was not excessively intrusive in light of that justification—the Court also concludes that the search would be “regarded as reasonable and normal in the private-employer context” and would satisfy the approach of Justice</p>
<p id="A_p">[<span class="citation no-link">560 U.S. 765</span>]</p>
<p id="b276-8">Scalia’s concurrence. <em>Id., </em>at 732, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">107 S. Ct. 1492</a></span>, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">94 L. Ed. 2d 714</a></span>. The search was reasonable, and the Court of Appeals erred by holding to the contrary. Petitioners did not violate Quon’s Fourth Amendment rights.</p>
<p id="b276-9">C</p>
<p id="b276-10">Finally, the Court must consider whether the search violated the Fourth Amendment rights of Jerilyn Quon, Florio, and Trujillo, the respondents who sent text messages to Jeff Quon. Petitioners and respondents disagree whether a sender of a text message can have a reasonable expectation of privacy in a message he knowingly sends to someone’s employer-provided pager. It is not necessary to resolve this question in order to dispose of the case, however. <page-number citation-index="1" label="231">*231</page-number>Respondents argue that because “the search was unreasonable as to Sergeant Quon, it was also unreasonable as to his correspondents.” Brief for Respondents 60 (some capitalization omitted; boldface deleted). They make no corollary argument that the search, if reasonable as to Quon, could nonetheless be unreasonable as to Quon’s correspondents. See <em>id., </em>at 65-66. In light of this litigating position and the Court’s conclusion that the search was reasonable as to Jeff Quon, it necessarily follows that these other respondents cannot prevail.</p>
<p id="pAiz">
<img class="p" height="29" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPgAAAAdAQAAAACvI5yXAAAAiUlEQVR4nM3SsQ0CMQwF0J8vRAsNPTABKzAVY8BGiHUQxXUXoYNPh618Kc1JCHfPju1ISRG6wX75F/Wa3YLAI6dazN//XFyCBmJcp+MO1dNK3zAQy+shWhzSTSlaENjn+xqkTW5pQbx22+gwENNxiJRDw3iOiYai973GTAPBKa00zH2/8v//uxsfCuKccmBnLFwAAAAASUVORK5CYII=" width="247"/>
</p>
<p id="b277-5">Because the search was reasonable, petitioners did not violate respondents’ Fourth Amendment rights, and the court below erred by concluding otherwise. The judgment of the Court of Appeals for the Ninth Circuit is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b277-6">It is so ordered.</p>
</opinion>
```

---
