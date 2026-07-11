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

## GROUP: _overhaul2/lake/cases/United States v. Jones.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Jones"
type: case
citation: "565 U.S. 400 (2012)"
parallel_cite: "132 S. Ct. 945; 181 L. Ed. 2d 911"
neutral_cite: 2012 U.S. LEXIS 1063
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2012
date_decided: 2012-01-23
docket: 10-1259
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2012-01-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Jones
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/622304/united-states-v-jones/"
  cluster_id: 622304
  opinion_id: 9485324
  identity_checked: true
homes:
  - page: "[[Trespass]]"
    role: "Key — Anchor"
  - page: "[[Real-Time Tracking]]"
    role: "Key — cross-ref (GPS trespass; mosaic concurrences)"
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Related (cross-ref — mosaic seed for Carpenter)"
related: ["[[Katz v. United States]]", "[[Carpenter v. United States]]", "[[Florida v. Jardines]]", "[[Olmstead v. United States]]", "[[United States v. Jacobsen]]"]
aliases: ["United States v. Jones (2012)", "United States v. Antoine Jones"]
tags: ["case", "fourth-amendment", "search-definition", "trespass-theory", "gps-tracking", "physical-intrusion"]
holding: "Installing a GPS tracker on a vehicle and monitoring it was a search under the revived trespass theory — physical intrusion on an 'effect' to obtain information; the controlling modern trespass-search case."
lake:
  record_id: United States v. Jones
  status: verified
  projected_at: 2026-07-06
---

# United States v. Jones

*565 U.S. 400 (2012)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating Antoine Jones for drug trafficking, agents installed a GPS tracking device on the undercarriage of a Jeep Jones used while it was parked in a public lot, then tracked the vehicle's movements for 28 days. The installation occurred outside the scope of the warrant they had obtained (wrong jurisdiction and after it expired), so it was treated as warrantless. The data tied Jones to a stash house, and he was convicted; the D.C. Circuit reversed, holding the tracking was an unconstitutional search.

## Issue
Whether the government's attachment of a GPS tracking device to a vehicle, and its use of that device to monitor the vehicle's movements on public roads, constitutes a "search" within the meaning of the Fourth Amendment.

## Rule
Yes — under a trespass-based theory of the Fourth Amendment. "We hold that the Government's installation of a GPS device on a target's vehicle, and its use of that device to monitor the vehicle's movements, constitutes a 'search.'" — 565 U.S. at 404. ^pin-404

The basis is physical intrusion on a constitutionally protected "effect": "The Government physically occupied private property for the purpose of obtaining information. We have no doubt that such a physical intrusion would have been considered a 'search' within the meaning of the Fourth Amendment when it was adopted." — *Id.* at 404–05. ^pin-404a

The trespass test survives alongside *[[Katz v. United States|Katz]]*: "the *Katz* reasonable-expectation-of-privacy test has been *added to*, not *substituted for*, the common-law trespassory test." — *Id.* at 409. ^pin-409

## Application
On these facts the GPS surveillance was a search. The agents physically attached the device to the Jeep — an "effect" — and did so "for the purpose of obtaining information" about its movements; that trespassory intrusion onto a protected area to gather information was itself a search, without regard to whether Jones had a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in his movements on public roads. The Court did not need to reach the *[[Katz v. United States|Katz]]* expectation-of-privacy question (or the *[[United States v. Knotts|Knotts]]* beeper line, which involved no trespass), because the common-law trespass theory independently resolved the case: installing and monitoring the device on Jones's vehicle was a Fourth Amendment search.

## Conclusion
Attaching and using the GPS device was a search; the D.C. Circuit's judgment reversing the conviction was affirmed. The Court left the reasonableness (warrant/exception) question for remand.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Jones* revives the common-law trespass test as one of the "two definitions of search" alongside the [[Katz v. United States]] privacy test; it anchors the property-based line later applied to the [[Curtilage|curtilage]] in [[Florida v. Jardines]] and informs the digital-privacy analysis of [[Carpenter v. United States]].

