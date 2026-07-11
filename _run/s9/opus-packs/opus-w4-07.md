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

## GROUP: _overhaul2/lake/cases/Foster v. California.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Foster v. California"
type: case
citation: "394 U.S. 440 (1969)"
parallel_cite: "89 S. Ct. 1127; 22 L. Ed. 2d 402"
neutral_cite: 1969 U.S. LEXIS 2050
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1969
date_decided: 1969-04-01
docket: 47
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1969-04-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Foster v. California
  varies_by_point: false
  scope_note: "Good law; the rare case in which the Court found a pretrial identification so suggestive as to violate due process (noted as such in Perry v. New Hampshire)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107890/foster-v-california/"
  cluster_id: 107890
  opinion_id: 107890
  identity_checked: true
homes:
  - page: "[[Eyewitness Identification]]"
    role: "Key — Progeny"
related: ["[[Stovall v. Denno]]", "[[Neil v. Biggers]]", "[[Manson v. Brathwaite]]", "[[Perry v. New Hampshire]]"]
aliases: []
tags: ["case", "due-process", "eyewitness-identification", "lineup", "suggestive"]
holding: "An identification procedure may be so unnecessarily suggestive that it denies due process; here a lineup that made the suspect stand out, followed by a one-on-one showup and a repeat lineup in which he was the only carryover, made identification all but inevitable and violated due process — the rare such reversal."
lake:
  record_id: Foster v. California
  status: verified
  projected_at: 2026-07-06
---

# Foster v. California

*394 U.S. 440 (1969)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
The only eyewitness to a Western Union armed robbery, manager Joseph David, viewed a police lineup of three men in which Foster — close to six feet tall — stood between two men five-foot-five or -six, and Foster wore a leather jacket like the robber's. David was unsure. Police then staged a one-to-one confrontation between David and Foster; David was still uncertain. About a week later police arranged a second lineup of five men in which Foster was the only person carried over from the first lineup. David was then "convinced."

## Issue
Whether a pretrial identification procedure can be so unnecessarily suggestive and conducive to mistaken identification that admitting the resulting identification denies the defendant due process of law.

## Rule
Yes. Even apart from the right-to-counsel rule of *[[United States v. Wade|Wade]]*/*[[Gilbert v. California|Gilbert]]* (inapplicable to pre-1967 lineups), "the conduct of identification procedures may be 'so unnecessarily suggestive and conducive to irreparable mistaken identification' as to be a denial of due process of law." — 394 U.S. at 442. ^pin-442

Applying that standard: "The suggestive elements in this identification procedure made it all but inevitable that David would identify petitioner whether or not he was in fact 'the man.' In effect, the police repeatedly said to the witness, 'This is the man.' ... This procedure so undermined the reliability of the eyewitness identification as to violate due process." — *Id.* at 443. ^pin-443

## Application
The cumulative suggestiveness was extreme: Foster stood out by height and clothing in the first lineup; when that failed to produce a positive identification, police escalated to a one-on-one showup; and when David was still tentative, a second lineup placed Foster as the only repeat participant. Each step pointed the witness to Foster, so his eventual "conviction" that Foster was the robber was the product of the procedure rather than independent recollection — a denial of due process.

## Conclusion
The identification procedure violated due process; the judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]]. *Foster* is the rare instance in which the Supreme Court found a suggestive pretrial identification unconstitutional.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The "unnecessarily suggestive" inquiry was later refined into a reliability test by [[Neil v. Biggers]] and [[Manson v. Brathwaite]], and the due-process screen was confined to police-arranged suggestiveness in [[Perry v. New Hampshire]]. *Foster* remains the paradigm of a procedure suggestive enough to require exclusion.

## Appears on
- [[Eyewitness Identification]] — *Key — Progeny*

## Sources
- *Foster v. California*, 394 U.S. 440 (1969) — https://www.courtlistener.com/opinion/107890/foster-v-california/ — pinpoints: 442, 443.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7f34c4b47d4dcead", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Foster v. California"}, "payload": {"all": [{"cite": "394 U.S. 440", "page": "440", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "394"}, {"cite": "89 S. Ct. 1127", "page": "1127", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "89"}, {"cite": "22 L. Ed. 2d 402", "page": "402", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "22"}, {"cite": "1969 U.S. LEXIS 2050", "page": "2050", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1969"}], "display": "394 U.S. 440", "official": {"cite": "394 U.S. 440", "page": "440", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "394"}, "official_selection_present": true, "record_id": "Foster v. California"}}
{"assertion_id": "89eea5c4f74f888b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-443", "record_id": "Foster v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-443", "pinpoint_status": "slip-only", "quote": "The suggestive elements in this identification procedure made it all but inevitable that David would identify petitioner whether or not he was in fact 'the man.' In effect, the police repeatedly said to the witness, 'This is the man.' ... This procedure so undermined the reliability of the eyewitness identification as to violate due process.", "quote_fidelity": "mismatch", "record_id": "Foster v. California", "star_marker": null}}
{"assertion_id": "9a8254639885e12e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-442", "record_id": "Foster v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-442", "pinpoint_status": "slip-only", "quote": "## Issue Whether a pretrial identification procedure can be so unnecessarily suggestive and conducive to mistaken identification that admitting the resulting identification denies the defendant due process of law. ## Rule Yes. Even apart from the right-to-counsel rule of *Wade*/*Gilbert* (inapplicable to pre-1967 lineups),", "quote_fidelity": "mismatch", "record_id": "Foster v. California", "star_marker": null}}
{"assertion_id": "b3ce630ad9fb899d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Foster v. California"}, "payload": {"as_of_content": "1969-04-01", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Foster v. California", "scope_note": "Good law; the rare case in which the Court found a pretrial identification so suggestive as to violate due process (noted as such in Perry v. New Hampshire).", "varies_by_point": false}}
```

### lake record — Foster v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Foster v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Foster v. California",
    "case_name_short": "Foster",
    "case_name_full": "Foster v. California",
    "input_case_name": "Foster v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1969-04-01",
    "year": 1969,
    "docket": "47",
    "cluster_id": 107890,
    "lead_opinion_id": 107890,
    "sibling_ids": [
      107890,
      9423977,
      9423978
    ],
    "absolute_url": "/opinion/107890/foster-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "394 U.S. 440",
      "volume": "394",
      "reporter": "U.S.",
      "page": "440",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "89 S. Ct. 1127",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "1127",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 L. Ed. 2d 402",
        "volume": "22",
        "reporter": "L. Ed. 2d",
        "page": "402",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1969 U.S. LEXIS 2050",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "2050",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "394 U.S. 440",
        "volume": "394",
        "reporter": "U.S.",
        "page": "440",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 S. Ct. 1127",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "1127",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 L. Ed. 2d 402",
        "volume": "22",
        "reporter": "L. Ed. 2d",
        "page": "402",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1969 U.S. LEXIS 2050",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "2050",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "394 U.S. 440",
    "official_selection": {
      "court_class": "scotus",
      "selected": "394 U.S. 440",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-442",
      "page": null,
      "quote": "## Issue Whether a pretrial identification procedure can be so unnecessarily suggestive and conducive to mistaken identification that admitting the resulting identification denies the defendant due process of law. ## Rule Yes. Even apart from the right-to-counsel rule of *Wade*/*Gilbert* (inapplicable to pre-1967 lineups),",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-443",
      "page": null,
      "quote": "The suggestive elements in this identification procedure made it all but inevitable that David would identify petitioner whether or not he was in fact 'the man.' In effect, the police repeatedly said to the witness, 'This is the man.' ... This procedure so undermined the reliability of the eyewitness identification as to violate due process.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1969-04-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Foster v. California",
    "varies_by_point": false,
    "scope_note": "Good law; the rare case in which the Court found a pretrial identification so suggestive as to violate due process (noted as such in Perry v. New Hampshire).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Dickson",
          "cluster_id": 4244499,
          "cite": [
            "141 A.3d 810",
            "322 Conn. 410",
            "2016 Conn. LEXIS 236"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Newman",
          "cluster_id": 2791286,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Carl Leonard Lively v. State",
          "cluster_id": 3100720,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Guidry",
          "cluster_id": 37891,
          "cite": [
            "406 F.3d 314",
            "2005 U.S. App. LEXIS 5607",
            "2005 WL 768764"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "James David Carter v. Ricky Bell, Warden Paul Summers, Attorney General",
          "cluster_id": 769405,
          "cite": [
            "218 F.3d 581",
            "2000 U.S. App. LEXIS 15651",
            "2000 F. App'x 0221P"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hull v. State",
          "cluster_id": 1142679,
          "cite": [
            "607 So. 2d 369",
            "1992 WL 201066"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Glover v. State",
          "cluster_id": 1639517,
          "cite": [
            "787 S.W.2d 544",
            "1990 Tex. App. LEXIS 1050",
            "1990 WL 59411"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Neil v. Biggers",
          "cluster_id": 108639,
          "cite": [
            "34 L. Ed. 2d 401",
            "93 S. Ct. 375",
            "409 U.S. 188",
            "1972 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baker v. McCollan",
          "cluster_id": 110132,
          "cite": [
            "61 L. Ed. 2d 433",
            "99 S. Ct. 2689",
            "443 U.S. 137",
            "1979 U.S. LEXIS 141"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Manson v. Brathwaite",
          "cluster_id": 109693,
          "cite": [
            "53 L. Ed. 2d 140",
            "97 S. Ct. 2243",
            "432 U.S. 98",
            "1977 U.S. LEXIS 116"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Young",
          "cluster_id": 111353,
          "cite": [
            "84 L. Ed. 2d 1",
            "105 S. Ct. 1038",
            "470 U.S. 1",
            "1985 U.S. LEXIS 49",
            "53 U.S.L.W. 4159"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barefoot v. Estelle",
          "cluster_id": 111017,
          "cite": [
            "77 L. Ed. 2d 1090",
            "103 S. Ct. 3383",
            "463 U.S. 880",
            "1983 U.S. LEXIS 110",
            "51 U.S.L.W. 5189",
            "13 Fed. R. Serv. 449"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
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
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kirby v. Illinois",
          "cluster_id": 108554,
          "cite": [
            "32 L. Ed. 2d 411",
            "92 S. Ct. 1877",
            "406 U.S. 682",
            "1972 U.S. LEXIS 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
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
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Coleman v. Alabama",
          "cluster_id": 108182,
          "cite": [
            "26 L. Ed. 2d 387",
            "90 S. Ct. 1999",
            "399 U.S. 1",
            "1970 U.S. LEXIS 17"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gimmy v. People",
          "cluster_id": 1231296,
          "cite": [
            "645 P.2d 262",
            "1982 Colo. LEXIS 568"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gregory v. City of Louisville",
          "cluster_id": 2973641,
          "cite": [
            "444 F.3d 725",
            "2006 WL 909935"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Manuel Concepcion, Roberto Aponte, and Nelson Frias",
          "cluster_id": 597808,
          "cite": [
            "983 F.2d 369"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Watkins v. Sowders",
          "cluster_id": 110371,
          "cite": [
            "66 L. Ed. 2d 549",
            "101 S. Ct. 654",
            "449 U.S. 341",
            "1981 U.S. LEXIS 53",
            "49 U.S.L.W. 4082"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gray v. State",
          "cluster_id": 1666205,
          "cite": [
            "728 So. 2d 36",
            "1998 WL 452320"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Frank Howard v. Barbara Bouchard, Warden",
          "cluster_id": 789998,
          "cite": [
            "405 F.3d 459",
            "2005 U.S. App. LEXIS 7271",
            "2005 WL 976980"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mattas",
          "cluster_id": 1231857,
          "cite": [
            "645 P.2d 254"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ex Parte Adams",
          "cluster_id": 1784512,
          "cite": [
            "768 S.W.2d 281",
            "1989 Tex. Crim. App. LEXIS 39",
            "1989 WL 16461"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Anderson",
          "cluster_id": 2222943,
          "cite": [
            "205 N.W.2d 461",
            "389 Mich. 155",
            "1973 Mich. LEXIS 99"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Diaz",
          "cluster_id": 75261,
          "cite": [
            "248 F.3d 1065",
            "2001 WL 392392"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alex Wong, Roger Kwok, Chen I. Chung, Tung Tran, Danny Ngo, Brian Chan, Joseph Wang, Chiang T. Cheng, and Steven Ng",
          "cluster_id": 683141,
          "cite": [
            "40 F.3d 1347",
            "1994 U.S. App. LEXIS 31286"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hernandez-Cuevas v. Taylor",
          "cluster_id": 1034188,
          "cite": [
            "723 F.3d 91",
            "2013 U.S. App. LEXIS 14469",
            "2013 WL 3742484"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gregory v. City of Louisville",
          "cluster_id": 793983,
          "cite": [
            "444 F.3d 725"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Foster v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107890 OR 9423977 OR 9423978) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NjIzNzc2MDAwMDAmcz01MTI4ODgzJnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107890+OR+9423977+OR+9423978%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 8,
        "triage_snippet_classified": 192
      },
      "lane2_top_cited": {
        "query": "cites:(107890 OR 9423977 OR 9423978)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTQmcz0xODExMzkyJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107890+OR+9423977+OR+9423978%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107890 OR 9423977 OR 9423978)",
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
    "complete_query": "cites:(107890 OR 9423977 OR 9423978)",
    "indexed_citing_opinions": 722,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107890,
        "count": 667,
        "count_source": "search"
      },
      {
        "opinion_id": 9423977,
        "count": 71,
        "count_source": "search"
      },
      {
        "opinion_id": 9423978,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1048,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/foster-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcxMzcwMyZzPTQ4NTY3MjgmdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28107890+OR+9423977+OR+9423978%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107890,
        "cited_id": 102885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 107638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 107685,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 107821,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 1184080,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 1341981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107890,
        "cited_id": 1376991,
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
    "date_created": "2026-07-05T04:37:49Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T04:38:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T04:38:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T04:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T04:38:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Foster v. California

```
<div>
<center><b><span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">394 U.S. 440</a></span> (1969)</b></center>
<center><h1>FOSTER<br>
v.<br>
CALIFORNIA.</h1></center>
<center>No. 47.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 19, 1968.</center>
<center>Decided April 1, 1969.</center>
CERTIORARI TO THE COURT OF APPEAL OF CALIFORNIA, FIFTH APPELLATE DISTRICT.
<p><i>Kenneth L. Maddy,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./391/902/">391 U. S. 902</a></span>, argued the cause and filed briefs for petitioner.</p>
<p><i>Doris H. Maier,</i> Assistant Attorney General of California, argued the cause for respondent. With her on the brief were <i>Thomas C. Lynch,</i> Attorney General, and <i>Charles P. Just,</i> Deputy Attorney General.</p>
<p><span class="star-pagination">*441</span> MR. JUSTICE FORTAS delivered the opinion of the Court.</p>
<p>Petitioner was charged by information with the armed robbery of a Western Union office in violation of California Penal Code § 211a. The day after the robbery one of the robbers, Clay, surrendered to the police and implicated Foster and Grice. Allegedly, Foster and Clay had entered the office while Grice waited in a car. Foster and Grice were tried together. Grice was acquitted. Foster was convicted. The California District Court of Appeal affirmed the conviction; the State Supreme Court denied review. We granted certiorari, limited to the question whether the conduct of the police lineup resulted in a violation of petitioner's constitutional rights. <span class="citation multiple-matches"><a href="/c/U.%20S./390/994/">390 U. S. 994</a></span> (1968).</p>
<p>Except for the robbers themselves, the only witness to the crime was Joseph David, the late-night manager of the Western Union office. After Foster had been arrested, David was called to the police station to view a lineup. There were three men in the lineup. One was petitioner. He is a tall manclose to six feet in height. The other two men were shortfive feet, five or six inches. Petitioner wore a leather jacket which David said was similar to the one he had seen underneath the coveralls worn by the robber. After seeing this lineup, David could not positively identify petitioner as the robber. He "thought" he was the man, but he was not sure. David then asked to speak to petitioner, and petitioner was brought into an office and sat across from David at a table. Except for prosecuting officials there was no one else in the room. Even after this one-to-one confrontation David still was uncertain whether petitioner was one of the robbers: "truthfully I was not sure," he testified at trial. A week or 10 days later, the police arranged for David to view a second lineup. There were five men in that lineup. Petitioner was the only person in the second lineup who had <span class="star-pagination">*442</span> appeared in the first lineup. This time David was "convinced" petitioner was the man.</p>
<p>At trial, David testified to his identification of petitioner in the lineups, as summarized above. He also repeated his identification of petitioner in the courtroom. The only other evidence against petitioner which concerned the particular robbery with which he was charged was the testimony of the alleged accomplice Clay.<sup>[1]</sup></p>
<p>In <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), and <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967), this Court held that because of the possibility of unfairness to the accused in the way a lineup is conducted, a lineup is a "critical stage" in the prosecution, at which the accused must be given the opportunity to be represented by counsel. That holding does not, however, apply to petitioner's case, for the lineups in which he appeared occurred before June 12, 1967. <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span> (1967). But in declaring the rule of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i> to be applicable only to lineups conducted after those cases were decided, we recognized that, judged by the "totality of the circumstances," the conduct of identification procedures may be "so unnecessarily suggestive and conducive to irreparable mistaken identification" as to be a denial of due process of law. <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#302" aria-description="Citation for case: Gilbert v. California"><i>Id.,</i> at 302</a></span>. See <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#383" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 383</a></span> (1968); cf. P. Wall, Eye-Witness Identification in Criminal Cases; J. Frank &amp; B. Frank, Not Guilty; 3 J. Wigmore, Evidence § 786<i>a</i> (3d ed. 1940); 4, <i>id.,</i> § 1130.</p>
<p>Judged by that standard, this case presents a compelling example of unfair lineup procedures.<sup>[2]</sup> In the <span class="star-pagination">*443</span> first lineup arranged by the police, petitioner stood out from the other two men by the contrast of his height and by the fact that he was wearing a leather jacket similar to that worn by the robber. See <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#233" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 233</a></span>. When this did not lead to positive identification, the police permitted a one-to-one confrontation between petitioner and the witness. This Court pointed out in <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> that "[t]he practice of showing suspects singly to persons for the purpose of identification, and not as part of a lineup, has been widely condemned." 388 U. S., at 302. Even after this the witness' identification of petitioner was tentative. So some days later another lineup was arranged. Petitioner was the only person in this lineup who had also participated in the first lineup. See Wall, <i>supra,</i> at 64. This finally produced a definite identification.</p>
<p>The suggestive elements in this identification procedure made it all but inevitable that David would identify petitioner whether or not he was in fact "the man." In effect, the police repeatedly said to the witness, "<i>This</i> is the man." See <i>Biggers</i> v. <i>Tennessee,</i> <span class="citation" data-id="9423641"><a href="/opinion/107638/biggers-v-tennessee/#407" aria-description="Citation for case: Biggers v. Tennessee">390 U. S. 404, 407</a></span> (dissenting opinion). This procedure so undermined the reliability of the eyewitness identification as to violate due process.</p>
<p>In a decision handed down since the Supreme Court of California declined to consider petitioner's case, it reversed a conviction because of the unfair makeup of a lineup. In that case, the California court said: "[W]e do no more than recognize . . . that unfairly constituted lineups have in the past too often brought about the conviction of the innocent." <i>People</i> v. <i>Caruso,</i> <span class="citation" data-id="9551395"><a href="/opinion/1184080/people-v-caruso/#188" aria-description="Citation for case: People v. Caruso">68 Cal. 2d 183, 188</a></span>, <span class="citation" data-id="9551395"><a href="/opinion/1184080/people-v-caruso/#340" aria-description="Citation for case: People v. Caruso">436 P. 2d 336, 340</a></span> (1968). In the present case the pretrial confrontations clearly were so arranged as to make the resulting identifications virtually inevitable.</p>
<p><span class="star-pagination">*444</span> The respondent invites us to hold that any error was harmless under <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967). We decline to rule upon this question in the first instance. Accordingly, the judgment is reversed and the case remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>Reversed and remanded.</i></p>
<p>MR. JUSTICE WHITE, with whom MR. JUSTICE HARLAN and MR. JUSTICE STEWART concur, being unwilling in this case to disagree with the jury on the weight of the evidence, would affirm the judgment.</p>
<p>MR. JUSTICE BLACK, dissenting.</p>
<p>The Court here directs the California courts to set aside petitioner Foster's conviction for armed robbery of the Western Union Telegraph Co. at Fresno, California. The night manager of the telegraph company testified before the court and jury that two men came into the office just after midnight, January 25, 1966, wrote a note telling him it was a holdup, put it under his face, and demanded money, flashed guns, took $531 and fled. The night manager identified Foster in the courtroom as one of the men, and he also related his identification of Foster in a lineup a week or so after the crime. The manager's evidence, which no witness disputed, was corroborated by the testimony of a man named Clay, who was Foster's accomplice in the robbery and who testified for the State. The testimony of these two eyewitnesses was also corroborated by proof that Foster and another person had committed a prior armed robbery of a Western Union office in another city six years before, when they appeared at the company's office, presented a note to an employee announcing their holdup, flashed a gun, and fled with company money. In this case Foster's attorney admitted conviction <span class="star-pagination">*445</span> for the prior Western Union armed robbery.<sup>[1]</sup> The circumstances of the two robberies appear to have been practically indistinguishable. Such evidence that a particular person committed a prior crime has been almost universally accepted as relevant and admissible to prove that the same person was responsible for a later crime of the same nature.<sup>[2]</sup> A narration of these facts, falling from the lips of eyewitnesses, and not denied by other eyewitnesses, would be enough, I am convinced, to persuade nearly all lawyers and judges, unhesitatingly to say, "There was clearly enough evidence of guilt here for a jury to convict the defendant since, according to practice, and indeed constitutional command, the weight of evidence is for a jury, and not for judges." Nevertheless the Court in this case looks behind the evidence given by witnesses on the stand and decides that because of the circumstances under which one witness first identified the defendant as the criminal, the United States Constitution requires that the conviction be reversed. The Court, however, fails to spell out exactly what should happen to this defendant if there must be a retrial, and thus avoids the apparently distasteful task of specifying whether (1) at the new trial the jury would again be permitted to hear the eyewitness' testimony and the in-court identification, so long as he does not refer to the previous lineups, or (2) the eyewitness' "tainted" identification testimony must be entirely excluded, thus compelling Foster's acquittal. Objection to this ambiguity is the first of my reasons for dissent.</p>
<p></p>
<h2>
<span class="star-pagination">*446</span> I.</h2>
<p>The Court declares the judgment of conviction is reversed and the case remanded for further proceedings not inconsistent with this opinion. I am compelled to say that if I were the trial judge in this case I would not know how to proceed or how to decide whether the "error" in this case was harmless. Of course, when a confession is held to have been compelled, that confession must not be admitted to convict the defendant at all. But the situation in this case is not that simple. For the Court has in effect decided here that the officers of the law have so "arranged" lineups that the eyewitness to the robbery has been led to make an "irreparable mistaken identification." In other words, no one now or hereafter can believe his identification of Foster as the robber. Since he and the accomplice are the only eyewitnesses, and since, in order to convict, California law requires evidence of an accomplice to be corroborated, the Court's direction means, I suppose, that the trial judge here should dismiss the case.<sup>[3]</sup> The Court's dilemma, which leads to its ambiguous judgment as to the further disposition of this case, points, I think, to the irreparable harm done to the cause of justice by the Court's holding in this case.</p>
<p></p>
<h2>II.</h2>
<p>Far more fundamental, however, is my objection to the Court's basic holding that evidence can be ruled constitutionally inadmissible whenever it results from identification <span class="star-pagination">*447</span> procedures that the Court considers to be " `unnecessarily suggestive and conducive to irreparable mistaken identification.' "<sup>[4]</sup> One of the proudest achievements of this country's Founders was that they had eternally guaranteed a trial by jury in criminal cases, at least until the Constitution they wrote had been amended in the manner they prescribed. Only last year in <i>Duncan</i> v. <i>Louisiana,</i> <span class="citation" data-id="9423691"><a href="/opinion/107685/duncan-v-louisiana/" aria-description="Citation for case: Duncan v. Louisiana">391 U. S. 145</a></span> (1968), this Court emphatically decided, over strong dissents, that this constitutional right to trial by jury in criminal cases is applicable to the States. Of course it is an incontestable fact in our judicial history that the jury is the sole tribunal to weigh and determine facts. That means that the jury must, if we keep faith with the Constitution, be allowed to hear eyewitnesses and decide for itself whether it can recognize the truth and whether they are telling the truth. It means that the jury must be allowed to decide for itself whether the darkness of the night, the weakness of a witness' eyesight, or any other factor impaired the witness' ability to make an accurate identification. To take that power away from the jury is to rob it of the responsibility to perform the precise functions the Founders most wanted it to perform. And certainly a Constitution written to preserve this indispensable, unerodible core of our system for trying criminal cases would not have included, hidden among its provisions, a slumbering sleeper granting the judges license to destroy trial by jury in whole or in part.</p>
<p>This brings me to the constitutional theory relied upon by the Court to justify its invading the constitutional right of jury trial. The Court here holds that:</p>
<blockquote>"[J]udged by the `totality of the circumstances,' the conduct of identification procedures may be `so <span class="star-pagination">*448</span> unnecessarily suggestive and conducive to irreparable mistaken identification' as to be a denial of due process of law. . . .</blockquote>
<blockquote>"Judged by that standard, this case presents a compelling example of unfair lineup procedures." <i>Ante,</i> at 442.</blockquote>
<p>I do not deny that the "totality of circumstances" can be considered to determine whether some specific constitutional prohibitions have been violated, such, for example, as the Fifth Amendment's command against compelling a witness to incriminate himself. Whether evidence has been compelled is, of course, a triable issue of fact. And the constitutional command not to compel a person to be a witness against himself, like other issues of fact, must be determined by a resolution of all facts and the "totality" of them offered in evidence. Consequently were the Court's legal formula posed for application in a coerced testimony case, I could agree to it. But it is not. Instead the Court looks to the "totality of circumstances" to show "unfair lineup procedures." This means "unfair" according to the Court's view of what is unfair. The Constitution, however, does not anywhere prohibit conduct deemed unfair by the courts. As we recently said in <i>United States</i> v. <i>Augenblick,</i> <span class="citation" data-id="107821"><a href="/opinion/107821/united-states-v-augenblick/#352" aria-description="Citation for case: United States v. Augenblick">393 U. S. 348, 352</a></span> (1969): "Rules of evidence are designed in the interests of fair trials. But unfairness in result is no sure measure of unconstitutionality."</p>
<p>The Constitution sets up its own standards of unfairness in criminal trials in the Fourth, Fifth, and Sixth Amendments, among other provisions of the Constitution. Many of these provisions relate to evidence and its use in criminal cases. The Constitution provides that the accused shall have the right to compulsory process for obtaining witnesses in his favor. It ordains that evidence shall not be obtained by compulsion of the accused. It ordains that the accused shall have the right to confront <span class="star-pagination">*449</span> the witnesses against him. In these ways the Constitution itself dictates what evidence is to be excluded because it was improperly obtained or because it is not sufficiently reliable. But the Constitution does not give this Court any general authority to require exclusion of all evidence that this Court considers improperly obtained or that this Court considers insufficiently reliable. Hearsay evidence, for example, is in most instances rendered inadmissible by the Confrontation Clause, which reflects a judgment, made by the Framers of the Bill of Rights, that such evidence may be unreliable and cannot be put in proper perspective by cross-examination of the person repeating it in court. Nothing in this constitutional plan suggests that the Framers drew up the Bill of Rights merely in order to mention a few types of evidence "for illustration," while leaving this Court with full power to hold unconstitutional the use of any other evidence that the Justices of this Court might decide was not sufficiently reliable or was not sufficiently subject to exposure by cross-examination. On the contrary, as we have repeatedly held, the Constitution leaves to the States and to the people all these questions concerning the various advantages and disadvantages of admitting certain types of evidence. <i>Spencer</i> v. <i>Texas,</i> <span class="citation" data-id="9423324"><a href="/opinion/107342/spencer-v-texas/" aria-description="Citation for case: Spencer v. Texas">385 U. S. 554</a></span> (1967); <i>Michelson</i> v. <i>United States,</i> <span class="citation" data-id="9420246"><a href="/opinion/104607/michelson-v-united-states/" aria-description="Citation for case: Michelson v. United States">335 U. S. 469</a></span> (1948).</p>
<p>It has become fashionable to talk of the Court's power to hold governmental laws and practices unconstitutional whenever this Court believes them to be "unfair," contrary to basic standards of decency, implicit in ordered liberty, or offensive to "those canons of decency and fairness which express the notions of justice of English-speaking peoples . . . ."<sup>[5]</sup> All of these different general <span class="star-pagination">*450</span> and indefinable words or phrases are the fruit of the same, what I consider to be poisonous, tree, namely, the doctrine that this Court has power to make its own ideas of fairness, decency, and so forth, enforceable as though they were constitutional precepts. When I consider the incontrovertible fact that our Constitution was written to limit and define the powers of the Federal Government as distinguished from the powers of States, and to divide those powers granted the United States among the separate Executive, Legislative, and Judicial branches, I cannot accept the premise that our Constitution grants any powers except those specifically written into it, or absolutely necessary and proper to carry out the powers expressly granted.</p>
<p>I realize that some argue that there is little difference between the two constitutional views expressed below:</p>
<blockquote>One. No law should be held unconstitutional unless its invalidation can be firmly planted on a specific constitutional provision plus the Necessary and Proper Clause.</blockquote>
<blockquote>Two. All laws are unconstitutional that are unfair, shock the conscience of the Court, offend its sense of decency, or violate concepts implicit in ordered liberty.</blockquote>
<p>The first of these two constitutional standards plainly tells judges they have no power to hold laws unconstitutional unless such laws are believed to violate the written Constitution. The second constitutional standard, based on the words "due process," not only does not require judges to follow the Constitution as written, but actually encourages judges to hold laws unconstitutional on the basis of their own conceptions of fairness and justice. This formula imposes no "restraint" on judges beyond requiring them to follow their own best judgment as to what is wise, just, and best under the circumstances of a particular case. This case well illustrates the extremes <span class="star-pagination">*451</span> to which the formula can take men who are both wise and good. Although due process requires that courts summon witnesses so that juries can determine the guilt or innocence of defendants, the Court, because of its sense of fairness, decides that due process deprives juries of a chance to hear witnesses who the Court holds could not or might not tell the truth.</p>
<p>I began my opposition to this fallacious concept of "due process" even before I became a member of this Court<sup>[6]</sup> and expressed it formally soon after my service on the Court began.<sup>[7]</sup> And it was not long before I emphasized that quite a different belief about the meaning of the phrase "due process" had long existed in our judicial history in opposition to the "decency and fairness" doctrine. See <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#235" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227, 235-236, n. 8</a></span> (1940).</p>
<p>My experience on the Court has confirmed my early belief that the "decency and fairness" due process test cannot stand consistently with our written Constitution.</p>
<p></p>
<h2>III.</h2>
<p>I agree with the Court that we should not undertake to pass on the question of harmless error for the first time in this Court. Under the Court's holding, the case should be remanded to the state courts for decision of this question.</p>
<p>In recent years this Court has, in a series of cases, held that most of the Bill of Rights is now applicable against the States as well as against the Federal Government. This has brought about a tremendous increase in the number of state criminal cases involving federal questions, some of which depend on the particular facts and circumstances of the case. In Fifth Amendment <span class="star-pagination">*452</span> confession cases, for example, courts must under prevailing practice hear evidence to determine whether confessions were compelled. This Court has power in cases of that kind to review evidence before the trial courts. No one can now predict with accuracy how great a number of such cases are destined to come before us, but all know it will be many. Should we not make it an almost invariable practice to accept lower court findings of fact on such issues, our Supreme Court is likely to find itself pre-occupied with the business of a state court of criminal appeals, a condition not devoutly to be wished in the Court's interest or in the interest of the administration of justice in general. This problem is magnified many times over when account is taken of the harmless-error rules that many States have now adopted, since these rules also raise factual issues involving a federal question whenever the error itself is federal. See <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967). If trial errors are found some courts along the line must determine whether the error was harmless. That question has, because of this Court's judgment, now arisen in this case. I agree with the Court that we should not decide this question here. In the present posture of criminal law, there are simply too many federal questions in the state cases before us to defend a practice of our deciding in the first instance that there was no harmless error. There are many reasons for this other than the necessity of saving our time for the vastly more important issues we must decide. To say the least, the question whether an error in a particular case is harmless is an issue peculiarly for lower, not for the highest, appellate courts. Then, too, this issue can usually be tried more efficiently, and just as fairly, by the local court that tried the case or by the local appellate court that heard the first appeal. This Court was not established to try such minor issues of fact for the first time. Of course, I do not mean to suggest that <span class="star-pagination">*453</span> there should be an ironclad rule always barring the Court from deciding an issue in cases if it plainly and manifestly appears that it would be egregiously unjust and undoubtedly wrong to leave an issue undecided. But I do not think this even distantly approaches being such a case. Even though I steadfastly believe the Court's basic holding is error, I do agree that we should not establish a precedent of passing on harmless error for the first time in this Court before the courts below have had an opportunity to consider the question.</p>
<p>For the above reasons I dissent from the reversal and remand of this case.</p>
<h2>NOTES</h2>
<p>[1]  California law requires that an accomplice's testimony be corroborated. California Penal Code § 1111. There was also evidence that Foster had been convicted for a similar robbery committed six years before.</p>
<p>[2]  The reliability of properly admitted eyewitness identification, like the credibility of the other parts of the prosecution's case is a matter for the jury. But it is the teaching of <i>Wade, Gilbert,</i> and <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall, supra,</a></span></i> that in some cases the procedures leading to an eyewitness identification may be so defective as to make the identification constitutionally inadmissible as a matter of law.</p>
<p>[1]  Counsel also admitted a prior felony conviction of assault with intent to commit rape, a circumstance relevant in California in connection with punishment.</p>
<p>[2]  See <i>Spencer</i> v. <i>Texas,</i> <span class="citation" data-id="9423324"><a href="/opinion/107342/spencer-v-texas/" aria-description="Citation for case: Spencer v. Texas">385 U. S. 554</a></span>, 560-561 and n. 7 (1967); <i>State</i> v. <i>Chance,</i> <span class="citation" data-id="1168782"><a href="/opinion/1168782/state-v-chance/" aria-description="Citation for case: State v. Chance">92 Ariz. 351</a></span>, <span class="citation" data-id="1168782"><a href="/opinion/1168782/state-v-chance/" aria-description="Citation for case: State v. Chance">377 P. 2d 197</a></span> (1962); <i>Nester</i> v. <i>State,</i> <span class="citation" data-id="1376991"><a href="/opinion/1376991/nester-v-state/" aria-description="Citation for case: Nester v. State">75 Nev. 41</a></span>, <span class="citation" data-id="1376991"><a href="/opinion/1376991/nester-v-state/" aria-description="Citation for case: Nester v. State">334 P. 2d 524</a></span> (1959); <i>Mosley</i> v. <i>State,</i> <span class="citation" data-id="1341981"><a href="/opinion/1341981/mosley-v-state/" aria-description="Citation for case: Mosley v. State">211 Ga. 611</a></span>, <span class="citation" data-id="1341981"><a href="/opinion/1341981/mosley-v-state/" aria-description="Citation for case: Mosley v. State">87 S. E. 2d 314</a></span> (1955); 2 J. Wigmore, Evidence § 416 (3d ed. 1940 and 1964 Supp.).</p>
<p>[3]  The Court apparently means that the only other evidence against Foster in this casehis prior conviction for involvement in a crime of a similar typeis constitutionally admissible. See <i>Spencer</i> v. <i><span class="citation" data-id="9423324"><a href="/opinion/107342/spencer-v-texas/" aria-description="Citation for case: Spencer v. Texas">Texas, supra</a></span></i><i>.</i> But it may be doubtful whether this past conviction, although highly relevant to the question of guilt, could constitute corroboration of the accomplice's testimony, within the meaning of the California requirement.</p>
<p>[4]  <i>Ante,</i> at 442, quoting from <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#302" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293, 302</a></span> (1967).</p>
<p>[5]  <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#417" aria-description="Citation for case: Malinski v. New York">324 U. S. 401, 417</a></span> (opinion of Frankfurter, J.) (1945); see also <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952); <i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">347 U. S. 128</a></span> (1954).</p>
<p>[6]  See, <i>e. g.,</i> 81 Cong. Rec. App., pt. 9, pp. 638-639; <i>id.,</i> at 307.</p>
<p>[7]  See, <i>e. g., </i><i>McCart</i> v. <i>Indianapolis Water Co.,</i> <span class="citation" data-id="9418947"><a href="/opinion/102885/mccart-v-indianapolis-water-co/#423" aria-description="Citation for case: McCart v. Indianapolis Water Co.">302 U. S. 419, 423</a></span> (1938) (dissenting opinion).</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Frank v. Maryland.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Frank v. Maryland
type: case
citation: "359 U.S. 360 (1959)"
parallel_cite: "79 S. Ct. 804; 3 L. Ed. 2d 877"
neutral_cite: 1959 U.S. LEXIS 1085
court: U.S.
court_level: scotus
circuit: ""
year: 1959
date_decided: 1959-05-04
docket: 278
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
  opinion_url: "https://www.courtlistener.com/opinion/105880/frank-v-maryland/"
  cluster_id: 105880
  opinion_id: null
  identity_checked: true
