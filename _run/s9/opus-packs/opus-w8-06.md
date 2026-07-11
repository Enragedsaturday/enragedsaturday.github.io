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

## GROUP: _overhaul2/lake/cases/Navarette v. California.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Navarette v. California"
type: case
citation: ""
parallel_cite: "134 S. Ct. 1683; 188 L. Ed. 2d 680; 82 U.S.L.W. 4282; 572 U.S. 393; 24 Fla. L. Weekly Fed. S 690"
neutral_cite: "2014 U.S. LEXIS 2930; 2014 WL 1577513"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2014
date_decided: 2014-04-22
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2014-04-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Navarette v. California
  varies_by_point: false
  scope_note: Good law on anonymous-tip reliability for reasonable suspicion.
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2670795/prado-navarette-v-california/"
  cluster_id: 2670795
  opinion_id: 2670795
  identity_checked: true
homes:
  - page: "[[Reasonable Suspicion]]"
    role: "Key — Progeny / Refinement"
related: ["[[Alabama v. White]]", "[[Florida v. J.L.]]", "[[Illinois v. Gates]]", "[[Terry v. Ohio]]"]
aliases: ["Prado Navarette v. California"]
tags: ["case", "fourth-amendment", "reasonable-suspicion", "anonymous-tip", "traffic-stop"]
holding: "A 911 call reporting dangerous/reckless driving can supply reasonable suspicion for a stop when it bears adequate indicia of reliability…"
lake:
  record_id: Navarette v. California
  status: verified
  projected_at: 2026-07-06
---

# Navarette v. California

*572 U.S. 393 (2014)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A 911 caller reported that a specific silver Ford pickup truck had just run her off the road, giving the truck's license plate and location. Officers located the truck and stopped it without independently observing any traffic violation; as they approached they smelled marijuana and found 30 pounds of it. The occupants moved to suppress, arguing the anonymous tip did not supply reasonable suspicion.

## Issue
Whether an anonymous 911 tip reporting dangerous driving can supply reasonable suspicion for an investigatory traffic stop.

## Rule
Under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], an anonymous tip may supply reasonable suspicion when it bears adequate indicia of reliability. Here, "we conclude that the call bore adequate indicia of reliability for the officer to credit the caller's account." — 572 U.S. at 398. ^pin-398

The Court found the 911 call reliable because the caller claimed eyewitness knowledge of dangerous driving, reported it contemporaneously, and used the 911 system, which has features that allow tracing callers and deter false reports.

## Application
The caller's report that the truck had run her off the road described conduct supporting reasonable suspicion of drunk driving; the caller's eyewitness basis of knowledge, near-contemporaneous report, and use of the 911 system gave the tip sufficient reliability. The officers were therefore justified in stopping the identified truck even though they had not personally witnessed erratic driving.

## Conclusion
The traffic stop complied with the Fourth Amendment; the judgment was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Navarette* applies the anonymous-tip framework of [[Alabama v. White]] and distinguishes [[Florida v. J.L.]], holding that a contemporaneous, eyewitness 911 report of dangerous driving can carry enough indicia of reliability to justify a stop.

## Appears on
- [[Reasonable Suspicion]] — *Key — Progeny / Refinement*