## Appears on
- [[Trespass]] — *Key — Anchor*
- [[Real-Time Tracking]] — *Key — cross-ref (GPS trespass; mosaic [[Common Legal Terms#concurring-opinion|concurrences]])*
- [[Third-Party Doctrine & CSLI]] — *Related (cross-ref — mosaic seed for Carpenter)*

## Sources
- *United States v. Jones*, 565 U.S. 400 (2012) — https://www.courtlistener.com/opinion/7350871/united-states-v-jones/ — pinpoints: 404, 409. (Lead majority opinion id 7268856.)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b51c4a0ee382658d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Jones"}, "payload": {"all": [{"cite": "132 S. Ct. 945", "page": "945", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "132"}, {"cite": "181 L. Ed. 2d 911", "page": "911", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "181"}, {"cite": "565 U.S. 400", "page": "400", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "565"}, {"cite": "2012 U.S. LEXIS 1063", "page": "1063", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2012"}], "display": "565 U.S. 400", "official": {"cite": "565 U.S. 400", "page": "400", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "565"}, "official_selection_present": true, "record_id": "United States v. Jones"}}
{"assertion_id": "8ad6f51b56299c74", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-409", "record_id": "United States v. Jones"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-409", "pinpoint_status": "slip-only", "quote": "the *Katz* reasonable-expectation-of-privacy test has been *added to*, not *substituted for*, the common-law trespassory test.", "quote_fidelity": "mismatch", "record_id": "United States v. Jones", "star_marker": null}}
{"assertion_id": "964e9779fc6c95dc", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-404a", "record_id": "United States v. Jones"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-404a", "pinpoint_status": "slip-only", "quote": "The Government physically occupied private property for the purpose of obtaining information. We have no doubt that such a physical intrusion would have been considered a 'search' within the meaning of the Fourth Amendment when it was adopted.", "quote_fidelity": "mismatch", "record_id": "United States v. Jones", "star_marker": null}}
{"assertion_id": "c7061ef6fb712bc7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-404", "record_id": "United States v. Jones"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-404", "pinpoint_status": "slip-only", "quote": "within the meaning of the Fourth Amendment. ## Rule Yes — under a trespass-based theory of the Fourth Amendment.", "quote_fidelity": "mismatch", "record_id": "United States v. Jones", "star_marker": null}}
{"assertion_id": "77bf031d68d8b4b1", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Jones"}, "payload": {"as_of_content": "2012-01-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Jones", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Jones

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Jones",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Jones",
    "case_name_short": "Jones",
    "case_name_full": "United States v. Jones",
    "input_case_name": "United States v. Jones",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2012-01-23",
    "year": 2012,
    "docket": "10-1259",
    "cluster_id": 622304,
    "lead_opinion_id": 9485324,
    "sibling_ids": [
      622304,
      9485324,
      9485325,
      9485326
    ],
    "absolute_url": "/opinion/622304/united-states-v-jones/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 7350871,
        "score": 120,
        "case_name": "United States v. Jones"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "565 U.S. 400",
      "volume": "565",
      "reporter": "U.S.",
      "page": "400",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "132 S. Ct. 945",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "945",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "181 L. Ed. 2d 911",
        "volume": "181",
        "reporter": "L. Ed. 2d",
        "page": "911",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2012 U.S. LEXIS 1063",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "1063",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "132 S. Ct. 945",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "945",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "181 L. Ed. 2d 911",
        "volume": "181",
        "reporter": "L. Ed. 2d",
        "page": "911",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "565 U.S. 400",
        "volume": "565",
        "reporter": "U.S.",
        "page": "400",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 U.S. LEXIS 1063",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "1063",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "565 U.S. 400",
    "official_selection": {
      "court_class": "scotus",
      "selected": "565 U.S. 400",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-404",
      "page": null,
      "quote": "within the meaning of the Fourth Amendment. ## Rule Yes \u2014 under a trespass-based theory of the Fourth Amendment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-404a",
      "page": null,
      "quote": "The Government physically occupied private property for the purpose of obtaining information. We have no doubt that such a physical intrusion would have been considered a 'search' within the meaning of the Fourth Amendment when it was adopted.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-409",
      "page": null,
      "quote": "the *Katz* reasonable-expectation-of-privacy test has been *added to*, not *substituted for*, the common-law trespassory test.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2012-01-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Jones",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Jerel Chinedu Igboji v. State",
          "cluster_id": 4789820,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane1_negative"
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
        "journal_ref": "United States v. Jones:lane1_negative"
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
        "journal_ref": "United States v. Jones:lane1_negative"
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
        "journal_ref": "United States v. Jones:lane1_negative"
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
        "journal_ref": "United States v. Jones:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532255,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532252,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane1_negative"
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
        "journal_ref": "United States v. Jones:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4381539,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane1_negative"
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
        "journal_ref": "United States v. Jones:lane2_top_cited"
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
        "journal_ref": "United States v. Jones:lane2_top_cited"
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
        "journal_ref": "United States v. Jones:lane2_top_cited"
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
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. Virginia",
          "cluster_id": 4501697,
          "cite": [
            "584 U.S. 586",
            "138 S. Ct. 1663",
            "201 L. Ed. 2d 9",
            "2018 U.S. LEXIS 3210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "American Civil Liberties Union of Ill. v. Alvarez",
          "cluster_id": 799453,
          "cite": [
            "679 F.3d 583",
            "40 Media L. Rep. (BNA) 1721",
            "2012 WL 1592618",
            "2012 U.S. App. LEXIS 9303"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thompson, Ex Parte Ronald",
          "cluster_id": 2949202,
          "cite": [
            "442 S.W.3d 325",
            "2014 Tex. Crim. App. LEXIS 969",
            "2014 WL 4627231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
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
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cregan",
          "cluster_id": 2681818,
          "cite": [
            "2014 IL 113600"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Robinson",
          "cluster_id": 3152697,
          "cite": [
            "303 Kan. 11",
            "363 P.3d 875",
            "2015 Kan. LEXIS 929"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Granville, Anthony",
          "cluster_id": 2950015,
          "cite": [
            "423 S.W.3d 399",
            "2014 WL 714730",
            "2014 Tex. Crim. App. LEXIS 237"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Free Speech Coalition, Inc. v. Attorney General of the United States",
          "cluster_id": 676451,
          "cite": [
            "677 F.3d 519",
            "2012 WL 1255056",
            "2012 U.S. App. LEXIS 7543"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Talkington",
          "cluster_id": 2784485,
          "cite": [
            "301 Kan. 453",
            "345 P.3d 258",
            "2015 Kan. LEXIS 167",
            "2015 WL 968451"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Perea-Rey",
          "cluster_id": 801335,
          "cite": [
            "680 F.3d 1179",
            "2012 U.S. App. LEXIS 10941",
            "2012 WL 1948973"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Drake v. Filko",
          "cluster_id": 1035893,
          "cite": [
            "724 F.3d 426",
            "2013 WL 3927735",
            "2013 U.S. App. LEXIS 15635"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ulbricht",
          "cluster_id": 4395694,
          "cite": [
            "858 F.3d 71",
            "2017 WL 2346566"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Aaron Graham",
          "cluster_id": 3208153,
          "cite": [
            "824 F.3d 421",
            "2016 WL 3068018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Quartavious Davis",
          "cluster_id": 2798570,
          "cite": [
            "785 F.3d 498",
            "2015 WL 2058977"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Fulton, I., Aplt.",
          "cluster_id": 4469590,
          "cite": [
            "179 A.3d 475"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neil Morgan v. Fairfield Cty., Ohio",
          "cluster_id": 4532978,
          "cite": [
            "903 F.3d 553"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Electronic Privacy Information Center v. United States Department of Homeland Security",
          "cluster_id": 2778134,
          "cite": [
            "414 U.S. App. D.C. 151",
            "777 F.3d 518",
            "2015 U.S. App. LEXIS 2043",
            "2015 WL 525183"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "American Civil Liberties Union v. Clapper",
          "cluster_id": 8442192,
          "cite": [
            "785 F.3d 787",
            "43 Media L. Rep. (BNA) 1649",
            "62 Communications Reg. (P&F) 945",
            "2015 U.S. App. LEXIS 7531",
            "2015 WL 2097814"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Earl Davis",
          "cluster_id": 2968788,
          "cite": [
            "690 F.3d 226",
            "2012 WL 3518479",
            "2012 U.S. App. LEXIS 17217"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nathaniel Holt, Jr.",
          "cluster_id": 2775033,
          "cite": [
            "777 F.3d 1234",
            "96 Fed. R. Serv. 747",
            "2015 WL 399128",
            "2015 U.S. App. LEXIS 1473"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nimesh Patel v. Facebook, Inc.",
          "cluster_id": 4646691,
          "cite": [
            "932 F.3d 1264"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(622304 OR 9485324 OR 9485325 OR 9485326) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDgwMzc3NjAwMDAwJnM9NDMyNTQ5NyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28622304+OR+9485324+OR+9485325+OR+9485326%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(622304 OR 9485324 OR 9485325 OR 9485326)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04NSZzPTQ0MDUyODImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28622304+OR+9485324+OR+9485325+OR+9485326%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(622304 OR 9485324 OR 9485325 OR 9485326)",
        "reviewed": 13,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 13,
        "triage_read": 0,
        "triage_snippet_classified": 13
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(622304 OR 9485324 OR 9485325 OR 9485326)",
    "indexed_citing_opinions": 584,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 622304,
        "count": 584,
        "count_source": "search"
      },
      {
        "opinion_id": 9485324,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9485325,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9485326,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 8,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-jones.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc1MzE4ODYmcz01MzAzNDYyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28622304+OR+9485324+OR+9485325+OR+9485326%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 622304,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 105021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 111600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 111833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 112218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 112795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 118354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 122246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 131154,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 152441,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 152929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 179601,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 215613,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 328036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 608150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 2311429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 2443377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 2574690,
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
    "date_created": "2026-07-06T00:55:27Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:56:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:56:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:01:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:56:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Jones

```
<opinion type="majority">
<author id="Ay9"><page-number citation-index="1" label="402">*402</page-number>Justice Scalia</author>
<p id="A-A">delivered the opinion of the Court.</p>
<p id="AJOK">We decide whether the attachment of a Global-Positioning-­System (GPS) tracking device to an individual’s vehicle, and subsequent use of that device to monitor the vehicle’s move­ments on public streets, constitutes a search or seizure within the meaning of the Fourth Amendment.</p>
<p id="Aem">HH</p>
<p id="Arl">In 2004 respondent Antoine Jones, owner and operator of a nightclub in the District of Columbia, came under suspicion of trafficking in narcotics and was made the target of an in­vestigation by a joint Federal Bureau of Investigation and Metropolitan Police Department task force. Officers em­ployed various investigative techniques, including visual sur­veillance of the nightclub, installation of a camera focused on the front door of the club, and a pen register and wiretap covering Jones’s cellular phone.</p>
<p id="AQN">Based in part on information gathered from these sources, in 2005 the Government applied to the United States District Court for the District of Columbia for a warrant authorizing the use of an electronic tracking device on the Jeep Grand Cherokee registered to Jones’s wife. A warrant issued, au­<page-number citation-index="1" label="403">*403</page-number>thorizing installation of the device in the District of Colum­bia and within 10 days.</p>
<p id="b617-5">On the 11th day, and not in the District of Columbia but in Maryland,<footnotemark>1</footnotemark> agents installed a GPS tracking device on the undercarriage of the Jeep while it was parked in a public parking lot. Over the next 28 days, the Government used the device to track the vehicle’s movements, and once had to replace the device’s battery when the vehicle was parked in a different public lot in Maryland. By means of signals from multiple satellites, the device established the vehicle’s loca­tion within 50 to 100 feet, and communicated that location by cellular phone to a Government computer. It relayed more than 2,000 pages of data over the 4-week period.</p>
<p id="b617-6">The Government ultimately obtained a multiple-count in­dictment charging Jones and several alleged co-conspirators with, as relevant here, conspiracy to distribute and possess with intent to distribute five kilograms or more of cocaine and 50 grams or more of cocaine base, in violation of <span class="citation no-link">21 U. S. C. §§ 841</span> and 846. Before trial, Jones filed a motion to suppress evidence obtained through the GPS device. The District Court granted the motion only in part, suppressing the data obtained while the vehicle was parked in the garage adjoining Jones’s residence. <span class="citation" data-id="2574690"><a href="/opinion/2574690/united-states-v-jones/#88" aria-description="Citation for case: United States v. Jones">451 F. Supp. 2d 71, 88</a></span> (2006). It held the remaining data admissible, because “ ‘[a] person traveling in an automobile on public thoroughfares has no reasonable expectation of privacy in his movements from one place to another.’ ” <em>Ibid, </em>(quoting <em>United States </em>v. <em>Knotts, </em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#281" aria-description="Citation for case: United States v. Knotts">460 U. S. 276, 281</a></span> (1983)). Jones’s trial in October 2006 produced a hung jury on the conspiracy count.</p>
<p id="b617-7">In March 2007, a grand jury returned another indictment, charging Jones and others with the same conspiracy. The Government introduced at trial the same GPS-derived loca­tional data admitted in the first trial, which connected Jones <page-number citation-index="1" label="404">*404</page-number>to the alleged conspirators’ stash house that contained $850,000 in cash, 97 kilograms of cocaine, and 1 kilogram of cocaine base. The jury returned a guilty verdict, and the District Court sentenced Jones to life imprisonment. The United States Court of Appeals for the District of Columbia Circuit reversed the conviction because of admis­sion of the evidence obtained by warrantless use of the GPS device which, it said, violated the Fourth Amendment. <em>United States </em>v. <em>Maynard, </em><span class="citation" data-id="152441"><a href="/opinion/152441/united-states-v-maynard/" aria-description="Citation for case: United States v. Maynard">615 F. 3d 544</a></span> (2010). The D. C. Circuit denied the Government’s petition for rehearing en banc, with four judges dissenting. <span class="citation" data-id="9438641"><a href="/opinion/179601/united-states-v-jones/" aria-description="Citation for case: United States v. Jones">625 F. 3d 766</a></span> (2010). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./564/1036/">564 U. S. 1036</a></span> (2011).</p>
<p id="AHl">1 — 1 1 — I</p>
<p id="ALr">A</p>
<p id="AR0">The Fourth Amendment provides in relevant part that “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated.” It is beyond dispute that a vehicle is an “effect” as that term is used in the Amendment. <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#12" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 12</a></span> (1977). We hold that the Government’s installation of a GPS device on a target’s vehicle,<footnotemark>2</footnotemark> and its use of that device to monitor the vehicle’s movements, constitutes a “search.”</p>
<p id="AKbo">It is important to be clear about what occurred in this case: The Government physically occupied private property for the purpose of obtaining information. We have no doubt that such a physical intrusion would have been considered a <page-number citation-index="1" label="405">*405</page-number>“search” within the meaning of the Fourth Amendment when it was adopted. <em>Entick </em>v. <em>Carrington, </em>95 Eng. Rep. 807 (C. P. 1765), is a “case we have described as a ‘monument of English freedom’ ‘undoubtedly familiar’ to ‘every American statesman’ at the time the Constitution was adopted, and considered to be ‘the true and ultimate expression of consti­tutional law’ ” with regard to search and seizure. <em>Brower </em>v. <em>County of Inyo, </em><span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/#596" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo">489 U. S. 593, 596</a></span> (1989) (quoting <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#626" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 626</a></span> (1886)). In that case, Lord Camden expressed in plain terms the significance of prop­erty rights in search-and-seizure analysis:</p>
<blockquote id="b619-5">“[O]ur law holds the property of every man so sacred, that no man can set his foot upon his neighbour’s close without his leave; if he does he is a trespasser, though he does no damage at all; if he will tread upon his neigh-­bour’s ground, he must justify it by law.” <em>Entick, swpra, </em>at 817.</blockquote>
<p id="b619-6">The text of the Fourth Amendment reflects its close connec­tion to property, since otherwise it would have referred simply to “the right of the people to be secure against unrea­sonable searches and seizures”; the phrase “in their persons, houses, papers, and effects” would have been superfluous.</p>
<p id="b619-7">Consistent with this understanding, our Fourth Amend­ment jurisprudence was tied to common-law trespass, at least until the latter half of the 20th century. <em>Kyllo </em>v. <em>United States, </em><span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/#31" aria-description="Citation for case: Kyllo v. United States">533 U. S. 27, 31</a></span> (2001); Kerr, The Fourth Amendment and New Technologies: Constitutional Myths and the Case for Caution, <span class="citation no-link">102 Mich. L. Rev. 801</span>, 816 (2004). Thus, in <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span> (1928), we held that wiretaps attached to telephone wires on the public streets did not constitute a Fourth Amendment search be­cause “ft]here was no entry of the houses or offices of the defendants,” <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#464" aria-description="Citation for case: Olmstead v. United States"><em>id., </em>at 464</a></span>.</p>
<p id="b619-8">Our later cases, of course, have deviated from that exclu­sively property-based approach. In <em>Katz </em>v. <em>United States, </em><page-number citation-index="1" label="406">*406</page-number><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967), we said that “the Fourth Amend­ment protects people, not places,” and found a violation in attachment of an eavesdropping device to a public telephone booth. Our later cases have applied the analysis of Justice Harlan’s concurrence in that case, which said that a violation occurs when government officers violate a person’s “reason­able expectation of privacy,” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States"><em>id., </em>at 360</a></span>. See, <em>e. g., Bond </em>v. <em>United States, </em><span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">529 U. S. 334</a></span> (2000); <em>California </em>v. <em>Ciraolo, </em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207</a></span> (1986); <em>Smith </em>v. <em>Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735</a></span> (1979).</p>
<p id="b620-5">The Government contends that the Harlan standard shows that no search occurred here, since Jones had no “reasonable expectation of privacy” in the area of the Jeep accessed by Government agents (its underbody) and in the locations of the Jeep on the public roads, which were visible to all. But we need not address the Government’s contentions, because Jones’s Fourth Amendment rights do not rise or fall with the <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>formulation. At bottom, we must “assur[e] preserva­tion of that degree of privacy against government that ex­isted when the Fourth Amendment was adopted.” <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/#34" aria-description="Citation for case: Kyllo v. United States"><em>Kyllo, supra, </em>at 34</a></span>. As explained, for most of our history the Fourth Amendment was understood to embody a particular concern for government trespass upon the areas (“persons, houses, papers, and effects”) it enumerates.<footnotemark>3</footnotemark> <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>did not <page-number citation-index="1" label="407">*407</page-number>repudiate that understanding. Less than two years later the Court upheld defendants’ contention that the Govern­ment could not introduce against them conversations be­tween <em>other </em>people obtained by warrantless placement of electronic surveillance devices in their homes. The opinion rejected the dissent’s contention that there was no Fourth Amendment violation “unless the conversational privacy of the homeowner himself is invaded.”<footnotemark>4</footnotemark> <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#176" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 176</a></span> (1969). “[W]e [do not] believe that <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>by holding that the Fourth Amendment protects per­sons and their private conversations, was intended to with­draw any of the protection which the Amendment extends to the home .. . .” <em>Id., </em>at 180.</p>
<p id="b621-5">More recently, in <em>Soldal </em>v. <em>Cook County, </em><span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/" aria-description="Citation for case: Soldal v. Cook County">506 U. S. 56</a></span> (1992), the Court unanimously rejected the argument that although a “seizure” had occurred “in a ‘technical’ sense” when a trailer home was forcibly removed, <span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/#62" aria-description="Citation for case: Soldal v. Cook County"><em>id., </em>at 62</a></span>, no Fourth Amendment violation occurred because law enforce­ment had not “invade[d] the [individuals’] privacy,” <span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/#60" aria-description="Citation for case: Soldal v. Cook County"><em>id., </em>at 60</a></span>. <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>the Court explained, established that “property rights are not the sole measure of Fourth Amendment violations,” but did not “snuf[f] out the previously recognized protection for property.” <span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/#64" aria-description="Citation for case: Soldal v. Cook County">506 U. S., at 64</a></span>. As Justice Brennan ex­plained in his concurrence in <em>Knotts, Katz </em>did not erode the principle “that, when the Government <em>does </em>engage in physi­cal intrusion of a constitutionally protected area in order to obtain information, that intrusion may constitute a violation of the Fourth Amendment.” <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#286" aria-description="Citation for case: United States v. Knotts">460 U. S., at 286</a></span> (opinion con­curring in judgment). We have embodied that preservation <page-number citation-index="1" label="408">*408</page-number>of past rights in our very definition of “reasonable expecta­tion of privacy” which we have said to be an expectation “that has a source outside of the Fourth Amendment, either by reference to concepts of real or personal property law or to understandings that are recognized and permitted by society.” <em>Minnesota </em>v. <em>Carter, </em><span class="citation" data-id="9433723"><a href="/opinion/118249/minnesota-v-carter/#88" aria-description="Citation for case: Minnesota v. Carter">525 U. S. 83, 88</a></span> (1998) (inter­nal quotation marks omitted). <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>did not narrow the Fourth Amendment’s scope.<footnotemark>5</footnotemark></p>
<p id="b622-5">The Government contends that several of our post-Aate cases foreclose the conclusion that what occurred here consti­tuted a search. It relies principally on two cases in which we rejected Fourth Amendment challenges to “beepers,” electronic tracking devices that represent another form of electronic monitoring. The first ease, <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span>, </em>upheld against Fourth Amendment challenge the use of a “beeper” that had been placed in a container of chloroform, allowing law enforcement to monitor the location of the container. <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#278" aria-description="Citation for case: United States v. Knotts">460 U. S., at 278</a></span>. We said that there had been no infringe­ment of Knotts’ reasonable expectation of privacy since the information obtained — the location of the automobile carry­<page-number citation-index="1" label="409">*409</page-number>ing the container on public roads, and the location of the off­loaded container in open fields near Knotts’ cabin — had been voluntarily conveyed to the public.<footnotemark>6</footnotemark> <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#281" aria-description="Citation for case: United States v. Knotts"><em>Id., </em>at 281-282</a></span>. But as we have discussed, the <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>reasonable-expeetation-of-­privacy test has been <em>added to, </em>not <em>substituted for, </em>the common-law trespassory test. The holding in <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span> </em>ad­dressed only the former, since the latter was not at issue. The beeper had been placed in the container before it came into Knotts’ possession, with the consent of the then-owner. <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#278" aria-description="Citation for case: United States v. Knotts">460 U. S., at 278</a></span>. Knotts did not challenge that installation, and we specifically declined to consider its effect on the Fourth Amendment analysis. <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#279" aria-description="Citation for case: United States v. Knotts"><em>Id., </em>at 279</a></span>, n. <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span> </em>would be relevant, perhaps, if the Government were making the argument that what would otherwise be an unconstitutional search is not such where it produces only public information. The Government does not make that argument, and we know of no case that would support it.</p>
<p id="b623-5">The second “beeper” case, <em>United States </em>v. <em>Karo, </em>468 U. S.-­705 (1984), does not suggest a different conclusion. There we addressed the question left open by <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span>, </em>whether the installation of a beeper in a container amounted to a search or seizure. 468 U. S., at 713. As in <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span>, </em>at the time the beeper was installed the container belonged to a third party, and it did not come into possession of the defendant until later. 468 U. S., at 708. Thus, the specific question we con­sidered was whether the installation <em>“with the consent of the original owner </em>constitute^] a search or seizure . . . when the container is delivered to a buyer having no knowledge of the presence of the beeper.” <em>Id., </em>at 707 (emphasis added). We held not. The Government, we said, came into physical contact with the container only before it belonged to the de­<page-number citation-index="1" label="410">*410</page-number>fendant Karo; and the transfer of the container with the un­monitored beeper inside did not convey any information and thus did not invade Karo’s privacy. See <em>id., </em>at 712. That conclusion is perfectly consistent with the one we reach here. Karo accepted the container as it came to him, beeper and all, and was therefore not entitled to object to the beeper’s presence, even though it was used to monitor the container’s location. Cf. <em>On Lee </em>v. <em>United States, </em><span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/#751" aria-description="Citation for case: On Lee v. United States">343 U. S. 747, 751-752</a></span> (1952) (no search or seizure where an informant, who was wearing a concealed microphone, was invited into the defend­ant’s business). Jones, who possessed the Jeep at the time the Government trespassorily inserted the information-­gathering device, is on much different footing.</p>
<p id="b624-5">The Government also points to our exposition in <em>New York </em>v. <em>Class, </em><span class="citation" data-id="9430353"><a href="/opinion/111600/new-york-v-class/" aria-description="Citation for case: New York v. Class">475 U. S. 106</a></span> (1986), that “[t]he exterior of a car . .. is thrust into the public eye, and thus to examine it does not constitute a ‘search.’ ” <span class="citation" data-id="9430353"><a href="/opinion/111600/new-york-v-class/#114" aria-description="Citation for case: New York v. Class"><em>Id., </em>at 114</a></span>. That statement is of marginal relevance here since, as the Government acknowl­edges, “the officers in this ease did <em>more </em>than conduct a visual inspection of respondent’s vehicle,” Brief for United States 41 (emphasis added). By attaching the device to the Jeep, officers encroached on a protected area. In <em><span class="citation" data-id="9430353"><a href="/opinion/111600/new-york-v-class/" aria-description="Citation for case: New York v. Class">Class</a></span> </em>it­self we suggested that this would make a difference, for we concluded that an officer’s momentary reaching into the interior of a vehicle did constitute a search.<footnotemark>7</footnotemark> <span class="citation" data-id="9430353"><a href="/opinion/111600/new-york-v-class/#114" aria-description="Citation for case: New York v. Class">475 U. S., at 114-115</a></span>.</p>
<p id="b624-6">Finally, the Government’s position gains little support from our conclusion in <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U. S. 170</a></span> <page-number citation-index="1" label="411">*411</page-number>(1984), that officers’ information-gathering intrusion on an “open field” did not constitute a Fourth Amendment search even though it was a trespass at common law, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#183" aria-description="Citation for case: Oliver v. United States"><em>id., </em>at 183</a></span>. Quite simply, an open field, unlike the curtilage of a home, see <em>United States </em>v. <em>Dunn, </em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/#300" aria-description="Citation for case: United States v. Dunn">480 U. S. 294, 300</a></span> (1987), is not one of those protected areas enumerated in the Fourth Amendment. <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#176" aria-description="Citation for case: Oliver v. United States"><em>Oliver, supra, </em>at 176-177</a></span>. See also <em>Hester </em>v. <em>United States, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#59" aria-description="Citation for case: Hester v. United States">265 U. S. 57, 59</a></span> (1924). The Government’s physical intrusion on such an area — unlike its intrusion on the “effect” at issue here — is of no Fourth Amendment significance.<footnotemark>8</footnotemark></p>
<p id="b625-5">B</p>
<p id="b625-6">The concurrence begins by accusing us of applying “18th-­century tort law.” <em>Post, </em>at 418. That is a distortion. What we apply is an 18th-century guarantee against unreasonable searches, which we believe must provide <em>at a minimum </em>the degree of protection it afforded when it was adopted. The concurrence does not share that belief. It would apply <em>ex­clusively Katz’s </em>reasonable-expectation-of-privacy test, even when that eliminates rights that previously existed.</p>
<p id="b625-7">The concurrence faults our approach for “presenting] par­ticularly vexing problems” in cases that do not involve physi­cal contact, such as those that involve the transmission of electronic signals. <em>Post, </em>at 426. We entirely fail to under­stand that point. For unlike the concurrence, which would make <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>the <em>exclusive </em>test, we do not make trespass the exclusive test. Situations involving merely the transmission of electronic signals without trespass would <em>remain </em>subject to <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>analysis.</p>
<p id="b626-4"><page-number citation-index="1" label="412">*412</page-number>In fact, it is the concurrence’s insistence on the exclusivity of the <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>test that needlessly leads us into “particularly vexing problems” in the present case. This Court has to date not deviated from the understanding that mere visual observation does not constitute a search. See <em>Kyllo, </em><span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/#31" aria-description="Citation for case: Kyllo v. United States">533 U. S., at 31-32</a></span>. We accordingly held in <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span> </em>that “[a] per­son traveling in an automobile on public thoroughfares has no reasonable expectation of privacy in his movements from one place to another.” <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#281" aria-description="Citation for case: United States v. Knotts">460 U. S., at 281</a></span>. Thus, even assum­ing that the concurrence is correct to say that “[tjraditional surveillance” of Jones for a 4-week period “would have re­quired a large team of agents, multiple vehicles, and perhaps aerial assistance,” <em>post, </em>at 429, our cases suggest that such visual observation is constitutionally permissible. It may be that achieving the same result through electronic means, without an accompanying trespass, is an unconstitutional in­vasion of privacy, but the present case does not require us to answer that question.</p>
<p id="b626-5">And answering it affirmatively leads us needlessly into ad­ditional thorny problems. The concurrence posits that “rel­atively short-term monitoring of a person’s movements on public streets” is okay, but that “the use of longer term GPS monitoring in investigations <em>of most offenses” </em>is no good. <em>Post, </em>at 430 (emphasis added). That introduces yet another novelty into our jurisprudence. There is no precedent for the proposition that whether a search has occurred depends on the nature of the crime being investigated. And even accepting that novelty, it remains unexplained why a 4-week investigation is “surely” too long and why a drug-trafficking conspiracy involving substantial amounts of cash and narcot­ics is not an “extraordinary offens[e]” which may permit longer observation. See <em>post, </em>at 430-431. What of a 2-day monitoring of a suspected purveyor of stolen electronics? Or of a 6-month monitoring of a suspected terrorist? We may have to grapple with these “vexing problems” in some future case where a classic trespassory search is not involved <page-number citation-index="1" label="413">*413</page-number>and resort must be had to <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>analysis; but there is no reason for rushing forward to resolve them here.</p>
<p id="AnBW">III</p>
<p id="A3H">The Government argues in the alternative that even if the attachment and use of the device was a search, it was reasonable — and thus lawful — under the Fourth Amend­ment because “officers had reasonable suspicion, and indeed probable cause, to believe that [Jones] was a leader in a large-scale cocaine distribution conspiracy.” Brief for United States 50-51. We have no occasion to consider this argument. The Government did not raise it below, and the D. C. Circuit therefore did not address it. See <span class="citation" data-id="9438641"><a href="/opinion/179601/united-states-v-jones/#767" aria-description="Citation for case: United States v. Jones">625 F. 3d, at 767</a></span> (Ginsburg, Tatel, and Griffith, JJ., concurring in de­nial of rehearing en banc). We consider the argument for­feited. See <em>Sprietsma </em>v. <em>Mercury Marine, </em><span class="citation" data-id="122246"><a href="/opinion/122246/sprietsma-v-mercury-marine/#56" aria-description="Citation for case: Sprietsma v. Mercury Marine">537 U. S. 51, 56, n. 4</a></span> (2002).</p>
<p id="AYc">* * *</p>
<p id="AjG">The judgment of the Court of Appeals for the D. C. Circuit is affirmed.</p>
<p id="AJT-">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b617-8"> In this litigation, the Government has conceded noncompliance with the warrant and has argued only that a warrant was not required. <em>United States </em>v. <em>Maynard, </em><span class="citation" data-id="152441"><a href="/opinion/152441/united-states-v-maynard/#566" aria-description="Citation for case: United States v. Maynard">615 F. 3d 544, 566</a></span>, n. (CADC 2010).</p>
</footnote>
<footnote label="2">
<p id="AAu4"> As we have noted, the Jeep was registered to Jones’s wife. The Gov­ernment acknowledged, however, that Jones was “the exclusive driver.” <span class="citation" data-id="152441"><a href="/opinion/152441/united-states-v-maynard/#555" aria-description="Citation for case: United States v. Maynard"><em>Id., </em>at 555</a></span>, n. (internal quotation marks omitted). If Jones was not the owner he had at least the property rights of a bailee. The Court of Ap­peals concluded that the vehicle’s registration did not affect his ability to make a Fourth Amendment objection, <em>ibid., </em>and the Government has not challenged that determination here. We therefore do not consider the Fourth Amendment significance of Jones’s status.</p>
</footnote>
<footnote label="3">
<p id="b620-6"> Justice Alito’s concurrence (hereinafter concurrence) doubts the wis­dom of our approach because “it is almost impossible to think of late-18th­century situations that are analogous to what took place in this case.” <em>Post, </em>at 420 (opinion concurring in judgment). But in fact it posits a sit­uation that is not far afield — a constable’s concealing himself in the target’s coach in order to track its movements. <em><span class="citation" data-id="152441"><a href="/opinion/152441/united-states-v-maynard/" aria-description="Citation for case: United States v. Maynard">Ibid.</a></span> </em>There is no doubt that the information gained by that trespassory activity would be the product of an unlawful search — whether that information consisted of the conversations occurring in the coach, or of the destinations to which the coach traveled.</p>
<p id="b620-7">In any case, it is quite irrelevant whether there was an 18th-century analog. Whatever new methods of investigation may be devised, our task, <em>at a minimum, </em>is to decide whether the action in question would have constituted a “search” within the original meaning of the Fourth Amendment. Where, as here, the Government obtains information by <page-number citation-index="1" label="407">*407</page-number>physically intruding on a constitutionally protected area, such a search has undoubtedly occurred.</p>
</footnote>
<footnote label="4">
<p id="b621-8"><em> </em>Thus, the concurrence’s attempt to recast <em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">Alderman</a></span> </em>as meaning that individuals have a “legitimate expectation of privacy in all conversations that [take] place under their roof,” <em>'post, </em>at 423-424, is foreclosed by the Court’s opinion. The Court took as a given that the homeowner’s “con­versational privacy” had not been violated.</p>
</footnote>
<footnote label="5">
<p id="b622-6"> The concurrence notes that post-Aate we have explained that <em>“ </em>‘an ac­tual trespass is neither necessary <em>nor sufficient </em>to establish a constitu­tional violation.’” <em>Post, </em>at 423 (quoting <em>United States </em>v. <em>Karo, </em><span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/#713" aria-description="Citation for case: United States v. Karo">468 U. S. 705, 713</a></span> (1984)). That is undoubtedly true, and undoubtedly irrelevant. <em><span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/" aria-description="Citation for case: United States v. Karo">Karo</a></span> </em>was considering whether a seizure occurred, and as the concurrence explains, a seizure of property occurs, not when there is a trespass, but “when there is some meaningful interference with an individual’s posses-­sory interests in that property.” <em>Post, </em>at 419 (internal quotation marks omitted). Likewise with a search. Trespass alone does not qualify, but there must be conjoined with that what was present here: an attempt .to find something or to obtain information.</p>
<p id="b622-7">Related to this, and similarly irrelevant, is the concurrence’s point that, if analyzed separately, neither the installation of the device nor its use would constitute a Fourth Amendment search. See <em>post, </em>at 420. Of course not. A trespass on “houses” or “effects,” or a <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>invasion of privacy, is not alone a search unless it is done to obtain information; and the obtaining of information is not alone a search unless it is achieved by such a trespass or invasion of privacy.</p>
</footnote>
<footnote label="6">
<p id="b623-6"> <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span> </em>noted the “limited use which the government made of the sig­nals from this particular beeper,” <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#284" aria-description="Citation for case: United States v. Knotts">460 U. S., at 284</a></span>, and reserved the ques­tion whether “different constitutional principles may be applicable” to “dragnet-type law enforcement practices” of the type that GPS tracking made possible here, <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">ibid.</a></span></em></p>
</footnote>
<footnote label="7">
<p id="b624-7"> The Government also points to <em>Cardwell </em>v. <em>Lewis, </em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583</a></span> (1974), in which the Court rejected the claim that the inspection of an impounded vehicle’s tire tread and the collection of paint scrapings from its exterior violated the Fourth Amendment. Whether the plurality said so because no search occurred or because the search was reasonable is unclear. Com­pare <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#591" aria-description="Citation for case: Cardwell v. Lewis"><em>id., </em>at 591</a></span> (opinion of Blackmun, J.) (“[W]e fail to comprehend what expectation of privacy was infringed”), with <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#592" aria-description="Citation for case: Cardwell v. Lewis"><em>id., </em>at 592</a></span> (“Under circum­stances such as these, where probable cause exists, a warrantless examina­tion of the exterior of a car is not unreasonable ... ”).</p>
</footnote>
<footnote label="8">
<p id="b625-8"> Thus, our theory is <em>not </em>that the Fourth Amendment is concerned with <em>“any </em>technical trespass that led to the gathering of evidence.” <em>Post, </em>at 420 (Alito, J., concurring in judgment) (emphasis added). The Fourth Amendment protects against trespassory searches only with regard to those items (“persons, houses, papers, and effects”) that it enumerates. The trespass that occurred in <em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver</a></span> </em>may properly be understood as a “search,” but not one “in the constitutional sense.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#170" aria-description="Citation for case: Oliver v. United States">466 U. S., at 170,183</a></span>.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Karo.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Karo"
type: case
citation: "468 U.S. 705 (1984)"
parallel_cite: "104 S. Ct. 3296; 82 L. Ed. 2d 530"
neutral_cite: 1984 U.S. LEXIS 148
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-09-18
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: null
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Karo
  varies_by_point: false
  scope_note: "Good law; the rule that monitoring a tracking device inside a private residence is a search requiring a warrant remains controlling and was reinforced by the trespass/aggregation analyses of United States v. Jones and Carpenter."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111257/united-states-v-karo/"
  cluster_id: 111257
  opinion_id: 9429751
  identity_checked: true
homes:
  - page: "[[Real-Time Tracking]]"
    role: "Key — Anchor (interior context-flip)"
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Related (cross-ref — umbrella)"
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Knotts]]", "[[Kyllo v. United States]]", "[[United States v. Jones]]", "[[Carpenter v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "beeper", "tracking", "surveillance", "home"]
holding: "Monitoring a beeper inside a private residence — a location not open to visual surveillance — is a Fourth Amendment search requiring a warrant, because it reveals a critical fact about the interior of the home."
lake:
  record_id: United States v. Karo
  status: verified
  projected_at: 2026-07-06
---

# United States v. Karo

*468 U.S. 705 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
With the informant-seller's consent, agents placed a beeper in a can of ether that Karo and others bought to extract cocaine. Agents monitored the beeper as the ether moved among vehicles and houses, including while it was inside a private residence, and used the in-house signal to confirm the ether's location and obtain a search warrant. Karo challenged the warrantless monitoring of the beeper while it was inside the home.

## Issue
Whether the warrantless monitoring of a beeper inside a private residence — a location not open to visual surveillance — violates the Fourth Amendment rights of those with a justifiable privacy interest in the residence.

## Rule
Yes. "This case . . . presents the question whether the monitoring of a beeper in a private residence, a location not open to visual surveillance, violates the Fourth Amendment rights of those who have a justifiable interest in the privacy of the residence. Contrary to the submission of the United States, we think that it does." — 468 U.S. at 714. ^pin-714

The decisive point is that the device reveals interior facts unobtainable from outside: the monitoring "does reveal a critical fact about the interior of the premises that the Government is extremely interested in knowing and that it could not have otherwise obtained without a warrant. The case is thus not like *Knotts*, for there the beeper told the authorities nothing about the interior of Knotts' cabin." — *Id.* at 715. ^pin-715

## Application
Agents used the beeper to establish that the ether was *inside* a particular residence — a fact they could not have verified by lawful outside observation. Because warrantless searches of a home are presumptively unreasonable, electronically determining that a specific article is within the home, without a warrant, was an unreasonable search. The Court contrasted this with public-road tracking ([[United States v. Knotts]]), where the beeper revealed only movements exposed to public view.

## Conclusion
Warrantless monitoring of the beeper inside the residence violated the Fourth Amendment. Paired with [[United States v. Knotts]], *Karo* draws the home/public line for location-tracking technology: tracking inside the home is a search; tracking public movements is not.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Companion to [[United States v. Knotts]]. Its interior-of-the-home reasoning anticipates [[Kyllo v. United States]] (sense-enhancing technology and the home) and the modern location-tracking cases [[United States v. Jones]] (trespassory GPS installation) and [[Carpenter v. United States]] (long-term cell-site aggregation).

## Appears on
- [[Real-Time Tracking]] — *Key — Anchor (interior context-flip)*
- [[Third-Party Doctrine & CSLI]] — *Related (cross-ref — umbrella)*
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*

## Sources
- *United States v. Karo*, 468 U.S. 705 (1984) — https://www.courtlistener.com/opinion/111257/united-states-v-karo/ — pinpoints: 714, 715.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "17a4cba35606a290", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Karo"}, "payload": {"all": [{"cite": "468 U.S. 705", "page": "705", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "468"}, {"cite": "104 S. Ct. 3296", "page": "3296", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "104"}, {"cite": "82 L. Ed. 2d 530", "page": "530", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "82"}, {"cite": "1984 U.S. LEXIS 148", "page": "148", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1984"}], "display": "468 U.S. 705", "official": {"cite": "468 U.S. 705", "page": "705", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "468"}, "official_selection_present": true, "record_id": "United States v. Karo"}}
{"assertion_id": "790b0016f2365e4a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-715", "record_id": "United States v. Karo"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-715", "pinpoint_status": "slip-only", "quote": "does reveal a critical fact about the interior of the premises that the Government is extremely interested in knowing and that it could not have otherwise obtained without a warrant. The case is thus not like *Knotts*, for there the beeper told the authorities nothing about the interior of Knotts' cabin.", "quote_fidelity": "mismatch", "record_id": "United States v. Karo", "star_marker": null}}
{"assertion_id": "e2d8c2cda7e5d932", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-714", "record_id": "United States v. Karo"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-714", "pinpoint_status": "slip-only", "quote": "--- # United States v. Karo *468 U.S. 705 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background With the informant-seller's consent, agents placed a beeper in a can of ether that Karo and others bought to extract cocaine. Agents monitored the beeper as the ether moved among vehicles and houses, including while it was inside a private residence, and used the in-house signal to confirm the ether's location and obtain a search warrant. Karo challenged the warrantless monitoring of the beeper while it was inside the home. ## Issue Whether the warrantless monitoring of a beeper inside a private residence — a location not open to visual surveillance — violates the Fourth Amendment rights of those with a justifiable privacy interest in the residence. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "United States v. Karo", "star_marker": null}}
{"assertion_id": "406a24c29dd19675", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Karo"}, "payload": {"as_of_content": null, "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Karo", "scope_note": "Good law; the rule that monitoring a tracking device inside a private residence is a search requiring a warrant remains controlling and was reinforced by the trespass/aggregation analyses of United States v. Jones and Carpenter.", "varies_by_point": false}}
```

### lake record — United States v. Karo

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Karo",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Karo",
    "case_name_short": "Karo",
    "case_name_full": "UNITED STATES v. KARO Et Al.",
    "input_case_name": "United States v. Karo",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-09-18",
    "year": 1984,
    "docket": null,
    "cluster_id": 111257,
    "lead_opinion_id": 9429751,
    "sibling_ids": [
      111257,
      9429751,
      9429752,
      9429753
    ],
    "absolute_url": "/opinion/111257/united-states-v-karo/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "468 U.S. 705",
      "volume": "468",
      "reporter": "U.S.",
      "page": "705",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 3296",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3296",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 530",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "530",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 148",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "148",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "468 U.S. 705",
        "volume": "468",
        "reporter": "U.S.",
        "page": "705",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 3296",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3296",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 530",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "530",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 148",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "148",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "468 U.S. 705",
    "official_selection": {
      "court_class": "scotus",
      "selected": "468 U.S. 705",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-714",
      "page": null,
      "quote": "--- # United States v. Karo *468 U.S. 705 (1984)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background With the informant-seller's consent, agents placed a beeper in a can of ether that Karo and others bought to extract cocaine. Agents monitored the beeper as the ether moved among vehicles and houses, including while it was inside a private residence, and used the in-house signal to confirm the ether's location and obtain a search warrant. Karo challenged the warrantless monitoring of the beeper while it was inside the home. ## Issue Whether the warrantless monitoring of a beeper inside a private residence \u2014 a location not open to visual surveillance \u2014 violates the Fourth Amendment rights of those with a justifiable privacy interest in the residence. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-715",
      "page": null,
      "quote": "does reveal a critical fact about the interior of the premises that the Government is extremely interested in knowing and that it could not have otherwise obtained without a warrant. The case is thus not like *Knotts*, for there the beeper told the authorities nothing about the interior of Knotts' cabin.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": null,
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Karo",
    "varies_by_point": false,
    "scope_note": "Good law; the rule that monitoring a tracking device inside a private residence is a search requiring a warrant remains controlling and was reinforced by the trespass/aggregation analyses of United States v. Jones and Carpenter.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "United States v. Karo:lane1_negative"
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
        "journal_ref": "United States v. Karo:lane1_negative"
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
        "journal_ref": "United States v. Karo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4288590,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4287047,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4286131,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Robert Hill",
          "cluster_id": 2769569,
          "cite": [
            "776 F.3d 243"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Augustine",
          "cluster_id": 6580805,
          "cite": [
            "467 Mass. 230",
            "4 N.E.3d 846",
            "2014 WL 901649",
            "2014 Mass. LEXIS 30"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane1_negative"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyllo v. United States",
          "cluster_id": 118443,
          "cite": [
            "150 L. Ed. 2d 94",
            "121 S. Ct. 2038",
            "533 U.S. 27",
            "2001 U.S. LEXIS 4487"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Carney",
          "cluster_id": 111423,
          "cite": [
            "85 L. Ed. 2d 406",
            "105 S. Ct. 2066",
            "471 U.S. 386",
            "1985 U.S. LEXIS 8",
            "53 U.S.L.W. 4521"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Daniel Good Real Property",
          "cluster_id": 112914,
          "cite": [
            "126 L. Ed. 2d 490",
            "114 S. Ct. 492",
            "510 U.S. 43",
            "1993 U.S. LEXIS 7941",
            "7 Fla. L. Weekly Fed. S 665",
            "93 Daily Journal DAR 15706",
            "93 Cal. Daily Op. Serv. 9143",
            "62 U.S.L.W. 4013",
            "1993 WL 505539"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bowers v. Hardwick",
          "cluster_id": 111738,
          "cite": [
            "92 L. Ed. 2d 140",
            "106 S. Ct. 2841",
            "478 U.S. 186",
            "1986 U.S. LEXIS 123"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bull",
          "cluster_id": 1998703,
          "cite": [
            "705 N.E.2d 824",
            "185 Ill. 2d 179",
            "235 Ill. Dec. 641",
            "1998 Ill. LEXIS 1578"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dow Chemical Co. v. United States Ex Rel. Administrator",
          "cluster_id": 111667,
          "cite": [
            "90 L. Ed. 2d 226",
            "106 S. Ct. 1819",
            "476 U.S. 227",
            "1986 U.S. LEXIS 155",
            "16 Envtl. L. Rep. (Envtl. Law Inst.) 20679",
            "54 U.S.L.W. 4464",
            "24 ERC (BNA) 1385"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hector Vega-Rodriguez v. Puerto Rico Telephone Company",
          "cluster_id": 739069,
          "cite": [
            "110 F.3d 174",
            "12 I.E.R. Cas. (BNA) 1253",
            "1997 U.S. App. LEXIS 6517",
            "1997 WL 154362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Young",
          "cluster_id": 1196592,
          "cite": [
            "867 P.2d 593",
            "123 Wash. 2d 173",
            "1994 Wash. LEXIS 122"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. 4492 South Livonia Road",
          "cluster_id": 8983256,
          "cite": [
            "889 F.2d 1258",
            "1989 U.S. App. LEXIS 17524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Henry Morgan",
          "cluster_id": 441786,
          "cite": [
            "743 F.2d 1158",
            "1984 U.S. App. LEXIS 18632"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jimmy Dewitt Webster, Sr., Candido Daniel Santiago, Barry Weinreich, Joe Buhajla, Arthur Byron Murphy, and Clarence Royalston",
          "cluster_id": 445460,
          "cite": [
            "750 F.2d 307"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4621444,
          "cite": [
            "2019 CO 36",
            "446 P.3d 397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111257 OR 9429751 OR 9429752 OR 9429753) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjEwODA5NjAwMDAwJnM9MjkyNTU3MCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111257+OR+9429751+OR+9429752+OR+9429753%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111257 OR 9429751 OR 9429752 OR 9429753)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDEmcz01ODAwMjgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111257+OR+9429751+OR+9429752+OR+9429753%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111257 OR 9429751 OR 9429752 OR 9429753)",
        "reviewed": 20,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 20,
        "triage_read": 0,
        "triage_snippet_classified": 20
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111257 OR 9429751 OR 9429752 OR 9429753)",
    "indexed_citing_opinions": 567,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111257,
        "count": 497,
        "count_source": "search"
      },
      {
        "opinion_id": 9429751,
        "count": 82,
        "count_source": "search"
      },
      {
        "opinion_id": 9429752,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429753,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 895,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-karo.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1ODM2Nzkmcz0xMDYzMTUxNCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111257+OR+9429751+OR+9429752+OR+9429753%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111257,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 108967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 109925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 110325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 111013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 420988,
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
    "date_created": "2026-07-06T01:01:16Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:01:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:01:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:06:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:01:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Karo

```
<opinion type="majority">
<author id="b749-6">Justice White</author>
<p id="Ark">delivered the opinion of the Court.</p>
<p id="b749-7">In <em>United States </em>v. <em>Knotts, </em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">460 U. S. 276</a></span> (1983), we held that the warrantless monitoring of an electronic tracking device (“beeper”)<footnotemark>1</footnotemark> inside a container of chemicals did not violate the Fourth Amendment when it revealed no information that could not have been obtained through visual surveillance. In this case, we are called upon to address two questions left unresolved in <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span>: </em>(1) whether installation of a beeper in a container of chemicals with the consent of the original owner constitutes a search or seizure within the meaning of the Fourth Amendment when the container is delivered to a buyer having no knowledge of the presence of the beeper, and (2) whether monitoring of a beeper falls within the ambit of the Fourth Amendment when it reveals information that could not have been obtained through visual surveillance.</p>
<p id="b750-3"><page-number citation-index="1" label="708">*708</page-number>I</p>
<p id="b750-4">In August 1980 Agent Rottinger of the Drug Enforcement Administration (DEA) learned that respondents James Karo, Richard Horton, and William Harley had ordered 50 gallons of ether from Government informant Carl Muehlenweg of Graphic Photo Design in Albuquerque, N. M. Muehlenweg told Rottinger that the ether was to be used to extract cocaine from clothing that had been imported into the United States. The Government obtained a court order authorizing the installation and monitoring of a beeper in one of the cans of ether. With Muehlenweg’s consent, agents substituted their own can containing a beeper for one of the cans in the shipment and then had all 10 cans painted to give them a uniform appearance.</p>
<p id="b750-5">On September 20, 1980, agents saw Karo pick up the ether from Muehlenweg. They then followed Karo to his house using visual and beeper surveillance. At one point later that day, agents determined by using the beeper that the ether was still inside the house, but they later determined that it had been moved undetected to Horton’s house, where they located it using the beeper. Agent Rottinger could smell the ether from the public sidewalk near Horton’s residence. Two days later, agents discovered that the ether had once again been moved, and, using the beeper, they located it at the residence of Horton’s father. The next day, the beeper was no longer transmitting from Horton’s father’s house, and agents traced the beeper to a commercial storage facility.</p>
<p id="b750-6">Because the beeper equipment was not sensitive enough to allow agents to learn precisely which locker the ether was in, agents obtained a subpoena for the records of the storage company and learned that locker 143 had been rented by Horton. Using the beeper, agents confirmed that the ether was indeed in one of the lockers in the row containing locker 143, and using their noses they detected the odor of ether emanating from locker 143. On October 8 agents obtained an order authorizing installation of an entry tone alarm into the door <page-number citation-index="1" label="709">*709</page-number>jamb of the locker so they would be able to tell when the door was opened. While installing the alarm, agents observed that the cans containing ether were still inside. Agents ceased visual and beeper surveillance, relying instead on the entry tone alarm. However, on October 16 Horton retrieved the contents from the locker without sounding the alarm. Agents did not learn of the entry until the manager of the storage facility notified them that Horton had been there.</p>
<p id="b751-5">Using the beeper, agents traced the beeper can to another self-storage facility three days later. Agents detected the smell of ether coming from locker 15 and learned from the manager that Horton and Harley had rented that locker using an alias the same day that the ether had been removed from the first storage facility. The agents obtained an order authorizing the installation of an entry tone alarm in locker 15, but instead of installing that alarm, they obtained consent from the manager of the facility to install a closed-circuit video camera in a locker that had a view of locker 15. On February 6, 1981, agents observed, by means of the video camera, Gene Rhodes and an unidentified woman removing the cans from the locker and loading them onto the rear bed of Horton’s pickup truck. Using both visual and beeper surveillance agents tracked the truck to Rhodes’ residence where it was parked in the driveway. Agents then observed Rhodes and a woman bringing boxes and other items from inside the house and loading the items into the trunk of an automobile. Agents did not see any cans being transferred from the pickup.</p>
<p id="b751-6">At about 6 p. m. on February 6, the car and the pickup left the driveway and traveled along public highways to Taos. During the trip, the two vehicles were under both physical and electronic surveillance. When the vehicles arrived at a house in Taos rented by Horton, Harley, and Michael Steele, the agents did not maintain tight surveillance for fear of detection. When the vehicles left the Taos residence, agents <page-number citation-index="1" label="710">*710</page-number>determined, using the beeper monitor, that the beeper can was still inside the house. Again on February 7, the beeper revealed that the ether can was still on the premises. At one point, agents noticed that the windows of the house were wide open on a cold windy day, leading them to suspect that the ether was being used. On February 8, the agents applied for and obtained a warrant to search the Taos residence based in part on information derived through use of the beeper. The warrant was executed on February 10, 1981, and Horton, Harley, Steele, and Evan Roth were arrested, and cocaine and laboratory equipment were seized.</p>
<p id="b752-5">Respondents Karo, Horton, Harley, Steele, and Roth were indicted for conspiring to possess cocaine with intent to distribute it and with the underlying offense. <span class="citation no-link">21 U. S. C. §§ 841</span>(a)(1) and 846. Respondent Rhodes was indicted only for conspiracy to possess. The District Court granted respondents’ pretrial motion to suppress the evidence seized from the Taos residence on the grounds that the initial warrant to install the beeper was invalid and that the Taos seizure was the tainted fruit of an unauthorized installation and monitoring of that beeper. The United States appealed but did not challenge the invalidation of the initial warrant. The Court of Appeals affirmed, except with respect to Rhodes, holding that a warrant was required to install the beeper in one of the 10 cans of ether and to monitor it in private dwellings and storage lockers. <span class="citation" data-id="420988"><a href="/opinion/420988/united-states-v-james-connors-karo-richard-miles-horton-william/" aria-description="Citation for case: United States v. James Connors Karo, Richard Miles...">710 F. 2d 1433</a></span> (CA10 1983). The warrant for the search in Taos and the resulting seizure were tainted by the prior illegal conduct of the Government. The evidence was therefore properly suppressed with respect to respondents Horton, Harley, Steele, and Roth, who were held to have protectible interests in the privacy of the Taos dwelling, and with respect to respondent Karo because the beeper had been installed without a warrant and had been monitored while its ether-can host was in his house.<footnotemark>2</footnotemark> We <page-number citation-index="1" label="711">*711</page-number>granted the Government’s petition for certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./464/1068/">464 U. S. 1068</a></span> (1984), which raised the question whether a warrant was required to authorize either the installation of the beeper or its subsequent monitoring. We deal with each contention in turn.</p>
<p id="b753-5">II</p>
<p id="b753-6">Because the judgment below in favor of Karo rested in major part on the conclusion that the installation violated his Fourth Amendment rights and that any information obtained from monitoring the beeper was tainted by the initial illegality, we must deal with the legality of the warrantless installation. It is clear that the actual placement of the beeper into the can violated no one’s Fourth Amendment rights. The can into which the beeper was placed belonged at the time to the DEA, and by no stretch of the imagination could it be said that respondents then had any legitimate expectation of privacy in it. The ether and the original 10 cans, on the other hand, belonged to, and were in the possession of, Muehlenweg, who had given his consent to any invasion of those items that occurred. Thus, even if there had been no substitution of cans and the agents had placed the beeper into one of the original 10 cans, Muehlenweg’s consent was sufficient to validate the placement of the beeper in the can. See <em>United States </em>v. <em>Matlock, </em><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">415 U. S. 164</a></span> (1974); <em>Frazier </em>v. <em>Cupp, </em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731</a></span> (1969).</p>
<p id="b753-7">The Court of Appeals acknowledged that before Karo took control of the ether “the DEA and Muehlenweg presumably could do with the can and ether whatever they liked without violating Karo’s rights.” <span class="citation" data-id="420988"><a href="/opinion/420988/united-states-v-james-connors-karo-richard-miles-horton-william/#1438" aria-description="Citation for case: United States v. James Connors Karo, Richard Miles...">710 F. 2d, at 1438</a></span>. It did not hold that the actual placement of the beeper into the ether can violated the Fourth Amendment. Instead, it held that the violation occurred at the time the beeper-laden can was transferred to Karo. The court stated:</p>
<blockquote id="b754-4"><page-number citation-index="1" label="712">*712</page-number>“All individuals have a legitimate expectation of privacy that objects coming into their rightful ownership do not have electronic devices attached to them, devices that would give law enforcement agents the opportunity to monitor the location of the objects at all times and in every place that the objects are taken, including inside private residences and other areas where the right to be free from warrantless governmental intrusion is unquestioned.” <em><span class="citation" data-id="420988"><a href="/opinion/420988/united-states-v-james-connors-karo-richard-miles-horton-william/" aria-description="Citation for case: United States v. James Connors Karo, Richard Miles...">Ibid.</a></span></em></blockquote>
<p id="b754-5">Not surprisingly, the Court of Appeals did not describe the transfer as either a “search” or a “seizure,” for plainly it is neither. A “search” occurs “when an expectation of privacy that society is prepared to consider reasonable is infringed.” <em>United States </em>v. <em>Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 113</a></span> (1984). The mere transfer to Karo of a can containing an unmonitored beeper infringed no privacy interest. It conveyed no information that Karo wished to keep private, for it conveyed no information at all. To be sure, it created a <em>potential </em>for an invasion of privacy, but we have never held that potential, as opposed to actual, invasions of privacy constitute searches for purposes of the Fourth Amendment. A holding to that effect would mean that a policeman walking down the street carrying a parabolic microphone capable of picking up conversations in nearby homes would be engaging in a search even if the microphone were not turned on. It is the exploitation of technological advances that implicates the Fourth Amendment, not their mere existence.</p>
<p id="b754-6">We likewise do not believe that the transfer of the container constituted a seizure. A “seizure” of property occurs when “there is some meaningful interference with an individual's possessory interests in that property.” <em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">Ibid.</a></span> </em>Although the can may have contained an unknown and unwanted foreign object, it cannot be said that anyone’s possessory interest was interfered with in a meaningful way. At most, there was a technical trespass on the space occupied by the beeper. The existence of a physical trespass is only <page-number citation-index="1" label="713">*713</page-number>marginally relevant to the question of whether the Fourth Amendment has been violated, however, for an actual trespass is neither necessary nor sufficient to establish a constitutional violation. Compare <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967) (no trespass, but Fourth Amendment violation), with <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U. S. 170</a></span> (1984) (trespass, but no Fourth Amendment violation). Of course, if the presence of a beeper in the can constituted a seizure merely because of its occupation of space, it would follow that the presence of any object, regardless of its nature, would violate the Fourth Amendment.</p>
<p id="AG0">We conclude that no Fourth Amendment interest of Karo or of any other respondent was infringed by the installation of the beeper. Rather, any impairment of their privacy interests that may have occurred was occasioned by the monitoring of the beeper.<footnotemark>3</footnotemark></p>
<p id="A1q">rH f-H Y — (</p>
<p id="AatS">In <em>United States </em>v. <em>Knotts, </em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">460 U. S. 276</a></span> (1983), law enforcement officials, with the consent of the seller, installed a beeper in a 5-gallon can of chloroform and monitored the beeper after delivery of the can to the buyer in Minneapolis, Minn. Although there was partial visual surveillance as the automobile containing the can moved along the public highways, the beeper enabled the officers to locate the can in the area of a cabin near Shell Lake, Wis., and it was this information that provided the basis for the issuance of a search warrant. As the case came to us, the installation of the beeper was not challenged; only the monitoring was at issue. The Court held that since the movements of the automobile and the arrival of the can containing the beeper in the area of the <page-number citation-index="1" label="714">*714</page-number>cabin could have been observed by the naked eye, no Fourth Amendment violation was committed by monitoring the beeper during the trip to the cabin. In <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span>, </em>the record did not show that the beeper was monitored while the can containing it was inside the cabin, and we therefore had no occasion to consider whether a constitutional violation would have occurred had the fact been otherwise.</p>
<p id="b756-5">Here, there is no gainsaying that the beeper was used to locate the ether in a specific house in Taos, N. M., and that that information was in turn used to secure a warrant for the search of the house. The affidavit supporting the application for a search warrant recited that the ether arrived at the residence in a motor vehicle that later departed and that:</p>
<blockquote id="AcC">“For fear of detection, we did not maintain tight surveillance of the residence. . . . Using the ‘beeper’ locator, I positively determined that the ‘beeper’ can (5-gallon can of ether, described earlier in this affidavit) was now inside the above-described premises to be searched because the ‘beeper’ locator (direction finder) pinpointed the beeper signal as emanating from the above-described premises. . . . Again, later on Saturday (now in the daytime), 7 February 1981, my ‘beeper’ locator still shows a strong ‘beeper’ signal emanating from inside the above-described residence.” App. 57-58.</blockquote>
<p id="b756-6">This case thus presents the question whether the monitoring of a beeper in a private residence, a location not open to visual surveillance, violates the Fourth Amendment rights of those who have a justifiable interest in the privacy of the residence. Contrary to the submission of the United States, we think that it does.</p>
<p id="b756-7">At the risk of belaboring the obvious, private residences are places in which the individual normally expects privacy free of governmental intrusion not authorized by a warrant, and that expectation is plainly one that society is prepared to recognize as justifiable. Our cases have not deviated from this basic Fourth Amendment principle. Searches and <page-number citation-index="1" label="715">*715</page-number>seizures inside a home without a warrant are presumptively unreasonable absent exigent circumstances. <em>Welsh </em>v. <em>Wisconsin, </em><span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/#748" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740, 748-749</a></span> (1984); <em>Steagald </em>v. <em>United States, </em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/#211" aria-description="Citation for case: Steagald v. United States">451 U. S. 204, 211-212</a></span> (1981); <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 586</a></span> (1980). In this case, had a DEA agent thought it useful to enter the Taos residence to verify that the ether was actually in the house and had he done so surreptitiously and without a warrant, there is little doubt that he would have engaged in an unreasonable search within the meaning of the Fourth Amendment. For purposes of the Amendment, the result is the same where, without a warrant, the Government surreptitiously employs an electronic device to obtain information that it could not have obtained by observation from outside the curtilage of the house. The beeper tells the agent that' a particular article is actually located at a particular time in the private residence and is in the possession of the person or persons whose residence is being watched. Even if visual surveillance has revealed that the article to which the beeper is attached has entered the house, the later monitoring not only verifies the officers’ observations but also establishes that the article remains on the premises. Here, for example, the beeper was monitored for a significant period after the arrival of the ether in Taos and before the application for a warrant to search.</p>
<p id="b757-5">The monitoring of an electronic device such as a beeper is, of course, less intrusive than a full-scale search, but it does reveal a critical fact about the interior of the premises that the Government is extremely interested in knowing and that it could not have otherwise obtained without a warrant. The case is thus not like <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span>, </em>for there the beeper told the authorities nothing about the interior of Knotts’ cabin. The information obtained in <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span> </em>was “voluntarily conveyed to anyone who wanted to look . . . ,” <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#281" aria-description="Citation for case: United States v. Knotts">460 U. S., at 281</a></span>; here, as we have said, the monitoring indicated that the beeper was inside the house, a fact that could not have been visually verified.</p>
<p id="b758-4"><page-number citation-index="1" label="716">*716</page-number>We cannot accept the Government’s contention that it should be completely free from the constraints of the Fourth Amendment to determine by means of an electronic device, without a warrant and without probable cause or reasonable suspicion, whether a particular article — or a person, for that matter — is in an individual’s home at a particular time. Indiscriminate monitoring of property that has been withdrawn from public view would present far too serious a threat to privacy interests in the home to escape entirely some sort of Fourth Amendment oversight.<footnotemark>4</footnotemark></p>
<p id="b759-4"><page-number citation-index="1" label="717">*717</page-number>We also reject the Government’s contention that it should be able to monitor beepers in private residences without a warrant if there is the requisite justification in the facts for believing that a crime is being or will be committed and that monitoring the beeper wherever it goes is likely to produce evidence of criminal activity. Warrantless searches are presumptively unreasonable, though the Court has recognized a few limited exceptions to this general rule. See, <em>e. g., United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982) (automobiles); <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973) (consent); <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967) (exigent circumstances). The Government’s contention that warrantless beeper searches should be deemed reasonable is based upon its deprecation of the benefits and exaggeration of the difficulties associated with procurement of a warrant. The Government argues that the traditional justifications for the warrant requirement are inapplicable in beeper cases, but to a large extent that argument is based upon the contention, rejected above, that the beeper constitutes only a minuscule intrusion on protected privacy interests. The primary reason for the warrant requirement is to interpose a “neutral and detached magistrate” between the citizen and “the officer engaged in the often competitive enterprise of ferreting out crime.” <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948). Those suspected of drug offenses are no less entitled to that protection than those suspected of nondrug offenses. Requiring a warrant will have the salutary effect of ensuring that use of beepers is not abused, by imposing upon agents the requirement that they demonstrate in advance their justification for the desired search. This is not to say that there <page-number citation-index="1" label="718">*718</page-number>are no exceptions to the warrant rule, because if truly exigent circumstances exist no warrant is required under general Fourth Amendment principles.</p>
<p id="b760-5">If agents are required to obtain warrants prior to monitoring a beeper when it has been withdrawn from public view, the Government argues, for all practical purposes they will be forced to obtain warrants in every case in which they seek to use a beeper, because they have no way of knowing in advance whether the beeper will be transmitting its signals from inside private premises. The argument that a warrant requirement would oblige the Government to obtain warrants in a large number of cases is hardly a compelling argument against the requirement. It is worthy of note that, in any event, this is not a particularly attractive case in which to argue that it is impractical to obtain a warrant, since a warrant was in fact obtained in this case, seemingly on probable cause.</p>
<p id="b760-6">We are also unpersuaded by the argument that a warrant should not be required because of the difficulty in satisfying the particularity requirement of the Fourth Amendment. The Government contends that it would be impossible to describe the “place” to be searched, because the location of the place is precisely what is sought to be discovered through the search. Brief for United States 42. However true that may be, it will still be possible to describe the object into which the beeper is to be placed, the circumstances that led agents to wish to install the beeper, and the length of time for which beeper surveillance is requested. In our view, this information will suffice to permit issuance of a warrant authorizing beeper installation and surveillance.</p>
<p id="b760-7">In sum, we discern no reason for deviating from the general rule that a search of a house should be conducted pursuant to a warrant.<footnotemark>5</footnotemark></p>
<p id="b761-9"><page-number citation-index="1" label="719">*719</page-number>t — I &lt;1</p>
<p id="b761-3">As we have said, by maintaining the beeper the agents verified that the ether was actually located in the Taos house and that it remained there while the warrant was sought. This information was obtained without a warrant and would therefore be inadmissible at trial against those with privacy interests in the house — Horton, Harley, Steele, and Roth. That information, which was included in the warrant affidavit, would also invalidate the warrant for the search of the house if it proved to be critical to establishing probable cause for the issuance of the warrant. However, if sufficient untainted evidence was presented in the warrant affidavit to establish probable cause, the warrant was nevertheless valid. <em>Franks </em>v. <em>Delaware, </em><span class="citation" data-id="9427321"><a href="/opinion/109925/franks-v-delaware/#172" aria-description="Citation for case: Franks v. Delaware">438 U. S. 154, 172</a></span> (1978).</p>
<p id="b761-4">It requires only a casual examination of the warrant affidavit, which in relevant respects consists of undisputed factual assertions, to conclude that the officers could have secured the warrant without relying on the beeper to locate the ether in the house sought to be searched. The affidavit recounted the months-long tracking of the evidence, including the visual and beeper surveillance of Horton’s pickup on its trip from Albuquerque to the immediate vicinity of the Taos residence; its departure a short time later without the ether; its later return to the residence; and the visual observation of the residence with its windows open on a cold night.</p>
<p id="b761-5">That leaves the question whether any part of this additional information contained in the warrant affidavit was itself the fruit of a Fourth Amendment violation to which any of the occupants of the house could object. As far as the <page-number citation-index="1" label="720">*720</page-number>present record reveals, two of the four respondents who had standing to object to the search of the residence — Steele and Roth — had no interest in any of the arguably private places in which the beeper was monitored prior to its arrival in Taos. The evidence seized in the house would be admissible against them.</p>
<p id="b762-5">The question as to Horton and Harley is somewhat more complicated. On the initial leg of its journey, the ether came to rest in Karo’s house where it was monitored; it then moved in succession to two other houses, including Horton’s, before it was moved first to a locker in one public warehouse and then to a locker in another. Both lockers were rented jointly by Horton and Harley. On September 6, the ether was removed from the second storage facility and transported to Taos.</p>
<p id="b762-6">Assuming for present purposes that prior to its arrival at the second warehouse the beeper was illegally used to locate the ether in a house or other place in which Horton or Harley had a justifiable claim to privacy, we are confident that such use of the beeper does not taint its later use in locating the ether and tracking it to Taos. The movement of the ether from the first warehouse was undetected, but by monitoring the beeper the agents discovered that it had been moved to the second storage facility. No prior monitoring of the beeper contributed to this discovery; using the beeper for this purpose was thus untainted by any possible prior illegality. Furthermore, the beeper informed the agents only that the ether was somewhere in the warehouse; it did not identify the specific locker in which the ether was located. Monitoring the beeper revealed nothing about the contents of the locker that Horton and Harley had rented and hence was not a search of that locker.<footnotemark>6</footnotemark> The locker was identified only <page-number citation-index="1" label="721">*721</page-number>when agents traversing the public parts of the facility found that the smell of ether was coming from a specific locker.</p>
<p id="b763-5">The agents set up visual surveillance of that locker, and on September 6, they observed Rhodes and a female remove the ether and load it into Horton’s pickup truck. The truck moved over the public streets and was tracked by beeper to Rhodes’ house, where it was temporarily parked. At about 6 p. m. the truck was observed departing and was tracked visually and by beeper to the vicinity of the house in Taos. Because locating the ether in the warehouse was not an illegal search — and because the ether was seen being loaded into Horton’s truck, which then traveled the public highways — it is evident that under <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span> </em>there was no violation of the Fourth Amendment as to anyone with or without standing to complain about monitoring the beeper while it was located in Horton’s truck. Under these circumstances, it is clear that the warrant affidavit, after striking the facts about monitoring the beeper while it was in the Taos residence, contained sufficient untainted information to furnish probable cause for the issuance of the search warrant. The evidence seized in the house should not have been suppressed with respect to any of the respondents.<footnotemark>7</footnotemark></p>
<p id="b763-6">The judgment of the Court of Appeals is accordingly</p>
<p id="b763-7">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b749-9"> “A beeper is a radio transmitter, usually battery operated, which emits periodic signals that can be picked up by a radio receiver.” <em>United States </em>v. <em>Knotts, </em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#277" aria-description="Citation for case: United States v. Knotts">460 U. S., at 277</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b752-6"> The Court of Appeals reversed as to Rhodes since he had not shown that the beeper had been located in any place in which he had a reasonable <page-number citation-index="1" label="711">*711</page-number>expectation of privacy, nor had he shown any possessory interest in the ether itself that would have been invaded by the installation of the beeper.</p>
</footnote>
<footnote label="3">
<p id="AKb"> Despite this holding, warrants for the installation and monitoring of a beeper will obviously be desirable since it may be useful, even critical, to monitor the beeper to determine that it is actually located in a place not open to visual surveillance. As will be evident below, such monitoring without a warrant may violate the Fourth Amendment.</p>
</footnote>
<footnote label="4">
<p id="b758-5"> Justice O’Connor observes that a homeowner has no reasonable expectation that a person invited into his home will not be wired with a microphone that transmits conversations in which he engages, see <em>United States </em>v. <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/" aria-description="Citation for case: United States v. White"><em>White, 401 U. </em>S. 746</a></span> (1971), and <em>from </em>this proposition she concludes that a homeowner has no reasonable expectation that an invitee will not bring an object containing a beeper into his home. <em>Post, </em>at 722-724. While that observation would be relevant if one of the conspirators in this case had consented to the placement of the beeper in the can, it has no relevance to the case at hand. Surely if the Government surreptitiously plants a listening device on an unsuspecting household guest or family member and then monitors conversations with the homeowner, the homeowner could challenge the monitoring of the conversations regardless of the fact that he did not have power “to give effective consent to the search” of the visitor. <em>Post, </em>at 724. As the plurality recognized in <em>United States </em>v. <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#749" aria-description="Citation for case: United States v. White"><em>White, supra, </em>at 749</a></span>, there is a substantial distinction between “revela-tionfs] to the Government by a party to conversations with the defendant” and eavesdropping on conversations without the knowledge or consent of either party to it. A homeowner takes the risk that his guest will cooperate with the Government but not the risk that a trustworthy friend has been bugged by the Government without his knowledge or consent. Under Justice O’Connor’s view it could easily be said that in <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), Katz had no reasonable expectation of privacy in his conversation because the person to whom he was speaking might have divulged the contents of the conversation. There would be nothing left of the Fourth Amendment right to privacy if anything that a <em>hypothetical </em>government informant <em>might </em>reveal is stripped of constitutional protection.</p>
<p id="b758-6"><em>Rawlings </em>v. <em>Kentucky, </em><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">448 U. S. 98</a></span> (1980), is simply inapposite, since it was not Rawlings’ home in which the challenged search occurred. Cf. <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">394 U. S. 165</a></span> (1969) (homeowner has standing to <page-number citation-index="1" label="717">*717</page-number>challenge illegal search of house even if he has no interest in the property seized). Justice O’Connor seems to recognize as much, noting in the discussion of <em>Katz, post, </em>at 725, that “a third person, <em>who never used a particular telephone line” </em>would have no standing to challenge illegal eavesdropping. If the phone line is that of the third person, however, a different analysis is involved.</p>
</footnote>
<footnote label="5">
<p id="b760-8"> The United States insists that if beeper monitoring is deemed a search, a showing of reasonable suspicion rather than probable cause <page-number citation-index="1" label="719">*719</page-number>should suffice for its execution. That issue, however, is not before us. The initial warrant was not invalidated for want of probable cause, which plainly existed, but for misleading statements in the affidavit. The Government did not appeal the invalidation of the warrant and as the case has turned out, the Government prevails without a warrant authorizing installation. It will be time enough to resolve the probable cause-reasonable suspicion issue in a case that requires it.</p>
</footnote>
<footnote label="6">
<p id="b762-7"> Had the monitoring disclosed the presence of the container within a particular locker the result would be otherwise, for surely Horton and Harley had a reasonable expectation of privacy in their own storage locker.</p>
</footnote>
<footnote label="7">
<p id="b763-11"> Although the unwarranted monitoring of the beeper in Karo’s house would foreclose using that evidence against him, it did not taint the discovery of the ether in the second warehouse and the ensuing surveillance of the trip to Taos.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Knights.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Knights"
type: case
citation: "534 U.S. 112 (2001)"
parallel_cite: "122 S. Ct. 587; 151 L. Ed. 2d 497"
neutral_cite: 2001 U.S. LEXIS 10950
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2001
date_decided: 2001-12-10
docket: 00-1260
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2001-12-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Knights
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118468/united-states-v-knights/"
  cluster_id: 118468
  opinion_id: 9434170
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Griffin v. Wisconsin]]", "[[Samson v. California]]", "[[United States v. Cortez]]", "[[Terry v. Ohio]]"]
aliases: []
tags: ["case", "fourth-amendment", "probation-search", "reasonable-suspicion", "search-condition", "general-balancing"]
holding: "A warrantless search of a probationer subject to a search condition, supported by reasonable suspicion, is reasonable under the Fourth…"
lake:
  record_id: United States v. Knights
  status: verified
  projected_at: 2026-07-09
---

# United States v. Knights

*534 U.S. 112 (2001)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Knights was on probation for a drug offense under a condition that he submit his person, property, residence, vehicle, and effects "to search at anytime, with or without a search warrant, warrant of arrest or reasonable cause by any probation officer or law enforcement officer." After a PG&E transformer was set on fire — the latest of many vandalism incidents for which Knights was a suspect — a detective searched his apartment, with reasonable suspicion, and found incendiary materials, bolt cutters, and a PG&E padlock. The District Court found reasonable suspicion but suppressed the evidence because the search was "investigatory" rather than "probationary"; the Ninth Circuit affirmed.

## Issue
Whether a warrantless search of a probationer's residence, authorized by a probation search condition and supported by reasonable suspicion, is reasonable under the Fourth Amendment — even where the officer's purpose was investigatory rather than probationary.

## Rule
Yes. Balancing the probationer's diminished privacy against the State's interest in supervising probationers, the Court applied ordinary Fourth Amendment reasonableness rather than the special-needs doctrine, and held: "We hold that the balance of these considerations requires no more than reasonable suspicion to conduct a search of this probationer's house." — 534 U.S. at 121. ^pin-121

"When an officer has reasonable suspicion that a probationer subject to a search condition is engaged in criminal activity, there is enough likelihood that criminal conduct is occurring that an intrusion on the probationer's significantly diminished privacy interests is reasonable." — *Id.*

The Court's ultimate holding: "We therefore hold that the warrantless search of Knights, supported by reasonable suspicion and authorized by a condition of probation, was reasonable within the meaning of the Fourth Amendment." — *Id.* at 122. ^pin-122

It expressly reserved the question whether a *suspicionless* search would be reasonable, "because the search in this case was supported by reasonable suspicion." — [*Id.* at 120](https://www.courtlistener.com/opinion/118468/united-states-v-knights/#:~:text=because%20the%20search%20in%20this) n.6. ^pin-120

## Application
On these facts the apartment search was reasonable. Knights's probation order "significantly diminished" his expectation of privacy, while the State's heightened interest in apprehending probationer-recidivists justified a lesser-than-probable-cause standard. The investigatory purpose did not matter, because the Court rested its holding on "ordinary Fourth Amendment analysis," under which "[s]ubjective intentions play no role." Since the District Court found — and Knights conceded — that the search was supported by reasonable suspicion, and the probation condition authorized it, the warrantless search of his apartment satisfied the Fourth Amendment. The Court did not decide whether the same search would have been reasonable with no individualized suspicion at all.

## Conclusion
A probation-condition search of Knights's home, supported by reasonable suspicion, was reasonable under the Fourth Amendment regardless of the officer's investigatory motive; the Ninth Circuit's judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Knights* rests on general Fourth Amendment balancing rather than the special-needs rationale of [[Griffin v. Wisconsin]], and it expressly left open the suspicionless-search question — which [[Samson v. California]] later answered for *parolees* (suspicionless searches reasonable given parolees' even more diminished privacy).

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Knights*, 534 U.S. 112 (2001) — https://www.courtlistener.com/opinion/118468/united-states-v-knights/ — pinpoints: 120 n.6, 121, 122.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d57058403e12b6b1", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Knights"}, "payload": {"all": [{"cite": "534 U.S. 112", "page": "112", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "534"}, {"cite": "122 S. Ct. 587", "page": "587", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "122"}, {"cite": "151 L. Ed. 2d 497", "page": "497", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "151"}, {"cite": "2001 U.S. LEXIS 10950", "page": "10950", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2001"}], "display": "534 U.S. 112", "official": {"cite": "534 U.S. 112", "page": "112", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "534"}, "official_selection_present": true, "record_id": "United States v. Knights"}}
{"assertion_id": "4cf46e2a64cd167d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-121", "record_id": "United States v. Knights"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-121", "pinpoint_status": "slip-only", "quote": "; the Ninth Circuit affirmed. ## Issue Whether a warrantless search of a probationer's residence, authorized by a probation search condition and supported by reasonable suspicion, is reasonable under the Fourth Amendment — even where the officer's purpose was investigatory rather than probationary. ## Rule Yes. Balancing the probationer's diminished privacy against the State's interest in supervising probationers, the Court applied ordinary Fourth Amendment reasonableness rather than the special-needs doctrine, and held:", "quote_fidelity": "mismatch", "record_id": "United States v. Knights", "star_marker": null}}
{"assertion_id": "4f659b0b2206cdb6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-120", "record_id": "United States v. Knights"}, "payload": {"fragment": "#:~:text=because%20the%20search%20in%20this", "page": null, "pin_id": "pin-120", "pinpoint_status": "star-verified", "quote": "because the search in this case was supported by reasonable suspicion.", "quote_fidelity": "matched", "record_id": "United States v. Knights", "star_marker": "122"}}
{"assertion_id": "503fec7a89cb238d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-122", "record_id": "United States v. Knights"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-122", "pinpoint_status": "slip-only", "quote": "— *Id.* The Court's ultimate holding:", "quote_fidelity": "mismatch", "record_id": "United States v. Knights", "star_marker": null}}
{"assertion_id": "eb09bd62d04d3d8e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Knights"}, "payload": {"as_of_content": "2001-12-10", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Knights", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Knights

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Knights",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Knights",
    "case_name_short": "Knights",
    "case_name_full": "United States v. Knights",
    "input_case_name": "United States v. Knights",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2001-12-10",
    "year": 2001,
    "docket": "00-1260",
    "cluster_id": 118468,
    "lead_opinion_id": 9434170,
    "sibling_ids": [
      118468,
      9434170,
      9434171
    ],
    "absolute_url": "/opinion/118468/united-states-v-knights/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "534 U.S. 112",
      "volume": "534",
      "reporter": "U.S.",
      "page": "112",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "122 S. Ct. 587",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "587",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "151 L. Ed. 2d 497",
        "volume": "151",
        "reporter": "L. Ed. 2d",
        "page": "497",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2001 U.S. LEXIS 10950",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "10950",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "534 U.S. 112",
        "volume": "534",
        "reporter": "U.S.",
        "page": "112",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "122 S. Ct. 587",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "587",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "151 L. Ed. 2d 497",
        "volume": "151",
        "reporter": "L. Ed. 2d",
        "page": "497",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 U.S. LEXIS 10950",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "10950",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "534 U.S. 112",
    "official_selection": {
      "court_class": "scotus",
      "selected": "534 U.S. 112",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-121",
      "page": null,
      "quote": "; the Ninth Circuit affirmed. ## Issue Whether a warrantless search of a probationer's residence, authorized by a probation search condition and supported by reasonable suspicion, is reasonable under the Fourth Amendment \u2014 even where the officer's purpose was investigatory rather than probationary. ## Rule Yes. Balancing the probationer's diminished privacy against the State's interest in supervising probationers, the Court applied ordinary Fourth Amendment reasonableness rather than the special-needs doctrine, and held:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-122",
      "page": null,
      "quote": "\u2014 *Id.* The Court's ultimate holding:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-120",
      "page": null,
      "quote": "because the search in this case was supported by reasonable suspicion.",
      "star_marker": "122",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 24268,
      "fragment": "#:~:text=because%20the%20search%20in%20this",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2001-12-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Knights",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
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
        "journal_ref": "United States v. Knights:lane1_negative"
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
        "journal_ref": "United States v. Knights:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Norman",
          "cluster_id": 4736927,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Shipps",
          "cluster_id": 4725703,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane1_negative"
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
        "journal_ref": "United States v. Knights:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Stenhoff",
          "cluster_id": 4609284,
          "cite": [
            "2019 ND 106",
            "925 N.W.2d 429"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane1_negative"
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
        "journal_ref": "United States v. Knights:lane1_negative"
      },
      {
        "citing_case": {
          "name": "The People v. Sean Garvin",
          "cluster_id": 4436829,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Parker",
          "cluster_id": 4329293,
          "cite": [
            "152 A.3d 309",
            "2016 Pa. Super. 280",
            "2016 Pa. Super. LEXIS 751"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane1_negative"
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
        "journal_ref": "United States v. Knights:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chandler",
          "cluster_id": 7318545,
          "cite": [
            "164 F. Supp. 3d 368",
            "2016 U.S. Dist. LEXIS 17682",
            "2016 WL 614679"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Moore",
          "cluster_id": 3168462,
          "cite": [
            "473 Mass. 481",
            "43 N.E.3d 294"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gall v. United States",
          "cluster_id": 145843,
          "cite": [
            "169 L. Ed. 2d 445",
            "128 S. Ct. 586",
            "552 U.S. 38",
            "2007 U.S. LEXIS 13083"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
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
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nicholas Omar Midgette",
          "cluster_id": 796984,
          "cite": [
            "478 F.3d 616",
            "2007 U.S. App. LEXIS 4153",
            "2007 WL 572127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
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
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Luedemann",
          "cluster_id": 2008176,
          "cite": [
            "857 N.E.2d 187",
            "222 Ill. 2d 530",
            "306 Ill. Dec. 94",
            "2006 Ill. LEXIS 1641"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cyril Korte v. HHS",
          "cluster_id": 2709178,
          "cite": [
            "735 F.3d 654",
            "2013 WL 5960692"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
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
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Delores Henry v. Melody Hulett",
          "cluster_id": 4774392,
          "cite": [
            "969 F.3d 769"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
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
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Parrish Kappes",
          "cluster_id": 2792248,
          "cite": [
            "782 F.3d 828",
            "2015 WL 1546810"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Fernandez",
          "cluster_id": 8438634,
          "cite": [
            "388 F.3d 1199",
            "2004 WL 2399856"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Center for Bio-Ethical Reform, Inc. v. Los Angeles County Sheriff Department",
          "cluster_id": 1235108,
          "cite": [
            "533 F.3d 780",
            "2008 U.S. App. LEXIS 13975",
            "2008 WL 2599683"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
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
        "journal_ref": "United States v. Knights:lane2_top_cited"
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
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Chanthasouxat",
          "cluster_id": 76272,
          "cite": [
            "342 F.3d 1271",
            "2003 WL 21994747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicholas v. Goord",
          "cluster_id": 8439101,
          "cite": [
            "430 F.3d 652",
            "2005 WL 3150611"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Merritt Sharp, III v. County of Orange",
          "cluster_id": 4427211,
          "cite": [
            "871 F.3d 901",
            "2017 WL 4126947",
            "2017 U.S. App. LEXIS 18148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ramos",
          "cluster_id": 2507985,
          "cite": [
            "101 P.3d 478",
            "21 Cal. Rptr. 3d 575",
            "34 Cal. 4th 494",
            "2004 Daily Journal DAR 14175",
            "2004 Cal. Daily Op. Serv. 10418",
            "2004 Cal. LEXIS 11332"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Cameron Kincade",
          "cluster_id": 787362,
          "cite": [
            "379 F.3d 813",
            "2004 U.S. App. LEXIS 17191",
            "2004 WL 1837840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Samuels",
          "cluster_id": 2601800,
          "cite": [
            "228 P.3d 229",
            "2009 Colo. App. LEXIS 1789",
            "2009 WL 3297504"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Donald Reyes, Robert Jubic",
          "cluster_id": 776901,
          "cite": [
            "283 F.3d 446",
            "2002 U.S. App. LEXIS 3646"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Motley v. Parks",
          "cluster_id": 3035469,
          "cite": [
            "432 F.3d 1072",
            "2005 WL 3556971"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Frank Fernandez, United States of America v. Roy Gavaldon, AKA Spider, United States of America v. David Gonzales-Contreras, AKA David Contreras-Gonzalez, United States of America v. Dominick Shewmaker Gonzales, AKA Solo, AKA Dominick Gonzales, United States of America v. Jimmy Sanchez, AKA Seal D, AKA Smokey, United States of America v. Suzanne Schoenberg Sanchez",
          "cluster_id": 788340,
          "cite": [
            "388 F.3d 1199",
            "2004 U.S. App. LEXIS 22328"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Tommy Tyler, Jr.",
          "cluster_id": 4472243,
          "cite": [
            "830 N.W.2d 288",
            "2013 WL 1785988",
            "2013 Iowa Sup. LEXIS 44"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knights:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118468 OR 9434170 OR 9434171) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDQ5MDE0NDAwMDAwJnM9MzE1OTI2NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118468+OR+9434170+OR+9434171%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 12,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(118468 OR 9434170 OR 9434171)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzEmcz0yODEyOTA1JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28118468+OR+9434170+OR+9434171%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118468 OR 9434170 OR 9434171)",
        "reviewed": 50,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 50,
        "triage_read": 0,
        "triage_snippet_classified": 50
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118468 OR 9434170 OR 9434171)",
    "indexed_citing_opinions": 872,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118468,
        "count": 762,
        "count_source": "search"
      },
      {
        "opinion_id": 9434170,
        "count": 126,
        "count_source": "search"
      },
      {
        "opinion_id": 9434171,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1481,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-knights.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxMjkxOTMmcz0xMDI5ODE1NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118468+OR+9434170+OR+9434171%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118468,
        "cited_id": 104314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 108606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 111105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 118277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 118391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 118405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 741978,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 1160907,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 1162126,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118468,
        "cited_id": 5452320,
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
    "date_created": "2026-07-06T01:06:03Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:07:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:07:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:11:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:07:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Knights

```
<opinion type="majority">
<author id="b304-4"><page-number citation-index="1" label="114">*114</page-number>Chief Justice Rehnquist</author>
<p id="A6f">delivered the opinion of the Court.</p>
<p id="b304-5">A California court sentenced respondent Mark James Knights to summary probation for a drug offense. The probation order included the following condition: that Knights would “[s]ubmit his . . . person, property, place of residence, vehicle, personal effects, to search at anytime, with or without a search warrant, warrant of arrest or reasonable cause by any probation officer or law enforcement officer.” Knights signed the probation order, which stated immediately above his signature that “I HAVE. RECEIVED A COPY, READ AND UNDERSTAND THE ABOVE TERMS AND CONDITIONS OF PROBATION AND AGREE TO ABIDE BY SAME.” App. 49. In this case, we decide whether a search pursuant to this probation condition, and supported by reasonable suspicion, satisfied the Fourth Amendment.</p>
<p id="b304-6">Three days after Knights was placed on probation, a Pacific Gas &amp; Electric (PG&amp;E) power transformer and adjacent Pacific Bell telecommunications vault near the Napa County Airport were pried open and set on fire, causing an estimated $1.5 million in damage. Brass padlocks had been removed and a gasoline accelerant had been used to ignite the fire. This incident was the latest in more than 30 recent acts of vandalism against PG&amp;E facilities in Napa County. Suspicion for these acts had long focused on Knights and his friend, Steven Simoneau. The incidents began after PG&amp;E <page-number citation-index="1" label="115">*115</page-number>had filed a theft-of-services complaint against Knights and discontinued his electrical service for failure to pay his bill. Detective Todd Hancock of the Napa County Sheriff’s Department had noticed that the acts of vandalism coincided with Knights’ court appearance dates concerning the theft of PG&amp;E services. And just a week before the arson, a sheriff’s deputy had stopped Knights and Simoneau near a PG&amp;E gas line and observed pipes and gasoline in Simon-eau’s pickup truck.</p>
<p id="b305-5">After the PG&amp;E arson, a sheriff’s deputy drove by Knights’ residence, where he saw Simoneau’s truck parked in front. The deputy felt the hood of the truck. It was warm. Detective Hancock decided to set up surveillance of Knights’ apartment. At about 3:10 the next morning, Simoneau exited the apartment carrying three cylindrical items. Detective Hancock believed the items were pipe bombs. Simoneau walked across the street to the bank of the Napa River, and Hancock heard three splashes. Simon-eau returned without the cylinders and drove away in his truck. Simoneau then stopped in a driveway, parked, and left the area. Detective Hancock entered the driveway and observed a number of suspicious objects in the truck: a Molotov cocktail and explosive materials, a gasoline can, and two brass padlocks that fit the description of those removed from the PG&amp;E transformer vault.</p>
<p id="b305-6">After viewing the objects in Simoneau’s truck, Detective Hancock decided to conduct a search of Knights’ apartment. Detective Hancock was aware of the search condition in Knights’ probation order and thus believed that a warrant was not necessary.<footnotemark>1</footnotemark> The search revealed a detonation cord, ammunition, liquid chemicals, instruction manuals on chemistry and electrical circuitry, bolt cutters, telephone pole-climbing spurs, drug paraphernalia, and a brass padlock stamped “PG&amp;E.”</p>
<p id="b306-4"><page-number citation-index="1" label="116">*116</page-number>Knights was arrested, and a federal grand jury subsequently indicted him for conspiracy to commit arson, for possession of an unregistered destructive device, and for being a felon in possession of ammunition. Knights moved to suppress the evidence obtained during the search of his apartment. The District Court held that Detective Hancock had “reasonable suspicion” to believe that Knights was involved with incendiary materials. App. to Pet. for Cert. 30a. The District Court nonetheless granted the motion to suppress on the ground that the search was for “investigatory” rather than “probationary” purposes. The Court of Appeals for the Ninth Circuit affirmed. <span class="citation multiple-matches"><a href="/c/F.%203d/219/1138/">219 F. 3d 1138</a></span> (2000). The Court of Appeals relied on its earlier decisions holding that the search condition in Knights’ probation order “must be seen as limited to probation searches, and must stop short of investigation searches.” <em>Id., </em>at 1142-1143 (citing <em>United States </em>v. <em>Ooley, </em><span class="citation" data-id="741978"><a href="/opinion/741978/united-states-of-america-plaintiff-appellee-v-norman-lee-ooley-jr/#371" aria-description="Citation for case: UNITED STATES of America, Plaintiff-Appellee, v. Norman...">116 F. 3d 370, 371</a></span> (CA9 1997)).</p>
<p id="b306-5">The Supreme Court of California has rejected this distinction and upheld searches pursuant to the California probation condition “whether the purpose of the search is to monitor the probationer or to serve some other law enforcement purpose.” <em>People </em>v. <em>Woods, </em><span class="citation" data-id="5452320"><a href="/opinion/5607944/people-v-woods/#681" aria-description="Citation for case: People v. Woods">21 Cal. 4th 668, 681</a></span>, <span class="citation" data-id="5452320"><a href="/opinion/5607944/people-v-woods/#1027" aria-description="Citation for case: People v. Woods">981 P. 2d 1019, 1027</a></span> (1999), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./529/1023/">529 U. S. 1023</a></span> (2000). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./532/1018/">532 U. S. 1018</a></span> (2001), to assess the constitutionality of searches made pursuant to this common California probation condition.</p>
<p id="b306-6">Certainly nothing in the condition of probation suggests that it was confined to searches bearing upon probationary status and nothing more. The search condition provides that Knights will submit to a search “by any probation officer or law enforcement officer” and does not mention anything about purpose. App. 49. The question then is whether the Fourth Amendment limits searches pursuant to this probation condition to those with a “probationary” purpose.</p>
<p id="b307-4"><page-number citation-index="1" label="117">*117</page-number>Knights argues that this limitation follows from our decision in <em>Griffin </em>v. <em>Wisconsin, </em><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868</a></span> (1987). Brief for Respondent 14. In <em><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span>, </em>we upheld a search of a probationer conducted pursuant to a Wisconsin regulation permitting “any probation officer to search a probationer’s home without a warrant as long as his supervisor approves and as long as there are ‘reasonable grounds’ to believe the presence of contraband,” <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#870" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S., at 870-871</a></span>. The Wisconsin regulation that authorized the search was not an express condition of Griffin’s probation; in fact, the regulation was not even promulgated at the time of Griffin’s sentence.<footnotemark>2</footnotemark> The regulation applied to all Wisconsin probationers, with no need for a judge to make an individualized determination that the probationer’s conviction justified the need for warrantless searches. We held that a State’s operation of its probation system presented a “special need” for the “exercise of supervision to assure that [probation] restrictions are in fact observed.” <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#875" aria-description="Citation for case: Griffin v. Wisconsin"><em>Id., </em>at 875</a></span>. That special need for supervision justified the Wisconsin regulation and the search pursuant to the regulation was thus reasonable. <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#875" aria-description="Citation for case: Griffin v. Wisconsin"><em>Id., </em>at 875-880</a></span>.</p>
<p id="b307-5">In Knights’ view, apparently shared by the Court of Appeals, a warrantless search of. a probationer satisfies the Fourth Amendment only if it is just like the search at issue in <em><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span> </em>— i. <em>e., </em>a “special needs” search conducted by a probation officer monitoring whether the probationer is complying with probation restrictions. This dubious logic — that an opinion upholding the constitutionality of a particular search implicitly holds unconstitutional any search that is not like it — runs contrary to <em>Griffin’s </em>express statement that its “special needs” holding made it “unnecessary to consider whether” warrantless searches of probationers were other<page-number citation-index="1" label="118">*118</page-number>wise reasonable within the meaning of the Fourth Amendment.<footnotemark>3</footnotemark> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#878" aria-description="Citation for case: Griffin v. Wisconsin"><em>Id., </em>at 878,880</a></span>.</p>
<p id="b308-5">We now consider that question in assessing the constitutionality of the search of Knights’ apartment. The Government, advocating the approach of the Supreme Court of California, see <em><span class="citation" data-id="5452320"><a href="/opinion/5607944/people-v-woods/" aria-description="Citation for case: People v. Woods">Woods, supra,</a></span> </em>contends that the search satisfied the Fourth Amendment under the “consent” rationale of cases such as <em>Zap </em>v. <em>United States, </em><span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/" aria-description="Citation for case: Zap v. United States">328 U. S. 624</a></span> (1946), and <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973). In the Government’s view, Knights’ acceptance of the search condition was voluntary because he had the option of rejecting probation and going to prison instead, which the Government argues is analogous to the voluntary decision defendants often make to waive their right to a trial and accept a plea bargain.<footnotemark>4</footnotemark></p>
<p id="b308-6">We need not decide whether Knights’ acceptance of the search condition constituted consent in the <em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span> </em>sense of a complete waiver of his Fourth Amendment rights, however, because we conclude that the search of Knights was reasonable under our general Fourth Amendment approach of “examining the totality of the circumstances,” <em>Ohio </em>v. <em>Robinette, </em><span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/#39" aria-description="Citation for case: Ohio v. Robinette">519 U. S. 33, 39</a></span> (1996), with the probation search condition being a salient circumstance.</p>
<p id="b308-7">The touchstone of the Fourth Amendment is reasonableness, and the reasonableness of a search is determined “by <page-number citation-index="1" label="119">*119</page-number>assessing, on the one hand, the degree to which it intrudes upon an individual’s privacy and, on the other, the degree to which it is needed for the promotion of legitimate governmental interests.” <em>Wyoming </em>v. <em>Houghton, </em><span class="citation" data-id="9433782"><a href="/opinion/118277/wyoming-v-houghton/#300" aria-description="Citation for case: Wyoming v. Houghton">526 U. S. 295, 300</a></span> (1999). Knights’ status as a probationer subject to a search condition informs both sides of that balance. “Probation, like incarceration, is ‘a form of criminal sanction imposed by a court upon an offender after verdict, finding, or plea of guilty.’ ” <em><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin, supra,</a></span> </em>at 874 (quoting G. Killinger, H. Kerper, &amp; P. Cromwell, Probation and Parole in the Criminal Justice System 14 (1976)). Probation is “one point. . . on a continuum of possible punishments ranging from solitary confinement in a maximum-security facility to a few hours of mandatory community service.” <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#874" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S., at 874</a></span>. Inherent in the very nature of probation is that probationers “do not enjoy/the absolute liberty to which every citizen is entitled.’” <em>Ibid, </em>(quoting <em>Morrissey </em>v. <em>Brewer, </em><span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/#480" aria-description="Citation for case: Morrissey v. Brewer">408 U. S. 471, 480</a></span> (1972)). Just as other punishments for criminal convictions curtail an offender’s freedoms, a court granting probation may impose reasonable conditions that deprive the offender of some freedoms enjoyed by law-abiding citizens.</p>
<p id="b309-5">The judge who sentenced Knights to probation determined that it was necessary to condition the probation on Knights’ acceptance of the search provision. It was reasonable to conclude that the search condition would further the two primary goals of probation — rehabilitation and protecting society from future criminal violations.<footnotemark>5</footnotemark> The probation order clearly expressed the search condition and Knights was unambiguously informed of it. The probation condition <page-number citation-index="1" label="120">*120</page-number>thus significantly diminished Knights’ reasonable expectation of privacy.<footnotemark>6</footnotemark></p>
<p id="b310-5">In assessing the governmental interest side of the balance, it must be remembered that “the very assumption of the institution of probation” is that the probationer “is more likely than the ordinary citizen to violate the law.” <em>Griffin, </em><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#880" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S., at 880</a></span>. The recidivism rate of probationers is significantly higher than the general crime rate. See U. S. Dept, of Justice, Office of Justice Programs, Bureau of Justice Statistics, Recidivism of Felons on Probation, 1986-89, pp. 1, 6 (Feb. 1992) (reporting that 43% of 79,000 felons placed on probation in 17 States were rearrested for a felony within three years while still on probation); U. S. Dept, of Justice, Office of Justice Programs, Bureau of Justice Statistics, Probation and Parole Violators in State Prison, 1991, p. 3 (Aug. 1995) (stating that in 1991, 23% of state prisoners were probation violators). And probationers have even more of an incentive to conceal their criminal activities and quickly dispose of incriminating evidence than the ordinary criminal because probationers are aware that they may be subject to supervision and face revocation of probation, and possible incarceration, in proceedings in which the trial rights of a jury and proof beyond a reasonable doubt, among other things, do not apply, see <em>Minnesota </em>v. <em>Murphy, </em><span class="citation" data-id="9429504"><a href="/opinion/111105/minnesota-v-murphy/#435" aria-description="Citation for case: Minnesota v. Murphy">465 U. S. 420, 435, n. 7</a></span> (1984) (“[TJhere is no right to a jury trial before probation may be revoked”); <span class="citation no-link">18 U. S. C. § 3583</span>(e).</p>
<p id="b310-6">The State has a dual concern with a probationer. On the one hand is the hope that he will successfully complete pro<page-number citation-index="1" label="121">*121</page-number>bation and be integrated back into the community. On the other is the concern, quite justified, that he will be more likely to engage in criminal conduct than an ordinary member of the community. The view of the Court of Appeals in this case would require the State to shut its eyes to the latter concern and concentrate only on the former. But we hold that the Fourth Amendment does not put the State to such a choice. Its interest in apprehending violators of the criminal law, thereby protecting potential victims of criminal enterprise, may therefore justifiably focus on probationers in a way that it does'not on the ordinary citizen.</p>
<p id="b311-5">We hold that the balance of these considerations requires no more than reasonable suspicion to conduct a search of this probationer’s house. The degree of individualized suspicion required of a search is a determination of when there is a sufficiently high probability that criminal conduct is occurring to make the intrusion on the individual’s privacy interest reasonable. See <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#418" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 418</a></span> (1981) (individualized suspicion deals “with probabilities”). Although the Fourth Amendment ordinarily requires the degree of probability embodied in the term “probable cause,” a lesser degree satisfies the Constitution when the balance of governmental and private interests makes such a standard reasonable. See, <em>e.g., Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968); <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975). Those interests warrant a lesser than probable-cause standard here. When an officer has reasonable suspicion that a probationer subject to a search condition is engaged in criminal activity, there is enough likelihood that criminal conduct is occurring that an intrusion on the probationer’s significantly diminished privacy interests is reasonable.</p>
<p id="b311-6">The same circumstances that lead us to conclude that reasonable suspicion is constitutionally sufficient also render a warrant requirement unnecessary. See <em>Illinois </em>v. <em>McArthur, </em><span class="citation" data-id="9434039"><a href="/opinion/118405/illinois-v-mcarthur/#330" aria-description="Citation for case: Illinois v. McArthur">531 U. S. 326, 330</a></span> (2001) (noting that general <page-number citation-index="1" label="122">*122</page-number>or individual circumstances, including “diminished expectations of privacy,” may justify an exception to the warrant requirement).</p>
<p id="b312-5">Because our holding rests on ordinary Fourth Amendment analysis that considers all the circumstances of a search, there is no basis for examining official purpose. With the limited exception of some special needs and administrative search cases, see <em>Indianapolis </em>v. <em>Edmond, </em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#45" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S. 32, 45</a></span> (2000), “we have been unwilling to entertain Fourth Amendment challenges based on the actual motivations of individual officers.” <em>Whren </em>v. <em>United States, </em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#813" aria-description="Citation for case: Whren v. United States">517 U. S. 806, 813</a></span> (1996).</p>
<p id="b312-6">The District Court found, and Knights concedes, that the search in this case was supported by reasonable suspicion. We therefore hold that the warrantless search of Knights, supported by reasonable suspicion and authorized by a condition of probation, was reasonable within the meaning of the Fourth Amendment. The judgment of the Court of Appeals is reversed, and the cause is remanded for further proceedings consistent with this opinion.</p>
<p id="b312-7">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b305-7"> Hancock had seen a copy of the probation order when he was checking Knights’ file in the Sheriff’s Department office.</p>
</footnote>
<footnote label="2">
<p id="b307-6"> Griffin was placed on probation in September 1980, <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#870" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S., at 870</a></span>, and the regulation was not promulgated until December 1981, <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#871" aria-description="Citation for case: Griffin v. Wisconsin"><em>id., </em>at 871</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b308-8"> The Wisconsin Supreme Court had held in <em><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span> </em>that “probation diminishes a probationer’s reasonable expectation of privacy — so that a probation officer may, consistent with the Fourth Amendment, search a probationer’s home without a warrant, and with only ‘reasonable grounds’ (not probable cause) to believe that contraband is present.” <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#872" aria-description="Citation for case: Griffin v. Wisconsin"><em>Id., </em>at 872</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b308-9"> The Government sees our unconstitutional conditions doctrine as a limitation on what a probationer may validly consent to in a probation order. The Government argues that the search condition is not an unconstitutional condition because waiver of Fourth Amendment rights “directly furthers the State’s interest in the effective administration of its probation system.” Brief for United States 22.</p>
</footnote>
<footnote label="5">
<p id="b309-6"> Under California law, a probation condition is invalid if it (1) has no relationship to the crime of which defendant was convicted; (2) relates to conduct which in itself is not criminal; and (3) requires or forbids conduct which is not reasonably related to future criminality. <em>People </em>v. <em>Lent, </em><span class="citation" data-id="9543130"><a href="/opinion/1162126/people-v-lent/#485" aria-description="Citation for case: People v. Lent">15 Cal. 3d 481, 485-486</a></span>, <span class="citation" data-id="9543130"><a href="/opinion/1162126/people-v-lent/#548" aria-description="Citation for case: People v. Lent">541 P. 2d 545, 548</a></span> (1975).</p>
</footnote>
<footnote label="6">
<p id="b310-7"> We do not decide whether the probation condition so diminished, or completely eliminated, Knights’ reasonable expectation of privacy (or constituted consent, see <em>supra, </em>at 118) that a search by a law enforcement officer without any individualized suspicion would have satisfied the reasonableness requirement of the Fourth Amendment. The terms of the probation condition permit such a search, but we need not address the constitutionality of a suspicionless search because the search in this case was supported by reasonable suspicion.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Knotts.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Knotts"
type: case
citation: "460 U.S. 276 (1983)"
parallel_cite: "103 S. Ct. 1081; 75 L. Ed. 2d 55; 51 U.S.L.W. 4232"
neutral_cite: 1983 U.S. LEXIS 135
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-03-02
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1983-03-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Knotts
  varies_by_point: false
  scope_note: "Good law for short-term tracking of public movements. United States v. Jones (2012) decided GPS installation on trespass grounds without disturbing Knotts, and Carpenter (2018) distinguished short-term public tracking from long-term aggregation; neither overruled Knotts."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110882/united-states-v-knotts/"
  cluster_id: 110882
  opinion_id: 9429102
  identity_checked: true
homes:
  - page: "[[Real-Time Tracking]]"
    role: "Key — Anchor (baseline)"
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Related (cross-ref — umbrella)"
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Karo]]", "[[United States v. Jones]]", "[[Carpenter v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "beeper", "tracking", "surveillance", "public-movements"]
holding: "Beeper-aided tracking of a vehicle over public roads is not a search; a person has no reasonable expectation of privacy in his movements over public thoroughfares."
lake:
  record_id: United States v. Knotts
  status: verified
  projected_at: 2026-07-09
---

# United States v. Knotts

*460 U.S. 276 (1983)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
With the seller's consent, officers placed a beeper in a drum of chloroform purchased by a co-conspirator. Using visual surveillance aided by the beeper, agents tracked the drum as it was driven over public roads to a secluded cabin. The tracking, combined with other facts, supported a search warrant for the cabin. Knotts argued the beeper-aided tracking was a warrantless search.

## Issue
Whether monitoring a beeper's signals to track a vehicle's movements over public roads invades a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] and thus constitutes a Fourth Amendment search.

## Rule
No. "A person traveling in an automobile on public thoroughfares has no reasonable expectation of privacy in his movements from one place to another." — 460 U.S. at 281. ^pin-281

The beeper added nothing the Fourth Amendment protects against: "Nothing in the Fourth Amendment prohibited the police from augmenting the sensory faculties bestowed upon them at birth with such enhancement as science and technology afforded them in this case." — [*Id.* at 282](https://www.courtlistener.com/opinion/110882/united-states-v-knotts/#:~:text=Nothing%20in%20the%20Fourth%20Amendment). ^pin-282

## Application
As the chloroform drum traveled the public roads, the driver voluntarily exposed his route, stops, and destination to anyone who cared to look. The beeper merely supplemented the agents' visual surveillance of those publicly observable movements; it revealed nothing about the interior of the cabin or any other constitutionally protected space. Because no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] was invaded, the tracking was not a search and required no warrant.

## Conclusion
The beeper-aided tracking of public movements was not a Fourth Amendment search. Paired with [[United States v. Karo]] (monitoring inside a residence is a search), *Knotts* anchors the public-movements / interior-of-the-home line for location-tracking technology.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Companion to [[United States v. Karo]]. [[United States v. Jones]] (2012) reached GPS *installation* on a trespass theory while preserving *Knotts*; [[Carpenter v. United States]] (2018) distinguished short-term public tracking (Knotts) from the long-term, comprehensive aggregation of cell-site records. *Knotts*' core holding for short-term public tracking stands.

## Appears on
- [[Real-Time Tracking]] — *Key — Anchor (baseline)*
- [[Third-Party Doctrine & CSLI]] — *Related (cross-ref — umbrella)*
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*

## Sources
- *United States v. Knotts*, 460 U.S. 276 (1983) — https://www.courtlistener.com/opinion/110882/united-states-v-knotts/ — pinpoints: 281, 282.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "df3d08717aaebcb2", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Knotts"}, "payload": {"all": [{"cite": "460 U.S. 276", "page": "276", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "460"}, {"cite": "103 S. Ct. 1081", "page": "1081", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "103"}, {"cite": "75 L. Ed. 2d 55", "page": "55", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "75"}, {"cite": "1983 U.S. LEXIS 135", "page": "135", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1983"}, {"cite": "51 U.S.L.W. 4232", "page": "4232", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "51"}], "display": "460 U.S. 276", "official": {"cite": "460 U.S. 276", "page": "276", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "460"}, "official_selection_present": true, "record_id": "United States v. Knotts"}}
{"assertion_id": "166aee4028f72fce", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-282", "record_id": "United States v. Knotts"}, "payload": {"fragment": "#:~:text=Nothing%20in%20the%20Fourth%20Amendment", "page": null, "pin_id": "pin-282", "pinpoint_status": "star-verified", "quote": "Nothing in the Fourth Amendment prohibited the police from augmenting the sensory faculties bestowed upon them at birth with such enhancement as science and technology afforded them in this case.", "quote_fidelity": "matched", "record_id": "United States v. Knotts", "star_marker": "282"}}
{"assertion_id": "bf47842b24d55802", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-281", "record_id": "United States v. Knotts"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-281", "pinpoint_status": "slip-only", "quote": "--- # United States v. Knotts *460 U.S. 276 (1983)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background With the seller's consent, officers placed a beeper in a drum of chloroform purchased by a co-conspirator. Using visual surveillance aided by the beeper, agents tracked the drum as it was driven over public roads to a secluded cabin. The tracking, combined with other facts, supported a search warrant for the cabin. Knotts argued the beeper-aided tracking was a warrantless search. ## Issue Whether monitoring a beeper's signals to track a vehicle's movements over public roads invades a reasonable expectation of privacy and thus constitutes a Fourth Amendment search. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "United States v. Knotts", "star_marker": null}}
{"assertion_id": "4c8e0b40d8da1f28", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Knotts"}, "payload": {"as_of_content": "1983-03-02", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Knotts", "scope_note": "Good law for short-term tracking of public movements. United States v. Jones (2012) decided GPS installation on trespass grounds without disturbing Knotts, and Carpenter (2018) distinguished short-term public tracking from long-term aggregation; neither overruled Knotts.", "varies_by_point": false}}
```

### lake record — United States v. Knotts

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Knotts",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Knotts",
    "case_name_short": "Knotts",
    "case_name_full": "United States v. Knotts",
    "input_case_name": "United States v. Knotts",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-03-02",
    "year": 1983,
    "docket": null,
    "cluster_id": 110882,
    "lead_opinion_id": 9429102,
    "sibling_ids": [
      110882,
      9429102,
      9429103,
      9429104
    ],
    "absolute_url": "/opinion/110882/united-states-v-knotts/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "460 U.S. 276",
      "volume": "460",
      "reporter": "U.S.",
      "page": "276",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 1081",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "1081",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 2d 55",
        "volume": "75",
        "reporter": "L. Ed. 2d",
        "page": "55",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4232",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4232",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 135",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "135",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "460 U.S. 276",
        "volume": "460",
        "reporter": "U.S.",
        "page": "276",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 1081",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "1081",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 2d 55",
        "volume": "75",
        "reporter": "L. Ed. 2d",
        "page": "55",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 135",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "135",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4232",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4232",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "460 U.S. 276",
    "official_selection": {
      "court_class": "scotus",
      "selected": "460 U.S. 276",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-281",
      "page": null,
      "quote": "--- # United States v. Knotts *460 U.S. 276 (1983)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background With the seller's consent, officers placed a beeper in a drum of chloroform purchased by a co-conspirator. Using visual surveillance aided by the beeper, agents tracked the drum as it was driven over public roads to a secluded cabin. The tracking, combined with other facts, supported a search warrant for the cabin. Knotts argued the beeper-aided tracking was a warrantless search. ## Issue Whether monitoring a beeper's signals to track a vehicle's movements over public roads invades a reasonable expectation of privacy and thus constitutes a Fourth Amendment search. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-282",
      "page": null,
      "quote": "Nothing in the Fourth Amendment prohibited the police from augmenting the sensory faculties bestowed upon them at birth with such enhancement as science and technology afforded them in this case.",
      "star_marker": "282",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15056,
      "fragment": "#:~:text=Nothing%20in%20the%20Fourth%20Amendment",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1983-03-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Knotts",
    "varies_by_point": false,
    "scope_note": "Good law for short-term tracking of public movements. United States v. Jones (2012) decided GPS installation on trespass grounds without disturbing Knotts, and Carpenter (2018) distinguished short-term public tracking from long-term aggregation; neither overruled Knotts.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "United States v. Knotts:lane1_negative"
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
        "journal_ref": "United States v. Knotts:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4381539,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4288590,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4287047,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4286131,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Augustine",
          "cluster_id": 6580805,
          "cite": [
            "467 Mass. 230",
            "4 N.E.3d 846",
            "2014 WL 901649",
            "2014 Mass. LEXIS 30"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane1_negative"
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
        "journal_ref": "United States v. Knotts:lane1_negative"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jardines",
          "cluster_id": 856347,
          "cite": [
            "185 L. Ed. 2d 495",
            "133 S. Ct. 1409",
            "569 U.S. 1",
            "2013 U.S. LEXIS 2542",
            "24 Fla. L. Weekly Fed. S 117",
            "81 U.S.L.W. 4209",
            "2013 WL 1196577"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Chesternut",
          "cluster_id": 112095,
          "cite": [
            "100 L. Ed. 2d 565",
            "108 S. Ct. 1975",
            "486 U.S. 567",
            "1988 U.S. LEXIS 2582",
            "56 U.S.L.W. 4558"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Andreas",
          "cluster_id": 111013,
          "cite": [
            "77 L. Ed. 2d 1003",
            "103 S. Ct. 3319",
            "463 U.S. 765",
            "1983 U.S. LEXIS 106",
            "51 U.S.L.W. 5157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. MacOn",
          "cluster_id": 111477,
          "cite": [
            "86 L. Ed. 2d 370",
            "105 S. Ct. 2778",
            "472 U.S. 463",
            "1985 U.S. LEXIS 110",
            "53 U.S.L.W. 4783"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Douglas Emmons v. Robert McLaughlin Donald Ratliff, Gary Dewalt, City of Norwalk, Reese Wineman",
          "cluster_id": 522917,
          "cite": [
            "874 F.2d 351"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Riley",
          "cluster_id": 112175,
          "cite": [
            "102 L. Ed. 2d 835",
            "109 S. Ct. 693",
            "488 U.S. 445",
            "1989 U.S. LEXIS 580"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Young",
          "cluster_id": 1196592,
          "cite": [
            "867 P.2d 593",
            "123 Wash. 2d 173",
            "1994 Wash. LEXIS 122"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anita Christensen and Robert Alty v. County of Boone, Illinois, and Edward Krieger",
          "cluster_id": 797469,
          "cite": [
            "483 F.3d 454"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas",
          "cluster_id": 8939436,
          "cite": [
            "757 F.2d 1359"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jimmy Dewitt Webster, Sr., Candido Daniel Santiago, Barry Weinreich, Joe Buhajla, Arthur Byron Murphy, and Clarence Royalston",
          "cluster_id": 445460,
          "cite": [
            "750 F.2d 307"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4621444,
          "cite": [
            "2019 CO 36",
            "446 P.3d 397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Maynard",
          "cluster_id": 152441,
          "cite": [
            "615 F.3d 544",
            "392 U.S. App. D.C. 291",
            "2010 U.S. App. LEXIS 16417",
            "2010 WL 3063788"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas",
          "cluster_id": 449643,
          "cite": [
            "757 F.2d 1359",
            "1985 U.S. App. LEXIS 29735"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Campbell",
          "cluster_id": 1215380,
          "cite": [
            "759 P.2d 1040",
            "306 Or. 157",
            "1988 Ore. LEXIS 400"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Donald Wesley Taylor, United States of America v. Steven Wayne Pressler, and Donald Wesley Taylor",
          "cluster_id": 424125,
          "cite": [
            "716 F.2d 701",
            "14 Fed. R. Serv. 218",
            "1983 U.S. App. LEXIS 16622"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110882 OR 9429102 OR 9429103 OR 9429104) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjY0OTgyNDAwMDAwJnM9MTMyNDYzNyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110882+OR+9429102+OR+9429103+OR+9429104%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 8,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 8,
        "triage_snippet_classified": 192
      },
      "lane2_top_cited": {
        "query": "cites:(110882 OR 9429102 OR 9429103 OR 9429104)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDMmcz00Mzg2NzcmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110882+OR+9429102+OR+9429103+OR+9429104%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110882 OR 9429102 OR 9429103 OR 9429104)",
        "reviewed": 27,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 27,
        "triage_read": 0,
        "triage_snippet_classified": 27
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110882 OR 9429102 OR 9429103 OR 9429104)",
    "indexed_citing_opinions": 454,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110882,
        "count": 368,
        "count_source": "search"
      },
      {
        "opinion_id": 9429102,
        "count": 96,
        "count_source": "search"
      },
      {
        "opinion_id": 9429103,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429104,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 751,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-knotts.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4NjY4Njgmcz05OTg2MTg3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110882+OR+9429102+OR+9429103+OR+9429104%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110882,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 101118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 109876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 337810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 342454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 349387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 352591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 356186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 364698,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 378215,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 380205,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 396251,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 402220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 1092690,
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
    "date_created": "2026-07-06T01:11:45Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:12:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:12:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:16:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:12:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Knotts

```
<opinion type="majority">
<author id="b339-11">Justice Rehnquist</author>
<p id="A4t">delivered the opinion of the Court.</p>
<p id="b339-12">A beeper is a radio transmitter, usually battery operated, which emits periodic signals that can be picked up by a radio receiver. In this case, a beeper was placed in a five-gallon drum containing chloroform purchased by one of respondent’s codefendants. By monitoring the progress of a car carrying the chloroform Minnesota law enforcement agents were able to trace the can of chloroform from its place of purchase in Minneapolis, Minn., to respondent’s secluded cabin near Shell Lake, Wis. The issue presented by the case is whether such use of a beeper violated respondent’s rights secured by the Fourth Amendment to the United States Constitution.</p>
<p id="b339-13">I — &lt;</p>
<p id="b339-3">Respondent and two codefendants were charged in the United States District Court for the District of Minnesota with conspiracy to manufacture controlled substances, including but not limited to methamphetamine, in violation of <span class="citation no-link">21 U. S. C. §846</span>. One of the codefendants, Darryl Petschen, <page-number citation-index="1" label="278">*278</page-number>was tried jointly with respondent; the other codefendant, Tristan Armstrong, pleaded guilty and testified for the Government at trial.</p>
<p id="b340-5">Suspicion attached to this trio when the 3M Co., which manufactures chemicals in St. Paul, notified a narcotics investigator for the Minnesota Bureau of Criminal Apprehension that Armstrong, a former 3M employee, had been stealing chemicals which could be used in manufacturing illicit drugs. Visual surveillance of Armstrong revealed that after leaving the employ of 3M Co., he had been purchasing similar chemicals from the Hawkins Chemical Co. in Minneapolis. The Minnesota narcotics officers observed that after Armstrong had made a purchase, he would deliver the chemicals to codefendant Petschen.</p>
<p id="b340-6">With the consent of the Hawkins Chemical Co., officers installed a beeper inside a five-gallon container of chloroform, one of the so-called “precursor” chemicals used to manufacture illicit drugs. Hawkins agreed that when Armstrong next purchased chloroform, the chloroform would be placed in this particular container. When Armstrong made the purchase, officers followed the car in which the chloroform had been placed, maintaining contact by using both visual surveillance and a monitor which received the signals sent from the beeper.</p>
<p id="b340-7">Armstrong proceeded to Petschen’s house, where the container was transferred to Petschen’s automobile. Officers then followed that vehicle eastward towards the state line, across the St. Croix River, and into Wisconsin. During the latter part of this journey, Petschen began making evasive maneuvers, and the pursuing agents ended their visual surveillance. At about the same time officers lost the signal from the beeper, but with the assistance of a monitoring device located in a helicopter the approximate location of the signal was picked up again about one hour later. The signal now was stationary and the location identified was a cabin occupied by respondent near Shell Lake, Wis. The record before us does not reveal that the beeper was used after the <page-number citation-index="1" label="279">*279</page-number>location in the area of the cabin had been initially determined.</p>
<p id="b341-5">Relying on the location of the chloroform derived through the use of the beeper and additional information obtained during three days of intermittent visual surveillance of respondent’s cabin, officers secured a search warrant. During execution of the warrant, officers discovered a fully operable, clandestine drug laboratory in the cabin. In the laboratory area officers found formulas for amphetamine and methamphetamine, over $10,000 worth of laboratory equipment, and chemicals in quantities sufficient to produce 14 pounds of pure amphetamine. Under a barrel outside the cabin, officers located the five-gallon container of chloroform.</p>
<p id="b341-6">After his motion to suppress evidence based on the war-rantless monitoring of the beeper was denied, respondent was convicted for conspiring to manufacture controlled substances in violation of 21 U. S. C. .§ 846. He was sentenced to five years’ imprisonment. A divided panel of the United States Court of Appeals for the Eighth Circuit reversed the conviction, finding that.the monitoring of the beeper was prohibited by the Fourth Amendment because its use had violated respondent’s reasonable expectation of privacy, and that all information derived after the location of the cabin was a fruit of the illegal beeper monitoring.<footnotemark>*</footnotemark> <span class="citation" data-id="9468533"><a href="/opinion/396251/united-states-v-leroy-carlton-knotts-and-darryl-petschen/" aria-description="Citation for case: United States v. Leroy Carlton Knotts and Darryl Petschen">662 F. 2d 515</a></span> <page-number citation-index="1" label="280">*280</page-number>(1981). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./457/1131/">457 U. S. 1131</a></span> (1982), and we now reverse the judgment of the Court of Appeals.</p>
<p id="b342-3">In <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span> (1928), this Court held that the wiretapping of a defendant’s private telephone line did not violate the Fourth Amendment because the wiretapping had been effectuated without a physical trespass by the Government. Justice Brandéis, joined by Justice Stone, dissented from that decision, believing that the actions of the Government in that case constituted an “unjustifiable intrusion . . . upon the privacy of the individual,” and therefore a violation of the Fourth Amendment. <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#478" aria-description="Citation for case: Olmstead v. United States"><em>Id., </em>at 478</a></span>. Nearly 40 years later, in <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), the Court overruled <em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">Olmstead</a></span> </em>saying that the Fourth Amendment’s reach “cannot turn upon the presence or absence of a physical intrusion into any given enclosure.” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States">389 U. S., at 353</a></span>. The Court said:</p>
<blockquote id="b342-4">“The Government’s activities in electronically listening to and recording the petitioner’s words violated the privacy upon which he justifiably relied while using the telephone booth and thus constituted a ‘search and seizure’ within the meaning of the Fourth Amendment. The fact that the electronic device employed to achieve that end did not happen to penetrate the wall of the booth can have no constitutional significance.” <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Ibid.</a></span></em></blockquote>
<p id="b342-5">In <em>Smith </em>v. <em>Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735</a></span> (1979), we elaborated on the principles stated in <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>:</em></p>
<blockquote id="b342-6">“Consistently with <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>this Court uniformly has held that the application of the Fourth Amendment depends on whether the person invoking its protection can claim a ‘justifiable,’ a ‘reasonable,’ or a ‘legitimate expectation of privacy’ that has been invaded by government action. [Citations omitted.] This inquiry, as Mr. Justice Harlan aptly noted in his <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>concurrence, normally embraces <page-number citation-index="1" label="281">*281</page-number>two discrete questions. The first is whether the individual, by his conduct, has ‘exhibited an actual (subjective) expectation of privacy,’ <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S., at 361</a></span> — whether, in the words of the <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>majority, the individual has shown that ‘he seeks to preserve [something] as private.’ <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States"><em>Id., </em>at 351</a></span>. The second question is whether the individual’s subjective expectation of privacy is ‘one that society is prepared to recognize as “reasonable,”’ <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">id.,</a></span> </em>at 361— whether, in the words of the <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>majority, the individual’s expectation, viewed objectively, is ‘justifiable’ under the circumstances. <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States"><em>Id., at </em>353</a></span>. <em>See Rakas </em>v. <em>Illinois, </em>439 U. S., at 143-144, n. 12; <em>id., </em>at 151 (concurring opinion); <em>United States </em>v. <em>White, </em>401 U. S., at 752 (plurality opinion).” <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#740" aria-description="Citation for case: Smith v. Maryland">442 U. S., at 740-741</a></span> (footnote omitted).</blockquote>
<p id="b343-5">The governmental surveillance conducted by means of the beeper in this case amounted principally to the following of an automobile on public streets and highways. We have commented more than once on the diminished expectation of privacy in an automobile:</p>
<blockquote id="b343-6">“One has a lesser expectation of privacy in a motor vehicle because its function is transportation and it seldom serves as one’s residence or as the repository of personal effects. A car has little capacity for escaping public scrutiny. It travels public thoroughfares where both its occupants and its contents are in plain view.” <em>Cardwell </em>v. <em>Lewis, </em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590</a></span> (1974) (plurality opinion).</blockquote>
<p id="b343-7">See also <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#153" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 153-154</a></span>, and n. 2 (1978) (Powell, J., concurring); <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#368" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 368</a></span> (1976).</p>
<p id="b343-8">A person traveling in an automobile on public thoroughfares has no reasonable expectation of privacy in his movements from one place to another. When Petschen traveled over the public streets he voluntarily conveyed to anyone who wanted to look the fact that he was traveling over par<page-number citation-index="1" label="282">*282</page-number>ticular roads in a particular direction, the fact of whatever stops he made, and the fact of his final destination when he exited from public roads onto private property.</p>
<p id="b344-5">Respondent Knotts, as the owner of the cabin and surrounding premises to which Petschen drove, undoubtedly had the traditional expectation of privacy within a dwelling place insofar as the cabin was concerned:</p>
<blockquote id="b344-6">“Crime, even in the privacy of one’s own quarters, is, of course, of grave concern to society, and the law allows such crime to be reached on proper showing. The right of officers to thrust themselves into a home is also of grave concern, not only to the individual, but to a society which chooses to dwell in reasonable security and freedom from surveillance. When the right of privacy must reasonably yield to the right of search is, as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent.” <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948), quoted with approval in <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 586</a></span> (1980).</blockquote>
<p id="b344-7">But no such expectation of privacy extended to the visual observation of Petschen’s automobile arriving on his premises after leaving a public highway, nor to movements of objects such as the drum of chloroform outside the cabin in the “open fields.” <em>Hester </em>v. <em>United States, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924).</p>
<p id="b344-8">Visual surveillance from public places along Petschen’s route or adjoining Knotts’ premises would have sufficed to reveal all of these facts to the police. The fact that the officers in this case relied not only on visual surveillance, but also on the use of the beeper to signal the presence of Petschen’s automobile to the police receiver, does not alter the situation. Nothing in the Fourth Amendment prohibited the police from augmenting the sensory faculties bestowed upon them at birth with such enhancement as science and technology afforded them in this case. In <em>United States </em>v. <em>Lee, </em><span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/" aria-description="Citation for case: United States v. Lee">274 U. S. 559</a></span> (1927), the Court said:</p>
<blockquote id="b345-4"><page-number citation-index="1" label="283">*283</page-number>“But no search on the high seas is shown. The testimony of the boatswain shows that he used a searchlight. It is not shown that there was any exploration below decks or under hatches. For aught that appears, the cases of liquor were on deck and, like the defendants, were discovered before the motor boat was boarded. Such use of a searchlight is comparable to the use of a marine glass or a field glass. It is not prohibited by the Constitution.” <span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/#563" aria-description="Citation for case: United States v. Lee"><em>Id., </em>at 563</a></span>.</blockquote>
<p id="b345-5">We have recently had occasion to deal with another claim which was to some extent a factual counterpart of respondent’s assertions here. In <em>Smith </em>v. <em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">Maryland</a></span>, </em>we said:</p>
<blockquote id="b345-6">“This analysis dictates that [Smith] can claim no legitimate expectation of privacy here. When he used his phone, [Smith] voluntarily conveyed numerical information to the telephone company and ‘exposed’ that information to its equipment in the ordinary course of business. In so doing, [Smith] assumed the risk that the company would reveal to police the numbers he dialed. The switching equipment that processed those numbers is merely the modern counterpart of the operator who, in ' an earlier day, personally completed calls for the subscriber. [Smith] concedes that if he had placed his calls through an operator, he could claim no legitimate expectation of privacy. [Citation omitted.] We are not inclined to hold that a different constitutional result is required because the telephone company has decided to automate.” <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#744" aria-description="Citation for case: Smith v. Maryland">442 U. S., at 744-745</a></span>.</blockquote>
<p id="b345-7">Respondent does not actually quarrel with this analysis, though he expresses the generalized view that the result of the holding sought by the Government would be that “twenty-four hour surveillance of any citizen of this country will be possible, without judicial knowledge or supervision.” Brief for Respondent 9 (footnote omitted). But the fact is that the “reality hardly suggests abuse,” <em>Zurcher </em>v. <em>Stanford </em><page-number citation-index="1" label="284">*284</page-number><em>Daily, </em><span class="citation" data-id="9427224"><a href="/opinion/109876/zurcher-v-stanford-daily/#566" aria-description="Citation for case: Zurcher v. Stanford Daily">436 U. S. 547, 566</a></span> (1978); if such dragnet-type law enforcement practices as respondent envisions should eventually occur, there will be time enough then to determine whether different constitutional principles may be applicable. <em><span class="citation" data-id="9427224"><a href="/opinion/109876/zurcher-v-stanford-daily/" aria-description="Citation for case: Zurcher v. Stanford Daily">Ibid.</a></span> </em>Insofar as respondent’s complaint appears to be simply that scientific devices such as the beeper enabled the police to be more effective in detecting crime, it simply has no constitutional foundation. We have never equated police efficiency with unconstitutionality, and we decline to do so now.</p>
<p id="b346-5">Respondent specifically attacks the use of the beeper insofar as it was used to determine that the can of chloroform had come to rest on his property at Shell Lake, Wis. He repeatedly challenges the “use of the beeper to determine the location of the chemical drum at Respondent’s premises,” Brief for Respondent 26; he states that “[t]he government thus overlooks the fact that this case involves the sanctity of Respondent’s residence, which is accorded the greatest protection available under the Fourth Amendment.” <em><span class="citation" data-id="9427224"><a href="/opinion/109876/zurcher-v-stanford-daily/" aria-description="Citation for case: Zurcher v. Stanford Daily">Ibid.</a></span> </em>The Court of Appeals appears to have rested its decision on this ground:</p>
<blockquote id="b346-6">“As noted above, a principal rationale for allowing war-rantless tracking of beepers, particularly beepers in or on an auto, is that beepers are merely a more effective means of observing what is already public. But people pass daily from public to private spheres. When police agents track bugged personal property without first obtaining a warrant, they must do so at the risk that this enhanced surveillance, intrusive at best, might push fortuitously and unreasonably into the private sphere protected by the Fourth Amendment.” <span class="citation" data-id="9468533"><a href="/opinion/396251/united-states-v-leroy-carlton-knotts-and-darryl-petschen/#518" aria-description="Citation for case: United States v. Leroy Carlton Knotts and Darryl Petschen">662 F. 2d, at 518</a></span>.</blockquote>
<p id="b346-7">We think that respondent’s contentions, and the above-quoted language from the opinion of the Court of Appeals, to some extent lose sight of the limited use which the government made of the signals from this particular beeper. As we have noted, nothing in this record indicates that the beeper <page-number citation-index="1" label="285">*285</page-number>signal was received or relied upon after it had indicated that the drum containing the chloroform had ended its automotive journey at rest on respondent’s premises in rural Wisconsin. Admittedly, because of the failure of the visual surveillance, the beeper enabled the law enforcement officials in this case to ascertain the ultimate resting place of the chloroform when they would not have been able to do so had they relied solely on their naked eyes. But scientific enhancement of this sort raises no constitutional issues which visual surveillance would not also raise. A police car following Petschen at a distance throughout his journey could have observed him leaving the public highway and arriving at the cabin owned by respondent, with the drum of chloroform still in the car. This fact, along with others, was used by the government in obtaining a search warrant which led to the discovery of the clandestine drug laboratory. But there is no indication that the beeper was used in any way to reveal information as to the movement of the drum within the cabin, or in any way that would not have been visible to the naked eye from outside the cabin. Just as notions of physical trespass based on the law of real property were not dispositive in <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), neither were they dis-positive in <em>Hester </em>v. <em>United States, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924).</p>
<p id="b347-5">We thus return to the question posed at the beginning of our inquiry in discussing <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz, supra;</a></span> </em>did monitoring the beeper signals complained of by respondent invade any legitimate expectation of privacy on his part? For the reasons previously stated, we hold it did not. Since it did not, there was neither a “search” nor a “seizure” within the contemplation of the Fourth Amendment. The judgment of the Court of Appeals is therefore</p>
<p id="b347-6">
<em>Reversed.</em>
</p>
<p id="b347-7">Justice Brennan, with whom Justice Marshall joins, concurring in the judgment.</p>
<p id="b347-8">I join Justice Blackmun’s and Justice Stevens’ opinions concurring in the judgment. I should add, however, <page-number citation-index="1" label="286">*286</page-number>that I think this would have been a much more difficult case if respondent had challenged, not merely certain aspects of the monitoring of the beeper installed in the chloroform container purchased by respondent’s compatriot, but also its original installation. See <em>ante, </em>at 279, n. <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), made quite clear that the Fourth Amendment protects against governmental invasions of a person’s reasonable “expectation[s] of privacy,” even when those invasions are not accompanied by physical intrusions. Cases such as <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#509" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 509-512</a></span> (1961), however, hold that, when the Government <em>does </em>engage in physical intrusion of a constitutionally protected area in order to obtain information, that intrusion may constitute a violation of the Fourth Amendment even if the same information could have been obtained by other means. I do not believe that <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>or its progeny, have eroded that principle. Cf. The Supreme Court, 1979 Term, <span class="citation no-link">94 Harv. L. Rev. 75</span>, 203-204 (1980).</p>
<p id="b348-4">I am also entirely unconvinced by the Court of Appeals’ footnote disposing of the installation issue with the statement: “we hold that the consent of the owner [of the chloroform drum] at the time of installation meets the requirements of the Fourth Amendment, even if the consenting owner intends to soon sell the ‘bugged’ property to an unsuspecting buyer. <em>Caveat </em>emptor.” <span class="citation" data-id="9468533"><a href="/opinion/396251/united-states-v-leroy-carlton-knotts-and-darryl-petschen/#517" aria-description="Citation for case: United States v. Leroy Carlton Knotts and Darryl Petschen">662 F. 2d 515, 517, n. 2</a></span> (1981) (citation omitted). The Government is not here defending against a claim for damages in an action for breach of a warranty; it is attempting to justify the legality of a search conducted in the course of a criminal investigation. I am not at all sure that, for purposes of the Fourth Amendment, there is a constitutionally significant difference between planting a beeper in an object in the possession of a criminal suspect and purposefully arranging that he be sold an object that, unknown to him, already has a beeper installed inside it. Cf. <em>Gouled </em>v. <em>United States, </em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#305" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 305-306</a></span> (1921); <em>Lewis </em>v. <em>United States, </em><span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/#211" aria-description="Citation for case: Lewis v. United States">385 U. S. 206, 211</a></span> (1966).</p>
<p id="b349-4"><page-number citation-index="1" label="287">*287</page-number>Respondent claimed at oral argument that, under this Court’s cases, he would not have standing to challenge the original installation of the beeper in the chloroform drum because the drum was sold, not to him, but to one of his compatriots. See <em>ante, </em>at 279, n. If respondent is correct, that would only confirm for me the formalism and confusion in this Court’s recent attempts to redefine Fourth Amendment standing. See <em>Rawlings </em>v. <em>Kentucky, </em><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/#114" aria-description="Citation for case: Rawlings v. Kentucky">448 U. S. 98, 114</a></span> (1980) (Marshall, J., dissenting); <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#156" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 156</a></span> (1978) (White, J., dissenting).</p>
<footnote label="*">
<p id="b341-7">Respondent does not challenge the warrantless installation of the beeper in the chloroform container, suggesting in oral argument that he did not believe he had standing to make such a challenge. We note that while several Courts of Appeals have approved warrantless installations, see <em>United States </em>v. <em>Bernard, </em><span class="citation" data-id="9466894"><a href="/opinion/380205/united-states-v-howard-dale-bernard-united-states-of-america-v-ralph/" aria-description="Citation for case: United States v. Howard Dale Bernard, United States of...">625 F. 2d 854</a></span> (CA9 1980); <em>United States </em>v. <em>Lewis, </em><span class="citation" data-id="378215"><a href="/opinion/378215/united-states-v-john-bradley-lewis-jr-kenneth-brooks-aka-james-earl/" aria-description="Citation for case: United States v. John Bradley Lewis, Jr., Kenneth Brooks,...">621 F. 2d 1382</a></span> (CA5 1980), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./450/935/">450 U. S. 935</a></span> (1981); <em>United States </em>v. <em>Bruneau, </em><span class="citation" data-id="364698"><a href="/opinion/364698/united-states-v-dale-david-bruneau-united-states-of-america-v-jeffrey/" aria-description="Citation for case: United States v. Dale David Bruneau, United States of...">594 F. 2d 1190</a></span> (CA8), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./444/847/">444 U. S. 847</a></span> (1979); <em>United States </em>v. <em>Miroyan, </em><span class="citation multiple-matches"><a href="/c/F.%202d/577/489/">577 F. 2d 489</a></span> (CA9), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./439/896/">439 U. S. 896</a></span> (1978); <em>United States </em>v. <em>Cheshire, </em><span class="citation" data-id="352591"><a href="/opinion/352591/united-states-v-alan-kent-cheshire/" aria-description="Citation for case: United States v. Alan Kent Cheshire">569 F. 2d 887</a></span> (CA5), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./437/907/">437 U. S. 907</a></span> (1978); <em>United States </em>v. <em>Curtis, </em><span class="citation" data-id="8903472"><a href="/opinion/8915345/united-states-v-curtis/" aria-description="Citation for case: United States v. Curtis">562 F. 2d 1153</a></span> (CA9 1977), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./439/910/">439 U. S. 910</a></span> (1978); <em>United States </em>v. <em>Abel, </em><span class="citation" data-id="342454"><a href="/opinion/342454/united-states-v-joseph-e-abel-sr-larry-neal-whittington-james-glenn/" aria-description="Citation for case: United States v. Joseph E. Abel, Sr., Larry Neal...">548 F. 2d 591</a></span> (CA5), cert. denied, 431U. S. 956 (1977); <em>United States </em>v. <em>Hufford, </em>539 F. 2d.32 (CA9), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./429/1002/">429 U. S. 1002</a></span> (1976), we have not before and do not now pass on the issue.</p>
</footnote>
</opinion>
```

---
