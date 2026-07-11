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

## GROUP: _overhaul2/lake/cases/Abel v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Abel v. United States"
type: case
citation: "362 U.S. 217 (1960)"
parallel_cite: "80 S. Ct. 683; 4 L. Ed. 2d 668"
neutral_cite: 1960 U.S. LEXIS 1412
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1960
date_decided: 1960-03-28
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1960-03-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Abel v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106021/abel-v-united-states/"
  cluster_id: 106021
  opinion_id: 106021
  identity_checked: true
homes:
  - page: "[[Abandonment]]"
    role: "Key — Anchor"
related: ["[[Hester v. United States]]", "[[California v. Greenwood]]"]
aliases: ["Abel v. US"]
tags: ["case", "fourth-amendment", "abandonment"]
holding: "Items left in a hotel-room wastebasket after the guest paid up and **vacated** the room were abandoned ('bona vacantia'); their warrantless seizure was lawful."
lake:
  record_id: Abel v. United States
  status: verified
  projected_at: 2026-07-06
---

# Abel v. United States

*362 U.S. 217 (1960)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
INS agents arrested the petitioner — a Soviet intelligence officer using the alias "Martin Collins" — at a New York City hotel on an administrative deportation warrant. Immediately after the petitioner paid his bill and checked out, an FBI agent searched the vacated room with the hotel management's consent and recovered, from the room's wastepaper basket, a hollowed-out pencil and a block of wood containing a "cipher pad." These and other items were introduced against him in an espionage prosecution.

## Issue
Whether the warrantless search of a hotel room — and seizure of items the guest had discarded in the wastebasket — after the guest paid his bill and vacated the room violated the Fourth Amendment.

## Rule
No. Once the guest vacated the room, the hotel regained the exclusive right to possession and could consent to the search; and the items left in the wastebasket were abandoned, so their warrantless seizure was lawful. The search "was entirely lawful, although undertaken without a warrant," because "at the time of the search petitioner had vacated the room. The hotel then had the exclusive right to its possession, and the hotel management freely gave its consent that the search be made." — 362 U.S. at 241. ^pin-241

As to the discarded items: "So far as the record shows, petitioner had abandoned these articles. He had thrown them away. So far as he was concerned, they were *bona vacantia.* There can be nothing unlawful in the Government's appropriation of such abandoned property." — *Id.* at 241. ^pin-241a

## Application
On these facts the FBI agent did not enter until after the petitioner had paid his bill and given up the room, so the hotel — not the petitioner — controlled the space and validly consented to the entry; and the pencil and cipher-pad block had been thrown into the wastebasket as the petitioner packed to leave, marking them as abandoned. Seizing the abandoned articles without a warrant was therefore lawful, and their use in evidence did not offend the Fourth Amendment.

## Conclusion
The warrantless search of the vacated room and seizure of the abandoned wastebasket items were lawful; the evidence was admissible and the conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No subsequent negative treatment. *Abel* remains a foundational statement of the abandoned-property (*bona vacantia*) principle — that one who relinquishes property retains no Fourth Amendment interest in it.
- Related applications of the same abandonment principle: [[California v. Greenwood]] (no expectation of privacy in curbside garbage); [[Hester v. United States]] (open-fields / discarded containers).

## Appears on
- [[Abandonment]] — *Key — Anchor*