lake:
  record_id: Frank v. Maryland
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: Historical / origin
related:
  - "[[Camara v. Municipal Court]]"
  - "[[See v. City of Seattle]]"
tags:
  - case
  - fourth-amendment
  - administrative-search
  - special-needs
  - housing-inspection
  - overruled
  - historical
holding: "A municipal health inspector could demand entry to a home to look for nuisance conditions without a warrant, enforced by a fine for refusal, without violating the Due Process Clause — a rule overruled eight years later by Camara v. Municipal Court (1967), which required warrants for administrative inspections."
---

# Frank v. Maryland

*359 U.S. 360 (1959)* (No. 278) · Supreme Court of the United States · **Historical** · Treatment: **Overruled — rendered as history (⚪ unverified, pending S9)** — overruled by [[Camara v. Municipal Court]] (1967)
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the subsequent-history treatment below is authored orientation, not machine-certified. Identity cluster 105880 → 359 U.S. 360, decided 1959-05-04; Rule quote string-matched to the CL opinion text 2026-07-07. -->

## Background
A Baltimore health inspector, investigating a rat-infestation complaint, came to Aaron Frank's home and asked to inspect it for conditions the City Health Code proscribed. Frank refused to admit him without a warrant. Under § 120 of the Code, that refusal was itself an offense, and Frank was convicted and fined $20. He challenged the conviction, arguing that punishing him for resisting a warrantless inspection of his home violated the Fourteenth Amendment.

## Issue
Whether conditioning a criminal penalty on a homeowner's refusal to admit a health inspector, who has no warrant, to search the home for code violations is consistent with the Due Process Clause of the Fourteenth Amendment.

## Rule
The Court (Frankfurter, J.) upheld the ordinance. It reasoned that a routine, area-based health inspection touches only the periphery of the privacy the Fourteenth Amendment protects, is hedged with safeguards (advance notice, no forced entry), and serves a long-settled public-health function. Weighing that limited intrusion against the community's interest, the Court concluded: "In light of the long history of this kind of inspection and of modern needs, we cannot say that the carefully circumscribed demand which Maryland here makes on appellant's freedom has deprived him of due process of law." — 359 U.S. at 373. ^pin-373

## Application
Because the inspector could not force entry and the only consequence of refusal was a modest fine — not a search of the home over the occupant's objection — the Court treated the demand as a reasonable administrative measure rather than the kind of criminal search the warrant requirement governs. The [[Common Legal Terms#dissenting-opinion|dissent]] (Douglas, J., joined by Warren, C.J., Black and Brennan, JJ.) warned that the decision let officials into the home without the warrant the Fourth Amendment was written to require.

## Conclusion
The conviction was **affirmed** by a 5–4 vote. Frankfurter, J., delivered the opinion of the Court.

## Treatment & subsequent history
**Overruled by [[Camara v. Municipal Court]] (1967).** *Frank* held that administrative inspections of the home fall outside the warrant requirement. Eight years later *[[Camara v. Municipal Court|Camara]]* rejected that view, holding that administrative searches are significant Fourth Amendment intrusions and generally require a warrant — though one issued on area-based "administrative probable cause" rather than individualized suspicion. Its companion case, *[[See v. City of Seattle]]*, applied the same rule to commercial premises.

*Status note (⚪):* authored from a CourtListener-verified identity stub; the overruled treatment above is well-settled but has not completed the project's two-key certification, so the page renders under the ⚪ banner until S9 promotion. Preserved as **history**, never as live law.

## Appears on
- [[Special Needs and Administrative Searches]] — *Historical / origin*