## Sources
- *Navarette v. California*, 572 U.S. 393 (2014) — https://www.courtlistener.com/opinion/2670795/prado-navarette-v-california/ — pinpoint: 398.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6e60844ade715358", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Navarette v. California"}, "payload": {"all": [{"cite": "134 S. Ct. 1683", "page": "1683", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "134"}, {"cite": "188 L. Ed. 2d 680", "page": "680", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "188"}, {"cite": "2014 U.S. LEXIS 2930", "page": "2930", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2014"}, {"cite": "82 U.S.L.W. 4282", "page": "4282", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "82"}, {"cite": "572 U.S. 393", "page": "393", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "572"}, {"cite": "24 Fla. L. Weekly Fed. S 690", "page": "690", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "24"}, {"cite": "2014 WL 1577513", "page": "1577513", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2014"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Navarette v. California"}}
{"assertion_id": "a95e39ded4debff0", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-398", "record_id": "Navarette v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-398", "pinpoint_status": "slip-only", "quote": "--- # Navarette v. California *572 U.S. 393 (2014)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A 911 caller reported that a specific silver Ford pickup truck had just run her off the road, giving the truck's license plate and location. Officers located the truck and stopped it without independently observing any traffic violation; as they approached they smelled marijuana and found 30 pounds of it. The occupants moved to suppress, arguing the anonymous tip did not supply reasonable suspicion. ## Issue Whether an anonymous 911 tip reporting dangerous driving can supply reasonable suspicion for an investigatory traffic stop. ## Rule Under the totality of the circumstances, an anonymous tip may supply reasonable suspicion when it bears adequate indicia of reliability. Here,", "quote_fidelity": "mismatch", "record_id": "Navarette v. California", "star_marker": null}}
{"assertion_id": "336dfcfd176dd938", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Navarette v. California"}, "payload": {"as_of_content": "2014-04-22", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Navarette v. California", "scope_note": "Good law on anonymous-tip reliability for reasonable suspicion.", "varies_by_point": false}}
```

### lake record — Navarette v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Navarette v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Prado Navarette v. California",
    "case_name_short": "Navarette",
    "case_name_full": "Lorenzo Prado NAVARETTE and Jos\u00e9 Prado Navarette, Petitioners, v. CALIFORNIA.",
    "input_case_name": "Navarette v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2014-04-22",
    "year": 2014,
    "docket": null,
    "cluster_id": 2670795,
    "lead_opinion_id": 2670795,
    "sibling_ids": [
      2670795
    ],
    "absolute_url": "/opinion/2670795/prado-navarette-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8414100,
        "score": 20,
        "case_name": "Navarette v. California"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "134 S. Ct. 1683",
        "volume": "134",
        "reporter": "S. Ct.",
        "page": "1683",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "188 L. Ed. 2d 680",
        "volume": "188",
        "reporter": "L. Ed. 2d",
        "page": "680",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 U.S.L.W. 4282",
        "volume": "82",
        "reporter": "U.S.L.W.",
        "page": "4282",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "572 U.S. 393",
        "volume": "572",
        "reporter": "U.S.",
        "page": "393",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 690",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "690",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2014 U.S. LEXIS 2930",
        "volume": "2014",
        "reporter": "U.S. LEXIS",
        "page": "2930",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 1577513",
        "volume": "2014",
        "reporter": "WL",
        "page": "1577513",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "134 S. Ct. 1683",
        "volume": "134",
        "reporter": "S. Ct.",
        "page": "1683",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "188 L. Ed. 2d 680",
        "volume": "188",
        "reporter": "L. Ed. 2d",
        "page": "680",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 U.S. LEXIS 2930",
        "volume": "2014",
        "reporter": "U.S. LEXIS",
        "page": "2930",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 U.S.L.W. 4282",
        "volume": "82",
        "reporter": "U.S.L.W.",
        "page": "4282",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "572 U.S. 393",
        "volume": "572",
        "reporter": "U.S.",
        "page": "393",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 690",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "690",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 1577513",
        "volume": "2014",
        "reporter": "WL",
        "page": "1577513",
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
      "id": "pin-398",
      "page": null,
      "quote": "--- # Navarette v. California *572 U.S. 393 (2014)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A 911 caller reported that a specific silver Ford pickup truck had just run her off the road, giving the truck's license plate and location. Officers located the truck and stopped it without independently observing any traffic violation; as they approached they smelled marijuana and found 30 pounds of it. The occupants moved to suppress, arguing the anonymous tip did not supply reasonable suspicion. ## Issue Whether an anonymous 911 tip reporting dangerous driving can supply reasonable suspicion for an investigatory traffic stop. ## Rule Under the totality of the circumstances, an anonymous tip may supply reasonable suspicion when it bears adequate indicia of reliability. Here,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2014-04-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Navarette v. California",
    "varies_by_point": false,
    "scope_note": "Good law on anonymous-tip reliability for reasonable suspicion.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Castillo-Martinez",
          "cluster_id": 9489871,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "The State of Texas v. Martin Eduardo Velasquezreyes",
          "cluster_id": 9481403,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane1_negative"
      },
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
        "journal_ref": "Navarette v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Reed",
          "cluster_id": 4731165,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kevin Gamble (071234)",
          "cluster_id": 2686119,
          "cite": [
            "218 N.J. 412",
            "95 A.3d 188",
            "2014 WL 3858497",
            "2014 N.J. LEXIS 801"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Erickson Meko Campbell",
          "cluster_id": 6357475,
          "cite": [
            "26 F.4th 860"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Beal, Jr. v. James Beller",
          "cluster_id": 4348069,
          "cite": [
            "847 F.3d 897",
            "2017 WL 544599",
            "2017 U.S. App. LEXIS 2439"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeff Courtright v. City of Battle Creek",
          "cluster_id": 4312445,
          "cite": [
            "839 F.3d 513",
            "2016 FED App. 0256P",
            "2016 U.S. App. LEXIS 18502",
            "2016 WL 5956725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
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
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Barbeau",
          "cluster_id": 4543099,
          "cite": [
            "301 Neb. 293",
            "917 N.W.2d 913"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Halley v. Huckaby",
          "cluster_id": 4530346,
          "cite": [
            "902 F.3d 1136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matthews, Cornelious L.",
          "cluster_id": 2949477,
          "cite": [
            "431 S.W.3d 596",
            "2014 WL 3029070",
            "2014 Tex. Crim. App. LEXIS 820"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Linda Brooks v. Avancez",
          "cluster_id": 6621840,
          "cite": [
            "39 F.4th 424"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Silveria and Travis",
          "cluster_id": 4774990,
          "cite": [
            "267 Cal. Rptr. 3d 303",
            "471 P.3d 412",
            "10 Cal. 5th 195"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Scottize Danyelle Brown",
          "cluster_id": 4635121,
          "cite": [
            "930 N.W.2d 840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sloley v. VanBramer",
          "cluster_id": 4686314,
          "cite": [
            "945 F.3d 30"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ezekiel Gardner",
          "cluster_id": 3204635,
          "cite": [
            "823 F.3d 793",
            "2016 U.S. App. LEXIS 9066",
            "2016 WL 2893881"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Brown",
          "cluster_id": 2824888,
          "cite": [
            "61 Cal. 4th 968",
            "353 P.3d 305",
            "190 Cal. Rptr. 3d 583",
            "2015 Cal. LEXIS 5404"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Carter",
          "cluster_id": 2756719,
          "cite": [
            "105 A.3d 765",
            "2014 Pa. Super. 265",
            "2014 Pa. Super. LEXIS 4539",
            "2014 WL 6756271"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mason v. Commonwealth",
          "cluster_id": 3200832,
          "cite": [
            "786 S.E.2d 148",
            "291 Va. 362",
            "2016 WL 2586178",
            "2016 Va. LEXIS 59"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gaytan",
          "cluster_id": 2812404,
          "cite": [
            "2015 IL 116223"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
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
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ernest D. Shields",
          "cluster_id": 2808513,
          "cite": [
            "789 F.3d 733",
            "2015 U.S. App. LEXIS 10058",
            "2015 WL 3654318"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hawkins (Slip Opinion)",
          "cluster_id": 4669773,
          "cite": [
            "2019 Ohio 4210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Correll Thomas v. C. Dillard",
          "cluster_id": 3191530,
          "cite": [
            "818 F.3d 864",
            "2016 U.S. App. LEXIS 6210",
            "2016 WL 1319765"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Warren Green, IV",
          "cluster_id": 4520277,
          "cite": [
            "897 F.3d 173"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Williams",
          "cluster_id": 3007498,
          "cite": [
            "125 A.3d 425",
            "2015 Pa. Super. 216",
            "2015 Pa. Super. LEXIS 581",
            "2015 WL 5810631"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Patrick I. Hogan",
          "cluster_id": 2816261,
          "cite": [
            "364 Wis. 2d 167",
            "2015 WI 76",
            "868 N.W.2d 124",
            "2015 Wisc. LEXIS 348"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hernandez",
          "cluster_id": 4347480,
          "cite": [
            "847 F.3d 1257",
            "2017 WL 526028",
            "2017 U.S. App. LEXIS 2324"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Navarette v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2670795) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTU0MTYzMjAwMDAwJnM9NDYwMzU4MCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%282670795%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 4,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 4,
        "triage_snippet_classified": 196
      },
      "lane2_top_cited": {
        "query": "cites:(2670795)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNyZzPTMxMzMzMjUmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%282670795%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2670795)",
        "reviewed": 116,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 116,
        "triage_read": 2,
        "triage_snippet_classified": 114
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2670795)",
    "indexed_citing_opinions": 442,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2670795,
        "count": 442,
        "count_source": "search"
      }
    ],
    "citation_count": 1112,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/navarette-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNjI2NDImcz0xMDM1NzU4NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%282670795%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2670795,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 112239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 112454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 117921,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 118352,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 118474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 776340,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 1990652,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 2089507,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 2575791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2670795,
        "cited_id": 2629186,
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
    "date_created": "2026-07-05T15:09:29Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:09:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:09:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:14:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:09:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Navarette v. California

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

         PRADO NAVARETTE ET AL. v. CALIFORNIA

    CERTIORARI TO THE COURT OF APPEAL OF CALIFORNIA,

                FIRST APPELLATE DISTRICT


    No. 12–9490. Argued January 21, 2014—Decided April 22, 2014
A California Highway Patrol officer stopped the pickup truck occupied
  by petitioners because it matched the description of a vehicle that a
  911 caller had recently reported as having run her off the road. As he
  and a second officer approached the truck, they smelled marijuana.
  They searched the truck’s bed, found 30 pounds of marijuana, and ar-
  rested petitioners. Petitioners moved to suppress the evidence, argu-
  ing that the traffic stop violated the Fourth Amendment. Their mo-
  tion was denied, and they pleaded guilty to transporting marijuana.
  The California Court of Appeal affirmed, concluding that the officer
  had reasonable suspicion to conduct an investigative stop.
Held: The traffic stop complied with the Fourth Amendment because,
 under the totality of the circumstances, the officer had reasonable
 suspicion that the truck’s driver was intoxicated. Pp. 3–11.
    (a) The Fourth Amendment permits brief investigative stops when
 an officer has “a particularized and objective basis for suspecting the
 particular person stopped of . . . criminal activity.” United States v.
 Cortez, 449 U. S. 411, 417–418. Reasonable suspicion takes into ac-
 count “the totality of the circumstances,” id., at 417, and depends
 “upon both the content of information possessed by police and its de-
 gree of reliability,” Alabama v. White, 496 U. S. 325, 330. An anony-
 mous tip alone seldom demonstrates sufficient reliability, White, 496
 U. S., at 329, but may do so under appropriate circumstances, id., at
 327. Pp. 3–5.
    (b) The 911 call in this case bore adequate indicia of reliability for
 the officer to credit the caller’s account. By reporting that she had
 been run off the road by a specific vehicle, the caller necessarily
 claimed an eyewitness basis of knowledge. The apparently short
 time between the reported incident and the 911 call suggests that the
2                 PRADO NAVARETTE v. CALIFORNIA

                                  Syllabus

    caller had little time to fabricate the report. And a reasonable officer
    could conclude that a false tipster would think twice before using the
    911 system, which has several technological and regulatory features
    that safeguard against making false reports with immunity. Pp. 5–8.
      (c) Not only was the tip here reliable, but it also created reasonable
    suspicion of drunk driving. Running another car off the road sug-
    gests the sort of impairment that characterizes drunk driving. While
    that conduct might be explained by another cause such as driver dis-
    traction, reasonable suspicion “need not rule out the possibility of in-
    nocent conduct.” United States v. Arvizu, 534 U. S. 266, 277. Finally,
    the officer’s failure to observe additional suspicious conduct during
    the short period that he followed the truck did not dispel the reason-
    able suspicion of drunk driving, and the officer was not required to
    surveil the truck for a longer period. Pp. 8–10.
Affirmed.

   THOMAS, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and KENNEDY, BREYER, and ALITO, JJ., joined. SCALIA, J., filed a
dissenting opinion, in which GINSBURG, SOTOMAYOR, and KAGAN, JJ.,
joined.
                        Cite as: 572 U. S. ____ (2014)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash­
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 12–9490
                                   _________________


  LORENZO PRADO NAVARETTE AND JOSE PRADO 

    NAVARETTE, PETITIONERS v. CALIFORNIA 

   ON WRIT OF CERTIORARI TO THE COURT OF APPEAL OF 

        CALIFORNIA, FIRST APPELLATE DISTRICT

                                 [April 22, 2014]

  JUSTICE THOMAS delivered the opinion of the Court.
  After a 911 caller reported that a vehicle had run her off
the road, a police officer located the vehicle she identified
during the call and executed a traffic stop. We hold that
the stop complied with the Fourth Amendment because,
under the totality of the circumstances, the officer had
reasonable suspicion that the driver was intoxicated.
                             I
   On August 23, 2008, a Mendocino County 911 dispatch
team for the California Highway Patrol (CHP) received a
call from another CHP dispatcher in neighboring Hum­
boldt County. The Humboldt County dispatcher relayed a
tip from a 911 caller, which the Mendocino County team
recorded as follows: “ ‘Showing southbound Highway 1 at
mile marker 88, Silver Ford 150 pickup. Plate of 8-David­
94925. Ran the reporting party off the roadway and was
last seen approximately five [minutes] ago.’ ” App. 36a.
The Mendocino County team then broadcast that infor­
mation to CHP officers at 3:47 p.m.
   A CHP officer heading northbound toward the reported
vehicle responded to the broadcast. At 4:00 p.m., the
2               PRADO NAVARETTE v. CALIFORNIA

                         Opinion of the Court

officer passed the truck near mile marker 69. At about
4:05 p.m., after making a U-turn, he pulled the truck over.
A second officer, who had separately responded to the
broadcast, also arrived on the scene. As the two officers
approached the truck, they smelled marijuana. A search
of the truck bed revealed 30 pounds of marijuana. The
officers arrested the driver, petitioner Lorenzo Prado
Navarette, and the passenger, petitioner José Prado
Navarette.
  Petitioners moved to suppress the evidence, arguing
that the traffic stop violated the Fourth Amendment
because the officer lacked reasonable suspicion of criminal
activity. Both the magistrate who presided over the sup­
pression hearing and the Superior Court disagreed.1
Petitioners pleaded guilty to transporting marijuana and
were sentenced to 90 days in jail plus three years of
probation.
  The California Court of Appeal affirmed, concluding
that the officer had reasonable suspicion to conduct an
investigative stop. 2012 WL 4842651 (Oct. 12, 2012). The
court reasoned that the content of the tip indicated that it
came from an eyewitness victim of reckless driving, and
that the officer’s corroboration of the truck’s description,
location, and direction established that the tip was reliable
enough to justify a traffic stop. Id., at *7. Finally, the
court concluded that the caller reported driving that was
sufficiently dangerous to merit an investigative stop with­
out waiting for the officer to observe additional reckless
driving himself. Id., at *9. The California Supreme Court
——————
   1 At the suppression hearing, counsel for petitioners did not dispute

that the reporting party identified herself by name in the 911 call
recording. Because neither the caller nor the Humboldt County dis­
patcher who received the call was present at the hearing, however, the
prosecution did not introduce the recording into evidence. The prosecu­
tion proceeded to treat the tip as anonymous, and the lower courts
followed suit. See 2012 WL 4842651, *6 (Cal. Ct. App., Oct. 12, 2012).
                  Cite as: 572 U. S. ____ (2014)            3

                      Opinion of the Court

denied review. We granted certiorari, 570 U. S. ___
(2013), and now affirm.
                             II
  The Fourth Amendment permits brief investigative
stops—such as the traffic stop in this case—when a law
enforcement officer has “a particularized and objective
basis for suspecting the particular person stopped of crim­
inal activity.” United States v. Cortez, 449 U. S. 411, 417–
418 (1981); see also Terry v. Ohio, 392 U. S. 1, 21–22
(1968). The “reasonable suspicion” necessary to justify
such a stop “is dependent upon both the content of infor­
mation possessed by police and its degree of reliability.”
Alabama v. White, 496 U. S. 325, 330 (1990). The stand­
ard takes into account “the totality of the circumstances—
the whole picture.” Cortez, supra, at 417. Although a
mere “ ‘hunch’ ” does not create reasonable suspicion,
Terry, supra, at 27, the level of suspicion the standard
requires is “considerably less than proof of wrongdoing by
a preponderance of the evidence,” and “obviously less”
than is necessary for probable cause, United States v.
Sokolow, 490 U. S. 1, 7 (1989).
                              A
   These principles apply with full force to investigative
stops based on information from anonymous tips. We
have firmly rejected the argument “that reasonable cause
for a[n investigative stop] can only be based on the officer’s
personal observation, rather than on information supplied
by another person.” Adams v. Williams, 407 U. S. 143,
147 (1972). Of course, “an anonymous tip alone seldom
demonstrates the informant’s basis of knowledge or verac­
ity.” White, 496 U. S., at 329 (emphasis added). That is
because “ordinary citizens generally do not provide exten­
sive recitations of the basis of their everyday observa­
tions,” and an anonymous tipster’s veracity is “ ‘by hypoth­
4            PRADO NAVARETTE v. CALIFORNIA

                     Opinion of the Court

esis largely unknown, and unknowable.’ ” Ibid. But under
appropriate circumstances, an anonymous tip can demon­
strate “sufficient indicia of reliability to provide reasona­
ble suspicion to make [an] investigatory stop.” Id., at 327.
   Our decisions in Alabama v. White, 496 U. S. 325 (1990),
and Florida v. J. L., 529 U. S. 266 (2000), are useful
guides. In White, an anonymous tipster told the police
that a woman would drive from a particular apartment
building to a particular motel in a brown Plymouth station
wagon with a broken right tail light. The tipster further
asserted that the woman would be transporting cocaine.
496 U. S., at 327. After confirming the innocent details,
officers stopped the station wagon as it neared the motel
and found cocaine in the vehicle. Id., at 331. We held that
the officers’ corroboration of certain details made the
anonymous tip sufficiently reliable to create reasonable
suspicion of criminal activity. By accurately predicting
future behavior, the tipster demonstrated “a special famil­
iarity with respondent’s affairs,” which in turn implied
that the tipster had “access to reliable information about
that individual’s illegal activities.” Id., at 332. We also
recognized that an informant who is proved to tell the
truth about some things is more likely to tell the truth
about other things, “including the claim that the object of
the tip is engaged in criminal activity.” Id., at 331 (citing
Illinois v. Gates, 462 U. S. 213, 244 (1983)).
   In J. L., by contrast, we determined that no reasonable
suspicion arose from a bare-bones tip that a young black
male in a plaid shirt standing at a bus stop was carrying a
gun. 529 U. S., at 268. The tipster did not explain how he
knew about the gun, nor did he suggest that he had any
special familiarity with the young man’s affairs. Id., at
271. As a result, police had no basis for believing “that the
tipster ha[d] knowledge of concealed criminal activity.”
Id., at 272. Furthermore, the tip included no predictions
of future behavior that could be corroborated to assess the
                  Cite as: 572 U. S. ____ (2014)            5

                      Opinion of the Court

tipster’s credibility. Id., at 271. We accordingly concluded
that the tip was insufficiently reliable to justify a stop and
frisk.
                                B
   The initial question in this case is whether the 911 call
was sufficiently reliable to credit the allegation that peti­
tioners’ truck “ran the [caller] off the roadway.” Even
assuming for present purposes that the 911 call was anon­
ymous, see n. 1, supra, we conclude that the call bore
adequate indicia of reliability for the officer to credit the
caller’s account. The officer was therefore justified in
proceeding from the premise that the truck had, in fact,
caused the caller’s car to be dangerously diverted from the
highway.
   By reporting that she had been run off the road by a
specific vehicle—a silver Ford F-150 pickup, license plate
8D94925—the caller necessarily claimed eyewitness
knowledge of the alleged dangerous driving. That basis of
knowledge lends significant support to the tip’s reliability.
See Gates, supra, at 234 (“[An informant’s] explicit and
detailed description of alleged wrongdoing, along with a
statement that the event was observed firsthand, entitles
his tip to greater weight than might otherwise be the
case”); Spinelli v. United States, 393 U. S. 410, 416 (1969)
(a tip of illegal gambling is less reliable when “it is not
alleged that the informant personally observed [the de­
fendant] at work or that he had ever placed a bet with
him”). This is in contrast to J. L., where the tip provided
no basis for concluding that the tipster had actually seen
the gun. 529 U. S., at 271. Even in White, where we
upheld the stop, there was scant evidence that the tipster
had actually observed cocaine in the station wagon. We
called White a “ ‘close case’ ” because “[k]nowledge about a
person’s future movements indicates some familiarity with
that person’s affairs, but having such knowledge does not
6            PRADO NAVARETTE v. CALIFORNIA

                     Opinion of the Court

necessarily imply that the informant knows, in particular,
whether that person is carrying hidden contraband.” 529
U. S., at 271. A driver’s claim that another vehicle ran her
off the road, however, necessarily implies that the inform­
ant knows the other car was driven dangerously.
   There is also reason to think that the 911 caller in this
case was telling the truth. Police confirmed the truck’s
location near mile marker 69 (roughly 19 highway miles
south of the location reported in the 911 call) at 4:00 p.m.
(roughly 18 minutes after the 911 call). That timeline of
events suggests that the caller reported the incident soon
after she was run off the road. That sort of contemporane­
ous report has long been treated as especially reliable. In
evidence law, we generally credit the proposition that
statements about an event and made soon after perceiving
that event are especially trustworthy because “substantial
contemporaneity of event and statement negate the likeli­
hood of deliberate or conscious misrepresentation.” Advi­
sory Committee’s Notes on Fed. Rule Evid. 803(1), 28
U. S. C. App., p. 371 (describing the rationale for the
hearsay exception for “present sense impression[s]”). A
similar rationale applies to a “statement relating to a
startling event”—such as getting run off the road—“made
while the declarant was under the stress of excitement
that it caused.” Fed. Rule Evid. 803(2) (hearsay exception
for “excited utterances”). Unsurprisingly, 911 calls that
would otherwise be inadmissible hearsay have often been
admitted on those grounds. See D. Binder, Hearsay
Handbook §8.1, pp. 257–259 (4th ed. 2013–2014) (citing
cases admitting 911 calls as present sense impressions);
id., §9.1, at 274–275 (911 calls admitted as excited utter­
ances). There was no indication that the tip in J. L. (or
even in White) was contemporaneous with the observation
of criminal activity or made under the stress of excitement
caused by a startling event, but those considerations
weigh in favor of the caller’s veracity here.
                 Cite as: 572 U. S. ____ (2014)            7

                     Opinion of the Court

  Another indicator of veracity is the caller’s use of the
911 emergency system. See Brief for Respondent 40–41,
44; Brief for United States as Amicus Curiae 16–18. A 911
call has some features that allow for identifying and trac­
ing callers, and thus provide some safeguards against
making false reports with immunity. See J. L., supra, at
276 (KENNEDY, J., concurring). As this case illustrates,
see n. 1, supra, 911 calls can be recorded, which provides
victims with an opportunity to identify the false tipster’s
voice and subject him to prosecution, see, e.g., Cal. Penal
Code Ann. §653x (West 2010) (makes “telephon[ing] the
911 emergency line with the intent to annoy or harass”
punishable by imprisonment and fine); see also §148.3
(2014 West Cum. Supp.) (prohibits falsely reporting “that
an ‘emergency’ exists”); §148.5 (prohibits falsely reporting
“that a felony or misdemeanor has been committed”). The
911 system also permits law enforcement to verify im­
portant information about the caller. In 1998, the Federal
Communications Commission (FCC) began to require
cellular carriers to relay the caller’s phone number to 911
dispatchers. 47 CFR §20.18(d)(1) (2013) (FCC’s “Phase I
enhanced 911 services” requirements). Beginning in 2001,
carriers have been required to identify the caller’s geo­
graphic location with increasing specificity. §§20.18(e)–(h)
(“Phase II enhanced 911 service” requirements). And
although callers may ordinarily block call recipients from
obtaining their identifying information, FCC regulations
exempt 911 calls from that privilege.           §§64.1601(b),
(d)(4)(ii) (“911 emergency services” exemption from rule
that, when a caller so requests, “a carrier may not reveal
that caller’s number or name”). None of this is to suggest
that tips in 911 calls are per se reliable. Given the forego­
ing technological and regulatory developments, however, a
reasonable officer could conclude that a false tipster would
think twice before using such a system. The caller’s use of
the 911 system is therefore one of the relevant circum­
8               PRADO NAVARETTE v. CALIFORNIA

                          Opinion of the Court

stances that, taken together, justified the officer’s reliance
on the information reported in the 911 call.
                               C
   Even a reliable tip will justify an investigative stop only
if it creates reasonable suspicion that “criminal activity
may be afoot.” Terry, 392 U. S., at 30. We must therefore
determine whether the 911 caller’s report of being run off
the roadway created reasonable suspicion of an ongoing
crime such as drunk driving as opposed to an isolated
episode of past recklessness. See Cortez, 449 U. S., at 417
(“An investigatory stop must be justified by some objective
manifestation that the person stopped is, or is about to be,
engaged in criminal activity”). We conclude that the
behavior alleged by the 911 caller, “viewed from the
standpoint of an objectively reasonable police officer,
amount[s] to reasonable suspicion” of drunk driving.
Ornelas v. United States, 517 U. S. 690, 696 (1996). The
stop was therefore proper.2
   Reasonable suspicion depends on “ ‘ “the factual and
practical considerations of everyday life on which reason-
able and prudent men, not legal technicians, act.” ’ ” Id., at
695. Under that commonsense approach, we can appro­
priately recognize certain driving behaviors as sound
indicia of drunk driving. See, e.g., People v. Wells,
38 Cal. 4th 1078, 1081, 136 P. 3d 810, 811 (2006) (“ ‘weav­
ing all over the roadway’ ”); State v. Prendergast, 103 Haw.
451, 452–453, 83 P. 3d 714, 715–716 (2004) (“cross[ing]
over the center line” on a highway and “almost caus[ing]
several head-on collisions”); State v. Golotta, 178 N. J.
205, 209, 837 A. 2d 359, 361 (2003) (driving “ ‘all over
the road’ ” and “ ‘weaving back and forth’ ”); State v.
——————
    2 Becausewe conclude that the 911 call created reasonable suspicion
of an ongoing crime, we need not address under what circumstances a
stop is justified by the need to investigate completed criminal activity.
Cf. United States v. Hensley, 469 U. S. 221, 229 (1985).
                 Cite as: 572 U. S. ____ (2014)           9

                     Opinion of the Court

Walshire, 634 N. W. 2d 625, 626 (Iowa 2001) (“driving in
the median”). Indeed, the accumulated experience of
thousands of officers suggests that these sorts of erratic
behaviors are strongly correlated with drunk driving.
See Nat. Highway Traffic Safety Admin., The Visual
Detection of DWI Motorists 4–5 (Mar. 2010), online at
http://nhtsa.gov/staticfiles/nti/pdf/808677.pdf (as visited
Apr. 18, 2014, and available in Clerk of Court’s case file).
Of course, not all traffic infractions imply intoxication.
Unconfirmed reports of driving without a seatbelt or
slightly over the speed limit, for example, are so tenuously
connected to drunk driving that a stop on those grounds
alone would be constitutionally suspect. But a reliable tip
alleging the dangerous behaviors discussed above gener-
ally would justify a traffic stop on suspicion of drunk
driving.
   The 911 caller in this case reported more than a minor
traffic infraction and more than a conclusory allegation of
drunk or reckless driving. Instead, she alleged a specific
and dangerous result of the driver’s conduct: running
another car off the highway. That conduct bears too great
a resemblance to paradigmatic manifestations of drunk
driving to be dismissed as an isolated example of reckless­
ness. Running another vehicle off the road suggests lane­
positioning problems, decreased vigilance, impaired judg­
ment, or some combination of those recognized drunk
driving cues. See Visual Detection of DWI Motorists 4–5.
And the experience of many officers suggests that a driver
who almost strikes a vehicle or another object—the exact
scenario that ordinarily causes “running [another vehicle]
off the roadway”—is likely intoxicated. See id., at 5, 8.
As a result, we cannot say that the officer acted unreason­
ably under these circumstances in stopping a driver
whose alleged conduct was a significant indicator of drunk
driving.
   Petitioners’ attempts to second-guess the officer’s rea­
10           PRADO NAVARETTE v. CALIFORNIA

                      Opinion of the Court

sonable suspicion of drunk driving are unavailing. It is
true that the reported behavior might also be explained
by, for example, a driver responding to “an unruly child or
other distraction.” Brief for Petitioners 21. But we have
consistently recognized that reasonable suspicion “need
not rule out the possibility of innocent conduct.” United
States v. Arvizu, 534 U. S. 266, 277 (2002).
   Nor did the absence of additional suspicious conduct,
after the vehicle was first spotted by an officer, dispel the
reasonable suspicion of drunk driving. Brief for Petition­
ers 23–24. It is hardly surprising that the appearance of a
marked police car would inspire more careful driving for a
time. Cf. Arvizu, supra, at 275 (“ ‘[s]lowing down after
spotting a law enforcement vehicle’ ” does not dispel rea­
sonable suspicion of criminal activity). Extended observa­
tion of an allegedly drunk driver might eventually dispel a
reasonable suspicion of intoxication, but the 5-minute
period in this case hardly sufficed in that regard. Of
course, an officer who already has such a reasonable sus­
picion need not surveil a vehicle at length in order to
personally observe suspicious driving. See Adams v.
Williams, 407 U. S., at 147 (repudiating the argument
that “reasonable cause for a[n investigative stop] can only
be based on the officer’s personal observation”). Once
reasonable suspicion of drunk driving arises, “[t]he rea­
sonableness of the officer’s decision to stop a suspect does
not turn on the availability of less intrusive investigatory
techniques.” Sokolow, 490 U. S., at 11. This would be a
particularly inappropriate context to depart from that
settled rule, because allowing a drunk driver a second
chance for dangerous conduct could have disastrous
consequences.
                              III
  Like White, this is a “close case.” 496 U. S., at 332. As
in that case, the indicia of the 911 caller’s reliability here
                  Cite as: 572 U. S. ____ (2014)            11

                      Opinion of the Court

are stronger than those in J. L., where we held that a
bare-bones tip was unreliable. 529 U. S., at 271. Alt­
hough the indicia present here are different from those we
found sufficient in White, there is more than one way to
demonstrate “a particularized and objective basis for
suspecting the particular person stopped of criminal activ­
ity.” Cortez, 449 U. S., at 417–418. Under the totality of
the circumstances, we find the indicia of reliability in this
case sufficient to provide the officer with reasonable suspi­
cion that the driver of the reported vehicle had run another
vehicle off the road. That made it reasonable under the
circumstances for the officer to execute a traffic stop. We
accordingly affirm.
                                              It is so ordered.
                 Cite as: 572 U. S. ____ (2014)            1

                     SCALIA, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 12–9490
                         _________________


  LORENZO PRADO NAVARETTE AND JOSE PRADO 

    NAVARETTE, PETITIONERS v. CALIFORNIA 

   ON WRIT OF CERTIORARI TO THE COURT OF APPEAL OF 

        CALIFORNIA, FIRST APPELLATE DISTRICT

                        [April 22, 2014]

   JUSTICE SCALIA, with whom JUSTICE GINSBURG,
JUSTICE SOTOMAYOR, and JUSTICE KAGAN join, dissenting.
   The California Court of Appeal in this case relied on
jurisprudence from the California Supreme Court (adopted
as well by other courts) to the effect that “an anonymous
and uncorroborated tip regarding a possibly intoxicated
highway driver” provides without more the reasonable
suspicion necessary to justify a stop. People v. Wells, 38
Cal. 4th l078, 1082, 136 P. 3d 810, 812, (2006). See also,
e.g., United States v. Wheat, 278 F. 3d 722, 729–730 (CA8
2001); State v. Walshire, 634 N. W. 2d 625, 626–627, 630
(Iowa 2001). Today’s opinion does not explicitly adopt
such a departure from our normal Fourth Amendment
requirement that anonymous tips must be corroborated; it
purports to adhere to our prior cases, such as Florida v.
J. L., 529 U. S. 266 (2000), and Alabama v. White, 496
U. S. 325 (1990). Be not deceived.
   Law enforcement agencies follow closely our judgments
on matters such as this, and they will identify at once our
new rule: So long as the caller identifies where the car is,
anonymous claims of a single instance of possibly careless
or reckless driving, called in to 911, will support a traffic
stop. This is not my concept, and I am sure would not be
the Framers’, of a people secure from unreasonable
searches and seizures. I would reverse the judgment of
2              PRADO NAVARETTE v. CALIFORNIA

                        SCALIA, J., dissenting

the Court of Appeal of California.
                                    I
    The California Highway Patrol in this case knew noth­
ing about the tipster on whose word—and that alone—
they seized Lorenzo and José Prado Navarette. They did
not know her name.1 They did not know her phone num­
ber or address. They did not even know where she called
from (she may have dialed in from a neighboring county,
App. 33a–34a).
    The tipster said the truck had “[run her] off the road­
way,” id., at 36a, but the police had no reason to credit
that charge and many reasons to doubt it, beginning with
the peculiar fact that the accusation was anonymous.
“[E]liminating accountability . . . is ordinarily the very
purpose of anonymity.”              McIntyre v. Ohio Elections
Comm’n, 514 U. S. 334, 385 (1995) (SCALIA, J., dissenting).
The unnamed tipster “can lie with impunity,” J. L., supra,
at 275 (KENNEDY, J., concurring). Anonymity is especially
suspicious with respect to the call that is the subject of the
present case. When does a victim complain to the police
about an arguably criminal act (running the victim off the
road) without giving his identity, so that he can accuse
and testify when the culprit is caught?
    The question before us, the Court agrees, ante, at 8, is
whether the “content of information possessed by police
and its degree of reliability,” White, 496 U. S., at 330, gave
the officers reasonable suspicion that the driver of the
truck (Lorenzo) was committing an ongoing crime. When
the only source of the government’s information is an
informant’s tip, we ask whether the tip bears sufficient
“ ‘indicia of reliability,’ ” id., at 328, to establish “a particu­
larized and objective basis for suspecting the particular
——————
  1 There was some indication below that the tipster was a woman. See

App. 18a. Beyond that detail, we must, as the Court notes, ante, at 2,
n. 1, assume that the identity of the tipster was unknown.
                 Cite as: 572 U. S. ____ (2014)            3

                     SCALIA, J., dissenting

person stopped of criminal activity,” United States v.
Cortez, 449 U. S. 411, 417–418 (1981).
   The most extreme case, before this one, in which an
anonymous tip was found to meet this standard was
White, supra. There the reliability of the tip was estab­
lished by the fact that it predicted the target’s behavior in
the finest detail—a detail that could be known only by
someone familiar with the target’s business: She would,
the tipster said, leave a particular apartment building, get
into a brown Plymouth station wagon with a broken right
tail light, and drive immediately to a particular motel.
Id., at 327. Very few persons would have such intimate
knowledge, and hence knowledge of the unobservable fact
that the woman was carrying unlawful drugs was plausi­
ble. Id., at 332. Here the Court makes a big deal of the
fact that the tipster was dead right about the fact that a
silver Ford F-150 truck (license plate 8D94925) was trav­
eling south on Highway 1 somewhere near mile marker
88. But everyone in the world who saw the car would have
that knowledge, and anyone who wanted the car stopped
would have to provide that information. Unlike the situa­
tion in White, that generally available knowledge in no
way makes it plausible that the tipster saw the car run
someone off the road.
   The Court says, ante, at 5, that “[b]y reporting that she
had been run off the road by a specific vehicle . . . the
caller necessarily claimed eyewitness knowledge.” So
what? The issue is not how she claimed to know, but
whether what she claimed to know was true. The claim to
“eyewitness knowledge” of being run off the road supports
not at all its veracity; nor does the amazing, mystifying
prediction (so far short of what existed in White) that the
petitioners’ truck would be heading south on Highway 1.
   The Court finds “reason to think” that the informant
“was telling the truth” in the fact that police observation
confirmed that the truck had been driving near the spot at
4             PRADO NAVARETTE v. CALIFORNIA

                      SCALIA, J., dissenting

which, and at the approximate time at which, the tipster
alleged she had been run off the road. Ante, at 6. Accord­
ing to the Court, the statement therefore qualifies as a
“ ‘present sense impression’ ” or “ ‘excited utterance,’ ” kinds
of hearsay that the law deems categorically admissible
given their low likelihood of reflecting “ ‘deliberate or
conscious misrepresentation.’ ” Ibid. (quoting Advisory
Committee’s Notes on Fed. Rule Evid. 803(1), 28 U. S. C.
App., p. 371). So, the Court says, we can fairly suppose
that the accusation was true.
   No, we cannot. To begin with, it is questionable whether
either the “present sense impression” or the “excited ut­
terance” exception to the hearsay rule applies here. The
classic “present sense impression” is the recounting of an
event that is occurring before the declarant’s eyes, as the
declarant is speaking (“I am watching the Hindenburg
explode!”). See 2 K. Broun, McCormick on Evidence 362
(7th ed. 2013) (hereinafter McCormick). And the classic
“excited utterance” is a statement elicited, almost involun­
tarily, by the shock of what the declarant is immediately
witnessing (“My God, those people will be killed!”). See
id., at 368–369. It is the immediacy that gives the state­
ment some credibility; the declarant has not had time to
dissemble or embellish. There is no such immediacy here.
The declarant had time to observe the license number of
the offending vehicle, 8D94925 (a difficult task if she was
forced off the road and the vehicle was speeding away), to
bring her car to a halt, to copy down the observed license
number (presumably), and (if she was using her own cell
phone) to dial a call to the police from the stopped car.
Plenty of time to dissemble or embellish.
   Moreover, even assuming that less than true immediacy
will suffice for these hearsay exceptions to apply, the
tipster’s statement would run into additional barriers to
admissibility and acceptance. According to the very Advi­
sory Committee’s Notes from which the Court quotes,
                 Cite as: 572 U. S. ____ (2014)            5

                     SCALIA, J., dissenting

cases addressing an unidentified declarant’s present sense
impression “indicate hesitancy in upholding the statement
alone as sufficient” proof of the reported event. 28 U. S. C.
App., at 371; see also 7 M. Graham, Handbook of Federal
Evidence 19–20 (7th ed. 2012). For excited utterances as
well, the “knotty theoretical” question of statement-alone
admissibility persists—seemingly even when the declarant
is known. 2 McCormick 368. “Some courts . . . have taken
the position that an excited utterance is admissible only if
other proof is presented which supports a finding of fact
that the exciting event did occur. The issue has not yet
been resolved under the Federal Rules.” Id., at 367–368
(footnote omitted). It is even unsettled whether excited
utterances of an unknown declarant are ever admissible.
A leading treatise reports that “the courts have been
reluctant to admit such statements, principally because of
uncertainty that foundational requirements, including the
impact of the event on the declarant, have been satisfied.”
Id., at 372. In sum, it is unlikely that the law of evidence
would deem the mystery caller in this case “especially
trustworthy,” ante, at 6.
   Finally, and least tenably, the Court says that another
“indicator of veracity” is the anonymous tipster’s mere
“use of the 911 emergency system,” ante, at 7. Because,
you see, recent “technological and regulatory develop­
ments” suggest that the identities of unnamed 911 callers
are increasingly less likely to remain unknown. Ibid.
Indeed, the systems are able to identify “the caller’s geo­
graphic location with increasing specificity.” Ibid. Amici
disagree with this, see Brief for National Association of
Criminal Defense Lawyers et al. 8–12, and the present
case surely suggests that amici are right—since we know
neither the identity of the tipster nor even the county from
which the call was made. But assuming the Court is right
about the ease of identifying 911 callers, it proves abso­
lutely nothing in the present case unless the anonymous
6               PRADO NAVARETTE v. CALIFORNIA

                          SCALIA, J., dissenting

caller was aware of that fact. “It is the tipster’s belief in
anonymity, not its reality, that will control his behavior.”
Id., at 10 (emphasis added). There is no reason to believe
that your average anonymous 911 tipster is aware that
911 callers are readily identifiable.2
                               II
   All that has been said up to now assumes that the anon­
ymous caller made, at least in effect, an accusation of
drunken driving. But in fact she did not. She said that
the petitioners’ truck “ ‘[r]an [me] off the roadway.’ ” App.
36a. That neither asserts that the driver was drunk nor
even raises the likelihood that the driver was drunk. The
most it conveys is that the truck did some apparently
nontypical thing that forced the tipster off the roadway,
whether partly or fully, temporarily or permanently. Who
really knows what (if anything) happened? The truck
might have swerved to avoid an animal, a pothole, or a
jaywalking pedestrian.
   But let us assume the worst of the many possibilities:
that it was a careless, reckless, or even intentional ma­
neuver that forced the tipster off the road. Lorenzo might
have been distracted by his use of a hands-free cell phone,
see Strayer, Drews, & Crouch, A Comparison of the Cell
Phone Driver and the Drunk Driver, 48 Human Factors 381,
388 (2006), or distracted by an intense sports argument with
José, see D. Strayer et al., AAA Foundation for Traffic
Safety, Measuring Cognitive Distraction in the Automobile
28 (June 2013), online at https://www.aaafoundation.org/
sites/default/files/MeasuringCognitiveDistractions.pdf as visited
Apr. 17, 2014, and available in Clerk of Court’s case file).
——————
   2 The Court’s discussion of reliable 911 traceability has so little rele­

vance to the present case that one must surmise it has been included
merely to assure officers in the future that anonymous 911 accusa­
tions—even untraced ones—are not as suspect (and hence as unrelia­
ble) as other anonymous accusations. That is unfortunate.
                     Cite as: 572 U. S. ____ (2014)                    7

                         SCALIA, J., dissenting

Or, indeed, he might have intentionally forced the tipster
off the road because of some personal animus, or hostility
to her “Make Love, Not War” bumper sticker. I fail to see
how reasonable suspicion of a discrete instance of irregular
or hazardous driving generates a reasonable suspicion of
ongoing intoxicated driving. What proportion of the hun­
dreds of thousands—perhaps millions—of careless, reck­
less, or intentional traffic violations committed each day is
attributable to drunken drivers? I say 0.1 percent. I have
no basis for that except my own guesswork. But unless
the Court has some basis in reality to believe that the
proportion is many orders of magnitude above that—say 1
in 10 or at least 1 in 20—it has no grounds for its unsup­
ported assertion that the tipster’s report in this case gave
rise to a reasonable suspicion of drunken driving.
   Bear in mind that that is the only basis for the stop that
has been asserted in this litigation.3 The stop required
suspicion of an ongoing crime, not merely suspicion of
having run someone off the road earlier. And driving
while being a careless or reckless person, unlike driving
while being a drunk person, is not an ongoing crime. In
other words, in order to stop the petitioners the officers
here not only had to assume without basis the accuracy of
the anonymous accusation but also had to posit an unlikely
reason (drunkenness) for the accused behavior.
   In sum, at the moment the police spotted the truck, it
was more than merely “possib[le]” that the petitioners
were not committing an ongoing traffic crime. United
States v. Arvizu, 534 U. S. 266, 277 (2002) (emphasis
——————
  3 The circumstances that may justify a stop under Terry v. Ohio, 392

U. S. 1 (1968), to investigate past criminal activity are far from clear,
see United States v. Hensley, 469 U. S. 221, 229 (1985), and have not
been discussed in this litigation. Hence, the Court says it “need not
address” that question. Ante, at 8, n. 2. I need not either. This case
has been litigated on the assumption that only suspicion of ongoing
intoxicated or reckless driving could have supported this stop.
8            PRADO NAVARETTE v. CALIFORNIA

                     SCALIA, J., dissenting

added). It was overwhelmingly likely that they were not.
                              III
   It gets worse. Not only, it turns out, did the police have
no good reason at first to believe that Lorenzo was driving
drunk, they had very good reason at last to know that he
was not. The Court concludes that the tip, plus confirma­
tion of the truck’s location, produced reasonable suspicion
that the truck not only had been but still was barreling
dangerously and drunkenly down Highway 1. Ante, at 8–
10. In fact, alas, it was not, and the officers knew it. They
followed the truck for five minutes, presumably to see if it
was being operated recklessly. And that was good police
work. While the anonymous tip was not enough to sup­
port a stop for drunken driving under Terry v. Ohio, 392
U. S. 1 (1968), it was surely enough to counsel observation
of the truck to see if it was driven by a drunken driver.
But the pesky little detail left out of the Court’s reason-
able-suspicion equation is that, for the five minutes that the
truck was being followed (five minutes is a long time),
Lorenzo’s driving was irreproachable. Had the officers
witnessed the petitioners violate a single traffic law, they
would have had cause to stop the truck, Whren v. United
States, 517 U. S. 806, 810 (1996), and this case would not
be before us. And not only was the driving irreproachable,
but the State offers no evidence to suggest that the peti­
tioners even did anything suspicious, such as suddenly
slowing down, pulling off to the side of the road, or turning
somewhere to see whether they were being followed. Cf.
Arvizu, supra, at 270–271, 277 (concluding that an officer’s
suspicion of criminality was enhanced when the driver,
upon seeing that he was being followed, “slowed dramati­
cally,” “appeared stiff,” and “seemed to be trying to pre­
tend” that the patrol car was not there). Consequently,
the tip’s suggestion of ongoing drunken driving (if it could
be deemed to suggest that) not only went uncorroborated;
                 Cite as: 572 U. S. ____ (2014)            9

                     SCALIA, J., dissenting

it was affirmatively undermined.
   A hypothetical variation on the facts of this case illus­
trates the point. Suppose an anonymous tipster reports
that, while following near mile marker 88 a silver Ford
F-150, license plate 8D949925, traveling southbound on
Highway 1, she saw in the truck’s open cab several five­
foot-tall stacks of what was unmistakably baled cannabis.
Two minutes later, a highway patrolman spots the truck
exactly where the tip suggested it would be, begins follow­
ing it, but sees nothing in the truck’s cab. It is not enough
to say that the officer’s observation merely failed to cor­
roborate the tipster’s accusation. It is more precise to say
that the officer’s observation discredited the informant’s
accusation: The crime was supposedly occurring (and
would continue to occur) in plain view, but the police saw
nothing. Similarly, here, the crime supposedly suggested
by the tip was ongoing intoxicated driving, the hallmarks
of which are many, readily identifiable, and difficult to
conceal. That the officers witnessed nary a minor traffic
violation nor any other “sound indici[um] of drunk driv­
ing,” ante, at 8, strongly suggests that the suspected crime
was not occurring after all. The tip’s implication of con­
tinuing criminality, already weak, grew even weaker.
   Resisting this line of reasoning, the Court curiously
asserts that, since drunk drivers who see marked squad
cars in their rearview mirrors may evade detection simply
by driving “more careful[ly],” the “absence of additional
suspicious conduct” is “hardly surprising” and thus largely
irrelevant. Ante, at 10. Whether a drunk driver drives
drunkenly, the Court seems to think, is up to him. That is
not how I understand the influence of alcohol. I subscribe
to the more traditional view that the dangers of intoxi-
cated driving are the intoxicant’s impairing effects on the
body—effects that no mere act of the will can resist. See,
e.g., A. Dasgupta, The Science of Drinking: How Alcohol
Affects Your Body and Mind 39 (explaining that the physi­
10           PRADO NAVARETTE v. CALIFORNIA

                     SCALIA, J., dissenting

ological effect of a blood alcohol content between 0.08 and
0.109, for example, is “sever[e] impair[ment]” of “[b]alance,
speech, hearing, and reaction time,” as well as one’s gen­
eral “ability to drive a motor vehicle”). Consistent with
this view, I take it as a fundamental premise of our intoxi­
cated-driving laws that a driver soused enough to swerve
once can be expected to swerve again—and soon. If he
does not, and if the only evidence of his first episode of
irregular driving is a mere inference from an uncorrobo­
rated, vague, and nameless tip, then the Fourth Amend­
ment requires that he be left alone.
                         *    *     *
  The Court’s opinion serves up a freedom-destroying
cocktail consisting of two parts patent falsity: (1) that
anonymous 911 reports of traffic violations are reliable so
long as they correctly identify a car and its location, and
(2) that a single instance of careless or reckless driving
necessarily supports a reasonable suspicion of drunken­
ness. All the malevolent 911 caller need do is assert a
traffic violation, and the targeted car will be stopped,
forcibly if necessary, by the police. If the driver turns out
not to be drunk (which will almost always be the case), the
caller need fear no consequences, even if 911 knows his
identity. After all, he never alleged drunkenness, but
merely called in a traffic violation—and on that point his
word is as good as his victim’s.
  Drunken driving is a serious matter, but so is the loss of
our freedom to come and go as we please without police
interference. To prevent and detect murder we do not
allow searches without probable cause or targeted Terry
stops without reasonable suspicion. We should not do so
for drunken driving either. After today’s opinion all of us
on the road, and not just drug dealers, are at risk of hav­
ing our freedom of movement curtailed on suspicion of
drunkenness, based upon a phone tip, true or false, of a
                  Cite as: 572 U. S. ____ (2014)           11

                      SCALIA, J., dissenting

single instance of careless driving. I respectfully dissent.

```

---

## GROUP: _overhaul2/lake/cases/New Jersey v. T.L.O..json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "New Jersey v. T.L.O."
type: case
citation: "469 U.S. 325 (1985)"
parallel_cite: "105 S. Ct. 733; 83 L. Ed. 2d 720; 53 U.S.L.W. 4083"
neutral_cite: 1985 U.S. LEXIS 41
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-01-15
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-01-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: New Jersey v. T.L.O.
  varies_by_point: false
  scope_note: "Anchor for the reasonableness standard governing school searches; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111301/new-jersey-v-t-l-o/"
  cluster_id: 111301
  opinion_id: 9429812
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Anchor"
related: ["[[Vernonia School District 47J v. Acton]]", "[[Safford Unified School District v. Redding]]", "[[National Treasury Employees Union v. Von Raab]]", "[[Terry v. Ohio]]"]
aliases: ["New Jersey v. TLO"]
tags: ["case", "fourth-amendment", "school-search", "special-needs", "reasonableness"]
holding: "A school official's search of a student requires only reasonableness under all the circumstances — justified at inception + reasonably…"
lake:
  record_id: New Jersey v. T.L.O.
  status: verified
  projected_at: 2026-07-09
---

# New Jersey v. T.L.O.

*469 U.S. 325 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A teacher found a 14-year-old student, T.L.O., smoking in a school bathroom. An assistant vice principal opened her purse, found cigarettes and rolling papers, and on continued inspection found marijuana, a pipe, plastic bags, money, and a list of students who owed her money. The evidence led to juvenile-delinquency charges.

## Issue
What standard governs a search of a student by a public school official under the Fourth Amendment.

## Rule
The Fourth Amendment applies to public school officials, but a school search requires only reasonableness under all the circumstances — not a warrant or probable cause. "[T]he legality of a search of a student should depend simply on the reasonableness, under all the circumstances, of the search." — 469 U.S. at 341. ^pin-341

"Determining the reasonableness of any search involves a twofold inquiry: first, one must consider 'whether the . . . action was justified at its inception,' . . . second, one must determine whether the search as actually conducted 'was reasonably related in scope to the circumstances which justified the interference in the first place.'" — *Id.* ^pin-341b

