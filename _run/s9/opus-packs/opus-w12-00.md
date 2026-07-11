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

## GROUP: _overhaul2/lake/cases/Spinelli v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Spinelli v. United States"
type: case
citation: "393 U.S. 410 (1969)"
parallel_cite: "89 S. Ct. 584; 21 L. Ed. 2d 637"
neutral_cite: 1969 U.S. LEXIS 2701
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1969
date_decided: 1969-01-27
docket: 8
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: superseded
  as_of_content: 1969-01-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Spinelli v. United States
  varies_by_point: false
  scope_note: "Refined the Aguilar two-prong informant-tip test; the rigid Aguilar-Spinelli framework was abandoned for a totality-of-the-circumstances approach by Illinois v. Gates (1983)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107831/spinelli-v-united-states/"
  cluster_id: 107831
  opinion_id: 107831
  identity_checked: true
homes:
  - page: "[[Probable Cause]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Probable Cause in the Affidavit]]"
    role: "Related (cross-doctrine)"
related: ["[[Aguilar v. Texas]]", "[[Illinois v. Gates]]"]
aliases: []
tags: ["case", "fourth-amendment", "probable-cause", "informants", "warrants", "historical"]
holding: "Refined Aguilar's two-prong informant-tip test: a tip is first measured against the basis-of-knowledge and veracity prongs, and innocent corroboration cannot cure a deficient tip — later abandoned by Illinois v. Gates' totality test."
lake:
  record_id: Spinelli v. United States
  status: verified
  projected_at: 2026-07-06
---

# Spinelli v. United States

*393 U.S. 410 (1969)* · U.S. Supreme Court · **Historical** · Treatment: **abrogated** *(as of 2026-06-30)* — abrogated by [[Illinois v. Gates]]
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Spinelli was convicted under the Travel Act for crossing from Illinois into St. Louis to conduct gambling (bookmaking). The FBI's warrant affidavit recited that agents had tracked his movements on several days, that he was known as a bookmaker, that an apartment he frequented contained two telephones with specified numbers, and that a "confidential reliable informant" had reported he was running a bookmaking operation using those two phones. The affidavit gave no facts showing why the informant was reliable or how he knew what he claimed.

## Issue
How the two-pronged test of [[Aguilar v. Texas]] — the informant's basis of knowledge and his veracity — applies when an informant's tip is partly corroborated by independent police investigation, and whether this affidavit established probable cause.

## Rule
The tip is first assessed under *[[Aguilar v. Texas|Aguilar]]*, and only then is corroboration considered. "The informer's report must first be measured against *Aguilar*'s standards so that its probative value can be assessed. If the tip is found inadequate under *Aguilar*, the other allegations which corroborate the information contained in the hearsay report should then be considered." — 393 U.S. at 415. ^pin-415

Corroboration suffices only if the corroborated tip is as trustworthy as one that would pass *[[Aguilar v. Texas|Aguilar]]* unaided. Applying that analysis here, "the informant's tip — even when corroborated to the extent indicated — was not sufficient to provide the basis for a finding of probable cause." — *Id.* at 418. ^pin-418

## Application
The affidavit failed both *[[Aguilar v. Texas|Aguilar]]* prongs: the bare assertion that the informant was "reliable" offered the magistrate no reason supporting that conclusion (veracity), and the tip recited no underlying circumstances showing how the informant learned that Spinelli was bookmaking (basis of knowledge). The independent FBI work — surveillance and the existence of two phones — corroborated only innocent detail (that Spinelli could have used those phones), unlike the minutely detailed, self-verifying corroboration in *[[Draper v. United States]]*. Because neither the tip nor its corroboration was as probative as a tip passing *[[Aguilar v. Texas|Aguilar]]* alone, probable cause was lacking.

## Conclusion
The warrant was not supported by probable cause; the conviction resting on the seized evidence was reversed. *Spinelli* (with *[[Aguilar v. Texas|Aguilar]]*) built the rigid two-prong informant framework later abandoned in [[Illinois v. Gates]].

## Treatment & subsequent history
- **Status:** abrogated *(as of 2026-06-30)* — **Historical** (tier 6).
- The structured two-prong "basis of knowledge" + "veracity" framework of [[Aguilar v. Texas]] and *Spinelli* was **abandoned by [[Illinois v. Gates]]** (1983) in favor of a **totality-of-the-circumstances** test. Under *[[Illinois v. Gates|Gates]]* the two prongs survive only as relevant, non-dispositive considerations.

## Appears on
- [[Probable Cause]] — *Key — Progeny / Refinement*
- [[Probable Cause in the Affidavit]] — *Related (cross-doctrine)*