## Sources
- [*Frank v. Maryland*, 359 U.S. 360 (1959)](https://www.courtlistener.com/opinion/105880/frank-v-maryland/) — pinpoint: 373 (Opinion of the Court; Frankfurter, J.); Rule quote string-matched to the CL opinion text 2026-07-07. Overruled by *Camara v. Municipal Court*, 387 U.S. 523 (1967) (successor page: [[Camara v. Municipal Court]]).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c0dfb2edec187bf2", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Frank v. Maryland"}, "payload": {"all": [{"cite": "359 U.S. 360", "page": "360", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "359"}, {"cite": "79 S. Ct. 804", "page": "804", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "79"}, {"cite": "3 L. Ed. 2d 877", "page": "877", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "3"}, {"cite": "1959 U.S. LEXIS 1085", "page": "1085", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1959"}], "display": "359 U.S. 360", "official": {"cite": "359 U.S. 360", "page": "360", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "359"}, "official_selection_present": true, "record_id": "Frank v. Maryland"}}
{"assertion_id": "a6f9e91e312152c5", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Frank v. Maryland"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Frank v. Maryland", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Frank v. Maryland

```json
{
  "schema_version": "s2.v1",
  "record_id": "Frank v. Maryland",
  "status": "under_review",
  "identity": {
    "case_name": "Frank v. Maryland",
    "case_name_short": "Frank",
    "case_name_full": "Frank v. Maryland",
    "input_case_name": "Frank v. Maryland",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1959-05-04",
    "year": 1959,
    "docket": "278",
    "cluster_id": 105880,
    "lead_opinion_id": 9421796,
    "sibling_ids": [],
    "absolute_url": "/opinion/105880/frank-v-maryland/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "359 U.S. 360",
      "volume": "359",
      "reporter": "U.S.",
      "page": "360",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "79 S. Ct. 804",
        "volume": "79",
        "reporter": "S. Ct.",
        "page": "804",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "3 L. Ed. 2d 877",
        "volume": "3",
        "reporter": "L. Ed. 2d",
        "page": "877",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1959 U.S. LEXIS 1085",
        "volume": "1959",
        "reporter": "U.S. LEXIS",
        "page": "1085",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "359 U.S. 360",
        "volume": "359",
        "reporter": "U.S.",
        "page": "360",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 S. Ct. 804",
        "volume": "79",
        "reporter": "S. Ct.",
        "page": "804",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "3 L. Ed. 2d 877",
        "volume": "3",
        "reporter": "L. Ed. 2d",
        "page": "877",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1959 U.S. LEXIS 1085",
        "volume": "1959",
        "reporter": "U.S. LEXIS",
        "page": "1085",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "359 U.S. 360",
    "official_selection": {
      "court_class": "scotus",
      "selected": "359 U.S. 360",
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
    "date_created": "2026-07-07T13:27:55Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:28:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:28:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:28:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:28:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "frank-v-maryland--105880",
      "to_record_id": "Frank v. Maryland",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Frank v. Maryland

```
<opinion type="majority">
<author id="b431-4"><page-number citation-index="1" label="361">*361</page-number>Mr. Justice Frankfurter</author>
<p id="Az-">delivered the opinion of the Court.</p>
<p id="b431-5">Acting on a complaint from a resident of the 4300 block of Reisterstown Road, Baltimore, Maryland, that there were rats in her basement, Gentry, an inspector of the Baltimore City Health Department, began an. inspection of the houses in the vicinity looking for the source of the rats. In the middle of the afternoon of February 27, 1958, Gentry knocked on the door of appellant’s detached frame home at 4335 Reisterstown Road. After receiving no response he proceeded to inspect the area outside the house. This inspection revealed that the house was in an “extreme state of decay,” and that in the rear of the house there was a pile later identified as “rodent feces mixed with, straw and trash and debris to approximately half a ton.” During this inspection appellant came around the side of the house and asked Gentry to explain, his presence. Gentry responded that he had evidence of rodent infestation and asked appellant for permission to inspect the basement area. Appellant refused. At no time did Gentry have a warrant authorizing him to enter. The next forenoon Gentry, in the company of two police officers, returned to appellant’s house. After receiving no response to his knock, he reinspécted the exterior of the premises. He then swore out a warrant for appellant’s arrest alleging a violation of § 120 of Art. 12 of the Baltimore City Code. That section provides: <page-number citation-index="1" label="362">*362</page-number>Appellant was arrested on March 5, and the next'day was found guilty of the offense alleged in the warrant by a Police Justice for the Northern District .of Baltimore and fined twenty dollars. Ón appeal, the Criminal Court of Baltimore, in a <em>de novo </em>proceeding, also found appellant guilty. The Maryland Court of Appeals denied certio-rari. . The case came here under a challenge, <span class="citation no-link">28 U. S. C. § 1257</span> (2), to the validity of § 120 to determine whether appellant’s conviction for resisting an inspection of his house without a warrant was obtained in violation of the Fourteenth Amendment.</p>
<blockquote id="AYK"><page-number citation-index="1" label="361">*361</page-number>“Whenever the Commissioner of Health shall have cause to suspect that a nuisance exists in any house, cellar or enclosure, he may demand entry therein in the day time, and if the owner or occupier shall refuse or delay to open the same and admit a free examination, he shall forfeit and pay for every such refusal the sum of Twenty Dollars.”</blockquote>
<p id="b432-4"><page-number citation-index="1" label="362">*362</page-number>The Health.Code of the City of Baltimore, of which § 120 is an important part, deals with many of the multiform aspects of hygiene in modern urban, areas. A vital portion concerns the hygiene of housing. Typical of the content and method of enforcing its provisions is the section requiring that-“[e]very'dwelling and every part thereof shall.be kept clean and free-from any accumulation- of dirt, filth, rubbish, garbage or similar matter, and shall be kept free from vermin or rodent infestation.” Baltimore City Code; Art. 12, § 112. If the occupant of a building fails to meet this standard, he is notified by the Commissioner of Health to abate the substandard conditions.<footnotemark>1</footnotemark> Failure to remove these hazards to community health gives- rise to criminal prosecution. <em>Ibid. </em>The attempted inspection of appellant’s home was merely to ascertain the existence of evils to be corrected upon due notification or, in default of such correction, to be made the basis of punishment.</p>
<p id="AF0">We have said that “[t]he security of one’s privacy against arbitrary intrusion by the police” is fundamental to a free society and as such protected by the Fourteenth <page-number citation-index="1" label="363">*363</page-number>Amendment. <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span>. Application of the broad, restraints of due process compels inquiry into the naturé of the demand being made upon individual freedom in a particular context and the justification of social need on which the demand rests.</p>
<p id="b433-4">The history of the constitutional protection against official invasion of the citizen’s home makes explicit the human concerns which it was meant to respect. In years prior to the Revolution leading voices in England and the Colonies protested against the ransacking by Crown officers of the homes of citizens in séarch of evidence of crime or of illegally imported goods. The vivid memory by the newly independent Americans of these abuses produced the Fourth Amendment as a safeguard against such arbitrary official action by officers of the new Union, as like provisions had already found their way into State Constitutions.</p>
<p id="b433-5">In 1765, in England, what is properly called the great case of <em>Entick </em>v. <em>Carrington, </em>19 Howell’s State Trials, col. 1029, announced the principle of English law which became part of the Bill of Rights and whose basic protection has become imbedded in the concept of due process of law. It was there decided that English law did not allow officers of the Crown to break into a citizen’s home, under cover of a general executive warrant, to search for evidence of the utterance of libel. Among the reasons given for that decision were these:</p>
<blockquote id="b433-6">“It is very certain, that the law obligeth no man to accuse himself; because the necessary means of compelling self-accusation, falling upon the innocent' as well as the guilty, would be both cruel and unjust; and it should seem, that search for evidence is disallowed upon the -same principle. There tod the innocent would be confounded with the guilty.” <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Id.,</a></span> </em>at col. 1073.</blockquote>
<p id="b434-3"><page-number citation-index="1" label="364">*364</page-number>These were not novel pronouncements to the colonists. A few years earlier, in Boston, revenue' officers had been authorized to uso-Writs of Assistance, empowering them to search suspected places, inclúding private houses, for smuggled goods. In 1761 the validity of the use of the Writs was contested in the historic proceedings in Boston. James Otis attacked the Writ of Assistance because its use placed “the liberty of every man in the hands of every petty officer.” <footnotemark>2</footnotemark> His powerful argument so impressed itself first on his audience and later on the people of all the Colonies that President Adams' was in retrospect moved to say that “American Independence was then and there bórn.” <footnotemark>3</footnotemark> Many years later this Court, in <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, carefully reviewed, this history and pointed "out, as did. Lord Camden in <em>Entick v. Carrington, </em>that</p>
<blockquote id="b434-4">“. . ., the ‘unreasonable searches and seizures’ condemned in the Fourth Amendment are almost always made for the purpose of compelling a man to give</blockquote>
<blockquote id="b435-3"><page-number citation-index="1" label="365">*365</page-number>evidence against himself, which in criminal cases is condemned in the. Fifth Amendment; and compelling a man 'in a criminal case to be a witness against himself,’ which is condemned in the Fifth Amendment, throws light on the question as to what is an ‘unreasonable search and seizure’ within the meaning of the Fourth Amendment.” ' <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#633" aria-description="Citation for case: Boyd v. United States">116 U. S., at 633</a></span>.</blockquote>
<p id="b435-4">Against this background two protections emerge from the broad constitutional proscription of official invasion. The first of these is the right to be secure from intrusion into personal privacy, the right to shut* the door on officials óf the state unless their entry is under proper authority of law. The second, and intimately related protection, is self-protection: the right to resist unauthorized entry which has as its design the securing of information to fortify the coercive power of the state against the individual, information which may be used to effect a further deprivation of life or liberty or property. Thus, evidence of criminal action may not, save in very limited and closely confined situations, be seized without a judicially issued search warrant. It is this aspect of the constitutional protection to. which the quoted passages from <em>Entick </em>v. <em>Carrington </em>and <em>Boyd </em>v. <em>United States </em>refer. Certainly it is not necessary to accept any particular theory of the interrelationship of the Fourth and Fifth Amendments<footnotemark>4</footnotemark> to realize what history makes plain, that it was on the issue of the right to be secure from searches for evidence to be used in criminal prosecutions or for forfeitures that the great battle for fundamental liberty was fought. While these concerns for individual rights were the historic impulses behind the Fourth Amendment and its analogues in state constitutions, the application <page-number citation-index="1" label="366">*366</page-number>of the Fourth Amendment and\the extent to which the essential right of privacy is protected by the Due Process Clause of the Fourteenth Amendment are of course not restricted within these historic bounds.</p>
<p id="A9oW">But giving the fullést scope to this constitutional right to privacy, its protection cannot be here invoked. The attempted inspection of appellant’s home is -merely to determine whether conditions exist which the Baltimore Health Code proscribes. If they do appellant is notified to remedy the infringing conditions. No evidence for criminal prosecution is sought to be seized. Appellant is simply directed to do what he could have been ordered to do without any inspection, and what he cannot properly resist, namely, act in a manner consistent with the maintenance of minimum community standards of health and well-being, including his own. Appellant’s resistance can only, be based, not on admissible self-protection, but on a rarely voiced denial of any official justification for seeking to enter his home. The constitutional “liberty” that is asserted is the absolute right to refuse consent for an inspéction designed and pursued solely for the protection of the community’s health, even when the inspection is conducted with due regard for every convenience of time and place.</p>
<p id="b436-5">• The power of inspection granted by the Baltimore City Code is strictly limited, moré exacting than the analogous provisions of many other municipal codes. ' Valid grounds for suspicion of the existence of a nuisance must exist. Certainly the presence of a pile of filth in the back yard combined with the run-down condition of the house gave adequate grounds for such suspicion. The inspection must be made in the day time. Here was no midnight knock on the door, but an orderly visit in the middle of the afternoon with no suggestion that the hour was inconvenient. Moreover, the inspector has no power to force <page-number citation-index="1" label="367">*367</page-number>entry and did not attempt it. A. fine is imposed for resistance, but officials are not authorized to break past the unwilling occupant.</p>
<p id="b437-5">Thus, not only does the inspection touch at most upon the periphery of the important interests safeguarded by the Fourteenth Amendment’s protection against official intrusion, but it is hedged about with safeguards designed to make the least possible demand on .the individual occupant, and to cause only the slightest restriction on his claims of privacy. Such a demand must be assessed in the light of thé needs which have produced it.</p>
<p id="b437-6">Inspection without a warrant, as an adjunct to a regulatory scheme for the general welfare, of the community and not as a means of enforcing the criminal law, has antecedents deep in our history. For more than 200 years Maryland has empowered its officers to enter upon ships, carriages', shops, and homes in the service of the common welfare. In pre-revolutionary days trade, on which the viability oh the struggling Colonies depended, was of primary concern. Thus, at a time when the' tobacco trade was a vital part of Maryland’s economy, inspections of ships and carriages without a warrant could be made' to enforce uniform' standards for packing and shipping tobacco.<footnotemark>5</footnotemark> Similarly, suspected evasion of import <page-number citation-index="1" label="368">*368</page-number>duties on liquor and other goods could be found out by-inspection of stores and homes.<footnotemark>6</footnotemark> Generally the power of entry' was carefully limited,, requiring that ground for suspicion must exist and that the inspection be conducted between “the rising and the setting of the sun.” <footnotemark>7</footnotemark></p>
<p id="A0Wc">In 1776 the newly independent State of Maryland incorporated, as part of its basic Declaration of Rights, the principle</p>
<blockquote id="b438-4">“That all warrants, without oath or affirmation, to search suspected places, or to seize any person or property, are grievous and oppressive; and all general warrants — to search suspected places, or to apprehend suspected persons, without naming or describing the place, or the person in special — are illegal, and ought not to be granted.” See 3 Thorpe, Federal-and State Constitutions (1909), 1688.</blockquote>
<p id="b438-5">This provision was a product of the same history of abuse and protest that gave birth to the Fourth ■ Amendment.<footnotemark>8</footnotemark> It remains today as an essential part of Maryland’s Constitution. Yet, the years following its proclamation saw not a decline but a'marked increase in statutory authorization for inspection of the citizen’s home. Not only were the old regulations continued, but the power of <page-number citation-index="1" label="369">*369</page-number>inspection was extended to new community concerns. In 1782, Commissioners were empowered to “enter upon the lots, grounds, and possessions, of any person or persons . ...” in order to regulate and keep in repair the common sewerage systems.<footnotemark>9</footnotemark> Five years later similar entries on private property were allowed for the purpose of keeping the public roads in repair.<footnotemark>10</footnotemark> Typical of the regulatory statutes enacted in this period was an act permitting the clerk of the market “to examine and weigh all such bread, and to seize, for the use of the poor of the county, all such as they shall find deficient in weight or fineness, and not baked or marked as aforesaid . .,. .” <footnotemark>11</footnotemark> The penalty for resisting the entry of the clerk was “five pounds current money.” And so; when, in 1801, the power of inspection without a warrant became an instrument of the enforcement of the Baltimore health laws, no novel or untried procedures' were being invoked. The ordinance now challenged derives from this 1801 ordinance. It provided:</p>
<blockquote id="b439-4">“And be it enanted and ordained, That when, and as often as. the said commissioners of health, or any of them, shall have cause-to suspect a nuisance dangerous to the health of the city exists in any house, cellar or inclosure shut up from public view, they, or any one of them, may demand entry therein in the day time for the purpose of examining the same, and if the owner or occupier thereof shall refuse or delay <page-number citation-index="1" label="370">*370</page-number>to open the same and to admit a free examination, he shall forfeit and pay for every such refusal the sum of twenty dollars, for the use of the corporation.” <footnotemark>12</footnotemark></blockquote>
<p id="b440-4">From the passage of this ordinance to the present the prevention and abatement of “nuisances” on private property has been one-of the chief concerns of the Baltimore City Health Department.<footnotemark>13</footnotemark> In the latter half of the nineteenth century, in the years following the ratification of the Fourteenth Amendment, thousands upon thousands of inspections were made under authority df this ordinance.<footnotemark>14</footnotemark>. Thus - the system of inspection here under attack, having its beginning in Maryland’s colonial history, has been an integral part of the enforcement of Baltimore’s health laws for more than a century and a half. The legal significance of such a long and consistent history of state practice has been illuminated for us by Mr. Justice Holmes:</p>
<blockquote id="b440-5">“The Fourteenth Amendment, itself a historical product, did not destroy history for the States and substitute mechanical compartments of law all exactly alike. If a thing has been practised for two hundred years by common consent, it will need a strong case for the Fourteenth Amendment to affect it, . . . .” <em>Jackman </em>v. <em>Rosenbaum Co., </em><span class="citation" data-id="100034"><a href="/opinion/100034/jackman-v-rosenbaum-co/#31" aria-description="Citation for case: Jackman v. Rosenbaum Co.">260 U. S. 22, 31</a></span>. (As to the constitutional significance of a “time-honored procedure” see <em>Murray’s Lessee </em>v. <em>Hoboken Land and Improvement Co., </em><span class="citation" data-id="87010"><a href="/opinion/87010/den-ex-dem-murray-v-hoboken-land-improvement-co/" aria-description="Citation for case: Den Ex Dem. Murray v. Hoboken Land &amp; Improvement Co.">18 How. 272</a></span>, and <em>Ownbey </em>v. <em>Morgan, </em><span class="citation" data-id="99782"><a href="/opinion/99782/ownbey-v-morgan/" aria-description="Citation for case: Ownbey v. Morgan">256 U. S. 94</a></span>.)</blockquote>
<p id="b441-4"><page-number citation-index="1" label="371">*371</page-number>Of course, this wise reminder, that what free people have found consistent' with their enjoyment of freedom for centuries is hardly to be deemed to violate due process, does not freeze due process within the confines of historical facts or discredited attitudes.<footnotemark>15</footnotemark> “It is of the very nature of a free .society to advance in its standards of what is deemed reasonable and right. Representing as it does a living principle, due process is not confined within a permanent catalogue of whgt may at a given time be deemed the limits or the essentials of fundamental rights.” <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span>.</p>
<p id="b441-5">The power here challenged rests not only on a long history of its exercise. It is a power which was continually strengthened and applied to wider concerns through those very years when the right of individuals to be free, from peremptory official invasion received increasing legislative and judicial protection. Nor is this a situation where a new body of knowledge displaces previous premises of action. There is a total want of important modification in the circumstances or the structure of society which calls for a disregard of so much history. On the contrary, the problems which gave rise to these ordinances have multiplied manifold, as have the difficulties of enforcement. The need to maintain basic, minimal standards of housing, to prevent the spread of disease and of that pervasive breakdown in the fiber of a people which is produced by slums and the absence of the barest essentials of civilized living, has mounted to a major concern of American government. The growth of cities, the crowding of populations, the increased awareness of the responsibility of the state for the living conditions of its citizens, all have combined to create problems of the <page-number citation-index="1" label="372">*372</page-number>enforcement of minimum standards of far greater magnitude than the writers of these ancient inspection laws ever dreamed. Time and experience have -forcefully taúght that the power to inspect dwelling places, either as a matter of. systematic área-by-area search or, as here, to treat a specific problem, is of indispensable importance to the maintenance of community health; a power that would be greatly hobbled by the blanket requirement of the safeguards necessary for a search of evidence of criminal acts. The need for preventive action is great, and city after city has seen this need and granted the power of inspection to its health officials; and these inspections are apparently welcomed by all but an insignificant few.<footnotemark>16</footnotemark> Certainly, the nature of our society has not vitiated the need for inspections first thought necessary 158 years;ago, nor has experience revealed any abuse or inroad on freedom in meeting this need by means that history and dominant public opinion have sanctioned.</p>
<p id="b442-4">That there is “a total unlikeness” between “official acts and proceedings,” <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 624</a></span>, for which the legal protection of privacy requires a <page-number citation-index="1" label="373">*373</page-number>search warrant under the Fourteenth Amendment, and the situation now under consideration is laid bare by the suggestion that the kind of an' inspection by a health official with which we are concerned may be satisfied by what is, in effect, a synthetic search warrant, an authorization “for periodic inspections.” L a search warrant •be constitutionally required, the requirement cannot be flexibly interpreted to dispense with the rigorous constitutional restrictions for its issue. A loose basis for granting a search warrant for the situation before us is to enter by way of the back door to a recognition of the fact that by reason of their intrinsic elements, their historic sanctions, and their safeguards, the Maryland proceedings .requesting permission to make a search without intruding when permission is denied, do not offend the protection of the Fourteenth Amendment.</p>
<p id="b443-4">In light of the long history of this kind of inspection and of modern needs, we cannot say that the carefully circumscribed demand which Maryland here makes on appellant’s freedom has deprived him of due process of law.</p>
<p id="b443-5">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b432-6"> If the nuisance constitutes an actual menace to health the Commissioner may abate it forthwith. Baltimore City Code, Art. 12, §112.</p>
</footnote>
<footnote label="2">
<p id="b434-5"> Tudor, Life of James Otis (1823), 66. No complete text of the Otis speech is extant, but see notes of Horace Gray, Jr. in Quincy’s Massachusetts Reports for 1761-1762, App. I, pp. 469 <em>et seq. </em>Tudor’s life contains an account of it as well as of the events leading to the. speech and the reaction to it-.</p>
</footnote>
<footnote label="3">
<p id="b434-6"> <em>Id., </em>at 61. Adams said:</p>
<blockquote id="b434-7">“Otis was a flame of fire; with a promptitude of classical allusions, a depth of research, a rapid summary of historical events and dates, a profusion of legal authorities, a prophetic glance of his eyes into futurity, and a ’ rapid torrent of impetuous eloquence, he hurried away all before him. American Independence was then and there born. The seeds of patriots and heroes, to defend the <em>Non sine Diis animosus infans; </em>to defend the vigorous youth, were then and there sown. Every man of an immense crouded audience appeared to me to go away as I did, ready to take arms against Writs of Assistance. Then and there, was the first scene of . the first act of opposition, to the arbitrary claims- of Great Britain. Then and there, the child Independence was born. In fifteen years, i. e. in 1776, he grew up to manhood, and declared himself free.” <em>Id., </em>at 60-61.</blockquote>
</footnote>
<footnote label="4">
<p id="b435-5"> The Court in <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, relied heavily on the interrelationship between the Fourth and Fifth Amendments, a view challenged by Professor Wigmore. See 8 Wigmore; Evidence. (3d ed. 19.40), §2264.</p>
</footnote>
<footnote label="5">
<p id="b437-7"> Nearly all the early Maryland statutes are contained in Records of the States of the United States of America, a collection compiled by the Library of Congress in association with .the University of North Carolina in 1949. This collection is on microfilm. Many volumes of the early Maryland Session Laws are available in various library collections throughout the country. No complete collection is known to exist. A typical tobacco inspection statute is Maryland Laws, November 1773, c. 1, §§ LXXIV, LXXX. At times a warrant was required for inspections. of homes. <em>Id., </em>§ LXXIII. See also Maryland Laws, 1717, c. VII. Other Colonies also had statutes allowing inspection to enforce standards for the manufacture or shipping of various items of trade. See, e. <em>g., </em>Virginia Laws, 15 Geo. II (1742), <page-number citation-index="1" label="368">*368</page-number>c. IV (pork and beef); Virginia Laws, 12 Geo. Ill (1772), c. ll (flour and bread); Pennsylvania Laws, 1722,' c. CCLII (flour and bread); Pennsylvania Laws, 1727, c. CCXCV (beef and pork); Pennsylvania Laws, 1729-1730, c. CCCXVI (hemp).</p>
</footnote>
<footnote label="6">
<p id="b438-9"> See, <em>e. g., </em>Maryland. Laws, 1715, e. XLVI (tobacco); Maryland Laws, May 1756, p. 5, §XLVI; Maryland Laws, March 1758, p. 3, §X.</p>
</footnote>
<footnote label="7">
<p id="b438-12"> <em>Ibid.</em></p>
</footnote>
<footnote label="8">
<p id="b438-13"> See <em>Givner </em>v. <em>State, </em><span class="citation" data-id="2305304"><a href="/opinion/2305304/givner-v-state/#492" aria-description="Citation for case: Givner v. State">210 Md. 484, 492-494</a></span>, <span class="citation" data-id="2305304"><a href="/opinion/2305304/givner-v-state/#768" aria-description="Citation for case: Givner v. State">124 A. 2d 764, 768-769</a></span>. The Maryland Court of Appeals has said that this provision of its Declaration of Rights (originally Article 23, now Article 26) is <em>“in pari materia” </em>with the Fourth Amendment to the United States Constitution. <span class="citation" data-id="2305304"><a href="/opinion/2305304/givner-v-state/#492" aria-description="Citation for case: Givner v. State"><em>Id., </em>at 492</a></span>.</p>
</footnote>
<footnote label="9">
<p id="b439-5"> Maryland Laws, Nov. 1782, c. XVII, § VII. A similar law had been in force in Pennsylvania since 1761. Pennsylvania Laws, 1761— 1762, c. C.CCCLXXX.</p>
</footnote>
<footnote label="10">
<p id="b439-7"> Maryland Laws, April 1787, c. XXIII. See also Pennsylvania Laws, 1782, ci MXXXI.</p>
</footnote>
<footnote label="11">
<p id="b439-8"> Maryland Laws, Nov. 1789, c. VIII, § 5. ■ See also Maryland Laws, Nov. 1792, c. LXV, § VII; Maryland Laws. 1793, c. LVI; Maryland Laws, 1784, c. VII.</p>
</footnote>
<footnote label="12">
<p id="b440-6"> Baltimore Ordinances, 1801-1802, No. 23, §6. The Baltimore City Health Department may be the oldest in the country. See 35 Am. J. of Public Health (Jan. 1945), 49.</p>
</footnote>
<footnote label="13">
<p id="b440-7"> See Howard, Public Health Administration and the Natural History of Disease in Baltimore, Maryland, 1797-1920 (1924), 140.</p>
</footnote>
<footnote label="14">
<p id="AOI"> See, <em>id., </em>at 145-146. For example, in 1880 there were 4,292 nuisances inspected by sanitary inspectors. In 1890 there were 34,138 such inspections. <em>Ibi</em>d.</p>
</footnote>
<footnote label="15">
<p id="b441-6"> Compare <em>Kotch </em>v. <em>Board of River Port Pilot Comm’rs, </em><span class="citation" data-id="9419962"><a href="/opinion/104397/kotch-v-board-of-river-port-pilot-commrs-for-port-of-new-orleans/" aria-description="Citation for case: Kotch v. Board of River Port Pilot Comm&#x27;rs for Port of...">330 U. S. 552</a></span>, and <em>Ownbey </em>v. <em>Morgan, </em><span class="citation" data-id="99782"><a href="/opinion/99782/ownbey-v-morgan/" aria-description="Citation for case: Ownbey v. Morgan">256 U. S. 94</a></span>, with <em>Brown </em>v. <em>Board of Education, </em><span class="citation" data-id="105221"><a href="/opinion/105221/brown-v-board-of-education/" aria-description="Citation for case: Brown v. Board of Education">347 U. S. 483</a></span>.</p>
</footnote>
<footnote label="16">
<p id="A2W"> The Baltimore Health Department keeps á record of the number of inspections made annually. All but a few of these are inspections of dwellings. The figures for the last five years are as follows: 1954, 28,081 inspections; 1955, 25,021 inspections; 1956, 35,120 inspections; 1957, 33,573 inspections; 1958, 36,119 inspections. Memorandum of Appellee at Request of Court 2. The Health Commissioner of Baltimore estimates that the number of prosecutions under §120 average one per year.</p>
<p id="b442-7">Of 57 cities whose health codes were studied by the Urban Renewal Administration, 36 empowered their officers to enter and inspect for violations. See Provisions of Housing Codes in Various American Cities, Urban Renewal Bulletin No. 3 (published by Urban Renewal Administration of the Housing and Home Finance Agency 1956).</p>
<p id="b442-8">For a discussion of some of the problems of Urban Renewal, see Note, <span class="citation no-link">72 Harv. L. Rev. 504</span>.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Franks v. Delaware.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Franks v. Delaware"
type: case
citation: "438 U.S. 154 (1978)"
parallel_cite: "98 S. Ct. 2674; 57 L. Ed. 2d 667"
neutral_cite: 1978 U.S. LEXIS 127
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1978
date_decided: 1978-06-26
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1978-06-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Franks v. Delaware
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109925/franks-v-delaware/"
  cluster_id: 109925
  opinion_id: 109925
  identity_checked: true
homes:
  - page: "[[Franks Challenges]]"
    role: "Key — Anchor"
  - page: "[[The Good-Faith Exception]]"
    role: "Related (cross-doctrine)"
related: ["[[Illinois v. Gates]]", "[[United States v. Leon]]", "[[Groh v. Ramirez]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant", "affidavit", "franks-hearing", "veracity"]
holding: "A warrant affidavit containing a knowing/intentional or reckless material falsehood may be challenged at a hearing on a substantial…"
lake:
  record_id: Franks v. Delaware
  status: verified
  projected_at: 2026-07-06
---

# Franks v. Delaware

*438 U.S. 154 (1978)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police obtained a warrant to search Jerome Franks's home in a rape investigation, relying in part on an affidavit reciting statements two officers attributed to named acquaintances about Franks's clothing. Franks contended the officers had not actually interviewed those people as the affidavit claimed and sought to prove the affidavit contained deliberate falsehoods. The Delaware Supreme Court held that a defendant may never go behind a facially sufficient warrant affidavit to attack its truthfulness.

## Issue
Whether a defendant ever has the right, after a warrant issues, to challenge the truthfulness of factual statements in the supporting affidavit — and to suppress the evidence if a deliberate or reckless falsehood necessary to probable cause is shown.

## Rule
Yes — on a substantial preliminary showing, the defendant is entitled to a veracity hearing, and a proven falsehood essential to probable cause voids the warrant. "[W]here the defendant makes a substantial preliminary showing that a false statement knowingly and intentionally, or with reckless disregard for the truth, was included by the affiant in the warrant affidavit, and if the allegedly false statement is necessary to the finding of probable cause, the Fourth Amendment requires that a hearing be held at the defendant's request." — 438 U.S. at 155–156. ^pin-155

"In the event that at that hearing the allegation of perjury or reckless disregard is established by the defendant by a preponderance of the evidence, and, with the affidavit's false material set to one side, the affidavit's remaining content is insufficient to establish probable cause, the search warrant must be voided and the fruits of the search excluded." — *Id.* at 156. ^pin-156

## Application
Franks made specific allegations — backed by an offer of proof — that the affiants had fabricated the statements they attributed to his acquaintances, and those statements bore on probable cause. Because that was the kind of substantial preliminary showing of deliberate or reckless falsehood that entitles a defendant to go behind the affidavit, the Delaware courts erred in treating such a challenge as categorically barred.

## Conclusion
A defendant may challenge a warrant affidavit's veracity on a substantial preliminary showing; the Delaware Supreme Court's categorical bar was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. The "Franks hearing" remains the standard mechanism for attacking deliberate or reckless falsehoods in a warrant affidavit.

## Appears on
- [[Franks Challenges]] — *Key — Anchor*
- [[The Exclusionary Rule]] — *Related (cross-doctrine)*

## Sources
- *Franks v. Delaware*, 438 U.S. 154 (1978) — https://www.courtlistener.com/opinion/109925/franks-v-delaware/ — pinpoints: 155, 156.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6ade265a6226cee0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Franks v. Delaware"}, "payload": {"all": [{"cite": "438 U.S. 154", "page": "154", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "438"}, {"cite": "98 S. Ct. 2674", "page": "2674", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "98"}, {"cite": "57 L. Ed. 2d 667", "page": "667", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "57"}, {"cite": "1978 U.S. LEXIS 127", "page": "127", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1978"}], "display": "438 U.S. 154", "official": {"cite": "438 U.S. 154", "page": "154", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "438"}, "official_selection_present": true, "record_id": "Franks v. Delaware"}}
{"assertion_id": "50d80cecea9545bb", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-155", "record_id": "Franks v. Delaware"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-155", "pinpoint_status": "slip-only", "quote": "--- # Franks v. Delaware *438 U.S. 154 (1978)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police obtained a warrant to search Jerome Franks's home in a rape investigation, relying in part on an affidavit reciting statements two officers attributed to named acquaintances about Franks's clothing. Franks contended the officers had not actually interviewed those people as the affidavit claimed and sought to prove the affidavit contained deliberate falsehoods. The Delaware Supreme Court held that a defendant may never go behind a facially sufficient warrant affidavit to attack its truthfulness. ## Issue Whether a defendant ever has the right, after a warrant issues, to challenge the truthfulness of factual statements in the supporting affidavit — and to suppress the evidence if a deliberate or reckless falsehood necessary to probable cause is shown. ## Rule Yes — on a substantial preliminary showing, the defendant is entitled to a veracity hearing, and a proven falsehood essential to probable cause voids the warrant.", "quote_fidelity": "mismatch", "record_id": "Franks v. Delaware", "star_marker": null}}
{"assertion_id": "a486e35beba2a054", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-156", "record_id": "Franks v. Delaware"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-156", "pinpoint_status": "slip-only", "quote": "In the event that at that hearing the allegation of perjury or reckless disregard is established by the defendant by a preponderance of the evidence, and, with the affidavit's false material set to one side, the affidavit's remaining content is insufficient to establish probable cause, the search warrant must be voided and the fruits of the search excluded.", "quote_fidelity": "mismatch", "record_id": "Franks v. Delaware", "star_marker": null}}
{"assertion_id": "bf2dff5559564b73", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Franks v. Delaware"}, "payload": {"as_of_content": "1978-06-26", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Franks v. Delaware", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Franks v. Delaware

```json
{
  "schema_version": "s2.v1",
  "record_id": "Franks v. Delaware",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Franks v. Delaware",
    "case_name_short": "Franks",
    "case_name_full": "Franks v. Delaware",
    "input_case_name": "Franks v. Delaware",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1978-06-26",
    "year": 1978,
    "docket": null,
    "cluster_id": 109925,
    "lead_opinion_id": 109925,
    "sibling_ids": [
      109925,
      9427321,
      9427322
    ],
    "absolute_url": "/opinion/109925/franks-v-delaware/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9016328,
        "score": 20,
        "case_name": "Franks v. Delaware"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "438 U.S. 154",
      "volume": "438",
      "reporter": "U.S.",
      "page": "154",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "98 S. Ct. 2674",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "2674",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 L. Ed. 2d 667",
        "volume": "57",
        "reporter": "L. Ed. 2d",
        "page": "667",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1978 U.S. LEXIS 127",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "127",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "438 U.S. 154",
        "volume": "438",
        "reporter": "U.S.",
        "page": "154",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 S. Ct. 2674",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "2674",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 L. Ed. 2d 667",
        "volume": "57",
        "reporter": "L. Ed. 2d",
        "page": "667",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1978 U.S. LEXIS 127",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "127",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "438 U.S. 154",
    "official_selection": {
      "court_class": "scotus",
      "selected": "438 U.S. 154",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-155",
      "page": null,
      "quote": "--- # Franks v. Delaware *438 U.S. 154 (1978)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police obtained a warrant to search Jerome Franks's home in a rape investigation, relying in part on an affidavit reciting statements two officers attributed to named acquaintances about Franks's clothing. Franks contended the officers had not actually interviewed those people as the affidavit claimed and sought to prove the affidavit contained deliberate falsehoods. The Delaware Supreme Court held that a defendant may never go behind a facially sufficient warrant affidavit to attack its truthfulness. ## Issue Whether a defendant ever has the right, after a warrant issues, to challenge the truthfulness of factual statements in the supporting affidavit \u2014 and to suppress the evidence if a deliberate or reckless falsehood necessary to probable cause is shown. ## Rule Yes \u2014 on a substantial preliminary showing, the defendant is entitled to a veracity hearing, and a proven falsehood essential to probable cause voids the warrant.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-156",
      "page": null,
      "quote": "In the event that at that hearing the allegation of perjury or reckless disregard is established by the defendant by a preponderance of the evidence, and, with the affidavit's false material set to one side, the affidavit's remaining content is insufficient to establish probable cause, the search warrant must be voided and the fruits of the search excluded.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1978-06-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Franks v. Delaware",
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
        "journal_ref": "Franks v. Delaware:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fields",
          "cluster_id": 10309030,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Seneca Warrior Steeprock",
          "cluster_id": 10102625,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Dunn",
          "cluster_id": 9500669,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Jesse Jon Harbach",
          "cluster_id": 9493041,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Whitfield",
          "cluster_id": 9400623,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane1_negative"
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
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
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
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
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
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "County Court of Ulster Cty. v. Allen",
          "cluster_id": 110093,
          "cite": [
            "60 L. Ed. 2d 777",
            "99 S. Ct. 2213",
            "442 U.S. 140",
            "1979 U.S. LEXIS 124"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
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
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Dominguez-Castor",
          "cluster_id": 4691722,
          "cite": [
            "2020 COA 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mills v. Maryland",
          "cluster_id": 112085,
          "cite": [
            "100 L. Ed. 2d 384",
            "108 S. Ct. 1860",
            "486 U.S. 367",
            "1988 U.S. LEXIS 2488",
            "56 U.S.L.W. 4503"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
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
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jerry L. Branch, Valenna Branch, Colby Branch v. Dale L. Tunnell, Individually and as Special Agent of Bureau of Land Management, State of Montana",
          "cluster_id": 660713,
          "cite": [
            "14 F.3d 449",
            "94 Cal. Daily Op. Serv. 253",
            "28 Fed. R. Serv. 3d 1211",
            "94 Daily Journal DAR 442",
            "1994 U.S. App. LEXIS 409",
            "1994 WL 5496"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
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
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Marshall",
          "cluster_id": 1969802,
          "cite": [
            "690 A.2d 1",
            "148 N.J. 89",
            "1997 N.J. LEXIS 70"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bradford",
          "cluster_id": 1239150,
          "cite": [
            "15 Cal. 4th 1229",
            "939 P.2d 259",
            "97 Daily Journal DAR 9003",
            "97 Cal. Daily Op. Serv. 5537",
            "65 Cal. Rptr. 2d 145",
            "1997 Cal. LEXIS 3699"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. Greenfield",
          "cluster_id": 111553,
          "cite": [
            "88 L. Ed. 2d 623",
            "106 S. Ct. 634",
            "474 U.S. 284",
            "1986 U.S. LEXIS 41",
            "54 U.S.L.W. 4077"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Williams",
          "cluster_id": 112730,
          "cite": [
            "118 L. Ed. 2d 352",
            "112 S. Ct. 1735",
            "504 U.S. 36",
            "1992 U.S. LEXIS 2688"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Martinez v. State",
          "cluster_id": 1561283,
          "cite": [
            "17 S.W.3d 677",
            "2000 Tex. Crim. App. LEXIS 53",
            "2000 WL 628325"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sykes v. Anderson",
          "cluster_id": 178987,
          "cite": [
            "625 F.3d 294",
            "2010 U.S. App. LEXIS 23204",
            "2010 WL 4453313"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gregory v. City of Louisville",
          "cluster_id": 2973641,
          "cite": [
            "444 F.3d 725",
            "2006 WL 909935"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Robinson",
          "cluster_id": 1539942,
          "cite": [
            "974 A.2d 1057",
            "200 N.J. 1",
            "2009 N.J. LEXIS 804"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Panah",
          "cluster_id": 2509294,
          "cite": [
            "107 P.3d 790",
            "25 Cal. Rptr. 3d 672",
            "35 Cal. 4th 395",
            "2005 Cal. Daily Op. Serv. 2194",
            "2005 Daily Journal DAR 3023",
            "2005 Cal. LEXIS 2712"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pagan v. State",
          "cluster_id": 1110208,
          "cite": [
            "830 So. 2d 792",
            "2002 WL 500315"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Janecka v. State",
          "cluster_id": 1743739,
          "cite": [
            "937 S.W.2d 456",
            "1996 Tex. Crim. App. LEXIS 240",
            "1996 WL 682137"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tyron Brown v. Lee Lucas",
          "cluster_id": 2675935,
          "cite": [
            "753 F.3d 606",
            "2014 WL 2198419",
            "2014 U.S. App. LEXIS 9771"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
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
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Waclawski",
          "cluster_id": 1703326,
          "cite": [
            "780 N.W.2d 321",
            "286 Mich. App. 634"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Greg Myers, Etc. v. R. Kathleen Morris, Scott County Attorney, Etc.",
          "cluster_id": 482831,
          "cite": [
            "810 F.2d 1437"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Franks v. Delaware:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109925 OR 9427321 OR 9427322) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjcxNTgwODAwMDAwJnM9OTM2NzYxNiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109925+OR+9427321+OR+9427322%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(109925 OR 9427321 OR 9427322)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00Mjkmcz0yNzA0JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109925+OR+9427321+OR+9427322%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109925 OR 9427321 OR 9427322)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzAzNzIxNjAwMDAwJnM9OTQ1NTgxNiZ0PW8mZD0yMDI2LTA3LTA2JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109925+OR+9427321+OR+9427322%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 5,
        "triage_snippet_classified": 195
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109925 OR 9427321 OR 9427322)",
    "indexed_citing_opinions": 5121,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109925,
        "count": 4294,
        "count_source": "search"
      },
      {
        "opinion_id": 9427321,
        "count": 880,
        "count_source": "search"
      },
      {
        "opinion_id": 9427322,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 8699,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/franks-v-delaware.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk1MDQ4NiZzPTEwNjU4ODk4JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109925+OR+9427321+OR+9427322%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109925,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 98212,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 104373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 105074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 105925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 106783,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 107394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 107951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 108302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 108582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 109302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 299224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 307033,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 316109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 317254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 318456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 324012,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 327139,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 331000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 338659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 338672,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 340645,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1130838,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1148533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1163909,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1176912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1180163,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1183476,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1190217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1198737,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1285341,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1306980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1311035,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1312713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1353828,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1363434,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1367322,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1367376,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1391098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1415130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1424506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1437089,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1445282,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1451648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1452068,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1498442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1530851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1600679,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1631048,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1760963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1768917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1769197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1828817,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1850125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1851918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1886978,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1895767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1973195,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 1987009,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2053522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2060217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2120568,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2133918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2184913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2215694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2221046,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2233092,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2341043,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2349003,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2356548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2379504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2386408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2398659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2442476,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2467369,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 2609109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 3423317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 3486405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 3493017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 3535850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 3744266,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109925,
        "cited_id": 3865272,
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
    "date_created": "2026-07-05T04:50:20Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T04:50:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T04:50:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T04:55:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T04:50:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Franks v. Delaware

```
<div>
<center><b><span class="citation" data-id="9427321"><a href="/opinion/109925/franks-v-delaware/" aria-description="Citation for case: Franks v. Delaware">438 U.S. 154</a></span> (1978)</b></center>
<center><h1>FRANKS<br>
v.<br>
DELAWARE.</h1></center>
<center>No. 77-5176.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 27, 1978.</center>
<center>Decided June 26, 1978.</center>
CERTIORARI TO THE SUPREME COURT OF DELAWARE.
<p><span class="star-pagination">*155</span> <i>Donald W. Huntley</i> argued the cause and filed briefs for petitioner.</p>
<p><i>Harrison F. Turner,</i> Deputy Attorney General of Delaware, argued the cause for respondent. With him on the brief was <i>Richard R. Wier, Jr.,</i> Attorney General.<sup>[*]</sup></p>
<p>MR. JUSTICE BLACKMUN delivered the opinion of the Court.</p>
<p>This case presents an important and longstanding issue of Fourth Amendment law. Does a defendant in a criminal proceeding ever have the right, under the Fourth and Fourteenth Amendments, subsequent to the <i>ex parte</i> issuance of a search warrant, to challenge the truthfulness of factual statements made in an affidavit supporting the warrant?</p>
<p>In the present case the Supreme Court of Delaware held, as a matter of first impression for it, that a defendant under <i>no</i> circumstances may so challenge the veracity of a sworn statement used by police to procure a search warrant. We reverse, and we hold that, where the defendant makes a substantial preliminary showing that a false statement knowingly and intentionally, or with reckless disregard for the truth, was <span class="star-pagination">*156</span> included by the affiant in the warrant affidavit, and if the allegedly false statement is necessary to the finding of probable cause, the Fourth Amendment requires that a hearing be held at the defendant's request. In the event that at that hearing the allegation of perjury or reckless disregard is established by the defendant by a preponderance of the evidence, and, with the affidavit's false material set to one side, the affidavit's remaining content is insufficient to establish probable cause, the search warrant must be voided and the fruits of the search excluded to the same extent as if probable cause was lacking on the face of the affidavit.</p>
<p></p>
<h2>I</h2>
<p>The controversy over the veracity of the search warrant affidavit in this case arose in connection with petitioner Jerome Franks' state conviction for rape, kidnaping, and burglary. On Friday, March 5, 1976, Mrs. Cynthia Bailey told police in Dover, Del., that she had been confronted in her home earlier that morning by a man with a knife, and that he had sexually assaulted her. She described her assailant's age, race, height, build, and facial hair, and gave a detailed description of his clothing as consisting of a white thermal undershirt, black pants with a silver or gold buckle, a brown leather three-quarter-length coat, and a dark knit cap that he wore pulled down around his eyes.</p>
<p>That same day, petitioner Franks coincidentally was taken into custody for an assault involving a 15-year-old girl, Brenda B. ______, six days earlier. After his formal arrest, and while awaiting a bail hearing in Family Court, petitioner allegedly stated to Robert McClements, the youth officer accompanying him, that he was surprised the bail hearing was "about Brenda B. ______. I know her. I thought you said Bailey. I don't know her." Tr. 175, 186. At the time of this statement, the police allegedly had not yet recited to petitioner his rights under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966).</p>
<p><span class="star-pagination">*157</span> On the following Monday, March 8, Officer McClements happened to mention the courthouse incident to a detective, Ronald R. Brooks, who was working on the Bailey case. Tr. 186, 190-191. On March 9, Detective Brooks and Detective Larry D. Gray submitted a sworn affidavit to a Justice of the Peace in Dover, in support of a warrant to search petitioner's apartment.<sup>[1]</sup> In paragraph 8 of the affidavit's "probable cause page" mention was made of petitioner's statement to McClements. In paragraph 10, it was noted that the description of the assailant given to the police by Mrs. Bailey included the above-mentioned clothing. Finally, the affidavit also described the attempt made by police to confirm that petitioner's typical outfit matched that of the assailant. Paragraph 15 recited: "On Tuesday, 3/9/76, your affiant contacted Mr. James Williams and Mr. Wesley Lucas of the Delaware Youth Center where Jerome Franks is employed and did have personal conversation with both these people." Paragraphs 16 and 17 respectively stated: "Mr. James Williams revealed to your affiant that the normal dress of Jerome Franks does consist of a white knit thermal undershirt and a brown leather jacket," and "Mr. Wesley Lucas revealed to your affiant that in addition to the thermal undershirt and jacket, Jerome Franks often wears a dark green knit hat."</p>
<p>The warrant was issued on the basis of this affidavit. App. 9. Pursuant to the warrant, police searched petitioner's apartment and found a white thermal undershirt, a knit hat, dark pants, and a leather jacket, and, on petitioner's kitchen table, a single-blade knife. All these ultimately were introduced in evidence at trial.</p>
<p>Prior to the trial, however, petitioner's counsel filed a written motion to suppress the clothing and the knife found in the search; this motion alleged that the warrant on its face did not show probable cause and that the search and seizure were <span class="star-pagination">*158</span> in violation of the Fourth and Fourteenth Amendments. <i>Id.,</i> at 11-12. At the hearing on the motion to suppress, defense counsel orally amended the challenge to include an attack on the veracity of the warrant affidavit; he also specifically requested the right to call as witnesses Detective Brooks, Wesley Lucas of the Youth Center, and James D. Morrison, formerly of the Youth Center.<sup>[2]</sup><i>Id.,</i> at 14-17. Counsel asserted that Lucas and Morrison would testify that neither had been personally interviewed by the warrant affiants, and that, although they might have talked to another police officer, any information given by them to that officer was "somewhat different" from what was recited in the affidavit. <i>Id.,</i> at 16. Defense counsel charged that the misstatements were included in the affidavit not inadvertently, but in "bad faith." <i>Id.,</i> at 25. Counsel also sought permission to call Officer McClements and petitioner as witnesses, to seek to establish that petitioner's courthouse statement to police had been obtained in violation of petitioner's <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, and that the search warrant was thereby tainted as the fruit of an illegally obtained confession. <i>Id.,</i> at 17, 27.</p>
<p>In rebuttal, the State's attorney argued in detail, App. 15-24, (a) that Del. Code Ann., Tit. 11, §§ 2306, 2307 (1974), contemplated that any challenge to a search warrant was to be limited to questions of sufficiency based on the face of the affidavit; (b) that, purportedly, a majority of the States whose <span class="star-pagination">*159</span> practice was not dictated by statute observed such a rule;<sup>[3]</sup> and (c) that federal cases on the issue were to be distinguished because of Fed. Rule Crim. Proc. 41 (e).<sup>[4]</sup> He also noted that <span class="star-pagination">*160</span> this Court had reserved the general issue of subfacial challenge to veracity in <i>Rugendorf</i> v. <i>United States,</i> <span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/#531" aria-description="Citation for case: Rugendorf v. United States">376 U. S. 528, 531-532</a></span> (1964). when it disposed of that case on the ground that, even if a veracity challenge were permitted, the alleged factual inaccuracies in that case's affidavit "were of only peripheral relevancy to the showing of probable cause, and, not being within the personal knowledge of the affiant, did not go to the integrity of the affidavit." <span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/#532" aria-description="Citation for case: Rugendorf v. United States"><i>Id.,</i> at 532</a></span>. The State objected to petitioner's "going behind [the warrant affidavit] in any way," and argued that the court must decide petitioner's motion "on the four corners" of the affidavit. App. 21.</p>
<p>The trial court sustained the State's objection to petitioner's proposed evidence. <i>Id.,</i> at 25, 27. The motion to suppress was denied, and the clothing and knife were admitted as evidence at the ensuing trial. Tr. 192-196. Petitioner was convicted. In a written motion for judgment of acquittal and/or new trial, Record Doc. No. 23, petitioner repeated his objection to the admission of the evidence, stating that he "should have been allowed to impeach the Affidavit used in the Search Warrant to show purposeful misrepresentation of information contained therein." <i>Id.,</i> at 2. The motion was denied, and petitioner was sentenced to two consecutive terms of 25 years each and an additional consecutive life sentence.</p>
<p>On appeal, the Supreme Court of Delaware affirmed. <span class="citation" data-id="2356548"><a href="/opinion/2356548/franks-v-state/" aria-description="Citation for case: Franks v. State">373 A. 2d 578</a></span> (1977). It agreed with what it deemed to be the "majority rule" that no attack upon the veracity of a warrant affidavit could be made:</p>
<blockquote>"We agree with the majority rule for two reasons. First, it is the function of the issuing magistrate to determine the reliability of information and credibility of affiants in deciding whether the requirement of probable cause has been met. There has been no need demonstrated for interfering with this function. Second, neither the probable cause nor suppression hearings are adjudications of guilt or innocence; the matters asserted by defendant are <span class="star-pagination">*161</span> more properly considered in a trial on the merits." <span class="citation" data-id="2356548"><a href="/opinion/2356548/franks-v-state/#580" aria-description="Citation for case: Franks v. State"><i>Id.,</i> at 580</a></span>.</blockquote>
<p>Because of this resolution, the Delaware Supreme Court noted that there was no need to consider petitioner's "other contentions, relating to the evidence that would have been introduced for impeachment purposes." <i><span class="citation" data-id="2356548"><a href="/opinion/2356548/franks-v-state/" aria-description="Citation for case: Franks v. State">Ibid.</a></span></i></p>
<p>Franks' petition for certiorari presented only the issue whether the trial court had erred in refusing to consider his allegation of misrepresentation in the warrant affidavit.<sup>[5]</sup> Because of the importance of the question, and because of the conflict among both state and federal courts, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./434/889/">434 U. S. 889</a></span> (1977).</p>
<p></p>
<h2>II</h2>
<p>It may be well first to note how we are compelled to reach the Fourth Amendment issue proffered in this case. In particular, the State's proposals of an independent and adequate state ground and of harmless error do not dispose of the controversy.</p>
<p>Respondent argues that petitioner's trial counsel, who is not the attorney representing him in this Court, failed to include the challenge to the veracity of the warrant affidavit in the written motion to suppress filed before trial, contrary to the requirement of Del. Super. Ct. Rule Crim. Proc. 41 (e) that a motion to suppress "shall state the grounds upon which it is made." The Supreme Court of Delaware, however, disposed of petitioner's Fourth Amendment claim on the merits. A ruling on the merits of a federal question by the highest state court leaves the federal question open to review <span class="star-pagination">*162</span> in this Court. <i>Manhattan Life Ins. Co.</i> v. <i>Cohen,</i> <span class="citation" data-id="98212"><a href="/opinion/98212/manhattan-life-ins-co-of-ny-v-cohen/#134" aria-description="Citation for case: Manhattan Life Ins. Co. of NY v. Cohen">234 U. S. 123, 134</a></span> (1914); <i>Raley</i> v. <i>Ohio,</i> <span class="citation" data-id="105925"><a href="/opinion/105925/raley-v-ohio/#436" aria-description="Citation for case: Raley v. Ohio">360 U. S. 423, 436-437</a></span> (1959); <i>Boykin</i> v. <i>Alabama,</i> <span class="citation" data-id="9424054"><a href="/opinion/107951/boykin-v-alabama/#241" aria-description="Citation for case: Boykin v. Alabama">395 U. S. 238, 241-242</a></span> (1969).</p>
<p>Respondent next suggests that any error here was harmless. Assuming, <i>arguendo,</i> respondent says, that petitioner's Fourth Amendment claim was valid, and that the warrant should have been tested for veracity and the evidence excluded, it is still clear beyond a reasonable doubt that the evidence complained of did not contribute to petitioner's conviction. <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 52-53</a></span> (1970). This contention falls of its own weight. The sole issue at trial was that of consent. Petitioner admitted, App. 37, that he had engaged in sexual relations with Mrs. Bailey on the day in question. She testified, Tr. 50-51, 69-70, that she had not consented to this, and that petitioner, upon first encountering her in the house, had threatened her with a knife to force her to submit. Petitioner claimed that she had given full consent and that no knife had been present. <i>Id.,</i> at 254, 271. To corroborate its contention that consent was lacking, the State introduced in evidence a stainless steel, wooden-handled kitchen knife found by the detectives on the kitchen table in petitioner's apartment four days after the alleged rape. <i>Id.,</i> at 195-196; Magistrate's Return on the Search Warrant March 9, 1976, Record Doc. No. 23. Defense counsel objected to its admission, arguing that Mrs. Bailey had not given any detailed description of the knife alleged to be involved in the incident and had claimed to have seen the knife only in "pitch blackness." Tr. 195. The State obtained its admission, however, as a knife that matched the description contained in the search warrant, and Mrs. Bailey testified that the knife allegedly used was, like the knife in evidence, single-edged and not a pocket knife, and that the knife in evidence was the same length and thickness as the knife used in the crime. <i>Id.,</i> at 69, 114-115. The State carefully elicited from Detective Brooks the fact that this was the only knife found in petitioner's <span class="star-pagination">*163</span> apartment. <i>Id.,</i> at 196. Although respondent argues that the knife was presented to the jury as "merely exemplary of the generic class of weapon testimonially described by the victim," Brief for Respondent 15-16, the State at trial clearly meant to suggest that this was the knife that had been used against Mrs. Bailey. Had the warrant been quashed, and the knife excluded from the trial as evidence, we cannot say with any assurance that the jury would have reached the same decision on the issue of consent, particularly since there was countervailing evidence on that issue.</p>
<p>We should note, in addition, why this case cannot be treated as was the situation in <i>Rugendorf</i> v. <i>United States</i><i>.</i> There the Court held that no Fourth Amendment question was presented when the claimed misstatements in the search warrant affidavit "were of only peripheral relevancy to the showing of probable cause, <i>and,</i> not being within the personal knowledge of the affiant, did not go to the integrity of the affidavit." <span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/#532" aria-description="Citation for case: Rugendorf v. United States">376 U. S., at 532</a></span> (emphasis added). <i><span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">Rugendorf</a></span></i> emphasized that the "erroneous statements . . . were not those of the affiant" and thus "fail[ed] to show that the affiant was in bad faith or that he made any misrepresentations to the Commissioner in securing the warrant." <span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/#533" aria-description="Citation for case: Rugendorf v. United States"><i>Id.,</i> at 533</a></span>.<sup>[6]</sup> Here, <span class="star-pagination">*164</span> whatever the judgment may be as to the relevancy of the alleged misstatements, the integrity of the affidavit was directly placed in issue by petitioner in his allegation that the affiants did not, as claimed, speak directly to Lucas and Morrison. Whether such conversations took place is surely a matter "within the personal knowledge of the affiant[s]." We also might note that although respondent's brief puts forth that the alleged misrepresentations in the affidavit were of little importance in establishing probable cause, Brief for Respondent 16, respondent at oral argument appeared to disclaim any reliance on <i><span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">Rugendorf</a></span>.</i> Tr. of Oral Arg. 30.</p>
<p></p>
<h2>III</h2>
<p>Whether the Fourth and Fourteenth Amendments, and the derivative exclusionary rule made applicable to the States under <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), ever mandate that a defendant be permitted to attack the veracity of a warrant affidavit after the warrant has been issued and executed, is a question that encounters conflicting values. The bulwark of Fourth Amendment protection, of course, is the Warrant Clause, requiring that, absent certain exceptions, police obtain a warrant from a neutral and disinterested magistrate before embarking upon a search. In deciding today that, in certain circumstances, a challenge to a warrant's veracity must be permitted, we derive our ground from language of the Warrant Clause itself, which surely takes the affiant's good faith as its premise: "[N]o Warrants shall issue, but upon probable cause, supported by Oath or affirmation . . . ." Judge Frankel, in <i>United States</i> v. <i>Halsey,</i> <span class="citation" data-id="1600679"><a href="/opinion/1600679/united-states-v-halsey/#1005" aria-description="Citation for case: United States v. Halsey">257 F. Supp. 1002, 1005</a></span> (SDNY 1966), aff'd, Docket No. 31369 (CA2, June 12, 1967) (unreported), put the matter simply: "[W]hen the Fourth Amendment demands a factual showing sufficient to comprise `probable cause,' the obvious assumption is that there will be a <span class="star-pagination">*165</span> <i>truthful</i> showing" (emphasis in original). This does not mean "truthful" in the sense that every fact recited in the warrant affidavit is necessarily correct, for probable cause may be founded upon hearsay and upon information received from informants, as well as upon information within the affiant's own knowledge that sometimes must be garnered hastily. But surely it is to be "truthful" in the sense that the information put forth is believed or appropriately accepted by the affiant as true. It is established law, see <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/#47" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41, 47</a></span> (1933); <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#485" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 485-486</a></span> (1958); <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#114" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108, 114-115</a></span> (1964), that a warrant affidavit must set forth particular facts and circumstances underlying the existence of probable cause, so as to allow the magistrate to make an independent evaluation of the matter. If an informant's tip is the source of information, the affidavit must recite "some of the underlying circumstances from which the informant concluded" that relevant evidence might be discovered, and "some of the underlying circumstances from which the officer concluded that the informant, whose identity need not be disclosed,. . . was `credible' or his information `reliable.'" <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#114" aria-description="Citation for case: Aguilar v. Texas"><i>Id.,</i> at 114</a></span>. Because it is the magistrate who must determine independently whether there is probable cause, <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-14</a></span> (1948); <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#270" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 270-271</a></span> (1960), it would be an unthinkable imposition upon his authority if a warrant affidavit, revealed after the fact to contain a deliberately or recklessly false statement, were to stand beyond impeachment.</p>
<p>In saying this, however, one must give cognizance to competing values that lead us to impose limitations. They perhaps can best be addressed by noting the arguments of respondent and others against allowing veracity challenges. The arguments are several:</p>
<p>First, respondent argues that the exclusionary rule, created in <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), is not a <span class="star-pagination">*166</span> personal constitutional right, but only a judicially created remedy extended where its benefit as a deterrent promises to outweigh the societal cost of its use; that the Court has declined to apply the exclusionary rule when illegally seized evidence is used to impeach the credibility of a defendant's testimony, <i>Walder</i> v. <i>United States,</i> <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span> (1954), is used in a grand jury proceeding, <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">414 U. S. 338</a></span> (1974), or is used in a civil trial, <i>United States</i> v. <i>Janis,</i> <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">428 U. S. 433</a></span> (1976); and that the Court similarly has restricted application of the Fourth Amendment exclusionary rule in federal habeas corpus review of a state conviction. See <i>Stone</i> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U. S. 465</a></span> (1976). Respondent argues that applying the exclusionary rule to another situationthe deterrence of deliberate or reckless untruthfulness in a warrant affidavitis not justified for many of the same reasons that led to the above restrictions; interfering with a criminal conviction in order to deter official misconduct is a burden too great to impose on society.</p>
<p>Second, respondent argues that a citizen's privacy interests are adequately protected by a requirement that applicants for a warrant submit a sworn affidavit and by the magistrate's independent determination of sufficiency based on the face of the affidavit. Applying the exclusionary rule to attacks upon veracity would weed out a minimal number of perjuries government statements, says respondent, but would overlap unnecessarily with existing penalties against perjury, including criminal prosecutions, departmental discipline for misconduct, contempt of court, and civil actions.</p>
<p>Third, it is argued that the magistrate already is equipped to conduct a fairly vigorous inquiry into the accuracy of the factual affidavit supporting a warrant application. He may question the affiant, or summon other persons to give testimony at the warrant proceeding. The incremental gain from a post-search adversary proceeding, it is said, would not be great.</p>
<p><span class="star-pagination">*167</span> Fourth, it is argued that it would unwisely diminish the solemnity and moment of the magistrate's proceeding to make his inquiry into probable cause reviewable in regard to veracity. The less final, and less deference paid to, the magistrate's determination of veracity, the less initiative will he use in that task. Denigration of the magistrate's function would be imprudent insofar as his scrutiny is the last bulwark preventing any particular invasion of privacy before it happens.</p>
<p>Fifth, it is argued that permitting a post-search evidentiary hearing on issues of veracity would confuse the pressing issue of guilt or innocence with the collateral question as to whether there had been official misconduct in the drafting of the affidavit. The weight of criminal dockets, and the need to prevent diversion of attention from the main issue of guilt or innocence, militate against such an added burden on the trial courts. And if such hearings were conducted routinely, it is said, they would be misused by defendants as a convenient source of discovery. Defendants might even use the hearings in an attempt to force revelation of the identity of informants.</p>
<p>Sixth and finally, it is argued that a post-search veracity challenge is inappropriate because the accuracy of an affidavit in large part is beyond the control of the affiant. An affidavit may properly be based on hearsay, on fleeting observations, and on tips received from unnamed informants whose identity often will be properly protected from revelation under <i>McCray</i> v. <i>Illinois,</i> <span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300</a></span> (1967).</p>
<p>None of these considerations is trivial. Indeed, because of them, the rule announced today has a limited scope, both in regard to when exclusion of the seized evidence is mandated, and when a hearing on allegations of misstatements must be accorded. But neither do the considerations cited by respondent and others have a fully controlling weight; we conclude that they are insufficient to justify an <i>absolute</i> ban on post-search impeachment of veracity. On this side of the balance, also, there are pressing considerations:</p>
<p><span class="star-pagination">*168</span> First, a flat ban on impeachment of veracity could denude the probable-cause requirement of all real meaning. The requirement that a warrant not issue "but upon probable cause, supported by Oath or affirmation," would be reduced to a nullity if a police officer was able to use deliberately falsified allegations to demonstrate probable cause, and, having misled the magistrate, then was able to remain confident that the ploy was worthwhile. It is this specter of intentional falsification that, we think, has evoked such widespread opposition to the flat nonimpeachment rule from the commentators,<sup>[7]</sup> from the American Law Institute in its Model Code of Pre-Arraignment Procedure, § SS290.3 (1) (Prop. Off. Draft 1975), from the federal courts of appeals, and from state courts. On occasion, of course, an instance of deliberate falsity will be exposed and confirmed without a special inquiry either at trial, see <i>United States ex rel. Petillo</i> v. <i>New Jersey,</i> <span class="citation" data-id="1367376"><a href="/opinion/1367376/united-states-ex-rel-petillo-v-state-of-nj/#1171" aria-description="Citation for case: United States Ex Rel. Petillo v. State of NJ">400 F. Supp. 1152, 1171-1172</a></span> (NJ 1975), vacated and remanded by order <i>sub nom. </i><i>Albanese</i> v. <i>Yeager,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/541/275/">541 F. 2d 275</a></span> (CA3 1976), or at a hearing on the sufficiency of the affidavit, cf. <i>United States</i> v. <i>Upshaw,</i> <span class="citation" data-id="9457392"><a href="/opinion/299224/united-states-v-eddie-upshaw/" aria-description="Citation for case: United States v. Eddie Upshaw">448 F. 2d 1218</a></span>, 1221-1222 <span class="star-pagination">*169</span> (CA5 1971), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./405/934/">405 U. S. 934</a></span> (1972). A flat nonimpeachment rule would bar re-examination of the warrant even in these cases.</p>
<p>Second, the hearing before the magistrate not always will suffice to discourage lawless or reckless misconduct. The pre-search proceeding is necessarily <i>ex parte,</i> since the subject of the search cannot be tipped off to the application for a warrant lest he destroy or remove evidence. The usual reliance of our legal system on adversary proceedings itself should be an indication that an <i>ex parte</i> inquiry is likely to be less vigorous. The magistrate has no acquaintance with the information that may contradict the good faith and reasonable basis of the affiant's allegations. The pre-search proceeding will frequently be marked by haste, because of the understandable desire to act before the evidence disappears; this urgency will not always permit the magistrate to make an extended independent examination of the affiant or other witnesses.</p>
<p>Third, the alternative sanctions of a perjury prosecution, administrative discipline, contempt, or a civil suit are not likely to fill the gap. <i>Mapp</i> v. <i>Ohio</i> implicitly rejected the adequacy of these alternatives. Mr. Justice Douglas noted this in his concurrence in <i>Mapp,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#670" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 670</a></span>, where he quoted from <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#42" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 42</a></span> (1949): " `Self-scrutiny is a lofty ideal, but its exaltation reaches new heights if we expect a District Attorney to prosecute himself or his associates for well-meaning violations of the search and seizure clause during a raid the District Attorney or his associates have ordered.'"</p>
<p>Fourth, allowing an evidentiary hearing, after a suitable preliminary proffer of material falsity, would not diminish the importance and solemnity of the warrant-issuing process. It is the <i>ex parte</i> nature of the initial hearing, rather than the magistrate's capacity, that is the reason for the review. A magistrate's determination is presently subject to review before trial as to <i>sufficiency</i> without any undue interference <span class="star-pagination">*170</span> with the dignity of the magistrate's function. Our reluctance today to extend the rule of exclusion beyond instances of deliberate misstatements, and those of reckless disregard, leaves a broad field where the magistrate is the sole protection of a citizen's Fourth Amendment rights, namely, in instances where police have been merely negligent in checking or recording the facts relevant to a probable-cause determination.</p>
<p>Fifth, the claim that a post-search hearing will confuse the issue of the defendant's guilt with the issue of the State's possible misbehavior is footless. The hearing will not be in the presence of the jury. An issue extraneous to guilt already is examined in any probable-cause determination or review of probable cause. Nor, if a sensible threshold showing is required and sensible substantive requirements for suppression are maintained, need there be any new large-scale commitment of judicial resources; many claims will wash out at an early stage, and the more substantial ones in any event would require judicial resources for vindication if the suggested alternative sanctions were truly to be effective. The requirement of a substantial preliminary showing should suffice to prevent the misuse of a veracity hearing for purposes of discovery or obstruction. And because we are faced today with only the question of the integrity of the affiant's representations as to his own activities, we need not decide, and we in no way predetermine, the difficult question whether a reviewing court must ever require the revelation of the identity of an informant once a substantial preliminary showing of falsity has been made. <i>McCray</i> v. <i>Illinois,</i> <span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300</a></span> (1967), the Court's earlier disquisition in this area, concluded only that the Due Process Clause of the Fourteenth Amendment did not require the State to expose an informant's identity routinely, upon a defendant's mere demand, when there was ample evidence in the probable-cause hearing to show that the informant was reliable and his information credible.</p>
<p>Sixth and finally, as to the argument that the exclusionary <span class="star-pagination">*171</span> rule should not be extended to a "new" area, we cannot regard any such extension really to be at issue here. Despite the deep skepticism of Members of this Court as to the wisdom of extending the exclusionary rule to collateral areas, such as civil or grand jury proceedings, the Court has not questioned, in the absence of a more efficacious sanction, the continued application of the rule to suppress evidence from the State's case where a Fourth Amendment violation has been substantial and deliberate. See <i>Brewer</i> v. <i>Williams,</i> <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#422" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387, 422</a></span> (1977) (BURGER, C. J., dissenting); <i>Stone</i> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#538" aria-description="Citation for case: Stone v. Powell">428 U. S., at 538</a></span> (WHITE, J., dissenting). We see no principled basis for distinguishing between the question of the sufficiency of an affidavit, which also is subject to a post-search re-examination, and the question of its integrity.</p>
<p></p>
<h2>IV</h2>
<p>In sum, and to repeat with some embellishment what we stated at the beginning of this opinion: There is, of course, a presumption of validity with respect to the affidavit supporting the search warrant. To mandate an evidentiary hearing, the challenger's attack must be more than conclusory and must be supported by more than a mere desire to cross-examine. There must be allegations of deliberate falsehood or of reckless disregard for the truth, and those allegations must be accompanied by an offer of proof. They should point out specifically the portion of the warrant affidavit that is claimed to be false; and they should be accompanied by a statement of supporting reasons. Affidavits or sworn or otherwise reliable statements of witnesses should be furnished, or their absence satisfactorily explained. Allegations of negligence or innocent mistake are insufficient. The deliberate falsity or reckless disregard whose impeachment is permitted today is only that of the affiant, not of any nongovernmental informant. Finally, if these requirements are met, and if, when material that is the subject of the alleged falsity or reckless <span class="star-pagination">*172</span> disregard is set to one side, there remains sufficient content in the warrant affidavit to support a finding of probable cause, no hearing is required.<sup>[8]</sup> On the other hand, if the remaining content is insufficient, the defendant is entitled, under the Fourth and Fourteenth Amendments, to his hearing. Whether he will prevail at that hearing is, of course, another issue.</p>
<p>Because of Delaware's absolute rule, its courts did not have occasion to consider the proffer put forward by petitioner Franks. Since the framing of suitable rules to govern proffers is a matter properly left to the States, we decline ourselves to pass on petitioner's proffer. The judgment of the Supreme Court of Delaware is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p></p>
<h2>APPENDIX A TO OPINION OF THE COURT</h2>
                                      J. P. COURT #7
