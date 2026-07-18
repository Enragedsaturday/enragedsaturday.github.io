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

## GROUP: content/cases/Gouled v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Gouled v. United States"
type: case
citation: "255 U.S. 298 (1921)"
parallel_cite: "41 S. Ct. 261; 65 L. Ed. 647"
neutral_cite: 1921 U.S. LEXIS 1826
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1921
date_decided: 1921-02-28
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: superseded
  as_of_content: 1921-02-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Gouled v. United States
  varies_by_point: false
  scope_note: "The mere-evidence rule was overruled/abandoned by Warden v. Hayden (1967), which held the Fourth Amendment does not bar the seizure of items of solely evidentiary value. The separate Gouled holding — that entry obtained by stealth, ruse, or social pretext can render a subsequent search unreasonable — retains vitality."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/99745/gouled-v-united-states/"
  cluster_id: 99745
  opinion_id: 99745
  identity_checked: true
homes:
  - page: "[[Trespass]]"
    role: "Historical (foil)"
related: ["[[Warden v. Hayden]]", "[[Boyd v. United States]]", "[[Weeks v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "mere-evidence-rule", "ruse-entry", "historical"]
holding: "Mere-evidence rule: warrants may seize only contraband, fruits, or instrumentalities, not items of solely evidentiary value (overruled by Warden v. Hayden); entry obtained by stealth or ruse can render a search unreasonable."
lake:
  record_id: Gouled v. United States
  status: verified
  projected_at: 2026-07-06
---

# Gouled v. United States

*255 U.S. 298 (1921)* · U.S. Supreme Court · **Historical** · Treatment: **overruled** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Gouled was suspected of conspiracy to defraud the United States in connection with war contracts. A business acquaintance, acting for federal officers, gained admission to Gouled's office under the pretense of a social/business visit and, in Gouled's absence, took a paper from the office. Later, papers were also seized from the office under search warrants issued on a Department of Justice agent's affidavit. The papers were admitted against Gouled at trial over Fourth and Fifth Amendment objections.

## Issue
(1) Is a search and seizure accomplished by an officer who obtains entry to an office by stealth or social/business pretext, rather than by force, within the Fourth Amendment's prohibition? (2) May a search warrant be used to seize a person's private papers that are of solely evidentiary value?

## Rule
**Entry by stealth or ruse.** A surreptitious taking is no less a Fourth Amendment violation than one by force. The Court held that "whether entrance to the home or office of a person suspected of crime be obtained by a representative of any branch or subdivision of the Government of the United States by stealth, or through social acquaintance, or in the guise of a business call, and whether the owner be present or not when he enters, any search and seizure subsequently and secretly made in his absence, falls within the scope of the prohibition of the Fourth Amendment." — 255 U.S. at 306. ^pin-306

**The mere-evidence rule.** Warrants "may not be used as a means of gaining access to a man's house or office and papers solely for the purpose of making search to secure evidence to be used against him in a criminal or penal proceeding, but . . . they may be resorted to only when a primary right to such search and seizure may be found in the interest which the public or the complainant may have in the property to be seized, or in the right to the possession of it." — *Id.* at 309. ^pin-309

*(This mere-evidence limitation was later overruled by [[Warden v. Hayden]].)*

## Application
On these facts, the federal agent's confederate gained entry to Gouled's office by pretext and, in Gouled's absence, took a document — a clandestine intrusion the Court treated as a Fourth Amendment search and seizure despite the absence of force. As to the warrant-seized papers, the items taken were of purely evidentiary character (an unexecuted contract form, a contract, and an attorney's bill said to be "without pecuniary value" but "evidence more or less injurious"), so under the then-governing rule they could not properly be made the object of a search warrant.

## Conclusion
The clandestine taking and the use of the evidentiary papers violated Gouled's Fourth and Fifth Amendment rights. The mere-evidence rule the case announced was abandoned in [[Warden v. Hayden]] (1967); Gouled survives today chiefly for its holding that a search obtained by stealth or pretext is not thereby removed from the Fourth Amendment.

## Treatment & subsequent history
- **Status:** overruled (in part) *(as of 2026-06-30)* — **Historical**.
- **Mere-evidence rule overruled/abandoned by** [[Warden v. Hayden]] (1967): the Fourth Amendment draws no distinction between "mere evidence" and contraband/fruits/instrumentalities, so evidentiary items may be seized on probable cause. This changes field application — officers may seize evidentiary materials, not only contraband, fruits, and instrumentalities.
- **Surviving principle:** the holding that entry obtained by stealth, ruse, or social pretext can render the ensuing search unreasonable remains good law and is cited in the consent/undercover line (cf. *[[Lewis v. United States (1966)|Lewis v. United States]]* (1966), distinguishing a legitimate undercover business visit).

## Appears on
- [[Trespass]] — *Historical (foil)*

