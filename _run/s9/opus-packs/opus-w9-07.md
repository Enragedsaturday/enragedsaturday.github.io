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

## GROUP: _overhaul2/lake/cases/Rivas-Villegas v. Cortesluna.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Rivas-Villegas v. Cortesluna"
type: case
citation: "595 U.S. 1 (2021)"
parallel_cite: "142 S. Ct. 4; 211 L. Ed. 2d 164"
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2021
date_decided: 2021-10-18
docket: 20-1539
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2021-10-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Rivas-Villegas v. Cortesluna
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/5290447/rivas-villegas-v-cortesluna/"
  cluster_id: 5290447
  opinion_id: 5118993
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[City of Tahlequah v. Bond]]", "[[District of Columbia v. Wesby]]", "[[Saucier v. Katz]]", "[[Pearson v. Callahan]]", "[[Graham v. Connor]]"]
aliases: []
tags: ["case", "qualified-immunity", "section-1983", "excessive-force", "clearly-established", "per-curiam"]
holding: "For QI, the plaintiff must identify a case that put the officer on notice that his specific conduct was unlawful, 'in light of the specific context of the case, not as a broad general proposition.'"
lake:
  record_id: Rivas-Villegas v. Cortesluna
  status: verified
  projected_at: 2026-07-06
---

# Rivas-Villegas v. Cortesluna

*595 U.S. 1 (2021)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers responded to a 911 call from a crying 12-year-old reporting that she, her mother, and her sister had locked themselves in a room because the mother's boyfriend, Cortesluna, was trying to hurt them and had a chainsaw. Officers ordered Cortesluna out and onto the ground and saw a knife in his left pocket. While removing the knife and handcuffing him, Officer Rivas-Villegas briefly placed his knee on the left side of Cortesluna's back for no more than eight seconds. Cortesluna sued under § 1983 for excessive force; the Ninth Circuit denied [[Qualified Immunity|qualified immunity]], relying on its precedent *LaLonde v. County of Riverside*.

## Issue
Whether Rivas-Villegas was entitled to [[Qualified Immunity|qualified immunity]] because he did not violate clearly established law.

## Rule
Clearly established law must be particularized to the case. The "clearly established" inquiry "must be undertaken in light of the specific context of the case, not as a broad general proposition." — 595 U.S. 1 (slip op., at 4) (quoting *Brosseau v. Haugen*). ^pin-op4

"[T]o show a violation of clearly established law, Cortesluna must identify a case that put Rivas-Villegas on notice that his specific conduct was unlawful." — *Id.* (slip op., at 5). ^pin-op5

## Application
Cortesluna identified no Supreme Court case addressing facts like these, and the Ninth Circuit relied solely on *LaLonde*, which is materially distinguishable: *LaLonde* involved a mere noise complaint and an unarmed suspect on whose back an officer "deliberately dug his knee" causing lasting injury, whereas here officers responded to a serious domestic-violence call possibly involving a chainsaw, Cortesluna had a knife in his pocket he had appeared to reach for, and Rivas-Villegas placed his knee on Cortesluna's back for no more than eight seconds beside the knife being retrieved. *LaLonde* therefore did not give fair notice that Rivas-Villegas's conduct was unlawful.