<p>IN THE MATTER OF: Jerome Franks, B/M, DOB: 10/9/54 and 222 S. Governors Ave., Apt. #3, Dover, Delaware. A two room apartment located on the South side, second floor, of a white block building on the west side of S. Governors Avenue, Between Loockerman Street and North Street, in the City of Dover. The ground floor of this building houses Wayman's Barber Shop.</p>
STATE OF DELAWARE
                     ss:
COUNTY OF KENT
<p>Be it remembered that on this 9th day of March A. D. <span class="star-pagination">*173</span> 1976 before me John Green, personally appeared Det. Ronald R. Brooks and Det. Larry Gray of the Dover Police Department who being by me duly sworn depose and say:</p>
<p>That they have reason to believe and do believe that in the 222 S. Governors Avenue, Apartment #3, Dover, Delaware. A two room apartment located on the south side second floor of a white block building on the west side of S. Governors Avenue between Loockerman Street and North Street in the City of Dover. The ground floor of this building houses Wayman's Barber Shop the occupant of which is Jerome Franks there has been and/or there is now located and/or concealed certain property in said house, place, conveyance and/or on the person or persons of the occupants thereof, consisting of property, papers, articles, or things which are the instruments of criminal offense, and/or obtained in the commission of a crime, and/or designated to be used in the commission of a crime, and not reasonably calculated to be used for any other purpose and/or the possession of which is unlawful, papers, articles, or things which are of an evidentiary nature pertaining to the commission of a crime or crimes specified therein and in particular, a white knit thermal undershirt; a brown 3/4 length leather jacket with a tie-belt; a pair of black mens pants; a dark colored knit hat; a long thin bladed knife or other instruments or items relating to the crime.</p>
<p>Articles, or things were, are, or will be possessed and/or used in violation of Title 11, Sub-Chapter D, Section 763, Delaware Code in that [see attached probable-cause page].</p>
<p>Wherefore, affiants pray that a search warrant may be issued authorizing a search of the aforesaid 222 S. Governors Avenue, Apartment #3, Dover, Delaware. A two room apartment located on the south side second floor of a white block building on the west side of S. Governors Avenue <span class="star-pagination">*174</span> between Loockerman St. and North Street, in the City of Dover in the manner provided by law.</p>
      /s/ Det. Ronald R. Brooks
          Affiant
      /s/ Det. Larry D. Gray
          Affiant