## Sources
- *Gouled v. United States*, 255 U.S. 298 (1921) — https://www.courtlistener.com/opinion/99745/gouled-v-united-states/ — pinpoints: 306, 309.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f0f45d88bdefb8ee", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "255 U.S. 298 (1921)", "court": "U.S. Supreme Court", "neutral_cite": "1921 U.S. LEXIS 1826", "official_citation_present": true, "parallel_cite": "41 S. Ct. 261; 65 L. Ed. 647", "title": "Gouled v. United States", "year": "1921"}}
{"assertion_id": "4c65aac887443315", "dimension": "support", "kind": "home_role", "locator": {"home": "Trespass"}, "payload": {"home": "Trespass", "role": "Historical (foil)", "title": "Gouled v. United States"}}
{"assertion_id": "fd9ae84693fc2fcc", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Mere-evidence rule: warrants may seize only contraband, fruits, or instrumentalities, not items of solely evidentiary value (overruled by Warden v. Hayden); entry obtained by stealth or ruse can render a search unreasonable.", "title": "Gouled v. United States"}}
{"assertion_id": "a5f30113c7b0b722", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Gouled v. United States"}}
{"assertion_id": "dfc42dcf4bb11749", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1921-02-28", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Gouled v. United States", "field_i_validity": "superseded", "scope_note": "The mere-evidence rule was overruled/abandoned by Warden v. Hayden (1967), which held the Fourth Amendment does not bar the seizure of items of solely evidentiary value. The separate Gouled holding — that entry obtained by stealth, ruse, or social pretext can render a subsequent search unreasonable — retains vitality.", "title": "Gouled v. United States", "varies_by_point": "false"}}
```

### lake record — Gouled v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Gouled v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Gouled v. United States",
    "case_name_short": "Gouled",
    "case_name_full": "Gouled v. United States",
    "input_case_name": "Gouled v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1921-02-28",
    "year": 1921,
    "docket": null,
    "cluster_id": 99745,
    "lead_opinion_id": 99745,
    "sibling_ids": [
      99745
    ],
    "absolute_url": "/opinion/99745/gouled-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "255 U.S. 298",
      "volume": "255",
      "reporter": "U.S.",
      "page": "298",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "41 S. Ct. 261",
        "volume": "41",
        "reporter": "S. Ct.",
        "page": "261",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 647",
        "volume": "65",
        "reporter": "L. Ed.",
        "page": "647",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1921 U.S. LEXIS 1826",
        "volume": "1921",
        "reporter": "U.S. LEXIS",
        "page": "1826",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "255 U.S. 298",
        "volume": "255",
        "reporter": "U.S.",
        "page": "298",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "41 S. Ct. 261",
        "volume": "41",
        "reporter": "S. Ct.",
        "page": "261",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 647",
        "volume": "65",
        "reporter": "L. Ed.",
        "page": "647",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1921 U.S. LEXIS 1826",
        "volume": "1921",
        "reporter": "U.S. LEXIS",
        "page": "1826",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "255 U.S. 298",
    "official_selection": {
      "court_class": "scotus",
      "selected": "255 U.S. 298",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-306",
      "page": null,
      "quote": "--- # Gouled v. United States *255 U.S. 298 (1921)* \u00b7 U.S. Supreme Court \u00b7 **Historical** \u00b7 Treatment: **overruled** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Gouled was suspected of conspiracy to defraud the United States in connection with war contracts. A business acquaintance, acting for federal officers, gained admission to Gouled's office under the pretense of a social/business visit and, in Gouled's absence, took a paper from the office. Later, papers were also seized from the office under search warrants issued on a Department of Justice agent's affidavit. The papers were admitted against Gouled at trial over Fourth and Fifth Amendment objections. ## Issue (1) Is a search and seizure accomplished by an officer who obtains entry to an office by stealth or social/business pretext, rather than by force, within the Fourth Amendment's prohibition? (2) May a search warrant be used to seize a person's private papers that are of solely evidentiary value? ## Rule **Entry by stealth or ruse.** A surreptitious taking is no less a Fourth Amendment violation than one by force. The Court held that",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-309",
      "page": null,
      "quote": "may not be used as a means of gaining access to a man's house or office and papers solely for the purpose of making search to secure evidence to be used against him in a criminal or penal proceeding, but . . . they may be resorted to only when a primary right to such search and seizure may be found in the interest which the public or the complainant may have in the property to be seized, or in the right to the possession of it.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "superseded",
    "as_of_content": "1921-02-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Gouled v. United States",
    "varies_by_point": false,
    "scope_note": "The mere-evidence rule was overruled/abandoned by Warden v. Hayden (1967), which held the Fourth Amendment does not bar the seizure of items of solely evidentiary value. The separate Gouled holding \u2014 that entry obtained by stealth, ruse, or social pretext can render a subsequent search unreasonable \u2014 retains vitality.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Warden v. Hayden",
          "cluster_id": 107465,
          "cite": "387 U.S. 294",
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:overruled"
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
        "journal_ref": "Gouled v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hernandez v. State",
          "cluster_id": 1882057,
          "cite": [
            "60 S.W.3d 106",
            "2001 Tex. Crim. App. LEXIS 104",
            "2001 WL 1415274"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hernandez v. State",
          "cluster_id": 2104545,
          "cite": [
            "13 S.W.3d 492",
            "2000 WL 246424"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Henry Jerome Hicks",
          "cluster_id": 593876,
          "cite": [
            "978 F.2d 722",
            "298 U.S. App. D.C. 225"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Andrew Eschweiler",
          "cluster_id": 442818,
          "cite": [
            "745 F.2d 435"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jones v. Berry",
          "cluster_id": 8928076,
          "cite": [
            "722 F.2d 443"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brown v. State",
          "cluster_id": 1753238,
          "cite": [
            "657 S.W.2d 797",
            "1983 Tex. Crim. App. LEXIS 1136"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rubio",
          "cluster_id": 8929383,
          "cite": [
            "727 F.2d 786",
            "13 Fed. R. Serv. 365"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Scherer, Jr.",
          "cluster_id": 400981,
          "cite": [
            "673 F.2d 176"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Nelson Bunker Hunt and W. Herbert Hunt",
          "cluster_id": 322924,
          "cite": [
            "505 F.2d 931",
            "1974 U.S. App. LEXIS 5521"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane1_negative"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wong Sun v. United States",
          "cluster_id": 106515,
          "cite": [
            "9 L. Ed. 2d 441",
            "83 S. Ct. 407",
            "371 U.S. 471",
            "1963 U.S. LEXIS 2431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carroll v. United States",
          "cluster_id": 100567,
          "cite": [
            "267 U.S. 132",
            "45 S. Ct. 280",
            "69 L. Ed. 543",
            "1925 U.S. LEXIS 361"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. United States",
          "cluster_id": 104504,
          "cite": [
            "92 L. Ed. 2d 436",
            "68 S. Ct. 367",
            "333 U.S. 10",
            "1948 U.S. LEXIS 2583",
            "92 L. Ed. 436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raddatz",
          "cluster_id": 110315,
          "cite": [
            "65 L. Ed. 2d 424",
            "100 S. Ct. 2406",
            "447 U.S. 667",
            "1980 U.S. LEXIS 49"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ker v. California",
          "cluster_id": 106641,
          "cite": [
            "10 L. Ed. 2d 726",
            "83 S. Ct. 1623",
            "374 U.S. 23",
            "1963 U.S. LEXIS 2473",
            "24 Ohio Op. 2d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Elkins v. United States",
          "cluster_id": 106107,
          "cite": [
            "4 L. Ed. 2d 1669",
            "80 S. Ct. 1437",
            "364 U.S. 206",
            "1960 U.S. LEXIS 1989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Olmstead v. United States",
          "cluster_id": 101320,
          "cite": [
            "277 U.S. 438",
            "48 S. Ct. 564",
            "72 L. Ed. 944",
            "1928 U.S. LEXIS 694",
            "66 A.L.R. 376"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hoffa v. United States",
          "cluster_id": 107318,
          "cite": [
            "17 L. Ed. 2d 374",
            "87 S. Ct. 408",
            "385 U.S. 293",
            "1966 U.S. LEXIS 2778"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rabinowitz",
          "cluster_id": 104769,
          "cite": [
            "94 L. Ed. 2d 653",
            "70 S. Ct. 430",
            "339 U.S. 56",
            "1950 U.S. LEXIS 2298",
            "94 L. Ed. 653"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fisher v. United States",
          "cluster_id": 109432,
          "cite": [
            "48 L. Ed. 2d 39",
            "96 S. Ct. 1569",
            "425 U.S. 391",
            "1976 U.S. LEXIS 98",
            "37 A.F.T.R.2d (RIA) 1244"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nardone v. United States",
          "cluster_id": 103259,
          "cite": [
            "308 U.S. 338",
            "60 S. Ct. 266",
            "84 L. Ed. 307",
            "1939 U.S. LEXIS 1132"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hoffman v. United States",
          "cluster_id": 104912,
          "cite": [
            "95 L. Ed. 2d 1118",
            "71 S. Ct. 814",
            "341 U.S. 479",
            "1951 U.S. LEXIS 1802",
            "95 L. Ed. 1118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Agnello v. United States",
          "cluster_id": 100711,
          "cite": [
            "269 U.S. 20",
            "46 S. Ct. 4",
            "70 L. Ed. 145",
            "1925 U.S. LEXIS 2",
            "51 A.L.R. 409"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Abel v. United States",
          "cluster_id": 106021,
          "cite": [
            "4 L. Ed. 2d 668",
            "80 S. Ct. 683",
            "362 U.S. 217",
            "1960 U.S. LEXIS 1412"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. United States",
          "cluster_id": 104422,
          "cite": [
            "67 S. Ct. 1098",
            "331 U.S. 145",
            "91 L. Ed. 1399",
            "1947 U.S. LEXIS 2936"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McNally v. United States",
          "cluster_id": 111945,
          "cite": [
            "97 L. Ed. 2d 292",
            "107 S. Ct. 2875",
            "483 U.S. 350",
            "1987 U.S. LEXIS 2878",
            "55 U.S.L.W. 5011"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(99745) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01OTk2MTYwMDAwMCZzPTE0MzcyMjgmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%2899745%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(99745)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03NTEmcz0xMTA4ODImdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%2899745%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(99745)",
        "reviewed": 4,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 4,
        "triage_read": 0,
        "triage_snippet_classified": 4
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(99745)",
    "indexed_citing_opinions": 766,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 99745,
        "count": 766,
        "count_source": "search"
      }
    ],
    "citation_count": 1256,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/gouled-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjI3MjUxNTcmcz0yMTEyMDY5JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%2899745%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 99745,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 99745,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 99745,
        "cited_id": 99506,
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
    "date_created": "2026-07-05T05:45:51Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: overruled -> superseded",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:46:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:46:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:31Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:46:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Gouled v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b340-9">
  Mr. Justice Clarke
 </author>
<p id="AbB">
  delivered the opinion of the court.
 </p>
<p id="b340-10">
  In a joint indictment the plaintiff in error, Gouled, one Vaughan, an officer of the United States Army, and a third, an attorney at law, were charged, in the first count, with being parties to a conspiracy to defraud the United States, in violation of § 37 of the Federal Criminal Code, and, in the second count, with having used the mails to
  <span citation-index="1" class="star-pagination" label="303"> 
   *303
   </span>
  promote a scheme to defraud the United States, in violation of § 215 of that Code. Vaughan pleaded guilty, the attorney was acquitted, and Gouled, whom we shall refer to as the defendant, was convicted, and thereupon prosecuted error from the Circuit Court of Appeals, which certifies to this court six questions which we are to consider.
 </p>
<p id="Asfi">
  Of these questions, the first two relate to the admission in evidence of a paper surreptitiously, taken from the office of the defendant by one acting under direction of officers of the Intelligence Department of the Army of the United States, and the remaining four relate to papers taken from defendant’s office, under two search warrants, issued pursuant to the Act of June 15, 1917, c. 30, <span class="citation no-link">40 Stat. 217</span>, 228. It was objected on the trial, and is here insisted, that it was error to admit these papers in evidence because possession of them was obtained by violating the rights secured to the defendant by the Fourth and Fifth Amendments to the Constitution of the United States.
 </p>
<p id="b341-6">
  The Fourth Amendment reads:
 </p>
<blockquote id="b341-7">
  • “The right of the people to be secure in their persons, houses, papers -and effects, against unreasonable searches and seizures, shall not be violated, and no warrants shall issue, but upon probable cause, supported by oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.”
 </blockquote>
<p id="b341-8">
  The part of the Fifth Amendment here involved reads:
 </p>
<blockquote id="Am3g">
  “No person . . . shall be compelled in any criminal case to be a witness against, himself.”
 </blockquote>
<p id="b341-10">
  It would not be possible to add to thé emphasis with which the framers of our Constitution' and this court (in
  <em>
   Boyd
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, in
  <em>
   Weeks
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, and in
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>) have declared the importance to political liberty and to the welfare of our country of the due observance of the. rights guaranteed under the Consti
  <span citation-index="1" class="star-pagination" label="304"> 
   *304
   </span>
  tution by "these two Amendments. The effect of the decisions cited is: that such rights are declared to be indispensable to the “full enjoyment of personal security, personal liberty and private property”; that they are to be regarded as of the very essence of constitutional liberty; and that the guaranty of them is as important and as imperative as are the guaranties of the other fundamental rights of the individual citizen, — the right, to trial by jury, to the writ of
  <em>
   habeas corpus
  </em>
  and to due process of law. It has been repeatedly decided that these Amendments should receive a liberal construction, so as to prevent stealthy encroachment upon or “gradual depreciation” of the rights secured by them, by imperceptible practice of courts or by well-intentioned but mistakenly over-zealous executive officers.
 </p>
<p id="b342-5">
  In the spirit of these decisions we must deal with the questions before us.
 </p>
<p id="b342-6">
  The facts derived from the certificate, • essential to be considered, in answering the first two questions, are: that in January, 1918, it was suspected that the defendant, Gouled, and Vaughan were conspiring to defraud the Government through contracts with it for clothing and equipment; that one Cohen, a private in the Army, attached to the Intelligence Department, and a business acquaintance of defendant Gouled, under direction of his superior officers, pretending to make a friendly call upon the defendant, gained admission to his office and, in his absence, without warrant of any character, seized and carried away sevéral documents; that one of these papers, described as “of evidential value only” and belonging to Gouled, was subsequently delivered to the United States District Attorney, and was by him introduced in evidence over the objection of the defendant that possession of it was obtained by a violation of the Fourth or Fifth Amendment to the Constitution; and that the defendant did not know that Cohen had earned away any of his papers until
  <span citation-index="1" class="star-pagination" label="305"> 
   *305
   </span>
  he appeared on the witness stand and detailed the facts with respect thereto as we have stated them, when, necessarily, objection was first made to the admission of the paper in evidence.
 </p>
<p id="b343-5">
  • Out of these facts arise the first two questions, both relating to the paper thus seized. The first of these, is:
 </p>
<blockquote id="b343-6">
  “Is the secret taking or abstraction, without force, by a. representative of any branch or subdivision of the Government of the United States, of a paper writing of evidential value only belonging to one suspected of crime and from the house or office of such person, — a violation of the 4th amendment?”
 </blockquote>
<p id="b343-7">
  The.ground on which the trial court overruled the objection to this paper is not stated, but from the certificate and the argument we must infer that it was admitted either because it appeared that the possession of it was obtained without the use of force or illegal coercion, or because the objection to it came too late.
 </p>
<p id="b343-8">
  The objection was not too late, for, coming as it did promptly upon the first notice the defendant had that the Government was in possession of the paper, the rule of practice relied upon, that such an objection will not be entertained unless made before trial, was obviously inapplicable.
 </p>
<p id="b343-9">
  The prohibition of the Fourth Amendment is against all unreasonable seárches and seizures and if for a Government officer to obtain entrance to a man’s house or office by force or by an illegal threat or show of force, amounting to coercion, and then to search for and seize his private papers would be an unreasonable and. therefore a prohibited search and seizure, as it certainly would be, it is impossible to successfully contend that a like search and seizure would be a reasonable one if only admission were obtained by stealth instead of by force or coercion. The security and privacy of the home or office ancLof the papers of the owner would be as much invaded and the search and
  <span citation-index="1" class="star-pagination" label="306"> 
   *306
   </span>
  seizure would be as much against his will in the one case as in the other, and it must therefore be regarded as equally in violation of his constitutional rights.
 </p>
<p id="b344-4">
  Without discussing them, we cannot doubt that such decisions as there are in conflict with this conclusion are unsound, and that, whether entrance to the home or office of a person suspected of crime be obtained by a representative of any branch or subdivision of the Government of the United States by stealth, or through social acquaintance, or in the guise of a business call, and whether the owner be present or not when he enters, any search and seizure subsequently and secretly made in his absence, falls within the scope of the prohibition of the Fourth Amendment.,, and therefore the answer to the first question must be in the affirmative.
 </p>
<p id="b344-5">
  The second question reads:
 </p>
<blockquote id="b344-6">
  “Is the admission of such paper in evidence against the same person when indicted for crime a violation of the bth amendment? ”
 </blockquote>
<p id="b344-7">
  Upon authority of the
  <em>
   Boyd Case, supra,
  </em>
  this second question must also be answered in the affirmative. In practice the result is the same to one accused of crime, whether he be obliged to supply evidence against himself or whether such evidence be obtained by an illegal search of his premises and seizure of his private papers. In either case he is the unwilling source of the evidence, and the Fifth Amendment forbids that he shall be compelled to be a witness against himself in a criminal case.
 </p>
<p id="b344-8">
  The remaining four questions relate' to three other papers which were admitted in evidence on the trial over the same constitutional objections as were interposed to the admission of the first paper. One was an unexecuted form of contract between the defendant and one Lavinsky, another was a written contract, signed by the defendant and one Steinthal, and the third was a bill for
  <span citation-index="1" class="star-pagination" label="307"> 
   *307
   </span>
  disbursements and professional services rendered by the attorney at law to the defendant Gouled.
 </p>
<p id="b345-5">
  Of these' papers, the first was seized in defendant’s office under a search warrant, dated June 17, and the other two under a like warrant dated July 22, 1918,-each of which was issued by a United States Commissioner on the affidavit of an agent of the Department of Justice. It is certified that it was averred in the first affidavit that there were in Gouled’s office “certain property, to wit: certain contracts of the said Felix Gouled with S. Lavihsky [which] were used as a means of committing a felony, to wit: ... as means for the bribery of a certain office? of the United States.” It is also certified that the second, affidavit declared that Gouled had at his office “certain letters, papers, documents and writings which ... relate to, concern and have been used in the commission of a felony, to wit: -a conspiracy to defraud the United States.” Neither the affidavits nor the warrants are given in full in the certificate, but no exception was taken to the sufficiency of either.
 </p>
<p id="b345-6">
  - After the seizure of the papers, a joint indictment was returned; as stated, against Gouled, Vaughan and the attorney, and before trial a motion,was made by Gouled, for a return of the papers seized under the search warrants, which was denied, and when the motion was renewed at the trial, but before any evidence was introduced, it was again , denied. The denial of this motion is not assigned as error.
 </p>
<p id="b345-7">
  The contract of the defendant with Steinthal, which-was seized under the warrant, was not offered in evidence ~but a duplicate original, .obtained from Steinthal, was admitted over the objection that the possession of the seized original must have suggested the existence and the obtaining of the counterpart, and that therefore the use of it in evidence would violate the rights of the defendant under the Fourth or Fifth Amendment.
  <em>
   Silverthorne
  </em>
<span citation-index="1" class="star-pagination" label="308"> 
   *308
   </span>
<em>
   Lumber Co.
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>. The unsigned form of contract and the attorney’s bill were offered and also admitted over the same constitutional objection. There is no statement in the certificate of the contents of these papers, but it is said of them only, that they belonged to Gouled, that they were without pecuniary value and that they- constituted evidence “more or less .injurious to” the defendant.
 </p>
<p id="b346-4">
  It is apparent from this statement that to answer the remaining four 'questions involves a consideration of the applicable law of search warrants.
 </p>
<p id="b346-5">
  The wording of the Fourth Amendment implies that search warrants were in familiar use when the Constitution was adopted and, plainly, that when issued “upon probable cause, supported by óáth or affirmation,' and particularly describing'the place to be searched, and the "persons or things to be seized,” searches, and seizures made under them, are to be regarded as not-unreasonable, and therefore not prohibited by the Amendment. Searches and seizures are as constitutional under the Amendment when made under valid search warrants as they áre unconstitutional,' because unreasonable,--when máde without them, — the .permission of the. Amendment has the same constitutional 'warrant as the prohibition has, ánd the definition of the former restrains the scope of the latter. All of this is abundantly recognized in the opinions of the
  <em>
   <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span>
  </em>
  and
  <em>
   Weeks Cases, supra,
  </em>
  in which it is pointed out that at the time the Constitution was adopted stolen of forfeited property, or property liable to duties and concealed to avoid payment of them, excisable articles and books required by law to be kept with respect to them,' counterfeit coin, burglars’ tools and weapons, impleráents 'of gambling “and many other things of like character,” might be seárched for in home of office and if found might be seized, under search warrants, lawfully applied for, issued and executed.
 </p>
<p id="A8p">
<span citation-index="1" class="star-pagination" label="309"> 
   *309
   </span>
  Although search warrants have thus been used in many cases ever since the adoption of the Constitution, and although their use has been extended from time to .time to meet new cases within the old rules, nevertheless it is clear that, at common law and as the result of the
  <em>
   <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span>
  </em>
  and Weeks
  <em>
   Cases, supra,
  </em>
  they may not be used as a means of gaming access to a man’s' house or office and papers solely for the purpose of making search to secure evidence to be used against him in a criminal or penal proceeding, but that they may be resorted to only when a primary right to such search and seizure may be found in the interest which the public or the complainant may have in the property to be seized, or in the right to the possession of it, or when a Valid exercise of the police power renders possession of the property by- the accused unlawful and provides that it may be taken.
  <em>
   Boyd Case,
  </em>
  pp. 623, 624.
 </p>
<p id="AxH">
  There is no special sanctity in papers, as distinguished from other forms of property, to render them immune from search and seizure, if only they fall within the scope of the principles of the cases in which other property may be seized, and if they be adequately described in the affidavit and warrant. Stolen or forged papers have been so seized,
  <em>
   Langdon
  </em>
  v.
  <em>
   People,
  </em>
  133 Illinois, 382, and lottery tickets, under a statute prohibiting their possession with intent to sell them,
  <em>
   Commonwealth
  </em>
  v.
  <em>
   Dana,
  </em>
  2 Mete. 329, and we cannot doubt that contracts may be so used as instruments or agencies for perpetrating frauds upon the Government as to give the public an interest in them which would justify the search for and seizure of them, under a properly issued search warrant, for the purpose of preventing further frauds.
 </p>
<p id="b347-6">
  With these principles of law in mind, we come to the remaining questions.
 </p>
<p id="A0uq1">
  The third question.reads: “Are papers of no pecuniary value ,but possessing evidential value against persons presently suspected and subsequently indicted under
  <span citation-index="1" class="star-pagination" label="310"> 
   *310
   </span>
  Sections 37 and 215 of the United States Criminal Code, when' taken under search warrants issued pursuant to the Act of June 15, 1917, from the house or office of the person so suspected, — seized and taken in violation of the 4th Amendment? ”
 </p>
<p id="AXY">
  That the papers involved are of no pecuniary value is of no significance. Many papers, having no pecuniary value to others, are of the greatest possible value to the owners and are property of a most important character
  <em>
   (Boyd Case, supra,
  </em>
  pp. 627, 628), and since those here involved possessed “evidential value ” against the defendant, we must assume that they were relevant to the issue..
 </p>
<p id="b348-6">
  Restraining the questions to the papers described, and first as to the unexecuted form of contract with Lavinsky, a stranger to the indictment. While the contents of this paper are not given, it is impossible to see how the Government could have such an interest in such a paper that under the principles of law stated it would have the right to take it into its possession to prevent injury to the public from its use. The Government could desire its possession only to use it as evidence against the defendant and to search for and seize it for such purpose was unlawful.
 </p>
<p id="b348-7">
  Likewise the public could be interested in the bill of the attorney for legal services only to the extent that it might be used as evidence and the seizure of this also was unlawful. '
 </p>
<p id="b348-8">
  As to the contract with Steinthal, also a stranger to the indictment. It is not difficult, as we have said, to imagine, how an executed written contract might be an important agency or instrumentality in the bribing of a public servant and in perpetrating frauds upon the Government so that it would have a legitimate and important interest in seizing such a paper in order to prevent further frauds, but the facts necessary to give this contract such a character do not appear in the certificate. On the con
  <span citation-index="1" class="star-pagination" label="311"> 
   *311
   </span>
  trary, -this third question recites that the papers are all of no pecuniary, but are of evidential, value, and in the sixth question it is recited that they are “of evidential value only,” so that it is impossible to say; on the record before us, that the Government had any interest in it other than as evidence against the accused, and therefore as to all three papers the answer to the question must be in the affirmative.
 </p>
<p id="b349-5">
  The fourth question reads: “If such papers so taken are admitted in evidence against the person from whose house or office they were taken, such person being then on trial for the crime of which he was accused in the affidavit for warrant, — is such admission in evidence a violation of the 5th amendment? ”
 </p>
<p id="b349-6">
  The same papers being involved, the answer to this question must be in the affirmative for, they having been seized in an unconstitutional search, to permit them to be used in evidence would be, in effect, as ruled in the
  <em>
   <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span>
  </em>
  Case, to compel the. defendant to become a witness against himself.
 </p>
<p id="b349-7">
  The fifth question reads: “If in the affidavit for search warrant under Act of June 15, 1917, the party whose premises are to be searched be charged with one crime and property be taken under the warrant issued thereon, —can such property so seized be introduced in evidence against said party when on trial for a different offence? ”
 </p>
<p id="b349-8">
  It has never been required that a criminal prosecution should be pending against a person in order to justify search for and seizure of his property under a proper warrant, if a case of crime having been committed and of probable cause is made out sufficient to satisfy the law and the officer having authority to issue it, and we see no reason why property seized under a valid search warrant, when thus lawfully obtained by the Government, may not be used in the prosecution of a suspected person for a crime other than that which may have been described
  <span citation-index="1" class="star-pagination" label="312"> 
   *312
   </span>
  in the affidavit as having been committed by him. The question assumes that the property seized was obtained on a search warrant, sufficient in form to satisfy the law, and if the papers to which the question refers had been of a character to be thus obtained, lawfully, it would have been competent to use then! to prove any crime against the accused as to which they constituted relevant evidence.
 </p>
<p id="b350-5">
  The sixth question reads: “If papers of evidential value only be seized under a search warrant and t^e party from whose house or office they are taken be indicted;— if he then move before trial for the return of said papers and said motion is denied — is the court at trial bound in law to inquire as to. the origin of or method of procuring said papers when they are offered in. evidence against the party so indicted? ”
 </p>
<p id="b350-6">
  The papers being of “evidential value only” and having been unlawfully seized, this question really is, whether, it having been decided on a motion before trial that they should not be returned to the defendant, the trial court, when objection was made to their use on the trial, was' bound to again inquire as to the unconstitutional origin of thé possession of them. It is'plain that the trial court acted upon the rule, widely adopted, that courts in criminal trials will not pause to. determine how the possession of evidence tendered has been obtained. While tliis is a rule; of great practical importance, yet, after all, it is only a rule of procedure, and therefore it is not to be applied as a hard and fast formula to every case, regardless of its.special circumstances. We think rather that it is a rule to be used to secure the ends of justice under the circumstances presented by each case, and -where, in the progress of a trial, it becomes propable that there has been an unconstitutional seizure of papers, it is the. duty of the trial court to entertain an objection to their admission or a motion for their exclusion and to consider
  <span citation-index="1" class="star-pagination" label="313"> 
   *313
   </span>
  and decide the question as then presented; even where a motion to return the papers may have been denied before trial. A rule, of practice must not be allowed for any technical reason to prevail over a constitutional right.
 </p>
<p id="b351-5">
  In the case we are considering the certificate shows that a motion to return the papers, seized under the search warrants, was made before the trial, and was denied, and that, on the trial of the case before another judge, this ruling was treated as conclusive, although, as we have seen, in the progress of the trial it must have become. apparent that the papers had been unconstitutionally seized. The constitutional objection having been renewed,.,. under the circumstances, the court should have inquired as to the origin of the possession of the papers when they were offered in evidence against the defendant.
 </p>
<p id="b351-6">
<em>
   Each question is answered, Yes.
  </em>
</p>
</opinion>
```

---

## GROUP: content/cases/Jones v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Jones v. United States"
type: case
citation: "362 U.S. 257 (1960)"
parallel_cite: "80 S. Ct. 725; 4 L. Ed. 2d 697; 78 A.L.R. 2d 233"
neutral_cite: 1960 U.S. LEXIS 1413
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1960
date_decided: 1960-03-28
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: superseded
  as_of_content: 1960-03-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Jones v. United States
  varies_by_point: false
  scope_note: "The 'automatic standing' rule was overruled by United States v. Salvucci (1980); the broad 'legitimately on premises' standing test was disavowed by Rakas v. Illinois (1978), which refocused standing on whether the defendant's own reasonable expectation of privacy was invaded."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106022/jones-v-united-states/"
  cluster_id: 106022
  opinion_id: 106022
  identity_checked: true
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: "Historical / origin"
related: ["[[Rakas v. Illinois]]", "[[United States v. Salvucci]]", "[[Katz v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "standing", "suppression", "historical"]
holding: "Established \"automatic standing\" for those charged with possessory offenses and the broader rule that anyone \"legitimately on the…"
lake:
  record_id: Jones v. United States
  status: verified
  projected_at: 2026-07-09
---

# Jones v. United States

*362 U.S. 257 (1960)* · U.S. Supreme Court · **Historical** · Treatment: **overruled** *(as of 2026-06-30)* — overruled by [[Rakas v. Illinois]] and [[United States v. Salvucci]]
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal narcotics agents executed a search warrant at an apartment belonging to Jones's friend Evans, where Jones was present with Evans's permission. The agents found narcotics and paraphernalia, and Jones was charged with federal possessory narcotics offenses. He moved to suppress, but the lower courts denied him standing because he asserted no ownership or possessory interest in the apartment or the seized items.

## Issue
Whether a defendant charged with a possessory offense, or a person who is legitimately on the premises searched, has standing to move to suppress evidence obtained in an allegedly unlawful search.

## Rule
Yes, on two independent grounds. First, automatic standing for those charged with possession: "In cases where the indictment itself charges possession, the defendant in a very real sense is revealed as a 'person aggrieved by an unlawful search and seizure' upon a motion to suppress evidence prior to trial." — 362 U.S. at 264. ^pin-264

Second, broader possessory-interest standing: "anyone legitimately on premises where a search occurs may challenge its legality by way of a motion to suppress, when its fruits are proposed to be used against him." — [*Id.* at 267](https://www.courtlistener.com/opinion/106022/jones-v-united-states/#:~:text=anyone%20legitimately%20on%20premises%20where). ^pin-267

## Application
Jones was charged with a possessory narcotics offense and was, by his own testimony, present in Evans's apartment with Evans's consent at the time of the search. Under either ground — the automatic standing flowing from the possessory charge, or his legitimate presence on the premises — Jones was a "person aggrieved" entitled to litigate the search, so he was entitled to have his motion to suppress adjudicated on the merits (the Court then sustained the warrant as adequately supported by corroborated hearsay).

## Conclusion
Jones had standing to contest the search; the lower courts erred in denying it. (On the merits the warrant was upheld and the conviction affirmed.) Both standing grounds announced here have since been overruled.

## Treatment & subsequent history
- **Status:** overruled *(as of 2026-06-30)* — **Historical** (tier 6).
- The "automatic standing" rule was **overruled by [[United States v. Salvucci]]** (1980) after *[[Simmons v. United States]]* removed the self-incrimination dilemma it was designed to cure.
- The "legitimately on premises" standing test was **disavowed by [[Rakas v. Illinois]]** (1978), which held that Fourth Amendment rights are personal and that standing turns on whether the defendant's **own** legitimate expectation of privacy was violated — not on mere lawful presence.

## Appears on
- [[Standing to Challenge a Search]] — *Historical / origin*

## Sources
- *Jones v. United States*, 362 U.S. 257 (1960) — https://www.courtlistener.com/opinion/106022/jones-v-united-states/ — pinpoints: 264, 267.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "164442afb28a2290", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "362 U.S. 257 (1960)", "court": "U.S. Supreme Court", "neutral_cite": "1960 U.S. LEXIS 1413", "official_citation_present": true, "parallel_cite": "80 S. Ct. 725; 4 L. Ed. 2d 697; 78 A.L.R. 2d 233", "title": "Jones v. United States", "year": "1960"}}
{"assertion_id": "3c383488569f9ab3", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Established \\\"automatic standing\\\" for those charged with possessory offenses and the broader rule that anyone \\\"legitimately on the…", "title": "Jones v. United States"}}
{"assertion_id": "6585d83978e2d0b4", "dimension": "support", "kind": "home_role", "locator": {"home": "Standing to Challenge a Search"}, "payload": {"home": "Standing to Challenge a Search", "role": "Historical / origin", "title": "Jones v. United States"}}
{"assertion_id": "39f99d2979d8be23", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Jones v. United States"}}
{"assertion_id": "fde71318d3aa0df7", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1960-03-28", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Jones v. United States", "field_i_validity": "superseded", "scope_note": "The 'automatic standing' rule was overruled by United States v. Salvucci (1980); the broad 'legitimately on premises' standing test was disavowed by Rakas v. Illinois (1978), which refocused standing on whether the defendant's own reasonable expectation of privacy was invaded.", "title": "Jones v. United States", "varies_by_point": "false"}}
```

### lake record — Jones v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Jones v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Jones v. United States",
    "case_name_short": "Jones",
    "case_name_full": "Jones v. United States",
    "input_case_name": "Jones v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1960-03-28",
    "year": 1960,
    "docket": null,
    "cluster_id": 106022,
    "lead_opinion_id": 106022,
    "sibling_ids": [
      106022
    ],
    "absolute_url": "/opinion/106022/jones-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8948768,
        "score": 20,
        "case_name": "Jones v. United States"
      },
      {
        "cluster_id": 8948588,
        "score": 20,
        "case_name": "Jones v. United States"
      },
      {
        "cluster_id": 8947339,
        "score": 20,
        "case_name": "Jones v. United States"
      },
      {
        "cluster_id": 8947221,
        "score": 20,
        "case_name": "Jones v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "362 U.S. 257",
      "volume": "362",
      "reporter": "U.S.",
      "page": "257",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "80 S. Ct. 725",
        "volume": "80",
        "reporter": "S. Ct.",
        "page": "725",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 L. Ed. 2d 697",
        "volume": "4",
        "reporter": "L. Ed. 2d",
        "page": "697",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "78 A.L.R. 2d 233",
        "volume": "78",
        "reporter": "A.L.R. 2d",
        "page": "233",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1960 U.S. LEXIS 1413",
        "volume": "1960",
        "reporter": "U.S. LEXIS",
        "page": "1413",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "362 U.S. 257",
        "volume": "362",
        "reporter": "U.S.",
        "page": "257",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 S. Ct. 725",
        "volume": "80",
        "reporter": "S. Ct.",
        "page": "725",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 L. Ed. 2d 697",
        "volume": "4",
        "reporter": "L. Ed. 2d",
        "page": "697",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1960 U.S. LEXIS 1413",
        "volume": "1960",
        "reporter": "U.S. LEXIS",
        "page": "1413",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "78 A.L.R. 2d 233",
        "volume": "78",
        "reporter": "A.L.R. 2d",
        "page": "233",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "362 U.S. 257",
    "official_selection": {
      "court_class": "scotus",
      "selected": "362 U.S. 257",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-264",
      "page": null,
      "quote": "--- # Jones v. United States *362 U.S. 257 (1960)* \u00b7 U.S. Supreme Court \u00b7 **Historical** \u00b7 Treatment: **overruled** *(as of 2026-06-30)* \u2014 overruled by [[Rakas v. Illinois]] and [[United States v. Salvucci]] <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Federal narcotics agents executed a search warrant at an apartment belonging to Jones's friend Evans, where Jones was present with Evans's permission. The agents found narcotics and paraphernalia, and Jones was charged with federal possessory narcotics offenses. He moved to suppress, but the lower courts denied him standing because he asserted no ownership or possessory interest in the apartment or the seized items. ## Issue Whether a defendant charged with a possessory offense, or a person who is legitimately on the premises searched, has standing to move to suppress evidence obtained in an allegedly unlawful search. ## Rule Yes, on two independent grounds. First, automatic standing for those charged with possession:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-267",
      "page": null,
      "quote": "anyone legitimately on premises where a search occurs may challenge its legality by way of a motion to suppress, when its fruits are proposed to be used against him.",
      "star_marker": "267",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 23289,
      "fragment": "#:~:text=anyone%20legitimately%20on%20premises%20where",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "superseded",
    "as_of_content": "1960-03-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Jones v. United States",
    "varies_by_point": false,
    "scope_note": "The 'automatic standing' rule was overruled by United States v. Salvucci (1980); the broad 'legitimately on premises' standing test was disavowed by Rakas v. Illinois (1978), which refocused standing on whether the defendant's own reasonable expectation of privacy was invaded.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Rakas v. Illinois",
          "cluster_id": 109953,
          "cite": "439 U.S. 128",
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:overruled"
      },
      {
        "citing_case": {
          "name": "United States v. Salvucci",
          "cluster_id": 110325,
          "cite": "448 U.S. 83",
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:overruled"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. DeJesus",
          "cluster_id": 4860242,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane1_negative"
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
        "journal_ref": "Jones v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ernest Glover",
          "cluster_id": 4433034,
          "cite": [
            "872 F.3d 625",
            "2017 WL 4507530",
            "2017 U.S. App. LEXIS 19741"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Glover",
          "cluster_id": 3190718,
          "cite": [
            "174 F. Supp. 3d 431",
            "2016 U.S. Dist. LEXIS 43260",
            "2016 WL 1273171"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Faux",
          "cluster_id": 7312636,
          "cite": [
            "94 F. Supp. 3d 258",
            "2015 U.S. Dist. LEXIS 37051",
            "2015 WL 1347041"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane1_negative"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wong Sun v. United States",
          "cluster_id": 106515,
          "cite": [
            "9 L. Ed. 2d 441",
            "83 S. Ct. 407",
            "371 U.S. 471",
            "1963 U.S. LEXIS 2431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "North Carolina v. Alford",
          "cluster_id": 108215,
          "cite": [
            "27 L. Ed. 2d 162",
            "91 S. Ct. 160",
            "400 U.S. 25",
            "1970 U.S. LEXIS 3",
            "56 Ohio Op. 2d 85"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mapp v. Ohio",
          "cluster_id": 106285,
          "cite": [
            "6 L. Ed. 2d 1081",
            "81 S. Ct. 1684",
            "367 U.S. 643",
            "1961 U.S. LEXIS 812"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aguilar v. Texas",
          "cluster_id": 106865,
          "cite": [
            "12 L. Ed. 2d 723",
            "84 S. Ct. 1509",
            "378 U.S. 108",
            "1964 U.S. LEXIS 994"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malley v. Briggs",
          "cluster_id": 111611,
          "cite": [
            "89 L. Ed. 2d 271",
            "106 S. Ct. 1092",
            "475 U.S. 335",
            "1986 U.S. LEXIS 29",
            "54 U.S.L.W. 4243"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Valley Forge Christian College v. Americans United for Separation of Church and State, Inc.",
          "cluster_id": 110599,
          "cite": [
            "70 L. Ed. 2d 700",
            "102 S. Ct. 752",
            "454 U.S. 464",
            "1982 U.S. LEXIS 22",
            "50 U.S.L.W. 4103"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Payne v. Tennessee",
          "cluster_id": 112643,
          "cite": [
            "115 L. Ed. 2d 720",
            "111 S. Ct. 2597",
            "501 U.S. 808",
            "1991 U.S. LEXIS 3821"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Calandra",
          "cluster_id": 108898,
          "cite": [
            "38 L. Ed. 2d 561",
            "94 S. Ct. 613",
            "414 U.S. 338",
            "1974 U.S. LEXIS 145",
            "66 Ohio Op. 2d 320"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ker v. California",
          "cluster_id": 106641,
          "cite": [
            "10 L. Ed. 2d 726",
            "83 S. Ct. 1623",
            "374 U.S. 23",
            "1963 U.S. LEXIS 2473",
            "24 Ohio Op. 2d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bumper v. North Carolina",
          "cluster_id": 107716,
          "cite": [
            "20 L. Ed. 2d 797",
            "88 S. Ct. 1788",
            "391 U.S. 543",
            "1968 U.S. LEXIS 1470",
            "46 Ohio Op. 2d 382"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Elkins v. United States",
          "cluster_id": 106107,
          "cite": [
            "4 L. Ed. 2d 1669",
            "80 S. Ct. 1437",
            "364 U.S. 206",
            "1960 U.S. LEXIS 1989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106022) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzI0MzM5MjAwMDAwJnM9NjE5MzM0JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106022%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(106022)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjMyJnM9MTA4NzYwJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106022%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106022)",
        "reviewed": 33,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 33,
        "triage_read": 0,
        "triage_snippet_classified": 33
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106022)",
    "indexed_citing_opinions": 3331,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106022,
        "count": 3331,
        "count_source": "search"
      }
    ],
    "citation_count": 4796,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/jones-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2NTk5MDMmcz05NDczODA1JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106022%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106022,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 96569,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 101148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 101963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 105837,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 226671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 230030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 231127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 233225,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 235396,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 243012,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 246901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 1471426,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 1473427,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 1477422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 1480436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 1504217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 1507600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 1507641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 1550051,
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
    "date_created": "2026-07-05T08:59:23Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: overruled -> superseded",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:59:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:59:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:31Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:59:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Jones v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b316-7">
  Mr. Justice Frankfurter
 </author>
<p id="AJs">
  delivered the opinion of the Court.
 </p>
<p id="b316-8">
  This is a prosecution for violation of federal narcotics laws. In the first count of a two-count indictment petitioner was charged with having “purchased, sold, dispensed and distributed” narcotics in violation of <span class="citation no-link">26 U. S. C. § 4704</span> (a), that is, not in or from the “original stamped package.” In the second count petitioner was charged under <span class="citation no-link">21 U. S. C. § 174</span> with having “facilitated the concealment and sale of” the same narcotics, knowing them to have been imported illegally into the United States. Petitioner was found guilty on both counts and sentenced to seven years’ imprisonment. The Court of Appeals, one judge dissenting, affirmed the conviction. 104 U. S. App. D. C. 345, <span class="citation" data-id="9446541"><a href="/opinion/246901/cecil-jones-v-united-states/" aria-description="Citation for case: Cecil Jones v. United States">262 F. 2d 234</a></span>. Since the case presented important questions in the administration of criminal justice, more particularly a defendant’s standing to challenge the legality of a search in the circumstances of this case, as well as the legality of the particular search should standing be established, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./359/988/">359 U. S. 988</a></span>.
 </p>
<p id="b316-9">
  Both statutory provisions under which petitioner was prosecuted permit conviction upon proof of the defendant’s possession of narcotics, and in the case of <span class="citation no-link">26 U. S. C. § 4704</span> (a) of the absence of the appropriate stamps. Possession was the basis of the Government’s case against petitioner. The evidence against him may be briefly summarized. He was arrested in an apartment in the District of Columbia by federal narcotics officers, who
  <span citation-index="1" class="star-pagination" label="259"> 
   *259
   </span>
  were executing a warrant to search for narcotics. Those officers found narcotics, without appropriate stamps, and narcotics paraphernalia in a bird’s nest in an awning just outside a window in the apartment. Another officer, stationed outside the building, had a short time before seen petitioner put his hand on the awning. Upon the discovery of the narcotics and the paraphernalia petitioner had admitted to the officers that some of these were his and that he was living in the apartment.
 </p>
<p id="b317-5">
  Prior to trial petitioner duly moved to suppress the evidence obtained through the execution of the search warrant on the ground that the warrant had been issued without a showing of probable cause. The Government challenged petitioner’s standing to make this motion because petitioner alleged neither ownership of the seized articles nor an interest in the apartment greater than that of an “invitee or guest.” The District Court agreed to take evidence on the issue of petitioner’s standing. Only petitioner gave evidence. On direct examination he testified that the apartment belonged to a friend, Evans, who had given him the use of it, and a key, with which petitioner had admitted himself on the day of the arrest. On cross-examination petitioner testified that he had a suit and shirt at the apartment, that his home was elsewhere, that he paid nothing for the use of the apartment, that Evans had let him use it “as a friend,” that he had slept there “maybe a night,” and that at the time of the search Evans had been away in Philadelphia for about five days.
 </p>
<p id="b317-6">
  Solely on the basis of petitioner’s lack of standing to make it, the district judge denied petitioner’s motion to suppress. When the case came on for trial before a different judge, the motion to suppress was renewed and was denied on the basis of the prior ruling. An unsuccessful objection was made when the seized items were offered in evidence at the trial.
 </p>
<p id="b318-3">
<span citation-index="1" class="star-pagination" label="260"> 
   *260
   </span>
  In affirming petitioner’s conviction the Court of Appeals agreed with the District Court that petitioner lacked standing, but proceeded to rule that even if it were to find that petitioner had standing, it would hold the evidence to have been- lawfully received. A challenge to the search which petitioner had not made in the District Court, namely, that the method of executing the warrant had been illegal, was considered by the Court of Appeals and rejected, while the contention petitioner had made below, that there had been insufficient cause to issue the warrant, was rejected without discussion.
 </p>
<p id="b318-4">
  The issue of petitioner’s standing is to be decided with reference to Rule 41 (e) of the Federal Rules of Criminal Procedure. This is a statutory direction governing the suppression of evidence acquired in violation of the conditions validating a search. It is desirable to set forth the Rule.
 </p>
<blockquote id="b318-5">
  “A person aggrieved by an unlawful search and seizure may move the district court for the district in which the property was seized for the return of the property and to suppress for use as evidence anything so obtained on the ground that (1) the property was illegally seized without warrant, or (2) the warrant is insufficient on its face, or (3) the property seized is not that described in the warrant, or (4) there was not probable cause for believing the existence of the grounds on which the warrant was issued, or (5) the warrant was illegally executed. The judge shall receive evidence on any issue of fact necessary to the decision of the motion. If the motion is granted the property shall be restored unless otherwise subject to lawful detention and it shall not be admissible in evidence at any hearing or trial. The motion to suppress evidence may also be made in the district where the trial is to be had. The motion shall be made before trial or hearing unless opportunity
  <span citation-index="1" class="star-pagination" label="261"> 
   *261
   </span>
  therefor did not exist or the defendant was not aware of the grounds for the motion, but the court in its discretion may entertain the motion at the trial or hearing.”
 </blockquote>
<p id="b319-5">
  In order to qualify as a “person aggrieved by an unlawful search and seizure” one must have been a victim of a search or seizure, one against whom the search was directed, as distinguished from one who claims prejudice only through the use of evidence gathered as a consequence of a search or seizure directed at someone else. Rule 41 (e) applies the general principle that a party will not be heard to claim a constitutional protection, unless he “belongs to the class for whose sake the constitutional protection is given.”
  <em>
   Hatch
  </em>
  v.
  <em>
   Reardon,
  </em>
  <span class="citation" data-id="96569"><a href="/opinion/96569/new-york-ex-rel-hatch-v-reardon/#160" aria-description="Citation for case: New York Ex Rel. Hatch v. Reardon">204 U. S. 152, 160</a></span>. The restrictions upon searches and seizures were obviously designed for protection against official invasion of privacy and the security of property. They are not exclusionary provisions against the admission of kinds of evidence deemed inherently unreliable or prejudicial. The exclusion in federal trials of evidence otherwise competent but gathered by federal officials in violation of the Fourth Amendment is a means for making effective the protection of privacy.
 </p>
<p id="b319-6">
  Ordinarily, then, it is entirely proper to require of one who seeks to challenge the legality of a search as the basis for suppressing relevant evidence that he allege, and if the allegation be disputed that he establish, that he himself was the victim of an invasion of privacy. But prosecutions like this one have presented a special problem. To establish “standing,” Courts of Appeals have generally required that the movant claim either to have owned or possessed the seized property or to have had a substantial possessory interest in the premises searched. Since narcotics charges like those in the present indictment may be established through proof solely of possession of narcotics, a defendant seeking to comply with what has
  <span citation-index="1" class="star-pagination" label="262"> 
   *262
   </span>
  been the conventional standing requirement has been forced to allege facts the proof of which would tend, if indeed not be sufficient, to convict him. At the least, such a defendant has been placed in the criminally tendentious position of explaining his possession of the premises. He has been faced, not only with the chance that the allegations made on the motion to suppress may be used against him at the trial, although that they may is by no means an inevitable holding, but also with the encouragement that he perjure himself if he seeks to establish “standing” while maintaining a defense to the charge of possession.
 </p>
<p id="b320-4">
  The dilemma that has thus been created for defendants in cases like this has been pointedly put by Judge Learned Hand:
 </p>
<blockquote id="b320-5">
  “Men may wince at admitting that they were the owners, or in possession, of contraband property; may wish at once to secure the remedies of a possessor, and avoid the perils of the part; but equivocation will not serve. If they come as victims, they must take on that role, with enough detail to cast them without question. The petitioners at bar shrank from that predicament; but they were obliged to choose one horn of the dilemma.”
  <em>
   Connolly
  </em>
  v.
  <em>
   Medalie,
  </em>
  <span class="citation" data-id="1504217"><a href="/opinion/1504217/connolly-v-medalie/#630" aria-description="Citation for case: Connolly v. Medalie">58 F. 2d 629, 630</a></span>.
 </blockquote>
<p id="b320-6">
  Following this holding, several Courts of Appeals have pinioned a defendant within this dilemma. See, e.
  <em>
   g., Scoggins
  </em>
  v.
  <em>
   United States,
  </em>
  92 U. S. App. D. C. 29-30, <span class="citation" data-id="231127"><a href="/opinion/231127/scoggins-v-united-states/#212" aria-description="Citation for case: Scoggins v. United States">202 F. 2d 211, 212</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Eversole,
  </em>
  <span class="citation" data-id="233225"><a href="/opinion/233225/united-states-v-eversole/#768" aria-description="Citation for case: United States v. Eversole">209 F. 2d 766, 768</a></span>;
  <em>
   Accardo
  </em>
  v.
  <em>
   United States,
  </em>
  101 U. S. App. D. C. 162, 163-164, <span class="citation" data-id="243012"><a href="/opinion/243012/anthony-m-accardo-v-united-states/#569" aria-description="Citation for case: Anthony M. Accardo v. United States">247 F. 2d 568, 569-570</a></span>;
  <em>
   Grainger
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="1473427"><a href="/opinion/1473427/grainger-v-united-states/" aria-description="Citation for case: Grainger v. United States">158 F. 2d 236</a></span>. A District Court has held otherwise.
  <em>
   United States
  </em>
  v.
  <em>
   Dean,
  </em>
  <span class="citation" data-id="6846493"><a href="/opinion/6949464/united-states-v-dean/#906" aria-description="Citation for case: United States v. Dean">50 F. 2d 905, 906</a></span> (D. C. Mass.). The Government urges us to follow the body of Court of Appeals’ decisions and to rule that the lower
  <span citation-index="1" class="star-pagination" label="263"> 
   *263
   </span>
  courts, including the courts below, have been right in barring a defendant in a case like this from challenging a search because of his failure, when making his motion to suppress, to allege either that he owned or possessed the property seized or that he had a possessory interest in the premises searched greater than the interest of an “invitee or guest.”
 </p>
<p id="b321-5">
  Judge Hand’s dilemma is not inescapable. It presupposes requirements of “standing” which we do not find compelling. Two separate lines of thought effectively sustain defendant’s standing in this case. (1) The same element in this prosecution which has caused a dilemma,
  <em>
   i. e.,
  </em>
  that possession both convicts and confers standing, eliminates any necessity for a preliminary showing of an interest in the premises searched or the property seized, which ordinarily is required when standing is challenged. (2) Even were this not a prosecution turning on illicit possession, the legally requisite interest in the premises was here satisfied, for it need not be as extensive a property interest as was required by the courts below.
 </p>
<p id="b321-6">
  As to the first ground, we are persuaded by this consideration : to hold to the contrary, that is, to hold that petitioner’s failure to acknowledge interest in the narcotics or the premises prevented his attack upon the search, would be to permit the Government to have the advantage of contradictory positions as a basis for conviction. Petitioner’s conviction flows from his possession of the narcotics at the time of the search. Yet the fruits of that search, upon which the conviction depends, were admitted into evidence on the ground that petitioner did not have possession of the narcotics at that time. The prosecution here thus subjected the defendant to the penalties meted out to one in lawless possession while refusing him the remedies designed for one in that situation. It is not consonant. with the amenities, to put it mildly, of the administration of criminal justice to sanction
  <span citation-index="1" class="star-pagination" label="264"> 
   *264
   </span>
  such squarely contradictory assertions of power by the Government. The possession on the basis of which petitioner is to be and was convicted suffices to give him standing under any fair and rational conception of the requirements of Rule 41 (e).
 </p>
<p id="b322-5">
  The Government’s argument to the contrary essentially invokes
  <em>
   elegantia juris.
  </em>
  In the interest of normal procedural orderliness, a motion to suppress, under Rule 41 (e),.must be made prior to trial, if the defendant then has knowledge of the grounds on which to base the motion. The Government argues that the defendant therefore must establish his standing to suppress the evidence at that time through affirmative allegations and may not wait to rest standing upon the Government’s case at the trial. This provision of Rule 41 (e), requiring the motion to suppress to be made before trial, is a crystallization of decisions of this Court requiring that procedure, and is designed to eliminate from the trial disputes over police conduct not immediately relevant to the question of guilt. See
  <em>
   Nardone
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341-342</a></span>;
  <em>
   Segurola
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="101148"><a href="/opinion/101148/segurola-v-united-states/" aria-description="Citation for case: Segurola v. United States">275 U. S. 106</a></span>, 111—112;
  <em>
   Agnello
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#34" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 34</a></span>;
  <em>
   Adams
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U. S. 585</a></span>. As codified, the rule is not a rigid one, for under Rule 41 (e)' “the court in its discretion may entertain the motion [to suppress] at the trial or hearing.” This qualification proves that we are dealing with carrying out an important social policy and not a narrow, finicky procedural requirement. This underlying policy likewise precludes application of the Rule so as to compel the injustice of an internally inconsistent conviction. In cases where the indictment itself charges possession, the defendant in a very real sense is revealed as a “person aggrieved by an unlawful search and seizure” upon a motion to suppress evidence prior to trial. Rule 41 (e) should not be applied to allow the Government to deprive the defendant of standing to bring a motion
  <span citation-index="1" class="star-pagination" label="265"> 
   *265
   </span>
  to suppress by framing the indictment in general terms, while prosecuting for possession.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
</p>
<p id="b323-5">
  As a second ground sustaining “standing” here we hold that petitioner’s testimony on the motion to suppress made out a sufficient interest in the premises to establish him as a “person aggrieved” by their search. That testimony established that at the time of the search petitioner was present in the apartment with the permission of Evans, whose apartment it was. The Government asserts that such an interest is insufficient to give standing. The Government does not contend that only ownership of the premises may confer standing. It would draw distinctions among various classes of possessors, deeming some, such as “guests” and “invitees” with only the “use” of the premises, to have too “tenuous” an interest although concededly having “some measure of control” through their “temporary presence,” while conceding that others, who in a “realistic sense, have dominion of the apartment” or who are “domiciled” there, have standing. Petitioner, it is insisted, by his own testimony falls in the former class.
 </p>
<p id="b323-6">
  While this Court has never passed upon the interest in the searched premises necessary to maintain a motion to suppress, the Government’s argument closely follows the prevailing view in the lower courts. They have denied standing to “guests” and “invitees” (e.
  <em>
   g., Gaskins
  </em>
  v.
  <em>
   United States,
  </em>
  95 U. S. App. D. C. 34, 35, <span class="citation" data-id="235396"><a href="/opinion/235396/ola-mary-gaskins-v-united-states/#48" aria-description="Citation for case: Ola Mary Gaskins v. United States">218 F. 2d 47, 48</a></span>;
  <em>
   Gibson
  </em>
  v.
  <em>
   United States,
  </em>
  80 U. S. App. D. C. 81, 84, <span class="citation" data-id="1507641"><a href="/opinion/1507641/gibson-v-united-states/#384" aria-description="Citation for case: Gibson v. United States">149 F. 2d 381, 384</a></span>;
  <em>
   In re Nassetta,
  </em>
  <span class="citation" data-id="1477422"><a href="/opinion/1477422/in-re-nassetta/" aria-description="Citation for case: In Re Nassetta">125 F. 2d 924</a></span>;
  <em>
   Jones
  </em>
  v.
  <em>
   United States,
  </em>
  104 U. S. App. D. C. 345, <span class="citation" data-id="9446541"><a href="/opinion/246901/cecil-jones-v-united-states/" aria-description="Citation for case: Cecil Jones v. United States">262 F. 2d 234</a></span>),
  <span citation-index="1" class="star-pagination" label="266"> 
   *266
   </span>
  and employees, who though in “control” or “occupancy” lacked “possession”
  <em>
   (e. g., Connolly
  </em>
  v.
  <em>
   Medalie,
  </em>
  <span class="citation" data-id="1504217"><a href="/opinion/1504217/connolly-v-medalie/#630" aria-description="Citation for case: Connolly v. Medalie">58 F. 2d 629, 630</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Conoscente,
  </em>
  <span class="citation" data-id="1480436"><a href="/opinion/1480436/united-states-v-conoscente/" aria-description="Citation for case: United States v. Conoscente">63 F. 2d 811</a></span>). The necessary quantum of interest has been distinguished as being, variously, “ownership in or right to possession of the premises”
  <em>
   (e. g., Jeffers
  </em>
  v.
  <em>
   United States,
  </em>
  88 U. S. App. D. C. 58, 61, <span class="citation" data-id="9442748"><a href="/opinion/226671/jeffers-v-united-states/#501" aria-description="Citation for case: Jeffers v. United States">187 F. 2d 498, 501</a></span>, affirmed,
  <em>
   Jeffers
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span>), the interest of a “lessee or licensee”
  <em>
   (United States
  </em>
  v.
  <em>
   De Bousi,
  </em>
  <span class="citation" data-id="1550051"><a href="/opinion/1550051/united-states-v-de-bousi/" aria-description="Citation for case: United States v. De Bousi">32 F. 2d 902</a></span>), or of one with “dominion”
  <em>
   (McMillan
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="1471426"><a href="/opinion/1471426/mcmillan-v-united-states/#60" aria-description="Citation for case: McMillan v. United States">26 F. 2d 58, 60</a></span>;
  <em>
   Steeber
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="230030"><a href="/opinion/230030/steeber-v-united-states/#617" aria-description="Citation for case: Steeber v. United States">198 F. 2d 615, 617</a></span>). We do not lightly depart from this course of decisions by the lower courts. We are persuaded, however, that it is unnecessary and ill-advised to import into the law surrounding the constitutional right to be free from unreasonable searches and seizures subtle distinctions, developed and refined by the common law in evolving the body of private property law which, more than almost any other branch of law, has been shaped by distinctions whose validity is largely historical. Even in the area from which they derive, due consideration has led to the discarding of these distinctions in the homeland of the common law. See Occupiers’ Liability Act, 1957, 5 and 6 Eliz. 2, c. 31, carrying out Law Reform Committee, Third Report, Cmd. 9305. Distinctions such as those between “lessee,” “licensee,” “invitee” and “guest,” often only of gossamer strength, ought not to be determinative in fashioning procedures ultimately referable to constitutional safeguards.
 </p>
<p id="b324-6">
  We rejected such distinctions as inappropriate to the law of maritime torts in
  <em>
   Kermarec
  </em>
  v.
  <em>
   Compagnie Generate,
  </em>
  <span class="citation" data-id="105837"><a href="/opinion/105837/kermarec-v-compagnie-generale-transatlantique/#630" aria-description="Citation for case: Kermarec v. Compagnie Generale Transatlantique">358 U. S. 625, 630-632</a></span>. We found there to be a duty of ordinary care to one rightfully on the ship, regardless of whether he was a “licensee” rather than an “invitee.” “For the admiralty law at this late date to import such conceptual distinctions would be foreign to its traditions
  <span citation-index="1" class="star-pagination" label="267"> 
   *267
   </span>
  of simplicity and practicality.” <span class="citation" data-id="105837"><a href="/opinion/105837/kermarec-v-compagnie-generale-transatlantique/#631" aria-description="Citation for case: Kermarec v. Compagnie Generale Transatlantique">358 U. S., at 631</a></span>.
  <em>
   A forti-ori
  </em>
  we ought not to bow to them in the fair administration of the criminal law. To do so would not comport with our justly proud claim of the procedural protections accorded to those charged with crime. No just interest of the Government in the effective and rigorous enforcement of the criminal law will be hampered by recognizing that anyone legitimately on premises where a search occurs may challenge its legality by way of a motion to suppress, when its fruits are proposed to be used against him. This would of course not avail those who, by virtue of their wrongful presence, cannot invoke the privacy of the premises searched. As petitioner’s testimony established Evans’ consent to his presence in the apartment, he was entitled to have the merits of his motion to suppress adjudicated.
 </p>
<p id="b325-5">
  We come to consider the grounds upon which the search is alleged to have been illegal. The attack which was made in the District Court was one of lack of probable cause for issuing the search warrant. The question raised is whether sufficient evidence to establish probable cause to search was put before the Commissioner by the officer, Didone, who applied for the warrant. The sole evidence upon which the warrant was issued was an affidavit signed by Didone. Both parties urge us to decide the question here, without remanding it to the District Court which, because it found lack of standing, did not pass on it. We think it appropriate to decide the question.
 </p>
<p id="b325-6">
  The affidavit is set out in the margin.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  Didone was a member of the Narcotic Squad in the District of Columbia.
  <span citation-index="1" class="star-pagination" label="268"> 
   *268
   </span>
  His affidavit claimed no direct knowledge of the presence of narcotics in the apartment. He swore that on the day before making the affidavit he had been given information, by one unnamed, that petitioner and another “were involved in the illicit narcotic traffic” and “kept a ready supply of heroin on hand” in the apartment. He swore that his informant claimed to have purchased narcotics at the apartment from petitioner and another “on many occasions,” the last of which had been the day before the warrant was applied for. Didone swore that his informant “has given information to the undersigned on previous occasion and which was correct,” that “[t]his same
  <span citation-index="1" class="star-pagination" label="269"> 
   *269
   </span>
  information” regarding petitioner had been given the narcotic squad by “other sources of information” and that the petitioner and the other implicated by the informant had admitted being users of narcotics. On this basis Didone founded his oath that he believed “that there is now illicit narcotic drugs being secreated [sic] in the above apartment by Cecil Jones.”
 </p>
<p id="b327-5">
  This affidavit was, it is claimed, insufficient to establish probable cause because it did not set forth the affiant’s personal observations regarding the presence of narcotics in the apartment, but rested wholly on hearsay. We held in
  <em>
   Nathanson
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span>, that an affidavit does not establish probable cause which merely states the affiant’s belief that there is cause to search, without stating facts upon which that belief is based.
  <em>
   A fortiori
  </em>
  this is true of an affidavit which states only the belief of one not the affiant. That is not, however, this case. The question here is whether an affidavit which sets out personal observations relating to the existence of cause to search is to be deemed insufficient by virtue of the fact that it sets out not the affiant’s observations but those of another. An affidavit is not to be deemed insufficient on that score, so long as a substantial basis for crediting the hearsay is presented.
 </p>
<p id="b327-6">
  In testing the sufficiency of probable cause for an officer’s action even without a warrant, we have held that he may rely upon information received through an informant, rather than upon his direct observations, so long as the informant’s statement is reasonably corroborated by other matters within the officer’s knowledge.
  <em>
   Draper
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span>. We there upheld an arrest without a warrant solely upon an informant’s statement that the defendant was peddling narcotics, as corroborated by the fact that the informant’s description of the defendant’s appearance, and of where he would be on a given morning (matters in themselves totally
  <span citation-index="1" class="star-pagination" label="270"> 
   *270
   </span>
  innocuous) agreed with the officer’s observations. We rejected the contention that an officer may act without a warrant only when his basis for acting would be competent evidence upon a trial to prove defendant’s guilt. Quoting from
  <em>
   Brinegar
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#172" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 172</a></span>, we said that such a contention “goes much too far in-confusing and disregarding the difference between what is required to prove guilt in a criminal case and what is required to show probable cause for arrest or search. . . . There is a large difference between the two things to be proved [guilt and probable cause] . . . and therefore a like difference in the
  <em>
   quanta
  </em>
  and modes of proof required to establish them.” 358 U. S., at 311-312. The dictum to the contrary in
  <em>
   Grau
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="101963"><a href="/opinion/101963/grau-v-united-states/#128" aria-description="Citation for case: Grau v. United States">287 U. S. 124, 128</a></span>, was expressly rejected in
  <em>
   Draper.
  </em>
  <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#312" aria-description="Citation for case: Draper v. United States">358 U. S., at 312, n. 4</a></span>. See also Judge Learned Hand in.
  <em>
   United States
  </em>
  v.
  <em>
   Heitner,
  </em>
  <span class="citation" data-id="1507600"><a href="/opinion/1507600/united-states-v-heitner/#106" aria-description="Citation for case: United States v. Heitner">149 F. 2d 105, 106</a></span>.
 </p>
<p id="b328-6">
  What we have ruled in the case of an officer who acts without a warrant governs our decision here. If an officer may act upon probable cause without a warrant when the only incriminating evidence in his possession is hearsay, it would be incongruous to hold that such evidence presented in an affidavit is insufficient basis for a warrant. If evidence of a more judicially competent or persuasive character than would have justified an officer in acting on his own without a warrant must be presented when a warrant is sought, warrants could seldom legitimatize police conduct, and resort to them would ultimately be discouraged. Due regard for the safeguards governing arrests and searches counsels the contrary. In a doubtful case, when the officer does not have clearly convincing evidence of the immediate need to search, it is most important that resort be had to a warrant, so that the evidence in the possession of the police may be weighed by an independent judicial officer, whose decision, not that
  <span citation-index="1" class="star-pagination" label="271"> 
   *271
   </span>
  of the police, may govern whether liberty or privacy is to be invaded.
 </p>
<p id="b329-5">
  We conclude therefore that hearsay may be the basis for a warrant. We cannot say that there was so little basis for accepting the hearsay here that the Commissioner acted improperly. The Commissioner need not have been convinced of the presence of narcotics in the apartment. He might have found the affidavit insufficient and withheld his warrant. But there was substantial basis for him to conclude that narcotics were probably present in the apartment, and that is sufficient. It is not suggested that the Commissioner doubted Didone’s word. Thus we may assume that Didone had the day before been told, by one who claimed to have bought narcotics there, that petitioner was selling narcotics in the apartment. Had that been all, it might not have been enough; but Didone swore to a basis for accepting the informant’s story. The informant had previously given accurate information. His story was corroborated by other sources of information. And petitioner was known by the police to be a user of narcotics. Corroboration through other sources of information reduced the chances of a reckless or prevaricating tale; that petitioner was a known user of narcotics made the charge against him much less subject to scepticism than would be such a charge against one without such a history.
 </p>
<p id="b329-6">
  Petitioner argues that the warrant was defective because Didone’s informants were not produced, because his affidavit did not even state their names, and Didone did not undertake and swear to the results of his own independent investigation of the claims made by his informants. If the objections raised were that Didone had misrepresented to the Commissioner his basis for seeking a warrant, these matters might be relevant. Such a charge is not made. All we are here asked to decide is
  <span citation-index="1" class="star-pagination" label="272"> 
   *272
   </span>
  whether the Commissioner acted properly, not whether Didone did. We have decided that, as hearsay alone does not render an affidavit insufficient, the Commissioner need not have required the informants or their affidavits to be produced, or that Didone have personally made inquiries about the apartment, so long as there was a substantial basis for crediting the hearsay.
 </p>
<p id="b330-5">
  In the Court of Appeals petitioner presented an additional attack upon the legality of the search, namely, that the warrant was not executed in conformity with <span class="citation no-link">18 U. S. C. § 3109</span>.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  Since petitioner did not, with ample opportunity to do so, make this claim in the District Court, we should not ordinarily consider it here had the Court of Appeals refused for that reason to entertain it. The Court of Appeals, however, fully considered the claim and rejected it; nor does the Government contend that it is not properly before us. In these circumstances we hold that the question of the legality of the execution of the search warrant under <span class="citation no-link">18 U. S. C. § 3109</span> is open for our decision.
 </p>
<p id="b330-6">
  Unlike the claim of lack of probable cause, this contention is not one which can satisfactorily be resolved upon the record before us. As
  <em>
   Miller
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">357 U. S. 301</a></span>, demonstrated, a claim under <span class="citation no-link">18 U. S. C. § 3109</span> depends upon the particular circumstances surrounding the execution of the warrant. The trial revealed a direct conflict in testimony on this matter. We cannot yield to the Government’s suggestion that we ignore that conflict and consider the question on the version of the warrant's execution given at the trial most favorable to the prosecution. We therefore vacate the
  <span citation-index="1" class="star-pagination" label="273"> 
   *273
   </span>
  decision of the Court of Appeals and remand the case to the District Court to consider petitioner’s contention under <span class="citation no-link">18 U. S. C. § 3109</span>, in light of our decision that petitioner had standing to make it.
 </p>
<p id="b331-5">
<em>
   Vacated and remanded.
  </em>
</p>
<author id="b331-6">
  Mr. Justice Douglas.
 </author>
<p id="b331-7">
  I join the part of the opinion which holds that petitioner had “standing” to challenge the legality of the search. But I dissent from the ruling that there was “probable cause” for issuance of the warrant. The view that there was “probable cause” finds some support in
  <em>
   Draper
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span>. But my dissent in
  <em>
   <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span>
  </em>
  gives, I think, the true dimensions of the problem. This is an age where faceless informers have been reintroduced into our society in alarming ways. Sometimes their anonymity is defended on the ground that revelation of their names would ruin counter-espionage or cripple an underground network of agents. Yet I think in these Fourth Amendment cases the duty of the magistrate is nondelegable. It is not sufficient that the police think there is cause for an invasion of the privacy of the home. The judicial officer must also be convinced; and to him the police must go except for emergency situations. The magistrate should know the evidence on which the police propose to act. Unless that is the requirement, unless the magistrate makes his independent judgment on all the known facts, then he tends to become merely the tool of police interests. Though the police are honest and their aims worthy, history shows they are not appropriate guardians of the privacy which the Fourth Amendment protects.
 </p>



<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b323-7">
   Ordinarily the Government should choose between opposing a motion to suppress made before trial and basing the case upon possession, but if necessary the District Court’s discretion to hear the motion to suppress during trial may be invoked. The Government must, in any case, not permit a conviction to be obtained on the basis of possession, without the merits of a duly made motion to suppress having been considered.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b325-7">
   “Affidavit in Support of a U. S. Commissioners Search Warrant for Premises 1436 Meridian Place, N. W., Washington, D. C., apartment 36, including window spaces of said apartment. Occupied by Cecil Jones and Earline Richardson.
  </p>
<p id="b325-8">
   “In the late afternoon of Tuesday, August 20, 1957, I, Detective Thomas Didone, Jr. received information that Cecil Jones and Earline
   <span citation-index="1" class="star-pagination" label="268"> 
    *268
    </span>
   Richardson were involved in the illicit narcotic traffic and that they kept a ready supply of heroin on hand in the above mentioned apartment. The source of information also relates that the two aforementioned persons kept these same narcotics either on their person, under a pillow, on a dresser or on a window ledge in said apartment. The source of information goes on to relate that on many occasions the source of information has gone to said apartment and purchased narcotic drugs from the above mentioned persons and that the narcotics were secreated [sic] in the above mentioned places. The last time being August 20, 1967.
  </p>
<p id="b326-7">
   “Both the aforementioned persons are familiar to the undersigned and other members of the Narcotic Squad. Both have admitted to the use of narcotic drugs and display needle marks as evidence of same.
  </p>
<p id="b326-8">
   “This same information, regarding the illicit narcotic traffic, conducted by Cecil Jones and Earline Richardson, has been given to the undersigned and to other officers of the narcotic squad by other sources of information.
  </p>
<p id="b326-9">
   “Because the source of information mentioned in the opening paragraph has given information to the undersigned on previous occasion and which was correct, and because this same information is given by other sources does believe that there is now illicit narcotic drugs being secreated [sic] in the above apartment by Cecil Jones and Earline Richardson.
  </p>
<p id="b326-10">
   “Det. Thomas Didone, Jr., Narcotic Squad, MPDC.
  </p>
<p id="b326-11">
   “Subscribed and sworn to before me this 21 day of August, 1957.
  </p>
<p id="b326-12">
   “James F. Splain, TJ. S. Commissioner, D. C.”
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b330-7">
   “The officer may break open any outer or inner door or window of a house, or any part of a house, or anything therein, to execute a search warrant, if, after notice of his authority and purpose, he is refused admittance or when necessary to liberate himself or a person aiding him in the execution of the warrant.”
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Mathis v. United States (1968).md  (`case`, 6 assertions)

### content_page

```
---
title: "Mathis v. United States (1968)"
type: case
citation: "391 U.S. 1 (1968)"
parallel_cite: "88 S. Ct. 1503; 20 L. Ed. 2d 381; 2 C.B. 903; 21 A.F.T.R.2d (RIA) 1251"
neutral_cite: 1968 U.S. LEXIS 3108
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1968
date_decided: 1968-05-06
docket: 726
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 1968-05-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "Mathis v. United States (1968)"
  varies_by_point: true
  scope_note: "Holding stands: Miranda is not lost because in-custody questioning concerns a separate/unrelated matter (here, an IRS interview of a state prisoner). But the broad reading that incarceration itself is always Miranda 'custody' was rejected/limited by Howes v. Fields, 565 U.S. 499 (2012) — prison questioning now takes a totality-of-circumstances custody analysis."
  point_overrides:
    - point: legacy-limited-mathis-v-united-states-1968
      point_label: Legacy limited treatment point
      field_i_validity: caution
      as_of_treatment: 2026-06-30
      s3_binding_status: provisional
      by:
        - name: Howes v. Fields
          cluster_id: 623144
          cite: 565 U.S. 499
          field_ii: limited
      scope_note: "Holding stands: Miranda is not lost because in-custody questioning concerns a separate/unrelated matter (here, an IRS interview of a state prisoner). But the broad reading that incarceration itself is always Miranda 'custody' was rejected/limited by Howes v. Fields, 565 U.S. 499 (2012) — prison questioning now takes a totality-of-circumstances custody analysis."
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107676/mathis-v-united-states/"
  cluster_id: 107676
  opinion_id: 9423682
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[Howes v. Fields]]", "[[Orozco v. Texas]]", "[[Beckwith v. United States]]"]
aliases: ["Mathis v. United States"]
tags: ["case", "fifth-amendment", "miranda", "custody", "prison-inmate", "irs"]
holding: "Miranda warnings are required when a person already in custody (here, serving a prison sentence) is interrogated by officers, even though the questioning concerns an entirely separate matter and even though it is a routine tax investigation; the reason the person is in custody does not curtail the warnings."
lake:
  record_id: "Mathis v. United States (1968)"
  status: under_review
  projected_at: 2026-07-06
---

# Mathis v. United States (1968)

*391 U.S. 1 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)* — by [[Howes v. Fields]]
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
While Mathis was serving a state sentence in prison, a federal revenue agent interviewed him about his individual income-tax returns, obtaining documents and oral statements without giving any [[Miranda and Custodial Interrogation|Miranda warnings]]. Those statements were later used to convict him in federal court of knowingly filing false claims for tax refunds. At trial he sought, unsuccessfully, to suppress the statements under [[Miranda v. Arizona]]; the District Court and Fifth Circuit rejected the claim.