## Conclusion
Because no precedent clearly established that Rivas-Villegas's specific conduct was unlawful, he was entitled to [[Qualified Immunity|qualified immunity]]; the Ninth Circuit was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. Decided the same day as the companion qualified-immunity [[Common Legal Terms#per-curiam|per curiam]] [[City of Tahlequah v. Bond]], reinforcing that "clearly established" law must be defined with specificity.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *Rivas-Villegas v. Cortesluna*, 595 U.S. 1 (2021) (per curiam) — https://www.courtlistener.com/opinion/5290447/rivas-villegas-v-cortesluna/ — pinpoints: slip op., at 4, 5 (CL carries the slip opinion; cluster 5290447 → opinion 5118993).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "91dbe9e2822c8429", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Rivas-Villegas v. Cortesluna"}, "payload": {"all": [{"cite": "595 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "595"}, {"cite": "142 S. Ct. 4", "page": "4", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "142"}, {"cite": "211 L. Ed. 2d 164", "page": "164", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "211"}], "display": "595 U.S. 1", "official": {"cite": "595 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "595"}, "official_selection_present": true, "record_id": "Rivas-Villegas v. Cortesluna"}}
{"assertion_id": "1717778d23f8217a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op5", "record_id": "Rivas-Villegas v. Cortesluna"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op5", "pinpoint_status": "slip-only", "quote": "[T]o show a violation of clearly established law, Cortesluna must identify a case that put Rivas-Villegas on notice that his specific conduct was unlawful.", "quote_fidelity": "mismatch", "record_id": "Rivas-Villegas v. Cortesluna", "star_marker": null}}
{"assertion_id": "2c66e36ce590b171", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op4", "record_id": "Rivas-Villegas v. Cortesluna"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op4", "pinpoint_status": "slip-only", "quote": "--- # Rivas-Villegas v. Cortesluna *595 U.S. 1 (2021)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers responded to a 911 call from a crying 12-year-old reporting that she, her mother, and her sister had locked themselves in a room because the mother's boyfriend, Cortesluna, was trying to hurt them and had a chainsaw. Officers ordered Cortesluna out and onto the ground and saw a knife in his left pocket. While removing the knife and handcuffing him, Officer Rivas-Villegas briefly placed his knee on the left side of Cortesluna's back for no more than eight seconds. Cortesluna sued under § 1983 for excessive force; the Ninth Circuit denied qualified immunity, relying on its precedent *LaLonde v. County of Riverside*. ## Issue Whether Rivas-Villegas was entitled to qualified immunity because he did not violate clearly established law. ## Rule Clearly established law must be particularized to the case. The", "quote_fidelity": "mismatch", "record_id": "Rivas-Villegas v. Cortesluna", "star_marker": null}}
{"assertion_id": "d5ee0d2353dc6a75", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Rivas-Villegas v. Cortesluna"}, "payload": {"as_of_content": "2021-10-18", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Rivas-Villegas v. Cortesluna", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Rivas-Villegas v. Cortesluna

```json
{
  "schema_version": "s2.v1",
  "record_id": "Rivas-Villegas v. Cortesluna",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Rivas-Villegas v. Cortesluna",
    "case_name_short": "Rivas-Villegas",
    "case_name_full": "",
    "input_case_name": "Rivas-Villegas v. Cortesluna",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2021-10-18",
    "year": 2021,
    "docket": "20-1539",
    "cluster_id": 5290447,
    "lead_opinion_id": 5118993,
    "sibling_ids": [
      5118993
    ],
    "absolute_url": "/opinion/5290447/rivas-villegas-v-cortesluna/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "595 U.S. 1",
      "volume": "595",
      "reporter": "U.S.",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "142 S. Ct. 4",
        "volume": "142",
        "reporter": "S. Ct.",
        "page": "4",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "211 L. Ed. 2d 164",
        "volume": "211",
        "reporter": "L. Ed. 2d",
        "page": "164",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "595 U.S. 1",
        "volume": "595",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "142 S. Ct. 4",
        "volume": "142",
        "reporter": "S. Ct.",
        "page": "4",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "211 L. Ed. 2d 164",
        "volume": "211",
        "reporter": "L. Ed. 2d",
        "page": "164",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "595 U.S. 1",
    "official_selection": {
      "court_class": "scotus",
      "selected": "595 U.S. 1",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op4",
      "page": null,
      "quote": "--- # Rivas-Villegas v. Cortesluna *595 U.S. 1 (2021)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers responded to a 911 call from a crying 12-year-old reporting that she, her mother, and her sister had locked themselves in a room because the mother's boyfriend, Cortesluna, was trying to hurt them and had a chainsaw. Officers ordered Cortesluna out and onto the ground and saw a knife in his left pocket. While removing the knife and handcuffing him, Officer Rivas-Villegas briefly placed his knee on the left side of Cortesluna's back for no more than eight seconds. Cortesluna sued under \u00a7 1983 for excessive force; the Ninth Circuit denied qualified immunity, relying on its precedent *LaLonde v. County of Riverside*. ## Issue Whether Rivas-Villegas was entitled to qualified immunity because he did not violate clearly established law. ## Rule Clearly established law must be particularized to the case. The",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op5",
      "page": null,
      "quote": "[T]o show a violation of clearly established law, Cortesluna must identify a case that put Rivas-Villegas on notice that his specific conduct was unlawful.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2021-10-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Rivas-Villegas v. Cortesluna",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Pearlie Gambrel v. Knox Cnty., Ky.",
          "cluster_id": 6347889,
          "cite": [
            "25 F.4th 391"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bretton Westmoreland v. Butler Cnty.",
          "cluster_id": 6454550,
          "cite": [
            "29 F.4th 721"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Melissa Knibbs v. Anthony Momphard, Jr.",
          "cluster_id": 6456228,
          "cite": [
            "30 F.4th 200"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jerry Lawler v. Hardeman Cnty., Tenn.",
          "cluster_id": 9476181,
          "cite": [
            "93 F.4th 919"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salvatore Palma, Jr. v. Matthew Johns",
          "cluster_id": 6445970,
          "cite": [
            "27 F.4th 419"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Trellus Richmond v. Mario J. Badia",
          "cluster_id": 7858519,
          "cite": [
            "47 F.4th 1172"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sheri Trozzi v. Lake County, Ohio",
          "cluster_id": 6455758,
          "cite": [
            "29 F.4th 745"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Shumate v. City of Adrian, Mich.",
          "cluster_id": 7855599,
          "cite": [
            "44 F.4th 427"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William LaPlante v. City of Battle Creek, Mich.",
          "cluster_id": 6458100,
          "cite": [
            "30 F.4th 572"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sherelle Thomas v. City of Harrisburg",
          "cluster_id": 9449712,
          "cite": [
            "88 F.4th 275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patricia Polanco v. Ralph Diaz",
          "cluster_id": 9418406,
          "cite": [
            "76 F.4th 918"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Mack v. John Yost",
          "cluster_id": 9385401,
          "cite": [
            "63 F.4th 211"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henderson v. Harris County",
          "cluster_id": 8248448,
          "cite": [
            "51 F.4th 125"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Azucena Zamorano Aleman v. City of Charlotte",
          "cluster_id": 9421054,
          "cite": [
            "80 F.4th 264"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salazar v. Molina",
          "cluster_id": 6478362,
          "cite": [
            "37 F.4th 278"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kamel Chaney-Snell v. Andrew Young",
          "cluster_id": 9493618,
          "cite": [
            "98 F.4th 699"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "George v. Beaver County",
          "cluster_id": 6465265,
          "cite": [
            "32 F.4th 1246"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony Novak v. City of Parma, Ohio",
          "cluster_id": 6464344,
          "cite": [
            "33 F.4th 296"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crittindon v. LeBlanc",
          "cluster_id": 6476851,
          "cite": [
            "37 F.4th 177"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Jackson v. City of Cleveland",
          "cluster_id": 9389985,
          "cite": [
            "64 F.4th 736"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Timmy Mosier v. Joseph Evans",
          "cluster_id": 9458549,
          "cite": [
            "90 F.4th 541"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark Campbell v. Cheatham County Sheriff's Dep't",
          "cluster_id": 7860703,
          "cite": [
            "47 F.4th 468"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Daniel Andrews v. City of Henderson",
          "cluster_id": 6470929,
          "cite": [
            "35 F.4th 710"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cameron Lewis v. Kevin Caraballo",
          "cluster_id": 9494123,
          "cite": [
            "98 F.4th 521"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dejuan Hopson v. Jacob Alexander",
          "cluster_id": 9407196,
          "cite": [
            "71 F.4th 692"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(5118993) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
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
      },
      "lane2_top_cited": {
        "query": "cites:(5118993)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMSZzPTU3OTM4ODUmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%285118993%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(5118993)",
        "reviewed": 77,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 77,
        "triage_read": 0,
        "triage_snippet_classified": 77
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(5118993)",
    "indexed_citing_opinions": 126,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 5118993,
        "count": 126,
        "count_source": "search"
      }
    ],
    "citation_count": 489,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/rivas-villegas-v-cortesluna.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5OTIyNzkmcz0xMDEyNDEwMSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%285118993%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 5118993,
        "cited_id": 4580945,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5118993,
        "cited_id": 9429990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5118993,
        "cited_id": 9431666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5118993,
        "cited_id": 9434715,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5118993,
        "cited_id": 9492827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5118993,
        "cited_id": 9820073,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "C",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T17:35:44Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:35:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:35:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:38:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:35:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Rivas-Villegas v. Cortesluna

```
                  Cite as: 595 U. S. ____ (2021)             1

                           Per Curiam

SUPREME COURT OF THE UNITED STATES
 DANIEL RIVAS-VILLEGAS v. RAMON CORTESLUNA
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED
    STATES COURT OF APPEALS FOR THE NINTH CIRCUIT
             No. 20–1539. Decided October 18, 2021

    PER CURIAM.
    Petitioner Daniel Rivas-Villegas, a police officer in Union
City, California, responded to a 911 call reporting that a
woman and her two children were barricaded in a room for
fear that respondent Ramon Cortesluna, the woman’s boy-
friend, was going to hurt them. After confirming that the
family had no way of escaping the house, Rivas-Villegas
and the other officers present commanded Cortesluna out-
side and onto the ground. Officers saw a knife in Cor-
tesluna’s left pocket. While Rivas-Villegas and another of-
ficer were in the process of removing the knife and
handcuffing Cortesluna, Rivas-Villegas briefly placed his
knee on the left side of Cortesluna’s back. Cortesluna later
sued under Rev. Stat. §1979, 42 U. S. C. §1983, alleging, as
relevant, that Rivas-Villegas used excessive force. At issue
here is whether Rivas-Villegas is entitled to qualified im-
munity because he did not violate clearly established law.
    The undisputed facts are as follows. A 911 operator re-
ceived a call from a crying 12-year-old girl reporting that
she, her mother, and her 15-year-old sister had shut them-
selves into a room at their home because her mother’s boy-
friend, Cortesluna, was trying to hurt them and had a
chainsaw. The girl told the operator that Cortesluna was
“ ‘always drinking,’ ” had “ ‘anger issues,’ ” was “ ‘really
mad,’ ” and was using the chainsaw to “ ‘break something in
the house.’ ” Cortesluna v. Leon, 979 F. 3d 645, 649 (CA9
2020). A police dispatcher relayed this information along
with a description of Cortesluna in a request for officers to
respond.
2             RIVAS-VILLEGAS v. CORTESLUNA

                         Per Curiam

   Rivas-Villegas heard the broadcast and responded to the
scene along with four other officers. The officers spent sev-
eral minutes observing the home and reported seeing
through a window a man matching Cortesluna’s descrip-
tion. One officer asked whether the girl and her family
could exit the house. Dispatch responded that they “ ‘were
unable to get out’ ” and confirmed that the 911 operator had
“ ‘hear[d] sawing in the background’ ” and thought that Cor-
tesluna might be trying to saw down the door. Cortesluna
v. Leon, 2018 WL 6727824, *2 (ND Cal., Dec. 21, 2018).
   After receiving this information, Rivas-Villegas knocked
on the door and stated loudly, “ ‘police department, come to
the front door, Union City police, come to the front door.’ ”
Ibid. Another officer yelled, “ ‘he’s coming and has a
weapon.’ ” Ibid. A different officer then stated, “ ‘use less-
lethal,’ ” referring to a beanbag shotgun. Ibid. When Rivas-
Villegas ordered Cortesluna to “ ‘drop it,’ ” Cortesluna
dropped the “weapon,” later identified as a metal tool. Ibid.
   Rivas-Villegas then commanded, “ ‘come out, put your
hands up, walk out towards me.’ ” 979 F. 3d, at 650. Cor-
tesluna put his hands up and Rivas-Villegas told him to
“ ‘keep coming.’ ” Ibid. As Cortesluna walked out of the
house and toward the officers, Rivas-Villegas said, “ ‘Stop.
Get on your knees.’ ” Ibid. Plaintiff stopped 10 to 11 feet
from the officers. Another officer then saw a knife sticking
out from the front left pocket of Cortesluna’s pants and
shouted, “ ‘he has a knife in his left pocket, knife in his
pocket,’ ” and directed Cortesluna, “ ‘don’t put your hands
down,’ ” “ ‘hands up.’ ” 2018 WL 6727824, *2. Cortesluna
turned his head toward the instructing officer but then low-
ered his head and his hands in contravention of the officer’s
orders. Another officer twice shot Cortesluna with a bean-
bag round from his shotgun, once in the lower stomach and
once in the left hip.
   After the second shot, Cortesluna raised his hands over
his head. The officers shouted for him to “ ‘get down,’ ”
                  Cite as: 595 U. S. ____ (2021)            3

                           Per Curiam

which he did. Another officer stated, “ ‘left pocket, he’s got
a knife.’ ” Ibid. Rivas-Villegas then straddled Cortesluna.
He placed his right foot on the ground next to Cortesluna’s
right side with his right leg bent at the knee. He placed his
left knee on the left side of Cortesluna’s back, near where
Cortesluna had a knife in his pocket. He raised both of Cor-
tesluna’s arms up behind his back. Rivas-Villegas was in
this position for no more than eight seconds before standing
up while continuing to hold Cortesluna’s arms. At that
point, another officer, who had just removed the knife from
Cortesluna’s pocket and tossed it away, came and hand-
cuffed Cortesluna’s hands behind his back. Rivas-Villegas
lifted Cortesluna up and moved him away from the door.
   Cortesluna brought suit under 42 U. S. C. §1983, claim-
ing, as relevant here, that Rivas-Villegas used excessive
force in violation of the Fourth Amendment. The District
Court granted summary judgment to Rivas-Villegas, but
the Court of Appeals for the Ninth Circuit reversed. 979
F. 3d, at 656.
   The Court of Appeals held that “Rivas-Villegas is not en-
titled to qualified immunity because existing precedent put
him on notice that his conduct constituted excessive force.”
Id., at 654. In reaching this conclusion, the Court of Ap-
peals relied solely on LaLonde v. County of Riverside, 204
F. 3d 947 (CA9 2000). The court acknowledged that “the
officers here responded to a more volatile situation than did
the officers in LaLonde.” 979 F. 3d, at 654. Nevertheless,
it reasoned: “Both LaLonde and this case involve suspects
who were lying face-down on the ground and were not re-
sisting either physically or verbally, on whose back the de-
fendant officer leaned with a knee, causing allegedly signif-
icant injury.” Ibid.
   Judge Collins dissented. As relevant, he argued that “the
facts of LaLonde are materially distinguishable from this
case and are therefore insufficient to have made clear to
every reasonable officer that the force Rivas-Villegas used
4              RIVAS-VILLEGAS v. CORTESLUNA

                          Per Curiam

here was excessive.” Id., at 664 (internal quotation marks
omitted).
   We agree and therefore reverse. Even assuming that con-
trolling Circuit precedent clearly establishes law for pur-
poses of §1983, LaLonde did not give fair notice to Rivas-
Villegas. He is thus entitled to qualified immunity.
   “Qualified immunity attaches when an official’s conduct
does not violate clearly established statutory or constitu-
tional rights of which a reasonable person would have
known.” White v. Pauly, 580 U. S. ___, ___ (2017) (per cu-
riam) (slip op., at 6) (internal quotation marks omitted). A
right is clearly established when it is “sufficiently clear that
every reasonable official would have understood that what
he is doing violates that right.” Mullenix v. Luna, 577 U. S.
7, 11 (2015) (per curiam) (internal quotation marks omit-
ted). Although “this Court’s case law does not require a case
directly on point for a right to be clearly established, exist-
ing precedent must have placed the statutory or constitu-
tional question beyond debate.” White, 580 U. S., at ___
(slip op., at 6) (alterations and internal quotation marks
omitted). This inquiry “must be undertaken in light of the
specific context of the case, not as a broad general proposi-
tion.” Brosseau v. Haugen, 543 U. S. 194, 198 (2004) (per
curiam) (internal quotation marks omitted).
   “[S]pecificity is especially important in the Fourth
Amendment context, where . . . it is sometimes difficult for
an officer to determine how the relevant legal doctrine, here
excessive force, will apply to the factual situation the officer
confronts.” Mullenix, 577 U. S., at 12 (alterations and in-
ternal quotation marks omitted). Whether an officer has
used excessive force depends on “the facts and circum-
stances of each particular case, including the severity of the
crime at issue, whether the suspect poses an immediate
threat to the safety of the officers or others, and whether he
is actively resisting arrest or attempting to evade arrest by
flight.” Graham v. Connor, 490 U. S. 386, 396 (1989); see
                  Cite as: 595 U. S. ____ (2021)            5

                           Per Curiam

also Tennessee v. Garner, 471 U. S. 1, 11 (1985) (“Where the
officer has probable cause to believe that the suspect poses
a threat of serious physical harm, either to the officer or to
others, it is not constitutionally unreasonable to prevent es-
cape by using deadly force”). However, Graham’s and Gar-
ner’s standards are cast “at a high level of generality.”
Brosseau, 543 U. S., at 199. “[I]n an obvious case, these
standards can ‘clearly establish’ the answer, even without
a body of relevant case law.” Ibid. But this is not an obvi-
ous case. Thus, to show a violation of clearly established
law, Cortesluna must identify a case that put Rivas-Ville-
gas on notice that his specific conduct was unlawful.
   Cortesluna has not done so. Neither Cortesluna nor the
Court of Appeals identified any Supreme Court case that
addresses facts like the ones at issue here. Instead, the
Court of Appeals relied solely on its precedent in LaLonde.
Even assuming that Circuit precedent can clearly establish
law for purposes of §1983, LaLonde is materially distin-
guishable and thus does not govern the facts of this case.
   In LaLonde, officers were responding to a neighbor’s com-
plaint that LaLonde had been making too much noise in his
apartment. 204 F. 3d, at 950–951. When they knocked on
LaLonde’s door, he “appeared in his underwear and a T-
shirt, holding a sandwich in his hand.” Id., at 951.
LaLonde testified that, after he refused to let the officers
enter his home, they did so anyway and informed him he
would be arrested for obstruction of justice. Ibid. One of-
ficer then knocked the sandwich from LaLonde’s hand and
“grabbed LaLonde by his ponytail and knocked him back-
wards to the ground.” Id., at 952. After a short scuffle, the
officer sprayed LaLonde in the face with pepper spray. At
that point, LaLonde ceased resisting and another officer,
while handcuffing LaLonde, “deliberately dug his knee into
LaLonde’s back with a force that caused him long-term if
not permanent back injury.” Id., at 952, 960, n. 17.
   The situation in LaLonde and the situation at issue here
6             RIVAS-VILLEGAS v. CORTESLUNA

                         Per Curiam

diverge in several respects. In LaLonde, officers were re-
sponding to a mere noise complaint, whereas here they
were responding to a serious alleged incident of domestic
violence possibly involving a chainsaw. In addition,
LaLonde was unarmed. Cortesluna, in contrast, had a
knife protruding from his left pocket for which he had just
previously appeared to reach. Further, in this case, video
evidence shows, and Cortesluna does not dispute, that Ri-
vas-Villegas placed his knee on Cortesluna for no more than
eight seconds and only on the side of his back near the knife
that officers were in the process of retrieving. LaLonde, in
contrast, testified that the officer deliberately dug his knee
into his back when he had no weapon and had made no
threat when approached by police. These facts, considered
together in the context of this particular arrest, materially
distinguish this case from LaLonde.
  “Precedent involving similar facts can help move a case
beyond the otherwise hazy borders between excessive and
acceptable force and thereby provide an officer notice that
a specific use of force is unlawful.” Kisela v. Hughes, 584
U. S. ___, ___ (2018) (per curiam) (slip op., at 5) (internal
quotation marks omitted). On the facts of this case, neither
LaLonde nor any decision of this Court is sufficiently simi-
lar. For that reason, we grant Rivas-Villegas’ petition for
certiorari and reverse the Ninth Circuit’s determination
that Rivas-Villegas is not entitled to qualified immunity.

                                             It is so ordered.

```

---

## GROUP: _overhaul2/lake/cases/Roaden v. Kentucky.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Roaden v. Kentucky
type: case
citation: "413 U.S. 496 (1973)"
parallel_cite: "93 S. Ct. 2796; 37 L. Ed. 2d 757"
neutral_cite: 1973 U.S. LEXIS 31
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1973
date_decided: 1973-06-25
docket: No. 71-1134
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
  opinion_url: "https://www.courtlistener.com/opinion/108854/roaden-v-kentucky/"
  cluster_id: 108854
  opinion_id: null
  identity_checked: true
lake:
  record_id: Roaden v. Kentucky
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Particularity]]"
    role: Anchor
related:
  - "[[The Warrant Requirement]]"
  - "[[Marcus v. Search Warrant]]"
  - "[[A Quantity of Copies of Books v. Kansas]]"
  - "[[Heller v. New York]]"
tags:
  - case
  - fourth-amendment
  - warrant-requirement
  - prior-restraint
  - first-amendment
  - obscenity
  - seizure
holding: "The warrantless seizure of an allegedly obscene film from a commercial theater, incident to the exhibitor's arrest and based solely on the arresting officer's own conclusion that the film was obscene, is an unreasonable seizure: because the material is presumptively protected by the First Amendment, its seizure is a form of prior restraint that 'calls for a higher hurdle in the evaluation of reasonableness' and ordinarily requires a warrant issued on a prior judicial determination of obscenity."
aliases:
  - Roaden v. Kentucky
  - "Roaden v. Kentucky (1973)"
---

# Roaden v. Kentucky

*413 U.S. 496 (1973)* (No. 71-1134) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 108854 → combined opinion 108854 (Burger, C.J.; 413 U.S. 496, argued Nov. 14, 1972, decided June 25, 1973). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*504`). S9 promotes. -->