<p>SWORN to (or affirmed) and subscribed before me this 9th day of March A. D. 1976.</p>
      /s/ John [illegible] Green
          Judge Ct 7
<p>The facts tending to establish probable cause for the issuance of this search warrant are:</p>
<blockquote>1. On Saturday, 2/28/76, Brenda L. B. ______, W/F/15, reported to the Dover Police Department that she had been kidnapped and raped.</blockquote>
<blockquote>2. An investigation of this complaint was conducted by Det. Boyce Failing of the Dover Police Department.</blockquote>
<blockquote>3. Investigation of the aforementioned complaint revealed that Brenda B. ______, while under the influence of drugs, was taken to 222 S. Governors Avenue, Apartment 3, Dover, Delaware.</blockquote>
<blockquote>4. Investigation of the aforementioned complaint revealed that 222 S. Governors Avenue, Apartment #3, Dover, Delaware, is the residence of Jerome Franks, B/M DOB: 10/9/54.</blockquote>
<blockquote>5. Investigation of the aforementioned complaint revealed that on Saturday, 2/2[8]/76, Jerome Franks did have sexual contact with Brenda B. ______ without her consent.</blockquote>
<blockquote>6. On Thursday, 3/4/76 at the Dover Police Department, Brenda B. ______ revealed to Det. Boyce Failing that Jerome Franks was the person who committed the Sexual Assault against her.</blockquote>
<blockquote>7. On Friday, 3/5/76, Jerome Franks was placed under <span class="star-pagination">*175</span> arrest by Cpl. Robert McClements of the Dover Police Department, and charged with Sexual Misconduct.</blockquote>
<blockquote>8. On 3/5/76 at Family Court in Dover, Delaware, Jerome Franks did, after being arrested on the charge of Sexual Misconduct, ma[k]e a statement to Cpl. Robert McClements, that he thought the charge was concerning Cynthia Bailey not Brenda B. ______.</blockquote>
<blockquote>9. On Friday, 3/5/76, Cynthia C. Bailey, W/F/21 of 132 North Street, Dover, Delaware, did report to Dover Police Department that she had been raped at her residence during the night.</blockquote>
<blockquote>10. Investigation conducted by your affiant on Friday, 3/5/76, revealed the perpetrator of the crime to be an unknown black male, approximately 5′7″, 150 lbs., dark complexion, wearing white thermal undershirt, black pants with a belt having a silver or gold buckle, a brown leather 3/4 length coat with a tie belt in the front, and a dark knit cap pulled around the eyes.</blockquote>
<blockquote>11. Your affiant can state, that during the commission of this crime, Cynthia Bailey was forced at knife point and with the threat of death to engage in sexual intercourse with the perpetrator of the crime.</blockquote>
<blockquote>12. Your affiant can state that entry was gained to the residence of Cynthia Bailey through a window located on the east side of the residence.</blockquote>
<blockquote>13. Your affiant can state that the residence of Jerome Franks is within a very short distance and direct sight of the residence of Cynthia Bailey.</blockquote>
<blockquote>14. Your affiant can state that the description given by Cynthia Bailey of the unknown black male does coincide with the description of Jerome Franks.</blockquote>
<blockquote>15. On Tuesday, 3/9/76, your affiant contacted Mr. James Williams and Mr. Wesley Lucas of the Delaware Youth Center where Jerome Franks is employed and did have personal conversation with both these people.</blockquote>
<blockquote>
<span class="star-pagination">*176</span> 16. On Tuesday, 3/9/76, Mr. James Williams revealed to your affiant that the normal dress of Jerome Franks does consist of a white knit thermal undershirt and a brown leather jacket.</blockquote>
<blockquote>17. On Tuesday, 3/9/76, Mr. Wesley Lucas revealed to your affiant that in addition to the thermal undershirt and jacket, Jerome Franks often wears a dark green knit hat.</blockquote>
<blockquote>18. Your affiant can state that a check of official records reveals that in 1971 Jerome Franks was arrested for the crime of rape and subsequently convicted with Assault with intent to Rape.</blockquote>
<p></p>
<h2>APPENDIX B TO OPINION OF THE COURT</h2>
<p>States permitting veracity challenges include:</p>
Alabama:           <i>McConnell</i> v. <i>State,</i> <span class="citation" data-id="1769197"><a href="/opinion/1769197/mcconnell-v-state/#526" aria-description="Citation for case: McConnell v. State">48 Ala. App. 523, 526-528</a></span>,
                   <span class="citation" data-id="1769197"><a href="/opinion/1769197/mcconnell-v-state/#330" aria-description="Citation for case: McConnell v. State">266 So. 2d 328, 330-333</a></span> (Crim. App.),
                   cert. denied, <span class="citation multiple-matches"><a href="/c/Ala./289/746/">289 Ala. 746</a></span>, <span class="citation" data-id="1768917"><a href="/opinion/1768917/mcconnell-v-state/" aria-description="Citation for case: McConnell v. State">266 So. 2d 334</a></span>
                   (1972).
Alaska:            <i>Davenport</i> v. <i>State,</i> <span class="citation" data-id="1452068"><a href="/opinion/1452068/davenport-v-state/#380" aria-description="Citation for case: Davenport v. State">515 P. 2d 377, 380</a></span>
                   (1973).
Arizona:           <i>State</i> v. <i>Payne,</i> <span class="citation" data-id="1367322"><a href="/opinion/1367322/state-v-payne/#456" aria-description="Citation for case: State v. Payne">25 Ariz. App. 454, 456</a></span>, <span class="citation" data-id="1367322"><a href="/opinion/1367322/state-v-payne/#673" aria-description="Citation for case: State v. Payne">544
                   P. 2d 671, 673</a></span> (1976); cf. <i>State</i> v. <i>Pike,</i> <span class="citation" data-id="1148533"><a href="/opinion/1148533/state-v-pike/#513" aria-description="Citation for case: State v. Pike">113
                   Ariz. 511, 513-514</a></span>, <span class="citation" data-id="1148533"><a href="/opinion/1148533/state-v-pike/#1070" aria-description="Citation for case: State v. Pike">557 P. 2d 1068, 1070-1071</a></span>
                   (1976) (en banc).
Colorado:          <i>People</i> v. <i>Arnold,</i> <span class="citation" data-id="9548905"><a href="/opinion/1176912/people-v-arnold/#377" aria-description="Citation for case: People v. Arnold">186 Colo. 372, 377-378</a></span>,
                   <span class="citation" data-id="9548905"><a href="/opinion/1176912/people-v-arnold/#809" aria-description="Citation for case: People v. Arnold">527 P. 2d 806, 809</a></span> (1974) (en banc).
Iowa:              <i>State</i> v. <i>Boyd,</i> <span class="citation" data-id="1851918"><a href="/opinion/1851918/state-v-boyd/#616" aria-description="Citation for case: State v. Boyd">224 N. W. 2d 609, 616</a></span>
                   (1974) (en banc).
Louisiana:         <i>State</i> v. <i>Melson,</i> <span class="citation" data-id="1828817"><a href="/opinion/1828817/state-v-melson/#874" aria-description="Citation for case: State v. Melson">284 So. 2d 873, 874-875</a></span>
                   (1973), limiting <i>State</i> v. <i>Anselmo,</i> <span class="citation" data-id="9534579"><a href="/opinion/1130838/state-v-anselmo/#313" aria-description="Citation for case: State v. Anselmo">260
                   La. 306, 313-322</a></span>, <span class="citation" data-id="9534579"><a href="/opinion/1130838/state-v-anselmo/#101" aria-description="Citation for case: State v. Anselmo">256 So. 2d 98, 101-104</a></span>
                   (1971), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./407/911/">407 U. S. 911</a></span> (1972).
Massachusetts:     <i>Commonwealth</i> v. <i>Reynolds,</i> <span class="citation" data-id="2233092"><a href="/opinion/2233092/commonwealth-v-reynolds/#149" aria-description="Citation for case: Commonwealth v. Reynolds">374 Mass. 142,
                   149-151</a></span>, <span class="citation" data-id="2233092"><a href="/opinion/2233092/commonwealth-v-reynolds/#1379" aria-description="Citation for case: Commonwealth v. Reynolds">370 N. E. 2d 1375, 1379-1380</a></span>
                   (1977).