## Sources
- *Abel v. United States*, 362 U.S. 217 (1960) — https://www.courtlistener.com/opinion/106021/abel-v-united-states/ — pinpoint: 241.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f7463c9501c4014e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Abel v. United States"}, "payload": {"all": [{"cite": "362 U.S. 217", "page": "217", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "362"}, {"cite": "80 S. Ct. 683", "page": "683", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "80"}, {"cite": "4 L. Ed. 2d 668", "page": "668", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "4"}, {"cite": "1960 U.S. LEXIS 1412", "page": "1412", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1960"}], "display": "362 U.S. 217", "official": {"cite": "362 U.S. 217", "page": "217", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "362"}, "official_selection_present": true, "record_id": "Abel v. United States"}}
{"assertion_id": "4df9b49082fb96d1", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-241", "record_id": "Abel v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-241", "pinpoint_status": "slip-only", "quote": "These and other items were introduced against him in an espionage prosecution. ## Issue Whether the warrantless search of a hotel room — and seizure of items the guest had discarded in the wastebasket — after the guest paid his bill and vacated the room violated the Fourth Amendment. ## Rule No. Once the guest vacated the room, the hotel regained the exclusive right to possession and could consent to the search; and the items left in the wastebasket were abandoned, so their warrantless seizure was lawful. The search", "quote_fidelity": "mismatch", "record_id": "Abel v. United States", "star_marker": null}}
{"assertion_id": "5155b514086db91d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-241a", "record_id": "Abel v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-241a", "pinpoint_status": "slip-only", "quote": "So far as the record shows, petitioner had abandoned these articles. He had thrown them away. So far as he was concerned, they were *bona vacantia.* There can be nothing unlawful in the Government's appropriation of such abandoned property.", "quote_fidelity": "mismatch", "record_id": "Abel v. United States", "star_marker": null}}
{"assertion_id": "161d1db4b3af38d7", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Abel v. United States"}, "payload": {"as_of_content": "1960-03-28", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Abel v. United States", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Abel v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Abel v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Abel v. United States",
    "case_name_short": "Abel",
    "case_name_full": "ABEL, Alias MARK, Alias COLLINS, Alias GOLDFUS, v. UNITED STATES",
    "input_case_name": "Abel v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1960-03-28",
    "year": 1960,
    "docket": null,
    "cluster_id": 106021,
    "lead_opinion_id": 106021,
    "sibling_ids": [
      106021,
      9421949,
      9421950,
      9421951
    ],
    "absolute_url": "/opinion/106021/abel-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8947572,
        "score": 10,
        "case_name": "Abel v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "362 U.S. 217",
      "volume": "362",
      "reporter": "U.S.",
      "page": "217",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "80 S. Ct. 683",
        "volume": "80",
        "reporter": "S. Ct.",
        "page": "683",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 L. Ed. 2d 668",
        "volume": "4",
        "reporter": "L. Ed. 2d",
        "page": "668",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1960 U.S. LEXIS 1412",
        "volume": "1960",
        "reporter": "U.S. LEXIS",
        "page": "1412",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "362 U.S. 217",
        "volume": "362",
        "reporter": "U.S.",
        "page": "217",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 S. Ct. 683",
        "volume": "80",
        "reporter": "S. Ct.",
        "page": "683",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 L. Ed. 2d 668",
        "volume": "4",
        "reporter": "L. Ed. 2d",
        "page": "668",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1960 U.S. LEXIS 1412",
        "volume": "1960",
        "reporter": "U.S. LEXIS",
        "page": "1412",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "362 U.S. 217",
    "official_selection": {
      "court_class": "scotus",
      "selected": "362 U.S. 217",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-241",
      "page": null,
      "quote": "These and other items were introduced against him in an espionage prosecution. ## Issue Whether the warrantless search of a hotel room \u2014 and seizure of items the guest had discarded in the wastebasket \u2014 after the guest paid his bill and vacated the room violated the Fourth Amendment. ## Rule No. Once the guest vacated the room, the hotel regained the exclusive right to possession and could consent to the search; and the items left in the wastebasket were abandoned, so their warrantless seizure was lawful. The search",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-241a",
      "page": null,
      "quote": "So far as the record shows, petitioner had abandoned these articles. He had thrown them away. So far as he was concerned, they were *bona vacantia.* There can be nothing unlawful in the Government's appropriation of such abandoned property.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1960-03-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Abel v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "People v. Konther",
          "cluster_id": 10874455,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ryan Mendoza",
          "cluster_id": 10771114,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Op. Atty. Gen. 3a; 390a6",
          "cluster_id": 10754685,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Bryant",
          "cluster_id": 10747664,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People of Guam v. Joseph Quichocho Taimanglo II (aka Joseph Quichocho Taimanglo; aka Baby Joe; aka Joseph Quintanilla Taimanglo II)",
          "cluster_id": 10713502,
          "cite": [
            "2025 Guam 7"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Charles Aaron Amble and John Joseph Mandracchia",
          "cluster_id": 10604543,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Charles Aaron Amble and John Joseph Mandracchia",
          "cluster_id": 10604323,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Missouri v. Theresa O'Connor",
          "cluster_id": 10631514,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Missouri v. Timothy R. Fernandez",
          "cluster_id": 10631444,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Jerry Lynn Burns",
          "cluster_id": 9388341,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Stark v. State",
          "cluster_id": 9371579,
          "cite": [
            "171 Idaho 541",
            "524 P.3d 43"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Terrance Baker",
          "cluster_id": 9371555,
          "cite": [
            "58 F.4th 1109"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Malagerio",
          "cluster_id": 8243624,
          "cite": [
            "49 F.4th 911"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jeremiah Edwards",
          "cluster_id": 6469003,
          "cite": [
            "34 F.4th 570"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Alan James Kuuttila",
          "cluster_id": 5290136,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Bortree",
          "cluster_id": 5030192,
          "cite": [
            "2021 Ohio 2873"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Nicholas Dean Wright",
          "cluster_id": 5290145,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Nicholas Dean Wright",
          "cluster_id": 4894883,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Nicholas Dean Wright",
          "cluster_id": 4893114,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gerardo Gonzalez v. Ice",
          "cluster_id": 4784538,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dixon",
          "cluster_id": 4805743,
          "cite": [
            "947 N.W.2d 563",
            "306 Neb. 853"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Franz Grey",
          "cluster_id": 4756521,
          "cite": [
            "959 F.3d 1166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Quentin Ferebee",
          "cluster_id": 4747521,
          "cite": [
            "957 F.3d 406"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jose Leonel Oseguera-Viera v. State",
          "cluster_id": 4685787,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dontae Small",
          "cluster_id": 4684957,
          "cite": [
            "944 F.3d 490"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Holley",
          "cluster_id": 4658152,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Thomas",
          "cluster_id": 4647637,
          "cite": [
            "2019 IL App (1st) 170474"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Martha Ann McClancy",
          "cluster_id": 4647175,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Scottize Danyelle Brown",
          "cluster_id": 4658982,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Joseph Watson v. Patrick Pearson",
          "cluster_id": 4635243,
          "cite": [
            "928 F.3d 507"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
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
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Valles",
          "cluster_id": 4609283,
          "cite": [
            "2019 ND 108",
            "925 N.W.2d 404"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Chavez v. Carmichael",
          "cluster_id": 4550937,
          "cite": [
            "822 S.E.2d 131",
            "262 N.C. App. 196"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
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
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "City of El Cenizo, Texas v. State of Texas",
          "cluster_id": 4476977,
          "cite": [
            "885 F.3d 332"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hull v. Town of Newtown",
          "cluster_id": 4453742,
          "cite": [
            "174 A.3d 174",
            "327 Conn. 402"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "City of El Cenizo v. Texas",
          "cluster_id": 7326561,
          "cite": [
            "264 F. Supp. 3d 744"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Bruce Wayne Sutton",
          "cluster_id": 4393282,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Joseph Durward Watson, II - Dissenting Opinion",
          "cluster_id": 4382006,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Byrd",
          "cluster_id": 4319283,
          "cite": [
            "2016 Ohio 7670"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hayward",
          "cluster_id": 4319281,
          "cite": [
            "2016 Ohio 7671"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jackson",
          "cluster_id": 4319280,
          "cite": [
            "2016 Ohio 7669"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Samalia",
          "cluster_id": 4242519,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jeffrey B. Melling",
          "cluster_id": 3191981,
          "cite": [
            "160 Idaho 209",
            "370 P.3d 412",
            "2016 WL 1355089",
            "2016 Ida. App. LEXIS 46"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Traci Sheppard Schroeder v. State",
          "cluster_id": 3072000,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Williford",
          "cluster_id": 2766778,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Borders",
          "cluster_id": 2726708,
          "cite": [
            "236 N.C. App. 149",
            "762 S.E.2d 490",
            "2014 N.C. App. LEXIS 975"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Olvera v. City of Modesto",
          "cluster_id": 7308114,
          "cite": [
            "38 F. Supp. 3d 1162",
            "2014 WL 3858362",
            "2014 U.S. Dist. LEXIS 108452"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Lee",
          "cluster_id": 2674606,
          "cite": [
            "2014 IL App (1st) 130507"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Maine v. Richard K. Ntim Jr.",
          "cluster_id": 2679977,
          "cite": [
            "2013 ME 80",
            "76 A.3d 370",
            "2013 WL 5201022",
            "2013 Me. LEXIS 81"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jerry Nelson, Jr.",
          "cluster_id": 2981963,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jerry Nelson, Jr.",
          "cluster_id": 1036714,
          "cite": [
            "725 F.3d 615",
            "92 Fed. R. Serv. 95",
            "2013 WL 4007652",
            "2013 U.S. App. LEXIS 16278"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Irizarry",
          "cluster_id": 858053,
          "cite": [
            "72 M.J. 100",
            "2013 WL 1628381",
            "2013 CAAF LEXIS 383"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "LAVAN v. City of Los Angeles",
          "cluster_id": 2113714,
          "cite": [
            "797 F. Supp. 2d 1005",
            "2011 U.S. Dist. LEXIS 67332",
            "2011 WL 2516484"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Wynn",
          "cluster_id": 2694594,
          "cite": [
            "2011 Ohio 1832"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Orval Roger Miller Jr. v. State",
          "cluster_id": 2954290,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Orval Roger Miller Jr. v. State",
          "cluster_id": 2954289,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Miller v. State",
          "cluster_id": 2280953,
          "cite": [
            "335 S.W.3d 847",
            "2011 Tex. App. LEXIS 1752",
            "2011 WL 832126"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Eaton",
          "cluster_id": 2393809,
          "cite": [
            "707 S.E.2d 642",
            "210 N.C. App. 142",
            "2011 N.C. App. LEXIS 319"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Marshall",
          "cluster_id": 2273474,
          "cite": [
            "319 S.W.3d 352",
            "2010 Ky. LEXIS 182",
            "2010 WL 3374171"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Eddie Carlisle",
          "cluster_id": 3004320,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Carlisle",
          "cluster_id": 2530423,
          "cite": [
            "614 F.3d 750",
            "2010 U.S. App. LEXIS 17026",
            "2010 WL 3155876"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Maurice Levie v. ESL Partners, L.P.",
          "cluster_id": 152710,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Nesbitt",
          "cluster_id": 2397780,
          "cite": [
            "699 S.E.2d 368",
            "305 Ga. App. 28",
            "2010 Fulton County D. Rep. 2538",
            "2010 Ga. App. LEXIS 656"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Williamson v. State",
          "cluster_id": 1917905,
          "cite": [
            "993 A.2d 626",
            "413 Md. 521",
            "2010 Md. LEXIS 175"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. VASQUEZ-ARENIVAR",
          "cluster_id": 1255552,
          "cite": [
            "779 N.W.2d 117",
            "18 Neb. Ct. App. 265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Howe",
          "cluster_id": 1887352,
          "cite": [
            "986 A.2d 631",
            "159 N.H. 366"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Club Retro LLC v. Hilton",
          "cluster_id": 66452,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
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
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 5143869,
          "cite": [
            "962 A.2d 973",
            "2009 ME 6",
            "2009 Me. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Assistance of Counsel in Removal Proceedings (I)",
          "cluster_id": 6236949,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Crist",
          "cluster_id": 1974111,
          "cite": [
            "627 F. Supp. 2d 575",
            "2008 U.S. Dist. LEXIS 84980",
            "2008 WL 4682806"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Smith v. State",
          "cluster_id": 1360884,
          "cite": [
            "667 S.E.2d 65",
            "284 Ga. 304",
            "2008 Fulton County D. Rep. 2964",
            "2008 Ga. LEXIS 753"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Parson",
          "cluster_id": 2584947,
          "cite": [
            "44 Cal. 4th 332",
            "187 P.3d 1",
            "79 Cal. Rptr. 3d 269",
            "2008 Cal. LEXIS 8243"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 2414367,
          "cite": [
            "556 F. Supp. 2d 985",
            "2008 WL 2251248"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Martin v. Mukasey",
          "cluster_id": 170353,
          "cite": [
            "517 F.3d 1201",
            "2008 U.S. App. LEXIS 4155",
            "2008 WL 501113"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Duplessis",
          "cluster_id": 1794695,
          "cite": [
            "974 So. 2d 65",
            "2007 WL 4554325"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bruce v. Beary",
          "cluster_id": 77819,
          "cite": [
            "498 F.3d 1232",
            "2007 U.S. App. LEXIS 21283",
            "2007 WL 2492101"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tylan Lucas",
          "cluster_id": 3042966,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Lucas",
          "cluster_id": 1362932,
          "cite": [
            "499 F.3d 769",
            "2007 U.S. App. LEXIS 20076",
            "2007 WL 2386580"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Shawn Patrick Bryan v. State",
          "cluster_id": 2914087,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. McKinney",
          "cluster_id": 1392222,
          "cite": [
            "637 S.E.2d 868",
            "361 N.C. 53",
            "2006 N.C. LEXIS 1298"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Sutherland",
          "cluster_id": 3135291,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Sutherland",
          "cluster_id": 2036519,
          "cite": [
            "860 N.E.2d 178",
            "223 Ill. 2d 187",
            "307 Ill. Dec. 524"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hudson v. State",
          "cluster_id": 2173357,
          "cite": [
            "205 S.W.3d 600",
            "2006 Tex. App. LEXIS 7699",
            "2006 WL 2507311"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Sedrick Roshun Decoud, Jr., A/K/A Rab Shaun Dee Merced and Shaun Vance, United States of America v. Kendra Trice, United States of America v. Audra Israel",
          "cluster_id": 795230,
          "cite": [
            "456 F.3d 996",
            "70 Fed. R. Serv. 893",
            "2006 U.S. App. LEXIS 19599"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Decoud",
          "cluster_id": 3038224,
          "cite": [
            "456 F.3d 996",
            "2006 WL 2136603"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Edward J. Zakrzewski v. James McDonough",
          "cluster_id": 77399,
          "cite": [
            "455 F.3d 1254",
            "2006 U.S. App. LEXIS 17484",
            "2006 WL 1911328"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Marzook",
          "cluster_id": 2434582,
          "cite": [
            "435 F. Supp. 2d 778",
            "2006 U.S. Dist. LEXIS 41898",
            "2006 WL 1735322"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sherman",
          "cluster_id": 1129307,
          "cite": [
            "931 So. 2d 286",
            "2006 WL 860652"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Clifton M. Menton v. State",
          "cluster_id": 2891732,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Clifton M. Menton v. State",
          "cluster_id": 2891731,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Clifton M. Menton v. State",
          "cluster_id": 2891730,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Adron Thomas v. State",
          "cluster_id": 2916555,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Washington v. State",
          "cluster_id": 1694079,
          "cite": [
            "922 So. 2d 145",
            "2005 WL 435119"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Stevenson",
          "cluster_id": 2968064,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Lee Ronald Stevenson",
          "cluster_id": 789072,
          "cite": [
            "396 F.3d 538",
            "2005 U.S. App. LEXIS 1558",
            "2005 WL 221869"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Nieves",
          "cluster_id": 2402008,
          "cite": [
            "861 A.2d 62",
            "383 Md. 573",
            "2004 Md. LEXIS 722"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fulani",
          "cluster_id": 3014175,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ibrahim Hamud Fulani",
          "cluster_id": 786196,
          "cite": [
            "368 F.3d 351",
            "2004 U.S. App. LEXIS 9896",
            "2004 WL 1119635"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Murph Omar McNaughton v. State",
          "cluster_id": 2882131,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "UNITED STATES v. WILLIAM SOTO-BEN\u00cdQUEZ, UNITED STATES OF AMERICA v. JUAN SOTO-RAM\u00cdREZ, UNITED STATES OF AMERICA v. EDUARDO ALICEA-TORRES, UNITED STATES OF AMERICA v. RAMON FERN\u00c1NDEZ-MALAV\u00c9, UNITED STATES OF AMERICA v. CARMELO VEGA-PACHECO, UNITED STATES OF AMERICA v. ARMANDO GARC\u00cdA-GARC\u00cdA, UNITED STATES OF AMERICA v. JOSE LUIS DE LE\u00d3N MAYSONET, UNITED STATES OF AMERICA v. RENE GONZALEZ-AYALA, UNITED STATES OF AMERICA v. JUAN ENRIQUE CINTR\u00d3N-CARABALLO, UNITED STATES OF AMERICA v. MIGUEL VEGA-COL\u00d3N, UNITED STATES OF AMERICA v. MIGUEL VEGA-COSME",
          "cluster_id": 784866,
          "cite": [
            "356 F.3d 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Samuel Mondragon-Garcia v. State",
          "cluster_id": 2913182,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mondragon-Garcia v. State",
          "cluster_id": 1466707,
          "cite": [
            "129 S.W.3d 674",
            "2004 Tex. App. LEXIS 444",
            "2004 WL 67625"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dominguez, Carlos Martinez v. State",
          "cluster_id": 2835714,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dominguez v. State",
          "cluster_id": 1384895,
          "cite": [
            "125 S.W.3d 755",
            "2003 Tex. App. LEXIS 10758",
            "2003 WL 22999897"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "UNITED STATES v. WILLIAM SOTO-BENIQUEZ, UNITED STATES OF AMERICA v. JUAN SOTO-RAMIREZ, UNITED STATES OF AMERICA v. EDUARDO ALICEA-TORRES, UNITED STATES OF AMERICA v. RAMON FERNANDEZ-MALAV\u00c9, UNITED STATES OF AMERICA v. CARMELO VEGA-PACHECO, UNITED STATES OF AMERICA v. ARMANDO GARCIA-GARCIA, UNITED STATES OF AMERICA v. JOSE LUIS DE LEON MAYSONET, UNITED STATES OF AMERICA v. RENE GONZALEZ-AYALA, UNITED STATES OF AMERICA v. JUAN ENRIQUE CINTRON-CARABALLO, UNITED STATES OF AMERICA v. MIGUEL VEGA-COLON, UNITED STATES OF AMERICA v. MIGUEL VEGA-COSME",
          "cluster_id": 784248,
          "cite": [
            "350 F.3d 131",
            "2003 U.S. App. LEXIS 23655"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Soto-Beniquez",
          "cluster_id": 200734,
          "cite": [
            "356 F.3d 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jackson",
          "cluster_id": 2572005,
          "cite": [
            "360 F. Supp. 2d 24",
            "2003 U.S. Dist. LEXIS 27347",
            "2003 WL 24008994"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cedric E. Wingfield v. State",
          "cluster_id": 2844500,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cedric E. Wingfield v. State",
          "cluster_id": 2844499,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cedric E. Wingfield v. State",
          "cluster_id": 2844774,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cedric E. Wingfield v. State",
          "cluster_id": 2844773,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ahern",
          "cluster_id": 200539,
          "cite": [
            "68 F. App'x 209"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Martin v. State",
          "cluster_id": 1129477,
          "cite": [
            "931 So. 2d 736",
            "2003 WL 21246587"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Reed Mouton v. State",
          "cluster_id": 2881730,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mouton v. State",
          "cluster_id": 1634836,
          "cite": [
            "101 S.W.3d 686",
            "2003 Tex. App. LEXIS 2022",
            "2003 WL 845498"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Netto",
          "cluster_id": 6578659,
          "cite": [
            "438 Mass. 686",
            "783 N.E.2d 439",
            "2003 Mass. LEXIS 171"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Mosby",
          "cluster_id": 1773883,
          "cite": [
            "94 S.W.3d 410",
            "2003 Mo. App. LEXIS 37",
            "2003 WL 138232"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Willie Roy Woods v. State",
          "cluster_id": 2877945,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ballew v. Walker",
          "cluster_id": 7295232,
          "cite": [
            "50 F. App'x 24"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Mallory",
          "cluster_id": 6587233,
          "cite": [
            "56 Mass. App. Ct. 153",
            "775 N.E.2d 764",
            "2002 Mass. App. LEXIS 1218"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Maria Alicia Walker v. State",
          "cluster_id": 2920179,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Matthew Downing v. State of Texas",
          "cluster_id": 2915536,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Donald Lee Morrison v. State",
          "cluster_id": 2920639,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Morrison v. State",
          "cluster_id": 1662228,
          "cite": [
            "71 S.W.3d 821",
            "2002 Tex. App. LEXIS 1427",
            "2002 WL 254027"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
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
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Preston v. State",
          "cluster_id": 2318723,
          "cite": [
            "784 A.2d 601",
            "141 Md. App. 54",
            "2001 Md. App. LEXIS 165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Rosenthal",
          "cluster_id": 6586859,
          "cite": [
            "52 Mass. App. Ct. 707",
            "755 N.E.2d 817",
            "2001 Mass. App. LEXIS 930"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Powell v. State",
          "cluster_id": 1946311,
          "cite": [
            "776 A.2d 700",
            "139 Md. App. 582",
            "2001 Md. App. LEXIS 126"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brixen & Christopher Architects, P.C. v. State",
          "cluster_id": 2599638,
          "cite": [
            "2001 UT App 210",
            "29 P.3d 650",
            "424 Utah Adv. Rep. 45",
            "2001 Utah App. LEXIS 49",
            "2001 WL 721723"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. McDermott",
          "cluster_id": 7089721,
          "cite": [
            "245 F.3d 133",
            "2001 WL 303634"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mitchell v. State",
          "cluster_id": 1852299,
          "cite": [
            "792 So. 2d 192",
            "2001 WL 302751"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. James J. McDermott Jr., Kathryn B. Gannon, Also Known as Kathryn B. Gannon-Akahoshi, Also Known as Marylin Star, and Anthony P. Pomponio",
          "cluster_id": 772671,
          "cite": [
            "245 F.3d 133",
            "56 Fed. R. Serv. 1086",
            "2001 U.S. App. LEXIS 5277"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Bin Laden",
          "cluster_id": 2457303,
          "cite": [
            "132 F. Supp. 2d 198",
            "2001 U.S. Dist. LEXIS 26300",
            "2001 WL 135858"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Citizen v. State",
          "cluster_id": 1947523,
          "cite": [
            "39 S.W.3d 367",
            "2001 Tex. App. LEXIS 1021",
            "2001 WL 126125"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Utecht, Kenneth L.",
          "cluster_id": 2994836,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth L. Utecht",
          "cluster_id": 771880,
          "cite": [
            "238 F.3d 882",
            "87 A.F.T.R.2d (RIA) 681",
            "2001 U.S. App. LEXIS 1060",
            "2001 WL 65066"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Lisenbee",
          "cluster_id": 2585425,
          "cite": [
            "13 P.3d 947",
            "116 Nev. 1124",
            "116 Nev. Adv. Rep. 117",
            "2000 Nev. LEXIS 132"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Ayala",
          "cluster_id": 2594572,
          "cite": [
            "6 P.3d 193",
            "99 Cal. Rptr. 2d 532",
            "24 Cal. 4th 243",
            "2000 WL 1210378"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Ayala",
          "cluster_id": 5593049,
          "cite": [
            "24 Cal. 243"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Pallone",
          "cluster_id": 2221553,
          "cite": [
            "2000 WI 77",
            "613 N.W.2d 568",
            "236 Wis. 2d 162",
            "2000 Wisc. LEXIS 415"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Ayala",
          "cluster_id": 2551468,
          "cite": [
            "1 P.3d 3",
            "96 Cal. Rptr. 2d 682",
            "23 Cal. 4th 225",
            "2000 Cal. Daily Op. Serv. 4490",
            "2000 Daily Journal DAR 6037",
            "2000 Cal. LEXIS 4545"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grant",
          "cluster_id": 2211483,
          "cite": [
            "614 N.W.2d 848",
            "2000 Iowa App. LEXIS 6",
            "2000 WL 504538"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "James Hollingsworth v. State",
          "cluster_id": 2863127,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hollingsworth v. State",
          "cluster_id": 2119689,
          "cite": [
            "15 S.W.3d 586",
            "2000 Tex. App. LEXIS 2033",
            "2000 WL 328041"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Beardslee",
          "cluster_id": 7079506,
          "cite": [
            "197 F.3d 378",
            "1999 WL 983680"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Florence Martha Beardslee, United States of America, Plaintiff-Appellant-Cross-Appellee v. Florence Martha Beardslee, Defendant-Appellee-Cross-Appellant",
          "cluster_id": 766868,
          "cite": [
            "197 F.3d 378",
            "99 Daily Journal DAR 11201",
            "99 Cal. Daily Op. Serv. 8756",
            "53 Fed. R. Serv. 494",
            "1999 U.S. App. LEXIS 28102"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Powell v. State",
          "cluster_id": 1660846,
          "cite": [
            "796 So. 2d 404",
            "1999 WL 982399"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Brauch",
          "cluster_id": 2614645,
          "cite": [
            "984 P.2d 703",
            "133 Idaho 215",
            "1999 Ida. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "James Edmond and Joell Palmer, on Their Own Behalf and on Behalf of a Class of Those Similarly Situated v. Stephen Goldsmith, in His Official Capacity as Mayor of the City of Indianapolis, Indiana City of Indianapolis, Indiana and Unknown Members of the Indianapolis Police Department",
          "cluster_id": 765145,
          "cite": [
            "183 F.3d 659",
            "1999 U.S. App. LEXIS 15010"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In Re Subpoenas Duces Tecum Nos. A99-0001, A99-0002, A99-0003 & A99-0004",
          "cluster_id": 2497025,
          "cite": [
            "51 F. Supp. 2d 726",
            "1999 U.S. Dist. LEXIS 10471",
            "1999 WL 451796"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Padilla",
          "cluster_id": 1441534,
          "cite": [
            "728 A.2d 279",
            "321 N.J. Super. 96"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Wilmington",
          "cluster_id": 1954189,
          "cite": [
            "729 A.2d 1160",
            "1999 Pa. Super. 66",
            "1999 Pa. Super. LEXIS 824"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gudema v. Nassau County",
          "cluster_id": 7075002,
          "cite": [
            "163 F.3d 717",
            "1998 WL 887048"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gudema v. Nassau County",
          "cluster_id": 760182,
          "cite": [
            "163 F.3d 717",
            "1998 U.S. App. LEXIS 31650"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Miller",
          "cluster_id": 2406906,
          "cite": [
            "26 F. Supp. 2d 415",
            "1998 U.S. Dist. LEXIS 15970",
            "1998 WL 709469"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gore",
          "cluster_id": 7069910,
          "cite": [
            "154 F.3d 34",
            "1998 WL 515720"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gore",
          "cluster_id": 757557,
          "cite": [
            "154 F.3d 34",
            "1998 U.S. App. LEXIS 20493"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "William Gerald Mitchell v. State of Mississippi",
          "cluster_id": 863672,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Holland v. State",
          "cluster_id": 1902684,
          "cite": [
            "713 A.2d 364",
            "122 Md. App. 532",
            "1998 Md. App. LEXIS 140"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Perkins",
          "cluster_id": 2023862,
          "cite": [
            "582 N.W.2d 876",
            "1998 Minn. LEXIS 388",
            "1998 WL 351051"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Reeves v. State",
          "cluster_id": 1534910,
          "cite": [
            "969 S.W.2d 471",
            "1998 Tex. App. LEXIS 2649",
            "1998 WL 220453"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Partee v. State",
          "cluster_id": 1997221,
          "cite": [
            "708 A.2d 1113",
            "121 Md. App. 237",
            "1998 Md. App. LEXIS 102"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Benjamin Armstrong v. State",
          "cluster_id": 2861573,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Armstrong v. State",
          "cluster_id": 2377535,
          "cite": [
            "966 S.W.2d 150",
            "1998 Tex. App. LEXIS 1841",
            "1998 WL 132941"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Holbrooks",
          "cluster_id": 1082984,
          "cite": [
            "983 S.W.2d 697",
            "1998 Tenn. Crim. App. LEXIS 175",
            "1998 WL 57527"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Bennett",
          "cluster_id": 1194986,
          "cite": [
            "17 Cal. 4th 373",
            "949 P.2d 947",
            "98 Daily Journal DAR 1155",
            "98 Cal. Daily Op. Serv. 863",
            "70 Cal. Rptr. 2d 850",
            "1998 Cal. LEXIS 28"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Larry Andre Sanders",
          "cluster_id": 748848,
          "cite": [
            "130 F.3d 1316",
            "1997 WL 762704"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Larry A. Sanders",
          "cluster_id": 3019806,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Neal v. State",
          "cluster_id": 1846732,
          "cite": [
            "731 So. 2d 609",
            "1997 WL 501462"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Maude C. Clarke",
          "cluster_id": 3018375,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Maude C. Clarke, Also Known as Tina Clarke, Also Known as Angela",
          "cluster_id": 739120,
          "cite": [
            "110 F.3d 612",
            "1997 U.S. App. LEXIS 6488",
            "1997 WL 160155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Calvin Porter",
          "cluster_id": 3018006,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Calvin Porter",
          "cluster_id": 736260,
          "cite": [
            "107 F.3d 582",
            "1997 U.S. App. LEXIS 3043",
            "1997 WL 71289"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "46 Fed. R. Evid. Serv. 240, 10 Fla. L. Weekly Fed. C 621 United States of America v. Ralph E. Brazel, Jr., Charles Hubbard, Norman L. Burgess, United States of America v. Sharvonne McKinnon United States of America v. Levine Justice Archer, A.K.A. Jamaican Joe, A.K.A. Joe, Willie Jefferson, Marlon McNealy A.K.A. Man",
          "cluster_id": 731292,
          "cite": [
            "102 F.3d 1120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Baldwin",
          "cluster_id": 1671891,
          "cite": [
            "686 So. 2d 682",
            "1996 WL 728697"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Lashawn Y. McDonald",
          "cluster_id": 729772,
          "cite": [
            "100 F.3d 1320",
            "1996 U.S. App. LEXIS 30224",
            "1996 WL 673246"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Stanberry v. State",
          "cluster_id": 2314219,
          "cite": [
            "684 A.2d 823",
            "343 Md. 720",
            "1996 Md. LEXIS 116"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Ienco",
          "cluster_id": 723976,
          "cite": [
            "92 F.3d 564",
            "45 Fed. R. Serv. 415",
            "1996 U.S. App. LEXIS 20183",
            "1996 WL 452248"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Richards",
          "cluster_id": 1840075,
          "cite": [
            "552 N.W.2d 197",
            "1996 Minn. LEXIS 444",
            "1996 WL 400300"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Roberts",
          "cluster_id": 1446652,
          "cite": [
            "928 F. Supp. 910",
            "1996 U.S. Dist. LEXIS 8590",
            "1996 WL 335492"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Clarke",
          "cluster_id": 2294285,
          "cite": [
            "925 F. Supp. 1433",
            "1996 U.S. Dist. LEXIS 6989",
            "1996 WL 268070"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
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
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Soca v. State",
          "cluster_id": 1657165,
          "cite": [
            "673 So. 2d 24",
            "1996 WL 196588"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Timothy Dwayne Austin",
          "cluster_id": 705154,
          "cite": [
            "66 F.3d 1115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Crittenden v. State",
          "cluster_id": 1506576,
          "cite": [
            "899 S.W.2d 668",
            "1995 Tex. Crim. App. LEXIS 57",
            "1995 WL 296354"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Walker",
          "cluster_id": 2264802,
          "cite": [
            "879 F. Supp. 1087",
            "1995 U.S. Dist. LEXIS 3297",
            "1995 WL 106386"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Perkins",
          "cluster_id": 1684979,
          "cite": [
            "871 F. Supp. 801",
            "1995 U.S. Dist. LEXIS 91",
            "1995 WL 7515"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lake County Mental Health Department v. Susan T.",
          "cluster_id": 2611902,
          "cite": [
            "884 P.2d 988",
            "8 Cal. 4th 1005",
            "36 Cal. Rptr. 2d 40",
            "94 Cal. Daily Op. Serv. 9381",
            "94 Daily Journal DAR 17330",
            "63 U.S.L.W. 2392",
            "1994 Cal. LEXIS 6211"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rockett v. State",
          "cluster_id": 2394789,
          "cite": [
            "890 S.W.2d 235",
            "318 Ark. 831",
            "1994 Ark. LEXIS 699"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Florez",
          "cluster_id": 1685213,
          "cite": [
            "871 F. Supp. 1411",
            "1994 U.S. Dist. LEXIS 19976",
            "1994 WL 728462"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jamal Deshon Segars",
          "cluster_id": 675779,
          "cite": [
            "31 F.3d 655",
            "1994 U.S. App. LEXIS 19724",
            "1994 WL 395230"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane1_negative"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. O'Brien",
          "cluster_id": 107701,
          "cite": [
            "20 L. Ed. 2d 672",
            "88 S. Ct. 1673",
            "391 U.S. 367",
            "1968 U.S. LEXIS 2910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Camara v. Municipal Court of City and County of San Francisco",
          "cluster_id": 107473,
          "cite": [
            "18 L. Ed. 2d 930",
            "87 S. Ct. 1727",
            "387 U.S. 523",
            "1967 U.S. LEXIS 1254"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Tyler",
          "cluster_id": 109874,
          "cite": [
            "56 L. Ed. 2d 486",
            "98 S. Ct. 1942",
            "436 U.S. 499",
            "1978 U.S. LEXIS 97"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Santana",
          "cluster_id": 109504,
          "cite": [
            "49 L. Ed. 2d 300",
            "96 S. Ct. 2406",
            "427 U.S. 38",
            "1976 U.S. LEXIS 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Poe v. Ullman",
          "cluster_id": 106282,
          "cite": [
            "6 L. Ed. 2d 989",
            "81 S. Ct. 1752",
            "367 U.S. 497",
            "1961 U.S. LEXIS 1953"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. Lopez-Mendoza",
          "cluster_id": 111265,
          "cite": [
            "82 L. Ed. 2d 778",
            "104 S. Ct. 3479",
            "468 U.S. 1032",
            "1984 U.S. LEXIS 156",
            "52 U.S.L.W. 5190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lopez v. United States",
          "cluster_id": 106622,
          "cite": [
            "10 L. Ed. 2d 462",
            "83 S. Ct. 1381",
            "373 U.S. 427",
            "1963 U.S. LEXIS 2618"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
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
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gustafson v. Florida",
          "cluster_id": 108894,
          "cite": [
            "38 L. Ed. 2d 456",
            "94 S. Ct. 488",
            "414 U.S. 260",
            "1973 U.S. LEXIS 22",
            "66 Ohio Op. 2d 275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. LaSalle National Bank",
          "cluster_id": 109901,
          "cite": [
            "57 L. Ed. 2d 221",
            "98 S. Ct. 2357",
            "437 U.S. 298",
            "1978 U.S. LEXIS 112",
            "42 A.F.T.R.2d (RIA) 5198"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Abel v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106021 OR 9421949 OR 9421950 OR 9421951) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03NzU3ODU2MDAwMDAmcz02NzU3NzkmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106021+OR+9421949+OR+9421950+OR+9421951%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "audit_marker": "R15 treatment audit required",
        "proposed_negative_events": 193
      },
      "lane2_top_cited": {
        "query": "cites:(106021 OR 9421949 OR 9421950 OR 9421951)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMjQmcz0zNjkwNzcmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28106021+OR+9421949+OR+9421950+OR+9421951%29&type=o",
        "audit_needed": true,
        "audit_marker": "R15 treatment audit required",
        "proposed_negative_events": 25
      },
      "lane3_recency": {
        "query": "cites:(106021 OR 9421949 OR 9421950 OR 9421951)",
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
    "complete_query": "cites:(106021 OR 9421949 OR 9421950 OR 9421951)",
    "indexed_citing_opinions": 995,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106021,
        "count": 916,
        "count_source": "search"
      },
      {
        "opinion_id": 9421949,
        "count": 104,
        "count_source": "search"
      },
      {
        "opinion_id": 9421950,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9421951,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1485,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/abel-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY3NDE4MDkmcz00NzQ3NTIxJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106021+OR+9421949+OR+9421950+OR+9421951%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106021,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 94479,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 95830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 97714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 100280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 104589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 104978,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 104980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 105227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 105341,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 105343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 105407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 245929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 1484849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106021,
        "cited_id": 1880326,
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
    "date_created": "2026-07-04T15:08:05Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T15:08:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T15:08:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T15:30:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T15:08:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Abel v. United States

```
<div>
<center><b><span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U.S. 217</a></span> (1960)</b></center>
<center><h1>ABEL, ALIAS MARK, ALIAS COLLINS, ALIAS GOLDFUS,<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 2.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 24-25, 1959.</center>
<center>Restored to the calendar for reargument March 23, 1959.</center>
<center>Reargued November 9, 1959.</center>
<center>Decided March 28, 1960.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SECOND CIRCUIT.
<p><span class="star-pagination">*218</span> <i>James B. Donovan</i> argued and reargued the cause for petitioner. With him on the briefs was <i>Thomas M. Debevoise II.</i></p>
<p><i>Solicitor General Rankin</i> argued and reargued the cause for the United States. With him on the original brief were <i>Acting Assistant Attorney General Yeagley, William F. Tompkins</i> and <i>Kevin T. Maroney.</i> With him on the supplemental brief on reargument were <i>Assistant Attorney General Yeagley, John F. Davis, William F. Tompkins</i> and <i>Kevin T. Maroney.</i></p>
<p>MR. JUSTICE FRANKFURTER delivered the opinion of the Court.</p>
<p>The question in this case is whether seven items were properly admitted into evidence at the petitioner's trial for conspiracy to commit espionage. All seven items were seized by officers of the Government without a search warrant. The seizures did not occur in connection with the exertion of the criminal process against petitioner. They arose out of his administrative arrest by the United States Immigration and Naturalization Service as a preliminary to his deportation. A motion to suppress these items as evidence, duly made in the District Court, was denied after a full hearing. <span class="citation" data-id="8725152"><a href="/opinion/8741899/united-states-v-abel/" aria-description="Citation for case: United States v. Abel">155 F. Supp. 8</a></span>. Petitioner was tried, convicted and sentenced to thirty years' imprisonment and to the payment of a fine of $3,000. The Court of Appeals affirmed, <span class="citation" data-id="245929"><a href="/opinion/245929/united-states-v-rudolph-ivanovich-abel-also-known-as-mark-and-also/" aria-description="Citation for case: United States v. Rudolph Ivanovich Abel, Also Known as...">258 F. 2d 485</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./358/813/">358 U. S. 813</a></span>, limiting the grant to the following two questions:</p>
<blockquote>"1. Whether the Fourth and Fifth Amendments to the Constitution of the United States are violated by <span class="star-pagination">*219</span> a search and the seizure of evidence without a search warrant, after an alien suspected and officially accused of espionage has been taken into custody for deportation, pursuant to an administrative Immigration Service warrant, but has not been arrested for the commission of a crime?</blockquote>
<blockquote>"2. Whether the Fourth and Fifth Amendments to the Constitution of the United States are violated when articles so seized are unrelated to the Immigration Service warrant and, together with other articles obtained from such leads, are introduced as evidence in a prosecution for espionage?"</blockquote>
<p>Argument was first heard at October Term, 1958. The case having been set down for reargument at this Term, <span class="citation multiple-matches"><a href="/c/U.%20S./359/940/">359 U. S. 940</a></span>, counsel were asked to discuss a series of additional questions, set out in the margin.<sup>[*]</sup></p>
<p>We have considered the case on the assumption that the conviction must be reversed should we find challenged items of evidence to have been seized in violation of the Constitution and therefore improperly admitted into evidence. We find, however, that the admission of these items was free from any infirmity and we affirm the judgment. (Of course the nature of the case, the fact that it was a prosecution for espionage, has no bearing <span class="star-pagination">*220</span> whatever upon the legal considerations relevant to the admissibility of evidence.)</p>
<p>The seven items, all in petitioner's possession at the time of his administrative arrest, the admissibility of which is in question, were the following:</p>
<blockquote>(1) a piece of graph paper, carrying groups of numbers arranged in rows, allegedly a coded message:</blockquote>
<blockquote>(2) a forged birth certificate, certifying the birth of "Martin Collins" in New York County in 1897:</blockquote>
<blockquote>(3) a birth certificate, certifying the birth of "Emil Goldfus" in New York in 1902 (Emil Goldfus died in 1903);</blockquote>
<blockquote>(4) an international certificate of vaccination, issued in New York to "Martin Collins" in 1957;</blockquote>
<blockquote>(5) a bank book of the East River Savings Bank containing the account of "Emil Goldfus";</blockquote>
<blockquote>(6) a hollowed-out pencil containing 18 microfilms; and</blockquote>
<blockquote>(7) a block of wood, wrapped in sandpaper, and containing within it a small booklet with a series of numbers on each page, a so-called "cipher pad."</blockquote>
<p>Items (2), (3), (4) and (5) were relevant to the issues of the indictment for which petitioner was on trial in that they corroborated petitioner's use of false identities. Items (1), (6) and (7) were incriminatory as useful means for one engaged in espionage.</p>
<p>The main claims which petitioner pressed upon the Court may be thus summarized: (1) the administrative arrest was used by the Government in bad faith; (2) administrative arrests as preliminaries to deportation are unconstitutional; and (3) regardless of the validity of the administrative arrest here, the searches and seizures through which the challenged items came into the Government's possession were not lawful ancillaries to such an arrest. These claims cannot be judged apart from the circumstances leading up to the arrest and the nature of <span class="star-pagination">*221</span> the searches and seizures. It becomes necessary to relate these matters in considerable detail.</p>
<p>Petitioner was arrested by officers of the Immigration and Naturalization Service (hereafter abbreviated as I. N. S.) on June 21, 1957, in a single room in the Hotel Latham in New York City, his then abode. The attention of the I. N. S. had first been drawn to petitioner several days earlier when Noto, a Deputy Assistant Commissioner of the I. N. S., was told by a liaison officer of the Federal Bureau of Investigation (hereafter abbreviated as F. B. I.) that petitioner was believed by the F. B. I. to be an alien residing illegally in the United States. Noto was told of the F. B. I.'s interest in petitioner in connection with espionage.</p>
<p>An uncontested affidavit before the District Court asserted the following with regard to the events leading up to the F. B. I.'s communication with Noto about petitioner. About one month before the F. B. I. communicated with Noto, petitioner had been mentioned by Hayhanen, a recently defected Russian spy, as one with whom Hayhanen had for several years cooperated in attempting to commit espionage. The F. B. I. had thereupon placed petitioner under investigation. At the time the F. B. I. communicated with the I. N. S. regarding petitioner, the case against him rested chiefly upon Hayhanen's story, and Hayhanen, although he was later to be the Government's principal witness at the trial, at that time insisted that he would refuse to testify should petitioner be brought to trial, although he would fully cooperate with the Government in secret. The Department of Justice concluded that without Hayhanen's testimony the evidence was insufficient to justify petitioner's arrest and indictment on espionage charges. The decision was thereupon made to bring petitioner to the attention of the I. N. S., with a view to commencing deportation proceedings against him.</p>
<p><span class="star-pagination">*222</span> Upon being notified of the F. B. I.'s belief that petitioner was residing illegally in this country, Noto asked the F. B. I. to supply the I. N. S. with further information regarding petitioner's status as an alien. The F. B. I. did this within a week. The I. N. S. concluded that if petitioner were, as suspected, an alien, he would be subject to deportation in that he had failed to comply with the legal duty of aliens to notify the Attorney General every January of their address in the United States. <span class="citation no-link">8 U. S. C. § 1305</span>. Noto then determined on petitioner's administrative arrest as a preliminary to his deportation. The F. B. I. was so informed. On June 20, two I. N. S. officers, Schoenenberger and Kanzler, were dispatched by Noto to New York to supervise the arrest. These officers carried with them a warrant for petitioner's arrest and an order addressed to petitioner directing him to show cause why he should not be deported. They met in New York with the District Director of the I. N. S. who, after the information in the possession of the I. N. S. regarding petitioner was put before him, signed the warrant and the order. Following this, Schoenenberger and Kanzler went to F. B. I. headquarters in New York where, by prearrangement with the F. B. I. in Washington, they were met by several F. B. I. officers. These agreed to conduct agents of the I. N. S. to petitioner's hotel so that the I. N. S. might accomplish his arrest. The F. B. I. officer in charge asked whether, before the petitioner was arrested, the F. B. I. might "interview" him in an attempt to persuade him to "cooperate" with regard to his espionage. To this Schoenenberger agreed.</p>
<p>At 7 o'clock the next morning, June 21, two officers of the I. N. S. and several F. B. I. men gathered in the corridor outside petitioner's room at the Hotel Latham. All but two F. B. I. agents, Gamber and Blasco, went into the room next to petitioner's, which the F. B. I. had occupied in the course of its investigation of petitioner. <span class="star-pagination">*223</span> Gamber and Blasco were charged with confronting petitioner and soliciting his cooperation with the F. B. I. They had no warrant either to arrest or to search. If petitioner proved cooperative their instructions were to telephone to their superior for further instructions. If petitioner failed to cooperate they were to summon the waiting I. N. S. agents to execute their warrant for his arrest.</p>
<p>Gamber rapped on petitioner's door. When petitioner released the catch, Gamber pushed open the door and walked into the room, followed by Blasco. The door was left ajar and a third F. B. I. agent came into the room a few minutes later. Petitioner, who was nude, was told to put on a pair of undershorts and to sit on the bed, which he did. The F. B. I. agents remained in the room questioning petitioner for about twenty minutes. Although petitioner answered some of their questions, he did not "cooperate" regarding his alleged espionage. A signal was thereupon given to the two agents of the I. N. S. waiting in the next room. These came into petitioner's room and served petitioner with the warrant for his arrest and with the order to show cause. Shortly thereafter Schoenenberger and Kanzler, who had been waiting outside the hotel, also entered petitioner's room. These four agents of the I. N. S. remained with petitioner in his room for about an hour. For part of this time an F. B. I. agent was also in the room and during all of it another F. B. I. agent stood outside the open door of the room, where he could observe the interior.</p>
<p>After placing petitioner under arrest, the four I. N. S. agents undertook a search of his person and of all of his belongings in the room, and the adjoining bathroom, which lasted for from fifteen to twenty minutes. Petitioner did not give consent to this search; his consent was not sought. The F. B. I. agents observed this search but took no part in it. It was Schoenenberger's testimony to <span class="star-pagination">*224</span> the District Court that the purpose of this search was to discover weapons and documentary evidence of petitioner's "alienage"that is, documents to substantiate the information regarding petitioner's status as an alien which the I. N. S. had received from the F. B. I. During this search one of the challenged items of evidence, the one we have designated (2), a birth certificate for "Martin Collins," was seized. Weapons were not found, nor was any other evidence regarding petitioner's "alienage."</p>
<p>When the search was completed, petitioner was told to dress himself, to assemble his things and to choose what he wished to take with him. With the help of the I. N. S. agents almost everything in the room was packed into petitioner's baggage. A few things petitioner deliberately left on a window sill, indicating that he did not want to take them, and several other things which he chose not to pack up into his luggage he put into the room's wastepaper basket. When everything had been assembled, petitioner asked and received permission to repack one of his suitcases. While petitioner was doing so, Schoenenberger noticed him slipping some papers into the sleeve of his coat. Schoenenberger seized these. One of them was the challenged item of evidence which we have designated (1), a piece of graph paper containing a coded message.</p>
<p>When petitioner's belongings had been completely packed, petitioner agreed to check out of the hotel. One of the F. B. I. agents obtained his bill from the hotel and petitioner paid it. Petitioner was then handcuffed and taken, along with his baggage, to a waiting automobile and thence to the headquarters of the I. N. S. in New York. At I. N. S. headquarters, the property petitioner had taken with him was searched more thoroughly than it had been in his hotel room, and three more of the challenged items were discovered and seized. These were the ones we have designated (3), (4) and (5), the "Emil <span class="star-pagination">*225</span> Goldfus" birth certificate, the international vaccination certificate, and the bank book.</p>
<p>As soon as petitioner had been taken from the hotel, an F. B. I. agent, Kehoe, who had been in the room adjoining petitioner's during the arrest and search and who, like the I. N. S. agents, had no search warrant, received permission from the hotel management to search the room just vacated by petitioner. Although the bill which petitioner had paid entitled him to occupy the room until 3 p. m. of that day, the hotel's practice was to consider a room vacated whenever a guest removed his baggage and turned in his key. Kehoe conducted a search of petitioner's room which lasted for about three hours. Among other things, he seized the contents of the wastepaper basket into which petitioner had put some things while packing his belongings. Two of the items thus seized were the challenged items of evidence we have designated (6) and (7): a hollow pencil containing microfilm and a block of wood containing a "cipher pad."</p>
<p>Later in the day of his arrest, petitioner was taken by airplane to a detention center for aliens in Texas. He remained there for several weeks until arrested upon the charge of conspiracy to commit espionage for which he was brought to trial and convicted in the Eastern District of New York.</p>
<p></p>
<h2>I.</h2>
<p>The underlying basis of petitioner's attack upon the admissibility of the challenged items of evidence concerns the motive of the Government in its use of the administrative arrest. We are asked to find that the Government resorted to a subterfuge, that the Immigration and Naturalization Service warrant here was a pretense and sham, was not what it purported to be. According to petitioner, it was not the Government's true purpose in arresting him under this warrant to take him into custody pending <span class="star-pagination">*226</span> a determination of his deportability. The Government's real aims, the argument runs, were (1) to place petitioner in custody so that pressure might be brought to bear upon him to confess his espionage and cooperate with the F. B. I., and (2) to permit the Government to search through his belongings for evidence of his espionage to be used in a designed criminal prosecution against him. The claim is, in short, that the Government used this administrative warrant for entirely illegitimate purposes and that articles seized as a consequence of its use ought to have been suppressed.</p>
<p>Were this claim justified by the record, it would indeed reveal a serious misconduct by law-enforcing officers. The deliberate use by the Government of an administrative warrant for the purpose of gathering evidence in a criminal case must meet stern resistance by the courts. The preliminary stages of a criminal prosecution must be pursued in strict obedience to the safeguards and restrictions of the Constitution and laws of the United States. A finding of bad faith is, however, not open to us on this record. What the motive was of the I. N. S. officials who determined to arrest petitioner, and whether the I. N. S. in doing so was not exercising its powers in the lawful discharge of its own responsibilities but was serving as a tool for the F. B. I. in building a criminal prosecution against petitioner, were issues fully canvassed in both courts below. The crucial facts were found against the petitioner.</p>
<p>On this phase of the case the district judge, having permitted full scope to the elucidation of petitioner's claim, having seen and heard witnesses, in addition to testimony by way of affidavits, and after extensive argument, made these findings:</p>
<blockquote>"[T]he evidence is persuasive that the action taken by the officials of the Immigration and Naturalization Service is found to have been in entire good faith. <span class="star-pagination">*227</span> The testimony of Schoenenberger and Noto leaves no doubt that while the first information that came to them concerning the [petitioner] . . . was furnished by the F. B. I.which cannot be an unusual happening the proceedings taken by the Department differed in no respect from what would have been done in the case of an individual concerning whom no such information was known to exist.</blockquote>
<blockquote>"The defendant argues that the testimony establishes that the arrest was made under the direction and supervision of the F. B. I., but the evidence is to the contrary, and it is so found.</blockquote>
<blockquote>"No good reason has been suggested why these two branches of the Department of Justice should not cooperate, and that is the extent of the showing made on the part of the defendant." <span class="citation" data-id="8725152"><a href="/opinion/8741899/united-states-v-abel/#11" aria-description="Citation for case: United States v. Abel">155 F. Supp. 8, 11</a></span>.</blockquote>
<p>The opinion of the Court of Appeals, after careful consideration of the matter, held that the answer "must clearly be in the affirmative" to the question "whether the evidence in the record supports the finding of good faith made by the court below." <span class="citation" data-id="245929"><a href="/opinion/245929/united-states-v-rudolph-ivanovich-abel-also-known-as-mark-and-also/#494" aria-description="Citation for case: United States v. Rudolph Ivanovich Abel, Also Known as...">258 F. 2d 485, 494</a></span>.</p>
<p>Among the statements in evidence relied upon by the lower courts in making these findings was testimony by Noto that the interest of the I. N. S. in petitioner was confined to petitioner's illegal status in the United States; that in informing the I. N. S. about petitioner's presence in the United States the F. B. I. did not indicate what action it wanted the I. N. S. to take; that Noto himself made the decision to arrest petitioner and to commence deportation proceedings against him; that the F. B. I. made no request of him to search for evidence of espionage at the time of the arrest; and that it was "usual and mandatory" for the F. B. I. and I. N. S. to work together in the manner they did. There was also the testimony of Schoenenberger, regarding the purpose of the search he <span class="star-pagination">*228</span> made of petitioner's belongings, that the motive was to look for weapons and documentary evidence of alienage. To be sure, the record is not barren of evidence supporting an inference opposed to the conclusion to which the two lower courts were led by the record as a whole: for example, the facts that the I. N. S. held off its arrest of petitioner while the F. B. I. solicited his cooperation, and that the F. B. I. held itself ready to search petitioner's room as soon as it was vacated. These elements, however, did not, and were not required to, persuade the two courts below in the face of ample evidence of good faith to the contrary, especially the human evidence of those involved in the episode. We are not free to overturn the conclusion of the courts below when justified by such solid proof.</p>
<p>Petitioner's basic contention comes down to this: even without a showing of bad faith, the F. B. I. and I. N. S. must be held to have cooperated to an impermissible extent in this case, the case being one where the alien arrested by the I. N. S. for deportation was also suspected by the F. B. I. of crime. At the worst, it may be said that the circumstances of this case reveal an opportunity for abuse of the administrative arrest. But to hold illegitimate, in the absence of bad faith, the cooperation between I. N. S. and F. B. I. would be to ignore the scope of rightful cooperation between two branches of a single Department of Justice concerned with enforcement of different areas of law under the common authority of the Attorney General.</p>
<p>The facts are that the F. B. I. suspected petitioner both of espionage and illegal residence in the United States as an alien. That agency surely acted not only with propriety but in discharge of its duty in bringing petitioner's illegal status to the attention of the I. N. S., particularly after it found itself unable to proceed with petitioner's prosecution for espionage. Only the I. N. S. is authorized to initiate deportation proceedings, and certainly the <span class="star-pagination">*229</span> F. B. I. is not to be required to remain mute regarding one they have reason to believe to be a deportable alien, merely because he is also suspected of one of the gravest of crimes and the F. B. I. entertains the hope that criminal proceedings may eventually be brought against him. The I. N. S., just as certainly, would not have performed its responsibilities had it been deterred from instituting deportation proceedings solely because it became aware of petitioner through the F. B. I., and had knowledge that the F. B. I. suspected petitioner of espionage. The Government has available two ways of dealing with a criminally suspect deportable alien. It would make no sense to say that branches of the Department of Justice may not cooperate in pursuing one course of action or the other, once it is honestly decided what course is to be preferred. For the same reasons this cooperation may properly extend to the extent and in the manner in which the F. B. I. and I. N. S. cooperated in effecting petitioner's administrative arrest. Nor does it taint the administrative arrest that the F. B. I. solicited petitioner's cooperation before it took place, stood by while it did, and searched the vacated room after the arrest. The F. B. I. was not barred from continuing its investigation in the hope that it might result in a prosecution for espionage because the I. N. S., in the discharge of its duties, had embarked upon an independent decision to initiate proceedings for deportation.</p>
<p>The Constitution does not require that honest law enforcement should be put to such an irrevocable choice between two recourses of the Government. For a contrast to the proper cooperation between two branches of a single Department of Justice as revealed in this case, see the story told in <i>Colyer</i> v. <i>Skeffington,</i> <span class="citation" data-id="8816033"><a href="/opinion/8831099/colyer-v-skeffington/" aria-description="Citation for case: Colyer v. Skeffington">265 F. 17</a></span>. That case sets forth in detail the improper use of immigration authorities by the Bureau of Investigation of the Department of Justice when the immigration service was <span class="star-pagination">*230</span> a branch of the Department of Labor and was acting not within its lawful authority but as the cat's paw of another, unrelated branch of the Government.</p>
<p>We emphasize again that our view of the matter would be totally different had the evidence established, or were the courts below not justified in not finding that the administrative warrant was here employed as an instrument of criminal law enforcement to circumvent the latter's legal restrictions, rather than as a bona fide preliminary step in a deportation proceeding. The test is whether the decision to proceed administratively toward deportation was influenced by, and was carried out for, a purpose of amassing evidence in the prosecution for crime. The record precludes such a finding by this Court.</p>
<p></p>
<h2>II.</h2>
<p>The claim that the administrative warrant by which petitioner was arrested was invalid, because it did not satisfy the requirements for "warrants" under the Fourth Amendment, is not entitled to our consideration in the circumstances before us. It was not made below; indeed, it was expressly disavowed. Statutes authorizing administrative arrest to achieve detention pending deportation proceedings have the sanction of time. It would emphasize the disregard for the presumptive respect the Court owes to the validity of Acts of Congress, especially when confirmed by uncontested historical legitimacy, to bring into question for the first time such a long-sanctioned practice of government at the behest of a party who not only did not challenge the exercise of authority below, but expressly acknowledged its validity.</p>
<p>The grounds relied on in the trial court and the Court of Appeals by petitioner were solely (in addition to the insufficiency of the evidence, a contention not here for review) (1) the bad faith of the Government's use of <span class="star-pagination">*231</span> the administrative arrest warrant and (2) the lack of a power incidental to the execution of an administrative warrant to search and seize articles for use as evidence in a later criminal prosecution. At no time did petitioner question the legality of the administrative arrest procedure either as unauthorized or as unconstitutional. Such challenges were, to repeat, disclaimed. At the hearing on the motion to suppress, petitioner's counsel was questioned by the court regarding the theory of relief relied upon:</p>
<blockquote>"The Court: They [the Government] were not at liberty to arrest him [petitioner]?</blockquote>
<blockquote>"Mr. Fraiman: No, your Honor.</blockquote>
<blockquote>"They were perfectly proper in arresting him.</blockquote>
<blockquote>"We don't contend that at all.</blockquote>
<blockquote>"As a matter of fact, we contend it was their duty to arrest this man as they did.</blockquote>
<blockquote>"I think it should show or rather, it showed admirable thinking on the part of the F. B. I. and the Immigration Service.</blockquote>
<blockquote>"We don't find any fault with that.</blockquote>
<blockquote>"Our contention is that although they were permitted to arrest this man, and in fact, had a duty to arrest this man in a manner in which they did, they did not have a right to search his premises for the material which related to espionage.</blockquote>
<blockquote>.....</blockquote>
<blockquote>". . . He was charged with no criminal offense in this warrant.</blockquote>
<blockquote>"The Court: He was suspected of being illegally in the country, wasn't he?</blockquote>
<blockquote>"Mr. Fraiman: Yes, your Honor.</blockquote>
<blockquote>"The Court: He was properly arrested.</blockquote>
<blockquote>"Mr. Fraiman: He was properly arrested, we concede that, your Honor."</blockquote>
<p><span class="star-pagination">*232</span> Counsel further made it plain that the arrest warrant whose validity he was conceding was "one of these Immigration warrants which is obtained without any background material at all." Affirmative acceptance of what is now sought to be questioned could not be plainer.</p>
<p>The present form of the legislation giving authority to the Attorney General or his delegate to arrest aliens pending deportation proceedings under an administrative warrant, not a judicial warrant within the scope of the Fourth Amendment, is § 242 (a) of the Immigration and Nationality Act of 1952. (<span class="citation no-link">8 U. S. C. § 1252</span> (a)). The regulations under this Act delegate the authority to issue these administrative warrants to the District Directors of the I. N. S. "[a]t the commencement of any proceeding [to deport] . . . or at any time thereafter . . . whenever, in [their] . . . discretion, it appears that the arrest of the respondent is necessary or desirable." <span class="citation no-link">8 CFR § 242.2</span> (a). Also, according to these regulations, proceedings to deport are commenced by orders to show cause issued by the District Directors or others; and the "Operating Instructions" of the I. N. S. direct that the application for an order to show cause should be based upon a showing of a prima facie case of deportability. The warrant of arrest for petitioner was issued by the New York District Director of the I. N. S. at the same time as he signed an order to show cause. Schoenenberger testified that, before the warrant and order were issued, he and Kanzler related to the District Director what they had learned from the F. B. I. regarding petitioner's status as an alien, and the order to show cause recited that petitioner had failed to register, as aliens must. Since petitioner was a suspected spy, who had never acknowledged his residence in the United States to the Government or openly admitted his presence here, there was ample reason to believe that his arrest pending deportation was "necessary or desirable." The arrest procedure followed <span class="star-pagination">*233</span> in the present case fully complied with the statute and regulations.</p>
<p>Statutes providing for deportation have ordinarily authorized the arrest of deportable aliens by order of an executive official. The first of these was in 1798. Act of June 25, 1798, c. 58, § 2, <span class="citation no-link">1 Stat. 571</span>. And see, since that time, and before the present Act, Act of Oct. 19, 1888, c. 1210, <span class="citation no-link">25 Stat. 566</span>; Act of Mar. 3, 1903, c. 1012, § 21, <span class="citation no-link">32 Stat. 1218</span>; Act of Feb. 20, 1907, c. 1134, § 20, <span class="citation no-link">34 Stat. 904</span>; Act of Feb. 5, 1917, c. 29, § 19, <span class="citation no-link">39 Stat. 889</span>; Act of Oct. 16, 1918, c. 186, § 2, <span class="citation no-link">40 Stat. 1012</span>; Act of May 10, 1920, c. 174, <span class="citation no-link">41 Stat. 593</span>; Internal Security Act of 1950, c. 1024, Title I, § 22, <span class="citation no-link">64 Stat. 1008</span>. To be sure, some of these statutes, namely the Acts of 1888, 1903 and 1907, dealt only with aliens who had landed illegally in the United States, and not with aliens sought to be deported by reason of some act or failure to act since entering. Even apart from these, there remains overwhelming historical legislative recognition of the propriety of administrative arrest for deportable aliens such as petitioner.</p>
<p>The constitutional validity of this long-standing administrative arrest procedure in deportation cases has never been directly challenged in reported litigation. Two lower court cases involved oblique challenges, which were summarily rejected. <i>Podolski</i> v. <i>Baird,</i> <span class="citation" data-id="1880326"><a href="/opinion/1880326/podolski-v-baird/" aria-description="Citation for case: Podolski v. Baird">94 F. Supp. 294</a></span>; <i>Ex parte Avakian,</i> <span class="citation" data-id="8779629"><a href="/opinion/8795568/ex-parte-avakian/#692" aria-description="Citation for case: Ex parte Avakian">188 F. 688, 692</a></span>. See also the discussion in <i>Colyer</i> v. <i>Skeffington,</i> <span class="citation" data-id="8816033"><a href="/opinion/8831099/colyer-v-skeffington/" aria-description="Citation for case: Colyer v. Skeffington">265 F. 17</a></span>, reversed on other grounds <i>sub nom. </i><i>Skeffington</i> v. <i>Katzeff,</i> <span class="citation" data-id="8823361"><a href="/opinion/8838268/skeffington-v-katzeff/" aria-description="Citation for case: Skeffington v. Katzeff">277 F. 129</a></span>, where the District Court made an exhaustive examination of the fairness of a group of deportation proceedings initiated by administrative arrests, but nowhere brought into question the validity of the administrative arrest procedure as such. This Court seems never expressly to have directed its attention to the particular question of the constitutional validity of administrative deportation warrants. It has <span class="star-pagination">*234</span> frequently, however, upheld administrative deportation proceedings shown by the Court's opinion to have been begun by arrests pursuant to such warrants. See <i>The Japanese Immigrant Case,</i> <span class="citation" data-id="95830"><a href="/opinion/95830/the-japanese-immigrant-case/" aria-description="Citation for case: The Japanese Immigrant Case">189 U. S. 86</a></span>; <i>Zakonaite</i> v. <i>Wolf,</i> <span class="citation" data-id="97714"><a href="/opinion/97714/zakonaite-v-wolf/" aria-description="Citation for case: Zakonaite v. Wolf">226 U. S. 272</a></span>; <i>Bilokumsky</i> v. <i>Tod,</i> <span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">263 U. S. 149</a></span>; <i>Carlson</i> v. <i>Landon,</i> <span class="citation" data-id="9420689"><a href="/opinion/104978/carlson-v-landon/" aria-description="Citation for case: Carlson v. Landon">342 U. S. 524</a></span>. In <i>Carlson</i> v. <i><span class="citation" data-id="9420689"><a href="/opinion/104978/carlson-v-landon/" aria-description="Citation for case: Carlson v. Landon">Landon</a></span></i><i>,</i> the validity of the arrest was necessarily implicated, for the Court there sustained discretion in the Attorney General to deny bail to alien Communists held pending deportation on administrative arrest warrants. In the presence of this impressive historical evidence of acceptance of the validity of statutes providing for administrative deportation arrest from almost the beginning of the Nation, petitioner's disavowal of the issue below calls for no further consideration.</p>
<p></p>
<h2>III.</h2>
<p>Since petitioner's arrest was valid, we reach the question whether the seven challenged items, all seized during searches which were a direct consequence of that arrest, were properly admitted into evidence. This issue raises three questions: (1) Were the searches which produced these items proper searches for the Government to have made? If they were not, then whatever the nature of the seized articles, and however proper it would have been to seize them during a valid search, they should have been suppressed as the fruits of activity in violation of the Fourth Amendment. <i>E. g., </i><i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#393" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 393</a></span>. (2) Were the articles seized properly subject to seizure, even during a lawful search? We have held in this regard that not every item may be seized which is properly inspectible by the Government in the course of a legal search; for example, private papers desired by the Government merely for use as evidence may not be seized, no matter how lawful the search which <span class="star-pagination">*235</span> discovers them, <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#310" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 310</a></span>, nor may the Government seize, wholesale, the contents of a house it might have searched, <i>Kremen</i> v. <i>United States,</i> <span class="citation" data-id="8931353"><a href="/opinion/8940894/kremen-v-united-states/" aria-description="Citation for case: Kremen v. United States">353 U. S. 346</a></span>. (3) Was the Government free to use the articles, even if properly seized, as evidence in a criminal case, the seizures having been made in the course of a separate administrative proceeding?</p>
<p>The most fundamental of the issues involved concerns the legality of the search and seizures made in petitioner's room in the Hotel Latham. The ground of objection is that a search may not be conducted as an incident to a lawful administrative arrest.</p>
<p>We take as a starting point the cases in this Court dealing with the extent of the search which may properly be made without a warrant following a lawful arrest for crime. The several cases on this subject in this Court cannot be satisfactorily reconciled. This problem has, as is well-known, provoked strong and fluctuating differences of view on the Court. This is not the occasion to attempt to reconcile all the decisions, or to re-examine them. Compare <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span>, with <i>Go-Bart Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span>, and <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452</a></span>; compare <i><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">Go-Bart, supra,</a></span></i> and <i><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">Lefkowitz, supra,</a></span></i> with <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span>, and <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>; compare also <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris, supra,</a></span></i> with <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span>, and <i><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span></i> with <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz, supra</a></span></i> (overruling <i><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span></i>). Of these cases, <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> set by far the most permissive limits upon searches incidental to lawful arrests. In view of their judicial context, the trial judge and the Government justifiably relied upon these cases for guidance at the trial; and the petitioner himself accepted the <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> case on the motion to suppress, nor does he ask this Court to reconsider <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span>.</i> It would, under these circumstances, be unjustifiable retrospective <span class="star-pagination">*236</span> lawmaking for the Court in this case to reject the authority of these decisions.</p>
<p>Are there to be permitted incidental to valid administrative arrests, searches as broad in physical area as, and analogous in purpose to, those permitted by the applicable precedents as incidents to lawful arrests for crime? Specifically, were the officers of the I. N. S. acting lawfully in this case when, after his arrest, they searched through petitioner's belongings in his hotel room looking for weapons and documents to evidence his "alienage"? There can be no doubt that a search for weapons has as much justification here as it has in the case of an arrest for crime, where it has been recognized as proper. <i>E. g., </i><i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span>. It is no less important for government officers, acting under established procedure to effect a deportation arrest rather than one for crime, to protect themselves and to insure that their prisoner retains no means by which to accomplish an escape.</p>
<p>Nor is there any constitutional reason to limit the search for materials proving the deportability of an alien, when validly arrested, more severely than we limit the search for materials probative of crime when a valid criminal arrest is made. The need for the proof is as great in one case as in the other, for deportation can be accomplished only after a hearing at which deportability is established. Since a deportation arrest warrant is not a judicial warrant, a search incidental to a deportation arrest is without the authority of a judge or commissioner. But so is a search incidental to a criminal arrest made upon probable cause without a warrant, and under <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#60" aria-description="Citation for case: United States v. Rabinowitz">339 U. S., at 60</a></span>, such a search does not require a judicial warrant for its validity. It is to be remembered that an I. N. S. officer may not arrest and search on his own. Application for a warrant must be made to an independent responsible officer, the District Director <span class="star-pagination">*237</span> of the I. N. S., to whom a prima facie case of deportability must be shown. The differences between the procedural protections governing criminal and deportation arrests are not of a quality or magnitude to warrant the deduction of a constitutional difference regarding the right of incidental search. If anything, we ought to be more vigilant, not less, to protect individuals and their property from warrantless searches made for the purpose of turning up proof to convict than we are to protect them from searches for matter bearing on deportability. According to the uniform decisions of this Court deportation proceedings are not subject to the constitutional safeguards for criminal prosecutions. Searches for evidence of crime present situations demanding the greatest, not the least, restraint upon the Government's intrusion into privacy; although its protection is not limited to them, it was at these searches which the Fourth Amendment was primarily directed. We conclude, therefore, that government officers who effect a deportation arrest have a right of incidental search analogous to the search permitted criminal law-enforcement officers.</p>
<p>Judged by the prevailing doctrine, the search of petitioner's hotel room was justified. Its physical scope, being confined to the petitioner's room and the adjoining bathroom, was far less extensive than the search in <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span>.</i> The search here was less intensive than were the deliberately exhaustive quests in <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span>,</i> and its purpose not less justifiable. The only things sought here, in addition to weapons, were documents connected with petitioner's status as an alien. These may well be considered as instruments or means for accomplishing his illegal status, and thus proper objects of search under <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris, supra,</a></span></i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#154" aria-description="Citation for case: Harris v. United States">331 U. S., at 154</a></span>.</p>
<p>Two of the challenged items were seized during this search of petitioner's property at his hotel room. The first was item (2), a forged New York birth certificate <span class="star-pagination">*238</span> for "Martin Collins," one of the false identities which petitioner assumed in this country in order to keep his presence here undetected. This item was seizable when found during a proper search, not only as a forged official document by which petitioner sought to evade his obligation to register as an alien, but also as a document which petitioner was using as an aid in the commission of espionage, for his undetected presence in this country was vital to his work as a spy. Documents used as a means to commit crime are the proper subjects of search warrants, <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span>, and are seizable when discovered in the course of a lawful search, <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span>.</p>
<p>The other item seized in the course of the search of petitioner's hotel room was item (1), a piece of graph paper containing a coded message. This was seized by Schoenenberger as petitioner, while packing his suitcase, was seeking to hide it in his sleeve. An arresting officer is free to take hold of articles which he sees the accused deliberately trying to hide. This power derives from the dangers that a weapon will be concealed, or that relevant evidence will be destroyed. Once this piece of graph paper came into Schoenenberger's hands, it was not necessary for him to return it, as it was an instrumentality for the commission of espionage. This is so even though Schoenenberger was not only not looking for items connected with espionage but could not properly have been searching for the purpose of finding such items. When an article subject to lawful seizure properly comes into an officer's possession in the course of a lawful search it would be entirely without reason to say that he must return it because it was not one of the things it was his business to look for. See <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris, supra,</a></span></i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#154" aria-description="Citation for case: Harris v. United States">331 U. S., at 154-155</a></span>.</p>
<p>Items (3), (4), and (5), a birth certificate for "Emil Goldfus" who died in 1903, a certificate of vaccination for "Martin Collins," and a bank book for "Emil Goldfus" <span class="star-pagination">*239</span> were seized, not in petitioner's hotel room, but in a more careful search at I. N. S. headquarters of the belongings petitioner chose to take with him when arrested. This search was a proper one. The property taken by petitioner to I. N. S. headquarters was all property which, under <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span>,</i> was subject to search at the place of arrest. We do not think it significantly different, when the accused decides to take the property with him, for the search of it to occur instead at the first place of detention when the accused arrives there, especially as the search of property carried by an accused to the place of detention has additional justifications, similar to those which justify a search of the person of one who is arrested. It is to be noted that this is not a case, like <i>Kremen</i> v. <i>United States,</i> <span class="citation" data-id="8931353"><a href="/opinion/8940894/kremen-v-united-states/" aria-description="Citation for case: Kremen v. United States">353 U. S. 346</a></span>, where the entire contents of the place where the arrest was made were seized. Such a mass seizure is illegal. The Government here did not seize the contents of petitioner's hotel room. Petitioner took with him only what he wished. He chose to leave some things behind in his room, which he voluntarily relinquished. And items (3), (4), and (5) were articles subject to seizure when found during a lawful search. They were all capable of being used to establish and maintain a false identity for petitioner, just as the forged "Martin Collins" birth certificate, and were seizable for the same reasons.</p>
<p>Items (1)-(5) having come into the Government's possession through lawful searches and seizures connected with an arrest pending deportation, was the Government free to use them as evidence in a criminal prosecution to which they related? We hold that it was. Good reason must be shown for prohibiting the Government from using relevant, otherwise admissible, evidence. There is excellent reason for disallowing its use in the case of evidence, though relevant, which is seized by the Government in violation of the Fourth Amendment to the Constitution. "If letters and private documents can thus <span class="star-pagination">*240</span> be seized and held and used in evidence against a citizen accused of an offense, the protection of the Fourth Amendment declaring his right to be secure against such searches and seizures is of no value, and, so far as those thus placed are concerned, might as well be stricken from the Constitution." <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#393" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 393</a></span>.</p>
<p>These considerations are here absent, since items (1)-(5) were seized as a consequence of wholly lawful conduct. That being so, we can see no rational basis for excluding these relevant items from trial: no wrong-doing police officer would thereby be indirectly condemned, for there were no such wrongdoers; the Fourth Amendment would not thereby be enforced, for no illegal search or seizure was made; the Court would be lending its aid to no lawless government action, for none occurred. Of course cooperation between the branch of the Department of Justice dealing with criminal law enforcement and the branch dealing with the immigration laws would be less effective if evidence lawfully seized by the one could not be used by the other. Only to the extent that it would be to the public interest to deter and prevent such cooperation, would an exclusionary rule in a case like the present be desirable. Surely no consideration of civil liberties commends discouragement of such cooperation between these two branches when undertaken in good faith. When undertaken in bad faith to avoid constitutional restraints upon criminal law enforcement the evidence must be suppressed. That is not, as we have seen, this case. Individual cases of bad faith cooperation should be dealt with by findings to that effect in the cases as they arise, not by an exclusionary rule preventing effective cooperation when undertaken in entirely good faith.</p>
<p>We have left to the last the admissibility of items (6) and (7), the hollowed-out pencil and the block of wood containing a "cipher pad," because their admissibility is founded upon an entirely different set of considerations. <span class="star-pagination">*241</span> These two items were found by an agent of the F. B. I. in the course of a search he undertook of petitioner's hotel room, immediately after petitioner had paid his bill and vacated the room. They were found in the room's wastepaper basket, where petitioner had put them while packing his belongings and preparing to leave. No pretense is made that this search by the F. B. I. was for any purpose other than to gather evidence of crime, that is, evidence of petitioner's espionage. As such, however, it was entirely lawful, although undertaken without a warrant. This is so for the reason that at the time of the search petitioner had vacated the room. The hotel then had the exclusive right to its possession, and the hotel management freely gave its consent that the search be made. Nor was it unlawful to seize the entire contents of the wastepaper basket, even though some of its contents had no connection with crime. So far as the record shows, petitioner had abandoned these articles. He had thrown them away. So far as he was concerned, they were <i>bona vacantia.</i> There can be nothing unlawful in the Government's appropriation of such abandoned property. See <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#58" aria-description="Citation for case: Hester v. United States">265 U. S. 57, 58</a></span>. The two items which were eventually introduced in evidence were assertedly means for the commission of espionage, and were themselves seizable as such. These two items having been lawfully seized by the Government in connection with an investigation of crime, we encounter no basis for discussing further their admissibility as evidence.</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE DOUGLAS, with whom MR. JUSTICE BLACK concurs, dissenting.</p>
<p>Cases of notorious criminalslike cases of small, miserable onesare apt to make bad law. When guilt permeates a record, even judges sometimes relax and let the police take shortcuts not sanctioned by constitutional <span class="star-pagination">*242</span> procedures. That practice, in certain periods of our history and in certain courts, has lowered our standards of law administration. The harm in the given case may seem excusable. But the practices generated by the precedent have far-reaching consequences that are harmful and injurious beyond measurement. The present decision is an excellent example.</p>
<p>The opening wedge that broadened the power of administrative officersas distinguished from policeto enter and search peoples' homes was <i>Frank</i> v. <i>Maryland,</i> <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360</a></span>. That case allowed a health inspector to enter a home without a warrant, even though he had ample time to get one. The officials of the Immigration and Naturalization Service (I. N. S.) are now added to the preferred list. They are preferred because their duties, being strictly administrative, put them in a separate category from those who enforce the criminal law. They need not go to magistrates, the Court says, for warrants of arrest. Their warrants are issued within the hierarchy of the agency itself.<sup>[1]</sup> Yet, as I attempted to show in my dissent in the <i><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span></i> case, the Fourth Amendment in origin had to do as much with ferreting out heretics and collecting taxes as with enforcement of the criminal laws. <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#376" aria-description="Citation for case: Frank v. Maryland">359 U. S., at 376-379</a></span>.</p>
<p>Moreover, the administrative officer who invades the privacy of the home may be only a front for the police who are thus saved the nuisance of getting a warrant. We need not go far to find examples. In <i>Maryland</i> v. <i>Pettiford,</i> Sup. Bench Balt. City, The Daily Record, Dec. 16, 1959, the police used the mask of a health inspector <span class="star-pagination">*243</span> to make the <i><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span></i> case serve as an easy way to get a search without a warrant. Happily, they were rebuked.<sup>[2]</sup> But that case shows the kind of problems the <i><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span></i> doctrine generates. The present case is another example of the same kind, although here the police are not rebuked. The administrative official with an administrative warrant, over which no judicial official exercises any supervision and which by statute may be used only for deportation, performs a new role. The police wear his mask to do police work. That, in my view, may not be done, even though we assume that the administrative warrant <span class="star-pagination">*244</span> issued by an administrative rather than a judicial officer is valid for an arrest for the purpose of deportation. We take liberties with an Act of Congress, as well as the Constitution, when we permit this to be done. The statute permits the arrest of an alien on an administrative warrant "[p]ending a determination of deportability."<sup>[3]</sup> The Court now reads the Act as if it read "Pending an investigation of criminal conduct." Such was the nature of the arrest.</p>
<p>With due deference to the two lower courts, I think the record plainly shows that F. B. I. agents were the moving force behind this arrest and search. For at least a month they investigated the espionage activities of petitioner. They were tipped off concerning this man and his role in May; the arrest and search were made on June 21. The F. B. I. had plenty of time to get a search warrant, as much if not more time than they had in <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, and <i>Kremen</i> v. <i>United States,</i> <span class="citation" data-id="8931353"><a href="/opinion/8940894/kremen-v-united-states/" aria-description="Citation for case: Kremen v. United States">353 U. S. 346</a></span>, where the Court held warrantless searches illegal. But the F. B. I. did not go to a magistrate for a search warrant. They went instead to the I. N. S. and briefed the officials of that agency on what they had discovered. On the basis of this data a report was made to John Murff, Acting District Director of the I. N. S., who issued the warrant of arrest.</p>
<p>No effort was made by the F. B. I. to obtain a search warrant from any judicial officer, though, as I said, there was plenty of time for such an application. The administrative warrant of arrest was chosen with care and calculation as the vehicle through which the arrest and search were to be made. The F. B. I. had an agreement with the officials of I. N. S. that this warrant of arrest would not be served at least until petitioner refused to <span class="star-pagination">*245</span> "cooperate." The F. B. I. agents went with agents of the I. N. S. to apprehend petitioner in his hotel room. Again, it was the F. B. I. agents who were first. They were the ones who entered petitioner's room and who interrogated him to see if he would "cooperate"; and when they were unable to get him to "cooperate" by threatening him with arrest, they signaled agents of the I. N. S. who had waited outside to come in and make the arrest. The search was made both by the F. B. I. agents and by officers of the I. N. S. And when petitioner was flown 1,000 miles to a special detention camp and held for three weeks, the agents of the F. B. I. as well as I. N. S. interrogated him.<sup>[4]</sup></p>
<p>Thus the F. B. I. used an administrative warrant to make an arrest for criminal investigation both in violation of § 242 (a) of the Immigration and Nationality Act<sup>[5]</sup> and in violation of the Bill of Rights.</p>
<p>The issue is not whether these F. B. I. agents acted in bad faith. Of course they did not. The question is how far zeal may be permitted to carry officials bent on law enforcement. As Mr. Justice Brandeis once said, "Experience should teach us to be most on our guard to protect liberty when the Government's purposes are beneficent." <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#479" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 479</a></span> (dissenting opinion). The facts seem to me clearly to establish that the F. B. I. agents wore the mask of I. N. S. to do what otherwise they could not have done. They did what they could do only if they had gone to a judicial officer pursuant to the requirements of the Fourth Amendment, disclosed <span class="star-pagination">*246</span> their evidence, and obtained the necessary warrant for the searches which they made.</p>
<p>If the F. B. I. agents had gone to a magistrate, any search warrant issued would by terms of the Fourth Amendment have to "particularly" describe "the place to be searched" and the "things to be seized." How much more convenient it is for the police to find a way around those specific requirements of the Fourth Amendment! What a hindrance it is to work laboriously through constitutional procedures! How much easier to go to another official in the same department! The administrative officer can give a warrant good for unlimited search. No more showing of probable cause to a magistrate! No more limitations on what may be searched and when!</p>
<p>In <i>Rea</i> v. <i>United States,</i> <span class="citation" data-id="9421227"><a href="/opinion/105343/rea-v-united-states/" aria-description="Citation for case: Rea v. United States">350 U. S. 214</a></span>, federal police officers, who obtained evidence in violation of federal law governing searches and seizures and so lost their case in the federal court, repaired to a state court and proposed to use it there in a state criminal prosecution. The Court held that the Federal District Court could properly enjoin the federal official from using the illegal search and seizure as basis for testifying in the state court. The federal rules governing searches and seizures, we held, are "designed as standards for federal agents" no more to be defeated by devious than by direct methods. The present case is even more palpably vulnerable. No state agency is involved. Federal police seek to do what immigration officials can do to deport a person but what our rules, statutes, and Constitution forbid the police from doing to prosecute him for a crime.</p>
<p>The tragedy in our approval of these short cuts is that the protection afforded by the Fourth Amendment is removed from an important segment of our life. We today forget what the Court said in <i>Johnson</i> v. <i>United States, supra,</i> at 14, that the Fourth Amendment provision <span class="star-pagination">*247</span> for "probable cause" requires that those inferences "be drawn by a neutral and detached magistrate" not "by the officer engaged in the often competitive enterprise of ferreting out crime." This is a protection given not only to citizens but to aliens as well, as the opinion of the Court by implication holds. The right "of the people" covered by the Fourth Amendment certainly gives security to aliens in the same degree that "person" in the Fifth and "the accused" in the Sixth Amendments also protects them. See <i>Wong Wing</i> v. <i>United States,</i> <span class="citation" data-id="9883065"><a href="/opinion/94479/wong-wing-v-united-states/#242" aria-description="Citation for case: Wong Wing v. United States">163 U. S. 228, 242</a></span>. Here the F. B. I. works exclusively through an administrative agencythe I. N. S.to accomplish what the Fourth Amendment says can be done only by a judicial officer. A procedure designed to serve administrative endsdeportationis cleverly adapted to serve other endscriminal prosecution. We have had like examples of this same trend in recent times. Lifting the requirements of the Fourth Amendment for the benefit of health inspectors was accomplished by <i>Frank</i> v. <i><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Maryland</a></span></i><i>,</i> as I have said. Allowing the Department of Justice rather than judicial officers to determine whether aliens will be entitled to release on bail pending deportation hearings is another. See <i>Carlson</i> v. <i>Landon,</i> <span class="citation" data-id="9420689"><a href="/opinion/104978/carlson-v-landon/" aria-description="Citation for case: Carlson v. Landon">342 U. S. 524</a></span>.</p>
<p>Some things in our protective scheme of civil rights are entrusted to the judiciary. Those controls are not always congenial to the police. Yet if we are to preserve our system of checks and balances and keep the police from being all-powerful, these judicial controls should be meticulously respected. When we read them out of the Bill of Rights by allowing short cuts as we do today and as the Court did in the <i><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span></i> and <i><span class="citation" data-id="9420689"><a href="/opinion/104978/carlson-v-landon/" aria-description="Citation for case: Carlson v. Landon">Carlson</a></span></i> cases, police and administrative officials in the Executive Branch acquire powers incompatible with the Bill of Rights.</p>
<p>The F. B. I. agents stalked petitioner for weeks and had plenty of time to obtain judicial warrants for searching the <span class="star-pagination">*248</span> premises he occupied. I would require them to adhere to the command of the Fourth Amendment and not evade it by the simple device of wearing the masks of immigration officials while in fact they are preparing a case for criminal prosecution.</p>
<p>MR. JUSTICE BRENNAN, with whom THE CHIEF JUSTICE, MR. JUSTICE BLACK and MR. JUSTICE DOUGLAS join, dissenting.</p>
<p>This is a notorious case, with a notorious defendant. Yet we must take care to enforce the Constitution without regard to the nature of the crime or the nature of the criminal. The Fourth Amendment protects "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures." This right is a basic one of all the people, without exception; and this Court ruled in <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, that the fruits of governmental violation of this guarantee could not be used in a criminal prosecution. The Amendment's protection is thus made effective for everyone only by upholding it when invoked by the worst of men.</p>
<p>The opinion of the Court makes it plain that the seizure of certain of the items of petitioner taken from his room at the Hotel Latham and used in evidence against him must depend upon the existence of a broad power, without a warrant, to search the premises of one arrested, in connection with and "incidental" to his arrest. This power is of the sort recognized by <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span>, and later asserted even where the arresting officers, as here, had ample time and opportunity to secure a search warrant. <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>, overruling <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span>. The leading early cases do not recognize any such power to make a search generally through premises attendant upon an arrest. See <i>Go-Bart Importing Co.</i> v. <span class="star-pagination">*249</span> <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span>; <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452</a></span>.<sup>[1]</sup></p>
<p>The general question has been extensively canvassed here, in the general context of an arrest for crime, in the <i>Harris, Trupiano</i> and <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> cases. Whether <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> should now be followed on their own facts is a question with which the Court is not now faced. Rather the question is whether the doctrine of those cases should be extended to a new and different set of facts facts which present a search made under circumstances much less consistent with the Fourth Amendment's prohibition against unreasonable searches than any which this Court has hitherto approved. Factual differences weigh heavily in this area: "There is no formula for the determination of reasonableness. Each case is to be decided on its own facts and circumstances." <i>Go-Bart Importing Co.</i> v. <i>United States, supra,</i> at 357. In <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span>,</i> the broad search was performed as an incident to an arrest for crime under warrants lawfully issued. <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#148" aria-description="Citation for case: Harris v. United States">331 U. S., at 148</a></span>; <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#58" aria-description="Citation for case: United States v. Rabinowitz">339 U. S., at 58</a></span>. The issuance of these warrants is by no means automaticit is controlled by a constitutionally prescribed standard. It thus could be held that sufficient protection was given the individual without the execution of a second warrant for the search. Cf. Clark, J., dissenting in <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9638337"><a href="/opinion/1484849/united-states-v-rabinowitz/#736" aria-description="Citation for case: United States v. Rabinowitz">176 F. 2d 732, 736</a></span>, reversed, <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>. And while a search generally through premises "incident" to an arrest for crime without a warrant has been sanctioned only inferentially here,<sup>[2]</sup> even if such a search be deemed permissible under the Fourth Amendment, it would not go so far as the result here. Such an arrest may <span class="star-pagination">*250</span> constitutionally be made only upon probable cause, the existence of which is subject to judicial examination, see <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#100" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 100</a></span>; and such an arrest demands the prompt bringing of the person arrested before a judicial officer, where the existence of probable cause is to be inquired into. Fed. Rules Crim. Proc., 5 (a) and (c). This Court has been astute to fashion methods of ensuring the due observance of these safeguards. <i>Henry</i> v. <i>United States, supra</i><i>; </i><i>Mallory</i> v. <i>United States,</i> <span class="citation" data-id="105545"><a href="/opinion/105545/mallory-v-united-states/" aria-description="Citation for case: Mallory v. United States">354 U. S. 449</a></span>; <i>McNabb</i> v. <i>United States,</i> <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">318 U. S. 332</a></span>.</p>
<p>Even assuming that the power of Congress over aliens may be as great as was said in <i>Galvan</i> v. <i>Press,</i> <span class="citation" data-id="9421085"><a href="/opinion/105227/galvan-v-press/" aria-description="Citation for case: Galvan v. Press">347 U. S. 522</a></span>, and that deportation may be styled "civil," <i>Harisiades</i> v. <i>Shaughnessy,</i> <span class="citation" data-id="9420696"><a href="/opinion/104980/harisiades-v-shaughnessy/#594" aria-description="Citation for case: Harisiades v. Shaughnessy">342 U. S. 580, 594</a></span>, it does not follow that Congress may strip aliens of the protections of the Fourth Amendment and authorize unreasonable searches of their premises, books and papers. Even if Congress could make the exclusionary sanction of the Amendment inapplicable in deportation proceedings, the fruits of the search here were used in a prosecution whose criminal character no dialectic can conceal. Clearly the consequence of the Fourth Amendment in such a trial is that the fruits of such a search may not be given in evidence, under the rule declared in <i>Weeks</i> v. <i>United States, supra</i><i>.</i> We need not, in my view, inquire as to whether the sort of "administrative" arrest made here is constitutionally valid as to permit the officers to hold petitioner's person for deportation proceedings. With the Court, this issue may be treated as not properly before us for our consideration, and the arrest may be treated for the purposes of this case as lawful in itself. But even with <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and <i>Rabinowitz,</i> that does not conclude the matter as to the search. It is patent that the sort of search permitted by those cases, and necessary to sustain the seizures here, goes beyond what is reasonably related <span class="star-pagination">*251</span> to the mechanics of the arrest itselfensuring the safety of the arresting officers and the security of the arrest against the prisoner's escape. Since it does, I think it plain that before it can be concluded here that the search was not an unreasonable one, there must be some inquiry into the over-all protection given the individual by the totality of the processes necessary to the arrest and the seizure. Here the arrest, while had on what is called a warrant, was made totally without the intervention of an independent magistrate; it was made on the authorization of one administrative official to another. And after the petitioner was taken into custody, there was no obligation upon the administrative officials who arrested him to take him before any independent officer, sitting under the conditions of publicity that characterize our judicial institutions, and justify what had been done.<sup>[3]</sup> Concretely, what happened instead was this: petitioner, upon his arrest, was taken to a local administrative headquarters and then flown in a special aircraft to a special detention camp over 1,000 miles away. He was incarcerated in solitary confinement there. As far as the world knew, he had vanished. He was questioned daily at the place of incarceration for over three weeks. An executive procedure as to his deportability was had, at the camp, after a few days, but there was never any independent inquiry or judicial control over the circumstances of the arrest and the seizure till over five weeks after his arrest, when, at the detention camp, he was served with a bench warrant for his arrest on criminal charges, upon an indictment.</p>
<p>The Fourth Amendment imposes substantive standards for searches and seizures; but with them one of the important safeguards it establishes is a procedure; and <span class="star-pagination">*252</span> central to this procedure is an independent control over the actions of officers effecting searches of private premises. "Indeed, the informed and deliberate determinations of magistrates empowered to issue warrants as to what searches and seizures are permissible under the Constitution are to be preferred over the hurried action of officers and others who may happen to make arrests." <i>United States</i> v. <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#464" aria-description="Citation for case: United States v. Lefkowitz"><i>Lefkowitz, supra,</i> at 464</a></span>. "Absent some grave emergency, the Fourth Amendment has interposed a magistrate between the citizen and the police." <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 455</a></span>. It is one thing to say that an adequate substitute for this sort of intervention by a magistrate can be found in the strict protections with which federal criminal procedure surrounds the making of a criminal arrestwhere the action of the officers must receive an antecedent or immediately subsequent independent scrutiny. It goes much further to say that such a substitute can be found in the executive processes employed here. The question is not whether they are constitutionally adequate in their own termswhether they are a proper means of taking into custody one not charged with crime. The question is rather whether they furnish a context in which a search generally through premises can be said to be a reasonable one under the Fourth Amendment. These arrest procedures, as exemplified here, differ as night from day from the processes of an arrest for crime. When the power to make a broad, warrantless search is added to them, we create a complete concentration of power in executive officers over the person and effects of the individual. We completely remove any independent control over the powers of executive officers to make searches. They may take any man they think to be a deportable alien into their own custody, hold him without arraignment or bond, and, having been careful to apprehend him at home, make a search generally through his premises. I cannot see <span class="star-pagination">*253</span> how this can be said to be consistent with the Fourth Amendment's command; it was, rather, against such a concentration of executive power over the privacy of the individual that the Fourth Amendment was raised. I do not think the <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and <i>Rabinowitz</i> cases have taken us to this point.</p>
<p>If the search here were of the sort the Fourth Amendment contemplated, there would be no need for the elaborate, if somewhat pointless, inquiry the Court makes into the "good faith" of the arrest. Once it is established that a simple executive arrest of one as a deportable alien gives the arresting officers the power to search his premises, what precise state of mind on the part of the officers will make the arrest a "subterfuge" for the start of criminal proceedings, and render the search unreasonable? We are not, I fear, given any workable answer, and of course the practical problems relative to the trial of such a matter hardly need elaboration; but the Court verbalizes the issue as "whether the decision to proceed administratively toward deportation was influenced by, and was carried out for, a purpose of amassing evidence in the prosecution for crime." But under today's ruling, every administrative arrest offers this possibility of a facile search, theoretically for things connected with unlawful presence in the country, that may turn up evidence of crime; and this possibility will be well known to arresting officers. Perhaps the question is how much basis the officers had to suspect the person of crime; but it would appear a strange test as to whether a search which turns up criminal evidence is unreasonable, that the search is the more justifiable the less there was antecedent probable cause to suspect the defendant of crime. If the search were made on a valid warrant, there would be no such issue even if it turned up matter relevant to another crime. See <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#311" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 311-312</a></span>. External procedural control in accord with the <span class="star-pagination">*254</span> basic demands of the Fourth Amendment removes the grounds for abuse; but the Court's attitude here must be based on a recognition of the great possibilities of abuse its decision leaves in the present situation. These possibilities have been recognized before, in a case posing less danger: "Arrest under a warrant for a minor or a trumped-up charge has been familiar practice in the past, is a commonplace in the police state of today, and too well-known in this country. . . . The progress is too easy from police action unscrutinized by judicial authorization to the police state." <i>United States</i> v. <i>Rabinowitz, supra,</i> at 82 (dissenting opinion). Where a species of arrest is available that is subject to no judicial control, the possibilities become more and more serious. The remedy is not to invite fruitless litigation into the purity of official motives, or the specific direction of official purposes. One may always assume that the officers are zealous to perform their duty. The remedy is rather to recognize that the power to perform a search generally throughout premises upon a purely executive arrest is so unconfined by any safeguards that it cannot be countenanced as consistent with the Fourth Amendment.</p>
<p>One more word. We are told that the governmental power to make a warrantless search might be greater where the object of the search is not related to crime but to some other "civil" proceedingsuch as matter bearing on the issue whether a man should forcibly be sent from the country. The distinction is rather hollow here, where the proofs that turn up are in fact given in evidence in a criminal prosecution. And the distinction, again, invites a trial of the officers' purposes. But in any event, I think it perverts the Amendment to make this distinction. The Amendment states its own purpose, the protection of the privacy of the individual and of his property against the incursions of officials: the "right of the people to be secure in their persons, houses, papers, and effects." See <span class="star-pagination">*255</span> <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#627" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 627</a></span>. Like most of the Bill of Rights it was not designed to be a shelter for criminals, but a basic protection for everyone; to be sure, it must be upheld when asserted by criminals, in order that it may be at all effective, but it "reaches all alike, whether accused of crime or not." <i>Weeks</i> v. <i>United States, supra,</i> at 392. It is the individual's interest in privacy which the Amendment protects, and that would not appear to fluctuate with the "intent" of the invading officers. It is true that the greatest and most effective preventive against unlawful searches that has been devised is the exclusion of their fruits from criminal evidence, see <i>Weeks</i> v. <i>United States, supra</i><i>; </i><i>Boyd</i> v. <i>United States, supra</i><i>;</i> but it is strange reasoning to infer from this that the central thrust of the guarantee is to protect against a search for such evidence. The argument that it is seems no more convincing to me now than when it was made by the Court in <i>Frank</i> v. <i>Maryland,</i> <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360</a></span>. To be sure, the Court in <i>Boyd</i> v. <i>United States, supra</i><i>,</i> and in subsequent cases<sup>[4]</sup> has commented upon the intimate relationship between the privilege against unlawful searches and seizures and that against self-incrimination. This has been said to be erroneous history;<sup>[5]</sup> if it was, it was even less than a harmless error; it was part of the process through which the Fourth Amendment, by means of the exclusionary rule, has become more than a dead letter in the federal courts. Certainly this putative relationship between the guarantees is not to be used as a <span class="star-pagination">*256</span> basis of a stinting construction of eitherit was the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case itself<sup>[6]</sup> which set what might have been hoped to be the spirit of later construction of these Amendments by declaring that the start of abuse can "only be obviated by adhering to the rule that constitutional provisions for the security of person and property should be liberally construed." <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U. S., at 635</a></span>.</p>
<p>Since evidence was introduced against petitioner which had been obtained in violation of his constitutional guarantees as embodied in the Fourth Amendment, I would reverse his conviction for a new trial on the evidence not subject to this objection.</p>
<h2>NOTES</h2>
<p>[*]  "1. Whether under the laws and Constitution of the United States (a) the administrative warrant of the New York Acting District Director of the Immigration and Naturalization Service was validly issued, (b) such administrative warrant constituted a valid basis for arresting petitioner or taking him into custody, and (c) such warrant furnished a valid basis for the searches and seizures affecting his person, luggage, and the room occupied by him at the Hotel Latham.
</p>
<p>"2. Whether, independently of such administrative warrant, petitioner's arrest, and the searches and seizures affecting his person, luggage, and the room occupied by him at the Hotel Latham, were valid under the laws and Constitution of the United States.</p>
<p>"3. Whether on the record before us the issues involved in Questions `1 (a),' `1 (b),' and `2' are properly before the Court."</p>
<p>[1]  Section 242 (a) of the Immigration and Nationality Act of 1952, <span class="citation no-link">66 Stat. 208</span>, <span class="citation no-link">8 U. S. C. § 1252</span> (a), provides "Pending a determination of deportability in the case of any alien . . . such alien may, upon warrant of the Attorney General, be arrested and taken into custody."</p>
<p>[2]  In the <i>Pettiford</i> case it appears that a police officer assigned to the Sanitation Division gained entrance into a home without a warrant and discovered that the defendant who occupied the premises was engaged in lottery activities. He then signaled to a policeman in charge of gambling activities who was waiting outside in accordance with a prior agreement. Lottery slips were seized and over the defendant's objection were received in evidence in a criminal trial. A motion for a new trial was granted. The Supreme Bench of Baltimore City said in its opinion:
</p>
<p>"Section 120 of Article 12 of the Baltimore City Code provides that if the Commissioner of Health has cause to suspect that a nuisance exists in any home, he may demand entry therein in the day-time and the owner or occupier is subject to a fine if entry is denied. A conviction under this Section by the Criminal Court of Baltimore City was sustained by the Supreme Court of the United States in a five to four decision. <i>Frank vs. Maryland</i> [<span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360</a></span>]. . . .</p>
<p>.....</p>
<p>"In this case, it is evident that a principal, if not the chief purpose of the entry of the police officer assigned to the sanitation division was to endeavor to secure evidence of a lottery violation for his colleague. "The security of one's privacy against arbitrary intrusion by the police . . . is basic to a free society.' <i>Wolf vs. Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span>. An exception to that security, upheld because indispensible for the maintenance of the community health, is not to be used to cover searches without warrants inconsistent with the conceptions of human rights [embodied] in our State and Federal Constitutions."</p>
<p>[3]  Note 1, <i>supra.</i></p>
<p>[4]  Immigration officials (who often claim that their actions have an administrative finality beyond the reach of courts, see <i>Ludecke</i> v. <i>Watkins,</i> <span class="citation" data-id="9420220"><a href="/opinion/104589/ludecke-v-watkins/" aria-description="Citation for case: Ludecke v. Watkins">335 U. S. 160</a></span>: <i>Jay</i> v. <i>Boyd,</i> <span class="citation" data-id="9421310"><a href="/opinion/105407/jay-v-boyd/" aria-description="Citation for case: Jay v. Boyd">351 U. S. 345</a></span>) have no authority to detain suspects for secret interrogation. See <i>United States</i> v. <i>Minker,</i> <span class="citation" data-id="9421220"><a href="/opinion/105341/united-states-v-minker/" aria-description="Citation for case: United States v. Minker">350 U. S. 179</a></span>.</p>
<p>[5]  Note 1, <i>supra.</i></p>
<p>[1]  Earlier expressions looking the other way, <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span>; <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#198" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 198-199</a></span>, were put in proper perspective by their author in <i>Go-Bart</i> and <i><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">Lefkowitz</a></span>.</i> See <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#358" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S., at 358</a></span>; <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#465" aria-description="Citation for case: United States v. Lefkowitz">285 U. S., at 465</a></span>.</p>
<p>[2]  See <i>United States</i> v. <i>Rabinowitz, supra,</i> at 60.</p>
<p>[3]  This procedure is statutorily based on § 242 (a) of the Immigration and Nationality Act of 1952, <span class="citation no-link">66 Stat. 208</span>, <span class="citation no-link">8 U. S. C. § 1252</span> (a).</p>
<p>[4]  See, <i>e. g., </i><i>Gouled</i> v. <i>United States, supra,</i> at 306; <i>United States</i> v. <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#466" aria-description="Citation for case: United States v. Lefkowitz"><i>Lefkowitz, supra,</i> at 466-467</a></span>. The <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case itself, though drawing great support from <i>Boyd,</i> appears to rest most heavily on the Fourth Amendment itself.</p>
<p>[5]  The famous attack on the <i>Boyd</i> case's historical basis is, of course, to be found in 8 Wigmore, Evidence (3d ed. 1940), §§ 2184, 2264. The attack is incident to Wigmore's strictures on the exclusionary rule. <i>Id.,</i> §§ 2183-2184.</p>
<p>[6]  It is not without interest to note, too, that the <i>Boyd</i> case itself involved a search not in connection with a prosecution to impose fine or imprisonment, but simply with an action to forfeit 35 cases of plate glass said to have been imported into the country under a false customs declaration.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Arizona v. Hicks.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Arizona v. Hicks"
type: case
citation: "480 U.S. 321 (1987)"
parallel_cite: "107 S. Ct. 1149; 94 L. Ed. 2d 347; 55 U.S.L.W. 4258"
neutral_cite: 1987 U.S. LEXIS 1056
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-03-03
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-03-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Arizona v. Hicks
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111834/arizona-v-hicks/"
  cluster_id: 111834
  opinion_id: 9430865
  identity_checked: true
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Key — Anchor"
  - page: "[[Trespass]]"
    role: "Related (cross-doctrine)"
related: ["[[Coolidge v. New Hampshire]]", "[[Horton v. California]]", "[[Texas v. Brown]]"]
aliases: []
tags: ["case", "fourth-amendment", "plain-view", "search"]
holding: "Moving stereo equipment a few inches to read serial numbers was a SEARCH separate from the lawful entry, and 'immediately apparent'…"
lake:
  record_id: Arizona v. Hicks
  status: verified
  projected_at: 2026-07-09
---

# Arizona v. Hicks

*480 U.S. 321 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police entered Hicks's apartment without a warrant under [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] — a bullet had been fired through the floor, injuring a man below — to look for the shooter, other victims, and weapons. Inside, an officer saw expensive stereo equipment that seemed out of place and suspected it was stolen. He moved the components to read and record their serial numbers, phoned them in, learned a turntable had been taken in an armed robbery, and the equipment was seized.

## Issue
Whether moving stereo equipment to read its serial numbers — done on reasonable suspicion during an exigent-circumstances entry — was a "search," and if so whether the [[Plain View Doctrine|plain-view doctrine]] required probable cause rather than mere reasonable suspicion.

## Rule
Moving the equipment to expose hidden information was a new search beyond the entry's justification: the moving of the components "did constitute a 'search' separate and apart from the search for ... the shooter, victims, and weapons that was the lawful objective of his entry into the apartment." — 480 U.S. at 324. ^pin-324

"A search is a search, even if it happens to disclose nothing but the bottom of a turntable." — [*Id.* at 325](https://www.courtlistener.com/opinion/111834/arizona-v-hicks/#:~:text=A%20search%20is%20a%20search%2C). ^pin-325

The [[Plain View Doctrine|plain-view doctrine]] requires probable cause: "We now hold that probable cause is required. To say otherwise would be to cut the 'plain view' doctrine loose from its theoretical and practical moorings." — *Id.* at 326. ^pin-326

## Application
The officer's lawful basis for being in the apartment was the shooting [[Exigent Circumstances and Hot Pursuit|exigency]]; turning the turntable to read a concealed serial number was unrelated to that [[Exigent Circumstances and Hot Pursuit|exigency]] and exposed information the officer could not otherwise see, so it was a separate search. Because the State conceded the officer had only reasonable suspicion — not probable cause — that the equipment was stolen, the [[Plain View Doctrine|plain-view doctrine]] could not justify the search on these facts, and it was unreasonable.

## Conclusion
Moving the equipment was an unreasonable search; the judgment of the Arizona Court of Appeals suppressing the evidence was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Hicks* fixes two plain-view rules: physically *moving* an object to expose hidden details is a search, and invoking the [[Plain View Doctrine|plain-view doctrine]] to examine or seize an item requires **probable cause** (the item's incriminating character must be "immediately apparent"). It works alongside [[Coolidge v. New Hampshire]] (origin of the doctrine) and [[Horton v. California]] (dropping the inadvertence requirement).

## Appears on
- [[Plain View Doctrine]] — *Key — Anchor*
- [[Trespass]] — *Related (cross-doctrine)*

## Sources
- *Arizona v. Hicks*, 480 U.S. 321 (1987) — https://www.courtlistener.com/opinion/111834/arizona-v-hicks/ — pinpoints: 324, 325, 326.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f8a0011db7060c13", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Arizona v. Hicks"}, "payload": {"all": [{"cite": "480 U.S. 321", "page": "321", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "480"}, {"cite": "107 S. Ct. 1149", "page": "1149", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "107"}, {"cite": "94 L. Ed. 2d 347", "page": "347", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "94"}, {"cite": "1987 U.S. LEXIS 1056", "page": "1056", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1987"}, {"cite": "55 U.S.L.W. 4258", "page": "4258", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "55"}], "display": "480 U.S. 321", "official": {"cite": "480 U.S. 321", "page": "321", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "480"}, "official_selection_present": true, "record_id": "Arizona v. Hicks"}}
{"assertion_id": "224263403f07c6b3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-325", "record_id": "Arizona v. Hicks"}, "payload": {"fragment": "#:~:text=A%20search%20is%20a%20search%2C", "page": null, "pin_id": "pin-325", "pinpoint_status": "star-verified", "quote": "A search is a search, even if it happens to disclose nothing but the bottom of a turntable.", "quote_fidelity": "matched", "record_id": "Arizona v. Hicks", "star_marker": "325"}}
{"assertion_id": "4ba306d61dd8a8bf", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-324", "record_id": "Arizona v. Hicks"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-324", "pinpoint_status": "slip-only", "quote": "and if so whether the plain-view doctrine required probable cause rather than mere reasonable suspicion. ## Rule Moving the equipment to expose hidden information was a new search beyond the entry's justification: the moving of the components", "quote_fidelity": "mismatch", "record_id": "Arizona v. Hicks", "star_marker": null}}
{"assertion_id": "f75b038d4cf08541", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-326", "record_id": "Arizona v. Hicks"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-326", "pinpoint_status": "slip-only", "quote": "We now hold that probable cause is required. To say otherwise would be to cut the 'plain view' doctrine loose from its theoretical and practical moorings.", "quote_fidelity": "mismatch", "record_id": "Arizona v. Hicks", "star_marker": null}}
{"assertion_id": "121d321aa5594e2b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Arizona v. Hicks"}, "payload": {"as_of_content": "1987-03-03", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Arizona v. Hicks", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Arizona v. Hicks

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arizona v. Hicks",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Arizona v. Hicks",
    "case_name_short": "Hicks",
    "case_name_full": "Arizona v. Hicks",
    "input_case_name": "Arizona v. Hicks",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-03-03",
    "year": 1987,
    "docket": null,
    "cluster_id": 111834,
    "lead_opinion_id": 9430865,
    "sibling_ids": [
      111834,
      9430865,
      9430866,
      9430867,
      9430868,
      9430869,
      9430870
    ],
    "absolute_url": "/opinion/111834/arizona-v-hicks/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "480 U.S. 321",
      "volume": "480",
      "reporter": "U.S.",
      "page": "321",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 1149",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1149",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 L. Ed. 2d 347",
        "volume": "94",
        "reporter": "L. Ed. 2d",
        "page": "347",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4258",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4258",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 1056",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "1056",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "480 U.S. 321",
        "volume": "480",
        "reporter": "U.S.",
        "page": "321",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 1149",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1149",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 L. Ed. 2d 347",
        "volume": "94",
        "reporter": "L. Ed. 2d",
        "page": "347",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 1056",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "1056",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4258",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4258",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "480 U.S. 321",
    "official_selection": {
      "court_class": "scotus",
      "selected": "480 U.S. 321",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-324",
      "page": null,
      "quote": "and if so whether the plain-view doctrine required probable cause rather than mere reasonable suspicion. ## Rule Moving the equipment to expose hidden information was a new search beyond the entry's justification: the moving of the components",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-325",
      "page": null,
      "quote": "A search is a search, even if it happens to disclose nothing but the bottom of a turntable.",
      "star_marker": "325",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 7220,
      "fragment": "#:~:text=A%20search%20is%20a%20search%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-326",
      "page": null,
      "quote": "We now hold that probable cause is required. To say otherwise would be to cut the 'plain view' doctrine loose from its theoretical and practical moorings.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-03-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Arizona v. Hicks",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Martin v. State",
          "cluster_id": 10740496,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Bock (A169480)",
          "cluster_id": 10134134,
          "cite": [
            "310 Or. App. 329",
            "485 P.3d 931"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane1_negative"
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
        "journal_ref": "Arizona v. Hicks:lane1_negative"
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
        "journal_ref": "Arizona v. Hicks:lane1_negative"
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
        "journal_ref": "Arizona v. Hicks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Barry Trynell Davis, Jr. v. State of Florida",
          "cluster_id": 4390534,
          "cite": [
            "217 So. 3d 1006",
            "42 Fla. L. Weekly Supp. 558",
            "2017 WL 1954979",
            "2017 Fla. LEXIS 1055"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Kaeppeler",
          "cluster_id": 3166351,
          "cite": [
            "473 Mass. 396",
            "42 N.E.3d 1090"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gamache",
          "cluster_id": 2814721,
          "cite": [
            "792 F.3d 194",
            "2015 U.S. App. LEXIS 11586",
            "2015 WL 4071911"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Telshaw",
          "cluster_id": 2701202,
          "cite": [
            "2011 Ohio 3373",
            "195 Ohio App. 3d 596",
            "961 N.E.2d 223"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane1_negative"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Layne",
          "cluster_id": 118289,
          "cite": [
            "143 L. Ed. 2d 818",
            "119 S. Ct. 1692",
            "526 U.S. 603",
            "1999 U.S. LEXIS 3633"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Dickerson",
          "cluster_id": 112873,
          "cite": [
            "124 L. Ed. 2d 334",
            "113 S. Ct. 2130",
            "508 U.S. 366",
            "1993 U.S. LEXIS 4018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marvin Berkowitz",
          "cluster_id": 557342,
          "cite": [
            "927 F.2d 1376",
            "1991 U.S. App. LEXIS 4135",
            "1991 WL 33079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Grimstead",
          "cluster_id": 1376491,
          "cite": [
            "407 S.E.2d 47",
            "12 Va. App. 1066",
            "8 Va. Law Rep. 449",
            "1991 Va. App. LEXIS 205"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Luis Guzman and Sonia Cruz-Lazo",
          "cluster_id": 516479,
          "cite": [
            "864 F.2d 1512",
            "1988 U.S. App. LEXIS 17681",
            "1988 WL 138644"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zarnow v. CITY OF WICHITA FALLS, TEX.",
          "cluster_id": 152551,
          "cite": [
            "614 F.3d 161",
            "2010 U.S. App. LEXIS 16445",
            "2010 WL 3093443"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bostic",
          "cluster_id": 2542685,
          "cite": [
            "148 P.3d 250",
            "2006 Colo. App. LEXIS 622",
            "2006 WL 1171864"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Clark",
          "cluster_id": 1121458,
          "cite": [
            "857 P.2d 1099",
            "5 Cal. 4th 950",
            "22 Cal. Rptr. 2d 689",
            "93 Daily Journal DAR 11122",
            "93 Cal. Daily Op. Serv. 6528",
            "1993 Cal. LEXIS 4179"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald Tobin, Clifford Roger Ackerson, United States of America v. Ronald Tobin",
          "cluster_id": 554960,
          "cite": [
            "923 F.2d 1506",
            "1991 U.S. App. LEXIS 2683"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jones",
          "cluster_id": 2058953,
          "cite": [
            "830 N.E.2d 541",
            "215 Ill. 2d 261",
            "294 Ill. Dec. 129",
            "2005 Ill. LEXIS 632"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Champion",
          "cluster_id": 2032324,
          "cite": [
            "549 N.W.2d 849",
            "452 Mich. 92"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Bridges",
          "cluster_id": 1060919,
          "cite": [
            "963 S.W.2d 487",
            "1997 Tenn. LEXIS 642",
            "1997 WL 804620"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Flamer v. State",
          "cluster_id": 1486303,
          "cite": [
            "585 A.2d 736",
            "1990 Del. LEXIS 408"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 853051,
          "cite": [
            "783 N.E.2d 1132",
            "2003 WL 734194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111834 OR 9430865 OR 9430866 OR 9430867 OR 9430868 OR 9430869 OR 9430870) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjQ4MTM0NDAwMDAwJnM9MjAxMDQ2MCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111834+OR+9430865+OR+9430866+OR+9430867+OR+9430868+OR+9430869+OR+9430870%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111834 OR 9430865 OR 9430866 OR 9430867 OR 9430868 OR 9430869 OR 9430870)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjgmcz02MDc4ODkmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111834+OR+9430865+OR+9430866+OR+9430867+OR+9430868+OR+9430869+OR+9430870%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111834 OR 9430865 OR 9430866 OR 9430867 OR 9430868 OR 9430869 OR 9430870)",
        "reviewed": 37,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 37,
        "triage_read": 1,
        "triage_snippet_classified": 36
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111834 OR 9430865 OR 9430866 OR 9430867 OR 9430868 OR 9430869 OR 9430870)",
    "indexed_citing_opinions": 951,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111834,
        "count": 821,
        "count_source": "search"
      },
      {
        "opinion_id": 9430865,
        "count": 148,
        "count_source": "search"
      },
      {
        "opinion_id": 9430866,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430867,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430868,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430869,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430870,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1525,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/arizona-v-hicks.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MjQ5Nzkmcz0xMDAzMjc0NSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111834+OR+9430865+OR+9430866+OR+9430867+OR+9430868+OR+9430869+OR+9430870%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111834,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 107898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 111013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 111477,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 111600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 365436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 377016,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 403710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 434694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 1172524,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 1268637,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 1286575,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 1939307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 1978640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 1998068,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 2056305,
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
    "date_created": "2026-07-04T18:25:14Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:25:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:25:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:30:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:25:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Arizona v. Hicks

```
<opinion type="majority">
<author id="b369-7"><page-number citation-index="1" label="323">*323</page-number>Justice Scalia</author>
<p id="ARf">delivered the opinion of the Court.</p>
<p id="b369-8">In <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971), we said that in certain circumstances a warrantless seizure by police of an item that comes within plain view during their lawful search of a private area may be reasonable under the Fourth Amendment. See <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#465" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 465-471</a></span> (plurality opinion); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#505" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 505-506</a></span> (Black, J., concurring and dissenting); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#521" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 521-522</a></span> (White, J., concurring and dissenting). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./475/1107/">475 U. S. 1107</a></span> (1986), in the present case to decide whether this “plain view” doctrine may be invoked when the police have less than probable cause to believe that the item in question is evidence of a crime or is contraband.</p>
<p id="b369-9">HH</p>
<p id="b369-3">On April 18, 1984, a bullet was fired through the floor of respondent’s apartment, striking and injuring a man in the apartment below. Police officers arrived and entered respondent’s apartment to search for the shooter, for other victims, and for weapons. They found and seized three weapons, including a sawed-off rifle, and in the course of their search also discovered a stocking-cap mask.</p>
<p id="b369-4">One of the policemen, Officer Nelson, noticed two sets of expensive stereo components, which seemed out of place in the squalid and otherwise ill-appointed four-room apartment. Suspecting that they were stolen, he read and recorded their serial numbers — moving some of the components, including a Bang and Olufsen turntable, in order to do so — which he then reported by phone to his headquarters. On being advised that the turntable had been taken in an armed robbery, he seized it immediately. It was later determined that some of the other serial numbers matched those on other stereo equipment taken in the same armed robbery, and a warrant <page-number citation-index="1" label="324">*324</page-number>was obtained and executed to seize that equipment as well. Respondent was subsequently indicted for the robbery.</p>
<p id="b370-7">The state trial court granted respondent’s motion to suppress the evidence that had been seized. The Court of Appeals of Arizona affirmed. It was conceded that the initial entry and search, although warrantless, were justified by the exigent circumstance of the shooting. The Court of Appeals viewed the obtaining of the serial numbers, however, as an additional search, unrelated to that exigency. Relying upon a statement in <em>Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385</a></span> (1978), that a “warrantless search must be ‘strictly circumscribed by the exigencies which justify its initiation,”’ <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#393" aria-description="Citation for case: Mincey v. Arizona"><em>id., </em>at 393</a></span> (citation omitted), the Court of Appeals held that the police conduct violated the Fourth Amendment, requiring the evidence derived from that conduct to be excluded. <span class="citation" data-id="1268637"><a href="/opinion/1268637/state-v-hicks/#534" aria-description="Citation for case: State v. Hicks">146 Ariz. 533, 534-535</a></span>, <span class="citation" data-id="1268637"><a href="/opinion/1268637/state-v-hicks/#332" aria-description="Citation for case: State v. Hicks">707 P. 2d 331, 332-333</a></span> (1985). Both courts-the trial court explicitly and the Court of Appeals by necessary implication — rejected the State’s contention that Officer Nelson’s actions were justified under the “plain view” doctrine of <em>Coolidge </em>v. <em>New <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Hampshire, supra.</a></span> </em>The Arizona Supreme Court denied review, and the State filed this petition.</p>
<p id="b370-8">r — 1 h — I</p>
<p id="b370-3">As an initial matter, the State argues that Officer Nelson s actions constituted neither a “search” nor a “seizure” within the meaning of the Fourth Amendment. We agree that the mere recording of the serial numbers did not constitute a seizure. To be sure, that was the first step in a process by which respondent was eventually deprived of the stereo equipment. In and of itself, however, it did not “meaningfully interfere” with respondent’s possessory interest in either the serial numbers or the equipment, and therefore did not amount to a seizure. See <em>Maryland </em>v. <em>Macon, </em><span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/#469" aria-description="Citation for case: Maryland v. MacOn">472 U. S. 463, 469</a></span> (1985).</p>
<p id="b370-4">Officer Nelson’s moving of the equipment, however, did constitute a “search” separate and apart from the search for <page-number citation-index="1" label="325">*325</page-number>the shooter, victims, and weapons that was the lawful objective of his entry into the apartment. Merely inspecting those parts of the turntable that came into view during the latter search would not have constituted an independent search, because it would have produced no additional invasion of respondent’s privacy interest. See <em>Illinois </em>v. <em>Andreas, </em><span class="citation" data-id="9429344"><a href="/opinion/111013/illinois-v-andreas/#771" aria-description="Citation for case: Illinois v. Andreas">463 U. S. 765, 771</a></span> (1983). But taking action, unrelated to the objectives of the authorized intrusion, which exposed to view concealed portions of the apartment or its contents, did produce a new invasion of respondent’s privacy unjustified by the exigent circumstance that validated the entry. This is why, contrary to Justice Powell’s suggestion, <em>post, </em>at 333, the “distinction between ‘looking’ at a suspicious object in plain view and ‘moving’ it even a few inches” is much more than trivial for purposes of the Fourth Amendment. It matters not that the search uncovered nothing of any great personal value to respondent — serial numbers rather than (what might conceivably have been hidden behind or under the equipment) letters or photographs. A search is a search, even if it happens to disclose nothing but the bottom of a turntable.</p>
<p id="b371-5">Ill</p>
<p id="b371-6">The remaining question is whether the search was “reasonable” under the Fourth Amendment.</p>
<p id="b371-7">On this aspect of the case we reject, at the outset, the apparent position of the Arizona Court of Appeals that because the officers’ action directed to the stereo equipment was unrelated to the justification for their entry into respondent’s apartment, it was <em>ipso facto </em>unreasonable. That lack of relationship <em>always </em>exists with regard to action validated under the “plain view” doctrine; where action is taken for the purpose justifying the entry, invocation of the doctrine is superfluous. <em>Mincey </em>v. <em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Arizona, supra,</a></span> </em>in saying that a warrantless search must be “strictly circumscribed by the exigencies which justify its initiation,” <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#393" aria-description="Citation for case: Mincey v. Arizona">437 U. S., at 393</a></span> (citation omitted), was addressing only the scope of the primary <page-number citation-index="1" label="326">*326</page-number>search itself, and was not overruling by implication the many cases acknowledging that the “plain view” doctrine can legitimate action beyond that scope.</p>
<p id="b372-5">We turn, then, to application of the doctrine to the facts of this case. “It is well established that under certain circumstances the police may <em>seize </em>evidence in plain view without a warrant,” <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#465" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 465</a></span> (plurality opinion) (emphasis added). Those circumstances include situations “[w]here the initial intrusion that brings the police within plain view of such [evidence] is supported ... by one of the recognized exceptions to the warrant requirement,” <em>ibid., </em>such as the exigent-circumstances intrusion here. It would be absurd to say that an object could lawfully be seized and taken from the premises, but could not be moved for closer examination. It is clear, therefore, that the search here was valid if the “plain view” doctrine would have sustained a seizure of the equipment.</p>
<p id="b372-6">There is no doubt it would have done so if Officer Nelson had probable cause to believe that the equipment was stolen. The State has conceded, however, that he had only a “reasonable suspicion,” by which it means something less than probable cause. See Brief for Petitioner 18-19.* We have not ruled on the question whether probable cause is required in order to invoke the “plain view” doctrine. Dicta in <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#587" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 587</a></span> (1980), suggested that the standard of probable cause must be met, but our later opinions in <em>Texas </em>v. <em>Brown, </em><span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/" aria-description="Citation for case: Texas v. Brown">460 U. S. 730</a></span> (1983), explicitly regarded the issue as unresolved, see <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#742" aria-description="Citation for case: Texas v. Brown"><em>id., </em>at 742, n. 7</a></span> (plurality opinion); <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#746" aria-description="Citation for case: Texas v. Brown"><em>id., </em>at 746</a></span> (Stevens, J., concurring in judgment).</p>
<p id="b372-7">We now hold that probable cause is required. To say otherwise would be to cut the “plain view” doctrine loose from its theoretical and practical moorings. The theory of that doctrine consists of extending to nonpublic places such as the <page-number citation-index="1" label="327">*327</page-number>home, where searches and seizures without a warrant are presumptively unreasonable, the police’s longstanding authority to make warrantless seizures in public places of such objects as weapons and contraband. See <em>Payton </em>v. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York"><em>New York, supra, </em>at 586-587</a></span>. And the practical justification for that extension is the desirability of sparing police, whose viewing of the object in the course of a lawful search is as legitimate as it would have been in a public place, the inconvenience and the risk — to themselves or to preservation of the evidence — of going to obtain a warrant. See <em>Coolidge </em>v. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#468" aria-description="Citation for case: Coolidge v. New Hampshire"><em>New Hampshire, supra, </em>at 468</a></span> (plurality opinion). Dispensing with the need for a warrant is worlds apart from permitting a lesser standard of <em>cause </em>for the seizure than a warrant would require, <em>i. e., </em>the standard of probable cause. No reason is apparent why an object should routinely be seizable on lesser grounds, during an unrelated search and seizure, than would have been needed to obtain a warrant for that same object if it had been known to be on the premises.</p>
<p id="b373-5">We do not say, of course, that a seizure can never be justified on less than probable cause. We have held that it can— where, for example, the seizure is minimally intrusive and operational necessities render it the only practicable means of detecting certain types of crime. See, <em>e. g., United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">449 U. S. 411</a></span> (1981) (investigative detention of vehicle suspected to be transporting illegal aliens); <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975) (same); <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place">462 U. S. 696, 709</a></span>, and n. 9 (1983) (dictum) (seizure of suspected drug dealer’s luggage at airport to permit exposure to specially trained dog). No special operational necessities are relied on here, however — but rather the mere fact that the items in question came lawfully within the officer’s plain view. That alone cannot supplant the requirement of probable cause.</p>
<p id="b373-6">The same considerations preclude us from holding that, even though probable cause would have been necessary for a <em>seizure, </em>the <em>search </em>of objects in plain view that occurred here <page-number citation-index="1" label="328">*328</page-number>could be sustained on lesser grounds. A dwelling-place search, no less than a dwelling-place seizure, requires probable cause, and there is no reason in theory or practicality why application of the “plain view” doctrine would supplant that requirement. Although the interest protected by the Fourth Amendment injunction against unreasonable searches is quite different from that protected by its injunction against unreasonable seizures, see <em>Texas </em>v. <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#747" aria-description="Citation for case: Texas v. Brown"><em>Brown, supra, </em>at 747-748</a></span> (Stevens, J., concurring in judgment), neither the one nor the other is of inferior worth or necessarily requires only lesser protection. We have not elsewhere drawn a categorical distinction between the two insofar as concerns the degree of justification needed to establish the reasonableness of police action, and we see no reason for a distinction in the particular circumstances before us here. Indeed, to treat searches more liberally would especially erode the plurality’s warning in <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>that “the ‘plain view’ doctrine may not be used to extend a general exploratory search from one object to another until something incriminating at last emerges.” <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#466" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 466</a></span>. In short, whether legal authority to move the equipment could be found only as an inevitable concomitant of the authority to seize it, or also as a consequence of some independent power to search certain objects in plain view, probable cause to believe the equipment was stolen was required.</p>
<footnote label="*">
<p id="b372-8">Contrary to the suggestion in Justice O’Connor’s dissent, <em>post, </em>at 339, this concession precludes our considering whether the probable-cause standard was satisfied in this case.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Austin v. United States.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Austin v. United States
type: case
citation: "509 U.S. 602 (1993)"
parallel_cite: "113 S. Ct. 2801; 125 L. Ed. 2d 488"
neutral_cite: "1993 U.S. LEXIS 4407; 1993 WL 224465"
court: U.S.
court_level: scotus
circuit: ""
year: 1993
date_decided: 1993-06-28
docket: 92-6073
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
  opinion_url: "https://www.courtlistener.com/opinion/112904/austin-v-united-states/"
  cluster_id: 112904
  opinion_id: 9432892
  identity_checked: true
lake:
  record_id: Austin v. United States
  status: under_review
  projected_at: 2026-07-09
homes:
  - page: "[[Civil Asset Forfeiture]]"
    role: Anchor
related:
  - "[[Civil Asset Forfeiture]]"
  - "[[United States v. Bajakajian]]"
  - "[[Timbs v. Indiana]]"
tags:
  - case
  - eighth-amendment
  - excessive-fines
  - civil-forfeiture
  - in-rem
  - punishment
holding: "Because in rem civil forfeiture of property used to facilitate drug offenses under 21 U.S.C. §§ 881(a)(4) and (a)(7) serves at least in part to punish, it constitutes 'payment to a sovereign as punishment for some offense' and is therefore subject to the Eighth Amendment's Excessive Fines Clause."
aliases:
  - Austin v. United States
  - "Austin v. United States (1993)"
---

# Austin v. United States

*509 U.S. 602 (1993)* (No. 92-6073) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 112904 → combined opinion 112904 (Blackmun, J.; 509 U.S. 602, decided June 28, 1993). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*622`). S9 promotes. -->

## Background
Richard Lyle Austin pleaded guilty in South Dakota state court to one count of possessing cocaine with intent to distribute, arising out of a small drug sale he made from his auto body shop. After his state conviction, the federal government brought an *in rem* civil forfeiture action under 21 U.S.C. §§ 881(a)(4) and (a)(7) against Austin's mobile home and auto body shop, on the theory that the properties had been used to facilitate the drug offense. The District Court and the Eighth Circuit ordered forfeiture, rejecting Austin's argument that taking his home and business was so disproportionate to his offense that it violated the Eighth Amendment's Excessive Fines Clause — reasoning that the Clause did not reach civil, *in rem* forfeitures at all.

## Issue
Whether the Excessive Fines Clause of the Eighth Amendment applies to *in rem* civil forfeitures of property used to facilitate a drug offense.

## Rule
The Court rejected the premise that a forfeiture escapes the Eighth Amendment merely because it is labeled "civil" and proceeds against the property rather than the owner. What matters is whether the sanction serves, even in part, to punish. Because the historical understanding of forfeiture, the statute's focus on the owner's culpability, and Congress's stated deterrent aims all showed these forfeitures to be at least partly punitive, the Court held: "We therefore conclude that forfeiture under these provisions constitutes 'payment to a sovereign as punishment for some offense,' ... and, as such, is subject to the limitations of the Eighth Amendment's Excessive Fines Clause." — 509 U.S. at 622. ^pin-622

## Application
Sections 881(a)(4) and (a)(7) tie forfeiture to the property's role in a crime and exempt "innocent owners" — features that make sense only if the statute aims to punish culpable owners, not merely to remove dangerous items from circulation. The Government's "remedial" characterizations (removing instrumentalities, recouping enforcement costs) could not explain a sanction whose value bears no fixed relation to any harm or cost. Having established that the Clause applies, the Court declined Austin's invitation to announce a test for when a forfeiture is constitutionally "excessive," leaving that question for the lower courts [[Reading and Citing Cases#on-remand|on remand]].

## Conclusion
The judgment was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]] for consideration of excessiveness. Blackmun, J., delivered the opinion of the Court; Scalia, J., and Kennedy, J. (joined by Rehnquist, C.J., and Thomas, J.), concurred in part and in the judgment.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Austin* is the anchor for subjecting civil forfeiture to the Excessive Fines Clause. It left the excessiveness *standard* open; the Court supplied it five years later in *[[United States v. Bajakajian]]* (1998) (a fine is unconstitutional if grossly disproportional to the offense), and it applied the Clause against the States through the Fourteenth Amendment in *[[Timbs v. Indiana]]* (2019). Teach *Austin* as step one — the Clause *applies* — and *[[United States v. Bajakajian|Bajakajian]]*/*[[Timbs v. Indiana|Timbs]]* as the standard and its reach.

## Appears on
- [[Civil Asset Forfeiture]] — *Anchor*

## Sources
- [*Austin v. United States*, 509 U.S. 602 (1993)](https://www.courtlistener.com/opinion/112904/austin-v-united-states/) — pinpoint: 622 (Blackmun, J., for the Court; the CL opinion text carries the reporter star `*622` immediately before the holding). Rule quote string-matched to the CL opinion text 2026-07-07 (internal citation to *Browning-Ferris* elided).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "48e3fa3e63e40127", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Austin v. United States"}, "payload": {"all": [{"cite": "509 U.S. 602", "page": "602", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "509"}, {"cite": "113 S. Ct. 2801", "page": "2801", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "113"}, {"cite": "125 L. Ed. 2d 488", "page": "488", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "125"}, {"cite": "1993 U.S. LEXIS 4407", "page": "4407", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1993"}, {"cite": "1993 WL 224465", "page": "224465", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "1993"}], "display": "509 U.S. 602", "official": {"cite": "509 U.S. 602", "page": "602", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "509"}, "official_selection_present": true, "record_id": "Austin v. United States"}}
{"assertion_id": "0d5b3f54c58eba8f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Austin v. United States"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Austin v. United States", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Austin v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Austin v. United States",
  "status": "under_review",
  "identity": {
    "case_name": "Austin v. United States",
    "case_name_short": "Austin",
    "case_name_full": "Austin v. United States",
    "input_case_name": "Austin v. United States",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1993-06-28",
    "year": 1993,
    "docket": "92-6073",
    "cluster_id": 112904,
    "lead_opinion_id": 9432892,
    "sibling_ids": [],
    "absolute_url": "/opinion/112904/austin-v-united-states/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "509 U.S. 602",
      "volume": "509",
      "reporter": "U.S.",
      "page": "602",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "113 S. Ct. 2801",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "2801",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "125 L. Ed. 2d 488",
        "volume": "125",
        "reporter": "L. Ed. 2d",
        "page": "488",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1993 U.S. LEXIS 4407",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "4407",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 WL 224465",
        "volume": "1993",
        "reporter": "WL",
        "page": "224465",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "509 U.S. 602",
        "volume": "509",
        "reporter": "U.S.",
        "page": "602",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 S. Ct. 2801",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "2801",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "125 L. Ed. 2d 488",
        "volume": "125",
        "reporter": "L. Ed. 2d",
        "page": "488",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 U.S. LEXIS 4407",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "4407",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 WL 224465",
        "volume": "1993",
        "reporter": "WL",
        "page": "224465",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "509 U.S. 602",
    "official_selection": {
      "court_class": "scotus",
      "selected": "509 U.S. 602",
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
    "date_created": "2026-07-07T13:22:16Z",
    "date_modified": "2026-07-09T23:29:56Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:22:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:22:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:22:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:22:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "austin-v-united-states--112904",
      "to_record_id": "Austin v. United States",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Austin v. United States

```
<opinion type="majority">
<author id="b646-4"><page-number citation-index="1" label="604">*604</page-number>Justice Blackmun</author>
<p id="AVJ">delivered the opinion of the Court.</p>
<p id="b646-5">In this case, we are asked to decide whether the Excessive Fines Clause of the Eighth Amendment applies to forfeitures of property under <span class="citation no-link">21 U. S. C. §§ 881</span>(a)(4) and (a)(7). We hold that it does and therefore remand the case for consideration of the question whether the forfeiture at issue here was excessive.</p>
<p id="b646-6">I</p>
<p id="b646-7">On August 2,1990, petitioner Richard Lyle Austin was indicted on four counts of violating South Dakota’s drug laws. Austin ultimately pleaded guilty to one count of possessing cocaine with intent to distribute and was sentenced by the state court to seven years’ imprisonment. On September 7, the United States filed an <em>in rem </em>action in the United States District Court for the District of South Dakota seeking forfeiture of Austin’s mobile home and auto body shop under <span class="citation no-link">21 <page-number citation-index="1" label="605">*605</page-number>U. S. C. §§ 881</span>(a)(4) and (a)(7).<footnotemark>1</footnotemark> Austin filed a claim and an answer to the complaint.</p>
<p id="b647-5">On February 4, 1991, the United States made a motion, supported by an affidavit from Sioux Falls Police Officer Donald Satterlee, for summary judgment. According to Satterlee’s affidavit, Austin met Keith Engebretson at Austin’s body shop on June 13, 1990, and agreed to sell cocaine to Engebretson. Austin left the shop, went to his mobile home, and returned to the shop with two grams of cocaine which he sold to Engebretson. State authorities executed a search warrant on the body shop and mobile home the following day. They discovered small amounts of marijuana and cocaine, a .22 caliber revolver, drug paraphernalia, and approximately $4,700 in cash. App. 13. In opposing summary judgment, Austin argued that forfeiture of the properties would violate the Eighth Amendment.<footnotemark>2</footnotemark> The District Court rejected this argument and entered summary judgment for the United States. <span class="citation no-link"><em>Id., </em>at 19</span>.</p>
<p id="b647-6">The United States Court of Appeals for the Eighth Circuit “reluctantly agree[d] with the government” and affirmed. <page-number citation-index="1" label="606">*606</page-number><em>United States </em>v. <em>One Parcel of Property, </em><span class="citation multiple-matches"><a href="/c/F.%202d/964/814/">964 F. 2d 814</a></span>, 817 (1992). Although it thought that “the principle of proportionality should be applied in civil actions that result in harsh penalties,” <em>ibid., </em>and that the Government was “exacting too high a penalty in relation to the offense committed,” <em>id., </em>at 818, the court felt constrained from holding the forfeiture unconstitutional. It cited this Court’s decision in <em>CaleroToledo </em>v. <em>Pearson Yacht Leasing Co., </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S. 663</a></span> (1974), for the proposition that, when the Government is proceeding against property <em>in rem, </em>the guilt or innocence of the property’s owner “is constitutionally irrelevant.” 964 F. 2d, at 817. It then reasoned: “We are constrained to agree with the Ninth Circuit that ‘[i]f the constitution allows <em>in rem </em>forfeiture to be visited upon innocent owners . . . the constitution hardly requires proportionality review of forfeitures.’” <em>Ibid., </em>quoting <em>United States </em>v. <em>Tax Lot 1500, </em><span class="citation" data-id="8965274"><a href="/opinion/8973657/united-states-v-tax-lot-1500/#234" aria-description="Citation for case: United States v. Tax Lot 1500">861 F. 2d 232, 234</a></span> (CA9 1988), cert. denied <em>sub nom. Jaffee </em>v. <em>United States, </em><span class="citation" data-id="9086527"><a href="/opinion/9092333/jaffee-v-united-states/" aria-description="Citation for case: Jaffee v. United States">493 U. S. 954</a></span> (1989).</p>
<p id="b648-5">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./506/1074/">506 U. S. 1074</a></span> (1993), to resolve an apparent conflict with the Court of Appeals for the Second Circuit over the applicability of the Eighth Amendment to <em>in rem </em>civil forfeitures. See <em>United States </em>v. <em>Certain Real Property, </em><span class="citation" data-id="576216"><a href="/opinion/576216/united-states-v-certain-real-property-and-premises-known-as-38-whalers/#35" aria-description="Citation for case: United States v. Certain Real Property and Premises Known...">954 F. 2d 29, 35, 38-39</a></span>, cert. denied <em>sub nom. Levin </em>v. <em>United States, </em><span class="citation" data-id="9118128"><a href="/opinion/9123561/levin-v-united-states/" aria-description="Citation for case: Levin v. United States">506 U. S. 815</a></span> (1992).</p>
<p id="b648-6">II</p>
<p id="b648-7">Austin contends that the Eighth Amendment’s Excessive Fines Clause applies to <em>in rem </em>civil forfeiture proceedings. See Brief for Petitioner 10,19, 23. We have had occasion to consider this Clause only once before. In <em>Browning-Ferris Industries of Vt., Inc. </em>v. <em>Kelco Disposal, Inc., </em><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U. S. 257</a></span> (1989), we held that the Excessive Fines Clause does not limit the award of punitive damages to a private party in a civil suit when the government neither has prosecuted the action nor has any right to receive a share of the damages. <span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/#264" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco..."><em>Id., </em>at 264</a></span>. The Court’s opinion and Justice O’Connor’s <page-number citation-index="1" label="607">*607</page-number>opinion, concurring in part and dissenting in part, reviewed in some detail the history of the Excessive Fines Clause. See <span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/#264" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco..."><em>id., </em>at 264-268,286-297</a></span>. The Court concluded that both the Eighth Amendment and § 10 of the English Bill of Rights of 1689, from which it derives, were intended to prevent <em>the government </em>from abusing its power to punish, see <em>id., </em>at 266-267, and therefore that “the Excessive Fines Clause was intended to limit only those fines directly imposed by, and payable to, the government,” <em>id., </em>at 268.<footnotemark>3</footnotemark></p>
<p id="b649-5">We found it unnecessary to decide in <em>Browning-Ferris </em>whether the Excessive Fines Clause applies only to criminal cases. <em>Id., </em>at 263. The United States now argues that</p>
<blockquote id="b649-6">“any claim that the government’s conduct in a civil proceeding is limited by the Eighth Amendment generally, or by the Excessive Fines Clause in particular, must fail unless the challenged governmental action, despite its label, would have been recognized as a <em>criminal </em>punishment at the time the Eighth Amendment was adopted.” Brief for United States 16 (emphasis added).</blockquote>
<p id="b649-7">It further suggests that the Eighth Amendment cannot apply to a civil proceeding unless that proceeding is so punitive that it must be considered criminal under <em>Kennedy </em>v. <em>Mendoza-Martinez, </em><span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/" aria-description="Citation for case: Kennedy v. Mendoza-Martinez">372 U. S. 144</a></span> (1963), and <em>United States </em>v. <em>Ward, </em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/" aria-description="Citation for case: United States v. Ward">448 U. S. 242</a></span> (1980). Brief for United States 26-27. We disagree.</p>
<p id="b649-8">Some provisions of the Bill of Rights are expressly limited to criminal cases. The Fifth Amendment’s Self-Incrimination Clause, for example, provides: “No person ... shall be compelled in any criminal case to be a witness <page-number citation-index="1" label="608">*608</page-number>against himself.” The protections provided by the Sixth Amendment are explicitly confined to “criminal prosecutions.” See generally <em>Ward, </em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/#248" aria-description="Citation for case: United States v. Ward">448 U. S., at 248</a></span>.<footnotemark>4</footnotemark> The text of the Eighth Amendment includes no similar limitation. See n. <em>2, supra.</em></p>
<p id="b650-5">Nor does the history of the Eighth Amendment require such a limitation. Justice O’Connor noted in <em>Browning-Ferris: </em>“Consideration of the Eighth Amendment immediately followed consideration of the Fifth Amendment. <page-number citation-index="1" label="609">*609</page-number>After deciding to confine the benefits of the Self-Inerimination Clause of the Fifth Amendment to criminal proceedings, the Framers turned their attention to the Eighth Amendment. There were no proposals to limit that Amendment to criminal proceedings ....” <span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/#294" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U. S., at 294</a></span>. Section 10 of the English Bill of Rights of 1689 is not expressly limited to criminal cases either. The original draft of § 10 as introduced in the House of Commons did contain such a restriction, but only with respect to the bail clause: “The requiring excessive Bail of Persons committed in criminal Cases, and imposing excessive Fines, and illegal Punishments, to be prevented.” 10 H. C. Jour. 17 (1688). The absence of any similar restriction in the other two clauses suggests that they were not limited to criminal cases. In the final version, even the reference to criminal cases in the bail clause was omitted. See 1 W. &amp; M., 2d Sess., ch. 2, 3 Stat. at Large 441 (1689) (“That excessive Bail ought not to be required, nor excessive Fines imposed; nor cruel and unusual Punishments inflicted”); see also L. Schwoerer, The Declaration of Rights, 1689, p. 88 (1981) (“But article 10 contains no reference to ‘criminal cases’ and, thus, would seem to apply ... to all cases”).<footnotemark>5</footnotemark></p>
<p id="b651-5">The purpose of the Eighth Amendment, putting the Bail Clause to one side, was to limit the government’s power to punish. See <em>Browning-Ferris, </em><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/#266" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U. S., at 266-267, 275</a></span>. The Cruel and Unusual Punishments Clause is self-evidently concerned with punishment. The Excessive Fines Clause limits the government’s power to extract payments, whether <page-number citation-index="1" label="610">*610</page-number>in cash or in kind, “as <em>punishment </em>for some offense.” <em>Id.¡ </em>at 265 (emphasis added). “The notion of punishment, as we commonly understand it, cuts across the division between the civil and the criminal law.” <em>United States </em>v. <em>Halper, </em><span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/#447" aria-description="Citation for case: United States v. Halper">490 U. S. 435, 447-448</a></span> (1989). “It is commonly understood that civil proceedings may advance punitive as well as remedial goals, and, conversely, that both punitive and remedial goals may be served by criminal penalties.” <span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/#447" aria-description="Citation for case: United States v. Halper"><em>Id., </em>at 447</a></span>. See also <em>United States ex rel. Marcus </em>v. <em>Hess, </em><span class="citation" data-id="9419289"><a href="/opinion/103757/united-states-ex-rel-marcus-v-hess/#554" aria-description="Citation for case: United States Ex Rel. Marcus v. Hess">317 U. S. 537, 554</a></span> (1943) (Frankfurter, J., concurring). Thus, the question is not, as the United States would have it, whether forfeiture under §§ 881(a)(4) and (a)(7) is civil or criminal, but rather whether it is punishment.<footnotemark>6</footnotemark></p>
<p id="b652-5">In considering this question, we are mindful of the fact that sanctions frequently serve more than one purpose. We need not exclude the possibility that a forfeiture serves remedial purposes to conclude that it is subject to the limitations of the Excessive Fines Clause. We, however, must determine that it can only be explained as serving in part to punish. We said in <em><span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/" aria-description="Citation for case: United States v. Halper">Halper</a></span> </em>that “a civil sanction that cannot fairly be said solely to serve a remedial purpose, but rather can only be explained as also serving either retributive or deterrent purposes, is punishment, as we have come to understand the term.” <span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/#448" aria-description="Citation for case: United States v. Halper">490 U. S., at 448</a></span>. We turn, then, to consider whether, at the time the Eighth Amendment was ratified, forfeiture was understood at least in part as punish<page-number citation-index="1" label="611">*611</page-number>ment and whether forfeiture under §§ 881(a)(4) and (a)(7) should be so understood today.</p>
<p id="b653-5">Ill</p>
<p id="b653-6">A</p>
<p id="b653-7">Three kinds of forfeiture were established in England at the time the Eighth Amendment was ratified in the United States: deodand, forfeiture upon conviction for a felony or treason, and statutory forfeiture. See <em>Calero-Toledo, </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#680" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 680-683</a></span>. Each was understood, at least in part, as imposing punishment.</p>
<blockquote id="b653-8">“At common law the value of an inanimate object directly or indirectly causing the accidental death of a King’s subject was forfeited to the Crown as a deodand. The origins of the deodand are traceable to Biblical and pre-Judeo-Christian practices, which reflected the view that the instrument of death was accused and that religious expiation was required. See O. Holmes, The Common Law, c. 1 (1881). The value of the instrument was forfeited to the King, in the belief that the King would provide the money for Masses to be said for the good of the dead man’s soul, or insure that the deodand was put to charitable uses. 1 W. Blackstone, Commentaries *300. When application of the deodand to religious or eleemosynary purposes ceased, and the deodand became a source of Crown revenue, the institution was justified as a penalty for carelessness.” <span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#680" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co."><em>Id., </em>at 680-681</a></span> (footnotes omitted).</blockquote>
<p id="b653-9">As Blackstone put it, “such misfortunes are in part owing to the negligence of the owner, and therefore he is properly punished by such forfeiture.” 1 W. Blackstone, Commentaries *301.</p>
<p id="b653-10">The second kind of common-law forfeiture fell only upon those convicted of a felony or of treason. “The convicted felon forfeited his chattels to the Crown and his lands es-<page-number citation-index="1" label="612">*612</page-number>cheated to his lord; the convicted traitor forfeited all of his property, real and personal, to the Crown.” <em>Calero-Toledo, </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#682" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 682</a></span>. Such forfeitures were known as forfeitures of estate. See 4 W. Blackstone, at *381. These forfeitures obviously served to punish felons and traitors, see <em>The Palmyra, </em><span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/#14" aria-description="Citation for case: The Palmyra">12 Wheat. 1, 14</a></span> (1827), and were justified on the ground that property was a right derived from society which one lost by violating society’s laws, see 1 W. Blackstone, at *299; 4 <em>id., </em>at *382.</p>
<p id="b654-5">Third, “English Law provided for statutory forfeitures of offending objects used in violation of the customs and revenue laws.” <em>Calero-Toledo, </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#682" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 682</a></span>. The most notable of these were the Navigation Acts of 1660 that required the shipping of most commodities in English vessels. Violations of the Acts resulted in the forfeiture of the illegally carried goods as well as the ship that transported them. See generally L. Harper, English Navigation Laws (1939). The statute was construed so that the act of an individual seaman, undertaken without the knowledge of the master or owner, could result in forfeiture of the entire ship. See <em>Mitchell </em>v. <em>Torup, </em>Park. 227, 145 Eng. Rep. 764 (Ex. 1766). Yet Blackstone considered such forfeiture statutes “penal.” 3 W. Blackstone, at *261.</p>
<p id="b654-6">In <em>Calero-Toledo, </em>we observed that statutory forfeitures were “likely a product of the confluence and merger of the deodand tradition and the belief that the right to own property could be denied the wrongdoer.” <span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#682" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 682</a></span>. Since each of these traditions had a punitive aspect, it is not surprising that forfeiture under the Navigation Acts was justified as a penalty for negligence: “But the Owners of Ships are to take Care what Master they employ, and the Master what Mariners; and here Negligence is plainly imputable to the Master; for he is to report the Cargo of the Ship, and if he had searched and examined the Ship with proper care, according to his Duty, he would have found the Tea . . . and <page-number citation-index="1" label="613">*613</page-number>so might have prevented the Forfeiture.” <em>Mitchell, </em>Park., at 238, 145 Eng. Rep., at 768.</p>
<p id="b655-5">B</p>
<p id="b655-6">Of England’s three kinds of forfeiture, only the third took hold in the United States. “Deodands did not become part of the common-law tradition of this country.” <em>CaleroToledo, </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#682" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 682</a></span>. The Constitution forbids forfeiture of estate as a punishment for treason “except during the Life of the Person attainted,” U. S. Const., Art. III, § 3, cl. 2, and the First Congress also abolished forfeiture of estate as a punishment for felons. Act of Apr. 30, 1790, ch. 9, §24, <span class="citation no-link">1 Stat. 117</span>. “But ‘[l]ong before the adoption of the Constitution the common law courts in the Colonies — and later in the states during the period of Confederation — were exercising jurisdiction <em>in rem </em>in the enforcement of [English and local] forfeiture statutes.’ ” <em>Calero-Toledo, </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#683" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 683</a></span>, quoting C. <em>J. Hendry Co. </em>v. <em>Moore, </em><span class="citation" data-id="9419300"><a href="/opinion/103775/c-j-hendry-co-v-moore/#139" aria-description="Citation for case: C. J. Hendry Co. v. Moore">318 U. S. 133, 139</a></span> (1943).</p>
<p id="b655-7">The First Congress passed laws subjecting ships and car-gos involved in customs offenses to forfeiture. It does not follow from that fact, however, that the First Congress thought such forfeitures to be beyond the purview of the Eighth Amendment. Indeed, examination of those laws suggests that the First Congress viewed forfeiture as punishment. For example, by the Act of July 31, 1789, ch. 5, § 12, <span class="citation no-link">1 Stat. 39</span>, Congress provided that goods could not be unloaded except during the day and with a permit.</p>
<blockquote id="b655-8">“[A]nd if the master or commander of any ship or vessel shall suffer or permit the same, such master and commander, and every other person who shall be aiding or assisting in landing, removing, housing, or otherwise securing the same, shall forfeit and pay the sum of four hundred dollars for every offence; shall moreover be disabled from holding any office of trust or profit under the United States, for a term not exceeding seven years; and it shall be the duty of the collector of the district, to <page-number citation-index="1" label="614">*614</page-number>advertise the names of all such persons in the public gazette of the State in which he resides, within twenty-days after each respective conviction. And all goods, wares and merchandise, so landed or discharged, shall become forfeited, and may be seized by any officer of the customs; and where the value thereof shall amount to four hundred dollars, the vessel, tackle, apparel and furniture, shall be subject to like forfeiture and seizure.”</blockquote>
<p id="b656-5">Forfeiture of the goods and vessel is listed alongside the other provisions for punishment. It is also of some interest that “forfeit” is the word Congress used for fine. See <em><span class="citation no-link">ibid.</span> </em>(“shall forfeit and pay the sum of four hundred dollars for every offence”).<footnotemark>7</footnotemark> Other early forfeiture statutes follow the same pattern. See, <em>e. g., </em>Act of Aug. 4, 1790, ch. 34, §§ 13, 22, 27, 28, <span class="citation no-link">1 Stat. 157</span>, 161, 163.</p>
<p id="b656-6">C</p>
<p id="b656-7">Our cases also have recognized that statutory <em>in rem </em>forfeiture imposes punishment. In <em>Peisch </em>v. <span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C."><em>Ware, 4 </em>Cranch 347</a></span> (1808), for example, the Court held that goods removed from the custody of a revenue officer without the payment of duties should not be forfeitable for that reason unless they were removed with the consent of the owner or his agent. Chief Justice Marshall delivered the opinion for a unanimous Court:</p>
<blockquote id="b656-8">“The court is also of opinion that the removal for which the act punishes the owner with a forfeiture of <page-number citation-index="1" label="615">*615</page-number>the goods must be made with his consent or connivance, or with that of some person employed or trusted by him. If, by private theft, or open robbery, without any fault on his part, his property should be invaded, while in the custody of the officer of the revenue, the law cannot be understood to punish him with the forfeiture of that property.” <span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/#364" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C."><em>Id., </em>at 364</a></span>.<footnotemark>8</footnotemark></blockquote>
<p id="b657-5">The same understanding of forfeiture as punishment runs through our cases rejecting the “innocence” of the owner as a common-law defense to forfeiture. See, <em>e. g., Calero-Toledo, </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#683" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 683</a></span>; <em>J. W. Goldsmith, Jr.-Grant Co. </em>v. <em>United States, </em><span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States">254 U. S. 505</a></span> (1921); <em>Dobbins’s Distillery </em>v. <em>United States, </em><span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">96 U. S. 395</a></span> (1878); <em>Harmony </em>v. <em>United States, </em><span class="citation" data-id="86274"><a href="/opinion/86274/united-states-v-brig-malek-adhel/" aria-description="Citation for case: United States v. Brig Malek Adhel">2 How. 210</a></span> (1844); <em>The Palmyra, </em><span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/" aria-description="Citation for case: The Palmyra">12 Wheat. 1</a></span> (1827). In these cases, forfeiture has been justified on two theories — that the property itself is “guilty” of the offense, and that the owner may_ be held accountable for the wrongs of others to whom he entrusts his property. Both theories rest, at bottom, on the notion that the owner has been negligent in allowing his property to be misused and that he is properly punished for that negligence.</p>
<p id="b657-6">The fiction that “the thing is primarily considered the offender,” <em>Goldsmith-Grant Co., </em><span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#511" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States">254 U. S., at 511</a></span>, has a venerable history in our case law.<footnotemark>9</footnotemark> See <em>The Palmyra, </em><span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/#14" aria-description="Citation for case: The Palmyra">12 Wheat., <page-number citation-index="1" label="616">*616</page-number>at 14</a></span> (“The thing is here primarily considered as the offender, or rather the offence is attached primarily to the thing”); <em>Harmony, </em><span class="citation" data-id="86274"><a href="/opinion/86274/united-states-v-brig-malek-adhel/#233" aria-description="Citation for case: United States v. Brig Malek Adhel">2 How., at 233</a></span> (“The vessel which commits the aggression is treated as the offender, as the guilty instrument or thing to which the forfeiture attaches, without any reference whatsoever to the character or conduct of the owner”); <em>Dobbins’s Distillery, </em><span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/#401" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">96 U. S., at 401</a></span> (“[T]he offence ... is attached primarily to the distillery, and the real and personal property used in connection with the same, without any regard whatsoever to the personal misconduct or responsibility of the owner”). Yet the Court has understood this fiction to rest on the notion that the owner who allows his property to become involved in an offense has been negligent. Thus, in <em>Goldsmith-Grant Co., </em>the Court said that “ascribing to the property a certain personality, a power of complicity and guilt in the wrong,” had “some analogy to the law of <span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#510" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States"><em>deodand.” 254 </em>U. S., at 510</a></span>. It then quoted Blackstone’s explanation of the reason for deodand: that “‘such misfortunes are in part owing to the negligence of the owner, and therefore he is properly punished by such forfeiture.’” <span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#510" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States"><em>Id., </em>at 510-511</a></span>, quoting 1 W. Blackstone, at *301.</p>
<p id="b658-5">In none of these cases did the Court apply the guilty-property fiction to justify forfeiture when the owner had done all that reasonably could be expected to prevent the unlawful use of his property. In <em><span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/" aria-description="Citation for case: The Palmyra">The Palmyra</a></span>, </em>it did no more than reject the argument that the criminal conviction of the owner was a prerequisite to the forfeiture of his property. See <span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/#15" aria-description="Citation for case: The Palmyra">12 Wheat., at 15</a></span> (“[N]o personal conviction of the offender is necessary to enforce a forfeiture <em>in rem </em>in cases of this nature”). In <em>Harmony, </em>the owners’ claim of “innocence” was limited to the fact that they “never contemplated <page-number citation-index="1" label="617">*617</page-number>or authorized the acts complained of.” <span class="citation" data-id="86274"><a href="/opinion/86274/united-states-v-brig-malek-adhel/#230" aria-description="Citation for case: United States v. Brig Malek Adhel">2 How., at 230</a></span>. And in <em><span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">Dobbins’s Distillery</a></span>, </em>the Court noted that some responsibility on the part of the owner arose “from the fact that he leased the property to the distiller, and suffered it to be occupied and used by the lessee as a distillery.” <span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/#401" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">96 U. S., at 401</a></span>. The more recent cases have expressly reserved the question whether the fiction could be employed to forfeit the property of a truly innocent owner. See, <em>e. g., Goldsmith-Grant Co., </em><span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#512" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States">254 U. S., at 512</a></span>; <em>Calero-Toledo, </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#689" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 689-690</a></span> (noting that forfeiture of a truly innocent owner’s property would raise “serious constitutional questions”).<footnotemark>10</footnotemark> If forfeiture had been understood not to punish the owner, there would have been no reason to reserve the case of a truly innocent owner. Indeed, it is only on the assumption that forfeiture serves in part to punish that the Court’s past reservation of that question makes sense.</p>
<p id="b659-5">The second theory on which the Court has justified the forfeiture of an “innocent” owner’s property is that the owner may be held accountable for the wrongs of others to whom he entrusts his property. In <em>Harmony, </em>it reasoned that “the acts of the master and crew, in cases of this sort, bind the interest of the owner of the ship, whether he be innocent or guilty; and he impliedly submits to whatever the law denounces as a forfeiture attached to the ship by reason of their unlawful or wanton wrongs.” <span class="citation" data-id="86274"><a href="/opinion/86274/united-states-v-brig-malek-adhel/#234" aria-description="Citation for case: United States v. Brig Malek Adhel">2 How., at 234</a></span>. It repeated this reasoning in <em><span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">Dobbins’s Distillery</a></span>:</em></p>
<blockquote id="b659-6">“[T]he unlawful acts of the distiller bind the owner of the property, in respect to the management of the same, as much as if they were committed by the owner himself. Power to that effect the law vests in him by virtue of his lease; and, if he abuses his trust, it is a matter to be settled between him and his lessor; but the acts of viola<page-number citation-index="1" label="618">*618</page-number>tion as to the penal consequences to the property are to be considered just the same as if they were the acts of the owner.” <span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/#404" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">96 U. S., at 404</a></span>.</blockquote>
<p id="b660-5">Like the guilty-property fiction, this theory of vicarious liability is premised on the idea that the owner has been negligent. Thus, in <em>Calero-Toledo, </em>we noted that application of forfeiture provisions “to lessors, bailors, or secured creditors who are innocent of any wrongdoing ... may have the desirable effect of inducing them to exercise greater care in transferring possession of their property.” <span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#688" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 688</a></span>.<footnotemark>11</footnotemark></p>
<p id="b660-6">In sum, even though this Court has rejected the “innocence” of the owner as a common-law defense to forfeiture, it consistently has recognized that forfeiture serves, at least in part, to punish the owner. See <em>Peisch </em>v. <span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/#364" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C."><em>Ware, 4 </em>Cranch, at 364</a></span> (“[T]he act punishes the owner with a forfeiture of the goods”); <em>Dobbins’s Distillery, </em><span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/#404" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">96 U. S., at 404</a></span> (“[T]he acts of violation as to the penal consequences to the property are to be considered just the same as if they were the acts of the owner”); <em>Goldsmith-Grant Co., </em><span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#511" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States">254 U. S., at 511</a></span> (“'[S]uch misfortunes are in part owing to the negligence of the owner, and therefore he is properly punished by such forfeiture’ ”). More recently, we have noted that forfeiture serves “punitive and deterrent purposes,” <em>Calero-Toledo, </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#686" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 686</a></span>, and “impos[es] an economic penalty,” <span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#687" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co."><em>id., </em>at 687</a></span>. We conclude, therefore, that forfeiture generally and statutory <em>in rem </em>forfeiture in particular historically have been understood, at least in part, as punishment.<footnotemark>12</footnotemark></p>
<p id="b661-4"><page-number citation-index="1" label="619">*619</page-number>IV</p>
<p id="b661-5">We turn next to consider whether forfeitures under <span class="citation no-link">21 U. S. C. §§ 881</span>(a)(4) and (a)(7) are properly considered punishment today. We find nothing in these provisions or their legislative history to contradict the historical understanding of forfeiture as punishment. Unlike traditional forfeiture statutes, §§ 881(a)(4) and (a)(7) expressly provide an “innocent owner” defense. See § 881(a)(4)(C) (“[N]o conveyance shall be forfeited under this paragraph to the extent of an interest of an owner, by reason of any act or omission established by that owner to have been committed or omitted without the knowledge, consent, or willful blindness of the owner”); § 881(a)(7) (“[N]o property shall be forfeited under this paragraph, to the extent of an interest of an owner, by reason of any act or omission established by that owner to have been committed or omitted without the knowledge or consent of that owner”); see also <em>United States </em>v. <em>Parcel of Rumson, N. J., Land, </em><span class="citation" data-id="9432740"><a href="/opinion/112823/united-states-v-parcel-of-rumson-nj-land/#122" aria-description="Citation for case: United States v. Parcel of Rumson, NJ, Land">507 U. S. 111, 122-123</a></span> (1993) (plurality opinion) (noting difference from traditional forfeiture statutes). These exemptions serve to focus the provisions on the culpability of the owner in a way that makes them look more like punishment, not less. In <em>United States </em>v. <em>United States Coin &amp; Currency, </em><span class="citation" data-id="9424510"><a href="/opinion/108303/united-states-v-united-states-coin-currency/" aria-description="Citation for case: United States v. United States Coin &amp; Currency">401 U. S. 715</a></span> (1971), we reasoned that <span class="citation no-link">19 U. S. C. § 1618</span>, which provides that the Secretary of the Treasury is to return the property of those who do not intend to violate the law, demonstrated Congress’ intent “to impose a penalty only upon those who are significantly involved in a criminal enterprise.” <span class="citation" data-id="9424510"><a href="/opinion/108303/united-states-v-united-states-coin-currency/#721" aria-description="Citation for case: United States v. United States Coin &amp; Currency">401 U. S., at 721-722</a></span>. The inclusion of innocent-owner defenses in §§ 881(a)(4) and (a)(7) reveals a similar congressional intent to punish only those involved in drug trafficking.</p>
<p id="b662-4"><page-number citation-index="1" label="620">*620</page-number>Furthermore, Congress has chosen to tie forfeiture directly to the commission of drug offenses. Thus, under § 881(a)(4), a conveyance is forfeitable if it is used or intended for use to facilitate the transportation of controlled substances, their raw materials, or the equipment used to manufacture or distribute them. Under § 881(a)(7), real property is forfeitable if it is used or intended for use to facilitate the commission of a drug-related crime punishable by more than one year’s imprisonment. See n. <span class="citation" data-id="8965274"><a href="/opinion/8973657/united-states-v-tax-lot-1500/" aria-description="Citation for case: United States v. Tax Lot 1500">1, <em>supra.</em></a></span></p>
<p id="b662-5">The legislative history of §881 confirms the punitive nature of these provisions. When it added subsection (a)(7) to §881 in 1984, Congress recognized “that the traditional criminal sanctions of fine and imprisonment are inadequate to deter or punish the enormously profitable trade in dangerous drugs.” S. Rep. No. 98-225, p. 191 (1983).<footnotemark>13</footnotemark> It characterized the forfeiture of real property as “a powerful deterrent.” <em>Id., </em>at 195. See also Joint House-Senate Explanation of Senate Amendment to Titles II and III of the Psychotropic Substances Act of 1978, 124 Cong. Rec. 34671 (1978) (noting “the penal nature of forfeiture statutes”).</p>
<p id="b662-6">The Government argues that §§ 881(a)(4) and (a)(7) are not punitive but, rather, should be considered remedial in two respects. First, they remove the “instruments” of the drug trade “thereby protecting the community from the threat of continued drug dealing.” Brief for United States 32. Second, the forfeited assets serve to compensate the Government for the expense of law enforcement activity and for its expenditure on societal problems such as urban blight, drug addiction, and other health concerns resulting from the drug trade. <em>Id., </em>at 25, 32.</p>
<p id="b663-4"><page-number citation-index="1" label="621">*621</page-number>In our view, neither argument withstands scrutiny. Concededly, we have recognized that the forfeiture of contraband itself may be characterized as remedial because it removes dangerous or illegal items from society. See <em>United States </em>v. <em>One Assortment of 89 Firearms, </em><span class="citation" data-id="111103"><a href="/opinion/111103/united-states-v-one-assortment-of-89-firearms/#364" aria-description="Citation for case: United States v. One Assortment of 89 Firearms">465 U. S. 354, 364</a></span> (1984). The Court, however, previously has rejected government’s attempt to extend that reasoning to conveyances used to transport illegal liquor. See <em>One 1958 Plymouth Sedan </em>v. <em>Pennsylvania, </em><span class="citation" data-id="9423021"><a href="/opinion/107043/one-1958-plymouth-sedan-v-pennsylvania/#699" aria-description="Citation for case: One 1958 Plymouth Sedan v. Pennsylvania">380 U. S. 693, 699</a></span> (1965). In that case it noted: “There is nothing even remotely criminal in possessing an automobile.” <em><span class="citation" data-id="9423021"><a href="/opinion/107043/one-1958-plymouth-sedan-v-pennsylvania/" aria-description="Citation for case: One 1958 Plymouth Sedan v. Pennsylvania">Ibid.</a></span> </em>The same, without question, is true of the properties involved here, and the Government’s attempt to characterize these properties as “instruments” of the drug trade must meet the same fate as Pennsylvania’s effort to characterize the 1958 Plymouth sedan as “contraband.”</p>
<p id="b663-5">The Government’s second argument about the remedial nature of this forfeiture is no more persuasive. We previously have upheld the forfeiture of goods involved in customs violations as “a reasonable form of liquidated damages.” <em>One Lot Emerald Cut Stones </em>v. <em>United States, </em><span class="citation" data-id="108643"><a href="/opinion/108643/one-lot-emerald-cut-stones-and-one-ring-v-united-states/#237" aria-description="Citation for case: One Lot Emerald Cut Stones and One Ring v. United States">409 U. S. 232, 237</a></span> (1972). But the dramatic variations in the value of conveyances and real property forfeitable under §§ 881(a)(4) and (a)(7) undercut any similar argument with respect to those provisions. The Court made this very point in <em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/" aria-description="Citation for case: United States v. Ward">Ward</a></span>: </em>The “forfeiture of property . . . [is] a penalty that ha[s] absolutely no correlation to any damages sustained by society or to the cost of enforcing the law.” <span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/#254" aria-description="Citation for case: United States v. Ward">448 U. S., at 254</a></span>.</p>
<p id="b663-6">Fundamentally, even assuming that §§ 881(a)(4) and (a)(7) serve some remedial purpose, the Government’s argument must fail. “[A] civil sanction that cannot fairly be said <em>solely </em>to serve a remedial purpose, but rather can only be explained as also serving either retributive or deterrent purposes, is punishment, as we have come to understand the term.” <em>Halper, </em><span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/#448" aria-description="Citation for case: United States v. Halper">490 U. S., at 448</a></span> (emphasis added). In light of the historical understanding of forfeiture as punishment, the <page-number citation-index="1" label="622">*622</page-number>clear focus of §§ 881(a)(4) and (a)(7) on the culpability of the owner, and the evidence that Congress understood those provisions as serving to deter and to punish, we cannot conclude that forfeiture under §§ 881(a)(4) and (a)(7) serves solely a remedial purpose.<footnotemark>14</footnotemark> We therefore conclude that forfeiture under these provisions constitutes “payment to a sovereign as punishment for some offense,” <em>Browning-Ferris, </em><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/#265" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U. S., at 265</a></span>, and, as such, is subject to the limitations of the Eighth Amendment’s Excessive Fines Clause.</p>
<p id="b664-5">V</p>
<p id="b664-6">Austin asks that we establish a multifactor test for determining whether a forfeiture is constitutionally “excessive.” See Brief for Petitioner 46-48. We decline that invitation. Although the Court of Appeals opined that “the government is exacting too high a penalty in relation to the offense committed,” 964 F. 2d, at 818, it had no occasion to consider what factors should inform such a decision because it thought it was foreclosed from engaging in the inquiry. Prudence dictates that we allow the lower courts to consider that question <page-number citation-index="1" label="623">*623</page-number>in the first instance. See <em>Yee </em>v. <em>Escondido, </em><span class="citation" data-id="9432511"><a href="/opinion/112719/yee-v-city-of-escondido/#538" aria-description="Citation for case: Yee v. City of Escondido">503 U. S. 519, 538</a></span> (1992).<footnotemark>15</footnotemark></p>
<p id="b665-5">The judgment of the Court of Appeals is reversed, and the case is remanded to that court for further proceedings consistent with this opinion.</p>
<p id="b665-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b647-7"> These statutes provide for the forfeiture of:</p>
<blockquote id="b647-8">“(4) All conveyances, including aircraft, vehicles, or vessels, which are used, or are intended for use, to transport, or in any manner to facilitate the transportation, sale, receipt, possession, or conceálment of [controlled substances, their raw materials, and equipment used in their manufacture and distribution]</blockquote>
<blockquote id="b647-9">“(7) All real property, including any right, title, and interest (including any leasehold interest) in the whole of any lot or tract of land and any appurtenances or improvements, which is used, or intended to be used, in any manner or part, to commit, or to facilitate the commission of, a violation of this subchapter punishable by more than one year’s imprisonment. ..</blockquote>
<p id="b647-10">Each provision has an “innocent owner” exception. See §§ 881(a)(4)(C) and (a)(7).</p>
</footnote>
<footnote label="2">
<p id="b647-11"> “Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted.” U. S. Const., Arndt. 8.</p>
</footnote>
<footnote label="3">
<p id="b649-9"> In <em>Browning-Ferris, </em>we left open the question whether the Excessive Fines Clause applies to <em>qui tam </em>actions in which a private party brings suit in the name of the United States and shares in the proceeds. See <span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/#276" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U. S., at 276, n. 21</a></span>. Because the instant suit was prosecuted by the United States and because Austin’s property was forfeited to the United States, we have no occasion to address that question here.</p>
</footnote>
<footnote label="4">
<p id="b650-6"> As a general matter, this Court’s decisions applying constitutional protections to civil forfeiture proceedings have adhered to this distinction between provisions that are limited to criminal proceedings and provisions that are not. Thus, the Court has held that the Fourth Amendment’s protection against unreasonable searches and seizures applies in forfeiture proceedings, see <em>One 1958 Plymouth Sedan </em>v. <em>Pennsylvania, </em><span class="citation" data-id="9423021"><a href="/opinion/107043/one-1958-plymouth-sedan-v-pennsylvania/#696" aria-description="Citation for case: One 1958 Plymouth Sedan v. Pennsylvania">380 U. S. 693, 696</a></span> (1965); <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#634" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 634</a></span> (1886), but that the Sixth Amendment’s Confrontation Clause does not, see <em>United States </em>v. <em>Zucker, </em><span class="citation" data-id="94399"><a href="/opinion/94399/united-states-v-zucker/#480" aria-description="Citation for case: United States v. Zucker">161 U. S. 475, 480-482</a></span> (1896). It has also held that the due process requirement that guilt in a criminal proceeding be proved beyond a reasonable doubt, see <em>In re Winship, </em><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">397 U. S. 358</a></span> (1970), does not apply to civil forfeiture proceedings. See <em>Lilienthal’s Tobacco </em>v. <em>United States, </em><span class="citation" data-id="89785"><a href="/opinion/89785/lilienthals-tobacco-v-united-states/#271" aria-description="Citation for case: Lilienthal&#x27;s Tobacco v. United States">97 U. S. 237, 271-272</a></span> (1878).</p>
<p id="b650-7">The Double Jeopardy Clause has been held not to apply in civil forfeiture proceedings, but only in cases where the forfeiture could properly be characterized as remedial. See <em>United States </em>v. <em>One Assortment of 89 Firearms, </em><span class="citation" data-id="111103"><a href="/opinion/111103/united-states-v-one-assortment-of-89-firearms/#364" aria-description="Citation for case: United States v. One Assortment of 89 Firearms">465 U. S. 354, 364</a></span> (1984); <em>One Lot Emerald Cut Stones </em>v. <em>United States, </em><span class="citation" data-id="108643"><a href="/opinion/108643/one-lot-emerald-cut-stones-and-one-ring-v-united-states/#237" aria-description="Citation for case: One Lot Emerald Cut Stones and One Ring v. United States">409 U. S. 232, 237</a></span> (1972); see generally <em>United States </em>v. <em>Halper, </em><span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/#446" aria-description="Citation for case: United States v. Halper">490 U. S. 435, 446-449</a></span> (1989) (Double Jeopardy Clause prohibits second sanction that may not fairly be characterized as remedial). Conversely, the Fifth Amendment’s Self-Incrimination Clause, which is textually limited to “criminal case[s],” has been applied in civil forfeiture proceedings, but only where the forfeiture statute had made the culpability of the owner relevant, see <em>United States </em>v. <em>United States Coin &amp; Currency, </em><span class="citation" data-id="9424510"><a href="/opinion/108303/united-states-v-united-states-coin-currency/#721" aria-description="Citation for case: United States v. United States Coin &amp; Currency">401 U. S. 715, 721-722</a></span> (1971), or where the owner faced the possibility of subsequent criminal proceedings, see <em>Boyd, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#634" aria-description="Citation for case: Boyd v. United States">116 U. S., at 634</a></span>; see also <em>United States </em>v. <em>Ward, </em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/#253" aria-description="Citation for case: United States v. Ward">448 U. S. 242, 253-254</a></span> (1980) (discussing <em>Boyd).</em></p>
<p id="b650-8">And, of course, even those protections associated with criminal cases may apply to a civil forfeiture proceeding if it is so punitive that the proceeding must reasonably be considered criminal. See <em>Kennedy </em>v. <em>Mendoza-Martinez, </em><span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/" aria-description="Citation for case: Kennedy v. Mendoza-Martinez">372 U. S. 144</a></span> (1963); <em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/" aria-description="Citation for case: United States v. Ward">Ward, supra.</a></span></em></p>
</footnote>
<footnote label="5">
<p id="b651-6"> In <em>Ingraham </em>v. <em>Wright, </em><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">430 U. S. 651</a></span> (1977), we concluded that the omission of any reference to criminal cases in § 10 was without substantive significance in light of the preservation of a similar reference to criminal cases in the preamble to the English Bill of Rights. <em>Id., </em>at 665. This reference in the preamble, however, related only to excessive bail. See 1 W. &amp; M., 2d Sess., ch. 2, 3 Stat. at Large 440 (1689). Moreover, the preamble appears designed to catalog the misdeeds of James II, see <em>ibid., </em>rather than to define the scope of the substantive rights set out in subsequent sections.</p>
</footnote>
<footnote label="6">
<p id="b652-6"> For this reason, the United States’ reliance on <em>Kennedy </em>v. <em><span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/" aria-description="Citation for case: Kennedy v. Mendoza-Martinez">Mendoza-Martinez</a></span> </em>and <em>United States </em>v. <em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/" aria-description="Citation for case: United States v. Ward">Ward</a></span> </em>is misplaced. The question in those cases was whether a nominally civil penalty should be reclassified as criminal and the safeguards that attend a criminal prosecution should be required. See <em>Mendoza-Martinez, </em><span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/#167" aria-description="Citation for case: Kennedy v. Mendoza-Martinez">372 U. S., at 167, 184</a></span>; <em>Ward, </em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/#248" aria-description="Citation for case: United States v. Ward">448 U. S., at 248</a></span>. In addressing the separate question whether punishment is being imposed, the Court has not employed the tests articulated in <em><span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/" aria-description="Citation for case: Kennedy v. Mendoza-Martinez">Mendoza-Martinez</a></span> </em>and <em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/" aria-description="Citation for case: United States v. Ward">Ward</a></span>. </em>See, <em>e. g., United States </em>v. <em>Halper, </em><span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/#447" aria-description="Citation for case: United States v. Halper">490 U. S., at 447</a></span>. Since in this case we deal only with the question whether the Eighth Amendment’s Excessive Fines Clause applies, we need not address the application of those tests.</p>
</footnote>
<footnote label="7">
<p id="b656-9"> Dictionaries of the time confirm that “fine” was understood to include “forfeiture” and vice versa. See 1 T. Sheridan, A General Dictionary of the English Language (1780) (unpaginated) (defining “fine” as: “A mulct, a pecuniary punishment; penalty; forfeit, money paid for any exemption or liberty”); J. Walker, A Critical Pronouncing Dictionary (1791) (unpaginated) (same); 1 Sheridan, <em>supra </em>(defining “forfeiture” as: “The act of forfeiting; the thing forfeited, a mulct, a fine”); Walker, <em>supra </em>(same); J. Kersey, A New English Dictionary (1702) (unpaginated) (defining “forfeit” as: “default, fine, or penalty”).</p>
</footnote>
<footnote label="8">
<p id="b657-7"> In <em><span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C.">Peisch</a></span>, </em>the removal of the goods from the custody of the revenue officer occurred not by theft or robbery, but pursuant to a writ of replevin issued by a state court. See <span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/#360" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C.">4 Cranch, at 360</a></span>. Thus, <em><span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C.">Peisch</a></span> </em>stands for the general principle that “the law is not understood to forfeit the property of owners or consignees, on account of the misconduct of mere strangers, over whom such owners or consignees could have no control.” <span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/#365" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C."><em>Id., </em>at 365</a></span>.</p>
</footnote>
<footnote label="9">
<p id="b657-8"> The Government relies heavily on this fiction. See Brief for United States 18. We do not understand the Government to rely separately on the technical distinction between proceedings <em>in rem </em>and proceedings <em>in personam, </em>but we note that any such reliance would be misplaced. “The fictions of <em>in rem </em>forfeiture were developed primarily to expand the reach of the courts,” <em>Republic Nat. Bank of Miami </em>v. <em>United States, </em><span class="citation" data-id="9432701"><a href="/opinion/112797/republic-national-bank-of-miami-v-united-states/#87" aria-description="Citation for case: Republic National Bank of Miami v. United States">506 U. S. <page-number citation-index="1" label="616">*616</page-number>80, 87</a></span> (1992), which, particularly in admiralty proceedings, might have lacked <em>in personam </em>jurisdiction over the owner of the property. See also <em>Harmony </em>v. <em>United States, </em><span class="citation" data-id="86274"><a href="/opinion/86274/united-states-v-brig-malek-adhel/#233" aria-description="Citation for case: United States v. Brig Malek Adhel">2 How. 210, 233</a></span> (1844). As is discussed in the text, forfeiture proceedings historically have been understood as imposing punishment despite their <em>in rem </em>nature.</p>
</footnote>
<footnote label="10">
<p id="b659-7"> Because the forfeiture provisions at issue here exempt “innocent owners,” we again have no occasion to decide in this case whether it would comport with due process to forfeit the property of a truly innocent owner.</p>
</footnote>
<footnote label="11">
<p id="b660-7"> In the criminal context, we have permitted punishment in the absence of conscious wrongdoing, so long as the defendant was not “ ‘powerless’ to prevent or correct the violation.” <em>United States </em>v. <em>Park, </em><span class="citation" data-id="9426096"><a href="/opinion/109264/united-states-v-park/#673" aria-description="Citation for case: United States v. Park">421 U. S. 658, 673</a></span> (1975) (corporate officer strictly liable under the Food, Drug, and Cosmetic Act). There is nothing inconsistent, therefore, in viewing forfeiture as punishment even though the forfeiture is occasioned by the acts of a person other than the owner.</p>
</footnote>
<footnote label="12">
<p id="b660-8"> The doubts that Justice Scalia, see <em>post, </em>at 625-627, and Justice Kennedy, see <em>post, </em>at 629, express with regard to the historical understanding of forfeiture as punishment appear to stem from a misunder<page-number citation-index="1" label="619">*619</page-number>standing of the relevant question. Under <em>United States </em>v. <em>Halper, </em><span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/#448" aria-description="Citation for case: United States v. Halper">490 U. S. 435, 448</a></span> (1989), the question is whether forfeiture serves <em>in part </em>to punish, and one need not exclude the possibility that forfeiture serves other purposes to reach that conclusion.</p>
</footnote>
<footnote label="13">
<p id="b662-7"> Although the United States omits any reference to this legislative history in its brief in the present case, it quoted the same passage with approval in its brief in <em>United States </em>v. <em>Parcel of Rumson, N. J., Land, </em><span class="citation" data-id="9432740"><a href="/opinion/112823/united-states-v-parcel-of-rumson-nj-land/" aria-description="Citation for case: United States v. Parcel of Rumson, NJ, Land">507 U. S. 111</a></span> (1993). See Brief for United States, O. T. 1992, No. 91-781, pp. 41-42.</p>
</footnote>
<footnote label="14">
<p id="b664-7"> In <em><span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/" aria-description="Citation for case: United States v. Halper">Halper</a></span>, </em>we focused on whether “the sanction as applied in the individual case serves the goals of punishment.” <span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/#448" aria-description="Citation for case: United States v. Halper">490 U. S., at 448</a></span>. In this case, however, it makes sense to focus on §§ 881(a)(4) and (a)(7) as a whole. <em><span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/" aria-description="Citation for case: United States v. Halper">Halper</a></span> </em>involved a small, fixed-penalty provision, which “in the ordinary case . . . can be said to do no more than make the Government whole.” <span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/#449" aria-description="Citation for case: United States v. Halper"><em>Id., </em>at 449</a></span>. The value of the conveyances and real property forfeitable under §§ 881(a)(4) and (a)(7), on the other hand, can vary so dramatically that any relationship between the Government’s actual costs and the amount of the sanction is merely coincidental. See <em>Ward, </em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/#254" aria-description="Citation for case: United States v. Ward">448 U. S., at 254</a></span>. Furthermore, as we have seen, forfeiture statutes historically have been understood as serving not simply remedial goals but also those of punishment and deterrence. Finally, it appears to make little practical difference whether the Excessive Fines Clause applies to all forfeitures under §§ 881(a)(4) and (a)(7) or only to those that cannot be characterized as purely remedial. The Clause prohibits only the imposition of “excessive” fines, and a fine that serves purely remedial purposes cannot be considered “excessive” in any event.</p>
</footnote>
<footnote label="15">
<p id="b665-11"> Justice Scalia suggests that the sole measure of an <em>in rem </em>forfeiture’s excessiveness is the relationship between the forfeited property and the offense. See <em>post, </em>at 627-628. We do not rule out the possibility that the connection between the property and the offense may be relevant, but our decision today in no way limits the Court of Appeals from considering other factors in determining whether the forfeiture of Austin’s property was excessive.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Bailey v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Bailey v. United States"
type: case
citation: "568 U.S. 186 (2013)"
parallel_cite: "133 S. Ct. 1031; 185 L. Ed. 2d 19"
neutral_cite: 2013 U.S. LEXIS 1075
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2013
date_decided: 2013-02-19
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2013-02-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Bailey v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/820749/bailey-v-united-states/"
  cluster_id: 820749
  opinion_id: 9502775
  identity_checked: true
homes:
  - page: "[[Detention and Search of Persons at the Scene]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Securing the Scene]]"
    role: "Related (scene-securing overlap)"
related: ["[[Michigan v. Summers]]", "[[Illinois v. McArthur]]", "[[Terry v. Ohio]]"]
aliases: ["Bailey v. US"]
tags: ["case", "fourth-amendment", "detention", "search-warrant", "securing-the-scene"]
holding: "The detention authority recognized in Michigan v. Summers is limited to the immediate vicinity of the premises to be searched; it does…"
lake:
  record_id: Bailey v. United States
  status: verified
  projected_at: 2026-07-09
---

# Bailey v. United States

*568 U.S. 186 (2013)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers had a warrant to search a basement apartment for a handgun. Before executing it, surveillance officers saw Bailey and another man leave the apartment by car. Officers followed and stopped them roughly a mile away, detained Bailey, patted him down, and drove him back to the apartment. The search turned up a gun and drugs, and a key in Bailey's possession opened the apartment door. The detention was justified below under [[Michigan v. Summers]], which allows detaining occupants while a search warrant is executed.

## Issue
Whether the *[[Michigan v. Summers|Summers]]* authority to detain occupants incident to the execution of a search warrant extends to a former occupant who has already left and is stopped away from the immediate vicinity of the premises.

## Rule
No — the *[[Michigan v. Summers|Summers]]* detention authority is spatially limited. "A spatial constraint defined by the immediate vicinity of the premises to be searched is therefore required for detentions incident to the execution of a search warrant." — 568 U.S. at 201 (slip op., at 13). ^pin-201

The interests *[[Michigan v. Summers|Summers]]* serves (officer safety, orderly completion of the search, preventing flight) do not reach a former occupant who has departed: that flight-prevention interest "does not independently justify detention of an occupant beyond the immediate vicinity of the premises to be searched." — [*Id.* at 199](https://www.courtlistener.com/opinion/820749/bailey-v-united-states/#:~:text=does%20not%20independently%20justify%20detention) (slip op., at 11). ^pin-199

## Application
Bailey was stopped about a mile from the apartment, well outside its immediate vicinity, after he had already left (apparently unaware of the impending search). Because he was not within the immediate vicinity, the *[[Michigan v. Summers|Summers]]* rule did not authorize his detention; absent that categorical authority, the officers would have needed probable cause to arrest or reasonable suspicion to make a *[[Terry v. Ohio|Terry]]* stop.

## Conclusion
The detention was not authorized by *[[Michigan v. Summers|Summers]]*; the judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]] to consider whether the stop could be justified on other grounds (e.g., *[[Terry v. Ohio|Terry]]*).

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of *Bailey*. *Bailey* **limits** [[Michigan v. Summers]] by confining the categorical, suspicionless detention authority to the immediate vicinity of the premises being searched.

## Appears on
- [[Securing the Scene]] — *Key — Progeny / Refinement*

## Sources
- *Bailey v. United States*, 568 U.S. 186 (2013) — https://www.courtlistener.com/opinion/820749/bailey-v-united-states/ — pinpoints: 199, 201 (CL carries the slip opinion; cited at slip op. 11, 13).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "bfdd9b809baf3a20", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Bailey v. United States"}, "payload": {"all": [{"cite": "133 S. Ct. 1031", "page": "1031", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "133"}, {"cite": "185 L. Ed. 2d 19", "page": "19", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "185"}, {"cite": "2013 U.S. LEXIS 1075", "page": "1075", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2013"}, {"cite": "568 U.S. 186", "page": "186", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "568"}], "display": "568 U.S. 186", "official": {"cite": "568 U.S. 186", "page": "186", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "568"}, "official_selection_present": true, "record_id": "Bailey v. United States"}}
{"assertion_id": "5b220a2b87f401c9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-201", "record_id": "Bailey v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-201", "pinpoint_status": "slip-only", "quote": "--- # Bailey v. United States *568 U.S. 186 (2013)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers had a warrant to search a basement apartment for a handgun. Before executing it, surveillance officers saw Bailey and another man leave the apartment by car. Officers followed and stopped them roughly a mile away, detained Bailey, patted him down, and drove him back to the apartment. The search turned up a gun and drugs, and a key in Bailey's possession opened the apartment door. The detention was justified below under [[Michigan v. Summers]], which allows detaining occupants while a search warrant is executed. ## Issue Whether the *Summers* authority to detain occupants incident to the execution of a search warrant extends to a former occupant who has already left and is stopped away from the immediate vicinity of the premises. ## Rule No — the *Summers* detention authority is spatially limited.", "quote_fidelity": "mismatch", "record_id": "Bailey v. United States", "star_marker": null}}
{"assertion_id": "9b466077cae517dc", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-199", "record_id": "Bailey v. United States"}, "payload": {"fragment": "#:~:text=does%20not%20independently%20justify%20detention", "page": null, "pin_id": "pin-199", "pinpoint_status": "star-verified", "quote": "does not independently justify detention of an occupant beyond the immediate vicinity of the premises to be searched.", "quote_fidelity": "matched", "record_id": "Bailey v. United States", "star_marker": "199"}}
{"assertion_id": "e08ab0d4d9081f93", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Bailey v. United States"}, "payload": {"as_of_content": "2013-02-19", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Bailey v. United States", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Bailey v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Bailey v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Bailey v. United States",
    "case_name_short": "Bailey",
    "case_name_full": "Bailey v. United States",
    "input_case_name": "Bailey v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2013-02-19",
    "year": 2013,
    "docket": null,
    "cluster_id": 820749,
    "lead_opinion_id": 9502775,
    "sibling_ids": [
      820749,
      9502775,
      9502776,
      9502777
    ],
    "absolute_url": "/opinion/820749/bailey-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8412656,
        "score": 10,
        "case_name": "Bailey v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "568 U.S. 186",
      "volume": "568",
      "reporter": "U.S.",
      "page": "186",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "133 S. Ct. 1031",
        "volume": "133",
        "reporter": "S. Ct.",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "185 L. Ed. 2d 19",
        "volume": "185",
        "reporter": "L. Ed. 2d",
        "page": "19",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2013 U.S. LEXIS 1075",
        "volume": "2013",
        "reporter": "U.S. LEXIS",
        "page": "1075",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "133 S. Ct. 1031",
        "volume": "133",
        "reporter": "S. Ct.",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "185 L. Ed. 2d 19",
        "volume": "185",
        "reporter": "L. Ed. 2d",
        "page": "19",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 U.S. LEXIS 1075",
        "volume": "2013",
        "reporter": "U.S. LEXIS",
        "page": "1075",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "568 U.S. 186",
        "volume": "568",
        "reporter": "U.S.",
        "page": "186",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "568 U.S. 186",
    "official_selection": {
      "court_class": "scotus",
      "selected": "568 U.S. 186",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-201",
      "page": null,
      "quote": "--- # Bailey v. United States *568 U.S. 186 (2013)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers had a warrant to search a basement apartment for a handgun. Before executing it, surveillance officers saw Bailey and another man leave the apartment by car. Officers followed and stopped them roughly a mile away, detained Bailey, patted him down, and drove him back to the apartment. The search turned up a gun and drugs, and a key in Bailey's possession opened the apartment door. The detention was justified below under [[Michigan v. Summers]], which allows detaining occupants while a search warrant is executed. ## Issue Whether the *Summers* authority to detain occupants incident to the execution of a search warrant extends to a former occupant who has already left and is stopped away from the immediate vicinity of the premises. ## Rule No \u2014 the *Summers* detention authority is spatially limited.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-199",
      "page": null,
      "quote": "does not independently justify detention of an occupant beyond the immediate vicinity of the premises to be searched.",
      "star_marker": "199",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 29407,
      "fragment": "#:~:text=does%20not%20independently%20justify%20detention",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2013-02-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Bailey v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 9352593,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 6620965,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 6478743,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane1_negative"
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
        "journal_ref": "Bailey v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Connor William Clar Steffens",
          "cluster_id": 4332280,
          "cite": [
            "889 N.W.2d 691",
            "2016 Iowa App. LEXIS 1316",
            "2016 WL 7393893"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane1_negative"
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
        "journal_ref": "Bailey v. United States:lane1_negative"
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
        "journal_ref": "Bailey v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Prall v. City of Boston",
          "cluster_id": 8729956,
          "cite": [
            "985 F. Supp. 2d 115",
            "2013 WL 6076462",
            "2013 U.S. Dist. LEXIS 166128"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Byron Halsey v. Frank Pfeiffer",
          "cluster_id": 2671183,
          "cite": [
            "750 F.3d 273",
            "2014 WL 1622769",
            "2014 U.S. App. LEXIS 7696"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maurice Lewis v. City of Chicago",
          "cluster_id": 4583974,
          "cite": [
            "914 F.3d 472"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shaun J. Matz v. Rodney Klotka",
          "cluster_id": 2739950,
          "cite": [
            "769 F.3d 517",
            "2014 U.S. App. LEXIS 19074",
            "2014 WL 4960311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
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
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Americans for Prosperity Foundation v. Bonta",
          "cluster_id": 4896549,
          "cite": [
            "594 U.S. 595",
            "210 L. Ed. 2d 716",
            "141 S. Ct. 2373"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Antoine D. Watts(074556)",
          "cluster_id": 3159265,
          "cite": [
            "223 N.J. 503",
            "126 A.3d 1216",
            "2015 N.J. LEXIS 1239"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "C. B. v. City of Sonora",
          "cluster_id": 2743611,
          "cite": [
            "769 F.3d 1005",
            "89 Fed. R. Serv. 3d 1624",
            "2014 U.S. App. LEXIS 19757",
            "2014 WL 5151632"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bailey",
          "cluster_id": 2654019,
          "cite": [
            "743 F.3d 322",
            "2014 WL 657932"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Eric Brodie",
          "cluster_id": 2653533,
          "cite": [
            "408 U.S. App. D.C. 326",
            "742 F.3d 1058",
            "2014 WL 593264",
            "2014 U.S. App. LEXIS 2874"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dwayne Sheckles",
          "cluster_id": 4879211,
          "cite": [
            "996 F.3d 330"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Davis",
          "cluster_id": 4759018,
          "cite": [
            "961 F.3d 181"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hackney",
          "cluster_id": 3218181,
          "cite": [
            "2016 Ohio 4609"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donald Delade v. John Cargan",
          "cluster_id": 4778175,
          "cite": [
            "972 F.3d 207"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jack Bruce Folk",
          "cluster_id": 2678192,
          "cite": [
            "754 F.3d 905",
            "2014 WL 2611272",
            "2014 U.S. App. LEXIS 10929"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gregorio Perez Cruz v. William Barr",
          "cluster_id": 4629270,
          "cite": [
            "926 F.3d 1128"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Isaiah Woodson, Jr.",
          "cluster_id": 6459262,
          "cite": [
            "30 F.4th 1295"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ryan Moderson v. City of Neenah",
          "cluster_id": 10581758,
          "cite": [
            "137 F.4th 611"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dwayne Furlow v. Jon Belmar",
          "cluster_id": 8436813,
          "cite": [
            "52 F.4th 393"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Karamanoglu v. Town of Yarmouth",
          "cluster_id": 5178962,
          "cite": [
            "15 F.4th 82"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thomas Moorer v. City of Chicago",
          "cluster_id": 9473951,
          "cite": [
            "92 F.4th 715"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Lewis",
          "cluster_id": 4412774,
          "cite": [
            "864 F.3d 937",
            "2017 WL 3186308",
            "2017 U.S. App. LEXIS 13583"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chacker v. JPMorgan Chase Bank, N.A.",
          "cluster_id": 6239907,
          "cite": [
            "237 Cal. Rptr. 3d 921",
            "27 Cal. App. 5th 351"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Mason",
          "cluster_id": 4299107,
          "cite": [
            "2016 Ohio 7081"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Wilson",
          "cluster_id": 4576198,
          "cite": [
            "821 S.E.2d 811",
            "371 N.C. 920"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Kaul",
          "cluster_id": 4374844,
          "cite": [
            "2017 ND 56",
            "891 N.W.2d 352",
            "2017 N.D. LEXIS 56",
            "2017 WL 968845"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(820749 OR 9502775 OR 9502776 OR 9502777) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 95,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 8,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 95,
        "triage_read": 8,
        "triage_snippet_classified": 87
      },
      "lane2_top_cited": {
        "query": "cites:(820749 OR 9502775 OR 9502776 OR 9502777)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zJnM9NDMzMjI4MCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28820749+OR+9502775+OR+9502776+OR+9502777%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(820749 OR 9502775 OR 9502776 OR 9502777)",
        "reviewed": 16,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 16,
        "triage_read": 0,
        "triage_snippet_classified": 16
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(820749 OR 9502775 OR 9502776 OR 9502777)",
    "indexed_citing_opinions": 122,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 820749,
        "count": 76,
        "count_source": "search"
      },
      {
        "opinion_id": 9502775,
        "count": 46,
        "count_source": "search"
      },
      {
        "opinion_id": 9502776,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9502777,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 392,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/bailey-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc3MDk1OSZzPTY0NTkyNjImdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28820749+OR+9502775+OR+9502776+OR+9502777%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 820749,
        "cited_id": 27226,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 111600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 112384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 134746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 142878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 145728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 145887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 183973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 220356,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 565019,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 618288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 2531019,
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
    "date_created": "2026-07-04T19:16:10Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T19:16:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T19:16:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T19:20:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T19:16:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Bailey v. United States

```
<opinion type="majority">
<author id="b407-5">Justice Kennedy</author>
<p id="AJ">delivered the opinion of the Court.</p>
<p id="b407-6">The Fourth Amendment guarantees the right to be free from unreasonable searches and seizures. A search may be of a person, a thing, or a place. So too a seizure may be of a person, a thing, or even a place. A search or a seizure may occur singly or in combination, and in differing sequence. In some cases the validity of one determines the validity of the other. The instant case involves the search of a place (an apartment dwelling) and the seizure of a person. But here, though it is acknowledged that the search was lawful,.it does not follow that the seizure was lawful as well. The seizure of the person is quite in question. The issue to be resolved is whether the seizure of the person was reasonable when he was stopped and detained at some distance away from the premises to be searched when the only justification for <page-number citation-index="1" label="190">*190</page-number>the detention was to ensure the safety and efficacy of the search.</p>
<p id="b408-5">I</p>
<p id="b408-6">A</p>
<p id="b408-7">At 8:45 p.m. on July 28, 2005, local police obtained a warrant to search a residence for a .380-caliber handgun. The residence was a basement apartment at 103 Lake Drive, in Wyandanch, New York. A confidential informant had told police he observed the gun when he was at the apartment to purchase drugs from “a heavy set black male with short hair” known as “Polo.” App. 16-26. As the search unit began preparations for executing the warrant, two officers, Detectives Richard Sneider and Richard Gorbecki, were conducting surveillance in an unmarked car outside the residence. About 9:56 p.m., Sneider and Gorbecki observed two men—later identified as petitioner Chunon Bailey and Bryant Middleton—leave the gated area above the basement apartment and enter a car parked in the driveway. Both matched the general physical description of “Polo” provided by the informant. There was no indication that the men were aware of the officers’ presence or had any knowledge of the impending search. The detectives watched the car leave the driveway. They waited for it to go a few hundred yards down the street and followed. The detectives informed the search team of their intent to follow and detain the departing occupants. The search team then executed the search warrant at the apartment.</p>
<p id="b408-8">Detectives Sneider and Gorbecki tailed Bailey’s car for about a mile—and for about five minutes—before pulling the vehicle over in a parking lot by a fire station. They ordered Bailey and Middleton out of the car and did a patdown search of both men. The officers found no weapons but discovered a ring of keys in Bailey’s pocket. Bailey identified himself and said he was coming from his home at 103 Lake Drive. His driver’s license, however, showed his address as Bay-<page-number citation-index="1" label="191">*191</page-number>shore, New York, the town where the confidential informant told the police the suspect, “Polo,” used to live. <em>Id., </em>at 89. Bailey’s passenger, Middleton, said Bailey was giving him a ride home and confirmed they were coming from Bailey’s residence at 103 Lake Drive. The officers put both men in handcuffs. When Bailey asked why, Gorbecki stated that they were being detained incident to the execution of a search warrant at 103 Lake Drive. Bailey responded: “I don’t live there. Anything you find there ain’t mine, and I’m not cooperating with your investigation.” <em>Id., </em>at 57, 77.</p>
<p id="Amr">The detectives called for a patrol cár to take Bailey and Middleton back’ to the Lake Drive apartment. Detective Sneider drove the unmarked car back, while Detective Gor-becki used Bailey’s set of keys to drive Bailey’s car back to the search scene. By the time the group returned to 103 Lake Drive, the search team had discovered a gun and drugs in plain view inside the apartment. Bailey and Middleton were placed under arrest, and Bailey’s keys were seized incident to the arrest. Officers later discovered that one of Bailey’s keys opened the door of the basement apartment.</p>
<p id="b409-6">B</p>
<p id="b409-7">Bailey was charged with three federal offenses: possession of cocaine with intent to distribute, in violation of <span class="citation no-link">21 U. S. C. §§ 841</span>(a)(1) and (b)(1)(B)(iii); possession of a firearm by a felon, in violation of <span class="citation no-link">18 U. S. C. § 922</span>(g)(1); and possession of a firearm in furtherance of a drug-trafficking offense, in violation of § 924(c)(1)(A)(i). At trial Bailey moved to suppress the apartment key and the statements he made when stopped by Detectives Sneider and Gorbecki. That evidence, Bailey argued, derived from an unreasonable seizure. After an evidentiary hearing the United States District Court for the Eastern District of New York denied the motion to suppress. The District Court held that Bailey’s detention was permissible under <em>Michigan </em>v. <em>Summers, </em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692</a></span> (1981), as a detention incident to the execution of <page-number citation-index="1" label="192">*192</page-number>a search warrant. In the alternative, it held that Bailey’s detention was lawful as an investigatory detention supported by reasonable suspicion under <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968). After a trial the jury found Bailey guilty on all three counts.</p>
<p id="b410-6">The Court of Appeals for the Second Circuit ruled that Bailey’s detention was proper and affirmed denial of the suppression motion. It interpreted this Court’s decision in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>to “authoriz[e] law enforcement to detain the occupant of premises subject to a valid search warrant when that person is seen leaving those premises and the detention is effected <em>as soon as reasonably practicable.” </em><span class="citation" data-id="220356"><a href="/opinion/220356/united-states-v-bailey/#208" aria-description="Citation for case: United States v. Bailey">652 F. 3d 197, 208</a></span> (2011). Having found Bailey’s detention justified under <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>the Court of Appeals did not address the District Court’s alternative holding that the stop was permitted under <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</em></p>
<p id="b410-7">The Federal Courts of Appeals have reached differing conclusions as to whether <em>Michigan </em>v. <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>justifies the detention of occupants beyond the immediate vicinity of the premises covered by a search warrant. This Court granted certiorari to address the question. <span class="citation multiple-matches"><a href="/c/U.%20S./566/1033/">566 U. S. 1033</a></span> (2012).</p>
<p id="pAa9">H—i</p>
<p id="b410-3">The Fourth Amendment, applicable through the- Four- ' teenth Amendment to the States, provides: “The right of the people to be secure in their persons ... against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause . . . particularly describing the place to be searched, and the persons or things to be seized.” This Court has stated “the general rule that Fourth Amendment seizures are ‘reasonable’ only if based on probable cause” to believe that the individual has committed a crime. <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#213" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 213</a></span> (1979). The standard of probable cause, with “roots that are deep in our history,” <em>Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#100" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 100</a></span> (1959), “represent[s] the accumulated wisdom of precedent and ex<page-number citation-index="1" label="193">*193</page-number>perience as to the minimum justification necessary to make the kind of intrusion involved in an arrest ‘reasonable’ under the Fourth Amendment.” <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#208" aria-description="Citation for case: Dunaway v. New York"><em>Dunaway, supra, </em>at 208</a></span>.</p>
<p id="b411-5">Within the framework of these fundamental rules there is some latitude for police to detain where “the intrusion on the citizen’s privacy ‘was so much less severe’ than that involved in a traditional arrest that ‘the opposing interests in crime prevention and detection and in the police officer’s safety’ could support the seizure as reasonable.” <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers, supra,</a></span> </em>at 697-698 (quoting <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#209" aria-description="Citation for case: Dunaway v. New York"><em>Dunaway, supra, </em>at 209</a></span>); see also <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><em>Terry, supra, </em>at 27</a></span> (holding that a police officer who has reasonable suspicion of criminal activity may conduct a brief investigative stop).</p>
<p id="b411-6">In <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>the Court defined an important category of cases in which detention is allowed without probable cause to arrest for a crime. It permitted officers executing a search warrant “to detain the occupants of the premises while a proper search is conducted.” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#705" aria-description="Citation for case: Michigan v. Summers">452 U. S., at 705</a></span>. The rule in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>extends further than some earlier exceptions because it does not require law enforcement to have particular suspicion that an individual is involved in criminal activity or poses a specific danger to the officers. <em>Muehler </em>v. <em>Mena, </em><span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/" aria-description="Citation for case: Muehler v. Mena">544 U. S. 93</a></span> (2005). In <em><span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/" aria-description="Citation for case: Muehler v. Mena">Muehler</a></span>, </em>applying the rule in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>the Court stated: “An officer’s authority to detain incident to a search is categorical; it does not depend on the ‘quantum of proof justifying detention or the extent of the intrusion to be imposed by the seizure.’ ” <span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/" aria-description="Citation for case: Muehler v. Mena">544 U. S., at 98</a></span> (quoting <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#705" aria-description="Citation for case: Michigan v. Summers"><em>Summers, supra, </em>at 705, n. 19</a></span>). The rule, announced in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>allows detention incident to the execution of a search warrant “because the character of the additional intrusion caused by detention is slight and because the justifications for detention are substantial.” <span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/#98" aria-description="Citation for case: Muehler v. Mena"><em>Muehler, supra, </em>at 98</a></span>.</p>
<p id="b411-7">In <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>and later cases, the occupants detained were found within or immediately outside a residence at the moment the police officers executed the search warrant. In <page-number citation-index="1" label="194">*194</page-number><em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>the defendant was detained on a walk leading down from the front steps of the house. See Tr. of Oral Arg. in O. T. 1980, No. 79-1794, pp. 41-42; see also <span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/#96" aria-description="Citation for case: Muehler v. Mena"><em>Muehler, supra, </em>at 96</a></span> (detention of occupant in adjoining garage); <em>Los Angeles County </em>v. <em>Rettele, </em><span class="citation" data-id="9435063"><a href="/opinion/145728/los-angeles-county-california-v-rettele/#611" aria-description="Citation for case: Los Angeles County, California v. Rettele">550 U. S. 609, 611</a></span> (2007) <em>(per curiam) </em>(detention of occupants in bedroom). Here, however, petitioner left the apartment before the search began; and the police officers waited to detain him until he was almost a mile away. The issue is whether the reasoning in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>can justify detentions beyond the immediate vicinity of the premises being searched. An exception to the Fourth Amendment rule prohibiting detention absent probable cause must not diverge from its purpose and rationale. See <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#500" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 500</a></span> (1983) (plurality opinion) (“The scope of the detention must be carefully tailored to its underlying justification”)- It is necessary, then, to discuss the reasons for the rule explained in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>to determine if its rationale extends to a detention like the one here.</p>
<p id="b412-5">A</p>
<p id="b412-6">In <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>the Court recognized three important law enforcement interests that, taken together, justify the detention of an occupant who is on the premises during the execution of a search warrant: officer safety, facilitating the completion of the search, and preventing flight. <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers">452 U. S., at 702-703</a></span>.</p>
<p id="b412-7">1</p>
<p id="b412-8">The first interest identified in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>was “the interest in minimizing the risk of harm to the officers.” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers"><em>Id., </em>at 702</a></span>. There the Court held that “the execution of a warrant to search for narcotics is the kind of transaction that may give rise to sudden violence or frantic efforts to conceal or destroy evidence,” and “[t]he risk of harm to both the police and the occupants is minimized if the officers routinely exercise unquestioned command of the situation.” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers"><em>Id., </em>at 702-703</a></span>.</p>
<p id="b413-3"><page-number citation-index="1" label="195">*195</page-number>When law enforcement officers execute a search warrant, safety considerations require that they secure the premises, which may include detaining current occupants. By taking “unquestioned command of. the situation,” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#703" aria-description="Citation for case: Michigan v. Summers"><em>id., </em>at 703</a></span>, the officers can search without fear that occupants, who are on the premises and able to observe the course of the search, will become disruptive, dangerous, or otherwise frustrate the search.</p>
<p id="b413-4">After <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>this Court decided <em>Muehler </em>v. <em><span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/" aria-description="Citation for case: Muehler v. Mena">Mena</a></span>. </em>The reasoning and conclusions in <em><span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/" aria-description="Citation for case: Muehler v. Mena">Muehler</a></span> </em>in applying the <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>rule go quite far in allowing seizure and detention of persons to accommodate the necessities of a search. There, the person detained and held in handcuffs was not suspected of the criminal activity being investigated; but, the Court held, she could be detained nonetheless, to secure the premises while the search was underway. The “safety risk inherent in executing a search warrant for weapons was sufficient to justify the use of handcuffs, [and] the need to detain multiple occupants made the use of handcuffs all the more reasonable.” <span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/#100" aria-description="Citation for case: Muehler v. Mena">544 U. S., at 100</a></span>. While the Court in <em><span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/" aria-description="Citation for case: Muehler v. Mena">Muehler</a></span> </em>did remand for consideration of whether the detention there—alleged to have been two or three hours—was necessary in light of all the circumstances, the fact that so prolonged a detention indeed might have been permitted illustrates the far-reaching authority the police have when the detention is made at the scene of the search. This in turn counsels caution before extending the power to detain persons stopped or apprehended away from the premises where the search is being conducted.</p>
<p id="b413-5">It is likely, indeed almost inevitable in the case of a resident, that an occupant will return to the premises at some point; and this might occur when the officers are still conducting the search. Officers can and do mitigate that risk, however, by taking routine precautions, for instance by erecting barricades or posting someone on the perimeter or at the door. In the instant case Bailey had left the premises, <page-number citation-index="1" label="196">*196</page-number>apparently without knowledge of the search. He posed little risk to the officers at the scene. If Bailey had rushed back to his apartment, the police could have apprehended and detained him under <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>. </em>There is no established principle, however, that allows the arrest of anyone away from the premises who is likely to return.</p>
<p id="b414-5">The risk, furthermore, that someone could return home during the execution of a search warrant is not limited to occupants who depart shortly before the start of a search. The risk that a resident might return home, either for reasons unrelated to the search or after being alerted by someone at the scene, exists whether he left five minutes or five hours earlier. Unexpected arrivals by occupants or other persons accustomed to visiting the premises might occur in many instances. Were police to have the authority to detain those persons away from the premises, the authority to detain incident to the execution of a search warrant would reach beyond the rationale of ensuring the integrity of the search by detaining those who are in fact on the scene.</p>
<p id="b414-6">The Court of Appeals relied on an additional safety consideration. It concluded that limiting the application of the authority to detain to the immediate vicinity would put law enforcement officers in a dilemma. They would have to choose between detaining an individual immediately (and risk alerting occupants still inside) or allowing the individual to leave (and risk not being able to arrest him later if incriminating evidence were discovered). <span class="citation" data-id="220356"><a href="/opinion/220356/united-states-v-bailey/#205" aria-description="Citation for case: United States v. Bailey">652 F. 3d, at 205-206</a></span>. Although the danger of alerting occupants who remain inside may be of real concern in some instances, as in the case when a no-knock warrant has been issued, this safety rationale rests on the false premise that a detention must take place. If the officers find that it would be dangerous to detain a departing individual in front of a residence, they are not required to stop him. And, where there are grounds to believe the departing occupant is dangerous, or involved in criminal activity, police will generally not need <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>to <page-number citation-index="1" label="197">*197</page-number>detain him at least for brief questioning, as they can rely instead on <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</em></p>
<p id="b415-5">The risk that a departing occupant might notice the police surveillance and alert others still inside the residence is also an insufficient safety rationale to justify expanding the existing categorical authority to detain so that it extends beyond the immediate vicinity of the premises to be searched. If extended in this way the rationale would justify detaining anyone in the neighborhood who could alert occupants that the police are outside, all without individualized suspicion of criminal activity or connection to the residence to be •searched. This possibility demonstrates why it is necessary to confine the <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>rule to those who are present when and where the search is being conducted.</p>
<p id="b415-6">2</p>
<p id="b415-7">The second law enforcement interest relied on in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>was that “the orderly completion of the search may be facilitated if the occupants of the premises are present.” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#703" aria-description="Citation for case: Michigan v. Summers">452 U. S., at 703</a></span>. This interest in efficiency derives from distinct, but related, concerns.</p>
<p id="b415-8">If occupants are permitted to wander around the premises, there is the potential for interference with the execution of the search warrant. They can hide or destroy evidence, seek to distract the officers, or simply get'in the way. Those risks are not presented by an occupant who departs beforehand. So, in this case, after Bailey drove away from the Lake Drive apartment, he was not a threat to the proper execution of the search. Had he returned, officers would have been free to detain him at that point. A general interest in avoiding obstruction of a search, however, cannot justify detention beyond the vicinity of the premises to be searched.</p>
<p id="b415-9"><em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>also noted that occupants can assist the officers. Under the reasoning in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>the occupants’ “self-interest may induce them to open locked doors or locked con<page-number citation-index="1" label="198">*198</page-number>tainers to avoid the use of force that is not only damaging to property but may also delay the completion of the task at hand.” <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Ibid.</a></span> </em>This justification must be confined to those persons who are on site and so in a position, when detained, to at once observe the progression of the search; and it would have no limiting principle were it to be applied to persons beyond the premises of the search. Here, it appears the police officers decided to wait until Bailey had left the vicinity of the search before detaining him. In any event it later became clear to the officers that Bailey did not wish to cooperate. See App. 57, 77 (“I don’t live there. Anything you find there ain’t mine, and I’m not cooperating with your investigation”). And, by the time the officers brought Bailey back to the apartment, the search team had discovered contraband. Bailey’s detention thus served no purpose in ensuring the efficient completion of the search.</p>
<p id="b416-5">a</p>
<p id="b416-6">The third law enforcement interest addressed in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>was the “the legitimate law enforcement interest in preventing flight in the event that incriminating evidence is found.” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers">452 U. S., at 702</a></span>. The proper interpretation of this language, in the context of <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>and in the broader context of the reasonableness standard that must govern and inform the detention incident to a search, is that the police can prohibit an occupant from leaving the scene of the search. As with the other interests identified in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>this justification serves to preserve the integrity of the search by controlling those persons who are on the scene. If police officers are concerned about flight, and have to keep close supervision of occupants who are not restrained, they might rush the search, causing unnecessary damage to property or compromising its careful execution. Allowing officers to secure the scene by detaining those present also prevents the search from being impeded by occupants leaving with the evidence being sought or the means to find it.</p>
<p id="b417-4"><page-number citation-index="1" label="199">*199</page-number>The concern over flight is not because of the danger of flight itself but because of the damage that potential flight can cause to the integrity of the search. This interest does not independently justify detention of an occupant beyond the immediate vicinity of the premises to be searched. The need to prevent flight, if unbounded, might be used to argue for detention, while a search is underway, of any regular occupant regardless of his or her location at the time of the search. If not circumscribed, the rationale of preventing flight would justify, for instance, detaining a suspect who is 10 miles away, ready to board a plane. The interest in preventing escape from police cannot extend this far without undermining the usual rules for arrest based on probable cause or a brief stop for questioning under standards derived from <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>. </em>Even if the detention of a former occupant away from the premises could facilitate a later arrest should incriminating evidence be discovered, “the mere fact that law enforcement may be made more efficient can never by itself justify disregard of the Fourth Amendment.” <em>Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#393" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 393</a></span> (1978).</p>
<p id="b417-5">In sum, of the three law enforcement interests identified to justify the detention in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>none applies with the same or similar force to the detention of recent occupants beyond the immediate vicinity of the premises to be searched. Any of the individual interests is also insufficient, on its own, to justify an expansion of the rule in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>to permit the detention of a former occupant, wherever he may be found away from the scene of the search. This would give officers too much discretion. The categorical authority to detain incident to the execution of a search warrant must be limited to the immediate vicinity of the premises to be searched.</p>
<p id="b417-6">B</p>
<p id="b417-7">In <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>the Court recognized the authority to detain occupants incident to the execution of a search warrant not only in light of the law enforcement interests at stake but <page-number citation-index="1" label="200">*200</page-number>also because the intrusion on personal liberty was limited. The Court held detention of a current occupant “represents only an incremental intrusion on personal liberty when the search of a home has been authorized by a valid warrant.” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#703" aria-description="Citation for case: Michigan v. Summers">452 U. S., at 703</a></span>. Because the detention occurs in the individual’s own home, “it could add only minimally to the public stigma associated with the search itself and would involve neither the inconvenience nor the indignity associated with a compelled visit to the police station.” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers"><em>Id., </em>at 702</a></span>.</p>
<p id="b418-5">Where officers arrest an individual away from his home, however, there is an additional level of intrusiveness. A public detention, even if merely incident to a search, will resemble a full-fledged arrest. As demonstrated here, detention beyond the immediate vicinity can involve an initial detention away from the scene and a second detention at the residence. In between, the individual will suffer the additional indignity of a compelled transfer back to the premises, giving all the appearances of an arrest. The detention here was more intrusive than a usual detention at the search scene. Bailey’s car was stopped; he was ordered to step out and was detained in full public view; he was handcuffed, transported in a marked patrol car, and detained further outside the apartment. These facts illustrate that detention away from a premises where police are already present often will be more intrusive than detentions at the scene.</p>
<p id="b418-6">C</p>
<p id="b418-7"><em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>recognized that a rule permitting the detention of occupants on the premises during the execution of a search warrant, even absent individualized suspicion, was reasonable and necessary in light of the law enforcement interests in conducting a safe and efficient search. Because this exception grants substantial authority to police officers to detain outside of the traditional rules of the Fourth Amendment, it must be circumscribed.</p>
<p id="b419-4"><page-number citation-index="1" label="201">*201</page-number>A spatial constraint defined by the immediate vicinity of the premises to be searched is therefore required for detentions incident to the execution of a séarch warrant. The police action permitted here—the .search of a residence—has a spatial dimension, and so a spatial or geographical boundary can be used to determine the area within which both the search and detention incident to that search may occur. Limiting the rule in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>to the area in which an occupant poses a real threat to the safe and efficient execution of a search warrant ensures that the scope of the detention incident to a search is confined to its underlying justification. Once an occupant is beyond the immediate vicinity of the premises to be searched, the search-related law enforcement interests are diminished and the. intrusiveness of the detention is more severe.</p>
<p id="b419-5">Here, petitioner was detained at a point beyond any reasonable understanding of the immediate vicinity of the premises in question; and so this case presents neither the necessity nor the occasion to further define the meaning of immediate vicinity. In closer cases courts can consider a number of factors to determine whether an occupant was detained within the immediate vicinity of the premises to be searched, including the lawful limits of the premises, whether the occupant was within the line of sight of his dwelling, the ease of reentry from the occupant’s location, and other relevant factors.</p>
<p id="b419-6">Confining an officer’s authority to detain under <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>to the immediate vicinity of a premises to be searched is a proper limit because it accords with the rationale of the rule. The rule adopted by the Court of Appeals here, allowing detentions of a departed occupant “as soon as reasonably practicable,” departs from the spatial limit that is necessary to confine the rule in light of the substantial intrusions on the liberty of those detained. Because detention is justified by the interests in executing a safe and efficient search, the decision to detain must be acted upon at the scene of the <page-number citation-index="1" label="202">*202</page-number>search and not at a later time in a more remote place. If officers elect to defer the detention until the suspect or departing occupant leaves the immediate vicinity, the lawfulness of detention is controlled by other standards, including, of course, a brief stop for questioning based on reasonable suspicion under <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>or an arrest based on probable cause. A suspect’s particular actions in leaving the scene, including whether he appears to be armed or fleeing with the evidence sought, and any information the officers acquire from those who are conducting the search, including information that incriminating evidence has been discovered, will bear, of course, on the lawfulness of a later stop or detention. For example, had the search team radioed Detectives Sneider and Gorbecki about the gun and drugs discovered in the Lake Drive apartment as the officers stopped Bailey and Middleton, this may have provided them with probable cause for an arrest.</p>
<p id="b420-5">Ill</p>
<p id="b420-6">Detentions incident to the execution of a search warrant are reasonable under the Fourth Amendment because the limited intrusion on personal liberty is outweighed by the special law enforcement interests at stake. Once an individual has left the immediate vicinity of a premises to be searched, however, detentions must be justified by some other rationale. In this respect it must be noted that the District Court, as an alternative ruling, held that stopping petitioner was lawful under <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>. </em>This opinion expresses no view on that issue. It will be open, on remand, for the Court of Appeals to address the matter and to determine whether, assuming the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop was valid, it yielded information that justified the detention the officers then imposed.</p>
<p id="b420-7">The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b420-8">
<em>It is so ordered.</em>
</p>
</opinion>
```

---