## Background
On September 29, 1970, the sheriff of Pulaski County, Kentucky, and the district prosecutor bought tickets to a local drive-in theater and watched a film called "Cindy and Donna." The sheriff concluded the film was obscene and, at its conclusion, went to the projection booth and arrested Roaden, the theater manager, for exhibiting an obscene film in violation of a Kentucky statute. Concurrent with the arrest, and with no warrant and no prior judicial determination of obscenity, the sheriff seized one copy of the film for use as evidence. Roaden's motion to suppress was denied, the film was admitted at trial, and he was convicted; the Court of Appeals of Kentucky affirmed, reasoning the film was properly seized incident to a lawful arrest.

## Issue
Whether allegedly obscene material — a film being exhibited to the public in a commercial theater — may be seized without a warrant, contemporaneously with and incident to an arrest for the public exhibition of that material.

## Rule
A seizure reasonable as to one kind of material may be unreasonable as to another: the seizure of presumptively expressive material implicates the First Amendment and cannot be assimilated to the warrantless seizure of weapons or contraband incident to arrest. Because taking a film in mid-exhibition halts a presumptively protected communication, it is a form of prior restraint and demands more, not less, than the ordinary warrant scrutiny: "Such precipitate action by a police officer, without the authority of a constitutionally sufficient warrant, is plainly a form of prior restraint and is, in those circumstances, unreasonable under Fourth Amendment standards. The seizure is unreasonable, not simply because it would have been easy to secure a warrant, but rather because prior restraint of the right of expression, whether by books or films, calls for a higher hurdle in the evaluation of reasonableness." — 413 U.S. at 504. ^pin-504

## Application
The film was seized on nothing more than the arresting officer's own conclusion that it was obscene; nothing before the seizure gave a magistrate the chance to focus searchingly on the question of obscenity, as *[[Marcus v. Search Warrant|Marcus]]* required. If a warrant to seize allegedly obscene material may not issue on an officer's bare conclusion, then *a fortiori* the officer may not seize it with no warrant at all. Nor was this a "now or never" situation: a film on a regular exhibition schedule in a public theater could be preserved by obtaining a warrant on a prior judicial determination of probable obscenity, without risking loss of the evidence. The incident-to-arrest rationale that justifies seizing a pistol or contraband therefore could not carry over to expressive material.

## Conclusion
The judgment of the Court of Appeals of Kentucky was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]]. Burger, C.J., delivered the opinion of the Court. Brennan, J., joined by Stewart and Marshall, JJ., concurred in the judgment; Douglas, J., dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Roaden* is a warrant-requirement anchor for the special protection expressive materials receive at the seizure stage: where the "things to be seized" are presumptively First-Amendment-protected, the Fourth Amendment tolerates no shortcut around the warrant and the prior judicial determination it secures. Teach it alongside its companion *[[Heller v. New York]]* (decided the same day, sustaining a seizure made under a warrant after the magistrate viewed the film) and its antecedents *[[Marcus v. Search Warrant|Marcus]]* and *[[A Quantity of Copies of Books v. Kansas|A Quantity of Books]]*.

## Appears on
- [[Particularity]] — *Anchor*