## Issue
Whether [[Miranda and Custodial Interrogation|Miranda warnings]] were required before a revenue agent questioned a person who was already in custody — serving a sentence for a separate offense — in the course of a tax investigation.

## Rule
Yes. The Court rejected the Government's two distinctions. "The Government here seeks to escape application of the *Miranda* warnings on two arguments: (1) that these questions were asked as a part of a routine tax investigation . . . and (2) that the petitioner had not been put in jail by the officers questioning him, but was there for an entirely separate offense. These differences are too minor and shadowy to justify a departure from the well-considered conclusions of *Miranda* with reference to warnings to be given to a person held in custody." — 391 U.S. at 4. ^pin-4

The reason for custody is irrelevant: "There is no substance to such a distinction . . . . We find nothing in the *Miranda* opinion which calls for a curtailment of the warnings to be given persons under interrogation by officers based on the reason why the person is in custody." — *Id.* at 4–5. ^pin-5

## Application
Mathis was indisputably "in custody" — he was serving a prison sentence — and the revenue agent's questioning produced strongly incriminating statements used against him. That the questioning arose from a "routine tax investigation" did not exempt it (tax investigations frequently become criminal prosecutions, as this one did), and that he was imprisoned for a different offense did not remove Miranda's protection. Because no warnings were given, the statements were inadmissible and the conviction had to be reversed.