## Sources
- *Spinelli v. United States*, 393 U.S. 410 (1969) — https://www.courtlistener.com/opinion/107831/spinelli-v-united-states/ — pinpoints: 415, 418.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "eb12f45352084c25", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Spinelli v. United States"}, "payload": {"all": [{"cite": "393 U.S. 410", "page": "410", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "393"}, {"cite": "89 S. Ct. 584", "page": "584", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "89"}, {"cite": "21 L. Ed. 2d 637", "page": "637", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "21"}, {"cite": "1969 U.S. LEXIS 2701", "page": "2701", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1969"}], "display": "393 U.S. 410", "official": {"cite": "393 U.S. 410", "page": "410", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "393"}, "official_selection_present": true, "record_id": "Spinelli v. United States"}}
{"assertion_id": "2cc1dc60fa3b2f50", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-415", "record_id": "Spinelli v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-415", "pinpoint_status": "slip-only", "quote": "had reported he was running a bookmaking operation using those two phones. The affidavit gave no facts showing why the informant was reliable or how he knew what he claimed. ## Issue How the two-pronged test of [[Aguilar v. Texas]] — the informant's basis of knowledge and his veracity — applies when an informant's tip is partly corroborated by independent police investigation, and whether this affidavit established probable cause. ## Rule The tip is first assessed under *Aguilar*, and only then is corroboration considered.", "quote_fidelity": "mismatch", "record_id": "Spinelli v. United States", "star_marker": null}}
{"assertion_id": "8a423aad1513180f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-418", "record_id": "Spinelli v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-418", "pinpoint_status": "slip-only", "quote": "the informant's tip — even when corroborated to the extent indicated — was not sufficient to provide the basis for a finding of probable cause.", "quote_fidelity": "mismatch", "record_id": "Spinelli v. United States", "star_marker": null}}
{"assertion_id": "3fcd1c6814289930", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Spinelli v. United States"}, "payload": {"as_of_content": "1969-01-27", "as_of_treatment": "2026-06-30", "field_i_validity": "superseded", "record_id": "Spinelli v. United States", "scope_note": "Refined the Aguilar two-prong informant-tip test; the rigid Aguilar-Spinelli framework was abandoned for a totality-of-the-circumstances approach by Illinois v. Gates (1983).", "varies_by_point": false}}
```

### lake record — Spinelli v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Spinelli v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Spinelli v. United States",
    "case_name_short": "Spinelli",
    "case_name_full": "Spinelli v. United States",
    "input_case_name": "Spinelli v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1969-01-27",
    "year": 1969,
    "docket": "8",
    "cluster_id": 107831,
    "lead_opinion_id": 107831,
    "sibling_ids": [
      107831,
      9423895,
      9423896,
      9423897,
      9423898,
      9423899
    ],
    "absolute_url": "/opinion/107831/spinelli-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "393 U.S. 410",
      "volume": "393",
      "reporter": "U.S.",
      "page": "410",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "89 S. Ct. 584",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "584",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "21 L. Ed. 2d 637",
        "volume": "21",
        "reporter": "L. Ed. 2d",
        "page": "637",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1969 U.S. LEXIS 2701",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "2701",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "393 U.S. 410",
        "volume": "393",
        "reporter": "U.S.",
        "page": "410",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 S. Ct. 584",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "584",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "21 L. Ed. 2d 637",
        "volume": "21",
        "reporter": "L. Ed. 2d",
        "page": "637",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1969 U.S. LEXIS 2701",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "2701",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "393 U.S. 410",
    "official_selection": {
      "court_class": "scotus",
      "selected": "393 U.S. 410",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-415",
      "page": null,
      "quote": "had reported he was running a bookmaking operation using those two phones. The affidavit gave no facts showing why the informant was reliable or how he knew what he claimed. ## Issue How the two-pronged test of [[Aguilar v. Texas]] \u2014 the informant's basis of knowledge and his veracity \u2014 applies when an informant's tip is partly corroborated by independent police investigation, and whether this affidavit established probable cause. ## Rule The tip is first assessed under *Aguilar*, and only then is corroboration considered.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-418",
      "page": null,
      "quote": "the informant's tip \u2014 even when corroborated to the extent indicated \u2014 was not sufficient to provide the basis for a finding of probable cause.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "superseded",
    "as_of_content": "1969-01-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Spinelli v. United States",
    "varies_by_point": false,
    "scope_note": "Refined the Aguilar two-prong informant-tip test; the rigid Aguilar-Spinelli framework was abandoned for a totality-of-the-circumstances approach by Illinois v. Gates (1983).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Illinois v. Gates",
          "cluster_id": 110959,
          "cite": "462 U.S. 213",
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:abrogated"
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
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Guardado",
          "cluster_id": 9391153,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Costa",
          "cluster_id": 4744366,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Marmon",
          "cluster_id": 10133414,
          "cite": [
            "303 Or. App. 469",
            "463 P.3d 555"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Barreto",
          "cluster_id": 4690114,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Arias",
          "cluster_id": 4600764,
          "cite": [
            "119 N.E.3d 257",
            "481 Mass. 604"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
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
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Luna",
          "cluster_id": 4449164,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. (And",
          "cluster_id": 7171453,
          "cite": [
            "94 N.E.3d 435",
            "92 Mass. App. Ct. 1107"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jordan",
          "cluster_id": 4406528,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Ramos",
          "cluster_id": 2827409,
          "cite": [
            "88 Mass. App. Ct. 68"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane1_negative"
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
        "journal_ref": "Spinelli v. United States:lane1_negative"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adams v. Williams",
          "cluster_id": 108571,
          "cite": [
            "32 L. Ed. 2d 612",
            "92 S. Ct. 1921",
            "407 U.S. 143",
            "1972 U.S. LEXIS 2206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alabama v. White",
          "cluster_id": 112454,
          "cite": [
            "110 L. Ed. 2d 301",
            "110 S. Ct. 2412",
            "496 U.S. 325",
            "1990 U.S. LEXIS 3053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Unger",
          "cluster_id": 1916834,
          "cite": [
            "749 N.W.2d 272",
            "278 Mich. App. 210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Idaho v. Wright",
          "cluster_id": 112488,
          "cite": [
            "111 L. Ed. 2d 638",
            "110 S. Ct. 3139",
            "497 U.S. 805",
            "1990 U.S. LEXIS 3461",
            "30 Fed. R. Serv. 24",
            "58 U.S.L.W. 5036"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whiteley v. Warden, Wyoming State Penitentiary",
          "cluster_id": 108297,
          "cite": [
            "28 L. Ed. 2d 306",
            "91 S. Ct. 1031",
            "401 U.S. 560",
            "1971 U.S. LEXIS 65",
            "58 Ohio Op. 2d 434"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Harris",
          "cluster_id": 108379,
          "cite": [
            "29 L. Ed. 2d 723",
            "91 S. Ct. 2075",
            "403 U.S. 573",
            "1971 U.S. LEXIS 18"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Salinas",
          "cluster_id": 1423352,
          "cite": [
            "829 P.2d 1068",
            "119 Wash. 2d 192",
            "1992 Wash. LEXIS 146"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Janis",
          "cluster_id": 109539,
          "cite": [
            "49 L. Ed. 2d 1046",
            "96 S. Ct. 3021",
            "428 U.S. 433",
            "1976 U.S. LEXIS 162"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Desist v. United States",
          "cluster_id": 107875,
          "cite": [
            "22 L. Ed. 2d 248",
            "89 S. Ct. 1030",
            "394 U.S. 244",
            "1969 U.S. LEXIS 2159"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. Nelson",
          "cluster_id": 107877,
          "cite": [
            "22 L. Ed. 2d 281",
            "89 S. Ct. 1082",
            "394 U.S. 286",
            "1969 U.S. LEXIS 2161"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Prado Navarette v. California",
          "cluster_id": 2670795,
          "cite": [
            "188 L. Ed. 2d 680",
            "134 S. Ct. 1683",
            "2014 U.S. LEXIS 2930",
            "82 U.S.L.W. 4282",
            "572 U.S. 393",
            "24 Fla. L. Weekly Fed. S 690",
            "2014 WL 1577513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
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
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zurcher v. Stanford Daily",
          "cluster_id": 109876,
          "cite": [
            "56 L. Ed. 2d 525",
            "98 S. Ct. 1970",
            "436 U.S. 547",
            "1978 U.S. LEXIS 98"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spinelli v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107831 OR 9423895 OR 9423896 OR 9423897 OR 9423898 OR 9423899) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzEzOTcxMjAwMDAwJnM9MjE1NzkxOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107831+OR+9423895+OR+9423896+OR+9423897+OR+9423898+OR+9423899%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 12,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 16,
        "triage_snippet_classified": 184
      },
      "lane2_top_cited": {
        "query": "cites:(107831 OR 9423895 OR 9423896 OR 9423897 OR 9423898 OR 9423899)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNzkmcz0xODkxNjM4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107831+OR+9423895+OR+9423896+OR+9423897+OR+9423898+OR+9423899%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107831 OR 9423895 OR 9423896 OR 9423897 OR 9423898 OR 9423899)",
        "reviewed": 30,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 30,
        "triage_read": 1,
        "triage_snippet_classified": 29
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107831 OR 9423895 OR 9423896 OR 9423897 OR 9423898 OR 9423899)",
    "indexed_citing_opinions": 4302,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107831,
        "count": 3864,
        "count_source": "search"
      },
      {
        "opinion_id": 9423895,
        "count": 545,
        "count_source": "search"
      },
      {
        "opinion_id": 9423896,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423897,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423898,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423899,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6224,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/spinelli-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2NzAxOSZzPTk0OTMwNDEmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28107831+OR+9423895+OR+9423896+OR+9423897+OR+9423898+OR+9423899%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107831,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 101963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 106783,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 107058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 107325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 107394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107831,
        "cited_id": 277169,
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
    "date_created": "2026-07-05T20:16:44Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: abrogated -> superseded",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:16:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:16:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:16:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Spinelli v. United States

```
<div>
<center><b><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U.S. 410</a></span> (1969)</b></center>
<center><h1>SPINELLI<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 8.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 16-17, 1968.</center>
<center>Decided January 27, 1969.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE EIGHTH CIRCUIT.
<p><span class="star-pagination">*411</span> <i>Irl B. Baris</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Joseph J. Connolly</i> argued the cause for the United States, <i>pro hac vice.</i> With him on the brief were <i>Solicitor General Griswold, Assistant Attorney General Vinson, Beatrice Rosenberg,</i> and <i>Sidney M. Glazer.</i></p>
<p>MR. JUSTICE HARLAN delivered the opinion of the Court.</p>
<p>William Spinelli was convicted under <span class="citation no-link">18 U. S. C. § 1952</span><sup>[1]</sup> of traveling to St. Louis, Missouri, from a nearby Illinois suburb with the intention of conducting gambling activities proscribed by Missouri law. See <span class="citation no-link">Mo. Rev. Stat. § 563.360</span> (1959). At every appropriate stage in the proceedings in the lower courts, the petitioner challenged the constitutionality of the warrant which authorized the FBI search that uncovered the evidence necessary for his conviction. At each stage, Spinelli's challenge was treated in a different way. At a pretrial suppression hearing, the United States District Court for the Eastern District of Missouri held that Spinelli <span class="star-pagination">*412</span> lacked standing to raise a Fourth Amendment objection. A unanimous panel of the Court of Appeals for the Eighth Circuit rejected the District Court's ground, a majority holding further that the warrant was issued without probable cause. After an <i>en banc</i> rehearing, the Court of Appeals sustained the warrant and affirmed the conviction by a vote of six to two. <span class="citation" data-id="9452981"><a href="/opinion/277169/william-spinelli-v-united-states/" aria-description="Citation for case: William Spinelli v. United States">382 F. 2d 871</a></span>. Both the majority and dissenting <i>en banc</i> opinions reflect a most conscientious effort to apply the principles we announced in <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), to a factual situation whose basic characteristics have not been at all uncommon in recent search warrant cases. Believing it desirable that the principles of <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> should be further explicated, we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./390/942/">390 U. S. 942</a></span>, our writ being later limited to the question of the constitutional validity of the search and seizure.<sup>[2]</sup> <span class="citation multiple-matches"><a href="/c/U.%20S./391/933/">391 U. S. 933</a></span>. For reasons that follow we reverse.</p>
<p>In <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>,</i> a search warrant had issued upon an affidavit of police officers who swore only that they had "received reliable information from a credible person and do believe" that narcotics were being illegally stored on the described premises. While recognizing that the constitutional requirement of probable cause can be satisfied by hearsay information, this Court held the <span class="star-pagination">*413</span> affidavit inadequate for two reasons. First, the application failed to set forth any of the "underlying circumstances" necessary to enable the magistrate independently to judge of the validity of the informant's conclusion that the narcotics were where he said they were. Second, the affiant-officers did not attempt to support their claim that their informant was " `credible' or his information `reliable.' " The Government is, however, quite right in saying that the FBI affidavit in the present case is more ample than that in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>.</i> Not only does it contain a report from an anonymous informant, but it also contains a report of an independent FBI investigation which is said to corroborate the informant's tip. We are, then, required to delineate the manner in which <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i>'s two-pronged test should be applied in these circumstances.</p>
<p>In essence, the affidavit, reproduced in full in the Appendix to this opinion, contained the following allegations:<sup>[3]</sup></p>
<p>1. The FBI had kept track of Spinelli's movements on five days during the month of August 1965. On four of these occasions, Spinelli was seen crossing one of two bridges leading from Illinois into St. Louis, Missouri, between 11 a. m. and 12:15 p. m. On four of the five days, Spinelli was also seen parking his car in a lot used by residents of an apartment house at 1108 Indian Circle Drive in St. Louis, between 3:30 p. m. and 4:45 p. m.<sup>[4]</sup><span class="star-pagination">*414</span> On one day, Spinelli was followed further and seen to enter a particular apartment in the building.</p>
<p>2. An FBI check with the telephone company revealed that this apartment contained two telephones listed under the name of Grace P. Hagen, and carrying the numbers WYdown 4-0029 and WYdown 4-0136.</p>
<p>3. The application stated that "William Spinelli is known to this affiant and to federal law enforcement agents and local law enforcement agents as a bookmaker, an associate of bookmakers, a gambler, and an associate of gamblers."</p>
<p>4. Finally, it was stated that the FBI "has been informed by a confidential reliable informant that William Spinelli is operating a handbook and accepting wagers and disseminating wagering information by means of the telephones which have been assigned the numbers WYdown 4-0029 and WYdown 4-0136."</p>
<p>There can be no question that the last item mentioned, detailing the informant's tip, has a fundamental place in this warrant application. Without it, probable cause could not be established. The first two items reflect only innocent-seeming activity and data. Spinelli's travels to and from the apartment building and his entry into a particular apartment on one occasion could hardly be taken as bespeaking gambling activity; and there is surely nothing unusual about an apartment containing two separate telephones. Many a householder indulges himself in this petty luxury. Finally, the allegation that Spinelli was "known" to the affiant and to other federal and local law enforcement officers as a gambler and an associate of gamblers is but a bald and unilluminating assertion of suspicion that is entitled to no weight in appraising the magistrate's decision. <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/#46" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41, 46</a></span> (1933).</p>
<p><span class="star-pagination">*415</span> So much indeed the Government does not deny. Rather, following the reasoning of the Court of Appeals, the Government claims that the informant's tip gives a suspicious color to the FBI's reports detailing Spinelli's innocent-seeming conduct and that, conversely, the FBI's surveillance corroborates the informant's tip, thereby entitling it to more weight. It is true, of course, that the magistrate is obligated to render a judgment based upon a common-sense reading of the entire affidavit. <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 108</a></span> (1965). We believe, however, that the "totality of circumstances" approach taken by the Court of Appeals paints with too broad a brush. Where, as here, the informer's tip is a necessary element in a finding of probable cause, its proper weight must be determined by a more precise analysis.</p>
<p>The informer's report must first be measured against <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i>'s standards so that its probative value can be assessed. If the tip is found inadequate under <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>,</i> the other allegations which corroborate the information contained in the hearsay report should then be considered. At this stage as well, however, the standards enunciated in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> must inform the magistrate's decision. He must ask: Can it fairly be said that the tip, even when certain parts of it have been corroborated by independent sources, is as trustworthy as a tip which would pass <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i>'s tests without independent corroboration? <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> is relevant at this stage of the inquiry as well because the tests it establishes were designed to implement the long-standing principle that probable cause must be determined by a "neutral and detached magistrate," and not by "the officer engaged in the often competitive enterprise of ferreting out crime." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948). A magistrate cannot be said to have properly discharged his constitutional duty if he relies on an informer's tip whicheven <span class="star-pagination">*416</span> when partially corroboratedis not as reliable as one which passes <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i>'s requirements when standing alone.</p>
<p>Applying these principles to the present case, we first consider the weight to be given the informer's tip when it is considered apart from the rest of the affidavit. It is clear that a Commissioner could not credit it without abdicating his constitutional function. Though the affiant swore that his confidant was "reliable," he offered the magistrate no reason in support of this conclusion. Perhaps even more important is the fact that <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i>'s other test has not been satisfied. The tip does not contain a sufficient statement of the underlying circumstances from which the informer concluded that Spinelli was running a bookmaking operation. We are not told how the FBI's source received his informationit is not alleged that the informant personally observed Spinelli at work or that he had ever placed a bet with him. Moreover, if the informant came by the information indirectly, he did not explain why his sources were reliable. Cf. <i>Jaben</i> v. <i>United States,</i> <span class="citation" data-id="9423037"><a href="/opinion/107058/jaben-v-united-states/" aria-description="Citation for case: Jaben v. United States">381 U. S. 214</a></span> (1965). In the absence of a statement detailing the manner in which the information was gathered, it is especially important that the tip describe the accused's criminal activity in sufficient detail that the magistrate may know that he is relying on something more substantial than a casual rumor circulating in the underworld or an accusation based merely on an individual's general reputation.</p>
<p>The detail provided by the informant in <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959), provides a suitable benchmark. While Hereford, the Government's informer in that case, did not state the way in which he had obtained his information, he reported that Draper had gone to Chicago the day before by train and that he would return to Denver by train with three ounces of heroin on one of two specified mornings. Moreover, <span class="star-pagination">*417</span> Hereford went on to describe, with minute particularity, the clothes that Draper would be wearing upon his arrival at the Denver station. A magistrate, when confronted with such detail, could reasonably infer that the informant had gained his information in a reliable way.<sup>[5]</sup> Such an inference cannot be made in the present case. Here, the only facts supplied were that Spinelli was using two specified telephones and that these phones were being used in gambling operations. This meager report could easily have been obtained from an offhand remark heard at a neighborhood bar.</p>
<p>Nor do we believe that the patent doubts <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> raises as to the report's reliability are adequately resolved by a consideration of the allegations detailing the FBI's independent investigative efforts. At most, these allegations indicated that Spinelli could have used the telephones specified by the informant for some purpose. This cannot by itself be said to support both the inference that the informer was generally trustworthy and that he had made his charge against Spinelli on the basis of information obtained in a reliable way. Once again, <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> provides a relevant comparison. Independent police work in that case corroborated much more than one small detail that had been provided by the informant. There, the police, upon meeting the inbound Denver train on the second morning specified by informer Hereford, saw a man whose dress corresponded precisely to Hereford's detailed description. It was then apparent that the informant had not been fabricating his report out of whole cloth; since the report was of the sort which in common experience may be recognized as having been <span class="star-pagination">*418</span> obtained in a reliable way, it was perfectly clear that probable cause had been established.</p>
<p>We conclude, then, that in the present case the informant's tipeven when corroborated to the extent indicated was not sufficient to provide the basis for a finding of probable cause. This is not to say that the tip was so insubstantial that it could not properly have counted in the magistrate's determination. Rather, it needed some further support. When we look to the other parts of the application, however, we find nothing alleged which would permit the suspicions engendered by the informant's report to ripen into a judgment that a crime was probably being committed. As we have already seen, the allegations detailing the FBI's surveillance of Spinelli and its investigation of the telephone company records contain no suggestion of criminal conduct when taken by themselvesand they are not endowed with an aura of suspicion by virtue of the informer's tip. Nor do we find that the FBI's reports take on a sinister color when read in light of common knowledge that bookmaking is often carried on over the telephone and from premises ostensibly used by others for perfectly normal purposes. Such an argument would carry weight in a situation in which the premises contain an unusual number of telephones or abnormal activity is observed, cf. <i>McCray</i> v. <i>Illinois,</i> <span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/#302" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300, 302</a></span> (1967), but it does not fit this case where neither of these factors is present.<sup>[6]</sup> All that remains to be considered is the flat statement that Spinelli was "known" to the FBI and others as a gambler. But just as a simple assertion of police suspicion is not itself a sufficient basis for a magistrate's finding of probable cause, we do not believe it may be used to give <span class="star-pagination">*419</span> additional weight to allegations that would otherwise be insufficient.</p>
<p>The affidavit, then, falls short of the standards set forth in <i>Aguilar, Draper,</i> and our other decisions that give content to the notion of probable cause.<sup>[7]</sup> In holding as we have done, we do not retreat from the established propositions that only the probability, and not a prima facie showing, of criminal activity is the standard of probable cause, <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 96</a></span> (1964); that affidavits of probable cause are tested by much less rigorous standards than those governing the admissibility of evidence at trial, <i>McCray</i> v. <i>Illinois,</i> <span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/#311" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300, 311</a></span> (1967); that in judging probable cause issuing magistrates are not to be confined by niggardly limitations or by restrictions on the use of their common sense, <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 108</a></span> (1965); and that their determination of probable cause should be paid great deference by reviewing courts, <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#270" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 270-271</a></span> (1960). But we cannot sustain this warrant without diluting important safeguards that assure that the judgment of a disinterested judicial officer will interpose itself between the police and the citizenry.<sup>[8]</sup></p>
<p><span class="star-pagination">*420</span> The judgment of the Court of Appeals is reversed and the case is remanded to that court for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE MARSHALL took no part in the consideration or decision of this case.</p>
<p></p>
<h2>APPENDIX TO OPINION OF THE COURT.</h2>
<p></p>
<h2>AFFIDAVIT IN SUPPORT OF SEARCH WARRANT.</h2>
<p>I, Robert L. Bender, being duly sworn, depose and say that I am a Special Agent of the Federal Bureau of Investigation, and as such am authorized to make searches and seizures.</p>
<p>That on August 6, 1965, at approximately 11:44 a. m., William Spinelli was observed by an Agent of the Federal Bureau of Investigation driving a 1964 Ford convertible, Missouri license HC3-649, onto the Eastern approach of the Veterans Bridge leading from East St. Louis, Illinois, to St. Louis, Missouri.</p>
<p>That on August 11, 1965, at approximately 11:16 a. m., William Spinelli was observed by an Agent of the Federal Bureau of Investigation driving a 1964 Ford convertible, Missouri license HC3-649, onto the Eastern approach of the Eads Bridge leading from East St. Louis, Illinois, to St. Louis, Missouri.</p>
<p>Further, at approximately 11:18 a. m. on August 11, 1965, I observed William Spinelli driving the aforesaid Ford convertible from the Western approach of the Eads Bridge into St. Louis, Missouri.</p>
<p>Further, at approximately 4:40 p. m. on August 11, 1965, I observed the aforesaid Ford convertible, bearing Missouri license HC3-649, parked in a parking lot used by residents of The Chieftain Manor Apartments, approximately one block east of 1108 Indian Circle Drive.</p>
<p>On August 12, 1965, at approximately 12:07 p. m., <span class="star-pagination">*421</span> William Spinelli was observed by an Agent of the Federal Bureau of Investigation driving the aforesaid 1964 Ford convertible onto the Eastern approach of the Veterans Bridge from East St. Louis, Illinois, in the direction of St. Louis, Missouri.</p>
<p>Further, on August 12, 1965, at approximately 3:46 p. m., I observed William Spinelli driving the aforesaid 1964 Ford convertible onto the parking lot used by the residents of The Chieftain Manor Apartments approximately one block east of 1108 Indian Circle Drive.</p>
<p>Further, on August 12, 1965, at approximately 3:49 p. m., William Spinelli was observed by an Agent of the Federal Bureau of Investigation entering the front entrance of the two-story apartment building located at 1108 Indian Circle Drive, this building being one of The Chieftain Manor Apartments.</p>
<p>On August 13, 1965, at approximately 11:08 a. m., William Spinelli was observed by an Agent of the Federal Bureau of Investigation driving the aforesaid Ford convertible onto the Eastern approach of the Eads Bridge from East St. Louis, Illinois, heading towards St. Louis, Missouri.</p>
<p>Further, on August 13, 1965, at approximately 11:11 a. m., I observed William Spinelli driving the aforesaid Ford convertible from the Western approach of the Eads Bridge into St. Louis, Missouri.</p>
<p>Further, on August 13, 1965, at approximately 3:45 p. m., I observed William Spinelli driving the aforesaid 1964 Ford convertible onto the parking area used by residents of The Chieftain Manor Apartments, said parking area being approximately one block from 1108 Indian Circle Drive.</p>
<p>Further, on August 13, 1965, at approximately 3:55 p. m., William Spinelli was observed by an Agent of the Federal Bureau of Investigation entering the corner apartment located on the second floor in the southwest corner, known as Apartment F, of the two-story <span class="star-pagination">*422</span> apartment building known and numbered as 1108 Indian Circle Drive.</p>
<p>On August 16, 1965, at approximately 3:22 p. m., I observed William Spinelli driving the aforesaid Ford convertible onto the parking lot used by the residents of The Chieftain Manor Apartments approximately one block east of 1108 Indian Circle Drive.</p>
<p>Further, an Agent of the F. B. I. observed William Spinelli alight from the aforesaid Ford convertible and walk toward the apartment building located at 1108 Indian Circle Drive.</p>
<p>The records of the Southwestern Bell Telephone Company reflect that there are two telephones located in the southwest corner apartment on the second floor of the apartment building located at 1108 Indian Circle Drive under the name of Grace P. Hagen. The numbers listed in the Southwestern Bell Telephone Company records for the aforesaid telephones are WYdown 4-0029 and WYdown 4-0136.</p>
<p>William Spinelli is known to this affiant and to federal law enforcement agents and local law enforcement agents as a bookmaker, an associate of bookmakers, a gambler, and an associate of gamblers.</p>
<p>The Federal Bureau of Investigation has been informed by a confidential reliable informant that William Spinelli is operating a handbook and accepting wagers and disseminating wagering information by means of the telephones which have been assigned the numbers WYdown 4-0029 and WYdown 4-0136.</p>
              /s/ Robert L. Bender,
                  Robert L. Bender,
                   Special Agent, Federal Bureau
                     of Investigation.
<p>Subscribed and sworn to before me this 18th day of August, 1965, at St. Louis, Missouri.</p>
                              /s/ William R. O'Toole.
<p><span class="star-pagination">*423</span> MR. JUSTICE WHITE, concurring.</p>
<p>An investigator's affidavit that he has seen gambling equipment being moved into a house at a specified address will support the issuance of a search warrant. The oath affirms the honesty of the statement and negatives the lie or imagination. Personal observation attests to the facts assertedthat there is gambling equipment on the premises at the named address.</p>
<p>But if the officer simply avers, without more, that there is gambling paraphernalia on certain premises, the warrant should not issue, even though the belief of the officer is an honest one, as evidenced by his oath, and even though the magistrate knows him to be an experienced, intelligent officer who has been reliable in the past. This much was settled in <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span> (1933), where the Court held insufficient an officer's affidavit swearing he had cause to believe that there was illegal liquor on the premises for which the warrant was sought. The unsupported assertion or belief of the officer does not satisfy the requirement of probable cause. <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#269" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 269</a></span> (1960); <i>Grau</i> v. <i>United States,</i> <span class="citation" data-id="101963"><a href="/opinion/101963/grau-v-united-states/" aria-description="Citation for case: Grau v. United States">287 U. S. 124</a></span> (1932); <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#29" aria-description="Citation for case: Byars v. United States">273 U. S. 28, 29</a></span> (1927).</p>
<p>What is missing in <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> and like cases is a statement of the basis for the affiant's believing the facts contained in the affidavitthe good "cause" which the officer in <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> said he had. If an officer swears that there is gambling equipment at a certain address, the possibilities are (1) that he has seen the equipment; (2) that he has observed or perceived facts from which the presence of the equipment may reasonably be inferred; and (3) that he has obtained the information from someone else. If (1) is true, the affidavit is good. But in (2), the affidavit is insufficient unless the perceived facts are given, for it is the magistrate, not the <span class="star-pagination">*424</span> officer, who is to judge the existence of probable cause. <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964); <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#486" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 486</a></span> (1958); <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948). With respect to (3), where the officer's information is hearsay, no warrant should issue absent good cause for crediting that hearsay. Because an affidavit asserting, without more, the location of gambling equipment at a particular address does not claim personal observation of any of the facts by the officer, and because of the likelihood that the information came from an unidentified third party, affidavits of this type are unacceptable.</p>
<p>Neither should the warrant issue if the officer states that there is gambling equipment in a particular apartment and that his information comes from an informant, named or unnamed, since the honesty of the informant and the basis for his report are unknown. Nor would the missing elements be completely supplied by the officer's oath that the informant has often furnished reliable information in the past. This attests to the honesty of the informant, but <i>Aguilar</i> v. <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Texas, supra</a></span></i><i>,</i> requires something moredid the information come from observation, or did the informant in turn receive it from another? Absent additional facts for believing the informant's report, his assertion stands no better than the oath of the officer to the same effect. Indeed, if the affidavit of an officer, known by the magistrate to be honest and experienced, stating that gambling equipment is located in a certain building is unacceptable, it would be quixotic if a similar statement from an honest informant were found to furnish probable cause. A strong argument can be made that both should be acceptable under the Fourth Amendment, but under our cases neither is. The past reliability of the informant can no more furnish probable cause for believing his <span class="star-pagination">*425</span> current report than can previous experience with the officer himself.</p>
<p>If the affidavit rests on hearsayan informant's report what is necessary under <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> is one of two things: the informant must declare either (1) that he has himself seen or perceived the fact or facts asserted; or (2) that his information is hearsay, but there is good reason for believing itperhaps one of the usual grounds for crediting hearsay information. The first presents few problems: since the report, although hearsay, purports to be first-hand observation, remaining doubt centers on the honesty of the informant, and that worry is dissipated by the officer's previous experience with the informant. The other basis for accepting the informant's report is more complicated. But if, for example, the informer's hearsay comes from one of the actors in the crime in the nature of admission against interest, the affidavit giving this information should be held sufficient.</p>
<p>I am inclined to agree with the majority that there are limited special circumstances in which an "honest" informant's report, if sufficiently detailed, will in effect verify itselfthat is, the magistrate when confronted with such detail could reasonably infer that the informant had gained his information in a reliable way. See <i>ante,</i> at 417. Detailed information may sometimes imply that the informant himself has observed the facts. Suppose an informant with whom an officer has had satisfactory experience states that there is gambling equipment in the living room of a specified apartment and describes in detail not only the equipment itself but also the appointments and furnishings in the apartment. Detail like this, if true at all, must rest on personal observation either of the informant or of someone else. If the latter, we know nothing of the third person's honesty or <span class="star-pagination">*426</span> sources; he may be making a wholly false report. But it is arguable that on these facts it was the informant himself who has perceived the facts, for the information reported is not usually the subject of casual, day-to-day conversation. Because the informant is honest and it is probable that he has viewed the facts, there is probable cause for the issuance of a warrant.</p>
<p>So too in the special circumstances of <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959), the kind of information related by the informant is not generally sent ahead of a person's arrival in a city except to those who are intimately connected with making careful arrangements for meeting him. The informant, posited as honest, somehow had the reported facts, very likely from one of the actors in the plan, or as one of them himself. The majority's suggestion is that a warrant could have been obtained based only on the informer's report. I am inclined to agree, although it seems quite plain that if it may be so easily inferred from the affidavit that the informant has himself observed the facts or has them from an actor in the event, no possible harm could come from requiring a statement to that effect, thereby removing the difficult and recurring questions which arise in such situations.</p>
<p>Of course, <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> itself did not proceed on this basis. Instead, the Court pointed out that when the officer saw a person getting off the train at the specified time, dressed and conducting himself precisely as the informant had predicted, all but the critical fact with respect to possessing narcotics had then been verified and for that reason the officer had "reasonable grounds" to believe also that Draper was carrying narcotics. Unquestionably, verification of arrival time, dress, and gait reinforced the honesty of the informanthe had not reported a made-up story. But if what <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> stands for is that the existence of the tenth and critical fact <span class="star-pagination">*427</span> is made sufficiently probable to justify the issuance of a warrant by verifying nine other facts coming from the same source, I have my doubts about that case.</p>
<p>In the first place, the proposition is not that the tenth fact may be logically inferred from the other nine or that the tenth fact is usually found in conjunction with the other nine. No one would suggest that just anyone getting off the 10:30 train dressed as Draper was, with a brisk walk and carrying a zipper bag, should be arrested for carrying narcotics. The thrust of <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> is not that the verified facts have independent significance with respect to proof of the tenth. The argument instead relates to the reliability of the source: because an informant is right about some things, he is more probably right about other facts, usually the critical, unverified facts.</p>
<p>But the Court's cases have already rejected for Fourth Amendment purposes the notion that the past reliability of an officer is sufficient reason for believing his current assertions. Nor would it suffice, I suppose, if a reliable informant states there is gambling equipment in Apartment 607 and then proceeds to describe in detail Apartment 201, a description which is verified before applying for the warrant. He was right about 201, but that hardly makes him more believable about the equipment in 607. But what if he states that there are narcotics locked in a safe in Apartment 300, which is described in detail, and the apartment manager verifies everything but the contents of the safe? I doubt that the report about the narcotics is made appreciably more believable by the verification. The informant could still have gotten his information concerning the safe from others about whom nothing is known or could have inferred the presence of narcotics from circumstances which a magistrate would find unacceptable.</p>
<p>The tension between <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> and the <i>Nathanson-Aguilar</i> line of cases is evident from the course followed <span class="star-pagination">*428</span> by the majority opinion. First, it is held that the report from a reliable informant that Spinelli is using two telephones with specified numbers to conduct a gambling business plus Spinelli's reputation in police circles as a gambler does not add up to probable cause. This is wholly consistent with <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> and <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span>:</i> the informant did not reveal whether he had personally observed the facts or heard them from another and, if the latter, no basis for crediting the hearsay was presented. Nor were the facts, as MR. JUSTICE HARLAN says, of such a nature that they normally would be obtainable only by the personal observation of the informant himself. The police, however, did not stop with the informant's report. Independently, they established the existence of two phones having the given numbers and located them in an apartment house which Spinelli was regularly frequenting away from his home. There remained little question but that Spinelli was using the phones, and it was a fair inference that the use was not for domestic but for business purposes. The informant had claimed the business involved gambling. Since his specific information about Spinelli using two phones with particular numbers had been verified, did not his allegation about gambling thereby become sufficiently more believable if the <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> principle is to be given any scope at all? I would think so, particularly since the information from the informant which was verified was not neutral, irrelevant information but was material to proving the gambling allegation: two phones with different numbers in an apartment used away from home indicates a business use in an operation, like bookmaking, where multiple phones are needed. The <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> approach would reasonably justify the issuance of a warrant in this case, particularly since the police had some awareness of Spinelli's past activities. The majority, however, <span class="star-pagination">*429</span> while seemingly embracing <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span>,</i> confines that case to its own facts. Pending full-scale reconsideration of that case, on the one hand, or of the <i>Nathanson-Aguilar</i> cases on the other, I join the opinion of the Court and the judgment of reversal, especially since a vote to affirm would produce an equally divided Court.</p>
<p>MR. JUSTICE BLACK, dissenting.</p>
<p>In my view, this Court's decision in <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), was bad enough. That decision went very far toward elevating the magistrate's hearing for issuance of a search warrant to a full-fledged trial, where witnesses must be brought forward to attest personally to all the facts alleged. But not content with this, the Court today expands <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> to almost unbelievable proportions. Of course, it would strengthen the probable-cause presentation if eyewitnesses could testify that they saw the defendant commit the crime. It would be stronger still if these witnesses could explain in detail the nature of the sensual perceptions on which they based their "conclusion" that the person they had seen was the defendant and that he was responsible for the events they observed. Nothing in our Constitution, however, requires that the facts be established with that degree of certainty and with such elaborate specificity before a policeman can be authorized by a disinterested magistrate to conduct a carefully limited search.</p>
<p>The Fourth Amendment provides that "no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." In this case a search warrant was issued supported by an oath and particularly describing the place to be searched and the things to be seized. The supporting oath was <span class="star-pagination">*430</span> three printed pages and the full text of it is included in an Appendix to the Court's opinion. The magistrate, I think properly, held the information set forth sufficient facts to show "probable cause" that the defendant was violating the law. Six members of the Court of Appeals also agreed that the affidavit was sufficient to show probable cause. A majority of this Court today holds, however, that the magistrate and all of these judges were wrong. In doing so, they substitute their own opinion for that of the local magistrate and the circuit judges, and reject the <i>en banc</i> factual conclusion of the Eighth Circuit and reverse the judgment based upon that factual conclusion. I cannot join in any such disposition of an issue so vital to the administration of justice, and dissent as vigorously as I can.</p>
<p>I repeat my belief that the affidavit given the magistrate was more than ample to show probable cause of the petitioner's guilt. The affidavit meticulously set out facts sufficient to show the following:</p>
<p>1. The petitioner had been shown going to and coming from a room in an apartment which contained two telephones listed under the name of another person. Nothing in the record indicates that the apartment was of that large and luxurious type which could only be occupied by a person to whom it would be a "petty luxury" to have two separate telephones, with different numbers, both listed under the name of a person who did not live there.</p>
<p>2. The petitioner's car had been observed parked in the apartment's parking lot. This fact was, of course, highly relevant in showing that the petitioner was extremely interested in some enterprise which was located in the apartment.</p>
<p>3. The FBI had been informed by a reliable informant that the petitioner was accepting wagering information by telephonesthe particular telephones located in the <span class="star-pagination">*431</span> apartment the defendant had been repeatedly visiting. Unless the Court, going beyond the requirements of the Fourth Amendment, wishes to require magistrates to hold trials before issuing warrants, it is not necessary as the Court holdsto have the affiant explain "the underlying circumstances from which the informer concluded that Spinelli was running a bookmaking operation." <i>Ante,</i> at 416.</p>
<p>4. The petitioner was known by federal and local law enforcement agents as a bookmaker and an associate of gamblers. I cannot agree with the Court that this knowledge was only a "bald and unilluminating assertion of suspicion that is entitled to no weight in appraising the magistrate's decision." <i>Ante,</i> at 414. Although the statement is hearsay that might not be admissible in a regular trial, everyone knows, unless he shuts his eyes to the realities of life, that this is a relevant fact which, together with other circumstances, might indicate a factual probability that gambling is taking place.</p>
<p>The foregoing facts should be enough to constitute probable cause for anyone who does not believe that the only way to obtain a search warrant is to prove beyond a reasonable doubt that a defendant is guilty. Even <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>,</i> on which the Court relies, cannot support the contrary result, at least as that decision was written before today's massive escalation of it. In <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> the Court dealt with an affidavit that stated only:</p>
<blockquote>"Affiants have received reliable information from a credible person and do believe that heroin . . . and other narcotics and narcotic paraphernalia are being kept at the above described premises for the purpose of sale and use contrary to the provisions of the law." <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#109" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 109</a></span>.</blockquote>
<p>The Court held, over the dissent of Mr. Justice Clark, MR. JUSTICE STEWART, and myself, that this unsupported conclusion of an unidentified informant provided no basis <span class="star-pagination">*432</span> for the magistrate to make an independent judgment as to the persuasiveness of the facts relied upon to show probable cause. Here, of course, we have much more, and the Court in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> was careful to point out that additional information of the kind presented in the affidavit before us now would be highly relevant:</p>
<blockquote>"If the fact and results of such a surveillance had been appropriately presented to the magistrate, this would, of course, present an entirely different case." <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#109" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 109, n. 1</a></span>.</blockquote>
<p>In the present case even the two-judge minority of the court below recognized, as this Court seems to recognize today, that this additional information took the case beyond the rule of <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>.</i> Six of the other circuit judges disagreed with the two dissenting judges, finding that all the circumstances considered together could support a reasonable judgment that gambling probably was taking place. I fully agree with this carefully considered opinion of the court below.</p>
<p>I regret to say I consider today's decision an indefensible departure from the principles of our former cases. Less than four years ago we reaffirmed these principles in <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 108</a></span> (1965):</p>
<blockquote>"If the teachings of the Court's cases are to be followed and the constitutional policy served, affidavits for search warrants . . . must be tested and interpreted by magistrates and courts in a commonsense and realistic fashion. . . . Technical requirements of elaborate specificity once exacted under common law pleadings have no proper place in this area."</blockquote>
<p>See also <i>Husty</i> v. <i>United States,</i> <span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/#700" aria-description="Citation for case: Husty v. United States">282 U. S. 694, 700-701</a></span> (1931).</p>
<p>Departures of this kind are responsible for considerable uneasiness in our lower courts, and I must say I <span class="star-pagination">*433</span> am deeply troubled by the statements of Judge Gibson in the court below:</p>
<blockquote>"I am, indeed, disturbed by decision after decision of our courts which place increasingly technical burdens upon law enforcement officials. I am disturbed by these decisions that appear to relentlessly chip away at the ever narrowing area of effective police operation. I believe the holdings in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>,</i> and <i>Rugendorf</i> v. <i>United States,</i> <span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">376 U. S. 528</a></span> (1964) are sufficient to protect the privacy of individuals from hastily conceived intrusions, and I do not think the limitations and requirements on the issuance of search warrants should be expanded by setting up over-technical requirements approaching the now discarded pitfalls of common law pleadings. Moreover, if we become increasingly technical and rigid in our demands upon police officers, I fear we make it increasingly easy for criminals to operate, detected but unpunished. I feel the significant movement of the law beyond its present state is unwarranted, unneeded, and dangerous to law enforcement efficiency." (Dissenting from panel opinion.)</blockquote>
<p>The Court of Appeals in this case took a sensible view of the Fourth Amendment, and I would wholeheartedly affirm its decision.</p>
<p><i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, decided in 1961, held for the first time that the Fourth Amendment and the exclusionary rule of <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914) are now applicable to the States. That Amendment provides that search warrants shall not be issued without probable cause. The existence of probable cause is a factual matter that calls for the determination of a factual question. While no statistics are immediately available, questions of probable cause to issue search <span class="star-pagination">*434</span> warrants and to make arrests are doubtless involved in many thousands of cases in state courts. All of those probable-cause state cases are now potentially reviewable by this Court. It is, of course, physically impossible for this Court to review the evidence in all or even a substantial percentage of those cases. Consequently, whether desirable or not, we must inevitably accept most of the fact findings of the state courts, particularly when, as here in a federal case, both the trial and appellate courts have decided the facts the same way. It cannot be said that the trial judge and six members of the Court of Appeals committed flagrant error in finding from evidence that the magistrate had probable cause to issue the search warrant here. It seems to me that this Court would best serve itself and the administration of justice by accepting the judgment of the two courts below. After all, they too are lawyers and judges, and much closer to the practical, everyday affairs of life than we are.</p>
<p>Notwithstanding the Court's belief to the contrary, I think that in holding as it does, the Court does:</p>
<blockquote>"retreat from the established propositions that only the probability, and not a prima facie showing, of criminal activity is the standard of probable cause, <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 96</a></span> (1964); that affidavits of probable cause are tested by much less rigorous standards than those governing the admissibility of evidence at trial, <i>McCray</i> v. <i>Illinois,</i> <span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/#311" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300, 311</a></span> (1967); that in judging probable cause issuing magistrates are not to be confined by niggardly limitations or by restrictions on the use of their common sense, <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 108</a></span> (1965); and that their determination of probable cause should be paid great deference by reviewing courts, <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#270" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 270-271</a></span> (1960)." <i>Ante,</i> at 419.</blockquote>
<p><span class="star-pagination">*435</span> In fact, I believe the Court is moving rapidly, through complex analyses and obfuscatory language, toward the holding that no magistrate can issue a warrant unless according to some unknown standard of proof he can be persuaded that the suspect defendant is actually guilty of a crime. I would affirm this conviction.</p>
<p>MR. JUSTICE FORTAS, dissenting.</p>
<p>My Brother HARLAN's opinion for the Court is animated by a conviction which I share that "[t]he security of one's privacy against arbitrary intrusion by the policewhich is at the core of the Fourth Amendment is basic to a free society." <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span> (1949).</p>
<p>We may well insist upon a sympathetic and even an indulgent view of the latitude which must be accorded to the police for performance of their vital task; but only a foolish or careless people will deduce from this that the public welfare requires or permits the police to disregard the restraints on their actions which historic struggles for freedom have developed for the protection of liberty and dignity of citizens against arbitrary state power.</p>
<p>As Justice Jackson (dissenting) stated in <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#180" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 180-181</a></span> (1949):</p>
<blockquote>"[The provisions of the Fourth Amendment] are not mere second-class rights but belong in the catalog of indispensable freedoms. Among deprivations of rights, none is so effective in cowing a population, crushing the spirit of the individual and putting terror in every heart. Uncontrolled search and seizure is one of the first and most effective weapons in the arsenal of every arbitrary government. And one need only briefly to have dwelt and worked among a people possessed of many admirable qualities but deprived of these rights to know that the <span class="star-pagination">*436</span> human personality deteriorates and dignity and self-reliance disappear where homes, persons and possessions are subject at any hour to unheralded search and seizure by the police."</blockquote>
<p>History<sup>[1]</sup> teaches us that this protection requires that the judgment of a judicial officer be interposed between the police, hot in pursuit of their appointed target, and the citizen;<sup>[2]</sup> that the judicial officer must judge and not merely rubber-stamp; and that his judgment must be based upon judicially reliable facts adequate to demonstrate that the search is justified by the probability that it will yield the fruits or instruments of crimeor, as this Court has only recently ruled, tangible evidence of its commission.<sup>[3]</sup> The exceptions to the requirement of a search warrant have always been narrowly restricted<sup>[4]</sup> because of this Court's long-standing awareness of the fundamental role of the magistrate's judgment in the preservation of a proper balance between individual freedom and state power. See <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/#700" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699, 700</a></span> (1948).</p>
<p>Today's decision deals, not with the necessity of obtaining a warrant prior to search, but with the difficult problem of the nature of the showing that must be made <span class="star-pagination">*437</span> before the magistrate to justify his issuance of a search warrant. While I do not subscribe to the criticism of the majority expressed by my Brother BLACK in dissent, I believewith all respectthat the majority is in error in holding that the affidavit supporting the warrant in this case is constitutionally inadequate.</p>
<p>The affidavit is unusually long and detailed. In fact, it recites so many minute and detailed facts developed in the course of the investigation of Spinelli that its substance is somewhat obscured. It is paradoxical that this very fullness of the affidavit may be the source of the constitutional infirmity that the majority finds. Stated in language more direct and less circumstantial than that used by the FBI agent who executed the affidavit, it sets forth that the FBI has been informed that Spinelli is accepting wagers by means of telephones numbered WY 4-0029 and WY 4-0136; that Spinelli is known to the affiant agent and to law enforcement agencies as a bookmaker; that telephones numbered WY 4-0029 and WY 4-0136 are located in a certain apartment; that Spinelli was placed under surveillance and his observed movements were such as to show his use of that apartment and to indicate that he frequented the apartment on a regular basis.</p>
<p><i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), holds that the reference in an affidavit to information described only as received from "a confidential reliable informant," standing alone, is not an adequate basis for issuance of a search warrant. The majority agrees that the "FBI affidavit in the present case is more ample than that in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>,</i>" but concludes that it is nevertheless constitutionally inadequate. The majority states that the present affidavit fails to meet the "two-pronged test" of <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> because (a) it does not set forth the basis for the assertion that the informer is "reliable" and (b) it fails to state the "underlying circumstances" upon which the <span class="star-pagination">*438</span> informant based his conclusion that Spinelli was engaged in bookmaking.</p>
<p>The majority acknowledges, however, that its reference to a "two-pronged test" should not be understood as meaning that an affidavit deficient in these respects is necessarily inadequate to support a search warrant. Other facts and circumstances may be attested which will supply the evidence of probable cause needed to support the search warrant. On this general statement we are agreed. Our difference is that I believe such facts and circumstances are present in this case, and the majority arrives at the opposite conclusion.</p>
<p><i>Aguilar</i> expressly recognized that if, in that case, the affidavit's conclusory report of the informant's story had been supplemented by "the fact and results of . . . a surveillance. . . this would, of course, present an entirely different case." <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#109" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 109, n. 1</a></span>. In the present case, as I view it, the affidavit showed not only relevant surveillance, entitled to some probative weight for purposes of the issuance of a search warrant, but also additional, specific facts of significance and adequate reliability: that Spinelli was using two telephone numbers, identified by an "informant" as being used for bookmaking, in his illegal operations; that these telephones were in an identified apartment; and that Spinelli, a known bookmaker,<sup>[5]</sup> frequented the apartment. Certainly, this is enough.</p>
<p>A policeman's affidavit should not be judged as an entry in an essay contest. It is not "abracadabra."<sup>[6]</sup><span class="star-pagination">*439</span> As the majority recognizes, a policeman's affidavit is entitled to common-sense evaluation. So viewed, I conclude that the judgment of the Court of Appeals for the Eighth Circuit should be affirmed.</p>
<p>MR. JUSTICE STEWART, dissenting.</p>
<p>For substantially the reasons stated by my Brothers BLACK and FORTAS, I believe the warrant in this case was supported by a sufficient showing of probable cause. I would therefore affirm the judgment.</p>
<h2>NOTES</h2>
<p>[1]  The relevant portion of the statute reads:
</p>
<p>"(a) Whoever travels in interstate or foreign commerce or uses any facility in interstate . . . commerce . . . with intent to</p>
<p>.....</p>
<p>"(3) otherwise promote, manage, establish, carry on . . . any unlawful activity, and thereafter performs or attempts to perform any of the acts specified in subparagraphs (1), (2), and (3), shall be fined not more than $10,000 or imprisoned for not more than five years, or both.</p>
<p>"(b) As used in this section `unlawful activity' means (1) any business enterprise involving gambling . . . in violation of the laws of the State in which they are committed or of the United States . . . ."</p>
<p>[2]  We agree with the Court of Appeals that Spinelli has standing to raise his Fourth Amendment claim. The issue arises because at the time the FBI searched the apartment in which Spinelli was alleged to be conducting his bookmaking operation, the petitioner was not on the premises. Instead, the agents did not execute their search warrant until Spinelli was seen to leave the apartment, lock the door, and enter the hallway. At that point, petitioner was arrested, the key to the apartment was demanded of him, and the search commenced. Since petitioner would plainly have standing if he had been arrested inside the apartment, <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 267</a></span> (1960), it cannot matter that the agents preferred to delay the arrest until petitioner stepped into the hallwayespecially when the FBI only managed to gain entry into the apartment by requiring petitioner to surrender his key.</p>
<p>[3]  It is, of course, of no consequence that the agents might have had additional information which could have been given to the Commissioner. "It is elementary that in passing on the validity of a warrant, the reviewing court may consider <i>only</i> information brought to the magistrate's attention." <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#109" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108, 109, n. 1</a></span> (emphasis in original). Since the Government does not argue that whatever additional information the agents may have possessed was sufficient to provide probable cause for the arrest, thereby justifying the resultant search as well, we need not consider that question.</p>
<p>[4]  No report was made as to Spinelli's movements during the period between his arrival in St. Louis at noon and his arrival at the parking lot in the late afternoon. In fact, the evidence at trial indicated that Spinelli frequented the offices of his stockbroker during this period.</p>
<p>[5]  While <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> involved the question whether the police had probable cause for an arrest without a warrant, the analysis required for an answer to this question is basically similar to that demanded of a magistrate when he considers whether a search warrant should issue.</p>
<p>[6]  A box containing three uninstalled telephones was found in the apartment, but only after execution of the search warrant.</p>
<p>[7]  In those cases in which this Court has found probable cause established, the showing made was much more substantial than the one made here. Thus, in <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#104" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 104</a></span> (1965), FBI agents observed repeated deliveries of loads of sugar in 60-pound bags, smelled the odor of fermenting mash, and heard " `sounds similar to that of a motor or a pump coming from the direction of' Ventresca's house." Again, in <i>McCray</i> v. <i>Illinois,</i> <span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/#303" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300, 303-304</a></span> (1967), the informant reported that McCray " `was selling narcotics and had narcotics on his person now in the vicinity of 47th and Calumet.' " When the police arrived at the intersection, they observed McCray engaging in various suspicious activities. <span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/#302" aria-description="Citation for case: McCray v. Illinois">386 U. S., at 302</a></span>.</p>
<p>[8]  In the view we have taken of this case, it becomes unnecessary to decide whether the search warrant was properly executed, or whether it sufficiently described the things that were seized.</p>
<p>[1]  "The knock at the door, whether by day or by night, as a prelude to a search, without authority of law but solely on the authority of the police, did not need the commentary of recent history to be condemned as inconsistent with the conception of human rights enshrined in the history and the basic constitutional documents of English-speaking peoples." <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#28" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 28</a></span> (1949). See <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#69" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 69-70</a></span> (1950) (Frankfurter, J., dissenting). See generally with respect to the history of the Fourth Amendment N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution (1937).</p>
<p>[2]  See <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-14</a></span> (1948).</p>
<p>[3]  <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967).</p>
<p>[4]  See <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499</a></span> (1958); <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#311" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 311</a></span> (1967) (concurring opinion).</p>
<p>[5]  Although Spinelli's reputation standing alone would not, of course, justify the search, this Court has held that such a reputation may make the informer's report "much less subject to scepticism than would be such a charge against one without such a history." <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#271" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 271</a></span> (1960).</p>
<p>[6]  See <i>Time, Inc.</i> v. <i>Hill,</i> <span class="citation" data-id="9423311"><a href="/opinion/107325/time-inc-v-hill/#418" aria-description="Citation for case: Time, Inc. v. Hill">385 U. S. 374, 418</a></span> (1967) (dissent) (relating to jury instructions).</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Stanford v. Texas.json  (`lake-record`, 6 assertions)