<span class="star-pagination">*177</span>
Minnesota:         <i>State</i> v. <i>Luciow,</i> <span class="citation" data-id="2215694"><a href="/opinion/2215694/state-v-luciow/#10" aria-description="Citation for case: State v. Luciow">308 Minn. 6, 10-13</a></span>, <span class="citation" data-id="2215694"><a href="/opinion/2215694/state-v-luciow/#837" aria-description="Citation for case: State v. Luciow">240
                   N. W. 2d 833, 837-838</a></span> (1976) (en banc).
Montana:           <i>State</i> v. <i>Nanoff,</i> <span class="citation" data-id="8026226"><a href="/opinion/8068009/state-v-nanoff/#348" aria-description="Citation for case: State v. Nanoff">160 Mont. 344, 348</a></span>, <span class="citation" data-id="8026226"><a href="/opinion/8068009/state-v-nanoff/#1140" aria-description="Citation for case: State v. Nanoff">502
                   P. 2d 1138, 1140</a></span> (1972), <i>sub silentio</i> overruling
                   <i>State</i> v. <i>English,</i> <span class="citation" data-id="8024116"><a href="/opinion/8066168/state-v-english/#350" aria-description="Citation for case: State v. English">71 Mont. 343, 350</a></span>,
                   <span class="citation" data-id="8024116"><a href="/opinion/8066168/state-v-english/#729" aria-description="Citation for case: State v. English">229 P. 727, 729</a></span> (1924).
New Hampshire:     <i>State</i> v. <i>Spero,</i> 177 N. H. 199, 204-205, <span class="citation" data-id="2365893"><a href="/opinion/2365893/state-v-spero/#1158" aria-description="Citation for case: State v. Spero">371
                   A. 2d 1155, 1158</a></span> (1977) (based on State
                   Constitution).
Pennsylvania:      <i>Commonwealth</i> v. <i>Hall,</i> <span class="citation" data-id="9757210"><a href="/opinion/2349003/commonwealth-v-hall/#204" aria-description="Citation for case: Commonwealth v. Hall">451 Pa. 201, 204</a></span>,
                   <span class="citation" data-id="9757210"><a href="/opinion/2349003/commonwealth-v-hall/#344" aria-description="Citation for case: Commonwealth v. Hall">302 A. 2d 342, 344</a></span> (1973).
South Carolina:    <i>State</i> v. <i>Sachs,</i> 264 S. C. 541, 556, <span class="citation" data-id="9616512"><a href="/opinion/1391098/state-v-sachs/#509" aria-description="Citation for case: State v. Sachs">216 S. E.
                   2d 501, 509</a></span> (1975).
Vermont:           <i>State</i> v. <i>Dupaw,</i> <span class="citation" data-id="1498442"><a href="/opinion/1498442/state-v-dupaw/#452" aria-description="Citation for case: State v. Dupaw">134 Vt. 451, 452-453</a></span>, <span class="citation" data-id="1498442"><a href="/opinion/1498442/state-v-dupaw/#968" aria-description="Citation for case: State v. Dupaw">365
                   A. 2d 967, 968</a></span> (1976).
Washington:        <i>State</i> v. <i>Lehman,</i> <span class="citation" data-id="1353828"><a href="/opinion/1353828/state-v-lehman/#414" aria-description="Citation for case: State v. Lehman">8 Wash. App. 408, 414</a></span>,
                   <span class="citation" data-id="1353828"><a href="/opinion/1353828/state-v-lehman/#1321" aria-description="Citation for case: State v. Lehman">506 P. 2d 1316, 1321</a></span> (1973) (Div. 3); <i>State</i>
                   v. <i>Goodlow,</i> <span class="citation" data-id="1163909"><a href="/opinion/1163909/state-v-goodlow/#535" aria-description="Citation for case: State v. Goodlow">11 Wash. App. 533, 535</a></span>, <span class="citation" data-id="1163909"><a href="/opinion/1163909/state-v-goodlow/#1206" aria-description="Citation for case: State v. Goodlow">523 P.
                   2d 1204, 1206</a></span> (1974) (Div. 1); cf. <i>State</i> v.
                   <i>Manly,</i> <span class="citation" data-id="9791370"><a href="/opinion/2609109/state-v-manly/#125" aria-description="Citation for case: State v. Manly">85 Wash. 2d 120, 125</a></span>, <span class="citation" data-id="9791370"><a href="/opinion/2609109/state-v-manly/#309" aria-description="Citation for case: State v. Manly">530 P. 2d
                   306, 309</a></span> (en banc), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./423/855/">423 U. S.
                   855</a></span> (1975).
<p>Five States, whose practice is dictated or may be dictated by statute, also permit veracity challenges:</p>
California:        <i>Theodor</i> v. <i>Superior Court,</i> <span class="citation" data-id="1180163"><a href="/opinion/1180163/theodor-v-superior-court/#90" aria-description="Citation for case: Theodor v. Superior Court">8 Cal. 3d 77, 90,
                   100-101</a></span>, <span class="citation" data-id="1180163"><a href="/opinion/1180163/theodor-v-superior-court/#243" aria-description="Citation for case: Theodor v. Superior Court">501 P. 2d 234, 243, 251</a></span> (1972)
                   (en banc); see Cal. Penal Code Ann.
                   §§ 1538.5, 1539, 1540 (West 1970 and Supp.
                   1978).
New York:          <i>People</i> v. <i>Alfinito,</i> 16 N. Y. 2d 181, 185-186,
                   <span class="citation" data-id="5522037"><a href="/opinion/5674467/people-v-alfinito/#646" aria-description="Citation for case: People v. Alfinito">211 N. E. 2d 644, 646</a></span> (1965); <i>People</i> v.
                   <i>Slaughter,</i> 37 N. Y. 2d 596, 600, <span class="citation" data-id="5529933"><a href="/opinion/5681518/people-v-slaughter/#624" aria-description="Citation for case: People v. Slaughter">338 N. E.
                   2d 622, 624</a></span> (1975); see N. Y. Code Crim.
                   Proc. §§ 813-c, 813-d, 813-e (McKinney
<span class="star-pagination">*178</span>
                   Supp. 1970-1971), superseded by N. Y.
                   Crim. Proc. Law, Art. 710 (McKinney
                   Supp. 1977-1978).
North Carolina:    See N. C. Gen. Stat. § 15A-978 (1978).
Oregon:            <i>State</i> v. <i>Wright,</i> <span class="citation" data-id="1183476"><a href="/opinion/1183476/state-v-wright/#168" aria-description="Citation for case: State v. Wright">266 Ore. 163, 168-169, n. 3</a></span>,
                   <span class="citation" data-id="1183476"><a href="/opinion/1183476/state-v-wright/#1225" aria-description="Citation for case: State v. Wright">511 P. 2d 1223, 1225-1226, n. 3</a></span> (1973) (en
                   banc); see Ore. Rev. Stat. § 133.693 (1977).
Utah:              <i>State</i> v. <i>Bankhead,</i> <span class="citation" data-id="1451648"><a href="/opinion/1451648/state-v-bankhead/#138" aria-description="Citation for case: State v. Bankhead">30 Utah 2d 135, 138</a></span>, <span class="citation" data-id="1451648"><a href="/opinion/1451648/state-v-bankhead/#802" aria-description="Citation for case: State v. Bankhead">514
                   P. 2d 800, 802</a></span> (1973); see <span class="citation no-link">Utah Code Ann.
                   §§ 77-54-17</span>, 77-54-18 (1953).
<p>Two other States are more doubtful, but seem to allow veracity challenges:</p>
Michigan:          <i>People</i> v. <i>Burt,</i> <span class="citation" data-id="3493017"><a href="/opinion/3523662/people-v-burt/#74" aria-description="Citation for case: People v. Burt">236 Mich. 62, 74</a></span>, <span class="citation" data-id="3493017"><a href="/opinion/3523662/people-v-burt/#101" aria-description="Citation for case: People v. Burt">210 N. W.
                   97, 101</a></span> (1926).
New Mexico:        <i>State</i> v. <i>Baca,</i> 84 N. M. 513, 515, <span class="citation" data-id="1445282"><a href="/opinion/1445282/state-v-baca/#858" aria-description="Citation for case: State v. Baca">505 P.
                   2d 856, 858</a></span> (1973) (dictum).
<p>The following States have disposed of particular veracity challenges on the ground the affidavits were in fact not false, or that any misstatements were immaterial or unintentional or were not by the affiant himself:</p>
Florida:           <i>McDougall</i> v. <i>State,</i> <span class="citation" data-id="1886978"><a href="/opinion/1886978/mcdougall-v-state/#625" aria-description="Citation for case: McDougall v. State">316 So. 2d 624, 625</a></span>
                   (Dist. Ct. App. 1975).
Georgia:           <i>Williams</i> v. <i>State,</i> <span class="citation" data-id="1363434"><a href="/opinion/1363434/williams-v-state/#213" aria-description="Citation for case: Williams v. State">232 Ga. 213, 213-214</a></span>,
                   <span class="citation" data-id="1363434"><a href="/opinion/1363434/williams-v-state/#860" aria-description="Citation for case: Williams v. State">205 S. E. 2d 859, 860</a></span> (1974); <i>Lee</i> v. <i>State,</i>
                   <span class="citation" data-id="1424506"><a href="/opinion/1424506/lee-v-state/#773" aria-description="Citation for case: Lee v. State">239 Ga. 769, 773-774</a></span>, <span class="citation" data-id="1424506"><a href="/opinion/1424506/lee-v-state/#856" aria-description="Citation for case: Lee v. State">238 S. E. 2d 852, 856</a></span>
                   (1977); <i>Birge</i> v. <i>State,</i> <span class="citation" data-id="1415130"><a href="/opinion/1415130/birge-v-state/#633" aria-description="Citation for case: Birge v. State">143 Ga. App. 632,
                   633</a></span>, <span class="citation" data-id="1415130"><a href="/opinion/1415130/birge-v-state/#397" aria-description="Citation for case: Birge v. State">239 S. E. 2d 395, 397</a></span> (1977).
Indiana:           <i>Moore</i> v. <i>State,</i> <span class="citation" data-id="2060217"><a href="/opinion/2060217/moore-v-state/#385" aria-description="Citation for case: Moore v. State">159 Ind. App. 381, 385-386</a></span>,
                   <span class="citation" data-id="2060217"><a href="/opinion/2060217/moore-v-state/#94" aria-description="Citation for case: Moore v. State">307 N. E. 2d 92, 94-95</a></span> (1974); <i>Grzesiowski</i>
                   v. <i>State,</i> <span class="citation" data-id="2221046"><a href="/opinion/2221046/grzesiowski-v-state/#328" aria-description="Citation for case: Grzesiowski v. State">168 Ind. App. 318, 328</a></span>, <span class="citation" data-id="2221046"><a href="/opinion/2221046/grzesiowski-v-state/#312" aria-description="Citation for case: Grzesiowski v. State">343
                   N. E. 2d 305, 312</a></span> (1976); but see <i>Seager</i> v.
                   <i>State,</i> <span class="citation" data-id="3423317"><a href="/opinion/3426273/seager-v-state/#582" aria-description="Citation for case: Seager v. State">200 Ind. 579, 582</a></span>, <span class="citation" data-id="3423317"><a href="/opinion/3426273/seager-v-state/#275" aria-description="Citation for case: Seager v. State">164 N. E. 274, 275</a></span>
                   (1928).
<span class="star-pagination">*179</span>
Ohio:              <i>State</i> v. <i>Dodson,</i> <span class="citation" data-id="3744266"><a href="/opinion/3991275/state-v-dodson/#35" aria-description="Citation for case: State v. Dodson">43 Ohio App. 2d 31, 35-36</a></span>,
                   <span class="citation" data-id="3744266"><a href="/opinion/3991275/state-v-dodson/#374" aria-description="Citation for case: State v. Dodson">332 N. E. 2d 371, 374-375</a></span> (1974).
Wisconsin:         <i>Scott</i> v. <i>State,</i> <span class="citation" data-id="1311035"><a href="/opinion/1311035/scott-v-state/#511" aria-description="Citation for case: Scott v. State">73 Wis. 2d 504, 511-512</a></span>, <span class="citation" data-id="1311035"><a href="/opinion/1311035/scott-v-state/#219" aria-description="Citation for case: Scott v. State">243
                   N. W. 2d 215, 219</a></span> (1976).
Cf. Maine:         <i>State</i> v. <i>Koucoules,</i> <span class="citation" data-id="2184913"><a href="/opinion/2184913/state-v-koucoules/" aria-description="Citation for case: State v. Koucoules">343 A. 2d 860</a></span>, 865 n. 3
                   (1974).
<p>Eleven States flatly prohibit veracity challenges:</p>
Arkansas:          <i>Liberto</i> v. <i>State,</i> <span class="citation" data-id="1631048"><a href="/opinion/1631048/liberto-v-state/#356" aria-description="Citation for case: Liberto v. State">248 Ark. 350, 356-357</a></span>, <span class="citation" data-id="1631048"><a href="/opinion/1631048/liberto-v-state/#468" aria-description="Citation for case: Liberto v. State">451
                   S. W. 2d 464, 468</a></span> (1970) (alternative holding);
                   cf. <i>Powell</i> v. <i>State,</i> <span class="citation" data-id="2467369"><a href="/opinion/2467369/powell-v-state/#383" aria-description="Citation for case: Powell v. State">260 Ark. 381, 383</a></span>,
                   <span class="citation" data-id="2467369"><a href="/opinion/2467369/powell-v-state/#2" aria-description="Citation for case: Powell v. State">540 S. W. 2d 1, 2</a></span> (1976).
Connecticut:       <i>State</i> v. <i>Williams,</i> <span class="citation" data-id="2398659"><a href="/opinion/2398659/state-v-williams/#327" aria-description="Citation for case: State v. Williams">169 Conn. 322, 327-329</a></span>,
                   <span class="citation" data-id="2398659"><a href="/opinion/2398659/state-v-williams/#76" aria-description="Citation for case: State v. Williams">363 A. 2d 72, 76-77</a></span> (1975).
Illinois:          <i>People</i> v. <i>Bak,</i> <span class="citation" data-id="9884743"><a href="/opinion/2133918/the-people-v-bak/#144" aria-description="Citation for case: The People v. Bak">45 Ill. 2d 140, 144-146</a></span>, <span class="citation" data-id="9884743"><a href="/opinion/2133918/the-people-v-bak/#343" aria-description="Citation for case: The People v. Bak">258
                   N. E. 2d 341, 343-344</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./400/882/">400
                   U. S. 882</a></span> (1970); <i>People</i> v. <i>Stansberry,</i> <span class="citation" data-id="9884688"><a href="/opinion/2120568/the-people-v-stansberry/#544" aria-description="Citation for case: The PEOPLE v. Stansberry">47
                   Ill. 2d 541, 544</a></span>, <span class="citation" data-id="9884688"><a href="/opinion/2120568/the-people-v-stansberry/#433" aria-description="Citation for case: The PEOPLE v. Stansberry">268 N. E. 2d 431, 433</a></span>, cert.
                   denied, <span class="citation multiple-matches"><a href="/c/U.%20S./404/873/">404 U. S. 873</a></span> (1971).
Kansas:            <i>State</i> v. <i>Lamb,</i> <span class="citation" data-id="1306980"><a href="/opinion/1306980/state-v-lamb/#467" aria-description="Citation for case: State v. Lamb">209 Kan. 453, 467-468</a></span>, <span class="citation" data-id="1306980"><a href="/opinion/1306980/state-v-lamb/#287" aria-description="Citation for case: State v. Lamb">497
                   P. 2d 275, 287</a></span> (1972); <i>State</i> v. <i>Sanders,</i> <span class="citation" data-id="1285341"><a href="/opinion/1285341/state-v-sanders/#194" aria-description="Citation for case: State v. Sanders">222
                   Kan. 189, 194-196</a></span>, <span class="citation" data-id="1285341"><a href="/opinion/1285341/state-v-sanders/#466" aria-description="Citation for case: State v. Sanders">563 P. 2d 461, 466-467</a></span>
                   (alternative holding), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./434/833/">434
                   U. S. 833</a></span> (1977).
Kentucky:          <i>Caslin</i> v. <i>Commonwealth,</i> <span class="citation" data-id="1530851"><a href="/opinion/1530851/caslin-v-commonwealth/#834" aria-description="Citation for case: Caslin v. Commonwealth">491 S. W. 2d 832,
                   834</a></span> (1973).
Maryland:          <i>Smith</i> v. <i>State,</i> <span class="citation" data-id="3486405"><a href="/opinion/3488471/smith-v-state/#334" aria-description="Citation for case: Smith v. State">191 Md. 329, 334-336</a></span>, <span class="citation" data-id="3486405"><a href="/opinion/3488471/smith-v-state/#289" aria-description="Citation for case: Smith v. State">62 A.
                   2d 287, 289-290</a></span> (1948), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./336/925/">336
                   U. S. 925</a></span> (1949); <i>Tucker</i> v. <i>State,</i> <span class="citation" data-id="2053522"><a href="/opinion/2053522/tucker-v-state/#499" aria-description="Citation for case: Tucker v. State">244 Md.
                   488, 499-500</a></span>, <span class="citation" data-id="2053522"><a href="/opinion/2053522/tucker-v-state/#117" aria-description="Citation for case: Tucker v. State">224 A. 2d 111, 117-118</a></span>
                   (1966), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./386/1024/">386 U. S. 1024</a></span> (1967);
                   <i>Dawson</i> v. <i>State,</i> <span class="citation" data-id="1895767"><a href="/opinion/1895767/dawson-v-state/#713" aria-description="Citation for case: Dawson v. State">11 Md. App. 694, 713-715</a></span>,
                   <span class="citation" data-id="1895767"><a href="/opinion/1895767/dawson-v-state/#690" aria-description="Citation for case: Dawson v. State">276 A. 2d 680, 690-691</a></span> (1971).
Mississippi:       <i>Wood</i> v. <i>State,</i> <span class="citation" data-id="1850125"><a href="/opinion/1850125/wood-v-state/#465" aria-description="Citation for case: Wood v. State">322 So. 2d 462, 465</a></span> (1975).
<span class="star-pagination">*180</span>
New Jersey:        <i>State</i> v. <i>Petillo,</i> 61 N. J. 165, 173-179, <span class="citation" data-id="2341043"><a href="/opinion/2341043/state-v-petillo/#653" aria-description="Citation for case: State v. Petillo">293
                   A. 2d 649, 653-656</a></span> (1972), cert. denied,
                   <span class="citation multiple-matches"><a href="/c/U.%20S./410/945/">410 U. S. 945</a></span> (1973); but see 61 N. J., at
                   178 n. 1, <span class="citation" data-id="2341043"><a href="/opinion/2341043/state-v-petillo/" aria-description="Citation for case: State v. Petillo">293 A. 2d, at 656</a></span> n. 1.
Oklahoma:          <i>Brown</i> v. <i>State,</i> <span class="citation" data-id="9559541"><a href="/opinion/1198737/brown-v-state/" aria-description="Citation for case: Brown v. State">565 P. 2d 697</a></span> (Crim. App.
                   1977), overruling <i>McCaskey</i> v. <i>State,</i> <span class="citation" data-id="1190217"><a href="/opinion/1190217/mccaskey-v-state/#1311" aria-description="Citation for case: McCaskey v. State">534
                   P. 2d 1309, 1311-1312</a></span> (Crim. App. 1975),
                   and <i>Henderson</i> v. <i>State,</i> <span class="citation" data-id="1437089"><a href="/opinion/1437089/henderson-v-state/#789" aria-description="Citation for case: Henderson v. State">490 P. 2d 786, 789</a></span>
                   (Crim. App. 1971), and reaffirming <i>Gaddis</i>
                   v. <i>State,</i> <span class="citation" data-id="9574534"><a href="/opinion/1312713/gaddis-v-state/" aria-description="Citation for case: Gaddis v. State">447 P. 2d 42</a></span> (Crim. App. 1968).
Tennessee:         <i>Owens</i> v. <i>State,</i> <span class="citation" data-id="2442476"><a href="/opinion/2442476/owens-v-state/#553" aria-description="Citation for case: Owens v. State">217 Tenn. 544, 553</a></span>, <span class="citation" data-id="2442476"><a href="/opinion/2442476/owens-v-state/#511" aria-description="Citation for case: Owens v. State">399
                   S. W. 2d 507, 511</a></span> (1965); <i>Poole</i> v. <i>State,</i> 4
                   Tenn. Crim. 41, 53-54, <span class="citation" data-id="2379504"><a href="/opinion/2379504/poole-v-state/#832" aria-description="Citation for case: Poole v. State">467 S. W. 2d 826,
                   832</a></span>, cert. denied, <i><span class="citation" data-id="2379504"><a href="/opinion/2379504/poole-v-state/" aria-description="Citation for case: Poole v. State">ibid.</a></span></i> (1971).
Texas:             <i>Phenix</i> v. <i>State,</i> <span class="citation" data-id="2386408"><a href="/opinion/2386408/phenix-v-state/#765" aria-description="Citation for case: Phenix v. State">488 S. W. 2d 759, 765</a></span>
                   (Crim. App. 1972); <i>Oubre</i> v. <i>State,</i> <span class="citation" data-id="1760963"><a href="/opinion/1760963/oubre-v-state/#877" aria-description="Citation for case: Oubre v. State">542
                   S. W. 2d 875, 877</a></span> (Crim. App. 1976).
<p>Two States have prohibited challenges that were directed seemingly against the conclusory nature of the affidavits, rather than their veracity.</p>
Missouri:          <i>State</i> v. <i>Brugioni,</i> <span class="citation" data-id="3535850"><a href="/opinion/3558063/state-v-brugioni/#206" aria-description="Citation for case: State v. Brugioni">320 Mo. 202, 206</a></span>, <span class="citation" data-id="3535850"><a href="/opinion/3558063/state-v-brugioni/#263" aria-description="Citation for case: State v. Brugioni">7 S. W.
                   2d 262, 263</a></span> (1928).
Rhode Island:      <i>State</i> v. <i>Seymour,</i> 46 R. I. 257, 260, <span class="citation" data-id="3865272"><a href="/opinion/4105545/state-v-seymour/#756" aria-description="Citation for case: State v. Seymour">126 A.
                   755, 756</a></span> (1924), partially overruled, <i>State</i>
                   v. <i>LeBlanc,</i> 100 R. I. 523, 528-529, <span class="citation" data-id="1987009"><a href="/opinion/1987009/state-v-leblanc/#474" aria-description="Citation for case: State v. LeBlanc">217 A.
                   2d 471, 474</a></span> (1966); but see <i>State</i> v. <i>Cofone,</i>
                   112 R. I. 760, 766-767, <span class="citation" data-id="1973195"><a href="/opinion/1973195/state-v-cofone/#755" aria-description="Citation for case: State v. Cofone">315 A. 2d 752, 755-756</a></span>
                   (1974).