A school search is "justified at its inception" when there are reasonable grounds to suspect it will turn up evidence the student has violated the law or school rules, and is permissible in scope when the measures are reasonably related to the search's objectives and not excessively intrusive in light of the student's age and sex and the nature of the infraction. — [*Id.* at 341–42](https://www.courtlistener.com/opinion/111301/new-jersey-v-t-l-o/#:~:text=was-,justified%20at%20its%20inception). ^pin-342

## Application
The report that T.L.O. had been smoking in the bathroom gave reasonable grounds to suspect her purse contained cigarettes, justifying the search at its inception. Discovery of the rolling papers then gave reasonable suspicion that she possessed marijuana, justifying the further inspection that uncovered the drug evidence. The search was reasonable in scope at each step on these facts.

## Conclusion
The search was reasonable; the evidence was admissible, and the New Jersey Supreme Court's suppression order was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *T.L.O.* established the reasonableness standard for school searches (and the "special needs" rationale articulated in Justice Blackmun's [[Common Legal Terms#concurring-opinion|concurrence]]), later applied to student drug testing ([[Vernonia School District 47J v. Acton]]) and to the scope of an intrusive school search ([[Safford Unified School District v. Redding]]).

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Anchor*

## Sources
- *New Jersey v. T.L.O.*, 469 U.S. 325 (1985) — https://www.courtlistener.com/opinion/111301/new-jersey-v-t-l-o/ — pinpoints: 341, 341–42.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1dcd8b0be8009901", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "New Jersey v. T.L.O."}, "payload": {"all": [{"cite": "469 U.S. 325", "page": "325", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "469"}, {"cite": "105 S. Ct. 733", "page": "733", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "105"}, {"cite": "83 L. Ed. 2d 720", "page": "720", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "83"}, {"cite": "1985 U.S. LEXIS 41", "page": "41", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1985"}, {"cite": "53 U.S.L.W. 4083", "page": "4083", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "53"}], "display": "469 U.S. 325", "official": {"cite": "469 U.S. 325", "page": "325", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "469"}, "official_selection_present": true, "record_id": "New Jersey v. T.L.O."}}
{"assertion_id": "2f7e84f5ecfb9c12", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-341b", "record_id": "New Jersey v. T.L.O."}, "payload": {"fragment": null, "page": null, "pin_id": "pin-341b", "pinpoint_status": "slip-only", "quote": "Determining the reasonableness of any search involves a twofold inquiry: first, one must consider 'whether the . . . action was justified at its inception,' . . . second, one must determine whether the search as actually conducted 'was reasonably related in scope to the circumstances which justified the interference in the first place.'", "quote_fidelity": "mismatch", "record_id": "New Jersey v. T.L.O.", "star_marker": null}}
{"assertion_id": "a938d13adeacca43", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-341", "record_id": "New Jersey v. T.L.O."}, "payload": {"fragment": null, "page": null, "pin_id": "pin-341", "pinpoint_status": "slip-only", "quote": "--- # New Jersey v. T.L.O. *469 U.S. 325 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A teacher found a 14-year-old student, T.L.O., smoking in a school bathroom. An assistant vice principal opened her purse, found cigarettes and rolling papers, and on continued inspection found marijuana, a pipe, plastic bags, money, and a list of students who owed her money. The evidence led to juvenile-delinquency charges. ## Issue What standard governs a search of a student by a public school official under the Fourth Amendment. ## Rule The Fourth Amendment applies to public school officials, but a school search requires only reasonableness under all the circumstances — not a warrant or probable cause.", "quote_fidelity": "mismatch", "record_id": "New Jersey v. T.L.O.", "star_marker": null}}
{"assertion_id": "b7689fdf21a283b2", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-342", "record_id": "New Jersey v. T.L.O."}, "payload": {"fragment": "#:~:text=was-,justified%20at%20its%20inception", "page": null, "pin_id": "pin-342", "pinpoint_status": "star-verified", "quote": "justified at its inception", "quote_fidelity": "matched", "record_id": "New Jersey v. T.L.O.", "star_marker": "341"}}
{"assertion_id": "2b9fef7159474236", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "New Jersey v. T.L.O."}, "payload": {"as_of_content": "1985-01-15", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "New Jersey v. T.L.O.", "scope_note": "Anchor for the reasonableness standard governing school searches; good law.", "varies_by_point": false}}
```

### lake record — New Jersey v. T.L.O.

```json
{
  "schema_version": "s2.v1",
  "record_id": "New Jersey v. T.L.O.",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "New Jersey v. T. L. O.",
    "case_name_short": "TLO",
    "case_name_full": "New Jersey v. T. L. O.",
    "input_case_name": "New Jersey v. T.L.O.",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-01-15",
    "year": 1985,
    "docket": null,
    "cluster_id": 111301,
    "lead_opinion_id": 9429812,
    "sibling_ids": [
      111301,
      9429812,
      9429813,
      9429814,
      9429815,
      9429816
    ],
    "absolute_url": "/opinion/111301/new-jersey-v-t-l-o/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "469 U.S. 325",
      "volume": "469",
      "reporter": "U.S.",
      "page": "325",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 733",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "733",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 L. Ed. 2d 720",
        "volume": "83",
        "reporter": "L. Ed. 2d",
        "page": "720",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4083",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4083",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 41",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "41",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "469 U.S. 325",
        "volume": "469",
        "reporter": "U.S.",
        "page": "325",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 733",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "733",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 L. Ed. 2d 720",
        "volume": "83",
        "reporter": "L. Ed. 2d",
        "page": "720",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 41",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "41",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4083",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4083",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "469 U.S. 325",
    "official_selection": {
      "court_class": "scotus",
      "selected": "469 U.S. 325",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-341",
      "page": null,
      "quote": "--- # New Jersey v. T.L.O. *469 U.S. 325 (1985)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A teacher found a 14-year-old student, T.L.O., smoking in a school bathroom. An assistant vice principal opened her purse, found cigarettes and rolling papers, and on continued inspection found marijuana, a pipe, plastic bags, money, and a list of students who owed her money. The evidence led to juvenile-delinquency charges. ## Issue What standard governs a search of a student by a public school official under the Fourth Amendment. ## Rule The Fourth Amendment applies to public school officials, but a school search requires only reasonableness under all the circumstances \u2014 not a warrant or probable cause.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-341b",
      "page": null,
      "quote": "Determining the reasonableness of any search involves a twofold inquiry: first, one must consider 'whether the . . . action was justified at its inception,' . . . second, one must determine whether the search as actually conducted 'was reasonably related in scope to the circumstances which justified the interference in the first place.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-342",
      "page": null,
      "quote": "justified at its inception",
      "star_marker": "341",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 33899,
      "fragment": "#:~:text=was-,justified%20at%20its%20inception",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-01-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "New Jersey v. T.L.O.",
    "varies_by_point": false,
    "scope_note": "Anchor for the reasonableness standard governing school searches; good law.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
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
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
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
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Fairfax Cnty. Sch. Bd. v. South Carolina",
          "cluster_id": 4624555,
          "cite": [
            "827 S.E.2d 592"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Gonzalez",
          "cluster_id": 4476634,
          "cite": [
            "96 N.E.3d 719",
            "93 Mass. App. Ct. 6"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Villagran",
          "cluster_id": 4422358,
          "cite": [
            "477 Mass. 711",
            "81 N.E.3d 310"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
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
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ulbricht",
          "cluster_id": 7311405,
          "cite": [
            "79 F. Supp. 3d 466",
            "96 Fed. R. Serv. 348",
            "2015 U.S. Dist. LEXIS 2016",
            "2015 WL 105799"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Andre Jerome Lyle Jr.",
          "cluster_id": 2687555,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Clark",
          "cluster_id": 2690293,
          "cite": [
            "2013 Ohio 4731",
            "137 Ohio St. 3d 346",
            "999 N.E.2d 592"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Christine Ann Kern",
          "cluster_id": 4472227,
          "cite": [
            "831 N.W.2d 149",
            "2013 WL 2278018",
            "2013 Iowa Sup. LEXIS 61"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Isaac Andrew Baldon III",
          "cluster_id": 4472245,
          "cite": [
            "829 N.W.2d 785",
            "2013 WL 1694553",
            "2013 Iowa Sup. LEXIS 42"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "K.W. v. State of Indiana",
          "cluster_id": 851991,
          "cite": [
            "984 N.E.2d 610",
            "2013 WL 653023",
            "2013 Ind. LEXIS 147"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. Wisconsin",
          "cluster_id": 111959,
          "cite": [
            "97 L. Ed. 2d 709",
            "107 S. Ct. 3164",
            "483 U.S. 868",
            "1987 U.S. LEXIS 2897",
            "55 U.S.L.W. 5156"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Buie",
          "cluster_id": 112384,
          "cite": [
            "108 L. Ed. 2d 276",
            "110 S. Ct. 1093",
            "494 U.S. 325",
            "1990 U.S. LEXIS 1176"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tennard v. Dretke, Director, Texas Department of Criminal Justice, Correctional Institutions Division",
          "cluster_id": 136994,
          "cite": [
            "159 L. Ed. 2d 384",
            "124 S. Ct. 2562",
            "542 U.S. 274",
            "2004 U.S. LEXIS 4575",
            "17 Fla. L. Weekly Fed. S 420",
            "72 U.S.L.W. 4540"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Hicks",
          "cluster_id": 111834,
          "cite": [
            "94 L. Ed. 2d 347",
            "107 S. Ct. 1149",
            "480 U.S. 321",
            "1987 U.S. LEXIS 1056",
            "55 U.S.L.W. 4258"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Soldal v. Cook County",
          "cluster_id": 112795,
          "cite": [
            "121 L. Ed. 2d 450",
            "113 S. Ct. 538",
            "506 U.S. 56",
            "1992 U.S. LEXIS 7835",
            "92 Daily Journal DAR 16378",
            "61 U.S.L.W. 4019",
            "6 Fla. L. Weekly Fed. S 769",
            "92 Cal. Daily Op. Serv. 9794"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Burger",
          "cluster_id": 111927,
          "cite": [
            "96 L. Ed. 2d 601",
            "107 S. Ct. 2636",
            "482 U.S. 691",
            "1987 U.S. LEXIS 2725",
            "55 U.S.L.W. 4890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'CONNOR v. Ortega",
          "cluster_id": 111851,
          "cite": [
            "94 L. Ed. 2d 714",
            "107 S. Ct. 1492",
            "480 U.S. 709",
            "1987 U.S. LEXIS 1507",
            "1 I.E.R. Cas. (BNA) 1617",
            "55 U.S.L.W. 4405",
            "42 Empl. Prac. Dec. (CCH) 36,891"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McKoy v. North Carolina",
          "cluster_id": 112388,
          "cite": [
            "108 L. Ed. 2d 369",
            "110 S. Ct. 1227",
            "494 U.S. 433",
            "1990 U.S. LEXIS 1179",
            "58 U.S.L.W. 4311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Waters v. Churchill",
          "cluster_id": 1087950,
          "cite": [
            "128 L. Ed. 2d 686",
            "114 S. Ct. 1878",
            "511 U.S. 661",
            "1994 U.S. LEXIS 4104"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hazelwood School District v. Kuhlmeier",
          "cluster_id": 111979,
          "cite": [
            "98 L. Ed. 2d 592",
            "108 S. Ct. 562",
            "484 U.S. 260",
            "1988 U.S. LEXIS 310",
            "56 U.S.L.W. 4079",
            "14 Media L. Rep. (BNA) 2081"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Arkansas",
          "cluster_id": 117936,
          "cite": [
            "131 L. Ed. 2d 976",
            "115 S. Ct. 1914",
            "514 U.S. 927",
            "1995 U.S. LEXIS 3464"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bethel School District No. 403 v. Fraser",
          "cluster_id": 111754,
          "cite": [
            "92 L. Ed. 2d 549",
            "106 S. Ct. 3159",
            "478 U.S. 675",
            "1986 U.S. LEXIS 139",
            "54 U.S.L.W. 5054"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Verdugo-Urquidez",
          "cluster_id": 112382,
          "cite": [
            "108 L. Ed. 2d 222",
            "110 S. Ct. 1056",
            "494 U.S. 259",
            "1990 U.S. LEXIS 1175",
            "1990 WL 16772"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111301 OR 9429812 OR 9429813 OR 9429814 OR 9429815 OR 9429816) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzIxMzE1MjAwMDAwJnM9NTk4MDg0MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111301+OR+9429812+OR+9429813+OR+9429814+OR+9429815+OR+9429816%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111301 OR 9429812 OR 9429813 OR 9429814 OR 9429815 OR 9429816)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00ODgmcz0xNDU3MDcmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111301+OR+9429812+OR+9429813+OR+9429814+OR+9429815+OR+9429816%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111301 OR 9429812 OR 9429813 OR 9429814 OR 9429815 OR 9429816)",
        "reviewed": 29,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 29,
        "triage_read": 0,
        "triage_snippet_classified": 29
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111301 OR 9429812 OR 9429813 OR 9429814 OR 9429815 OR 9429816)",
    "indexed_citing_opinions": 1437,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111301,
        "count": 1267,
        "count_source": "search"
      },
      {
        "opinion_id": 9429812,
        "count": 199,
        "count_source": "search"
      },
      {
        "opinion_id": 9429813,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429814,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429815,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429816,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2396,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/new-jersey-v-t-l-o.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4NDQ1NyZzPTk1NDYxMjYmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28111301+OR+9429812+OR+9429813+OR+9429814+OR+9429815+OR+9429816%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111301,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 103870,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 105221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107793,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110055,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110501,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110742,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110765,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111157,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111268,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 370522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 382282,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 386325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 409447,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 438820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 440480,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1292717,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1304814,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1381369,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1391108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1406903,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1463269,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1554742,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1567651,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1595918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1616294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1677246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1739670,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1900299,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1950670,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1961736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1969621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 2029772,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 2122374,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 2156966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 2183546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 2261463,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 2308367,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 2372587,
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
    "date_created": "2026-07-05T15:28:21Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:28:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:28:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:31:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:28:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — New Jersey v. T.L.O.

```
<opinion type="majority">
<author id="b469-7">Justice White</author>
<p id="AEJ">delivered the opinion of the Court.</p>
<p id="b469-8">We granted certiorari in this case to examine the appropriateness of the exclusionary rule as a remedy for searches carried out in violation of the Fourth Amendment by public school authorities. Our consideration of the proper application of the Fourth Amendment to the public schools, however, has led us to conclude that the search that gave rise to <page-number citation-index="1" label="328">*328</page-number>the case now before us did not violate the Fourth Amendment. Accordingly, we here address only the questions of the proper standard for assessing the legality of searches conducted by public school officials and the application of that standard to the facts of this case.</p>
<p id="b470-5">I</p>
<p id="b470-6">On March 7, 1980, a teacher at Piscataway High School in Middlesex County, N. J., discovered two girls smoking in a lavatory. One of the two girls was the respondent T. L. 0., who at that time was a 14-year-old high school freshman. Because smoking in the lavatory was a violation of a school rule, the teacher took the two girls to the Principal’s office, where they met with Assistant Vice Principal Theodore Choplick. In response to questioning by Mr. Choplick, T. L. O.’s companion admitted that she had violated the rule. T. L. 0., however, denied that she had been smoking in the lavatory and claimed that she did not smoke at all.</p>
<p id="b470-7">Mr. Choplick asked T. L. O. to come into his private office and demanded to see her purse. Opening the purse, he found a pack of cigarettes, which he removed from the purse and held before T. L. O. as he accused her of having lied to him. As he reached into the purse for the cigarettes, Mr. Choplick also noticed a package of cigarette rolling papers. In his experience, possession of rolling papers by high school students was closely associated with the use of marihuana. Suspecting that a closer examination of the purse might yield further evidence of drug use, Mr. Choplick proceeded to search the purse thoroughly. The search revealed a smáll amount of marihuana, a pipe, a number of empty plastic bags, a substantial quantity of money in one-dollar bills, an index card that appeared to be a list of students who owed T. L. O. money, and two letters that implicated T. L. O. in marihuana dealing.</p>
<p id="b470-8">Mr. Choplick notified T. L. O.’s mother and the police, and turned the evidence of drug dealing over to the police. At <page-number citation-index="1" label="329">*329</page-number>the request of the police, T. L. O.’s mother took her daughter to police headquarters, where T. L. O. confessed that she had been selling marihuana at the high school. On the basis of the confession and the evidence seized by Mr. Choplick, the State brought delinquency charges against T. L. O. in the Juvenile and Domestic Relations Court of Middlesex County.<footnotemark>1</footnotemark> Contending that Mr. Choplick’s search of her purse violated the Fourth Amendment, T. L. O. moved to suppress the evidence found in her purse as well as her confession, which, she argued, was tainted by the allegedly unlawful search. The Juvenile Court denied the motion to suppress. <em>State ex rel. T. L. O., </em>178 N. J. Super. 329, <span class="citation" data-id="2261463"><a href="/opinion/2261463/state-in-interest-of-tlo/" aria-description="Citation for case: State in Interest of TLO">428 A. 2d 1327</a></span> (1980). Although the court concluded that the Fourth Amendment did apply to searches carried out by school officials, it held that</p>
<blockquote id="b471-5">“a school official may properly conduct a search of a student’s person if the official has a reasonable suspicion that a crime has been or is in the process of being committed, or reasonable cause to believe that the search is necessary to maintain school discipline or enforce school policies.” <em>Id., </em>at 341, <span class="citation" data-id="2261463"><a href="/opinion/2261463/state-in-interest-of-tlo/#1333" aria-description="Citation for case: State in Interest of TLO">428 A. 2d, at 1333</a></span> (emphasis in original).</blockquote>
<p id="b471-6">Applying this standard, the court concluded that the search conducted by Mr. Choplick was a reasonable one. The initial decision to open the purse was justified by Mr. Choplick’s well-founded suspicion that T. L. O. had violated the rule forbidding smoking in the lavatory. Once the purse <page-number citation-index="1" label="330">*330</page-number>was open, evidence of marihuana violations was in plain view, and Mr. Choplick was entitled to conduct a thorough search to determine the nature and extent of T. L. O.’s drug-related activities. <em>Id., </em>at 343, <span class="citation" data-id="2261463"><a href="/opinion/2261463/state-in-interest-of-tlo/#1334" aria-description="Citation for case: State in Interest of TLO">428 A. 2d, at 1334</a></span>. Having denied the motion to suppress, the court on March 23, 1981, found T. L. O. to be a delinquent and on January 8, 1982, sentenced her to a year’s probation.</p>
<p id="b472-5">On appeal from the final judgment of the Juvenile Court, a divided Appellate Division affirmed the trial court’s finding that there had been no Fourth Amendment violation, but vacated the adjudication of delinquency and remanded for a determination whether T. L. O. had knowingly and voluntarily waived her Fifth Amendment rights before confessing. <em>State ex rel. T. L. O., </em>185 N. J. Super. 279, <span class="citation" data-id="7318184"><a href="/opinion/7399164/state-ex-rel-t-l-o/" aria-description="Citation for case: State ex rel. T. L. O.">448 A. 2d 493</a></span> (1982). T. L. O. appealed the Fourth Amendment ruling, and the Supreme Court of New Jersey reversed the judgment of the Appellate Division and ordered the suppression of the evidence found in T. L. O.’s purse. <em>State ex rel. T. L. O., </em>94 N. J. 331, <span class="citation" data-id="7305116"><a href="/opinion/7386217/state-v-engerud/" aria-description="Citation for case: State v. Engerud">463 A. 2d 934</a></span> (1983).</p>
<p id="b472-6">The New Jersey Supreme Court agreed with the lower courts that the Fourth Amendment applies to searches conducted by school officials. The court also rejected the State of New Jersey’s argument that the exclusionary rule should not be employed to prevent the use in juvenile proceedings of evidence unlawfully seized by school officials. Declining to consider whether applying the rule to the fruits of searches by school officials would have any deterrent value, the court held simply that the precedents of this Court establish that “if an official search violates constitutional rights, the evidence is not admissible in criminal proceedings.” <em>Id., </em>at 341, <span class="citation" data-id="7305116"><a href="/opinion/7386217/state-v-engerud/#939" aria-description="Citation for case: State v. Engerud">463 A. 2d, at 939</a></span> (footnote omitted).</p>
<p id="b472-7">With respect to the question of the legality of the search before it, the court agreed with the Juvenile Court that a warrantless search by a school official does not violate the Fourth Amendment so long as the official “has reasonable grounds to believe that a student possesses evidence of illegal <page-number citation-index="1" label="331">*331</page-number>activity or activity that would interfere with school discipline and order.” <em>Id., </em>at 346, <span class="citation" data-id="7305116"><a href="/opinion/7386217/state-v-engerud/#941" aria-description="Citation for case: State v. Engerud">463 A. 2d, at 941-942</a></span>. However, the court, with two justices dissenting, sharply disagreed with the Juvenile Court’s conclusion that the search of the purse was reasonable. According to the majority, the contents of T. L. O.’s purse had no bearing on the accusation against T. L. 0., for possession of cigarettes (as opposed to smoking them in the lavatory) did not violate school rules, and a mere desire for evidence that would impeach T. L. O.’s claim that she did not smoke cigarettes could not justify the search. Moreover, even if a reasonable suspicion that T. L. O. had cigarettes in her purse would justify a search, Mr. Choplick had no such suspicion, as no one had furnished him with any specific information that there were cigarettes in the purse. Finally, leaving aside the question whether Mr. Choplick was justified in opening the purse, the court held that the evidence of drug use that he saw inside did not justify the extensive “rummaging” through T. L. O.’s papers and effects that followed. <em>Id., </em>at 347, <span class="citation" data-id="7305116"><a href="/opinion/7386217/state-v-engerud/#942" aria-description="Citation for case: State v. Engerud">463 A. 2d, at 942-943</a></span>.</p>
<p id="b473-5">We granted the State of New Jersey’s petition for certio-rari. <span class="citation multiple-matches"><a href="/c/U.%20S./464/991/">464 U. S. 991</a></span> (1983). Although the State had argued in the Supreme Court of New Jersey that the search of T. L. O.’s purse did not violate the Fourth Amendment, the petition for certiorari raised only the question whether the exclusionary rule should operate to bar consideration in juvenile delinquency proceedings of evidence unlawfully seized by a school official without the involvement of law enforcement officers. When this case was first argued last Term, the State conceded for the purpose of argument that the standard devised by the New Jersey Supreme Court for determining the legality of school searches was appropriate and that the court had correctly applied that standard; the State contended only that the remedial purposes of the exclusionary rule were not well served by applying it to searches conducted by public authorities not primarily engaged in law enforcement.</p>
<p id="b474-4"><page-number citation-index="1" label="332">*332</page-number>Although we originally granted certiorari to decide the issue of the appropriate remedy in juvenile court proceedings for unlawful school searches, our doubts regarding the wisdom of deciding that question in isolation from the broader question of what limits, if any, the Fourth Amendment places on the activities of school authorities prompted us to order reargument on that question.<footnotemark>2</footnotemark> Having heard argument on <page-number citation-index="1" label="333">*333</page-number>the legality of the search of T. L. O.’s purse, we are satisfied that the search did not violate the Fourth Amendment.<footnotemark>3</footnotemark></p>
<p id="b475-5">II</p>
<p id="b475-6">In determining whether the search at issue in this case violated the Fourth Amendment, we are faced initially with the question whether that Amendment’s prohibition on unreasonable searches and seizures applies to searches conducted by public school officials. We hold that it does.</p>
<p id="b476-4"><page-number citation-index="1" label="334">*334</page-number>It is now beyond dispute that “the Federal Constitution, by virtue of the Fourteenth Amendment, prohibits unreasonable searches and seizures by state officers.” <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#213" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 213</a></span> (1960); accord, <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961); <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span> (1949). Equally indisputable is the proposition that the Fourteenth Amendment protects the rights of students against encroachment by public school officials:</p>
<blockquote id="b476-5">“The Fourteenth Amendment, as now applied to the States, protects the citizen against the State itself and all of its creatures — Boards of Education not excepted. These have, of course, important, delicate, and highly discretionary functions, but none that they may not perform within the limits of the Bill of Rights. That they are educating the young for citizenship is reason for scrupulous protection of Constitutional freedoms of the individual, if we are not to strangle the free mind at its source and teach youth to discount important principles of our government as mere platitudes.” <em>West Virginia State Bd. of Ed. </em>v. <em>Barnette, </em><span class="citation" data-id="9419378"><a href="/opinion/103870/west-virginia-state-board-of-education-v-barnette/#637" aria-description="Citation for case: West Virginia State Board of Education v. Barnette">319 U. S. 624, 637</a></span> (1943).</blockquote>
<p id="b476-6">These two propositions — that the Fourth Amendment applies to the States through the Fourteenth Amendment, and that the actions of public school officials are subject to the limits placed on state action by the Fourteenth Amendment — might appear sufficient to answer the suggestion that the Fourth Amendment does not proscribe unreasonable searches by school officials. On reargument, however, the State of New Jersey has argued that the history of the Fourth Amendment indicates that the Amendment was intended to regulate only searches and seizures carried out by law enforcement officers; accordingly, although public school officials are concededly state agents for purposes of the Fourteenth Amendment, the Fourth Amendment creates no rights enforceable against them.<footnotemark>4</footnotemark></p>
<p id="b477-4"><page-number citation-index="1" label="335">*335</page-number>It may well be true that the evil toward which the Fourth Amendment was primarily directed was the resurrection of the pre-Revolutionary practice of using general warrants or “writs of assistance” to authorize searches for contraband by officers of the Crown. See <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#7" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 7-8</a></span> (1977); <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 624-629</a></span> (1886). But this Court has never limited the Amendment’s prohibition on unreasonable searches and seizures to operations conducted by the police. Rather, the Court has long spoken of the Fourth Amendment’s strictures as restraints imposed upon “governmental action” — that is, “upon the activities of sovereign authority.” <em>Burdeau </em>v. <em>McDowell, </em><span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/#475" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465, 475</a></span> (1921). Accordingly, we have held the Fourth Amendment applicable to the activities of civil as well as criminal authorities: building inspectors, see <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528</a></span> (1967), Occupational Safety and Health Act inspectors, see <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#312" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 312-313</a></span> (1978), and even firemen entering privately owned premises to battle a fire, see <em>Michigan </em>v. <em>Tyler, </em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#506" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499, 506</a></span> (1978), are all subject to the restraints imposed by the Fourth Amendment. As we observed in <em>Camara </em>v. <em>Municipal <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Court, supra,</a></span> </em>“[t]he basic purpose of this Amendment, as recognized in countless decisions of this Court, is to safeguard the privacy and security of individuals against arbitrary invasions by governmental officials.” <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 528</a></span>. Because the individual’s interest in privacy and personal security “suffers whether the government’s motivation is to investigate violations of criminal laws or breaches of other statutory or regulatory standards,” <em>Marshall </em>v. <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#312" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><em>Barlow’s, Inc., supra, </em>at 312-313</a></span>, it would be “anomalous to say that the individual and his private property are fully protected by the Fourth Amendment only when the individual is suspected of criminal behavior.” <em>Camara </em>v. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#530" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><em>Municipal Court, supra, </em>at 530</a></span>.</p>
<p id="b478-3"><page-number citation-index="1" label="336">*336</page-number>Notwithstanding the general applicability of the Fourth Amendment to the activities of civil authorities, a few courts have concluded that school officials are exempt from the dictates of the Fourth Amendment by virtue of the special nature of their authority over schoolchildren. See, <em>e. g., R. C. M. </em>v. <em>State, </em><span class="citation" data-id="5060443"><a href="/opinion/5235277/rcm-v-state/" aria-description="Citation for case: R.C.M. v. State">660 S. W. 2d 552</a></span> (Tex. App. 1983). Teachers and school administrators, it is said, act <em>in loco parentis </em>in their dealings with students: their authority is that of the parent, not the State, and is therefore not subject to the limits of the Fourth Amendment. <em><span class="citation" data-id="5060443"><a href="/opinion/5235277/rcm-v-state/" aria-description="Citation for case: R.C.M. v. State">Ibid.</a></span></em></p>
<p id="b478-4">Such reasoning is in tension with contemporary reality and the teachings of this Court. We have held school officials subject to the commands of the First Amendment, see <em>Tinker </em>v. <em>Des Moines Independent Community School District, </em><span class="citation" data-id="9423907"><a href="/opinion/107841/tinker-v-des-moines-independent-community-school-district/" aria-description="Citation for case: Tinker v. Des Moines Independent Community School District">393 U. S. 503</a></span> (1969), and the Due Process Clause of the Fourteenth Amendment, see <em>Goss </em>v. <em>Lopez, </em><span class="citation" data-id="9425909"><a href="/opinion/109136/goss-v-lopez/" aria-description="Citation for case: Goss v. Lopez">419 U. S. 565</a></span> (1975). If school authorities are state actors for purposes of the constitutional guarantees of freedom of expression and due process, it is difficult to understand why they should be deemed to be exercising parental rather than public authority when conducting searches of their students. More generally, the Court has recognized that “the concept of parental delegation” as a source of school authority is not entirely “consonant with compulsory education laws.” <em>Ingraham </em>v. <em>Wright, </em><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#662" aria-description="Citation for case: Ingraham v. Wright">430 U. S. 651, 662</a></span> (1977). Today’s public school officials do not merely exercise authority voluntarily conferred on them by individual parents; rather, they act in furtherance of publicly mandated educational and disciplinary policies. See, <em>e. g., </em>the opinion in <em>State ex rel. T. L. O., </em>94 N. J., at 343, <span class="citation" data-id="7305116"><a href="/opinion/7386217/state-v-engerud/#934" aria-description="Citation for case: State v. Engerud">463 A. 2d, at 934, 940</a></span>, describing the New Jersey statutes regulating school disciplinary policies and establishing the authority of school officials over their students. In carrying out searches and other disciplinary functions pursuant to such policies, school officials act as representatives of the State, not merely as surrogates for the parents, and they <page-number citation-index="1" label="337">*337</page-number>cannot claim the parents’ immunity from the strictures of the Fourth Amendment.</p>
<p id="b479-5">Ill</p>
<p id="b479-6">To hold that the Fourth Amendment applies to searches conducted by school authorities is only to begin the inquiry into the standards governing such searches. Although the underlying command of the Fourth Amendment is always that searches and seizures be reasonable, what is reasonable depends on the context within which a search takes place. The determination of the standard of reasonableness governing any specific class of searches requires “balancing the need to search against the invasion which the search entails.” <em>Camara </em>v. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#536" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><em>Municipal Court, supra, </em>at 536-537</a></span>. On one side of the balance are arrayed the individual’s legitimate expectations of privacy and personal security; on the other, the government’s need for effective methods to deal with breaches of public order.</p>
<p id="b479-7">We have recognized that even a limited search of the person is a substantial invasion of privacy. <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 24-25</a></span> (1967). We have also recognized that searches of closed items of personal luggage are intrusions on protected privacy interests, for “the Fourth Amendment pro-' vides protection to the owner of every container that conceals" its contents from plain view.” <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#822" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 822-823</a></span> (1982). A search of a child’s person or of' a closed purse or other bag carried on her person,<footnotemark>5</footnotemark> no less <page-number citation-index="1" label="338">*338</page-number>than a similar search carried out on an adult, is undoubtedly a severe violation of subjective expectations of privacy.</p>
<p id="b480-5">. Of course, the Fourth Amendment does not protect subjective expectations of privacy that are unreasonable or otherwise “illegitimate.” See, <em>e. g., Hudson </em>v. <em>Palmer, </em><span class="citation" data-id="9429735"><a href="/opinion/111252/hudson-v-palmer/" aria-description="Citation for case: Hudson v. Palmer">468 U. S. 517</a></span> (1984); <em>Rawlings </em>v. <em>Kentucky, </em><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">448 U. S. 98</a></span> (1980). To receive the protection of the Fourth Amendment, an expectation of privacy must be one that society is “prepared to recognize as legitimate.” <em>Hudson </em>v. <span class="citation" data-id="9429735"><a href="/opinion/111252/hudson-v-palmer/#526" aria-description="Citation for case: Hudson v. Palmer"><em>Palmer, supra, </em>at 526</a></span>. The State of New Jersey has argued that because of the pervasive supervision to which children in the schools are necessarily subject, a child has virtually no legitimate expectation of privacy in articles of personal property “unnecessarily” carried into a school. This argument has two factual premises: (1) the fundamental incompatibility of expectations of privacy with the maintenance of a sound educational environment; and (2) the minimal interest of the child in bringing any items of personal property into the school. Both premises are severely flawed.</p>
<p id="b480-6">Although this Court may take notice of the difficulty of maintaining discipline in the public schools today, the situation is not so dire that students in the schools may claim no legitimate expectations of privacy. We have recently recognized that the need to maintain order in a prison is such that prisoners retain no legitimate expectations of privacy in their cells, but it goes almost without saying that “[tjhe prisoner and the schoolchild stand in wholly different circumstances, separated by the harsh facts of criminal conviction and incarceration.” <em>Ingraham </em>v. <span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#669" aria-description="Citation for case: Ingraham v. Wright"><em>Wright, supra, </em>at 669</a></span>. We are not <page-number citation-index="1" label="339">*339</page-number>yet ready to hold that the schools and the prisons need be equated for purposes of the Fourth Amendment.</p>
<p id="b481-5">Nor does the State’s suggestion that children have no legitimate need to bring personal property into the schools seem well anchored in reality. Students at a minimum must bring to school not only the supplies needed for their studies, but also keys, money, and the necessaries of personal hygiene and grooming. In addition, students may carry on their persons or in purses or wallets such nondisruptive yet highly personal items as photographs, letters, and diaries. Finally, students may have perfectly legitimate reasons to carry with them articles of property needed in connection with extracurricular or recreational activities. In short, schoolchildren may find it necessary to carry with them a variety of legitimate, noncontraband items, and there is no reason to conclude that they have necessarily waived all rights to privacy in such items merely by bringing them onto school grounds.</p>
<p id="b481-6">Against the child’s interest in privacy must be set the substantial interest of teachers and administrators in maintaining discipline in the classroom and on school grounds. Maintaining order in the classroom has never been easy, but in recent years, school disorder has often taken particularly ugly forms: drug use and violent crime in the schools have become major social problems. See generally 1 NIE, U. S. Dept, of Health, Education and Welfare, Violent Schools— Safe Schools: The Safe School Study Report to the Congress (1978). Even in schools that have been spared the most severe disciplinary problems, the preservation of order and a proper educational environment requires close supervision of schoolchildren, as well as the enforcement of rules against conduct that would be perfectly permissible if undertaken by an adult. “Events calling for discipline are frequent occurrences and sometimes require immediate, effective action.” Goss v. <em>Lopez, </em><span class="citation" data-id="9425909"><a href="/opinion/109136/goss-v-lopez/#580" aria-description="Citation for case: Goss v. Lopez">419 U. S., at 580</a></span>. Accordingly, we have rec<page-number citation-index="1" label="340">*340</page-number>ognized that maintaining security and order in the schools requires a certain degree of flexibility in school disciplinary procedures, and we have respected the value of preserving the informality of the student-teacher relationship. See <span class="citation" data-id="9425909"><a href="/opinion/109136/goss-v-lopez/#582" aria-description="Citation for case: Goss v. Lopez"><em>id., </em>at 582-583</a></span>; <em>Ingraham </em>v. <em>Wright, </em><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#680" aria-description="Citation for case: Ingraham v. Wright">430 U. S., at 680-682</a></span>.</p>
<p id="b482-5">How, then, should we strike the balance between the schoolchild’s legitimate expectations of privacy and the school’s equally legitimate need to maintain an environment in which learning can take place? It is evident that the school setting requires some easing of the restrictions to which searches by public authorities are ordinarily subject. The warrant requirement, in particular, is unsuited to the school environment: requiring a teacher to obtain a warrant before searching a child suspected of an infraction of school rules (or of the criminal law) would unduly interfere with the maintenance of the swift and informal disciplinary procedures needed in the schools. Just as we have in other cases dispensed with the warrant requirement when “the burden of obtaining a warrant is likely to frustrate the governmental purpose behind the search,” <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 532-533</a></span>, we hold today that school officials need not obtain a warrant before searching a student who is under their authority.</p>
<p id="b482-6">The school setting also requires some modification of the level of suspicion of illicit activity needed to justify a search. Ordinarily, a search — even one that may permissibly be carried out without a warrant — must be based upon “probable cause” to believe that a violation of the law has occurred. See, <em>e. g., Almeida-Sanchez </em>v. <em>United States, </em><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#273" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 273</a></span> (1973); <em>Sibron </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#62" aria-description="Citation for case: Sibron v. New York">392 U. S. 40, 62-66</a></span> (1968). However, “probable cause” is not an irreducible requirement of a valid search. The fundamental command of the Fourth Amendment is that searches and seizures be reasonable, and although “both the concept of probable cause and the requirement of a warrant bear on the reasonableness of a search, . . . in certain limited circumstances neither is required.” <em>Almeida-Sanchez </em>v. <em>United States, supra, </em>at 277 (Powell, <page-number citation-index="1" label="341">*341</page-number>J., concurring). Thus, we have in a number of cases recognized the legality of searches and seizures based on suspicions that, although “reasonable,” do not rise to the level of probable cause. See, <em>e. g., Terry </em>v. Ohio, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968); <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 881</a></span> (1975); <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654-655</a></span> (1979); <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976); cf. <em>Camara </em>v. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><em>Municipal Court, supra, </em>at 534-539</a></span>. Where a careful balancing of governmental and private interests suggests that the public interest is best served by a Fourth Amendment standard of reasonableness that stops short of probable cause, we have not hesitated to adopt such a standard.</p>
<p id="b483-5">We join the majority of courts that have examined this issue<footnotemark>6</footnotemark> in concluding that the accommodation of the privacy interests of schoolchildren with the substantial need of teachers and administrators for freedom to maintain order in the schools does not require strict adherence to the requirement that searches be based on probable cause to believe that the subject of the search has violated or is violating the law. Rather, the legality of a search of a student should depend simply on the reasonableness, under all the circumstances, of the search. Determining the reasonableness of any search involves a twofold inquiry: first, one must consider “whether the . . . action was justified at its inception,” <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20</a></span>; second, one must determine whether the search as actually conducted “was reasonably related in scope to the circumstances which justified the interference in the first place,” <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">ibid.</a></span> </em>Under ordinary circumstances, a search of a student by a teacher or other school official<footnotemark>7</footnotemark> will be <page-number citation-index="1" label="342">*342</page-number>“justified at its inception” when there are reasonable grounds for suspecting that the search will turn up evidence that the student has violated or is violating either the law or the rules of the school.<footnotemark>8</footnotemark> Such a search will be permissible in its scope when the measures adopted are reasonably related to the objectives of the search and not excessively intrusive in light of the age and sex of the student and the nature of the infraction.<footnotemark>9</footnotemark></p>
<p id="b484-5">This standard will, we trust, neither unduly burden the efforts of school authorities to maintain order in their schools <page-number citation-index="1" label="343">*343</page-number>nor authorize unrestrained intrusions upon the privacy of schoolchildren. By focusing attention on the question of reasonableness, the standard will spare teachers and school administrators the necessity of schooling themselves in the niceties of probable cause and permit them to regulate their conduct according to the dictates of reason and common sense. At the same time, the reasonableness standard should ensure that the interests of students will be invaded no more than is necessary to achieve the legitimate end of preserving order in the schools.</p>
<p id="b485-5">IV</p>
<p id="b485-6">There remains the question of the legality of the search in this case. We recognize that the “reasonable grounds” standard applied by the New Jersey Supreme Court in its consideration of this question is not substantially different from the standard that we have adopted today. Nonetheless, we believe that the New Jersey court’s application of that standard to strike down the search of T. L. O.’s purse reflects a somewhat crabbed notion of reasonableness. Our review of the facts surrounding the search leads us to conclude that the search was in no sense unreasonable for Fourth Amendment purposes.<footnotemark>10</footnotemark></p>
<p id="b485-7">The incident that gave rise to this case actually involved two separate searches, with the first — the search for cigarettes — providing the suspicion that gave rise to the sec<page-number citation-index="1" label="344">*344</page-number>ond — the search for marihuana. Although it is the fruits of the second search that are at issue here, the validity of the search for marihuana must depend on the reasonableness of the initial search for cigarettes, as there would have been no reason to suspect that T. L. O. possessed marihuana had the first search not taken place. Accordingly, it is to the search for cigarettes that we first turn our attention.</p>
<p id="b486-5">The New Jersey Supreme Court pointed to two grounds for its holding that the search for cigarettes was unreasonable. First, the court observed that possession of cigarettes was not in itself illegal or a violation of school rules. Because the contents of T. L. O.’s purse would therefore have “no direct bearing on the infraction” of which she was accused (smoking in a lavatory where smoking was prohibited), there was no reason to search her purse.<footnotemark>11</footnotemark> Second, even assuming that a search of T. L. O.’s purse might under some circumstances be reasonable in light of the accusation made against T. L. 0., the New Jersey court concluded that Mr. Choplick in this particular case had no reasonable grounds to suspect that T. L. O. had cigarettes in her purse. At best, accord<page-number citation-index="1" label="345">*345</page-number>ing to the court, Mr. Chopliek had “a good hunch.” 94 N. J., at 347, <span class="citation" data-id="7305116"><a href="/opinion/7386217/state-v-engerud/#942" aria-description="Citation for case: State v. Engerud">463 A. 2d, at 942</a></span>.</p>
<p id="b487-5">Both these conclusions are implausible. T. L. O. had been accused of smoking, and had denied the accusation in the strongest possible terms when she stated that she did not smoke at all. Surely it cannot be said that under these circumstances, T. L. O.’s possession of cigarettes would be irrelevant to the charges against her or to her response to those charges. T. L. O.’s possession of cigarettes, once it was discovered, would both corroborate the report that she had been smoking and undermine the credibility of her defense to the charge of smoking. To be sure, the discovery of the cigarettes would not prove that T. L. O. had been smoking in the lavatory; nor would it, strictly speaking, necessarily be inconsistent with her claim that she did not smoke at all. But it is universally recognized that evidence, to be relevant to an inquiry, need not conclusively prove the ultimate fact in issue, but only have “any tendency to make the existence of any fact that is of consequence to the determination of the action more probable or less probable than it would be without the evidence.” Fed. Rule Evid. 401. The relevance of T. L. O.’s possession of cigarettes to the question whether she had been smoking and to the credibility of her denial that she smoked supplied the necessary “nexus” between the item searched for and the infraction under investigation. See <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#306" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 306-307</a></span> (1967). Thus, if Mr. Chopliek in fact had a reasonable suspicion that T. L. O. had cigarettes in her purse, the search was justified despite the fact that the cigarettes, if found, would constitute “mere evidence” of a violation. <em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Ibid.</a></span></em></p>
<p id="b487-6">Of course, the New Jersey Supreme Court also held that Mr. Chopliek had no reasonable suspicion that the purse would contain cigarettes. This conclusion is puzzling. A teacher had reported that T. L. O. was smoking in the lavatory. Certainly this report gave Mr. Chopliek reason to suspect that T. L. O. was carrying cigarettes with her; and <page-number citation-index="1" label="346">*346</page-number>if she did have cigarettes, her purse was the obvious place in which to find them. Mr. Choplick’s suspicion that there were cigarettes in the purse was not an “inchoate and un-particularized suspicion or ‘hunch,’” <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 27</a></span>; rather, it was the sort of “common-sense conclusio[n] about human behavior” upon which “practical people” — including government officials — are entitled to rely. <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#418" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 418</a></span> (1981). Of course, even if the teacher’s report were true, T. L. O. <em>might </em>not have had a pack of cigarettes with her; she might have borrowed a cigarette from someone else or have been sharing a cigarette with another student. But the requirement of reasonable suspicion is not a requirement of absolute certainty: “sufficient probability, not certainty, is the touchstone of reasonableness under the Fourth Amendment. ...” <em>Hill </em>v. <em>California, </em><span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/#804" aria-description="Citation for case: Hill v. California">401 U. S. 797, 804</a></span> (1971). Because the hypothesis that T. L. O. was carrying cigarettes in her purse was itself not unreasonable, it is irrelevant that other hypotheses were also consistent with the teacher’s accusation. Accordingly, it cannot be said that Mr. Choplick acted unreasonably when he examined T. L. O.’s purse to see if it contained cigarettes.<footnotemark>12</footnotemark></p>
<p id="b489-4"><page-number citation-index="1" label="347">*347</page-number>Our conclusion that Mr. Choplick’s decision to open T. L. O.’s purse was reasonable brings us to the question of the further search for marihuana once the pack of cigarettes was located. The suspicion upon which the search for marihuana was founded was provided when Mr. Choplick observed a package of rolling papers in the purse as he removed the pack of cigarettes. Although T. L. O. does not dispute the reasonableness of Mr. Choplick’s belief that the rolling papers indicated the presence of marihuana, she does contend that the scope of the search Mr. Choplick conducted exceeded permissible bounds when he seized and read certain letters that implicated T. L. O. in drug dealing. This argument, too, is unpersuasive. The discovery of the rolling papers concededly gave rise to a reasonable suspicion that T. L. O. was carrying marihuana as well as cigarettes in her purse. This suspicion justified further exploration of T. L. O.’s purse, which turned up more evidence of drug-related activities: a pipe, a number of plastic bags of the type commonly used to store marihuana, a small quantity of marihuana, and a fairly substantial amount of money. Under these circumstances, it was not unreasonable to extend the search to a separate zippered compartment of the purse; and when a search of that compartment revealed an index card containing a list of “people who owe me money” as well as two letters, the inference that T. L. O. was involved in marihuana trafficking was substantial enough to justify Mr. Choplick in examining the letters to determine whether they contained any further evidence. In short, we cannot conclude that the search for marihuana was unreasonable in any respect.</p>
<p id="b489-5">Because the search resulting in the discovery of the evidence of marihuana dealing by T. L. O. was reasonable, the New Jersey Supreme Court’s decision to exclude that evi<page-number citation-index="1" label="348">*348</page-number>dence from T. L. O.’s juvenile delinquency proceedings on Fourth Amendment grounds was erroneous. Accordingly, the judgment of the Supreme Court of New Jersey is</p>
<p id="b490-5">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b471-7"> T. L. O. also received a 3-day suspension from school for smoking cigarettes in a nonsmoking area and a 7-day suspension for possession of marihuana. On T. L. O.’s motion, the Superior Court of New Jersey, Chancery Division, set aside the 7-day suspension on the ground that it was based on evidence seized in violation of the Fourth Amendment. <em>(T. L. O.) </em>v. <em>Piscataway Bd. of Ed., </em>No. C.2865-79 (Super. Ct. N. J., Ch. Div., Mar. 31, 1980). The Board of Education apparently did not appeal the decision of the Chancery Division.</p>
</footnote>
<footnote label="2">
<p id="b474-5"> State and federal courts considering these questions have struggled to accommodate the interests protected by the Fourth Amendment and the interest of the States in providing a safe environment conducive to education in the public schools. Some courts have resolved the tension between these interests by giving full force to one or the other side of the balance. Thus, in a number of cases courts have held that school officials conducting in-school searches of students are private parties acting <em>in loco parentis </em>and are therefore not subject to the constraints of the Fourth Amendment. See, <em>e. g., D. R. C. </em>v. <em>State, </em><span class="citation" data-id="5157665"><a href="/opinion/5327621/d-r-c-v-state/" aria-description="Citation for case: D. R. C. v. State">646 P. 2d 252</a></span> (Alaska App. 1982); <em>In re G., </em><span class="citation multiple-matches"><a href="/c/Cal.%20App.%203d/11/1193/">11 Cal. App. 3d 1193</a></span>, <span class="citation multiple-matches"><a href="/c/Cal.%20Rptr./90/361/">90 Cal. Rptr. 361</a></span> (1970); <em>In re Donaldson, </em><span class="citation" data-id="2205714"><a href="/opinion/2205714/mercer-v-donaldson/" aria-description="Citation for case: Mercer v. Donaldson">269 Cal. App. 2d 509</a></span>, <span class="citation" data-id="2205714"><a href="/opinion/2205714/mercer-v-donaldson/" aria-description="Citation for case: Mercer v. Donaldson">75 Cal. Rptr. 220</a></span> (1969); <em>R. C. M. </em>v. <em>State, </em><span class="citation" data-id="5060443"><a href="/opinion/5235277/rcm-v-state/" aria-description="Citation for case: R.C.M. v. State">660 S. W. 2d 552</a></span> (Tex. App. 1983); <em>Mercer </em>v. <em>State, </em><span class="citation" data-id="9653644"><a href="/opinion/1567651/mercer-v-state/" aria-description="Citation for case: Mercer v. State">450 S. W. 2d 715</a></span> (Tex. Civ. App. 1970). At least one court has held, on the other hand, that the Fourth Amendment applies in full to in-school searches by school officials and that a search conducted without probable cause is unreasonable, see <em>State </em>v. <em>Mora, </em><span class="citation" data-id="1739670"><a href="/opinion/1739670/state-v-mora/" aria-description="Citation for case: State v. Mora">307 So. 2d 317</a></span> (La.), vacated, <span class="citation multiple-matches"><a href="/c/U.%20S./423/809/">423 U. S. 809</a></span> (1975), on remand, <span class="citation" data-id="1950670"><a href="/opinion/1950670/state-v-mora/" aria-description="Citation for case: State v. Mora">330 So. 2d 900</a></span> (La. 1976); others have held or suggested that the probable-cause standard is applicable at least where the police are involved in a search, see <em>M. </em>v. <em>Board of Ed. Ball-Chatham Community Unit School Dist. No. 5, </em><span class="citation" data-id="1554742"><a href="/opinion/1554742/m-ex-rel-r-v-board-of-education-ball-chatham-community-unit-school/#292" aria-description="Citation for case: M. Ex Rel. R. v. Board of Education Ball-Chatham...">429 F. Supp. 288, 292</a></span> (SD Ill. 1977); <em>Picha </em>v. <em>Wielgos, </em><span class="citation" data-id="2308367"><a href="/opinion/2308367/picha-v-wielgos/#1219" aria-description="Citation for case: Picha v. Wielgos">410 F. Supp. 1214, 1219-1221</a></span> (ND Ill. 1976); <em>State </em>v. <em>Young, </em><span class="citation" data-id="9616519"><a href="/opinion/1391108/state-v-young/#498" aria-description="Citation for case: State v. Young">234 Ga. 488, 498</a></span>, <span class="citation" data-id="9616519"><a href="/opinion/1391108/state-v-young/#594" aria-description="Citation for case: State v. Young">216 S. E. 2d 586, 594</a></span> (1975); or where the search is highly intrusive, see <em>M. M. </em>v. <em>Anker, </em><span class="citation multiple-matches"><a href="/c/F.%202d/607/588/">607 F. 2d 588</a></span>, 589 (CA2 1979).</p>
<p id="b474-6">The majority of courts that have addressed the issue of the Fourth Amendment in the schools have, like the Supreme Court of New Jersey in this case, reached a middle position: the Fourth Amendment applies to searches conducted by school authorities, but the special needs of the school environment require assessment of the legality of such searches against a standard less exacting than that of probable cause. These courts have, by and large, upheld warrantless searches by school authorities provided that they are supported by a reasonable suspicion that the search will uncover evidence of an infraction of school disciplinary rules or a violation of the law. See, <em>e. g., Tarter </em>v. <em>Baybuck, </em>No. 83-3174 (CA6, Aug. 31, 1984); <em>Bilbrey </em>v. <em>Brown, </em><span class="citation multiple-matches"><a href="/c/F.%202d/738/1462/">738 F. 2d 1462</a></span> (CA91984); <em>Horton </em>v. <em>Goose Creek </em><page-number citation-index="1" label="333">*333</page-number><em>Independent School Dist., </em><span class="citation multiple-matches"><a href="/c/F.%202d/690/470/">690 F. 2d 470</a></span> (CA5 1982); <em>Bellnier </em>v. <em>Lund, </em><span class="citation" data-id="1463269"><a href="/opinion/1463269/bellnier-v-lund/" aria-description="Citation for case: Bellnier v. Lund">438 F. Supp. 47</a></span> (NDNY 1977); <em>M. </em>v. <em>Board of Ed. Ball-Chatham Community Unit School Dist. No. <span class="citation" data-id="1554742"><a href="/opinion/1554742/m-ex-rel-r-v-board-of-education-ball-chatham-community-unit-school/" aria-description="Citation for case: M. Ex Rel. R. v. Board of Education Ball-Chatham...">5, supra;</a></span> In re W., </em><span class="citation" data-id="2122374"><a href="/opinion/2122374/beckley-v-christopher-w/" aria-description="Citation for case: Beckley v. Christopher W.">29 Cal. App. 3d 777</a></span>, <span class="citation" data-id="2122374"><a href="/opinion/2122374/beckley-v-christopher-w/" aria-description="Citation for case: Beckley v. Christopher W.">105 Cal. Rptr. 775</a></span> (1973); <em>State </em>v. <em>Baccino, </em><span class="citation" data-id="1969621"><a href="/opinion/1969621/state-v-baccino/" aria-description="Citation for case: State v. Baccino">282 A. 2d 869</a></span> (Del. Super. 1971); <em>State </em>v. <em>D. T. W., </em><span class="citation" data-id="7523311"><a href="/opinion/7593883/state-v-dtw/" aria-description="Citation for case: State v. D.T.W.">425 So. 2d 1383</a></span> (Fla. App. 1983); <em>State </em>v. <em><span class="citation" data-id="9616519"><a href="/opinion/1391108/state-v-young/" aria-description="Citation for case: State v. Young">Young, supra;</a></span> In re J. </em>A., <span class="citation multiple-matches"><a href="/c/Ill.%20App.%203d/85/567/">85 Ill. App. 3d 567</a></span>, <span class="citation multiple-matches"><a href="/c/N.%20E.%202d/406/958/">406 N. E. 2d 958</a></span> (1980); <em>People </em>v. <em>Ward, </em><span class="citation" data-id="2183546"><a href="/opinion/2183546/people-v-ward/" aria-description="Citation for case: People v. Ward">62 Mich. App. 46</a></span>, <span class="citation" data-id="2183546"><a href="/opinion/2183546/people-v-ward/" aria-description="Citation for case: People v. Ward">233 N. W. 2d 180</a></span> (1975); <em>Doe </em>v. <em>State, </em>88 N. M. 347, <span class="citation" data-id="1304814"><a href="/opinion/1304814/doe-v-state/" aria-description="Citation for case: Doe v. State">540 P. 2d 827</a></span> (App. 1975); <em>People </em>v. <em>D., </em>34 N. Y. 2d 483, <span class="citation" data-id="5528818"><a href="/opinion/5680501/people-v-scott-d/" aria-description="Citation for case: People v. Scott D.">315 N. E. 2d 466</a></span> (1974); <em>State </em>v. <em>McKinnon, </em><span class="citation" data-id="9623173"><a href="/opinion/1406903/state-v-mckinnon/" aria-description="Citation for case: State v. McKinnon">88 Wash. 2d 75</a></span>, <span class="citation" data-id="9623173"><a href="/opinion/1406903/state-v-mckinnon/" aria-description="Citation for case: State v. McKinnon">558 P. 2d 781</a></span> (1977); <em>In re L. L., </em><span class="citation" data-id="1900299"><a href="/opinion/1900299/interest-of-l-l-v-circuit-court-of-washington-county/" aria-description="Citation for case: Interest of L. L. v. Circuit Court of Washington County">90 Wis. 2d 585</a></span>, <span class="citation" data-id="1900299"><a href="/opinion/1900299/interest-of-l-l-v-circuit-court-of-washington-county/" aria-description="Citation for case: Interest of L. L. v. Circuit Court of Washington County">280 N. W. 2d 343</a></span> (App. 1979).</p>
<p id="b475-8">Although few have considered the matter, courts have also split over whether the exclusionary rule is an appropriate remedy for Fourth Amendment violations committed by school authorities. The Georgia courts have held that although the Fourth Amendment applies to the schools, the exclusionary rule does not. See, <em>e. g., State </em>v. <em><span class="citation" data-id="9616519"><a href="/opinion/1391108/state-v-young/" aria-description="Citation for case: State v. Young">Young, supra;</a></span> State </em>v. <em>Lamb, </em><span class="citation" data-id="1292717"><a href="/opinion/1292717/state-v-lamb/" aria-description="Citation for case: State v. Lamb">137 Ga. App. 437</a></span>, <span class="citation" data-id="1292717"><a href="/opinion/1292717/state-v-lamb/" aria-description="Citation for case: State v. Lamb">224 S. E. 2d 51</a></span> (1976). Other jurisdictions have applied the rule to exclude the fruits of unlawful school searches from criminal trials and delinquency proceedings. See <em>State </em>v. <em>Mora, supra; People </em>v. <em>D., supra.</em></p>
</footnote>
<footnote label="3">
<p id="b475-9"> In holding that the search of T. L. O.’s purse did not violate the Fourth Amendment, we do not implicitly determine that the exclusionary rule applies to the fruits of unlawful searches conducted by school authorities. . The question whether evidence should be excluded from a criminal proceeding involves two discrete inquiries: whether the evidence was seized in violation of the Fourth Amendment, and whether the exclusionary rule is the appropriate remedy for the violation. Neither question'is logically antecedent to the other, for a negative answer to either question is sufficient to dispose of the case. Thus, our determination that the search at issue in this case did not violate the Fourth Amendment implies no particular resolution of the question of the applicability of the exclusionary rule.</p>
</footnote>
<footnote label="4">
<p id="b476-7"> Cf. <em>Ingraham </em>v. <em>Wright, </em><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">430 U. S. 651</a></span> (1977) (holding that the Eighth Amendment’s prohibition of cruel and unusual punishment applies only to <page-number citation-index="1" label="335">*335</page-number>punishments imposed after criminal convictions and hence does not apply to the punishment of schoolchildren by public school officials).</p>
</footnote>
<footnote label="5">
<p id="b479-8"> We do not address the question, not presented by this case, whether a schoolchild has a legitimate expectation of privacy in lockers, desks, or other school property provided for the storage of school supplies. Nor do we express any opinion on the standards (if any) governing searches of such areas by school officials or by other public authorities acting at the request of school officials. Compare <em>Zamora </em>v. <em>Pomeroy, </em><span class="citation multiple-matches"><a href="/c/F.%202d/639/662/">639 F. 2d 662</a></span>, 670 (CA10 1981) (“Inasmuch as the school had assumed joint control of the locker it cannot be successfully maintained that the school did not have a right to inspect it”), and <em>People </em>v. <em>Overton, </em>24 N. Y. 2d 522, <span class="citation" data-id="5524876"><a href="/opinion/5677061/people-v-overton/" aria-description="Citation for case: People v. Overton">249 N. E. 2d 366</a></span> (1969) (school administrators have power to consent to search of a <page-number citation-index="1" label="338">*338</page-number>student’s locker), with <em>State </em>v. <em>Engerud, </em>94 N. J. 331, 348, <span class="citation" data-id="7305116"><a href="/opinion/7386217/state-v-engerud/#943" aria-description="Citation for case: State v. Engerud">463 A. 2d 934, 943</a></span> (1983) (“We are satisfied that in the context of this case the student had an expectation of privacy in the contents of his locker. . . . For the four years of high school, the school locker is a home away from home. In it the student stores the kind of personal ‘effects’ protected by the Fourth Amendment”).</p>
</footnote>
<footnote label="6">
<p id="b483-6"> See eases cited in n. 2, <em>supra.</em></p>
</footnote>
<footnote label="7">
<p id="b483-7"> We here consider only searches carried out by school authorities acting alone and on their own authority. This case does not present the question of the appropriate standard for assessing the legality of searches conducted by school officials in conjunction with or at the behest of law enforcement agencies, and we express no opinion on that question. Cf. <em>Picha </em>v. <em>Wielgos, </em><span class="citation" data-id="2308367"><a href="/opinion/2308367/picha-v-wielgos/#1219" aria-description="Citation for case: Picha v. Wielgos">410 F. Supp. 1214, 1219-1221</a></span> (ND Ill. 1976) (holding probable-cause standard applicable to searches involving the police).</p>
</footnote>
<footnote label="8">
<p id="b484-6"> We do not decide whether individualized suspicion is an essential element of the reasonableness standard we adopt for searches by school authorities. In other contexts, however, we have held that although “some quantum of individualized suspicion is usually a prerequisite to a constitutional search or seizure[,]. . . the Fourth Amendment imposes no irreducible requirement of such suspicion.” <em>United States </em>v. <em>Martinez-</em>Fuerte, <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#560" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 560-561</a></span> (1976). See also <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967). Exceptions to the requirement of individualized suspicion are generally appropriate only where the privacy interests implicated by a search are minimal and where “other safeguards” are available “to assure that the individual’s reasonable expectation of privacy is not ‘subject to the discretion of the official in the field.’” <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654-655</a></span> (1979) (citation omitted). Because the search of T. L. O.’s purse was based upon an individualized suspicion that she had violated school rules, see <em>infra, </em>at 343-347, we need not consider the circumstances that might justify school authorities in conducting searches unsupported by individualized suspicion.</p>
</footnote>
<footnote label="9">
<p id="b484-7"> Our reference to the nature of the infraction is not intended as an endorsement of Justice Stevens’ suggestion that some rules regarding student conduct are by nature too “trivial” to justify a search based upon reasonable suspicion. See <em>post, </em>at 377-382. We are unwilling to adopt a standard under which the legality of a search is dependent upon a judge’s evaluation of the relative importance of various school rules. The maintenance of discipline in the schools requires not only that students be restrained from assaulting one another, abusing drugs and alcohol, and committing other crimes, but also that students conform themselves to the standards of conduct prescribed by school authorities. We have “repeatedly emphasized the need for affirming the comprehensive authority of the States and of school officials, consistent with fundamental constitutional safeguards, to prescribe and control conduct in the schools.” <em>Tinker </em>v. <em>Des Moines Independent Community School District, </em><span class="citation" data-id="9423907"><a href="/opinion/107841/tinker-v-des-moines-independent-community-school-district/#507" aria-description="Citation for case: Tinker v. Des Moines Independent Community School District">393 U. S. 503, 507</a></span> <page-number citation-index="1" label="343">*343</page-number>(1969). The promulgation of a rule forbidding specified conduct presumably reflects a judgment on the part of school officials that such conduct is destructive of school order or of a proper educational environment. Absent any suggestion that the rule violates some substantive constitutional guarantee, the courts should, as a general matter, defer to that judgment and refrain from attempting to distinguish between rules that are important to the preservation of order in the schools and rules that are not.</p>
</footnote>
<footnote label="10">
<p id="b485-9"> Of course, New Jersey may insist on a more demanding standard under its own Constitution or statutes. In that case, its courts would not purport to be applying the Fourth Amendment when they invalidate a search.</p>
</footnote>
<footnote label="11">
<p id="b486-6"> Justice Stevens interprets these statements as a holding that enforcement of the school’s smoking regulations was not sufficiently related to the goal of maintaining discipline or order in the school to justify a search under the standard adopted by the New Jersey court. See <em>post, </em>at 382-384. We do not agree that this is an accurate characterization of the New Jersey Supreme Court’s opinion. The New Jersey court did not hold that the school’s smoking rules were unrelated to the goal of maintaining discipline or order, nor did it suggest that a search that would produce evidence bearing directly on an accusation that a student had violated the smoking rules would be impermissible under the court’s reasonable-suspicion standard; rather, the court concluded that any evidence a search of T. L. O.’s purse was likely to produce would not have a sufficiently direct bearing on the infraction to justify a search — a conclusion with which we cannot agree for the reasons set forth <em>infra, </em>at 345. Justice Stevens’ suggestion that the New Jersey Supreme Court’s decision rested on the perceived triviality of the smoking infraction appears to be a reflection of his own views rather than those of the New Jersey court.</p>
</footnote>
<footnote label="12">
<p id="b488-5"> T. L. O. contends that even if it was reasonable for Mr. Choplick to open her purse to look for cigarettes, it was not reasonable for him to reach in and take the cigarettes out of her purse once he found them. Had he not removed the cigarettes from the purse, she asserts, he would not have observed the rolling papers that suggested the presence of marihuana, and the search for marihuana could not have taken place. T. L. O.’s argument is based on the fact that the cigarettes were not “contraband,” as no school rule forbade her to have them. Thus, according to T. L. 0., the cigarettes were not subject to seizure or confiscation by school authorities, and Mr. Choplick was not entitled to take them out of T. L. O.’s purse regardless of whether he was entitled to peer into the purse to see if they were there. Such hairsplitting argumentation has no place in an inquiry addressed to the issue of reasonableness. If Mr. Choplick could permissibly search T. L. O.’s purse for cigarettes, it hardly seems reasonable to suggest that his natural reaction to finding them — picking them up — could <page-number citation-index="1" label="347">*347</page-number>be a constitutional violation. We find that neither in opening the purse nor in reaching into it to remove the cigarettes did Mr. Choplick violate the Fourth Amendment.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/New York v. Belton.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "New York v. Belton"
type: case
citation: "453 U.S. 454 (1981)"
parallel_cite: "101 S. Ct. 2860; 69 L. Ed. 2d 768"
neutral_cite: 1981 U.S. LEXIS 13
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1981
date_decided: 1981-09-23
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 2026-06-30
  as_of_treatment: 2026-06-30
  composite_basis: principal-holding
  composite_basis_ref: search.vehicle.sia-recent-occupant
  varies_by_point: true
  scope_note: "Composite reflects the principal holding; the vehicle-search point is superseded by Arizona v. Gant (2009) — Belton's container rule survives within Gant's narrowed framework."
  point_overrides:
    - point: search.vehicle.sia-recent-occupant
      point_label: "Vehicle search incident to a recent occupant's arrest"
      field_i_validity: superseded
      as_of_treatment: 2026-06-30
      s3_binding_status: bound
      by:
        - name: Arizona v. Gant
          cluster_id: 145887
          cite: 556 U.S. 332
          field_ii: limited
      scope_note: "The automatic passenger-compartment rule is replaced by Gant's two-justification test."
lake:
  record_id: New York v. Belton
  status: verified
  projected_at: 2026-07-06
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110559/new-york-v-belton/"
  cluster_id: 110559
  opinion_id: 9428488
  identity_checked: true
homes:
  - page: "[[SIA Vehicles]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Traffic Stops]]"
    role: "Related (cross-doctrine)"
related: ["[[Arizona v. Gant]]", "[[Chimel v. California]]", "[[Thornton v. United States]]", "[[Davis v. United States (2011)|Davis v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "automobile", "vehicle-search"]
holding: "Defines the SCOPE of a vehicle search incident to arrest: on a lawful custodial arrest of a vehicle occupant, police may search the…"
---

# New York v. Belton

*453 U.S. 454 (1981)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **Caution — varies by point**
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A police officer stopped a speeding car with four occupants, smelled marijuana, and saw an envelope he associated with marijuana. He ordered the occupants out, arrested all four, and searched the passenger compartment, finding cocaine in the zipped pocket of Belton's jacket on the back seat.

## Issue
What is the permissible scope of a search of an automobile's passenger compartment incident to the lawful custodial arrest of an occupant.

## Rule
The Court adopted a [[Common Legal Terms#bright-line-rule|bright-line rule]]: "when a policeman has made a lawful custodial arrest of the occupant of an automobile, he may, as a contemporaneous incident of that arrest, search the passenger compartment of that automobile." — 453 U.S. at 460. ^pin-460

"It follows from this conclusion that the police may also examine the contents of any containers found within the passenger compartment." — *Id.* ^pin-460b

**This bright-line authority was later limited by [[Arizona v. Gant]]** as applied to vehicle [[Search Incident to Arrest|searches incident to arrest]] (see Treatment).

## Application
Because the officer had made lawful custodial arrests of the car's occupants, he was entitled to search the passenger compartment as a contemporaneous incident of those arrests, including the zipped pocket of the jacket on the back seat. On these facts the cocaine was the product of a lawful [[Search Incident to Arrest|search incident to arrest]].

## Conclusion
The search of the jacket was a lawful [[Search Incident to Arrest|search incident to arrest]]; the New York Court of Appeals' suppression order was reversed.

## Treatment & subsequent history

**Composite: Caution — treatment varies by point.** *Belton* is not simply "good" or "bad" law; its validity depends on which point you rely on.

| Point of law | Status | Controlling authority |
|---|---|---|
| Vehicle search incident to a recent occupant's arrest | **Superseded** | *[[Arizona v. Gant]]*, 556 U.S. 332 (2009) — the automatic passenger-compartment rule is replaced by *[[Arizona v. Gant\|Gant]]*'s two-justification test |
| Containers within the passenger compartment (within a lawful search) | **Good law** | *Belton*'s container rule survives inside *[[Arizona v. Gant\|Gant]]*'s narrowed framework |

*[[Arizona v. Gant|Gant]]* rejected the broad reading of *Belton* that authorized an automatic passenger-compartment search whenever an occupant was arrested. After *[[Arizona v. Gant|Gant]]*, a vehicle [[Search Incident to Arrest|search incident to arrest]] is permissible only if the arrestee is within reaching distance of the passenger compartment at the time of the search, or it is reasonable to believe the vehicle contains evidence of the offense of arrest. Officers' reasonable pre-*[[Arizona v. Gant|Gant]]* reliance on *Belton* was addressed in [[Davis v. United States (2011)|Davis v. United States]].

## Appears on
- [[SIA Vehicles]] — *Key — Progeny / Refinement*
- [[Traffic Stops]] — *Related (cross-doctrine)*

## Sources
- *New York v. Belton*, 453 U.S. 454 (1981) — https://www.courtlistener.com/opinion/110559/new-york-v-belton/ — pinpoint: 460.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9f930906d914185d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "New York v. Belton"}, "payload": {"all": [{"cite": "453 U.S. 454", "page": "454", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "453"}, {"cite": "101 S. Ct. 2860", "page": "2860", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "101"}, {"cite": "69 L. Ed. 2d 768", "page": "768", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "69"}, {"cite": "1981 U.S. LEXIS 13", "page": "13", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1981"}], "display": "453 U.S. 454", "official": {"cite": "453 U.S. 454", "page": "454", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "453"}, "official_selection_present": true, "record_id": "New York v. Belton"}}
{"assertion_id": "c94712e2e6980829", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-460", "record_id": "New York v. Belton"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-460", "pinpoint_status": "slip-only", "quote": "--- # New York v. Belton *453 U.S. 454 (1981)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **Caution — varies by point** <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A police officer stopped a speeding car with four occupants, smelled marijuana, and saw an envelope he associated with marijuana. He ordered the occupants out, arrested all four, and searched the passenger compartment, finding cocaine in the zipped pocket of Belton's jacket on the back seat. ## Issue What is the permissible scope of a search of an automobile's passenger compartment incident to the lawful custodial arrest of an occupant. ## Rule The Court adopted a bright-line rule:", "quote_fidelity": "mismatch", "record_id": "New York v. Belton", "star_marker": null}}
{"assertion_id": "e50d5458b37720dd", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-460b", "record_id": "New York v. Belton"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-460b", "pinpoint_status": "slip-only", "quote": "It follows from this conclusion that the police may also examine the contents of any containers found within the passenger compartment.", "quote_fidelity": "mismatch", "record_id": "New York v. Belton", "star_marker": null}}
{"assertion_id": "acb94106fc91e05c", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "New York v. Belton"}, "payload": {"as_of_content": "2026-06-30", "as_of_treatment": "2026-06-30", "field_i_validity": "caution", "record_id": "New York v. Belton", "scope_note": "Composite reflects the principal holding; the vehicle-search point is superseded by Arizona v. Gant (2009) — Belton's container rule survives within Gant's narrowed framework.", "varies_by_point": true}}
```

### lake record — New York v. Belton

```json
{
  "schema_version": "s2.v1",
  "record_id": "New York v. Belton",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "New York v. Belton",
    "case_name_short": "Belton",
    "case_name_full": "New York v. Belton",
    "input_case_name": "New York v. Belton",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1981-09-23",
    "year": 1981,
    "docket": null,
    "cluster_id": 110559,
    "lead_opinion_id": 9428488,
    "sibling_ids": [
      110559,
      9428488,
      9428489,
      9428490,
      9428491,
      9428492
    ],
    "absolute_url": "/opinion/110559/new-york-v-belton/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9031723,
        "score": 20,
        "case_name": "New York v. Belton"
      },
      {
        "cluster_id": 9030420,
        "score": 20,
        "case_name": "New York v. Belton"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "453 U.S. 454",
      "volume": "453",
      "reporter": "U.S.",
      "page": "454",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "101 S. Ct. 2860",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "2860",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 2d 768",
        "volume": "69",
        "reporter": "L. Ed. 2d",
        "page": "768",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1981 U.S. LEXIS 13",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "13",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "453 U.S. 454",
        "volume": "453",
        "reporter": "U.S.",
        "page": "454",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 S. Ct. 2860",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "2860",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 2d 768",
        "volume": "69",
        "reporter": "L. Ed. 2d",
        "page": "768",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1981 U.S. LEXIS 13",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "13",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "453 U.S. 454",
    "official_selection": {
      "court_class": "scotus",
      "selected": "453 U.S. 454",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-460",
      "page": null,
      "quote": "--- # New York v. Belton *453 U.S. 454 (1981)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **Caution \u2014 varies by point** <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A police officer stopped a speeding car with four occupants, smelled marijuana, and saw an envelope he associated with marijuana. He ordered the occupants out, arrested all four, and searched the passenger compartment, finding cocaine in the zipped pocket of Belton's jacket on the back seat. ## Issue What is the permissible scope of a search of an automobile's passenger compartment incident to the lawful custodial arrest of an occupant. ## Rule The Court adopted a bright-line rule:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-460b",
      "page": null,
      "quote": "It follows from this conclusion that the police may also examine the contents of any containers found within the passenger compartment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "2026-06-30",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "principal-holding",
    "composite_basis_ref": "search.vehicle.sia-recent-occupant",
    "varies_by_point": true,
    "scope_note": "Composite reflects the principal holding; the vehicle-search point is superseded by Arizona v. Gant (2009) \u2014 Belton's container rule survives within Gant's narrowed framework.",
    "point_overrides": [
      {
        "point": "search.vehicle.sia-recent-occupant",
        "point_label": "Vehicle search incident to a recent occupant's arrest",
        "field_i_validity": "superseded",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "bound",
        "by": [
          {
            "name": "Arizona v. Gant",
            "cluster_id": 145887,
            "cite": "556 U.S. 332",
            "field_ii": "limited"
          }
        ],
        "scope_note": "The automatic passenger-compartment rule is replaced by Gant's two-justification test."
      }
    ],
    "edges": [
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
        "journal_ref": "New York v. Belton:lane1_negative"
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
        "journal_ref": "New York v. Belton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ramos v. Louisiana",
          "cluster_id": 9231323,
          "cite": [
            "140 S. Ct. 1390",
            "206 L. Ed. 2d 583"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andre Anderson v. State of Indiana",
          "cluster_id": 4327181,
          "cite": [
            "64 N.E.3d 903",
            "2016 Ind. App. LEXIS 432",
            "2016 WL 7078344"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane1_negative"
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
        "journal_ref": "New York v. Belton:lane1_negative"
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
        "journal_ref": "New York v. Belton:lane1_negative"
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
        "journal_ref": "New York v. Belton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jermaine Lebron v. State of Florida",
          "cluster_id": 2686855,
          "cite": [
            "135 So. 3d 1040",
            "39 Fla. L. Weekly Supp. 62",
            "2014 WL 321817",
            "2014 Fla. LEXIS 376"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane1_negative"
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
        "journal_ref": "New York v. Belton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Isaac Andrew Baldon III",
          "cluster_id": 4472245,
          "cite": [
            "829 N.W.2d 785",
            "2013 WL 1694553",
            "2013 Iowa Sup. LEXIS 42"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gary Lynn Patton v. State",
          "cluster_id": 3128917,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane1_negative"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Long",
          "cluster_id": 111020,
          "cite": [
            "77 L. Ed. 2d 1201",
            "103 S. Ct. 3469",
            "463 U.S. 1032",
            "1983 U.S. LEXIS 7",
            "51 U.S.L.W. 5231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Wilson",
          "cluster_id": 118086,
          "cite": [
            "137 L. Ed. 2d 41",
            "117 S. Ct. 882",
            "519 U.S. 408",
            "1997 U.S. LEXIS 1271"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Greenwood",
          "cluster_id": 112067,
          "cite": [
            "100 L. Ed. 2d 30",
            "108 S. Ct. 1625",
            "486 U.S. 35",
            "1988 U.S. LEXIS 2279",
            "56 U.S.L.W. 4409"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Class",
          "cluster_id": 111600,
          "cite": [
            "89 L. Ed. 2d 81",
            "106 S. Ct. 960",
            "475 U.S. 106",
            "1986 U.S. LEXIS 5",
            "54 U.S.L.W. 4178"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Square",
          "cluster_id": 1827528,
          "cite": [
            "433 So. 2d 104"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florence v. Board of Chosen Freeholders of County of Burlington",
          "cluster_id": 626454,
          "cite": [
            "182 L. Ed. 2d 566",
            "132 S. Ct. 1510",
            "566 U.S. 318",
            "2012 U.S. LEXIS 2712"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Archer v. Commonwealth",
          "cluster_id": 1067256,
          "cite": [
            "492 S.E.2d 826",
            "26 Va. App. 1",
            "1997 Va. App. LEXIS 683"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane2_top_cited"
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
        "journal_ref": "New York v. Belton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Montejo v. Louisiana",
          "cluster_id": 145873,
          "cite": [
            "173 L. Ed. 2d 955",
            "129 S. Ct. 2079",
            "556 U.S. 778",
            "2009 U.S. LEXIS 3973"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Belton:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110559 OR 9428488 OR 9428489 OR 9428490 OR 9428491 OR 9428492) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjk3ODE0NDAwMDAwJnM9MzEyODkxNyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110559+OR+9428488+OR+9428489+OR+9428490+OR+9428491+OR+9428492%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110559 OR 9428488 OR 9428489 OR 9428490 OR 9428491 OR 9428492)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNzYmcz0zMDA2NDExJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110559+OR+9428488+OR+9428489+OR+9428490+OR+9428491+OR+9428492%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110559 OR 9428488 OR 9428489 OR 9428490 OR 9428491 OR 9428492)",
        "reviewed": 27,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 27,
        "triage_read": 1,
        "triage_snippet_classified": 26
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110559 OR 9428488 OR 9428489 OR 9428490 OR 9428491 OR 9428492)",
    "indexed_citing_opinions": 2230,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110559,
        "count": 2032,
        "count_source": "search"
      },
      {
        "opinion_id": 9428488,
        "count": 238,
        "count_source": "search"
      },
      {
        "opinion_id": 9428489,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428490,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428491,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428492,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3483,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/new-york-v-belton.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4NTY0NTkmcz05NjkxMjk4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110559+OR+9428488+OR+9428489+OR+9428490+OR+9428491+OR+9428492%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110559,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 107982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 108894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 108995,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 109196,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 347138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 382105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 382713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 382715,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 1391930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110559,
        "cited_id": 1687668,
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
    "date_created": "2026-07-05T15:31:51Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "pre-seeded new-schema treatment (planning-time projection); R6 derivation to confirm",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:32:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "pre-seeded new-schema treatment (planning-time projection); R6 derivation to confirm",
        "at": "2026-07-05T15:32:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:32:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — New York v. Belton

```
<opinion type="majority">
<author id="b497-8">Justice Stewart</author>
<p id="AyB">delivered the opinion of the Court.</p>
<p id="b497-9">When the occupant of an automobile is subjected to a lawful custodial arrest, does the constitutionally permissible scope of a search incident to his arrest include the passenger compartment of the automobile in which he was riding? That is the question at issue in the present case.</p>
<p id="b497-10">I</p>
<p id="b497-11">On April 9, 1978, Trooper Douglas Nicot, a New York State policeman driving an unmarked car on the New York Thruway, was passed by another automobile traveling at an excessive rate of speed. Nicot gave chase, overtook the speeding vehicle, and ordered its driver to pull it over to the side of the road and stop. There were four men in the car, one of whom was Roger Belton, the respondent in this case. The policeman asked to see the driver’s license and automobile registration, and discovered that none of the men owned the vehicle or was related to its owner. Meanwhile, the policeman had smelled burnt marihuana and had seen on <page-number citation-index="1" label="456">*456</page-number>the floor of the car an envelope marked “Supergold” that he associated with marihuana. He therefore directed the men to get out of the car, and placed them under arrest for the unlawful possession of marihuana. He patted down each of the men and “split them up into four separate areas of the Thruway at this time so they would not be in physical touching area of each other.” He then picked up the envelope marked “Supergold” and found that it contained marihuana. After giving the arrestees the warnings required by <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, the state policeman searched each one of them. He then searched the passenger compartment of the car. On the back seat he found a black leather jacket belonging to Belton. He unzipped one of the pockets of the jacket and discovered cocaine. Placing the jacket in his automobile, he drove the four arrestees to a nearby police station.</p>
<p id="b498-5">Belton was subsequently indicted for criminal possession of a controlled substance. In the trial court he moved that the cocaine the trooper had seized from the jacket pocket be suppressed. The court denied the motion. Belton then pleaded guilty to a lesser included offense, but preserved his claim that the cocaine had been seized in violation of the Fourth and Fourteenth Amendments. See <em>Lefkowitz </em>v. <em>Newsome, </em><span class="citation" data-id="9426003"><a href="/opinion/109196/lefkowitz-v-newsome/" aria-description="Citation for case: Lefkowitz v. Newsome">420 U. S. 283</a></span>. The Appellate Division of the New York Supreme Court upheld the constitutionality of the search and seizure, reasoning that “[o]nce defendant was validly arrested for possession of marihuana, the officer was justified in searching the immediate area for other contraband.” 68 App. Div. 2d 198, 201, 416 N. Y. S. 2d 922, 926.</p>
<p id="b498-6">The New York Court of Appeals reversed, holding that “[a] warrantless search of the zippered pockets of an unacces-sible jacket may not be upheld as a search incident to a lawful arrest where there is no longer any danger that the arrestee or a confederate might gain access to the article.” 60 N. Y. 2d 447, 449, <span class="citation" data-id="5533089"><a href="/opinion/5684296/people-v-belton/#421" aria-description="Citation for case: People v. Belton">407 N. E. 2d 420, 421</a></span>. Two judges dis<page-number citation-index="1" label="457">*457</page-number>sented. They pointed out that the “search was conducted by a lone peace officer who was in the process of arresting four unknown individuals whom he had stopped in a speeding car owned by none of them and apparently containing an uncertain quantity of a controlled substance. The suspects were standing by the side of the car as the officer gave it a quick check to confirm his suspicions before attempting to transport them to police headquarters . . . <span class="citation" data-id="5533089"><a href="/opinion/5684296/people-v-belton/#454" aria-description="Citation for case: People v. Belton"><em>Id., </em>at 454</a></span>, <span class="citation" data-id="5533089"><a href="/opinion/5684296/people-v-belton/#424" aria-description="Citation for case: People v. Belton">407 N. E. 2d, at 424</a></span>. We granted certiorari to consider the constitutionally permissible scope of a search in circumstances such as these. <span class="citation multiple-matches"><a href="/c/U.%20S./449/1109/">449 U. S. 1109</a></span>.</p>
<p id="b499-4">II</p>
<p id="b499-5">It is a first principle of Fourth Amendment jurisprudence that the police may not conduct a search unless they first convince a neutral magistrate that there is probable cause to do so. This Court has recognized, however, that “the exigencies of the situation” may sometimes make exemption from the warrant requirement “imperative.” <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#456" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 456</a></span>. Specifically, the Court held in <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span>, that a lawful custodial arrest creates a situation which justifies the contemporaneous search without a warrant of the person arrested and of the immediately surrounding area. Such searches have long been considered valid because of the need “to remove any weapons that [the arrestee] might seek to use in order to resist arrest or effect his escape” and the need to prevent the concealment or destruction of evidence. <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California"><em>Id., </em>at 763</a></span>.</p>
<p id="b499-6">The Court’s opinion in <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>emphasized the principle that, as the Court had said in <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19</a></span>, “[t]he scope of [a] search must be 'strictly tied to and justified by’ the circumstances which rendered its initiation permissible.” Quoted in <em>Chimel </em>v. <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#762" aria-description="Citation for case: Chimel v. California"><em>California, supra, </em>at 762</a></span>. Thus while the Court in <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>found “ample justification” for a search of “the area from within which [an arrestee] <page-number citation-index="1" label="458">*458</page-number>might gain possession of a weapon or destructible evidence,” the Court found “no comparable justification ... for routinely searching any room other than that in which an arrest occurs — or, for that matter, for searching through all the desk drawers or other closed or concealed areas in that room itself.” <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S., at 763</a></span>.</p>
<p id="b500-5">Although the principle that limits a search incident to a lawful custodial arrest may be stated clearly enough, courts have discovered the principle difficult to apply in specific cases. Yet, as one commentator has pointed out, the protection of the Fourth and Fourteenth Amendments “can only be realized if the police are acting under a set of rules which, in most instances, makes it possible to reach a correct determination beforehand as to whether an invasion of privacy is justified in the interest of law enforcement.” LaFave, “Case-By-Case Adjudication” versus “Standardized Procedures”: The Robinson Dilemma, 1974 S. Ct. Rev. 127, 142. This is because</p>
<blockquote id="b500-6">“Fourth Amendment doctrine, given force and effect by the exclusionary rule, is primarily intended to regulate the police in their day-to-day activities and thus ought to be expressed in terms that are readily applicable by the police in the context of the law enforcement activities in which they are necessarily engaged. A highly sophisticated set of rules, qualified by all sorts of ifs, ands, and buts and requiring the drawing of subtle nuances and hairline distinctions, may be the sort of heady stuff upon which the facile minds of lawyers and judges eagerly feed, but they may be 'literally impossible of application by the officer in the field.’ ” <em>Id., </em>at 141.</blockquote>
<p id="b500-7">In short, “[a] single familiar standard is essential to guide police officers, who have only limited time and expertise to reflect on and balance the social and individual interests involved in the specific circumstances they confront.” <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#213" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 213-214</a></span>.</p>
<p id="b501-4"><page-number citation-index="1" label="459">*459</page-number>So it was that, in <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span>, the Court hewed to a straightforward rule, easily applied, and predictably enforced: “[I]n the case of a lawful custodial arrest a full search of the person is not only an exception to the warrant requirement of the Fourth Amendment, but is also a 'reasonable’ search under that Amendment.” <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#235" aria-description="Citation for case: United States v. Robinson"><em>Id., </em>at 235</a></span>. In so holding, the Court rejected the suggestion that “there must be litigated in each case the issue of whether or not there was present one of the reasons supporting the authority for a search of the person incident to a lawful arrest.” <em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Ibid.</a></span></em></p>
<p id="b501-5">But no straightforward rule has emerged from the litigated cases respecting the question involved here — the question of the proper scope of a search of the interior of an automobile incident to a lawful custodial arrest of its occupants. The difficulty courts have had is reflected in the conflicting views of the New York judges who dealt with the problem in the present case, and is confirmed by a look at even a small sample drawn from the narrow class of cases in which courts have decided whether, in the course of a search incident to the lawful custodial arrest of the occupants of an automobile, police may search inside the automobile after the arrestees are no longer in it. On the one hand, decisions in cases such as <em>United States </em>v. <em>Sanders, </em><span class="citation" data-id="9467153"><a href="/opinion/382713/united-states-v-willard-r-sanders/" aria-description="Citation for case: United States v. Willard R. Sanders">631 F. 2d 1309</a></span> (CA8 1980); <em>United States </em>v. <em>Dixon, </em><span class="citation" data-id="347138"><a href="/opinion/347138/united-states-v-lewis-nathaniel-dixon/" aria-description="Citation for case: United States v. Lewis Nathaniel Dixon">558 F. 2d 919</a></span> (CA9 1977); and <em>United States </em>v. <em>Frick, </em><span class="citation" data-id="9460209"><a href="/opinion/316377/united-states-v-robert-lee-frick-and-quimet-john-petersen/" aria-description="Citation for case: United States v. Robert Lee Frick and Quimet John Petersen">490 F. 2d 666</a></span> (CA5 1973), have upheld such warrantless searches as incident to lawful arrests. On the other hand, in cases such as <em>United States </em>v. <em>Benson, </em><span class="citation" data-id="9467155"><a href="/opinion/382715/united-states-v-jeffrey-joseph-benson/" aria-description="Citation for case: United States v. Jeffrey Joseph Benson">631 F. 2d 1336</a></span> (CA8 1980), and <em>United States </em>v. <em>Rigales, </em><span class="citation" data-id="382105"><a href="/opinion/382105/united-states-v-ernesto-g-rigales-jr/" aria-description="Citation for case: United States v. Ernesto G. Rigales, Jr.">630 F. 2d 364</a></span> (CA5 1980), such searches, in comparable factual circumstances, have been held constitutionally invalid.<footnotemark>1</footnotemark></p>
<p id="b501-6">When a person cannot know how a court will apply a <page-number citation-index="1" label="460">*460</page-number>settled principle to a recurring factual situation, that person cannot know the scope of his constitutional protection, nor can a policeman know the scope of his authority. While the <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>case established that a search incident to an arrest may not stray beyond the area within the immediate control of the arrestee, courts have found no workable definition of “the area within the immediate control of the arrestee” when that area arguably includes the interior of an automobile and the arrestee is its recent occupant. Our reading of the cases suggests the generalization that articles inside the relatively narrow compass of the passenger compartment of an automobile are in fact generally, even if not inevitably, within “the area into which an arrestee might reach in order to grab a weapon or evidentiary ite[m].” <em>Chimel, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S., at 763</a></span>. In order to establish the workable rule this category of cases requires, we read Chimel’s definition of the limits of the area that may be searched in light of that generalization. Accordingly, we hold that when a policeman has made a lawful custodial arrest of the occupant of an automobile,<footnotemark>2</footnotemark> he may, as a contemporaneous incident of that arrest, search the passenger compartment of that automobile.<footnotemark>3</footnotemark></p>
<p id="b502-5">It follows from this conclusion that the police may also examine the contents of any containers found within the passenger compartment, for if the passenger compartment is within reach of the arrestee, so also will containers in it be within his reach.<footnotemark>4</footnotemark> <em>United States </em>v. <em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Robinson, supra;</a></span> Draper </em><page-number citation-index="1" label="461">*461</page-number>v. <em>United States, </em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span>. Such a container may, of course, be searched whether it is open or closed, since the justification for the search is not that the arrestee has no privacy interest in the container, but that the lawful custodial arrest justifies the infringement of any privacy interest the arrestee may have. Thus, while the Court in <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>held that the police could not search all the drawers in an arrestee’s house simply because the police had arrested him at home, the Court noted that drawers within an arrestee’s reach could be searched because of the danger their contents might pose to the police. <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S., at 763</a></span>.</p>
<p id="b503-5">It is true, of course, that these containers will sometimes be such that they could hold neither a weapon nor evidence of the criminal conduct for which the suspect was arrested. However, in <em>United States </em>v. <em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Robinson</a></span>, </em>the Court rejected the argument that such a container — there a “crumpled up' cigarette package” — located during a search of Robinson incident to his arrest could not be searched: “The authority to search the person incident to a lawful custodial arrest, while based upon the need to disarm and to discover evidence, does not depend on what a court may later decide was the probability in a particular arrest situation that weapons or evidence would in fact be found upon the person of the suspect. A custodial arrest of a suspect based on probable cause is a reasonable intrusion under the Fourth Amendment; that intrusion being lawful, a search incident to the arrest requires no additional justification.” <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#235" aria-description="Citation for case: United States v. Robinson">414 U. S., at 235</a></span>.</p>
<p id="b503-6">The New York Court of Appeals relied upon <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span>, and <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span>, in concluding that the search and seizure in the present case were constitutionally invalid.<footnotemark>5</footnotemark> But neither of those <page-number citation-index="1" label="462">*462</page-number>cases involved an arguably valid search incident to a lawful custodial arrest. As the Court pointed out in the <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>case: “Here the search was conducted more than an hour after federal agents had gained exclusive control of the footlocker and long after respondents were securely in custody; the search therefore cannot be viewed as incidental to the arrest or as justified by any other exigency.” <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#15" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 15</a></span>. And in the <em>Sanders </em>case, the Court explicitly stated that it did not “consider the constitutionality of searches of luggage incident to the arrest of its possessor. See, <em>e. g., United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973). The State has not argued that respondent’s suitcase was searched incident to his arrest, and it appears that the bag was not within his ‘immediate control’ at the time of the search.” 442 U. S., at 764, n. 11. (The suitcase in question was in the trunk of the taxicab. See n. 4, <em>supra.)</em></p>
<p id="b504-5">Ill</p>
<p id="b504-6">It is not questioned that the respondent was the subject of a lawful custodial arrest on a charge of possessing marihuana. The search of the respondent’s jacket followed immediately upon that arrest. The jacket was located inside the passenger compartment of the car in which the respondent had been a passenger just before he was arrested. The jacket was. thus within the area which we have concluded was “within the arrestee’s immediate control” within the meaning of the <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>case.<footnotemark>6</footnotemark> The search of the jacket, therefore, was a <page-number citation-index="1" label="463">*463</page-number>search incident to a lawful custodial arrest, and it did not violate the Fourth and Fourteenth Amendments. Accordingly, the judgment is reversed.</p>
<p id="b505-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b501-7"> The state-court cases are in similar disarray. Compare, <em>e. g., Hinkel </em>v. <em>Anchorage, </em><span class="citation" data-id="9617077"><a href="/opinion/1391930/hinkel-v-anchorage/" aria-description="Citation for case: Hinkel v. Anchorage">618 P. 2d 1069</a></span> (Alaska 1980), with <em>Ulesky </em>v. <em>State, </em><span class="citation" data-id="1687668"><a href="/opinion/1687668/ulesky-v-state/" aria-description="Citation for case: Ulesky v. State">379 So. 2d 121</a></span> (Fla. App. 1979).</p>
</footnote>
<footnote label="2">
<p id="b502-6"> The validity of the custodial arrest of Belton has not been questioned in this case. Cf. <em>Gustafson </em>v. <em>Florida </em><span class="citation" data-id="9425477"><a href="/opinion/108894/gustafson-v-florida/#266" aria-description="Citation for case: Gustafson v. Florida">414 U. S. 260, 266</a></span> (concurring opinion).</p>
</footnote>
<footnote label="3">
<p id="b502-7"> Our holding today does no more than determine the meaning of Chimel’s principles in this particular and problematic context. It in no way alters the fundamental principles established in the <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>case regarding the basic scope of searches incident to lawful custodial arrests.</p>
</footnote>
<footnote label="4">
<p id="b502-8"> “Container” here denotes any object capable of holding another object. It thus includes closed or open glove compartments, consoles, or other receptacles located anywhere within the passenger compartment, as well as <page-number citation-index="1" label="461">*461</page-number>luggage, boxes, bags, clothing, and the like. Our holding encompasses only the interior of the passenger compartment of an automobile and does not encompass the trunk.</p>
</footnote>
<footnote label="5">
<p id="b503-10"> It seems to have been the theory of the Court of Appeals that the search and seizure in the present case could not have been incident to the <page-number citation-index="1" label="462">*462</page-number>respondent’s arrest, because Trooper Nicot, by the very act of searching the respondent’s jacket and seizing the contents of its pocket, had gained “exclusive control” of them. 50 N. Y. 2d 447, 451, <span class="citation" data-id="5533089"><a href="/opinion/5684296/people-v-belton/#422" aria-description="Citation for case: People v. Belton">407 N. E. 2d 420, 422</a></span>. But under this fallacious theory no search or seizure incident to a lawful custodial arrest would ever be valid; by seizing an article even on the arrestee’s person, an officer may be said to have reduced that article to his “exclusive control.”</p>
</footnote>
<footnote label="6">
<p id="b504-8"> Because of this disposition of the case, there is no need here to consider whether the search and seizure were permissible under the so-called <page-number citation-index="1" label="463">*463</page-number>“automobile exception.” <em>Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span>; <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/New York v. Burger.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "New York v. Burger"
type: case
citation: "482 U.S. 691 (1987)"
parallel_cite: "107 S. Ct. 2636; 96 L. Ed. 2d 601; 55 U.S.L.W. 4890"
neutral_cite: 1987 U.S. LEXIS 2725
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-06-19
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-06-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: New York v. Burger
  varies_by_point: false
  scope_note: "Three-part test for warrantless inspection of closely regulated businesses; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111927/new-york-v-burger/"
  cluster_id: 111927
  opinion_id: 9431050
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Donovan v. Dewey]]", "[[Marshall v. Barlow's, Inc.]]", "[[United States v. Biswell]]", "[[Camara v. Municipal Court]]"]
aliases: []
tags: ["case", "fourth-amendment", "administrative-search", "closely-regulated-business", "inspection"]
holding: "A warrantless administrative inspection of a closely (pervasively) regulated business — here, an automobile junkyard — is reasonable if…"
lake:
  record_id: New York v. Burger
  status: verified
  projected_at: 2026-07-06
---

# New York v. Burger

*482 U.S. 691 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police conducted a warrantless inspection of Burger's automobile junkyard under a New York statute authorizing inspection of vehicle-dismantling businesses. They found stolen vehicles and parts and charged him with possession of stolen property.

## Issue
Whether a warrantless administrative inspection of a closely (pervasively) regulated business is reasonable under the Fourth Amendment.

## Rule
A warrantless inspection of a pervasively regulated business is reasonable only if three criteria are met. "This warrantless inspection, however, even in the context of a pervasively regulated business, will be deemed to be reasonable only so long as three criteria are met. First, there must be a 'substantial' government interest that informs the regulatory scheme pursuant to which the inspection is made." — 482 U.S. at 702. ^pin-702

Second, the warrantless inspections must be necessary to further the regulatory scheme. "Finally, 'the statute's inspection program, in terms of the certainty and regularity of its application, [must] provid[e] a constitutionally adequate substitute for a warrant.'" — *Id.* at 703. ^pin-703

## Application
Junkyards/vehicle-dismantling businesses are closely regulated; New York had a substantial interest in combating automobile theft; warrantless, unannounced inspections were necessary because stolen cars and parts pass quickly through such businesses and surprise is essential to detection; and the statute provided a constitutionally adequate substitute for a warrant by notifying operators that inspections would occur on a regular basis and by limiting inspectors' discretion. The inspection of Burger's junkyard was therefore reasonable.

## Conclusion
The warrantless inspection was constitutional; the New York Court of Appeals' suppression order was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Burger* synthesizes the closely-regulated-business inspection line ([[United States v. Biswell]]; [[Donovan v. Dewey]]) into a three-part test, distinct from the warrant-based regime for ordinary commercial premises in [[Marshall v. Barlow's, Inc.]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *New York v. Burger*, 482 U.S. 691 (1987) — https://www.courtlistener.com/opinion/111927/new-york-v-burger/ — pinpoints: 702, 703.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7d1674d7db68ad9f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "New York v. Burger"}, "payload": {"all": [{"cite": "482 U.S. 691", "page": "691", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "482"}, {"cite": "107 S. Ct. 2636", "page": "2636", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "107"}, {"cite": "96 L. Ed. 2d 601", "page": "601", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "96"}, {"cite": "1987 U.S. LEXIS 2725", "page": "2725", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1987"}, {"cite": "55 U.S.L.W. 4890", "page": "4890", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "55"}], "display": "482 U.S. 691", "official": {"cite": "482 U.S. 691", "page": "691", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "482"}, "official_selection_present": true, "record_id": "New York v. Burger"}}
{"assertion_id": "a2f03751bf2d4f73", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-702", "record_id": "New York v. Burger"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-702", "pinpoint_status": "slip-only", "quote": "--- # New York v. Burger *482 U.S. 691 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police conducted a warrantless inspection of Burger's automobile junkyard under a New York statute authorizing inspection of vehicle-dismantling businesses. They found stolen vehicles and parts and charged him with possession of stolen property. ## Issue Whether a warrantless administrative inspection of a closely (pervasively) regulated business is reasonable under the Fourth Amendment. ## Rule A warrantless inspection of a pervasively regulated business is reasonable only if three criteria are met.", "quote_fidelity": "mismatch", "record_id": "New York v. Burger", "star_marker": null}}
{"assertion_id": "f88a9a240883f6f6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-703", "record_id": "New York v. Burger"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-703", "pinpoint_status": "slip-only", "quote": "Finally, 'the statute's inspection program, in terms of the certainty and regularity of its application, [must] provid[e] a constitutionally adequate substitute for a warrant.'", "quote_fidelity": "mismatch", "record_id": "New York v. Burger", "star_marker": null}}
{"assertion_id": "0c8f5d05be066f4e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "New York v. Burger"}, "payload": {"as_of_content": "1987-06-19", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "New York v. Burger", "scope_note": "Three-part test for warrantless inspection of closely regulated businesses; good law.", "varies_by_point": false}}
```

### lake record — New York v. Burger

```json
{
  "schema_version": "s2.v1",
  "record_id": "New York v. Burger",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "New York v. Burger",
    "case_name_short": "Burger",
    "case_name_full": "New York v. Burger",
    "input_case_name": "New York v. Burger",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-06-19",
    "year": 1987,
    "docket": null,
    "cluster_id": 111927,
    "lead_opinion_id": 9431050,
    "sibling_ids": [
      111927,
      9431050,
      9431051
    ],
    "absolute_url": "/opinion/111927/new-york-v-burger/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "482 U.S. 691",
      "volume": "482",
      "reporter": "U.S.",
      "page": "691",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 2636",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "2636",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 L. Ed. 2d 601",
        "volume": "96",
        "reporter": "L. Ed. 2d",
        "page": "601",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4890",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4890",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 2725",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "2725",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "482 U.S. 691",
        "volume": "482",
        "reporter": "U.S.",
        "page": "691",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 2636",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "2636",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 L. Ed. 2d 601",
        "volume": "96",
        "reporter": "L. Ed. 2d",
        "page": "601",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 2725",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "2725",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4890",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4890",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "482 U.S. 691",
    "official_selection": {
      "court_class": "scotus",
      "selected": "482 U.S. 691",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-702",
      "page": null,
      "quote": "--- # New York v. Burger *482 U.S. 691 (1987)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police conducted a warrantless inspection of Burger's automobile junkyard under a New York statute authorizing inspection of vehicle-dismantling businesses. They found stolen vehicles and parts and charged him with possession of stolen property. ## Issue Whether a warrantless administrative inspection of a closely (pervasively) regulated business is reasonable under the Fourth Amendment. ## Rule A warrantless inspection of a pervasively regulated business is reasonable only if three criteria are met.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-703",
      "page": null,
      "quote": "Finally, 'the statute's inspection program, in terms of the certainty and regularity of its application, [must] provid[e] a constitutionally adequate substitute for a warrant.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-06-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "New York v. Burger",
    "varies_by_point": false,
    "scope_note": "Three-part test for warrantless inspection of closely regulated businesses; good law.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "New York v. Burger:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jonathan Albert Leal v. State",
          "cluster_id": 2751234,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vivid Entertainment, LLC v. Fielding",
          "cluster_id": 8727579,
          "cite": [
            "965 F. Supp. 2d 1113",
            "2013 WL 4451068",
            "2013 U.S. Dist. LEXIS 116731"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ortiz",
          "cluster_id": 8477550,
          "cite": [
            "507 F. App'x 339"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Al-Kidd v. Ashcroft",
          "cluster_id": 1204118,
          "cite": [
            "580 F.3d 949",
            "2009 U.S. App. LEXIS 20000",
            "2009 WL 2836448"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane1_negative"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. Wisconsin",
          "cluster_id": 111959,
          "cite": [
            "97 L. Ed. 2d 709",
            "107 S. Ct. 3164",
            "483 U.S. 868",
            "1987 U.S. LEXIS 2897",
            "55 U.S.L.W. 5156"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Waters v. Churchill",
          "cluster_id": 1087950,
          "cite": [
            "128 L. Ed. 2d 686",
            "114 S. Ct. 1878",
            "511 U.S. 661",
            "1994 U.S. LEXIS 4104"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dolan v. City of Tigard",
          "cluster_id": 117861,
          "cite": [
            "129 L. Ed. 2d 304",
            "114 S. Ct. 2309",
            "512 U.S. 374",
            "1994 U.S. LEXIS 4826"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Verdugo-Urquidez",
          "cluster_id": 112382,
          "cite": [
            "108 L. Ed. 2d 222",
            "110 S. Ct. 1056",
            "494 U.S. 259",
            "1990 U.S. LEXIS 1175",
            "1990 WL 16772"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robinson",
          "cluster_id": 2140668,
          "cite": [
            "767 N.E.2d 638",
            "97 N.Y.2d 341",
            "741 N.Y.S.2d 147"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garcia v. State",
          "cluster_id": 2428168,
          "cite": [
            "827 S.W.2d 937",
            "1992 Tex. Crim. App. LEXIS 83",
            "1992 WL 61756"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carlos Botero-Ospina",
          "cluster_id": 709242,
          "cite": [
            "71 F.3d 783",
            "1995 U.S. App. LEXIS 34347",
            "1995 WL 723102"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cecil Ferguson",
          "cluster_id": 656143,
          "cite": [
            "8 F.3d 385",
            "1993 U.S. App. LEXIS 28306",
            "1993 WL 437691"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Segundo v. State",
          "cluster_id": 1590541,
          "cite": [
            "270 S.W.3d 79",
            "2008 Tex. Crim. App. LEXIS 1505",
            "2008 WL 4724093"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mitchell",
          "cluster_id": 168153,
          "cite": [
            "518 F.3d 740",
            "69 Fed. R. Serv. 3d 1713",
            "2008 U.S. App. LEXIS 4505",
            "2008 WL 542130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spinelli v. City of New York",
          "cluster_id": 2490,
          "cite": [
            "579 F.3d 160",
            "2009 U.S. App. LEXIS 17640",
            "2009 WL 2413929"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ronald Calzone v. Josh Hawley",
          "cluster_id": 4416575,
          "cite": [
            "866 F.3d 866",
            "2017 WL 3366519",
            "2017 U.S. App. LEXIS 14476"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Santikos v. State",
          "cluster_id": 1653416,
          "cite": [
            "836 S.W.2d 631",
            "1992 Tex. Crim. App. LEXIS 131",
            "1992 WL 116096"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Burger:lane2_top_cited"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
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
        "journal_ref": "New York v. Burger:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111927 OR 9431050 OR 9431051) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTU4NjI0MDAwMDAwJnM9Nzk1ODY3JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111927+OR+9431050+OR+9431051%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111927 OR 9431050 OR 9431051)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzImcz0yODEwNTI0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111927+OR+9431050+OR+9431051%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111927 OR 9431050 OR 9431051)",
        "reviewed": 25,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 25,
        "triage_read": 0,
        "triage_snippet_classified": 25
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111927 OR 9431050 OR 9431051)",
    "indexed_citing_opinions": 691,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111927,
        "count": 608,
        "count_source": "search"
      },
      {
        "opinion_id": 9431050,
        "count": 111,
        "count_source": "search"
      },
      {
        "opinion_id": 9431051,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1073,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/new-york-v-burger.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxNjU0ODUmcz0xMDMxNDM4MCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111927+OR+9431050+OR+9431051%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111927,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 110530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 111835,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 317754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 427553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 1108128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 1244252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 1382601,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 1557646,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 1601166,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 2024330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 2102923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 2123138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 2123937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 2583761,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111927,
        "cited_id": 3778084,
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
    "date_created": "2026-07-05T15:36:22Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:36:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:36:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:38:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:36:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — New York v. Burger

```
<opinion type="majority">
<author id="b731-6">Justice Blackmun</author>
<p id="ANB">delivered the opinion of the Court.</p>
<p id="b731-7">This case presents the question whether the warrantless search of an automobile junkyard, conducted pursuant to a statute authorizing such a search, falls within the exception to the warrant requirement for administrative inspections of pervasively regulated industries. The case also presents the question whether an otherwise proper administrative inspection is unconstitutional because the ultimate purpose of the regulatory statute pursuant to which the search is done — the deterrence of criminal behavior — is the same as that of penal laws, with the result that the inspection may disclose violations not only of the regulatory statute but also of the penal statutes.</p>
<p id="b731-8">I</p>
<p id="b731-9">Respondent Joseph Burger is the owner of a junkyard in Brooklyn, N. Y. His business consists, in part, of the dismantling of automobiles and the selling of their parts. His junkyard is an open lot with no buildings. A high metal fence surrounds it, wherein are located, among other things, vehicles and parts of vehicles. At approximately noon on November 17, 1982, Officer Joseph Vega and four other plainclothes officers, all members of the Auto Crimes Division of the New York City Police Department, entered re<page-number citation-index="1" label="694">*694</page-number>spondent’s junkyard to conduct an inspection pursuant to N. Y. Veh. &amp; Traf. Law §415-a5 (McKinney 1986).<footnotemark>1</footnotemark> Tr. 6. On any given day, the Division conducts from 6 to 10 inspections of vehicle dismantlers, automobile junkyards, and related businesses.<footnotemark>2</footnotemark> <em>Id., </em>at 26.</p>
<p id="b732-5">Upon entering the junkyard, the officers asked to see Burger’s license<footnotemark>3</footnotemark> and his “police book” — the record of the auto<page-number citation-index="1" label="695">*695</page-number>mobiles and vehicle parts in his possession. Burger replied that he had neither a license nor a police book.<footnotemark>4</footnotemark> The officers then announced their intention to conduct a § 415-a5 inspection. Burger did not object. Tr. 6, 47. In accordance with their practice, the officers copied down the Vehicle Identification Numbers (VINs) of several vehicles and parts of vehicles that were in the junkyard. <em>Id., </em>at 7, 20, 44, 46. After checking these numbers against a police computer, the officers determined that respondent was in possession of stolen vehicles and parts.<footnotemark>5</footnotemark> Accordingly, Burger was arrested and charged with five counts of possession of stolen property<footnotemark>6</footnotemark> <page-number citation-index="1" label="696">*696</page-number>and one count of unregistered operation as a vehicle dismantle^ in violation of § 415-al.</p>
<p id="b734-5">In the Kings County Supreme Court, Burger moved to suppress the evidence obtained as a result of the inspection, primarily on the ground that § 415-a5 was unconstitutional. After a hearing, the court denied the motion. It reasoned that the junkyard business was a “pervasively regulated” industry in which warrantless administrative inspections were appropriate, that the statute was properly limited in “time, place and scope,” and that, once the officers had reasonable cause to believe that certain vehicles and parts were stolen, they could arrest Burger and seize the property without a warrant. App. to Pet. for Cert. 18a-19a. When respondent moved for reconsideration in light of a recent decision of the Appellate Division, <em>People </em>v. <em>Pace, </em>101 App. Div. 2d 336, 475 N. Y. S. 2d 443 (1984), aff’d, 65 N. Y. 2d 684, <span class="citation no-link">481 N. E. 2d 250</span> (1985),<footnotemark>7</footnotemark> the court granted reargument. Upon re<page-number citation-index="1" label="697">*697</page-number>consideration, the court distinguished the situation in <em>Pace </em>from that in the instant case. It observed that the Appellate Division in <em>Pace </em>did not apply § 415-a5 to the search in question, <span class="citation" data-id="6204687"><a href="/opinion/6336105/people-v-burger/#711" aria-description="Citation for case: People v. Burger">125 Misc. 2d 709, 711</a></span>, 479 N. Y. S. 2d 936, 938 (1984), and that, in any event, the police officers in that case were not conducting an administrative inspection, but were acting on the basis of recently discovered evidence that criminal activity was taking place at the automobile salvage yard. <span class="citation" data-id="6204687"><a href="/opinion/6336105/people-v-burger/#712" aria-description="Citation for case: People v. Burger"><em>Id., </em>at 712-714</a></span>, 479 N. Y. S. 2d, at 939-940. The court therefore reaffirmed its earlier determination in the instant case that § 415-a5 was constitutional.<footnotemark>8</footnotemark> For the same reasons, the Appellate Division affirmed. 112 App. Div. 2d 1046, 493 N. Y. S. 2d 34 (1985).</p>
<p id="b735-5">The New York Court of Appeals, however, reversed. 67 N. Y. 2d 338, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/" aria-description="Citation for case: People v. Burger">493 N. E. 2d 926</a></span> (1986). In its view, § 415-a5 violated the Fourth Amendment’s prohibition of unreasonable searches and seizures.<footnotemark>9</footnotemark> According to the Court of Ap<page-number citation-index="1" label="698">*698</page-number>peals, “[t]he fundamental defect [of § 415-a5] ... is that [it] authorize [s] searches undertaken solely to uncover evidence of criminality and not to enforce a comprehensive regulatory scheme. The asserted ‘administrative schem[e]’ here [is], in reality, designed simply to give the police an expedient means of enforcing penal sanctions for possession of stolen property.” <em>Id., </em>at 344, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/#929" aria-description="Citation for case: People v. Burger">493 N. E. 2d, at 929</a></span>. In contrast to the statutes authorizing warrantless inspections whose constitutionality this Court has upheld, §415-a5, it was said, “do[es] little more than authorize general searches, including those conducted by the police, of certain commercial premises.” <em>Ibid. </em>To be sure, with its license and recordkeeping requirements, and with its authorization for inspections of records, § 415-a appears to be administrative in character. “It fails to satisfy the constitutional requirements for a valid, comprehensive regulatory scheme, however, inasmuch as it permits searches, such as conducted here, of vehicles and vehicle parts notwithstanding the absence of any records against which the findings of such a search could be compared.” <em>Id., </em>at 344-345, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/#929" aria-description="Citation for case: People v. Burger">493 N. E. 2d, at 929-930</a></span>. Accordingly, the only purpose of such searches is to determine whether a junkyard owner is storing stolen property on business premises.<footnotemark>10</footnotemark></p>
<p id="b736-5">Because of the important state interest in administrative schemes designed to regulate the vehicle-dismantling or automobile-junkyard industry,<footnotemark>11</footnotemark> we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./479/812/">479 U. S. 812</a></span> (1986).</p>
<p id="Ai6G"><page-number citation-index="1" label="699">*699</page-number>l — l I</p>
<p id="Ank">A</p>
<p id="AAH">The Court long has recognized that the Fourth Amendment’s prohibition on unreasonable searches and seizures is applicable to commercial premises, as'well as to private homes. <em>See </em>v. <em>City of Seattle, </em><span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/#543" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541, 543, 546</a></span> (1967). An owner or operator of a business thus has an expectation of privacy in commercial property, which society is prepared to consider to be reasonable, see <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 361</a></span> (1967) (Harlan, J., concurring). This expecta<page-number citation-index="1" label="700">*700</page-number>tion exists not only with respect to traditional police searches conducted for the gathering of criminal evidence but also with respect to administrative inspections designed to enforce regulatory statutes. See <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#312" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 312-313</a></span> (1978). An expectation of privacy in commercial premises, however, is different from, and indeed less than, a similar expectation in an individual’s home. See <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#598" aria-description="Citation for case: Donovan v. Dewey">452 U. S. 594, 598-599</a></span> (1981). This expectation is particularly attenuated in commercial property employed in “closely regulated” industries. The Court observed in <em>Marshall </em>v. <em>Barlow’s, Inc.: </em>“Certain industries have such a history of government oversight that no reasonable expectation of privacy, see <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351-352</a></span> (1967), could exist for a proprietor over the stock of such an enterprise.” <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#313" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 313</a></span>.</p>
<p id="b738-5">The Court first examined the “unique” problem of inspections of “closely regulated” businesses in two enterprises that had “a long tradition of close government supervision.” <em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">Ibid.</a></span> </em>In <em>Colonnade Corp. </em>v. <em>United States, </em><span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970), it considered a warrantless search of a catering business pursuant to several federal revenue statutes authorizing the inspection of the premises of liquor dealers. Although the Court disapproved the search because the statute provided that a sanction be imposed when entry was refused, and because it did not authorize entry without a warrant as an alternative in this situation, it recognized that “the liquor industry [was] long subject to close supervision and inspection.” <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#77" aria-description="Citation for case: Colonnade Catering Corp. v. United States"><em>Id., </em>at 77</a></span>. We returned to this issue in <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972), which involved a warrantless inspection of the premises of a pawnshop operator, who was federally licensed to sell sporting , weapons pursuant to the Gun Control Act of 1968, <span class="citation no-link">18 U. S. C. § 921</span> <em>et seq. </em>While noting that “[fjederal regulation of the interstate' traffic in firearms is not as deeply rooted in history as is governmental control of the liquor industry,” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell">406 U. S., at 315</a></span>, we nonetheless concluded that the warrantless inspec<page-number citation-index="1" label="701">*701</page-number>tions authorized by the Gun Control Act would “pose only limited threats to the dealer’s justifiable expectations of privacy.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell"><em>Id., </em>at 316</a></span>. We observed: “When a dealer chooses to engage in this pervasively regulated business and to accept a federal license, he does so with the knowledge that his business records, firearms, and ammunition will be subject to effective inspection.” <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Ibid.</a></span></em></p>
<p id="b739-5">The “Colonnade-Biswell” doctrine, stating the reduced expectation of privacy by an owner of commercial premises in a “closely regulated” industry, has received renewed emphasis in more recent decisions. In <em>Marshall </em>v. <em>Barlow’s, Inc., </em>we noted its continued vitality but declined to find that war-rantless inspections, made pursuant to the Occupational Safety and Health Act of 1970, <span class="citation no-link">84 Stat. 1598</span>, <span class="citation no-link">29 U. S. C. § 657</span>(a), of <em>all </em>businesses engaged in interstate commerce fell within the narrow focus of this doctrine. <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#313" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 313-314</a></span>. However, we found warrantless inspections made pursuant to the Federal Mine Safety and Health Act of 1977, <span class="citation no-link">91 Stat. 1290</span>, <span class="citation no-link">30 U. S. C. §801</span> <em>et seq., </em>proper because they were of a “closely regulated” industry. <em>Donovan </em>v. <em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">Dewey, supra.</a></span></em></p>
<p id="b739-6">Indeed, in <em>Donovan </em>v. <em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">Dewey</a></span>, </em>we declined to limit our consideration to the length of time during which the business in question — stone quarries — had been subject to federal regulation. <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#605" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 605-606</a></span>. We pointed out that the doctrine is essentially defined by “the pervasiveness and regularity of the federal regulation” and the effect of such regulation upon an owner’s expectation of privacy. See <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#600" aria-description="Citation for case: Donovan v. Dewey"><em>id., </em>at 600, 606</a></span>. We observed, however, that “the duration of a particular regulatory scheme” would remain an “important factor” in deciding whether a warrantless inspection pursuant to the scheme is permissible. <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#606" aria-description="Citation for case: Donovan v. Dewey"><em>Id., </em>at 606</a></span>.<footnotemark>12</footnotemark></p>
<p id="b740-4"><page-number citation-index="1" label="702">*702</page-number>B</p>
<p id="b740-5">Because the owner or operator of commercial premises in a “closely regulated” industry has a reduced expectation of privacy, the warrant and probable-cause requirements, which fulfill the traditional Fourth Amendment standard of reasonableness for a government search, see <em>O’Connor </em>v. <em>Ortega, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#741" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709, 741</a></span> (1987) (dissenting opinion), have lessened application in this context. Rather, we conclude that, as in other situations of “special need,” see New <em>Jersey </em>v. <em>T. L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#353" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 353</a></span> (1985) (opinion concurring in judgment), where the privacy interests of the owner are weakened and the government interests in regulating particular businesses are concomitantly heightened, a warrant-less inspection of commercial premises may well be reasonable within the meaning of the Fourth Amendment.</p>
<p id="b740-7">This warrantless inspection, however, even in the context of a pervasively regulated business, will be deemed to be reasonable only so long as three criteria are met. First, there must be a “substantial” government interest that informs the regulatory scheme pursuant to which the inspection is made. See <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#602" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 602</a></span> (“substantial federal interest in improving the health and safety conditions in the Nation’s underground and surface mines”); <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell">406 U. S., at 315</a></span> (regulation of firearms is “of central importance to federal efforts to prevent violent crime and to assist the States in regulating the firearms traffic within their borders”); <em>Colonnade Corp. </em>v. <em>United States, </em><span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#75" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S., at 75</a></span> (federal interest “in protecting the revenue against various types of fraud”).</p>
<p id="b740-8">Second, the warrantless inspections must be “necessary to further [the] regulatory scheme.” <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#600" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 600</a></span>. For example, in <em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">Dewey</a></span> </em>we recognized that forcing mine inspectors to obtain a warrant before every in<page-number citation-index="1" label="703">*703</page-number>spection might alert mine owners or operators to the impending inspection, thereby frustrating the purposes of the Mine Safety and Health Act — to detect and thus to deter safety and health violations. <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#603" aria-description="Citation for case: Donovan v. Dewey">Id., at 603</a></span>.</p>
<p id="b741-8">Finally, “the statute’s inspection program, in terms of the certainty and regularity of its application, [must] provid[e] a constitutionally adequate substitute for a warrant.” <em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">Ibid.</a></span> </em>In other words, the regulatory statute must perform the two basic functions of a warrant: it must advise the owner of the commercial premises that the search is being made pursuant to the law and has a properly defined scope, and it must limit the discretion of the inspecting officers. See <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#323" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 323</a></span>; see also <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#332" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><em>id., </em>at 332</a></span> (Stevens, J., dissenting). To perform this first function, the statute must be “sufficiently comprehensive and defined that the owner of commercial property cannot help but be aware that his property will be subject to periodic inspections undertaken for specific purposes.” <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#600" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 600</a></span>. In addition, in defining how a statute limits the discretion of the inspectors, we have observed that it must be “carefully limited in time, place, and scope.” <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell">406 U. S., at 315</a></span>.</p>
<p id="b741-9">hH I — I hH</p>
<p id="b741-3">A</p>
<p id="b741-4">Searches made pursuant to § 415-a5, in our view, clearly fall within this established exception to the warrant requirement for administrative inspections in “closely regulated” businesses.<footnotemark>13</footnotemark> First, the nature of the regulatory statute reveals that the operation of a junkyard, part of which is devoted to <page-number citation-index="1" label="704">*704</page-number>vehicle dismantling, is a “closely regulated” business in the State of New York.<footnotemark>14</footnotemark> The provisions regulating the activity of vehicle dismantling are extensive. An operator cannot engage in this industry without first obtaining a license, which means that he must meet the registration requirements and must pay a fee.<footnotemark>15</footnotemark> Under § 415-a5(a), the operator must maintain a police book recording the acquisition and disposition of motor vehicles and vehicle parts, and make such records and inventory available for inspection by the police or any agent of the Department of Motor Vehicles. The operator also must display his registration number prominently at his place of business, on business documentation, and on vehicles and parts that pass through his business. § 415-a5(b). Moreover, the person engaged in this activity is subject to criminal penalties, as well as to loss of license or civil fines, <page-number citation-index="1" label="705">*705</page-number>for failure to comply with these provisions. See §§ 415-al, 5, and 6.<footnotemark>16</footnotemark> That other States besides New York have imposed similarly extensive regulations on automobile junkyards further supports the “closely regulated” status of this industry. See n. 11, <em>supra.</em></p>
<p id="b743-5">In determining whether vehicle dismantlers constitute a “closely regulated” industry, the “duration of [this] particular regulatory scheme,” <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#606" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 606</a></span>, has some relevancy. Section 415-a could be said to be of fairly recent vintage, see 1973 N. Y. Laws, ch. 225, § 1 (McKinney), and the inspection provision of § 415-a5 was added only in 1979, see 1979 N. Y. Laws, ch. 691, §2 (McKinney). But because the automobile is a relatively new phenomenon in our society and because its widespread use is even newer, automobile junkyards and vehicle dismantlers have not been in existence very long and thus do not have an ancient history of government oversight. Indeed, the indus<page-number citation-index="1" label="706">*706</page-number>try did not attract government attention until the 1950’s, when all used automobiles were no longer easily reabsorbed into the steel industry and attention then focused on the environmental and aesthetic problems associated with abandoned vehicles. See Landscape 1970: National Conference on the Abandoned Automobile 11; see also Report to the President from the Panel on Automobile Junkyards, White House Conference on Natural Beauty 1 (1965) (statement of Charles M. Haar, Chairman: “There are junkyards and abandoned cars in the streets and along the countryside that are making America ugly, not beautiful”).</p>
<p id="b744-4">The automobile-junkyard business, however, is simply a new branch of an industry that has existed, and has been closely regulated, for many years. The automobile junkyard is closely akin to the secondhand shop or the general junkyard. Both share the purpose of recycling salvageable articles and components of items no longer usable in their original form. As such, vehicle dismantlers represent a modern, specialized version of a traditional activity.<footnotemark>17</footnotemark> In New York, general junkyards and secondhand shops long have been subject to regulation. One New York court has explained:</p>
<blockquote id="b745-4"><page-number citation-index="1" label="707">*707</page-number>“Vehicle dismantlers are part of the junk industry as well as part of the auto industry. . . . Prior to the enactment of section 415-a of the Vehicle and Traffic Law, auto dismantlers were subject to regulatory provisions governing the licensing and operation of junkyards. These regulations included provisions mandating the keeping of detailed records of purchases and sales, and the making of such records available at reasonable times to designated officials including police officers, by junk dealers . . . and by dealers in secondhand articles ....</blockquote>
<blockquote id="b745-5">“These regulatory, record keeping and warrantless inspection provisions for junk shops have been a part of the law of the City of New York and of Brooklyn for at least 140 years.” <em>People </em>v. <em>Tinneny, </em><span class="citation" data-id="6199918"><a href="/opinion/6331361/people-v-tinneny/#969" aria-description="Citation for case: People v. Tinneny">99 Misc. 2d 962, 969</a></span>, 417 N. Y. S. 2d 840, 845 (Sup. 1979).</blockquote>
<p id="b745-6">See also N. Y. C. Charter and Admin. Code § B32-113.01 (1977) (“ ‘Junk dealer’. Any person engaged in the business of purchasing or selling junk”); §B32-126.0a (‘“dealer in second-hand articles’ shall mean any person who, in any way or as a principal broker or agent: 1. [d]eals in the purchase or sale of second-hand articles of whatever nature”).<footnotemark>18</footnotemark> The history of government regulation of junk-related activities argues strongly in favor of the “closely regulated” status of the automobile junkyard.</p>
<p id="b745-7">Accordingly, in light of the regulatory framework governing his business and the history of regulation of related industries, an operator of a junkyard engaging in vehicle dismantling has a reduced expectation of privacy in this “closely regulated” business.</p>
<p id="b746-3"><page-number citation-index="1" label="708">*708</page-number>B</p>
<p id="b746-4">The New York regulatory scheme satisfies the three criteria necessary to make reasonable warrantless inspections pursuant to § 415-a5. First, the State has a substantial interest in regulating the vehicle-dismantling and automobile-junkyard industry because motor vehicle theft has increased in the State and because the problem of theft is associated with this industry. In this day, automobile theft has become a significant social problem, placing enormous economic and personal burdens upon the citizens of different States. For example, when approving the 1979 amendment to § 415-a5, which added the provision for inspections of records and inventory of junkyards, the Governor of the State explained:</p>
<blockquote id="b746-5">“Motor vehicle theft in New York State has been rapidly increasing. It has become a multimillion dollar industry which has resulted in an intolerable economic burden on the citizens of New York. In 1976, over 130,000 automobiles were reported stolen in New York, resulting in losses in excess of $225 million. Because of the high rate of motor vehicle theft, the premiums for comprehensive motor vehicle insurance in New York are significantly above the national average. In addition, stolen automobiles are often used in the commission of other crimes and there is a high incidence of accidents resulting in property damage and bodily injury involving stolen automobiles.” Governor’s Message approving L. 1979, chs. 691 and 692,1979 N. Y. Laws 1826,1826-1827 (McKinney).</blockquote>
<p id="b746-6">See also 25 Legislative Newsletter, New York State Automobile Assn., p. 1 (May 10, 1978), reprinted in Governor’s Bill Jacket, L. 1979, ch. 691 (1979 Bill Jacket) (“Auto theft in New York State has become a low-risk, high-profit, multi<page-number citation-index="1" label="709">*709</page-number>million dollar growth industry that is imposing intolerable economic burdens on motorists”).<footnotemark>19</footnotemark> Because contemporary automobiles are made from standardized parts, the nationwide extent of vehicle theft and concern about it are understandable.</p>
<p id="b747-5">Second, regulation of the vehicle-dismantling industry reasonably serves the State’s substantial interest in eradicating automobile theft. It is well established that the theft problem can be addressed effectively by controlling the receiver of, or market in, stolen property. 2 W. LaFave &amp; A. Scott, Substantive Criminal Law §8.10(a), p. 422 (1986) (“Without [professional receivers of stolen property], theft ceases to be profitable”); 2 Encyclopedia of Crime and Justice 789 (Kadish ed. 1983) (“[The criminal receiver] . . . inspires 95 per cent or more of the theft in America”). Automobile junkyards and vehicle dismantlers provide the major market for stolen vehicles and vehicle parts. See Memorandum from Paul Goldman, Counsel, State Consumer Protection Board, to Richard A. Brown, Counsel to the Governor (June 29, 1979), 1979 Bill Jacket (“It is believed that a major source of stolen vehicles, parts and registration documentation may involve vehicles which pass through the hands of [junk vehicle] dealers”). Thus, the State rationally may believe that it will reduce car theft by regulations that prevent automobile junkyards from becoming markets for stolen vehicles and that help trace the origin and destination of vehicle parts.<footnotemark>20</footnotemark></p>
<p id="b748-3"><page-number citation-index="1" label="710">*710</page-number>Moreover, the warrantless administrative inspections pursuant to § 415-a5 “are necessary to further [the] regulatory scheme.” <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#600" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 600</a></span>. In this respect, we see no difference between these inspections and those approved by the Court in <em>United States </em>v. <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span> </em>and <em>Donovan </em>v. <em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">Dewey</a></span>. </em>We explained in <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>:</em></p>
<blockquote id="b748-4">“[I]f inspection is to be effective and serve as a credible deterrent, unannounced, even frequent, inspections are essential. In this context, the prerequisite of a warrant could easily frustrate inspection; and if the necessary flexibility as to time, scope, and frequency is to be preserved, the protections afforded by a warrant would be negligible.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S., at 316</a></span>.</blockquote>
<p id="b748-5">See also <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#603" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 603</a></span>. Similarly, in the present case, a warrant requirement would interfere with the statute’s purpose of deterring automobile theft accomplished by identifying vehicles and parts as stolen and shutting down the market in such items. Because stolen cars and parts often pass quickly through an automobile junkyard, “frequent” and “unannounced” inspections are necessary in order to detect them. In sum, surprise is crucial if the regulatory scheme aimed at remedying this major social problem is to function at all.</p>
<p id="b749-4"><page-number citation-index="1" label="711">*711</page-number>Third, § 415-a5 provides a “constitutionally adequate substitute for a warrant.” <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#603" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 603</a></span>. The statute informs the operator of a vehicle dismantling business that inspections will be made on a regular basis. <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#605" aria-description="Citation for case: Donovan v. Dewey"><em>Id., </em>at 605</a></span>. Thus, the vehicle dismantler knows that the inspections to which he is subject do not constitute discretionary acts by a government official but are conducted pursuant to statute. See <em>Marshall </em>v. <em>Barlow's, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#332" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 332</a></span> (dissenting opinion). Section 415-a5 also sets forth the scope of the inspection and, accordingly, places the operator on notice as to how to comply with the statute. In addition, it notifies the operator as to who is authorized to conduct an inspection.</p>
<p id="b749-5">Finally, the “time, place, and scope” of the inspection is limited, <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell">406 U. S., at 315</a></span>, to place appropriate restraints upon the discretion of the inspecting officers. See <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#605" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 605</a></span>. The officers are allowed to conduct an inspection only “during [the] regular and usual business hours.” §415-a5.<footnotemark>21</footnotemark> The inspections can be made only of vehicle-dismantling and related industries. And the permissible scope of these searches is narrowly defined: the inspectors may examine the records, as well as “any vehicles or parts of vehicles which are subject to <page-number citation-index="1" label="712">*712</page-number>the record keeping requirements of this section and which are on the premises.” Ibid.<footnotemark>22</footnotemark></p>
<p id="b750-5">IV</p>
<p id="b750-6">A search conducted pursuant to § 415-a5, therefore, clearly falls within the well-established exception to the warrant requirement for administrative inspections of “closely regulated” businesses. The Court of Appeals, nevertheless, struck down the statute as violative of the Fourth Amendment because, in its view, the statute had no truly administrative purpose but was “designed simply to give the police an expedient means of enforcing penal sanctions for possession of stolen property.” 67 N. Y. 2d, at 344, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/#929" aria-description="Citation for case: People v. Burger">493 N. E. 2d, at 929</a></span>. The court rested its conclusion that the administrative goal of the statute was pretextual and that § 415-a5 really “authorized searches undertaken solely to uncover evidence of criminality” particularly on the fact that, even if an operator failed to produce his police book, the inspecting officers could continue their inspection for stolen vehicles and parts. <em>Id., </em>at 344, 345, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/#929" aria-description="Citation for case: People v. Burger">493 N. E. 2d, at 929, 930</a></span>. The court also suggested that the identity of the inspectors — police officers — was significant in revealing the true nature of the statutory scheme. <em>Id., </em>at 344, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/#929" aria-description="Citation for case: People v. Burger">493 N. E. 2d, at 929</a></span>.</p>
<p id="b750-7">In arriving at this conclusion, the Court of Appeals failed to recognize that a State can address a major social problem <em>both </em>by way of an administrative scheme <em>and </em>through penal sanctions. Administrative statutes and penal laws may have the same <em>ultimate </em>purpose of remedying the social problem, but they have different subsidiary purposes and prescribe different methods of addressing the problem. An administrative statute establishes how a particular business in a <page-number citation-index="1" label="713">*713</page-number>“closely regulated” industry should be operated, setting forth rules to guide an operator’s conduct of the business and allowing government officials to ensure that those rules are followed. Such a regulatory approach contrasts with that of the penal laws, a major emphasis of which is the punishment of individuals for specific acts of behavior.</p>
<p id="b751-5">In <em>United States </em>v. <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>we recognized this fact that both administrative and penal schemes can serve the same purposes by observing that the ultimate purposes of the Gun Control Act were “to prevent violent crime and to assist the States in regulating the firearms traffic within their borders.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell">406 U. S., at 315</a></span>. It is beyond dispute that certain state penal laws had these same purposes. Yet the regulatory goals of the Gun Control Act were narrower: the Act ensured that “weapons [were] distributed through regular channels and in a traceable manner and [made] possible the prevention of sales to undesirable customers and the detection of the origin of particular firearms.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell"><em>Id., </em>at 315-316</a></span>. The provisions of the Act, including those authorizing the warrantless inspections, served these immediate goals and also contributed to achieving the same ultimate purposes that the penal laws were intended to achieve.</p>
<p id="b751-6">This case, too, reveals that an administrative scheme may have the same ultimate purpose as penal laws, even if its regulatory goals are narrower. As we have explained above, New York, like many States, faces a serious social problem in automobile theft and has a substantial interest in regulating the vehicle-dismantling industry because of this problem. The New York penal laws address automobile theft by punishing it or the possession of stolen property, including possession by individuals in the business of buying and selling property. See n. 6, <em>supra.</em><footnotemark><em>23</em></footnotemark><em> </em>In accordance with its interest <page-number citation-index="1" label="714">*714</page-number>in regulating the automobile-junkyard industry, the State also has devised a regulatory manner of dealing with this problem. Section 415-a, as a whole, serves the regulatory goals of seeking to ensure that vehicle dismantlers are legitimate businesspersons and that stolen vehicles and vehicle parts passing through automobile junkyards can be identified.<footnotemark>24</footnotemark> In particular, §415-a5 was designed to contribute to these goals, as explained at the time of its passage:</p>
<blockquote id="b752-5">“This bill attempts to provide enforcement not only through means of law enforcement but by making it unprofitable for persons to operate in the stolen car field.</blockquote>
<blockquote id="b753-4"><page-number citation-index="1" label="715">*715</page-number>“The various businesses which are engaged in this operation have been studied and the control and requirements on the businesses have been written in a manner which would permit the persons engaged in the business to legally operate in a manner conducive to good business practices while making it extremely difficult for a person to profitably transfer a stolen vehicle or stolen part. The general scheme is to identify every person who may legitimately be involved in the operation and to provide a record keeping system which will enable junk vehicles and parts to be traced back to the last legitimately registered or titled owner. Legitimate businessmen engaged in this field have complained with good cause that the lack of comprehensive coverage of the field has put them at a disadvantage with persons who currently are able to operate outside of statute and regulations. They have also legitimately complained that delays inherent in the present statutory regulation and onerous record keeping requirements have made profitable operation difficult.</blockquote>
<blockquote id="b753-5">“The provisions of this bill have been drafted after consultation with respected members of the various industries and provides <em>[sic] </em>a more feasible system of controlling traffic in stolen vehicles and parts.” Letter of Stanley M. Gruss, Deputy Commissioner and Counsel, to Richard A. Brown, Counsel to the Governor (June 20, 1979), 1979 Bill Jacket.</blockquote>
<p id="b753-6">Accordingly, to state that §415-a5 is “really” designed to gather evidence to enable convictions under the penal laws is to ignore the plain administrative purposes of § 415-a, in general, and § 415-a5, in particular.</p>
<p id="b753-7">If the administrative goals of § 415-a5 are recognized, the difficulty the Court of Appeals perceives in allowing inspecting officers to examine vehicles and vehicle parts even in the absence of records evaporates. The regulatory purposes of § 415-a5 certainly are served by having the inspecting offi<page-number citation-index="1" label="716">*716</page-number>cers compare the records of a particular vehicle dismantler with vehicles and vehicle parts in the junkyard. The purposes of maintaining junkyards in the hands of legitimate businesspersons and of tracing vehicles that pass through these businesses, however, <em>also </em>are served by having the officers examine the operator’s inventory even when the operator, for whatever reason, fails to produce the police book.<footnotemark>25</footnotemark> Forbidding inspecting officers to examine the inventory in this situation would permit an illegitimate vehicle dismantler to thwart the purposes of the administrative scheme and would have the absurd result of subjecting his counterpart who maintained records to a more extensive search.<footnotemark>26</footnotemark></p>
<p id="b754-4">Nor do we think that this administrative scheme is unconstitutional simply because, in the course of enforcing it, an inspecting officer may discover evidence of crimes, besides violations of the scheme itself. In <em>United States </em>v. <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>the pawnshop operator was charged not only with a violation of the recordkeeping provision, pursuant to which the inspection was made, but also with other violations detected during the inspection, see <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#313" aria-description="Citation for case: United States v. Biswell">406 U. S., at 313, n. 2</a></span>, and convicted of a failure to pay an occupational tax for dealing in specific firearms, <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#312" aria-description="Citation for case: United States v. Biswell">id., at 312-313</a></span>. The discovery of evidence of crimes in the course of an otherwise proper administrative inspection does not render that search illegal or the administrative scheme suspect. Cf. <em>United States </em>v. <em>Villamonte-Marquez, </em><span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/#583" aria-description="Citation for case: United States v. Villamonte-Marquez">462 U. S. 579, 583-584</a></span>, and n. 3 (1983).<footnotemark>27</footnotemark></p>
<p id="b755-4"><page-number citation-index="1" label="717">*717</page-number>Finally, we fail to see any constitutional significance in the fact that police officers, rather than “administrative” agents, are permitted to conduct the § 415-a5 inspection. The significance respondent alleges lies in the role of police officers as enforcers of the penal laws and in the officers’ power to arrest for offenses other than violations of the administrative scheme. It is, however, important to note that state police officers, like those in New York, have numerous duties in addition to those associated with traditional police work. See <em>People </em>v. <em>De Bour, </em>40 N. Y. 2d 210, 218, <span class="citation" data-id="5530768"><a href="/opinion/5682261/people-v-de-bour/#568" aria-description="Citation for case: People v. De Bour">352 N. E. 2d 562, 568</a></span> (1976) (“To consider the actions of the police solely in terms of arrest and criminal process is an unnecessary distortion”); see also ABA Standards for Criminal Justice 1-1.1(b) and commentary (2d ed. 1980, Supp. 1982). As a practical matter, many States do not have the resources to assign the enforcement of a particular administrative scheme to a specialized agency. So long as a regulatory scheme is properly administrative, it is not rendered illegal by the fact that the inspecting officer has the power to arrest individuals for violations other than those created by the scheme itself.<footnotemark>28</footnotemark> In <page-number citation-index="1" label="718">*718</page-number>sum, we decline to impose upon the States the burden of requiring the enforcement of their regulatory statutes to be carried out by specialized agents.</p>
<p id="b756-4">V</p>
<p id="b756-5">Accordingly, the judgment of the New York Court of Appeals is reversed, and the case is remanded to that court for further proceedings not inconsistent with this opinion.</p>
<p id="b756-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b732-6"> This statute reads in pertinent part:</p>
<blockquote id="b732-7">“Records and identification, (a) Any records required by this section shall apply only to vehicles or parts of vehicles for which a certificate of title has been issued by the commissioner [of the Department of Motor Vehicles] or which would be eligible to have such a certificate of title issued. Every person required to be registered pursuant to this section shall maintain a record of all motor vehicles, trailers, and major component parts thereof, coming into his possession together with a record of the disposition of any such motor vehicle, trailer or part thereof and shall maintain proof of ownership for any motor vehicle, trailer or major component part thereof while in his possession. Such records shall be maintained in a manner and form prescribed by the commissioner. The commissioner may, by regulation, exempt vehicles or major component parts of vehicles from all or a portion of the record keeping requirements based upon the age of the vehicle if he deems that such record keeping requirements would serve no substantial value. Upon request of an agent of the commissioner or of any police officer and during his regular and usual business hours, a vehicle dismantler shall produce such records and permit said agent or police officer to examine them and any vehicles or parts of vehicles which are subject to the record keeping requirements of this section and which are on the premises. . . . The failure to produce such records or to permit such inspection on the part of any person required to be registered pursuant to this section as required by this paragraph shall be a class A misdemeanor.”</blockquote>
</footnote>
<footnote label="2">
<p id="b732-8"> It was unclear from the record why, on that particular day, Burger’s junkyard was selected for inspection. Tr. 23-24. The junkyards designated for inspection apparently were selected from a list of such businesses compiled by New York City police detectives. <em>Id., </em>at 24.</p>
</footnote>
<footnote label="3">
<p id="b732-9"> An individual operating a vehicle-dismantling business in New York is required to have a license:</p>
<blockquote id="b732-10">“Definition and registration of vehicle dismantlers. A vehicle dis-mantler is any person who is engaged in the business of acquiring motor vehicles or trailers for the purpose of dismantling the same for parts or reselling such vehicles as scrap. No person shall engage in the business of or <page-number citation-index="1" label="695">*695</page-number>operate as a vehicle dismantler unless there shall have been issued to him a registration in accordance with the provisions of this section. A violation of this subdivision shall be a class E felony.” N. Y. Veh. &amp; Traf. Law § 415-al (McKinney 1986).</blockquote>
</footnote>
<footnote label="4">
<p id="b733-8"> There appears to have been some initial confusion among the inspecting officers as to whether Burger had not compiled a police book or whether, at the moment of the inspection, it simply was not in his possession. See Tr. 6, 30, 46-47, 59-60.</p>
</footnote>
<footnote label="5">
<p id="b733-9"> The officers also determined that Burger possessed a wheelchair and a handicapped person’s walker that had been located in a stolen vehicle. See <em>id., </em>at 8-11, 13, 34-36.</p>
</footnote>
<footnote label="6">
<p id="b733-10"> Respondent was charged with two counts of criminal possession of stolen property in the second degree in violation of a New York statute that, at that time, read:</p>
<blockquote id="b733-11">“A person is guilty of criminal possession of stolen property in the second degree when he knowingly possesses stolen property, with intent to benefit himself or a person other than an owner thereof or to impede the recovery by an owner thereof, and when:</blockquote>
<blockquote id="b733-12">“1. The value of the property exceeds two hundred fifty dollars; or</blockquote>
<blockquote id="b733-13">“3. He is a pawnbroker or is in the business of buying, selling or otherwise dealing in property ....</blockquote>
<blockquote id="b733-14">“Criminal possession of stolen property in the second degree is a class E felony.” N. Y. Penal Law § 165.45 (McKinney 1975).</blockquote>
<p id="b733-15">Burger also was charged with three counts of criminal possession of stolen property in the third degree pursuant to the following provision of a New York statute:</p>
<blockquote id="AXq"><page-number citation-index="1" label="696">*696</page-number>“A person is guilty of criminal possession of stolen property in the third degree when he knowingly possesses stolen property, with intent to benefit himself or a person other than an owner thereof or to impede the recovery by an owner thereof.</blockquote>
<blockquote id="AyG">“Criminal possession of stolen property in the third degree is a class A misdemeanor.” N. Y. Penal Law § 165.40 (McKinney 1975).</blockquote>
</footnote>
<footnote label="7">
<p id="b734-12"> In <em>People </em>v. <em>Pace, </em>the Appellate Division was faced with a situation in which officers had conducted a warrantless search of an automobile salvage yard immediately after having their suspicions aroused about criminal activity there. The court did not find the exception for warrantless administrative inspections applicable in that situation, 101 App. Div. 2d, at 340, 475 N. Y. S. 2d, at 446, but made the following footnote remark:</p>
<blockquote id="b734-13">“Subdivision 5 of section 415-a of the Vehicle and Traffic Law, the statute under which the police officers said they were acting, has no application. While this section requires dismantlers to keep a police book, the book was missing when the officers entered and it would thus have been impossible for the officers to exercise the alleged implied authority to compare the book entries to the contents of the yard.” <em>Id., </em>at 339, n. 1, 475 N. Y. S. 2d, at 445, n. 1.</blockquote>
<p id="b734-14">Respondent construed this footnote to mean that police officers had to obtain a search warrant if a vehicle dismantler did not produce a police book <page-number citation-index="1" label="697">*697</page-number>and thus they could not conduct a warrantless inspection in the absence of this book. See <span class="citation" data-id="6204869"><a href="/opinion/6336287/camphill-special-schools-inc-v-prentice/#711" aria-description="Citation for case: Camphill Special Schools, Inc. v. Prentice">126 Misc. 2d 709, 711</a></span>, 479 N. Y. S. 2d 936, 938 (Sup. 1984).</p>
</footnote>
<footnote label="8">
<p id="b735-8"> In addition, the court determined that the search was proper under New York City Charter and Admin. Code § 436 (Supp. 1985). <span class="citation" data-id="6204687"><a href="/opinion/6336105/people-v-burger/#712" aria-description="Citation for case: People v. Burger">125 Misc. 2d, at 712-715</a></span>, 479 N. Y. S. 2d, at 939-940. That section reads:</p>
<blockquote id="b735-9">“The commissioner [of the Police Department] shall possess powers of general supervision and inspection over all licensed and unlicensed pawnbrokers, vendors, junkshop keepers, junk boatmen, cartmen, dealers in second-hand merchandise and auctioneers within the city; and in connection with the performance of any police duties he shall have power to examine such persons, their clerks and employees and their books, business premises, and any articles of merchandise in their possession. A refusal or neglect to comply in any respect with the provisions of this section on the part of any pawnbroker, vendor, junkshop keeper, junk boatman, cart-man, dealer in second-hand merchandise or auctioneer, or any clerk or employee of any thereof shall be triable by a judge of the criminal court and punishable by not more than thirty days’ imprisonment, or by a fine of not more than fifty dollars, or both.”</blockquote>
</footnote>
<footnote label="9">
<p id="b735-10"> The Court of Appeals found that the question of the constitutionality of the statute and charter was squarely presented by this case, as it had not been in <em>People </em>v. <em>Pace, </em>because there was no dispute that the inspection was made pursuant to those provisions. 67 N. Y. 2d, at 342-343, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/#928" aria-description="Citation for case: People v. Burger">493 N. E. 2d, at 928</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b736-6"> For similar reasons, the Court of Appeals concluded that Charter § 436 also violated the Fourth Amendment’s prohibition on unreasonable searches and seizures. 67 N. Y. 2d, at 344-346, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/#929" aria-description="Citation for case: People v. Burger">493 N. E. 2d, at 929-930</a></span>.</p>
</footnote>
<footnote label="11">
<p id="b736-7"> Numerous States have provisions for the warrantless inspections of vehicle dismantlers and automobile junkyards. See, <em>e. g., </em><span class="citation no-link">Ala. Code §40-12-419</span> (1985); <span class="citation no-link">Ariz. Rev. Stat. Ann. §28</span>-1307C (Supp. 1986); Ark. Stat. Ann. §75-1803 (1979); Cal. Veh. Code Ann. §§ 2805(a) and (c) (West Supp. 1987); <span class="citation no-link">Conn. Gen. Stat. §14</span>-67m(a) (Supp. 1987); Del. Code Ann., Tit. 21, § 6717(a) (1985); <span class="citation no-link">Fla. Stat. §812.055</span> (Supp. 1987); <span class="citation no-link">Ga. Code Ann. §43-48-16</span> (1984); Ill. Rev. Stat., ch. 95½, ¶5-403 (Supp. 1986); <span class="citation no-link">Ind. <page-number citation-index="1" label="699">*699</page-number>Code §§ 9-1-3.6</span>-10(a) and (d) and 9-1-3.6-12 (1979 and Supp. 1986); <span class="citation no-link">Iowa Code §§ 321.90</span>(3)(b) and 321.95 (1985); <span class="citation no-link">Kan. Stat. Ann. §8-2408</span>(c) (1982); Ky. Rev. Stat. §177.935(7) (1985); La. Rev. Stat. Ann. §32:757 (West Supp. 1987); Me. Rev. Stat. Ann., Tit. 29, §2459 (Supp. 1986); Md. Transp. Code Ann. § 15-105 (Supp. 1986); <span class="citation no-link">Mich. Comp. Laws § 257.251</span> (Supp. 1987); <span class="citation no-link">Miss. Code Ann. §27-19-313</span> (1972); <span class="citation no-link">Mo. Rev. Stat. §301.225</span> (Supp. 1986); <span class="citation no-link">Mont. Code Ann. §§ 75-10-503</span> and 75-10-513 (1985); <span class="citation no-link">Nev. Rev. Stat. §482.3263</span> (1986); N. H. Rev. Stat. Ann. §261:132 (1982); N. J. Stat. Ann. § 39.10B-2c (West Supp. 1987); N. M. Stat. Ann. § 66-2-12(A)(4) (1984); Okla. Stat., Tit. 47, §591.6 (Supp. 1987); Ore. Rev. Stat. §810.480 (1985); R. I. Gen. Laws §42-14.2-15 (Supp. 1986); S. C. Code § 56-5-5670(b) (1976); S. D. Codified Laws §§32-6B-38 to 32-6B-40 (Supp. 1987); <span class="citation no-link">Tenn. Code Ann. §55-14-106</span> (1980); Tex. Rev. Civ. Stat. Ann., Art. 6687-2(e) (Vernon Supp. 1987); <span class="citation no-link">Utah Code Ann. §§41-3-23</span>(2) and (4) (Supp. 1987); Vt. Stat. Ann., Tit. 23, §466 (1978); Va. Code §46.1-550.12 (Supp. 1986); <span class="citation no-link">Wash. Rev. Code §§46.80.080</span>(5) and 46.80.150 (1970); W. Va. Code § 17A-6-25 (1986); <span class="citation no-link">Wis. Stat. § 218.22</span>(4)(c) (1982); Wyo. Stat. § 31-13-112(e)(iii) (1987).</p>
<p id="AXu">Courts have upheld such statutes against federal constitutional attack. See, <em>e. g., Bionic Auto Parts &amp; Sales, Inc. </em>v. <em>Fahner, </em><span class="citation" data-id="427553"><a href="/opinion/427553/bionic-auto-parts-and-sales-inc-v-tyrone-c-fahner/#1081" aria-description="Citation for case: Bionic Auto Parts and Sales, Inc. v. Tyrone C. Fahner">721 F. 2d 1072, 1081</a></span> (CA7 1983); <em>People </em>v. <em>Easley, </em><span class="citation" data-id="2123937"><a href="/opinion/2123937/people-v-easley/#445" aria-description="Citation for case: People v. Easley">90 Cal. App. 3d 440, 445</a></span>, <span class="citation" data-id="2123937"><a href="/opinion/2123937/people-v-easley/#399" aria-description="Citation for case: People v. Easley">153 Cal. Rptr. 396, 399</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./444/899/">444 U. S. 899</a></span> (1979); <em>Moore </em>v. <em>State, </em><span class="citation" data-id="1108128"><a href="/opinion/1108128/moore-v-state/#216" aria-description="Citation for case: Moore v. State">442 So. 2d 215, 216</a></span> (Fla. 1983); <em>People </em>v. <em>Barnes, </em><span class="citation" data-id="1601166"><a href="/opinion/1601166/people-v-barnes/#42" aria-description="Citation for case: People v. Barnes">146 Mich. App. 37, 42</a></span>, <span class="citation" data-id="1601166"><a href="/opinion/1601166/people-v-barnes/#466" aria-description="Citation for case: People v. Barnes">379 N. W. 2d 464, 466</a></span> (1985); <em>State </em>v. <em>Zinmeister, </em><span class="citation" data-id="3778084"><a href="/opinion/4022001/state-v-zinmeister/#318" aria-description="Citation for case: State v. Zinmeister">27 Ohio App. 3d 313, 318</a></span>, <span class="citation" data-id="3778084"><a href="/opinion/4022001/state-v-zinmeister/#65" aria-description="Citation for case: State v. Zinmeister">501 N. E. 2d 59, 65</a></span> (1985); see also <em>State </em>v. <em>Tindell, </em><span class="citation" data-id="2123138"><a href="/opinion/2123138/state-v-tindell/#483" aria-description="Citation for case: State v. Tindell">272 Ind. 479, 483</a></span>, <span class="citation" data-id="2123138"><a href="/opinion/2123138/state-v-tindell/#748" aria-description="Citation for case: State v. Tindell">399 N. E. 2d 746, 748</a></span> (1980); <em>Shirley </em>v. <em>Commonwealth, </em><span class="citation" data-id="1244252"><a href="/opinion/1244252/shirley-v-commonwealth/#57" aria-description="Citation for case: Shirley v. Commonwealth">218 Va. 49, 57-58</a></span>, <span class="citation" data-id="1244252"><a href="/opinion/1244252/shirley-v-commonwealth/#436" aria-description="Citation for case: Shirley v. Commonwealth">235 S. E. 2d 432, 436-437</a></span> (1977). But see <em>People </em>v. <em>Krull, </em><span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/#116" aria-description="Citation for case: People v. Krull">107 Ill. 2d 107, 116-117</a></span>, <span class="citation" data-id="2102923"><a href="/opinion/2102923/people-v-krull/#707" aria-description="Citation for case: People v. Krull">481 N. E. 2d 703, 707-708</a></span> (1985), rev’d, <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">480 U. S. 340</a></span> (1987); <em>State </em>v. <em>Galio, </em>92 N. M. 266, 268-269, <span class="citation" data-id="9611504"><a href="/opinion/1382601/state-v-galio/#46" aria-description="Citation for case: State v. Galio">587 P. 2d 44, 46-47</a></span> (1978).</p>
</footnote>
<footnote label="12">
<p id="b739-7"> We explained in <em>Donovan </em>v. <em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">Dewey</a></span>: </em>“If the length of regulation were the only criterion, absurd results would occur. Under appellees’ view, new or emerging industries, including ones such as the nuclear power industry that pose enormous potential safety and health problems, <page-number citation-index="1" label="702">*702</page-number>could never be subject to warrantless searches even under the most carefully structured inspection program simply because of the recent vintage of regulation.” <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#606" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 606</a></span>.</p>
</footnote>
<footnote label="13">
<p id="b741-5"> Because we find the inspection at issue here constitutional under § 415-a5, we have no reason to reach the question of the constitutionality of §436 of the New York City Charter. Moreover, because the Court of Appeals addressed only the general question concerning the constitutionality of the administrative inspection, not the specific question whether the search and seizure of the wheelchair and walker were within the scope of the inspection, we do not reach here this latter issue.</p>
</footnote>
<footnote label="14">
<p id="b742-4"> The New York Court of Appeals did not imply that automobile junkyards were <em>not </em>a “closely regulated” business in that State. Rather, it found fault with one aspect of the administrative statutes regulating these junkyards. 67 N. Y. 2d, at 344-345, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/#929" aria-description="Citation for case: People v. Burger">493 N. E. 2d, at 929-930</a></span>. In his brief in opposition to the petition for certiorari, respondent appears to concede that this industry in New York is “closely regulated” by his statement that the New York Legislature could enact a ‘“comprehensive regulatory scheme’ ” directed at the industry. Brief in Opposition 3.</p>
</footnote>
<footnote label="15">
<p id="b742-5"> Under § 415-al, “[n]o person shall engage in the business of or operate as a vehicle dismantler unless there shall have been issued to him a registration in accordance with the provisions of this section.” In making an application for a registration, the operator must provide “a listing of all felony convictions and all other convictions relating to the illegal sale or possession of a motor vehicle or motor vehicle parts, and a listing of all arrests for any such violations by the applicant and any other person required to be named in such application.” § 415-a2. Section 415-a3 requires that the operator pay a registration fee, and § 415-a4 stipulates that “no registration shall be issued or renewed unless the applicant has a permanent place of business at which the activity requiring registration is performed which conforms to section one hundred thirty-six of the general municipal law as such section applies and to all local laws or ordinances and the applicant and all persons having a financial interest in the business have been determined by the commissioner to be fit persons to engage in such business.”</p>
</footnote>
<footnote label="16">
<p id="b743-6"> The broad extent of the regulation of the vehicle-dismantling industry further is shown by the fact that § 415-a regulates the activities not only of vehicle dismantlers but also of those in similar businesses, such as salvage pool operators, § 415-al-a, mobile ear crushers, § 415-al-b, itinerant vehicle collectors, § 415-al-e, vehicle rebuilders, § 415-a8, scrap processors, § 415-a9, and scrap collectors and repair shops, § 415-alO. Moreover, the Commissioner of the Department of Motor Vehicles has promulgated regulations dealing specifically with this industry: e. <em>g., </em>N. Y. Comp. Codes, Rules &amp; Regs., Tit. 15, § 81.2 (1986) (registration); § 81.8 (procedures upon acquisition of junk and salvage vehicles); §81.10 (vehicle identification numbers); §81.12 (records).</p>
<p id="b743-7"><em>Amici </em>argue that § 415-a does not create a truly administrative scheme, because its provisions are not sufficiently voluminous. See Brief for American Civil Liberties Union et al. as <em>Amici Curiae </em>34-36. Although the number of regulations certainly is a factor in the determination whether a particular business is “closely regulated,” the sheer quantity of pages of statutory material is not dispositive of this question. Rather, the proper focus is on whether the “regulatory presence is sufficiently comprehensive and defined that the owner of commercial property cannot help but be aware that his property will be subject to periodic inspections undertaken for specific purposes.” <em>Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#600" aria-description="Citation for case: Donovan v. Dewey">452 U. S., at 600</a></span>. Section 415-a plainly satisfies this criterion.</p>
</footnote>
<footnote label="17">
<p id="b744-5"> A member of the automobile-junkyard industry described it this way:</p>
<blockquote id="b744-6">“Webster says junk is old metal, rags, and rubbish. The word ‘junk’ can also be used as a verb, and as such would mean to discard. I represent an industry that buys vehicles which are no longer suitable for transportation. These vehicles have been wrecked, damaged, or have otherwise become inoperative. They are taken apart by members of our industry. The components that are still usable are made available to garages, body shops, and the general public as used parts for repair of other vehicles. The portion of the vehicle that is not suitable for parts is passed on to a scrap processor who then transforms the hulk, or the remnants, into a product suitable for resmelting purposes.” Junkyards &amp; Solid Waste Disposal in the Highway Environment, Proceedings of National Seminar, June 10-11, 1975, p. 19 (1976) (statement of Donald J. Rouse, National Association of Auto and Truck Recyclers, now known as Automotive Dismantlers and Recyclers of America).</blockquote>
</footnote>
<footnote label="18">
<p id="b745-8"> In fact, by assuming that Charter § 436 with its use of the terms “junk-shop keepers” and “dealers in second-hand merchandise,” see n. 8, <em>supra, </em>could be applied to respondent, the New York Court of Appeals understood that a vehicle dismantler fell within the scope of those terms. See also <em>People </em>v. <em>Cusumano, </em>108 App. Div. 2d 752, 754, 484 N. Y. S. 2d 909, 912 (1985).</p>
</footnote>
<footnote label="19">
<p id="b747-6"> A similar concern with stemming the social plague of automobile theft has motivated other States to pass legislation aimed at the vehicle-dismantling industry. See, <em>e. g., </em>Ill. Rev. Stat., eh. 9572, ¶ 5-100-1 (Supp. 1985) (legislative finding that “crimes involving the theft of motor vehicles and their parts have risen steadily over the past years, with a resulting loss of millions of dollars to the residents of this State”).</p>
</footnote>
<footnote label="20">
<p id="b747-7"> See Governor’s Message approving L. 1979, chs. 691 and 692, 1979 N. Y. Laws 1826, 1827 (McKinney) (“By making it difficult to traffic in stolen vehicles and parts, it can be anticipated that automobile theft problems will be decreased and the cost to insurance companies and the public <page-number citation-index="1" label="710">*710</page-number>may be reduced”). As the Illinois Legislature found in passing regulations aimed at this industry,</p>
<blockquote id="Afr">“(2) essential to the criminal enterprise of motor vehicle theft operations is the ability of thieves to transfer or sell stolen vehicles or their parts through legitimate commercial channels making them available for sale to the automotive industry; and (3) motor vehicle dealers, used parts dealers, scrap processors, automotive parts recyclers, and rebuilders are engaged in a type of business which often exposes them and their operations to pressures and influences from motor vehicle thieves; and (4) elements of organized crime are constantly attempting to take control of businesses engaged in the sale and repair of motor vehicles so as to further their own criminal interests.” Ill. Rev. Stat., ch. 9572, ¶ 5-100-1 (1985).</blockquote>
<p id="A82">See also <span class="citation no-link">Kan. Stat. Ann. § 8-2402</span> (1982); <span class="citation no-link">Nev. Rev. Stat. § 482.318</span> (1985).</p>
</footnote>
<footnote label="21">
<p id="b749-6"> Respondent contends that § 415-a5 is unconstitutional because it fails to limit the number of searches that may be conducted of a particular business during any given period. Brief for Respondent 12. While such limitations, or the absence thereof, are a factor in an analysis of the adequacy of a particular statute, they are not determinative of the result so long as the statute, as a whole, places adequate limits upon the discretion of the inspecting officers. Indeed, we have approved statutes authorizing war-rantless inspections even when such statutes did not establish a fixed number of inspections for a particular time period. See <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#312" aria-description="Citation for case: United States v. Biswell">406 U. S. 311, 312, n. 1</a></span> (1972). And we have suggested that, in some situations, inspections must be conducted frequently to achieve the purposes of the statutory scheme. <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell"><em>Id., </em>at 316</a></span> (“Here, if inspection is to be effective and serve as a credible deterrent, unannounced, even <em>frequent, </em>inspections are essential”) (emphasis added).</p>
</footnote>
<footnote label="22">
<p id="b750-8"> With respect to the adequacy of the statutory procedures, this case is indistinguishable from <em>United States </em>v. <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>. </em>There, the regulatory provisions of the Gun Control Act permitted warrantless inspections of <em>both </em>records <em>and </em>inventory “at all reasonable times.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#312" aria-description="Citation for case: United States v. Biswell"><em>Id., </em>at 312, n. 1</a></span>. The Court held that the statute gave a firearms dealer adequate notice of “the purposes of the inspector [and] the limits of his task.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell"><em>Id., </em>at 316</a></span>.</p>
</footnote>
<footnote label="23">
<p id="b751-7"> The penal laws often are changed in response to the growth of a particular type of crime. For example, in 1986 New York amended its definition of grand larceny to include the following provision:</p>
<blockquote id="AbA"><page-number citation-index="1" label="714">*714</page-number>“A person is guilty of grand larceny in the fourth degree when he steals property and when:</blockquote>
<blockquote id="Aci">“8. The value of the property exceeds one hundred dollars and the property consists of a motor vehicle, as defined in section one hundred twenty-five of the vehicle and traffic law, other than a motorcycle, as defined in section one hundred twenty-three of such law.” 1986 N. Y. Laws, ch. 515, § 1 (McKinney), codified at N. Y. Penal Law § 155.30 (McKinney Supp. 1987).</blockquote>
</footnote>
<footnote label="24">
<p id="b752-8"> See, <em>e. g., </em>Memorandum of State Department of Motor Vehicles in support of 1973 N. Y. Laws, eh. 225, 1973 N. Y. Laws 2166, 2167 (McKinney) (purpose of § 415-a “is to provide a system of record keeping so that vehicles can be traced through junk yards and to assure that such junk yards are run by legitimate business men rather than by auto theft rings”); Letter of John D. Caemmerer, Chairman of Senate Committee on Transportation, to Michael Whiteman, Counsel to the Governor (Apr. 12, 1973), reprinted in Governor’s Bill Jacket, L. 1973, eh. 225, p. 15 (1973 Bill Jacket) (“This bill establishes much needed safeguards for an industry which can be readily infiltrated by those wishing to dispose of stolen automobiles or automobile parts”); Letter of Peter M. Pryor, Chairman of New York State Consumer Protection Board, to Michael Whiteman, Counsel to the Governor (Apr. 18, 1973), 1973 Bill Jacket, p. 6 (“Organized crime has used the junk and salvage industry as a convenient staging ground for illicit activities concerning motor vehicles as well as for operations into other areas. The proposed legislation opens the junk and salvage business to the scrutiny of the police and the Department of Motor Vehicles thereby reducing the possibility of utilizing such dealerships as covers for covert businesses”).</p>
</footnote>
<footnote label="25">
<p id="b754-5"> Failure to produce a record is a misdemeanor, § 415-a5, which can be a ground for suspension of the operator’s license, § 415-a6. This suspension serves to remove illegitimate operators from the industry.</p>
</footnote>
<footnote label="26">
<p id="b754-6"> Indeed, in <em>United States </em>v. <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>we found no constitutional problem with a statute that authorized inspection both of records and inventory, <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#312" aria-description="Citation for case: United States v. Biswell">406 U. S., at 312, n. 1</a></span>, and with an actual inspection of a dealer’s premises despite the fact that the dealer’s records were not properly maintained, <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#313" aria-description="Citation for case: United States v. Biswell"><em>id., </em>at 313, n. 2</a></span>.</p>
</footnote>
<footnote label="27">
<p id="b754-7"> The legislative history of § 415-a, in general, and § 415-a5, in particular, reveals that the New York Legislature had proper regulatory purposes for enacting the administrative scheme and was not using it as a <page-number citation-index="1" label="717">*717</page-number>“pretext” to enable law enforcement authorities to gather evidence of penal law violations. See <em>supra, </em>at 714-715 and n. 24; see also <em>Illinois </em>v. <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#351" aria-description="Citation for case: Illinois v. Krull">480 U. S. 340, 351</a></span> (1987) (“[W]e are given no basis for believing that legislators are inclined to subvert their oaths and the Fourth Amendment”). There is, furthermore, no reason to believe that the instant inspection was actually a “pretext” for obtaining evidence of respondent’s violation of the penal laws. It is undisputed that the inspection was made solely pursuant to the administrative scheme. In fact, because the search here was truly a § 415-a5 inspection, the Court of Appeals was able to reach in this case, as it could not in <em>People </em>v. <em>Pace, </em>65 N. Y. 2d 684, <span class="citation no-link">481 N. E. 2d 250</span> (1985), the question of the constitutionality of the statute. See 67 N. Y. 2d, at 342-343, <span class="citation" data-id="5537320"><a href="/opinion/5688150/people-v-burger/#928" aria-description="Citation for case: People v. Burger">493 N. E. 2d, at 928</a></span>; see also n. 7, <em>supra.</em></p>
</footnote>
<footnote label="28">
<p id="b755-6"> In <em>United States </em>v. <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>, </em>the search in question was conducted by a city police officer and by a United States Treasury agent, <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#312" aria-description="Citation for case: United States v. Biswell">406 U. S., at 312</a></span>, the latter being authorized to make arrests for federal crimes. See <span class="citation no-link">27 CFR § 70.28</span> (1986). The Internal Revenue agents involved in the search in <em>Colonnade Corp. </em>v. <em>United States, </em><span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#73" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72, 73</a></span> (1970), had similar powers. See <span class="citation no-link">26 U. S. C. § 7608</span>(a).</p>
</footnote>
</opinion>
```

---