### content_page

```
---
title: "Stanford v. Texas"
type: case
citation: "379 U.S. 476 (1965)"
parallel_cite: "85 S. Ct. 506; 13 L. Ed. 2d 431"
neutral_cite: 1965 U.S. LEXIS 2380
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1965
date_decided: 1965-03-01
docket: 40
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1965-03-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Stanford v. Texas
  varies_by_point: false
  scope_note: "Controlling: warrants for expressive materials seized for their ideas demand 'the most scrupulous exactitude'; a warrant sweeping in books and papers by subject matter is an unconstitutional general warrant."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106964/stanford-v-texas/"
  cluster_id: 106964
  opinion_id: 106964
  identity_checked: true
homes:
  - page: "[[Particularity]]"
    role: "Progeny"
related: ["[[Maryland v. Garrison]]", "[[Groh v. Ramirez]]", "[[Andresen v. Maryland]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant-requirement", "particularity", "general-warrant", "first-amendment"]
holding: "When a warrant authorizes the seizure of books and papers because of the ideas they contain, the particularity requirement must be applied with the most scrupulous exactitude; a warrant authorizing seizure of all materials 'concerning' a subject is an unconstitutional general warrant."
lake:
  record_id: Stanford v. Texas
  status: verified
  projected_at: 2026-07-09
---

# Stanford v. Texas

*379 U.S. 476 (1965)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating violations of the Texas Communist Control Law, state officers obtained a warrant to search John Stanford's home for "books, records, pamphlets, cards, receipts, lists, memoranda, pictures, recordings and other written instruments concerning the Communist Party of Texas." Executing it, the officers spent hours seizing some 2,000 of Stanford's books and papers. Stanford challenged the warrant as an unconstitutional general warrant.

## Issue
Does a warrant authorizing seizure of all books and papers "concerning the Communist Party of Texas" satisfy the Fourth Amendment's [[Particularity|particularity]] requirement when the items seized are expressive materials taken for the ideas they contain?

## Rule
No. "[T]he constitutional requirement that warrants must particularly describe the 'things to be seized' is to be accorded the most scrupulous exactitude when the 'things' are books, and the basis for their seizure is the ideas which they contain." — 379 U.S. at 485. ^pin-485

[[Particularity]] exists precisely so that, "[a]s to what is to be taken, nothing is left to the discretion of the officer executing the warrant." — *Id.* at 485–86 (quoting *Marron v. United States*). ^pin-485b

A warrant whose sweep delegates that choice to the officer is the general warrant the Fourth Amendment forbids.

## Application
The warrant authorized the seizure not of contraband but of "literary material" — "book[s], records, pamphlets, cards, receipts, lists, memoranda, pictures, recordings and other written instruments concerning the Communist Party of Texas." That "indiscriminate sweep of that language is constitutionally intolerable" because it left the selection of expressive materials, seized for their ideas, to the discretion of the executing officers. — [*Id.* at 486](https://www.courtlistener.com/opinion/106964/stanford-v-texas/#:~:text=literary%20material). ^pin-486

The Fourth and Fourteenth Amendments guarantee that no official "shall ransack [Stanford's] home and seize his books and papers under the unbridled authority of a general warrant — no less than the law 200 years ago shielded John Entick from the messengers of the King." — *Id.* ^pin-486b

## Conclusion
The warrant was an unconstitutional general warrant; the order was [[Reading and Citing Cases#vacated|vacated]] and the cause [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Stanford* remains the controlling statement that warrants reaching expressive materials demand heightened, "scrupulous" [[Particularity|particularity]], drawing directly on the general-warrant history of *[[Entick v. Carrington]]*. It sits within the [[Particularity|particularity]] line alongside [[Maryland v. Garrison]], [[Groh v. Ramirez]], and [[Andresen v. Maryland]]. No negative treatment.

## Appears on
- [[Particularity]] — *Progeny*

## Sources
- *Stanford v. Texas*, 379 U.S. 476 (1965) — https://www.courtlistener.com/opinion/106964/stanford-v-texas/ — pinpoints: 485, 486.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "db73bb7eb7ea7bd9", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Stanford v. Texas"}, "payload": {"all": [{"cite": "379 U.S. 476", "page": "476", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "379"}, {"cite": "85 S. Ct. 506", "page": "506", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "85"}, {"cite": "13 L. Ed. 2d 431", "page": "431", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "13"}, {"cite": "1965 U.S. LEXIS 2380", "page": "2380", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1965"}], "display": "379 U.S. 476", "official": {"cite": "379 U.S. 476", "page": "476", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "379"}, "official_selection_present": true, "record_id": "Stanford v. Texas"}}
{"assertion_id": "06f7a73d6959eaf7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-486b", "record_id": "Stanford v. Texas"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-486b", "pinpoint_status": "slip-only", "quote": "shall ransack [Stanford's] home and seize his books and papers under the unbridled authority of a general warrant — no less than the law 200 years ago shielded John Entick from the messengers of the King.", "quote_fidelity": "mismatch", "record_id": "Stanford v. Texas", "star_marker": null}}
{"assertion_id": "2f4a7cca7fc8c43a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-486", "record_id": "Stanford v. Texas"}, "payload": {"fragment": "#:~:text=literary%20material", "page": null, "pin_id": "pin-486", "pinpoint_status": "star-verified", "quote": "literary material", "quote_fidelity": "matched", "record_id": "Stanford v. Texas", "star_marker": "486"}}
{"assertion_id": "567a40594782bc33", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-485", "record_id": "Stanford v. Texas"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-485", "pinpoint_status": "slip-only", "quote": "satisfy the Fourth Amendment's particularity requirement when the items seized are expressive materials taken for the ideas they contain? ## Rule No.", "quote_fidelity": "mismatch", "record_id": "Stanford v. Texas", "star_marker": null}}
{"assertion_id": "f3938e30b3efe5ae", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-485b", "record_id": "Stanford v. Texas"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-485b", "pinpoint_status": "slip-only", "quote": "[a]s to what is to be taken, nothing is left to the discretion of the officer executing the warrant.", "quote_fidelity": "mismatch", "record_id": "Stanford v. Texas", "star_marker": null}}
{"assertion_id": "fd372e99a341d51d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Stanford v. Texas"}, "payload": {"as_of_content": "1965-03-01", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Stanford v. Texas", "scope_note": "Controlling: warrants for expressive materials seized for their ideas demand 'the most scrupulous exactitude'; a warrant sweeping in books and papers by subject matter is an unconstitutional general warrant.", "varies_by_point": false}}
```

### lake record — Stanford v. Texas