<p>MR. JUSTICE REHNQUIST, with whom THE CHIEF JUSTICE joins, dissenting.</p>
<p>The Court's opinion in this case carefully identifies the factors which militate against the result which it reaches, and emphasizes their weight in attempting to limit the circumstances <span class="star-pagination">*181</span> under which an affidavit supporting a search warrant may be impeached. I am not ultimately persuaded, however, that the Court is correct as a matter of constitutional law that the impeachment of such an affidavit must be permitted under the circumstances described by the Court, and I am thoroughly persuaded that the barriers which the Court believes that it is erecting against misuse of the impeachment process are frail indeed.</p>
<p></p>
<h2>I</h2>
<p>The Court's reliance on <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (1948), for the proposition that a determination by a neutral magistrate is a prerequisite to the sufficiency of an application for a warrant is obviously correct. In that case the Court said:</p>
<blockquote>"The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime." <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States"><i>Id.,</i> at 13-14</a></span>.</blockquote>
<p>The notion that there may be incorrect or even deliberately falsified information presented to a magistrate in the course of an effort to obtain a search warrant does not render the proceeding before a magistrate any different from any other factfinding procedure known to the law. The Court here says that "it would be an unthinkable imposition upon [the magistrate's] authority if a warrant affidavit, revealed after the fact to contain a deliberately or recklessly false statement, were to stand beyond impeachment." <i>Ante,</i> at 165. I do not believe that this flat statement survives careful analysis.</p>
<p>If the function of the warrant requirement is to obtain the determination of a neutral magistrate as to whether sufficient <span class="star-pagination">*182</span> grounds have been urged to support the issuance of a warrant, that function is fulfilled at the time the magistrate concludes that the requirement has been met. Like any other determination of a magistrate, of a court, or of countless other factfinding tribunals, the decision may be incorrect as a matter of law. Even if correct, some inaccurate or falsified information may have gone into the making of the determination. But unless we are to exalt as the <i>ne plus ultra</i> of our system of criminal justice the absolute correctness of every factual determination made along the tortuous route from the filing of the complaint or the issuance of an indictment to the final determination that a judgment of conviction was properly obtained, we shall lose perspective as to the purposes of the system as well as of the warrant requirement of the Fourth and Fourteenth Amendments. Much of what Mr. Justice Harlan said in his separate opinion in <i>Mackey</i> v. <i>United States,</i> <span class="citation" data-id="9424506"><a href="/opinion/108302/mackey-v-united-states/" aria-description="Citation for case: MacKey v. United States">401 U. S. 667</a></span> (1971), with respect to collateral relief from a criminal conviction is likewise applicable to collateral impeachment of a search warrant:</p>
<blockquote>"At some point, the criminal process, if it is to function at all, must turn its attention from whether a man ought properly to be incarcerated to how he is to be treated once convicted. If law, criminal or otherwise, is worth having and enforcing, it must at some time provide a definitive answer to the questions litigants present or else it never provides an answer at all. Surely it is an unpleasant task to strip a man of his freedom and subject him to institutional restraints. But this does not mean that in so doing, we should always be halting or tentative. No one, not criminal defendants, not the judicial system, not society as a whole is benefited by a judgment providing a man shall tentatively go to jail today, but tomorrow and every day thereafter his continued incarceration shall be subject to fresh litigation on issues already resolved.</blockquote>
<blockquote>
<span class="star-pagination">*183</span> "A rule of law that fails to take account of these finality interests would do more than subvert the criminal process itself. It would also seriously distort the very limited resources society has allocated to the criminal process. While men languish in jail, not uncommonly for over a year, awaiting a first trial on their guilt or innocence, it is not easy to justify expending substantial quantities of the time and energies of judges, prosecutors, and defense lawyers litigating the validity under present law of criminal convictions that were perfectly free from error when made final. [Citation omitted.] This drain on society's resources is compounded by the fact that issuance of the habeas writ compels a State that wishes to continue enforcing its laws against the successful petitioner to relitigate facts buried in the remote past through presentation of witnesses whose memories of the relevant events often have dimmed. This very act of trying stale facts may well, ironically, produce a second trial no more reliable as a matter of getting at the truth than the first." <span class="citation" data-id="9424506"><a href="/opinion/108302/mackey-v-united-states/#690" aria-description="Citation for case: MacKey v. United States"><i>Id.,</i> at 690-691</a></span>.</blockquote>
<p>I am quite confident that if our system of justice were not administered by judges who were once lawyers, it might well be less satisfactory than it now is. But I am equally confident that one improvement which would manifest itself as a result of such a change would be a willingness, reflected in almost all callings in our society except lawyers, to refrain from constant relitigation, whether in the form of collateral attack, appeal, retrial, or whatever, of issues that have originally been decided by a competent authority.</p>
<p>It would be extraordinarily troubling in any system of criminal justice if a verdict or finding of guilt, later conclusively shown to be based on false testimony, were to result in the incarceration of the accused notwithstanding this fact. But the Court's reference to the "unthinkable imposition" of not allowing the impeachment of an affiant's testimony in support <span class="star-pagination">*184</span> of a search warrant is a horse of quite another color. Particularly in view of the many hurdles which the prosecution must surmount to ultimately obtain and retain a finding of guilt in the light of the many constitutional safeguards which surround a criminal accused, it is essential to understand the role of a search warrant in the process which may lead to the conviction of such an accused. The warrant issued on impeachable testimony has, by hypothesis, turned up incriminating and admissible evidence to be considered by the jury at the trial. The fact that it was obtained by reason of an impeachable warrant bears not at all on the innocence or guilt of the accused. The only conceivable harm done by such evidence is to the accused's rights under the Fourth and Fourteenth Amendments, which have nothing to do with his guilt or innocence of the crime with which he is charged.</p>
<p>Given the definitive exposition of the warrant requirement quoted above from <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S., at 13-14</a></span>, it seems to me it would be quite reasonable for this Court, consistently with the Fourth and Fourteenth Amendments, to adopt any one of three positions with respect to the impeachability of a search warrant which had been in fact issued by a neutral magistrate who satisfied the requirements of <i>Shadwick</i> v. <i>Tampa,</i> <span class="citation" data-id="108582"><a href="/opinion/108582/shadwick-v-city-of-tampa/" aria-description="Citation for case: Shadwick v. City of Tampa">407 U. S. 345</a></span> (1972).</p>
<p>First, it could decide that the warrant requirement was satisfied when such a magistrate had been persuaded, and allow no further collateral attack on the warrant. In <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), the Court in reliance on <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span> (1958), a case concededly decided pursuant to Fed. Rule Crim. Proc. 4, nonetheless held that the determination by a magistrate that the affidavit submitted to him made out "probable cause" for purposes of the Fourth and Fourteenth Amendments was subject to later judicial review as to the sufficiency of the affidavit. This rule was later reaffirmed in <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969). The Court has thus for more than a decade <span class="star-pagination">*185</span> rejected the first possible stopping place in judicial re-examination of affidavits in support of warrants, and held that the legal determination as to probable cause was subject to collateral attack. While this conclusion does not seem to me to flow inexorably from the Fourth Amendment, I think that it makes a good deal of sense in light of the fact that a magistrate need not be a trained lawyer, see <i><span class="citation" data-id="108582"><a href="/opinion/108582/shadwick-v-city-of-tampa/" aria-description="Citation for case: Shadwick v. City of Tampa">Shadwick, supra,</a></span></i> and therefore may not be versed in the latest nuances of what is or what is not "probable cause" for purposes of the Fourth Amendment.</p>
<p>But to allow collateral examination of an affidavit in support of a warrant on a legal ground such as that is quite different from the rejection of the second possible stopping place as the Court does today. Magistrates need not be lawyers, but lawyers have no monopoly on determining whether or not an affiant who appears before them is or is not telling the truth. Indeed, a magistrate whose time may be principally spent in conducting preliminary hearings and trying petty offenses may have every bit as good a feel for the veracity of a particular witness as a judge of a court of general jurisdiction.</p>
<p>True, a warrant is issued <i>ex parte,</i> without an opportunity for the person whose effects are to be seized to impeach the testimony of the affiant. The proceeding leading to the issuance of a warrant is, therefore, obviously less reliable and less likely to be a searching inquiry into the truth of the affiant's statements than is a full-dress adversary proceeding. But it is at this point that I part company with the Court in its underlying assumption that somehow a full-dress adversary proceeding will virtually guarantee a truthful answer to the question of whether or not the affiant seeking the warrant falsified his testimony. A full-dress adversary proceeding is undoubtedly a better vehicle than an <i>ex parte</i> proceeding for arriving at the truth of any particular inquiry, but it is scarcely a guarantee of truth. Mr. Justice Jackson in his <span class="star-pagination">*186</span> opinion concurring in the result in <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">344 U. S. 443</a></span> (1953), observed with respect to purely legal issues decided by this Court:</p>
<blockquote>"However, reversal by a higher court is not proof that justice is thereby better done. There is no doubt that if there were a super-Supreme Court, a substantial proportion of our reversals of state courts would also be reversed. We are not final because we are infallible, but we are infallible only because we are final." <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#540" aria-description="Citation for case: Brown v. Allen"><i>Id.,</i> at 540</a></span>.</blockquote>
<p>The same is surely true of a judge's review of the factual determinations of a magistrate; a larger percentage of the judge's findings as to the truth of an affiant's statement may be objectively correct than the percentage of the magistrate's determinations which are, but neither one is going to be 100 percent. Since once the warrant is issued and the search is made, the privacy interest protected by the Fourth and Fourteenth Amendments is breached, a subsequent determination that it was wrongfully breached cannot possibly restore the privacy interest. See <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">414 U. S. 338</a></span> (1974). Since the evidence obtained pursuant to the warrant is by hypothesis relevant and admissible on the issue of guilt, the only purpose served by suppression of such evidence is deterrence of falsified testimony on the part of affiant in the future. Without attempting to summarize the many cases in which this Court has discussed the balance to be struck in such situations, see <i>United States</i> v. <i>Peltier,</i> <span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/" aria-description="Citation for case: United States v. Peltier">422 U. S. 531</a></span> (1975), I simply do not think the game is worth the candle in this situation.</p>
<p>As the Court's opinion points out, the other jurisdictions which have considered this question are divided, although a majority of them favor the result reached by the Court today. The signed articles and student law review notes which the Court refers to in its opinion are not there, I trust, to be considered <i>en bloc</i> or by some process of counting without weighing. Presumably, to the extent that their reasoning <span class="star-pagination">*187</span> commends itself to the courts which are committed to decide these questions, that reasoning will find its way into the opinions of those courts; to the extent that the reasoning does not so commend itself, the piece containing the reasoning does not weigh in the scales of decision simply because it appeared in a periodical devoted to the discussion of legal questions.</p>
<p></p>
<h2>II</h2>
<p>The Court has commendably, in my opinion, surrounded the right to impeach the affidavit relied upon to support the issuance of a warrant with numerous limitations. My fear, and I do not think it an unjustified one, is that these limitations will quickly be subverted in actual practice. The Court states:</p>
<blockquote>"Nor, if a sensible threshold showing is required and sensible substantive requirements for suppression are maintained, need there be any new large-scale commitment of judicial resources; many claims will wash out at an early stage, and the more substantial ones in any event would require judicial resources for vindication if the suggested alternative sanctions were truly to be effective. The requirement of a substantial preliminary showing should suffice to prevent the misuse of a veracity hearing for purposes of discovery or obstruction." <i>Ante,</i> at 170.</blockquote>
<p>I greatly fear that this generalized language will afford insufficient protection against the natural tendency of ingenious lawyers charged with representing their client's cause to ceaselessly undermine the limitations which the Court has placed on impeachment of the affidavit offered in support of a search warrant. I am sure that the Court is sincere in its expressed hope that the doctrine which it adopts will not lead to "any new large-scale commitment of judicial resources," but in the end I am led once more to echo the <span class="star-pagination">*188</span> observation contained in another opinion of Mr. Justice Jackson:</p>
<blockquote>"The case which irresistibly comes to mind as the most fitting precedent is that of Julia who, according to Byron's reports, `whispering "I will ne'er consent,"consented.'" <i>Everson</i> v. <i>Board of Education,</i> <span class="citation" data-id="9419925"><a href="/opinion/104373/everson-v-board-of-ed-of-ewing/#19" aria-description="Citation for case: Everson v. Board of Ed. of Ewing">330 U. S. 1, 19</a></span> (1947) (dissenting opinion).</blockquote>
<p>Since I would not "consent" even to the extent that the Court does in its opinion, I dissent from that opinion and would affirm the judgment of the Supreme Court of Delaware.</p>
<h2>NOTES</h2>
<p>[*]  Briefs of <i>amici curiae</i> were filed by <i>Solicitor General McCree, Assistant Attorney General Civiletti, Kenneth S. Geller, Jerome M. Feit,</i> and <i>Paul J. Brysh</i> for the United States, and by <i>Bruce J. Ennis</i> for the American Civil Liberties Union.</p>
<p>[1]  The affidavit is reproduced as Appendix A to this opinion. <i>Post,</i> at 172.</p>
<p>[2]  The references in paragraphs 15 and 16 of the warrant affidavit's probable-cause page to "James Williams" appear to have been intended as references to James D. Morrison, who was petitioner's supervisor at the Youth Center. Tr. 269. This misapprehension on the part of the State continued until shortly before trial. Eleven days prior to trial, the prosecution requested the Clerk of the Kent Country Superior Court to summon "James Williams, Delaware Youth Center," for petitioner's trial. In his return on the summons, Record Doc. No. 16, the Kent County Sheriff stated that he "[s]erved the within summons upon . . . James Williams (Morrison)." The summons actually delivered was made out in the name of James Morrison.</p>
<p>[3]  It appears this is no longer the majority rule among the States. Compare Comment, <span class="citation no-link">7 Seton Hall L. Rev. 827</span>, 844 (1976) (about half of the States have addressed the issue, and the weight of authority is "slightly in favor" of permitting veracity challenges), with <i>North Carolina</i> v. <i>Wrenn,</i> <span class="citation" data-id="8991165"><a href="/opinion/8998746/north-carolina-v-wrenn/" aria-description="Citation for case: North Carolina v. Wrenn">417 U. S. 973</a></span> (1974) (WHITE, J., dissenting from denial of certiorari) (majority of state decisions prohibit subsequent impeachment of an affidavit).
</p>
<p>By our count, 19 States, and perhaps as many as 21, permit veracity challenges; 5 of these apparently rely on statutory provisions in so holding. Five States have disposed of particular veracity challenges on the ground there was no misstatement, or that any misstatement was immaterial or unintentional, without opining what would be done when there is a deliberate and material misrepresentation. There are now only 11 States that prohibit veracity challenges outright. Another two have barred impeachment challenges that seemed directed at the conclusory nature of affidavit allegations rather than at their veracity.</p>
<p>The case law is detailed in Appendix B. <i>Post,</i> at 176.</p>
<p>[4]  This reasoning is misplaced. The Federal Courts of Appeals decisions allowing a defendant to challenge the veracity of a warrant affidavit rest on a constitutional footing. See <i>United States</i> v. <i>Belculfine,</i> <span class="citation" data-id="324012"><a href="/opinion/324012/united-states-v-joseph-l-belculfine/#61" aria-description="Citation for case: United States v. Joseph L. Belculfine">508 F. 2d 58, 61, 63</a></span> (CA1 1974); <i>United States</i> v. <i>Dunnings,</i> <span class="citation" data-id="9455592"><a href="/opinion/289921/united-states-v-edward-dunnings/#839" aria-description="Citation for case: United States v. Edward Dunnings">425 F. 2d 836, 839-840</a></span> (CA2 1969), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./397/1002/">397 U. S. 1002</a></span> (1970); <i>United States</i> v. <i>Armocida,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/515/29/">515 F. 2d 29</a></span>, 41 (CA3), cert. denied <i>sub nom. </i><i>Gazal</i> v. <i>United States,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./423/858/">423 U. S. 858</a></span> (1975); <i>United States</i> v. <i>Lee,</i> <span class="citation" data-id="9463031"><a href="/opinion/338672/united-states-v-bernard-jerome-lee-aka-james-wesley-carter/#1208" aria-description="Citation for case: United States v. Bernard Jerome Lee, A/K/A James Wesley...">540 F. 2d 1205, 1208-1209</a></span> (CA4), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./429/894/">429 U. S. 894</a></span> (1976); <i>United States</i> v. <i>Thomas,</i> <span class="citation" data-id="315831"><a href="/opinion/315831/united-states-v-titus-thomas-aka-tee/#668" aria-description="Citation for case: United States v. Titus Thomas, AKA Tee">489 F. 2d 664, 668, 671</a></span> (CA5 1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./423/844/">423 U. S. 844</a></span> (1975); <i>United States</i> v. <i>Luna,</i> <span class="citation" data-id="331000"><a href="/opinion/331000/united-states-v-gilbert-luna/#8" aria-description="Citation for case: United States v. Gilbert Luna">525 F. 2d 4, 8</a></span> (CA6 1975), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./424/965/">424 U. S. 965</a></span> (1976); <i>United States</i> v. <i>Carmichael,</i> <span class="citation" data-id="316109"><a href="/opinion/316109/united-states-v-robert-e-carmichael/#988" aria-description="Citation for case: United States v. Robert E. Carmichael">489 F. 2d 983, 988-989</a></span> (CA7 1973) (en banc); <i>United States</i> v. <i>Marihart,</i> <span class="citation" data-id="9460368"><a href="/opinion/317254/united-states-v-james-marihart/#898" aria-description="Citation for case: United States v. James Marihart">492 F. 2d 897, 898</a></span> (CA8), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./419/827/">419 U. S. 827</a></span> (1974); <i>United States</i> v. <i>Damitz,</i> <span class="citation" data-id="318456"><a href="/opinion/318456/united-states-v-dwight-edward-damitz-united-states-of-america-v-harry/#54" aria-description="Citation for case: United States v. Dwight Edward Damitz, United States of...">495 F. 2d 50, 54-56</a></span> (CA9 1974); <i>United States</i> v. <i>Harwood,</i> <span class="citation" data-id="307033"><a href="/opinion/307033/united-states-v-gerald-paul-harwood/#324" aria-description="Citation for case: United States v. Gerald Paul Harwood">470 F. 2d 322, 324-325</a></span> (CA10 1972).
</p>
<p>Of all the Federal Courts of Appeals, only one now apparently refrains from permitting challenges to affidavit veracity. See <i>United States</i> v. <i>Watts,</i> 176 U. S. App. D. C. 314, 317-318 n. 5, <span class="citation" data-id="338659"><a href="/opinion/338659/united-states-v-schuessler-watts-jr/" aria-description="Citation for case: United States v. Schuessler Watts, Jr.">540 F. 2d 1093</a></span>, 1096-1097 n. 5 (1976); <i>United States</i> v. <i>Branch,</i> 178 U. S. App. D. C. 99, 102 n. 2, <span class="citation" data-id="340645"><a href="/opinion/340645/united-states-v-joseph-p-branch-united-states-of-america-v-eric-b/" aria-description="Citation for case: United States v. Joseph P. Branch, United States of...">545 F. 2d 177</a></span>, 180 n. 2 (1976).</p>
<p>[5]  Franks did not raise in his petition the issue of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> challenge to the courthouse statement given to police and the use of that statement in the warrant affidavit. The propriety of the trial court's refusal to hear testimony on that subject is therefore not before us. It also appears that Franks did not take that issue to the Supreme Court of Delaware. See Opening Brief for Appellant, No. 259, 1976 (Del. Sup. Ct.).</p>
<p>[6]  The <i><span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">Rugendorf</a></span></i> affidavit, sworn to by FBI Special Agent Moore, contained two alleged inaccuracies; a double hearsay statement that petitioner Samuel Rugendorf was the manager of Rugendorf Brothers Meat Market, and a double hearsay statement that he was associated with his brother, Leo, in the meat business. As to the second, the affidavit stated that a confidential informant told FBI Special Agent McCormick about the Rugendorf brothers' association, and McCormick told affiant Moore. As to the first, the affidavit stated that the information was given by Chicago Police Officer Kelleher to Special Agent McCormick, who in turn relayed it to affiant Moore. Kelleher testified that he did not so inform McCormick, but the petitioner in <i><span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">Rugendorf</a></span></i> had failed to pursue the discrepancy: He did not seek a deposition from McCormick, who was in the hospital at the time of trial, and did not seek a postponement to enable McCormick to be present. <span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">376 U. S., at 533</a></span> n. 4. In characterizing the affidavit in <i><span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">Rugendorf</a></span></i> as raising no question of integrity, the Court took as its premise that police could not insulate one officer's deliberate misstatement merely by relaying it through an officer-affiant personally ignorant of its falsity.</p>
<p>[7]  Mascolo, Impeaching the Credibility of Affidavits for Search Warrants: Piercing the Presumption of Validity, 44 Conn. Bar J. 9, 19, 25-28 (1970); Kipperman, Inaccurate Search Warrant Affidavits as a Ground for Suppressing Evidence, <span class="citation no-link">84 Harv. L. Rev. 825</span>, 830-832 (1971); Grano, A Dilemma for Defense Counsel; Spinelli-Harris Search Warrants and the Possibility of Police Perjury, 1971 U. Ill. Law Forum 405, 456; Forkosh, The Constitutional Right to Challenge the Content of Affidavits in Warrants Issued Under the Fourth Amendment, 34 Ohio St. L. J. 297, 306, 308, 340 (1973); Sevilla, The Exclusionary Rule and Police Perjury, <span class="citation no-link">11 San Diego L. Rev. 839</span>, 869 (1974); Herman, Warrants for Arrest or Search: Impeaching the Allegations of a Facially Sufficient Affidavit, 36 Ohio St. L. J. 721, 738-739, 750 (1975); Note, 15 Buffalo L. Rev. 712, 716-717 (1966); Note, 51 Cornell L. Q. 822, 825-826 (1966); Note, 34 Ford. L. Rev. 740, 745 (1966); Note, <span class="citation no-link">67 Colum. L. Rev. 1529</span>, 1530-1531 (1967); Comment, <span class="citation no-link">19 UCLA L. Rev. 96</span>, 108, 146 (1971); Comment, 63 J. Crim. L., C. &amp; P. S. 41, 48, 50 (1972); Note, <span class="citation no-link">23 Drake L. Rev. 623</span>, 638-639 (1974); Comment, <span class="citation no-link">7 Seton Hall L. Rev. 827</span>, 859-860 (1976).</p>
<p>[8]  Petitioner conceded that if what is left is sufficient to sustain probable cause, the inaccuracies are irrelevant. Tr. of Oral Arg. 3, 13. Petitioner also conceded that if the warrant affiant had no reason to believe the information was false, there was no violation of the Fourth Amendment. <span class="citation no-link"><i>Id.,</i> at 16-17</span>.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Frazier v. Cupp.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Frazier v. Cupp"
type: case
citation: "394 U.S. 731 (1969)"
parallel_cite: "89 S. Ct. 1420; 22 L. Ed. 2d 684"
neutral_cite: 1969 U.S. LEXIS 1870
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1969
date_decided: 1969-04-23
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1969-04-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Frazier v. Cupp
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107913/frazier-v-cupp/"
  cluster_id: 107913
  opinion_id: 107913
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
related: ["[[Colorado v. Connelly]]", "[[Brown v. Mississippi]]", "[[Schneckloth v. Bustamonte]]"]
aliases: []
tags: ["case", "confessions", "voluntariness", "police-deception", "due-process", "totality"]
holding: "Police misrepresentation (falsely telling a suspect his codefendant had confessed) did not render the confession involuntary; deception…"
lake:
  record_id: Frazier v. Cupp
  status: under_review
  projected_at: 2026-07-06
---

# Frazier v. Cupp

*394 U.S. 731 (1969)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Martin Frazier was questioned about a murder. During the interrogation an officer falsely told him that his cousin and companion, Jerry Lee Rawls, had already confessed and implicated him. After receiving partial warnings of his rights, Frazier then made an incriminating statement. He later argued the confession was involuntary because it had been induced by the officer's deception.

## Issue
Whether a confession is rendered involuntary, and thus inadmissible, because the police obtained it by falsely telling the suspect that an accomplice had already confessed.

## Rule
No. Police deception is one relevant factor, but it does not by itself make an otherwise voluntary confession inadmissible; voluntariness is judged on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]. "The fact that the police misrepresented the statements that Rawls had made is, while relevant, insufficient in our view to make this otherwise voluntary confession inadmissible. These cases must be decided by viewing the 'totality of the circumstances' . . . ." — 394 U.S. at 739. ^pin-739

## Application
Frazier received partial warnings of his rights before confessing, the questioning was of short duration, and he was a mature individual of normal intelligence. Against that backdrop the officer's misrepresentation that Rawls had confessed — though relevant — was not enough to overbear his will, so on the totality of these circumstances the confession was voluntary and properly admitted.

## Conclusion
The confession was voluntary despite the police misrepresentation; the conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Frazier* remains the leading authority that interrogation deception is only one factor in the totality-of-the-circumstances voluntariness inquiry — consistent with the later rule of [[Colorado v. Connelly]] that involuntariness requires coercive police conduct.

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*