## Sources
- [*Roaden v. Kentucky*, 413 U.S. 496 (1973)](https://www.courtlistener.com/opinion/108854/roaden-v-kentucky/) — pinpoint: 504 (Burger, C.J., for the Court; the CL opinion text carries the reporter star `*504` at the start of the paragraph containing the quoted "higher hurdle" holding). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3a41296ac50c63c1", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Roaden v. Kentucky"}, "payload": {"all": [{"cite": "413 U.S. 496", "page": "496", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "413"}, {"cite": "93 S. Ct. 2796", "page": "2796", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "93"}, {"cite": "37 L. Ed. 2d 757", "page": "757", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "37"}, {"cite": "1973 U.S. LEXIS 31", "page": "31", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1973"}], "display": "413 U.S. 496", "official": {"cite": "413 U.S. 496", "page": "496", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "413"}, "official_selection_present": true, "record_id": "Roaden v. Kentucky"}}
{"assertion_id": "14870486d4bf0548", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Roaden v. Kentucky"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Roaden v. Kentucky", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Roaden v. Kentucky

```json
{
  "schema_version": "s2.v1",
  "record_id": "Roaden v. Kentucky",
  "status": "under_review",
  "identity": {
    "case_name": "Roaden v. Kentucky",
    "case_name_short": "Roaden",
    "case_name_full": "Roaden v. Kentucky",
    "input_case_name": "Roaden v. Kentucky",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1973-06-25",
    "year": 1973,
    "docket": "No. 71-1134",
    "cluster_id": 108854,
    "lead_opinion_id": 9425416,
    "sibling_ids": [],
    "absolute_url": "/opinion/108854/roaden-v-kentucky/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "413 U.S. 496",
      "volume": "413",
      "reporter": "U.S.",
      "page": "496",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "93 S. Ct. 2796",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2796",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 L. Ed. 2d 757",
        "volume": "37",
        "reporter": "L. Ed. 2d",
        "page": "757",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1973 U.S. LEXIS 31",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "31",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "413 U.S. 496",
        "volume": "413",
        "reporter": "U.S.",
        "page": "496",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 S. Ct. 2796",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2796",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 L. Ed. 2d 757",
        "volume": "37",
        "reporter": "L. Ed. 2d",
        "page": "757",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. LEXIS 31",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "31",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "413 U.S. 496",
    "official_selection": {
      "court_class": "scotus",
      "selected": "413 U.S. 496",
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
    "date_created": "2026-07-06T13:44:00Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:44:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:44:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:44:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:44:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "roaden-v-kentucky--108854",
      "to_record_id": "Roaden v. Kentucky",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Roaden v. Kentucky

```
<opinion type="majority">
<author id="b541-4"><page-number citation-index="1" label="497">*497</page-number>Mr. Chief Justice Burger</author>
<p id="AXD">delivered the opinion of of the Court.</p>
<p id="b541-5">The question presented in this case is whether the seizure of allegedly obscene material, contemporaneous with and as an incident to an arrest for the public exhibition of such material in a commercial theater may be accomplished without a warrant.</p>
<p id="b541-6">On September 29, 1970, the sheriff of Pulaski County, Kentucky, accompanied by the district prosecutor, purchased tickets to a local drive-in theater. There the sheriff observed, in its entirety, a film called “Cindy and Donna” and concluded that it was obscene and that its exhibition was in violation of a state statute. A substantial part of the film was also observed by a deputy sheriff from a vantage point on the road outside the theater. Since the petitioner conceded the obscenity of the film at trial, that issue is not before us for decision.<footnotemark>1</footnotemark></p>
<p id="b541-7">The sheriff, at the conclusion of the film, proceeded to the projection booth, where he arrested petitioner, the manager of the theater, on the charge of exhibiting an obscene film to the public contrary to Ky. Rev. Stat. § 436.101 (1973).<footnotemark>2</footnotemark> Concurrent with the arrest, the sheriff <page-number citation-index="1" label="498">*498</page-number>seized one copy of the film for use as evidence. It is uncontested: (a) that the sheriff had no warrant when he made the arrest and seizure, (b) that there had been no <page-number citation-index="1" label="499">*499</page-number>prior determination by a judicial officer on the question of obscenity, and (c) that the arrest was based solely on the sheriff’s observing the exhibition of the film.</p>
<p id="b543-5">On September 30, 1970, the day following the arrest of petitioner and the seizure of the film, the Grand Jury of Pulaski County heard testimony concerning the scenes and content of the film and returned an indictment charging petitioner with exhibiting an obscene film in violation of Ky. Rev. Stat. § 436.101. On October 3, 1970, petitioner entered a plea of not guilty in the Pulaski Circuit Court, and the case was set for trial. On October 12, 1970, petitioner filed a motion to suppress the film as evidence and to dismiss the indictment. The motion was predicated upon the ground that the film was “improperly, unlawfully and illegally seized, contrary to . . . the laws of the land.” Four days later, on October 16, 1970, the Pulaski Circuit Court heard argument at an adversary hearing on petitioner’s motion. The motion was denied.</p>
<p id="b543-6">Petitioner’s trial began on October 20, 1970. The arresting sheriff and one of his deputies were the only witnesses for the prosecution. The sheriff testified that the film displayed nudity and “intimate love scenes.” The sheriff further testified that, upon viewing the film, he determined that it was obscene and that its exhibition <page-number citation-index="1" label="500">*500</page-number>violated state law. He therefore arrested petitioner. Together with the testimony of the sheriff, the film itself was introduced in evidence. Petitioner's motion to suppress the film was renewed, and again overruled. The sheriff’s deputy took the stand and testified that he had viewed the final 30 minutes of the film from a vantage point on a public road outside the theater. Following this testimony, the jury was permitted to see the film.</p>
<p id="b544-5">Petitioner testified in his own behalf. He stated that, to his knowledge, no juveniles had been admitted to see the film, and that he had received no complaints about the film until it was seized by the sheriff. At the close of his testimony, the jury found petitioner guilty as charged. The jury rendered both a general verdict of guilty and a special verdict that the film was obscene, as provided by Ky. Rev. Stat. §436.101 (8).</p>
<p id="b544-6">On appeal, the Court of Appeals of Kentucky affirmed petitioner’s conviction. The Court of Appeals first emphasized that “[i]t was conceded by [petitioner’s] counsel in closing argument to the jury that the film is obscene. No issue is presented on appeal as to the obscenity of the material.” <span class="citation" data-id="5038205"><a href="/opinion/5214390/roaden-v-commonwealth/#815" aria-description="Citation for case: Roaden v. Commonwealth">473 S. W. 2d 814, 815</a></span> (1971). The Court of Appeals then held that the film was properly seized incident to a lawful arrest, distinguishing the holdings of this Court in <em>A Quantity of Books </em>v. <em>Kansas, </em><span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">378 U. S. 205</a></span> (1964), and <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717</a></span> (1961), on the ground that those decisions related to seizure of allegedly obscene materials “for destruction or suppression, not to seizures incident to an arrest for possessing, selling, or exhibiting a specific item.” <span class="citation" data-id="5038205"><a href="/opinion/5214390/roaden-v-commonwealth/#815" aria-description="Citation for case: Roaden v. Commonwealth">473 S. W. 2d, at 815</a></span>. It also distinguished <em>Lee Art Theatre </em>v. <em>Virginia, </em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">392 U. S. 636</a></span> (1968), on the grounds that there film “had been seized pursuant to a [defective] search warrant, not incident to an arrest.” <span class="citation" data-id="5038205"><a href="/opinion/5214390/roaden-v-commonwealth/#816" aria-description="Citation for case: Roaden v. Commonwealth">473 S. W. 2d, at 816</a></span>. The Court of Appeals relied on a decision of a federal three-judge <page-number citation-index="1" label="501">*501</page-number>court in <em>Hosey </em>v. <em>City of Jackson, </em><span class="citation" data-id="9716282"><a href="/opinion/2096144/hosey-v-city-of-jackson-mississippi/" aria-description="Citation for case: Hosey v. City of Jackson, Mississippi">309 F. Supp. 527</a></span> (SD Miss. 1970), which concluded that:</p>
<blockquote id="b545-5">“[Sjeizure of an allegedly obscene film as an incident to lawful arrests for a crime committed in the presence of the arresting officers, i. e., the public showing of such film, does not exceed constitutional bounds in the absence of a prior judicial hearing on the question of its obscenity.” <span class="citation" data-id="9716282"><a href="/opinion/2096144/hosey-v-city-of-jackson-mississippi/#533" aria-description="Citation for case: Hosey v. City of Jackson, Mississippi"><em>Id., </em>at 533</a></span>.</blockquote>
<p id="b545-6">The Court of Appeals specifically declined to follow a decision by another federal three-judge court in <em>Ledesma </em>v. <em>Perez, </em><span class="citation" data-id="9690341"><a href="/opinion/1867767/delta-book-distributors-inc-v-cronvich/" aria-description="Citation for case: Delta Book Distributors, Inc. v. Cronvich">304 F. Supp. 662</a></span> (ED La. 1969), which held unconstitutional the seizure of allegedly obscene material incident to an arrest, but without a warrant or a prior adversary hearing.<footnotemark>3</footnotemark></p>
<p id="b545-7">I</p>
<p id="b545-8">The Fourth Amendment proscription against “unreasonable . . . seizures,” applicable to the States through the Fourteenth Amendment, must not be read in a vacuum. A seizure reasonable as to one type of material in one setting may be unreasonable in a different setting or with respect to another kind of material. Cf. <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#471" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 471-472</a></span> (1971); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#509" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., at </em>509-510</a></span> (Black, J., concurring and dissenting); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#512" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 512-513</a></span> (White, J., concurring and dissenting). The question to be resolved is whether the seizure of the film without a warrant was unreasonable under Fourth Amendment standards and, if so, <page-number citation-index="1" label="502">*502</page-number>whether the film was therefore inadmissible at-the trial. The seizure of instruments of a crime, such as a pistol or a knife, or “contraband or stolen goods or objects dangerous in themselves,” <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#472" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 472</a></span>, are to be distinguished from quantities of books and movie films when a court appraises the reasonableness of the seizure under Fourth or Fourteenth Amendment standards.</p>
<p id="b546-5"><em>Marcus </em>v. <em>Search <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Warrant, supra,</a></span> </em>held that a warrant for the seizure of allegedly obscene books could not be issued on the conclusory opinion of a police officer that the books sought to be seized were obscene. Such a warrant lacked the safeguards demanded “to assure nonobscene material the constitutional protection to which it is entitled. . . . [T]he warrants issued on the strength of the conclusory assertions of a single police officer, without any scrutiny by the judge of any materials considered by the complainant to be obscene.” <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#731" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S., at 731-732</a></span>. There had been “no step in the procedure before seizure designed to focus searchingly on the question of obscenity.” <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#732" aria-description="Citation for case: Marcus v. Search Warrant of Property"><em>Id., </em>at 732</a></span>.</p>
<p id="b546-6">The sense of this holding was reaffirmed in <em>A Quantity of Books </em>v. <em><span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">Kansas, supra,</a></span> </em>where the Court found unconstitutional a “massive seizure” of books from a commercial bookstore for the purpose of destroying the books as contraband. The result was premised on the lack of an adversary hearing prior to seizure, and the Court did not find it necessary to reach the claim that the seizure violated Fourth Amendment standards. <span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">378 U. S., at 210</a></span> n. 2. However, the Court emphasized:</p>
<blockquote id="b546-7">“It is no answer to say that obscene books are contraband, and that consequently the standards governing searches and seizures of allegedly obscene books should not differ from those applied with respect to narcotics, gambling paraphernalia and <page-number citation-index="1" label="503">*503</page-number>other contraband. We rejected that proposition in <span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/#211" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas"><em>Marcus.” Id., </em>at 211-212</a></span>.</blockquote>
<p id="b547-5"><em>Lee Art Theatre </em>v. <em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">Virginia, supra,</a></span> </em>was to the same effect with regard to seizure of a film from a commercial theater regularly open to the public. There a warrant for the seizure of the film was issued on the basis of a police officer’s affidavit giving the titles of the film and asserting in conclusory fashion that he had personally viewed the films and considered them obscene. The films were seized pursuant to the warrant and introduced into evidence in a criminal case against the exhibitor. Conviction ensued. On review, the Court held that “[t]he admission of the films in evidence requires reversal of petitioner’s conviction” because</p>
<blockquote id="b547-6">“[t]he procedure under which the warrant issued solely upon the conclusory assertions of the police officer without any inquiry by the justice of the peace into the factual basis for the officer’s conclusions was not a procedure 'designed to focus searchingly on the question of obscenity,’ <em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">id.,</a></span> [Marcus </em>v. <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#732" aria-description="Citation for case: Marcus v. Search Warrant of Property"><em>Search Warrant, </em>supra] at 732</a></span>, and therefore fell short of constitutional requirements demanding necessary sensitivity to freedom of expression.” <span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/#637" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">392 U. S., at 637</a></span>.</blockquote>
<p id="b547-7">No mention was made in the brief <em>per curiam Lee Art Theatre </em>opinion as to whether or not the seizure was incident to an arrest. The Court relied on <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span> </em>and <em><span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">A Quantity of Books</a></span>.</em></p>
<p id="b547-8">The common thread of <em>Marcus, A Quantity of Books, </em>and <em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">Lee Art Theatre</a></span> </em>is to be found in the nature of the materials seized and the setting in which they were taken. See <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#486" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 486</a></span> (1965).<footnotemark>4</footnotemark> <page-number citation-index="1" label="504">*504</page-number>In each case the material seized fell arguably within First Amendment protection, and the taking brought to an abrupt halt an orderly and presumptively legitimate distribution or exhibition. Seizing a film then being exhibited to the general public presents essentially the same restraint on expression as the seizure of all the books in <em>a </em>bookstore. Such precipitate action by a police officer, without the authority of a constitutionally sufficient warrant, is plainly a form of prior restraint and is, in those circumstances, unreasonable under Fourth Amendment standards. The seizure is unreasonable, not simply because it would have been easy to secure a warrant, but rather because prior restraint of the right of expression, whether by books or films, calls for a higher hurdle in the evaluation of reasonableness. The setting of the bookstore or the commercial theater, each presumptively under the protection of the First Amendment, invokes such Fourth Amendment warrant requirements because we examine what is “unreasonable” in the light of the values of freedom of expression.<footnotemark>5</footnotemark> As we stated in <em>Stanford </em>v. <em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">Texas, supra:</a></span></em></p>
<blockquote id="b548-5">“In short, . . . the constitutional requirement that warrants must particularly describe the ‘things to be seized’ is to be accorded the most scrupulous exactitude when the ‘things’ are books, and the basis for their seizure is the ideas which they contain. See <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717</a></span>; <em>A Quantity of Books </em>v. <em>Kansas, </em><span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">378 U. S. 205</a></span>. No less a standard could be faithful to First Amendment freedoms. The constitutional impossibility of leav<page-number citation-index="1" label="505">*505</page-number>ing the protection of those freedoms to the whim of the officers charged with executing the warrant is dramatically underscored by what the officers saw fit to seize under the warrant in this case.” <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas">379 U. S., at 485</a></span> (footnotes omitted).</blockquote>
<p id="b549-5">Moreover, ordinary human experience should teach that the seizure of a movie film from a commercial theater with regularly scheduled performances, where a film is being played and replayed to paid audiences, presents a very different situation from that in which contraband is changing hands or where a robbery or assault is being perpetrated. In the latter settings, the probable cause for an arrest might justify the seizure of weapons, or other evidence or instruments of crime, without a warrant. Cf. <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#764" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 764</a></span> (1969); <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#773" aria-description="Citation for case: Chimel v. California"><em>id., </em>at 773-774</a></span> (White, J., dissenting); <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964). Where there are exigent circumstances in which police action literally must be “now or never” to preserve the evidence of the crime, it is reasonable to permit action without prior judicial evaluation.<footnotemark>6</footnotemark> See <em>Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#47" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 47-51</a></span> (1970). Cf. <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925). The facts surrounding the “massive seizures” of books in <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span> </em><page-number citation-index="1" label="506">*506</page-number>and <em><span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">A Quantity of Books</a></span>, </em>or the seizure of the film in <em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">Lee Art Theatre</a></span>, </em>presented no such “now or never” circumstances.</p>
<p id="b550-5">II</p>
<p id="b550-6">The film seized in this case was being exhibited at a commercial theater showing regularly scheduled performances to the general public. The seizure proceeded solely on a police officer’s conclusions that the film was obscene; there was no warrant. Nothing prior to seizure afforded a magistrate an opportunity to “focus searchingly on the question of obscenity.” See <em>Heller </em>v. <em>New York, ante, </em>at 488-489; <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#732" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S., at 732</a></span>. If, as <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span> </em>and <em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">Lee Art Theatre</a></span> </em>held, a warrant for seizing allegedly obscene material may not issue on the mere conclusory allegations of an officer, <em>a fortiori, </em>the officer may not make such a seizure with no warrant at all. “The use by government of the power of search and seizure as an adjunct to a system for the suppression of objectionable publications is not new. . . . The Bill of Rights was fashioned against the background of knowledge that unrestricted power of search and seizure could also be an instrument for stifling liberty of expression.” <em>Marcus </em>v. <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#724" aria-description="Citation for case: Marcus v. Search Warrant of Property"><em>Search Warrant, supra, </em>at 724, 729</a></span>. In this case, as in <em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">Lee Art Theatre</a></span>, </em>the admission of the film in evidence requires reversal of petitioner’s conviction. <span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/#637" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">392 U. S., at 637</a></span>.</p>
<p id="b550-7">The judgment of the Court of Appeals of Kentucky is reversed and this case remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b550-8">
<em>Reversed and remanded.</em>
</p>
<p id="b550-9">[For dissenting opinion of Mr. Justice Douglas, see <em>ante, </em>p. 494.]</p>
<footnote label="1">
<p id="b541-8"> Petitioner’s lawyer made the following statement to the trial jury during the closing arguments:</p>
<blockquote id="b541-9">“I would be good enough to tell you at the outset that, in behalf of Mr. Roaden, I am not going to get up here and defend the film observed yesterday nor the revolting scenes in it or try to argue or persuade you that those scenefs] were not obscene.” App. 37.</blockquote>
</footnote>
<footnote label="2">
<p id="b541-10"> Kentucky Revised Statutes §436.101 (1973), reads in relevant part as follows:</p>
<blockquote id="b541-11">“Obscene matter, distribution, penalties, destruction.</blockquote>
<blockquote id="b541-12">“(1) As used in this section:</blockquote>
<blockquote id="b541-13">“(a) 'Distribute' means to transfer possession of, whether with or without consideration.</blockquote>
<blockquote id="b541-14">“(b) ‘Matter’ means any book, magazine, newspaper, or other printed or written material or any picture, drawing, photograph, motion picture, or other pictorial representation or any statue or <page-number citation-index="1" label="498">*498</page-number>other figure, or any recording, transcription or mechanical, chemical or electrical reproduction or any other articles, equipment, machines or materials.</blockquote>
<blockquote id="AMp">“(c) 'Obscene’ means that to the average person, applying contemporary standards, the predominant appeal of the matter, taken as a whole, is to prurient interest, a shameful or morbid interest in nudity, sex, or excretion, which goes substantially beyond customary limits of candor in description or representation of such matters.</blockquote>
<blockquote id="ATl9">“(d) 'Person’ means any individual, partnership, firm, association, corporation, or other legal entity.</blockquote>
<blockquote id="AQz">“(2) Any person who, having knowledge of the obscenity thereof, sends or causes to be sent, or brings or causes to be brought, into this state for sale or distribution, or in this state prepares, publishes, prints, exhibits, distributes, or offers to distribute, or has in his possession with intent to distribute or to exhibit or offer to distribute, any obscene matter is punishable by fine of not more than $1,000 plus five dollars ($5.00) for each additional unit of material coming within the provisions of this chapter, which is involved in the offense, not to exceed ten thousand dollars ($10,000), or by imprisonment in the county jail for not more than six (6) months plus one (1) day for each additional unit of material coming -within the provisions of this chapter, and which is involved in the offense, such basic maximum and additional days not to exceed 360 days in the county jail, or by both such fine and imprisonment. If such person has previously been convicted of a violation of this subsection, he is punishable by fine of not more than $2,000 plus five dollars ($5.00) for each additional unit of material coming within the provisions of this chapter, which is involved in the offense, not to exceed $25,000, or by imprisonment in the county jail for not more than one (1) year, or by both such fine and such imprisonment. If a person has been twice convicted of a violation of this section, a violation of this subsection is punishable by imprisonment in the state penitentiary not exceeding five (5) years.</blockquote>
<blockquote id="A_DJ">“(8) The jury, or the court, if a jury trial is waived, shall render a general verdict, and shall also render a special verdict as to whether the matter named in the charge is obscene. The special <page-number citation-index="1" label="499">*499</page-number>verdict or findings on the issue of obscenity may be: ‘We find the . . . (title or description of matter) to be obscene,’ or, ‘We find the . . . (title or description of matter) not to be obscene/ as they may find each item is or is not obscene.</blockquote>
<blockquote id="Aob">“ (9) Upon the conviction of the accused, the court may, when the conviction becomes final, order any matter or advertisement, in respect whereof the accused stands convicted, and which remains in the possession or under the control of the attorney general, commonwealth’s attorney, county attorney, city attorney or their authorized assistants, or any law enforcement agency, to be destroyed, and the court may cause to be destroyed any such material in its possession or under its control.”</blockquote>
</footnote>
<footnote label="3">
<p id="b545-9"> We vacated the judgment in <em>Hosey </em>v. <em>City of Jackson, </em><span class="citation" data-id="9716282"><a href="/opinion/2096144/hosey-v-city-of-jackson-mississippi/" aria-description="Citation for case: Hosey v. City of Jackson, Mississippi">309 F. Supp. 527</a></span> (SD Miss. 1970), on the grounds of the Court’s policy of noninterference in state prosecution; we did not reach the merits. <em>Hosey </em>v. <em>City of Jackson, </em><span class="citation multiple-matches"><a href="/c/U.%20S./401/987/">401 U. S. 987</a></span> (1971). We also vacated the judgment in <em>Ledesma </em>v. <em>Perez, </em><span class="citation" data-id="9690341"><a href="/opinion/1867767/delta-book-distributors-inc-v-cronvich/" aria-description="Citation for case: Delta Book Distributors, Inc. v. Cronvich">304 F. Supp. 662</a></span> (ED La. 1969), again on the grounds of noninterference with state criminal proceedings prior to adjudications by state courts. <em>Perez </em>v. <em>Ledesma, </em><span class="citation" data-id="9424442"><a href="/opinion/108266/perez-v-ledesma/" aria-description="Citation for case: Perez v. Ledesma">401 U. S. 82</a></span> (1971).</p>
</footnote>
<footnote label="4">
<p id="b547-9"> In <em>Stanford </em>v. <em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">Texas, supra,</a></span> </em>we acknowledged the difference between books and weapons, narcotics, or cases of whiskey.</p>
</footnote>
<footnote label="5">
<p id="b548-6"> This does not mean an adversary proceeding is needed before seizure, since a warrant may be issued <em>ex parte. Heller </em>v. <em>New York, ante, </em>p. 483.</p>
</footnote>
<footnote label="6">
<p id="b549-6"> Counsel for Kentucky, together with counsel for New York in <em>Heller </em>v. <em>New York, ante, </em>at 493, and counsel for California as <em>amicus curiae </em>in <em>Heller, </em>have emphasized that allegedly obscene films are particularly difficult evidence to preserve unless kept in custody. We again take judicial notice that films may be compact, may be easy to destroy or to remove to another jurisdiction, and may be subject to pretrial alterations by cutting out scenes and resplicing reels. See <em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">ibid.</a></span> </em>But, as the <em>Heller </em>case demonstrates, where films are scheduled for exhibition in a commercial theater open to the public, procuring a warrant based on a prior judicial determination of probable cause of obscenity need not risk loss of the evidence.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Robbins v. California.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Robbins v. California
type: case
citation: "453 U.S. 420 (1981)"
parallel_cite: "101 S. Ct. 2841; 69 L. Ed. 2d 744"
neutral_cite: 1981 U.S. LEXIS 132
court: U.S.
court_level: scotus
circuit: ""
year: 1981
date_decided: 1981-07-01
docket: 80-148
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
  opinion_url: "https://www.courtlistener.com/opinion/110558/robbins-v-california/"
  cluster_id: 110558
  opinion_id: null
  identity_checked: true
lake:
  record_id: Robbins v. California
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Automobile Exception]]"
    role: Historical / origin