## Conclusion
Miranda applied to the custodial interrogation; the failure to warn required reversal. The judgment of the Court of Appeals was reversed.

## Treatment & subsequent history
- **Status:** limited *(as of 2026-06-30)* — **Binding — SCOTUS**; **limited by** [[Howes v. Fields]].
- *Mathis*'s core holding remains good law: a person already in custody does not lose Miranda's protection because the questioning concerns a *separate* matter. But the broad reading that **incarceration itself always constitutes Miranda "custody"** was **rejected/limited** in [[Howes v. Fields]], 565 U.S. 499 (2012), which holds that questioning an inmate requires a totality-of-circumstances custody analysis (imprisonment alone is not enough). The custody-not-focus principle was also developed in [[Beckwith v. United States]], and the in-home custody analog appears in [[Orozco v. Texas]].

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Mathis v. United States*, 391 U.S. 1 (1968) — https://www.courtlistener.com/opinion/107676/mathis-v-united-states/ — pinpoints: 4, 5.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a5ce74f91f1279ff", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "391 U.S. 1 (1968)", "court": "U.S. Supreme Court", "neutral_cite": "1968 U.S. LEXIS 3108", "official_citation_present": true, "parallel_cite": "88 S. Ct. 1503; 20 L. Ed. 2d 381; 2 C.B. 903; 21 A.F.T.R.2d (RIA) 1251", "title": "Mathis v. United States (1968)", "year": "1968"}}
{"assertion_id": "1488f53847e1dd0b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Miranda warnings are required when a person already in custody (here, serving a prison sentence) is interrogated by officers, even though the questioning concerns an entirely separate matter and even though it is a routine tax investigation; the reason the person is in custody does not curtail the warnings.", "title": "Mathis v. United States (1968)"}}
{"assertion_id": "e4ffd8a7a4636ba9", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key — Progeny / Refinement", "title": "Mathis v. United States (1968)"}}
{"assertion_id": "1ec2bf6842363815", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Mathis v. United States (1968)"}}
{"assertion_id": "4fc11cf6d3c4c9ae", "dimension": "treatment", "kind": "treatment_override", "locator": {"point": "legacy-limited-mathis-v-united-states-1968"}, "payload": {"by": [{"cite": "565 U.S. 499", "cluster_id": "623144", "field_ii": "limited", "name": "Howes v. Fields"}], "field_i_validity": "caution", "point": "legacy-limited-mathis-v-united-states-1968", "point_label": "Legacy limited treatment point", "s3_binding_status": "provisional", "title": "Mathis v. United States (1968)"}}
{"assertion_id": "b4b33fdebf54750c", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1968-05-06", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Mathis v. United States (1968)", "field_i_validity": "caution", "scope_note": "Holding stands: Miranda is not lost because in-custody questioning concerns a separate/unrelated matter (here, an IRS interview of a state prisoner). But the broad reading that incarceration itself is always Miranda 'custody' was rejected/limited by Howes v. Fields, 565 U.S. 499 (2012) — prison questioning now takes a totality-of-circumstances custody analysis.", "title": "Mathis v. United States (1968)", "varies_by_point": "true"}}
```

### lake record — Mathis v. United States (1968)

```json
{
  "schema_version": "s2.v1",
  "record_id": "Mathis v. United States (1968)",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Mathis v. United States",
    "case_name_short": "Mathis",
    "case_name_full": "Mathis v. United States",
    "input_case_name": "Mathis v. United States (1968)",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-05-06",
    "year": 1968,
    "docket": "726",
    "cluster_id": 107676,
    "lead_opinion_id": 9423682,
    "sibling_ids": [
      107676,
      9423682,
      9423683
    ],
    "absolute_url": "/opinion/107676/mathis-v-united-states/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "391 U.S. 1",
      "volume": "391",
      "reporter": "U.S.",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "88 S. Ct. 1503",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1503",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 381",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "381",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2 C.B. 903",
        "volume": "2",
        "reporter": "C.B.",
        "page": "903",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "21 A.F.T.R.2d (RIA) 1251",
        "volume": "21",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1251",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1968 U.S. LEXIS 3108",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "3108",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "391 U.S. 1",
        "volume": "391",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 1503",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1503",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 381",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "381",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1968 U.S. LEXIS 3108",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "3108",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2 C.B. 903",
        "volume": "2",
        "reporter": "C.B.",
        "page": "903",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "21 A.F.T.R.2d (RIA) 1251",
        "volume": "21",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1251",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "391 U.S. 1",
    "official_selection": {
      "court_class": "scotus",
      "selected": "391 U.S. 1",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-4",
      "page": null,
      "quote": "--- # Mathis v. United States (1968) *391 U.S. 1 (1968)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **limited** *(as of 2026-06-30)* \u2014 by [[Howes v. Fields]] <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background While Mathis was serving a state sentence in prison, a federal revenue agent interviewed him about his individual income-tax returns, obtaining documents and oral statements without giving any Miranda warnings. Those statements were later used to convict him in federal court of knowingly filing false claims for tax refunds. At trial he sought, unsuccessfully, to suppress the statements under [[Miranda v. Arizona]]; the District Court and Fifth Circuit rejected the claim. ## Issue Whether Miranda warnings were required before a revenue agent questioned a person who was already in custody \u2014 serving a sentence for a separate offense \u2014 in the course of a tax investigation. ## Rule Yes. The Court rejected the Government's two distinctions.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-5",
      "page": null,
      "quote": "There is no substance to such a distinction . . . . We find nothing in the *Miranda* opinion which calls for a curtailment of the warnings to be given persons under interrogation by officers based on the reason why the person is in custody.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "1968-05-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Mathis v. United States (1968)",
    "varies_by_point": true,
    "scope_note": "Holding stands: Miranda is not lost because in-custody questioning concerns a separate/unrelated matter (here, an IRS interview of a state prisoner). But the broad reading that incarceration itself is always Miranda 'custody' was rejected/limited by Howes v. Fields, 565 U.S. 499 (2012) \u2014 prison questioning now takes a totality-of-circumstances custody analysis.",
    "point_overrides": [
      {
        "point": "legacy-limited-mathis-v-united-states-1968",
        "point_label": "Legacy limited treatment point",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "provisional",
        "by": [
          {
            "name": "Howes v. Fields",
            "cluster_id": 623144,
            "cite": "565 U.S. 499",
            "field_ii": "limited"
          }
        ],
        "scope_note": "Holding stands: Miranda is not lost because in-custody questioning concerns a separate/unrelated matter (here, an IRS interview of a state prisoner). But the broad reading that incarceration itself is always Miranda 'custody' was rejected/limited by Howes v. Fields, 565 U.S. 499 (2012) \u2014 prison questioning now takes a totality-of-circumstances custody analysis."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "Howes v. Fields",
          "cluster_id": 623144,
          "cite": "565 U.S. 499",
          "field_ii": "limited"
        },
        "field_ii": "limited",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:limited"
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
        "journal_ref": "Mathis v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Ledbetter",
          "cluster_id": 6294956,
          "cite": [
            "47 Misc. 3d 336",
            "998 N.Y.S.2d 286"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Passino",
          "cluster_id": 5899747,
          "cite": [
            "53 A.D.3d 204",
            "861 N.Y.S.2d 168"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wilkerson, Ray Mitchell",
          "cluster_id": 2936737,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Harper",
          "cluster_id": 2382899,
          "cite": [
            "613 A.2d 945",
            "1992 Me. LEXIS 202"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States of America David E. Mitchell, Revenue Office of the Internal Revenue Service v. Roger L. Sharp",
          "cluster_id": 552785,
          "cite": [
            "920 F.2d 1167"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ingersoll v. Palmer",
          "cluster_id": 2604190,
          "cite": [
            "743 P.2d 1299",
            "43 Cal. 3d 1321",
            "241 Cal. Rptr. 42",
            "1987 Cal. LEXIS 451"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Larson",
          "cluster_id": 2080732,
          "cite": [
            "346 N.W.2d 199",
            "1984 Minn. App. LEXIS 3051"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Falby",
          "cluster_id": 2380627,
          "cite": [
            "187 Conn. 6",
            "444 A.2d 213",
            "1982 Conn. LEXIS 499"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Berkemer v. McCarty",
          "cluster_id": 111249,
          "cite": [
            "82 L. Ed. 2d 317",
            "104 S. Ct. 3138",
            "468 U.S. 420",
            "1984 U.S. LEXIS 140",
            "52 U.S.L.W. 5023"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Mathiason",
          "cluster_id": 109587,
          "cite": [
            "50 L. Ed. 2d 714",
            "97 S. Ct. 711",
            "429 U.S. 492",
            "1977 U.S. LEXIS 38"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baxter v. Palmigiano",
          "cluster_id": 109429,
          "cite": [
            "47 L. Ed. 2d 810",
            "96 S. Ct. 1551",
            "425 U.S. 308",
            "1976 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Quarles",
          "cluster_id": 111214,
          "cite": [
            "81 L. Ed. 2d 550",
            "104 S. Ct. 2626",
            "467 U.S. 649",
            "1984 U.S. LEXIS 111",
            "52 U.S.L.W. 4790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donaldson v. United States",
          "cluster_id": 108236,
          "cite": [
            "27 L. Ed. 2d 580",
            "91 S. Ct. 534",
            "400 U.S. 517",
            "1971 U.S. LEXIS 147",
            "14 Fed. R. Serv. 2d 1096",
            "27 A.F.T.R.2d (RIA) 482"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Petzoldt v. Commissioner",
          "cluster_id": 4706920,
          "cite": [
            "92 T.C. 661",
            "1989 U.S. Tax Ct. LEXIS 42",
            "92 T.C. No. 37"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Orozco v. Texas",
          "cluster_id": 107883,
          "cite": [
            "22 L. Ed. 2d 311",
            "394 U.S. 324",
            "89 S. Ct. 1095",
            "1969 U.S. LEXIS 2154"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Roldan",
          "cluster_id": 2546413,
          "cite": [
            "110 P.3d 289",
            "27 Cal. Rptr. 3d 360",
            "35 Cal. 4th 646",
            "2005 Cal. Daily Op. Serv. 3440",
            "2005 Daily Journal DAR 4656",
            "2005 Cal. LEXIS 4270"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adams v. Illinois",
          "cluster_id": 108480,
          "cite": [
            "31 L. Ed. 2d 202",
            "92 S. Ct. 916",
            "405 U.S. 278",
            "1972 U.S. LEXIS 81"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Blain v. Commonwealth",
          "cluster_id": 1349204,
          "cite": [
            "371 S.E.2d 838",
            "7 Va. App. 10",
            "5 Va. Law Rep. 356",
            "1988 Va. App. LEXIS 94"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Leonard David Griffin",
          "cluster_id": 553880,
          "cite": [
            "922 F.2d 1343",
            "1990 U.S. App. LEXIS 22396",
            "1990 WL 212298"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Avant v. Clifford",
          "cluster_id": 1549504,
          "cite": [
            "341 A.2d 629",
            "67 N.J. 496",
            "1975 N.J. LEXIS 205"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Conway",
          "cluster_id": 2718013,
          "cite": [
            "763 F.3d 115",
            "2014 WL 3953234",
            "2014 U.S. App. LEXIS 15589"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wicker v. State",
          "cluster_id": 1655134,
          "cite": [
            "740 S.W.2d 779",
            "1987 Tex. Crim. App. LEXIS 671",
            "1987 WL 1000"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Walton",
          "cluster_id": 1203058,
          "cite": [
            "824 P.2d 533",
            "64 Wash. App. 410",
            "1992 Wash. App. LEXIS 249"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cannon v. State",
          "cluster_id": 1564923,
          "cite": [
            "691 S.W.2d 664",
            "1985 Tex. Crim. App. LEXIS 1371"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Haas",
          "cluster_id": 2057986,
          "cite": [
            "369 N.E.2d 692",
            "373 Mass. 545",
            "1977 Mass. LEXIS 1107"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth George Montos",
          "cluster_id": 288244,
          "cite": [
            "421 F.2d 215"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Heggins",
          "cluster_id": 1547181,
          "cite": [
            "809 A.2d 908"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107676 OR 9423682 OR 9423683) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zODkzMTg0MDAwMDAmcz0yMzgwNjI3JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107676+OR+9423682+OR+9423683%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107676 OR 9423682 OR 9423683)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDAmcz0xMzEyMjYyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107676+OR+9423682+OR+9423683%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107676 OR 9423682 OR 9423683)",
        "reviewed": 3,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 3,
        "triage_read": 0,
        "triage_snippet_classified": 3
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107676 OR 9423682 OR 9423683)",
    "indexed_citing_opinions": 477,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107676,
        "count": 444,
        "count_source": "search"
      },
      {
        "opinion_id": 9423682,
        "count": 44,
        "count_source": "search"
      },
      {
        "opinion_id": 9423683,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 762,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/mathis-v-united-states-1968.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY0MzMwNzMmcz00NjU2NTgxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107676+OR+9423682+OR+9423683%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107676,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107676,
        "cited_id": 275662,
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
    "date_created": "2026-07-05T12:53:28Z",
    "date_modified": "2026-07-06T08:17:45Z",
    "warnings": [
      "legacy treatment migrated: limited -> caution",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T12:53:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T12:53:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T12:53:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Mathis v. United States (1968)

```
<opinion type="majority">
<author id="b48-6">Me. Justice Black</author>
<p id="AN">delivered the opinion of the Court.</p>
<p id="b48-7">Petitioner was convicted by a jury in a United States District Court on two counts charging that he knowingly filed false claims against the Government in violation of <span class="citation no-link">18 U. S. C. § 287</span><footnotemark>1</footnotemark> and sentenced to 30 months’ imprisonment on each count, the sentences to run concurrently. The frauds charged were claims for tax refunds growing out of petitioner’s individual income taxes for 1960 and 1961. Both income tax returns for these two years asserted receipts of income from two different companies which the government agents were unable to locate and which evidence offered tended to show were nonexistent. The amount of income claimed in each tax return was calculated in such a way as to show that these two nonexistent employers had withheld taxes sufficient to justify substantial refunds to petitioner. The Government paid the 1960 tax refund to petitioner of $885.60 as claimed, but the record fails to show whether the 19.61 claimed refund was paid. A part of the evidence on which the conviction rested consisted of documents and oral statements obtained from petitioner by a government agent while petitioner was in prison serving a state sentence. Before eliciting this information, the government agent did not not warn petitioner that any evi<page-number citation-index="1" label="3">*3</page-number>dence he gave the Government could be used against him, and that he had a right to remain silent if he desired as well as a right to the presence of counsel and that if he was unable to afford counsel one would be appointed for him. At trial petitioner sought several times without success to have the judge hold hearings out of the presence of the jury to prove that his statements to the revenue agent were given without these warnings and should therefore not be used as evidence against him. For this contention he relied exclusively on our case of <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). The District Court rejected this contention as did the Court of Appeals in affirming. <span class="citation" data-id="9452694"><a href="/opinion/275684/perma-life-mufflers-inc-v-international-parts-corporation/" aria-description="Citation for case: Perma Life Mufflers, Inc. v. International Parts Corporation">376 F. 2d 695</a></span>. We granted certiorari to decide whether the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>case calls for reversal. We hold that it does.</p>
<p id="b49-5">There can be no doubt that the documents and oral statements given by petitioner to the government agent and used against him were strongly incriminating.<footnotemark>2</footnotemark> In the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>case this Court’s opinion stated at some length the constitutional reasons why one in custody who is interrogated by officers about matters that might tend to incriminate him is entitled to be warned “that he has the right to remain silent, that anything he says can be used against him in a court of law, that he has the right to the presence of an attorney, and that if he cannot afford an attorney one will be appointed for him <page-number citation-index="1" label="4">*4</page-number>prior to any questioning if he so desires.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 479</a></span>. The Government here seeks to escape application of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings on two arguments: (1) that these questions were asked as a part of a routine tax investigation where no criminal proceedings might even be brought, and (2) that the petitioner had not been put in jail by the officers questioning him, but was there for an entirely separate offense. These differences are too minor and shadowy to justify a departure from the well-considered conclusions of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>with reference to warnings to be given to a person held in custody.</p>
<p id="b50-6">It is true that a “routine tax investigation” may be initiated for the purpose of a civil action rather than criminal prosecution. To this extent tax investigations differ from investigations of murder, robbery, and other crimes. But tax investigations frequently lead to criminal prosecutions, just as the one here did. In fact, the last visit of the revenue agent to the jail to question petitioner took place only eight days before the full-fledged criminal investigation concededly began. And, as the investigating revenue agent was compelled to admit, there was always the possibility during his investigation that his work would end up in a criminal prosecution. We reject the contention that tax investigations are immune from the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requirements <em>for </em>warnings to be given a person in custody.</p>
<p id="b50-7">The Government also seeks to narrow the scope of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>holding by making it applicable only to questioning one who is “in custody” in connection with the very case under investigation. There is no substance to such a distinction, and in effect it goes against the whole purpose of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>decision which was designed to give meaningful protection to Fifth Amendment rights. We find nothing in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>opinion which calls for a curtailment of the warnings to be given persons <page-number citation-index="1" label="5">*5</page-number>under interrogation by officers based on the reason why the person is in custody. In speaking of “custody” the language of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>opinion is clear and unequivocal:</p>
<blockquote id="b51-5">“To summarize, we hold that when an individual is taken into custody or otherwise deprived of his freedom by the authorities in any significant way and is subjected to questioning, the privilege against self-incrimination is jeopardized.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#478" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 478</a></span>.</blockquote>
<p id="b51-6">And the opinion goes on to say that the person so held must be given the warnings about his right to be silent and his right to have a lawyer.</p>
<p id="b51-7">Thus, the courts below were wrong in permitting the introduction of petitioner’s self-incriminating evidence given without warning of his right to be silent and right to counsel. The cause is reversed and remanded for further proceedings consistent with this opinion.</p>
<p id="b51-8">
<em>It is so ordered.</em>
</p>
<judges id="b51-9">Mr. Justice Marshall took no part in the consideration or decision of this case.</judges>
<footnote label="1">
<p id="b48-8"> <span class="citation no-link">18 U. S. C. § 287</span> provides: “Whoever makes or presents to any person or officer in the civil, military, or naval service of the United States, or to any department or agency thereof, any claim upon or against the United States, or any department or agency thereof, knowing such claim to be false, fictitious, or fraudulent, shall be fined not more than $10,000 or imprisoned not more than five years, or both.”</p>
</footnote>
<footnote label="2">
<p id="b49-6"> Internal Revenue Agent Lawless testified that on October 30, 1964, he interviewed petitioner in the Florida State Penitentiary to determine if the 1960 return had been prepared by petitioner and to obtain petitioner’s consent in writing to extend the statute of limitations on the 1960 return. At this interview petitioner identified the 1960 tax return and the signature thereon as his; he also signed the extension form. Again on March 2, 1965, Agent Lawless interviewed petitioner at the penitentiary, and this time petitioner identified the 1961 tax return and signature thereon as his and signed an extension form for this return.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Michigan v. Jackson.md  (`case`, 5 assertions)

### content_page

```
---
title: "Michigan v. Jackson"
type: case
citation: "475 U.S. 625 (1986)"
parallel_cite: "106 S. Ct. 1404; 89 L. Ed. 2d 631; 54 U.S.L.W. 4334"
neutral_cite: 1986 U.S. LEXIS 91
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1986
date_decided: 1986-04-01
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: superseded
  as_of_content: 1986-04-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Michigan v. Jackson
  varies_by_point: false
  scope_note: "Overruled by Montejo v. Louisiana, 556 U.S. 778 (2009); survives only as history."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111622/michigan-v-jackson/"
  cluster_id: 111622
  opinion_id: 9430407
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Historical / origin"
related: ["[[Montejo v. Louisiana]]", "[[Edwards v. Arizona]]", "[[McNeil v. Wisconsin]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "waiver", "overruled", "historical"]
holding: "Held a post-appointment, police-initiated waiver of the Sixth Amendment right to counsel presumptively invalid — **overruled by *Montejo v. Louisiana* (2009)**; survives only as history."
lake:
  record_id: Michigan v. Jackson
  status: verified
  projected_at: 2026-07-06
---

# Michigan v. Jackson

*475 U.S. 625 (1986)* · U.S. Supreme Court · **Historical** · Treatment: **overruled** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
In consolidated cases, defendants requested counsel at their arraignments. Police then initiated interrogation, the defendants waived their rights, and they made incriminating statements. The Michigan Supreme Court ordered the confessions suppressed.

## Issue
Whether a waiver of the Sixth Amendment right to counsel is valid where police initiate interrogation after the defendant has requested counsel at an arraignment or similar proceeding.

## Rule
Extending [[Edwards v. Arizona]] to the Sixth Amendment, the Court held such a waiver presumptively invalid: "We thus hold that, if police initiate interrogation after a defendant's assertion, at an arraignment or similar proceeding, of his right to counsel, any waiver of the defendant's right to counsel for that police-initiated interrogation is invalid." — 475 U.S. at 636. ^pin-636

## Application
Each defendant had requested counsel at arraignment, and police then initiated the interrogations that produced the confessions. Under the rule the Court announced, those police-initiated waivers were presumptively invalid, so the resulting confessions could not be used against the defendants.

## Conclusion
Affirmed; the suppression of the confessions was upheld under the now-overruled *Jackson* presumption.

## Treatment & subsequent history
- **Status:** overruled *(as of 2026-06-30)* — **Historical**.
- **Overruled by** [[Montejo v. Louisiana]], 556 U.S. 778 (2009). *[[Montejo v. Louisiana|Montejo]]* abandoned *Jackson*'s prophylactic presumption, holding that a defendant may validly waive the Sixth Amendment right to counsel during police-initiated interrogation even after counsel has attached or been requested, with the *[[Miranda v. Arizona|Miranda]]*/*[[Edwards v. Arizona|Edwards]]* framework providing the protection instead. *Jackson* survives only as history; its rule is no longer good law.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Historical / origin*

## Sources
- *Michigan v. Jackson*, 475 U.S. 625 (1986) — https://www.courtlistener.com/opinion/111622/michigan-v-jackson/ — pinpoint: 636. (Cluster/opinion located via the L6 ladder from reporter cite 475 U.S. 625; identity and proposition confirmed in the returned text.)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0dbeb58aea6efa02", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "475 U.S. 625 (1986)", "court": "U.S. Supreme Court", "neutral_cite": "1986 U.S. LEXIS 91", "official_citation_present": true, "parallel_cite": "106 S. Ct. 1404; 89 L. Ed. 2d 631; 54 U.S.L.W. 4334", "title": "Michigan v. Jackson", "year": "1986"}}
{"assertion_id": "420bdd9b778df061", "dimension": "support", "kind": "home_role", "locator": {"home": "Sixth Amendment Right to Counsel"}, "payload": {"home": "Sixth Amendment Right to Counsel", "role": "Historical / origin", "title": "Michigan v. Jackson"}}
{"assertion_id": "554828db1b78b7f1", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Held a post-appointment, police-initiated waiver of the Sixth Amendment right to counsel presumptively invalid — **overruled by *Montejo v. Louisiana* (2009)**; survives only as history.", "title": "Michigan v. Jackson"}}
{"assertion_id": "9c8413ebd5d4aa60", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Michigan v. Jackson"}}
{"assertion_id": "ebc830289605a030", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1986-04-01", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Michigan v. Jackson", "field_i_validity": "superseded", "scope_note": "Overruled by Montejo v. Louisiana, 556 U.S. 778 (2009); survives only as history.", "title": "Michigan v. Jackson", "varies_by_point": "false"}}
```

### lake record — Michigan v. Jackson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Michigan v. Jackson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Michigan v. Jackson",
    "case_name_short": "",
    "case_name_full": "Michigan v. Jackson",
    "input_case_name": "Michigan v. Jackson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1986-04-01",
    "year": 1986,
    "docket": null,
    "cluster_id": 111622,
    "lead_opinion_id": 9430407,
    "sibling_ids": [
      111622,
      9430407,
      9430408,
      9430409
    ],
    "absolute_url": "/opinion/111622/michigan-v-jackson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "475 U.S. 625",
      "volume": "475",
      "reporter": "U.S.",
      "page": "625",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "106 S. Ct. 1404",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1404",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 2d 631",
        "volume": "89",
        "reporter": "L. Ed. 2d",
        "page": "631",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4334",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4334",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. LEXIS 91",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "91",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "475 U.S. 625",
        "volume": "475",
        "reporter": "U.S.",
        "page": "625",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 S. Ct. 1404",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1404",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 2d 631",
        "volume": "89",
        "reporter": "L. Ed. 2d",
        "page": "631",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. LEXIS 91",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "91",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4334",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4334",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "475 U.S. 625",
    "official_selection": {
      "court_class": "scotus",
      "selected": "475 U.S. 625",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-636",
      "page": null,
      "quote": "--- # Michigan v. Jackson *475 U.S. 625 (1986)* \u00b7 U.S. Supreme Court \u00b7 **Historical** \u00b7 Treatment: **overruled** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In consolidated cases, defendants requested counsel at their arraignments. Police then initiated interrogation, the defendants waived their rights, and they made incriminating statements. The Michigan Supreme Court ordered the confessions suppressed. ## Issue Whether a waiver of the Sixth Amendment right to counsel is valid where police initiate interrogation after the defendant has requested counsel at an arraignment or similar proceeding. ## Rule Extending [[Edwards v. Arizona]] to the Sixth Amendment, the Court held such a waiver presumptively invalid:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "superseded",
    "as_of_content": "1986-04-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Michigan v. Jackson",
    "varies_by_point": false,
    "scope_note": "Overruled by Montejo v. Louisiana, 556 U.S. 778 (2009); survives only as history.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Montejo v. Louisiana",
          "cluster_id": 145873,
          "cite": "556 U.S. 778",
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:overruled"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Scott",
          "cluster_id": 4834608,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane1_negative"
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
        "journal_ref": "Michigan v. Jackson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Turner v. United States",
          "cluster_id": 4480399,
          "cite": [
            "885 F.3d 949"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jenkins v. Bergeron",
          "cluster_id": 3207734,
          "cite": [
            "824 F.3d 148",
            "2016 U.S. App. LEXIS 9732",
            "2016 WL 3031089"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jones v. Stephens",
          "cluster_id": 7317930,
          "cite": [
            "157 F. Supp. 3d 623",
            "2016 U.S. Dist. LEXIS 3888",
            "2016 WL 147919"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hodson v. State",
          "cluster_id": 2542781,
          "cite": [
            "350 S.W.3d 169",
            "2011 WL 1796088"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Tlasek",
          "cluster_id": 6589376,
          "cite": [
            "77 Mass. App. Ct. 298",
            "930 N.E.2d 170",
            "2010 Mass. App. LEXIS 999"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pecina v. State",
          "cluster_id": 2292956,
          "cite": [
            "326 S.W.3d 249",
            "2010 Tex. App. LEXIS 5631",
            "2010 WL 2825663"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Flores v. State",
          "cluster_id": 1871985,
          "cite": [
            "299 S.W.3d 843",
            "2009 WL 3466009"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Arabzadegan v. State",
          "cluster_id": 2166816,
          "cite": [
            "240 S.W.3d 44",
            "2007 WL 2066225"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wesbrook v. State",
          "cluster_id": 1473130,
          "cite": [
            "29 S.W.3d 103",
            "2000 Tex. Crim. App. LEXIS 86",
            "2000 WL 1346901"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 117863,
          "cite": [
            "129 L. Ed. 2d 362",
            "114 S. Ct. 2350",
            "512 U.S. 452",
            "1994 U.S. LEXIS 4827"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
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
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McNeil v. Wisconsin",
          "cluster_id": 112622,
          "cite": [
            "115 L. Ed. 2d 158",
            "111 S. Ct. 2204",
            "501 U.S. 171",
            "1991 U.S. LEXIS 3483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McFarland v. State",
          "cluster_id": 2413967,
          "cite": [
            "928 S.W.2d 482",
            "1996 Tex. Crim. App. LEXIS 19",
            "1996 WL 71513"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Citizens United v. Federal Election Commission",
          "cluster_id": 1741,
          "cite": [
            "175 L. Ed. 2d 753",
            "130 S. Ct. 876",
            "558 U.S. 310",
            "2010 U.S. LEXIS 766",
            "22 Fla. L. Weekly Fed. S 73",
            "78 U.S.L.W. 4078",
            "187 L.R.R.M. (BNA) 2961",
            "159 Lab. Cas. (CCH) 10,166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marin v. State",
          "cluster_id": 1471238,
          "cite": [
            "851 S.W.2d 275",
            "1993 Tex. Crim. App. LEXIS 57",
            "1993 WL 62078"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patterson v. Illinois",
          "cluster_id": 112127,
          "cite": [
            "101 L. Ed. 2d 261",
            "108 S. Ct. 2389",
            "487 U.S. 285",
            "1988 U.S. LEXIS 2876",
            "56 U.S.L.W. 4733"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Roberson",
          "cluster_id": 112100,
          "cite": [
            "100 L. Ed. 2d 704",
            "108 S. Ct. 2093",
            "486 U.S. 675",
            "1988 U.S. LEXIS 2726",
            "56 U.S.L.W. 4590"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
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
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnick v. Mississippi",
          "cluster_id": 112513,
          "cite": [
            "112 L. Ed. 2d 489",
            "111 S. Ct. 486",
            "498 U.S. 146",
            "1990 U.S. LEXIS 6118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Harris",
          "cluster_id": 1476684,
          "cite": [
            "859 A.2d 364",
            "181 N.J. 391",
            "2004 N.J. LEXIS 1080"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
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
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albert L. Wilson v. Edward Murray, Director of the Virginia Department of Corrections",
          "cluster_id": 480360,
          "cite": [
            "806 F.2d 1232",
            "1986 U.S. App. LEXIS 34712"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
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
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
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
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
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
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Stephenson",
          "cluster_id": 2410270,
          "cite": [
            "878 S.W.2d 530",
            "1994 Tenn. LEXIS 143"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Connecticut v. Barrett",
          "cluster_id": 111796,
          "cite": [
            "93 L. Ed. 2d 920",
            "107 S. Ct. 828",
            "479 U.S. 523",
            "1987 U.S. LEXIS 419",
            "55 U.S.L.W. 4151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Cobb",
          "cluster_id": 118417,
          "cite": [
            "149 L. Ed. 2d 321",
            "121 S. Ct. 1335",
            "532 U.S. 162",
            "2001 U.S. LEXIS 2696"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fuller v. State",
          "cluster_id": 1575568,
          "cite": [
            "829 S.W.2d 191",
            "1992 Tex. Crim. App. LEXIS 62",
            "1992 WL 55274"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rothgery v. Gillespie County",
          "cluster_id": 145785,
          "cite": [
            "171 L. Ed. 2d 366",
            "128 S. Ct. 2578",
            "554 U.S. 191",
            "2008 U.S. LEXIS 5057",
            "21 Fla. L. Weekly Fed. S 429",
            "76 U.S.L.W. 4520"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Yousef",
          "cluster_id": 781722,
          "cite": [
            "327 F.3d 56",
            "61 Fed. R. Serv. 251",
            "2003 U.S. App. LEXIS 6437"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Briggs",
          "cluster_id": 2550075,
          "cite": [
            "12 A.3d 291",
            "608 Pa. 430",
            "2011 Pa. LEXIS 107"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Jackson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111622 OR 9430407 OR 9430408 OR 9430409) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTgyOTg4ODAwMDAwJnM9MTA1MzQxMSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111622+OR+9430407+OR+9430408+OR+9430409%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111622 OR 9430407 OR 9430408 OR 9430409)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNTkmcz03MDU5OTYmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111622+OR+9430407+OR+9430408+OR+9430409%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111622 OR 9430407 OR 9430408 OR 9430409)",
        "reviewed": 15,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 15,
        "triage_read": 0,
        "triage_snippet_classified": 15
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111622 OR 9430407 OR 9430408 OR 9430409)",
    "indexed_citing_opinions": 954,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111622,
        "count": 875,
        "count_source": "search"
      },
      {
        "opinion_id": 9430407,
        "count": 115,
        "count_source": "search"
      },
      {
        "opinion_id": 9430408,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430409,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1418,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/michigan-v-jackson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc4ODUxMjUmcz03ODU3OTAyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111622+OR+9430407+OR+9430408+OR+9430409%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111622,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 108794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 109757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 110300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 110474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 110987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 111112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 111193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 111288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 111355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 111546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 1576588,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 1853839,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 2206509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 2510431,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111622,
        "cited_id": 3580565,
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
    "date_created": "2026-07-05T13:27:48Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: overruled -> superseded",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:28:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:28:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:28:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Michigan v. Jackson

```
<opinion type="majority">
<author id="A23">Justice Stevens</author>
<p id="A7d">delivered the opinion of the Court.</p>
<p id="AauU">In <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981), we held that an accused person in custody who has “expressed his desire to deal with the police only through counsel, is not subject to further interrogation by the authorities until counsel has been made available to him, unless the accused himself initiates further communication, exchanges, or conversations with the police.” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona"><em>Id., </em>at 484-485</a></span>. In <em>Solem </em>v. <em>Stumes, </em><span class="citation" data-id="9429516"><a href="/opinion/111112/solem-v-stumes/" aria-description="Citation for case: Solem v. Stumes">465 U. S. 638</a></span> (1984), we reiterated that <em>“Edwards </em>established a bright-line rule to safeguard pre-existing rights,” <em><span class="citation" data-id="9429516"><a href="/opinion/111112/solem-v-stumes/" aria-description="Citation for case: Solem v. Stumes">id.,</a></span> </em>at 646: “once a suspect has invoked the right to counsel, any subsequent conversation must be initiated by him.” <span class="citation" data-id="9429516"><a href="/opinion/111112/solem-v-stumes/#641" aria-description="Citation for case: Solem v. Stumes"><em>Id., </em>at 641</a></span>.</p>
<p id="AOk">The question presented by these two cases is whether the same rule applies to a defendant who has been formally charged with a crime and who has requested appointment of counsel at his arraignment. In both cases, the Michigan Supreme Court held that postarraignment confessions were improperly obtained — and the Sixth Amendment violated— because the defendants had “requested counsel during their arraignments, but were not afforded an opportunity to consult with counsel before the police initiated further interrogations.” <span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/#67" aria-description="Citation for case: People v. Bladel">421 Mich. 39, 67-68</a></span>, <span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/#69" aria-description="Citation for case: People v. Bladel">365 N. W. 2d 56, 69</a></span> (1984). We agree with that holding.</p>
<p id="AS7">H-{</p>
<p id="AY_">The relevant facts may be briefly stated. Respondent Bladel was convicted of the murder of three railroad employees at the Amtrak Station in Jackson, Michigan, on Decem<page-number citation-index="1" label="627">*627</page-number>ber 31, 1978. Bladel, a disgruntled former employee, was arrested on January 1, 1979, and, after being questioned on two occasions, was released on January 3. He was arrested again on March 22, 1979, and agreed to talk to the police that evening without counsel. On the following morning, Friday, March 23, 1979, Bladel was arraigned. He requested that counsel be appointed for him because he was indigent. The detective in charge of the Bladel investigation was present at the arraignment. A notice of appointment was promptly mailed to a law firm, but the law firm did not receive it until Tuesday, March 27. In the interim, on March 26, 1979, two police officers interviewed Bladel in the county jail and obtained a confession from him. Prior to that questioning, the officers properly advised Bladel of his <em>Miranda </em>rights.<footnotemark>1</footnotemark> Although he had inquired about his representation several times since the arraignment, Bladel was not told that a law firm had been appointed to represent him.</p>
<p id="b709-4">The trial court overruled Bladel’s objection to the admissibility of all four statements. On appeal from his conviction and sentence, Bladel challenged only the postarraignment confession. The Michigan Court of Appeals first rejected that challenge and affirmed the conviction, <span class="citation" data-id="1853839"><a href="/opinion/1853839/people-v-bladel/" aria-description="Citation for case: People v. Bladel">106 Mich. App. 397</a></span>, <span class="citation" data-id="1853839"><a href="/opinion/1853839/people-v-bladel/" aria-description="Citation for case: People v. Bladel">308 N. W. 2d 230</a></span> (1981), but, after reconsideration in the light of a recent decision by the State Supreme Court, it reversed and remanded for a new trial. <span class="citation" data-id="1576588"><a href="/opinion/1576588/people-v-bladel/" aria-description="Citation for case: People v. Bladel">118 Mich. App. 498</a></span>, <span class="citation" data-id="1576588"><a href="/opinion/1576588/people-v-bladel/" aria-description="Citation for case: People v. Bladel">325 N. W. 2d 421</a></span> (1982). The Michigan Supreme Court then granted the prosecutor’s application for leave to appeal and considered the case with respondent Jackson’s appeal of his conviction. <span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/" aria-description="Citation for case: People v. Bladel">421 Mich. 39</a></span>, <span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/" aria-description="Citation for case: People v. Bladel">365 N. W. 2d 56</a></span> (1984).</p>
<p id="b710-4"><page-number citation-index="1" label="628">*628</page-number>Respondent Jackson was convicted of second-degree murder and conspiracy to commit second-degree murder. He was one of four participants in a wife’s plan to have her husband killed on July 12, 1979. Arrested on an unrelated charge on July 30, 1979, he made a series of six statements in response to police questioning prior to his arraignment at 4:30 p.m. on August 1. During the arraignment, Jackson requested that counsel be appointed for him. The police involved in his investigation were present at the arraignment. On the following morning, before he had an opportunity to consult with counsel, two police officers obtained another statement from Jackson to “confirm” that he was the person who had shot the victim. As was true of the six prearraignment statements, the questioning was preceded by advice of his <em>Miranda </em>rights and Jackson’s agreement to proceed without counsel being present.</p>
<p id="b710-5">The Michigan Court of Appeals held that the seventh statement was properly received in evidence. <span class="citation" data-id="9736654"><a href="/opinion/2206509/people-v-jackson/" aria-description="Citation for case: People v. Jackson">114 Mich. App. 649</a></span>, <span class="citation" data-id="9736654"><a href="/opinion/2206509/people-v-jackson/" aria-description="Citation for case: People v. Jackson">319 N. W. 2d 613</a></span> (1982). It distinguished <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>on the ground that Jackson’s request for an attorney had been made at his arraignment whereas Edwards’ request had been made during a custodial interrogation by the police. Accordingly, it affirmed Jackson’s conviction of murder, although it set aside the conspiracy conviction on unrelated grounds.</p>
<p id="b710-6">The Michigan Supreme Court held that the postarraignment statements in both cases should have been suppressed. Noting that the Sixth Amendment right to counsel attached at the time of the arraignments, the court concluded that the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule “applies by analogy to those situations where an accused requests counsel before the arraigning magistrate. Once this request occurs, the police may not conduct further interrogations until counsel has been made available to the accused, unless the accused initiates further communications, exchanges, or conversations with the police. . . . The police cannot simply ignore a defendant’s unequivocal request for counsel.” <span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/#66" aria-description="Citation for case: People v. Bladel">421 Mich., at 66-67</a></span>, <span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/#68" aria-description="Citation for case: People v. Bladel">365 N. W. 2d, at 68-69</a></span> <page-number citation-index="1" label="629">*629</page-number>(footnote omitted). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./471/1124/">471 U. S. 1124</a></span> (1985), and we now affirm.<footnotemark>2</footnotemark></p>
<p id="b711-5">II</p>
<p id="b711-6">The question is not whether respondents had a right to counsel at their postarraignment, custodial interrogations. The existence of that right is clear. It has two sources. The Fifth Amendment protection against compelled self-incrimination provides the right to counsel at custodial interrogations. <em>Edwards, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#482" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 482</a></span>; <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#470" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 470</a></span> (1966). The Sixth Amendment guarantee of the assistance of counsel also provides the right to counsel at postarraignment interrogations. The arraignment signals “the initiation of adversary judicial proceedings” and thus the attachment of the Sixth Amendment, <em>United States </em>v. <em>Gouveia, </em><span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/#187" aria-description="Citation for case: United States v. Gouveia">467 U. S. 180, 187, 188</a></span> (1984);<footnotemark>3</footnotemark> there<page-number citation-index="1" label="630">*630</page-number>after, government efforts to elicit information from the accused, including interrogation, represent “critical stages” at which the Sixth Amendment applies. <em>Maine </em>v. <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">474 U. S. 159</a></span> (1985); <em>United States </em>v. <em>Henry, </em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">447 U. S. 264</a></span> (1980); <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387</a></span> (1977); <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964). The question in these cases is whether respondents validly waived their right to counsel at the postarraignment custodial interrogations.</p>
<p id="b712-5">In <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>, </em>the request for counsel was made to the police during custodial interrogation, and the basis for the Court’s holding was the Fifth Amendment privilege against compelled self-incrimination. The Court noted the relevance of various Sixth Amendment precedents, <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484, n. 8</a></span>, but found it unnecessary to rely on the possible applicability of the Sixth Amendment. <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#480" aria-description="Citation for case: Edwards v. Arizona"><em>Id., </em>at 480, n. 7</a></span>. In these cases, the request for counsel was made to a judge during arraignment, and the basis for the Michigan Supreme Court opinion was the Sixth Amendment’s guarantee of the assistance of counsel.<footnotemark>4</footnotemark> The State argues that the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule should not apply to these circumstances because there are legal differences in the basis for the claims; because there are <page-number citation-index="1" label="631">*631</page-number>factual differences in the contexts of the claims; and because respondents signed valid waivers of their right to counsel at the postarraignment custodial interrogations. We consider these contentions in turn.</p>
<p id="b713-5">The State contends that differences in the legal principles underlying the Fifth and Sixth Amendments compel the conclusion that the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule should not apply to a Sixth Amendment claim. <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>flows from the Fifth Amendment’s right to counsel at custodial interrogations, the State argues; its relevance to the Sixth Amendment’s provision of the assistance of counsel is far less clear, and thus the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>principle for assessing waivers is unnecessary and inappropriate.</p>
<p id="b713-6">In our opinion, however, the reasons for prohibiting the interrogation of an uncounseled prisoner who has asked for the help of a lawyer are even stronger after he has been formally charged with an offense than before. The State’s argument misapprehends the nature of the pretrial protections afforded by the Sixth Amendment. In <em>United States </em>v. <em><span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/" aria-description="Citation for case: United States v. Gouveia">Gouveia</a></span>, </em>we explained the significance of the formal accusation, and the corresponding attachment of the Sixth Amendment right to counsel:</p>
<blockquote id="b713-7">“[G]iven the plain language of the Amendment and its purpose of protecting the unaided layman at critical confrontations with his adversary, our conclusion that the right to counsel attaches at the initiation of adversary judicial criminal proceedings ‘is far from a mere formalism.’ <em>Kirby </em>v. <em>Illinois, </em>406 U. S., at 689. It is only at that time ‘that the government has committed itself to prosecute, and only then that the adverse positions of government and defendant have solidified. It is then that a defendant finds himself faced with the prosecuto-rial forces of organized society, and immersed in the intricacies of substantive and procedural criminal law.’” <span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/#189" aria-description="Citation for case: United States v. Gouveia">467 U. S., at 189</a></span>.</blockquote>
<p id="b714-4"><page-number citation-index="1" label="632">*632</page-number>As a result, the “Sixth Amendment guarantees the accused, at least after the initiation of formal charges, the right to rely on counsel as a ‘medium’ between him and the State.” <em>Maine </em>v. <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#176" aria-description="Citation for case: Maine v. Moulton">474 U. S., at 176</a></span>. Thus, the Sixth Amendment right to counsel at a postarraignment interrogation requires at least as much protection as the Fifth Amendment right to counsel at any custodial interrogation.</p>
<p id="b714-5">Indeed, after a formal accusation has been made — and a person who had previously been just a “suspect” has become an “accused” within the meaning of the Sixth Amendment— the constitutional right to the assistance of counsel is of such importance that the police may no longer employ techniques for eliciting information from an uncounseled defendant that might have been entirely proper at an earlier stage of their investigation. Thus, the surreptitious employment of a cellmate, see <em>United States </em>v. <em>Henry, </em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">447 U. S. 264</a></span> (1980), or the electronic surveillance of conversations with third parties, see <em>Maine </em>v. <em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">Moulton, supra;</a></span> Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964), may violate the defendant’s Sixth Amendment right to counsel even though the same methods of investigation might have been permissible before arraignment or indictment.<footnotemark>5</footnotemark> Far from undermining the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule, the difference between the legal basis for the rule applied in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>and the Sixth Amendment claim asserted in these cases actually provides additional support for the application of the rule in these circumstances.</p>
<p id="b714-6">The State also relies on the factual differences between a request for counsel during custodial interrogation and a request for counsel at an arraignment. The State maintains that respondents may not have actually intended their re<page-number citation-index="1" label="633">*633</page-number>quest for counsel to encompass representation during any further questioning by the police. This argument, however, must be considered against the backdrop of our standard for assessing waivers of constitutional rights. Almost a half century ago, in <em>Johnson </em>v. <em>Zerbst, </em><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458</a></span> (1938), a case involving an alleged waiver of a defendant’s Sixth Amendment right to counsel, the Court explained that we should “indulge every reasonable presumption against waiver of fundamental constitutional rights.” <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst"><em>Id., </em>at 464</a></span>. For that reason, it is the State that has the burden of establishing a valid waiver. <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#404" aria-description="Citation for case: Brewer v. Williams">430 U. S., at 404</a></span>. Doubts must be resolved in favor of protecting the constitutional claim. This settled approach to questions of waiver requires us to give a broad, rather than a narrow, interpretation to a defendant’s request for counsel — we presume that the defendant requests the lawyer’s services at every critical stage of the prosecution.<footnotemark>6</footnotemark> We thus reject the State’s suggestion that respondents’ requests for the appointment of counsel should be construed to apply only to representation in formal legal proceedings.<footnotemark>7</footnotemark></p>
<p id="b716-4"><page-number citation-index="1" label="634">*634</page-number>The State points to another factual difference: the police may not know of the defendant’s request for attorney at the arraignment. That claimed distinction is similarly unavailing. In the cases at bar, in which the officers in charge of the investigations of respondents were present at the arraignments, the argument is particularly unconvincing. More generally, however, Sixth Amendment principles require that we impute the State’s knowledge from one state actor to another. For the Sixth Amendment concerns the confrontation between the State and the individual.<footnotemark>8</footnotemark> One set of state actors (the police) may not claim ignorance of defendants’ unequivocal request for counsel to another state actor (the court).</p>
<p id="b716-5">The State also argues that, because of these factual differences, the application of <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>in a Sixth Amendment context will generate confusion. However, we have frequently emphasized that one of the characteristics of <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>is its clear, “bright-line” quality. See, <em>e. g., Smith </em>v. <em>Illinois, </em><span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#98" aria-description="Citation for case: Smith v. Illinois">469 U. S. 91, 98</a></span> (1984); <em>Solem </em>v. <em>Stumes, </em><span class="citation" data-id="9429516"><a href="/opinion/111112/solem-v-stumes/#646" aria-description="Citation for case: Solem v. Stumes">465 U. S., at 646</a></span>; <em>Oregon </em>v. <em>Bradshaw, </em><span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1044" aria-description="Citation for case: Oregon v. Bradshaw">462 U. S. 1039, 1044</a></span> (1983) (plurality opinion); <span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1054" aria-description="Citation for case: Oregon v. Bradshaw"><em>id., </em>at 1054, n. 2</a></span> (MARSHALL, J., dissenting). We do not agree that applying the rule when the accused requests counsel at an arraignment, rather than in the police station, somehow diminishes that clarity. To the extent that there may have been any doubts about interpreting a request <page-number citation-index="1" label="635">*635</page-number>for counsel at an arraignment, or about the police responsibility to know of and respond to such a request, our opinion today resolves them.</p>
<p id="b717-5">Finally, the State maintains that each of the respondents made a valid waiver of his Sixth Amendment rights by signing a postarraignment confession after again being advised of his constitutional rights. In <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>, </em>however, we rejected the notion that, after a suspect’s request for counsel, advice of rights and acquiescence in police-initiated questioning could establish a valid waiver. <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484</a></span>. We find no warrant for a different view under a Sixth Amendment analysis. Indeed, our rejection of the comparable argument in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>was based, in part, on our review of earlier Sixth Amendment cases.<footnotemark>9</footnotemark> Just as written waivers are insufficient to justify police-initiated interrogations after the request for counsel in a Fifth Amendment analysis, so too they are insufficient to justify police-initiated interrogations after the request for counsel in a Sixth Amendment analysis.<footnotemark>10</footnotemark></p>
<p id="AZ4"><page-number citation-index="1" label="636">*636</page-number>r — H l-H</p>
<p id="A1H1"><em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>is grounded in the understanding that “the assertion of the right to counsel [is] a significant event,” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#485" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 485</a></span>, and that “additional safeguards are necessary when the accused asks for counsel.” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona"><em>Id., </em>at 484</a></span>. We conclude that the assertion is no less significant, and the need for additional safeguards no less clear, when the request for counsel is made at an arraignment and when the basis for the claim is the Sixth Amendment. We thus hold that, if police initiate interrogation after a defendant’s assertion, at an arraignment or similar proceeding, of his right to counsel, any waiver of the defendant’s right to counsel for that police-initiated interrogation is invalid.</p>
<p id="AKK">Although the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>decision itself rested on the Fifth Amendment and concerned a request for counsel made during custodial interrogation, the Michigan Supreme Court correctly perceived that the reasoning of that case applies with even greater force to these cases. The judgments are accordingly affirmed.</p>
<p id="AbLq">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b709-5"> See <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings were also given prior to the questioning on January 1, January 2, and March 22. Although Bladel made certain inculpatory statements on those occasions, he denied responsibility for the murder until after the arraignment. As the Michigan Supreme Court noted, even without his own statements, the evidence against Bladel was substantial. <span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/#44" aria-description="Citation for case: People v. Bladel">421 Mich., at 44</a></span>, and n. 2, <span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/#58" aria-description="Citation for case: People v. Bladel">365 N. W. 2d, at 58-59</a></span>, and n. 2.</p>
</footnote>
<footnote label="2">
<p id="b711-7"> Respondent Jackson points out that the Michigan Supreme Court also held that his fourth, fifth, and sixth statements should have been suppressed on grounds of prearraignment delay under a state statute. He therefore argues that the decision rests on an adequate and independent state ground and that the writ of certiorari should be dismissed. The state-court opinion, however, does not apply that prearraignment-delay holding to the seventh statement. Thus, although the Michigan court’s holding on the other statements does mean that Jackson’s conviction must be reversed regardless of this Court’s decision, the admissibility of the seventh statement is controlled by that court’s Sixth Amendment analysis, and is properly before us.</p>
</footnote>
<footnote label="3">
<p id="b711-13"> In <em>Jackson, </em>the State concedes that the arraignment represented the initiation of formal legal proceedings, and that the Sixth Amendment attached at that point. Brief for Petitioner in No. 84-1531, p. 10. In <em>Bladel, </em>however, the State disputes that contention, Brief for Petitioner in No. 84-1539, pp. 24-26. In view of the clear language in our decisions about the significance of arraignment, the State’s argument is untenable. See, <em>e. g., Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#398" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387, 398</a></span> (1977) (“[A] person is entitled to the help of a lawyer at or after the time that judicial proceedings have been initiated against him — ‘whether by way of formal charge, preliminary hearing, indictment, information, <em>or </em>arraignment’”) (emphasis added), quoting <em>Kirby </em>v. <em>Illinois, </em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682, 689</a></span> (1972) (plurality opinion). See also <em>United States </em>v. <em>Gouveia, </em><span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/" aria-description="Citation for case: United States v. Gouveia">467 U. S., at 187</a></span>-188 (quoting <page-number citation-index="1" label="630">*630</page-number><em>Kirby); Estelle </em>v. <em>Smith, </em><span class="citation" data-id="9428322"><a href="/opinion/110474/estelle-v-smith/#469" aria-description="Citation for case: Estelle v. Smith">451 U. S. 454, 469-470</a></span> (1981) (quoting <em>Kirby); Moore </em>v. <em>Illinois, </em><span class="citation" data-id="9427017"><a href="/opinion/109757/moore-v-illinois/#226" aria-description="Citation for case: Moore v. Illinois">434 U. S. 220, 226</a></span> (1977) (quoting <em>Kirby). </em>Cf. <em>Powell </em>v. <em>Alabama, </em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#57" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45, 57</a></span> (1932) (“[T]he most critical period of the proceedings against these defendants” was <em>“from the time of their arraignment </em>until the beginning of their trial”) (emphasis added). The question whether arraignment signals the initiation of adversary judicial proceedings, moreover, is distinct from the question whether the arraignment itself is a critical stage requiring the presence of counsel, absent a valid waiver. Cf. <em>Hamilton </em>v. <em>Alabama, </em><span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span> (1961) (Alabama arraignment is a “critical stage”).</p>
</footnote>
<footnote label="4">
<p id="b712-9"> The Michigan Supreme Court found that “defendants’ request to the arraigning magistrate for appointment of counsel implicated only their Sixth Amendment right to counsel,” <span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/#52" aria-description="Citation for case: People v. Bladel">421 Mich., at 52</a></span>, <span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/#62" aria-description="Citation for case: People v. Bladel">365 N. W. 2d, at 62</a></span>, because the request was not made during custodial interrogation. It was for that reason that the Michigan court did not rely on a Fifth Amendment <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>analysis. We express no comment on the validity of the Michigan court’s Fifth Amendment analysis.</p>
</footnote>
<footnote label="5">
<p id="b714-7"> Similarly, after the initiation of adversary judicial proceedings, the Sixth Amendment provides a right to counsel at a “critical stage” even when there is no interrogation and no Fifth Amendment applicability. See <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967) (Sixth Amendment provides right to counsel at postindictment lineup even though Fifth Amendment is not implicated).</p>
</footnote>
<footnote label="6">
<p id="b715-5"> In construing respondents’ request for counsel, we do not, of course, suggest that the right to counsel turns on such a request. See <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#404" aria-description="Citation for case: Brewer v. Williams">430 U. S., at 404</a></span> (“[T]he right to counsel does not depend upon a request by the defendant”); <em>Carnley </em>v. <em>Cochran, </em><span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/#513" aria-description="Citation for case: Carnley v. Cochran">369 U. S. 506, 513</a></span> (1962) (“[I]t is settled that where the assistance of counsel is a constitutional requisite, the right to be furnished counsel does not depend on a request”). Rather, we construe the defendant’s request for counsel as an extremely important fact in considering the validity of a subsequent waiver in response to police-initiated interrogation.</p>
</footnote>
<footnote label="7">
<p id="b715-6"> We also agree with the comments of the Michigan Supreme Court about the nature of an accused’s request for counsel:</p>
<blockquote id="b715-7">“Although judges and lawyers may understand and appreciate the subtle distinctions between the Fifth and Sixth Amendment rights to counsel, the average person does not. When an accused requests an attorney, either before a police officer or a magistrate, he does not know which constitutional right he is invoking; he therefore should not be expected to articulate exactly why or for what purposes he is seeking counsel. It makes little sense to afford relief from further interrogation to a defendant who asks a <page-number citation-index="1" label="634">*634</page-number>police officer for an attorney, but permit further interrogation to a defendant who makes an identical request to a judge. The simple fact that defendant has requested an attorney indicates that he does not believe that he is sufficiently capable of dealing with his adversaries singlehandedly.” <span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/#63" aria-description="Citation for case: People v. Bladel">421 Mich., at 63-64</a></span>, <span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/#67" aria-description="Citation for case: People v. Bladel">365 N. W. 2d, at 67</a></span>.</blockquote>
</footnote>
<footnote label="8">
<p id="b716-11"> See, e. <em>g., Maine </em>v. <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#170" aria-description="Citation for case: Maine v. Moulton">474 U. S. 159, 170-171</a></span> (1985):</p>
<blockquote id="b716-12">“Once the right to counsel has attached and been asserted, <em>the State </em>must of course honor it. This means more than simply that <em>the State </em>cannot prevent the accused from obtaining the assistance of counsel. The Sixth Amendment also imposes on <em>the State </em>an affirmative obligation to respect and preserve the accused’s choice to seek this assistance” (emphasis added) (footnote omitted).</blockquote>
</footnote>
<footnote label="9">
<p id="b717-6"> After stating our holding that “when an accused has invoked his right to have counsel present during custodial interrogation, a valid waiver of that right cannot be established by showing only that he responded to further police-initiated custodial interrogation even if he has been advised of his rights,” 451 U. S., at 484, we appended this footnote:</p>
<blockquote id="b717-7">“In <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387</a></span> (1977), where, as in <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964), the Sixth Amendment right to counsel had accrued, the Court held that a valid waiver of counsel rights should not be inferred from the mere response by the accused to overt or more subtle forms of interrogation or other efforts to elicit incriminating information. In <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>and <em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">Brewer</a></span>, </em>counsel had been engaged or appointed and the admissions in question were elicited in his absence. But in <em>McLeod </em>v. <em>Ohio, </em><span class="citation" data-id="107070"><a href="/opinion/107070/mcleod-v-ohio/" aria-description="Citation for case: McLEOD v. OHIO">381 U. S. 356</a></span> (1965), we summarily reversed a decision that the police could elicit information after indictment even though counsel had not yet been appointed.” <span class="citation" data-id="107070"><a href="/opinion/107070/mcleod-v-ohio/#484" aria-description="Citation for case: McLEOD v. OHIO"><em>Id., </em>at 484, n. 8</a></span>.</blockquote>
</footnote>
<footnote label="10">
<p id="b717-8"> The State also argues that the Michigan Supreme Court’s finding of a valid Fifth Amendment waiver should require the finding of a valid Sixth Amendment waiver. The relationship between the validity of waivers for Fifth and Sixth Amendment purposes has been the subject of considerable attention in the courts, <span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/#55" aria-description="Citation for case: People v. Bladel">421 Mich., at 55-62</a></span>, <span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/#63" aria-description="Citation for case: People v. Bladel">365 N. W. 2d, at 63-67</a></span> (discussing and collecting eases), and the commentaries, <span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/#54" aria-description="Citation for case: People v. Bladel"><em>id., </em>at 54, n. 15</a></span>, <span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/#63" aria-description="Citation for case: People v. Bladel">365 <page-number citation-index="1" label="636">*636</page-number>N. W. 2d, at 63, n. 15</a></span>. In view of our holding that the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule applies to the Sixth Amendment and that the Sixth Amendment requires the suppression of the postarraignment statements, we need not decide either the validity of the Fifth Amendment waiver in this case, see n. 4, <em>supra, </em>or the general relationship between Fifth and Sixth Amendment waivers.</p>
</footnote>
</opinion>
```

---