```json
{
  "schema_version": "s2.v1",
  "record_id": "Stanford v. Texas",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Stanford v. Texas",
    "case_name_short": "Stanford",
    "case_name_full": "Stanford v. Texas",
    "input_case_name": "Stanford v. Texas",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1965-03-01",
    "year": 1965,
    "docket": "40",
    "cluster_id": 106964,
    "lead_opinion_id": 106964,
    "sibling_ids": [
      106964
    ],
    "absolute_url": "/opinion/106964/stanford-v-texas/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "379 U.S. 476",
      "volume": "379",
      "reporter": "U.S.",
      "page": "476",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "85 S. Ct. 506",
        "volume": "85",
        "reporter": "S. Ct.",
        "page": "506",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "13 L. Ed. 2d 431",
        "volume": "13",
        "reporter": "L. Ed. 2d",
        "page": "431",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1965 U.S. LEXIS 2380",
        "volume": "1965",
        "reporter": "U.S. LEXIS",
        "page": "2380",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "379 U.S. 476",
        "volume": "379",
        "reporter": "U.S.",
        "page": "476",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 S. Ct. 506",
        "volume": "85",
        "reporter": "S. Ct.",
        "page": "506",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "13 L. Ed. 2d 431",
        "volume": "13",
        "reporter": "L. Ed. 2d",
        "page": "431",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1965 U.S. LEXIS 2380",
        "volume": "1965",
        "reporter": "U.S. LEXIS",
        "page": "2380",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "379 U.S. 476",
    "official_selection": {
      "court_class": "scotus",
      "selected": "379 U.S. 476",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-485",
      "page": null,
      "quote": "satisfy the Fourth Amendment's particularity requirement when the items seized are expressive materials taken for the ideas they contain? ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-485b",
      "page": null,
      "quote": "[a]s to what is to be taken, nothing is left to the discretion of the officer executing the warrant.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-486",
      "page": null,
      "quote": "literary material",
      "star_marker": "486",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 20345,
      "fragment": "#:~:text=literary%20material",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-486b",
      "page": null,
      "quote": "shall ransack [Stanford's] home and seize his books and papers under the unbridled authority of a general warrant \u2014 no less than the law 200 years ago shielded John Entick from the messengers of the King.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1965-03-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Stanford v. Texas",
    "varies_by_point": false,
    "scope_note": "Controlling: warrants for expressive materials seized for their ideas demand 'the most scrupulous exactitude'; a warrant sweeping in books and papers by subject matter is an unconstitutional general warrant.",
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
        "journal_ref": "Stanford v. Texas:lane1_negative"
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
        "journal_ref": "Stanford v. Texas:lane1_negative"
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
        "journal_ref": "Stanford v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hector Feliciano(074395)",
          "cluster_id": 3183943,
          "cite": [
            "224 N.J. 351",
            "132 A.3d 1245",
            "2016 N.J. LEXIS 229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wheeler v. State",
          "cluster_id": 3182294,
          "cite": [
            "135 A.3d 282",
            "2016 Del. LEXIS 121",
            "2016 WL 825395"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jon Thomas Ford v. State",
          "cluster_id": 2719207,
          "cite": [
            "444 S.W.3d 171",
            "2014 Tex. App. LEXIS 9159",
            "2014 WL 4099731"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane1_negative"
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
        "journal_ref": "Stanford v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Tanaya Montgomery v. State",
          "cluster_id": 2922297,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Porath v. State",
          "cluster_id": 1770795,
          "cite": [
            "148 S.W.3d 402",
            "2004 WL 1660763"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. One Parcel of Real Property Described as Lot 41, Berryhill Farm Estates, Etc., Tommy Lee Dunmore, Claimant-Appellant",
          "cluster_id": 747825,
          "cite": [
            "128 F.3d 1386",
            "1997 Colo. J. C.A.R. 2612",
            "1997 U.S. App. LEXIS 29832"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Gauthier",
          "cluster_id": 6577354,
          "cite": [
            "425 Mass. 37",
            "679 N.E.2d 211",
            "1997 Mass. LEXIS 111"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Terry Burton Kimbrough",
          "cluster_id": 707532,
          "cite": [
            "69 F.3d 723",
            "1995 WL 662084"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thacker v. State",
          "cluster_id": 1634092,
          "cite": [
            "889 S.W.2d 380",
            "1994 WL 456786"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Steven Ricciardelli",
          "cluster_id": 610895,
          "cite": [
            "998 F.2d 8",
            "1993 U.S. App. LEXIS 14891",
            "1993 WL 210540"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Joseph v. State",
          "cluster_id": 1665187,
          "cite": [
            "807 S.W.2d 303",
            "1991 WL 22992"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane1_negative"
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
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
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
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
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
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
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
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
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
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
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
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
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
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
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
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ybarra v. Illinois",
          "cluster_id": 110158,
          "cite": [
            "62 L. Ed. 2d 238",
            "100 S. Ct. 338",
            "444 U.S. 85",
            "1979 U.S. LEXIS 151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
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
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stanley v. Georgia",
          "cluster_id": 107898,
          "cite": [
            "22 L. Ed. 2d 542",
            "89 S. Ct. 1243",
            "394 U.S. 557",
            "1969 U.S. LEXIS 1972"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. United States District Court for the Eastern District of Michigan",
          "cluster_id": 108581,
          "cite": [
            "32 L. Ed. 2d 752",
            "92 S. Ct. 2125",
            "407 U.S. 297",
            "1972 U.S. LEXIS 38"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Steagald v. United States",
          "cluster_id": 110464,
          "cite": [
            "68 L. Ed. 2d 38",
            "101 S. Ct. 1642",
            "451 U.S. 204",
            "1981 U.S. LEXIS 89",
            "49 U.S.L.W. 4418"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nixon v. Administrator of General Services",
          "cluster_id": 109729,
          "cite": [
            "53 L. Ed. 2d 867",
            "97 S. Ct. 2777",
            "433 U.S. 425",
            "1977 U.S. LEXIS 24",
            "2 Media L. Rep. (BNA) 2025"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
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
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Groh v. Ramirez",
          "cluster_id": 131161,
          "cite": [
            "157 L. Ed. 2d 1068",
            "124 S. Ct. 1284",
            "540 U.S. 551",
            "2004 U.S. LEXIS 1624",
            "2004 WL 330057"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
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
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Berger v. New York",
          "cluster_id": 107483,
          "cite": [
            "18 L. Ed. 2d 1040",
            "87 S. Ct. 1873",
            "388 U.S. 41",
            "1967 U.S. LEXIS 2964"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
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
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Krull",
          "cluster_id": 111835,
          "cite": [
            "94 L. Ed. 2d 364",
            "107 S. Ct. 1160",
            "480 U.S. 340",
            "1987 U.S. LEXIS 1061",
            "55 U.S.L.W. 4291"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Garrison",
          "cluster_id": 111823,
          "cite": [
            "94 L. Ed. 2d 72",
            "107 S. Ct. 1013",
            "480 U.S. 79",
            "1987 U.S. LEXIS 559",
            "55 U.S.L.W. 4190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zurcher v. Stanford Daily",
          "cluster_id": 109876,
          "cite": [
            "56 L. Ed. 2d 525",
            "98 S. Ct. 1970",
            "436 U.S. 547",
            "1978 U.S. LEXIS 98"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Massachusetts v. Sheppard",
          "cluster_id": 111263,
          "cite": [
            "82 L. Ed. 2d 737",
            "104 S. Ct. 3424",
            "468 U.S. 981",
            "1984 U.S. LEXIS 154",
            "52 U.S.L.W. 5177"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Couch v. United States",
          "cluster_id": 108650,
          "cite": [
            "34 L. Ed. 2d 548",
            "93 S. Ct. 611",
            "409 U.S. 322",
            "1973 U.S. LEXIS 23",
            "31 A.F.T.R.2d (RIA) 477"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walter v. United States",
          "cluster_id": 110314,
          "cite": [
            "65 L. Ed. 2d 410",
            "100 S. Ct. 2395",
            "447 U.S. 649",
            "1980 U.S. LEXIS 135"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stanford v. Texas:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106964) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NDU4NDAwMDAwMDAmcz0yMTUzMTM3JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106964%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 15,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 15,
        "triage_snippet_classified": 185
      },
      "lane2_top_cited": {
        "query": "cites:(106964)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMzAmcz01MDU5MjImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28106964%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106964)",
        "reviewed": 13,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 13,
        "triage_read": 1,
        "triage_snippet_classified": 12
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106964)",
    "indexed_citing_opinions": 619,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106964,
        "count": 619,
        "count_source": "search"
      }
    ],
    "citation_count": 948,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/stanford-v-texas.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY4OTczMjkmcz00Nzc2ODEwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106964%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106964,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106964,
        "cited_id": 100621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106964,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106964,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106964,
        "cited_id": 105371,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106964,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106964,
        "cited_id": 106017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106964,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106964,
        "cited_id": 106287,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106964,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106964,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106964,
        "cited_id": 106878,
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
    "date_created": "2026-07-05T20:20:47Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:21:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:21:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:24:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:21:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Stanford v. Texas

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b576-10">
  Mr. Justice Stewart
 </author>
<p id="A4M">
  delivered the opinion of the Court.
 </p>
<p id="b576-11">
  On December 27, 1963, several Texas law-enforcement officers presented' themselves at the petitioner’s San
  <span citation-index="1" class="star-pagination" label="477"> 
   *477
   </span>
  Antonio home for the purpose of searching it under authority of a. warrant issued by a local magistrate. By the time they had finished, five hours later, they had seized some 2,000 of the petitioner’s books, pamphlets, and papers. The question presented by this case is whether the search and seizure were constitutionally valid.
 </p>
<p id="b577-4">
  The warrant was issued under § 9 of Art. 6889-3A of the Revised Civil Statutes of Texas. That Article, enacted in 1955 and known as the Suppression Act, is a sweeping and many-faceted law which, among other things, outlaws the Communist Party and creates various individual criminal offenses, each punishable by imprisonment for up to 20 years. Section 9 authorizes the issuance of a warrant “for the purpose of searching for and seizing any books, records, pamphlets, cards, receipts, lists, memoranda, pictures, recordings, or any written instruments showing that a person or organization is violating or has violated any provision of this Act.” The section sets forth various procedural requirements, among them that “if the premises to be searched constitute a private, residence, such application for a search warrant shall be accompanied by the affidavits of two credible citizens.”
 </p>
<p id="b577-5">
  The application for the warrant was filed in a Bexar County court by the Criminal District Attorney of that County. It recited that the applicant
 </p>
<blockquote id="b577-6">
  “. . . has good reason to believe and does believe that a certain place and premises in Bexar County, Texas, described as two white frame houses and one garage, located at the address of 1118 West Rosewood, in the City of San Antonio, Bexar County, Texas, and being'the premises under the control and in charge of John William Stanford, Jr., is a place where books, records, pamphlets, cards, receipts, fists, memoranda, pictures, recordings and other written instruments
  <span citation-index="1" class="star-pagination" label="478"> 
   *478
   </span>
  concerning the Communist Party of Texas, and the operations of the Communist Party in Texas are unlawfully possessed and used in violation of Articles 6889-3
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  and 6889-3A, Revised Civil Statutes of the State of Texas, and that such belief of this officer is founded upon the following information:
 </blockquote>
<blockquote id="b578-5">
  “That this officer has received information from two credible persons that the party named above has such books and records in his possession which are books and records of the Communist Party including party lists and dues payments, and in addition other items listed above. That such information is of recent origin and has been confirmed by recent mailings by Stanford on the 12th of December, 1963 of pro-Communist material.”
 </blockquote>
<p id="b578-6">
  Attached to the application was an affidavit signed by two Assistant Attorneys General of Texas. The affidavit repeated the words of the application, except that the basis for the affiants’ belief was stated to be as follows:
 </p>
<blockquote id="b578-7">
  “Recent mailings by Stanford on the 12th of December, 1963, of material from his home address, such material being identified as pro-Communist material and other information received in the course of investigation that Stanford has in his possession the books and records of the Texas Communist Party.”
 </blockquote>
<p id="b578-8">
  The district judge issued a warrant which specifically described the premises to be searched, recited the allegations of the applicant’s and affiants’ belief that the premises were “a place where books, records, pamphlets,
  <span citation-index="1" class="star-pagination" label="479"> 
   *479
   </span>
  cards, receipts, lists, memoranda, pictures, recordings and other written instruments concerning the Communist Party of Texas, and the operations of the Communist Party in Texas are unlawfully possessed and used in violation of Article 6889-3 and Article 6889-3A, Revised Civil Statutes of the State of Texas,” and ordered the executing officers (&lt;to enter immediately and search the above described premises for such items listed above unlawfully possessed in violation of Article 6889-3 and Article 6889-3A, Revised Civil Statutes, State of .Texas, and to take possession of same.”
 </p>
<p id="b579-4">
  The warrant was executed by the two Assistant Attorneys General who had signed the affidavit, accompanied by a number of county officers. They went to the place described in the warrant, which was where the petitioner resided and carried on a mail order book business under the trade name “All Points of View.”
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  The petitioner was not at home when the officers arrived, but his wife was, and she let the officers in after one of them had read the warrant to her.
 </p>
<p id="b579-5">
  After some delay occasioned by an unsuccessful effort to locate the petitioner in another part of town, the search began. Under the general supervision of one of the Assistant Attorneys General the officers spent more than four hours in gathering up about half the books they found in the house. Most of the material they took came from the stock in trade, of the petitioner’s business, but they took a number of books from his personal library as well. The books and pamphlets taken comprised approximately 300 separate titles, in addition to numerous issues of several different periodicals. Among the books taken were works by such diverse writers as Karl Marx, Jean Paul Sartre, Theodore Draper, Fidel Castro, Earl
  <span citation-index="1" class="star-pagination" label="480"> 
   *480
   </span>
  Browder, Pope John XXIII, and Me. Justice Hugo L. Black; The officers also took possession of many of the petitioner’s private documents and papers, including his marriage certificate, his insurance policies, his household bills and receipts, and files of his personal correspondence. All this material was packed into 14 cartons and hauled off to an investigator’s office in the county courthouse. The officers did not find any “records of the Communist Party” or any “party lists and dues payments.”
 </p>
<p id="b580-4">
  The petitioner filed a motion with the magistrate who had issued the warrant, asking him to annul the warrant and order the return of all the property which had been seized under it. The motion asserted several federal constitutional claims. After a hearing the motion was denied without opinion. This order of denial was, as the parties agree, final and not appealable or otherwise reviewable under Texas law. See
  <em>
   Ex parte Wolfson,
  </em>
  <span class="citation" data-id="4899240"><a href="/opinion/5083158/ex-parte-wolfson/" aria-description="Citation for case: Ex parte Wolfson">127 Tex. Cr. R. 277</a></span>,
  <span class="citation" data-id="4899240"><a href="/opinion/5083158/ex-parte-wolfson/" aria-description="Citation for case: Ex parte Wolfson"><em>
   75
  </em>
  S. W. 2d 440</a></span>. Accordingly, we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./377/989/">377 U. S. 989</a></span>. See
  <em>
   Thompson
  </em>
  v.
  <em>
   City of Louisville,
  </em>
  <span class="citation" data-id="106017"><a href="/opinion/106017/thompson-v-city-of-louisville/#202" aria-description="Citation for case: Thompson v. City of Louisville">362 U. S. 199, 202-203</a></span>.
 </p>
<p id="b580-5">
  The petitioner has attacked the constitutional validity of this search and seizure upon several grounds. We rest our decision upon just one, without pausing to assess the substantiality of the others. For we think it is clear that this warrant was of a kind which it was the purpose of the Fourth Amendment to forbid — a general warrant. Therefore, even accepting the premise that some or even all of the substantive provisions of Articles 6889-3 and 6889-3A of the Revised Civil Statutes of Texas are constitutional and have not' been pre-empted by federal law,
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  even accepting the premise that the warrant sufficiently specified the offense believed to have been committed and was issued., upon probable cause,
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  the
  <span citation-index="1" class="star-pagination" label="481"> 
   *481
   </span>
  magistrate’s order denying the motion to annul the warrant and return the property must nonetheless be set aside.
 </p>
<p id="b581-5">
  It is now settled that the fundamental protections of the Fourth Amendment are guaranteed by the Fourteenth Amendment' against invasion by the States.
  <em>
   Wolf
  </em>
  v.
  <em>
   Colorado,
  </em>
  338 U S. 25, 27;
  <em>
   Mapp
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>;
  <em>
   Ker
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span>. The Fourth Amendment provides that “no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and
  <em>
   particularly describing
  </em>
  the place to be-searched, and the persons or
  <em>
   things to be
  </em>
  seized.” (Emphasis supplied.)
 </p>
<p id="b581-6">
  These words are precise and clear. They reflect the. determination of those who wrote the Bill of Rights that the people of this new Nation should forever “be secure in their persons, houses, papers, and effects” from intrusion and seizure by officers acting under the unbridled authority of a general warrant. Vivid in the memory of the newly independent Americans were those general warrants known as writs of assistance under which officers of the Crown had so bedeviled the colonists. •. The hated writs of assistance had given customs officials blanket authority to search where they pleased for goods imported in violation of the British tax laws. They weré denounced by James Otis as “the worst instrument of arbitrary power, the most destructive of English liberty, and the fundamental principles of law, that ever was found in an English law book,” because they placed “the liberty of every man in the hands of every petty officer.” The historic occasion of that denunciation, in 1761 at Boston, has been characterizéd as “perhaps the most prominent event which inaugurated the resistance of the colonies to the oppressions of the mother country. ‘Then and there,’ said John Adams, ‘then and there Was the first scene of the first act of opposition to the arbi
  <span citation-index="1" class="star-pagination" label="482"> 
   *482
   </span>
  trary claims of -Great Britain. Then and there the child Independence was born.’ ”
  <em>
   Boyd
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#625" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 625</a></span>.
 </p>
<p id="b582-6">
  But while the Fourth Amendment was most immediately the product of contemporary revulsion against a regime of writs of assistance, its roots go far deeper. Its adoption in the Constitution of this new Nation reflected the culmination in England a few years earlier of a struggle against oppression which had endured for centuries. The story of that struggle has been fully chronicled' in the pages of this Court’s report?,
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  and it would be a needless exercise in pedantry to review again the detailed history of the use of general warrants as instruments of oppression-from the time of the Tudors, through the Star Chamber, the Long Parliament, the Restoration, and beyond.
 </p>
<p id="b582-7">
  What is significant to note is that this history is largely a history of conflict between the Crown and the press. It was in enforcing the laws licensing the publication of literature and, later, in prosecutions for seditious libel that general warrants were systematically used in the sixteenth, seventeenth, and eighteenth centuries. In Tudor England officers of the Crown were given roving commissions to search where they pleased in order to suppress and destroy the literature of dissent, both Catholic and Puritan.
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
  'In later years warrants were sometimes more specific in content, but they typically authorized the arrest and search of the premises of all persons connected with the publication of a particular libel, or
  <span citation-index="1" class="star-pagination" label="483"> 
   *483
   </span>
  the arrest and seizure of all the papers of a named person thought to be connected with a libel.
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
</p>
<p id="b583-5">
  It was in the context of the latter kinds of general warrants that the battle for individual liberty and privacy was finally won — in the landmark cases of
  <em>
   Wilkes
  </em>
  v.
  <em>
   Wood
  </em>
<a class="footnote" href="#fn8" id="fn8_ref">
<em>
    8
   </em>
</a>
<em>
</em>
  and
  <em>
   Entick
  </em>
  v. Carrington.
  <a class="footnote" href="#fn9" id="fn9_ref">
   9
  </a>
  The
  <em>
   Wilkes
  </em>
  case arose out of the Crown’s attempt to stifle a publication called The North Briton, anonymously published by John Wilkes, then a member of Parliament — particularly issue No. 45 of that journal. Lord Halifax, as Secretary of State, issued a warrant ordering four of the King’s messengers “to make strict and diligent search for the authors, printers, and publishers of a seditious and treasonable paper, entitled, The North Briton, No. 45, . . . and them, or any of them, having found, to apprehend and .seize, together with their papers.”
  <a class="footnote" href="#fn10" id="fn10_ref">
   10
  </a>
  “Armed with thbir roving commission, they set forth in quest of unknown offenders; and unable to take evidence, listened to rumors, idle tales, and curious guesses. They held in their hands the liberty of every man whom they were pleased to suspect.”
  <a class="footnote" href="#fn11" id="fn11_ref">
   11
  </a>
  Holding that this was “a ridiculous warrant against the whole English nation,”
  <a class="footnote" href="#fn12" id="fn12_ref">
   12
  </a>
  the Court of Common Pleas awarded Wilkes damages against the Secretary of State. John Entick was the author of a publication called Monitor or British Freeholder. A warrant was issued specifically naming him and that publication, and authorizing his arrest for seditious libel and the seizure of his “books and papers.” The King’s messengers executing the warrant ransacked Entick’s home for four hours and carted
  <span citation-index="1" class="star-pagination" label="484"> 
   *484
   </span>
  away quantities of his books and papers. In an opinion which this Court has characterized as a wellspring of the rights now protected by the Fourth Amendment,
  <a class="footnote" href="#fn13" id="fn13_ref">
   13
  </a>
  Lord Camden declared the warrant to be unlawful. “This power,” he-said, “so assumed by the secretary of state is an execution upon all the party’s papers, in the first instance. His house is rifled; his most valuable secrets are taken,out of his possession, before the paper for which he is charged is found to be criminal by any competent jurisdiction, and before he is convicted either of writing, publishing, or being concerned in the paper.”
  <em>
   Entick
  </em>
  v.
  <em>
   Carrington.
  </em>
<a class="footnote" href="#fn14" id="fn14_ref">
<em>
    14
   </em>
</a>
<em>
</em>
  Thereafter, the House of Commons passed two. resolutions condemning general warrants, the first limiting its condemnation to their use in cases of libel, and the second condemning their use generally.
  <a class="footnote" href="#fn15" id="fn15_ref">
   15
  </a>
</p>
<p id="b584-6">
  This is the history which prompted the Court less than four years ago to remark that “ [t]he use by government of the power of search and seizure as an adjunct to a system for the suppression of objectionable publications is not new.”
  <em>
   Marcus
  </em>
  v.
  <em>
   Search Warrant,
  </em>
  <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#724" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717, at 724</a></span>. “This history was, of course, part of the intellectual matrix within which our own constitutional fabric was shaped. The Bill of Rights was fashioned against the background of knowledge that unrestricted power of search and seizure could also be an instrument for stifling liberty of expression.”
  <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#729" aria-description="Citation for case: Marcus v. Search Warrant of Property"><em>
   Id.,
  </em>
  at 729</a></span>. As Mr. Justice Douglas has put it, “The commands of our First Amend
  <span citation-index="1" class="star-pagination" label="485"> 
   *485
   </span>
  ment (as well as the prohibitions of the Fourth and the Fifth) reflect the teachings of
  <em>
   Entick
  </em>
  v.
  <em>
   Carrington, supra.
  </em>
  These three amendments are indeed closely related, safeguarding not only privacy and protection against self-incrimination but ‘conscience and human dignity and freedom of expression as well.’ ”
  <em>
   Frank
  </em>
  v.
  <em>
   Maryland,
  </em>
  <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#376" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360, 376</a></span> (dissenting opinion).
 </p>
<p id="b585-5">
  In short, what this history indispensably teaches is that the constitutional requirement that warrants must particularly describe the “things to be seized” is to be accorded the most scrupulous exactitude when the “things” are books, and the basis for their seizure is the ideas which they contain.
  <a class="footnote" href="#fn16" id="fn16_ref">
   16
  </a>
  See
  <em>
   Marcus
  </em>
  v.
  <em>
   Search Warrant,
  </em>
  <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717</a></span>;
  <em>
   A Quantity of Books
  </em>
  v.
  <em>
   Kansas,
  </em>
  <span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">378 U. S. 205</a></span>. No less a standard could be faithful to First Amendment freedoms. The constitutional impossibility of leaving the protection of those freedoms to the whim of the officers charged with executing the warrant is dramatically underscored by what the officers saw fit to seize under the warrant in this case.
  <a class="footnote" href="#fn17" id="fn17_ref">
   17
  </a>
</p>
<p id="b585-6">
  “The requirement that warrants shall particularly describe the things to be seized makes general searches under them impossible and prevents the seizure of one thing under a warrant describing another. As to what is to be taken, nothing is left to the discretion of the officer executing the warrant.”
  <em>
   Marron
  </em>
  v.
  <em>
   United States,
  </em>
<span citation-index="1" class="star-pagination" label="486"> 
   *486
   </span>
  <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U. S. 192, at 196</a></span>. We need not decide in the present case whether the description of the things to be seized would have been too generalized to pass constitutional muster, had the things been weapons, narcotics or “cases of whiskey.” See
  <em>
   Steele
  </em>
  v.
  <em>
   United States No. 1,
  </em>
  <span class="citation" data-id="100621"><a href="/opinion/100621/steele-v-united-states-no-1/#504" aria-description="Citation for case: Steele v. United States No. 1">267 U. S. 498, 504</a></span>.
  <a class="footnote" href="#fn18" id="fn18_ref">
   18
  </a>
  The point is that it was not any contraband of that kind which was ordered to be seized, but literary material — “book^, records, pamphlets, cards, receipts, lists, memoranda, pictures, recordings and other written instruments concerning the Communist Party of Texas, and the operations of the Communist Party in Texas.” The indiscriminate sweep of that language is constitutionally intolerable. To hold otherwise would be false to the terms of the Fourth Amendment, false to its meaning, and false to its history.
 </p>
<p id="b586-4">
  Two centuries have passed since the historic decision in
  <em>
   Entick
  </em>
  v.
  <em>
   Carrington,
  </em>
  almost to the. very day. The world has greatly changed, and the voice of nonconformity now sometimes speaks a tongue which Lord Camden might find hard to understand. But the Fourth and Fourteenth Amendments guarantee to John Stanford that no official of the State shall ransack his home and seize his books and papers under the unbridled authority of a general warrant — no less than the law 200 years ago shielded John Entick from the messengers of the King.
 </p>
<p id="b586-5">
  The order is vacated and the cause remanded for further proceedings not inconsistent with this opinion.
 </p>
<p id="b586-6">
<em>
   It is so ordered.
  </em>
</p>


















<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b578-9">
   Article 6889-3 of the Revised Civil Statutes of Texas, enacted in 1951 and known as the Texas Communist Control Law, provides, among other things, that, various people and organizations defined by the law who fail to register with the Téxas Department of Public Safety are guilty of criminal offenses punishable by imprisonment of up to 10 years.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b579-6">
   The petitioner had obtained a certificate to transact business under this trade name in accordance with the Texas “Assumed Name Law.”
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b580-6">
   See
   <em>
    Pennsylvania
   </em>
   v.
   <em>
    Nelson,
   </em>
   <span class="citation" data-id="9883090"><a href="/opinion/105371/pennsylvania-v-nelson/" aria-description="Citation for case: Pennsylvania v. Nelson">350 U. S. 497</a></span>.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b580-7">
   See
   <em>
    Aguilar v. Texas,
   </em>
   <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span>.
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b582-8">
   See
   <em>
    Marcus
   </em>
   v.
   <em>
    Search Warrant,
   </em>
   <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717</a></span>, 724—729;
   <em>
    Frank v. Maryland,
   </em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360</a></span>, 363-366 and 376-377 (dissenting opinion); see also
   <em>
    Boyd
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b582-9">
   See Siebert, Freedom of the Press in England, 1476-1776, pp. 83, 85-86, 97.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b583-6">
   See Siebert,
   <em>
    supra,
   </em>
   pp. 374-376.
  </p>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b583-7">
   19 How. St. Tr. 1153 (1763).
  </p>
</div><div class="footnote" id="fn9" label="9">
<a class="footnote" href="#fn9_ref">
   9
  </a>
<p id="b583-8">
   19 How. St. Tr. 1029 (1765).
  </p>
</div><div class="footnote" id="fn10" label="10">
<a class="footnote" href="#fn10_ref">
   10
  </a>
<p id="b583-9">
   See Lasson, Development of the Fourth Amendment, p. 43.
  </p>
</div><div class="footnote" id="fn11" label="11">
<a class="footnote" href="#fn11_ref">
   11
  </a>
<p id="b583-10">
   II May’s Constitutional History of England, 246 (Am. ed. 1864).
  </p>
</div><div class="footnote" id="fn12" label="12">
<a class="footnote" href="#fn12_ref">
   12
  </a>
<p id="b583-11">
<em>
    Id.,
   </em>
   at 247.
  </p>
</div><div class="footnote" id="fn13" label="13">
<a class="footnote" href="#fn13_ref">
   13
  </a>
<p id="b584-7">
   “As every American statesman, during our revolutionary and formative period as a nation, was' undoubtedly familiar with this monument of English freedom, and considered it as the true and ultimate expression of constitutional law, it may be confidently asserted that its propositions were in the minds of those who framed the Fourth Amendment to the Constitution ...”
   <em>
    Boyd
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#626" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, at 626-627</a></span>.
  </p>
</div><div class="footnote" id="fn14" label="14">
<a class="footnote" href="#fn14_ref">
   14
  </a>
<p id="b584-8">
   19 How. St. Tr., at 1064.
  </p>
</div><div class="footnote" id="fn15" label="15">
<a class="footnote" href="#fn15_ref">
   15
  </a>
<p id="b584-9">
   See XVI Hansard’s Parliamentary History of England 207
   <em>
    et seq.
   </em>
</p>
</div><div class="footnote" id="fn16" label="16">
<a class="footnote" href="#fn16_ref">
   16
  </a>
<p id="b585-7">
   The word “books” in the context of a phrase like “books and records” has, of course, a quite different meaning. A “book” which is no more than a ledger of ah unlawful enterprise thus might stand on a quite different constitutional footing from the books involved in the present case. See
   <em>
    Marron
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#198" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 198-199</a></span>. And in some situations books even of the kind seized here might, -for purposes of the Fourth Amendment, be constitutionally indistinguishable from other'
   <em>
    goods
   </em>
   — e.
   <em>
    g.,
   </em>
   if the books were stolen' property.
  </p>
</div><div class="footnote" id="fn17" label="17">
<a class="footnote" href="#fn17_ref">
   17
  </a>
<p id="b585-8">
   See pp. 479-480, supra.
  </p>
</div><div class="footnote" id="fn18" label="18">
<a class="footnote" href="#fn18_ref">
   18
  </a>
<p id="b586-7">
   “The authority to the police officers under the warrants issued in this case . . . poses problems not raised by . . . warrants to seize ‘gambling implements’ and ‘all intoxicating liquors’.... For the use of these warrants implicates questions whether the procedures leading to their issuance and surrounding their execution were adequate to avoid suppression of constitutionally protected publications.”
   <em>
    Marcus
   </em>
   v.
   <em>
    Search Warrant,
   </em>
   <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#731" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717, at 731</a></span>.
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Stansbury v. California.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Stansbury v. California"
type: case
citation: "511 U.S. 318 (1994)"
parallel_cite: "114 S. Ct. 1526; 128 L. Ed. 2d 293"
neutral_cite: 1994 U.S. LEXIS 3293
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1994
date_decided: 1994-04-26
docket: 93-5770
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1994-04-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Stansbury v. California
  varies_by_point: false
  scope_note: Per curiam.
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/117843/stansbury-v-california/"
  cluster_id: 117843
  opinion_id: 9432992
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Berkemer v. McCarty]]", "[[Howes v. Fields]]"]
aliases: []
tags: ["case", "miranda", "custody", "objective-test"]
holding: "Custody is determined by the objective circumstances of the interrogation, not by the subjective, undisclosed views of the officer or…"
lake:
  record_id: Stansbury v. California
  status: verified
  projected_at: 2026-07-06
---

# Stansbury v. California

*511 U.S. 318 (1994)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police questioned Robert Stansbury about a child's murder, treating him initially as a potential witness rather than a suspect; during the questioning he made incriminating statements. The California Supreme Court had treated the officers' subjective view of whether Stansbury was a suspect as bearing on whether he was in custody.

## Issue
Whether a person is "in custody" for *[[Miranda v. Arizona|Miranda]]* purposes turns on the interrogating officer's subjective, undisclosed view that the person is a suspect.

## Rule
Custody is an objective inquiry. "We hold, not for the first time, that an officer's subjective and undisclosed view concerning whether the person being interrogated is a suspect is irrelevant to the assessment whether the person is in custody." — 511 U.S. at 318. ^pin-318

"[T]he initial determination of custody depends on the objective circumstances of the interrogation, not on the subjective views harbored by either the interrogating officers or the person being questioned." — *Id.* at 323. ^pin-323

## Application
Because the state court had relied on whether the officers subjectively regarded Stansbury as a suspect, it applied the wrong standard. The Court [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]] so that the custody question could be decided on the objective circumstances of the interrogation—whether a reasonable person would have felt restraint of the degree associated with a formal arrest—not on the officers' undisclosed suspicions.

## Conclusion
An officer's subjective, undisclosed suspicion is irrelevant to custody; the judgment was [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- Coheres with the objective custody analysis of [[Berkemer v. McCarty]] and [[Howes v. Fields]].

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Stansbury v. California*, 511 U.S. 318 (1994) — https://www.courtlistener.com/opinion/117843/stansbury-v-california/ — pinpoints: 318, 323.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "330fd2e95a695cc2", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Stansbury v. California"}, "payload": {"all": [{"cite": "511 U.S. 318", "page": "318", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "511"}, {"cite": "114 S. Ct. 1526", "page": "1526", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "114"}, {"cite": "128 L. Ed. 2d 293", "page": "293", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "128"}, {"cite": "1994 U.S. LEXIS 3293", "page": "3293", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1994"}], "display": "511 U.S. 318", "official": {"cite": "511 U.S. 318", "page": "318", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "511"}, "official_selection_present": true, "record_id": "Stansbury v. California"}}
{"assertion_id": "45315911a369b94f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-318", "record_id": "Stansbury v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-318", "pinpoint_status": "slip-only", "quote": "for *Miranda* purposes turns on the interrogating officer's subjective, undisclosed view that the person is a suspect. ## Rule Custody is an objective inquiry.", "quote_fidelity": "mismatch", "record_id": "Stansbury v. California", "star_marker": null}}
{"assertion_id": "8b8011e207ea2981", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-323", "record_id": "Stansbury v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-323", "pinpoint_status": "slip-only", "quote": "[T]he initial determination of custody depends on the objective circumstances of the interrogation, not on the subjective views harbored by either the interrogating officers or the person being questioned.", "quote_fidelity": "mismatch", "record_id": "Stansbury v. California", "star_marker": null}}
{"assertion_id": "4ae705eb1be2e34f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Stansbury v. California"}, "payload": {"as_of_content": "1994-04-26", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Stansbury v. California", "scope_note": "Per curiam.", "varies_by_point": false}}
```