related:
  - "[[United States v. Ross]]"
  - "[[California v. Acevedo]]"
  - "[[United States v. Chadwick]]"
  - "[[Arkansas v. Sanders]]"
tags:
  - case
  - fourth-amendment
  - automobile-exception
  - containers
  - warrant-requirement
  - overruled
  - historical
holding: "A closed, opaque container found during the lawful search of an automobile may not be opened without a warrant even where police have probable cause — a bright-line container rule the Court overruled one Term later in United States v. Ross (1982)."
---

# Robbins v. California

*453 U.S. 420 (1981)* (No. 80-148) · Supreme Court of the United States · **Historical** · Treatment: **Overruled — rendered as history (⚪ unverified, pending S9)** — overruled by [[United States v. Ross]] (1982)
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the subsequent-history treatment below is authored orientation, not machine-certified. Identity cluster 110558 → 453 U.S. 420, decided 1981-07-01; Rule quote string-matched to the CL opinion text 2026-07-07. -->

## Background
Highway patrol officers stopped Robbins for erratic driving, smelled marihuana, and searched his station wagon. In a recessed luggage compartment they found two packages wrapped in opaque green plastic; they unwrapped them without a warrant and found bricks of marihuana. The California courts upheld the search, and Robbins argued that the closed, opaque packages were entitled to Fourth Amendment protection notwithstanding the lawful search of the car.

## Issue
Whether police who are lawfully searching an automobile may open a closed, opaque container found inside without first obtaining a warrant.

## Rule
The plurality (Stewart, J.) extended *[[United States v. Chadwick|Chadwick]]* and *[[Arkansas v. Sanders|Sanders]]* to any closed container: a piece of luggage or wrapped package found in a car is protected to the same degree as one found anywhere else, and the automobile exception does not reach it. "We reaffirm today that such a container may not be opened without a warrant, even if it is found during the course of the lawful search of an automobile." — 453 U.S. at 428. ^pin-428