## Sources
- *Frazier v. Cupp*, 394 U.S. 731 (1969) — https://www.courtlistener.com/opinion/107913/frazier-v-cupp/ — pinpoint: 739.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ea2b4b530b4168fa", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Frazier v. Cupp"}, "payload": {"all": [{"cite": "394 U.S. 731", "page": "731", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "394"}, {"cite": "89 S. Ct. 1420", "page": "1420", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "89"}, {"cite": "22 L. Ed. 2d 684", "page": "684", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "22"}, {"cite": "1969 U.S. LEXIS 1870", "page": "1870", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1969"}], "display": "394 U.S. 731", "official": {"cite": "394 U.S. 731", "page": "731", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "394"}, "official_selection_present": true, "record_id": "Frazier v. Cupp"}}
{"assertion_id": "ee8dfda25c1f606f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-739", "record_id": "Frazier v. Cupp"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-739", "pinpoint_status": "slip-only", "quote": "--- # Frazier v. Cupp *394 U.S. 731 (1969)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Martin Frazier was questioned about a murder. During the interrogation an officer falsely told him that his cousin and companion, Jerry Lee Rawls, had already confessed and implicated him. After receiving partial warnings of his rights, Frazier then made an incriminating statement. He later argued the confession was involuntary because it had been induced by the officer's deception. ## Issue Whether a confession is rendered involuntary, and thus inadmissible, because the police obtained it by falsely telling the suspect that an accomplice had already confessed. ## Rule No. Police deception is one relevant factor, but it does not by itself make an otherwise voluntary confession inadmissible; voluntariness is judged on the totality of the circumstances.", "quote_fidelity": "mismatch", "record_id": "Frazier v. Cupp", "star_marker": null}}
{"assertion_id": "6aa66411694a7f94", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Frazier v. Cupp"}, "payload": {"as_of_content": "1969-04-22", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Frazier v. Cupp", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Frazier v. Cupp

```json
{
  "schema_version": "s2.v1",
  "record_id": "Frazier v. Cupp",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Frazier v. Cupp",
    "case_name_short": "Frazier",
    "case_name_full": "Frazier v. Cupp, Warden",
    "input_case_name": "Frazier v. Cupp",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1969-04-23",
    "year": 1969,
    "docket": null,
    "cluster_id": 107913,
    "lead_opinion_id": 107913,
    "sibling_ids": [
      107913
    ],
    "absolute_url": "/opinion/107913/frazier-v-cupp/",
    "identity_method": "pending",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "394 U.S. 731",
      "volume": "394",
      "reporter": "U.S.",
      "page": "731",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "89 S. Ct. 1420",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "1420",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 L. Ed. 2d 684",
        "volume": "22",
        "reporter": "L. Ed. 2d",
        "page": "684",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1969 U.S. LEXIS 1870",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "1870",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "394 U.S. 731",
        "volume": "394",
        "reporter": "U.S.",
        "page": "731",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 S. Ct. 1420",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "1420",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 L. Ed. 2d 684",
        "volume": "22",
        "reporter": "L. Ed. 2d",
        "page": "684",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1969 U.S. LEXIS 1870",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "1870",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "394 U.S. 731",
    "official_selection": {
      "court_class": "scotus",
      "selected": "394 U.S. 731",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-739",
      "page": null,
      "quote": "--- # Frazier v. Cupp *394 U.S. 731 (1969)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Martin Frazier was questioned about a murder. During the interrogation an officer falsely told him that his cousin and companion, Jerry Lee Rawls, had already confessed and implicated him. After receiving partial warnings of his rights, Frazier then made an incriminating statement. He later argued the confession was involuntary because it had been induced by the officer's deception. ## Issue Whether a confession is rendered involuntary, and thus inadmissible, because the police obtained it by falsely telling the suspect that an accomplice had already confessed. ## Rule No. Police deception is one relevant factor, but it does not by itself make an otherwise voluntary confession inadmissible; voluntariness is judged on the totality of the circumstances.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1969-04-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Frazier v. Cupp",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Flores Ramos",
          "cluster_id": 10160768,
          "cite": [
            "367 Or. 292",
            "478 P.3d 515"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Vasquez-Santiago",
          "cluster_id": 10133179,
          "cite": [
            "301 Or. App. 90",
            "456 P.3d 270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Larry Whitfield",
          "cluster_id": 2968731,
          "cite": [
            "695 F.3d 288",
            "2012 U.S. App. LEXIS 17762",
            "2012 WL 3591038"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hughes",
          "cluster_id": 214334,
          "cite": [
            "640 F.3d 428",
            "2011 U.S. App. LEXIS 7338",
            "2011 WL 1332061"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Burnette",
          "cluster_id": 2519721,
          "cite": [
            "535 F. Supp. 2d 772",
            "2007 WL 4911523"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane1_negative"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "North Carolina v. Butler",
          "cluster_id": 110065,
          "cite": [
            "60 L. Ed. 2d 286",
            "99 S. Ct. 1755",
            "441 U.S. 369",
            "1979 U.S. LEXIS 91"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sharp v. State",
          "cluster_id": 2458281,
          "cite": [
            "707 S.W.2d 611",
            "1986 Tex. Crim. App. LEXIS 1225"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Tucker",
          "cluster_id": 109063,
          "cite": [
            "41 L. Ed. 2d 182",
            "94 S. Ct. 2357",
            "417 U.S. 433",
            "1974 U.S. LEXIS 71"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Green v. State",
          "cluster_id": 1657475,
          "cite": [
            "934 S.W.2d 92",
            "1996 Tex. Crim. App. LEXIS 185",
            "1996 WL 512395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beckwith v. United States",
          "cluster_id": 109430,
          "cite": [
            "48 L. Ed. 2d 1",
            "96 S. Ct. 1612",
            "425 U.S. 341",
            "1976 U.S. LEXIS 147",
            "37 A.F.T.R.2d (RIA) 1232"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Perkins",
          "cluster_id": 112452,
          "cite": [
            "110 L. Ed. 2d 243",
            "110 S. Ct. 2394",
            "496 U.S. 292",
            "1990 U.S. LEXIS 2885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
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
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tennessee v. Street",
          "cluster_id": 111424,
          "cite": [
            "85 L. Ed. 2d 425",
            "105 S. Ct. 2078",
            "471 U.S. 409",
            "1985 U.S. LEXIS 9",
            "53 U.S.L.W. 4527",
            "17 Fed. R. Serv. 817"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moore v. Illinois",
          "cluster_id": 109757,
          "cite": [
            "54 L. Ed. 2d 424",
            "98 S. Ct. 458",
            "434 U.S. 220",
            "1977 U.S. LEXIS 163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Frazier v. Cupp:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107913) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDgwMjU5MjAwMDAwJnM9MjIyNDg4MiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107913%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 6,
        "triage_snippet_classified": 194
      },
      "lane2_top_cited": {
        "query": "cites:(107913)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMzUmcz0xNTUwODA2JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107913%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107913)",
        "reviewed": 22,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 22,
        "triage_read": 0,
        "triage_snippet_classified": 22
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107913)",
    "indexed_citing_opinions": 940,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107913,
        "count": 940,
        "count_source": "search"
      }
    ],
    "citation_count": 1469,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/frazier-v-cupp.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc5MDYxNTImcz03ODYxNzE4JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107913%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107913,
        "cited_id": 103352,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107419,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107684,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 107848,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 278627,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107913,
        "cited_id": 1296618,
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
    "date_created": "2026-07-05T04:55:46Z",
    "date_modified": "2026-07-06T07:48:51Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T04:55:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T04:55:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:01:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T04:55:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Frazier v. Cupp

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b806-12">
  Mr. Justice Marshall
 </author>
<p id="AKM">
  delivered the opinion of the Court.
 </p>
<p id="b806-13">
  Petitioner was convicted in an Oregon state court of second-degree murder in connection with the September 22, 1964, slaying of one Russell Anton Marleau. After the Supreme Court of Oregon had affirmed his conviction, <span class="citation" data-id="1296618"><a href="/opinion/1296618/state-v-frazier/" aria-description="Citation for case: State v. Frazier">245 Ore. 4</a></span>, <span class="citation" data-id="1296618"><a href="/opinion/1296618/state-v-frazier/" aria-description="Citation for case: State v. Frazier">418 P. 2d 841</a></span> (1966), petitioner filed a petition for a writ of habeas corpus in the United States District Court for the District of Oregon. The District Court granted the writ, but the Court of Appeals for the Ninth Circuit reversed, <span class="citation" data-id="278627"><a href="/opinion/278627/clarence-t-gladden-warden-v-martin-rene-frazier/" aria-description="Citation for case: Clarence T. Gladden, Warden v. Martin Rene Frazier">388 F. 2d 777</a></span> (1968). We
  <span citation-index="1" class="star-pagination" label="733"> 
   *733
   </span>
  granted certiorari to consider three contentions of error raised by petitioner. <span class="citation multiple-matches"><a href="/c/U.%20S./393/821/">393 U. S. 821</a></span> (1968). Although petitioner’s case has been ably briefed and argued by appointed counsel, we find none of these allegations sufficient to warrant reversal.
 </p>
<p id="b807-5">
  I.
 </p>
<p id="b807-6">
  Petitioner’s first argument centers on certain allegedly prejudicial remarks made during the prosecutor’s opening statement. Petitioner had been indicted jointly with his cousin, Jerry Lee Rawls, who pleaded guilty to the same offense. Prior to petitioner’s trial, petitioner’s defense counsel told the prosecutor that Rawls would invoke his privilege against self-incrimination if he were called to the stand; defense counsel warned the prosecutor not to rely in his opening statement upon Rawls’ expected testimony. The prosecutor replied that he would act on the basis of “all of the information I have concerning [Rawls’] testimony.” Before trial, he consulted with a police officer who had spoken to Rawls and with Rawls’ probation officer; each indicated his belief that Rawls would testify. Similar information came, through a sheriff’s report, from some of Rawls’ close relatives. Because of these reports, the prosecutor concluded that Rawls would testify if asked to do so. The court below felt that the prosecutor also relied on the fact that Rawls had pleaded guilty and was awaiting sentence. This would give him reason, the court felt, to cooperate with the prosecutor.
 </p>
<p id="b807-7">
  In any case, after the trial began the prosecutor included in his opening statement a summary of the testimony he expected to receive from Rawls. The summary was not emphasized in any particular way; it took only a few minutes to recite and was sandwiched between a summary of petitioner’s own confession and a description of the circumstantial evidence the State would introduce.
 </p>
<p id="b808-5">
<span citation-index="1" class="star-pagination" label="734"> 
   *734
   </span>
  At one point the prosecutor referred to a paper he was holding in his hands to refresh his memory about something Rawls had said. Although the State admitted in argument here that the jury might fairly have believed that the prosecutor was referring to Rawls’ statement, he did not explicitly tell the jury that this paper was Rawls’ confession, nor did he purport to read directly from it. A motion for a mistrial was made at the close of the opening statement, but it was denied. Later, the prosecutor called Rawls to the stand. Rawls informed the court that he intended to assert his privilege against self-incrimination in regard to every question concerning his activities on the morning of September 22,1964. The matter was not further pursued, and Rawls was dismissed from the stand. His appearance could not have lasted more than two or three minutes. The motion for mistrial was renewed and once again denied.
 </p>
<p id="b808-6">
  Petitioner argues that this series of events placed the substance of Rawls’ statement before the jury in a way that “may well have been the equivalent in the jury’s mind of testimony,”
  <em>
   Douglas
  </em>
  v.
  <em>
   Alabama,
  </em>
  <span class="citation" data-id="9422992"><a href="/opinion/107015/douglas-v-alabama/#419" aria-description="Citation for case: Douglas v. Alabama">380 U. S. 415, 419</a></span> (1965), and that, as in
  <em>
   Bruton
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/#128" aria-description="Citation for case: Bruton v. United States">391 U. S. 123, 128</a></span> (1968), the statement “added substantial, perhaps even critical, weight to the Government’s case in a form not subject to cross-examination . . . .” In this way, petitioner claims he was denied his constitutional right of confrontation, guaranteed by the Sixth and Fourteenth Amendments to the Constitution. See
  <em>
   Pointer
  </em>
  v.
  <em>
   Texas,
  </em>
  <span class="citation" data-id="9422988"><a href="/opinion/107014/pointer-v-texas/" aria-description="Citation for case: Pointer v. Texas">380 U. S. 400</a></span> (1965). Although the judge did caution the jurors that they “must not regard any statement made by counsel in your presence during the proceedings concerning the facts of this case as evidence,” petitioner contends that
  <em>
   Bruton
  </em>
  v.
  <em>
   United <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">States, supra,</a></span>
  </em>
  disposes of the contention that limiting instructions of this sort can be relied upon to cure the error which occurred. Although the question thus posed is not an
  <span citation-index="1" class="star-pagination" label="735"> 
   *735
   </span>
  easy one, we cannot agree with petitioner’s conclusion.
 </p>
<p id="b809-4">
  First of all, it is clear that this case is quite different from either
  <em>
   <span class="citation" data-id="9422992"><a href="/opinion/107015/douglas-v-alabama/" aria-description="Citation for case: Douglas v. Alabama">Douglas</a></span>
  </em>
  or
  <em>
   <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span>.
  </em>
  In
  <em>
   <span class="citation" data-id="9422992"><a href="/opinion/107015/douglas-v-alabama/" aria-description="Citation for case: Douglas v. Alabama">Douglas</a></span>,
  </em>
  the prosecutor called the defendant’s coconspirator to the stand and read his alleged confession to him; the coconspirator was required to assert his privilege against self-incrimination repeatedly as the prosecutor asked him to confirm or deny each statement. The Court found that this procedure placed powerfully incriminating evidence before the jury in a manner which effectively denied the right of cross-examination. Here, Rawls was on the stand for a very short time and only a paraphrase of the statement was placed before the jury. This was done not during the trial, while the person making the statement was on the stand, but in an opening statement. In addition, the jury was told that the opening statement should not be considered as evidence. Certainly the impact of the procedure used here was much less damaging than was the case in
  <em>
   <span class="citation" data-id="9422992"><a href="/opinion/107015/douglas-v-alabama/" aria-description="Citation for case: Douglas v. Alabama">Douglas</a></span>.
  </em>
  And unlike the situation in
  <em>
   <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span>,
  </em>
  the jury was not being asked to perform the mental gymnastics of considering an incriminating statement against only one of two defendants in a joint trial. Moreover, unlike the situation in either
  <em>
   <span class="citation" data-id="9422992"><a href="/opinion/107015/douglas-v-alabama/" aria-description="Citation for case: Douglas v. Alabama">Douglas</a></span>
  </em>
  or
  <em>
   <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span>,
  </em>
  Rawls’ statement was not a vitally important part of the prosecution’s case.
 </p>
<p id="b809-5">
  We believe that in these circumstances the limiting instructions given were sufficient to protect petitioner’s constitutional rights.
  <a class="footnote" href="#fn*" id="fn*_ref">
   *
  </a>
  As the Court said in
  <em>
   Bruton,
  </em>
  <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/#135" aria-description="Citation for case: Bruton v. United States">391 U. S., at 135</a></span>, “Not every admission of inadmissible hearsay or other evidence can be considered to be reversible error unavoidable through limiting instructions; instances occur in almost every trial where inadmissible evidence creeps in, usually inadvertently.” See
  <em>
   Hopt
  </em>
  v.
  <em>
   Utah,
  </em>
  120
  <span citation-index="1" class="star-pagination" label="736"> 
   *736
   </span>
  U. S. 430, 438 (1887). It may be that some remarks included in an opening or closing statement could be so prejudicial that a finding of error, or even constitutional error, would be unavoidable. But here we have no more than an objective summary of evidence which the prosecutor reasonably expected to produce. Many things might happen during the course of the trial which would prevent the presentation of all the evidence described in advance. Certainly not every variance between the advance description and the actual presentation constitutes reversible error, when a proper limiting instruction has been given. Even if it is unreasonable to assume that a jury can disregard a coconspirator’s statement when introduced against one of two joint defendants, it does not seem at all remarkable to assume that the jury will ordinarily be able to limit its consideration to the evidence introduced during the trial. At least where the anticipated, and unproduced, evidence is not touted to the jury as a crucial part of the prosecution’s case, “it is hard for us to imagine that the minds of the jurors would be so influenced by such incidental statements during this long trial that they would not appraise the evidence objectively and dispassionately.”
  <em>
   United States
  </em>
  v.
  <em>
   Socony-Vacuum Oil Co.,
  </em>
  <span class="citation" data-id="9419105"><a href="/opinion/103352/united-states-v-socony-vacuum-oil-co/#239" aria-description="Citation for case: United States v. Socony-Vacuum Oil Co.">310 U. S. 150, 239</a></span> (1940).
 </p>
<p id="b810-5">
  The Court of Appeals seemed to feel that this aspect of the case turned on whether or not the prosecutor acted “in a good faith expectation that Rawls would testify.” <span class="citation" data-id="278627"><a href="/opinion/278627/clarence-t-gladden-warden-v-martin-rene-frazier/#780" aria-description="Citation for case: Clarence T. Gladden, Warden v. Martin Rene Frazier">388 F. 2d, at 780-781</a></span>. While we do not believe that the prosecutor’s good faith, or lack of it, is controlling in determining whether a defendant has been deprived of the right of confrontation guaranteed by the Sixth and Fourteenth Amendments, we agree with the Court of Appeals’ factual determination in this case. The evidence presented in the record is sufficient to support the Oregon Supreme Court’s conclusion that “the state could reasonably expect [Rawls] to testify in line with his
  <span citation-index="1" class="star-pagination" label="737"> 
   *737
   </span>
  previous statements.” <span class="citation" data-id="1296618"><a href="/opinion/1296618/state-v-frazier/#9" aria-description="Citation for case: State v. Frazier">245 Ore., at 9</a></span>, <span class="citation" data-id="1296618"><a href="/opinion/1296618/state-v-frazier/#843" aria-description="Citation for case: State v. Frazier">418 P. 2d, at 843</a></span>, Accordingly, there is no need to decide whether the type of prosecutorial misconduct alleged to have occurred would have been sufficient to constitute reversible constitutional error. Cf.
  <em>
   Miller
  </em>
  v.
  <em>
   Pate,
  </em>
  <span class="citation" data-id="107354"><a href="/opinion/107354/miller-v-pate/" aria-description="Citation for case: Miller v. Pate">386 U. S. 1</a></span> (1967). Therefore, because we find neither prosecutorial misconduct nor a deprivation of the right of confrontation, we agree with the Court of Appeals that nothing which occurred during the prosecution’s opening statement would warrant federal habeas relief.
 </p>
<p id="b811-5">
  II.
 </p>
<p id="b811-6">
  Petitioner’s second argument concerns the admission into evidence of his own confession. The circumstances under which the confession was obtained can be summarized briefly. Petitioner was arrested about 4:15 p. m. on September 24, 1964. He was taken to headquarters where questioning began at about 5 p. m. The interrogation, which was tape-recorded, ended slightly more than an hour later, and by 6:45 p. m. petitioner had signed a written version of his confession.
 </p>
<p id="b811-7">
  After the questioning had begun and after a few routine facts were ascertained, petitioner was questioned briefly about the location of his Marine uniform. He was next asked where he was on the night in question. Although he admitted that he was with his cousin Rawls, he denied being with any third person. Then petitioner was given a somewhat abbreviated description of his constitutional rights. He was told that he could have an attorney if he wanted one and that anything he said could be used against him at trial. Questioning thereafter became somewhat more vigorous, but petitioner continued to deny being with anyone but Rawls. At this point, the officer questioning petitioner told him, falsely, that Rawls had been brought in and that he had confessed. Petitioner still was reluctant to talk, but
  <span citation-index="1" class="star-pagination" label="738"> 
   *738
   </span>
  after the officer sympathetically suggested that the victim had started a fight by making homosexual advances, petitioner began to spill out his story. Shortly after he began he again showed signs of reluctance and said, “I think I had better get a lawyer before I talk any more. I am going to get into trouble more than I am in now.” The officer replied simply, “You can’t be in any more trouble than you are in now,” and the questioning session proceeded. A full confession was obtained and, after further warnings, a written version was signed.
 </p>
<p id="b812-5">
  Since petitioner was tried after this Court’s decision in
  <em>
   Escobedo
  </em>
  v.
  <em>
   Illinois,
  </em>
  <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964), but before the decision in
  <em>
   Miranda
  </em>
  v.
  <em>
   Arizona,
  </em>
  <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), only the rule of the former case is directly applicable.
  <em>
   Johnson
  </em>
  v.
  <em>
   New Jersey,
  </em>
  <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719</a></span> (1966). Petitioner argues that his statement about getting a lawyer was sufficient to bring
  <em>
   <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>
  </em>
  into play and that the police should immediately have stopped the questioning and obtained counsel for him. We might agree were
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  applicable to this case, for in
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  this Court held that “[i]f . . . [a suspect] indicates in any manner and at any stage of the process that he wishes to consult with an attorney before speaking there can be no questioning.” 384 U. S., at 444-445. But
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  does not apply to this case. This Court in
  <em>
   Johnson
  </em>
  v.
  <em>
   <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">New Jersey</a></span>
  </em>
  pointedly rejected the contention that the specific commands of
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  should apply to all
  <em>
   post-Escobedo
  </em>
  cases. The Court recognized “[t]he disagreements among other courts concerning the implications of
  <em>
   Escobedo,” Johnson
  </em>
  v.
  <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#734" aria-description="Citation for case: Johnson v. New Jersey"><em>
   New Jersey, supra,
  </em>
  at 734</a></span>, and concluded that the States, although free to apply
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  to
  <em>
   post-Escobedo
  </em>
  cases,
  <em>
   id.,
  </em>
  at 733, were not required to do so. The Oregon Supreme Court, in affirming petitioner’s conviction, concluded that the confession was properly introduced into evidence. Under
  <em>
   <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">Johnson</a></span>,
  </em>
  we would be
  <span citation-index="1" class="star-pagination" label="739"> 
   *739
   </span>
  free to disagree with this conclusion only if we felt compelled to do so by the specific holding of
  <em>
   <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>.
  </em>
</p>
<p id="b813-5">
  We do not believe that
  <em>
   <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>
  </em>
  covers this case. Petitioner's statement about seeing an attorney was neither as clear nor as unambiguous as the request Escobedo made. The police in
  <em>
   <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>
  </em>
  were unmistakably informed of their suspect’s wishes; in fact Escobedo’s attorney was present and repeatedly requested permission to see his client. Here, on the other hand, it is possible that the questioning officer took petitioner’s remark not as a request that the interrogation cease but merely as a passing comment. Petitioner did not pursue the matter, but continued answering questions. In this context, we cannot find the denial of the right to counsel which was found so crucial in
  <em>
   <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>.
  </em>
</p>
<p id="b813-6">
  Petitioner also presses the alternative argument that his confession was involuntary and that it should have been excluded for that reason. The trial judge, after an evidentiary hearing during which the tape recording was played, could not agree with this contention, and our reading of the record does not lead us to a contrary conclusion. Before petitioner made any incriminating statements, he received partial warnings of his constitutional rights; this is, of course, a circumstance quite relevant to a finding of voluntariness.
  <em>
   Davis
  </em>
  v.
  <em>
   North Carolina,
  </em>
  <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#740" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737, 740-741</a></span> (1966). The questioning was of short duration, and petitioner was a mature individual of normal intelligence. The fact that the police misrepresented the statements that Rawls had made is, while relevant, insufficient in our view to make this otherwise voluntary confession inadmissible. These cases must be decided by viewing the “totality of the circumstances,” see,
  <em>
   e. g., Clewis
  </em>
  v.
  <em>
   Texas,
  </em>
  <span class="citation" data-id="107419"><a href="/opinion/107419/clewis-v-texas/#708" aria-description="Citation for case: Clewis v. Texas">386 U. S. 707, 708</a></span> (1967), and on the facts of this case we can find no error in the admission of petitioner’s confession.
 </p>
<p id="b814-4">
<span citation-index="1" class="star-pagination" label="740"> 
   *740
   </span>
  III.
 </p>
<p id="b814-5">
  Petitioner’s final contention can be dismissed rather quickly. He argues that the trial judge erred in permitting some clothing seized from petitioner’s duffel bag to be introduced into evidence. This duffel bag was being used jointly by petitioner and his cousin Rawls and it had been left in Rawls’ home. The police, while arresting Rawls, asked him if they could have his clothing. They were directed to the duffel bag and both Rawls and his mother consented to its search. During this search, the officers came upon petitioner’s clothing and it was seized as well. Since Rawls was a joint user of the bag, he clearly had authority to consent to its search. The officers therefore found evidence against petitioner while in the course of an otherwise lawful search. Under this Court’s past decisions, they were clearly permitted to seize it.
  <em>
   Harris
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">390 U. S. 234</a></span>
  <em>
   (1968); Warden
  </em>
  v.
  <em>
   Hayden,
  </em>
  <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967). Petitioner argues that Rawls only had actual permission to use one compartment of the bag and that he had no authority to consent to a search of the other compartments. We will not, however, engage in such metaphysical subtleties in judging the efficacy of Rawls’ consent. Petitioner, in allowing Rawls to use the bag and in leaving it in his house, must be taken to have assumed the risk that Rawls would allow someone else to look inside. We find no valid search and seizure claim in this case.
 </p>
<p id="b814-6">
  Because we find none of petitioner’s contentions meritorious, we affirm the judgment of the Court of Appeals.
 </p>
<p id="b814-7">
<em>
   Affirmed.
  </em>
</p>
<judges id="b814-8">
  Mr. Chief Justice Warren and Mr. Justice Douglas concur in the result.
 </judges>
<judges id="b814-9">
  Mr. Justice Fortas took no part in the consideration or decision of this case.
 </judges>

<div class="footnotes"><div class="footnote" id="fn*" label="*">
<a class="footnote" href="#fn*_ref">
   *
  </a>
<p id="b809-6">
   A more specific limiting instruction might have been desirable, but none was requested.
  </p>
</div></div></opinion>
```

---