### lake record — Stansbury v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Stansbury v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Stansbury v. California",
    "case_name_short": "Stansbury",
    "case_name_full": "Stansbury v. California",
    "input_case_name": "Stansbury v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1994-04-26",
    "year": 1994,
    "docket": "93-5770",
    "cluster_id": 117843,
    "lead_opinion_id": 9432992,
    "sibling_ids": [
      117843,
      9432992,
      9432993
    ],
    "absolute_url": "/opinion/117843/stansbury-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "511 U.S. 318",
      "volume": "511",
      "reporter": "U.S.",
      "page": "318",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "114 S. Ct. 1526",
        "volume": "114",
        "reporter": "S. Ct.",
        "page": "1526",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "128 L. Ed. 2d 293",
        "volume": "128",
        "reporter": "L. Ed. 2d",
        "page": "293",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1994 U.S. LEXIS 3293",
        "volume": "1994",
        "reporter": "U.S. LEXIS",
        "page": "3293",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "511 U.S. 318",
        "volume": "511",
        "reporter": "U.S.",
        "page": "318",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "114 S. Ct. 1526",
        "volume": "114",
        "reporter": "S. Ct.",
        "page": "1526",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "128 L. Ed. 2d 293",
        "volume": "128",
        "reporter": "L. Ed. 2d",
        "page": "293",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1994 U.S. LEXIS 3293",
        "volume": "1994",
        "reporter": "U.S. LEXIS",
        "page": "3293",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "511 U.S. 318",
    "official_selection": {
      "court_class": "scotus",
      "selected": "511 U.S. 318",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-318",
      "page": null,
      "quote": "for *Miranda* purposes turns on the interrogating officer's subjective, undisclosed view that the person is a suspect. ## Rule Custody is an objective inquiry.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-323",
      "page": null,
      "quote": "[T]he initial determination of custody depends on the objective circumstances of the interrogation, not on the subjective views harbored by either the interrogating officers or the person being questioned.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1994-04-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Stansbury v. California",
    "varies_by_point": false,
    "scope_note": "Per curiam.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Louisiana v. John Noehl and Analise Noehl",
          "cluster_id": 10618700,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jenkins v. State",
          "cluster_id": 10680001,
          "cite": [
            "894 S.E.2d 566",
            "317 Ga. 585"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Welch",
          "cluster_id": 4883662,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Barksdale",
          "cluster_id": 4867083,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Evelyn",
          "cluster_id": 4786331,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Tejada",
          "cluster_id": 4720843,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ricky Moreno v. State",
          "cluster_id": 4658088,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Cawthron",
          "cluster_id": 4500714,
          "cite": [
            "97 N.E.3d 671",
            "479 Mass. 612"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Mattox",
          "cluster_id": 4478290,
          "cite": [
            "2018 Ohio 992",
            "108 N.E.3d 1139"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Yarborough v. Alvarado",
          "cluster_id": 134748,
          "cite": [
            "158 L. Ed. 2d 938",
            "124 S. Ct. 2140",
            "541 U.S. 652",
            "2004 U.S. LEXIS 3843"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
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
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thompson v. Keohane",
          "cluster_id": 117982,
          "cite": [
            "133 L. Ed. 2d 383",
            "116 S. Ct. 457",
            "516 U.S. 99",
            "1995 U.S. LEXIS 8315",
            "95 Cal. Daily Op. Serv. 8968"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
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
        "journal_ref": "Stansbury v. California:lane2_top_cited"
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
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Zamudio",
          "cluster_id": 2634388,
          "cite": [
            "181 P.3d 105",
            "75 Cal. Rptr. 3d 289",
            "43 Cal. 4th 327",
            "2008 Cal. LEXIS 4431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Minjarez",
          "cluster_id": 2623400,
          "cite": [
            "81 P.3d 348",
            "2003 WL 22938909"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Rodrigues",
          "cluster_id": 2613958,
          "cite": [
            "885 P.2d 1",
            "8 Cal. 4th 1060",
            "36 Cal. Rptr. 2d 235",
            "94 Cal. Daily Op. Serv. 9194",
            "94 Daily Journal DAR 17083",
            "1994 Cal. LEXIS 6025"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Frye",
          "cluster_id": 5607916,
          "cite": [
            "18 Cal. 4th 894",
            "98 Cal. Daily Op. Serv. 5949",
            "959 P.2d 183",
            "98 Daily Journal DAR 8259",
            "77 Cal. Rptr. 2d 25",
            "1998 Cal. LEXIS 4688"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Howes v. Fields",
          "cluster_id": 623144,
          "cite": [
            "182 L. Ed. 2d 17",
            "132 S. Ct. 1181",
            "565 U.S. 499",
            "2012 U.S. LEXIS 1077",
            "2012 WL 538280"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
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
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Boyette",
          "cluster_id": 2544386,
          "cite": [
            "58 P.3d 391",
            "127 Cal. Rptr. 2d 544",
            "29 Cal. 4th 381"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
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
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Rogers",
          "cluster_id": 2633651,
          "cite": [
            "141 P.3d 135",
            "48 Cal. Rptr. 3d 1",
            "39 Cal. 4th 826",
            "2006 Cal. Daily Op. Serv. 7701",
            "2006 Daily Journal DAR 11065",
            "2006 Cal. LEXIS 9862"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lucas",
          "cluster_id": 1152592,
          "cite": [
            "907 P.2d 373",
            "12 Cal. 4th 415",
            "48 Cal. Rptr. 2d 525",
            "96 Daily Journal DAR 96",
            "96 Cal. Daily Op. Serv. 70",
            "1995 Cal. LEXIS 7350"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Walton",
          "cluster_id": 2355344,
          "cite": [
            "41 S.W.3d 75",
            "2001 Tenn. LEXIS 222"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Shatzer",
          "cluster_id": 1734,
          "cite": [
            "175 L. Ed. 2d 1045",
            "130 S. Ct. 1213",
            "559 U.S. 98",
            "2010 U.S. LEXIS 1899"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Patane",
          "cluster_id": 137003,
          "cite": [
            "159 L. Ed. 2d 667",
            "124 S. Ct. 2620",
            "542 U.S. 630",
            "2004 U.S. LEXIS 4577"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lewis",
          "cluster_id": 5607965,
          "cite": [
            "25 Cal. 4th 610",
            "22 P.3d 392",
            "2001 Cal. Daily Op. Serv. 3958",
            "106 Cal. Rptr. 2d 629",
            "2001 Daily Journal DAR 4843",
            "2001 Cal. LEXIS 3090"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Anderson",
          "cluster_id": 5607964,
          "cite": [
            "25 Cal. 4th 543",
            "106 Cal. Rptr. 2d 575",
            "2001 Cal. Daily Op. Serv. 3861",
            "2001 Daily Journal DAR 4715",
            "22 P.3d 347",
            "2001 Cal. LEXIS 3089"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estrada v. State",
          "cluster_id": 1890229,
          "cite": [
            "313 S.W.3d 274",
            "2010 Tex. Crim. App. LEXIS 722",
            "2010 WL 2382555"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "J. D. B. v. North Carolina",
          "cluster_id": 218925,
          "cite": [
            "180 L. Ed. 2d 310",
            "131 S. Ct. 2394",
            "564 U.S. 261",
            "2011 U.S. LEXIS 4557",
            "22 Fla. L. Weekly Fed. S 1135",
            "79 U.S.L.W. 4504"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Carpenter",
          "cluster_id": 5607872,
          "cite": [
            "15 Cal. 4th 312",
            "935 P.2d 708",
            "63 Cal. Rptr. 2d 1",
            "97 Cal. Daily Op. Serv. 3058",
            "97 Daily Journal DAR 5375",
            "1997 Cal. LEXIS 1948"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nenno v. State",
          "cluster_id": 1491957,
          "cite": [
            "970 S.W.2d 549",
            "1998 Tex. Crim. App. LEXIS 81",
            "1998 WL 331283"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herrera v. State",
          "cluster_id": 1872663,
          "cite": [
            "241 S.W.3d 520",
            "2007 Tex. Crim. App. LEXIS 1675",
            "2007 WL 4146707"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stansbury v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(117843 OR 9432992 OR 9432993) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTEyNjA0ODAwMDAwJnM9NDQ1MDU0NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28117843+OR+9432992+OR+9432993%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(117843 OR 9432992 OR 9432993)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yOTImcz0yMTcwNTUzJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28117843+OR+9432992+OR+9432993%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(117843 OR 9432992 OR 9432993)",
        "reviewed": 61,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 61,
        "triage_read": 2,
        "triage_snippet_classified": 59
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(117843 OR 9432992 OR 9432993)",
    "indexed_citing_opinions": 1598,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 117843,
        "count": 1378,
        "count_source": "search"
      },
      {
        "opinion_id": 9432992,
        "count": 243,
        "count_source": "search"
      },
      {
        "opinion_id": 9432993,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2603,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/stansbury-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNzYzNDgmcz0xMDM2ODE3NSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28117843+OR+9432992+OR+9432993%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 117843,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117843,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117843,
        "cited_id": 109430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117843,
        "cited_id": 109587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117843,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117843,
        "cited_id": 111023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117843,
        "cited_id": 111105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117843,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117843,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117843,
        "cited_id": 112152,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117843,
        "cited_id": 112452,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117843,
        "cited_id": 1282767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117843,
        "cited_id": 1367676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117843,
        "cited_id": 1504175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117843,
        "cited_id": 2131068,
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
    "date_created": "2026-07-05T20:24:13Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:24:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:24:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:26:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:24:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Stansbury v. California

```
<opinion type="majority">
<author id="b393-5">Per Curiam.</author>
<p id="b393-6">This case concerns the rules for determining whether a person being questioned by law enforcement officers is held in custody, and thus entitled to the warnings required by <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). We hold, not for the first time, that an officer’s subjective and undisclosed view concerning whether the person being interrogated is a suspect is irrelevant to the assessment whether the person is in custody.</p>
<p id="b393-7">I</p>
<p id="b393-8">Ten-year-old Robyn Jackson disappeared from a playground in Baldwin Park, California, at around 6:30 p.m. on September 28, 1982. Early the next morning, about 10 miles away in Pasadena, Andrew Zimmerman observed a large man emerge from a turquoise American, sedan and throw something into a nearby flood control channel. Zimmerman called the police, who arrived at the seene and discovered the girl’s body in the channel. There was evidence that she had been raped, and the cause of death was determined to be asphyxia complicated by blunt force trauma to the head.</p>
<p id="b393-9">Lieutenant Thomas Johnston, a detective with the Los Angeles County Sheriff’s Department, investigated the hom<page-number citation-index="1" label="320">*320</page-number>icide. From witnesses interviewed on the day the body was discovered, he learned that Robyn had talked to two ice cream truck drivers, one being petitioner Robert Edward Stansbury, in the hours before her disappearance. Given these contacts, Johnston thought Stansbury and the other driver might have some connection with the homicide or knowledge thereof, but for reasons unimportant here Johnston considered only the other driver to be a leading suspect. After the suspect driver was brought in for interrogation, Johnston asked Officer Lee of the Baldwin Park Police Department to contact Stansbury to see if he would come in for questioning as a potential witness.</p>
<p id="b394-5">Lee and three other plainclothes officers arrived at Stansbury’s trailer home at about 11:00 that evening. The officers surrounded the door and Lee knocked. When Stansbury answered, Lee told him the officers were investigating a homicide to which Stansbury was a possible witness and asked if he would accompany them to the police station to answer some questions. Stansbury agreed to the interview and accepted a ride to the station in the front seat of Lee’s police car.</p>
<p id="b394-6">At the station, Lieutenant Johnston, in the presence of another officer, questioned Stansbury about his whereabouts and activities during the afternoon and evening of September 28. Neither Johnston nor the other officer issued <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. Stansbury told the officers (among other things) that on the evening of the 28th he spoke with the victim at about 6:00, returned to his trailer home after work at 9:00, and left the trailer at about midnight in his housemate’s turquoise, American-made car. This last detail aroused Johnston’s suspicions, as the turquoise car matched the description of the one Andrew Zimmerman had observed in Pasadena. When Stansbury, in response to a further question, admitted to prior convictions for rape, kidnaping, and child molestation, Johnston terminated the interview and another officer advised Stansbury of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. <page-number citation-index="1" label="321">*321</page-number>Stansbury declined to make further statements, requested an attorney, and was arrested. Respondent State of California charged Stansbury with first-degree murder and other crimes.</p>
<p id="b395-5">Stansbury filed a pretrial motion to suppress all statements made at the station, and the evidence discovered as a result of those statements. The trial court denied the motion in relevant part, ruling that Stansbury was not “in custody” — and thus not entitled to <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings — until he mentioned that he had taken his housemate’s turquoise car for a midnight drive. Before that stage of the interview, the trial court reasoned, “the focus in [Lieutenant Johnston’s] mind certainly was on the other ice cream [truck] driver,” Tr. 2368; only “after Mr. Stansbury made the comment . . . describing the . . . turquoise-colored automobile” did Johnston’s suspicions “shif[t] to Mr. Stansbury,” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">ibid.</a></span> </em>Based upon its conclusion that Stansbury was not in custody until Johnston’s suspicions had focused on him, the trial court permitted the prosecution to introduce in its case in chief the statements Stansbury made before that time. At trial, the jury convicted Stansbury of first-degree murder, rape, kidnaping, and lewd act on a child under the age of 14, and fixed the penalty for the first-degree murder at death.</p>
<p id="b395-6">The California Supreme Court affirmed. Before determining whether Stansbury was in custody during the interview at the station, the court set out what it viewed as the applicable legal standard:</p>
<blockquote id="b395-7">“In deciding the custody issue, the totality of the circumstances is relevant, and no one factor is dispositive. However, the most important considerations include (1) the. site of the interrogation, (2) whether the investigation has focused on the subject, (3) whether the objective indicia of arrest are present, and (4) the length and form of questioning.” <span class="citation" data-id="9604223"><a href="/opinion/1367676/people-v-stansbury/#1050" aria-description="Citation for case: People v. Stansbury">4 Cal. 4th 1017, 1050</a></span>, 846 R 2d 756, 775 (1993) (internal quotation marks omitted).</blockquote>
<p id="b396-4"><page-number citation-index="1" label="322">*322</page-number>The court proceeded to analyze the second factor in detail, in the end accepting the trial court’s factual determination “that suspicion focused on [Stansbury] only when he mentioned that he had driven a turquoise car on the night of the crime.” <span class="citation" data-id="9604223"><a href="/opinion/1367676/people-v-stansbury/#1052" aria-description="Citation for case: People v. Stansbury"><em>Id., </em>at 1052</a></span>, <span class="citation" data-id="9604223"><a href="/opinion/1367676/people-v-stansbury/#776" aria-description="Citation for case: People v. Stansbury">846 P. 2d, at 776</a></span>. The court “conclude[d] that [Stansbury] was not subject to custodial interrogation before he mentioned the turquoise car,” and thus approved the trial court’s ruling that <em>Miranda </em>v. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona</a></span> </em>did not bar the admission of statements Stansbury made before that point. <span class="citation" data-id="9604223"><a href="/opinion/1367676/people-v-stansbury/#1054" aria-description="Citation for case: People v. Stansbury">4 Cal. 4th, at 1054</a></span>, <span class="citation" data-id="9604223"><a href="/opinion/1367676/people-v-stansbury/#777" aria-description="Citation for case: People v. Stansbury">846 P. 2d, at 777-778</a></span>.</p>
<p id="b396-5">We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./510/943/">510 U. S. 943</a></span> (1993).</p>
<p id="b396-6">II</p>
<p id="b396-7">We held in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>that a person questioned by law enforcement officers after being “taken into custody or otherwise deprived of his freedom of action in any significant way” must first “be warned that he has a right to remain silent, that any statement he does make may be used as evidence against him, and that he has a right to the presence of an attorney, either retained or appointed.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444</a></span>. Statements elicited in noncompliance with this rule may not be admitted for certain purposes in a criminal trial. Compare <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#492" aria-description="Citation for case: Miranda v. Arizona"><em>id., </em>at 492, 494</a></span>, with <em>Harris </em>v. <em>New York, </em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971). An officer’s obligation to administer <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings attaches, however, “only where there has been such a restriction on a person’s freedom as to render him ‘in custody.’” <em>Oregon </em>v. <em>Mathiason, </em><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U. S. 492, 495</a></span> (1977) <em>(per curiam); </em>see also <em>Illinois </em>v. <em>Perkins, </em><span class="citation" data-id="9432050"><a href="/opinion/112452/illinois-v-perkins/#296" aria-description="Citation for case: Illinois v. Perkins">496 U. S. 292, 296</a></span> (1990). In determining whether an individual was in custody, a court must examine all of the circumstances surrounding the interrogation, but “the ultimate inquiry is simply whether there [was] a ‘formal arrest or restraint on freedom of movement’ of the degree associated with a formal arrest.” <em>California </em>v. <em>Beheler, </em><span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1125" aria-description="Citation for case: California v. Beheler">463 U. S. 1121, 1125</a></span> (1983) <em>(per curiam) </em>(quoting <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason"><em>Mathiason, supra, </em>at 495</a></span>).</p>
<p id="b397-4"><page-number citation-index="1" label="323">*323</page-number>Our decisions make clear that the initial determination of custody depends on the objective circumstances of the interrogation, not on the subjective views harbored by either the interrogating officers or the person being questioned. In <em>Beckwith </em>v. <em>United States, </em><span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/" aria-description="Citation for case: Beckwith v. United States">425 U. S. 341</a></span> (1976), for example, the defendant, without being advised of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, made incriminating statements to Government agents during an interview in a private home. He later asked that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>“be extended to cover interrogation in noncustodial circumstances after a police investigation has focused on the suspect.” <span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/#345" aria-description="Citation for case: Beckwith v. United States">425 U. S., at 345</a></span> (internal quotation marks omitted). We found his argument unpersuasive, explaining that it “was the compulsive aspect of custodial interrogation, and not the strength or content of the government’s suspicions at the time the questioning was conducted, which led the Court to impose the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requirements with regard to custodial questioning.” <em>Id., </em>at 346-347 (internal quotation marks omitted). As a result, we concluded that the defendant was not entitled to <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings: “Although the ‘focus’ of an investigation may indeed have been on Beckwith at the time of the interview ... , he hardly found himself in the custodial situation described by the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>Court as the basis for its holding.” <span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/#347" aria-description="Citation for case: Beckwith v. United States">425 U. S., at 347</a></span>.</p>
<p id="b397-5"><em>Berkemer </em>v. <em>McCarty, </em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420</a></span> (1984), reaffirmed the conclusions reached in <em>Beckwith. Berkemer </em>concerned the roadside questioning of a motorist detained in a traffic stop. We decided that the motorist was not in custody for purposes of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>even though the traffic officer “apparently decided as soon as [the motorist] stepped out of his car that [the motorist] would be taken into custody and charged with a traffic offense.” <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#442" aria-description="Citation for case: Berkemer v. McCarty">468 U. S., at 442</a></span>. The reason, we explained, was that the officer “never communicated his intention to” the motorist during the relevant questioning. <em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Ibid.</a></span> </em>The lack of communication was crucial, for under <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>“[a] policeman’s unarticulated plan has no bearing on the question whether a suspect was ‘in custody’ at a particular <page-number citation-index="1" label="324">*324</page-number>time”; rather, “the only relevant inquiry is how a reasonable man in the suspect’s position would have understood his situation.” <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#442" aria-description="Citation for case: Berkemer v. McCarty">468 U. S., at 442</a></span>. Other cases of ours have been consistent in adhering to this understanding of the custody element of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>See, <em>e. g., Mathias on, supra, </em>at 495 (“Nor is the requirement of warnings to be imposed simply because . . . the questioned person is one whom the police suspect. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings are required only where there has been such a restriction on a person’s freedom as to render him ‘in custody’”); <span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1124" aria-description="Citation for case: California v. Beheler"><em>Beheler, supra, </em>at 1124, n. 2</a></span> (“Our holding in <em><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">Mathiason</a></span> </em>reflected our earlier decision in <em>[Beck-with], </em>in which we rejected the notion that the ‘in custody’ requirement was satisfied merely because the police interviewed a person who was the ‘focus’ of a criminal investigation”); <em>Minnesota </em>v. <em>Murphy, </em><span class="citation" data-id="9429504"><a href="/opinion/111105/minnesota-v-murphy/#431" aria-description="Citation for case: Minnesota v. Murphy">465 U. S. 420, 431</a></span> (1984) (“The mere fact that an investigation has focused on a suspect does not trigger the need for <em>Miranda </em>warnings in noncustodial settings, and the probation officer’s knowledge and intent have no bearing on the outcome of this case”) (citation omitted); cf. <em>Pennsylvania </em>v. <em>Bruder, </em><span class="citation" data-id="9431478"><a href="/opinion/112152/pennsylvania-v-bruder/#11" aria-description="Citation for case: Pennsylvania v. Bruder">488 U. S. 9, 11, n. 2</a></span> (1988).</p>
<p id="b398-5">It is well settled, then, that a police officer’s subjective view that the individual under questioning is a suspect, if undisclosed, does not bear upon the question whether the individual is in custody for purposes of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>See F. Inbau, J. Reid, &amp; J. Buckley, Criminal Interrogation and Confessions 232, 236, 297-298 (3d ed. 1986). The same principle obtains if an officer’s undisclosed assessment is that the person being questioned is not a suspect. In either instance, one cannot expect the person under interrogation to probe the officer’s innermost thoughts. Save as they are communicated or otherwise manifested to the person being ques-. tioned, an officer’s evolving but unarticulated suspicions do not affect the objective circumstances of an interrogation or interview, and thus cannot affect the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>custody inquiry. “The threat to a citizen’s Fifth Amendment rights <page-number citation-index="1" label="325">*325</page-number>that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was designed to neutralize has little to do with the strength of an interrogating officer’s suspicions.” <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#435" aria-description="Citation for case: Berkemer v. McCarty"><em>Berkemer, supra, </em>at 435, n. 22</a></span>.</p>
<p id="b399-5">An officer’s knowledge or beliefs may bear upon the custody issue if they are conveyed, by word or deed, to the individual being questioned. Cf. <em>Michigan </em>v. <em>Chesternut, </em><span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#575" aria-description="Citation for case: Michigan v. Chesternut">486 U. S. 567,575, n. 7</a></span> (1988) (citing <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544,554, n. 6</a></span> (1980) (opinion of Stewart, J.)). Those beliefs are relevant only to the extent they would affect how a reasonable person in the position of the individual being questioned would gauge the breadth of his or her “ ‘freedom of action.’” <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#440" aria-description="Citation for case: Berkemer v. McCarty"><em>Berkemer, supra, </em>at 440</a></span>. Even a clear statement from an officer that the person under interrogation is a prime suspect is not, in itself, dispositive of the custody issue, for some suspects are free to come and go until the police decide to make an arrest. The weight and pertinence of any communications regarding the officer’s degree of suspicion will depend upon the facts and circumstances of the particular case. In sum, an officer’s views concerning the nature of an interrogation, or beliefs concerning the potential culpability of the individual being questioned, may be one among many factors that bear upon the assessment whether that individual was in custody, but only if the officer’s views or beliefs were somehow manifested to the individual under interrogation and would have affected how a reasonable person in that position would perceive his or her freedom to leave. (Of course, instances may arise in which the officer’s undisclosed views are relevant in testing the credibility of his or her account of what happened during an interrogation; but it is the objective surroundings, and not any undisclosed views, that control the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>custody inquiry.)</p>
<p id="b399-6">We decide on this state of the record that the California Supreme Court’s analysis of whether Stansbury was in custody is not consistent in all respects with the foregoing principles. Numerous statements in the court’s opinion are open <page-number citation-index="1" label="326">*326</page-number>to the interpretation that the court regarded the officers’ subjective beliefs regarding Stansbury’s status as a suspect (or nonsuspect) as significant in and of themselves, rather than as relevant only to the extent they influenced the objective conditions surrounding his interrogation. See <span class="citation" data-id="9604223"><a href="/opinion/1367676/people-v-stansbury/#1050" aria-description="Citation for case: People v. Stansbury">4 Cal. 4th, at 1050</a></span>, <span class="citation" data-id="9604223"><a href="/opinion/1367676/people-v-stansbury/#775" aria-description="Citation for case: People v. Stansbury">846 P. 2d, at 775</a></span> (“whether the investigation ha[d] focused on the” person being questioned is among the “most important considerations” in assessing whether the person was in custody). So understood, the court’s analysis conflicts with our precedents. The court’s apparent conclusion that Stansbury’s <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights were triggered by virtue of the fact that he had become the focus of the officers’ suspicions, see <span class="citation" data-id="9604223"><a href="/opinion/1367676/people-v-stansbury/#1052" aria-description="Citation for case: People v. Stansbury">4 Cal. 4th, at 1052, 1054</a></span>, <span class="citation" data-id="9604223"><a href="/opinion/1367676/people-v-stansbury/#776" aria-description="Citation for case: People v. Stansbury">846 P. 2d, at 776, 777-778</a></span>; cf., <em>e.g., State </em>v. <em>Blanding, </em><span class="citation" data-id="1282767"><a href="/opinion/1282767/state-v-blanding/#586" aria-description="Citation for case: State v. Blanding">69 Haw. 583, 586-587</a></span>, <span class="citation" data-id="1282767"><a href="/opinion/1282767/state-v-blanding/#101" aria-description="Citation for case: State v. Blanding">752 P. 2d 99, 101</a></span> (1988); <em>State </em>v. <em>Hartman, </em><span class="citation" data-id="9642566"><a href="/opinion/1504175/state-v-hartman/#120" aria-description="Citation for case: State v. Hartman">703 S. W. 2d 106, 120</a></span> (Tenn. 1985), cert, denied, <span class="citation multiple-matches"><a href="/c/U.%20S./478/1010/">478 U. S. 1010</a></span> (1986); <em>People </em>v. <em>Herdon, </em><span class="citation multiple-matches"><a href="/c/Cal.%20App.%203d/42/300/">42 Cal. App. 3d 300</a></span>, 307, n. 10, <span class="citation multiple-matches"><a href="/c/Cal.%20Rptr./116/641/">116 Cal. Rptr. 641</a></span>, 645, n. 10 (1974), is incorrect as well. Our cases make clear, in no uncertain terms, that any inquiry into whether the interrogating officers have focused their suspicions upon the individual being questioned (assuming those suspicions remain undisclosed) is not relevant for purposes of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>See generally 1 W. LaFave &amp; J. Israel, Criminal Procedure §6.6(a), pp. 489-490 (1984).</p>
<p id="b400-5">The State acknowledges that Lieutenant Johnston’s and the other officers’ subjective and undisclosed suspicions (or lack thereof) do not bear upon the question whether Stansbury was in custody, for purposes of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>during the station house interview. It maintains, however, that the objective facts in the record support a finding that Stansbury was not in custody until his arrest. Stansbury, by contrast, asserts that the objective circumstances show that he was in custody during the entire interrogation. We think it appropriate for the California Supreme Court to consider this question in the first instance. We therefore reverse its <page-number citation-index="1" label="327">*327</page-number>judgment and remand the case for further proceedings not inconsistent with this opinion.</p>
<p id="b401-5">
<em>It is so ordered.</em>
</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/State v. Christensen.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: State v. Christensen
type: case
citation: "2017 Tenn. LEXIS 195 (2017)"
parallel_cite: 517 S.W.3d 60
neutral_cite: 2017 WL 1291657
court: Tenn.
court_level: state
circuit: ""
year: 2017
date_decided: 2017-04-07
docket: W2014-00931-SC-R11-CD
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
  opinion_url: "https://www.courtlistener.com/opinion/4381703/state-of-tennessee-v-james-robert-christensen-jr/"
  cluster_id: 4381703
  opinion_id: null
  identity_checked: true
lake:
  record_id: State v. Christensen
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Knock and Talk]]"
    role: Key
related:
  - "[[Knock and Talk]]"
  - "[[Florida v. Jardines]]"
  - "[[Katz v. United States]]"
tags:
  - case
  - fourth-amendment
  - knock-and-talk
  - curtilage
  - implied-license
  - no-trespassing
  - jardines
holding: "'No Trespassing' signs posted near an unobstructed driveway do not, by themselves, revoke the implied license that permits police to approach a home and conduct a knock-and-talk; only barriers like a fence and closed gate that physically block access will do so."
---

# State v. Christensen

*517 S.W.3d 60 (Tenn. 2017)* (2017 Tenn. LEXIS 195) (No. W2014-00931-SC-R11-CD) · Supreme Court of Tennessee · **Persuasive — state, illustrative** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 4381703 → lead opinion 4158956 (517 S.W.3d 60, decided 2017-04-07); Rule quote string-matched to the CL opinion text 2026-07-07. CL text is slip-paginated (no S.W.3d star pagination), so the pin is slip-style per S2 A3. S9 promotes. -->

## Background
Acting on a tip that Christensen was operating a methamphetamine lab, investigators drove up his long rural driveway — past several "No Trespassing" signs — to his home to conduct a [[Knock and Talk|knock-and-talk]]. They detected evidence of a meth lab and ultimately obtained a warrant. Christensen moved to suppress, arguing that his posted signs revoked any implied license for officers to enter his property, making the [[Knock and Talk|knock-and-talk]] an unlawful [[Curtilage|curtilage]] intrusion under *[[Florida v. Jardines]]*.

## Issue
Whether "No Trespassing" signs posted along an otherwise unobstructed driveway revoke the implied license that allows a police officer to approach a residence to conduct a [[Knock and Talk|knock-and-talk]].

## Rule
The Tennessee Supreme Court held they do not. A [[Knock and Talk|knock-and-talk]] within constitutional bounds is a legitimate reason to enter [[Curtilage|curtilage]], and ambiguous signage does not withdraw the customary invitation that *[[Florida v. Jardines|Jardines]]* recognized visitors enjoy: "we hold that, under the totality of the circumstances, the Defendant's 'No Trespassing' signs posted near his unobstructed driveway were not sufficient to revoke the implied license referred to in *Jardines*." — slip op. at 18. Only a physical barrier such as "a fence and a closed gate" — not "mere ambiguous signage and unkemptness" — may revoke that license.

## Application
The court reasoned that a "No Trespassing" sign merely makes explicit the ordinary rule that entrants need a legitimate reason to be on the land; a lawful [[Knock and Talk|knock-and-talk]] supplies exactly such a reason. The defendant's added factors — overgrown vegetation, debris, and the length of the driveway — did not transform the approach into a trespass, because they would not have deterred a reasonably respectful visitor from approaching the home. (The court separately applied the reasonable-expectation-of-privacy test of *[[Katz v. United States|Katz]]* and reached the same result.)

## Conclusion
The defendant was **not entitled to relief** on the implied-license theory; the [[Knock and Talk|knock-and-talk]] did not violate the Fourth Amendment.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Christensen* is a leading state-high-court application of *[[Florida v. Jardines]]*'s implied-license framework to the recurring "No Trespassing" problem, holding that ordinary signage does not, by itself, defeat the customary license underlying the [[Knock and Talk|knock-and-talk]].

## Appears on
- [[Knock and Talk]] — *Key*

## Sources
- [*State v. Christensen*, 517 S.W.3d 60 (Tenn. 2017)](https://www.courtlistener.com/opinion/4381703/state-of-tennessee-v-james-robert-christensen-jr/) — pinpoint: slip op. at 18 (implied-license holding); the CL opinion text carries the slip-opinion page numbers rather than 517 S.W.3d star pagination, so the pin is slip-style per S2 A3. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "608da4abe4f8db6e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "State v. Christensen"}, "payload": {"all": [{"cite": "517 S.W.3d 60", "page": "60", "reporter": "S.W.3d", "selected_official": false, "source": "cluster.citations[]", "type": 3, "volume": "517"}, {"cite": "2017 WL 1291657", "page": "1291657", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2017"}, {"cite": "2017 Tenn. LEXIS 195", "page": "195", "reporter": "Tenn. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "2017"}], "display": "2017 Tenn. LEXIS 195", "official": {"cite": "2017 Tenn. LEXIS 195", "page": "195", "reporter": "Tenn. LEXIS", "selected_official": true, "source": "cluster.citations[]", "type": 2, "volume": "2017"}, "official_selection_present": true, "record_id": "State v. Christensen"}}
{"assertion_id": "372a487c55ea6260", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "State v. Christensen"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "State v. Christensen", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — State v. Christensen

```json
{
  "schema_version": "s2.v1",
  "record_id": "State v. Christensen",
  "status": "under_review",
  "identity": {
    "case_name": "State of Tennessee v. James Robert Christensen, Jr.",
    "case_name_short": "",
    "case_name_full": "STATE of Tennessee v. James Robert CHRISTENSEN, Jr.",
    "input_case_name": "State v. Christensen",
    "court": "Tenn.",
    "court_id": null,
    "court_level": "state",
    "circuit": null,
    "state": "Tennessee",
    "date_decided": "2017-04-07",
    "year": 2017,
    "docket": "W2014-00931-SC-R11-CD",
    "cluster_id": 4381703,
    "lead_opinion_id": 9874089,
    "sibling_ids": [],
    "absolute_url": "/opinion/4381703/state-of-tennessee-v-james-robert-christensen-jr/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "2017 Tenn. LEXIS 195",
      "volume": "2017",
      "reporter": "Tenn. LEXIS",
      "page": "195",
      "type": 2,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "517 S.W.3d 60",
        "volume": "517",
        "reporter": "S.W.3d",
        "page": "60",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2017 WL 1291657",
        "volume": "2017",
        "reporter": "WL",
        "page": "1291657",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "517 S.W.3d 60",
        "volume": "517",
        "reporter": "S.W.3d",
        "page": "60",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 WL 1291657",
        "volume": "2017",
        "reporter": "WL",
        "page": "1291657",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 Tenn. LEXIS 195",
        "volume": "2017",
        "reporter": "Tenn. LEXIS",
        "page": "195",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "2017 Tenn. LEXIS 195",
    "official_selection": {
      "court_class": "state",
      "selected": "2017 Tenn. LEXIS 195",
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
    "date_created": "2026-07-07T01:38:24Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:38:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:38:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:38:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:38:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "state-v-christensen--4381703",
      "to_record_id": "State v. Christensen",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — State v. Christensen

```
<opinion type="majority">
<p id="b79-16">OPINION</p>
<author id="b79-17">Jeffrey S. Bivins, C.J.,</author>
<p id="AvW">delivered the opinion of the Court,</p>
<judges id="AZ-">in which Cornelia A. Clark and Holly Kirby, JJ., joined. Sharon G. Lee, J., filed a dissenting opinion. Roger A. Page, J., not participating.</judges>
<p id="b79-19">James Robert Christensen, Jr., (“the Defendant”) was convicted by a jury of resisting arrest, promoting the manufacture of methamphetamine, initiating the manufacture of methamphetamine, and two counts of possession of a firearm during the commission of a dangerous felony. Prior to trial, the Defendant moved to suppress evidence obtained through what he claimed was an illegal search. The trial court denied the Defendant’s motion and also denied the Defendant’s motion seeking an interlocutory appeal. On direct appeal following trial, the Court of Criminal Appeals affirmed the trial court’s judgments, including the trial court’s ruling on the suppression issue. We granted the Defendant’s application for permission to appeal in order to address the legality of the police officers’ warrantless entry onto the curtilage of the Defendant’s residence. We hold that the officers’ entry onto the De<page-number citation-index="1" label="64">*64</page-number>fendant’s property was constitutionally permissible in spite of the posted “No Trespassing” signs near the Defendant’s unobstructed driveway. Accordingly, we affirm the judgment of the Court of Criminal Appeals.</p>
<p id="b80-4">Factual and Procedural Background</p>
<p id="b80-5">In August 2013, two law enforcement officers drove down the Defendant’s unobstructed driveway, parked near his residence, and walked up to the Defendant’s front porch. The Defendant opened his front door, stepped onto his porch, and closed and locked the front door behind him. After the Defendant opened his door, the officers smelled the odor of methamphetamine being manufactured. They asked the Defendant for consent to enter his residence, but the Defendant refused to give consent. One of the officers then forced open the front door, while the other officer detained the Defendant. Inside the residence, the entering officer discovered an active methamphetamine lab, along with several inactive labs, various items commonly associated with the manufacture of methamphetamine, and several guns. The Defendant subsequently was indicted on one count each of resisting arrest, promoting the manufacture of methamphetamine, and initiating the manufacture of methamphetamine, and two counts of possession of a firearm during the commission of a dangerous felony.</p>
<p id="b80-6">Prior to trial, the Defendant filed a motion to suppress evidence, claiming that the evidence had been seized as the result of an unlawful search because he had posted “No Trespassing” signs near his driveway. The Defendant asserted that the officers’ entry onto his property without a warrant violated both the United States and Tennessee Constitutions. After a hearing, the trial court denied the motion. The Defendant then filed a motion for interlocutory appeal, which the trial court also denied. Accordingly, the Defendant proceeded to a jury trial, and he was convicted as charged. The Court of Criminal Appeals affirmed the Defendant’s convictions and sentences. State v. Christensen, No. W2014-00931-CCA-R3-CD, <span class="citation no-link">2015 WL 2330185</span>, at *11 (Tenn. Crim. App. May 14, 2015).<footnotemark>1</footnotemark></p>
<p id="b80-11">Before this Court, the Defendant challenges only the denial of his motion to suppress. We summarize below the relevant proof adduced at the suppression hearing and the trial.<footnotemark>2</footnotemark></p>
<p id="b80-12">On August 3, 2013, Investigators Michael Green and Brent Chunn, narcotics investigators for the Tipton County Sheriffs Office, went to a residence on Beaver Creek Lane in Tipton County after receiving information regarding a pseudoephed-rine purchase at a Kroger by Mariah Davis. They also received information from an informant named Kyle Wolfe regarding an individual named Cody Gatlin, who was in a relationship with Ms. Davis. Investigator Green was familiar with Mr. Gatlin “through [his] law enforcement career.”</p>
<p id="b80-13">At this residence, the investigators spoke with Ms. Davis, Mr. Gatlin, and John Harkness.<footnotemark>3</footnotemark> The investigators first spoke with Ms. Davis and questioned her <page-number citation-index="1" label="65">*65</page-number>about her pseudoephedrine purchase. Initially, she told the investigators that she had taken the medicine to her grandmother’s house in Mason, The investigators then asked if Mr. Gatlin was home. While Mr. Gatlin was not initially present, he eventually walked over from the Defendant’s residence next door, about forty to fifty feet away. During this time, Investigator Green observed the Defendant, over at his residence, looking “out [his] screen door over to where [they] were.”</p>
<p id="b81-4">When the investigators asked Mr. Gatlin about the pseudoephedrine purchase, he replied that he had taken the pills next door to the Defendant, who was in the process of using them to make methamphetamine. At that point, the investigators backed down Mr. Harkness’ driveway and drove thirty to forty feet to the Defendant’s driveway next door. The investigators then drove down the Defendant’s driveway and parked near the Defendant’s trailer home.</p>
<p id="b81-5">Investigator Green described the Defendant’s driveway as being gravel and approximately sixty to seventy yards long, with a sign near the roadway that said “no spraying.” He did not recall, however, seeing a “No Trespassing" sign. Investigator Chunn did not recall seeing any posted signs when they entered the Defendant’s property. Because it was summertime, the grass was very tall. Investigator Green estimated that the grass “would come up probably to my chin, and I’m six three.”</p>
<p id="b81-6">As the officers walked up to the Defendant’s front porch, the Defendant, holding a cane, opened the door and walked out to meet them. As soon as the Defendant opened the door, both investigators smelled an overwhelming odor associated with the manufacture of methamphetamine, even though the Defendant was several feet from the investigators at the time. Investigator Green explained that the smell differed from methamphetamine in its finished product state, in that</p>
<blockquote id="AcU">[w]hen the chemical reaction is actually taking place, your smells are louder, you know. And at the finished product you’ve basically just got a powder there that maybe if you open a bag you’ll get a hit [sic] of starter fluid or something, but nothing like it is when it’s being manufactured.</blockquote>
<p id="b81-9">From his training with methamphetamine, Investigator Green knew that methamphetamine labs were “very volatile,” in that they could catch on fire quickly.</p>
<p id="b81-10">As the investigators explained to the Defendant why they were there, the Defendant denied any illegal activity. The investigators asked for consent to enter the residence because the Defendant initially seemed cooperative, and, according to Investigator Green, he “would much rather have consent than ... just have to kick a door in.” When the Defendant denied consent, however, the investigators decided to enter the trailer “[d]ue to .,. exigent circumstances.” According to Investigator Green, there was no time to obtain a search warrant because</p>
<blockquote id="Abk">Methamphetamine is basically, it’s starter fluid, ammonium nitrate. It’s a bomb in a bottle. It builds up pressure in a bottle. If you’re not there to release that pressure, it’s going to blow out, blow up, whatever you want to call it. So exigent circumstances, it’s I don’t have time to go get a search warrant. I’ve got to get in that house and make it safe right now. If I wait, it’s going to blow up on us.</blockquote>
<p id="b81-11">Investigator Chunn forced open the locked front door to the residence and entered to “make sure no one else was inside,” while Investigator Green attempted to detain the Defendant. Investigator Green and the Defendant engaged in a struggle, and Investigator Chunn, after <page-number citation-index="1" label="66">*66</page-number>“clearing] the residence,” stepped back outside to assist in apprehending the Defendant. While Investigator Green struggled to handcuff the Defendant, the Defendant called for “Bear,” which Investigator Green later learned was a dog. The Defendant also screamed for his mother, who was in the other trailer on the property, to call 1-800-THE-FIRM.<footnotemark>4</footnotemark></p>
<p id="b82-4">Investigator Green confirmed that the Defendant probably told him at some point to get off his property but stated that it was after Investigator Green attempted to detain him. Investigator Chunn recalled that, when they arrived on the Defendant’s property, the Defendant asked the officers some type of question as to why they were there, but he did not recall the Defendant telling them to get off his property at that point.</p>
<p id="b82-5">At approximately the same time they had detained the Defendant, the patrol deputies arrived, and Investigator Green had the Defendant sit down and provided him some water. At that time, the Defendant said, “It’s in the freezer. It’s in the freezer.” Investigator Green then yelled to Investigator Chunn, who was inside the residence with the other officers, that the lab was located in the freezer. Investigator Chunn brought the active lab outside, and at some point, the officers had to relieve pressure in the bottle.</p>
<p id="b82-6">Upon entering the Defendant’s residence, Investigator Green found the house to be “very unkept.” Additionally, he observed the following:</p>
<blockquote id="b82-7">When I entered I noticed there was a bolt action 410 pistol right at the door, a 410 shotgun and a rifle on the couch.... And there was—Investigator Chunn had located the active meth lab and took it out, and then we saw remnants of, you know, older cooks, several cans of empty Coleman fuel, and then we located the ten separate one-pot labs in the freezer.</blockquote>
<p id="b82-10">Investigator Green clarified at trial that the pistol at the door actually was a 410 shotgun that had been sawed off. The sawed-off shotgun was loaded with two or three rounds. The other 410 shotgun had a laser on the barrel. Investigator Green believed the Defendant “intended to go armed” even though the guns were inside the locked residence.</p>
<p id="b82-11">Investigator Chunn confirmed that the active methamphetamine lab was found in the refrigerator freezer. He noted that it was uncommon to find an active lab in the freezer but that the Defendant told them later in a statement that he placed the lab in the freezer “to stop the reaction process so he would be able to restart the lab at a later date or sometime later.” Investigator Chunn estimated that it takes approximately one to four hours to manufacture methamphetamine using the “shake and bake” method. He could not say, however, how close the active lab was to completing the manufacturing process when they found it at the Defendant’s residence.</p>
<p id="b82-12">The officers found ten “already cooked off’ labs located in a deep freezer inside the residence. The officers also found:</p>
<blockquote id="b82-13">one pound of drain opener or lye; a 32-ounce bottle of drain opener liquid; four empty Coleman cans; one-half gallon of Coleman; two jars with Coleman fuel; ... eight [hydrochloric acid] generators; a bag of live trash; a bag of Epsom salt; and the empty box of pseudoephedrine, the box itself that had just been purchased.</blockquote>
<p id="af-dedup-0"><page-number citation-index="1" label="67">*67</page-number>Investigator Chunn identified a picture of the bathtub in the master bathroom, which contained “a bag of dog food with empty, numerous empty bottles that were previous methamphetamine labs.”</p>
<p id="b83-5">The officers wanted to leave the Defendant’s residence as quickly as possible because of its condition. They requested a methamphetamine task force clean-up truck, which arrived at the scene and “dismantled [the active lab] and took away all the hazardous materials.” Investigator Chunn confirmed that the Defendant’s residence was quarantined, meaning that it was considered unsuitable for habitation given that it had been contaminated with methamphetamine.</p>
<p id="b83-6">Tammy Atkins testified that she knew the Defendant through her church. She regularly traveled through the local neighborhoods “witnessing” and kept a journal of her experiences. On July 13, 2013, Ms. Atkins was on Beaver Creek Road but was not supposed to go on properties with “No Trespassing” signs. She observed that the Defendant’s property had several “No Trespassing” signs posted, despite the high grass. Ms. Atkins identified several of the Defendant’s “No Trespassing” and “Private Property’ signs in photographs that were admitted into evidence.</p>
<p id="b83-7">The Defendant testified that he now lived in his mother’s residence, which is on the same property and next door to the residence where he was living on August 3, 2013. The Defendant identified a photograph of a “No Trespassing” sign which he stated was at the beginning of the driveway onto the property, and this photograph was admitted into evidence. The Defendant stated that the property was posted with four or five such signs.</p>
<p id="b83-8">The Defendant testified that, when he looked outside and saw the officers at Mr. Gatlin’s father’s residence, he shut and locked his front door and “exited out the back door, walked around and stood on the front porch.” He explained that he locked his front door from the inside, so when he was standing on the front porch, he had no immediate access to get inside the front door.</p>
<p id="b83-10">The Defendant testified that the following occurred when the officers arrived on his property:</p>
<blockquote id="b83-11">Well, I saw them get out of the vehicle and come walking up to me. And I asked them, Could I help you? I don’t know if you’ve noticed this or not, but you passed “no trespassing” signs to get here. If you don’t have a search warrant, you need to leave my property. What you’re doing is unconstitutional.</blockquote>
<p id="b83-12">The officers asked for permission to enter his residence, which he denied and told them to leave the property. At that time, Investigator Green told the Defendant that he was going to detain the Defendant. The Defendant placed his arms out but asked that he not be handcuffed behind his back because of his left arm being dislocated and broken so many times. According to the Defendant, Investigator Chunn said, “oh we’re breaking your arm. We’re handcuffing you behind your back.” When the Defendant resisted, “[t]hey started punching [him] and kicking [him] and choking [him].” He denied that he “freaked out” during the struggle due to being under the influence of methamphetamine. Rather, he asserted that he was scared of the pain the officers were going to inflict by breaking his arm.</p>
<p id="b83-13">A video recording made by the “dash cam” of one of the reporting patrol cars was admitted into evidence and established that the Defendant’s driveway was not blocked by any gates or other physical obstructions.</p>
<p id="b83-14">At the conclusion of the proof at trial, the jury deliberated and convicted the De<page-number citation-index="1" label="68">*68</page-number>fendant of all charged offenses. The trial court subsequently sentenced the Defendant to an effective sentence of three years’ incarceration, followed by eight years suspended to supervised probation. On direct appeal, the Defendant argued that the trial court erred in denying his motion to suppress and that there was insufficient evidence to support his firearms convictions. The Court of Criminal Appeals affirmed the Defendant’s convictions and sentences. Christensen, <span class="citation no-link">2015 WL 2330185</span>, at *11. Judge John Everett Williams filed a separate opinion, concluding that, by posting “No Trespassing” signs, the Defendant had revoked any implied consent for the officers to enter his property without a warrant. Id. at *11 (Williams, J., concurring in part and dissenting in part). We subsequently granted the Defendant’s application for permission to appeal on the suppression issue. In our Order granting the application, we noted our particular interest in “(1) the effect, if any, of the ‘unlicensed physical intrusion’ definition of a search as articulated in Florida v. Jardines, — U.S. —, <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">133 S.Ct. 1409</a></span>, <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">185 L.Ed.2d 495</a></span> (2013); and (2) if the officers’ entry into the curtilage of [the Defendant’s] home constituted a search, whether it was supported by probable cause and the existence of exigent circumstances.”</p>
<p id="b84-6">Standard of Review</p>
<p id="b84-7">In evaluating whether the trial court’s ruling on a suppression motion was correct, we consider the proof adduced at both the suppression hearing and at trial. State v. Henning, <span class="citation" data-id="9524377"><a href="/opinion/1060855/state-v-henning/#299" aria-description="Citation for case: State v. Henning">975 S.W.2d 290, 299</a></span> (Tenn. 1998). Questions regarding the witnesses’ credibility, “the weight and value of the evidence, and resolution of conflicts in the evidence are matters entrusted to the trial judge as the trier of fact.” State v. Odom, <span class="citation" data-id="5091079"><a href="/opinion/5263918/state-v-odom/#23" aria-description="Citation for case: State v. Odom">928 S.W.2d 18, 23</a></span> (Tenn. 1996). Thus, we will uphold the trial court’s factual findings unless the preponderance of the evidence is otherwise. <span class="citation" data-id="5091079"><a href="/opinion/5263918/state-v-odom/" aria-description="Citation for case: State v. Odom">Id.</a></span> However, where the trial court has applied the law to the facts, we will conduct a de novo review. See State v. Walton, <span class="citation" data-id="9758143"><a href="/opinion/2355344/state-v-walton/#81" aria-description="Citation for case: State v. Walton">41 S.W.3d 75, 81</a></span> (Tenn. 2001). Because the State is the prevailing party, it is “entitled to the strongest legitimate view of the evidence adduced at the suppression hearing as well as all reasonable and legitimate inferences that may be drawn from that evidence.” Odom, <span class="citation" data-id="5091079"><a href="/opinion/5263918/state-v-odom/#23" aria-description="Citation for case: State v. Odom">928 S.W.2d at 23</a></span>.</p>
<p id="b84-9">Analysis</p>
<p id="b84-10">The Fourth Amendment to the United States Constitution provides that “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause ....” U.S. Const. amend. IV. “The purpose of the prohibition against unreasonable searches and seizures under the Fourth Amendment is to ‘safeguard the privacy and security of individuals against arbitrary invasions [by] government[al] officials.’ ” State v. Yeargan, <span class="citation" data-id="9524423"><a href="/opinion/1060948/state-v-yeargan/#629" aria-description="Citation for case: State v. Yeargan">958 S.W.2d 626, 629</a></span> (Tenn. 1997) (quoting Camara v. Municipal Court, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U.S. 523, 528</a></span>, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">87 S.Ct. 1727</a></span>, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">18 L.Ed.2d 930</a></span> (1967)).</p>
<p id="b84-11">Likewise, Article I, section 7 of the Tennessee Constitution provides that “the people shall be secure in their persons, houses, papers and possessions, from unreasonable searches and seizures” and that general warrants lacking particularity or evidentiary support “ought not to be granted.” Tenn. Const, art. I, § 7. This Court has stated that the Tennessee Constitution’s search and seizure provision is “identical in intent and purpose with the Fourth Amendment.” Sneed v. State, <span class="citation" data-id="1795662"><a href="/opinion/1795662/sneed-v-state/" aria-description="Citation for case: Sneed v. State">221 Tenn. 6</a></span>, <span class="citation" data-id="1795662"><a href="/opinion/1795662/sneed-v-state/#860" aria-description="Citation for case: Sneed v. State">423 S.W.2d 857, 860</a></span> (1968); see also, e.g., State v. Scarborough, <span class="citation" data-id="1057956"><a href="/opinion/1057956/state-v-scarborough/#622" aria-description="Citation for case: State v. Scarborough">201 S.W.3d 607, 622</a></span> (Tenn. 2006). Accordingly, <page-number citation-index="1" label="69">*69</page-number>“under both the federal and state constitutions, a warrantless search or seizure is presumed unreasonable, and evidence discovered as a result thereof is subject to suppression unless the State demonstrates that the search or seizure was conducted pursuant to one of the narrowly defined exceptions to the warrant requirement.” Yeargan, <span class="citation" data-id="9524423"><a href="/opinion/1060948/state-v-yeargan/#629" aria-description="Citation for case: State v. Yeargan">958 S.W.2d at 629</a></span>.</p>
<p id="b85-4">
<em><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">Jardines</a></span></em>
</p>
<p id="b85-5">The issue before us is whether Investigators Green and Chunn engaged in an unconstitutional intrusion onto the Defendant’s property when they drove down the Defendant’s unobstructed driveway near which were posted “No Trespassing” signs. This is an issue of first impression before this Court.</p>
<p id="b85-6">The text of both the Fourth Amendment and Article I, section 7 refers to “houses.” Therefore, when a police officer obtains information by physically intruding into someone’s house, “a ‘search’ within the original meaning of the Fourth Amendment has undoubtedly occurred.” Jardines, <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">133 S.Ct. at 1414</a></span> (quoting United States v. Jones, <span class="citation" data-id="7268856"><a href="/opinion/7350871/united-states-v-jones/" aria-description="Citation for case: United States v. Jones">565 U.S. 400</a></span>, 406 n.3, <span class="citation multiple-matches"><a href="/c/S.Ct./132/945/">132 S.Ct. 945</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/181/911/">181 L.Ed.2d 911</a></span> (2012)) (internal quotation marks omitted); see also Lester v. State, <span class="citation" data-id="9863021"><a href="/opinion/2419209/lester-v-state/" aria-description="Citation for case: Lester v. State">216 Tenn. 615</a></span>, <span class="citation" data-id="9863021"><a href="/opinion/2419209/lester-v-state/#289" aria-description="Citation for case: Lester v. State">393 S.W.2d 288, 289-90</a></span> (1965) (stating that a search within the meaning of the Tennessee Constitution occurs when the police examine “a man’s home ... with a view to the discovery of ... some evidence of guilt”). Additionally, the curtilage, or the area immediately surrounding and associated with a particular house, also is protected by our constitutions. See Jardines, <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/#1414" aria-description="Citation for case: Florida v. Jardines">133 S.Ct. at 1414-15</a></span>; State v. Talley, <span class="citation" data-id="1403583"><a href="/opinion/1403583/state-v-talley/#729" aria-description="Citation for case: State v. Talley">307 S.W.3d 723, 729</a></span> (Tenn. 2010) (stating that Article 1, section 7 of the Tennessee Constitution “protect[s] the curtilage, which is defined as any area adjacent to a residence in which an individual can reasonably expect privacy”); State v. Prier, <span class="citation" data-id="2391848"><a href="/opinion/2391848/state-v-prier/#671" aria-description="Citation for case: State v. Prier">725 S.W.2d 667, 671</a></span> (Tenn. 1987) (“To make explicit what is unmistakably implicit in our cases and the federal cases, the curtilage is entitled to the same constitutional protection against ground entry and seizure as the home.”).</p>
<p id="b85-10">There is no bright-line rule delineating the inclusion or exclusion of a given driveway within a house’s curtilage for Fourth Amendment purposes. See Vanessa Rownaghi, Comment, Driving Into Unreasonableness: The Driveway, The Curtilage, and Reasonable Expectations of Privacy, 11 Am. U. J. Gender Soc. Pol’y <em>&amp; </em>L. 1165, 1165-67 (2003). Because the inclusion of the Defendant’s driveway within the curtilage of the Defendant’s residence does not impact our resolution of the issues before us, we will assume, without deciding, that the driveway was part of the curtilage.<footnotemark>5</footnotemark></p>
<p id="b85-11">Although a home’s curtilage is constitutionally protected against unreasonable searches by the government, not every entry upon a curtilage is a search. Rather, as the Supreme Court in Jardines recently explained,</p>
<blockquote id="b85-12">“the knocker on the front door is treated as an invitation or license to attempt an entry, justifying ingress to the home by solicitors, hawkers and peddlers of all kinds.” Breard v. Alexandria, <span class="citation" data-id="9420616"><a href="/opinion/104917/breard-v-alexandria/#626" aria-description="Citation for case: Breard v. Alexandria">341 U.S. 622, 626</a></span>, <span class="citation" data-id="9420616"><a href="/opinion/104917/breard-v-alexandria/" aria-description="Citation for case: Breard v. Alexandria">71 S.Ct. 920</a></span>, <span class="citation" data-id="9420616"><a href="/opinion/104917/breard-v-alexandria/" aria-description="Citation for case: Breard v. Alexandria">95 L.Ed. 1233</a></span> (1951). This implicit license typically permits the visitor to approach the home by the front path, knock promptly, wait <page-number citation-index="1" label="70">*70</page-number>briefly to be received, and then (absent invitation to linger longer) leave.... Thus, a police officer not armed with a warrant may approach a home and knock, precisely because that is “no more than any private citizen might do.” Kentucky v. King, <span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/#469" aria-description="Citation for case: Kentucky v. King">563 U.S. 452, 469</a></span>, <span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">131 S.Ct. 1849</a></span>, <span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">179 L.Ed.2d 865</a></span> (2011).</blockquote>
<p id="AYX">Jardines, <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/#1415" aria-description="Citation for case: Florida v. Jardines">133 S.Ct. at 1415-16</a></span> (parallel citations omitted). As expressed by the United States Court of Appeals for the Ninth Circuit more than fifty years ago,</p>
<blockquote id="adz-dedup-0">Absent express orders from the person in possession against any possible trespass, there is no rule of private or public conduct which makes it illegal per se, or a condemned invasion of the person’s right of privacy, for anyone openly and peaceably, at high noon, to walk up the steps and knock on the front door of any man’s “castle” with the honest intent of asking questions of the occupant thereof—whether the questioner be a pollster, a salesman, or an officer of the law.</blockquote>
<p id="ADG">Davis v. United States, <span class="citation" data-id="263083"><a href="/opinion/263083/albert-douglas-davis-v-united-states/#303" aria-description="Citation for case: Albert Douglas Davis v. United States">327 F.2d 301, 303</a></span> (9th Cir. 1964)<footnotemark>6</footnotemark>; see also, e.g., Nieminski v. State, <span class="citation" data-id="4864684"><a href="/opinion/5050361/nieminski-v-state/#526" aria-description="Citation for case: Nieminski v. State">60 So.3d 521, 526</a></span> (Fla. Dist. Ct. App. 2011) (noting that “a citizen’s encounter, including a knock and talk, is not regarded as a search or seizure” but is, rather, “a purely consensual encounter, which officers may initiate without any objective level of suspicion”) (citations and internal quotation marks omitted).</p>
<p id="b86-4">Our Court of Criminal Appeals has recognized that a so-called “knock-and-talk” by police officers is not prohibited by either the federal or state constitutions. See, e.g., State v. Cothran, <span class="citation" data-id="1073268"><a href="/opinion/1073268/state-v-cothran/#522" aria-description="Citation for case: State v. Cothran">115 S.W.3d 513, 522</a></span> (Tenn. Crim. App. 2003) (holding that a police officer may approach the front door of a house in order to investigate a complaint or to conduct other official business because “[a] sidewalk or pathway leading from a public street to the front door of a residence represents an ‘implied invitation’ to the public to use a pathway” and recognizing that “[pjolice officers, who are conducting official police business, are considered members of the general public”) (citing State v. Harris, <span class="citation" data-id="9777503"><a href="/opinion/2459843/state-v-harris/#623" aria-description="Citation for case: State v. Harris">919 S.W.2d 619, 623</a></span> (Tenn. Crim. App. 1995)). In short,</p>
<blockquote id="b86-7">[w]hen law enforcement officers who are not armed with a warrant knock on a door, they do no more than any private citizen might do. And whether the person who knocks on the door and requests the opportunity to speak is a police officer or a private citizen, the occupant has no obligation to open the door or to speak.</blockquote>
<p id="b86-8">Kentucky v. King, <span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/#469" aria-description="Citation for case: Kentucky v. King">563 U.S. 452, 469-70</a></span>, <span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">131 S.Ct. 1849</a></span>, <span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">179 L.Ed.2d 865</a></span> (2011). Indeed, “even if an occupant chooses to open the door and speak with the officers, the occupant need not allow the officers to enter the premises and may refuse to answer any questions at any time.” <span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/#470" aria-description="Citation for case: Kentucky v. King">Id. at 470</a></span>, <span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">131 S.Ct. 1849</a></span>.</p>
<p id="b86-9">Thus, a so-called “knock-and-talk” is not a “search” as that term is understood within the context of the Fourth Amendment, at least if the intrusion is conducted within the scope of the implicit license recognized by the Supreme Court in Jardines. Rather, only if an officer’s conduct in approaching a front door “objectively reveals a purpose to conduct a search,” such as by bringing a drug-sniffing dog onto the front porch, will his approach offend the Fourth Amendment. Jardines, <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/#1417" aria-description="Citation for case: Florida v. Jardines">133 S.Ct. at 1417-18</a></span>; see also People v. Frederick, <span class="citation" data-id="9820554"><a href="/opinion/3161379/people-v-frederick-people-v-van-doorne/" aria-description="Citation for case: People v. Frederick; People v. Van Doorne">313 Mich.App. 457</a></span>, <page-number citation-index="1" label="71">*71</page-number><span class="citation" data-id="9820554"><a href="/opinion/3161379/people-v-frederick-people-v-van-doorne/#9" aria-description="Citation for case: People v. Frederick; People v. Van Doorne">886 N.W.2d 1, 9</a></span> (2015) (stating that, under Jardines, officers “do not violate the Fourth Amendment by approaching a home and seeking to speak with its occupant. .., However, if police enter a protected area not intending to speak with the occupant, but rather, solely to conduct a search, the line has been crossed”). Indeed, the United States Court of Appeals for the Tenth Circuit has noted that its sister courts in the Fourth and Eleventh Circuits have upheld knock-and-talk encounters after Jardines and that “[t]here does not appear to be any circuit that has concluded, after Jardines, that a knock- and-talk is invalid.” United States v. Carloss, <span class="citation" data-id="9822082"><a href="/opinion/3184928/united-states-v-carloss/" aria-description="Citation for case: United States v. Carloss">818 F.3d 988</a></span>, 994 n.4 (10th Cir. 2016) (citing Covey v. Assessor of Ohio Cnty., <span class="citation" data-id="2773276"><a href="/opinion/2773276/christopher-covey-v-assessor-of-ohio-county/#192" aria-description="Citation for case: Christopher Covey v. Assessor of Ohio County">777 F.3d 186, 192-93</a></span> (4th Cir. 2015); United States v. Walker, <span class="citation" data-id="2844024"><a href="/opinion/2844024/united-states-v-wayne-walker/#1363" aria-description="Citation for case: United States v. Wayne Walker">799 F.3d 1361, 1363</a></span> (11th Cir. 2015)); see also, e.g., Smith v. City of Wyoming, <span class="citation" data-id="3194675"><a href="/opinion/3194781/glenda-smith-v-city-of-wyoming/#713" aria-description="Citation for case: Glenda Smith v. City of Wyoming">821 F.3d 697, 713</a></span> (6th Cir. 2016) (holding that, post-Jardines, a knock-and-talk is generally permissible); Frederick, <span class="citation" data-id="9820554"><a href="/opinion/3161379/people-v-frederick-people-v-van-doorne/#7" aria-description="Citation for case: People v. Frederick; People v. Van Doorne">886 N.W.2d at 7-8</a></span> (stating that, “as Jardines makes clear, an ordinary knock-and-talk is well within the scope of the license that may be implied from the habits of the country” and that “even pos1&gt; Jardines, an officer may conduct a knock- and-talk with the intent to gain the occupant’s consent to a search or to otherwise acquire information from the occupant. That an officer intends to obtain information from the occupant does not transform a knock-and-talk into an unconstitutional search”) (internal quotation marks omitted).<footnotemark>7</footnotemark></p>
<p id="b87-5">Given the Supreme Court’s recognition that “the knocker on the front door is treated as an <em>invitation or license </em>to attempt an entry,” Jardines, <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/#1415" aria-description="Citation for case: Florida v. Jardines">133 S.Ct. at 1415</a></span> (emphasis added) (quotation marks omitted), it is axiomatic that a homeowner may take actions to <em>revoke </em>or otherwise limit that invitation or license. As elucidated by the United States District Court for the Middle District of Florida,</p>
<blockquote id="b87-8">[T]he license granted to enter property to knock on a person’s door is not unlimited. Rather, it extends unless and until the homeowner provides “express orders” to the contrary. In determining the scope of the implied license, and therefore whether a police officer’s approach to the front door was permissible under the Fourth Amendment, courts ask whether a reasonable person could do as the police did. Factors that may aid in the analysis include the appearance of the property, whether entry might cause a resident alarm, what ordinary visitors would be expected to do, and what a reasonably respectful citizen would be expected to do.</blockquote>
<p id="b87-9">United States v. Holmes, <span class="citation" data-id="7234664"><a href="/opinion/7316756/united-states-v-holmes/#1259" aria-description="Citation for case: United States v. Holmes">143 F.Supp.3d 1252, 1259</a></span> (M.D. Fla. 2015) (citations and footnote omitted); see also State v. Grice, <span class="citation" data-id="9805778"><a href="/opinion/2772730/state-v-grice/" aria-description="Citation for case: State v. Grice">367 N.C. 753</a></span>, <span class="citation" data-id="9805778"><a href="/opinion/2772730/state-v-grice/#319" aria-description="Citation for case: State v. Grice">767 S.E.2d 312, 319</a></span> (2015) (stating that “[t]he implicit license enjoyed by law enforcement and citizens alike to approach the front doors of homes may be limited or rescinded by clear demonstrations by the homeowners”). The “express orders” sufficient to revoke the implied license “must be by ‘clear demonstrations,’ ‘unambiguous,’ and ‘obvious to the casual visitor.’” Holmes, <span class="citation" data-id="7234664"><a href="/opinion/7316756/united-states-v-holmes/" aria-description="Citation for case: United States v. Holmes">143 F.Supp.3d at 1262</a></span> (citing Grice, <span class="citation" data-id="9805778"><a href="/opinion/2772730/state-v-grice/#319" aria-description="Citation for case: State v. Grice">767 S.E.2d at 319</a></span>; State v. Howard, <span class="citation" data-id="2646952"><a href="/opinion/2646952/state-v-howard-motion-to-suppress/" aria-description="Citation for case: State v. Howard -Motion to suppress">155 Idaho 666</a></span>, <span class="citation" data-id="2646952"><a href="/opinion/2646952/state-v-howard-motion-to-suppress/#860" aria-description="Citation for case: State v. Howard -Motion to suppress">315 P.3d 854, 860</a></span> (Idaho Ct. App. 2013); Christensen, <span class="citation no-link">2015 WL 2330185</span>, at *8).</p>
<p id="b88-3"><page-number citation-index="1" label="72">*72</page-number>The question before us in this case is whether posting “No Trespassing” signs near an unobstructed driveway is an express order sufficient to revoke or limit the invitation/license such that a police officer may not legitimately approach the residence via the driveway in order to conduct a warrantless knock-and-talk encounter. That is, did the Defendant’s signs turn the investigators’ entry onto his property into an intrusion subject to constitutional protections? It is the Defendant’s burden of establishing, by a preponderance of the evidence, that the investigators’ knock-and-talk was invalid. See Holmes, <span class="citation" data-id="7234664"><a href="/opinion/7316756/united-states-v-holmes/#1261" aria-description="Citation for case: United States v. Holmes">143 F.Supp.3d at 1261</a></span>.<footnotemark>8</footnotemark></p>
<p id="b88-4">The impact of “No Trespassing” signs on the validity of a knock-and-talk excursion onto a resident’s curtilage has been the subject of numerous decisions by both federal and state courts and, as with much search and seizure jurisprudence, the anal-yses and results have varied. A few states have concluded that “No Trespassing” signs establish a legitimate expectation of privacy that renders a knock-and-talk invalid. See, e.g., State v. Roubique, <span class="citation" data-id="1798985"><a href="/opinion/1798985/state-v-roubique/#862" aria-description="Citation for case: State v. Roubique">421 So.2d 859, 862</a></span> (La. 1982) (holding that “Private Road, No Trespassing” sign at driveway’s entrance was “ample evidence of [the defendant’s] intent to preserve his privacy” and that officer’s entry onto the defendant’s property violated the Fourth Amendment); State v. Bullock, <span class="citation" data-id="883585"><a href="/opinion/883585/state-v-bullock/" aria-description="Citation for case: State v. Bullock">272 Mont. 361</a></span>, <span class="citation" data-id="883585"><a href="/opinion/883585/state-v-bullock/#75" aria-description="Citation for case: State v. Bullock">901 P.2d 61, 75-76</a></span> (1995) (holding that, under the Montana Constitution, “No Trespassing” signs to either side of gate across driveway gave the defendant a reasonable expectation of privacy that officer violated by entering property without a warrant); People v. Scott, <span class="citation" data-id="5540124"><a href="/opinion/5690717/people-v-scott/" aria-description="Citation for case: People v. Scott">79 N.Y.2d 474</a></span>, <span class="citation no-link">583 N.Y.S.2d 920</span>, <span class="citation no-link">593 N.E.2d 1328</span>, 1338 (1992) (holding that, under the New York Constitution, officers’ warrantless entry onto land posted with “No Trespassing” signs was illegal); State v. Roper, <span class="citation" data-id="6954509"><a href="/opinion/7051112/state-v-roper/" aria-description="Citation for case: State v. Roper">254 Or.App. 197</a></span>, <span class="citation" data-id="6954509"><a href="/opinion/7051112/state-v-roper/#520" aria-description="Citation for case: State v. Roper">294 P.3d 517, 520</a></span> (2012) (upholding grant of motion to suppress under the Oregon Constitution because defendant’s “No Trespassing” signs manifested his intent to exclude the public from his fenced yard, notwithstanding open gate); see also Robinson v. Commonwealth, <span class="citation" data-id="1058715"><a href="/opinion/1058715/robinson-v-com/" aria-description="Citation for case: Robinson v. Com.">273 Va. 26</a></span>, <span class="citation" data-id="1058715"><a href="/opinion/1058715/robinson-v-com/#222" aria-description="Citation for case: Robinson v. Com.">639 S.E.2d 217, 222</a></span> (2007) (stating that “[i]mplied consent can be negated by obvious indicia of restricted access, such as posted ‘no trespassing’ signs, gates, or other means that deny access to uninvited persons”). Indeed, our Court of Criminal Appeals has indicated that “No Trespassing” signs may render a knock-and-talk invalid. See State v. Blackwell, No. E2009-00043-CCA-R3-CD, <span class="citation no-link">2010 WL 454864</span>, at *7 (Tenn. Crim. App. Feb. 10, 2010) (“Clearly, the presence of the ‘No Trespassing’ sign evinced an actual subjective expectation of privacy and a revocation of the ‘implied invitation’ of the front door.”); see also State v. Draper, No. E2011-01047-CCA-R3-CD, <span class="citation no-link">2012 WL 1895869</span>, at *6 (Tenn. Crim. App. May 24, 2012) (stating, “the presence of a ‘no trespassing’ sign ’evince[s] an actual subjective expectation of privacy and a revocation of the implied invitation of the front door”) (quoting Blackwell, <span class="citation no-link">2010 WL 454864</span>, at *7); State v. Henry, No. W2005-02890-CCA-R3-CD, <span class="citation no-link">2007 WL 1094146</span>, at *5 (Tenn. Crim. App. Apr. 11, 2007) (noting in dictum that the only way in which the knock-and-talk would have been “unacceptable would have been the presence of the ‘No Trespassing’ signs”).</p>
<p id="b89-3"><page-number citation-index="1" label="73">*73</page-number>Most jurisdictions that have considered the issue, however, appear to hold that “No Trespassing” signs, in and of themselves, will not invalidate a knock-and-talk. See, e.g., United States v. Bearden, <span class="citation" data-id="2786693"><a href="/opinion/2786693/united-states-v-anthony-bearden/#892" aria-description="Citation for case: United States v. Anthony Bearden">780 F.3d 887, 892-94</a></span> (8th Cir. 2015) (upholding knock-and-talk where officers entered property through open driveway gate despite “No Trespassing” signs); United States v. Hopper, <span class="citation" data-id="7216174"><a href="/opinion/7298359/united-states-v-hopper/#623" aria-description="Citation for case: United States v. Hopper">58 Fed.Appx. 619, 623</a></span> (6th Cir. 2003) (holding that knock-and-talk was allowed despite several “No Trespassing” signs near driveway); Holmes, <span class="citation" data-id="7234664"><a href="/opinion/7316756/united-states-v-holmes/#1265" aria-description="Citation for case: United States v. Holmes">143 F.Supp.3d at 1265</a></span> (holding that, “in the absence of another barrier (such as a fence and gate), ‘No Trespassing’ signs do not, in and of themselves, withdraw the implied consent to conduct a knock and talk”); Davis v. City of Milwaukee, No. 13-CV-982-JPS, <span class="citation no-link">2015 WL 5010459</span>, at *13 (E.D. Wis. Aug. 21, 2015) (stating that “signs stating ‘Private Property<footnotemark>5</footnotemark> or ‘No Trespassing’ do not, by themselves, create an impenetrable privacy zone”); United States v. Jones, No. 4:13CR00011-003, <span class="citation no-link">2013 WL 4678229</span>, at *2 n.2, *6, *9 (W.D. Va. Aug. 30, 2013) (holding that multiple signs along driveway and on property stating “No Trespassing,” “Posted: Private Property,” and “Keep Out” did not invalidate knock-and-talk under the Fourth Amendment); United States v. Denim, No. 2:13-CR-63, <span class="citation no-link">2013 WL 4591469</span>, at *4 (E.D. Tenn. Aug. 28, 2013), (stating, post-Jar-dines, that, “[e]ven in the face of ,No Trespassing signs, it is not unreasonable for a police officer to intrude upon private property to ask if the resident has any information that will aid in the investigation of a crime”); United States v. Schultz, No. 13-20023, <span class="citation no-link">2013 WL 2352742</span>, at *5 (E.D. Mich. May 29, 2013) (holding that knock-and-talk entry via driveway was valid under the Fourth Amendment despite “No Trespassing” signs); Michel v. State, <span class="citation" data-id="1161072"><a href="/opinion/1161072/michel-v-state/#437" aria-description="Citation for case: Michel v. State">961 P.2d 436, 437-38</a></span> (Alaska Ct. App. 1998) (holding that four “No Trespassing” signs along three-hundred-yard driveway did not invalidate knock-and-talk); Burdyshaw v. State, <span class="citation" data-id="6553103"><a href="/opinion/6674339/burdyshaw-v-state/" aria-description="Citation for case: Burdyshaw v. State">69 Ark. App. 243</a></span>, <span class="citation" data-id="6553103"><a href="/opinion/6674339/burdyshaw-v-state/#921" aria-description="Citation for case: Burdyshaw v. State">10 S.W.3d 918, 921</a></span> (2000) (holding that officers’ entry onto property via driveway did not violate the Fourth Amendment in spite of “No Trespassing” signs posted on property); State v. Rigoulot, <span class="citation" data-id="1367569"><a href="/opinion/1367569/state-v-rigoulot/" aria-description="Citation for case: State v. Rigoulot">123 Idaho 267</a></span>, <span class="citation" data-id="1367569"><a href="/opinion/1367569/state-v-rigoulot/#923" aria-description="Citation for case: State v. Rigoulot">846 P.2d 918, 923</a></span> (Idaho Ct. App. 1992) (stating that “No Trespassing” signs cannot “reasonably be interpreted to exclude normal, legitimate inquiries” and holding that officers did not violate the Fourth Amendment despite the presence of “No Trespassing” signs); Jones v. State, <span class="citation" data-id="1990248"><a href="/opinion/1990248/jones-v-state/" aria-description="Citation for case: Jones v. State">178 Md.App. 454</a></span>, <span class="citation" data-id="1990248"><a href="/opinion/1990248/jones-v-state/#12" aria-description="Citation for case: Jones v. State">943 A.2d 1, 12</a></span> (Md. Ct. Spec. App. 2008) (holding that “No Trespassing” sign did not preclude knock-and-talk by police and noting that “courts have been very consistent in concluding that no trespassing signs, in and of themselves, do not make a police officer’s entry on property unlawful”); City of Beatrice v. Meints, <span class="citation no-link">289 Neb. 558</span>, <span class="citation no-link">856 N.W.2d 410</span>, 421 (2014) (holding that a resident “could not reasonably expect that tacking a ‘no trespassing' sign to a tree would prevent others from viewing or walking on his land”), cert. denied — U.S. —, <span class="citation multiple-matches"><a href="/c/S.Ct./135/2388/">135 S.Ct. 2388</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/192/166/">192 L.Ed.2d 166</a></span> (2015); State v. Smith, — N.C.App. —, <span class="citation" data-id="3181367"><a href="/opinion/3181385/state-v-smith/#509" aria-description="Citation for case: State v. Smith">783 S.E.2d 504, 509-10</a></span> (2016) (holding that “No Trespassing” sign did not revoke the implied license to approach the defendant’s home, therefore knock-and-talk did not violate the Fourth Amendment); State v. Mittleider, <span class="citation" data-id="899106"><a href="/opinion/899106/state-v-mittleider/#307" aria-description="Citation for case: State v. Mittleider">809 N.W.2d 303, 307-08</a></span> (N.D. 2011) (holding that “No Trespassing” signs posted around the defendant’s farmstead “did not create a reasonable expectation of privacy in the entrance of the farmstead”); State v, Morgan, No. 13-CA-30, <span class="citation no-link">2014 WL 1836015</span>, at *6 (Ohio Ct. App. May 1, 2014) (stating that “[t]he presence of ‘no trespassing' signs does not make law enforcement’s encroachment onto the curtilage presumptively unreasonable when officers <page-number citation-index="1" label="74">*74</page-number>are otherwise lawfully present”). As stated by the Idaho Court of Appeals,</p>
<blockquote id="b90-4">[while] posting “No Trespassing” signs may indicate a desire to restrict unwanted visitors and announce one’s expectations of privacy[,] ... such signs cannot reasonably be interpreted to exclude normal, legitimate inquiries or visits by mail carriers, newspaper deliverers, census takers, neighbors, friends, utility workers and others who restrict their movements to the areas of one’s property normally used to approach the home.</blockquote>
<p id="AH6">Rigoulot, <span class="citation" data-id="1367569"><a href="/opinion/1367569/state-v-rigoulot/#923" aria-description="Citation for case: State v. Rigoulot">846 P.2d at 923</a></span>. Indeed, the dissent recognizes that, even for those jurisdictions that may find “No Trespassing” signs to be sufficient in and of themselves to revoke the implied license to approach the front door, such signs “must be appropriately worded and placed.” In our view, this analytical approach is inadequate to provide our police officers with sufficient guidance in their efforts to act within constitutional parameters.</p>
<p id="b90-5">Recently, the United States Court of Appeals for the Tenth Circuit considered a case in which two police officers knocked on the defendant’s front door in spite of several “No Trespassing” signs posted around the house and on the house’s front door. United States v. Carloss, <span class="citation" data-id="9822082"><a href="/opinion/3184928/united-states-v-carloss/#990" aria-description="Citation for case: United States v. Carloss">818 F.3d 988, 990</a></span> (10th Cir. 2016), cert. denied, — U.S. —, <span class="citation multiple-matches"><a href="/c/S.Ct./137/231/">137 S.Ct. 231</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/196/178/">196 L.Ed.2d 178</a></span> (2016). The case generated a lead opinion, a concurring opinion, and a dissent. The lead opinion stated that “just the presence of a ‘No Trespassing<footnotemark>1</footnotemark> sign is not alone sufficient to convey to an objective officer, or member of the public, that he cannot go to the front door and knock,” id. at 995, and held that the sign on the front door, which stated “Posted Private Property Hunting, Fishing, Trapping or Trespassing for Any Purpose is Strictly Forbidden Violators Will Be Prosecuted,” was “ambiguous and did not clearly revoke the implied license extended to members of the public, including police officers, to enter the home’s curtilage and knock on the front door, seeking to speak consensually with the occupants,” id. at 996. “Therefore, the officers did not violate the Fourth Amendment when they went onto the porch and knocked on the front door of the house in which [the defendant] lived.” Id. at 997.</p>
<p id="b90-9">The separate concurring opinion advocated that the court “deploy an objective test, asking whether a reasonable person would conclude that entry onto the curtilage-the front porch here-by police or others was <em>categorically </em>barred.” Id. at 999 (Tymkovich, C.J., concurring). The Chief Judge elaborated:</p>
<blockquote id="b90-10">The signs in this case of course communicated variants of the phrase “No Trespassing.” But in light of the strong social presumption that a visitor to a residential neighborhood can enter the front porch curtilage to knock, I doubt a reasonable, lawful visitor would believe that “No Trespassing” eliminated that presumption in every instance. Every reasonable person knows-even without seeing a “No Trespassing” sign-that one cannot trespass on private property. But that knowledge coexists with knowledge of the equally well-established principle that one may generally enter the curti-lage to knock. A reasonable observer could also understand a “No Trespassing” sign as restating the “no-trespassing” principle without thinking it had any bearing on the implicit license to enter the curtilage for social reasons. In a residential context, the intention of the homeowner who posts signs, without more, seems inadequate to revoke the license. See, e.g., State v. Hiebert, <span class="citation" data-id="3149298"><a href="/opinion/3149298/state-v-dennis-earl-hiebert/" aria-description="Citation for case: State v. Dennis Earl Hiebert">156 Idaho 637</a></span>, <span class="citation" data-id="3149298"><a href="/opinion/3149298/state-v-dennis-earl-hiebert/#1090" aria-description="Citation for case: State v. Dennis Earl Hiebert">329 P.3d 1085, 1090</a></span> (App. 2014) (noting that “where a ‘no trespassing’ sign is ambiguous and not clearly posted, the implied invitation to enter the curtilage of a home via the normal <page-number citation-index="1" label="75">*75</page-number>access routes is not revoked”). I emphasize that it is not my view that a “No Trespassing” sign will <em>never </em>indicate the revocation of the implied license. Rather, the circumstances of this case do not indicate a revocation occurred such that the police could not reasonably believe entry was permissible.</blockquote>
<blockquote id="adq-dedup-0">[[Image here]]</blockquote>
<blockquote id="b91-4">Of course, the right facts could remove that ambiguity. For example, a “No Trespassing” sign posted on a fence encircling a property imparts a different message than the same sign standing alone. And a closed or locked gate, especially in the residential context, imparts more information to the reasonable observer. See, e.g., State v. Christensen, <span class="citation" data-id="9609876"><a href="/opinion/1378909/state-v-christensen/" aria-description="Citation for case: State v. Christensen">131 Idaho 143</a></span>, <span class="citation" data-id="9609876"><a href="/opinion/1378909/state-v-christensen/#587" aria-description="Citation for case: State v. Christensen">953 P.2d 583, 587-88</a></span> (1998) (holding that “No Trespassing” sign “clearly posted on a gate across the only public access to the property” revoked the implicit license because “the message to the public was [not] ambiguous”). But nothing aside from their nu-merosity makes the “No Trespassing” signs in this case particularly distinctive. And numerosity alone does not eliminate the ambiguity I noted above. No special facts-like a fence or other physical obstacle-clarified to the reasonable visitor that these signs revoked the license.</blockquote>
<p id="b91-5">Id. at 999-1000 (Tymkovich, C.J., concurring) (footnote omitted). The concurring opinion stressed the frequent axiom of Fourth Amendment jurisprudence: “The result turns on the totality of the circumstances.” Id. at 1001 (Tymkovich, C.J., concurring). We agree with Chief Judge Tym-kovich’s approach:<footnotemark>9</footnotemark> under the totality of the circumstances, would an objectively reasonable person conclude that entry onto the Defendant’s driveway was categorically barred?</p>
<p id="b91-9">The United States Supreme Court stated long ago that “[t]he law of trespass recognizes the interest in possession and control of one’s property and for that reason permits exclusion of unwanted intruders. <em>But it does not follow that the right to exclude conferred by trespass law embodies a privacy interest also protected by the Fourth Amendment.” </em>Oliver v. United States, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U.S. 170</a></span>, 183 n.15, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">104 S.Ct. 1735</a></span>, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">80 L.Ed.2d 214</a></span> (1984) (emphasis added). “Thus, trespass laws are designed to keep out unwanted intruders, such as vandals, thieves, and squatters, but those laws do not implicate the privacy interests in ‘persons, houses, papers, and effects’ protected by the Fourth Amendment.” Holmes, <span class="citation" data-id="7234664"><a href="/opinion/7316756/united-states-v-holmes/" aria-description="Citation for case: United States v. Holmes">143 F.Supp.3d at 1264</a></span> (citing Oliver, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#176" aria-description="Citation for case: Oliver v. United States">466 U.S. at 176</a></span>, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">104 S.Ct. 1735</a></span>). Therefore,</p>
<blockquote id="b91-10">[t]o find that a “No Trespassing” sign on its own expressly revokes the implied consent to walk up to a front door and knock, [we] would have to find that the sign means something like, “Do not do those things that would normally be considered trespassing, and also, I now consider anyone walking up to my front door to be a trespasser as well.”</blockquote>
<p id="b91-11">Id. at 1264-65.</p>
<p id="b91-12">We agree with the overwhelming majority of jurisdictions that have ad<page-number citation-index="1" label="76">*76</page-number>dressed the issue that signs admonishing “No Trespassing,” in and of themselves, are rarely going to be sufficient to revoke the implied license allowing persons to approach a front door and knock. The term “No Trespassing” is not so clear and unambiguous as the Defendant and the dissent claim. See Carloss, <span class="citation" data-id="9822082"><a href="/opinion/3184928/united-states-v-carloss/#995" aria-description="Citation for case: United States v. Carloss">818 F.3d at 995</a></span> (stating that no trespassing signs “by themselves, do not have the talismanic quality [the defendant] attributes to them”). Black’s Law Dictionary defines the term “trespass” as “[a]n <em>unlawful, </em>act committed against the person or property of another; especially, <em>wrongful </em>entry on another’s real property.” Black’s Law Dictionary 1503 (10th ed. 2014) (emphases added). This definition implies clearly that some entries onto another’s real property are neither unlawful nor wrongful and, therefore, are not trespasses. Indeed, this Court recognized over one hundred and fifty years ago that, “[i]n law every entry upon the soil of another, <em>in the absence of a lawful authority, without the owner’s license, </em>is a trespass.” Norvell v. Gray’s Lessee, <span class="citation" data-id="7663099"><a href="/opinion/7727413/norvell-v-grays-lessee/#103" aria-description="Citation for case: Norvell v. Gray&#x27;s lessee">31 Tenn. 96, 103</a></span> (1851) (emphasis added); see also, e.g., City of Townsend v. Damico, No. E2013-01778-COA-R3-CV, <span class="citation no-link">2014 WL 2194453</span>, at *3 (Tenn. Ct. App. 2014) (recognizing that “[t]he courts of this state have ... defined the tort of trespass as an unauthorized entry upon the land of another”) (citing Norvell, <span class="citation" data-id="7663099"><a href="/opinion/7727413/norvell-v-grays-lessee/#103" aria-description="Citation for case: Norvell v. Gray&#x27;s lessee">31 Tenn. at 103</a></span>); Holmes, <span class="citation" data-id="7234664"><a href="/opinion/7316756/united-states-v-holmes/#1265" aria-description="Citation for case: United States v. Holmes">143 F.Supp.3d at 1265</a></span> (stating that “the plain meaning of ‘No Trespassing’ is that it prohibits what people ordinarily think of as trespassing, and does not alter the character of an entry that one would not otherwise think to be a trespass, such as the implied license to approach the homeowner’s door to knock and talk”) (citing Oliver, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U.S. at 183</a></span> n.15, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">104 S.Ct. 1735</a></span>).</p>
<p id="b92-5">In short, a homeowner who posts a “No Trespassing” sign is simply making explicit what the law already recognizes: that persons entering onto another person’s land must have a legitimate reason for doing so or risk being held civilly, or perhaps even criminally, liable for trespass. Consequently, as set forth above, a knock-and-talk conducted within constitutional parameters is a legitimate reason for police officers to enter the curti-lage of a house via a driveway that is obstructed by nothing more than several “No Trespassing” signs. For this reason, we disagree with the dissent that “a ‘No Trespassing<footnotemark>1</footnotemark> sign should be of particular significance to law enforcement officers in communicating that they may need to obtain a warrant before entering the property.”<footnotemark>10</footnotemark> Officers engaging in legitimate police business will conclude, correctly, that they are not engaging in a “trespass” when they approach a front door to conduct a knock- and-talk. We also emphasize that the occupant of a residence is under no obligation to open a door when knocked upon by a police officer who holds no warrant.</p>
<p id="b92-6">The Defendant asserts that his signs were accompanied by other barriers to entry, including overgrown vegetation, the lack of a pathway to his house, and debris blocking any possible route from the driveway to the front porch, and that the totality of these circumstances made clear that no one was to enter his property absent an express invitation. We are not persuaded. First, the impact of signs at the beginning of a long driveway is not altered by the eventual accessibility of the front porch sixty or seventy yards later. Second, while a fence and a closed gate that physically block access to the front <page-number citation-index="1" label="77">*77</page-number>door of a house, in some instances, may be sufficient to revoke the implied license to enter the curtilage of a residence,<footnotemark>11</footnotemark> mere ambiguous signage and unkemptness are not.</p>
<p id="b93-5">We agree with the lead opinion below that the Defendant’s signs “would not have prevented the casual visitor or the reasonably respectful citizen from approaching [the Defendant’s] residence.” Christensen, <span class="citation no-link">2015 WL 2330185</span>, at *8. Accordingly, we hold that, under the totality of the circumstances, the Defendant’s “No Trespassing” signs posted near his unobstructed driveway were not sufficient to revoke the implied license referred to in Jardines. The Defendant is not entitled to relief on this basis.</p>
<p id="b93-6">
<em>Reasonable Expectation of Privacy</em>
</p>
<p id="AIs">Jardines dealt with, two officers who entered the defendant’s curtilage with a drug-sniffing dog which proceeded to sniff and, therefore, to search. <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/#1416" aria-description="Citation for case: Florida v. Jardines">133 S.Ct. at 1416</a></span>. Because the search was not supported by a warrant or any of the recognized exceptions to the warrant requirement, the Supreme Court held that the search was unconstitutional. See <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/#1417" aria-description="Citation for case: Florida v. Jardines">id. at 1417</a></span>. The Supreme Court based its decision on “the traditional property-based understanding of the Fourth Amendment,” rather than on the “reasonable expectation of privacy” test set forth in Katz v. United States, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U.S. 347</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L.Ed.2d 576</a></span> (1967). <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Id.</a></span> See Holmes, <span class="citation" data-id="7234664"><a href="/opinion/7316756/united-states-v-holmes/#1257" aria-description="Citation for case: United States v. Holmes">143 F.Supp.3d at 1257</a></span> (noting that the determination of whether an intrusion was a search under the Fourth Amendment “ ‘originally was tied to common-law trespass and involved some trespassory intrusion on property<footnotemark>5</footnotemark> ” but that the United States Supreme Court subsequently ‘“added a separate test—the reasonable-expectation-of-privacy test—to analyze whether a search occurred for purposes of the Fourth Amendment’ ”) (quoting United States v. Davis, <span class="citation" data-id="9807149"><a href="/opinion/2798570/united-states-v-quartavious-davis/#506" aria-description="Citation for case: United States v. Quartavious Davis">785 F.3d 498, 506, 507</a></span> (11th Cir. 2015)).</p>
<p id="b93-10">Unlike the Supreme Court in Jardines, we have concluded that the facts of this case do not indicate that a search in violation of the Fourth Amendment. occurred under the property-based analysis used in Jardines when Investigators Green and Chunn drove up to the Defendant’s residence. Because the Supreme Court in Jar-dines indicated that “[t]he Katz reasonable-expectations test ‘has been <em>added to, </em>not <em>substituted for,’ </em>the traditional property-based understanding of the Fourth Amendment,” <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">133 S.Ct. at 1417</a></span> (quoting Jones, <span class="citation" data-id="7268856"><a href="/opinion/7350871/united-states-v-jones/#409" aria-description="Citation for case: United States v. Jones">565 U.S. at 409</a></span>, <span class="citation" data-id="7268856"><a href="/opinion/7350871/united-states-v-jones/" aria-description="Citation for case: United States v. Jones">132 S.Ct. 945</a></span>), we now apply the reasonable-expectations test to the facts of this case. That is also the test we utilize under the Tennessee Constitution. See Talley, <span class="citation" data-id="1403583"><a href="/opinion/1403583/state-v-talley/#730" aria-description="Citation for case: State v. Talley">307 S.W.3d at 730</a></span>.</p>
<p id="b93-11">Under the reasonable-expectations test, a warrantless intrusion by government agents onto a homeowner’s real <page-number citation-index="1" label="78">*78</page-number>property does not violate either the federal or state constitution unless the intrusion violates the homeowner’s “reasonable expectation of privacy.” See Katz, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U.S. at 361</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span> (Harlan, J., concurring); Talley, <span class="citation" data-id="1403583"><a href="/opinion/1403583/state-v-talley/#730" aria-description="Citation for case: State v. Talley">307 S.W.3d at 730</a></span>. Initially, it is the homeowner’s burden to establish that he had a “reasonable expectation of privacy” against the intrusion. Talley, <span class="citation" data-id="1403583"><a href="/opinion/1403583/state-v-talley/#730" aria-description="Citation for case: State v. Talley">307 S.W.3d at 730</a></span>. The homeowner must satisfy two prongs: (1) that he had “an actual, subjective expectation of privacy,” and (2) that “society is willing to view [his] subjective expectation of privacy as reasonable and justifiable under the circumstances.” <span class="citation" data-id="1403583"><a href="/opinion/1403583/state-v-talley/" aria-description="Citation for case: State v. Talley">Id.</a></span> (quoting State v. Munn, <span class="citation" data-id="1426382"><a href="/opinion/1426382/state-v-munn/#494" aria-description="Citation for case: State v. Munn">56 S.W.3d 486, 494</a></span> (Tenn. 2001)). We examine the totality of the circumstances in determining the reasonableness of a claimed expectation of privacy. Id. at 734.</p>
<p id="b94-4">As he contended in his argument regarding the Jardines property-based test, the Defendant argues that his “No Trespassing” signs established that he had a reasonable expectation of privacy that precluded any entry onto his curtilage by Investigators Green and Chunn. We disagree. For the same reasons supporting our holding under the Jardines test, we hold that the Defendant has failed to satisfy the second prong of the reasonable expectations test. See Jardines, <span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/#1419" aria-description="Citation for case: Florida v. Jardines">133 S.Ct. at 1419</a></span> (noting that, “[i]t is not surprising that in a case involving a search of a home, property concepts and privacy concepts should so align. The law of property ‘naturally enough influence[s]’ our ‘shared social expectations’ of what places should be free from governmental incursions” (Kagan, J., concurring) (quoting Georgia v. Randolph, <span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/#111" aria-description="Citation for case: Georgia v. Randolph">547 U.S. 103, 111</a></span>, <span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span>, <span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">164 L.Ed.2d 208</a></span> (2006))). Even if the Defendant had an actual, subjective expectation that his signs would keep all persons from entering his property under all circumstances, a reasonable member of society would not view that expectation as reasonable and justifiable. Rather, a reasonable member of society would view the Defendant’s “No Trespassing” signs as simply forbidding any unauthorized or illegitimate entry onto his property.</p>
<p id="b94-7">In short, the Defendant has failed to demonstrate that he had a <em>reasonable </em>expectation that ordinary citizens would not occasionally enter his property by walking or driving up his driveway and approaching his front door to talk with him “for all of the many reasons that people knock on front doors.” Nieminski v. State, <span class="citation" data-id="4864684"><a href="/opinion/5050361/nieminski-v-state/#528" aria-description="Citation for case: Nieminski v. State">60 So.3d 521, 528</a></span> (Fla. Dist. Ct. App. 2011). Therefore, Investigators Green and Chunn did not violate the Defendant’s federal or state constitutional rights against unreasonable searches when they drove up his driveway and approached his front door. The Defendant is not entitled to relief on this basis.</p>
<p id="b94-8">Because we have determined that the officers’ initial entry onto the Defendant’s property did not violate either the federal or Tennessee constitutions, we need not determine whether the entry was supported by probable cause and the existence of exigent circumstances.<footnotemark>12</footnotemark></p>
<p id="b94-9">Conclusion</p>
<p id="b94-10">We hold that Investigators Green and Chunn did not violate either the federal or Tennessee constitutional prohibitions <page-number citation-index="1" label="79">*79</page-number>against unreasonable searches when they drove down the Defendant’s unobstructed driveway past “No Trespassing” signs and approached his residence in order to conduct a knoek-and-talk consensual encounter. The Defendant was not entitled to the suppression of evidence on this basis. Accordingly, we affirm the judgment of the Court of Criminal Appeals.</p>
<footnote label="1">
<p id="b80-7">. Judge John Everett Williams filed a separate opinion, concurring in part and dissenting in part. See Christensen, <span class="citation no-link">2015 WL 2330185</span>, at *11 (Williams, J., concurring in part and dissenting in part).</p>
</footnote>
<footnote label="2">
<p id="b80-8">. Because the Court of Criminal Appeals also evaluated the sufficiency of the evidence underlying the Defendant's firearms convictions, that court's opinion contains a more detailed summary of the proof adduced at trial. See Christensen, <span class="citation no-link">2015 WL 2330185</span>, at *1-4.</p>
</footnote>
<footnote label="3">
<p id="b80-15">. Mr. Harkness, the owner of the residence and Mr, Gatlin’s father, was deceased by the time of the suppression hearing.</p>
</footnote>
<footnote label="4">
<p id="b82-8">. As the Court of Criminal Appeals noted, "1-800-THE-FIRM is the number for the Cochran Firm, established by the late Johnnie Cochran.” Christensen, <span class="citation no-link">2015 WL 2330185</span>, at *1.</p>
</footnote>
<footnote label="5">
<p id="b85-7">. Property outside of a residence's curtilage is considered "open fields,” and a resident is not entitled to Fourth Amendment protections as to evidence collected from open fields. See Oliver v. United States, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#181" aria-description="Citation for case: Oliver v. United States">466 U.S. 170, 181</a></span>, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">104 S.Ct. 1735</a></span>, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">80 L.Ed.2d 214</a></span> (1984) (holding that "an individual has no legitimate expectation that open fields will remain free from warrantless intrusion by government officers”),</p>
</footnote>
<footnote label="6">
<p id="b86-5">. Prior to Jardines, the United States Court of Appeals for the Ninth Circuit recognized that the “honest intent” language of Davis was somewhat problematic in light of the United States Supreme Court's "rejection of good faith, subjective intent tests to gauge Fourth Amendment violations.” United States v. Perea-Rey, <span class="citation" data-id="801335"><a href="/opinion/801335/united-states-v-perea-rey/#1187" aria-description="Citation for case: United States v. Perea-Rey">680 F.3d 1179, 1187</a></span> (9th Cir. 2012).</p>
</footnote>
<footnote label="7">
<p id="b87-6">. The dissent asserts that "[o]ur homes and adjoining land are protected spaces; governmental officers must have a warrant, absent special circumstances, to intrude onto this private area.” As the foregoing discussion makes clear, however, officers need neither a warrant nor any special circumstances to approach a home's front door in order to conduct a knock-and-talk.</p>
</footnote>
<footnote label="8">
<p id="b88-5">. While it is the State's burden to establish an exception to the warrant requirement when it engages in a warrantless <em>search, </em>see State v. Meeks, <span class="citation" data-id="1057727"><a href="/opinion/1057727/state-v-meeks/#722" aria-description="Citation for case: State v. Meeks">262 S.W.3d 710, 722</a></span> (Tenn. 2008); Vale v. Louisiana, <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#34" aria-description="Citation for case: Vale v. Louisiana">399 U.S. 30, 34</a></span>, <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/" aria-description="Citation for case: Vale v. Louisiana">90 S.Ct. 1969</a></span>, <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/" aria-description="Citation for case: Vale v. Louisiana">26 L.Ed.2d 409</a></span> (1970), a knock-and-talk is simply a consensual encounter, not a search. Accordingly, it falls on the defendant to demonstrate, initially, that a knock-and-talk was, instead, a warrantless search.</p>
</footnote>
<footnote label="9">
<p id="b91-6">. We emphasize that this approach recognizes the possibility that a sign, under the right circumstances, <em>could </em>be sufficient to revoke the implied license. Accordingly, we also emphasize that we are not adopting a per se rule in this case. Nor, as the dissent contends, are we adopting a rule that differentiates between persons based upon their economic resources. This case presents the issue of whether "No Trespassing” signs posted near a private driveway are sufficient, <em>in and of themselves, </em>to create a constitutional barrier to police officers attempting to conduct legitimate police business via the resource of a consensual encounter with the occupant of the private residence. Nothing about this narrow issue reasonably implies that only wealthy homeowners can insulate themselves from law enforcement incursions onto their curtilage.</p>
</footnote>
<footnote label="10">
<p id="b92-4">. The dissent's approach of allowing a simple "No Trespassing” sign to prohibit a legitimate knock-and-talk by law enforcement also would create even more problematic consequences in more densely populated areas of our state.</p>
</footnote>
<footnote label="11">
<p id="b93-7">. See, e.g., State v. Koenig, — Vt. —, <span class="citation" data-id="3209074"><a href="/opinion/3209180/state-v-amy-koenig/#984" aria-description="Citation for case: State v. Amy Koenig">148 A.3d 977, 984</a></span> (2016) (stating that "[flences, gates <em>and </em>no-trespassing signs generally suffice to apprise a person that the area is private”) (emphasis added); Burkholder v. Superior Court, <span class="citation" data-id="2110625"><a href="/opinion/2110625/burkholder-v-superior-court/#428" aria-description="Citation for case: Burkholder v. Superior Court">96 Cal.App.3d 421, 428</a></span>, <span class="citation" data-id="2110625"><a href="/opinion/2110625/burkholder-v-superior-court/" aria-description="Citation for case: Burkholder v. Superior Court">158 Cal.Rptr. 86</a></span> (Cal. Ct. App. 1979) (holding that agents’ entry onto defendant’s property violated the Fourth Amendment because "[e]ntry to the property was openly restricted by posted signs along, and locked gates across, the rural access road signifying an intention to deny access to the public in general, including government agents”); Brown v. State, <span class="citation" data-id="2736404"><a href="/opinion/2736404/brown-v-state/#624" aria-description="Citation for case: Brown v. State">152 So.3d 619, 624</a></span> (Fla. Dist. Ct. App. 2014) (holding that agents' knock-and-talk excursion onto the defendant’s curtilage offended the Fourth Amendment because the defendant's curtilage was surrounded by two gated fences posted with no trespassing signs); State v. Johnson, <span class="citation" data-id="1159003"><a href="/opinion/1159003/state-v-johnson/" aria-description="Citation for case: State v. Johnson">75 Wash.App. 692</a></span>, <span class="citation" data-id="1159003"><a href="/opinion/1159003/state-v-johnson/#992" aria-description="Citation for case: State v. Johnson">879 P.2d 984, 992</a></span> (1994) (agents violated Washington Constitution by entering property that defendant had fenced, gated, and posted with no trespassing and private property signs).</p>
</footnote>
<footnote label="12">
<p id="b94-5">. The issue of Investigator Chunn’s forcible entry into the Defendant’s home is not before us. Indeed, during oral arguments before this Court, defense counsel acknowledged that Investigator Chunn's entry into the residence after smelling the odor associated with the active manufacture of methamphetamine was supported by exigent circumstances and probable cause. See United States v. Brown, <span class="citation" data-id="794495"><a href="/opinion/794495/united-states-v-dois-edward-brown/#745" aria-description="Citation for case: United States v. Dois Edward Brown">449 F.3d 741, 745</a></span> (6th Cir. 2006) (recognizing that, "[t]o justify a warrantless entry based on exigent circumstances, there must also be probable cause to enter the residence”).</p>
</footnote>
<footnote label="1">
<p id="b95-7">. “The poorest man may in his cottage bid defiance to all the forces of the Crown. It may be frail; its roof may shake; the wind may blow through it; the storm may enter; the rain may enter; but the King of England cannot enter—all his force dares not cross the threshold of the ruined tenement!” <em>Miller v. United States, </em><span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#307" aria-description="Citation for case: Miller v. United States">357 U.S. 301, 307</a></span>, <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">78 S.Ct. 1190</a></span>, <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">2 L.Ed.2d 1332</a></span> (1958) (quoting remarks of William Pitt, Earl of Chatham, during 1763 debate in Parliament) (internal quotation marks omitted).</p>
</footnote>
<footnote label="5">
<p id="b96-6">. <em>See also State </em>v. <em>Cothran, </em><span class="citation" data-id="1073268"><a href="/opinion/1073268/state-v-cothran/#522" aria-description="Citation for case: State v. Cothran">115 S.W.3d 513, 522</a></span> (Tenn. Crim. App. 2003) (“A sidewalk or pathway leading from a public street to the front door of a residence represents an ‘implied invitation' to the public to use the pathway in pursuing legitimate business or social interests with those inside the residence.” (quoting <em>State v. Harris, </em><span class="citation" data-id="9777503"><a href="/opinion/2459843/state-v-harris/#623" aria-description="Citation for case: State v. Harris">919 S.W.2d 619, 623</a></span> (Tenn. Crim. App. 1995))).</p>
</footnote>
</opinion>
```

---