## Application
The plurality announced a [[Common Legal Terms#bright-line-rule|bright-line rule]]: absent a recognized exception, a closed, opaque container's contents are shielded from a warrantless search regardless of the container's size or shape. Because no exception applied, the officers should have secured the packages and obtained a warrant; opening them on the roadside violated the Fourth and Fourteenth Amendments.

## Conclusion
The judgment of the California Court of Appeal was **reversed**. Stewart, J., announced the judgment of the Court in a [[Common Legal Terms#plurality-opinion|plurality opinion]].

## Treatment & subsequent history
**Overruled by [[United States v. Ross]] (1982).** *Robbins*'s bright-line container rule survived barely a year. In *[[United States v. Ross|Ross]]* the Court held that when police have probable cause to search a lawfully stopped vehicle, that authority extends to every part of the car and any container within it that might conceal the object of the search — rejecting *Robbins*. *[[California v. Acevedo]]* (1991) then completed the shift, unifying the container rule and overruling *[[Arkansas v. Sanders]]* as well.

*Status note (⚪):* authored from a CourtListener-verified identity stub; the overruled treatment above is well-settled but has not completed the project's two-key certification, so the page renders under the ⚪ banner until S9 promotion. Preserved as **history**, never as live law.

## Appears on
- [[Automobile Exception]] — *Historical / origin*

## Sources
- [*Robbins v. California*, 453 U.S. 420 (1981)](https://www.courtlistener.com/opinion/110558/robbins-v-california/) — pinpoint: 428 (plurality; Stewart, J.); Rule quote string-matched to the CL opinion text 2026-07-07. Overruled by *United States v. Ross*, 456 U.S. 798 (1982) (successor page: [[United States v. Ross]]).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ea37186dbf64d3b6", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Robbins v. California"}, "payload": {"all": [{"cite": "453 U.S. 420", "page": "420", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "453"}, {"cite": "101 S. Ct. 2841", "page": "2841", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "101"}, {"cite": "69 L. Ed. 2d 744", "page": "744", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "69"}, {"cite": "1981 U.S. LEXIS 132", "page": "132", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1981"}], "display": "453 U.S. 420", "official": {"cite": "453 U.S. 420", "page": "420", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "453"}, "official_selection_present": true, "record_id": "Robbins v. California"}}
{"assertion_id": "59d19066a754387c", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Robbins v. California"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Robbins v. California", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Robbins v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Robbins v. California",
  "status": "under_review",
  "identity": {
    "case_name": "Robbins v. California",
    "case_name_short": "Robbins",
    "case_name_full": "Robbins v. California",
    "input_case_name": "Robbins v. California",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1981-07-01",
    "year": 1981,
    "docket": "80-148",
    "cluster_id": 110558,
    "lead_opinion_id": 9428483,
    "sibling_ids": [],
    "absolute_url": "/opinion/110558/robbins-v-california/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "453 U.S. 420",
      "volume": "453",
      "reporter": "U.S.",
      "page": "420",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "101 S. Ct. 2841",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "2841",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 2d 744",
        "volume": "69",
        "reporter": "L. Ed. 2d",
        "page": "744",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1981 U.S. LEXIS 132",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "132",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "453 U.S. 420",
        "volume": "453",
        "reporter": "U.S.",
        "page": "420",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 S. Ct. 2841",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "2841",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 2d 744",
        "volume": "69",
        "reporter": "L. Ed. 2d",
        "page": "744",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1981 U.S. LEXIS 132",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "132",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "453 U.S. 420",
    "official_selection": {
      "court_class": "scotus",
      "selected": "453 U.S. 420",
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
    "date_created": "2026-07-07T13:28:16Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:28:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:28:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:28:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:28:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "robbins-v-california--110558",
      "to_record_id": "Robbins v. California",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Robbins v. California

```
<opinion type="majority">
<author id="b464-4"><page-number citation-index="1" label="422">*422</page-number>Justice Stewart</author>
<p id="A74">announced the judgment of the Court and delivered an opinion, in which Justice Brennan, Justice White, and Justice Marshall joined.</p>
<p id="b464-5">I</p>
<p id="b464-6">On the early morning of January 5, 1975, California Highway Patrol officers stopped the petitioner’s car — a 1966 Chevrolet station wagon — because he had been driving erratically. He got out of his vehicle and walked towards the patrol car. When one of the officers asked him for his driver’s license and the station wagon’s registration, he fumbled with his wallet. When the petitioner opened the car door to get out the registration, the officers smelled marihuana smoke. One of the officers patted down the petitioner, and discovered a vial of liquid. The officer then searched the passenger compartment of the car, and found marihuana as well as equipment for using it.</p>
<p id="b464-7">After putting the petitioner in the patrol car, the officers opened the tailgate of the station wagon, located a handle set flush in the deck, and lifted it up to uncover a recessed luggage compartment. In the compartment were a totebag and two packages wrapped in green opaque plastic.<footnotemark>1</footnotemark> The police unwrapped the packages; each one contained 15 pounds of marihuana.</p>
<p id="b464-8">The petitioner was charged with various drug offenses, his pretrial motion to suppress the evidence found when the <page-number citation-index="1" label="423">*423</page-number>packages were unwrapped was denied, and a jury convicted him. In an unpublished opinion, the California Court of Appeal affirmed the judgment in all relevant respects. This Court granted a writ of certiorari, vacated the Court of Appeal’s judgment, and remanded the case for further consideration in light of <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span>. <span class="citation multiple-matches"><a href="/c/U.%20S./443/903/">443 U. S. 903</a></span>. On remand, the Court of Appeal again found the warrantless opening of the packages constitutionally permissible, since the trial court “could reasonably [have] conclude [d] that the contents of the packages could have been inferred from their outward appearance, so that appellant could not have held a reasonable expectation of privacy with respect to the contents.” <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#40" aria-description="Citation for case: People v. Robbins">103 Cal. App. 3d 34, 40</a></span>, <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#783" aria-description="Citation for case: People v. Robbins">162 Cal. Rptr. 780, 783</a></span>. Because of continuing uncertainty as to whether closed containers found during a lawful warrantless search of an automobile may themselves be searched without a warrant, this Court granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./449/1109/">449 U. S. 1109</a></span>.</p>
<p id="b465-5">II</p>
<p id="b465-6">The Fourth Amendment to the Constitution, which is made applicable to the States through the Fourteenth Amendment, establishes “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures.” This Court has held that a search is <em>per se </em>unreasonable, and thus violates the Fourth Amendment, if the police making the search have not first secured from a neutral magistrate a warrant that satisfies the terms of the Warrant Clause of the Fourth Amendment. See, <em>e. g., Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span>; <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33</a></span>. Although the Court has identified some exceptions to this warrant requirement, the Court has emphasized that these exceptions are “few,” “specifically established,” and “well-delineated.” <em>Katz </em>v. <em>United States, supra, </em>at 357.</p>
<p id="b465-7">Among these exceptions is the so-called “automobile exception.” See <em>Colorado </em>v. <em>Bannister, </em><span class="citation" data-id="110351"><a href="/opinion/110351/colorado-v-bannister/" aria-description="Citation for case: Colorado v. Bannister">449 U. S. 1</a></span>. In <em>Carroll </em><page-number citation-index="1" label="424">*424</page-number>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>, the Court held that a search warrant is unnecessary “where there is probable cause to search an automobile stopped on the highway; the car is movable, the occupants are alerted, and the car’s contents may never be found again if a warrant must be obtained.” <em>Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 51</a></span>. In recent years, we have twice been confronted with the suggestion that this “automobile exception” somehow justifies the warrantless search of a closed container found inside an automobile. Each time, the Court has refused to accept the suggestion.</p>
<p id="b466-5">In <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span>, the Government argued in part that luggage is analogous to motor vehicles for Fourth Amendment purposes, and that the “automobile exception” should thus be extended to encompass closed pieces of luggage. The Court rejected the analogy and insisted that the exception is confined to the special and possibly unique circumstances which were the occasion of its genesis. First, the Court said that “[o]ur treatment of automobiles has been based in part on their inherent mobility, which often makes obtaining a judicial warrant impracticable.” <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#12" aria-description="Citation for case: United States v. Chadwick"><em>Id., </em>at 12</a></span>. While both cars and luggage may be “mobile,” luggage itself may be brought and kept under the control of the police.</p>
<p id="b466-6">Second, the Court acknowledged that “inherent mobility” cannot alone justify the automobile exception, since the Court has sometimes approved warrantless searches in which the automobile’s mobility was irrelevant. See <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 441-442</a></span>; <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#367" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 367</a></span>. The automobile exception, the Court said, is thus also supported by “the diminished expectation of privacy which surrounds the automobile” and which arises from the facts that a car is used for transportation and not as a residence or a repository of personal effects, that a car’s occupants and contents travel in plain view, and that automobiles are necessarily highly regulated by government. <em>United States </em>v. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#12" aria-description="Citation for case: United States v. Chadwick"><em>Chadwick, supra, </em>at 12-13</a></span>. No such dimin<page-number citation-index="1" label="425">*425</page-number>ished expectation of privacy characterizes luggage; on the contrary, luggage typically is a repository of personal effects, the contents of closed pieces of luggage are hidden from view, and luggage is not generally subject to state regulation.</p>
<p id="b467-5">In <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span>, the State of Arkansas argued that the “automobile exception” should be extended to allow the warrantless search of everything found in an automobile during a lawful warrantless search of the vehicle itself. The Court rejected this argument for much the same reason it had rejected the Government’s argument in <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>. </em>Pointing out, first, that “[o]nce police have seized a suitcase, as they did here, the extent of its mobility is in no way affected by the place from which it was taken,” the Court said that there generally “is no greater need for war-rantless searches of luggage taken from automobiles than of luggage taken from other places.” <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#763" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 763-764</a></span>. Second, the Court saw no reason to believe that the privacy expectation in a closed piece of luggage taken from a car is necessarily less than the privacy expectation in closed pieces of luggage found elsewhere.</p>
<p id="b467-6">In the present case, the Court once again encounters the argument — made in the Government’s brief as <em>amicus </em>curiae— that the contents of a closed container carried in a vehicle are somehow not fully protected by the Fourth Amendment. But this argument is inconsistent with the Court’s decisions in <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>and <em>Sanders. </em>Those cases made clear, if it was not clear before, that a closed piece of luggage found in a lawfully searched car is constitutionally protected to the same extent as are closed pieces of luggage found anywhere else.</p>
<p id="b467-7">The .respondent, however, proposes that the <em>nature </em>of a container may diminish the constitutional protection to which it otherwise would be entitled — that the Fourth Amendment protects only containers commonly used to transport “personal effects.” By personal effects the respondent means property worn on or carried about the person or having some intimate relation to the person. In taking this position, the <page-number citation-index="1" label="426">*426</page-number>respondent relies on numerous opinions that have drawn a distinction between pieces of sturdy luggage, like suitcases, and flimsier containers, like cardboard boxes. Compare, <em>e. g., United States </em>v. Benson, <span class="citation" data-id="9467155"><a href="/opinion/382715/united-states-v-jeffrey-joseph-benson/" aria-description="Citation for case: United States v. Jeffrey Joseph Benson">631 F. 2d 1336</a></span> (CA8 1980) (leather totebag); <em>United States </em>v. <em>Miller, </em><span class="citation" data-id="371228"><a href="/opinion/371228/united-states-v-clifford-jerome-miller-and-kathelyn-vandraiss-miller/" aria-description="Citation for case: United States v. Clifford Jerome Miller and Kathelyn...">608 F. 2d 1089</a></span> (CA5 1979) (plastic portfolio); <em>United States </em>v. <em>Presler, </em><span class="citation" data-id="372532"><a href="/opinion/372532/united-states-v-lee-alton-presler-aka-robert-ray-presler-aka-robert/" aria-description="Citation for case: United States v. Lee Alton Presler, A/K/A Robert Ray...">610 F. 2d 1206</a></span> (CA4 1979) <em>(briefcase); United States </em>v. <em>Meier, </em><span class="citation" data-id="368269"><a href="/opinion/368269/united-states-v-paul-william-meier/" aria-description="Citation for case: United States v. Paul William Meier">602 F. 2d 253</a></span> (CA10 1979) (backpack); <em>United States </em>v. <em>Johnson, </em><span class="citation" data-id="9465310"><a href="/opinion/361214/united-states-v-dennis-michael-johnson-and-stephen-arthur-baldwin/" aria-description="Citation for case: United States v. Dennis Michael Johnson, and Stephen...">588 F. 2d 147</a></span> (CA5 1979) <em>(duffelbag); United States </em>v. <em>Stevie, </em><span class="citation" data-id="9465095"><a href="/opinion/359034/united-states-v-robert-charles-stevie-united-states-of-america-v-raymond/" aria-description="Citation for case: United States v. Robert Charles Stevie, United States of...">582 F. 2d 1175</a></span> (CA8 1978), with <em>United States </em>v. <em>Mannino, </em><span class="citation" data-id="384549"><a href="/opinion/384549/united-states-v-paul-mannino/" aria-description="Citation for case: United States v. Paul Mannino">635 F. 2d 110</a></span> (CA2 1980) (plastic bag inside paper bag); <em>United States </em>v. <em>Goshorn, </em><span class="citation" data-id="381355"><a href="/opinion/381355/united-states-v-arthur-k-goshorn/#699" aria-description="Citation for case: United States v. Arthur K. Goshorn">628 F. 2d 697, 699</a></span> (CA1 1980) (“([t]wo plastic bags, further in three brown paper bags, further in two clear plastic bags’ ”); <em>United States </em>v. <em>Gooch, </em><span class="citation" data-id="9465960"><a href="/opinion/368494/united-states-v-william-daniel-gooch-jr/" aria-description="Citation for case: United States v. William Daniel Gooch, Jr.">603 F. 2d 122</a></span> (CA10 1979) (plastic bag); <em>United States </em>v. <em>Mackey, </em><span class="citation" data-id="9466932"><a href="/opinion/380505/united-states-v-osborne-mackey/" aria-description="Citation for case: United States v. Osborne MacKey">626 F. 2d 684</a></span> (CA9 1980) (paper bag); <em>United States </em>v. <em>Neumann, </em><span class="citation" data-id="360237"><a href="/opinion/360237/united-states-v-bradley-raymond-neumann/" aria-description="Citation for case: United States v. Bradley Raymond Neumann">585 F. 2d 355</a></span> (CA8 1978) (cardboard box).</p>
<p id="b468-5">The respondent’s argument cannot prevail for at least two reasons. First, it has no basis in the language or meaning of the Fourth Amendment. That Amendment protects people and their effects, and it protects those effects whether they are “personal” or “impersonal.” The contents of Chadwick’s footlocker and Sanders’ suitcase were immune from a warrantless search because they had been placed within a closed, opaque container and because Chadwick and Sanders had thereby reasonably “manifested an expectation that the contents would remain free from public examination.” <em>United States </em>v. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#11" aria-description="Citation for case: United States v. Chadwick"><em>Chadwick, supra, </em>at 11</a></span>. Once placed within such a container, a diary and a dishpan are equally protected by the Fourth Amendment.</p>
<p id="b468-6">Second, even if one wished to import such a distinction into the Fourth Amendment, it is difficult if not impossible to perceive any objective criteria by which that task might be accomplished. What one person may put into a suitcase, another may put into a paper bag. <em>United States </em>v. <em>Ross, </em><page-number citation-index="1" label="427">*427</page-number>210 U. S. App. D. C. 342, <span class="citation" data-id="9468224"><a href="/opinion/392944/united-states-v-albert-ross-jr/" aria-description="Citation for case: United States v. Albert Ross, Jr.">655 F. 2d 1159</a></span> (1981) (en banc). And as the disparate results in the decided cases indicate, no court, no constable, no citizen, can sensibly be asked to distinguish the relative “privacy interests” in a closed suitcase, briefcase, portfolio, duffelbag, or box.</p>
<p id="b469-5">The respondent protests that footnote 13 of the <em>Sanders </em>opinion says that “[n]ot all containers and packages found by police during the course of a search will deserve the full protection of the Fourth Amendment.” <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 764, n. 13</a></span>. But the exceptions listed in the succeeding sentences of the footnote are the very model of exceptions which prove the rule: “Thus, some containers (for example a kit of burglar tools or a gun case) by their very nature cannot support any reasonable expectation of privacy because their contents can be inferred from their outward appearance. Similarly, in some cases the contents of a package will be open to ‘plain view/ thereby obviating the need for a warrant.” <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders"><em>Id., </em>at 764-765, n. 13</a></span>. The second of these exceptions obviously refers to items in a container that is not closed. The first exception is likewise little more than another variation of the “plain view” exception, since, if the distinctive configuration of a container proclaims its contents, the contents cannot fairly be said to have been removed from a searching officer’s view. The same would be true, of course, if the container were transparent, or otherwise clearly revealed its contents. In short, the negative implication of footnote 13 of the <em>Sanders </em>opinion is that, unless the container is such that its contents may be said to be in plain view, those contents are fully protected by the Fourth Amendment.</p>
<p id="b469-6">The California Court of Appeal believed that the packages in the present case fell directly within the second exception described in this footnote, since “[a]ny experienced observer could have inferred from the appearance of the packages that they contained bricks of marijuana.” <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#40" aria-description="Citation for case: People v. Robbins">103 Cal. App. 3d, at 40</a></span>, <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#783" aria-description="Citation for case: People v. Robbins">162 Cal. Rptr., at 783</a></span>. The only evidence the court <page-number citation-index="1" label="428">*428</page-number>cited to support this proposition was the testimony of one of the officers who arrested the petitioner. When asked whether there was anything about “these two plastic wrapped green blocks which attracted your attention,” the officer replied, somewhat obscurely:</p>
<blockquote id="b470-5">“A. I had previous knowledge of transportation of such blocks. Normally contraband is wrapped this way, merely hearsay. I had never seen them before.</blockquote>
<blockquote id="b470-6">“Q. You had heard contraband was packaged this way?</blockquote>
<blockquote id="b470-7">“A. Yes.” <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#40" aria-description="Citation for case: People v. Robbins"><em>Id., </em>at 40, n. 2</a></span>, <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#783" aria-description="Citation for case: People v. Robbins">162 Cal. Rptr., at 783, n. 4</a></span>.</blockquote>
<p id="b470-8">This vague testimony certainly did not establish that marihuana is ordinarily “packaged this way.” Expectations of privacy are established by general social norms, and to fall within the second exception of the footnote in question a container must so clearly announce its contents, whether by its distinctive configuration, its transparency, or otherwise, that its contents are obvious to an observer. If indeed a green plastic wrapping reliably indicates that a package could only contain marihuana, that fact was not shown by the evidence of record in this case.<footnotemark>2</footnotemark></p>
<p id="b470-9">Although the two bricks of marihuana were discovered during a lawful search of the petitioner’s car, they were inside a closed, opaque container. We reaffirm today that such a container may not be opened without a warrant, even if it is found during the course of the lawful search of an automobile. Since the respondent does not allege the presence of any circumstances that would constitute a valid exception <page-number citation-index="1" label="429">*429</page-number>to this general rule,<footnotemark>3</footnotemark> it is clear that the opening of the closed containers without a search warrant violated the Fourth and Fourteenth Amendments. Accordingly, the judgment of the California Court of Appeal is reversed.</p>
<p id="b471-5">
<em>It is so ordered.</em>
</p>
<p id="b471-6">The Chief Justice concurs in the judgment.</p>
<footnote label="1">
<p id="b464-9"><em> ‘■A </em>photograph was made of one of the packages, and it was later described as follows:</p>
<blockquote id="b464-10">“The package visible in the photograph is apparently wrapped or boxed in an opaque material covered by an outer wrapping of transparent, cellophane-type plastic. (The photograph is not in color, and the ‘green’ plastic cannot be seen at all.) Both wrappings are sealed on the outside with at least one strip of opaque tape. As thus wrapped and sealed, the package roughly resembles an oversized, extra-long cigar box with slightly rounded corners and edges. It bears no legend or other written indicia supporting any inference concerning its contents.” <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#44" aria-description="Citation for case: People v. Robbins">103 Cal. App. 3d 34, 44</a></span>, <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#785" aria-description="Citation for case: People v. Robbins">162 Cal. Rptr. 780, 785</a></span> (Rattigan, J., dissenting).</blockquote>
</footnote>
<footnote label="2">
<p id="b470-10"> As Judge Rattigan wrote in his dissenting opinion in the California Court of Appeal: “For all that I see, it could contain books, stationery, canned goods, or any number of other wholly innocuous items which might be heavy in weight. In fact, it bears a remarkable resemblance to an unlabelled carton of emergency highway flares that I bought from a store shelf and have carried in the trunk of my own automobile.” <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#44" aria-description="Citation for case: People v. Robbins">103 Cal. App. 3d, at 44</a></span>, <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#785" aria-description="Citation for case: People v. Robbins">162 Cal. Rptr., at 785</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b471-9"> In particular, it is not argued that the opening of the packages was incident to a lawful custodial arrest. Cf. <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span>. See <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 764, n. 11</a></span>. Further, the respondent does not argue that the petitioner consented to the opening of the packages.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Robinson v. Commonwealth.json  (`lake-record`, 1 assertions)

### content_page

```
---
title: Robinson v. Commonwealth
type: case
citation: "No. 1912-24-1, slip op. (Virginia 2026)"
parallel_cite: ""
neutral_cite: ""
court: Va. Ct. App.
court_level: state
circuit: ""
year: 2026
date_decided: 2026-04-07
docket: 1912-24-1
authority_weight: "Persuasive — state, illustrative"
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
  opinion_url: "https://www.courtlistener.com/opinion/10838748/eddie-eugene-robinson-v-commonwealth-of-virginia/"
  cluster_id: 10838748
  opinion_id: null
  identity_checked: false
lake:
  record_id: Robinson v. Commonwealth
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Lower-court development (ALPR network)"
related:
  - "[[Carpenter v. United States]]"
  - "[[United States v. Knotts]]"
  - "[[United States v. Jones]]"
tags:
  - case
  - fourth-amendment
  - digital-surveillance
  - automatic-license-plate-reader
  - flock
  - carpenter
  - third-party-doctrine
  - virginia-court-of-appeals
holding: "A police query of a network of fixed automatic license plate reader (Flock) cameras that photograph plates and vehicle exteriors on public roads and retain the data for 30 days is not a Fourth Amendment search on this record, because the system captures only a vehicle's public movements and does not create the kind of comprehensive chronicle of a person's life that Carpenter found to invade a reasonable expectation of privacy; the warrantless database query therefore required no warrant."
aliases:
  - Robinson v. Commonwealth
  - "Robinson v. Commonwealth (Va. Ct. App. 2026)"
  - Eddie Eugene Robinson v. Commonwealth
---

# Robinson v. Commonwealth

*No. 1912-24-1, slip op. (Virginia 2026)* · Court of Appeals of Virginia · **Persuasive — state, illustrative** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10838748 → published opinion 11306090 (Beales, J.; Record No. 1912-24-1, decided Apr. 7, 2026). Rule quote string-matched to the CL opinion text 2026-07-07; slip-style pin (published Va. Ct. App. slip; no S.E.2d/Va. App. reporter cite assigned yet — S2 A3). S9 promotes. -->

## Background
The City of Norfolk operates 172 fixed Flock Safety cameras at intersections on public roads; they photograph passing vehicles and their plates, recording the plate number, color, make, model, and identifying features, and store the data for 30 days. After a string of predawn commercial burglaries, an investigator matched a stolen lottery ticket to surveillance footage of a white BMW SUV with distinctive black rims. Detective Gross queried the Flock database for that vehicle near the location and time, obtained one image showing the plate, ran the plate through DMV records, and identified Eddie Eugene Robinson. Robinson entered conditional guilty pleas after the circuit court denied his motion to suppress the Flock-derived evidence.

## Issue
Whether a police query of Norfolk's Flock automatic license plate reader system is a Fourth Amendment search requiring a warrant.

## Rule
A search occurs when the government invades a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]], and under *[[Carpenter v. United States]]* some digital dragnets — like long-term cell-site location tracking — do so by creating "a comprehensive chronicle" of a person's movements. But the court held this system different: "We decline to speculate as to when — or if — the Flock cameras could create such 'a comprehensive chronicle' of a person's movements where that person would then have a reasonable expectation of privacy. The search of the Flock database in this case was not an unreasonable search in violation of the Fourth Amendment." — slip op. at 9. ^pin-slip9

## Application
Distinguishing *[[Carpenter v. United States|Carpenter]]* and the Fourth Circuit's aerial-surveillance decision in *Leaders of a Beautiful Struggle*, the court reasoned that the Norfolk Flock system took discrete pictures of a vehicle's plate and exterior as it moved on public thoroughfares — where there is no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in one's movements or license plate — and could not track a vehicle in real time. On the current record and this configuration, the system did not amass the pervasive, all-encompassing record that made cell-site tracking a search. The Fourth Amendment therefore imposed no warrant requirement on the database query.

## Conclusion
**Affirmed.** On this record the police were not required under the Fourth Amendment to obtain a search warrant to access the Flock system. Judge Beales wrote the published opinion.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Robinson* is a frontier state-court application of *[[Carpenter v. United States|Carpenter]]* to fixed ALPR networks, expressly fact-bound and explicitly declining to say whether a denser or longer-retained system might cross the line. It is persuasive, illustrative authority on the third-party-doctrine/digital-surveillance frontier, not binding federal precedent, and the "comprehensive chronicle" question it reserves remains open.

## Appears on
- [[Third-Party Doctrine & CSLI]] — *Lower-court development (ALPR network)*

## Sources
- [*Eddie Eugene Robinson v. Commonwealth of Virginia*, No. 1912-24-1, slip op. (Va. Ct. App. 2026)](https://www.courtlistener.com/opinion/10838748/eddie-eugene-robinson-v-commonwealth-of-virginia/) — pinpoint: slip op. at 9 (Flock ALPR query not a Fourth Amendment search on this record). Rule quote string-matched to the CL opinion text 2026-07-07. Published Va. Ct. App. slip; no S.E.2d/Va. App. reporter cite assigned yet (S2 A3 slip precedent).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e452b8c532a1a61b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Robinson v. Commonwealth"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Robinson v. Commonwealth", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Robinson v. Commonwealth

```json
{
  "schema_version": "s2.v1",
  "record_id": "Robinson v. Commonwealth",
  "status": "under_review",
  "identity": {
    "case_name": "Eddie Eugene Robinson v. Commonwealth of Virginia",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "Robinson v. Commonwealth",
    "court": "Va. Ct. App.",
    "court_id": null,
    "court_level": "state",
    "circuit": null,
    "state": "Virginia",
    "date_decided": "2026-04-07",
    "year": 2026,
    "docket": "1912-24-1",
    "cluster_id": 10838748,
    "lead_opinion_id": 11306090,
    "sibling_ids": [],
    "absolute_url": "/opinion/10838748/eddie-eugene-robinson-v-commonwealth-of-virginia/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [],
    "all": [],
    "display": null,
    "official_selection": {
      "court_class": "state",
      "selected": null,
      "reason": "no_official_class_citation"
    },
    "slip_only": true,
    "slip_only_provenance": {
      "source": "R8-R3-web-cites.jsonl",
      "as_of": "2026-07-07",
      "by": "s6-slip-stamp",
      "note": "W9 RE-STAMP after pre-W5 re-key (prior stamp was on superseded cluster 10793178). Eddie Eugene Robinson v. Commonwealth of Virginia, Va. Ct. App. PUBLISHED slip, Record No. 1912-24-1, decided 2026-04-07 (Flock ALPR digital surveillance). CL cluster 10838748 Published, citations[] empty (live-verified 2026-07-07); no S.E.2d/Va. App. reporter cite assigned yet.",
      "legs": [
        {
          "source": "Court PDF",
          "url": "https://www.vacourts.gov/static/opinions/opncavwp/1912241.pdf",
          "cite": "Record No. 1912-24-1, published 2026-04-07"
        },
        {
          "source": "CourtListener",
          "url": "https://www.courtlistener.com/opinion/10838748/eddie-eugene-robinson-v-commonwealth-of-virginia/",
          "cite": "cluster 10838748 Published, citations[] empty"
        }
      ]
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
    "date_created": "2026-07-07T18:26:46Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:26:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:26:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:26:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:26:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "robinson-v-commonwealth--10838748",
      "to_record_id": "Robinson v. Commonwealth",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Robinson v. Commonwealth

```
                         COURT OF APPEALS OF VIRGINIA

                                      Record No. 1912-24-1


                                EDDIE EUGENE ROBINSON
                                          v.
                              COMMONWEALTH OF VIRGINIA


Present: Judges Beales, Malveaux and Frucci
Argued at Norfolk, Virginia
                                                                      Opinion Issued April 7, 2026


                FROM THE CIRCUIT COURT OF THE CITY OF NORFOLK
                             Jamilah D. LeCruise, Judge1

J. Barry McCracken, Assistant Public Defender, for appellant.

Israel-David J.J. Healy, Assistant Attorney General (Jason S. Miyares,2 Attorney General, on
brief), for appellee.


                                 PUBLISHED OPINION BY
                               JUDGE RANDOLPH A. BEALES

       Eddie Eugene Robinson entered conditional guilty pleas to three felony charges of

statutory burglary in violation of Code § 18.2-91, one felony charge of larceny of lottery tickets

in violation of Code § 58.1-4018.1(A), one charge of grand larceny in violation of Code

§ 18.2-95(ii), and one charge of being a nonviolent felon in possession of a firearm in violation

of Code § 18.2-308.2(A). On appeal, Robinson contends that the circuit court erred in denying

his motion to suppress evidence from automatic license plate reader cameras made by Flock




       1
         Judge David W. Lannetti denied Robinson’s motion to suppress, which is the issue
before the Court in this appeal.
       2
           Jay C. Jones succeeded Jason S. Miyares as Attorney General on January 17, 2026.
Safety (“Flock cameras”), arguing that the evidence was obtained in violation of the Fourth

Amendment.

                                       I. BACKGROUND3

       In 2023, the City of Norfolk installed a system of 172 cameras at intersections on public

roadways throughout Norfolk. They capture still images of cars and their license plates and store

the information—the license plate number, the color, manufacturer, and model of the car, as well

as any identifying characteristics such as roof racks or bumper stickers—on servers for 30 days.

Norfolk Police detectives have access to the database, and they can use it to search for particular

vehicles in particular places. Police can narrow their search of the Flock database by location or

timeframe but generally cannot track a vehicle in real time.

       Over the course of three weeks in November 2023, several commercial storefronts in

Norfolk were broken into and a number of items stolen, all in the early hours of the morning.

The first of these occurred on November 5, 2023, at around 3:50 a.m., when someone broke into

Nu Beauty Supply. The owner reported that money and merchandise had been stolen.

Surveillance footage of the burglary showed that the perpetrator was wearing a hoodie, a head

covering, a medical mask, and duck boots.

       On November 12, 2023, at around 3:00 a.m., someone broke into George’s Seafood. The

owner reported that money and an iPad had been stolen. Surveillance footage of the burglary

showed that the perpetrator was wearing a hoodie, a backpack, a face mask, and duck boots.

       On November 29, 2023, at around 4:00 a.m., someone broke into Quick Serve. The

owner reported that money and lottery tickets had been stolen. Surveillance footage of the

burglary showed a black male wearing a hoodie, a backpack, and duck boots.


       3
         “In reviewing the denial of a motion to suppress, we ‘consider the facts in the light most
favorable to the Commonwealth, the prevailing party at trial.’” Aponte v. Commonwealth, 68
Va. App. 146, 156 (2017) (quoting Hairston v. Commonwealth, 67 Va. App. 552, 560 (2017)).
                                               -2-
       Adam Hankins, an investigator at Virginia Lottery, entered the numbers of the stolen

lottery tickets into a database that alerts investigators if someone attempts to cash them in. At

9:15 a.m. on November 29, 2023, the same day that Quick Serve was broken into, the database

notified Investigator Hankins that someone had attempted to cash in one of the stolen tickets at

Miller’s Store, a gas station in Norfolk. Investigator Hankins accessed the surveillance footage

from Miller’s and, believing the person depicted at Miller’s to match the description of the

person who broke into Quick Serve, shared still photographs from the footage with the Norfolk

Police Department. One of the photographs showed a white BMW SUV with black rims but did

not show the car’s license plate.

       Knowing that there were two Flock cameras near Miller’s, Norfolk Police Detective

Kevin Gross entered the make and model of the vehicle into the Flock system, limiting his search

to the two hours surrounding the burglary. The Flock system returned one image of a white

BMW with black rims, and its license plate.4 Detective Gross then looked up the license plate

number in a Virginia Department of Motor Vehicles database, which revealed Robinson as the

car’s registered owner. The DMV search also yielded a photo of Robinson, whom Detective

Gross determined to be the same person depicted in the footage of the burglary at Quick Serve.

       Detective Gross obtained an arrest warrant for Robinson, and Robinson was arrested on

December 4, 2023. Detective Gross also obtained a search warrant for Robinson’s home, in

which officers found lottery tickets stolen from Quick Serve, checks made out to George’s

Seafood, and beauty products sold by Nu Beauty Supply. Officers also found a firearm in




       4
          Detective Gross could not recall how many white BMW SUVs the Flock system
returned but was able to identify Robinson’s vehicle because of its “distinctive black rims.” He
testified, “Not many pictures that I [had] seen while looking at that data had black rims.”
                                                -3-
Robinson’s home. Robinson was charged with felony burglary, grand larceny, and larceny of

lottery tickets.5

        Robinson moved to suppress, arguing that the warrantless search of the Flock database

violated the Fourth Amendment and that the evidence obtained as a result of the Flock search—

the stolen property and weapon found in his home—should be suppressed. After a hearing, the

circuit court denied Robinson’s motion to suppress.

        Robinson entered conditional guilty pleas to three felony charges of statutory burglary,

one felony charge of larceny of lottery tickets, one charge of grand larceny, and one charge of

being a nonviolent felon in possession of a firearm. Robinson now appeals to this Court.

                                          II. ANALYSIS

        Robinson argues,

                        The trial court erred in denying the Appellant’s motion to
                suppress the warrantless obtaining of location and movement data
                of the Appellant’s vehicle by police from the collection and storage
                of license plate and location information by means of the Flock
                System which constituted a search within the meaning of the
                Fourth Amendment requiring a warrant.

                                      A. Standard of Review

        “The law regarding appellate review of a trial court’s decision on a motion to suppress is

well settled. The appellant bears the burden of establishing that reversible error occurred.”

Williams v. Commonwealth, 71 Va. App. 462, 474 (2020) (quoting Glenn v. Commonwealth, 275

Va. 123, 130 (2008)). “A defendant’s claim that evidence was seized in violation of the Fourth

Amendment presents a mixed question of law and fact.” Jones v. Commonwealth, 277 Va. 171,



        5
         Robinson was indicted for several other commercial burglaries: T&T Seafood Market,
Cajun Seafood, Golden City Chinese Food, Mina Seafood, and Latiendita Costa Del Mar. The
Commonwealth later nolle prossed several of these charges in exchange for Robinson’s
conditional guilty plea. Robinson stipulated to the burglaries of Nu Beauty Supply, George’s
Seafood, and Quick Serve.
                                               -4-
177 (2009) (quoting McCain v. Commonwealth, 275 Va. 546, 551-52 (2008)). “We are bound

by the trial court’s factual findings unless those findings are plainly wrong or unsupported by the

evidence.” Whitaker v. Commonwealth, 279 Va. 268, 273-74 (2010) (quoting Whitehead v.

Commonwealth, 278 Va. 300, 306-07 (2009)). This “Court reviews de novo the overarching

question of whether a search or seizure violated the Fourth Amendment.” Williams, 71 Va. App.

at 475 (citing Glenn, 275 Va. at 130). “Whether a particular governmental intrusion is

reasonable within the meaning of the Fourth Amendment depends upon the particular facts and

circumstances of the case.” Bennett v. Commonwealth, 212 Va. 863, 865 (1972) (citing Cabbler

v. Commonwealth, 212 Va. 520, 522 (1971)).

                        B. The Flock System and the Fourth Amendment

       The Fourth Amendment provides that the “right of the people to be secure in their

persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be

violated.” U.S. CONST. amend. IV. The “basic purpose of this Amendment . . . is to safeguard

the privacy and security of individuals against arbitrary invasions by governmental officials.”

Camara v. Municipal Court of City and County of San Francisco, 387 U.S. 523, 528 (1967).

Therefore, a search without a warrant is “presumptively unreasonable.” Bryant v.

Commonwealth, 72 Va. App. 179, 187-88 (2020) (quoting Glenn, 275 Va. at 130).

       “Since Katz v. United States, the touchstone of [Fourth] Amendment analysis has been

the question whether a person has a ‘constitutionally protected reasonable expectation of

privacy.’” Rideout v. Commonwealth, 62 Va. App. 779, 786 (2014) (alteration in original)

(citation omitted) (quoting Oliver v. United States, 466 U.S. 170, 177 (1984)). In other words, a

search violates the Fourth Amendment if it invades a person’s reasonable expectation of privacy.

       New technology often “does not fit neatly under existing precedents.” Carpenter v.

United States, 585 U.S. 296, 306 (2018). “[A]s technology continues to enhance the

                                               -5-
‘Government’s ability to encroach upon areas normally guarded from inquisitive eyes,’ courts

must assure that individuals maintain the ‘degree of privacy against government that existed

when the Fourth Amendment was adopted.’” United States v. Martin, 753 F. Supp. 3d 454, 462

(E.D. Va. 2024) (quoting Carpenter, 585 U.S. at 305). See also Kyllo v. United States, 533 U.S.

27, 34 (2001).

       In Knotts, police installed a beeper in a container of chloroform that allowed them to

track the container’s location as it was driven on public highways. United States v. Knotts, 460

U.S. 276, 278-79 (1983). The United States Supreme Court held that the warrantless use of the

beeper was constitutional because “[n]othing in the Fourth Amendment prohibited the police

from augmenting the sensory faculties bestowed upon them at birth with such enhancement as

science and technology afforded them in this case.” Id. at 282 (citing United States v. Lee, 274

U.S. 559, 563 (1927)).

       In Carpenter, the United States Supreme Court held that accessing a person’s cell-site

location information (“CSLI”) required a search warrant because CSLI “provides an all-

encompassing record of the holder’s whereabouts.” 585 U.S. at 311. In that case, the CSLI

captured 127 days of Carpenter’s movements, with an average of 101 data points per day. Id. at

302. The United States Supreme Court stated that CSLI “provides an intimate window into a

person’s life, revealing not only his particular movements, but through them his ‘familial,

political, professional, religious, and sexual associations’” because “[a] cell phone faithfully

follows its owner beyond public thoroughfares and into private residences, doctor’s offices,

political headquarters, and other potentially revealing locales.” Id. at 310-11 (quoting United

States v. Jones, 565 U.S. 400, 415 (2012)). “Accordingly, when the Government tracks the

location of a cell phone it achieves near perfect surveillance, as if it had attached an ankle

monitor to the phone’s user.” Id. at 311-12. The Court held that using CSLI to create and

                                                -6-
maintain a comprehensive chronicle of a person’s movements for a period of over 100 days

invaded that person’s reasonable expectation of privacy. Id. at 311, 313. Thus, the Supreme

Court held, accessing the data was a search within the meaning of the Fourth Amendment and

required a search warrant. Id. at 316.

       Finally, in Leaders of a Beautiful Struggle, the United States Court of Appeals for the

Fourth Circuit, sitting en banc, held that an aerial surveillance program that tracked the

movements of people and vehicles in Baltimore violated the Fourth Amendment because its

extensive tracking of city residents revealed “intimate details through habits and patterns.”

Leaders of a Beautiful Struggle v. Baltimore Police Department, 2 F.4th 330, 341 (4th Cir. 2021)

(en banc). The cameras were operated from the air twelve hours a day—only during daylight—

and covered ninety percent of the city. Id. at 334. The data was retained for 45 days. Id. The

court applied Carpenter in holding that a search warrant was required to access the system. Id.

at 341-42.

       These precedents guide our review. As our Supreme Court has instructed, “Whether a

particular governmental intrusion is reasonable within the meaning of the Fourth Amendment

depends upon the particular facts and circumstances of the case.” Bennett, 212 Va. at 865 (citing

Cabbler, 212 Va. at 522). We find that the use of the Flock system in this case is similar to

Knotts, but significantly factually distinguishable from both Carpenter and Leaders of a

Beautiful Struggle.

       As a threshold matter, Robinson had no reasonable expectation of privacy in the physical

characteristics of his vehicle as he drove it down a public street. In the case now before us, as in

Knotts, the use of the Flock cameras did not constitute a search because “the movements of the

vehicle . . . had been ‘voluntarily conveyed to anyone who wanted to look.’” Carpenter, 585

U.S. at 306 (quoting Knotts, 460 U.S. at 281). Indeed, as this Court has recently stated, “A

                                                -7-
person driving his vehicle on a public street with his license plate in plain view has no reasonable

expectation of privacy that his vehicle and license plate will not be seen by other persons,

including law enforcement officers.” Commonwealth v. Church, No. 0737-25-1, slip op. at 4,

2025 Va. App. LEXIS 627, at *5 (Oct. 14, 2025) (citing Knotts, 460 U.S. at 281).

       Moreover, it simply cannot be said that the City of Norfolk’s system of Flock cameras

amounted to “near perfect surveillance.” Carpenter, 585 U.S. at 312. The 172 Flock cameras

situated throughout Norfolk are not as intrusive as the cell towers in Carpenter that monitor the

movement of cell phones both inside and outside of homes and buildings—or the surveillance of

a city from the air in Leaders of a Beautiful Struggle. The images captured by the Flock cameras

are of vehicles, not persons, and the only pieces of information collected—license plates and

physical characteristics of the vehicle—are already publicly viewable to anyone who sees the

vehicle on the street. The search of the Flock system yielded a photo of Robinson’s car as it

passed down a public highway. The cameras did not continuously monitor all of his travels

around the city and did not create an “intimate window” of Robinson’s overall movements and

associations. See, e.g., Schmidt v. City of Norfolk, ___ F. Supp. 3d ___, ___ (E.D. Va. 2026)

(noting that the Flock cameras appear intermittently “across the many miles of Norfolk roadways

such that they are incapable of cataloging the whole of vehicles’ movements”). Unlike in

Carpenter and Leaders of a Beautiful Struggle, the Flock system takes only still images of a

vehicle’s exterior as it passes down public thoroughfares—not of the person. It is not “a detailed

chronicle of a person’s physical presence compiled every day, every moment, over several

years.” Carpenter, 585 U.S. at 315.

       Thus, Detective Gross did not have to obtain a search warrant to access the Flock system

because he was merely requesting information that showed still images of a vehicle in which

Robinson did not have a reasonable expectation of privacy. In addition, the Flock cameras did

                                               -8-
not augment police officers’ sensory faculties to an impermissible degree. The cameras

interspersed along public roads throughout the City of Norfolk are hardly analogous to the 127

days of cell-site location information at issue in Carpenter, and the images are only stored on

servers for 30 days. The scope and scale of the information captured by the Flock cameras are

also not analogous to the aerial surveillance of every movement of virtually every resident of

Baltimore for twelve hours a day that the Fourth Circuit considered in Leaders of a Beautiful

Struggle. For all of these reasons, we therefore hold that the use of the Flock system in this case

did not constitute a search that violated the Fourth Amendment.

       We are also persuaded by recent federal cases that have already addressed the Flock

systems in Richmond and Norfolk. See United States v. Martin, 753 F. Supp. 3d 454 (E.D. Va.

2024) (Richmond); Schmidt, ___ F. Supp. 3d at ___ (Norfolk). While not binding on this Court,

we find these federal district court decisions instructive as they concern the same system of

cameras as in the case now before this Court. In Martin, the United States District Court for the

Eastern District of Virginia held that police officers in Richmond and Chesterfield County did

not violate any reasonable expectation of privacy by using information obtained from the Flock

system in their investigation of the defendant, Martin. 753 F. Supp. 3d at 476. In that case, out

of 2,500 photographs taken of vehicles in a 30-day period, only three were of the defendant’s

vehicle. Id. at 472. In Schmidt, the court held that the City of Norfolk’s system of Flock

cameras—the very same system at issue in the case now before this Court—did not violate the

plaintiffs’ Fourth Amendment rights and awarded summary judgment to the City of Norfolk.6

___ F. Supp. 3d at ___. Both Martin and Schmidt distinguished Carpenter and Leaders of a




       6
       In Schmidt, the plaintiffs brought suit under 42 U.S.C. § 1983 and the Declaratory
Judgment Act.
                                               -9-
Beautiful Struggle, finding that those cases involved much more invasive searches. Martin, 753

F. Supp. 3d at 471-73; Schmidt, ___ F. Supp. 3d at ___.

       The Virginia Supreme Court has stated that an assessment of whether a new technology

runs afoul of the Fourth Amendment is a fact-based inquiry. See Bennett, 212 Va. at 865. See

also Martin, 753 F. Supp. 3d at 476 (“This Court must rule on the facts as they are and may not

speculate about what the future may hold for Flock’s capabilities.”). We must decide each case

on its facts and therefore our decision is based on the current system of Flock cameras in the City

of Norfolk. We decline to speculate as to when—or if—the Flock cameras could create such “a

comprehensive chronicle” of a person’s movements where that person would then have a

reasonable expectation of privacy. Carpenter, 585 U.S. at 300. The search of the Flock database

in this case was not an unreasonable search in violation of the Fourth Amendment.

                                       III. CONCLUSION

       In short, because the Flock system simply took pictures of the license plate of Robinson’s

vehicle and the exterior of his vehicle as he drove it down public thoroughfares in the City of

Norfolk, the police were not required under the Fourth Amendment to obtain a search warrant in

order to access the Flock system. Consequently, for all of the foregoing reasons, we affirm the

judgment of the circuit court.

                                                                                         Affirmed.




                                               - 10 -

```

---
